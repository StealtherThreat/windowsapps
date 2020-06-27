from json import loads
from subprocess import check_output, call

def get_apps():
	apps = loads(check_output(['powershell.exe','Get-StartApps|convertto-json']))
	names = {}
	for each in apps:
		names.update({each['Name']:each['AppID']})
	return names

def find_app(app_name):
	apps = get_apps()
	for each in sorted(apps,key=len):
		if app_name.upper() in each.upper():
			return each,apps[each]

def open_app(app_name):
	app = find_app(app_name)
	if app == None:
		raise ValueError('Application not found!')
	else:
		call("powershell.exe start 'shell:AppsFolder\%s'"%app[1])

if __name__ == "__main__":
    open_app("Calculator")
