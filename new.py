import sys
import os

name = sys.argv[1]
if os.path.isdir("app\\blueprints\\" + name):
    raise OSError

os.mkdir("app\\blueprints\\" + name)
os.mkdir("app\\blueprints\\" + name + "\\static")
os.mkdir("app\\blueprints\\" + name + "\\templates")
os.mkdir("app\\blueprints\\" + name + "\\templates\\" + name)
with open("app\\blueprints\\" + name + "\\" + name + ".py", "w+") as f:
    f.write("from flask import Blueprint\n" + name + "_bp = Blueprint(\"" + name + "_bp\", __name__)\n\n" + \
        "@" + name + "_bp.route(\"/\")\ndef " + name + "_index():\n    return \"" + name + "_index\"")

with open("app\\blueprints\\" + name + "\\__init__.py", "w+") as f:
    f.write("from ." + name + " import " + name + "_bp")

with open("app\\blueprints\\__init__.py", "a") as f:
    f.write("\nfrom ." + name + " import " + name + "_bp")