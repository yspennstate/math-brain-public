#define main i0130_p1_main
#include "2026-09-20T13-25-52Z__exact_path_weight_checker.cpp"
#undef main
int main(){
 long long P=21471646LL,Q=4870886400LL; auto g=build_gen(P,Q);
 if(s128(g.S)!="202391574968484000000000") return 10;
 struct T{int J; const char* v;};
 T ts[]={{7016,"57704102461588798433630822400000000000"},{811,"151127280916349715999090892800000000000"},{4480,"89814898252348289024714956800000000000"},{2823,"115562622066938801325250560000000000000"}};
 for(auto t:ts){ if(s128(g.val[t.J])!=string(t.v)) return 11; if(g.w[t.J]*96 != g.S*(i128)97895) return 12; }
 cout<<"I0130_P21471646_EXACT_PATH_WEIGHT_PASS\n";
 cout<<"P="<<P<<" Q="<<Q<<" S="<<s128(g.S)<<"\n";
 cout<<"generated_plus_old654_worst_path_weight=97895/96\n";
 for(auto t:ts) cout<<"J="<<t.J<<" value="<<s128(g.val[t.J])<<" weight_num_over_S="<<s128(g.w[t.J])<<"/"<<s128(g.S)<<"\n";
 return 0;
}
