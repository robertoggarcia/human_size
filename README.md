## Human Size Challenge

Write a function in Python called ‘humanSize’ that takes a non-negative number of bytes and returns a string with the equivalent number of ‘kB’, ‘MB’, ‘GB’, ‘TB’, ‘PB’, ‘EB’, ‘ZB’, or ‘YB’, between [0, 1000), with at most 1 digit of precision after the decimal. If the number of bytes is >= 1000 YB, return this number of YB, for example 5120 YB. For example, your function might return ‘107.3MB’.
Write this function without writing a separate case for each byte prefix, and without using Math.log or Math.pow.

### International System of Units

Multiples using the prefixes of the International System

| Unit | Factor |
| ------ | ------ |
| B | 10⁰ |
| KB | 10³ |
| MB | 10⁶ |
| GB | 10⁹ |
| TB | 10¹2 |
| PB | 10¹5 |
| EB | 10¹8 |
| ZB | 10²1 |
| YB | 10²4 |

### Test

Run tests:
```sh
$ python -m unittest discover
```