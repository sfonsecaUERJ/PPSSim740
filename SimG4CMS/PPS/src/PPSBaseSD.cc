///////////////////////////////////////////////////////////////////////////////
// File: PPSBaseSD.cc
// Date: 02.2006
// Description: Sensitive Detector class for PPS
// Modifications: 
///////////////////////////////////////////////////////////////////////////////
#include "SimG4CMS/PPS/interface/PPSBaseSD.h"
 
#ifdef DUMPPROCESSES
#include "G4VProcess.hh"
#endif

//#include "G4UnitsTable.hh"
using std::cout;
using std::endl;
using std::vector;
using std::string;

//#define debug
//-------------------------------------------------------------------
PPSBaseSD::PPSBaseSD(std::string name, const DDCompactView & cpv,
		 const SensitiveDetectorCatalog & clg,
		 edm::ParameterSet const & p, const SimTrackManager* manager) :
        SensitiveTkDetector(name, cpv, clg, p), theManager(manager), numberingScheme(0), theHC(0), 
        currentHit(0), theTrack(0), currentPV(0), unitID(0),  previousUnitID(0), preStepPoint(0), 
        postStepPoint(0), name(name), hcID(-1), eventno(0){
                //-------------------------------------------------------------------

    cout<< "Entering PPSBaseSD function with name: " << name << endl;
    //Add PPS Sentitive Detector Name
    collectionName.insert(name);
    slave  = new TrackingSlaveSD(name);
}

PPSBaseSD::~PPSBaseSD() { 
  if (slave)           delete slave; 
  if (numberingScheme) delete numberingScheme;
}



void PPSBaseSD::Initialize(G4HCofThisEvent * HCE) {
#ifdef debug
    LogDebug("PPSBasem") << "PPSBaseSD : Initialize called for " << name << std::endl;
#endif

    if (!slave) return;
    theHC = new PPSG4HitCollection(name, collectionName[0]);
    if (hcID<0) hcID = G4SDManager::GetSDMpointer()->GetCollectionID(collectionName[0]);
    HCE->AddHitsCollection(hcID, theHC);
    primID = 0;
}

bool PPSBaseSD::ProcessHits(G4Step * aStep, G4TouchableHistory * tH) {

     std::cout << "PPSBaseSD: Entering ProcessHits in volume = ";
     if (aStep == NULL) {
        return true;
     } else {
        std::cout << aStep->GetPreStepPoint()->GetPhysicalVolume()<<std::endl;
        GetStepInfo(aStep);
        if (HitExists()) UpdateHit();
        else CreateNewHit();
     }
     return true;
}

void PPSBaseSD::StoreHit(PPSG4Hit* hit){

  //  if (primID<0) return;
      if (hit == 0 ) {
         edm::LogWarning("PPSBasem") << "PPSBaseSD: hit to be stored is NULL !!";
         return;
      }
      theHC->insert( hit );
}

double PPSBaseSD::getEnergyDeposit(G4Step* aStep) {
  return aStep->GetTotalEnergyDeposit();
}

void PPSBaseSD::GetStepInfo(G4Step* aStep) {
  
     preStepPoint = aStep->GetPreStepPoint(); 
     postStepPoint= aStep->GetPostStepPoint(); 
     theTrack     = aStep->GetTrack();   
     hitPoint     = preStepPoint->GetPosition();	
     currentPV    = preStepPoint->GetPhysicalVolume();
     hitPointExit = postStepPoint->GetPosition();	
     hitPointLocal = preStepPoint->GetTouchable()->GetHistory()->GetTopTransform().TransformPoint(hitPoint);
     hitPointLocalExit = preStepPoint->GetTouchable()->GetHistory()->GetTopTransform().TransformPoint(hitPointExit);

     //G4int particleCode = theTrack->GetDefinition()->GetPDGEncoding();

     edeposit  = aStep->GetTotalEnergyDeposit();
     tSlice    = (postStepPoint->GetGlobalTime() )/nanosecond;
     tSliceID  = (int) tSlice;
     unitID    = setDetUnitId(aStep);
#ifdef debug
     LogDebug("PPSBasem") << "unitID=" << unitID <<std::endl;
#endif
     primaryID    = theTrack->GetTrackID();
     //  Position     = hitPoint;
     Pabs         = aStep->GetPreStepPoint()->GetMomentum().mag()/GeV;
     //Tof          = 1400. + aStep->GetPostStepPoint()->GetGlobalTime()/nanosecond;
     Tof          = aStep->GetPostStepPoint()->GetGlobalTime()/nanosecond;
     Eloss        = aStep->GetTotalEnergyDeposit()/GeV;
     ParticleType = theTrack->GetDefinition()->GetPDGEncoding();      
     ThetaAtEntry = aStep->GetPreStepPoint()->GetPosition().theta()/deg;
     PhiAtEntry   = aStep->GetPreStepPoint()->GetPosition().phi()/deg;

     ParentId = theTrack->GetParentID();
     Vx = theTrack->GetVertexPosition().x();
     Vy = theTrack->GetVertexPosition().y();
     Vz = theTrack->GetVertexPosition().z();
     X  = hitPoint.x();
     Y  = hitPoint.y();
     Z  = hitPoint.z();
}

uint32_t PPSBaseSD::setDetUnitId(G4Step * aStep) {
  return (numberingScheme == 0 ? 0 : numberingScheme->getUnitID(aStep));
}

void PPSBaseSD::ResetForNewPrimary() {
     entrancePoint  = SetToLocal(hitPoint);
     exitPoint      = SetToLocalExit(hitPointExit);
     incidentEnergy = preStepPoint->GetKineticEnergy();
}

G4bool PPSBaseSD::HitExists() {
  if (primaryID<1) {
    edm::LogWarning("PPSBasem") << "***** PPSBaseSD error: primaryID = "
                                  << primaryID
                                  << " maybe detector name changed";
  }
   // Update if in the same detector, time-slice and for same track   
   //  if (primaryID == primID && tSliceID == tsID && unitID==previousUnitID) {
  //if (tSliceID == tsID && unitID==previousUnitID) {
  if (primaryID==primID && unitID==previousUnitID) { return true; }
  //look in the HitContainer whether a hit with the same primID, unitID,
  //tSliceID already exists:
                                     
  G4bool found = false;

  //    LogDebug("PPSBasem") << "PPSBaseSD: HCollection=  " << theHC->entries()    <<std::endl;
                                           
  for (int j=0; j<theHC->entries()&&!found; j++) {
         PPSG4Hit* aPreviousHit = (*theHC)[j];
         if (aPreviousHit->getTrackID()     == primaryID &&
             //aPreviousHit->getTimeSliceID() == tSliceID  &&
             aPreviousHit->getUnitID()      == unitID       ) {
            currentHit = aPreviousHit;
            found      = true;
          }
  }          
  return false;
}

G4ThreeVector PPSBaseSD::SetToLocal(const G4ThreeVector& global){
     const G4VTouchable* touch= preStepPoint->GetTouchable();
     theEntryPoint = touch->GetHistory()->GetTopTransform().TransformPoint(global);
     return theEntryPoint;  
}
     
G4ThreeVector PPSBaseSD::SetToLocalExit(const G4ThreeVector& globalPoint){
     const G4VTouchable* touch= postStepPoint->GetTouchable();
     theExitPoint = touch->GetHistory()->GetTopTransform().TransformPoint(globalPoint);
     return theExitPoint;  
}
     
void PPSBaseSD::clearHits(){
     slave->Initialize();
}

std::vector<std::string> PPSBaseSD::getNames(){
     std::vector<std::string> temp;
     temp.push_back(slave->name());
     return temp;
}

void PPSBaseSD::Summarize() {
}


void PPSBaseSD::clear() {
}


void PPSBaseSD::DrawAll() {
}

void PPSBaseSD::PrintAll() {
  LogDebug("PPSBasem") << "PPSBaseSD: Collection " << theHC->GetName() << "\n";
  theHC->PrintAllHits();
}

void PPSBaseSD::fillHits(edm::PSimHitContainer& c, std::string n) {
  if (slave->name() == n) {
    c=slave->hits();
    std::cout << "PPSBaseSD: fillHits to PSimHitContainer for name= " <<  name << std::endl;
  }
}

void PPSBaseSD::update (const BeginOfTrack * trk) {
     const G4Track* aTrack = (G4Track*)trk->operator()();
     std::string name = aTrack->GetLogicalVolumeAtVertex()->GetName();
     double z = aTrack->GetVertexPosition().z();
     std::cout << "BeginOfTrack: Volume = " << name<< " Z: " << z << std::endl;
}
void PPSBaseSD::update (const BeginOfEvent * i) {
  LogDebug("ForwardSim") << " Dispatched BeginOfEvent for " << GetName()
                       << " !" ;
   clearHits();
   eventno = (*i)()->GetEventID();
}
void PPSBaseSD::update(const BeginOfRun *run) {

}
/*
void PPSBaseSD::update(const EndOfEvent* evt) {
}
*/
void PPSBaseSD::EndOfEvent(G4HCofThisEvent* HCE) {
  // here we loop over transient hits and make them persistent
  
  //  if(theHC->entries() > 100){
  //    LogDebug("PPSBasem") << "PPSBaseSD: warning!!! Number of hits exceed 100 and =" << theHC->entries() << "\n";
  //  }
  //  for (int j=0; j<theHC->entries() && j<100; j++) {
  int nhitsPPS=0;
  for (int j=0; j<theHC->entries(); j++) {
    PPSG4Hit* aHit = (*theHC)[j];
    if((fabs(aHit->getTof())>1380. && fabs(aHit->getTof())<1450.)) ++nhitsPPS;
    //    if(fabs(aHit->getTof()) < 1700.) {
    if(( fabs(aHit->getTof())>1380. && fabs(aHit->getTof())<1450. && nhitsPPS<200.)) {
      
      Local3DPoint locExitPoint(aHit->getExitLocalP().x(),
				aHit->getExitLocalP().y(),
				aHit->getExitLocalP().z());
      Local3DPoint locEntryPoint(aHit->getEntryLocalP().x(),
				 aHit->getEntryLocalP().y(),
				 aHit->getEntryLocalP().z());
      // implicit conversion (slicing) to PSimHit!!!
      slave->processHits(PSimHit(locEntryPoint,locExitPoint,//entryPoint(), exitPoint()  Local3DPoint
				 aHit->getPabs(),// pabs()  float
				 aHit->getTof(), // tof() float
				 aHit->getEnergyLoss(), // energyLoss() float
				 aHit->getParticleType(),// particleType()   int
				 aHit->getUnitID(), // detUnitId() unsigned int 
				 aHit->getTrackID(),// trackId() unsigned int 
				 aHit->getThetaAtEntry(),//  thetaAtEntry()   float
				 aHit->getPhiAtEntry())); //  phiAtEntry()   float  
      
    }//if Tof<1600. if nhits<100
  } // for loop on hits
  
  Summarize();
}
void PPSBaseSD::CreateNewHit() {

  currentHit = new PPSG4Hit;
  currentHit->setTrackID(primaryID);
  currentHit->setTimeSlice(tSlice);
  currentHit->setUnitID(unitID);
  currentHit->setIncidentEnergy(incidentEnergy);

  currentHit->setPabs(Pabs);
  currentHit->setTof(Tof);
  currentHit->setEnergyLoss(Eloss);
  currentHit->setParticleType(ParticleType);
  currentHit->setThetaAtEntry(ThetaAtEntry);
  currentHit->setPhiAtEntry(PhiAtEntry);

// currentHit->setEntry(entrancePoint);
  currentHit->setEntry(hitPoint);

  currentHit->setEntryLocalP(hitPointLocal);
  currentHit->setExitLocalP(hitPointLocalExit);

  currentHit->setParentId(ParentId);
  currentHit->setVx(Vx);
  currentHit->setVy(Vy);
  currentHit->setVz(Vz);

  currentHit->setX(X);
  currentHit->setY(Y);
  currentHit->setZ(Z);
  //AZ:12.10.2007
  //  UpdateHit();
  // buffer for next steps:
  tsID           = tSliceID;
  primID         = primaryID;
  previousUnitID = unitID;
  
  StoreHit(currentHit);
}	 
 
void PPSBaseSD::UpdateHit() {
  //
  if (Eloss > 0.) {
     //currentHit->addEnergyDeposit(edepositEM,edepositHAD);
     currentHit->addEnergyLoss(Eloss);
  }  

  // buffer for next steps:
  tsID           = tSliceID;
  primID         = primaryID;
  previousUnitID = unitID;
}
