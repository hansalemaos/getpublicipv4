# script to get the public IP (v4) of a PC 

## Tested against Windows 10 / Python 3.10 / Anaconda - should work on MacOS / Linux

## pip install getpublicipv4


```python
from getpublicipv4 import get_ip_of_this_pc
print(get_ip_of_this_pc())

```