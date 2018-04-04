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
serverchan.send('title', 'body')
```

* PushBear
```python
from python_serverchan import PushBear

pushbear = PushBear('your_send_key')
pushbear.send('title', 'body')
```
