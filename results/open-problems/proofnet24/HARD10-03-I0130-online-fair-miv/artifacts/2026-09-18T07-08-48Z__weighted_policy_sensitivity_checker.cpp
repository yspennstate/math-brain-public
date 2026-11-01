#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// I0130 exact finite certificate for the B9/B10/B28 run.
// Baseline target: delta0=1/10 (alpha0=9/10), action grid Q=24.
//
// For every Bellman state through horizon H=300 this program:
//   (i) maximizes the exact baseline guaranteed tilted-safety decrease;
//  (ii) among all value-optimal canonical actions a<=b, minimizes the
//       fixed-policy sensitivity weight
//          S(Pi)=max_root-to-leaf sum_t max(a_t,b_t).
// On the canonical half-square max(a,b)=b=j/Q, so the scaled recurrence is
//          s_h(D)=j+max{s_{h-1}(D_H),s_{h-1}(D_L)}.
//
// The earlier exact B4/B14/B25 certificate established that restricting the
// full Q=24 Bellman search to a<=b changes no value through horizon 300.
// Thus the policy certified here is baseline-value-optimal in that exact
// finite game. The continuous weighted fixed-policy parameter theorem used
// to lift this policy away from delta0 is proved in the accompanying report;
// this checker certifies only the finite Bellman/policy arithmetic.

static constexpr int p=1;
static constexpr int q=10;
static constexpr int Q=24;
static constexpr int H=300;
static constexpr int SCALE=q*Q;                 // 240
static constexpr int START_D=2*SCALE;           // 480
static constexpr int START_X=(q+3*p)*Q;         // 312 = (13/10)*240
static constexpr int STEP=2*q*Q;                // 480

int main(){
    static_assert(SCALE==240 && START_D==480 && START_X==312);

    const int maxD=START_D+STEP*H;
    vector<int> prev(maxD+1,0), prevSens(maxD+1,0), cur, curSens;
    vector<int> roots(H+1,0), rootSens(H+1,0);
    long long checked_states=0;

    // Track the strongest lift among the exact baseline-value-optimal policies
    // at all horizons <=300.  If root value r>312 and sensitivity numerator s
    // represents S=s/Q, then
    // epsilon <= ((r-312)/SCALE)/(s/Q+3).
    long long bestNum=-1,bestDen=1;
    int bestH=-1,bestRoot=-1,bestSens=-1;

    for(int h=1;h<=H;++h){
        const int lim=maxD-STEP*h;
        cur.assign(lim+1,0);
        curSens.assign(lim+1,0);

        for(int D=0;D<=lim;++D){
            int bestVal=INT32_MIN;
            int bestS=INT32_MAX;

            for(int i=0;i<=Q;++i){
                for(int j=i;j<=Q;++j){
                    const int DH=D+(q-p)*i+(q+p)*j;
                    const int valH=(q-p)*i+prev[DH];

                    const int C=(q+p)*i+(q-p)*j;
                    int DL,costL;
                    if(D>=C){
                        DL=D-C;
                        costL=-(q+p)*i;
                    }else{
                        DL=C-D;
                        costL=(q-p)*j-D;
                    }
                    const int valL=costL+prev[DL];
                    const int w=min(valH,valL);

                    // Because i<=j, max(a,b)=j/Q.
                    const int candS=j+max(prevSens[DH],prevSens[DL]);
                    if(w>bestVal || (w==bestVal && candS<bestS)){
                        bestVal=w;
                        bestS=candS;
                    }
                }
            }

            cur[D]=bestVal;
            curSens[D]=bestS;
            ++checked_states;
        }

        prev.swap(cur);
        prevSens.swap(curSens);
        roots[h]=prev[START_D];
        rootSens[h]=prevSens[START_D];
        assert(roots[h]>=roots[h-1]);

        if(roots[h]>START_X){
            const long long num=1LL*(roots[h]-START_X)*Q;
            const long long den=1LL*SCALE*(rootSens[h]+3*Q);
            if(bestNum<0 || num*bestDen>bestNum*den){
                bestNum=num; bestDen=den;
                bestH=h; bestRoot=roots[h]; bestSens=rootSens[h];
            }
        }
    }

    // Preserved exact baseline roots, plus the new minimum sensitivity.
    assert(roots[117]==316);
    assert(roots[125]==317);
    assert(roots[132]==318);
    assert(roots[145]==319);
    assert(roots[300]==319);
    assert(rootSens[145]==3384);

    // Among baseline-value-optimal canonical policies through h=300, the
    // strongest weighted-sensitivity lift is attained first at h=145.
    assert(bestH==145 && bestRoot==319 && bestSens==3384);

    // S=3384/24=141; hence S+3=144 exactly.
    assert(bestSens/Q==141 && bestSens%Q==0);
    const long long Splus3=144;

    // Baseline margin M=(319-312)/240=7/240.
    // epsilon=M/(S+3)=7/34560.
    long long epsNum=7,epsDen=240*Splus3;
    long long eg=gcd(epsNum,epsDen);
    epsNum/=eg; epsDen/=eg;
    assert(epsNum==7 && epsDen==34560);

    // delta1=1/10+7/34560=3463/34560.
    long long deltaNum=epsDen+10*epsNum;
    long long deltaDen=10*epsDen;
    long long dg=gcd(deltaNum,deltaDen);
    deltaNum/=dg; deltaDen/=dg;
    assert(deltaNum==3463 && deltaDen==34560);

    // alpha1=1-delta1=31097/34560.
    long long alphaNum=deltaDen-deltaNum;
    long long alphaDen=deltaDen;
    assert(alphaNum==31097 && alphaDen==34560);
    assert(gcd(alphaNum,alphaDen)==1);

    // W=alpha1-19/30=9209/34560.
    long long wnum=alphaNum*30-19LL*alphaDen;
    long long wden=alphaDen*30;
    long long wg=gcd(wnum,wden);
    wnum/=wg; wden/=wg;
    assert(wnum==9209 && wden==34560);

    // Improvement over prior U=31961/35520 is 7/1278720.
    long long inum=31961LL*alphaDen-alphaNum*35520LL;
    long long iden=35520LL*alphaDen;
    long long ig=gcd(inum,iden);
    inum/=ig; iden/=ig;
    assert(inum==7 && iden==1278720);

    assert(alphaNum*10LL<9LL*alphaDen);
    assert(alphaNum*30LL>19LL*alphaDen);

    cout << "I0130_WEIGHTED_POLICY_SENSITIVITY_PASS\n";
    cout << "baseline_delta=1/10\n";
    cout << "action_grid_denominator=24\n";
    cout << "scan_horizons=1..300\n";
    cout << "h117_root=316/240\n";
    cout << "h125_root=317/240\n";
    cout << "h132_root=318/240\n";
    cout << "h145_root=319/240\n";
    cout << "h300_root=319/240\n";
    cout << "best_weighted_lift_horizon=145\n";
    cout << "baseline_start_target=312/240=13/10\n";
    cout << "baseline_margin=7/240\n";
    cout << "minimum_value_optimal_policy_sensitivity=3384/24=141\n";
    cout << "policy_sensitivity_plus_target_slope=144\n";
    cout << "epsilon=7/34560\n";
    cout << "lifted_delta=3463/34560\n";
    cout << "source_valid_upper_bound=31097/34560\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width=9209/34560\n";
    cout << "improvement_over_31961_35520=7/1278720\n";
    cout << "checked_dp_states=" << checked_states << "\n";
    return 0;
}
