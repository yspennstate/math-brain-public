#include <boost/multiprecision/cpp_int.hpp>
#define main i0130_inherited_main
#include "2026-09-20T04-25-00Z__frozen_policy_right_derivative_checker.cpp"
#undef main

static boost::multiprecision::cpp_int Z(const char* s){ return boost::multiprecision::cpp_int(string(s)); }
static boost::multiprecision::cpp_int gcdz(boost::multiprecision::cpp_int a, boost::multiprecision::cpp_int b){ if(a<0)a=-a;if(b<0)b=-b;while(b!=0){boost::multiprecision::cpp_int r=a%b;a=b;b=r;}return a; }
int main(){
    using boost::multiprecision::cpp_int;
    const long long Q=4870886400LL;
    const long long P=21454950LL; // P0 + 30688
    const int J0=3840, KH=3176, QLOW=3029;
    auto gp=build_gen_policy(P,Q,25000,416);
    if(s128(gp.S)!="202391574968484000000000") return 10;
    i128 FHi=gp.finalv[J0+KH], FLi=gp.finalv[J0-QLOW];
    if(s128(FHi)!="57721999839463163025285120000000000000") return 11;
    if(s128(FLi)!="151136423727392343150259200000000000000") return 12;

    cpp_int S(s128(gp.S)), FH(s128(FHi)), FL(s128(FLi));
    cpp_int aN=440718941, aD=714396672;
    cpp_int bN=583858483, bD=584506368;
    if(aN<=0 || aN>=aD || bN<=0 || bN>=bD) return 13;
    if(aN*bD>=bN*aD) return 14; // a<b

    cpp_int g=gcdz(aD,bD), D=aD/g*bD;
    cpp_int A=aN*(D/aD), B=bN*(D/bD);
    // u=1728a+2112b = 13293138833/4185918, v=2112a+1728b=3029.
    cpp_int uN=1728*A+2112*B, vN=2112*A+1728*B;
    if(vN != cpp_int(QLOW)*D) return 15;
    if(!(cpp_int(KH-1)*D < uN && uN < cpp_int(KH)*D)) return 16;

    cpp_int H = FH*D + cpp_int(8)*S*(cpp_int(8640)*Q*A-cpp_int(9600)*P*B);
    cpp_int L = FL*D + cpp_int(8)*S*(-cpp_int(10560)*Q*A-cpp_int(9600)*P*B);
    if(H!=L) return 17;
    cpp_int T = cpp_int(8)*S*(cpp_int(12480)*Q+cpp_int(28800)*P)*D;
    cpp_int G=H-T;
    if(G<=0) return 18;

    // Published simplified gap: G/D = 16070129752483441923000000000000/29.
    cpp_int gn=Z("16070129752483441923000000000000"), gd=29;
    if(G*gd != gn*D) return 19;

    // alpha = 9/10 - P/Q = 145411427/162362880.
    cpp_int Un=145411427, Ud=162362880;
    if((cpp_int(9)*Q-cpp_int(10)*P)*Ud != cpp_int(10)*Q*Un) return 20;
    // W = alpha - 19/30 = 42581603/162362880.
    cpp_int Wn=42581603, Wd=162362880;
    if(Un*30*Wd - cpp_int(19)*Ud*Wd != Wn*30*Ud) return 21;

    cout << "I0130_P30688_ROOT_JUMP_PASS\n";
    cout << "P="<<P<<" Q="<<Q<<" epsilon=P/Q\n";
    cout << "finite_policy_goods<=3+1+416+612=1032\n";
    cout << "root_cell=ceil(u)=3176,floor(v)=3029,a<b\n";
    cout << "a=440718941/714396672\n";
    cout << "b=583858483/584506368\n";
    cout << "u=13293138833/4185918 in (3175,3176), v=3029\n";
    cout << "FH="<<s128(FHi)<<" FL="<<s128(FLi)<<"\n";
    cout << "branch_equal=1\n";
    cout << "gap=16070129752483441923000000000000/29>0\n";
    cout << "U_MIV=145411427/162362880\n";
    cout << "W_MIV=42581603/162362880\n";
    cout << "old_algebraic_improvement=(30688-tau)/4870886400 > 0\n";
    return 0;
}
