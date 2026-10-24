#include <boost/rational.hpp>
#define main i0130_inherited_main
#include "2026-09-20T04-25-00Z__frozen_policy_right_derivative_checker.cpp"
#undef main

using boost::multiprecision::cpp_int;
using Rat=boost::rational<cpp_int>;
static cpp_int BI(const char*s){return cpp_int(s);}
static string rs(const Rat&r){return r.numerator().convert_to<string>()+"/"+r.denominator().convert_to<string>();}

int main(){
 const long long P=21454951LL,Q=4870886400LL; const int H=416;
 auto gp=build_gen_policy(P,Q,25000,H); cpp_int S(s128(gp.S));
 if(S!=BI("202391574968484000000000")) return 10;

 // Targeted full-continuum reflected separator at J=811.
 // Choose high wall u=3669 and reflected low cell ceil(v)=3634, then solve H=L exactly.
 const int J=811,K=3669,CV=3634;
 cpp_int FH(s128(gp.finalv[J+K])), FL(s128(gp.finalv[CV-J])), B0(s128(gp.finalv[J]));
 if(FH!=BI("89844598037244560704230071378582323200")) return 11;
 if(FL!=BI("115582335272231743319992012800000000000")) return 12;
 if(B0!=BI("151136423214451135550133350400000000000")) return 13;
 Rat d(FL-FH-cpp_int(40)*Q*J*S, cpp_int(8)*S*cpp_int(8640)*Q); // d=a-b
 Rat b=(Rat(cpp_int(K))-Rat(cpp_int(1728))*d)/Rat(cpp_int(3840));
 Rat a=b+d;
 Rat u=Rat(cpp_int(1728))*a+Rat(cpp_int(2112))*b;
 Rat v=Rat(cpp_int(2112))*a+Rat(cpp_int(1728))*b;
 if(u!=Rat(cpp_int(3669))) return 14;
 if(!(Rat(cpp_int(3633))<v && v<Rat(cpp_int(3634)))) return 15;
 if(!(Rat(cpp_int(0))<a && a<b && b<Rat(cpp_int(1)))) return 16;
 Rat Hi=Rat(FH)+Rat(cpp_int(8))*Rat(S)*(Rat(cpp_int(8640)*Q)*a-Rat(cpp_int(9600)*P)*b);
 Rat Li=Rat(FL)+Rat(cpp_int(8))*Rat(S)*(Rat(cpp_int(8640)*Q)*b-Rat(cpp_int(9600)*P)*b)-Rat(cpp_int(40)*Q*J)*Rat(S);
 if(Hi!=Li || !(Hi>Rat(B0))) return 17;
 Rat innerGain=Hi-Rat(B0);

 // Source root: retain the large-wall geometry but replace its low continuation by the new J=811 separator.
 cpp_int FHr(s128(gp.finalv[7016]));
 if(FHr!=BI("57721999155541552891783987200000000000")) return 18;
 Rat ar=(Hi-Rat(FHr))/(Rat(cpp_int(8))*Rat(S)*Rat(cpp_int(19200)*Q));
 Rat br=(Rat(cpp_int(3029))-Rat(cpp_int(2112))*ar)/Rat(cpp_int(1728));
 Rat ur=Rat(cpp_int(1728))*ar+Rat(cpp_int(2112))*br;
 Rat vr=Rat(cpp_int(2112))*ar+Rat(cpp_int(1728))*br;
 if(vr!=Rat(cpp_int(3029))) return 19;
 if(!(Rat(cpp_int(3175))<ur && ur<Rat(cpp_int(3176)))) return 20;
 if(!(Rat(cpp_int(0))<ar && ar<br && br<Rat(cpp_int(1)))) return 21;
 Rat Hr=Rat(FHr)+Rat(cpp_int(8))*Rat(S)*(Rat(cpp_int(8640)*Q)*ar-Rat(cpp_int(9600)*P)*br);
 Rat Lr=Hi+Rat(cpp_int(8))*Rat(S)*(Rat(cpp_int(-10560)*Q)*ar-Rat(cpp_int(9600)*P)*br);
 if(Hr!=Lr) return 22;
 Rat T=Rat(cpp_int(8))*Rat(S)*Rat(cpp_int(12480)*Q+cpp_int(28800)*P);
 Rat gap=Hr-T;
 if(!(gap>Rat(cpp_int(0)))) return 23;

 // Freeze this finite nested adaptive policy.  At most 1030 reward-bearing goods occur after the exact-MIV prefix.
 // Every immediate reward has |d/dP| <= 76800 S; the physical threshold has derivative 230400 S.
 // Therefore the same witness remains valid for P -> P+eta up to the exact robust endpoint below.
 const long long N=1030, Ccoef=N*76800LL+230400LL;
 Rat eta=gap/(Rat(S)*Rat(cpp_int(Ccoef)));
 if(!(eta>Rat(cpp_int(1363)) && eta<Rat(cpp_int(1364)))) return 24;
 if(gap!=Rat(S)*Rat(cpp_int(Ccoef))*eta) return 25;
 Rat Pnew=Rat(cpp_int(P))+eta;
 Rat U=Rat(cpp_int(9),cpp_int(10))-Pnew/Rat(cpp_int(Q));
 Rat W=U-Rat(cpp_int(19),cpp_int(30));
 Rat Uexpected(BI("22974092575376445790975264528190846585875386237683"),BI("25652323754312700812535643741618176000000000000000"));
 Rat Wexpected(BI("6727620864311735276369356825166001785875386237683"),BI("25652323754312700812535643741618176000000000000000"));
 if(U!=Uexpected || W!=Wexpected) return 26;

 cout<<"I0130_NESTED_REFLECTED_SEPARATOR_ROBUST_ENDPOINT_PASS\n";
 cout<<"P1="<<P<<" Q="<<Q<<" S="<<S<<" generated_horizon="<<H<<"\n";
 cout<<"inner_state=811 high_wall_u=3669 reflected_ceil_v=3634 high_child=4480 reflected_low_child=2823\n";
 cout<<"inner_a="<<rs(a)<<"\ninner_b="<<rs(b)<<"\ninner_v="<<rs(v)<<"\ninner_gain="<<rs(innerGain)<<"\n";
 cout<<"root_high_child=7016 root_low_child=811 root_v=3029 root_u="<<rs(ur)<<"\n";
 cout<<"root_a="<<rs(ar)<<"\nroot_b="<<rs(br)<<"\nroot_gap="<<rs(gap)<<"\n";
 cout<<"max_reward_goods_after_prefix="<<N<<" total_goods<=1033 sensitivity_coef="<<Ccoef<<"\n";
 cout<<"eta_max="<<rs(eta)<<"\n";
 cout<<"U_MIV="<<rs(U)<<"\nW_MIV="<<rs(W)<<"\n";
 return 0;
}
