import os

from profiles.models import Profile, IpSpec
from ufw import frontend
from ufw.common import UFWRule


def whitelist_new_client_ip(client_ip: str):
    # os.system('ufw insert 1 allow from {}'.format(client_ip))
    rule = UFWRule(action='allow', protocol='any', src=client_ip)
    front = frontend.UFWFrontend(False)
    result = front.set_rule(rule, 'both')
    print(result)


def remove_whitelist_ip(client_ip: str):
    os.system('ufw delete allow from {}'.format(client_ip))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def submit_client(request):
    client_ip = get_client_ip(request)
    current_ips = request.user.ipspec_set.all()
    expire_time = None

    found = False
    for ipspec in current_ips:
        if ipspec.address == client_ip:
            ipspec.save()  # update expire time
            expire_time = ipspec.expire_time
            found = True
            break

    if not found:
        inst = IpSpec(address=client_ip, owner=request.user)
        inst.save()
        expire_time = inst.expire_time
        whitelist_new_client_ip(client_ip)

        if request.user.ipspec_set.count() > request.user.max_ip:
            to_remove = request.user.ipspec_set.order_by('expire_time').first()
            to_remove.delete()

    return client_ip, expire_time
