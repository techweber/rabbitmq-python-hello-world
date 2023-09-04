# rabbitmq-python-hello-world

Creating RabbitMQ Send / Receive Hello World code using Python

This piece of code is in Python, so you need python and pika library.

* Create and activate virutual environment

```
$ python3 -m venv env
$ source env/bin/activate
```

* Install pika with pip

```$ python3 -m pip install pika```


* RabbitMQ: Downloading & Installing.

[website](https://www.rabbitmq.com/download.html)

Run with docker 

```$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```

* First Open new terminal window, Then start consumer (receiver) receive.py 

```$ python3 receive.py```

* Open another new terminal window, start producer (sender) send.py

```$ python3 send.py```


