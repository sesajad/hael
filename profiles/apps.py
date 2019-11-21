from django.apps import AppConfig
import firewall

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        firewall.main()
