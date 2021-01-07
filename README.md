# pyTree

This is a Python 3.9.0 script that behaves like the tree command.

## Specifications

* Display directories & files of the specified path in order by name.
* By default, hidden files are not displayed, but can be displayed by specifying an argument.

```shell
# Do not show hidden files.

$ python tree.py /Users/hoge/foo/pyTree

/Users/hoge/foo/pyTree
┃
┣━ LICENSE
┣━ Pipfile
┣━ Pipfile.lock
┣━ README.md
┣━ tree.py
┣━ pyproject.toml
┗━ test
    ┗━ test_sample
        ┣━ pic1.jpg
        ┣━ sample1
        ┃   ┗━ pic1.png
        ┣━ sample2.txt
        ┗━ sample3
            ┣━ pic2.png
            ┣━ sample4
            ┃   ┗━ text.txt
            ┗━ sample5

```

```shell
# Show hidden files.

$ python tree.py /Users/hoge/foo/pyTree/test --full

/Users/hoge/foo/pyTree/test
┃
┗━ test_sample
    ┣━ .DS_Store
    ┣━ .sample
    ┣━ pic1.jpg
    ┣━ sample1
    ┃   ┗━ pic1.png
    ┣━ sample2.txt
    ┗━ sample3
        ┣━ .DS_Store
        ┣━ pic2.png
        ┣━ sample4
        ┃   ┣━ .DS_Store
        ┃   ┗━ text.txt
        ┗━ sample5
```

Command details are below.

```shell
$ python tree.py -h

usage: tree.py [-h] [--full] Path

positional arguments:
  Path        root directory to be scanned

optional arguments:
  -h, --help  show this help message and exit
  --full      option to show hidden directories & files
```

## Note

Developed for the purpose of learning Python. It's also for my own brain training.  I had fun developing it :)
