#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// I0130 exact finite certificate for the B11/B24/B30 robust-Bellman run.
// Baseline target: delta0=1/10 (alpha0=9/10), legal action grid Q=24.
// Candidate transport: epsilon=P/R=11/13630.
//
// Scaled gap units are 1/240.  For action (a,b)=(i/24,j/24):
//   D_H = D + 9 i + 11 j,
//   c_H = 9 i,
//   C   = 11 i + 9 j,
//   if D>=C: D_L=D-C, c_L=-11 i;
//   if D< C: D_L=C-D, c_L=9 j-D.
// Here c_H,c_L are baseline tilted-safety decreases in units 1/240.
//
// Define the robust value by subtracting epsilon*max(a,b) per post-unit good.
// Multiplying by 240R makes the immediate sensitivity penalty exactly
//   10 P max(i,j).
// The DP searches the FULL 25x25 action square.  No a<=b quotient is assumed.
//
// Support: R_h(D)=0 for D>=2h, i.e. D>=480 h in these scaled units.  We
// compute backwards on a shrinking domain, so every child lookup is in-bounds.

static constexpr int Q = 24;
static constexpr int SCALE = 240;
static constexpr int START_D = 480;
static constexpr int H = 255;
static constexpr int STEP = 480;
static constexpr long long P = 11;
static constexpr long long R = 13630;

struct Action { int i,j,dh,c,m; };

int main() {
    const int maxD = START_D + STEP*H;
    vector<long long> prev(maxD+1,0), cur;
    vector<Action> actions;
    actions.reserve((Q+1)*(Q+1));
    for(int i=0;i<=Q;++i) for(int j=0;j<=Q;++j)
        actions.push_back({i,j,9*i+11*j,11*i+9*j,max(i,j)});
    assert(actions.size()==625);

    // (13/10 + 3 epsilon)*(240R) = 312R + 720P.
    const long long threshold = 312LL*R + 720LL*P;
    assert(threshold==4260480);

    long long checkedStates=0;
    long long root117=-1, root145=-1, root200=-1, root255=-1;
    long long bestDiff=LLONG_MIN;
    int bestH=-1;

    for(int h=1; h<=H; ++h) {
        const int lim = maxD - STEP*h;
        cur.assign(lim+1,0);
        for(int D=0; D<=lim; ++D) {
            long long best=0; // zero action is legal
            for(const auto &ac: actions) {
                const long long penalty = 10LL*P*ac.m;
                const long long vH = R*(9LL*ac.i) - penalty + prev[D+ac.dh];

                int DL;
                long long cL;
                if(D>=ac.c) { DL=D-ac.c; cL=-11LL*ac.i; }
                else        { DL=ac.c-D; cL=  9LL*ac.j-D; }
                const long long vL = R*cL - penalty + prev[DL];
                best=max(best,min(vH,vL));
            }
            cur[D]=best;
            ++checkedStates;
        }
        prev.swap(cur);
        const long long root=prev[START_D];
        const long long diff=root-threshold;
        if(diff>bestDiff){ bestDiff=diff; bestH=h; }
        if(h==117) root117=root;
        if(h==145) root145=root;
        if(h==200) root200=root;
        if(h==255) root255=root;
    }

    assert(root255==threshold);
    assert(bestDiff==0 && bestH==255);
    assert(checkedStates==15667455);

    // delta1=1/10+11/13630=687/6815; alpha1=6128/6815.
    long long deltaNum=R+10LL*P, deltaDen=10LL*R;
    long long dg=gcd(deltaNum,deltaDen); deltaNum/=dg; deltaDen/=dg;
    assert(deltaNum==687 && deltaDen==6815);
    long long alphaNum=deltaDen-deltaNum, alphaDen=deltaDen;
    assert(alphaNum==6128 && alphaDen==6815 && gcd(alphaNum,alphaDen)==1);

    // W=6128/6815-19/30=10871/40890.
    long long wnum=alphaNum*30LL-19LL*alphaDen, wden=alphaDen*30LL;
    long long wg=gcd(wnum,wden); wnum/=wg; wden/=wg;
    assert(wnum==10871 && wden==40890);

    // Improvement over prior U=31097/34560.
    long long inum=31097LL*alphaDen-alphaNum*34560LL;
    long long iden=34560LL*alphaDen;
    long long ig=gcd(inum,iden); inum/=ig; iden/=ig;
    assert(inum==5695 && iden==9421056 && inum>0);

    cout << "I0130_ROBUST_BELLMAN_FULLSQUARE_PASS\n";
    cout << "baseline_delta=1/10\n";
    cout << "action_grid_denominator=24\n";
    cout << "full_action_square=625_actions\n";
    cout << "scan_horizons=1..255\n";
    cout << "epsilon=11/13630\n";
    cout << "root_h117_scaled=" << root117 << "\n";
    cout << "root_h145_scaled=" << root145 << "\n";
    cout << "root_h200_scaled=" << root200 << "\n";
    cout << "robust_root_h255=" << root255 << "/(240*13630)\n";
    cout << "robust_threshold=" << threshold << "/(240*13630)\n";
    cout << "first_best_horizon=" << bestH << "\n";
    cout << "best_scaled_excess=" << bestDiff << "\n";
    cout << "lifted_delta=687/6815\n";
    cout << "source_valid_upper_bound=6128/6815\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width=10871/40890\n";
    cout << "improvement_over_31097_34560=5695/9421056\n";
    cout << "checked_dp_states=" << checkedStates << "\n";
    return 0;
}
