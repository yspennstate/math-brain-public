# Source-bound joint handoff — B17 affine-parity straightening

Source run: fleet02/B17 `B17-20260921T224419Z-r11`.
Scientific source refreshed before persistence: `yspennstate/math-open-problems@04b23c1d04f73bee258b7b69775d3556e63ff032`.

Consumed peer results:
- fleet04/B13 `20260921T2122Z-source-frontier-one-shot`: coordinate-subcube robust one-shot elimination, with arbitrary exceptional mass left unpaid.
- fleet04/B18 `20260921T221132Z-support-depth-stalled-core`: `M=(1/4)sum p_ik` is the unsigned support-depth bank; exceptional/error sector remains live.
- fleet01/B14 `20260921T224055Z-adaptive-pivotality-selector`, blob `585cbdfc282e636c95b70bd479d4c720b19f1948`: adaptive pivotality determination is paid by actual folded-J drift, leaving a corrected-cost selection problem.

New Boolean obstruction:
For
`f_n(x)=(-1)^{sum_i x_i x_{i+1}}`, `n>=5`,
every derivative support is the parity halfspace
`x_{i-1} xor x_{i+1}=1`.
It is distance exactly `1/4` from the nearest coordinate subcube, while
`j_i=1/2`, so every row is exceptional at relative threshold `1/16`.
Nevertheless `p_ik=1` exactly on cycle neighbours, hence `M=J=n/2`, and the
interaction graph is connected.  Thus a bounded `M/J` scalar threshold cannot
by itself force any positive coordinate-subcube robust mass.  This is not an
FEI counterexample.

Replacement theorem:
If a centered derivative support `E_i` is at symmetric-difference error `e`
from an affine parity halfspace on `r` controls, an invertible linear map on
those controls straightens it to a coordinate halfcube, preserves Fourier
entropy, and after character recentering satisfies

    J_new <= J_old + r e <= J_old/(1-2e).

For `e=0`, the operation is free in folded influence.  For `e<=1/34`,
`J_new<=17J_old/16`, the row has relative coordinate-subcube error at most
`1/16`, and the straightened literal-control restriction obeys

    D_control >= 1-3e,
    Delta_control H <= 2,
    Delta_control H <= (68/31) D_control.

Exact elementary shear accounting retains the signed credit:

    I(f o T_{a->b})-J(f)
      = j_a - 2 q_ab
      = j_a - p_ab/2 - 2 o_ab.

Next recipient / exact missing formula:
B13/B18 stability and A-interface selector workers should replace the binary
"near coordinate subcube / exceptional" classifier by a quotient that first
straightens cheap affine-parity rows.  The remaining universal bridge is an
adaptive nonreusing affine-inflation ledger:

    sum_v pi_v c_v <= theta J(root),
    c_v=[J(T_v f_v)-J(f_v)]_+ <= r_v e_v,

combined with paid physical splits
`Delta_v H <= C_0 D_v` and already-paid terminals.
Exact-parity nodes have `c_v=0`, so the cycle obstruction is handled at zero
affine cost.  The approximate amortization is OPEN.

Full FEI remains OPEN / NOT PROVED.
