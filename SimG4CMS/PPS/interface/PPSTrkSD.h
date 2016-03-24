//
#ifndef PPS_PPSTrkSD_h
#define PPS_PPSTrkSD_h
//
#include "SimG4CMS/PPS/interface/PPSBaseSD.h"
class PPSTrkSD;

//-------------------------------------------------------------------
class PPSTrkSD : public PPSBaseSD {

public:
  
        PPSTrkSD(std::string, const DDCompactView &, const SensitiveDetectorCatalog &,
                 edm::ParameterSet const &, const SimTrackManager* );
//-------------------------------------------------------------------

        virtual ~PPSTrkSD();

        virtual void Initialize(G4HCofThisEvent * HCE);
        virtual bool ProcessHits(G4Step *st,G4TouchableHistory *th) {
                                 std::cout << "Entering PPSTrkSD::ProcessHits" <<std::endl;
                                 return PPSBaseSD::ProcessHits(st,th);
                     };
private:

};

#endif // PPSTrkSD_h
