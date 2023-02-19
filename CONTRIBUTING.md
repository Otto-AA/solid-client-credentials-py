# Contributor Guide

## Setup

### Requirements

* Make:
    * macOS: `$ xcode-select --install`
    * Linux: [https://www.gnu.org/software/make](https://www.gnu.org/software/make)
    * Windows: [https://mingw.org/download/installer](https://mingw.org/download/installer)
* Python: `$ asdf install`
* Poetry: [https://poetry.eustace.io/docs/#installation](https://poetry.eustace.io/docs/#installation)
* Graphviz:
    * macOS: `$ brew install graphviz`
    * Linux: [https://graphviz.org/download](https://graphviz.org/download/)
    * Windows: [https://graphviz.org/download](https://graphviz.org/download/)

To confirm these system dependencies are configured correctly:

```text
$ make doctor
```

### Installation

Install project dependencies into a virtual environment:

```text
$ make install
```

## Development Tasks

### List commands

To get a list of available commands run:

```bash
$ make
```

### Manual

Run the tests:

```bash
$ make test # all tests
$ make test-unit
$ make test-int
```

Run static analysis and automatically fix some errors:

```bash
$ make check
```

Serve the documentation locally:

```bash
$ make docs
```

### Automatic

Keep all of the above tasks running on change:

```bash
$ make dev
```

> In order to have OS X notifications, `brew install terminal-notifier`.

## Release Tasks

Release to PyPI:

```bash
$ make upload
```
