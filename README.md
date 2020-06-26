# windowsapps - Python library for managing installed applications on Windows
[![License](https://img.shields.io/github/license/StealtherThreat/WindowsApps)](https://opensource.org/licenses/MIT)

## Installation
To install `windowsapps` from PyPi run:
```shell
pip install windowsapps
```
## Usage

### Getting all Installed Applicatons
```python
import windowsapps

installed_applications = windowsapps.get_apps() 
#Gives Dictionary of Application names along with their AppID
```

### Getting the Name, AppId for a particular application
```python
import windowsapps

name, appid = windowsapps.find_app('APPLICATION NAME')
#searches for the APPLICATION NAME and returns:-
#name = Name of the application.
#appid = AppId of the application
```

### Open an application
```python
import windowsapps

windowsapps.open_app('APPLICATION NAME')
#Will search for the application APPLICATION NAME and open it.
```

## Caveats
This library will works for all applications installed on the PC including Windows Store Applications.
Works perfectly fine on Windows 10.
Use json & subprocess modules to work.

