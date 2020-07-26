# Fintual CLI

Unofficial CLI to get investment data from [Fintual](https://www.fintual.cl)

## Installation

### Flexible invocation

The application can be run right from the source directory, in different
ways:

1) Treating the fintual-cli directory as a package *and* as the main script::

```
$ python -m fintual-cli arg1 arg2
Executing fintual-cli version 0.2.0.
List of argument strings: ['arg1', 'arg2']
Stuff and Boo():
<class 'fintualcli.stuff.Stuff'>
<fintualcli.fintualcli.Boo object at 0x7f43d9f65a90>
```
    
2) Using ```setup.py develop``` documented [here](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)

```
# This installs the fintualcli command linking back
# to the current checkout, quite neat for development!
$ python setup.py develop
...
$ fintualcli arg1 arg2
```

3) Using the fintualcli-runner.py wrapper::

```
$ ./fintualcli-runner.py arg1 arg2
Executing fintualcli version 0.2.0.
List of argument strings: ['arg1', 'arg2']
Stuff and Boo():
<class 'fintualcli.stuff.Stuff'>
<fintualcli.fintualcli.Boo object at 0x7f149554ead0>
```
   
### Installation sets up fintualcli command

Situation before installation::

```
$ fintualcli
bash: fintualcli: command not found
```

Installation right from the source tree (or via pip from PyPI)::

```
$ python setup.py install
```

Now, the ``fintualcli`` command is available::

```
$ fintualcli arg1 arg2
Executing fintualcli version 0.2.0.
List of argument strings: ['arg1', 'arg2']
Stuff and Boo():
<class 'fintualcli.stuff.Stuff'>
<fintualcli.fintualcli.Boo object at 0x7f366749a190>
```

On Unix-like systems, the installation places a ```fintualcli``` script into a
centralized ```bin``` directory, which should be in your ```PATH```. On Windows,
```fintualcli.exe``` is placed into a centralized ```Scripts``` directory which
should also be in your ```PATH```.

## Usage

### Auth
### Commands


## Acknowledgments

* [Jan-Philip Gehrcke - Distributing a Python Command Line Application](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/)