# pyTree

This is a Python3.9.0 script that behaves like the tree command.

## Specifications

* Display directories & files of the specified path in order by name.
* By default, hidden files are not displayed, but can be displayed by specifying an argument.

```shell
# Do not show hidden files.

/Users/hoge/foo/pyTree
┃
┣━ LICENSE
┣━ Pipfile
┣━ Pipfile.lock
┣━ README.md
┣━ main.py
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

Currently, this is a simple script, but I plan to make it as a command line tool. See the Todo in main.py.

## Note

Developed for the purpose of learning Python. It's also for my own brain training. I had fun developing it :)
