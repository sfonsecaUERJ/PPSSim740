//
#ifndef PPS_PPSToFSD_h
#define PPS_PPSToFSD_h
//
#include "SimG4CMS/PPS/interface/PPSBaseSD.h"
class PPSToFSD;

//-------------------------------------------------------------------
class PPSToFSD : public PPSBaseSD {

public:
  
        PPSToFSD(std::string, const DDCompactView &, const SensitiveDetectorCatalog &,
                 edm::ParameterSet const &, const SimTrackManager* );
//-------------------------------------------------------------------

        virtual ~PPSToFSD();

        virtual void Initialize(G4HCofThisEvent * HCE);
        virtual bool ProcessHits(G4Step *st,G4TouchableHistory *th) {
                                 std::cout << "Entering PPSToFSD::ProcessHits" <<std::endl;
                                 return PPSBaseSD::ProcessHits(st,th);
                     };
private:

};

#endif // PPSToFSD_h
