///////////////////////////////////////////////////////////////////////////////
// File: PPSG4Hit.cc
// Date: 02.2006
// Description: Transient Hit class for the PPS
///////////////////////////////////////////////////////////////////////////////
#include "SimG4CMS/PPS/interface/PPSG4Hit.h"
#include <iostream>
       
PPSG4Hit::PPSG4Hit():entry(0), entrylp(0), exitlp(0) {
        theIncidentEnergy = 0.;
        theTimeSlice      = 0.;
        theTrackID        =-1;
        theUnitID         = 0;
        thePabs           = 0.;
        theTof            = 0. ;
        theEnergyLoss     = 0.   ;
        theParticleType   = 0 ;
        theUnitID         = 0;
        theTrackID        =-1;
        theThetaAtEntry   =-10000. ;
        thePhiAtEntry     =-10000. ;
        theParentId       = 0;
        theX              = 0.;
        theY              = 0.;
        theZ              = 0.;
        theVx             = 0.;
        theVy             = 0.;
        theVz             = 0.;
}

PPSG4Hit::~PPSG4Hit(){}

PPSG4Hit::PPSG4Hit(const PPSG4Hit &right) {
        theUnitID         = right.theUnitID;
        theTrackID        = right.theTrackID;
        theTof            = right.theTof ;
        theEnergyLoss     = right.theEnergyLoss   ;
        theParticleType   = right.theParticleType ;
        thePabs           = right.thePabs;
        theIncidentEnergy = right.theIncidentEnergy;
        theTimeSlice      = right.theTimeSlice;
        entry             = right.entry;
        entrylp           = right.entrylp;
        exitlp            = right.exitlp;
        theThetaAtEntry   = right.theThetaAtEntry;
        thePhiAtEntry     = right.thePhiAtEntry;
        theParentId       = right.theParentId;
        theX              = right.theX;
        theY              = right.theY;
        theZ              = right.theZ;
        theVx             = right.theVx;
        theVy             = right.theVy;
        theVz             = right.theVz;
}

const PPSG4Hit& PPSG4Hit::operator=(const PPSG4Hit &right) {
        theUnitID         = right.theUnitID;
        theTrackID        = right.theTrackID;
        theTof            = right.theTof ;
        theEnergyLoss     = right.theEnergyLoss   ;
        theParticleType   = right.theParticleType ;
        thePabs           = right.thePabs;
        theIncidentEnergy = right.theIncidentEnergy;
        theTimeSlice      = right.theTimeSlice;
        entry             = right.entry;
        entrylp           = right.entrylp;
        exitlp            = right.exitlp;
        theThetaAtEntry   = right.theThetaAtEntry;
        thePhiAtEntry     = right.thePhiAtEntry;
        theParentId       = right.theParentId;
        theX              = right.theX;
        theY              = right.theY;
        theZ              = right.theZ;
        theVx             = right.theVx;
        theVy             = right.theVy;
        theVz             = right.theVz;

        return *this;
}

void PPSG4Hit::Print() {
  std::cout << (*this);
}

std::ostream& operator<<(std::ostream& os, const PPSG4Hit& hit) {
  os << " Data of this PPSG4Hit are:" << std::endl
     << " hitEntryLocalP: " << hit.getEntryLocalP() << std::endl
     << " hitExitLocalP: " << hit.getExitLocalP() << std::endl
     << " Time slice ID: " << hit.getTimeSliceID() << std::endl
     << " Time slice : " << hit.getTimeSlice() << std::endl
     << " Tof : " << hit.getTof() << std::endl
     //<< " EnergyDeposit = " << hit.getEnergyDeposit() << std::endl
     //<< " elmenergy = " << hit.getEM() << std::endl
     //<< " hadrenergy = " << hit.getHadr() << std::endl
     << " EnergyLoss = " << hit.getEnergyLoss() << std::endl
     << " ParticleType = " << hit.getParticleType() << std::endl
     << " ParticleType = " << hit.getParticleType() << std::endl
     << " Theta at Entry = " << hit.getThetaAtEntry() << std::endl
     << " Phi at Entry = " << hit.getPhiAtEntry() << std::endl
     << " X at Entry = " << hit.getX() << std::endl
     << " Y at Entry = " << hit.getY() << std::endl
     << " Z at Entry = " << hit.getZ() << std::endl
     << " VtxX = " << hit.getVx() << std::endl
     << " VtxY = " << hit.getVy() << std::endl
     << " VtxZ = " << hit.getVz() << std::endl
     << " parentID = " << hit.getParentId() << std::endl
     << " Pabs = " << hit.getPabs() << std::endl
     << " Energy of primary particle (ID = " << hit.getTrackID()
     << ") = " << hit.getIncidentEnergy() << " (MeV)"<<std::endl
     << " Entry point in PPS unit number " << hit.getUnitID()
     << " is: " << hit.getEntry() << " (mm)" << std::endl;
  os << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
     << std::endl;
  return os;
}
