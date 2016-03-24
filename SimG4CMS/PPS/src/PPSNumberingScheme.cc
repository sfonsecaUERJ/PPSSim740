///////////////////////////////////////////////////////////////////////////////
// File: PPSNumberingScheme.cc
// Date: 02.2006
// Description: Numbering scheme for PPS
// Modifications: 08.2008  mside and fside added
///////////////////////////////////////////////////////////////////////////////
#include "SimG4CMS/PPS/interface/PPSNumberingScheme.h"
//
#include "CLHEP/Units/GlobalSystemOfUnits.h"
#include "globals.hh"
#include "G4Step.hh"
#include <iostream>

PPSNumberingScheme::PPSNumberingScheme() {
//  sn0=3, pn0=6, rn0=7;   
}

PPSNumberingScheme::~PPSNumberingScheme() {
  //  std::cout << " Deleting PPSNumberingScheme" << std::endl;
}

int PPSNumberingScheme::detectorLevel(const G4Step* aStep) const {
  //Find number of levels
  const G4VTouchable* touch = aStep->GetPreStepPoint()->GetTouchable();
  int level = 0;
  if (touch) level = ((touch->GetHistoryDepth())+1);
  return level;
}
                                                                                
void PPSNumberingScheme::detectorLevel(const G4Step* aStep, int& level,
                                        int* copyno, G4String* name) const {
  //Get name and copy numbers
  if (level > 0) {
    const G4VTouchable* touch = aStep->GetPreStepPoint()->GetTouchable();
    for (int ii = 0; ii < level; ii++) {
      int i      = level - ii - 1;
      name[ii]   = touch->GetVolume(i)->GetName();
      copyno[ii] = touch->GetReplicaNumber(i);
    }
  }
}

unsigned int PPSNumberingScheme::getUnitID(const G4Step* aStep) const {
  
  unsigned intindex=0;
  int level = detectorLevel(aStep);
  
  // std::cout << "PPSNumberingScheme number of levels= " << level << std::endl;
  
  if (level > 0) {
    int*      copyno = new int[level];
    G4String* name   = new G4String[level];
    detectorLevel(aStep, level, copyno, name);
    
    int det = 1; 
    //int stationgen  = 0;
    int zside   = 0;
    int station  = 0;
    int plane = 0;
    for (int ich=0; ich  <  level; ich++) {
      std::cout << name[ich] << std::endl;
    }
    // det = 1 for +PPS ,  = 2 for -PPS  / (det-1) = 0,1
    // det = 3 for +HPS240 , = 4 for -HPS240 / (det-1) = 2,3
    // 0 is as default for every below:
    // zside = 1 for z>0, 2 for z<0
    // Z index 
    // station number 1 - 8   (in reality just 2 ones)
    // superplane(superlayer) number  1 - 16 (in reality just 5 ones)
    // intindex = myPacker.packEcalIndex (det, zside, station, plane);// see examples
    // intindex = myPacker.packCastorIndex (det, zside, station, plane);// see examples
    intindex = packPPSIndex (det, zside, station, plane);
    delete[] copyno;
    delete[] name;
  }
  return intindex;
}

unsigned PPSNumberingScheme::packPPSIndex(int det, int zside, int station,int plane){
        unsigned int idx = ((det-1)&3)<<19;   //bit 19-20 (det-1):0- 3 = 4-->2**2 = 4  -> 4-1  ->((det-1)&3)  2 bit: 0-1
        // unsigned int idx = ((det-1)&1)<<20;//bit 20-20 (det-1):0- 1 = 2-->2**1 = 2  -> 2-1  ->((det-1)&1)  1 bit: 0
        idx += (zside&7)<<7;                 //bits  7- 9   zside:0- 7 = 8-->2**3 = 8  -> 8-1  ->  (zside&7)  3 bits:0-2
        //  idx += (zside&3)<<7;             //bits  7- 8   zside:0- 3 = 4-->2**2 = 4  -> 4-1  ->  (zside&3)  2 bits:0-1
        idx += (station&7)<<4;               //bits  4- 6 station:0- 7 = 8-->2**3 = 8  -> 8-1  ->(station&7)  3 bits:0-2
        idx += (plane&15);                   //bits  0- 3   plane:0-15 =16-->2**4 =16  ->16-1  -> (plane&15)  4 bits:0-3
        return idx;
}

void PPSNumberingScheme::unpackPPSIndex(const unsigned int& idx, int& det, int& zside, int& station, int& plane) {
        det  = (idx>>19)&3;
        det += 1;
        zside   = (idx>>7)&7;
        station = (idx>>4)&7;
        plane   =  idx&15;
}

