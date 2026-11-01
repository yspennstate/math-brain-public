#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

struct Action { int A,B,dh,c,m; };
static Action mk(int A,int B){
    assert(0<=A&&A<=960&&0<=B&&B<=960);
    assert((9*A+11*B)%40==0 && (11*A+9*B)%40==0);
    return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam654(){
    vector<Action> v;
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk(40*i,40*j));
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto&p:ex) v.push_back(mk(4*p[0],4*p[1]));
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};
    for(auto&p:cut) v.push_back(mk(p[0],p[1]));
    assert(v.size()==654);
    return v;
}
static void print128(__int128 x){
    if(x<0){ cout<<'-'; x=-x; }
    if(x==0){ cout<<0; return; }
    string s; while(x){ s.push_back(char('0'+x%10)); x/=10; }
    reverse(s.begin(),s.end()); cout<<s;
}

// Exact Bellman continuation on the sign-orbit {r,1-r} of one fractional coset.
// State x=k+r/R. Old 654 actions have integer quotient shifts, so high/nonreflection
// preserve r and reflection swaps r <-> 1-r. Values are scaled by 9600*Q*R.
struct OrbitTables { vector<long long> r,s; };
static OrbitTables solve_orbit(const vector<Action>& acts,long long P,long long Q,
                               long long rnum,long long R,int M,int H){
    assert(0<rnum && rnum<R);
    long long snum=R-rnum;
    vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1);
    for(int h=1;h<=H;++h){
        for(int k=0;k<=M;++k){
            long long br=0,bs=0;
            for(const auto&a:acts){
                int kh=k+a.dh;
                long long HR=(9LL*a.A*Q-10LL*P*a.m)*R + (kh<=M?pr[kh]:0);
                long long HS=(9LL*a.A*Q-10LL*P*a.m)*R + (kh<=M?ps[kh]:0);
                long long LR,LS;
                if(k>=a.c){
                    LR=(-11LL*a.A*Q-10LL*P*a.m)*R + pr[k-a.c];
                    LS=(-11LL*a.A*Q-10LL*P*a.m)*R + ps[k-a.c];
                } else {
                    int kl=a.c-k-1;
                    long long xr=k*R+rnum, xs=k*R+snum;
                    LR=(9LL*a.B*Q-10LL*P*a.m)*R - 40LL*xr*Q + ps[kl];
                    LS=(9LL*a.B*Q-10LL*P*a.m)*R - 40LL*xs*Q + pr[kl];
                }
                br=max(br,min(HR,LR));
                bs=max(bs,min(HS,LS));
            }
            cr[k]=br; cs[k]=bs;
        }
        pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps)};
}

struct Aff { long long C,S; }; // value = C*Q + S*P in the same R-scaled units
static inline __int128 eval(const Aff&a,long long P,long long Q){ return (__int128)a.C*Q+(__int128)a.S*P; }
static vector<Aff> solve_orbit_symbolic(const vector<Action>& acts,long long Pref,long long Qref,
                                        long long rnum,long long R,int M,int H){
    long long snum=R-rnum;
    vector<Aff> pr(M+1,{0,0}),ps(M+1,{0,0}),cr(M+1),cs(M+1);
    for(int h=1;h<=H;++h){
        for(int k=0;k<=M;++k){
            Aff br{0,0},bs{0,0}; __int128 vr=0,vs=0;
            for(const auto&a:acts){
                int kh=k+a.dh;
                Aff HR{9LL*a.A*R,-10LL*a.m*R}, HS=HR;
                if(kh<=M){ HR.C+=pr[kh].C; HR.S+=pr[kh].S; HS.C+=ps[kh].C; HS.S+=ps[kh].S; }
                Aff LR,LS;
                if(k>=a.c){
                    LR={-11LL*a.A*R,-10LL*a.m*R}; LS=LR;
                    LR.C+=pr[k-a.c].C; LR.S+=pr[k-a.c].S;
                    LS.C+=ps[k-a.c].C; LS.S+=ps[k-a.c].S;
                } else {
                    int kl=a.c-k-1;
                    long long xr=k*R+rnum, xs=k*R+snum;
                    LR={9LL*a.B*R-40LL*xr,-10LL*a.m*R};
                    LS={9LL*a.B*R-40LL*xs,-10LL*a.m*R};
                    LR.C+=ps[kl].C; LR.S+=ps[kl].S;
                    LS.C+=pr[kl].C; LS.S+=pr[kl].S;
                }
                Aff mr=eval(HR,Pref,Qref)<=eval(LR,Pref,Qref)?HR:LR;
                Aff ms=eval(HS,Pref,Qref)<=eval(LS,Pref,Qref)?HS:LS;
                auto er=eval(mr,Pref,Qref), es=eval(ms,Pref,Qref);
                if(er>vr){vr=er;br=mr;} if(es>vs){vs=es;bs=ms;}
            }
            cr[k]=br; cs[k]=bs;
        }
        pr.swap(cr); ps.swap(cs);
    }
    return pr;
}

int main(){
    const auto old=fam654();
    // One-shot exact continuous/KKT action inherited from the previous structural cell.
    // U=240u, V=240v have common denominator R; b=1 exactly.
    const long long R=309151;
    const long long U_num=117314257, V_num=122964843;
    const long long A_num=40LL*4594331; // A=960a=A_num/R; a=4594331/7419624
    assert(-9LL*U_num+11LL*V_num==960LL*R);
    assert(11LL*U_num-9LL*V_num==A_num);
    const long long rL=(R-U_num%R)%R, rH=V_num%R;
    assert(rL==163123 && R-rL==146028);
    assert(rH==231896 && R-rH==77255);
    assert(rL!=rH && rL!=R-rH && R-rL!=rH && R-rL!=R-rH);
    const long long kL=(480LL*R-U_num)/R, kH=(480LL*R+V_num)/R;
    assert(kL==100 && kH==877);

    // B27 source-valid one-shot certificate.
    const long long P=936,Q=386255; // epsilon=936/386255
    const int M=3200, HCONT=612;
    auto Ltab=solve_orbit(old,P,Q,rL,R,M,HCONT);
    auto Htab=solve_orbit(old,P,Q,rH,R,M,HCONT);
    __int128 Hroot=(__int128)9*A_num*Q-(__int128)9600*P*R+Htab.r[kH];
    __int128 Lroot=-(__int128)11*A_num*Q-(__int128)9600*P*R+Ltab.r[kL];
    __int128 threshold=((__int128)12480*Q+(__int128)28800*P)*R;
    __int128 Hmargin=Hroot-threshold, Lmargin=Lroot-threshold;
    assert(Hmargin==(__int128)1126996590870LL);
    assert(Lmargin==(__int128)551830LL);
    assert(min(Hmargin,Lmargin)>0);

    // B5 active finite-horizon affine face at the exact feasible parameter.
    auto Lsym=solve_orbit_symbolic(old,P,Q,rL,R,M,HCONT);
    auto Hsym=solve_orbit_symbolic(old,P,Q,rH,R,M,HCONT);
    Aff BH{9*A_num+Hsym[kH].C,-9600LL*R+Hsym[kH].S};
    Aff BL{-11*A_num+Lsym[kL].C,-9600LL*R+Lsym[kL].S};
    assert(BH.C==4349137578LL && BH.S==-192483595620LL);
    assert(BL.C==6282908522LL && BL.S==-991688394780LL);
    assert(eval(BL,P,Q)<eval(BH,P,Q));
    long long num=BL.C-12480LL*R, den=28800LL*R-BL.S;
    long long g=gcd(llabs(num),llabs(den)); num/=g; den/=g;
    assert(num==1212352021LL && den==500295971790LL);
    // Chosen rational epsilon lies strictly below this local-face transport equality.
    assert((__int128)P*den < (__int128)num*Q);

    long long un=9*Q-10*P, ud=10*Q; g=gcd(llabs(un),llabs(ud)); un/=g;ud/=g;
    assert(un==693387 && ud==772510);
    long long wn=30*un-19*ud, wd=30*ud; g=gcd(llabs(wn),llabs(wd)); wn/=g;wd/=g;
    assert(wn==306196 && wd==1158765);
    long long in=21872LL*ud-un*24367LL, id=24367LL*ud; g=gcd(llabs(in),llabs(id)); in/=g;id/=g;
    assert(in==577691 && id==18823751170LL);

    cout << "I0130_B12_B27_B5_ONE_SHOT_COSET_PASS\n";
    cout << "coset_den="<<R<<" low_orbit={163123,146028}/"<<R
         <<" high_orbit={231896,77255}/"<<R<<"\n";
    cout << "one_shot_action=(4594331/7419624,1) continuation_family=old654 continuation_h="<<HCONT
         <<" total_goods_max="<<(3+1+HCONT)<<"\n";
    cout << "epsilon=936/386255 Hmargin_scaled="; print128(Hmargin);
    cout << " Lmargin_scaled="; print128(Lmargin); cout << "\n";
    cout << "active_h612_root_faces H=(4349137578-192483595620eps)*Qscale"
         << " L=(6282908522-991688394780eps)*Qscale\n";
    cout << "local_face_transport_equality=1212352021/500295971790\n";
    cout << "new_upper=693387/772510 new_width=306196/1158765 improvement=577691/18823751170\n";
}
