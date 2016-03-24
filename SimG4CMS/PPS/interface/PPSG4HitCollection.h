///////////////////////////////////////////////////////////////////////////////
// File: PPSG4HitCollection.h
// Date: 02.2006
// Description: PPS detector Hit collection
// Modifications:
///////////////////////////////////////////////////////////////////////////////
#ifndef PPSG4HitCollection_h
#define PPSG4HitCollection_h

#include "G4THitsCollection.hh"
#include "SimG4CMS/PPS/interface/PPSG4Hit.h"
#include "G4Step.hh"
#include <boost/cstdint.hpp>

typedef G4THitsCollection<PPSG4Hit> PPSG4HitCollection;

#endif

