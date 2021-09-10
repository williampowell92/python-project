# Python Project

### Getting Started

To initialise the python environment run:

```
$ make init
```

To run all tests run:

```
$ make test
```

To run pytest with specific arguments, run:

```
$ make pytest ARGS=<your_args>
```

For example, to run tests from a specific folder run `make pytest ARGS=./tests`

### VS Code Settings

The suggested VS Code settings are as follows:

```
{
  "python.linting.pylintEnabled": true,
  "python.linting.enabled": true,
}
```
