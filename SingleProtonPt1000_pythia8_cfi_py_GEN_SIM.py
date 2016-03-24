# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleMuPt100_pythia8_cfi.py --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions 74X_mcRun2_asymptotic_v2 --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1 --step GEN,SIM --geometry Extended --processName=CTPPS --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('CTPPS')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtendedReco_cff')
#process.load('Configuration.Geometry.GeometryExtended_cff')

process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Geometry.PPSCommonData.cmsPPSGeometryXML_cfi")

process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.Sim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')



########## Testing SimTransport###################################
process.load("SimG4Core.Application.g4SimHits_cfi")
process.load("SimTransport.HectorProducer.HectorTransport_cfi")
process.LHCTransport.Verbosity = cms.bool(True)
#process.LHCTransport.PPSTrackerFirstStation_F=cms.double(det1)
#process.LHCTransport.PPSTrackerFirstStation_B=cms.double(det1)
#process.LHCTransport.PPSToFStation_F=cms.double(tof)
#process.LHCTransport.PPSToFStation_B=cms.double(tof)
#process.LHCTransport.TCL4Position    = cms.untracked.double(143.0)
#process.LHCTransport.TCL5Position    = cms.untracked.double(183.8)
#process.LHCTransport.TCL6Position    = cms.untracked.double(256.7)
process.LHCTransport.Hector.RP420f = cms.double(203.1)
process.LHCTransport.Hector.RP420b = cms.double(203.1)
process.LHCTransport.Hector.BeamLineLengthFP420 = cms.double(250.)

beamfile1 = './beamfiles/LHCB1_Beta90_6.5TeV_CR142.5_v6.503.tfs'
beamfile2 = './beamfiles/LHCB2_Beta90_6.5TeV_CR142.5_v6.503.tfs'

process.LHCTransport.Hector.Beam1 = cms.string(beamfile1)
process.LHCTransport.Hector.Beam2 = cms.string(beamfile2)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)


process.common_maximum_timex = cms.PSet( # need to be localy redefined
   MaxTrackTime  = cms.double(2000.0),  # need to be localy redefined
   MaxTimeNames  = cms.vstring('ZDCRegion'), # need to be localy redefined
   MaxTrackTimes = cms.vdouble(10000.0),  # need to be localy redefined
   DeadRegions = cms.vstring()
)


process.g4SimHits.Physics.DefaultCutValue = 10.
#process.g4SimHits.CaloTrkProcessing.TestBeam = True
process.g4SimHits.UseMagneticField              = False
process.g4SimHits.Generator.ApplyPCuts          = False
process.g4SimHits.Generator.ApplyPhiCuts        = False
process.g4SimHits.Generator.ApplyEtaCuts        = False
process.g4SimHits.Generator.HepMCProductLabel   = 'LHCTransport'
process.g4SimHits.Generator.MinEtaCut        = -12.0
process.g4SimHits.Generator.MaxEtaCut        = 12.0
process.g4SimHits.Generator.Verbosity        = 1
process.g4SimHits.Generator.EtaCutForHector  = 12.0



# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleMuPt100_pythia8_cfi.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SimTransport_GEN_SIM.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(12.0),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(1000.01),
        MinEta = cms.double(8.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(999.99),
        ParticleID = cms.vint32(-2212)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single mu pt 100')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.lhctransport_step = cms.Path(process.LHCTransport)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.lhctransport_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
process = customisePostLS1(process)

# End of customisation functions

