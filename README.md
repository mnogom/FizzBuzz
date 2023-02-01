## FizzBuzz!
[![Maintainability](https://api.codeclimate.com/v1/badges/034c1658d14832cc1033/maintainability)](https://codeclimate.com/github/mnogom/FizzBuzz/maintainability)
[![python-ci](https://github.com/mnogom/FizzBuzz/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mnogom/FizzBuzz/actions/workflows/python-ci.yml)

---
### Usage:
* From bash
```shell
poetry run fizz_buz --help
```
```shell
usage: fizz_buzz [-h]

Console utility to convert number to FizzBuzz notation

options:
  -h, --help  show this help message and exit
```
* From Python:
```python
from fizz_buzz.core import convert_number
a = convert_number(3)  # "Fizz!"
```

### Example usage:
[![asciicast](https://asciinema.org/a/DbhpvPPNNK46DmdFHt40mucFB.svg)](https://asciinema.org/a/DbhpvPPNNK46DmdFHt40mucFB)
