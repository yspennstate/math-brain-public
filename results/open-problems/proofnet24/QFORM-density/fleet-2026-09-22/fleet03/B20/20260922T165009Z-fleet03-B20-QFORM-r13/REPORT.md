# fleet03/B20 QFORM r13 — nested original-coordinate resource extraction

**Status:** `NEW UNIVERSAL REDUCTION IN THE CURRENT UNRESOLVED BRANCH / FULL TARGET OPEN`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Owner control used:** `QFORM-DENSITY-3EIG-20260922`, live revision `2026-09-22.7`, including `QFORM-PROOF-FIRST-20260922T161801Z`.  
**Model self-report:** GPT-5.6 Sol. Requested reasoning: highest exposed/supported. Configured/provider reasoning counters: `UNKNOWN / NOT_EXPOSED`.

## 1. Exact target and inherited current branch

The full target is: for independent real coordinates with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal `L^infinity` density bound for `Q=X^TAX`, or give a genuine counterexample. No moment, log-concavity, compact-support, diagonal-basis, or post-rotation independence assumption is used below.

I use the completed fleet03/B19 reduction `QFORM-SCHUR-CROSS-LOWRIDGE-STABILITY-v1` / r14 only for its already-paid complement: every still-unresolved target candidate satisfies, for

`H = A - diag(A)`,

` s_2(H) > 3/20. `

The point of this run is to solve the next *resource-extraction* implication without asking for one good principal minor or a rank-three single cut. The latter is source-validly refuted by the singleton-plus-two-banks family in the correction ledger.

## 2. Theorem: nested-cut three-resource reduction

### Theorem `QFORM-NESTED-CUT-THREE-RESOURCE-v1`

Let `A` be a real symmetric matrix with `s_3(A)>=1`, where singular values are decreasing, and put `H=A-diag(A)`. Assume

` s_2(H) > 3/20. `

Then there is a partition of the **original physical coordinates** into `L disjoint_union R`, with cross block `C=A[L,R]=H[L,R]`, for which one of the following three alternatives holds.

1. **Two-direction cross bank:**

   `s_2(C) >= 3/160`.

   Hence both `s_1(C),s_2(C)` are at least `3/160`.

2. **Outer cross bank plus physical pivot:**

   `s_1(C) > 9/160`, and one of the two sides, say `S in {L,R}`, contains an original coordinate `i` with

   `|A_ii| >= 157/320`.

3. **Nested three-bank form:**

   `s_1(C) > 9/160`, and one side `S in {L,R}` admits a further partition `S=S_1 disjoint_union S_2` such that

   `s_1(A[S_1,S_2]) > 157/640`.

Thus every unresolved candidate has either two quantitatively nontrivial singular directions in one product-preserving cross bank, or a quantitatively nontrivial outer bilinear bank together with a third resource that is either a physical square or a second bilinear bank on a nested disjoint physical partition. No rotated coordinate is declared independent.

### Proof

Let `epsilon=(epsilon_1,...,epsilon_n)` have independent Rademacher signs and `D_epsilon=diag(epsilon)`. Define

`M_epsilon = (H-D_epsilon H D_epsilon)/2`.

Because `H` has zero diagonal, for `i!=j`

`(M_epsilon)_ij = H_ij (1-epsilon_i epsilon_j)/2`.

If `L={i:epsilon_i=1}` and `R={i:epsilon_i=-1}`, then, after reordering coordinates,

`M_epsilon = [[0,C],[C^T,0]]`, `C=H[L,R]`.

The nonzero singular values of `M_epsilon` are the singular values of `C`, each repeated twice. Therefore

`||M_epsilon||_(4) = 2(s_1(C)+s_2(C))`,

where `||.||_(4)` is the Ky–Fan four-norm. Also

`E M_epsilon = H/2`.

Ky–Fan norms are convex, so Jensen gives

`E ||M_epsilon||_(4) >= ||E M_epsilon||_(4)
 = (1/2) sum_{j=1}^4 s_j(H)`.

Consequently some physical cut satisfies

`2(s_1(C)+s_2(C)) >= (1/2) sum_{j=1}^4 s_j(H)`,

hence

` s_1(C)+s_2(C) >= (1/4)sum_{j=1}^4s_j(H)
                   >= (s_1(H)+s_2(H))/4
                   > 3/40. `                                           (2.1)

If `s_2(C)>=3/160`, alternative 1 holds.

Assume instead `s_2(C)<3/160`. From (2.1),

` s_1(C) > 3/40-3/160 = 9/160. `                         (2.2)

Take a top singular pair `u,v` and write

`C=sigma u v^T+E`, `sigma=s_1(C)`, `||E||=s_2(C)<3/160`.

Set

`K=[[0,sigma u v^T],[sigma v u^T,0]]`.

Then `rank(K)<=2`. Since `s_3(A)>=1`, the spectral-norm Eckart–Young inequality gives, for *every* rank-at-most-two matrix and therefore for this `K`,

` ||A-K||_op >= s_3(A) >=1. `                              (2.3)

In the same `L/R` ordering,

`A-K = [[A_LL,E],[E^T,A_RR]]`.

Let `B=diag(A_LL,A_RR)`. Since

`||(A-K)-B||_op = ||[[0,E],[E^T,0]]||_op = ||E|| <3/160`,

(2.3) implies

` max(||A_LL||_op,||A_RR||_op)=||B||_op >1-3/160=157/160. `       (2.4)

Choose a side `S` whose principal block `A_SS` has norm `>157/160`. If

`max_{i in S}|A_ii| >=157/320`,

then (2.2) gives alternative 2.

Otherwise let

`J=A_SS-diag(A_SS)`.

Then

`||J||_op >= ||A_SS||_op-||diag(A_SS)||_op >157/320`.             (2.5)

Apply the same random-sign cut inside the **original coordinate set** `S`. For signs `eta` on `S`,

`N_eta=(J-D_eta J D_eta)/2`

is a cross-only matrix for a physical partition `S=S_1 disjoint_union S_2`, with

`||N_eta||_op=s_1(J[S_1,S_2])`,

and `E N_eta=J/2`. Convexity of the operator norm and (2.5) yield a cut with

` s_1(A[S_1,S_2]) = s_1(J[S_1,S_2])
  >= ||J||_op/2 >157/640. `

Together with (2.2), this is alternative 3. The theorem is proved. `square`

## 3. Why this is compatible with the correction ledger

The theorem does **not** assert any of the refuted statements “one good principal minor,” “one rank-three cut,” or “one fixed pair captures a constant fraction of an aggregate.” In the rank-one-dominant outer-cut case it explicitly allows the third resource to remain inside one whole side and then extracts it by a second **group cut**. This is exactly the shape needed to survive the singleton-plus-two-banks correction family.

The theorem also never rotates the random vector. SVD vectors are used only to form the rank-two comparison matrix `K`; the actual banks `L,R,S_1,S_2` are subsets of original coordinates, so product independence between disjoint banks remains available to subsequent analytic steps.

## 4. Assigned partner fleet04/B20 actually applied

The completed fleet04/B20 theorem at `yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f` gives the exact original-coordinate conditioning/whitening rule. In the high spectral window used in B20 r12, with `P=UU^T`, conditioning a physical set `G` gives

`S_G=I-U_G^TU_G`,

and every unconditioned row has whitened leverage

`ell_i=u_i^T S_G^{-1}u_i`.

Hence, whenever `S_G >= I/2` and `P_ii=||u_i||^2<=1/64` for every `i notin G`, the partner inequality is applied exactly as

`ell_i <= ||S_G^{-1}|| P_ii <= 2(1/64)=1/32`.                 (4.1)

The partner theorem then closes the conditioned spectral core; the already-proved B20-r12 small-tail splice upgrades this to the exact target matrix with a continuous density and the archived bound `<194`.

Apply (4.1) to the *physical banks produced by the new theorem*. For the outer cut `L/R`, an unresolved candidate must satisfy both localization alternatives

`||U_L^TU_L||_op>1/2  OR  max_{i in R} P_ii>1/64`,

`||U_R^TU_R||_op>1/2  OR  max_{i in L} P_ii>1/64`.             (4.2)

Indeed, if the first disjunction failed, condition `G=L`; then `S_G>=I/2` and all residual rows satisfy (4.1), so the partner/B20-r12 branch closes. The second follows by swapping the sides. The same test applies to either nested bank in alternative 3.

Thus the new resource extraction is not merely spectral bookkeeping: after the designated partner theorem, every surviving two-bank or three-bank resource is forced to coexist with a concrete high-window localization certificate. This is the source-compatible branch that remains to be paid analytically.

## 5. Fresh compatible cross-account result consumed

Fresh fleet02/B01 r24 (`math-open-problems@007d06d8118bc87becd247676c7a63ae336755c9`) proves that a heavy rank-two residual row can be conditioned when its whitened tail is diffuse, and gives an explicit family where every fixed physical-pair certificate shrinks to zero. The nested-cut theorem above is designed around that falsifier: alternative 3 retains a whole grouped bank rather than choosing a pair.

## 6. What is and is not proved

**Proved this run:** the exact three-way product-preserving reduction above, with universal constants `3/160`, `9/160`, `157/320`, `157/640`, and the partner-forced localization conditions (4.2).

**Not proved:** that alternatives 1–3 themselves imply the universal density bound without additional analytic work. In particular, a single bilinear bank has a logarithmic singularity, so alternative 2 cannot be closed merely by counting it as two eigenvalues. The next argument must exploit the physical pivot or the nested third bank without discarding dependence-producing self terms.

**Continuity:** no new full-branch continuity theorem is claimed. The partner/B20-r12 diffuse branch used in (4.1)–(4.2) has a continuous `C_0` density; the new residual branches remain open.

**Full QFORM:** `OPEN / NOT PROVED / NOT DISPROVED`.

## 7. First unpaid implication

`QFORM-NESTED-BANK-ANALYTIC-PAYMENT-v1`:

Prove a dimension-free density estimate for either

- a physical pivot `|A_ii|>=157/320` together with an outer cross bank `s_1>9/160`, or
- the nested three-bank configuration with outer `s_1>9/160` and inner `s_1>157/640`,

under the forced localization alternatives (4.2), while retaining all self blocks and arbitrary remaining spectral components. A valid route may use the current fractional-trace / dependent-square machinery, but it must not replace the original-coordinate banks by independent rotated eigen-coordinates.
