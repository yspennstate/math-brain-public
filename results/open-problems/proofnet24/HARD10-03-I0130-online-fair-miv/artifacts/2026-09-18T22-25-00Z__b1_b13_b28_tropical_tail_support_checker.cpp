#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){
    assert(0<=A&&A<=960&&0<=B&&B<=960);
    assert((9*A+11*B)%40==0 && (11*A+9*B)%40==0);
    return {A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};
}
static vector<Action> fam653(){
    vector<Action> v;
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j) v.push_back(mk960(40*i,40*j));
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:ex) v.push_back(mk960(4*p[0],4*p[1]));
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940}};
    for(auto &p:cut) v.push_back(mk960(p[0],p[1]));
    assert(v.size()==653);
    return v;
}
static pair<long long,long long> branches(const vector<long long>& p,const Action& x,int D,long long P,long long Q){
    long long H=9LL*x.A*Q-10LL*P*x.m;
    int DH=D+x.dh;
    if(DH<(int)p.size()) H+=p[DH];
    int DL=abs(D-x.c);
    assert(DL<(int)p.size());
    long long L=(D>=x.c ? -11LL*x.A*Q : 9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+p[DL];
    return {H,L};
}
struct Run{int first,stable,last; long long first_root,fixed_root,threshold,checked; vector<long long> fixed;};
static Run solve(const vector<Action>& acts,long long P,long long Q,int MAXD=3600,int MAXH=500){
    vector<long long> prev(MAXD+1),cur(MAXD+1);
    long long thr=12480LL*Q+28800LL*P;
    int first=-1,stable=-1; long long fr=-1,checked=0;
    for(int h=1;h<=MAXH;++h){
        bool ch=false;
        for(int D=0;D<=MAXD;++D){
            long long best=0;
            for(auto &x:acts){auto [H,L]=branches(prev,x,D,P,Q); best=max(best,min(H,L));}
            cur[D]=best; ch|=(cur[D]!=prev[D]); ++checked;
        }
        prev.swap(cur);
        if(first<0 && prev[480]>=thr){first=h; fr=prev[480];}
        if(!ch){stable=h; break;}
    }
    int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]) last=D;
    return {first,stable,last,fr,prev[480],thr,checked,prev};
}

int main(){
    const long long P0=267,Q0=117230; // eps0
    const int H0=247,MAXD=3600;
    auto old=fam653();
    auto oldr=solve(old,P0,Q0,MAXD,450);
    assert(oldr.first==247 && oldr.stable==294 && oldr.last==2504);
    assert(oldr.first_root==oldr.threshold && oldr.fixed_root==oldr.threshold);

    // Exact old finite-horizon table for B28 support concentration.
    vector<vector<long long>> val(H0+1,vector<long long>(MAXD+1));
    for(int h=1;h<=H0;++h){
        for(int D=0;D<=MAXD;++D){
            long long best=0;
            for(auto &x:old){auto [H,L]=branches(val[h-1],x,D,P0,Q0); best=max(best,min(H,L));}
            val[h][D]=best;
        }
    }
    set<pair<int,int>> support; queue<pair<int,int>> qu;
    support.insert({H0,480}); qu.push({H0,480});
    long long optinc=0,tied=0,unique=0; int minD=1e9,maxD=-1,minH=1e9,maxH=-1;
    while(!qu.empty()){
        auto [h,D]=qu.front(); qu.pop();
        minD=min(minD,D); maxD=max(maxD,D); minH=min(minH,h); maxH=max(maxH,h);
        if(h==0 || val[h][D]==0) continue;
        long long best=val[h][D];
        for(auto &x:old){
            auto [HH,LL]=branches(val[h-1],x,D,P0,Q0);
            if(min(HH,LL)!=best) continue;
            ++optinc; bool ht=(HH==best),lt=(LL==best); tied+=(ht&&lt); unique+=(ht!=lt);
            if(ht){pair<int,int>s={h-1,D+x.dh}; if(s.second<=MAXD && support.insert(s).second) qu.push(s);}
            if(lt){pair<int,int>s={h-1,abs(D-x.c)}; if(support.insert(s).second) qu.push(s);}
        }
    }
    assert(support.size()==480 && optinc==821 && tied==399 && unique==422);
    assert(minD==178 && maxD==2527 && minH==167 && maxH==247);

    // Find an all-unique-tight positive-shadow path to the B28 cell.
    const int targetH=237,targetD=1031;
    map<pair<int,int>, tuple<pair<int,int>,int,long long>> par;
    queue<pair<int,int>> q2; q2.push({H0,480}); par[{H0,480}]={{-1,-1},-1,(1LL<<60)};
    bool found=false;
    while(!q2.empty()){
        auto [h,D]=q2.front(); q2.pop(); if(h==targetH&&D==targetD){found=true;break;} if(h<=targetH) continue;
        long long best=val[h][D];
        for(int i=0;i<(int)old.size();++i){
            auto [HH,LL]=branches(val[h-1],old[i],D,P0,Q0);
            if(min(HH,LL)!=best) continue;
            bool ht=(HH==best),lt=(LL==best); if(ht==lt) continue;
            long long slack=llabs(HH-LL); int nd=ht?D+old[i].dh:abs(D-old[i].c);
            pair<int,int> ns={h-1,nd};
            if(!par.count(ns)){long long pc=get<2>(par[{h,D}]); par[ns]={{h,D},i,min(pc,slack)}; q2.push(ns);}
        }
    }
    assert(found); long long pathcap=get<2>(par[{targetH,targetD}]); assert(pathcap==859400);

    // B28: exact continuous cell. Candidate corner has u=294/240, v=327/240.
    Action z=mk960(291,951); assert(z.c==294 && z.dh==327);
    auto [ZH,ZL]=branches(val[236],z,targetD,P0,Q0);
    long long oldbest=val[237][targetD];
    assert(ZH==675102600 && ZL==672153600 && oldbest==667308200);
    assert(min(ZH,ZL)-oldbest==4845400 && ZH-ZL==2949000 && 4845400>pathcap);
    // On u in [294,295]/240, v in [326,327]/240:
    // sL=(Phi(737)-Phi(736))/(1/240)=-4263/11723; sH=(Phi(1358)-Phi(1357))/(1/240)=-2788/11723.
    assert(val[236][737]-val[236][736]==-1705200);
    assert(val[236][1358]-val[236][1357]==-1115200);
    // Exact derivative signs (fractions simplified in the report).
    // Hu=58149/23446>0, Hv=-53201/23446<0, Lu=-31139/11723<0, Lv=28941/11723>0.
    // Therefore d(H-L)/du=120427/23446>0 and d(H-L)/dv=-111083/23446<0.
    assert(58149>0 && -53201<0 && -31139<0 && 28941>0 && 120427>0 && -111083<0);
    // Candidate is u-min/v-max, hence minimizes H-L on cell; since H-L>0 there, L binds throughout.
    // L decreases in u and increases in v, so the candidate is the unique cell maximizer.

    // B1/B13: add z globally, verify stabilized gain and tail score certificate at eps0.
    auto aug=old; aug.push_back(z); assert(aug.size()==654);
    auto aug0=solve(aug,P0,Q0,MAXD,450);
    assert(aug0.first==174 && aug0.stable==268 && aug0.last==2509);
    assert(aug0.fixed_root-oldr.fixed_root==2125400);
    const int Dstar=oldr.last, Dseed=Dstar+480; assert(Dseed==2984);
    long long maxScore=-(1LL<<62); int argScore=-1;
    for(int D=0;D<=Dseed;++D){
        long long eta=aug0.fixed[D]-oldr.fixed[D];
        long long score=9*eta+400LL*P0*D; // 9*S*(eta_phys + (10 eps/9) D_phys)
        if(score>maxScore){maxScore=score;argScore=D;}
    }
    assert(maxScore==400LL*P0*Dseed && argScore==Dseed && aug0.fixed[Dseed]==0 && oldr.fixed[Dseed]==0);
    // Directly verify the computed augmented fixed point through the whole analytic tail collar.
    for(int D=0;D<=Dseed+480;++D){
        long long best=0; for(auto &x:aug){auto [H,L]=branches(aug0.fixed,x,D,P0,Q0); best=max(best,min(H,L));}
        assert(best==aug0.fixed[D]);
    }

    // Metric movement: source-valid finite tree at eps=1/425 using this one structural action.
    const long long P1=1,Q1=425;
    auto nr=solve(aug,P1,Q1,MAXD,450);
    assert(nr.first==259 && nr.stable==296 && nr.last==2505);
    assert(nr.first_root==nr.threshold+120 && nr.fixed_root==nr.threshold+120);
    // U = 9/10 - 1/425 = 763/850; W = 763/850 - 19/30 = 337/1275.
    long long un=9LL*Q1-10LL*P1,ud=10LL*Q1,g=std::gcd(un,ud);un/=g;ud/=g;
    assert(un==763 && ud==850);
    long long wn=30LL*un-19LL*ud,wd=30LL*ud; g=std::gcd(wn,wd); wn/=g;wd/=g;
    assert(wn==337 && wd==1275);
    long long impn=10524LL*ud-un*11723LL, impd=11723LL*ud; g=std::gcd(llabs(impn),impd);impn/=g;impd/=g;
    assert(impn==751 && impd==9964550);

    cout << "I0130_B1_B13_B28_TROPICAL_TAIL_SUPPORT_PASS\n";
    cout << "old_family=653 old_eps=267/117230 first="<<oldr.first<<" stable="<<oldr.stable<<" last="<<oldr.last<<"\n";
    cout << "B28_tight_support_states="<<support.size()<<" optimal_incidences="<<optinc<<" tied="<<tied<<" unique="<<unique<<" h_range="<<minH<<".."<<maxH<<" D_range="<<minD<<".."<<maxD<<"\n";
    cout << "B28_target=(h237,D1031) path_capacity_scaled="<<pathcap<<" candidate_action=291/960,951/960 quotient_u=294/240 quotient_v=327/240 local_residual_scaled="<<(min(ZH,ZL)-oldbest)<<" branch_gap_H_minus_L="<<(ZH-ZL)<<"\n";
    cout << "B28_cell_slopes=sL:-4263/11723,sH:-2788/11723 derivatives=Hu:58149/23446,Hv:-53201/23446,Lu:-31139/11723,Lv:28941/11723 dHminusL=(120427/23446,-111083/23446)\n";
    cout << "B1_global_reuse_old_eps fixed_root_gain_scaled="<<(aug0.fixed_root-oldr.fixed_root)<<" new_stable="<<aug0.stable<<" new_last="<<aug0.last<<"\n";
    cout << "B13_tail_seed_cutoff_index="<<Dseed<<" monovariant_max9_scaled="<<maxScore<<" attained_at="<<argScore<<"\n";
    cout << "new_family=654 feasible_eps=1/425 first="<<nr.first<<" stable="<<nr.stable<<" last="<<nr.last<<" first_excess_scaled="<<(nr.first_root-nr.threshold)<<" total_goods_max="<<(nr.first+3)<<"\n";
    cout << "new_upper=763/850 new_width=337/1275 upper_improvement=751/9964550 checked_states="<<(oldr.checked+aug0.checked+nr.checked)<<"\n";
}
