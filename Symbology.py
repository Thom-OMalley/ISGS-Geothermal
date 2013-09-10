#Run in ArcGIS Python Window
path = "C:\\datafiles\\aasggeothermal\\Layers\\" #Location of Layer files
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrList = arcpy.mapping.ListLayers(mxd)
for lyr in lyrList:
    try:
        print lyr
        sourceLyr = arcpy.mapping.Layer(path + str(lyr) + ".lyr")
        for df in arcpy.mapping.ListDataFrames(mxd):
            updateLyr = arcpy.mapping.ListLayers(mxd, lyr, df)[0]
            arcpy.mapping.UpdateLayer(df, updateLyr, sourceLyr)
        del sourceLyr
    except: print str(lyr) + "Failed"

mxd.save()
del mxd
