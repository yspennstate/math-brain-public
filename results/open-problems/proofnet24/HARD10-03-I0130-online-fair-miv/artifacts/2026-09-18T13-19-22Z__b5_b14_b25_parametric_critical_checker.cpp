#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// I0130 exact self-check for the B5/B14/B25 run.
// Baseline delta0=1/10. Gap state D is in units 1/240.
// Actions are represented as a=A/960,b=B/960; the frozen 643-action family
// is the Q=24 square, 13 earlier cuts, and 5 structural cuts from the prior run.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> final643(){
  vector<Action> v;
  for(int i=0;i<=24;++i)for(int j=0;j<=24;++j)v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex)v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955}};
  for(auto&p:cut)v.push_back(mk960(p[0],p[1]));
  assert(v.size()==643); return v;
}

struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked;};
static Run solve(long long P,long long Q,int MAXD=2700,int MAXH=700){
  auto acts=final643();
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  // Robust values are scaled by 9600 Q.  Threshold is
  // (13/10+3 eps)*9600 Q = 12480 Q + 28800 P.
  const long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0; // optional stop
      for(const auto& x:acts){
        long long H=9LL*x.A*Q-10LL*P*x.m;
        const int DH=D+x.dh; if(DH<=MAXD) H+=prev[DH];
        const int DL=abs(D-x.c);
        long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)
                    -10LL*P*x.m + prev[DL];
        best=max(best,min(H,L));
      }
      cur[D]=best; changed|=(cur[D]!=prev[D]); ++checked;
    }
    prev.swap(cur);
    if(first<0 && prev[480]>=threshold){first=h;first_root=prev[480];}
    if(!changed){stable=h;break;}
  }
  int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
  return {first,stable,last,first_root,prev[480],threshold,checked};
}

int main(){
  // B5 symbolic active-face critical price for the frozen 643-action family.
  // The active root affine face near the critical point is
  //   R(2)=(13749-643010 eps)/9600.
  // Solving R(2)=13/10+3 eps gives eps=1269/671810 exactly.
  const long long P=1269,Q=671810;
  static_assert(13749-12480==1269);
  static_assert(643010+28800==671810);
  assert(gcd(P,Q)==1);

  auto r=solve(P,Q);
  assert(r.first==293);
  assert(r.stable==367);
  assert(r.first_root==r.threshold);
  assert(r.fixed_root==r.threshold);
  assert(r.last==2522);

  // Source endpoint: delta=1/10+eps, so U=9/10-eps=60336/67181.
  long long un=9LL*Q-10LL*P,ud=10LL*Q,g=gcd(un,ud); un/=g;ud/=g;
  assert(un==60336 && ud==67181);
  long long wn=un*30-19LL*ud,wd=ud*30; g=gcd(wn,wd); wn/=g;wd/=g;
  assert(wn==533641 && wd==2015430);
  long long oldn=179623,oldd=200000;
  long long in=oldn*ud-un*oldd,id=oldd*ud; g=gcd(in,id); in/=g;id/=g;
  assert(in==52763 && id==13436200000LL);

  // B14 coordinate identities used in the report.  For
  // u=(11a+9b)/10 and v=(9a+11b)/10,
  // a=(11u-9v)/4, b=(-9u+11v)/4 and a-b=5(u-v).
  // Integer-scaled spot checks cover both action orders.
  for(const auto& x:final643()){
    const long long U=11LL*x.A+9LL*x.B;
    const long long V=9LL*x.A+11LL*x.B;
    assert(11*U-9*V==40LL*x.A);
    assert(-9*U+11*V==40LL*x.B);
    assert(U-V==2LL*(x.A-x.B));
  }

  cout<<"I0130_B5_B14_B25_PARAMETRIC_CRITICAL_PASS\n";
  cout<<"action_family_size=643\n";
  cout<<"critical_epsilon=1269/671810\n";
  cout<<"active_root_face=(13749-643010*epsilon)/9600\n";
  cout<<"first_threshold_cross_h="<<r.first<<"\n";
  cout<<"first_cross_excess_scaled="<<r.first_root-r.threshold<<"\n";
  cout<<"fixed_point_stable_h="<<r.stable<<"\n";
  cout<<"fixed_point_root_minus_threshold="<<r.fixed_root-r.threshold<<"\n";
  cout<<"fixed_point_last_nonzero_gap_units="<<r.last<<"\n";
  cout<<"source_valid_upper_bound=60336/67181\n";
  cout<<"width=533641/2015430\n";
  cout<<"improvement_over_179623_200000=52763/13436200000\n";
  cout<<"checked_states="<<r.checked<<"\n";
}
