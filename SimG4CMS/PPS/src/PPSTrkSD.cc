///////////////////////////////////////////////////////////////////////////////
// File: PPSTrkSD.cc
// Date: 02.2006
// Description: Sensitive Detector class for PPS
// Modifications: 
///////////////////////////////////////////////////////////////////////////////
 
#include "SimG4CMS/PPS/interface/PPSTrkSD.h"
//#define debug
//-------------------------------------------------------------------
PPSTrkSD::PPSTrkSD(std::string name, const DDCompactView & cpv,
		 const SensitiveDetectorCatalog & clg,
		 edm::ParameterSet const & p, const SimTrackManager* manager) :
  PPSBaseSD(name,cpv,clg,p,manager) {
//-------------------------------------------------------------------

//Parameters
    if (_Verbosity) edm::LogInfo("PPSSD") << "Entering PPSTrkSD.";

    //
    // attach detectors (LogicalVolumes)
    //
    const std::vector<std::string>& lvNames = clg.logicalNames(name);

    this->Register();

    for (std::vector<std::string>::const_iterator it=lvNames.begin(); it !=lvNames.end(); it++) {
      this->AssignSD(*it);
      if (_Verbosity) edm::LogInfo("PPSSD") << "PPSTrkSD : Assigns SD to LV " << (*it);
    }
    
    if (name == "PPSTrkSI") {
       if (_Verbosity) edm::LogInfo("PPSSD") << "name = PPSTrkSI and  new PPSNumberingSchem";
       numberingScheme = new PPSNumberingScheme();
    } else {
       edm::LogInfo("PPSSD") << "PPSTrkSD: ReadoutName not supported";
    }
}

PPSTrkSD::~PPSTrkSD() { }

void PPSTrkSD::Initialize(G4HCofThisEvent * HCE) { 
#ifdef debug
    LogDebug("PPSTrkm") << "PPSTrkSD : Initialize called for " << name << std::endl;
#endif

  theHC = new PPSG4HitCollection(name, collectionName[0]);
  if (hcID<0) hcID = G4SDManager::GetSDMpointer()->GetCollectionID(collectionName[0]);
  HCE->AddHitsCollection(hcID, theHC);

  //  primID = -2;
  primID = 0;

  ////    slave->Initialize();
}

