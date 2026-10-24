#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact integer self-check for the B6/B19/B27 run.
// Baseline delta0=1/10. Gap units are 1/240 and actions are A=240a,B=240b.
// Robust values at epsilon=P/R are stored in scale 2400*R, so no divisibility
// assumption on R is needed. The action family is the 638-action family from
// the preceding cutting-plane report. All actions are legal continuous-source
// valuations in [0,1]^2.

struct Action { int A,B,dh,c,m; };
static Action make_action(int A,int B){
    assert(0<=A && A<=240 && 0<=B && B<=240);
    assert((B-A)%10==0); // makes both child gap shifts integral in 1/240 units
    return {A,B,(9*A+11*B)/10,(11*A+9*B)/10,max(A,B)};
}

static vector<Action> full638(){
    vector<Action> a;
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j)
        a.push_back(make_action(10*i,10*j));
    const int extra[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},
        {84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:extra) a.push_back(make_action(p[0],p[1]));
    assert(a.size()==638);
    return a;
}

static long long Hterm(const Action& ac,long long P,long long R){
    // (9A/2400 - (P/R)m/240) * 2400R
    return 9LL*ac.A*R - 10LL*P*ac.m;
}
static long long Lterm(const Action& ac,int D,long long P,long long R){
    if(D>=ac.c) return -11LL*ac.A*R - 10LL*P*ac.m;
    return (9LL*ac.B-10LL*D)*R - 10LL*P*ac.m;
}

struct FullRun {
    int first_cross=-1, stable=-1, last_nonzero=-1;
    long long root=0, threshold=0, checked=0;
    vector<vector<int16_t>> policy; // only stored through first-cross horizon
};

static FullRun full_fixed_point(const vector<Action>& acts,long long P,long long R,int MAXD,int MAXH,int STOREH){
    vector<long long> prev(MAXD+1,0),cur(MAXD+1,0);
    vector<vector<int16_t>> pol(STOREH+1,vector<int16_t>(MAXD+1,-1));
    const long long threshold=3120LL*R+7200LL*P; // (13/10+3eps)*2400R
    int first=-1,stable=-1;
    long long checked=0;
    for(int h=1;h<=MAXH;++h){
        bool changed=false;
        for(int D=0;D<=MAXD;++D){
            long long best=0; int bi=-1; // optional stop
            for(int k=0;k<(int)acts.size();++k){
                const auto &ac=acts[k];
                long long H=Hterm(ac,P,R);
                int DH=D+ac.dh;
                if(DH<=MAXD) H+=prev[DH];
                int DL=abs(D-ac.c);
                long long L=Lterm(ac,D,P,R)+prev[DL];
                long long v=min(H,L);
                if(v>best){ best=v; bi=k; }
            }
            cur[D]=best;
            if(h<=STOREH) pol[h][D]=bi;
            changed |= (cur[D]!=prev[D]);
            ++checked;
        }
        prev.swap(cur);
        if(first<0 && prev[480]>=threshold) first=h;
        if(!changed){ stable=h; break; }
    }
    assert(stable>0);
    int last=-1; for(int D=0;D<=MAXD;++D) if(prev[D]!=0) last=D;
    return {first,stable,last,prev[480],threshold,checked,move(pol)};
}

struct Reach { long long nodes; int unique_actions; };
static Reach reachable_policy(const vector<Action>& acts,const vector<vector<int16_t>>& pol,int H,int D0,int MAXD){
    set<pair<int,int>> seen;
    set<int> used;
    vector<pair<int,int>> stack={{H,D0}};
    while(!stack.empty()){
        auto [h,D]=stack.back(); stack.pop_back();
        if(h<=0 || D<0 || D>MAXD) continue;
        if(!seen.insert({h,D}).second) continue;
        int k=pol[h][D];
        if(k<0) continue;
        used.insert(k);
        const auto &ac=acts[k];
        int DH=D+ac.dh, DL=abs(D-ac.c);
        if(DH<=MAXD) stack.push_back({h-1,DH});
        stack.push_back({h-1,DL});
    }
    return {(long long)seen.size(),(int)used.size()};
}

static vector<Action> compressed_family(int mode){
    vector<Action> a;
    auto add=[&](int A,int B){ a.push_back(make_action(A,B)); };
    if(mode==0){ // one top edge b=1, plus cuts
        for(int A=0;A<=240;A+=10) add(A,240);
        add(0,0);
    } else if(mode==1){ // high-b triangular strip b>=2/3
        for(int B=160;B<=240;B+=10) for(int A=0;A<=B;A+=10) add(A,B);
        add(0,0);
    } else { // wider high-b triangular strip b>=5/12
        for(int B=100;B<=240;B+=10) for(int A=0;A<=B;A+=10) add(A,B);
        add(0,0);
    }
    const int extra[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},
        {84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:extra) add(p[0],p[1]);
    sort(a.begin(),a.end(),[](const Action& x,const Action& y){return tie(x.A,x.B)<tie(y.A,y.B);});
    a.erase(unique(a.begin(),a.end(),[](const Action& x,const Action& y){return x.A==y.A&&x.B==y.B;}),a.end());
    return a;
}

static tuple<int,long long,int> fixed_root(const vector<Action>& acts,long long P,long long R,int MAXD,int MAXH){
    vector<long long> prev(MAXD+1,0),cur(MAXD+1,0);
    int stable=-1,last=-1;
    for(int h=1;h<=MAXH;++h){
        bool changed=false;
        for(int D=0;D<=MAXD;++D){
            long long best=0;
            for(const auto& ac:acts){
                long long H=Hterm(ac,P,R); int DH=D+ac.dh; if(DH<=MAXD) H+=prev[DH];
                int DL=abs(D-ac.c); long long L=Lterm(ac,D,P,R)+prev[DL];
                best=max(best,min(H,L));
            }
            cur[D]=best; changed |= (cur[D]!=prev[D]);
        }
        prev.swap(cur);
        if(!changed){stable=h;break;}
    }
    assert(stable>0);
    for(int D=0;D<=MAXD;++D) if(prev[D]!=0) last=D;
    return {stable,prev[480],last};
}

int main(){
    constexpr int MAXD=5500;
    const long long P=3,R=1835; // epsilon*=3/1835
    const auto acts=full638();
    auto fr=full_fixed_point(acts,P,R,MAXD,1000,271);
    assert(fr.first_cross==271);
    assert(fr.stable==307);
    assert(fr.last_nonzero==2522);
    assert(fr.root==fr.threshold);
    assert(fr.threshold==5746800);

    auto reach=reachable_policy(acts,fr.policy,271,480,MAXD);
    assert(reach.nodes==381872);
    assert(reach.unique_actions==201);

    const long long threshold=fr.threshold;
    auto f0=compressed_family(0),f1=compressed_family(1),f2=compressed_family(2);
    auto [s0,r0,l0]=fixed_root(f0,P,R,MAXD,1500);
    auto [s1,r1,l1]=fixed_root(f1,P,R,MAXD,1500);
    auto [s2,r2,l2]=fixed_root(f2,P,R,MAXD,1500);
    assert(f0.size()==39 && s0==181 && r0==5408230 && l0==2405 && r0<threshold);
    assert(f1.size()==203 && s1==373 && r1==5709900 && l1==2486 && r1<threshold);
    assert(f2.size()==284 && s2==311 && r2==5737025 && l2==2522 && r2<threshold);

    // delta=1/10+3/1835=373/3670, so U=3297/3670.
    long long delta_num=373,delta_den=3670, upper_num=3297,upper_den=3670;
    assert(delta_num+upper_num==delta_den);
    long long width_num=upper_num*30-19LL*upper_den;
    long long width_den=upper_den*30;
    long long g=gcd(width_num,width_den); width_num/=g; width_den/=g;
    assert(width_num==1459 && width_den==5505);
    long long imp_num=89837LL*upper_den-upper_num*100000LL;
    long long imp_den=100000LL*upper_den;
    g=gcd(imp_num,imp_den); imp_num/=g; imp_den/=g;
    assert(imp_num==179 && imp_den==36700000);

    cout << "I0130_B6_B19_B27_CRITICAL_FAMILY_PASS\n";
    cout << "model_math_scope=exact_integer_self_check\n";
    cout << "action_family_size=" << acts.size() << "\n";
    cout << "critical_epsilon=3/1835\n";
    cout << "first_threshold_cross_h=" << fr.first_cross << "\n";
    cout << "fixed_point_stable_h=" << fr.stable << "\n";
    cout << "fixed_point_last_nonzero_gap_units=" << fr.last_nonzero << "\n";
    cout << "root_scaled=" << fr.root << "\n";
    cout << "threshold_scaled=" << fr.threshold << "\n";
    cout << "reachable_policy_nodes_h271=" << reach.nodes << "\n";
    cout << "reachable_unique_actions_h271=" << reach.unique_actions << "\n";
    cout << "compressed_39_fixed_deficit=" << threshold-r0 << "\n";
    cout << "compressed_203_fixed_deficit=" << threshold-r1 << "\n";
    cout << "compressed_284_fixed_deficit=" << threshold-r2 << "\n";
    cout << "source_valid_upper_bound=3297/3670\n";
    cout << "width=1459/5505\n";
    cout << "improvement_over_89837_100000=179/36700000\n";
    cout << "checked_full_states=" << fr.checked << "\n";
}
