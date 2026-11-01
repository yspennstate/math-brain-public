SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T00:40:36.798579Z.
attacking: the newest localized/diffuse split with an explicit ACTUAL principal-spectrum gate, and the one-/two-direction hybrid left after the cross-volume payment.

# fleet02/B08 r18 — actual spectral gate, D' payment, and a sharp no-pivot hybrid family

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / REFUTED_STRONGER_DICHOTOMY`  
**Full target:** OPEN / not proved / not disproved  
**Continuity:** not claimed by the new structural splice  
**Execution context:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and source discipline

The target is unchanged: for independent real coordinates with arbitrary probability densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a genuine counterexample. No moments, compact support, log-concavity, identical laws, diagonal-basis product structure, or independence after spectral rotation is used below.

I consumed the current correction set. In particular I do **not** use the false arbitrary-joint coarea bound, the false law-uniform pointwise quadratic-phase decay, positive moments of worst conditional projection-density caps, a uniformly good single physical minor, or a rank-three physical cross-cut dichotomy.

The two source inputs used at equations are:

1. **Designated partner fleet03/B08 r24**, `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`, source `yspennstate/math-open-problems@1bf6f41d81ffddcc6e8ff93b4df165d0ce5bbd05:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T231729Z-fleet03-B08-qform-diffuse-r24/REPORT.md`. It works with three genuine eigenvectors of the full arbitrary matrix and transfers missing ACTUAL principal curvature to singular values of the ACTUAL original-coordinate cross block.

2. **Newest Claude Fourier source**, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, especially Theorem D' and Theorem F. D' is the relaxed volume-sampling Brascamp--Lieb bound; Theorem F is the exact diagonal-plus-diffuse-low-rank Fresnel--Brascamp--Lieb theorem.

The no-pivot reduction used only as a structural gate is the current synthesis `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`. I do not assume its still-open N3 statement.

## 2. The first unpaid implication, stated before the calculation

The latest partner theorem gives a three-unit curvature ledger but does not by itself pay the mixed states in which an actual physical child retains one or two substantial eigenvalues while the cross block carries only the complementary two or one substantial singular directions.

The question for this run is therefore:

> After a genuinely diffuse selected three-eigenvector frame is split into two balanced ORIGINAL-coordinate sides, can the full target be reduced to (i) an ACTUAL three-eigenvalue child, or (ii) a three-singular-direction cross block to which Theorem D' applies, with no one-/two-direction hybrid?

The answer is **no**. I prove the exact spectral gate, pay the zero-child spread-cross branch, and then construct no-pivot matrices with exactly three large eigenvalues showing that the one-/two-direction hybrid is real and rank-sharp even as the selected leverage tends to zero.

## 3. Actual spectral-gate ledger from the designated partner

Let `R` be the `n x 3` matrix of three orthonormal eigenvectors of the actual full matrix `A`,

`A R = R Lambda`,   `min_j |lambda_j| >= L >= 1`.

Assume the selected-frame physical row leverage

`mu := max_i ||R_{i,*}||_2^2 <= 1/48`.

The partner r24 signed physical partition gives a cut `I|J` of the ORIGINAL coordinates such that

`G_I=R_I^T R_I >= (3/8) I_3`,   `G_J=R_J^T R_J >= (3/8) I_3`.

Set

`c_L := (L/2) sqrt(3/5) = 0.387298334620742... L`,

`beta_L := (3/16) sqrt(3/5) L = 0.145236875482778... L`,

and let

`k_I = min(3, #{eigenvalues nu of A[I,I] with |nu| >= c_L})`,
`k_J = min(3, #{eigenvalues nu of A[J,J] with |nu| >= c_L})`.

### Theorem 3.1 — `QFORM-DIFFUSE-ACTUAL-SPECTRAL-GATE-v1`

For `K=I` and `K=J` separately, if `k_K<3`, then the ACTUAL cross block `B=A[I,J]` has

`s_{3-k_K}(B) > beta_L`.

Consequently, with `k=min(k_I,k_J)`,

`k=0  => s_3(B)>beta_L`,
`k=1  => s_2(B)>beta_L`,
`k=2  => s_1(B)>beta_L`,
`k=3  => both physical children have three c_L-large actual eigenvalues`.

#### Proof

Apply partner Theorem 5.1 to side `K` with `m=k_K+1`. By definition the principal-curvature alternative fails: `A[K,K]` has fewer than `m` eigenvalues of modulus at least `c_L`. The partner cross-curvature alternative therefore gives at least

`4-m = 3-k_K`

singular values larger than `beta_L`. Apply this to both sides and retain the stronger conclusion, which is the one corresponding to `min(k_I,k_J)`. No component of `A` has been discarded and no product law has been rotated. QED.

This is the requested **actual spectral gate**: the gate is defined by eigenvalues of actual physical principal matrices, not by eigenvalues of a chosen rank-three component that could be cancelled by the remaining spectrum.

## 4. The zero-child branch is paid by the newest D' theorem

Suppose `k=0`. Then Theorem 3.1 gives `s_3(B)>beta_L`. Put

`Z_3=e_3(B^T B)`.

Since the three largest singular values of `B` exceed `beta_L`,

`Z_3 >= beta_L^6`.                                               (4.1)

Let `alpha_i` be the row marginals of three-volume sampling,

`w_{S,T}=det(B_{S,T})^2/Z_3`, `|S|=|T|=3`,
`alpha_i=P_w(i in S)`.

If either orientation of the cut has maximum three-volume row marginal at most `h=5/8`, apply the completed Claude Theorem D' in that orientation. It gives

`||p_Q||_infinity
 <= 6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z_3^(-1/6)`

` <= 24 sqrt(e/5) / beta_L`

` = 128 sqrt(e/3) / L`

` = 121.841877690545... / L`.                                  (4.2)

This is a genuine full-form density estimate: the same-side blocks, all remaining eigenvalues and arbitrary affine terms are retained by Theorem D'. It applies to the original cap-one product law.

Thus a diffuse balanced cut whose actual principal side has **zero** c_L-large eigenvalues is already paid unless the three-volume itself is physically concentrated on both sides.

### 4.1 What D' failure actually forces

If D' at `h=5/8` fails in both orientations, choose a row `i in I` and a column `j in J` with

`P_w(i in S)>5/8`,  `P_w(j in T)>5/8`.

By the union bound in reverse,

`P_w(i in S and j in T)>1/4`.

Hence the double-incident three-volume bank satisfies

`V_ij := sum_{S contains i, T contains j} det(B_{S,T})^2
       > Z_3/4
       >= beta_L^6/4`.                                         (4.3)

This is an aggregate-before-inversion statement; it does not select one large minor. Also, because the row and column marginals each sum to three, there are at most four `>5/8` rows and at most four `>5/8` columns. The unpaid zero-child survivor is therefore a **double-heavy volume hub**, not an unstructured rank-three cross block.

## 5. Insert the current no-pivot gate: bounded physical cores disappear

Fix the no-pivot scale

`tau_0 = 1/8192`.

Assume only the N3 **matrix inequalities** (not the unproved N3 density assertion):

`|A_ii|<tau_0`,
`|A_ii A_jj - A_ij^2|<tau_0` for every `i != j`.

Then

`|A_ij|^2 <= tau_0^2+tau_0`,

so every off-diagonal entry has magnitude at most

`eps_0 := sqrt(tau_0+tau_0^2)=0.0110492177850377...`.           (5.1)

For a physical principal block on `m` coordinates, Gershgorin / the maximum absolute row sum gives

`||A[K,K]||_op <= tau_0 + (m-1) eps_0`.                         (5.2)

At the target normalization `L>=1`,

`c_L >= c_1 = (1/2)sqrt(3/5)=0.387298334620742...`.

The exact numerical boundary is

`tau_0+35 eps_0 =0.386844692788820... < c_1`,
`tau_0+36 eps_0 =0.397893910573858... > c_1`.

Therefore:

### Corollary 5.1 — `QFORM-N3-ACTUAL-CORE-GATE-v1`

Inside the no-`tau_0`-pivot class, **no physical principal block on at most 36 coordinates has even one eigenvalue of modulus `c_L` or larger**. Any child passing the first actual spectral gate has at least 37 original coordinates.

In particular the newest bounded physical-core example `m<=30` cannot be the terminal mechanism at this scale inside N3. This is not a failure of that finite-core theorem; it says exactly where the live N3 hybrid must sit: its retained curvature is itself physically large-scale.

If additionally the zero-child D' branch fails in both orientations, every entry in the incident bank (4.3) is at most `eps_0` in magnitude. Hadamard's determinant bound gives for each `3 x 3` minor

`|det B_{S,T}| <= (sqrt(3) eps_0)^3 = 3sqrt(3) eps_0^3`,

so a squared minor is at most `27 eps_0^6`. Consequently (4.3) forces more than

`beta_1^6 /(108 eps_0^6)
 = 47758.2522706...`                                             (5.3)

nonzero incident minors. Thus at `tau_0` the D'-escaping zero-child state cannot be a single-minor/local-core phenomenon: at least **47,759** nonzero `3 x 3` cross minors pass through one heavy row and one heavy column.

This is a quantitative source-valid obstruction to reviving a single-good-minor reduction.

## 6. Sharp hybrid witnesses inside the no-pivot class

The remaining `k=1` and `k=2` states are not proof artifacts. They survive with exactly three large eigenvalues, arbitrarily small selected leverage, and arbitrarily small unneeded cross singular values.

Let `m=2^q` and let `U` be the first three columns of the normalized Sylvester Hadamard matrix of order `m`. Thus

`U^T U=I_3`,  `||U_{a,*}||^2=3/m` for every row.

Fix `k in {0,1,2}` and `0<delta<=1/10`. Define

`P_{k,delta}=diag(p_1,p_2,p_3)`,

with the first `k` entries `p_j=1-delta` and the remaining `3-k` entries `p_j=1/5`. Put on `R^m direct_sum R^m`

`A_{m,k,delta} = [[ U P U^T,       U(I-P)U^T ],
                   [ U(I-P)U^T,    U P U^T     ]]`.             (6.1)

### Proposition 6.1 — `QFORM-N3-HYBRID-HADAMARD-SHARP-v1`

The matrices (6.1) have the following exact properties.

1. **Exactly three target-large eigenvalues.** On the plus vectors `(Uv,Uv)/sqrt(2)`, the eigenvalues are `1,1,1`. On the minus vectors `(Uv,-Uv)/sqrt(2)`, the eigenvalues are

`2p_j-1 = 1-2delta` for the first `k` directions and `-3/5` for the others.

All remaining eigenvalues are zero. Since `0<delta<=1/10`, every minus eigenvalue has modulus strictly below one. Hence the matrix has **exactly three** eigenvalues of modulus at least one.

2. **Arbitrarily diffuse selected large eigenspace.** The plus-frame is

`R=(U;U)/sqrt(2)`,

and every physical row has selected leverage

`3/(2m) -> 0`.

The half/half physical cut is perfectly balanced: `G_I=G_J=(1/2)I_3`.

3. **The hybrid rank ledger is sharp.** Each physical child has nonzero eigenvalues `p_j`. Since `1-delta>c_1` and `1/5<c_1`,

`k_I=k_J=k`.

The cross block has singular values

`delta` in the first `k` directions and `4/5` in the remaining `3-k` directions.

Because `delta<beta_1<4/5`, it has **exactly `3-k` singular values above the partner threshold `beta_1`**. The other `k` cross singular values can be sent to zero with `delta`. Thus the implications

`k=1 => two large cross singular directions`,
`k=2 => one large cross singular direction`

cannot be strengthened to a uniform three-singular-direction conclusion, even with selected leverage tending to zero and even with exactly three target-large eigenvalues.

4. **The witnesses lie in N3 at every fixed no-pivot scale.** Every entry of (6.1) has magnitude at most `3/m`, hence every actual physical `2 x 2` principal determinant has magnitude at most `18/m^2`. Therefore for any fixed `tau>0`, every sufficiently large Hadamard order satisfying

`3/m<tau`, `18/m^2<tau`

lies in the strict no-`tau`-pivot class. For `tau_0=1/8192`, the power-of-two choice `m=32768` works.

This proves that the one-/two-direction hybrid is genuinely present in the single remaining N3 class; it cannot be discarded as a finite-dimensional or pivot artifact.

### 6.2 These are mechanism counterexamples, not QFORM counterexamples

The same family is uniformly controlled by the completed Claude Theorem F. The six nonzero eigenvectors (three plus, three minus) form a range frame with row leverage `3/m`, and for `delta<=1/10` the product of nonzero eigenvalue magnitudes is at least

`(4/5)^k (3/5)^(3-k)`.

Theorem F with rank `r=6` therefore gives, for **every** original cap-one product law,

`||p_{X^T A_{m,k,delta}X}||_infinity
 <= 6 [(4/5)^k(3/5)^(3-k)]^(-1/6)`.

Numerically this is

`k=0: 7.7459666924...`,
`k=1: 7.3833337853...`,
`k=2: 7.0376777941...`.

So Proposition 6.1 refutes only the stronger structural shortcut. It also diagnoses what is missing in the arbitrary hybrid: in this exact family the **whole six-dimensional nonzero spectral range** is diffuse and Theorem F pays it, whereas an arbitrary QFORM matrix may carry an unrestricted extra spectral remainder that destroys this exact diffuse-low-rank representation.

## 7. Net reduction and the first remaining implication

The diffuse selected-three-eigenvector regime is now reduced more sharply as follows.

* If a balanced side has **zero** actual `c_L`-large eigenvalues and the resulting rank-three cross volume is not physically heavy, D' gives the explicit full-form bound

`||p_Q||_infinity <= 128 sqrt(e/3)/L < 121.842/L`.

* If that D' payment fails on both orientations, the zero-child branch has a double-heavy incident three-volume bank (4.3); inside `N3(1/8192)` it contains at least 47,759 nonzero incident minors.

* If the side retains one or two actual `c_L`-large eigenvalues, the partner theorem guarantees only the complementary two or one `beta_L`-large cross singular directions. Proposition 6.1 proves this count is optimal even in the strict no-pivot class, with exactly three target-large eigenvalues and leverage tending to zero.

* A bounded actual physical core is not the missing endpoint inside `N3(1/8192)`: every child carrying even one `c_L` eigenvalue has at least 37 original coordinates.

The first unpaid implication is therefore:

**`QFORM-DIFFUSE-HYBRID-ONE-TWO-DIRECTION-PAYMENT-v1` — OPEN.**  
For the balanced diffuse cut, pay the states `k=1` and `k=2` (or produce a genuine product-source counterexample) while retaining an arbitrary spectral remainder. The proof must combine one/two ACTUAL principal eigen-directions with the complementary two/one ACTUAL cross singular directions. It may use the double-heavy incident-volume structure when the three-volume D' gate fails, but it cannot assume the remaining small cross singular values are bounded below, cannot replace the arbitrary remainder by a diagonal twist, and cannot condition in spectral coordinates.

The Hadamard family identifies a plausible correct compiler: a theorem stable under arbitrary spectral remainder that recovers the whole-range Fresnel payment when the retained principal and cross directions together form a diffuse physical frame. That stability, not another local-minor extraction, is the next target.

## 8. Finite check

`check.py` and `check_output.txt` in this run root verify the constants, the exact 36/37 no-pivot gate, the D' simplification, the N3 entry/determinant bounds at `m=32768`, the hybrid eigenvalue counts at the endpoint `delta=1/10`, and the stated Theorem F constants. The executed output terminates with `QFORM_B08_ACTUAL_SPECTRAL_GATE_CHECK_PASS`.

No scheduler/task mutation, notification/email action, paid call, remote workflow, permission change, public release, FEI/installation/benchmark work, or cross-account authentication is part of this report.
