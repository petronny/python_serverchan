python_serverchan
====
Tiny python library for [ServerChan](http://sc.ftqq.com/3.version) and [PushBear](https://pushbear.ftqq.com/admin/#/)

### Dependencies
* Python 3

### Install
Just clone this repository

```sh
$ git clone https://github.com/petronny/python_serverchan
```

### Usage

* ServerChan
```python
from python_serverchan import ServerChan

serverchan = ServerChan('your_serverchan_key')
response = serverchan.send('title', 'body')
print(response)
```

* PushBear
```python
from python_serverchan import PushBear

pushbear = PushBear('your_send_key')
response = pushbear.send('title', 'body')
print(response)
```
