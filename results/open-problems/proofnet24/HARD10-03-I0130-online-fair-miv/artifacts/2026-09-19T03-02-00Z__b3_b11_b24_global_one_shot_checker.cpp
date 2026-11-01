#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using i128 = __int128_t;

struct Action { int A,B,dh,c,m; };
static inline Action mk(int A,int B){
    assert(0<=A&&A<=960&&0<=B&&B<=960);
    assert((9*A+11*B)%40==0 && (11*A+9*B)%40==0);
    return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam654(){
    vector<Action> v; v.reserve(654);
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk(40*i,40*j));
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto&p:ex) v.push_back(mk(4*p[0],4*p[1]));
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};
    for(auto&p:cut) v.push_back(mk(p[0],p[1]));
    assert(v.size()==654); return v;
}

struct Orbit { vector<long long> r,s; };
static Orbit solve_orbit(const vector<Action>& acts,long long P,long long Q,
                         long long rnum,long long R,int M,int H){
    const long long snum=R-rnum;
    vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1);
    for(int h=1;h<=H;++h){
        for(int k=0;k<=M;++k){
            long long br=0,bs=0;
            for(const auto&a:acts){
                int kh=k+a.dh;
                long long baseH=(9LL*a.A*Q-10LL*P*a.m)*R;
                long long HR=baseH+(kh<=M?pr[kh]:0);
                long long HS=baseH+(kh<=M?ps[kh]:0);
                long long LR,LS;
                if(k>=a.c){
                    long long baseL=(-11LL*a.A*Q-10LL*P*a.m)*R;
                    LR=baseL+pr[k-a.c]; LS=baseL+ps[k-a.c];
                } else {
                    int kl=a.c-k-1;
                    long long xr=k*R+rnum, xs=k*R+snum;
                    long long baseL=(9LL*a.B*Q-10LL*P*a.m)*R;
                    LR=baseL-40LL*xr*Q+ps[kl];
                    LS=baseL-40LL*xs*Q+pr[kl];
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

struct Aff { long long C,S; };
static inline i128 eval(const Aff&a,long long P,long long Q){
    return (i128)a.C*Q+(i128)a.S*P;
}
static pair<vector<Aff>,vector<Aff>> solve_symbolic(
    const vector<Action>& acts,long long Pref,long long Qref,
    long long rnum,long long R,int M,int H){
    const long long snum=R-rnum;
    vector<Aff> pr(M+1,{0,0}),ps(M+1,{0,0}),cr(M+1),cs(M+1);
    for(int h=1;h<=H;++h){
        for(int k=0;k<=M;++k){
            Aff br{0,0},bs{0,0}; i128 vr=0,vs=0;
            for(const auto&a:acts){
                int kh=k+a.dh;
                Aff HR{9LL*a.A*R,-10LL*a.m*R}, HS=HR;
                if(kh<=M){
                    HR.C+=pr[kh].C; HR.S+=pr[kh].S;
                    HS.C+=ps[kh].C; HS.S+=ps[kh].S;
                }
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
                i128 er=eval(mr,Pref,Qref), es=eval(ms,Pref,Qref);
                if(er>vr){vr=er;br=mr;} if(es>vs){vs=es;bs=ms;}
            }
            cr[k]=br; cs[k]=bs;
        }
        pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps)};
}

static void print128(i128 x){
    if(x<0){ cout<<'-'; x=-x; }
    if(x==0){ cout<<0; return; }
    string s; while(x){ s.push_back(char('0'+x%10)); x/=10; }
    reverse(s.begin(),s.end()); cout<<s;
}

int main(){
    const auto old=fam654();
    const long long R=309151;
    const long long A_num=183613240;
    const long long U_num=(11LL*A_num+8640LL*R)/40;
    const long long V_num=(9LL*A_num+10560LL*R)/40;
    assert(U_num==117270257 && V_num==122928843);
    const long long rL=(R-U_num%R)%R, rH=V_num%R;
    const long long kL=(480LL*R-U_num)/R, kH=(480LL*R+V_num)/R;
    assert(kL==100 && rL==207123 && R-rL==102028);
    assert(kH==877 && rH==195896 && R-rH==113255);

    const long long P=617,Q=253330;
    const int M=3200,H=612;
    auto Ltab=solve_orbit(old,P,Q,rL,R,M,H);
    auto Htab=solve_orbit(old,P,Q,rH,R,M,H);
    i128 Hroot=(i128)9*A_num*Q-(i128)9600*P*R+Htab.r[kH];
    i128 Lroot=-(i128)11*A_num*Q-(i128)9600*P*R+Ltab.r[kL];
    i128 threshold=((i128)12480*Q+(i128)28800*P)*R;
    i128 Hmargin=Hroot-threshold, Lmargin=Lroot-threshold;
    assert(Hmargin==(i128)2715305000LL);
    assert(Lmargin==0);

    auto Lsym=solve_symbolic(old,P,Q,rL,R,M,H);
    auto Hsym=solve_symbolic(old,P,Q,rH,R,M,H);
    Aff BH{9*A_num+Hsym.first[kH].C,-9600LL*R+Hsym.first[kH].S};
    Aff BL{-11*A_num+Lsym.first[kL].C,-9600LL*R+Lsym.first[kL].S};
    assert(BH.C==4145512824LL && BH.S==-109056106760LL);
    assert(BL.C==4239696814LL && BL.S==-147730896860LL);

    auto equality=[&](Aff B){
        long long num=B.C-12480LL*R;
        long long den=28800LL*R-B.S;
        long long g=gcd(llabs(num),llabs(den));
        return pair<long long,long long>{num/g,den/g};
    };
    auto eh=equality(BH), el=equality(BL);
    assert(eh.first==35913543LL && eh.second==14744956945LL);
    assert(el.first==617LL && el.second==253330LL);
    assert((i128)eh.first*el.second>(i128)el.first*eh.second);

    long long un=9*Q-10*P, ud=10*Q;
    long long g=gcd(llabs(un),llabs(ud)); un/=g; ud/=g;
    assert(un==22738 && ud==25333);
    long long wn=30*un-19*ud, wd=30*ud; g=gcd(llabs(wn),llabs(wd)); wn/=g; wd/=g;
    assert(wn==200813 && wd==759990);
    const long long old_un=693387, old_ud=772510;
    long long in=old_un*ud-un*old_ud, id=old_ud*ud; g=gcd(llabs(in),llabs(id)); in/=g; id/=g;
    assert(in==240491 && id==19569995830LL);

    cout << "I0130_B3_B11_B24_GLOBAL_ONE_SHOT_PASS\n";
    cout << "one_shot_action=(4590331/7419624,1) quotient=(117270257,122928843)/309151\n";
    cout << "low_orbit={207123,102028}/309151 high_orbit={195896,113255}/309151 continuation_h=612 total_goods_max=616\n";
    cout << "epsilon=617/253330 Hmargin_scaled="; print128(Hmargin);
    cout << " Lmargin_scaled="; print128(Lmargin); cout << "\n";
    cout << "active_root_faces H=(4145512824-109056106760eps)/(9600R)"
         << " L=(4239696814-147730896860eps)/(9600R)\n";
    cout << "H_transport_equality=35913543/14744956945 L_transport_equality=617/253330\n";
    cout << "new_upper=22738/25333 new_width=200813/759990 improvement=240491/19569995830\n";
    cout << "outer_state_updates_exact_plus_symbolic=" << 4LL*H*(M+1) << "\n";
}
