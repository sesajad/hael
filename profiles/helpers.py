from profiles.models import Profile, IpSpec


def whitelist_new_client_ip(client_ip: str):
    pass


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def submit_client(request):
    client_ip = get_client_ip(request)
    current_ips = request.user.ipspec_set

    found = False
    for ipspec in current_ips:
        if ipspec.address == client_ip:
            ipspec.save()  # update expire time
            found = True
            break

    if not found:
        inst = IpSpec(address=client_ip, owner=request.user)
        inst.save()
        whitelist_new_client_ip(client_ip)
