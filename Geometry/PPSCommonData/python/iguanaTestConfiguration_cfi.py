import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/extend/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/PPSCommonData/data/cmspps.xml', 
        'Geometry/PPSCommonData/data/pps.xml', 
        'Geometry/PPSCommonData/data/ppsrectangle.xml', 
        'Geometry/PPSCommonData/data/materialspps.xml', 
        'Geometry/PPSCommonData/data/PPSRot.xml', 
        'Geometry/PPSSimData/data/ppssens.xml', 
        'Geometry/PPSSimData/data/PPSProdCuts.xml'),
    rootNodeName = cms.string('cms:OCMS')
)
