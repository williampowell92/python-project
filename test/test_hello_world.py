from src.hello_world import HelloWorld

hello_world = HelloWorld()


def test_should_say_hello():
    assert hello_world.say_hello() == "Hello, Will!"
