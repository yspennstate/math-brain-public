# fleet02/B12 — hostile-sign spectral-budget stability for redundant physical triples

**Run:** `20260922T215532Z-fleet02-B12-QFORM-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`  
**Owner control observed:** revision `2026-09-22.15` at brain commit `87b38a1e34c9b77a03d34ab98d35df8813d7fb0b`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED_SUPPORTING_THEOREM + SHARP MECHANISM BARRIER / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-22T21:55:32Z.
attacking: redundant physical-core survival under arbitrary signed spectral additions; quantify how many disjoint source-valid certificates are needed to absorb a hostile-sign spectral budget without rotating the product source.

## 1. Target and source discipline

The target is unchanged: for independent real inputs with densities at most one and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal `L^infinity` density bound for `X^T A X`, or exhibit a valid counterexample. No moments, support bounds, rotation-independence, or post-rotation convolution are assumed.

This report uses only original-coordinate principal blocks. It respects the live corrections against pointwise oscillatory decay, fiber-sup dimension-free bounds, false post-rotation independence, fixed cross-minor closure, single-Schur rank-two extraction, and exact-bank universal extraction.

The completed assigned-partner result actually used is fleet03/B12, theorem `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`, canonical source

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

It proves: if one physical original-coordinate `3 x 3` principal block has two eigenvalues at least `L>0`, or two eigenvalues at most `-L`, then after conditioning all outside original coordinates,

`||p_Q||_infinity <= C_*/L`,

where

`C_* = 2*pi + 3*sqrt(3) + sqrt((2*pi+3*sqrt(3))^2+3*pi^2)`

`=24.183038289961516...`.

All outside quadratic coefficients, signs, magnitudes and cross couplings are arbitrary. This is precisely source-valid for the present reduction because the conditioning is on original independent coordinates.

## 2. First unpaid implication attacked

A single definite physical triple is stable under one arbitrary hostile rank-one perturbation, but a bare three-large-eigenvalue hypothesis need not supply such a triple. A natural next question is whether **many disjoint definite physical triples** can absorb many arbitrary added eigendirections without paying the largest added eigenvalue.

The answer is quantitative: same-sign added spectrum is completely free; opposite-sign added spectrum is paid only through the second local hostile eigenvalue, and disjointness averages that cost with an exact factor `1/(2K)`. Rank one is free at every magnitude. The factor is sharp for this certificate family, already for a rank-two hostile perturbation.

## 3. Hostile-sign local lemma

Let `B_0` be real symmetric `3 x 3` with

`B_0 >= L I_3`, `L>0`.

Let an added perturbation on this block be written

`E = G - H`,

with `G,H >=0`. Write the eigenvalues of `H` as

`mu_1(H) >= mu_2(H) >= mu_3(H) >=0`.

Then

`B_0+E >= L I_3-H`.

By monotonicity of ordered eigenvalues under Loewner order,

`lambda_2(B_0+E) >= lambda_2(L I_3-H) = L-mu_2(H)`.              (3.1)

Therefore, whenever `mu_2(H)<L`, the final block has two positive eigenvalues at least `L-mu_2(H)`. Applying the fleet03/B12 theorem gives

`||p_Q||_infinity <= C_* / (L-mu_2(H))`.                        (3.2)

The sign-reversed statement is identical: if `B_0 <= -L I_3`, then only the positive part of the added perturbation is hostile.

Two consequences are immediate.

* Any same-sign positive-semidefinite addition is free, regardless of rank and magnitude.
* Any hostile rank-one addition is also free, regardless of magnitude, because every `3 x 3` compression of a rank-one positive-semidefinite matrix has `mu_2=0`.

Thus one arbitrarily large opposite-sign eigendirection plus arbitrarily many arbitrarily large same-sign eigendirections cannot worsen the partner constant around a physical definite triple.

## 4. Disjoint-triple spectral-budget theorem

### Theorem — `QFORM-DISJOINT-TRIPLE-HOSTILE-KYFAN-v1`

Let `T_1,...,T_K` be pairwise-disjoint triples of original coordinates. Fix `sigma in {+1,-1}` and suppose

`sigma A_0[T_j,T_j] >= L I_3`                                    (4.1)

for every `j=1,...,K`.

Let the added symmetric matrix be `E`, and decompose its sign relative to `sigma` by

`sigma E = G-H`, `G,H >=0`.                                     (4.2)

Equivalently, `G=(sigma E)_+`, `H=(sigma E)_-`. Define the hostile spectral mass

`N_- = tr H = sum_{sigma*tau_l<0} |tau_l|`,                     (4.3)

where `tau_l` are the eigenvalues of `E`.

If

`N_- < 2 K L`,                                                   (4.4)

then for the full matrix `A=A_0+E`, and every independent cap-one product source,

`||p_{X^T A X}||_infinity <= C_* / (L-N_-/(2K))`.               (4.5)

No restriction is imposed on the same-sign eigenvalues of `E`: they may be arbitrarily many and arbitrarily large. The hostile eigenvalues may also be individually arbitrarily large; only their total hostile mass enters (4.5).

#### Proof

For each `j`, let

`H_j=H[T_j,T_j] >=0`,

and let `eta_j=mu_2(H_j)` be its second-largest eigenvalue. Since a positive semidefinite `3 x 3` matrix has

`tr H_j >= 2 eta_j`,                                             (4.6)

and the triples are disjoint,

`2 sum_j eta_j <= sum_j tr H_j <= tr H = N_-`.                  (4.7)

Hence some `j_*` satisfies

`eta_{j_*} <= N_-/(2K)`.                                        (4.8)

On this triple,

`sigma A[T_{j_*},T_{j_*}]`
` = sigma A_0[T_{j_*},T_{j_*}] + G[T_{j_*},T_{j_*}] - H[T_{j_*},T_{j_*}]`
` >= L I_3-H_{j_*}`.                                            (4.9)

By (3.1), the second-largest eigenvalue of this signed block is at least

`L-eta_{j_*} >= L-N_-/(2K)>0`.                                  (4.10)

Thus the physical block has two same-sign eigenvalues of magnitude at least the right side of (4.10). Apply `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`, conditioning every outside original coordinate. This gives (4.5). No rotation of the input source occurs. QED.

### Small full-rank tail

More generally, if

`sigma E = G-H+S`, `G,H>=0`, `||S||_op<=delta<L`,                (4.11)

then exactly the same proof plus Weyl gives

`||p_Q||_infinity <= C_* / (L-delta-tr(H)/(2K))`                 (4.12)

whenever the denominator is positive. This permits arbitrary large same-sign spectrum, hostile spectral mass, and an arbitrary both-sign small operator-norm tail simultaneously.

## 5. Exact rank-one corollary

If the hostile part `H` has rank at most one, every compression `H_j` also has rank at most one, so `eta_j=0` for every `j`. Therefore one does not need the trace condition (4.4): for any hostile eigenvalue magnitude,

`||p_Q||_infinity <= C_*/L`                                     (5.1)

from any one of the definite triples. With a small tail of norm `delta<L`, the bound is `C_*/(L-delta)`.

This recovers the assigned partner's one-spike stability but places it inside a sign-budget hierarchy that continues to arbitrary-rank additions.

## 6. Sharp mechanism barrier at rank two

The factor `1/(2K)` in (4.5) is exact for the disjoint-certificate averaging step.

Take `n=3K`, `L>0`,

`A_0=L I_n`,

and let

`v_1=K^(-1/2) sum_{j=1}^K e_{3j-2}`,
`v_2=K^(-1/2) sum_{j=1}^K e_{3j-1}`.

The vectors are orthonormal. For `alpha>0` set

`H=K alpha (v_1 v_1^T+v_2 v_2^T)`.                              (6.1)

Then `H>=0`, `rank H=2`, `tr H=2K alpha`, and on every designated triple

`H[T_j,T_j]=alpha diag(1,1,0)`,

so

`mu_2(H[T_j,T_j])=alpha=tr(H)/(2K)`.                             (6.2)

Thus (4.8) is equality simultaneously on every block. At the threshold `alpha=L`,

`(A_0-H)[T_j,T_j]=diag(0,0,L)`                                  (6.3)

for every `j`: every designated definite-triple/two-same-sign certificate collapses at once.

Globally,

`spec(A_0-H)={L (multiplicity 3K-2), -(K-1)L, -(K-1)L}`.         (6.4)

For `K>=2` and `L>=1`, the final matrix is still deep inside the QFORM target class and the two newly added hostile eigenvalues have magnitude `K L`, which is unbounded with `K`. Therefore **rank two is enough to poison arbitrarily many prescribed disjoint definite triples simultaneously**. Redundancy alone, without a hostile-mass/leverage payment or certificate switching, cannot control arbitrary added eigendirections.

This is not a counterexample to QFORM: other physical certificates may remain. It is a sharp counterexample only to the stronger mechanism claim that the prescribed disjoint definite cores remain uniformly useful under arbitrary rank-two spectral completion.

## 7. What changed and what remains

The full conjecture remains OPEN. The new reduction identifies an exact monotone quantity for extra-eigenvalue transport around localized cores:

* same-sign added spectrum: free;
* one hostile eigendirection: free at any magnitude;
* arbitrary hostile spectrum: paid by the second local hostile eigenvalue;
* across `K` disjoint triples: a global hostile trace budget is diluted by the sharp factor `2K`;
* a small arbitrary full-rank tail costs only its operator norm.

The first unpaid implication is structural: derive, from only `s_3(A)>=1`, either an already-paid aggregate/diffuse branch or a family of physical triples/banks whose hostile second-eigenvalue budget is controlled **before** reciprocal local conditioning. The rank-two construction shows that merely counting disjoint definite triples is insufficient when two delocalized hostile directions are allowed; a closure must exploit their global mixed geometry or switch certificates.

## 8. Finite checks

`CHECK.py` verifies the sharp rank-two family for `K=1,...,8`, the exact identity `tr(H)/(2K)=mu_2(H[T_j])`, the final spectrum, and 1600 random positive-semidefinite tests of

`min_j mu_2(H[T_j]) <= tr(H)/(2K)`.

These computations are sanity checks only; the proof above is exact.
