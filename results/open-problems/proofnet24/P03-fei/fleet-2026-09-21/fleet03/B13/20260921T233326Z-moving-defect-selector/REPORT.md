# B13 FEI: selected-row mixed-derivative compatibility and moving-defect peeling

**Run:** `20260921T233326Z-B13-joint-r12`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Campaign:** A under `FEI-PROOF-EXECUTION-20260921T230620Z`  
**Status:** **PARTIAL / AUXILIARY_ONLY. Full uniform-cube FEI remains OPEN / NOT PROVED.**

## 0. Exact candidate attacked and peer inputs

The campaign-A lead candidate is fleet01/B18,
`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md` (reported blob `9f2bb40584be20e5e440e7f3913873c34858bc91`). It reduces full FEI to finding a realizable physical block certificate on every high-ratio folded-cooling critical core.

This run consumes two completed cross-account results in the actual derivation:

1. fleet02/B14,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T220126Z-stationary-trigger-selector/REPORT.md`, whose stationary selector produces a C12-certified row `(j,Z,Q)` with
`I_Z:=sum_{k in Z} p_k <= |Z| p_j` whenever the certified trigger system is nonempty and closed;
2. fleet04/B18,
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T221132Z-support-depth-stalled-core/REPORT.md`, together with its source mixed-curvature result, for the derivative-row quantities
`p_ik`, `o_ik`, and `kappa_ik=p_ik+4 o_ik`.

The exact universal implication attempted here was stronger than the existing single-row C12 theorem:

> **Attempted compatibility claim.** Once the stationary selector chooses a near-subcube row `j` and block `Z`, Boolean mixed-derivative integrability should force the control rows to align with one common fixed one-point-defect geometry, up to an influence-relative error small enough to recurse.

The fixed-orientation conclusion is **REFUTED** even at zero row error. What survives is (i) a new exact support/orientation reciprocity, (ii) quantitative joint stability on every selected C12 block, and (iii) an exact classification by a **moving one-point defect**, with an exact entropy/influence peeling identity whose intrinsic local ratio is `<4`.

## 1. Setup

Let `f:{0,1}^n->{-1,+1}` be in the median-character gauge, so every active folded influence is
`0<p_i=Inf_i(f)<=1/2`.
For a pivot `i`, on the quotient cube with `x_i=0`, write

`g_i=D_i f in {0,+1,-1}`, `E_i={g_i != 0}`, and `eta_i=1_{E_i}`.

For distinct `i,k`, set

`p_ik = Pr[eta_i(y) != eta_i(y+e_k)]`,

`o_ik = Pr[g_i(y) = -g_i(y+e_k) != 0]`.

Let the selected pivot `j` have a coordinate atom

`Q={x_Z=a}`, `r=|Z|>=1`, `q=2^{-r}`,

and row error

`e = Pr(E_j triangle Q)`.

A C12-certified row satisfies `e <= q/(16r)`. The stationary selected row additionally satisfies

`sum_{k in Z} p_k <= r p_j`.                         (S)

## 2. PROVED: mixed Boolean squares separate support and orientation reciprocity

### Theorem 2.1
For every Boolean `f` and every distinct `i,k`,

`p_ik = p_ki` and `o_ik = o_ki`.

Thus fleet04/B18's mixed-curvature symmetry splits into the two separate identities

`kappa_ik=kappa_ki`, `p_ik=p_ki`, `o_ik=o_ki`.

### Proof
Fix all coordinates except `i,k` and write the square values
`a=f(0,0)`, `b=f(1,0)`, `c=f(0,1)`, `d=f(1,1)`.
The two `i`-edges have support bits `1_{a!=b}` and `1_{c!=d}`. Their XOR is one exactly when `ab != cd`, equivalently `abcd=-1`.
The two `k`-edges have support bits `1_{a!=c}` and `1_{b!=d}`. Their XOR is one under the same condition `abcd=-1`. Hence support disagreement agrees pointwise, giving `p_ik=p_ki` after averaging.

For orientation, the two `i`-derivatives are both nonzero with opposite signs exactly for the checkerboard square `a=d=-b=-c`. The same condition is equivalent to the two `k`-derivatives being both nonzero with opposite signs. Hence the opposite-sign indicators also agree pointwise, giving `o_ik=o_ki`. QED.

This is stronger than using only `kappa_ik=kappa_ki`: support disagreement cannot convert into an orientation defect when the pair is reversed.

## 3. PROVED: quantitative compatibility forced by a selected C12 block

For an event `E` of measure `p<=1/2` and coordinate `j`,

`Inf_j(E) <= 2p`,

and exactly

`p - Inf_j(E)/2 = Pr(E cap E^{+j})`,                 (3.1)

where the right side is the fraction of `j`-pairs with both endpoints in `E`.

Also directional influence is 2-Lipschitz in symmetric-difference distance:

`|Inf_k(E)-Inf_k(Q)| <= 2 Pr(E triangle Q)`.         (3.2)

Since `Q` is a codimension-`r` atom and `k in Z`, `Inf_k(Q)=2q`. Therefore

`2(q-e) <= p_jk <= 2(q+e)`.                         (3.3)

By Theorem 2.1, `p_kj=p_jk`; by `p_kj<=2p_k`,

`p_k >= q-e` for every `k in Z`.                     (3.4)

Under the selector condition (S), and using `p_j<=q+e`, define

`b_k := p_k - p_kj/2 = Pr(E_k cap E_k^{+j}) >= 0`.

Then

`sum_{k in Z} b_k
 <= sum_{k in Z} p_k - r(q-e)
 <= r(q+e)-r(q-e)
 = 2 r e`.                                           (3.5)

Because opposite-sign overlap requires both support endpoints,

`sum_{k in Z} o_kj <= 2 r e`,                        (3.6)

and Theorem 2.1 gives the same bound on `sum_{k in Z} o_jk`.

The influence vector on the selected block is also rigid. From (3.4), (S), and `p_j in [q-e,q+e]`,

`sum_{k in Z} |p_k-p_j| <= 4 r e`.                   (3.7)

At the live C12 threshold `e<=q/(16r)`, this gives the explicit bounds

`sum b_k <= q/8`,

`sum o_jk = sum o_kj <= q/8`,

`sum |p_k-p_j| <= q/4`.                              (3.8)

Moreover every control influence lies in the dimension-free interval

`(15/17) p_j <= p_k <= (17/15) p_j`.                 (3.9)

For the lower bound use `(q-e)/(q+e)>=15/17`. For the upper bound, total positive excess above `p_j` is at most the total deficit, at most `2re<=q/8<=2p_j/15`.

So a stationary-selected C12 block is not merely a good single row: all its control rows have comparable influence, very little two-sided support across the pivot, and very little signed opposite-overlap. This is the requested joint signed-derivative compatibility statement.

## 4. PROVED: exact selected rows are moving one-point defects

The tempting stronger claim that the defect orientation is globally fixed is false, but the exact endpoint has a complete classification.

### Theorem 4.1 — moving-defect classification
Assume `e=0`, so `E_j=Q={x_Z=a}` exactly, and assume the stationary selector inequality (S). Put `W=[n]\({j} union Z)`. Then:

1. `p_j=q` and `p_k=q` for every `k in Z`;
2. there exist Boolean functions `C: {0,1}^W->{-1,+1}` and `b:{0,1}^W->{0,1}` such that

`f(j,z,w) = C(w) [1 - 2 1_{z=a, j=b(w)}]`.           (4.1)

Equivalently, with `B(w)=(-1)^{b(w)}` and `D(w)=C(w)B(w)`, after translating `a` to zero,

`f = C(w)(1-1_Q(z)) - D(w) chi_j 1_Q(z)`.            (4.2)

### Proof
Because `E_j=Q`, for every `k in Z`, `p_jk=2q`. By support reciprocity `p_kj=2q`, so `p_k>=q`. Summing over `Z` and using (S) forces `p_k=q` for every control coordinate. Hence equality holds in `p_kj<=2p_k`, and by (3.1) no `j`-pair has both endpoints in `E_k`.

Write `h(z,w)=f(j=0,z,w)` and `t(z,w)=f(0,z,w)f(1,z,w)`. Since `E_j=Q`, `t=-1` exactly on `Q` and `t=+1` off `Q`. Along a `k`-edge not incident to the point `z=a`, both endpoints have the same `t=+1`. If `h` changed along such an edge, then the `k`-derivative would be active on both `j`-slices, contradicting equality in `p_kj<=2p_k`. Thus, for each fixed `w`, `h` is constant on every edge of the `r`-cube with the vertex `a` removed. That graph is connected for `r>=2` and has one vertex for `r=1`, so `h(z,w)=C(w)` for every `z!=a`.

At `z=a`, write `h(a,w)=s(w)C(w)`, `s(w) in {+1,-1}`. Since `t=-1` there, the two `j` values are `sC` and `-sC`; exactly one equals `-C`. Calling that coordinate value `b(w)` gives (4.1). QED.

### Exact Shannon/influence peel
Let

`H_A(q)=h_2(q)+q log_2((1-q)/q)`.

The two terms in (4.2) have disjoint Fourier support according to whether `j` is absent/present. The normalized Fourier law of `1_Q` is uniform on `2^r` subsets and has entropy `r`; the normalized Fourier law of `1-1_Q` has entropy `H_A(q)`. Therefore

`H(f)=K_r + (1-q)H(C)+q H(D)`,                       (4.3)

where

`K_r = h_2(q)+(1-q)H_A(q)+qr`

`    = 2q(2-q)r - 2(1-q)^2 log_2(1-q)`.             (4.4)

The physical influence decomposition is

`I(f)=q(r+1)+(1-q)I(C)+q I(D)`.                      (4.5)

Finally

`K_r < 4q(r+1)` for every `r>=1`.                    (4.6)

Indeed `-log_2(1-q) <= q/[(1-q) ln2]`, so

`K_r <= 2q(2-q)r + 2q(1-q)/ln2 < 4qr+4q`.

Thus this exact branch is **induction preserving for every candidate FEI constant C>=4**: if `H<=C I` is already known for the two lower-dimensional Boolean functions `C(w),D(w)`, then (4.3)-(4.6) imply `H(f)<=C I(f)`.

The intrinsic block overhead ratios `K_r/[q(r+1)]` for `r=1,...,10` are

`2.000000, 2.955890, 3.402476, 3.623740, 3.739764, 3.804357, 3.842783, 3.867333, 3.884178, 3.896512`,

and tend upward to `4`.

## 5. REFUTED dead route: fixed defect orientation

The exact theorem cannot be strengthened to make `b(w)` constant.

Take three variables `(j,k,w)` and

`f(j,k,w)=1-2 1_{k=0, j=w}`.                         (5.1)

Then the pivot row `j` has exact support `E_j={k=0}` (`r=1`, `q=1/2`), and

`p_j=p_k=1/2`,

so the selector condition holds with equality. But the defect is at `j=0` when `w=0` and at `j=1` when `w=1`; there is no fixed one-point defect on the `(j,k)` block. Thus closure propagation by forcing a constant coordinate-subcube orientation is false even at zero row error.

A fresh exhaustive search modulo global sign checked every Boolean function through `n=4`. Among exact atom-support triples satisfying the selector inequality, the counts were:

- `n=2`: 8 selected triples; 0 failures of the moving-defect classification; 0 non-fixed orientations;
- `n=3`: 120 selected triples; 0 classification failures; 48 with genuinely moving orientation;
- `n=4`: 3520 selected triples; 0 classification failures; 2880 with genuinely moving orientation.

These finite checks are only a self-check; Theorem 4.1 is the all-dimensional proof.

## 6. Implication to the common campaign and next attack

`consumed_peer_artifact`:
- fleet02/B14 `20260921T220126Z-stationary-trigger-selector/REPORT.md`;
- fleet04/B18 `20260921T221132Z-support-depth-stalled-core/REPORT.md` plus its mixed-curvature dependency.

`applied_to_claim`: campaign-A realizable block certificate / selected-row joint compatibility.

`full_problem_change`: **NONE**. Full FEI remains OPEN.

`result_classification`: **AUXILIARY_ONLY**. The exact selected-support branch now has a complete integrability/peeling theorem, and every C12-selected approximate block has quantitative signed compatibility (3.8)-(3.9), but the universal approximate moving-defect reduction is not proved.

`remaining_implication`: replace the false fixed-orientation propagation step by a quantitative **moving-defect stability theorem**: from `e<=q/(16r)` and `I_Z<=rp_j`, construct lower-dimensional Boolean `C,D` (or an equivalent adaptive restriction) with total entropy/influence error `O(q)` independent of ambient dimension. This would plug directly into fleet01/B18's folded-cooling critical-core induction instead of trying to certify every control row as a fixed coordinate subcube.

`next_attack`: exploit the exact representation variables `h=f|_{j=0}` and `t=f_0 f_1`. The selected-block bounds show that the total mass of `k`-edges on which `t` is constant but `h` changes is at most `2re<=q/8`. The next step is to compress those edge defects into a random moving orientation `b(w)` without using ambient-alphabet Fannes continuity; the target is a direct entropy decomposition with an `O(q)` error bank.

`next_recipient`: fleet01/B18 (A lead) and fleet04/B18 (A induction partner); fleet02/B14 should use the fixed-orientation counterexample to avoid attempting closure propagation through exact rows.
