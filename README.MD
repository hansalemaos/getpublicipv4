# script to get the public IP (v4) of a PC 

## Tested against Windows 10 / Python 3.10 / Anaconda - should work on MacOS / Linux

## pip install getpublicipv4


```python
from getpublicipv4 import get_ip_of_this_pc, doiploop
print(get_ip_of_this_pc())

# Added 
doiploop(*args, **kwargs):
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
```