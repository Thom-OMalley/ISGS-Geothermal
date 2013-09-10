import glob, arcpy

print "working"
path = "C:\\datafiles\\BareEarth\\BareEarthTest.gdb"

print "Path: " + str(path)

#Search home directory and sub directories for gdb files
if path.endswith(".gdb"):
    gdbList = [path]
else:
    print "Searching for GDB files in " + str(path)
    gdbaList = glob.glob(path+'\\*\\*\\*.gdb')
    gdbbList = glob.glob(path+'\\*\\*\\*\\*.gdb')
    gdbcList = glob.glob(path+'\\*\\*\\*\\*\\*.gdb')
    gdbdList = glob.glob(path+'\\*\\*\\*\\*\\*\\*.gdb')
    gdbeList = glob.glob(path+'\\*\\*.gdb')
    gdbfList = glob.glob(path+'\\*.gdb')

    #Add the contents of each sub directory to the same list
    gdbList = gdbaList+gdbbList+gdbcList+gdbdList+gdbeList+gdbfList

print gdbList

for gdb in gdbList:
    arcpy.env.workspace = gdb
    tables = arcpy.ListRasters()
    for table in tables:
        inFeatures = str(table)
        output = "C:\\datafiles\\BareEarth\\"+str(table)+".tif"
        print output

        try:
            arcpy.CopyRaster_management(inFeatures,output)
        except:
            print "ERROR:"
            print gdb
            print table
print "Task Complete"
