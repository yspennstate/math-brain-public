#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact checker for B6/B18/B24 run.
// Gap D uses units 1/240. Actions are a=A/960, b=B/960.
// At epsilon=P/Q, Bellman values use exact integer scale 9600*Q.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam648(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959},{586,946},{215,955}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  assert(v.size()==648); return v;
}
static pair<long long,long long> branches(const vector<long long>&prev,const Action&x,int D,long long P,long long Q){
  long long H=9LL*x.A*Q-10LL*P*x.m;
  int DH=D+x.dh; if(DH<(int)prev.size()) H+=prev[DH];
  int DL=abs(D-x.c);
  long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+prev[DL];
  return {H,L};
}
struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long> fixed;};
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=700){
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
static pair<Face,int> fixed_face(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=700){
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
  const long long P0=57,Q0=27370; const int HMAX=247,MAXD=2800;
  auto old=fam648();
  vector<vector<long long>> val(HMAX+1,vector<long long>(MAXD+1));
  for(int h=1;h<=HMAX;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(const auto&x:old){auto [H,L]=branches(val[h-1],x,D,P0,Q0);best=max(best,min(H,L));} val[h][D]=best;
  }
  const long long threshold0=12480LL*Q0+28800LL*P0;
  assert(val[247][480]==threshold0);

  // B18 tropical support prefix: select old optimal action with maximal nonbinding slack.
  // The exact slacks are the min-plus capacities that any descendant improvement must cross.
  int h=247,D=480; vector<long long> slack; vector<pair<int,int>> states;
  for(int step=0;step<6;++step){
    states.push_back({h,D}); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)old.size();++i){auto [H,L]=branches(val[h-1],old[i],D,P0,Q0); if(min(H,L)==best){long long s=llabs(H-L); if(s>bestSlack){bestSlack=s;sel=i;sh=H-best;sl=L-best;}}}
    assert(sel>=0); assert((sh==0)!=(sl==0)); slack.push_back(bestSlack);
    const auto&x=old[sel]; D=(sh==0?D+x.dh:abs(D-x.c)); --h;
  }
  assert(h==241 && D==486);
  const long long wantSlack[6]={541240,2119800,672120,369040,1384240,135600};
  for(int i=0;i<6;++i) assert(slack[i]==wantSlack[i]);
  long long capacity=*min_element(slack.begin(),slack.end()); assert(capacity==135600);

  // B24 exact lattice-preserving cut at the occupied support state.
  Action witness=mk960(579,959); set<pair<int,int>> seen; for(auto&x:old) seen.insert({x.A,x.B});
  assert(!seen.count({579,959}));
  auto [wH,wL]=branches(val[240],witness,486,P0,Q0);
  long long localResidual=min(wH,wL)-val[241][486];
  assert(localResidual==465000); assert(wH-wL==-1517080); assert(localResidual>capacity);

  // Continuation values that certify the adjacent continuous lifted cell used in the written proof.
  assert(val[240][111]==516334240);
  assert(val[240][112]==516231080);
  assert(val[240][880]==197872560);
  assert(val[240][881]==197872560);

  // Add only the structurally derived cut. Exact root gain at old epsilon exceeds the guaranteed bottleneck.
  auto newer=old; newer.push_back(witness); assert(newer.size()==649);
  auto atOld=solve(newer,P0,Q0);
  assert(atOld.fixed_root-atOld.threshold==330800);
  assert(atOld.fixed_root-atOld.threshold>=capacity);

  // Active-face iteration reaches the exact frozen-family critical sensitivity.
  auto [f0,s0]=fixed_face(newer,P0,Q0); assert(f0.C==13355 && f0.S==-385550 && s0==272);
  auto mid=solve(newer,35,16574); assert(mid.fixed_root>mid.threshold);
  auto [fm,sm]=fixed_face(newer,35,16574); assert(fm.C==12946 && fm.S==-190140 && sm==286);
  long long num=fm.C-12480,den=28800-fm.S,g=gcd(num,den); num/=g;den/=g;
  assert(num==233 && den==109470);
  auto crit=solve(newer,num,den);
  assert(crit.first==215 && crit.stable==287 && crit.last==2505 && crit.fixed_root==crit.threshold && crit.first_root==crit.threshold);
  auto [fc,sc]=fixed_face(newer,num,den); assert(fc.C==12946 && fc.S==-190140 && sc==287);

  long long un=9LL*den-10LL*num,ud=10LL*den; g=gcd(un,ud);un/=g;ud/=g; assert(un==9829&&ud==10947);
  long long wn=30LL*un-19LL*ud,wd=30LL*ud; g=gcd(wn,wd);wn/=g;wd/=g; assert(wn==9653&&wd==36490);
  long long impn=12288LL*ud-un*13685LL,impd=13685LL*ud;g=gcd(llabs(impn),impd);impn/=g;impd/=g; assert(impn==6871&&impd==149809695LL);

  cout<<"I0130_B6_B18_B24_TROPICAL_SUPPORT_CUT_PASS\n";
  cout<<"support_prefix="; for(auto [hh,DD]:states) cout<<"("<<hh<<","<<DD<<")"; cout<<" -> (241,486)\n";
  cout<<"support_slacks="; for(size_t i=0;i<slack.size();++i) cout<<(i?",":"")<<slack[i]; cout<<" capacity="<<capacity<<"\n";
  cout<<"witness=579/960,959/960 local_residual_scaled="<<localResidual<<" H_minus_L="<<wH-wL<<"\n";
  cout<<"old_eps_root_gain_scaled="<<atOld.fixed_root-atOld.threshold<<" theorem_bottleneck="<<capacity<<"\n";
  cout<<"new_fixed_face=(12946-190140*eps)/9600\n";
  cout<<"new_critical_eps=233/109470 first_h="<<crit.first<<" stable_h="<<crit.stable<<" last_nonzero_D="<<crit.last<<"\n";
  cout<<"source_valid_upper_bound=9829/10947\n";
  cout<<"width=9653/36490\n";
  cout<<"improvement_over_12288_13685=6871/149809695\n";
  cout<<"checked_states="<<atOld.checked+mid.checked+crit.checked<<"\n";
}
