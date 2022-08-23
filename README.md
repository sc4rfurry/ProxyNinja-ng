[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
##
# ProxyNinja-ng
Python script to get https or socks(4/5) proxies by scraping the web and api.
##
### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

##
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.
```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
    python3 -m pip install venv
    cd ProxyNinja-ng
    python3 -m venv env
    source env/bin/activate
```
After that run the following commands:
```bash
  python3 -m pip install -r requirements.txt
```
    
## Usage/Examples

```bash
python3 main.py -t PROXY_TYPE -o OUTPUT_FILENAME -f OUTPUT_FORMAT
```
- PROXY_TYPE: https/socks4/socks5
- OUTPUT_FILENAME: Enter the filename
- OUTPUT_FORMAT: txt/json
OR
```bash
python3 main.py -h/--help
``` 
#### Example:
```bash
python3 main.py -t socks5 -o proxies -f json
```
## Features

- Fetch proxies from different url's and api's.
- Fast, using request lib. 
- save output in txt or json format.
- User Friendly. :D

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License

[MIT](https://choosealicense.com/licenses/mit/)

## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch
