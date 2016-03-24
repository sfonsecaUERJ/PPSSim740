#ifndef PPS_PPSBaseSD_h
#define PPS_PPSBaseSD_h
//

#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "SimDataFormats/SimHitMaker/interface/TrackingSlaveSD.h"
#include "SimDataFormats/TrackingHit/interface/UpdatablePSimHit.h"
#include "SimG4CMS/PPS/interface/PPSG4Hit.h"
#include "SimG4CMS/PPS/interface/PPSG4Hit.h"
#include "SimG4CMS/PPS/interface/PPSG4HitCollection.h"
#include "SimG4CMS/PPS/interface/PPSG4HitCollection.h"
#include "SimG4CMS/PPS/interface/PPSNumberingScheme.h"
#include "SimG4CMS/PPS/interface/PPSNumberingScheme.h"
#include "SimG4Core/Notification/interface/BeginOfEvent.h"
#include "SimG4Core/Notification/interface/BeginOfJob.h"
#include "SimG4Core/Notification/interface/BeginOfRun.h"
#include "SimG4Core/Notification/interface/BeginOfTrack.h"
#include "SimG4Core/Notification/interface/EndOfEvent.h"
#include "SimG4Core/Notification/interface/G4TrackToParticleID.h"
#include "SimG4Core/Notification/interface/Observer.h"
#include "SimG4Core/Notification/interface/TrackInformation.h"
#include "SimG4Core/Notification/interface/TrackInformation.h"
#include "SimG4Core/Physics/interface/G4ProcessTypeEnumerator.h"
#include "SimG4Core/SensitiveDetector/interface/FrameRotation.h"
#include "SimG4Core/SensitiveDetector/interface/SensitiveTkDetector.h"

#include "G4EventManager.hh"
#include "G4ParticleTable.hh"
#include "G4SDManager.hh"
#include "G4Step.hh"
#include "G4StepPoint.hh"
#include "G4Track.hh"
#include "G4VPhysicalVolume.hh"
#include "G4VProcess.hh"

#include "G4SystemOfUnits.hh"

#include <string>
#include <vector>
#include <iostream>


#include <string>

class TrackingSlaveSD;
//AZ:
//class PPSBaseSD;
class FrameRotation;
class TrackInformation;
class SimTrackManager;
class TrackingSlaveSD;
class UpdatablePSimHit;
class G4ProcessTypeEnumerator;
class G4TrackToParticleID;


//-------------------------------------------------------------------
class PPSBaseSD : public SensitiveTkDetector ,
                  public Observer<const BeginOfRun *>,
                  public Observer<const BeginOfEvent *>,
                  //public Observer<const EndOfEvent *>,
                  public Observer<const BeginOfTrack *> {

public:
  
        PPSBaseSD(std::string, const DDCompactView &, const SensitiveDetectorCatalog &,
                  edm::ParameterSet const &, const SimTrackManager* );

//-------------------------------------------------------------------

        virtual ~PPSBaseSD();

        virtual bool ProcessHits(G4Step *,G4TouchableHistory *);
        virtual void Initialize(G4HCofThisEvent * HCE);
        virtual void clear();

        virtual double getEnergyDeposit(G4Step* step);
        virtual void fillHits(edm::PSimHitContainer&, std::string use);
        virtual uint32_t  setDetUnitId(G4Step*);
        std::vector<std::string> getNames();
  
 private:
 protected:
        virtual void           EndOfEvent(G4HCofThisEvent * eventHC);
        virtual void           DrawAll();
        virtual void           PrintAll();
        virtual void           update(const BeginOfRun *);
        virtual void           update(const BeginOfEvent *);
        //virtual void           update(const EndOfEvent *);
        virtual void           update(const BeginOfTrack *);
        virtual void           clearHits();

        //virtual void  SetNumberingScheme(PPSNumberingScheme* scheme);
  
        G4ThreeVector SetToLocal(const G4ThreeVector& global);
        G4ThreeVector SetToLocalExit(const G4ThreeVector& globalPoint);
        void          GetStepInfo(G4Step* aStep);
        G4bool        HitExists();
        void          CreateNewHit();
        void          UpdateHit();
        void          StoreHit(PPSG4Hit*);
        void          ResetForNewPrimary();
        void          Summarize();

  //AZ:
  
        bool           _Verbosity;
        G4ThreeVector entrancePoint, exitPoint;
        G4ThreeVector theEntryPoint ;
        G4ThreeVector theExitPoint  ;

        //  Local3DPoint  entrancePoint, exitPoint, theEntryPoint, theExitPoint;

        float                incidentEnergy;
  
        const SimTrackManager*  theManager;
        TrackingSlaveSD*        slave;
        PPSNumberingScheme *    numberingScheme;
        PPSG4HitCollection*     theHC;

 
        PPSG4Hit*               currentHit;
        G4Track*                theTrack;
        G4VPhysicalVolume*      currentPV;
        uint32_t                unitID, previousUnitID;

        G4StepPoint*            preStepPoint; 
        G4StepPoint*            postStepPoint; 
        float                   edeposit;

        G4ThreeVector           hitPoint;
        G4ThreeVector           hitPointExit;
        G4ThreeVector           hitPointLocal;
        G4ThreeVector           hitPointLocalExit;
//
        std::string             name;
        G4int                   hcID;
        G4int                   tsID;
        G4double                tSlice;
        G4int                   tSliceID;
        unsigned int            primaryID, primID  ;
//
        float Pabs;
        float Tof;
        float Eloss;	
        short ParticleType; 

        float ThetaAtEntry;
        float PhiAtEntry;

        int   ParentId;
        float Vx,Vy,Vz;
        float X,Y,Z;
        int   eventno;
  
 protected:
  
        G4int emPDG;
        G4int epPDG;
        G4int gammaPDG;
};

#endif // PPSBaseSD_h
