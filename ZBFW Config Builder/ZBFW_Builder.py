import sys
import yaml
import os

from jinja2 import Environment, FileSystemLoader

#This line uses the current directory
file_loader = FileSystemLoader('.')

#Load the enviroment
env = Environment(loader=file_loader, lstrip_blocks=True)
template = env.get_template('ZBFW_Template.j2')

#Build Switch Dictionary
zbfw_dict = yaml.load(open('ZBFW_YAML.yml'))

#Add the varibles
output = template.render(zbfw=zbfw_dict)
data_folder = ""


#Write file
filename= data_folder + zbfw_dict["hostname"] + "_ZBFW.cfg"
with open(filename, 'w') as f:
    f.write(output)

print("Configuration File for " + zbfw_dict["hostname"] + " has been created and stored in: \n" + data_folder)
print("\n")
input("Press 'enter' to continue")
