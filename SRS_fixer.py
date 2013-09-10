import glob, arcpy
from arcpy import env
import easygui as eg

print "working"

path = eg.diropenbox("Path to master directory.  Program will search subfolders.  GDB must be in folder named 'service_gdb'")

print "Path: " + str(path)

#Search home directory and sub directories for gdb files
if path.endswith(".gdb"):
    gdbList = [path]
else:
    print "Searching for GDB files in " + str(path)
    gdbaList = glob.glob(path+'\\*\\service_gdb\\*.gdb')
    gdbbList = glob.glob(path+'\\*\\*\\service_gdb\\*.gdb')
    gdbcList = glob.glob(path+'\\*\\*\\*\\service_gdb\\*.gdb')
    gdbdList = glob.glob(path+'\\*\\*\\*\\*\\service_gdb\\*.gdb')
    gdbeList = glob.glob(path+'\\service_gdb\\*.gdb')
    if path.endswith("service_gdb"):
        gdbfList = glob.glob(path+'\\*.gdb')
    else: gdbfList = []

    #Add the contents of each sub directory to the same list
    gdbList = gdbaList+gdbbList+gdbcList+gdbdList+gdbeList+gdbfList

print gdbList

for gdb in gdbList:
    env.workspace = gdb
    tables = arcpy.ListFeatureClasses()
    for table in tables:
        print table
        inFeatures = str(table)
        fieldName = "SRS"
        expression = "'EPSG:4326'"
        arcpy.CalculateField_management(inFeatures, fieldName, expression, "PYTHON")

print "Task Complete"
