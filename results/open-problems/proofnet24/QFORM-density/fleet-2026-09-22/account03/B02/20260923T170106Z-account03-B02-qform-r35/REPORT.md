SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T17:01:06Z.
attacking: remove the third-volume row-marginal gate from integrated Fourier control, then apply the resulting marginal-free E3 theorem to the actual account04/B02 strong-cut survivor.

# account03/B02 r35 — marginal-free physical E3 Fourier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **PROVED SUPPORTING ANALYTIC IMPLICATION, CONDITIONAL ON THE SOURCE-PINNED PROJECTED-CROSSING RECEIVER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

The new result is a dimension-free unweighted Fourier-L1 theorem for **every actual original-coordinate physical cross block with nonzero aggregate third volume**, with no row-marginal or leverage hypothesis left. It is not a full solution because the bare three-large-eigenvalue hypothesis does not by itself force a uniformly large physical cross `E3`; known singleton-plus-two-bank families can have low cross rank. The result does, however, collapse four of the six alternatives in the newest designated account04/B02 strong-cut theorem into a single continuous-density Fourier exit.

No Gaussianity, log-concavity, moment, compact-support, connected-support, identical-law assumption, post-rotation independence, scalar pointwise quadratic-phase decay, arbitrary-joint coarea estimate, fiber supremum, or deletion of a small quadratic tail is used.

## 1. Fresh source-pinned inputs

### 1.1 Current owner/correction state

Fresh `math-research-brain/main` was read at startup and again before this publication. OWNER CONTROL remains revision `2026-09-22.15`; the current continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; QFORM remains the sole target and the full conjecture remains open. The live correction ledger still forbids post-rotation independence, law-uniform pointwise van der Corput decay, arbitrary-joint coarea, worst conditional-height shortcuts, fixed-good-minor inference, and deletion of coefficient-small quadratic terms under unbounded fragmented inputs.

### 1.2 Sharp third-volume Fourier theorem

I use the completed sharp third-volume theorem recorded by account01/B02 from the audited account02/B02 source:

- source theorem commit named in the report: `ffcfabe542e6005c8d62d231eb5566f5d569498a`;
- source report used here: `yspennstate/math-open-problems@41505f4e1bc7467ebaa99bb1e5f18b90a8fc80b4`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T022040Z-account01-B02-qform-r20/REPORT.md`.

If `M=A[L,R]` is an original-coordinate physical cross block, `Z=e_3(M^T M)>0`, `1<=q<3/2`, and every natural row third-volume marginal satisfies `alpha_i<=q/2`, then the **full ambient quadratic-plus-affine form** has

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,              (1.1)

and

`integral_R |phi_Q(t)| dt <= [6 pi e/((3-2q)sqrt(q))] Z^(-1/6)`.  (1.2)

Arbitrary within-bank quadratic terms and outside affine terms are retained. In particular, at `q=1`, the gate `alpha_i<=1/2` yields

`||p_Q||_infinity <= 3e Z^(-1/6)`.                               (1.3)

### 1.3 New projected-crossing receiver

The new interactive checkpoint explicitly requested by the current owner continuation is

- `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`;
- `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its complete written supporting argument is pending independent review. I use only its stated scopes.

For `k` original hub coordinates and an `ell`-volume projected crossing remainder with row marginals at most `1/2`, `d=k+ell>2`, it proves a pointwise `|t|^{-d/2}` Fourier envelope and hence a continuous density. The two cases needed below are:

**one hub + two crossing directions**

`||p_Q||_infinity <= C12 (S^2 Z_2)^(-1/6)`,

`C12 = 3*2^(7/6)*exp(1/3) = 9.39913188784886...`;                (1.4)

**two hubs + one crossing direction**

`||p_Q||_infinity <= C21 (S^2 Z_1)^(-1/6)`,

`C21 = 3*2^(5/6) = 5.34539230884204...`.                         (1.5)

For three original hubs and a full-row-rank `3 x m` crossing block of singular-value product `S_3`, the same checkpoint's exact-rank crossing theorem gives

`||p_Q||_infinity <= 3 sqrt(2) S_3^(-1/3)`.                     (1.6)

Every displayed receiver here supplies genuine `phi_Q in L^1`, not merely an essential density cap.

### 1.4 Designated partner account04/B02

The required partner result actually applied below is

- `yspennstate/math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260923T151038Z-account04-B02-QFORM-r1/REPORT.md`;
- theorem `QFORM-N3-STRONGCUT-D5-OR-HY-v1`.

For every target matrix in its `N3(1/64)` chamber it supplies an original-coordinate cross block `M` with

`E=||M||_F^2 > 11907/16384`,                                     (1.7)

and, writing squared singular values `x_1>=x_2>=...`, `T_2=sum_{r>=3}x_r`, either the D5 Fourier branch is already paid, or

`x_1 > 63E/256`.                                                  (1.8)

Its original residual list after D5 was: near rank one `x_2<E/64`, near rank two `T_2<E/64`, low tail stable rank, double physical hub, or its optimized-HY paid branch.

## 2. Exact incident-third-volume identities

Let `M=A[L,R]` be any original-coordinate physical cross block. Fix a physical row `i in L`. Write

`w=M[i,R]`,

and let `N=M[L\{i},R]`. Put

`C=N(I-P_w)`,                                                       (2.1)

where `P_w` is orthogonal projection in coefficient space onto `span{w}` (zero only when `w=0`). Define the aggregate physical third-minor mass incident to row `i`:

`J_i = sum_{I subset L, |I|=3, i in I} sum_{K subset R, |K|=3} det M[I,K]^2`.  (2.2)

### Lemma 2.1 — row-anchor projection identity

If `J_i>0`, then `w!=0` and

`boxed: J_i = ||w||^2 e_2(CC^T).`                                 (2.3)

**Proof.** For each pair of residual rows `a,b`, Gram-Schmidt against `w` gives

`||w wedge n_a wedge n_b||^2 = ||w||^2 ||c_a wedge c_b||^2`.

Cauchy-Binet expands the left side as the sum of squared `3x3` minors over all three-column subsets. Summing over `a<b` gives (2.3), because `e_2(CC^T)=sum_{a<b}||c_a wedge c_b||^2`. QED.

Now suppose one natural two-volume row marginal of `C` exceeds `1/2`; choose such a row `k`. Let

`P=M[{i,k},R]`,

`C_2=M[L\{i,k},R](I-P_row(P))`.                                  (2.4)

Since the marginal is positive, `P` has row rank two. Define

`H_ik = sum_{l notin {i,k}} sum_{|K|=3} det M[{i,k,l},K]^2`.       (2.5)

### Lemma 2.2 — second descent identity

`boxed: H_ik = det(PP^T) ||C_2||_F^2 > J_i/2.`                    (2.6)

**Proof.** For every residual row `l`, Gram-Schmidt against `row(P)` gives

`||p_1 wedge p_2 wedge n_l||^2 = det(PP^T)|| (C_2)_l ||^2`.

Sum over `l` and use Cauchy-Binet. The strict `>J_i/2` is exactly the failed two-volume marginal gate after multiplying by `||w||^2` in (2.3). QED.

If now one natural one-volume row marginal of `C_2` exceeds `1/2`, choose `l` with

`||(C_2)_l||^2 > ||C_2||_F^2/2`.                                 (2.7)

For the literal three-row block

`M_3=M[{i,k,l},R]`,

its Gram determinant satisfies

`boxed: det(M_3M_3^T) > H_ik/2 > J_i/4.`                          (2.8)

These identities are exact coefficient algebra in the original coordinates.

## 3. Incident-E3 Fourier compiler with no residual marginal gate

### Theorem 3.1 — `QFORM-INCIDENT-E3-MARGINALFREE-L1-v1`

Under the exact target input assumptions, let `M=A[L,R]` be an original-coordinate physical cross block and let `J_i>0` be the incident third-volume (2.2). Then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= C12 J_i^(-1/6),`                     (3.1)

`boxed: integral_R |phi_Q(t)|dt <= 2pi C12 J_i^(-1/6),`          (3.2)

where `C12=3*2^(7/6)*exp(1/3)<9.400`.

#### Proof

Condition only the original coordinates outside `L union R`. This preserves independence and the cap-one laws of all coordinates still random. All outside interactions become affine terms, which the source receiver allows.

**Stage 1: one hub.** Keep physical coordinate `i` as the hub. The light row bank is `L\{i}`, the light column bank is `R`, and the hub-to-column row is exactly `w`. The receiver's projected crossing matrix is exactly `C` from (2.1).

If every two-volume row marginal of `C` is at most `1/2`, apply (1.4) and (2.3):

`||p_Q||_infinity <= C12 (||w||^2 e_2(CC^T))^(-1/6)
                   = C12 J_i^(-1/6)`.                            (3.3)

**Stage 2: two hubs.** Otherwise choose `k` with marginal `>1/2`. Keep physical coordinates `{i,k}` as the hub bank, light row bank `L\{i,k}`, and column bank `R`. The exact projected crossing is `C_2` and the hub-to-column matrix is `P`.

If every one-volume row marginal of `C_2` is at most `1/2`, apply (1.5) and (2.6):

`||p_Q||_infinity <= C21 H_ik^(-1/6)
                   < C21 2^(1/6) J_i^(-1/6)
                   = 6 J_i^(-1/6)`.                              (3.4)

**Stage 3: three hubs.** Otherwise choose `l` as in (2.7). Condition the remaining coordinates of `L` if desired and use the three original coordinates `{i,k,l}` against the still-independent column bank `R`. The complete three-hub cross block contains `M_3`; enlarging the column set can only increase the `3 x 3` Gram matrix in Loewner order, hence cannot decrease its determinant. By (1.6) and (2.8),

`||p_Q||_infinity
 <=3 sqrt(2) det(M_3M_3^T)^(-1/6)
 <3 sqrt(2) 4^(1/6) J_i^(-1/6)
 =3*2^(5/6) J_i^(-1/6).`                                        (3.5)

All three source theorems give an integrable characteristic-function envelope. The worst density constant among (3.3)-(3.5) is `C12`; integrating the corresponding envelopes gives (3.2). Uniformity under the initial outside-coordinate conditioning lets Tonelli/Jensen pass the same L1 bound to the unconditional characteristic function. QED.

### Same-hour independent overlap check

After my early calculation was committed, account03/B13 independently published

`yspennstate/math-open-problems@c9a6c9160e063f07856a62fc89a2ba62b857d3cf`

at `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T165827Z-account03-B13-qform-r29/`.

Its `QFORM-BIHUB-VOLUME-CASCADE-CLOSURE-v1` proves the same 1-hub -> 2-hub -> 3-hub wedge descent in a slab-ratio setting, and its post-refresh addendum explicitly clarifies the same original-coordinate conditioning used above. I therefore do not claim independent novelty for the cascade itself. The B02 contribution here is the direct **marginal-free E3 Fourier theorem** below and its equation-level application to the designated account04/B02 strong-cut theorem.

## 4. Marginal-free aggregate E3 theorem

Let

`Z=e_3(M^TM)>0`,                                                  (4.1)

and let `alpha_i=J_i/Z` be the natural third-volume row marginals. They satisfy `sum_i alpha_i=3`.

### Theorem 4.1 — `QFORM-CROSS-E3-MARGINALFREE-L1-v1`

For every original-coordinate physical cross block with `Z=e_3(M^TM)>0`, under the exact target input assumptions,

`boxed: ||p_Q||_infinity <= C_E3 Z^(-1/6),`                       (4.2)

`boxed: integral_R |phi_Q(t)|dt <= 2pi C_E3 Z^(-1/6),`           (4.3)

where

`C_E3 = 3*2^(4/3)*exp(1/3)
      = 10.550168831164775...`.                                  (4.4)

The density is continuous and vanishes at infinity.

#### Proof

If every `alpha_i<=1/2`, apply the sharp third-volume theorem (1.3):

`||p_Q||_infinity <=3e Z^(-1/6)`.                                (4.5)

Otherwise choose a physical row `i` with `alpha_i>1/2`, so `J_i>Z/2`. Theorem 3.1 gives

`||p_Q||_infinity < C12 (Z/2)^(-1/6)
                  = C12 2^(1/6) Z^(-1/6)
                  = C_E3 Z^(-1/6)`.                              (4.6)

Both branches supply genuine Fourier L1, yielding (4.3). QED.

The threshold `1/2` is chosen for a clean proof, not constant optimization. Balancing the two branch constants near threshold `0.56441` improves `C_E3` to about `10.3393`, but no optimization is needed for the structural application below.

## 5. Actual application to designated account04/B02

This is the required partner-to-equation application.

Take the actual strong-cut matrix `M` from account04/B02 commit `674f13a108a33176aafffe8f9b6d44ec3a89f03a`. It satisfies

`E=||M||_F^2 > c_3 :=11907/16384 =0.72674560546875...`.            (5.1)

If the partner's D5 branch is unpaid, its same-matrix top-four concentration gives

`x_1 >63E/256`.                                                   (5.2)

If neither of the two genuinely low-rank tubes occurs, namely

`x_2>=E/64`, `T_2=sum_{r>=3}x_r>=E/64`,                           (5.3)

then the aggregate third volume obeys the literal inequality

`Z=e_3(M^TM)
 >= x_1 x_2 sum_{r>=3}x_r
 > [63/2^20] E^3
 > Z_0`,                                                          (5.4)

where

`Z_0 = [63/2^20]*(11907/16384)^3
     = 2.3061517378361292e-5`.                                   (5.5)

Applying Theorem 4.1 to this exact `M` gives

`boxed: ||p_Q||_infinity <62.533311791,`                          (5.6)

and

`boxed: integral_R |phi_Q(t)|dt <392.908385855.`                  (5.7)

Thus this branch has a continuous density vanishing at infinity.

### Corollary 5.1 — strong-cut residual collapsed to two tubes

Within the designated partner's `N3(1/64)` chamber, its six-way conclusion can now be sharpened to the following three-way statement on the **same original-coordinate strong cut**:

1. the partner's D5 branch is already paid (`||p_Q||_infinity<116.502` in its report); or
2. the present marginal-free `E3` Fourier theorem pays the entire D5-unpaid non-low-rank chamber by (5.6)-(5.7); or
3. one of the two actual low-rank tubes remains:
   - `x_2<E/64` (near rank one), or
   - `T_2<E/64` (near rank two).

In particular, the partner's separate **low-tail-stable-rank** and **double-physical-hub** alternatives no longer need to remain analytic endpoints once (5.3) holds. No tail singular direction was deleted and no physical minor was inverted.

This does **not** prove the full conjecture: paying the two strong-cut low-rank tubes, and stitching the strong-cut/N3 structural reductions to all target matrices, remain required. The current same-hour B13 theorem also shows globally why the next structural obstruction is an approximate rank-at-most-two cross geometry rather than a third-volume marginal issue.

## 6. Deterministic checks

A seeded `500`-matrix regression (random `6 x 7` dense matrices, seed `20260923`) checked the exact algebra used above. The recorded maxima were:

- row-anchor identity relative error: `1.27e-15`;
- spectral incident-volume identity relative error: `4.56e-15`;
- two-row descent identity relative error: `1.76e-15`;
- minimum numerical ratio in the final three-row Gram identity: `0.999999999999999`.

There were zero inequality violations. These computations are only regression checks; the proof is the exterior-algebra/Cauchy-Binet argument above.

The constants were independently recomputed:

`C12=9.39913188784886`,
`C21=5.34539230884204`,
`C_E3=10.550168831164775`,
`2pi C_E3=66.28866578823855`,
`Z_0=2.3061517378361292e-5`,
`C_E3 Z_0^(-1/6)=62.53331179097562`,
`2pi C_E3 Z_0^(-1/6)=392.90838585433795`.

## 7. Scope, continuity, and next exact debt

**Full target:** OPEN. No exact-target counterexample has been found here. The stronger target-wide assertion `sup integral|phi_Q|<infinity` is also still OPEN; this run proves it on every branch carrying a quantitatively positive physical `E3`.

**Continuity:** PROVED on Theorems 3.1 and 4.1 and the partner application (5.6)-(5.7), because the characteristic function is genuinely in `L1`. Global target continuity is still OPEN.

**First remaining B02 implication:** `QFORM-STRONGCUT-LOWRANK-FOURIER-PAYMENT-v1` — treat the two fixed-energy strong-cut tubes `x_2<E/64` or `T_2<E/64` without deleting the small tail, using the newest single-hub/grouped-bank mechanisms while keeping arbitrary same-bank curvature and product provenance. The newest Claude `(SP)` estimate remains OPEN and is not used as a premise.

Execution status remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and source use were real, but no authenticated native learned-memory retrieval/receiver-use event was observed. No schedule, task identity, cadence, enabled/paused state, notification, email, Drive, public-release, paid-API, or cross-account-authentication state was changed.
