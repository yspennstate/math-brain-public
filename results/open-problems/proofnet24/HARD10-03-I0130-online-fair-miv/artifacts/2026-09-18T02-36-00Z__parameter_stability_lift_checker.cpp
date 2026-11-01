#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// Exact finite core for I0130 parameter-stability lift.
// Baseline: delta0=1/10, alpha0=9/10, action grid Q=24, horizon H=117.
// We recompute the exact grid Bellman root value G_{117,Q}^{delta0}(2)=316/240=79/60.
// The report proves the continuous-operator parameter Lipschitz theorem
// |G_h^delta-G_h^{delta'}| <= 2h |delta-delta'|.
// With eps=1/14220, delta1=1/10+eps and alpha1=1-delta1=12797/14220,
// the baseline margin exactly pays for the parameter perturbation and the increased target.

static constexpr int p=1, q=10, Q=24, H=117;
static constexpr int SCALE=q*Q;
static constexpr int START_D=2*SCALE;
static constexpr int STEP=2*q*Q;
static constexpr int TARGET0=(q+3*p)*Q;

int main(){
    const int maxD=START_D+STEP*H;
    vector<int> prev(maxD+1,0), cur;
    int root=0;
    for(int h=1;h<=H;++h){
        int lim=maxD-STEP*h;
        cur.assign(lim+1,0);
        for(int D=0;D<=lim;++D){
            int best=INT32_MIN;
            for(int i=0;i<=Q;++i) for(int j=0;j<=Q;++j){
                int incH=(q-p)*i+(q+p)*j;
                int valH=(q-p)*i+prev[D+incH];
                int C=(q+p)*i+(q-p)*j;
                int DL,costL;
                if(D>=C){DL=D-C; costL=-(q+p)*i;}
                else{DL=C-D; costL=(q-p)*j-D;}
                int valL=costL+prev[DL];
                best=max(best,min(valH,valL));
            }
            cur[D]=best;
        }
        prev.swap(cur);
        root=prev[START_D];
    }
    assert(root==316);
    assert(TARGET0==312);

    const long long eps_den=14220;
    assert((316-312)*eps_den == SCALE*(2*H+3));

    long long dnum=1423, den=14220, anum=12797;
    assert(dnum+anum==den);
    assert(std::gcd(anum,den)==1);

    long long left_num = 79LL*237 - 234LL;
    long long target_num = den + 3*dnum;
    assert(left_num==target_num);
    long long g=std::gcd(left_num,den);
    assert(left_num/g==6163 && den/g==4740);

    long long wnum=anum*30-19LL*den;
    long long wden=den*30;
    long long gw=std::gcd(wnum,wden);
    assert(wnum/gw==3791 && wden/gw==14220);

    assert(9LL*den - 10LL*anum == 10);

    cout << "I0130_PARAMETER_STABILITY_LIFT_PASS\n";
    cout << "baseline_delta=1/10\n";
    cout << "baseline_grid_Q=24\n";
    cout << "baseline_horizon=117\n";
    cout << "baseline_root=316/240=79/60\n";
    cout << "baseline_target=312/240=13/10\n";
    cout << "baseline_margin=4/240=1/60\n";
    cout << "parameter_lipschitz_constant_per_step=2\n";
    cout << "epsilon=1/14220\n";
    cout << "lifted_delta=1423/14220\n";
    cout << "lifted_alpha=12797/14220\n";
    cout << "perturbed_value_lower_bound=6163/4740\n";
    cout << "lifted_target=6163/4740\n";
    cout << "current_lower_endpoint=19/30\n";
    cout << "new_metric_width=3791/14220\n";
    cout << "improvement_over_9_10=1/14220\n";
    return 0;
}
