Access to features and their attributes:
(Source: http://resources.arcgis.com/en/help/main/10.2/index.html#/FeatureClassToNumPyArray/018w00000015000000/)

Example 1: Print a feature's OID and coordinates 
```python
import arcpy
features_array = arcpy.da.FeatureClassToNumPyArray(fc, ["OID@", "SHAPE@XY"])

#    Additional information can be accessed using tokens (such as OID@) in place of field names:
#    SHAPE@XY —A tuple of the feature's centroid x,y coordinates.
#    SHAPE@TRUECENTROID —A tuple of the feature's true centroid x,y coordinates.
#    SHAPE@X —A double of the feature's x-coordinate.
#    SHAPE@Y —A double of the feature's y-coordinate.
#    SHAPE@Z —A double of the feature's z-coordinate.
#    SHAPE@M —A double of the feature's m-value.
#    SHAPE@AREA —A double of the feature's area.
#    SHAPE@LENGTH —A double of the feature's length.
#    OID@ —The value of the ObjectID field.

for feature_x in features_array:
  print(feature_x)
  # The first row would look similar to the following:
  #  (1, [-147.82339477539062, 64.86953735351562])
```

Example 2: Print attribute fields 
```python
import arcpy
import numpy

input = "c:/data/usa.gdb/USA/counties"
features_array = arcpy.da.FeatureClassToNumPyArray(input, ('STATE_NAME', 'POP1990', 'POP2000'))

for feature_x in features_array:
  print(feature_x)
```
