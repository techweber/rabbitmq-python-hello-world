# rabbitmq-python-hello-world

Creating RabbitMQ Send / Receive Hello World code using Python

This piece of code is in Python, so you need python and pika library.

$> python -m pip install pika --upgrade


RabbitMQ: Downloading & Installing.

https://www.rabbitmq.com/download.html

If you're on Linux or Ubuntu, simplest way is to use RabbiMQ docker image.

$> docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Open new terminal window, Then start consumer (receiver) receive.py first
$> python receive.py

Open another new terminal window, start producer (sender) send.py ,
$> python send.py

Thats it! Enjoy.
