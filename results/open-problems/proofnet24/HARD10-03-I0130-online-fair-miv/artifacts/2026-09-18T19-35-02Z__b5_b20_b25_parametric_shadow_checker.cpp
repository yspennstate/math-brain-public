#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact checker for B5/B20/B25.
// Gap D is in units 1/240. Actions are a=A/960, b=B/960.
// At epsilon=P/Q Bellman values use integer scale 9600*Q.
struct Action { int A,B,dh,c,m; };
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam650(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959},{586,946},{215,955},{579,959}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  v.push_back(mk960(70,910));
  assert(v.size()==650); return v;
}
static pair<long long,long long> branches(const vector<long long>&prev,const Action&x,int D,long long P,long long Q){
  long long H=9LL*x.A*Q-10LL*P*x.m;
  int DH=D+x.dh; if(DH<(int)prev.size()) H+=prev[DH];
  int DL=abs(D-x.c);
  long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+prev[DL];
  return {H,L};
}
struct Run { int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long> fixed; };
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=800){
  vector<long long> prev(MAXD+1),cur(MAXD+1);
  const long long threshold=12480LL*Q+28800LL*P;
  int first=-1,stable=-1; long long first_root=-1,checked=0;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      long long best=0;
      for(const auto&x:acts){ auto [H,L]=branches(prev,x,D,P,Q); best=max(best,min(H,L)); }
      cur[D]=best; changed|=(cur[D]!=prev[D]); ++checked;
    }
    prev.swap(cur);
    if(first<0 && prev[480]>=threshold){ first=h; first_root=prev[480]; }
    if(!changed){ stable=h; break; }
  }
  int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
  return {first,stable,last,first_root,prev[480],threshold,checked,prev};
}
struct Face { long long C,S; };
static __int128 fv(Face f,long long P,long long Q){ return (__int128)f.C*Q+(__int128)f.S*P; }
static Face minR(Face a,Face b,long long P,long long Q){
  auto A=fv(a,P,Q),B=fv(b,P,Q); if(A<B)return a; if(B<A)return b; return a.S<b.S?a:b;
}
static Face maxR(Face a,Face b,long long P,long long Q){
  auto A=fv(a,P,Q),B=fv(b,P,Q); if(A>B)return a; if(B>A)return b; return a.S>b.S?a:b;
}
static pair<Face,int> fixed_face(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=800){
  vector<Face> prev(MAXD+1,{0,0}),cur(MAXD+1); int stable=-1;
  for(int h=1;h<=MAXH;++h){
    bool changed=false;
    for(int D=0;D<=MAXD;++D){
      Face best{0,0};
      for(const auto&x:acts){
        int DH=D+x.dh; Face ch=DH<=MAXD?prev[DH]:Face{0,0};
        Face H{ch.C+9LL*x.A,ch.S-10LL*x.m};
        int DL=abs(D-x.c); Face cl=prev[DL];
        long long base=(D>=x.c ? -11LL*x.A : 9LL*x.B-40LL*D);
        Face L{cl.C+base,cl.S-10LL*x.m};
        best=maxR(best,minR(H,L,P,Q),P,Q);
      }
      cur[D]=best; changed|=(cur[D].C!=prev[D].C||cur[D].S!=prev[D].S);
    }
    prev.swap(cur); if(!changed){ stable=h; break; }
  }
  return {prev[480],stable};
}

int main(){
  const long long P0=253,Q0=115870; const int H0=300,MAXD=2800;
  auto old=fam650();
  auto oldfix=solve(old,P0,Q0,MAXD,800);
  assert(oldfix.first==300 && oldfix.stable==411 && oldfix.last==2509);
  assert(oldfix.fixed_root==oldfix.threshold);

  // Exact finite-horizon table at the old first-equality horizon.
  vector<vector<long long>> val(H0+1,vector<long long>(MAXD+1));
  for(int h=1;h<=H0;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(const auto&x:old){ auto [H,L]=branches(val[h-1],x,D,P0,Q0); best=max(best,min(H,L)); }
    val[h][D]=best;
  }
  assert(val[H0][480]==oldfix.threshold);

  // B5: selected root-support prefix and its exact bottleneck.
  const int wantD[]={480,106,352,51,502,887,572};
  const long long wantSlack[]={910700,8267700,1205800,5600,8473000,6466800};
  int h=300,D=480; long long capacity=(1LL<<62);
  for(int step=0;step<6;++step){
    assert(D==wantD[step]); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)old.size();++i){ auto [H,L]=branches(val[h-1],old[i],D,P0,Q0); if(min(H,L)!=best)continue;
      long long s=llabs(H-L); bool unique=((H==best)!=(L==best)); if(unique && s>bestSlack){bestSlack=s;sel=i;sh=H-best;sl=L-best;}
    }
    assert(sel>=0 && bestSlack==wantSlack[step]); capacity=min(capacity,bestSlack);
    const auto&x=old[sel]; D=(sh==0?D+x.dh:abs(D-x.c)); --h;
  }
  assert(h==294 && D==572 && D==wantD[6] && capacity==5600);

  // Exact affine bottleneck at state (297,51), action (880,920): q(eps)=(2648-1212720 eps)/9600.
  vector<Face> fp(MAXD+1,{0,0}),fc(MAXD+1);
  for(int hh=1;hh<=296;++hh){
    for(int DD=0;DD<=MAXD;++DD){
      Face best{0,0}; for(const auto&x:old){
        int DH=DD+x.dh; Face ch=DH<=MAXD?fp[DH]:Face{0,0}; Face H{ch.C+9LL*x.A,ch.S-10LL*x.m};
        int DL=abs(DD-x.c); Face cl=fp[DL]; long long base=(DD>=x.c?-11LL*x.A:9LL*x.B-40LL*DD); Face L{cl.C+base,cl.S-10LL*x.m};
        best=maxR(best,minR(H,L,P0,Q0),P0,Q0);
      } fc[DD]=best;
    } fp.swap(fc);
  }
  Action bott=mk960(880,920); int BD=51; int BDH=BD+bott.dh, BDL=abs(BD-bott.c);
  Face BH{fp[BDH].C+9LL*bott.A,fp[BDH].S-10LL*bott.m};
  long long bbase=(BD>=bott.c?-11LL*bott.A:9LL*bott.B-40LL*BD);
  Face BL{fp[BDL].C+bbase,fp[BDL].S-10LL*bott.m};
  assert(BL.C-BH.C==2648 && BL.S-BH.S==-1212720);
  assert((BL.C-BH.C)*Q0+(BL.S-BH.S)*P0==5600);
  long long tg=gcd(2648LL,1212720LL); assert(2648/tg==331 && 1212720/tg==151590);
  // turnoff minus eps0 = 7/175647333
  long long dn=331LL*115870-253LL*151590, dd=151590LL*115870, dg=gcd(llabs(dn),dd); dn/=dg; dd/=dg;
  assert(dn==7 && dd==175647333LL);

  // B5 exact continuous occupied cell at state (294,572), h-1=293.
  // Cell: u in [357,358]/240, v in [379,380]/240 intersect legal actions.
  // Candidate corner u=358/240, v=379/240 => (a,b)=(527,947)/960.
  assert(val[293][214]==1973084100LL && val[293][215]==1970488700LL);
  assert(val[293][951]==750708900LL && val[293][952]==750708900LL);
  Action witness=mk960(527,947); assert(witness.c==358 && witness.dh==379);
  set<pair<int,int>> existing; for(auto&x:old) existing.insert({x.A,x.B}); assert(!existing.count({527,947}));
  auto [wH,wL]=branches(val[293],witness,572,P0,Q0);
  long long local_res=min(wH,wL)-val[294][572];
  assert(local_res==6622300 && wH-wL==-1105400 && local_res>capacity);
  // Continuation slopes and branch derivatives at eps0.
  // sL=-12977/23174, sH=0;
  // Hu=114939/46348>0, Hv=-94133/46348<0;
  // Lu=-114021/46348<0, Lv=114433/46348>0;
  // hence (H-L)_u=57240/11587>0 and (H-L)_v=-9/2<0.
  // Since H-L is maximized at (u,v)=(358,379)/240 and is negative there,
  // H is binding throughout the legal cell; H is uniquely maximized at this corner.
  assert(114939>0 && -94133<0 && -114021<0 && 114433>0);
  assert(57240>0);
  // Parametric residual face against the old state face is (57+70 eps)/9600.
  // Candidate H/L switch on these local affine faces is eps=108/48370.
  assert(57LL*Q0+70LL*P0==local_res);
  long long sg=gcd(432LL,193480LL); assert(432/sg==54 && 193480/sg==24185);

  // B25: localized tropical propagation through old optimal actions.
  // A perturbation only at (294,572) propagates exactly 5600 to the old root.
  vector<vector<long long>> gain(H0+1,vector<long long>(MAXD+1));
  gain[294][572]=local_res;
  for(int hh=295;hh<=H0;++hh) for(int DD=0;DD<=MAXD;++DD){
    long long oldv=val[hh][DD],bestgain=0;
    for(const auto&x:old){ auto [H,L]=branches(val[hh-1],x,DD,P0,Q0); if(min(H,L)!=oldv)continue;
      int DH=DD+x.dh,DL=abs(DD-x.c); long long qH=H-oldv,qL=L-oldv;
      long long gH=DH<=MAXD?gain[hh-1][DH]:0,gL=gain[hh-1][DL];
      bestgain=max(bestgain,min(qH+gH,qL+gL));
    }
    gain[hh][DD]=bestgain;
  }
  assert(gain[300][480]==5600);

  // Add the single continuous-cell extremizer. Global reuse of the same action at all states gives a much larger root gain.
  auto newer=old; newer.push_back(witness); assert(newer.size()==651);
  auto at_old=solve(newer,P0,Q0,MAXD,800);
  assert(at_old.fixed_root-at_old.threshold==6671200);

  // Exact new all-horizon critical epsilon and source endpoint for the frozen 651-action family.
  const long long P1=531,Q1=239590;
  auto crit=solve(newer,P1,Q1,MAXD,800);
  assert(crit.first==198 && crit.stable==247 && crit.last==2510);
  assert(crit.first_root==crit.threshold && crit.fixed_root==crit.threshold);
  auto [face,facestable]=fixed_face(newer,P1,Q1,MAXD,800);
  assert(face.C==13011 && face.S==-210790 && facestable==247);
  long long num=face.C-12480,den=28800-face.S,g=gcd(num,den); num/=g; den/=g;
  assert(num==P1 && den==Q1);

  long long un=9LL*Q1-10LL*P1,ud=10LL*Q1; g=gcd(un,ud); un/=g; ud/=g;
  assert(un==21510 && ud==23959);
  long long wn=30LL*un-19LL*ud,wd=30LL*ud; g=gcd(wn,wd); wn/=g; wd/=g;
  assert(wn==190079 && wd==718770);
  long long impn=10403LL*ud-un*11587LL,impd=11587LL*ud; g=gcd(llabs(impn),impd); impn/=g; impd/=g;
  assert(impn==9107 && impd==277612933LL);

  cout<<"I0130_B5_B20_B25_PARAMETRIC_SHADOW_PASS\n";
  cout<<"old_critical_eps=253/115870 old_upper=10403/11587 old_first=300 old_stable=411\n";
  cout<<"selected_support_target=(294,572) path_capacity_scaled="<<capacity<<"\n";
  cout<<"bottleneck_q=(2648-1212720*eps)/9600 turnoff_eps=331/151590 turnoff_minus_old_eps=7/175647333\n";
  cout<<"continuous_cell=u[357,358]/240_v[379,380]/240_intersect_legal extremizer_action=527/960,947/960\n";
  cout<<"local_residual_scaled="<<local_res<<" H_minus_L_scaled="<<wH-wL<<" residual_face=(57+70*eps)/9600 branch_switch_eps=54/24185\n";
  cout<<"localized_tropical_root_gain_scaled="<<gain[300][480]<<" global_action_fixed_root_gain_at_old_eps="<<at_old.fixed_root-at_old.threshold<<"\n";
  cout<<"new_fixed_face=(13011-210790*eps)/9600 new_critical_eps=531/239590 first_h="<<crit.first<<" stable_h="<<crit.stable<<" last_nonzero_D="<<crit.last<<"\n";
  cout<<"source_valid_upper_bound=21510/23959 width=190079/718770 improvement=9107/277612933\n";
  cout<<"checked_states="<<oldfix.checked+at_old.checked+crit.checked<<"\n";
}
