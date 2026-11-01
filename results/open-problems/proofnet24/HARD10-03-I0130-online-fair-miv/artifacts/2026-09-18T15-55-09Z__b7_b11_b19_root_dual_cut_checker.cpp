#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact checker for B7/B11/B19.
// Gap D is in units 1/240. Actions are a=A/960, b=B/960.
// Bellman values at epsilon=P/Q are stored in scale 9600*Q.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam646(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  assert(v.size()==646); return v;
}
static vector<Action> fam647_rootcut(){
  auto v=fam646(); v.push_back(mk960(586,946)); assert(v.size()==647); return v;
}
static vector<Action> fam647_nonmoving(){
  auto v=fam646(); v.push_back(mk960(699,959)); assert(v.size()==647); return v;
}
static pair<long long,long long> branches(const vector<long long>&prev,const Action&x,int D,long long P,long long Q){
  long long H=9LL*x.A*Q-10LL*P*x.m;
  int DH=D+x.dh; if(DH<(int)prev.size()) H+=prev[DH];
  int DL=abs(D-x.c);
  long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)
      -10LL*P*x.m + prev[DL];
  return {H,L};
}
struct Run{int first,stable,last;long long first_root,fixed_root,threshold,checked;vector<long long>fixed;};
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=2700,int MAXH=700){
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  const long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0;
      for(const auto&x:acts){auto [H,L]=branches(prev,x,D,P,Q); best=max(best,min(H,L));}
      cur[D]=best; changed|=(cur[D]!=prev[D]); ++checked;
    }
    prev.swap(cur);
    if(first<0 && prev[480]>=threshold){first=h;first_root=prev[480];}
    if(!changed){stable=h;break;}
  }
  int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
  return {first,stable,last,first_root,prev[480],threshold,checked,prev};
}

// Compute exact first-equality layers for the old 646 family at eps=227/113830,
// and extract one basic tight chain by selecting, among optimal actions, the action
// with largest slack on its nonbinding branch. This is a valid basic dual/subgradient
// occupation chain; it is not claimed to be the unique dual solution.
struct TightData{vector<pair<int,int>> chain; long long candidate_residual; long long candH,candL,oldroot;};
static TightData old_tight_chain_and_rootcut(){
  auto acts=fam646(); const long long P=227,Q=113830; const int HMAX=201,MAXD=2700;
  vector<vector<long long>> val(HMAX+1,vector<long long>(MAXD+1));
  for(int h=1;h<=HMAX;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(auto&x:acts){auto [H,L]=branches(val[h-1],x,D,P,Q); best=max(best,min(H,L));}
    val[h][D]=best;
  }
  const long long threshold=12480LL*Q+28800LL*P;
  assert(val[HMAX][480]==threshold);
  vector<pair<int,int>> chain; int h=HMAX,D=480;
  while(h>0 && val[h][D]>0){
    chain.push_back({h,D}); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)acts.size();++i){auto [H,L]=branches(val[h-1],acts[i],D,P,Q);if(min(H,L)==best){long long slack=llabs(H-L);if(slack>bestSlack){bestSlack=slack;sel=i;sh=H-best;sl=L-best;}}}
    assert(sel>=0); assert((sh==0) != (sl==0)); // unique tight branch in this chosen basic chain
    const auto&x=acts[sel];
    D=(sh==0 ? D+x.dh : abs(D-x.c)); --h; assert(D<=MAXD);
  }
  assert(chain.size()==22);
  bool has316=false;for(auto [hh,DD]:chain) if(DD==316) has316=true; assert(!has316);
  Action cand=mk960(586,946); auto [H,L]=branches(val[200],cand,480,P,Q);
  long long res=min(H,L)-val[201][480];
  assert(cand.dh==392 && cand.c==374 && cand.m==946);
  assert(res==2018800LL && H-L==1407000LL);
  return {chain,res,H,L,val[201][480]};
}

// Right-hand active affine face at an exact epsilon. Value is represented as
// (C + S*epsilon)/9600 locally. min ties choose smaller slope; max ties larger slope.
struct Face{long long C,S;};
static __int128 faceval(Face f,long long P,long long Q){return (__int128)f.C*Q+(__int128)f.S*P;}
static Face minR(Face a,Face b,long long P,long long Q){auto A=faceval(a,P,Q),B=faceval(b,P,Q);if(A<B)return a;if(B<A)return b;return a.S<b.S?a:b;}
static Face maxR(Face a,Face b,long long P,long long Q){auto A=faceval(a,P,Q),B=faceval(b,P,Q);if(A>B)return a;if(B>A)return b;return a.S>b.S?a:b;}
static pair<Face,int> fixed_face(const vector<Action>&acts,long long P,long long Q,int MAXD=2700,int MAXH=700){
  vector<Face> prev(MAXD+1,{0,0}),cur(MAXD+1); int stable=-1;
  for(int h=1;h<=MAXH;++h){bool changed=false;for(int D=0;D<=MAXD;++D){Face best{0,0};for(auto&x:acts){int DH=D+x.dh;Face ch=DH<=MAXD?prev[DH]:Face{0,0};Face H{ch.C+9LL*x.A,ch.S-10LL*x.m};int DL=abs(D-x.c);Face cl=prev[DL];long long base=(D>=x.c?-11LL*x.A:9LL*x.B-40LL*D);Face L{cl.C+base,cl.S-10LL*x.m};best=maxR(best,minR(H,L,P,Q),P,Q);}cur[D]=best;changed|=(cur[D].C!=prev[D].C||cur[D].S!=prev[D].S);}prev.swap(cur);if(!changed){stable=h;break;}}
  return {prev[480],stable};
}

int main(){
  auto old=fam646();
  auto oldrun=solve(old,227,113830); assert(oldrun.first==201&&oldrun.stable==241&&oldrun.fixed_root==oldrun.threshold);
  auto td=old_tight_chain_and_rootcut();

  // Previously known positive residual outside this chosen critical chain can be all-horizon nonmoving.
  Action non=mk960(699,959); auto [nH,nL]=branches(oldrun.fixed,non,316,227,113830);
  long long nonres=min(nH,nL)-oldrun.fixed[316]; assert(nonres==8540400LL);
  auto nonrun=solve(fam647_nonmoving(),227,113830); assert(nonrun.fixed_root==oldrun.fixed_root&&nonrun.first==197&&nonrun.stable==236);

  // Root-relevant cut directly improves the first-equality root local Bellman value.
  auto newacts=fam647_rootcut();
  auto atOld=solve(newacts,227,113830); assert(atOld.fixed_root>oldrun.fixed_root);

  // B11 parametric active face and exact critical epsilon for the new frozen family.
  const long long P=43,Q=20670;
  auto [face,faceStable]=fixed_face(newacts,P,Q);
  assert(face.C==13641 && face.S==-529290 && faceStable==316);
  long long num=face.C-12480, den=28800-face.S, g=gcd(num,den); num/=g;den/=g;
  assert(num==43&&den==20670);
  auto nr=solve(newacts,P,Q); assert(nr.first==301&&nr.stable==316&&nr.fixed_root==nr.threshold&&nr.first_root==nr.threshold);

  // Source endpoint arithmetic.
  long long an=9LL*den-10LL*num, ad=10LL*den; g=gcd(an,ad);an/=g;ad/=g; assert(an==1856&&ad==2067);
  long long wn=30LL*an-19LL*ad, wd=30LL*ad; g=gcd(wn,wd);wn/=g;wd/=g; assert(wn==1823&&wd==6890);
  long long in=10222LL*ad-an*11383LL, id=11383LL*ad; g=gcd(llabs(in),id);in/=g;id/=g; assert(in==2026&&id==23528661LL);

  // B19 compression diagnostic for the new first-equality policy: exact reachable tree is still large.
  const int HMAX=301,MAXD=2700; vector<vector<long long>> val(HMAX+1,vector<long long>(MAXD+1)); vector<vector<short>> pol(HMAX+1,vector<short>(MAXD+1,-1));
  for(int h=1;h<=HMAX;++h)for(int D=0;D<=MAXD;++D){long long best=0;int bi=-1;for(int i=0;i<(int)newacts.size();++i){auto [H,L]=branches(val[h-1],newacts[i],D,P,Q);long long w=min(H,L);if(w>best){best=w;bi=i;}}val[h][D]=best;pol[h][D]=bi;}
  vector<vector<char>> seen(HMAX+1,vector<char>(MAXD+1));queue<pair<int,int>>qq;qq.push({HMAX,480});seen[HMAX][480]=1;set<int> used;long long nodes=0;
  while(!qq.empty()){auto [h,D]=qq.front();qq.pop();++nodes;if(h==0||val[h][D]==0)continue;int i=pol[h][D];assert(i>=0);used.insert(i);auto&x=newacts[i];int DH=D+x.dh,DL=abs(D-x.c);if(DH<=MAXD&&!seen[h-1][DH]){seen[h-1][DH]=1;qq.push({h-1,DH});}if(!seen[h-1][DL]){seen[h-1][DL]=1;qq.push({h-1,DL});}}
  assert(nodes==360544 && used.size()==184);

  cout<<"I0130_B7_B11_B19_ROOT_DUAL_CUT_PASS\n";
  cout<<"old_critical_eps=227/113830 old_first_h="<<oldrun.first<<" old_stable_h="<<oldrun.stable<<"\n";
  cout<<"selected_basic_tight_chain_nodes="<<td.chain.size()<<" contains_D316=0\n";
  cout<<"root_cut=586/960,946/960 root_h201_residual_scaled="<<td.candidate_residual
      <<" root_cut_H_minus_L="<<td.candH-td.candL<<"\n";
  cout<<"nonmoving_cut=699/960,959/960 fixed_residual_scaled="<<nonres
      <<" augmented_root_unchanged=1\n";
  cout<<"new_root_face=(13641-529290*eps)/9600\n";
  cout<<"new_critical_eps=43/20670 first_h="<<nr.first<<" stable_h="<<nr.stable<<"\n";
  cout<<"source_valid_upper_bound=1856/2067\n";
  cout<<"width=1823/6890\n";
  cout<<"improvement_over_10222_11383=2026/23528661\n";
  cout<<"new_policy_reachable_nodes="<<nodes<<" distinct_actions="<<used.size()<<" compression_small_state_machine=FAIL\n";
  cout<<"checked_states="<<oldrun.checked+nonrun.checked+atOld.checked+nr.checked<<"\n";
}
