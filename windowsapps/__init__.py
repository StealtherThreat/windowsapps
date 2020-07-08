from json import loads
from subprocess import call, check_output
from os import startfile

def run_powershell(cmd):
    open('powershell_cmd.ps1','w').write(cmd)
    call('wscript.exe PsRun.vbs powershell_cmd.ps1')

def get_apps():
	cmd = 'Get-StartApps|convertto-json|Out-File -Filepath temp.json'
	run_powershell(cmd)
	f = open('temp.json','r',encoding='utf-16').read()[:-1]
	x=f.replace('null','""')
	apps=eval(x)
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
		startfile('shell:AppsFolder\%s'%app[1])

if __name__ == "__main__":
	open_app('calculator')
