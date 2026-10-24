#define main i0130_previous_checker_main
#include "2026-09-20T14-24-00Z__p21476383_frozen_chord_checker.cpp"
#undef main

int main(){
    long long P0=21476383,Q=4870886400,N=6000;
    auto g=build_gen_pair(P0,P0+N,Q);
    if(s128(g.S)!="202391574968484000000000") return 10;
    struct T{int J;const char* v0;const char* vN;};
    T ts[]={
      {7015,"57719977623155054880651571200000000000","57718589902403197490037964800000000000"},
      {4483,"89757393707928277928706048000000000000","89753663226418458831618048000000000000"},
      {6141,"67864014914209824195763200000000000000","67855807854888222182169600000000000000"},
      {382,"159557404200594447305155247280000000000","159531099558230723173198624080000000000"}
    };
    for(auto t:ts){
      if(s128(g.val0[t.J])!=string(t.v0)) return 11;
      if(s128(g.val1[t.J])!=string(t.vN)) return 12;
    }
    cout<<"I0130_P21476383_N6000_FROZEN_CHORD_PASS\n";
    cout<<"base_blob=6520f5085fb7abef50f7a7692a9dac93e2d1f041\n";
    cout<<"S="<<s128(g.S)<<"\n";
    for(auto t:ts) cout<<"J="<<t.J<<" F0="<<s128(g.val0[t.J])<<" F6000frozen="<<s128(g.val1[t.J])<<" diff="<<s128(g.val1[t.J]-g.val0[t.J])<<"\n";
}
