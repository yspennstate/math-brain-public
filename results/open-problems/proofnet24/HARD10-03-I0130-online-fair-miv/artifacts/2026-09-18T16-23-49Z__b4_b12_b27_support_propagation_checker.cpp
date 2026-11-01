#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact checker for B4/B12/B27 support-propagation run.
// Gap D uses units 1/240. Actions are a=A/960, b=B/960.
// At epsilon=P/Q, Bellman values use the exact integer scale 9600*Q.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam647(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959},{586,946}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  assert(v.size()==647); return v;
}
static pair<long long,long long> branches(const vector<long long>&prev,const Action&x,int D,long long P,long long Q){
  long long H=9LL*x.A*Q-10LL*P*x.m;
  int DH=D+x.dh; if(DH<(int)prev.size()) H+=prev[DH];
  int DL=abs(D-x.c);
  long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+prev[DL];
  return {H,L};
}
struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long> fixed;};
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=2700,int MAXH=700){
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  const long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0;
      for(const auto&x:acts){auto [H,L]=branches(prev,x,D,P,Q);best=max(best,min(H,L));}
      cur[D]=best; changed|=(cur[D]!=prev[D]); ++checked;
    }
    prev.swap(cur);
    if(first<0 && prev[480]>=threshold){first=h;first_root=prev[480];}
    if(!changed){stable=h;break;}
  }
  int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
  return {first,stable,last,first_root,prev[480],threshold,checked,prev};
}
struct Face{long long C,S;};
static __int128 fv(Face f,long long P,long long Q){return (__int128)f.C*Q+(__int128)f.S*P;}
static Face minR(Face a,Face b,long long P,long long Q){auto A=fv(a,P,Q),B=fv(b,P,Q);if(A<B)return a;if(B<A)return b;return a.S<b.S?a:b;}
static Face maxR(Face a,Face b,long long P,long long Q){auto A=fv(a,P,Q),B=fv(b,P,Q);if(A>B)return a;if(B>A)return b;return a.S>b.S?a:b;}
static pair<Face,int> fixed_face(const vector<Action>&acts,long long P,long long Q,int MAXD=2700,int MAXH=700){
  vector<Face> prev(MAXD+1,{0,0}),cur(MAXD+1); int stable=-1;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      Face best{0,0};
      for(const auto&x:acts){
        int DH=D+x.dh; Face ch=DH<=MAXD?prev[DH]:Face{0,0};
        Face H{ch.C+9LL*x.A,ch.S-10LL*x.m};
        int DL=abs(D-x.c); Face cl=prev[DL];
        long long base=(D>=x.c?-11LL*x.A:9LL*x.B-40LL*D);
        Face L{cl.C+base,cl.S-10LL*x.m};
        best=maxR(best,minR(H,L,P,Q),P,Q);
      }
      cur[D]=best; changed|=(cur[D].C!=prev[D].C||cur[D].S!=prev[D].S);
    }
    prev.swap(cur); if(!changed){stable=h;break;}
  }
  return {prev[480],stable};
}

int main(){
  const long long P0=43,Q0=20670; const int HMAX=301,MAXD=2700;
  auto old=fam647();
  vector<vector<long long>> val(HMAX+1,vector<long long>(MAXD+1));
  for(int h=1;h<=HMAX;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(const auto&x:old){auto [H,L]=branches(val[h-1],x,D,P0,Q0);best=max(best,min(H,L));} val[h][D]=best;
  }
  assert(val[301][480]==12480LL*Q0+28800LL*P0);

  // B4: selected basic support chain. At each node choose an optimal action with
  // maximum nonbinding slack, then follow its unique tight branch. If a descendant
  // node improves by eta, the same selected action improves its parent by at least
  // min(eta,slack). Iterating gives root improvement >= min(descendant improvement,
  // all ancestor nonbinding slacks). We verify the concrete 4-edge prefix used here.
  int h=301,D=480; vector<long long> prefixSlack; vector<pair<int,int>> prefixStates;
  for(int step=0;step<4;++step){
    prefixStates.push_back({h,D}); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)old.size();++i){auto [H,L]=branches(val[h-1],old[i],D,P0,Q0); if(min(H,L)==best){long long s=llabs(H-L); if(s>bestSlack){bestSlack=s;sel=i;sh=H-best;sl=L-best;}}}
    assert(sel>=0); assert((sh==0)!=(sl==0)); prefixSlack.push_back(bestSlack);
    const auto&x=old[sel]; D=(sh==0?D+x.dh:abs(D-x.c)); --h;
  }
  assert(h==297 && D==1238);
  assert(prefixSlack[0]==12800 && prefixSlack[1]==474800 && prefixSlack[2]==536400 && prefixSlack[3]==464600);

  // B27 separation on the positive-occupation support state: this exact missing
  // legal action has positive residual at (h,D)=(297,1238).
  set<pair<int,int>> existing; for(auto&x:old) existing.insert({x.A,x.B});
  Action witness=mk960(215,955); assert(!existing.count({215,955}));
  auto [wH,wL]=branches(val[296],witness,1238,P0,Q0);
  long long residual=min(wH,wL)-val[297][1238]; assert(residual==1638000);
  long long bottleneck=*min_element(prefixSlack.begin(),prefixSlack.end()); assert(bottleneck==12800);

  // Add only this root-support witness. The B4 theorem guarantees at least bottleneck
  // improvement at the old root; exact DP shows equality.
  auto newer=old; newer.push_back(witness); assert(newer.size()==648);
  auto atOld=solve(newer,P0,Q0); assert(atOld.fixed_root-atOld.threshold==12800);

  // Affine fixed face generates the candidate; exact Bellman iteration independently
  // certifies equality and all-horizon criticality for the frozen family.
  auto [face0,faceStable0]=fixed_face(newer,P0,Q0);
  assert(face0.C==13050 && face0.S==-244900 && faceStable0==273);
  long long num=face0.C-12480, den=28800-face0.S, g=gcd(num,den); num/=g;den/=g;
  assert(num==57 && den==27370);
  auto crit=solve(newer,num,den); assert(crit.first==247 && crit.stable==273 && crit.fixed_root==crit.threshold && crit.first_root==crit.threshold && crit.last==2507);
  auto [face1,faceStable1]=fixed_face(newer,num,den); assert(face1.C==13050 && face1.S==-244900 && faceStable1==273);

  // Source endpoint and width.
  long long un=9LL*den-10LL*num,ud=10LL*den; g=gcd(un,ud);un/=g;ud/=g;assert(un==12288&&ud==13685);
  long long wn=30LL*un-19LL*ud,wd=30LL*ud;g=gcd(wn,wd);wn/=g;wd/=g;assert(wn==4345&&wd==16422);
  long long impn=1856LL*ud-un*2067LL, impd=2067LL*ud;g=gcd(llabs(impn),impd);impn/=g;impd/=g;assert(impn==64&&impd==28286895LL);

  cout<<"I0130_B4_B12_B27_SUPPORT_PROPAGATION_PASS\n";
  cout<<"selected_support_prefix_states=";
  for(auto [hh,DD]:prefixStates) cout<<"("<<hh<<","<<DD<<")"; cout<<"\n";
  cout<<"ancestor_nonbinding_slacks="<<prefixSlack[0]<<","<<prefixSlack[1]<<","<<prefixSlack[2]<<","<<prefixSlack[3]<<" bottleneck="<<bottleneck<<"\n";
  cout<<"support_witness=215/960,955/960 at_h=297 D=1238 residual_scaled="<<residual<<" H_minus_L="<<wH-wL<<"\n";
  cout<<"old_eps_root_improvement_scaled="<<atOld.fixed_root-atOld.threshold<<" theorem_lower_bound="<<bottleneck<<"\n";
  cout<<"new_root_face=(13050-244900*eps)/9600\n";
  cout<<"new_critical_eps=57/27370 first_h="<<crit.first<<" stable_h="<<crit.stable<<" last_nonzero_D="<<crit.last<<"\n";
  cout<<"source_valid_upper_bound=12288/13685\n";
  cout<<"width=4345/16422\n";
  cout<<"improvement_over_1856_2067=64/28286895\n";
  cout<<"checked_states="<<atOld.checked+crit.checked<<"\n";
}
