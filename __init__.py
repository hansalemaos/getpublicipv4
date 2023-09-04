import re
import random
import requests

ipreg = re.compile(
    r"""^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"""
)


def _getip(link, action):
    result = None
    try:
        with requests.get(link) as fa:
            result = action(fa)
            result = ipreg.findall(result)[0]
    except Exception:
        pass
    return result


def get_ip_of_this_pc():
    fu1 = lambda fa: fa.text.strip()
    fu2 = lambda fa: fa.json()["ip"].strip()
    sites_and_actions = [
        ("https://checkip.amazonaws.com", fu1),
        ("https://api.ipify.org", fu1),
        ("https://ident.me", fu1),
        ("http://myip.dnsomatic.com", fu1),
        ("http://ipinfo.io/json", fu2),
        ("http://ipgrab.io", fu1),
        ("http://icanhazip.com/", fu1),
        ("https://www.trackip.net/ip", fu1),
    ]
    random.shuffle(sites_and_actions)
    for link, action in sites_and_actions:
        result = _getip(link, action)
        if result:
            return result
