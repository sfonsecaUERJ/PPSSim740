#ifndef PPSHitsObject_H
#define PPSHitsObject_H

#include "SimDataFormats/SimHitMaker/interface/TrackingSlaveSD.h"

class PPSHitsObject{
 public:
  PPSHitsObject(std::string, TrackingSlaveSD::Collection &);
  std::string name(){return _name;}
  TrackingSlaveSD::Collection& hits(){return _hits;}
 private:
  TrackingSlaveSD::Collection& _hits;
  std::string _name;

};


#endif
