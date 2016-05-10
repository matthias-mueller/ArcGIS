import arcpy, os, glob, multiprocessing

suffix = '.xyz'
suffix_len = len(suffix)
cellsize = 2
datatype = "32_BIT_FLOAT"
projection = arcpy.SpatialReference(31469) # "DHDN_3_Degree_Gauss_Zone_5"


# some useful stuff came from here: http://gis.stackexchange.com/questions/62984/importing-xyz-to-arcmap
def processFile(fn):
  if os.path.isfile(fn) & fn.endswith(suffix):
    arcpy.CheckOutExtension("3D")
    print (fn)
    xyz = os.path.abspath(fn)
    print (xyz)
    shape_name = str(xyz[:-suffix_len])+".shp"
    raster_name = str(xyz[:-suffix_len])+".tif"
    
    arcpy.ASCII3DToFeatureClass_3d(xyz,"XYZ",shape_name,"POINT","1",projection,"1","","DECIMAL_POINT")
    print (shape_name)	
    
    arcpy.PointToRaster_conversion(shape_name, "Shape.Z", raster_name, "MEAN", "NONE", cellsize)
    print (raster_name)
	
    arcpy.management.Delete(shape_name)
    return raster_name
	
def main():
  pool = multiprocessing.Pool(processes=4)
  files = os.listdir('.')
  rasters = pool.map(processFile, files)

  # collect all geotiffs
  gtiff_files = []
  gtiff_files += [each for each in os.listdir(".") if each.endswith('.tif')]

  # mosaic to raster
  ws_mosaic = os.path.abspath(".")
  arcpy.MosaicToNewRaster_management(gtiff_files, ws_mosaic, "mosaic.tif", projection, datatype, cellsize, "1", "MEAN","FIRST")

if __name__ == "__main__":
  #freeze_support()
  main()