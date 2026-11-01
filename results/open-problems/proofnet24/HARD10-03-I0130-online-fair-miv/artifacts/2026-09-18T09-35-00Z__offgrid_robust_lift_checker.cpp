#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// I0130 exact certificate for the B5/B12/B16 run.
// Baseline: delta0=1/10, alpha0=9/10, beta0=11/10.
// Gap units are 1/240. Actions are represented by A=240a, B=240b.
//
// This file certifies three facts:
// (1) At epsilon0=11/13630 the full Q=24 robust Bellman operator has an
//     exact finite-support fixed point whose root equals the old threshold.
//     This proves the old epsilon is optimal for the frozen Q=24 robust game.
// (2) The best denominator-240 lattice-aligned one-step deviation from that
//     fixed point is the legal off-grid action (a,b)=(1/40,59/60) at
//     D=439/48, with exact positive gain.
// (3) Adding only that one action to Q=24 and using epsilon1=7/6250 gives a
//     finite optional-stop Bellman certificate at horizon 371, hence the
//     source-valid exact-MIV PROP1 upper bound 2809/3125.

struct Action { int A,B,dh,c,m; };
struct Jet { long long v; int leftSlope240, rightSlope240; };

static vector<Action> makeQ24(bool addOffgrid=false) {
    vector<Action> out;
    out.reserve(addOffgrid ? 626 : 625);
    for (int i=0;i<=24;++i) for (int j=0;j<=24;++j) {
        const int A=10*i, B=10*j;
        out.push_back({A,B,(9*A+11*B)/10,(11*A+9*B)/10,max(A,B)});
    }
    if (addOffgrid) out.push_back({6,236,265,219,236});
    return out;
}

static inline long long zeroTail(const vector<long long>& phi, int cutoff, int D) {
    return D<cutoff ? phi[D] : 0LL;
}

int main() {
    constexpr int START_D=480; // D=2.

    // ------------------------------------------------------------------
    // B12: exact finite-support Q=24 robust fixed point at epsilon0.
    // ------------------------------------------------------------------
    constexpr long long P0=11, R0=13630; // epsilon0=P0/R0.
    const auto q24=makeQ24(false);
    assert(q24.size()==625);

    constexpr int MAXD0=4000;
    vector<long long> prev(MAXD0+1,0), cur(MAXD0+1,0);
    int stableH=-1;
    for (int h=1;h<=300;++h) {
        bool changed=false;
        for (int D=0;D<=MAXD0;++D) {
            long long best=0; // zero action is legal.
            for (const auto& ac:q24) {
                const long long penalty=P0*ac.m;
                long long vH=(9LL*ac.A*R0)/10-penalty;
                const int DH=D+ac.dh;
                if (DH<=MAXD0) vH+=prev[DH]; // outside => optional stop.

                int DL; long long immediateL;
                if (D>=ac.c) {
                    DL=D-ac.c;
                    immediateL=(-11LL*ac.A*R0)/10-penalty;
                } else {
                    DL=ac.c-D;
                    immediateL=(9LL*ac.B*R0)/10-1LL*D*R0-penalty;
                }
                const long long vL=immediateL+prev[DL];
                best=max(best,min(vH,vL));
            }
            cur[D]=best;
            if (cur[D]!=prev[D]) changed=true;
        }
        prev.swap(cur);
        if (!changed) { stableH=h; break; }
    }
    assert(stableH==300);

    int lastNonzero=-1;
    for (int D=0;D<=MAXD0;++D) if (prev[D]!=0) lastNonzero=D;
    assert(lastNonzero==2198);
    const int zeroCutoff=lastNonzero+1; // phi(D)=0 for D>=2199.

    // Global fixed-point verification. It suffices to check D through
    // zeroCutoff+480, because every action has c,dh<=480. Beyond that range
    // both continuations lie in the zero tail; the low nonreflection branch
    // has nonpositive immediate reward and the zero action gives exactly 0.
    for (int D=0;D<=zeroCutoff+480;++D) {
        long long best=0;
        for (const auto& ac:q24) {
            const long long penalty=P0*ac.m;
            const long long vH=(9LL*ac.A*R0)/10-penalty
                +zeroTail(prev,zeroCutoff,D+ac.dh);
            int DL; long long immediateL;
            if (D>=ac.c) {
                DL=D-ac.c;
                immediateL=(-11LL*ac.A*R0)/10-penalty;
            } else {
                DL=ac.c-D;
                immediateL=(9LL*ac.B*R0)/10-1LL*D*R0-penalty;
            }
            const long long vL=immediateL+zeroTail(prev,zeroCutoff,DL);
            best=max(best,min(vH,vL));
        }
        assert(best==zeroTail(prev,zeroCutoff,D));
    }

    const long long oldThreshold=312LL*R0+720LL*P0;
    assert(oldThreshold==4260480);
    assert(prev[START_D]==oldThreshold);

    // ------------------------------------------------------------------
    // B5: exact local parameter slope of the h=255 Q=24 root.
    // For finite action/state/horizon Bellman recursions, the value is
    // continuous piecewise linear in epsilon. Propagate exact one-sided
    // derivatives at epsilon0. Slopes below are derivatives of 240*R wrt
    // epsilon, so dividing by 240 gives dR/d epsilon.
    // ------------------------------------------------------------------
    constexpr int SLOPE_MAXD=3000, SLOPE_H=255;
    vector<Jet> jp(SLOPE_MAXD+1,{0,0,0}), jq(SLOPE_MAXD+1);
    for (int h=1;h<=SLOPE_H;++h) {
        for (int D=0;D<=SLOPE_MAXD;++D) {
            Jet best{0,0,0};
            for (const auto& ac:q24) {
                const Jet childH=(D+ac.dh<=SLOPE_MAXD)?jp[D+ac.dh]:Jet{0,0,0};
                Jet H{
                    (9LL*ac.A*R0)/10-P0*ac.m+childH.v,
                    -ac.m+childH.leftSlope240,
                    -ac.m+childH.rightSlope240
                };
                int DL; long long baseL;
                if (D>=ac.c) { DL=D-ac.c; baseL=(-11LL*ac.A*R0)/10; }
                else { DL=ac.c-D; baseL=(9LL*ac.B*R0)/10-1LL*D*R0; }
                Jet L{
                    baseL-P0*ac.m+jp[DL].v,
                    -ac.m+jp[DL].leftSlope240,
                    -ac.m+jp[DL].rightSlope240
                };

                Jet branch;
                if (H.v<L.v) branch=H;
                else if (H.v>L.v) branch=L;
                else {
                    branch.v=H.v;
                    // min: for t<0 the larger slope is selected; for t>0 the smaller.
                    branch.leftSlope240=max(H.leftSlope240,L.leftSlope240);
                    branch.rightSlope240=min(H.rightSlope240,L.rightSlope240);
                }

                if (branch.v>best.v) best=branch;
                else if (branch.v==best.v) {
                    // max: tie rules reverse those for min.
                    best.leftSlope240=min(best.leftSlope240,branch.leftSlope240);
                    best.rightSlope240=max(best.rightSlope240,branch.rightSlope240);
                }
            }
            jq[D]=best;
        }
        jp.swap(jq);
    }
    const Jet rootJet=jp[START_D];
    assert(rootJet.v==oldThreshold);
    assert(rootJet.leftSlope240==-12910);
    assert(rootJet.rightSlope240==-12910);
    // Therefore dR_255/depsilon=-12910/240=-1291/24, while the transport
    // threshold 13/10+3epsilon has derivative +3. The certified epsilon0 is
    // an intersection inside a differentiable Bellman face, not a Bellman kink.

    // ------------------------------------------------------------------
    // B16: exact denominator-240 symbolic deviation search against phi.
    // Restrict only to actions whose child gaps stay on the 1/240 state
    // lattice: A congruent B (mod 10). This yields 5809 exact candidates.
    // ------------------------------------------------------------------
    vector<Action> candidates;
    for (int A=0;A<=240;++A) for (int B=0;B<=240;++B) {
        if ((B-A)%10!=0) continue;
        candidates.push_back({A,B,(9*A+11*B)/10,(11*A+9*B)/10,max(A,B)});
    }
    assert(candidates.size()==5809);

    long long bestGain=LLONG_MIN, bestV=0, bestH=0, bestL=0, bestBase=0;
    int bestD=-1,bestA=-1,bestB=-1;
    for (int D=0;D<zeroCutoff;++D) {
        for (const auto& ac:candidates) {
            const long long penalty=P0*ac.m;
            const long long vH=(9LL*ac.A*R0)/10-penalty
                +zeroTail(prev,zeroCutoff,D+ac.dh);
            int DL; long long immediateL;
            if (D>=ac.c) {
                DL=D-ac.c;
                immediateL=(-11LL*ac.A*R0)/10-penalty;
            } else {
                DL=ac.c-D;
                immediateL=(9LL*ac.B*R0)/10-1LL*D*R0-penalty;
            }
            const long long vL=immediateL+zeroTail(prev,zeroCutoff,DL);
            const long long v=min(vH,vL);
            const long long gain=v-zeroTail(prev,zeroCutoff,D);
            if (gain>bestGain) {
                bestGain=gain; bestV=v; bestH=vH; bestL=vL;
                bestBase=zeroTail(prev,zeroCutoff,D);
                bestD=D; bestA=ac.A; bestB=ac.B;
            }
        }
    }
    assert(bestGain==51916);
    assert(bestD==2195 && bestA==6 && bestB==236);
    assert(bestH==71006 && bestL==59896 && bestBase==7980);
    // Thus a=6/240=1/40, b=236/240=59/60, D=2195/240=439/48.

    // ------------------------------------------------------------------
    // Metric movement: add only that one off-grid action and certify a
    // stronger rational sensitivity price epsilon1=7/6250.
    // ------------------------------------------------------------------
    constexpr long long P1=7, R1=6250;
    const auto augmented=makeQ24(true);
    assert(augmented.size()==626);
    constexpr int MAXD1=3000, H1=371;
    vector<long long> p(MAXD1+1,0), q(MAXD1+1,0);
    const long long newThreshold=312LL*R1+720LL*P1;
    assert(newThreshold==1955040);
    int firstCross=-1;
    long long root370=-1,root371=-1,checkedStates=0;

    for (int h=1;h<=H1;++h) {
        for (int D=0;D<=MAXD1;++D) {
            long long best=0;
            for (const auto& ac:augmented) {
                const long long penalty=P1*ac.m;
                long long vH=(9LL*ac.A*R1)/10-penalty;
                const int DH=D+ac.dh;
                if (DH<=MAXD1) vH+=p[DH];
                // If DH>MAXD1, continuation is exactly zero: the adversary
                // stops on that branch. This is a legal finite source policy.
                int DL; long long immediateL;
                if (D>=ac.c) {
                    DL=D-ac.c;
                    immediateL=(-11LL*ac.A*R1)/10-penalty;
                } else {
                    DL=ac.c-D;
                    immediateL=(9LL*ac.B*R1)/10-1LL*D*R1-penalty;
                }
                const long long vL=immediateL+p[DL];
                best=max(best,min(vH,vL));
            }
            q[D]=best;
            ++checkedStates;
        }
        p.swap(q);
        const long long root=p[START_D];
        if (root>=newThreshold && firstCross<0) firstCross=h;
        if (h==370) root370=root;
        if (h==371) root371=root;
    }
    assert(firstCross==371);
    assert(root370==1954988 && root370<newThreshold);
    assert(root371==1955058 && root371-newThreshold==18);
    assert(checkedStates==1113371);

    // Source arithmetic.
    long long deltaNum=R1+10LL*P1, deltaDen=10LL*R1;
    long long g=gcd(deltaNum,deltaDen); deltaNum/=g; deltaDen/=g;
    assert(deltaNum==316 && deltaDen==3125);
    const long long upperNum=deltaDen-deltaNum, upperDen=deltaDen;
    assert(upperNum==2809 && upperDen==3125);

    long long widthNum=upperNum*30LL-19LL*upperDen;
    long long widthDen=upperDen*30LL;
    g=gcd(widthNum,widthDen); widthNum/=g; widthDen/=g;
    assert(widthNum==4979 && widthDen==18750);

    long long improveNum=6128LL*upperDen-upperNum*6815LL;
    long long improveDen=6815LL*upperDen;
    g=gcd(improveNum,improveDen); improveNum/=g; improveDen/=g;
    assert(improveNum==1333 && improveDen==4259375 && improveNum>0);

    cout << "I0130_OFFGRID_ROBUST_LIFT_PASS\n";
    cout << "model_math_scope=exact_integer_self_check\n";
    cout << "old_epsilon=11/13630\n";
    cout << "q24_fixed_point_stable_h=" << stableH << "\n";
    cout << "q24_fixed_point_last_nonzero_gap_units=" << lastNonzero << "\n";
    cout << "q24_fixed_point_root=" << prev[START_D] << "/(240*13630)\n";
    cout << "q24_old_threshold=" << oldThreshold << "/(240*13630)\n";
    cout << "q24_root_left_slope=-1291/24\n";
    cout << "q24_root_right_slope=-1291/24\n";
    cout << "denominator240_lattice_aligned_candidates=" << candidates.size() << "\n";
    cout << "best_offgrid_action_a=1/40\n";
    cout << "best_offgrid_action_b=59/60\n";
    cout << "best_offgrid_state_gap=439/48\n";
    cout << "best_offgrid_high_branch_scaled=" << bestH << "\n";
    cout << "best_offgrid_low_branch_scaled=" << bestL << "\n";
    cout << "best_offgrid_base_scaled=" << bestBase << "\n";
    cout << "best_offgrid_one_step_gain_scaled=" << bestGain << "\n";
    cout << "augmented_action_count=" << augmented.size() << "\n";
    cout << "new_epsilon=7/6250\n";
    cout << "optional_stop_gap_domain_max=" << MAXD1 << "/240\n";
    cout << "first_threshold_cross_h=" << firstCross << "\n";
    cout << "root_h370_scaled=" << root370 << "\n";
    cout << "root_h371_scaled=" << root371 << "\n";
    cout << "new_threshold_scaled=" << newThreshold << "\n";
    cout << "new_exact_excess_scaled=" << (root371-newThreshold) << "\n";
    cout << "lifted_delta=316/3125\n";
    cout << "source_valid_upper_bound=2809/3125\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width=4979/18750\n";
    cout << "improvement_over_6128_6815=1333/4259375\n";
    cout << "new_dp_states=" << checkedStates << "\n";
    return 0;
}
