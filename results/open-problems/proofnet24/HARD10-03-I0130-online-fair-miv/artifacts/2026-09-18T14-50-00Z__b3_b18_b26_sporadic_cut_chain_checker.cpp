#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// I0130 exact checker for the B3/B18/B26 run.
// Baseline delta0=1/10. Gap state D is measured in 1/240 units.
// Actions use a=A/960,b=B/960 and all stored cuts preserve the gap lattice.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> base643(){
  vector<Action> v;
  for(int i=0;i<=24;++i)for(int j=0;j<=24;++j)v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex)v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955}};
  for(auto&p:cut)v.push_back(mk960(p[0],p[1]));
  assert(v.size()==643); return v;
}
static vector<Action> fam(int n){
  auto v=base643();
  if(n>=644)v.push_back(mk960(885,945)); // 59/64,63/64; from cell at D=66/240
  if(n>=645)v.push_back(mk960(561,941)); // from cell at D=506/240
  if(n>=646)v.push_back(mk960(419,959)); // from cell at D=770/240
  if(n>=647)v.push_back(mk960(699,959)); // positive residual but no root movement
  assert((int)v.size()==n); return v;
}

struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long> fixed;};
static Run solve(const vector<Action>& acts,long long P,long long Q,int MAXD=2700,int MAXH=700){
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  const long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0;
      for(const auto& x:acts){
        long long H=9LL*x.A*Q-10LL*P*x.m;
        int DH=D+x.dh; if(DH<=MAXD) H+=prev[DH];
        int DL=abs(D-x.c);
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
  return {first,stable,last,first_root,prev[480],threshold,checked,prev};
}
static long long residual(const vector<long long>& phi,const Action& x,int D,long long P,long long Q){
  long long H=9LL*x.A*Q-10LL*P*x.m+phi[D+x.dh];
  int DL=abs(D-x.c);
  long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)
              -10LL*P*x.m+phi[DL];
  return min(H,L)-phi[D];
}
static void exact_critical(const Run&r){
  assert(r.first>0 && r.stable>0 && r.first_root==r.threshold && r.fixed_root==r.threshold);
}
int main(){
  auto r643=solve(fam(643),1269,671810); exact_critical(r643);
  assert(r643.first==293 && r643.stable==367 && r643.last==2522);
  Action c1=mk960(885,945); assert(c1.dh==459&&c1.c==456);
  long long e1=residual(r643.fixed,c1,66,1269,671810);
  assert(e1==49677400LL);

  auto r644=solve(fam(644),173,91570); exact_critical(r644);
  assert(r644.first==292 && r644.stable==355 && r644.last==2522);
  Action c2=mk960(561,941); assert(c2.dh==385&&c2.c==366);
  long long e2=residual(r644.fixed,c2,506,173,91570);
  assert(e2==9211000LL);

  auto r645=solve(fam(645),1069,556010); exact_critical(r645);
  assert(r645.first==262 && r645.stable==303 && r645.last==2517);
  Action c3=mk960(419,959); assert(c3.dh==358&&c3.c==331);
  long long e3=residual(r645.fixed,c3,770,1069,556010);
  assert(e3==47141800LL);

  auto r646=solve(fam(646),227,113830); exact_critical(r646);
  assert(r646.first==201 && r646.stable==241 && r646.last==2511);

  Action c4=mk960(699,959); assert(c4.dh==421&&c4.c==408);
  long long e4=residual(r646.fixed,c4,316,227,113830);
  assert(e4==8540400LL);
  auto r647=solve(fam(647),227,113830); exact_critical(r647);
  assert(r647.first==197 && r647.stable==236 && r647.fixed_root==r646.fixed_root);

  long long un=9LL*113830-10LL*227,ud=10LL*113830,g=gcd(un,ud);un/=g;ud/=g;
  assert(un==10222 && ud==11383);
  long long wn=un*30-19LL*ud,wd=ud*30;g=gcd(wn,wd);wn/=g;wd/=g;
  assert(wn==90383 && wd==341490);
  long long in=60336LL*ud-un*67181LL,id=67181LL*ud;g=gcd(in,id);in/=g;id/=g;
  assert(in==80506 && id==764721323LL);

  cout<<"I0130_B3_B18_B26_SPORADIC_CUT_CHAIN_PASS\n";
  cout<<"cut1=885/960,945/960 residual_scaled="<<e1<<" parent_D=66\n";
  cout<<"critical_644=173/91570 first_h="<<r644.first<<" stable_h="<<r644.stable<<"\n";
  cout<<"cut2=561/960,941/960 residual_scaled="<<e2<<" parent_D=506\n";
  cout<<"critical_645=1069/556010 first_h="<<r645.first<<" stable_h="<<r645.stable<<"\n";
  cout<<"cut3=419/960,959/960 residual_scaled="<<e3<<" parent_D=770\n";
  cout<<"critical_646=227/113830 first_h="<<r646.first<<" stable_h="<<r646.stable<<"\n";
  cout<<"final_fixed_point_last_nonzero_gap_units="<<r646.last<<"\n";
  cout<<"cut4_nonmoving=699/960,959/960 residual_scaled="<<e4<<" parent_D=316\n";
  cout<<"cut4_augmented_first_h="<<r647.first<<" stable_h="<<r647.stable<<" root_unchanged=1\n";
  cout<<"source_valid_upper_bound=10222/11383\n";
  cout<<"width=90383/341490\n";
  cout<<"improvement_over_60336_67181=80506/764721323\n";
  cout<<"checked_states="<<r643.checked+r644.checked+r645.checked+r646.checked+r647.checked<<"\n";
}
