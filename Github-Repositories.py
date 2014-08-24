import urllib2 , re

name = raw_input("Enter GitHub Account: ")
project_name = raw_input("Enter the project name: ")

url = "https://github.com/" + name + "?tab=repositories" 

searching = urllib2.urlopen(url) 

reading = searching.read() 
  
string = '<a href="/' + name + '/(.*?)" class="css-truncate css-truncate-target">'

project = re.findall(string, reading)

for i in range(len(project)) :
	if project[i] == project_name :
		print "Project Name: ",project[i]
		
		#Get Description...
		_url = "https://github.com/" + name + "/" + project_name
		_searching = urllib2.urlopen(_url)		
		_reading = _searching.read()
		description = re.findall('<div class="repository-description">\n      <p>(.*?)</p>', _reading)
		if description : 
			print "Description: ",description[0]
		else : 
			print "Description:  Description not found."

		break



downlink = "http://github.com/"+name+"/"+project_name+"/archive/master.zip"

print "Download Link: ",downlink
