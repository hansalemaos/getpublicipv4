import json
import random
import re
import time
import requests

ipreg = re.compile(
    r"""^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"""
)


def _getip(link, action, *args, **kwargs):
    result = None
    if "timeout" not in kwargs:
        kwargs["timeout"] = 5
    try:
        with requests.get(link, **kwargs) as fa:
            result = fa.content
    except Exception as e:
        pass
    try:
        result = action(result.decode("utf-8", "replace"))
        result = ipreg.findall(result)[0]
    except Exception as e:
        pass
    return result


def get_ip_of_this_pc(*args, **kwargs):
    fu1 = lambda fa: fa.strip()
    fu2 = lambda fa: json.loads(fa)["ip"].strip()
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
    result = None
    for link, action in sites_and_actions:
        try:
            result = _getip(link, action, *args, **kwargs)
            result = ipreg.findall(result)[0]
        except Exception as e:
            pass
        if result:
            return result


def doiploop(*args, **kwargs):
    r"""
    This function takes in variable positional and keyword arguments, and it retrieves
    the WAN IP address of the current PC.
    It also allows for a loop timeout (looptimeout) to be specified.
    The function returns the WAN IP address if it is found, and returns None if a
    timeout occurs or an exception is encountered.
    kwargs are passed to requests.get()

    print(doiploop())
    print(
        doiploop(
            proxies={
                "https": "socks5://111.113.119.110:53681",
                "http": "socks5://111.113.119.110:53681",
            }
        )
    )
    """
    looptimeout = kwargs.pop("looptimeout", 0)
    try:
        mywanip = get_ip_of_this_pc(*args, **kwargs)
        if looptimeout:
            timeoutfinal = time.time() + looptimeout
        while not re.match(r"^\d+\.\d+\.\d+\.\d+$", mywanip):
            if looptimeout:
                if time.time() > timeoutfinal:
                    return None
            mywanip = get_ip_of_this_pc(*args, **kwargs)
    except Exception as fe:
        pass
    return mywanip

