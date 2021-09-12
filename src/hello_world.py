from dynaconf import settings


class HelloWorld:
    def say_hello(self):
        return "Hello, " + settings.NAME + "!"
