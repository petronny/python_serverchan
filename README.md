python_serverchan
====
Tiny python library for [ServerChan](http://sc.ftqq.com/3.version)

### Dependencies
* Python 3

### Install
Just clone this repository

```sh
$ git clone https://github.com/petronny/python_serverchan
```

### Usage
```python
from python_serverchan import ServerChan

serverchan = ServerChan('your_serverchan_key')
serverchan.send('title', 'body')
```
