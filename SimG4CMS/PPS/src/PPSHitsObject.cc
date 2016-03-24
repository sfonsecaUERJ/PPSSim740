#include "SimG4CMS/PPS/interface/PPSHitsObject.h"

PPSHitsObject::PPSHitsObject(std::string n, TrackingSlaveSD::Collection& h): _hits(h), _name(n)
{}
