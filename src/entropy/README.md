# Entropy Toolkit

![entropy](https://user-images.githubusercontent.com/54115104/74149935-04b43100-4c1a-11ea-8bba-d2663b02184a.jpeg)

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a>
  <a href="https://github.com/entynetproject/entropy/releases">
    <img src="https://img.shields.io/github/release/entynetproject/entropy.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/entropy/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/entropy.svg">
  </a>
  <a href="https://github.com/entynetproject/entropy/wiki">
      <img src="https://img.shields.io/badge/wiki%20-entropy-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About Entropy Toolkit

    Entropy Toolkit is a set of tools to exploit 
    Netwave and GoAhead IP Webcams. Entropy is a 
    powerful toolkit for webcams penetration testing.

***

# Getting started

## Entropy installation

> cd entropy

> chmod +x install.sh

> ./install.sh

## Entropy uninstallation

> cd entropy

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Entropy Toolkit execution

> entropy -h

```
usage: entropy [-h] [-b [1|2]] [-o <outputfile>] [--timeout <timeout>]
               [-t <tasks>] [-c <count>] [-q | -v]
               [-a <address> | -i <inputfile> | --shodan <API> | --zoomeye <API>]
               [-u]

optional arguments:
  -h, --help            show this help message and exit
  -b [1|2], --brand [1|2]
                        Choose the brand of IP Webcam. (1)Netwave, (2)GoAhead.
  -o <outputfile>, --output <outputfile>
                        Output into path you input.
  --timeout <timeout>   Timeout in seconds.
  -t <tasks>, --task <tasks>
                        Run tasks number of connects in parallel.
  -c <count>, --count <count>
                        The number of IP you want to get from ZoomEye.
  -q, --quiet           Quiet mode.
  -v, --verbose         Verbose mode.
  -a <address>, --address <address>
                        IP:port address of the webcam.
  -i <inputfile>, --input <inputfile>
                        List of IP:port addresses of webcams.
  --shodan <API>        Your Shodan API key.
  --zoomeye <API>       Your ZoomEye API key.
  -u, --update          Update Entropy Toolkit.
```

***

# Entropy Toolkit examples

## Example of exploiting a single webcam
    
> entropy -b 1 -i 192.168.1.100:80 -v  

## Example of exploiting webcams from a file

> entropy -b 2 -l iplist.txt -v

## Example of exploiting webcams using shodan

> entropy -b 2 -v --shodan PSKINdQe1GyxGgecYz2191H2JoS9qvgD

***

# Entropy Toolkit disclaimer

    Usage of the Entropy Toolkit for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    
***
    
# Entropy Toolkit license

    MIT License

    Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
