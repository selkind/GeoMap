



# Faults Field Glossary

## ACCURACY
  
**Description:**  
  
The accuracy of mapped features  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/accuracy.md)  

## NAME
  
**Description:**  
  
The name of the feature.  
  
**Source of Values:**  
  
Value from GeoMAP contributers based on SOURCE publication  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
Unrestricted  

## DESCR
  
**Description:**  
  
A short textual description of the feature. Includes type, activity, and optionally the accuracy  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
<type> <(activity)>, <feature inferred>  
  
**Field Value Restrictions:**  
  
<type> <(activity)>, <feature inferred>  

## EXPOSURE
  
**Description:**  
  
Whether or not the fault is exposed at the surface  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
{unknown, exposed, concealed, uncertain}  

## ACTIVITY
  
**Description:**  
  
Whether or not the fault is active  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
{inactive, probably inactive, possibly active, active}  

## TYPENAME
  
**Description:**  
  
The type of feature. Includes information about the sense of movement and dip angle  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
String  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifierscheme/cgi/2016.01/faulttype](http://resource.geosciml.org/classifierscheme/cgi/2016.01/faulttype)  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/faulttype ](http://resource.geosciml.org/classifier/cgi/faulttype )  

## TYPE_URI
  
**Description:**  
  
The link to the definition of the TYPENAME based upon GeosciML definitions  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
Link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/cgi/faulttype ](http://resource.geosciml.org/classifier/cgi/faulttype )  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/faulttype ](http://resource.geosciml.org/classifier/cgi/faulttype )  

## DOMSENSE
  
**Description:**  
  
The dominant sense of movement  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/fault_sense.md)  

## SUBSENSE
  
**Description:**  
  
The subordinate sense of movement  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/fault_sense.md)  

## TYPE
  
**Description:**  
  
The type of feature.  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/fault_type.md)  

## DEFRMSTYLE
  
**Description:**  
  
The deformation style of the feature  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
String  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifierscheme/cgi/2016.01/deformationstyle ](http://resource.geosciml.org/classifierscheme/cgi/2016.01/deformationstyle )  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/deformationstyle ](http://resource.geosciml.org/classifier/cgi/deformationstyle )  

## DEFRM_URI
  
**Description:**  
  
The link to the definition of the deformation style based upon GeosciML definitions  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
Link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/cgi/deformationstyle](http://resource.geosciml.org/classifier/cgi/deformationstyle)  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/deformationstyle](http://resource.geosciml.org/classifier/cgi/deformationstyle)  

## MVTTYPE
  
**Description:**  
  
The term used to define the type of movement  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
String  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifierscheme/cgi/2016.01/faultmovementtype ](http://resource.geosciml.org/classifierscheme/cgi/2016.01/faultmovementtype )  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/faultmovementtype ](http://resource.geosciml.org/classifier/cgi/faultmovementtype )  

## MVTTYP_URI
  
**Description:**  
  
The link to the definition of the movement type based upon GeosciML definitions  
  
**Source of Values:**  
  
GeosciML  
  
**Value Format:**  
  
Link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/cgi/faultmovementtype ](http://resource.geosciml.org/classifier/cgi/faultmovementtype )  
  
**Field Value Restrictions:**  
  
[http://resource.geosciml.org/classifier/cgi/faultmovementtype ](http://resource.geosciml.org/classifier/cgi/faultmovementtype )  

## DISPLCMNT
  
**Description:**  
  
The total displacement  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
{total slip unknown, total slip less than 0.1 km, total slip in the range 0.1-1 km, total slip in the range 1-10 km, total slip in the range 10-100 km}  

## TOTSLIP_KM
  
**Description:**  
  
The total displacement in kilometers  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
{Unknown, <0.1, 0.1-1, 1-10, 10-100}  

## DOWNQUAD
  
**Description:**  
  
The cardinal direction of the down thrown side of the fault  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/down_thrown.md)  

## DIP_DEG
  
**Description:**  
  
The angle in degrees of the dip slope  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
Integer  
  
**Field Value Restrictions:**  
  
(0-90), 99 indicates DIP_DEG is unknown  

## DIPDIR_DEG
  
**Description:**  
  
The compass heading in degrees of the direction of the dip slope  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
Integer  
  
**Field Value Restrictions:**  
  
(0-360), 999 indicates DIPDIR_DEG is unknown  

## GEOLHIST
  
**Description:**  
  
A textual representation of the range of time associated with the activity of the feature  
  
**Source of Values:**  
  
GeoSciML  
  
**Value Format:**  
  
see GeoSciML link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Value Restrictions:**  
  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  

## REPAGE_URI
  
**Description:**  
  
The link to the geologic period or era that is representative of the activity of the feature  
  
**Source of Values:**  
  
GeoSciML  
  
**Value Format:**  
  
see GeoSciML link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Value Restrictions:**  
  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  

## YNGAGE_URI
  
**Description:**  
  
The link to the youngest geologic period or era that is associated with the activity of the feature.  
  
**Source of Values:**  
  
GeoSciML  
  
**Value Format:**  
  
see GeoSciML link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Value Restrictions:**  
  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  

## OLDAGE_URI
  
**Description:**  
  
The link to the oldest geologic period or era that is associated with the activity of the feature.  
  
**Source of Values:**  
  
GeoSciML  
  
**Value Format:**  
  
see GeoSciML link  
  
**Metadata Link:**  
  
[http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Value Restrictions:**  
  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  

## AGE
  
**Description:**  
  
The age of movement  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
String  
  
**Field Value Restrictions:**  
  
see [legend](legend.md)  

## FLTSYS
  
**Description:**  
  
The name of the fault system associated with the feature  
  
**Source of Values:**  
  
Value from GeoMAP contributers based on SOURCE publication  
  
**Value Format:**  
  
String  

## OBSMETHOD
  
**Description:**  
  
The manner in which the feature’s attributes were assigned. Values are loosely guided by GeoSciML’s list of Geologic Feature Observation Methods  
  
**Source of Values:**  
  
GeoSciML  
  
**Value Format:**  
  
see GeoSciML link  
  
**Metadata Link:**  
  
[http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod](http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod)  

## CONFIDENCE
  
**Description:**  
  
An explanation of the manner by which the age of the feature was determined. Free text that provides a statement concerning the accuracy of the data provided in associated fields.  
  
**Source of Values:**  
  
Value from GeoMAP contributers based on SOURCE publication  
  
**Value Format:**  
  
String  

## POSACC_M
  
**Description:**  
  
The estimated positional accuracy of the feature margins. Units: meters  
  
**Source of Values:**  
  
Value from GeoMAP contributers  

## SOURCE
  
**Description:**  
  
The primary published or unpublished source referenced to assign attributes to the feature.  A unique identifier that links to the GeoMAP spatial bibliography of geological maps and the geodatabase feature feature class (or shapefile) ATA_sources_poly.  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
String  

## METADATA
  
**Description:**  
  
The link to the metadata for this dataset  
  
**Source of Values:**  
  
https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7  
  
**Value Format:**  
  
Link  
  
**Metadata Link:**  
  
[https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7](https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7)  

## RESSCALE
  
**Description:**  
  
The resolution scale at which the feature was designed to be used or viewed at.  
  
**Source of Values:**  
  
Value from GeoMAP contributers  

## CAPTSCALE
  
**Description:**  
  
The scale at which the feature was digitized  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
Date  

## CAPTDATE
  
**Description:**  
  
The date the feature was added to the dataset  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
Datetime: YYYY-MM-DDThh:mm:ss  

## MODDATE
  
**Description:**  
  
The most recent date when the feature was modified.  
  
**Source of Values:**  
  
Value from GeoMAP contributers  
  
**Value Format:**  
  
Datetime: YYYY-MM-DDThh:mm:ss  

## PLOTRANK
  
**Description:**  
  
The smallest scale appropriate for plotting  
  
**Source of Values:**  
  
Value from GeoMAP contributors  
  
**Value Format:**  
  
Integer  
  
**Field Value Restrictions:**  
  
[Restricted List](restricted_values/plotrank.md)  

## FEATUREID
  
**Description:**  
  
Globally unique identifer for the feature and conforming to the GeoSciML usage of identifier. (e.g. ATA_SVL_250k_geological_units_001607)  
  
**Source of Values:**  
  
Geomap naming scheme  
  
**Value Format:**  
  
Geomap naming scheme  
