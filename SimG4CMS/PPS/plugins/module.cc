//#include "SimG4CMS/PPS/interface/PPSTest.h"
#include "SimG4CMS/PPS/interface/PPSBaseSD.h"
#include "SimG4Core/SensitiveDetector/interface/SensitiveDetectorPluginFactory.h"
#include "SimG4Core/Watcher/interface/SimWatcherFactory.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
//#include "FWCore/Framework/interface/MakerMacros.h"
  

typedef PPSBaseSD PPSSensitiveDetector;
DEFINE_SENSITIVEDETECTOR(PPSSensitiveDetector);
