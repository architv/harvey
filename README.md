Harvey
=====
![](http://i.imgur.com/raSkNrr.png?1)

Image: [buylocalexperts.com](http://www.buylocalexperts.com/sanantonio/images/stories/buy-local-legal-expert.png)

Harvey is a command line legal expert who manages license for you.

## Demo

![](http://i.imgur.com/gEKlzfv.gif?1)

## Features

- Written in Python
- Supports all Github-supported [`licenses`](https://github.com/architv/harvey#List-all-licenses)
- Works on Mac, Linux (haven't tested on windows)

## Installation


### Option 1: [Pip](https://pypi.python.org/pypi/harvey)

```bash
$ pip install harvey
```

### Option 2: From source

```bash
$ git clone git@github.com:architv/harvey.git
$ cd harvey/
$ python setup.py install
```

## Usage

### Get summary, can, cannot and must rules for a license

```bash
$ harvey gpl-2.0 --tldr 
```

### Get a `LICENSE` for your git repo


```bash
$ harvey mit    # outputs mit license to stdout
```

### Overwrite existing `LICENSE`

```bash
$ harvey mit > LICENSE   # saves a new mit LICENSE file
```


### List all licenses

```bash
$ harvey ls    # or `harvey list`
```

### List of supported licenses

* BSD 3-clause "New" or "Revised" License [bsd-3-clause]
* GNU Lesser General Public License v3.0 [lgpl-3.0]
* GNU General Public License v2.0 [gpl-2.0]
* Mozilla Public License 2.0 [mpl-2.0]
* GNU General Public License v3.0 [gpl-3.0]
* The Unlicense [unlicense]
* Creative Commons Zero v1.0 Universal [cc0-1.0]
* Artistic License 2.0 [artistic-2.0]
* GNU Affero General Public License v3.0 [agpl-3.0]
* ISC License [isc]
* GNU Lesser General Public License v2.1 [lgpl-2.1]
* Eclipse Public License 1.0 [epl-1.0]
* Apache License 2.0 [apache-2.0]
* BSD 2-clause "Simplified" License [bsd-2-clause]
* MIT License [mit]


## Contributing

#### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/architv/harvey/issues) to report any bugs or file feature requests.

#### Developing

PRs are welcome. To begin developing, do this:

```bash
# make virtual env
$ git clone git@github.com:architv/harvey.git
$ pip install requirements.txt
$ cd harvey/
$ python harvey/harvey.py mit
```

Licence
====
Open sourced under [MIT License](LICENSE) (Created by harvey)
