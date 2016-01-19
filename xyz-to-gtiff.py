# Converts 3D xyz data to geotiff

import arcpy, os

arcpy.CheckOutExtension("3D")

projection = arcpy.SpatialReference(31469) # "DHDN_3_Degree_Gauss_Zone_5"

# some useful stuff came from here: http://gis.stackexchange.com/questions/62984/importing-xyz-to-arcmap
for fn in os.listdir('.'):
    if os.path.isfile(fn) & fn.endswith('.xyz'):
      xyz = os.path.abspath(fn)
      print (xyz)
      shape_name = str(xyz[:-4])+".shp"
      raster_name = str(xyz[:-4])+".tif"
      arcpy.ASCII3DToFeatureClass_3d(xyz,"XYZ",shape_name,"POINT","1",projection,"1","","DECIMAL_POINT")
      print (shape_name)
      arcpy.PointToRaster_conversion(shape_name, "Shape.Z", raster_name, "MEAN", "NONE", "2")
      print (raster_name)
      arcpy.management.Delete(shape_name)
      
