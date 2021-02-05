# SHT30 Sensor driver in micropython

## Example


```python
from sht30 import SHT30

s = SHT30()
s.init()
temperature, humidity = s.measure()

print('Temperature:', temperature, 'ºC, RH:', humidity, '%')
```
