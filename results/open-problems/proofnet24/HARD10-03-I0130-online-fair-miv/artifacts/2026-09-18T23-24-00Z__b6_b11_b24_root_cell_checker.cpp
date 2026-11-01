#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
    assert(0<=A&&A<=960&&0<=B&&B<=960);
    assert((9*A+11*B)%40==0 && (11*A+9*B)%40==0);
    return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam654(){
    vector<Action> v;
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:ex) v.push_back(mk960(4*p[0],4*p[1]));
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};
    for(auto &p:cut) v.push_back(mk960(p[0],p[1]));
    assert(v.size()==654);
    return v;
}
static pair<long long,long long> branches(const vector<long long>&p,const Action&x,int D,long long P,long long Q){
    long long H=9LL*x.A*Q-10LL*P*x.m;
    int DH=D+x.dh; if(DH<(int)p.size()) H+=p[DH];
    int DL=abs(D-x.c); assert(DL<(int)p.size());
    long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+p[DL];
    return {H,L};
}
struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long>fixed;};
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=3200,int MAXH=520){
    vector<long long>prev(MAXD+1),cur(MAXD+1);
    long long thr=12480LL*Q+28800LL*P; int first=-1,stable=-1; long long fr=-1,checked=0;
    for(int h=1;h<=MAXH;++h){
        bool ch=false;
        for(int D=0;D<=MAXD;++D){
            long long best=0;
            for(auto &x:acts){auto [H,L]=branches(prev,x,D,P,Q); best=max(best,min(H,L));}
            cur[D]=best; ch|=(cur[D]!=prev[D]); ++checked;
        }
        prev.swap(cur);
        if(first<0 && prev[480]>=thr){first=h;fr=prev[480];}
        if(!ch){stable=h;break;}
    }
    int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
    return {first,stable,last,fr,prev[480],thr,checked,prev};
}
struct Aff{long long C,S;};
static __int128 ev(const Aff&a,long long P,long long Q){return (__int128)a.C*Q+(__int128)a.S*P;}
static pair<Aff,Aff> brAff(const vector<Aff>&p,const Action&x,int D){
    Aff H{9LL*x.A,-10LL*x.m}; int DH=D+x.dh; if(DH<(int)p.size()){H.C+=p[DH].C;H.S+=p[DH].S;}
    int DL=abs(D-x.c); Aff L{(D>=x.c?-11LL*x.A:9LL*x.B-40LL*D),-10LL*x.m}; L.C+=p[DL].C;L.S+=p[DL].S; return {H,L};
}
static Aff symRoot(const vector<Action>&acts,long long P,long long Q,int MAXD=3200,int MAXH=520){
    vector<Aff>prev(MAXD+1,{0,0}),cur(MAXD+1);
    for(int h=1;h<=MAXH;++h){
        bool ch=false;
        for(int D=0;D<=MAXD;++D){
            Aff best{0,0}; __int128 bv=0;
            for(auto &x:acts){auto [H,L]=brAff(prev,x,D); Aff mn=ev(H,P,Q)<=ev(L,P,Q)?H:L; auto mv=ev(mn,P,Q); if(mv>bv){bv=mv;best=mn;}}
            cur[D]=best; ch|=(cur[D].C!=prev[D].C||cur[D].S!=prev[D].S);
        }
        prev.swap(cur); if(!ch) return prev[480];
    }
    assert(false); return {0,0};
}
int main(){
    auto old=fam654();
    const long long P0=38,Q0=16145;
    auto r0=solve(old,P0,Q0);
    assert(r0.first==260 && r0.stable==297 && r0.last==2505);
    assert(r0.first_root==r0.threshold && r0.fixed_root==r0.threshold);
    Aff f0=symRoot(old,P0,Q0); assert(f0.C==13392 && f0.S==-358680);
    long long n0=f0.C-12480,d0=28800-f0.S,g=std::gcd(llabs(n0),llabs(d0)); n0/=g;d0/=g;
    assert(n0==38 && d0==16145);

    Action z=mk960(598,958); assert(z.c==380 && z.dh==398);
    vector<long long>prev(3201),cur(3201); for(int h=1;h<=259;++h){for(int D=0;D<=3200;++D){long long best=0;for(auto &x:old){auto [H,L]=branches(prev,x,D,P0,Q0);best=max(best,min(H,L));}cur[D]=best;}prev.swap(cur);}
    auto [ZH,ZL]=branches(prev,z,480,P0,Q0); long long old260=r0.threshold;
    assert(ZH-ZL==903975); assert(min(ZH,ZL)-old260==130900);
    long long bestVertex=-1; int bU=-1,bV=-1,bA=-1,bB=-1; long long legalVertices=0;
    for(int U=0;U<=480;++U) for(int V=0;V<=480;++V){int A=11*U-9*V,B=-9*U+11*V;if(A<0||A>960||B<0||B>960)continue;++legalVertices;Action w=mk960(A,B);auto hhll=branches(prev,w,480,P0,Q0);long long rr=min(hhll.first,hhll.second)-old260;if(rr>bestVertex){bestVertex=rr;bU=U;bV=V;bA=A;bB=B;}}
    assert(legalVertices==23089 && bestVertex==130900 && bU==380 && bV==398 && bA==598 && bB==958);

    auto aug=old; aug.push_back(z); assert(aug.size()==655);
    auto oldepsAug=solve(aug,P0,Q0);
    assert(oldepsAug.first<=260 && oldepsAug.fixed_root-r0.fixed_root==182550);

    const long long P1=327,Q1=136730;
    auto r1=solve(aug,P1,Q1);
    assert(r1.first==380 && r1.stable==444 && r1.last==2503);
    assert(r1.first_root==r1.threshold && r1.fixed_root==r1.threshold);
    Aff f1=symRoot(aug,P1,Q1); assert(f1.C==13134 && f1.S==-244660);
    long long n1=f1.C-12480,d1=28800-f1.S;g=std::gcd(llabs(n1),llabs(d1));n1/=g;d1/=g;
    assert(n1==327 && d1==136730);
    long long un=9LL*Q1-10LL*P1,ud=10LL*Q1;g=std::gcd(un,ud);un/=g;ud/=g;assert(un==12273&&ud==13673);
    long long wn=30LL*un-19LL*ud,wd=30LL*ud;g=std::gcd(wn,wd);wn/=g;wd/=g;assert(wn==108403&&wd==410190);
    long long impn=763LL*ud-un*850LL,impd=850LL*ud;g=std::gcd(llabs(impn),impd);impn/=g;impd/=g;assert(impn==449&&impd==11622050);

    cout<<"I0130_B6_B11_B24_ROOT_CELL_PASS\n";
    cout<<"old654_critical_eps=38/16145 first="<<r0.first<<" stable="<<r0.stable<<" last="<<r0.last<<" root_face=(13392-358680eps)/9600\n";
    cout<<"B24_legal_breakpoint_vertices="<<legalVertices<<" best_lattice_cut=(598/960,958/960) quotient=(380/240,398/240) direct_root_residual_scaled=130900 branch_gap_scaled=903975 oldeps_fixed_root_gain_scaled="<<(oldepsAug.fixed_root-r0.fixed_root)<<"\n";
    cout<<"new655_critical_eps=327/136730 first="<<r1.first<<" stable="<<r1.stable<<" last="<<r1.last<<" root_face=(13134-244660eps)/9600\n";
    cout<<"new_upper=12273/13673 new_width=108403/410190 improvement_from_763/850=449/11622050 total_goods_max="<<(r1.first+3)<<" checked_states="<<(r0.checked+oldepsAug.checked+r1.checked)<<"\n";
}
