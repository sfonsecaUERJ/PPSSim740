///////////////////////////////////////////////////////////////////////////////
// File: PPSG4Hit.h
// Date: 02.2006 
// 
// Package:     PPS
// Class  :     PPSG4Hit
// 
///////////////////////////////////////////////////////////////////////////////
#ifndef PPSG4Hit_h
#define PPSG4Hit_h

#include "G4VHit.hh"
#include <boost/cstdint.hpp>
#include <iostream>

#include "G4Step.hh"
//#include "G4StepPoint.hh"

class PPSG4Hit : public G4VHit {
  
public:
  
        PPSG4Hit();
        ~PPSG4Hit();
        PPSG4Hit(const PPSG4Hit &right);
        const PPSG4Hit& operator=(const PPSG4Hit &right);
        int operator==(const PPSG4Hit &){return 0;}
  
        void           Draw()                             {};
        void           Print();
  
public:
       G4ThreeVector   getEntry() const                   {return entry;};
       void            setEntry(G4ThreeVector xyz)        {entry=xyz;};

       G4ThreeVector   getEntryLocalP() const             {return entrylp;};
       void            setEntryLocalP(G4ThreeVector xyz1) {entrylp=xyz1;};

       G4ThreeVector   getExitLocalP() const              {return exitlp;};
       void            setExitLocalP(G4ThreeVector xyz1)  {exitlp = xyz1;};

       double          getIncidentEnergy() const          {return theIncidentEnergy;};
       void            setIncidentEnergy (double e)       {theIncidentEnergy=e;};

       unsigned int    getTrackID() const                 {return theTrackID;};
       void            setTrackID (int i)                 {theTrackID = i;};

       unsigned int    getUnitID() const                  {return theUnitID;};
       void            setUnitID (unsigned int i)         {theUnitID=i;};

       double          getTimeSlice() const               {return theTimeSlice;};     
       void            setTimeSlice(double d)             {theTimeSlice = d;};
       int             getTimeSliceID() const             {return (int)theTimeSlice;};     

       //void            addEnergyDeposit(double em, double hd) {elem+=em;hadr+=hd;};
       //void            addEnergyDeposit(const PPSG4Hit& aHit) {elem+=aHit.getEM();hadr+=aHit.getHadr();};
       //double          getEnergyDeposit() const               {return elem+hadr;};

       float           getPabs() const                    {return thePabs;};
       void            setPabs(float e)                   {thePabs=e;};

       float           getTof() const                     {return theTof;};
       void            setTof(float e)                    {theTof=e;};

       float           getEnergyLoss() const              {return theEnergyLoss;};
       void            setEnergyLoss(float e)             {theEnergyLoss=e;};
       void            addEnergyLoss(float e)             {theEnergyLoss+=e;};

       int             getParticleType() const            {return theParticleType;};
       void            setParticleType(short i)           {theParticleType=i;};

       float           getThetaAtEntry() const            {return theThetaAtEntry;};   
       void            setThetaAtEntry(float t)           {theThetaAtEntry=t;};

       float           getPhiAtEntry() const              {return thePhiAtEntry;};
       void            setPhiAtEntry(float f)             {thePhiAtEntry=f;};

       float           getX() const                       {return theX;};
       void            setX(float t)                      {theX=t;};

       float           getY() const                       {return theY;};
       void            setY(float t)                      {theY=t;};

       float           getZ() const                       {return theZ;};
       void            setZ(float t)                      {theZ=t;};

       int             getParentId() const                {return theParentId;};
       void            setParentId(int p)                 {theParentId=p;};

       float           getVx() const                      {return theVx;};
       void            setVx(float p)                     {theVx=p;};

       float           getVy() const                      {return theVy;};
       void            setVy(float p)                     {theVy=p;};

       float           getVz() const                      {return theVz;};
       void            setVz(float p)                     {theVz=p;};

private:

       G4ThreeVector entry;             //Entry point
       G4ThreeVector entrylp;           //Entry  local point
       G4ThreeVector exitlp;            //Exit  local point
       double        theIncidentEnergy; //Energy of the primary particle
       G4int         theTrackID;        //Identification number of the primary
       //particle
       double        theTimeSlice;      //Time Slice Identification

       int           theUnitID;         //PPS Unit Number

       float         theX;
       float         theY;
       float         theZ;
       float         thePabs  ;
       float         theTof ;
       float         theEnergyLoss   ;
       int           theParticleType ;
       float         theThetaAtEntry ;
       float         thePhiAtEntry    ;
       int           theParentId;
       float         theVx;
       float         theVy;
       float         theVz;
};
std::ostream& operator<<(std::ostream&, const PPSG4Hit&);
#endif

