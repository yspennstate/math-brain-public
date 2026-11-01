#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;

// I0130 exact integer self-check for the B3/B13/B18 run.
// Baseline delta0=1/10. Gap units are 1/240 and actions are A=240a,B=240b.
// The checker implements an exact semi-infinite/cutting-plane idea on the
// denominator-240 lattice-aligned separation family, then certifies the final
// finite adaptive source-valid policy. It does NOT claim the separation family
// is the full continuous action square.

struct Action { int A,B,dh,c,m; };

static Action make_action(int A,int B){
    assert(0<=A && A<=240 && 0<=B && B<=240);
    assert((9*A+11*B)%10==0);
    assert((11*A+9*B)%10==0);
    return {A,B,(9*A+11*B)/10,(11*A+9*B)/10,max(A,B)};
}

static vector<Action> q24(){
    vector<Action> a;
    for(int i=0;i<=24;++i) for(int j=0;j<=24;++j)
        a.push_back(make_action(10*i,10*j));
    return a;
}

static vector<Action> candidates240(){
    vector<Action> a;
    for(int A=0;A<=240;++A) for(int B=0;B<=240;++B){
        if((B-A)%10!=0) continue;
        a.push_back(make_action(A,B));
    }
    assert(a.size()==5809);
    return a;
}

struct FixedOut { vector<long long> phi; int stable_h; int last_nonzero; };

static FixedOut fixed_point(const vector<Action>& acts,long long P,long long R,int MAXD,int MAXH){
    vector<long long> prev(MAXD+1,0), cur(MAXD+1,0);
    int stable=-1;
    for(int h=1;h<=MAXH;++h){
        bool changed=false;
        for(int D=0;D<=MAXD;++D){
            long long best=0; // optional stop / zero action
            for(const auto& ac:acts){
                long long H=(9LL*ac.A*R)/10-P*ac.m;
                int DH=D+ac.dh;
                if(DH<=MAXD) H+=prev[DH];
                int DL; long long L;
                if(D>=ac.c){
                    DL=D-ac.c;
                    L=(-11LL*ac.A*R)/10-P*ac.m+prev[DL];
                }else{
                    DL=ac.c-D;
                    L=(9LL*ac.B*R)/10-1LL*D*R-P*ac.m+prev[DL];
                }
                best=max(best,min(H,L));
            }
            cur[D]=best;
            changed |= (cur[D]!=prev[D]);
        }
        prev.swap(cur);
        if(!changed){ stable=h; break; }
    }
    assert(stable>0);
    int last=-1;
    for(int D=0;D<=MAXD;++D) if(prev[D]!=0) last=D;
    return {move(prev),stable,last};
}

struct Residual { long long gain,H,L,base; int D,A,B; };

static Residual best_residual(const vector<long long>& phi,int cutoff,long long P,long long R,const vector<Action>& cand){
    Residual best{numeric_limits<long long>::min(),0,0,0,-1,-1,-1};
    for(const auto& ac:cand){
        for(int D=0;D<cutoff;++D){
            long long H=(9LL*ac.A*R)/10-P*ac.m;
            int DH=D+ac.dh;
            if(DH<cutoff) H+=phi[DH];
            int DL; long long L;
            if(D>=ac.c){
                DL=D-ac.c;
                L=(-11LL*ac.A*R)/10-P*ac.m+phi[DL];
            }else{
                DL=ac.c-D;
                L=(9LL*ac.B*R)/10-1LL*D*R-P*ac.m+phi[DL];
            }
            long long v=min(H,L), g=v-phi[D];
            if(g>best.gain) best={g,H,L,phi[D],D,ac.A,ac.B};
        }
    }
    return best;
}

struct ActionResidual { long long gain; int D; Action ac; long long H,L,base; };

static vector<ActionResidual> top_action_residuals(const vector<long long>& phi,int cutoff,long long P,long long R,const vector<Action>& cand,int k){
    vector<ActionResidual> rows;
    rows.reserve(cand.size());
    for(const auto& ac:cand){
        ActionResidual br{numeric_limits<long long>::min(),-1,ac,0,0,0};
        for(int D=0;D<cutoff;++D){
            long long H=(9LL*ac.A*R)/10-P*ac.m;
            int DH=D+ac.dh;
            if(DH<cutoff) H+=phi[DH];
            int DL; long long L;
            if(D>=ac.c){
                DL=D-ac.c;
                L=(-11LL*ac.A*R)/10-P*ac.m+phi[DL];
            }else{
                DL=ac.c-D;
                L=(9LL*ac.B*R)/10-1LL*D*R-P*ac.m+phi[DL];
            }
            long long g=min(H,L)-phi[D];
            if(g>br.gain) br={g,D,ac,H,L,phi[D]};
        }
        rows.push_back(br);
    }
    sort(rows.begin(),rows.end(),[](const auto& x,const auto& y){
        if(x.gain!=y.gain) return x.gain>y.gain;
        if(x.D!=y.D) return x.D<y.D;
        if(x.ac.A!=y.ac.A) return x.ac.A<y.ac.A;
        return x.ac.B<y.ac.B;
    });
    if((int)rows.size()>k) rows.resize(k);
    return rows;
}

struct CrossOut { int first_h; long long root,threshold,excess,checked_states; };

static CrossOut first_cross(const vector<Action>& acts,long long P,long long R,int MAXD,int MAXH){
    vector<long long> prev(MAXD+1,0),cur(MAXD+1,0);
    const long long threshold=312LL*R+720LL*P;
    long long checked=0;
    for(int h=1;h<=MAXH;++h){
        for(int D=0;D<=MAXD;++D){
            long long best=0;
            for(const auto& ac:acts){
                long long H=(9LL*ac.A*R)/10-P*ac.m;
                int DH=D+ac.dh;
                if(DH<=MAXD) H+=prev[DH]; // otherwise stop on that branch
                int DL; long long L;
                if(D>=ac.c){
                    DL=D-ac.c;
                    L=(-11LL*ac.A*R)/10-P*ac.m+prev[DL];
                }else{
                    DL=ac.c-D;
                    L=(9LL*ac.B*R)/10-1LL*D*R-P*ac.m+prev[DL];
                }
                best=max(best,min(H,L));
            }
            cur[D]=best;
            ++checked;
        }
        prev.swap(cur);
        if(prev[480]>=threshold)
            return {h,prev[480],threshold,prev[480]-threshold,checked};
    }
    return {-1,prev[480],threshold,prev[480]-threshold,checked};
}

int main(){
    constexpr int MAXD=5500;
    const auto cand=candidates240();

    auto acts=q24();
    acts.push_back(make_action(6,236)); // prior repository cut (1/40,59/60)
    assert(acts.size()==626);

    // Cutting plane 1 at epsilon=7/6250.
    auto fp1=fixed_point(acts,7,6250,MAXD,1000);
    assert(fp1.stable_h==523 && fp1.last_nonzero==2356);
    assert(fp1.phi[480]==1955468);
    auto r1=best_residual(fp1.phi,fp1.last_nonzero+1,7,6250,cand);
    assert(r1.gain==16024 && r1.D==1970 && r1.A==13 && r1.B==233);
    assert(r1.H==103592 && r1.L==103510 && r1.base==87486);
    acts.push_back(make_action(13,233));

    // Cutting plane 2 at epsilon=621/500000.
    auto fp2=fixed_point(acts,621,500000,MAXD,1200);
    assert(fp2.stable_h==816 && fp2.last_nonzero==2359);
    assert(fp2.phi[480]==156462571);
    auto r2=best_residual(fp2.phi,fp2.last_nonzero+1,621,500000,cand);
    assert(r2.gain==1427172 && r2.D==1092 && r2.A==67 && r2.B==237);
    assert(r2.H==64823125 && r2.L==64598434 && r2.base==63171262);
    acts.push_back(make_action(67,237));
    assert(acts.size()==628);

    // Cutting plane 3 at epsilon=161/125000: rank exact violated actions.
    auto fp3=fixed_point(acts,161,125000,MAXD,1000);
    assert(fp3.stable_h==473 && fp3.last_nonzero==2353);
    assert(fp3.phi[480]==39116945);
    assert(fp3.phi[480]-(312LL*125000+720LL*161)==1025);
    auto top=top_action_residuals(fp3.phi,fp3.last_nonzero+1,161,125000,cand,10);
    const int expA[10]={26,94,84,3,3,74,114,4,176,115};
    const int expB[10]={236,234,234,223,233,234,234,234,236,235};
    const int expD[10]={1661,829,919,2353,2353,1027,692,2334,302,692};
    const long long expG[10]={310073,291456,289126,286787,285177,280063,279796,268456,263963,263395};
    for(int i=0;i<10;++i){
        assert(top[i].ac.A==expA[i] && top[i].ac.B==expB[i]);
        assert(top[i].D==expD[i] && top[i].gain==expG[i]);
        acts.push_back(top[i].ac);
    }
    assert(acts.size()==638);

    // Exact source-valid finite policy at epsilon=163/100000.
    auto cross=first_cross(acts,163,100000,MAXD,600);
    assert(cross.first_h==254);
    assert(cross.threshold==31317360);
    assert(cross.root==31319975 && cross.excess==2615);
    assert(cross.checked_states==254LL*(MAXD+1));

    // delta=1/10+163/100000=10163/100000; U=89837/100000.
    const long long upper_num=89837, upper_den=100000;
    long long width_num=upper_num*30-19LL*upper_den;
    long long width_den=upper_den*30;
    long long g=gcd(width_num,width_den); width_num/=g; width_den/=g;
    assert(width_num==79511 && width_den==300000);

    long long imp_num=2809LL*upper_den-upper_num*3125LL;
    long long imp_den=3125LL*upper_den;
    g=gcd(imp_num,imp_den); imp_num/=g; imp_den/=g;
    assert(imp_num==51 && imp_den==100000);

    cout << "I0130_CUTTING_PLANE_ROBUST_LIFT_PASS\n";
    cout << "model_math_scope=exact_integer_self_check\n";
    cout << "candidate_separator_count=5809\n";
    cout << "cut1_epsilon=7/6250\n";
    cout << "cut1_action=13/240,233/240\n";
    cout << "cut1_state_gap=197/24\n";
    cout << "cut1_residual_scaled=16024\n";
    cout << "cut2_epsilon=621/500000\n";
    cout << "cut2_action=67/240,237/240\n";
    cout << "cut2_state_gap=91/20\n";
    cout << "cut2_residual_scaled=1427172\n";
    cout << "cut3_epsilon=161/125000\n";
    cout << "cut3_top10_verified=1\n";
    cout << "final_action_count=" << acts.size() << "\n";
    cout << "new_epsilon=163/100000\n";
    cout << "first_threshold_cross_h=" << cross.first_h << "\n";
    cout << "root_scaled=" << cross.root << "\n";
    cout << "threshold_scaled=" << cross.threshold << "\n";
    cout << "excess_scaled=" << cross.excess << "\n";
    cout << "source_valid_upper_bound=89837/100000\n";
    cout << "width=79511/300000\n";
    cout << "improvement_over_2809_3125=51/100000\n";
    cout << "checked_final_states=" << cross.checked_states << "\n";
}
