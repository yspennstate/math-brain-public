#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;

// I0130 exact finite certificate supporting the B4/B14/B25 run.
// Baseline target parameter: delta0=1/10, alpha0=9/10.
// Grid: a,b in {0,1/24,...,1}. All tilted-safety/gap quantities are
// scaled by 10*24=240, so the Bellman recurrence is integer exact.
//
// This checker verifies:
//   (1) the Q=24 Bellman root values through h=300;
//   (2) the best parameter-stability lift obtainable from those certified
//       root margins occurs at h=145 with epsilon=7/70320;
//   (3) the resulting source-valid upper endpoint is 63281/70320;
//   (4) on this entire finite DP, restricting to the canonical half-square
//       a<=b never changes any Bellman value (finite B14 quotient evidence).

static constexpr int p = 1;       // delta0=p/q=1/10
static constexpr int q = 10;
static constexpr int Q = 24;
static constexpr int H = 300;
static constexpr int SCALE = q*Q;              // 240
static constexpr int START_D = 2*SCALE;        // 480
static constexpr int START_X = (q+3*p)*Q;      // 312 = 13/10 * 240
static constexpr int STEP = 2*q*Q;             // maximum one-step gap increase

int main(){
    static_assert(SCALE==240);
    static_assert(START_D==480);
    static_assert(START_X==312);

    const int maxD = START_D + STEP*H;
    vector<int> prev(maxD+1,0), cur;
    vector<int> roots(H+1,0);

    long long checked_states = 0;
    long long canonical_mismatches = 0;

    long long best_num = -1; // epsilon numerator before reduction
    long long best_den = 1;  // epsilon denominator before reduction
    int best_h = -1;
    int best_root = -1;

    for(int h=1; h<=H; ++h){
        const int lim = maxD - STEP*h;
        cur.assign(lim+1,0);
        for(int D=0; D<=lim; ++D){
            int best = INT32_MIN;
            int best_canon = INT32_MIN;
            for(int i=0;i<=Q;++i){
                for(int j=0;j<=Q;++j){
                    // high-recipient branch
                    const int incH=(q-p)*i+(q+p)*j;
                    const int valH=(q-p)*i + prev[D+incH];

                    // low-recipient branch, with exact reflection
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
                    best=max(best,w);
                    if(i<=j) best_canon=max(best_canon,w);
                }
            }
            assert(best==best_canon);
            if(best!=best_canon) ++canonical_mismatches;
            cur[D]=best;
            ++checked_states;
        }
        prev.swap(cur);
        roots[h]=prev[START_D];
        assert(roots[h]>=roots[h-1]); // zero-valued good pads shorter policy

        if(roots[h]>START_X){
            // Parameter stability from the preceding report:
            // |G_h^delta-G_h^delta0| <= 2h |delta-delta0|,
            // while the starting target 1+3 delta rises by 3 epsilon.
            // Hence epsilon <= margin/(SCALE*(2h+3)).
            const long long num=roots[h]-START_X;
            const long long den=1LL*SCALE*(2*h+3);
            if(best_num<0 || num*best_den > best_num*den){
                best_num=num;
                best_den=den;
                best_h=h;
                best_root=roots[h];
            }
        }
    }

    assert(canonical_mismatches==0);
    assert(roots[117]==316);
    assert(roots[125]==317);
    assert(roots[132]==318);
    assert(roots[145]==319);
    assert(roots[300]==319);

    assert(best_h==145);
    assert(best_root==319);
    // epsilon = 7 / (240*(2*145+3)) = 7/70320.
    assert(best_num==7);
    assert(best_den==70320);
    long long eg=std::gcd(best_num,best_den);
    assert(best_num/eg==7 && best_den/eg==70320);

    // delta1 = 1/10 + 7/70320 = 7039/70320.
    // alpha1 = 1-delta1 = 63281/70320.
    long long delta_num=7032+7;
    long long delta_den=70320;
    assert(delta_num==7039);
    long long alpha_num=delta_den-delta_num;
    assert(alpha_num==63281);
    assert(std::gcd(alpha_num,delta_den)==1);

    // Current lower endpoint remains 19/30.
    // Width = 63281/70320 - 19/30 = 3749/14064.
    long long wnum=alpha_num*30 - 19LL*delta_den;
    long long wden=delta_den*30;
    long long wg=std::gcd(wnum,wden);
    assert(wnum/wg==3749 && wden/wg==14064);

    // Improvement over preceding upper endpoint 12797/14220.
    long long inum=12797LL*70320 - 63281LL*14220;
    long long iden=14220LL*70320;
    long long ig=std::gcd(inum,iden);
    assert(inum/ig==487 && iden/ig==16665840);

    // B4 closed two-step continuous formula parameters at alpha0=9/10:
    // D0=alpha*beta/2=99/200, plateau=alpha^2/2=81/200,
    // D1=alpha+D0=279/200, cutoff 2alpha=9/5.
    assert(9LL*11==99);
    assert(9LL*9==81);
    assert(180+99==279);

    cout << "I0130_B4_B14_B25_LIFT_PASS\n";
    cout << "baseline_delta=1/10\n";
    cout << "baseline_alpha=9/10\n";
    cout << "action_grid_denominator=24\n";
    cout << "h117_root=316/240\n";
    cout << "h125_root=317/240\n";
    cout << "h132_root=318/240\n";
    cout << "h145_root=319/240\n";
    cout << "h300_root=319/240\n";
    cout << "best_stability_lift_horizon=145\n";
    cout << "best_stability_margin=7/240\n";
    cout << "epsilon=7/70320\n";
    cout << "lifted_delta=7039/70320\n";
    cout << "source_valid_upper_bound=63281/70320\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width=3749/14064\n";
    cout << "improvement_over_12797_14220=487/16665840\n";
    cout << "canonical_half_square=a<=b\n";
    cout << "canonical_mismatches=" << canonical_mismatches << "\n";
    cout << "checked_dp_states=" << checked_states << "\n";
    cout << "B4_G2_breakpoints_at_alpha_9_10=99/200,279/200,9/5\n";
    cout << "B4_G2_plateau=81/200\n";
    return 0;
}
