from json import loads
from subprocess import getoutput
from os import startfile

def get_apps():
	cmd = 'powershell "Get-StartApps|convertto-json"'
	apps=loads(getoutput(cmd))
	names = {}
	for each in apps:
		names.update({each['Name']:each['AppID']})
	return names

def find_app(app_name):
	apps = get_apps()
	for each in sorted(apps,key=len):
		if app_name.upper() in each.upper():
			return each,apps[each]
	else:
		return "Application not found!"

def open_app(app_name):
	app = find_app(app_name)
	if app == None:
		raise ValueError('Application not found!')
	else:
		startfile('shell:AppsFolder\%s'%app[1])
