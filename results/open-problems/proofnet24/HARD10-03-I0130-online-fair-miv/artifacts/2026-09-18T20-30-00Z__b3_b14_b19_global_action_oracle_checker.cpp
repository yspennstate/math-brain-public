#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact checker for B3/B14/B19.
// Gap D is in units 1/240. Actions are a=A/960, b=B/960.
// At epsilon=P/Q Bellman values use integer scale 9600*Q.
struct Action { int A,B,dh,c,m; };
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam651(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959},{586,946},{215,955},{579,959}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  v.push_back(mk960(70,910));
  v.push_back(mk960(527,947));
  assert(v.size()==651); return v;
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
  const int MAXD=2800,H0=198;
  const long long P0=531,Q0=239590;
  auto old=fam651();
  auto oldfix=solve(old,P0,Q0,MAXD,800);
  assert(oldfix.first==198 && oldfix.stable==247 && oldfix.last==2510);
  assert(oldfix.fixed_root==oldfix.threshold);

  // Exact old finite-horizon table through first equality.
  vector<vector<long long>> val(H0+1,vector<long long>(MAXD+1));
  for(int h=1;h<=H0;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(const auto&x:old){ auto [H,L]=branches(val[h-1],x,D,P0,Q0); best=max(best,min(H,L)); }
    val[h][D]=best;
  }
  assert(val[H0][480]==oldfix.threshold);

  // B3/B19: selected unique-tight root-support path to (191,622).
  const int wantD[]={480,872,595,236,189,247,178,622};
  const long long wantSlack[]={417800,3467200,10624600,6897800,18267600,23276000,10895800};
  int h=198,D=480; long long capacity=(1LL<<62);
  for(int step=0;step<7;++step){
    assert(D==wantD[step]); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)old.size();++i){ auto [H,L]=branches(val[h-1],old[i],D,P0,Q0); if(min(H,L)!=best)continue;
      bool unique=((H==best)!=(L==best)); long long s=llabs(H-L);
      if(unique && s>bestSlack){ bestSlack=s; sel=i; sh=H-best; sl=L-best; }
    }
    assert(sel>=0 && bestSlack==wantSlack[step]); capacity=min(capacity,bestSlack);
    const auto&x=old[sel]; D=(sh==0?D+x.dh:abs(D-x.c)); --h;
  }
  assert(h==191 && D==622 && D==wantD[7] && capacity==417800);

  // B14 exact quotient-cell analysis at occupied state (191,622/240).
  // Cell u in [351,352]/240, v in [375,376]/240, chamber b>a, nonreflection.
  // Its candidate corner u=352/240,v=375/240 inverts to (a,b)=(497,957)/960.
  Action z=mk960(497,957); assert(z.c==352 && z.dh==375);
  set<pair<int,int>> existing; for(auto&x:old) existing.insert({x.A,x.B}); assert(!existing.count({497,957}));
  assert(val[190][270]==3814076000LL && val[190][271]==3807879200LL);
  assert(val[190][997]==1431161600LL && val[190][998]==1424385800LL);
  // Continuation slopes: sL=-15492/23959, sH=-33879/47918.
  // Branch derivatives at eps0:
  // Hu=59418/23959>0, Hv=-131205/47918<0,
  // Lu=-113729/47918<0, Lv=118305/47918>0.
  // Hence (H-L)_u=232565/47918>0 and (H-L)_v=-124755/23959<0.
  // So H-L is maximized on the cell at this corner; exact H-L there is negative,
  // proving H binds throughout the cell. Since Hu>0 and Hv<0, the same corner
  // uniquely maximizes the Bellman minimum throughout this whole continuous cell.
  auto [zH,zL]=branches(val[190],z,622,P0,Q0);
  long long local_res=min(zH,zL)-val[191][622];
  assert(local_res==2246000 && zH-zL==-1389800);
  assert(59418>0 && -131205<0 && -113729<0 && 118305>0);
  assert(232565>0 && -124755<0);
  assert(local_res>capacity);

  // Localized tropical gain at (191,622) propagates through the old game by exactly capacity.
  vector<vector<long long>> loc(H0+1,vector<long long>(MAXD+1));
  loc[191][622]=local_res;
  for(int hh=192;hh<=H0;++hh) for(int DD=0;DD<=MAXD;++DD){
    long long oldv=val[hh][DD],bestg=0;
    for(const auto&x:old){ auto [H,L]=branches(val[hh-1],x,DD,P0,Q0); if(min(H,L)!=oldv) continue;
      int DH=DD+x.dh,DL=abs(DD-x.c); long long qH=H-oldv,qL=L-oldv;
      long long gH=DH<=MAXD?loc[hh-1][DH]:0,gL=loc[hh-1][DL];
      bestg=max(bestg,min(qH+gH,qL+gL));
    }
    loc[hh][DD]=bestg;
  }
  assert(loc[198][480]==417800);

  // B3 exact globally-reusable-action gain theorem, finite-horizon certificate.
  // If eta=V'-V, subtracting old V from the enlarged Bellman equation gives exactly
  // eta_h(D)=max(0, max_{A in old U {z}} min_j(q_{A,j}+eta_{h-1}(child_j))).
  // Check this identity for every state through h=198 against a direct augmented DP.
  auto newer=old; newer.push_back(z); assert(newer.size()==652);
  vector<vector<long long>> aug(H0+1,vector<long long>(MAXD+1));
  vector<vector<long long>> eta(H0+1,vector<long long>(MAXD+1));
  long long identity_states=0;
  for(int hh=1;hh<=H0;++hh){
    for(int DD=0;DD<=MAXD;++DD){
      long long augbest=0;
      for(const auto&x:newer){ auto [H,L]=branches(aug[hh-1],x,DD,P0,Q0); augbest=max(augbest,min(H,L)); }
      aug[hh][DD]=augbest;

      long long oldv=val[hh][DD],bestgain=0;
      for(const auto&x:newer){
        auto [H0b,L0b]=branches(val[hh-1],x,DD,P0,Q0);
        int DH=DD+x.dh,DL=abs(DD-x.c);
        long long eH=DH<=MAXD?eta[hh-1][DH]:0,eL=eta[hh-1][DL];
        bestgain=max(bestgain,min(H0b-oldv+eH,L0b-oldv+eL));
      }
      eta[hh][DD]=bestgain;
      assert(aug[hh][DD]-oldv==eta[hh][DD]); ++identity_states;
    }
  }
  assert(eta[198][480]==1092000);

  // Global reuse has a larger stabilized footprint than the single-state localization.
  auto at_old=solve(newer,P0,Q0,MAXD,800);
  assert(at_old.fixed_root-oldfix.fixed_root==4019600);

  // B19: exact new all-horizon critical point for the frozen 652-action family.
  const long long P1=64,Q1=28335;
  auto crit=solve(newer,P1,Q1,MAXD,800);
  assert(crit.first==248 && crit.stable==293 && crit.last==2506);
  assert(crit.first_root==crit.threshold && crit.fixed_root==crit.threshold);
  auto [face,facestable]=fixed_face(newer,P1,Q1,MAXD,800);
  assert(face.C==12992 && face.S==-197880 && facestable==293);
  long long num=face.C-12480,den=28800-face.S,g=gcd(num,den); num/=g; den/=g;
  assert(num==P1 && den==Q1);

  long long un=9LL*Q1-10LL*P1,ud=10LL*Q1; g=gcd(un,ud); un/=g; ud/=g;
  assert(un==10175 && ud==11334);
  long long wn=30LL*un-19LL*ud,wd=30LL*ud; g=gcd(wn,wd); wn/=g; wd/=g;
  assert(wn==7492 && wd==28335);
  long long impn=21510LL*ud-un*23959LL,impd=23959LL*ud; g=gcd(llabs(impn),impd); impn/=g; impd/=g;
  assert(impn==11515 && impd==271551306LL);

  cout<<"I0130_B3_B14_B19_GLOBAL_ACTION_ORACLE_PASS\n";
  cout<<"old_critical_eps=531/239590 old_upper=21510/23959 old_first=198 old_stable=247\n";
  cout<<"support_target=(191,622) ancestor_capacity_scaled="<<capacity<<" local_residual_scaled="<<local_res<<" H_minus_L_scaled="<<zH-zL<<"\n";
  cout<<"continuous_cell=u[351,352]/240_v[375,376]/240 extremizer_action=497/960,957/960\n";
  cout<<"continuation_slopes=sL:-15492/23959,sH:-33879/47918 diff_derivatives=du:232565/47918,dv:-124755/23959\n";
  cout<<"localized_root_gain_scaled="<<loc[198][480]<<" global_action_h198_root_gain_scaled="<<eta[198][480]<<" global_action_fixed_root_gain_scaled="<<at_old.fixed_root-oldfix.fixed_root<<"\n";
  cout<<"global_gain_identity_checked_states="<<identity_states<<"\n";
  cout<<"new_family_size="<<newer.size()<<" new_critical_eps="<<P1<<"/"<<Q1<<" first="<<crit.first<<" stable="<<crit.stable<<" last="<<crit.last<<"\n";
  cout<<"new_fixed_face=(12992-197880*eps)/9600 root_equals_threshold="<<(crit.fixed_root==crit.threshold)<<"\n";
  cout<<"new_upper=10175/11334 new_width=7492/28335 upper_improvement=11515/271551306\n";
  cout<<"source_valid_total_goods_max="<<crit.first+3<<"\n";
}
