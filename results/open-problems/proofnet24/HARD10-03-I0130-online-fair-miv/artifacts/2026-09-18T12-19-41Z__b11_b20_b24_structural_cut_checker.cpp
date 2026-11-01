#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <climits>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact self-check for B11/B20/B24 run.
// Baseline delta0=1/10. Gap state is in units 1/240.
// Actions are represented as a=A/960,b=B/960; all selected cuts have
// c=(11a+9b)/10 and dh=(9a+11b)/10 on the 1/240 gap lattice.
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> base638(){
  vector<Action> v;
  for(int i=0;i<=24;++i)for(int j=0;j<=24;++j)v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex)v.push_back(mk960(4*p[0],4*p[1]));
  assert(v.size()==638); return v;
}
static vector<Action> final643(){
  auto v=base638();
  // Five exact lattice-preserving structural cuts selected from Bellman residuals.
  v.push_back(mk960(179,959));
  v.push_back(mk960(613,953));
  v.push_back(mk960(649,949));
  v.push_back(mk960(539,959));
  v.push_back(mk960(775,955));
  assert(v.size()==643); return v;
}

static long long Hterm(const Action& x,long long P,long long Q){
  // (0.9a-eps*m)*9600Q
  return 9LL*x.A*Q-10LL*P*x.m;
}
static long long Lterm(const Action& x,int D,long long P,long long Q){
  // D is in 1/240 units; robust values use scale 9600Q.
  if(D>=x.c) return -11LL*x.A*Q-10LL*P*x.m;
  return 9LL*x.B*Q-40LL*D*Q-10LL*P*x.m;
}

struct Run{int first,stable,last;long long first_root,fixed_root,threshold,checked;};
static Run solve(const vector<Action>& acts,long long P,long long Q,int MAXD=3500,int MAXH=1200){
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  // (13/10+3eps)*9600Q = 12480 Q + 28800 P.
  long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0; // optional stop
      for(const auto& x:acts){
        long long H=Hterm(x,P,Q);
        int DH=D+x.dh; if(DH<=MAXD) H+=prev[DH];
        int DL=abs(D-x.c);
        long long L=Lterm(x,D,P,Q)+prev[DL];
        long long z=min(H,L); if(z>best)best=z;
      }
      cur[D]=best; changed|=(cur[D]!=prev[D]); ++checked;
    }
    prev.swap(cur);
    if(first<0 && prev[480]>=threshold){first=h;first_root=prev[480];}
    if(!changed){stable=h;break;}
  }
  int last=-1;for(int D=0;D<=MAXD;++D)if(prev[D])last=D;
  return {first,stable,last,first_root,prev[480],threshold,checked};
}

// Exact B20 diagnostic: solve the three compression families on the original
// denominator-240 scale and find the strongest missing full638 residual.
struct A24{int A,B,dh,c,m;};
static A24 mk24(int A,int B){assert((B-A)%10==0);return {A,B,(9*A+11*B)/10,(11*A+9*B)/10,max(A,B)};}
static vector<A24> full638_24(){
  vector<A24> a;for(int i=0;i<=24;++i)for(int j=0;j<=24;++j)a.push_back(mk24(10*i,10*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex)a.push_back(mk24(p[0],p[1]));return a;
}
static vector<A24> compressed(int mode){
  vector<A24>a;auto add=[&](int A,int B){a.push_back(mk24(A,B));};
  if(mode==0){for(int A=0;A<=240;A+=10)add(A,240);add(0,0);} 
  else if(mode==1){for(int B=160;B<=240;B+=10)for(int A=0;A<=B;A+=10)add(A,B);add(0,0);} 
  else {for(int B=100;B<=240;B+=10)for(int A=0;A<=B;A+=10)add(A,B);add(0,0);} 
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex)add(p[0],p[1]);
  sort(a.begin(),a.end(),[](auto&x,auto&y){return tie(x.A,x.B)<tie(y.A,y.B);});
  a.erase(unique(a.begin(),a.end(),[](auto&x,auto&y){return x.A==y.A&&x.B==y.B;}),a.end());return a;
}
static vector<long long> fp24(const vector<A24>& acts,int MAXD=3500){
  const long long P=3,Q=1835;vector<long long>p(MAXD+1),q(MAXD+1);
  for(int h=1;h<=1000;++h){bool ch=false;for(int D=0;D<=MAXD;++D){long long best=0;for(auto&x:acts){
    long long H=9LL*x.A*Q-10LL*P*x.m;int DH=D+x.dh;if(DH<=MAXD)H+=p[DH];int DL=abs(D-x.c);
    long long L=(D>=x.c?-11LL*x.A*Q:(9LL*x.B-10LL*D)*Q)-10LL*P*x.m+p[DL];best=max(best,min(H,L));}
    q[D]=best;ch|=q[D]!=p[D];}p.swap(q);if(!ch)return p;}assert(false);return p;
}
static tuple<long long,int,int,int> strongest_missing_residual(int mode){
  const long long P=3,Q=1835;auto psi=fp24(compressed(mode));auto full=full638_24();
  long long best=LLONG_MIN;int bD=-1,bA=-1,bB=-1;
  for(int D=0;D<=3000;++D)for(auto&x:full){long long H=9LL*x.A*Q-10LL*P*x.m;int DH=D+x.dh;if(DH<(int)psi.size())H+=psi[DH];int DL=abs(D-x.c);long long L=(D>=x.c?-11LL*x.A*Q:(9LL*x.B-10LL*D)*Q)-10LL*P*x.m+psi[DL];long long r=min(H,L)-psi[D];if(r>best){best=r;bD=D;bA=x.A;bB=x.B;}}
  return {best,bD,bA,bB};
}

static tuple<long long,int,int,int> strongest_aligned_vertex_cut(){
  // Against the exact 638-action fixed point at eps=3/1835, search every
  // action whose two child shifts are grid breakpoints: c=k/240, dh=l/240.
  // Solving the two linear equations gives a=A/960,b=B/960 with
  // A=11k-9l, B=-9k+11l. This is a structural breakpoint-vertex family,
  // not a uniform action mesh.
  const long long P=3,Q=1835;
  auto phi=fp24(full638_24());
  assert(phi[1347]==1429745);
  assert(phi[1081]==2400975);
  assert(phi[1651]==750305 && phi[1652]==750305);
  long long best=LLONG_MIN; int bD=-1,bA=-1,bB=-1;
  for(int D=0;D<=3000;++D){
    long long ph=4*phi[D]; // lift from scale 2400Q to 9600Q
    for(int k=0;k<=480;++k)for(int l=0;l<=480;++l){
      int A=11*k-9*l, B=-9*k+11*l;
      if(A<0||A>960||B<0||B>960)continue;
      int m=max(A,B);
      long long H=9LL*A*Q-10LL*P*m + 4*phi[D+l];
      int DL=abs(D-k);
      long long L=(D>=k ? -11LL*A*Q : 9LL*B*Q-40LL*D*Q)-10LL*P*m + 4*phi[DL];
      long long r=min(H,L)-ph;
      if(r>best){best=r;bD=D;bA=A;bB=B;}
    }
  }
  return {best,bD,bA,bB};
}

int main(){
  // B24 finite-core metric certificate at eps=377/200000.
  auto run=solve(final643(),377,200000);
  assert(run.first==221);
  assert(run.first_root-run.threshold==9080);
  assert(run.first_root>=run.threshold);
  assert(run.stable>0);

  // Source endpoint: delta=1/10+377/200000=20377/200000, U=179623/200000.
  long long un=179623,ud=200000;
  long long wn=un*30-19LL*ud,wd=ud*30,g=gcd(wn,wd);wn/=g;wd/=g;
  assert(wn==158869 && wd==600000);
  long long oldn=3297,oldd=3670;
  long long in=oldn*ud-un*oldd,id=oldd*ud;g=gcd(in,id);in/=g;id/=g;
  assert(in==18359 && id==73400000);

  // B24 exact breakpoint-vertex separation diagnostic.
  auto [rv,dv,av,bv]=strongest_aligned_vertex_cut();
  assert(rv==211375 && dv==1348 && av==179 && bv==959);

  // B20 exact compression obstruction diagnostics.
  auto [r0,d0,a0,b0]=strongest_missing_residual(0);
  auto [r1,d1,a1,b1]=strongest_missing_residual(1);
  auto [r2,d2,a2,b2]=strongest_missing_residual(2);
  assert(r0==101110 && d0==1315 && a0==40 && b0==220);
  assert(r1==30880 && d1==163 && a1==10 && b1==10);
  assert(r2==30375 && d2==164 && a2==10 && b2==10);

  cout<<"I0130_B11_B20_B24_STRUCTURAL_CUT_PASS\n";
  cout<<"final_action_family_size=643\n";
  cout<<"certified_epsilon=377/200000\n";
  cout<<"first_threshold_cross_h="<<run.first<<"\n";
  cout<<"first_cross_excess_scaled="<<run.first_root-run.threshold<<"\n";
  cout<<"fixed_point_stable_h="<<run.stable<<"\n";
  cout<<"fixed_point_last_nonzero_gap_units="<<run.last<<"\n";
  cout<<"source_valid_upper_bound=179623/200000\n";
  cout<<"width=158869/600000\n";
  cout<<"improvement_over_3297_3670=18359/73400000\n";
  cout<<"aligned_vertex_max_residual_scaled="<<rv<<" at_D="<<dv<<" action="<<av<<","<<bv<<"\n";
  cout<<"compression39_max_missing_residual="<<r0<<" at_D="<<d0<<" action="<<a0<<","<<b0<<"\n";
  cout<<"compression203_max_missing_residual="<<r1<<" at_D="<<d1<<" action="<<a1<<","<<b1<<"\n";
  cout<<"compression284_max_missing_residual="<<r2<<" at_D="<<d2<<" action="<<a2<<","<<b2<<"\n";
  cout<<"checked_final_states="<<run.checked<<"\n";
}
