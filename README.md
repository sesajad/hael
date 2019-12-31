# Hael
somethings lays in between

## Description
Hael is a firewall controller, which opens blocked ports for a limited time (default=24h) for anybody who logs into it account.
it whitelists the IP, therefore it's not that much safe. you must NOT rely on it.

## Usage

### Requirements

* Python 3.5+
* UFW
* Django

### Installation

assumptions:
* hael main directory is `/root/hael/`
* python binary is in `/root/hael/venv/bin/python` (it means you should make a venv)

create a database, and then a superuser
```
cd /root/heal
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```

now for development:
```
python manage.py runserver 0.0.0.0:80
```

also for production (I know we must not use it for production):
```
systemctl link /root/hael.service
systemctl enable hael
systemctl start hael
```

then you must add garbage collector to system cron jobs, in order to do that, enter `crontab -e` and add following line:
```
0 */6 * * * /root/hael/venv/bin/python /root/heal/manage.py gc
```


**Note: don't forget to `ufw deny YOUR_SERIVCE_PORT` and `ufw allow http`**
