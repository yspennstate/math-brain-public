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

// I0130 exact checker for B2/B11/B30.
// Gap D is in units 1/240. Actions are a=A/960, b=B/960.
// At epsilon=P/Q, Bellman values use integer scale 9600*Q.
struct Action { int A,B,dh,c,m; };
static Action mk960(int A,int B){
  assert(0<=A&&A<=960&&0<=B&&B<=960);
  assert((9*A+11*B)%40==0);
  assert((11*A+9*B)%40==0);
  return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam649(){
  vector<Action> v;
  for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
  const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},
    {3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
  for(auto&p:ex) v.push_back(mk960(4*p[0],4*p[1]));
  const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},
    {885,945},{561,941},{419,959},{586,946},{215,955},{579,959}};
  for(auto&p:cut) v.push_back(mk960(p[0],p[1]));
  assert(v.size()==649); return v;
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
  const long long P0=233,Q0=109470; const int H0=215,MAXD=2800;
  auto old=fam649();
  auto oldfix=solve(old,P0,Q0,MAXD,800);
  assert(oldfix.first==215 && oldfix.stable==287 && oldfix.last==2505);
  assert(oldfix.fixed_root==oldfix.threshold);

  vector<vector<long long>> val(H0+1,vector<long long>(MAXD+1));
  for(int h=1;h<=H0;++h) for(int D=0;D<=MAXD;++D){
    long long best=0; for(const auto&x:old){auto [H,L]=branches(val[h-1],x,D,P0,Q0);best=max(best,min(H,L));}
    val[h][D]=best;
  }
  assert(val[H0][480]==oldfix.threshold);

  // B2: exact current root-support scan. Ties occur, but never with two distinct tight children.
  set<pair<int,int>> support; queue<pair<int,int>> qu; support.insert({H0,480}); qu.push({H0,480});
  long long optimal_edges=0,tied_actions=0,distinct_tied_actions=0;
  while(!qu.empty()){
    auto [h,D]=qu.front(); qu.pop(); if(h==0)continue; long long best=val[h][D];
    for(const auto&x:old){
      auto [H,L]=branches(val[h-1],x,D,P0,Q0); if(min(H,L)!=best)continue; ++optimal_edges;
      bool th=(H==best),tl=(L==best); if(th&&tl){++tied_actions; if(D+x.dh!=abs(D-x.c)) ++distinct_tied_actions;}
      if(th){pair<int,int> k={h-1,D+x.dh}; if(k.second<=MAXD&&support.insert(k).second)qu.push(k);}
      if(tl){pair<int,int> k={h-1,abs(D-x.c)}; if(support.insert(k).second)qu.push(k);}
    }
  }
  assert(support.size()==612);
  assert(tied_actions>0);
  assert(distinct_tied_actions==0);
  bool support_has_D316=false; for(auto [h,D]:support) if(D==316) support_has_D316=true;
  assert(!support_has_D316);

  // B11 zero-shadow witness: positive local residual outside the root support, no root movement.
  Action irrelevant=mk960(699,959);
  auto [iH,iL]=branches(oldfix.fixed,irrelevant,316,P0,Q0);
  long long irrelevant_res=min(iH,iL)-oldfix.fixed[316];
  assert(irrelevant_res==5944300 && irrelevant_res>0);
  auto old_plus_irrelevant=old; old_plus_irrelevant.push_back(irrelevant);
  auto ir=solve(old_plus_irrelevant,P0,Q0,MAXD,800);
  assert(ir.fixed_root==ir.threshold);

  // B30 positive-shadow component to (203,1825).
  const int wantD[]={480,106,352,51,398,6,474,873,1218,1505,1763,2034,1825};
  const long long wantSlack[]={1175800,7827300,1557500,181900,4714100,1105200,
    682600,12085100,7436400,2498400,49200,562700};
  int h=215,D=480; long long capacity=(1LL<<62);
  for(int step=0;step<12;++step){
    assert(D==wantD[step]); long long best=val[h][D]; int sel=-1; long long bestSlack=-1,sh=0,sl=0;
    for(int i=0;i<(int)old.size();++i){auto [H,L]=branches(val[h-1],old[i],D,P0,Q0);if(min(H,L)==best){
      long long s=llabs(H-L); if(s>bestSlack){bestSlack=s;sel=i;sh=H-best;sl=L-best;}}}
    assert(sel>=0 && ((sh==0)!=(sl==0))); assert(bestSlack==wantSlack[step]);
    capacity=min(capacity,bestSlack); const auto&x=old[sel]; D=(sh==0?D+x.dh:abs(D-x.c)); --h;
  }
  assert(h==203 && D==1825 && D==wantD[12]); assert(capacity==49200);

  Action witness=mk960(70,910); // (a,b)=(7/96,91/96), (u,v)=(224/240,266/240)
  set<pair<int,int>> existing; for(auto&x:old)existing.insert({x.A,x.B}); assert(!existing.count({70,910}));
  auto [wH,wL]=branches(val[202],witness,1825,P0,Q0);
  long long local_res=min(wH,wL)-val[203][1825];
  assert(local_res==6108500 && wH-wL==-3831900 && local_res>capacity);
  assert(val[202][1601]==201805100);
  assert(val[202][1602]==201278100);
  assert(val[202][2091]==44715200);
  assert(val[202][2092]==42540100);

  auto newer=old; newer.push_back(witness); assert(newer.size()==650);
  vector<long long> p(MAXD+1),c(MAXD+1); long long root215=0;
  for(int hh=1;hh<=215;++hh){for(int DD=0;DD<=MAXD;++DD){long long best=0;for(auto&x:newer){auto [H,L]=branches(p,x,DD,P0,Q0);best=max(best,min(H,L));}c[DD]=best;}p.swap(c);} root215=p[480];
  assert(root215-val[215][480]==1396400);
  assert(root215-val[215][480]>=capacity);

  const long long P1=253,Q1=115870;
  auto crit=solve(newer,P1,Q1,MAXD,800);
  assert(crit.first==300 && crit.stable==411 && crit.last==2509);
  assert(crit.first_root==crit.threshold && crit.fixed_root==crit.threshold);
  auto [fc,sc]=fixed_face(newer,P1,Q1,MAXD,800);
  assert(fc.C==12986 && fc.S==-202940 && sc==411);
  long long num=fc.C-12480,den=28800-fc.S,g=gcd(num,den); num/=g; den/=g;
  assert(num==P1 && den==Q1);

  long long un=9LL*Q1-10LL*P1,ud=10LL*Q1; g=gcd(un,ud);un/=g;ud/=g;
  assert(un==10403 && ud==11587);
  long long wn=30LL*un-19LL*ud,wd=30LL*ud; g=gcd(wn,wd);wn/=g;wd/=g;
  assert(wn==91937 && wd==347610);
  long long impn=9829LL*ud-un*10947LL,impd=10947LL*ud; g=gcd(llabs(impn),impd);impn/=g;impd/=g;
  assert(impn==6982 && impd==126842889LL);

  cout<<"I0130_B2_B11_B30_SHADOW_GLUE_PASS\n";
  cout<<"old_critical_eps=233/109470 old_upper=9829/10947 support_states="<<support.size()
      <<" optimal_edges="<<optimal_edges<<" tied_actions="<<tied_actions
      <<" distinct_tied_actions="<<distinct_tied_actions<<"\n";
  cout<<"abstract_B2_counterexample=one_max_action_two_distinct_tight_children_single_child_gain_does_not_move_min\n";
  cout<<"off_support_cut=699/960,959/960 D=316 positive_residual_scaled="<<irrelevant_res
      <<" augmented_fixed_root_gain="<<ir.fixed_root-ir.threshold<<"\n";
  cout<<"positive_support_path_capacity_scaled="<<capacity<<" target_state=(203,1825)\n";
  cout<<"structural_cut=70/960,910/960 local_residual_scaled="<<local_res
      <<" H_minus_L="<<wH-wL<<" root_h215_gain_scaled="<<root215-val[215][480]<<"\n";
  cout<<"cell_children_low=1601..1602 high=2091..2092\n";
  cout<<"new_fixed_face=(12986-202940*eps)/9600\n";
  cout<<"new_critical_eps=253/115870 first_h="<<crit.first<<" stable_h="<<crit.stable<<" last_nonzero_D="<<crit.last<<"\n";
  cout<<"source_valid_upper_bound=10403/11587 width=91937/347610 improvement=6982/126842889\n";
  cout<<"checked_states="<<oldfix.checked+ir.checked+crit.checked<<"\n";
}
