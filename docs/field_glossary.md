



# Fields

## SOURCECODE
  
**Description:**  
A value indicating the geologic identity of the polygon. This is the code or classification initially assigned by a map author (source) pulled directly from the SOURCE publication, following whatever convention was used by the author in their original publication. Values generally follow conventional geological labels (1-2 characters indicating age followed by 1-2 characters indicating lithology) or they can be a number or character-number combination like a sample Identifier. Question marks in the symbol indicate uncertainty in the original author’s identification.    
  
**Source of Values:**  
Derived from publication listed in SOURCE    
  
**Value Format:**  
Determined by original publication authors    
  
**Field Values:**  
[List of Values](field_values/SOURCECODE_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 801
- Most frequently occurring value: C-Tr
- Number of values with a single occurrence: 54

## MAPSYMBOL
  
**Description:**  
A value indicating the principal geological identity of the polygon. Values are restricted by the formatting convention defined by the GeoMAP [legend](legend.md), using CAPITAL letters representing AGE (Chronostratigraphic subdivision) and small letters representing lithology (rock-type as a lithostratigraphic classification). MAPSYMBOL is used to unify original SOURCECODE and classify polygons consistently across the entire GeoMAP dataset.  
  
**Source of Values:**  
Value based on the compiler's interpretation of publication listed in SOURCE that conforms to the GeoMap Legend included in download zip  
  
**Value Format:**  
The first one or two UPPERCASE characters represent the geological time period. The last lowercase character is a code corresponding to the type of geologic unit as defined in the [legend](legend.md). NOTE: Geological units which span multiple time periods have symbols showing the oldest and youngest time periods. e.g. Cambrian to Ordovician sedimentary rocks = EOs; Paleoproterozoic to Mesoproterozoic high grade metamorphics = LMn     
  
**Field Values:**  
[List of Values](field_values/MAPSYMBOL_values.md)  
  
**Field Value Restrictions:**  
See [legend](legend.md)  
  
**Descriptive Statistics:**  

- Unique Values: 173
- Most frequently occurring value: JKg
- Number of values with a single occurrence: 3

## PLOTSYMBOL
  
**Description:**  
A value that is generally the same as MAPSYMBOL.  PLOTSYMBOL is used for cartographic purposes to generate colour, or symbols on hard-copy maps. Enables greater user-control. Hs, Qs, Jd are examples where Holocene and Quaternary sediments, or Jurassic dolerites, are differentiated with different PLOTSYMBOL from MAPSYMBOL.   
  
**Source of Values:**  
Value based on the compiler's interpretation of publication listed in SOURCE that conforms to the GeoMap Legend included in download zip  
  
**Value Format:**  
Determined by GeoMAP dataset compilers  
  
**Field Values:**  
[List of Values](field_values/PLOTSYMBOL_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 183
- Most frequently occurring value: JKg
- Number of values with a single occurrence: 3

## NAME
  
**Description:**  
A textual name of the rock unit or simplified type of rock. Where possible the formally defined and published stratigraphic name is adopted, however many units have been named informally or only classified by lithology.  NAME is generally pulled from the SOURCE publication and follows whatever convention is established by the authors.    
  
**Source of Values:**  
Copied from publication listed in SOURCE  
  
**Value Format:**  
Determined by original publication authors    
  
**Field Values:**  
[List of Values](field_values/NAME_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 666
- Most frequently occurring value: marine sedimentary and metasedimentary rocks (Carboniferous to Triassic)
- Number of values with a single occurrence: 36

## DESCR
  
**Description:**  
A description of the geological mapping unit that the polygon is identified as. Geological maps can be based on lithostratigraphy, biostratigraphy, age, and rock types, or combinations of these. A lithostratigraphic approach has generally been adopted for GeoMAP. Mapping units are based on age and/or rock type. DESCR provides a text description of the range and/or most common rock-types encountered, typically taken from an entry on a geological map [legend](legend.md).    
  
**Source of Values:**  
Copied from publication listed in SOURCE  
  
**Value Format:**  
Determined by dataset compilers, summarized from SOURCE author descriptions  
  
**Field Values:**  
[List of Values](field_values/DESCR_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 757
- Most frequently occurring value: unfossiliferous low grade regional metamorphic clastic sedimentary rocks; some basaltic to andesitic lavas
- Number of values with a single occurrence: 41

## POLYGTYPE
  
**Description:**  
A restricted value. One of either rock, moraine, or ice. A simplistic description of dominant material within the polygon.  
  
**Source of Values:**  
Based on an interpretation of SOURCECODE or MAPSYMBOL  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/POLYGTYPE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 3
- Most frequently occurring value: rock
- Number of values with a single occurrence: 0

## MBREQUIV
  
**Description:**  
When the STRATRANK of the polygon is “member”, this is the lithologic member associated with the SOURCECODE. Otherwise value will be “None”  
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/MBREQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 19
- Most frequently occurring value:  
- Number of values with a single occurrence: 5

## FMNEQUIV
  
**Description:**  
When the STRATRANK of the polygon is “formation” or narrower, this is the lithologic formation associated with the SOURCECODE. Otherwise value will be “None”  
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/FMNEQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 246
- Most frequently occurring value: LeMay Formation; Trinity Penninsula Formation
- Number of values with a single occurrence: 15

## SBGRPEQUIV
  
**Description:**  
When the STRATRANK of the polygon is “subgroup” or narrower, this is the lithologic subgroup associated with the SOURCECODE. Otherwise value will be “None”. Currently, the only named subgroup is “Ross Sea Drift” which has a strat rank of “rank not specified”  
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/SBGRPEQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 1
- Most frequently occurring value: Ross Sea Drift
- Number of values with a single occurrence: 0

## GRPEQUIV
  
**Description:**  
When the STRATRANK of the polygon is “group” or narrower, this is the lithologic group associated with the SOURCECODE.  
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/GRPEQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 59
- Most frequently occurring value:  
- Number of values with a single occurrence: 0

## SPGRPEQUIV
  
**Description:**  
When the STRATRANK of the polygon is “supergroup” or narrower, this is the lithologic supergroup associated with the SOURCECODE. Otherwise value will be “None”. Currently most supergroups   
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/SPGRPEQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 14
- Most frequently occurring value:  
- Number of values with a single occurrence: 0

## TERREQUIV
  
**Description:**  
When the STRATRANK of the polygon is “terrane”, this is the lithologic terrane associated with the SOURCECODE. Otherwise value will be “None”  
  
**Source of Values:**  
Interpretation based upon multiple sources  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/TERREQUIV_values.md)  
  
**Field Value Restrictions:**  
Unrestricted  
  
**Descriptive Statistics:**  

- Unique Values: 11
- Most frequently occurring value: Wilson Terrane
- Number of values with a single occurrence: 0

## STRATRANK
  
**Description:**  
The level of lithologic classification associated with the SOURCECODE  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/stratigraphicrank](http://cgi.vocabs.ga.gov.au/vocab/stratigraphicrank)  
  
**Field Values:**  
[List of Values](field_values/STRATRANK_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/stratigraphicrank](http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/stratigraphicrank)  
  
**Descriptive Statistics:**  

- Unique Values: 12
- Most frequently occurring value: rank not specified
- Number of values with a single occurrence: 0

## TYPENAME
  
**Description:**  
The geologic unit type as defined by GeoSciML following the IUGS Commission for Geoscience Information (CGI) Geoscience Terminology Working Group. Unit types are differentiated based on their defining lithological, stratigraphic, or other physical properties.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/geologicunittype](http://cgi.vocabs.ga.gov.au/vocab/geologicunittype)  
  
**Field Values:**  
[List of Values](field_values/TYPENAME_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/geologicunittype](http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/geologicunittype)  
  
**Descriptive Statistics:**  

- Unique Values: 6
- Most frequently occurring value: lithostratigraphic unit
- Number of values with a single occurrence: 0

## TYPE_URI
  
**Description:**  
The link to the geologic unit type.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/geologicunittype](http://cgi.vocabs.ga.gov.au/vocab/geologicunittype)  
  
**Field Values:**  
[List of Values](field_values/TYPE_URI_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/geologicunittype](http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/geologicunittype)  
  
**Descriptive Statistics:**  

- Unique Values: 5
- Most frequently occurring value: http://resource.geosciml.org/classifier/cgi/geologicunittype/lithostratigraphic_unit
- Number of values with a single occurrence: 0

## GEOLHIST
  
**Description:**  
A textual representation of the range of time associated with the genesis of the SOURCECODE’s geology.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Values:**  
[List of Values](field_values/GEOLHIST_values.md)  
  
**Field Value Restrictions:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  
  
**Descriptive Statistics:**  

- Unique Values: 113
- Most frequently occurring value: early Jurassic to early Cretaceous
- Number of values with a single occurrence: 2

## REPAGE_URI
  
**Description:**  
The link to the geologic period or era that is representative of the formation of the SOURCECODE’s geological unit.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Values:**  
[List of Values](field_values/REPAGE_URI_values.md)  
  
**Field Value Restrictions:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  
  
**Descriptive Statistics:**  

- Unique Values: 41
- Most frequently occurring value: http://resource.geosciml.org/classifier/ics/ischart/Paleozoic
- Number of values with a single occurrence: 0

## YNGAGE_URI
  
**Description:**  
The link to the youngest geologic period or era that is associated with the genesis of the SOURCECODE’s geology  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Values:**  
[List of Values](field_values/YNGAGE_URI_values.md)  
  
**Field Value Restrictions:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  
  
**Descriptive Statistics:**  

- Unique Values: 51
- Most frequently occurring value: http://resource.geosciml.org/classifier/ics/ischart/Albian
- Number of values with a single occurrence: 0

## OLDAGE_URI
  
**Description:**  
The link to the oldest geologic period or era that is associated with the genesis of the SOURCECODE’s geology  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/GeochronologicEras)  
  
**Field Values:**  
[List of Values](field_values/OLDAGE_URI_values.md)  
  
**Field Value Restrictions:**  
[https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection](https://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/collection)  
  
**Descriptive Statistics:**  

- Unique Values: 52
- Most frequently occurring value: http://resource.geosciml.org/classifier/ics/ischart/Cambrian
- Number of values with a single occurrence: 0

## ABSMIN_MA
  
**Description:**  
A floating point value associated with the age in million years when the young-age geologic period or era ended.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
Float  
  
**Field Values:**  
[List of Values](field_values/ABSMIN_MA_values.md)  
  
**Field Value Restrictions:**  
Positive Integer  
  
**Descriptive Statistics:**  

- Unique Values: 121
- Most frequently occurring value: 100.5
- Number of values with a single occurrence: 2

## ABSMAX_MA
  
**Description:**  
A floating point value associated with the age in million years when the old-age geologic period or era began.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
Float  
  
**Field Values:**  
[List of Values](field_values/ABSMAX_MA_values.md)  
  
**Field Value Restrictions:**  
Positive Integer  
  
**Descriptive Statistics:**  

- Unique Values: 130
- Most frequently occurring value: 541.0
- Number of values with a single occurrence: 2

## AGECODE
  
**Description:**  
A one to three character symbol for the representative age geologic period or era used in the MAPSYMBOL value. These values are defined in the [legend](legend.md).  
  
**Source of Values:**  
Defined for GeoMAP (following convention used for digital geological map of Australia)  
  
**Value Format:**  
2-3 Characters  
  
**Field Values:**  
[List of Values](field_values/AGECODE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 46
- Most frequently occurring value: JK
- Number of values with a single occurrence: 0

## LITHCODE
  
**Description:**  
A one character symbol for the representative lithology of the MAPSYMBOL rock-type letter. Defined and restricted by the values in the [legend](legend.md).  
  
**Field Values:**  
[List of Values](field_values/LITHCODE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 25
- Most frequently occurring value: s
- Number of values with a single occurrence: 0

## LITHOLOGY
  
**Description:**  
A textual description of the lithology restricted to values appearing on GeoSciML’s Simple Lithology list.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/simplelithology](http://cgi.vocabs.ga.gov.au/vocab/simplelithology)  
  
**Field Values:**  
[List of Values](field_values/LITHOLOGY_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/lithology](http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/lithology)  
  
**Descriptive Statistics:**  

- Unique Values: 410
- Most frequently occurring value: unknown
- Number of values with a single occurrence: 11

## REPLITH_URI
  
**Description:**  
Restricted text that contains a link to the GeoSciML definition of the lithology that best represents this unit.  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/simplelithology](http://cgi.vocabs.ga.gov.au/vocab/simplelithology)  
  
**Field Values:**  
[List of Values](field_values/REPLITH_URI_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/lithology](http://cgi.vocabs.ga.gov.au/object?uri=http://resource.geosciml.org/classifier/cgi/lithology)  
  
**Descriptive Statistics:**  

- Unique Values: 80
- Most frequently occurring value: http://resource.geosciml.org/classifier/cgi/lithology/metamorphic_rock
- Number of values with a single occurrence: 3

## OBSMETHOD
  
**Description:**  
The manner in which the polygon’s attributes were assigned. Values are loosely guided by GeoSciML’s list of Geologic Feature Observation Methods  
  
**Source of Values:**  
GeoSciML  
  
**Value Format:**  
see GeoSciML link  
  
**Metadata Link:**  
[http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod](http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod)  
  
**Field Values:**  
[List of Values](field_values/OBSMETHOD_values.md)  
  
**Field Value Restrictions:**  
[http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod](http://cgi.vocabs.ga.gov.au/vocab/featureobservationmethod)  
  
**Descriptive Statistics:**  

- Unique Values: 5
- Most frequently occurring value: synthesis from multiple sources
- Number of values with a single occurrence: 0

## CONFIDENCE
  
**Description:**  
An explanation of the manner by which the age of the geology was determined. Free text that provides a statement concerning the accuracy of the data provided in associated fields.  
  
**Source of Values:**  
Value from GeoMap contributers based on SOURCE publication  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/CONFIDENCE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 162
- Most frequently occurring value: GEOLHIST uncertain
- Number of values with a single occurrence: 12

## POSACC_M
  
**Description:**  
The estimated positional accuracy of the polygon margins. Units: meters  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Field Values:**  
[List of Values](field_values/POSACC_M_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 1
- Most frequently occurring value: 250.0
- Number of values with a single occurrence: 0

## SOURCE
  
**Description:**  
The primary published or unpublished source referenced to assign attributes to the polygon.  A unique identifier that links to the GeoMAP spatial bibliography of geological maps and the geodatabase polygon feature class (or shapefile) ATA_sources_poly.  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/SOURCE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 158
- Most frequently occurring value: Burton-Johnson & Riley 2015
- Number of values with a single occurrence: 8

## METADATA
  
**Description:**  
The link to the metadata for this dataset  
  
**Source of Values:**  
https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7  
  
**Value Format:**  
Link  
  
**Metadata Link:**  
[https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7](https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7)  
  
**Field Values:**  
[List of Values](field_values/METADATA_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 1
- Most frequently occurring value: https://data.gns.cri.nz/metadata/srv/eng/catalog.search#/metadata/1482B48B-3E70-41AE-9BD0-672722A81EC7
- Number of values with a single occurrence: 0

## RESSCALE
  
**Description:**  
The resolution scale at which the polygon was designed to be used or viewed at.  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Field Values:**  
[List of Values](field_values/RESSCALE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 3
- Most frequently occurring value: 250000
- Number of values with a single occurrence: 0

## CAPTSCALE
  
**Description:**  
The scale at which the polygon was digitized  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Value Format:**  
Date  
  
**Field Values:**  
[List of Values](field_values/CAPTSCALE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 1
- Most frequently occurring value: 50000
- Number of values with a single occurrence: 0

## CAPTDATE
  
**Description:**  
The date the polygon was added to the dataset  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Value Format:**  
Datetime: YYYY-MM-DDThh:mm:ss  
  
**Field Values:**  
[List of Values](field_values/CAPTDATE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 14
- Most frequently occurring value: 2017-07-26T00:00:00
- Number of values with a single occurrence: 0

## MODDATE
  
**Description:**  
The most recent date when the polygon was modified.  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Value Format:**  
Datetime: YYYY-MM-DDThh:mm:ss  
  
**Field Values:**  
[List of Values](field_values/MODDATE_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 15
- Most frequently occurring value: 2018-06-06T00:00:00
- Number of values with a single occurrence: 0

## FEATUREID
  
**Description:**  
The unique identifier of the polygon  
  
**Source of Values:**  
Geomap naming scheme  
  
**Value Format:**  
Geomap naming scheme  
  
**Field Values:**  
[List of Values](field_values/FEATUREID_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 95161
- Most frequently occurring value: ATA_geological_units_055438
- Number of values with a single occurrence: 95161

## SPEC_URI
  
**Description:**  
Not really sure what this is  
  
**Source of Values:**  
http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/nil/OGC/0/missing&_format=html  
  
**Value Format:**  
Link  
  
**Metadata Link:**  
[http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/nil/OGC/0/missing&_format=html](http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/nil/OGC/0/missing&_format=html)  
  
**Field Values:**  
[List of Values](field_values/SPEC_URI_values.md)  
  
**Field Value Restrictions:**  
[http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/nil/OGC/0/missing&_format=html](http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/nil/OGC/0/missing&_format=html)  
  
**Descriptive Statistics:**  

- Unique Values: 1
- Most frequently occurring value: http://www.opengis.net/def/nil/OGC/0/missing
- Number of values with a single occurrence: 0

## DATASET
  
**Description:**  
The dataset from which the polygon came from. Alludes to the region of Antarctica where the polygon is located (Peninsula, North Victoria Land, etc).  
  
**Source of Values:**  
Geomap naming scheme  
  
**Value Format:**  
Geomap naming scheme  
  
**Field Values:**  
[List of Values](field_values/DATASET_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 9
- Most frequently occurring value: ATA_PEN_geological_units
- Number of values with a single occurrence: 0

## REGION
  
**Description:**  
The region in which the polygon is located {East Antarctica, West Antarctica}  
  
**Source of Values:**  
Value from GeoMap contributers  
  
**Value Format:**  
String  
  
**Field Values:**  
[List of Values](field_values/REGION_values.md)  
  
**Descriptive Statistics:**  

- Unique Values: 2
- Most frequently occurring value: East Antarctica
- Number of values with a single occurrence: 0
