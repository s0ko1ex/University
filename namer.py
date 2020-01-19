#!python
import os, sys, json

my_dir = sys.argv[1].split(r"/")
my_dir = r"/".join(my_dir if my_dir[-1] else my_dir[:-1]) + r"/" 

for name in os.listdir(my_dir):
    if name[-6:] == ".ipynb":
        with open(my_dir + name) as file:
            new_name = json.load(file)["cells"][0]["source"][0].replace("#", "")
            new_name = ".".join(new_name[1:].split(".")[:2]) + ".ipynb"
            os.system("mv '%s' '%s'" % (my_dir + name, my_dir + new_name))
