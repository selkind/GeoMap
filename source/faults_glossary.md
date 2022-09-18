



# Faults Field Glossary

## NAME
  
+ **Reference:** Free text containing name of the fault and conforming to the GeoSciML usage of name.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **GeoSciML Name:** name  
  
**More Information:**  
  
+ **Unique Values:** 66  
+ **Most frequently occurring value:**   
+ **Number of values with a single occurrence:** 35
## DESCR
  
+ **Reference:** Restricted text that describes the fault and conforming to the GeoSciML usage of description.  
  
+ **Type:** Text  
  
+ **Length:** 255.0  
  
+ **Source:** [Restricted List](restricted_values.md)  
  
+ **GeoSciML Name:** description  
  
**More Information:**  
  
+ **Unique Values:** 10  
+ **Most frequently occurring value:** fault (inactive)  
+ **Number of values with a single occurrence:** 3
## TYPENAME
  
+ **Reference:** Restricted text that describes the type of fault and conforming to the GeoSciML usage of faultType. Must match entryname of TYPE_URI.  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **Field Values:** [List of Values](field_values/TYPENAME_values.md)  
  
+ **GeoSciML Name:** faultType  
  
**More Information:**  
  
+ **Unique Values:** 12  
+ **Most frequently occurring value:** fault  
+ **Number of values with a single occurrence:** 1
## TYPE_URI
  
+ **Reference:** Restricted text that contains a link to the GeoSciML definition of the faultType. Must be a valid URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/TYPE_URI_values.md)  
  
+ **Source:** [http://resource.geosciml.org/classifier/cgi/faulttype](http://resource.geosciml.org/classifier/cgi/faulttype)  
  
+ **GeoSciML Name:** faultType_uri  
  
**More Information:**  
  
+ **Unique Values:** 12  
+ **Most frequently occurring value:** http://resource.geosciml.org/classifier/cgi/faulttype/fault  
+ **Number of values with a single occurrence:** 1
## ACCURACY
  
+ **Reference:** Restricted text describing the accuracy with which the feature is located.   
  
+ **Type:** Text  
  
+ **Length:** 20.0  
  
+ **Source:** [Restricted List](restricted_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 3  
+ **Most frequently occurring value:** uncertain  
+ **Number of values with a single occurrence:** 0
## EXPOSURE
  
+ **Reference:** Restricted text that describes the exposure of the fault.   
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **Source:** [Restricted List](restricted_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 3  
+ **Most frequently occurring value:** unknown  
+ **Number of values with a single occurrence:** 0
## ACTIVITY
  
+ **Reference:** Restricted text that describes if the fault is considered active.   
  
+ **Type:** Text  
  
+ **Length:** 20.0  
  
+ **Source:** [Restricted List](restricted_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 4  
+ **Most frequently occurring value:** inactive  
+ **Number of values with a single occurrence:** 0
## DEFRMSTYLE
  
+ **Reference:** Restricted text that describes the style of deformation associated with fault and conforming to the GeoSciML usage of deformationStyle. Must match entryname of DEFRM_URI.  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **GeoSciML Name:** deformationStyle  
  
**More Information:**  
  
+ **Unique Values:** 4  
+ **Most frequently occurring value:** unknown  
+ **Number of values with a single occurrence:** 0
## DEFRM_URI
  
+ **Reference:** Restricted text that contains a link to the GeoSciML definition of the deformationStyle. Must be a valid URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Source:** [http://resource.geosciml.org/classifier/cgi/faultmovementsense](http://resource.geosciml.org/classifier/cgi/faultmovementsense)  
  
+ **GeoSciML Name:** deformationStyle_uri  
  
**More Information:**  
  
+ **Unique Values:** 4  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/unknown  
+ **Number of values with a single occurrence:** 0
## MVTTYPE
  
+ **Reference:** Restricted text that describes the type of movement associated with fault and conforming to the GeoSciML usage of movementType. Must match entryname of MVTTYP_URI.  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **GeoSciML Name:** movementType  
  
**More Information:**  
  
+ **Unique Values:** 5  
+ **Most frequently occurring value:** unknown  
+ **Number of values with a single occurrence:** 0
## MVTTYP_URI
  
+ **Reference:** Restricted text that contains a link to the GeoSciML definition of the movementType. Must be a valid URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Source:** [http://resource.geosciml.org/classifier/cgi/faultmovementtype](http://resource.geosciml.org/classifier/cgi/faultmovementtype)  
  
+ **GeoSciML Name:** movementType_uri  
  
**More Information:**  
  
+ **Unique Values:** 5  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/unknown  
+ **Number of values with a single occurrence:** 0
## DISPLCMNT
  
+ **Reference:** Free text that summarises the displacement across the fault and conforming to the GeoSciML usage of displacement.  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **GeoSciML Name:** displacement  
  
**More Information:**  
  
+ **Unique Values:** 5  
+ **Most frequently occurring value:** total slip unknown  
+ **Number of values with a single occurrence:** 0
## DOWNQUAD
  
+ **Reference:**  Restricted text defining the down thrown side of the fault.  
  
+ **Type:** Text  
  
+ **Length:** 4.0  
  
+ **Source:** [Restricted List](restricted_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 9  
+ **Most frequently occurring value:** unknown  
+ **Number of values with a single occurrence:** 0
## DIP_DEG
  
+ **Reference:** Restricted value that defines the mean dip of the fault plane.  
  
+ **Type:** Short  
  
+ **Source:** Any integer value between 0 and 90.  99 indicates a missing value.  
  
**More Information:**  
  
+ **Unique Values:** 14  
+ **Most frequently occurring value:** 99  
+ **Number of values with a single occurrence:** 3
## DIPDIR_DEG
  
+ **Reference:** Restricted value that defines the mean dip direction of the fault plane  
  
+ **Type:** Short  
  
+ **Source:** Any integer value between 0 and 360.  999 indicates a missing value.  
  
**More Information:**  
  
+ **Unique Values:** 36  
+ **Most frequently occurring value:** 999  
+ **Number of values with a single occurrence:** 8
## GEOLHIST
  
+ **Reference:** Free text that describes the age of faulting events and conforming to the GeoSciML usage of geologicHistory.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/GEOLHIST_values.md)  
  
+ **GeoSciML Name:** geologicHistory  
  
**More Information:**  
  
+ **Unique Values:** 16  
+ **Most frequently occurring value:** Activity unknown  
+ **Number of values with a single occurrence:** 3
## REPAGE_URI
  
+ **Reference:**  Restricted text that contains a link to the GeoSciML definition of the stratigraphic age that best represents the activity on the fault. Must be a URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/REPAGE_URI_values.md)  
  
+ **Source:** [http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
+ **GeoSciML Name:** representativeAge_uri  
  
**More Information:**  
  
+ **Unique Values:** 9  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/unknown  
+ **Number of values with a single occurrence:** 0
## YNGAGE_URI
  
+ **Reference:** Restricted text that contains a link to the GeoSciML definition of the stratigraphic age that best represents the youngest activity on the fault. Must be a URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/YNGAGE_URI_values.md)  
  
+ **Source:** [http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
+ **GeoSciML Name:** representativeOlderAge_uri  
  
**More Information:**  
  
+ **Unique Values:** 10  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/unknown  
+ **Number of values with a single occurrence:** 0
## OLDAGE_URI
  
+ **Reference:** Restricted text that contains a link to the GeoSciML definition of the stratigraphic age that best represents the oldest activity on the fault. Must be a URI from:  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/OLDAGE_URI_values.md)  
  
+ **Source:** [http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
+ **GeoSciML Name:** representativeYoungerAge_uri  
  
**More Information:**  
  
+ **Unique Values:** 11  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/unknown  
+ **Number of values with a single occurrence:** 0
## OBSMETHOD
  
+ **Reference:** Restricted text that describes the method of observation used to capture the fault and conforming to the GeoSciML usage of observationMethod. Must match entryname of URI from:  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **Field Values:** [List of Values](field_values/OBSMETHOD_values.md)  
  
+ **Source:** [http://resource.geosciml.org/classifier/cgi/featureobservationmethod](http://resource.geosciml.org/classifier/cgi/featureobservationmethod)  
  
+ **GeoSciML Name:** observationMethod  
  
**More Information:**  
  
+ **Unique Values:** 4  
+ **Most frequently occurring value:** digital conversion from published source  
+ **Number of values with a single occurrence:** 1
## CONFIDENCE
  
+ **Reference:** Free text that provides a statement concerning the accuracy of the data provided in associated fields. Fields which contain data about which there is uncertainty are listed.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/CONFIDENCE_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 30  
+ **Most frequently occurring value:** TYPENAME from SOURCE map; DEFRMSTYLE, MVTTYPE, DISPLCMNT and GEOLHIST uncertain  
+ **Number of values with a single occurrence:** 4
## POSACC_M
  
+ **Reference:** An estimate of the accuracy (in metres) within which the fault has been located and conforming to the GeoSciML usage of positionalAccuracy.  
  
+ **Type:** Long  
  
+ **Field Values:** [List of Values](field_values/POSACC_M_values.md)  
  
+ **GeoSciML Name:** positionalAccuracy  
  
**More Information:**  
  
+ **Unique Values:** 6  
+ **Most frequently occurring value:** 1000  
+ **Number of values with a single occurrence:** 0
## SOURCE
  
+ **Reference:** Free text that contains information on the source of the fault and conforming to the GeoSciML usage of source.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/SOURCE_values.md)  
  
+ **GeoSciML Name:** source  
  
**More Information:**  
  
+ **Unique Values:** 72  
+ **Most frequently occurring value:** Cox et al. 2012  
+ **Number of values with a single occurrence:** 5
## METADATA
  
+ **Reference:** Free text that contains a link to metadata describing the dataset and conforming to the GeoSciML usage of metadata.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Field Values:** [List of Values](field_values/METADATA_values.md)  
  
+ **GeoSciML Name:** metadata_uri  
  
**More Information:**  
  
+ **Unique Values:** 1  
+ **Most frequently occurring value:** https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/04A23A8E-DF36-4C06-9EF4-4DB4AC9A9E19  
+ **Number of values with a single occurrence:** 0
## RESSCALE
  
+ **Reference:** Resolution at which the fault is intended to be used.  
  
+ **Type:** Long  
  
+ **Length:** 4.0  
  
+ **Field Values:** [List of Values](field_values/RESSCALE_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 8  
+ **Most frequently occurring value:** 250000  
+ **Number of values with a single occurrence:** 0
## CAPTSCALE
  
+ **Reference:** Resolution at which the fault was captured.  
  
+ **Type:** Long  
  
+ **Length:** 4.0  
  
+ **Field Values:** [List of Values](field_values/CAPTSCALE_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 8  
+ **Most frequently occurring value:** 50000  
+ **Number of values with a single occurrence:** 1
## CAPTDATE
  
+ **Reference:** Date when the fault was added to this dataset.  
  
+ **Type:** Date  
  
+ **Length:** 8.0  
  
+ **Field Values:** [List of Values](field_values/CAPTDATE_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 22  
+ **Most frequently occurring value:** 2015-11-24 00:00:00+00:00  
+ **Number of values with a single occurrence:** 2
## MODDATE
  
+ **Reference:** Date when the fault was last modified.  
  
+ **Type:** Date  
  
+ **Length:** 8.0  
  
+ **Field Values:** [List of Values](field_values/MODDATE_values.md)  
  
**More Information:**  
  
+ **Unique Values:** 29  
+ **Most frequently occurring value:** 2019-03-29 00:00:00+00:00  
+ **Number of values with a single occurrence:** 3
## PLOTRANK
  
+ **Reference:** Free integer controling plotting of the fault for a specific use.  
  
+ **Type:** Long  
  
**More Information:**  
  
+ **Unique Values:** 3  
+ **Most frequently occurring value:** 250000  
+ **Number of values with a single occurrence:** 0
## FEATUREID
  
+ **Reference:** Globally unique identifer for the fault and conforming to the GeoSciML usage of identifier. (e.g. ATA_GeoMAP_faults_00066)  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **GeoSciML Name:** identifier  
  
**More Information:**  
  
+ **Unique Values:** 1784  
+ **Most frequently occurring value:** ATA_GeoMAP_faults_00001  
+ **Number of values with a single occurrence:** 1784
## SPEC_URI
  
+ **Reference:** Restricted text that contains a link referring to the GeoSciML ShearDisplacementStructure feature that describes the instance in detail.  
  
+ **Type:** Text  
  
+ **Length:** 150.0  
  
+ **Source:** [http://www.opengis.net/def/nil/OGC/0/missing](http://www.opengis.net/def/nil/OGC/0/missing)  
  
+ **GeoSciML Name:** specification_uri  
  
**More Information:**  
  
+ **Unique Values:** 1  
+ **Most frequently occurring value:** http://www.opengis.net/def/nil/OGC/0/missing  
+ **Number of values with a single occurrence:** 0
## SYMBOL
  
+ **Reference:** Restricted text containing an identifier for a symbol from standard symbolization scheme for use in GeoSciML portrayal.  
  
+ **Type:** Text  
  
+ **Length:** 50.0  
  
+ **GeoSciML Name:** genericSymbolizer  
  
**More Information:**  
  
+ **Unique Values:** 1  
+ **Most frequently occurring value:**   
+ **Number of values with a single occurrence:** 0