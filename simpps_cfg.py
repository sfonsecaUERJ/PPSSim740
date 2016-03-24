import FWCore.ParameterSet.Config as cms
import math
import sys
import random
phys_processes =  ["GG","QQ","gg","DiPhoton","WW","PG","QCD","DPE"]
NEvents = 0 #number of events to simulate
det1 = 203.8   #position of first tracker detector
det2 = 215.
tof  = 215.5   #position of time of flight detector
trklen = 10 # default tracker length
phys_process = ""
Qtype = 0
OutputFile = ""
InputFile = ""
min_mass = 100
max_mass = 1000
higgs_decay = 0
higgs_mass  = 125.7
top_mass = 173.34
phi_min = -math.pi
phi_max =  math.pi
t_min   = 0.
t_max   = 2.
xi_min  = 0.
xi_max  = 0.2
pileup  = True
hit_smear= True
Ang_smear= True
E_smear = True
vtx_smear= True
run_with_CR = True
beta_star = 0.60
det1xoffset = 0.
det2xoffset = 0.

ecms = 13000.
#ecms = 8000.

for arg in sys.argv[2:]:
    if arg=="no-pileup":
         pileup = False 
         continue
    if arg=="no-smearing":
         vtx_smear = False
         Ang_smear = False
         E_smear   = False
         hit_smear = False
    if arg=="no-vertexsmear":
         vtx_smear = False
         continue
    if arg=="no-anglesmear":
         Ang_smear = False
         continue
    if arg=="no-energysmear":
         E_smear = False
         continue
    if arg=="no-beamsmear":
         Ang_smear = False
         E_smear   = False
         continue
    if arg=="no-crossingangle":
         run_with_CR = False
         continue
    opt = arg[0:arg.find("=")]
    if opt=="process":
         phys_process = arg[arg.find("=")+1:]
         if phys_process not in phys_processes:
            print "Invalid physics process"
            sys.exit(2)
    elif opt.lower()=="nevents":
         NEvents = int(arg[arg.find("=")+1:])
    elif opt=="output":
         OutputFile = arg[arg.find("=")+1:]
    elif opt=="input":
         InputFile = arg[arg.find("=")+1:]
    elif opt=="det1":
         det1=float(arg[arg.find("=")+1:])
    elif opt=="det2":
         det2=float(arg[arg.find("=")+1:])
    elif opt=="tof":
         tof=float(arg[arg.find("=")+1:])
    elif opt=="min_mass":
         min_mass=float(arg[arg.find("=")+1:])
    elif opt=="max_mass":
         max_mass=float(arg[arg.find("=")+1:])
    elif opt=="hdecay":
         hdecay=arg[arg.find("=")+1:]
         if hdecay=="b":
            higgs_decay = 5
         elif hdecay=="c":
            higgs_decay = 4
         elif hdecay=="W":
            higgs_decay = 24
         elif hdecay=="G":
            higgs_decay = 21
         elif hdecay=="tau":
            higgs_decay = 15
         elif hdecay=="Z":
            higgs_decay = 23
         elif hdecay=="g":
            higgs_decay = 22
         else:
            print "Unknown decay mode"
            sys.exit(2)
    elif opt=="higgs_mass":
         higgs_mass = float(arg[arg.find("=")+1:])  
    elif opt=="min_t":
         t_min = float(arg[arg.find("=")+1:])
    elif opt=="max_t":
         t_max = float(arg[arg.find("=")+1:])
    elif opt=="min_xi":
         xi_min = float(arg[arg.find("=")+1:])
    elif opt=="max_xi":
         xi_max = float(arg[arg.find("=")+1:])
    elif opt=="ecms":
         ecms = float(arg[arg.find("=")+1:])
    elif opt=="Q":
         if (arg[arg.find("=")+1:]=="top"):
            Qtype=6
         if (arg[arg.find("=")+1:]=="bottom"):
            Qtype=5
    elif opt=="beta_star":
         beta_star=float(arg[arg.find("=")+1:])
         if beta_star!=0.55 and beta_star!=0.60 and beta_star!=90:
            print "Unknown BetaStar (0.55, 0.60 or 90)"
            sys.exit(2)
    elif opt=="det1Offset":
         det1xoffset = float(arg[arg.find("=")+1:])
    elif opt=="det2Offset":
         det2xoffset = float(arg[arg.find("=")+1:])
    else:
         print opt
         print "Usage: cmsRun ",sys.argv[1],"process=[QQ,GG,DiPhoton]","NEvent=# events","det1=det positon","tof=ToF position"

print det1xoffset,det2xoffset

if phys_process=="QQ":
   if Qtype==0:
      print "Usage: cmsRun ",sys.argv[1],"process=QQ Q=[top,bottom] ..."
      sys.exit(2)

if beta_star==90: run_with_CR=False

if det2>0:
   trklen=det2-det1
else:
   det2=det1+trklen

if run_with_CR:
   useCR     = True
   if beta_star==90:
      beamfile1 = './beamfiles/LHCB1_Beta90_6.5TeV_CR142.5_v6.503.tfs'
      beamfile2 = './beamfiles/LHCB2_Beta90_6.5TeV_CR142.5_v6.503.tfs'
   else:
      beamfile1 = './beamfiles/LHCB1_Beta0.60_6.5TeV_CR142.5_v6.503.tfs'
      beamfile2 = './beamfiles/LHCB2_Beta0.60_6.5TeV_CR142.5_v6.503.tfs'
else: # there is not need to change the beamline file when running without the CR, it is enough to turn off the kickers (KickersOFF=True)
   useCR = False
   if beta_star==90:
      beamfile1 = './beamfiles/LHCB1_Beta90_6.5TeV_CR0.0_v6.503.tfs'
      beamfile2 = './beamfiles/LHCB2_Beta90_6.5TeV_CR0.0_v6.503.tfs'
   else:
      #beamfile1 = '/afs/cern.ch/work/m/mundim/public/PPS/CMSSW_7_0_0_pre2/src/SimTransport/HectorProducer/data/LHCB1_Beta0.60_6.5TeV_CR142.5_v6.503.tfs'
      #beamfile2 = '/afs/cern.ch/work/m/mundim/public/PPS/CMSSW_7_0_0_pre2/src/SimTransport/HectorProducer/data/LHCB2_Beta0.60_6.5TeV_CR142.5_v6.503.tfs'
      beamfile1 = './beamfiles/LHCB1_Beta0.60_6.5TeV_CR0.0_v6.503.tfs'
      beamfile2 = './beamfiles/LHCB2_Beta0.60_6.5TeV_CR0.0_v6.503.tfs'

if phys_process=="Higgs":
   min_mass = 120.
   max_mass = 130.

print "Number of events : ",NEvents
print "Physics process  : ",phys_process
print "sqrt(s)          : ",ecms
print "1st Det. position: ",det1
print "2nd Det. position: ",det2
print "Tracker length   : ",trklen
print "ToF det. position: ",tof
print "Minimum mass     : ",min_mass
print "Maximum mass     : ",max_mass
print "Minimum t        : ",t_min
print "Maximum t        : ",t_max
print "Minimum xi       : ",xi_min
print "Maximum xi       : ",xi_max
print "Minimum phi      : ",phi_min
print "Maximum phi      : ",phi_max
print "Higgs mass       : ",higgs_mass
print "Higgs decay      : ",higgs_decay
print "Output File      : ",OutputFile
print "PileUp           : ",pileup
print "Angle smearing   : ",Ang_smear
print "Energy smearing  : ",E_smear
print "Vertex smearing  : ",vtx_smear
print "Use Xangle       : ",useCR
print "Quark type       : ",Qtype
print "BeamLine file 1  : ",beamfile1
print "BeamLine file 2  : ",beamfile2

if (NEvents==0 and phys_process!="WW" and InputFile=="") or phys_process=="" or OutputFile=="" or det1==0 or tof==0 or (phys_process=="H" and higgs_decay==0):
   print
   print "Usage: cmsRun ",sys.argv[1],"process=[QQ,GG,DiPhoton]","NEvent=# events","det1=det positon","tof=ToF position","output=file.root"
   print "Usage: cmsRun ",sys.argv[1],"process=[WW]","input=file.lhe","det1=det positon","tof=ToF position","output=file.root"
   print
   print
   sys.exit(2)

process = cms.Process("PPS")

# import of standard configurations
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Geometry.PPSCommonData.cmsPPSGeometryXML_cfi")
#process.load("Geometry.FP420CommonData.cmsFP420GeometryXML_cfi")
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

process.LHCTransport.Hector.Beam1 = cms.string(beamfile1)
process.LHCTransport.Hector.Beam2 = cms.string(beamfile2)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('cout')
)

process.load('Configuration.EventContent.EventContent_cff')

process.common_maximum_timex = cms.PSet( # need to be localy redefined
   MaxTrackTime  = cms.double(2000.0),  # need to be localy redefined
   MaxTimeNames  = cms.vstring('ZDCRegion'), # need to be localy redefined
   MaxTrackTimes = cms.vdouble(10000.0),  # need to be localy redefined
   DeadRegions = cms.vstring()
)

#process.Timing = cms.Service("Timing")
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

"""
process.g4SimHits.SteppingAction = cms.PSet(
        process.common_maximum_timex,
        KillBeamPipe            = cms.bool(True),
        CriticalEnergyForVacuum = cms.double(2.0),
        CriticalDensity         = cms.double(1e-15),
        EkinNames               = cms.vstring(),
        EkinThresholds          = cms.vdouble(),
        EkinParticles           = cms.vstring(),
        Verbosity               = cms.untracked.int32(0)
)

process.g4SimHits.StackingAction = cms.PSet(
        process.common_heavy_suppression,
        process.common_maximum_timex,        # need to be localy redefined
        TrackNeutrino = cms.bool(False),
        KillDeltaRay  = cms.bool(False),
        KillHeavy     = cms.bool(False),
        KillGamma     = cms.bool(False),
        SaveFirstLevelSecondary = cms.untracked.bool(True),
        SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True),
        SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True),
        SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)
)
"""
# Pileup
if pileup:
   #process.load('SimGeneral.MixingModule.mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi')
   process.load('SimGeneral.MixingModule.mix_E14TeV_L10E33_BX2808_cfi')
   process.mix.input.fileNames = cms.untracked.vstring(
          #'file:/afs/cern.ch/work/m/mundim/public/PPS/RelValMinBias_CMSSW_5_3_0-START53_V4-v1_GEN-SIM-DIGI-RAW-HLTDEBUG_0266_D6F277EA-5799-E111-81D1-003048FFD7A2.root'
          #'root://xrootd.unl.edu//store/mc/Summer13/MinBias_TuneZ2star_13TeV-pythia6/GEN-SIM/START53_V7C-v1/10000/00169F30-79D0-E211-B8FC-003048F5ADF2.root'
          'file:/afs/cern.ch/work/m/mundim/public/PPS/MinBias_TuneZ2star_13TeV-pythia6_GEN-SIM_START53_V7C-v1_0204517E-E9CF-E211-9617-001EC9AF256E.root',
          'file:/afs/cern.ch/work/m/mundim/public/PPS/MinBias_TuneZ2star_13TeV-pythia6_GEN-SIM_START53_V7C-v1_022E836C-EFCF-E211-ADB7-00074305CF10.root',
          'file:/afs/cern.ch/work/m/mundim/public/PPS/MinBias_TuneZ2star_13TeV-pythia6_GEN-SIM_START53_V7C-v1_02445F51-69CF-E211-A50E-0002C94CD0B8.root'
          #'file:/afs/cern.ch/work/m/mundim/public/PPS/MinBias_TuneA2MB_13TeV_CMSSW_6_2_0-pythia8_GEN-SIM-00DD7446-B51D-E311-B714-001E6739CEB1.root'
   )
   process.mix.input.nbPileupEvents.Lumi = cms.double(20) # pileup 50
   #process.mix.input.nbPileupEvents.Lumi = cms.double(10) # pileup 25
   process.mix.minBunch = cms.int32(0)
   process.mix.maxBunch = cms.int32(0)
else:
   process.load('SimGeneral.MixingModule.mixNoPU_cfi')

process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
#process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('IOMC.EventVertexGenerators.VtxSmearedGauss_cfi')
#process.load('IOMC.EventVertexGenerators.VtxSmearedBetafuncNominalCollision_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.SimulationRandomNumberGeneratorSeeds_cff")
#process.RandomNumberGeneratorService.simSiPixelDigis.initialSeed = random.randint(0,900000000)
#process.RandomNumberGeneratorService.simSiPixelDigis.engineName = cms.untracked.string('TRandom3')
process.RandomNumberGeneratorService.g4SimHits.initialSeed  = cms.untracked.uint32(random.randint(0,900000000))
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(random.randint(0,900000000))
process.RandomNumberGeneratorService.generator.initialSeed  = cms.untracked.uint32(random.randint(0,900000000))
#process.RandomNumberGeneratorService.g4SimHits.initialSeed  = cms.untracked.uint32(12345)
#process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(12345)
#process.RandomNumberGeneratorService.generator.initialSeed  = cms.untracked.uint32(12345)
process.RandomNumberGeneratorService.mix.initialSeed  = cms.untracked.uint32(random.randint(0,900000000))

#
process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')

# Vertex position. Taken from EventVertexGenerators/python/VtxSmearedParameters_cfi, the closest from the MB vertex position used
if vtx_smear:
   VertexX = 0.2440
   VertexY = 0.3929
   VertexZ = 0.4145
else:
   VertexX = 0.
   VertexY = 0.
   VertexZ = 0.

process.VtxSmeared.MeanX    = cms.double(VertexX)
process.VtxSmeared.MeanY    = cms.double(VertexY)
process.VtxSmeared.MeanZ    = cms.double(VertexZ)


# import of standard configurations
from GeneratorInterface.ExhumeInterface.ExhumeParameters_cfi import ExhumeParameters as ExhumeParametersRef
ExhumeParametersRef.HiggsMass = cms.double(higgs_mass)
ExhumeParametersRef.TopMass = cms.double(top_mass)

if phys_process=="PG":
   process.generator = cms.EDProducer("RandomtXiGunProducer",
       PGunParameters = cms.PSet(
           PartID = cms.vint32(2212),
           MinPhi = cms.double(phi_min),
           MaxPhi = cms.double(phi_max),
           ECMS   = cms.double(ecms),
           Mint   = cms.double(t_min),
           Maxt   = cms.double(t_max),
           MinXi  = cms.double(xi_min),
           MaxXi  = cms.double(xi_max)
       ),
       Verbosity = cms.untracked.int32(0),
       psethack = cms.string('single protons'),
       FireBackward = cms.bool(True),
       FireForward  = cms.bool(True),
       firstRun = cms.untracked.uint32(1)
   )
   process.source = cms.Source("EmptySource")
elif phys_process=="QQ" or phys_process=="GG" or phys_process=="DiPhoton":
   process.generator = cms.EDFilter("ExhumeGeneratorFilter",
       PythiaParameters = cms.PSet(
          parameterSets = cms.vstring()
       ),
       ExhumeParameters = ExhumeParametersRef,
       comEnergy = cms.double(ecms),
       pythiaHepMCVerbosity = cms.untracked.bool(False),
       maxEventsToPrint = cms.untracked.int32(2),
       pythiaPylistVerbosity = cms.untracked.int32(0),
       ExhumeProcess = cms.PSet(
           MassRangeLow = cms.double(min_mass),
           MassRangeHigh = cms.double(max_mass),
           ProcessType = cms.string(phys_process),
           ThetaMin = cms.double(0.30),
           HiggsDecay = cms.int32(higgs_decay),
           QuarkType  = cms.int32(Qtype)
       )
   )
   process.source = cms.Source("EmptySource")
elif phys_process=="WW":
   process.source = cms.Source("LHESource",
                    fileNames=cms.untracked.vstring(
                              'file:'+InputFile
                           )
                 )
   from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
   process.generator = cms.EDFilter("LHEProducer",hadronisation = cms.PSet(generator = cms.string('None')))
elif phys_process=="QCD":
   process.source = cms.Source("EmptySource")
   process.generator = cms.EDFilter("Pythia8GeneratorFilter",
                   comEnergy = cms.double(13000.0),
                   crossSection = cms.untracked.double(1.246406e+09),
                   filterEfficiency = cms.untracked.double(1),
                   maxEventsToPrint = cms.untracked.int32(0),
                   pythiaHepMCVerbosity = cms.untracked.bool(False),
                   pythiaPylistVerbosity = cms.untracked.int32(0),
#       useUserHook = cms.bool(True),

                   PythiaParameters = cms.PSet(
                           processParameters = cms.vstring(
                                   'Main:timesAllowErrors    = 10000',
                                   'ParticleDecays:limitTau0 = on',
                                   'ParticleDecays:tauMax = 10',
                                   'HardQCD:all = on',
                                   'PhaseSpace:pTHatMin = 50',
                                   'PhaseSpace:pTHatMax = 3000',
                                   'PhaseSpace:bias2Selection = off',
                                   'PhaseSpace:bias2SelectionPow = 4.5',
                                   'PhaseSpace:bias2SelectionRef = 15.',
                                   'Tune:pp 5',
                                   'Tune:ee 3',
                                   ),
                           parameterSets = cms.vstring('processParameters')
                           )
                   )
elif phys_process=="DPE":
   process.generator = cms.EDFilter("PomwigGeneratorFilter",
      doMPInteraction = cms.bool(False),
      useJimmy = cms.bool(False),
      herwigHepMCVerbosity = cms.untracked.bool(False),
      filterEfficiency = cms.untracked.double(1.0),
      herwigVerbosity = cms.untracked.int32(0),
      comEnergy = cms.double(ecms),
      printCards = cms.untracked.bool(True),
      crossSection = cms.untracked.double(-1.0),
      maxEventsToPrint = cms.untracked.int32(2),
      survivalProbability = cms.double(0.05),
      HerwigParameters = cms.PSet(
        DPEInclusiveJets = cms.vstring('NSTRU      = 14         ! H1 Pomeron Fit B',
            'Q2WWMN     = 1E-6       ! Minimum |t|',
            'Q2WWMX     = 4.0        ! Maximum |t|',
            'YWWMIN     = 0.01       ! Minimum xi',
            'YWWMAX     = 0.2        ! Maximum xi',
            'IPROC      = 11500      ! Process PomPom -> jets',
            'PTMIN      = 80         ! 2->2 PT min',
            'MODPDF(1)  = -1         ! Set MODPDF',
            'MODPDF(2)  = -1      ! Set MODPDF'),
        parameterSets = cms.vstring('DPEInclusiveJets')
      ),
      h1fit = cms.int32(2),
      doPDGConvert = cms.bool(False),
      diffTopology = cms.int32(0)
   )
   process.source = cms.Source("EmptySource")

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('\$Revision: 1.1 $'),
        name = cms.untracked.string('\$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/ThirteenTeV/QCD_Pt_15to3000_Tune4C_Flat_8TeV_pythia8_cff.py,v $'),
        annotation = cms.untracked.string('Summer2013 sample with PYTHIA8: QCD dijet production, pTHat = 15 .. 3000 GeV, weighted, Tune4C')
)
process.options = cms.untracked.PSet( SkipEvent = cms.untracked.vstring('ProductNotFound'))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(NEvents) )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.398 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

ppssim_options = cms.PSet(
                         Verbosity = cms.untracked.int32(0),
                         Beam1File = cms.string(beamfile1),
                         Beam2File = cms.string(beamfile2),
                         Beam1Direction = cms.int32(1),
                         Beam2Direction = cms.int32(1),
                         SmearEnergy    = cms.bool(E_smear),
                         SmearAngle     = cms.bool(Ang_smear),
                         BeamEnergyRMS  = cms.double(1.11e-4),
                         BeamAngleRMS   = cms.double(30.03), # in mrad
                         ShowBeamLine   = cms.untracked.bool(False),
                         SimBeamProfile = cms.untracked.bool(False),
                         VtxMeanX       = cms.untracked.double(VertexX),
                         VtxMeanY       = cms.untracked.double(VertexY),
                         VtxMeanZ       = cms.untracked.double(VertexZ),
                         CollisionPoint = cms.string("IP5"),
                         TrackerPosition = cms.double(det1),
                         TrackerLength   = cms.double(trklen),
                         TrkDet1XOffset  = cms.double(det1xoffset),
                         TrkDet2XOffset  = cms.double(det2xoffset),
                         ToFPosition     = cms.double(tof),
                         TCL4Position    = cms.untracked.double(143.0),
                         TCL5Position    = cms.untracked.double(183.8),
                         TCL6Position    = cms.untracked.double(256.7),
                         SmearHit        = cms.bool(hit_smear),
                         HitSigmaX       = cms.double(10),
                         HitSigmaY       = cms.double(10),
                         HitSigmaZ       = cms.double(0),
                         TimeSigma       = cms.double(0.01), #in ns
                         PhiMin          = cms.double(phi_min),
                         PhiMax          = cms.double(phi_max),
                         CentralMass     = cms.double(125.7),
                         CentralMassErr  = cms.double(0.4),
                         KickersOFF      = cms.bool(True),
                         CrossAngleCorr  = cms.bool(useCR),
                         CrossingAngle   = cms.double(142.5), #in mrad
                         EtaMin          = cms.double(7.0),  # min eta to be tracked by HECTOR
                         MomentumMin     = cms.double(3.000), # min mom. to be tracked by HECTOR
                         TrackImpactParameterCut = cms.double(-1), # max. imp. par. for reco tracks
                         MinThetaXatDet1 = cms.double(-500.), #min. theta x at first tracker in urad
                         MaxThetaXatDet1 = cms.double(500.),   #max. theta x at first tracker in urad
                         MinThetaYatDet1 = cms.double(-500.), #min. theta y at first tracker in urad
                         MaxThetaYatDet1 = cms.double(500.), #max. theta y at first tracker in urad
                         DetectorClosestX= cms.double(-2.),  #min. distance to the beam
                         MaxXfromBeam    = cms.double(-25),  #max. x from beam for a hit
                         MaxYfromBeam    = cms.double(10.),  #max |y| from beam for a hit
                         FilterHitMap    = cms.bool(True)    #apply geometrical (X,Y) in the hits
                     )

if phys_process=="PG":
    process.ppssim = cms.EDAnalyzer('PPSAnalyzer',
                         ppssim_options,
                         OutputFile= cms.string(OutputFile)
                     )
else:
    process.ppssim = cms.EDProducer('PPSProducer',
                         ppssim_options,
                         genSource       = cms.InputTag("genProtonsPU") if pileup else  cms.InputTag("generator")  # for HepMC event -> no pileup events
                     )

# Output definition
if phys_process=="PG":
    process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
            splitLevel = cms.untracked.int32(0),
            eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
            outputCommands = cms.untracked.vstring('drop *',
                            'keep PPSSpectrometer_*_*_*'
            ),
            fileName = cms.untracked.string(OutputFile),
            dataset = cms.untracked.PSet(
                      filterName = cms.untracked.string(''),
                      dataTier = cms.untracked.string('')
            )
    )
elif phys_process=="QCD" or phys_process=="GG" or phys_process=="DiPhoton":
    print "QCD output"
    process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
            outputCommands = cms.untracked.vstring('drop *',
                             'keep PPSSpectrometer_*_*_*',
                             'keep recoTracksToOnerecoTracksAssociation_*_*_*',
                             'keep edmHepMCProduct_*_*_*',
                             'keep GenRunInfoProduct_*_*_*',
                             'keep GenEventInfoProduct_*_*_*',
                             'keep TrackingRecHitsOwned_*_*_*',
                             'keep CaloTowersSorted_*_*_*',
                             'keep CastorRecHitsSorted_*_*_*',
                             'keep edmTriggerResults_*_*_*',
                             'keep recoJetIDedmValueMap_*_*_*',
                             'keep recoBeamSpot_*_*_*',
                             'keep recoBeamHaloSummary_*_*_*',
                             'keep TrajectorysToOnerecoGsfTracksAssociation_*_*_*',
                             'keep PileupSummaryInfos_*_*_*',
                             'keep TrackCandidates_*_*_*',
                             'keep TrajectorySeeds_*_*_*',
                             'keep recoBasicJets_*_*_*',
                             'keep recoCaloJets_*_*_*',
                             'keep *_genParticles_*_*',
                             'keep *_genParticlesForJets_*_*',
                             'keep *_iterativeCone5GenJets_*_*',
                             'keep *_ak5GenJets_*_*',
                             'keep *_ak7GenJets_*_*',
                             'keep recoPFCandidateedmPtredmValueMap_*_*_*',
                             'keep recoPFCandidates_*_*_*',
                             'keep recoPFClusters_*_*_*',
                             'keep recoPFJets_*_*_*',
                             'keep recoTrackJets_*_*_*',
                             'keep recoTracks_*_*_*',
                             'keep recoTrackExtras_*_*_*',
                             'keep recoVertexs_*_*_*',
                             'keep recoVertex_*_*_*',
                             'keep recoVertexCompositeCandidates_*_*_*'
                             ),
            fileName = cms.untracked.string(OutputFile),
            dataset = cms.untracked.PSet(
                      filterName = cms.untracked.string(''),
                      dataTier = cms.untracked.string('')
            )
    )
elif phys_process=="QQ":
    process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
            outputCommands = cms.untracked.vstring('drop *',
                             'keep PPSSpectrometer_*_*_*',
                             'keep HcalNoiseSummary_*_*_*' 
                           , 'keep *_kt6PFJets_*_*'
                           , 'keep *_hfEMClusters_*_*'
                           , 'keep *_hybridSuperClusters_*_*'
                           , 'keep *_multi5x5SuperClusters_*_*'
                           , 'keep *_pfElectronTranslator_*_*'
                           , 'keep *_pfPhotonTranslator_*_*'
                           , 'keep *_genMetTrue_*_*'
                           ),
            fileName = cms.untracked.string(OutputFile),
            dataset = cms.untracked.PSet(
                      filterName = cms.untracked.string(''),
                      dataTier = cms.untracked.string('')
            )
    )
else:
    process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
            outputCommands = cms.untracked.vstring(
                             'keep PileupSummaryInfos_*_*_*',
                             'keep edmHepMCProduct_*_*_*',
                             'keep edmTriggerResults_*_*_*',
                             'keep SimTracks_*_*_*',
                             'keep SimVertexs_*_*_*',
                             'keep recoCaloJets_*_*_*',
                             'keep recoPFCandidates_*_*_*',
                             'keep recoPFJets_*_*_*',
                             'keep recoPFMETs_*_*_*',
                             'keep recoVertexs_*_*_*',
                             'keep recoBeamSpot_*_*_*',
                             'keep recoConversions_*_*_*',
                             'keep recoTracks_*_*_*',
                             'keep recoMuons_*_*_*',
                             'keep recoGsfTracks_*_*_*',
                             'keep recoGsfTrackExtras_*_*_*',
                             'keep recoGsfElectrons_*_*_*',
                             'keep recoGsfElectronCores_*_*_*',
                             'keep recoGenParticles_*_*_*',
                             'keep recoIsoDepositedmValueMap_*_*_*',
                             'keep recoSuperClusters_*_*_*',
                             'keep EcalRecHitsSorted_*_*_*',
                             'keep recoPFRecHits_*_*_*',
                             'keep doubleedmValueMap_*_*_*',
                             'keep PPSSpectrometer_*_*_*'
                             ),
            fileName = cms.untracked.string(OutputFile),
            dataset = cms.untracked.PSet(
                      filterName = cms.untracked.string(''),
                      dataTier = cms.untracked.string('')
            )
    )
# Other statements
if pileup:
   process.genParticlesPU = cms.EDProducer("GenParticleProducer",
                            saveBarCodes = cms.untracked.bool(True),
                            #src = cms.untracked.InputTag("mix","generator"),
                            mix = cms.string("mix"),
                            abortOnUnknownPDGCode = cms.untracked.bool(False),
                            useCrossingFrame = cms.untracked.bool(True)
        )
   process.genProtonsPU = cms.EDFilter("GenParticleSelector",
                          filter = cms.bool(False),
                          src = cms.InputTag("genParticlesPU"),
                          cut = cms.string('')
        )
   process.genProtonsPU.cut = 'status = 1 & pdgId == 2212 & abs(pz) >= %f' % ( 0.5*ecms/2.0)
   outputCommandsPU = [ 'keep *_genParticlesPU_*_*', 'keep *_genProtonsPU_*_*' ]
   process.AODSIMoutput.outputCommands.extend( outputCommandsPU )


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')
#process.GlobalTag.globaltag = 'START50_V16::All'

# Path and EndPath definitions
process.generation_step = cms.Path(process.generator)
process.genparticle_step= cms.Path(process.genParticles)
 
if phys_process=="QCD":
   process.genparticle_step= cms.Path(process.genParticles*process.genParticlesForJets+process.kt4GenJets+process.kt6GenJets+process.iterativeCone5GenJets+process.ak5GenJets+process.ak8GenJets+process.genCandidatesForMET+process.genParticlesForMETAllVisible+process.genMetCalo+process.genMetCaloAndNonPrompt+process.genMetTrue+process.genMetIC5GenJets)

process.lhctransport_step = cms.Path(process.LHCTransport)
process.vtxsmearing_step = cms.Path(process.VtxSmeared)
process.simulation_step = cms.Path(process.psim)
process.g4Simhits_step  = cms.Path(process.g4SimHits)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.ppssim_step = cms.Path(process.ppssim)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

if pileup:
   process.digitisation_step.replace(process.pdigi, process.pdigi * process.genParticlesPU * process.genProtonsPU)

if vtx_smear:
   process.generation_step.replace(process.generator,process.generator * process.VtxSmeared)

# Schedule definition
if phys_process=="PG":
   process.schedule = cms.Schedule(process.generation_step, process.lhctransport_step,process.g4Simhits_step,
                                   process.ppssim_step
   )

else:
   process.schedule = cms.Schedule(
                                   process.generation_step,
                                   process.genparticle_step,
                                   process.lhctransport_step,
                                   process.g4Simhits_step,
                                   process.simulation_step,
                                   process.digitisation_step,
                                   process.L1simulation_step,
                                   process.digi2raw_step,
                                   process.raw2digi_step,
                                   process.reconstruction_step,
                                   process.ppssim_step,
                                   process.endjob_step,
                                   process.AODSIMoutput_step
   )
