import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/PPSCommonData/data/ppsworld.xml', 
        'Geometry/PPSCommonData/data/cmspps.xml', 
        'Geometry/PPSCommonData/data/pps.xml', 
        'Geometry/PPSCommonData/data/ppsDummySensors.xml', 
        'Geometry/PPSCommonData/data/materialspps.xml', 
        'Geometry/PPSCommonData/data/PPSRot.xml'
        #'Geometry/PPSSimData/data/ppssens.xml', 
        #'Geometry/PPSSimData/data/PPSProdCuts.xml'
        ),
    rootNodeName = cms.string('ppsworld:OCMS')
)


