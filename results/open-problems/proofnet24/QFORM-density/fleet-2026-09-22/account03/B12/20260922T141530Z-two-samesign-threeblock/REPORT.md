# account03/B12 — dependent square + aggregate rank-two cross smoothing, and one-arbitrary-eigenvalue stability

**Run:** `20260922T141530Z-two-samesign-threeblock`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source discipline

The target remains: for every dimension `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with `||p_Q||_infinity<=C` for one universal finite `C`, or give a valid counterexample. Continuity is tracked separately.

Fresh control commit before the run: `230c9be157c3c405499041b389b359f0e15f32ec`. The current owner revision remains `2026-09-22.5`; FEI is suspended.

No spectral rotation is used to claim independence. All conditioning below is on subsets of the original independent coordinates. The refuted pointwise van-der-Corput/Fresnel envelope and naive fiber-supremum mechanisms are not used.

The preceding B12 run proved an exterior-power cross-block criterion and identified the overlap channels in the exact identity

`e_3(A^2)=sum_{|I|=|J|=3} det(A[I,J])^2`.

This run advances the mixed overlap mechanism rather than repeating the prior diffuse proof.

## 2. Completed inputs actually used

### 2.1 Regularized cross-block determinant theorem

From the completed interactive report

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`,

for a physical original-coordinate cut with cross block `C` whose range leverage on the chosen side is at most `1/2`, the quadratic remainder `R` satisfies

`|phi_R(t)| <= det(I + c_1 t^2 C C^T)^(-1/4)`,

where

`c_1 = 2/(pi^2 e^2)`.

This estimate is uniform over all within-side quadratic phases, outside variables/couplings and all input laws with density cap one.

### 2.2 account04 dependent square smoothing

The assigned partner path `account04/B12` still has no current QFORM artifact in either the shared handoff tree or the canonical account04 QFORM archive at the source-bound read. I therefore do not fabricate a B12 result. I instead apply the closest compatible completed account04 result, account04/B18:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its key lemma says that if `R` has density bounded by `M` and the conditional density of `V|R=r` is bounded by one, with no independence assumed, then

`||p_{R+aV^2}||_infinity <= 2 sqrt(M/|a|)`.

I strengthen the analytic interface needed here from `R in L^infinity` to `R in L^p`, `p>2`; this makes the rank-two cross channel usable.

### 2.3 fixed invertible physical triple

From account02/B15,

`yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`,

an invertible symmetric physical `3x3` block `B`, with arbitrary affine tilt, gives

`||p||_infinity <= C_3/sigma_min(B)`,

`C_3=2*pi+3*sqrt(3)`.

This is used only in the rank-one stability corollary below.

## 3. A dependent square smoothing lemma from an L^p remainder

### Lemma 3.1 — `QFORM-DEPENDENT-SQUARE-LP-v1`

Let `R` have density `g in L^p(R)` with `p>2`, and suppose the conditional law of `V` given `R=r` has a density bounded by one for almost every `r`. No independence between `R` and `V` is assumed. Put

`s=p/(p-1) in (1,2)`, `beta=1-s/2`.

Then for every nonzero real `a`, `T=R+aV^2` has an essentially bounded density and

`||p_T||_infinity <= |a|^(-1/2) D_s ||g||_p^(s/2)`,                 (3.1)

where

`D_s = (2/s) beta^(-1/2) [s/(2 beta)]^beta`.                     (3.2)

#### Proof

It suffices to write the case `a>0`; reflection handles `a<0`. Conditional on `R=r`, the density of `aV^2` at `u>0` is at most

`1/sqrt(a u)`.

Thus

`p_T(t) <= a^(-1/2) int_0^infinity g(t-u) u^(-1/2) du`.          (3.3)

For any cutoff `H>0`, Holder on `(0,H)` and `||g||_1=1` on `(H,infinity)` give

`p_T(t) <= a^(-1/2) [ G beta^(-1/s) H^(1/s-1/2) + H^(-1/2) ]`,  (3.4)

where `G=||g||_p` and `beta=1-s/2` because

`int_0^H u^(-s/2) du = H^beta/beta`.

Optimizing in `H` gives (3.1)-(3.2). Explicitly the minimizing relation is

`H^(1/s) = [2(1/s-1/2) G beta^(-1/s)]^(-1)`,

and substitution simplifies to (3.2). QED.

This strictly extends the account04/B18 dependent-square interface: the remainder no longer needs an `L^infinity` density; any `L^p`, `p>2`, is sufficient.

## 4. Aggregate rank-two cross block plus one square pivot

Let `k` be one original coordinate with `a=A_kk !=0`. Complete the square **without rotating coordinates**:

`Q = a V^2 + R`,

`V = X_k + a^(-1) A[k,-k] X_-k`,

`R = X_-k^T S X_-k`,

`S = A[-k,-k] - a^(-1) A[-k,k] A[k,-k]`.                       (4.1)

Because `X_k` is independent of `X_-k` and has density at most one, conditional on `X_-k` the variable `V` has density at most one. Passing to the coarser conditioning on the scalar `R` preserves this bound by mixing. Hence Lemma 3.1 applies as soon as `R` has an `L^p` density.

Choose disjoint sets of original coordinates `I,J subset -{k}` and let

`C=S[I,J]`.

Assume the leverage of `range(C)` on the determinant-theorem side is at most `1/2`. Define the aggregate two-direction energy

`E_2 = e_2(CC^T) = sum_{r<q} sigma_r(C)^2 sigma_q(C)^2`.         (4.2)

No rank-exactly-two assumption is made; every additional cross singular direction only increases `E_2`.

### Theorem 4.1 — `QFORM-PIVOT-E2-CROSS-v1`

If `E_2>0`, then `Q` has an essentially bounded density and, for every `1<s<2`,

`||p_Q||_infinity <= K_s |a|^(-1/2) E_2^(-1/8)`,               (4.3)

where

`K_s = D_s sqrt(e) 2^(-5/4) sqrt(B(1/4,(s-1)/4))`.             (4.4)

In particular, with the simple rational choice `s=8/5`,

`K_{8/5}`
`= (5/4) sqrt(5e) 2^(-17/20) sqrt(B(1/4,3/20))`
`= 8.152027307129858...`,

so

`||p_Q||_infinity <= 8.153 |a|^(-1/2) E_2^(-1/8)`.             (4.5)

#### Proof

The regularized determinant theorem and determinant expansion give

`|phi_R(t)|`
` <= det(I+c_1 t^2 CC^T)^(-1/4)`
` <= (1+c_1^2 E_2 t^4)^(-1/4)`.                                (4.6)

Raise to the power `s>1` and integrate:

`||phi_R||_s^s`
` <= c_1^(-1/2) E_2^(-1/4) * (1/2) B(1/4,(s-1)/4).`           (4.7)

Hausdorff-Young for the convention

`phi(t)=int exp(itx) g(x) dx`,
`g(x)=(2pi)^(-1) int exp(-itx) phi(t) dt`

gives, with `p=s/(s-1)`,

`||g||_p <= (2pi)^(-1/s) ||phi_R||_s`.                         (4.8)

Insert (4.7) into (4.8), then insert the result into Lemma 3.1. Since `c_1=2/(pi^2 e^2)`, all powers simplify to (4.3)-(4.4). QED.

### Why this is genuine additional-direction control

The price in (4.3) is `E_2^(-1/8)`, not the reciprocal product of every nonzero singular direction. If the residual cross block acquires arbitrary extra singular directions, tiny or huge, then `E_2` cannot decrease under literal augmentation of its singular spectrum. The proof keeps all within-side quadratic terms and all signs. It never treats the added quadratic remainder as an independent convolution.

For a genuine `2x2` residual cross block, `E_2=det(C)^2`, so (4.5) becomes

`||p_Q||_infinity <= 8.153 |a|^(-1/2) |det C|^(-1/4)`.         (4.9)

If `M=A[{k} union I,{k} union J]` is the corresponding overlap-one `3x3` mixed minor and `I,J` are two-element sets, Schur's determinant identity gives

`det M = a det C`.                                             (4.10)

Thus (4.9) is equivalently

`||p_Q||_infinity <= 8.153 (|a| |det M|)^(-1/4)`.              (4.11)

Equation (4.10) identifies exactly how the overlap-one channel in `e_3(A^2)` becomes a square pivot plus a rank-two cross smoother. This is the first source-exact local analytic payment for that mixed channel.

## 5. Exact overlap-channel bookkeeping

For completeness, define

`M_r(A)=sum_{|I|=|J|=3, |I cap J|=r} det(A[I,J])^2`, `r=0,1,2,3`.

Cauchy-Binet gives the exact identity

`M_0+M_1+M_2+M_3 = e_3(A^2)`.                                  (5.1)

If `A` has at least three eigenvalues of absolute value at least one, then

`e_3(A^2)>=1`, hence some `M_r>=1/4`.                           (5.2)

There are useful dimension-free random-color realizations of each nonprincipal mixed channel:

- `r=0`: under an independent two-color split with probabilities `(1/2,1/2)`, the expected disjoint `3x3` cross-minor-square mass is `M_0/64`.
- `r=2`: color coordinates `K,L,R` with probabilities `(1/2,1/4,1/4)`; the expected mass of minors with two common `K` coordinates, one `L` row-only coordinate and one `R` column-only coordinate is `M_2/64`.
- `r=1`: color with probabilities `(1/5,2/5,2/5)` for `(K,L,R)`; the expected mass with one common coordinate, two row-only coordinates and two column-only coordinates is `(16/3125) M_1`.
- `r=3`: the resource is simply the principal mass `M_3`.

Therefore if the dominant channel is `r=0` or `r=2`, there exists a coloring carrying at least `1/256` of the corresponding aggregate resource; if it is `r=1`, there exists a coloring carrying at least `4/3125`. These are exact expectation identities, not maximum-minor claims.

Theorem 4.1 shows how an individual overlap-one mixed minor is paid when its shared diagonal pivot is nonzero and the residual rank-two cross geometry satisfies the leverage hypothesis. The **remaining unpaid step for the `M_1` channel** is to aggregate this payment without taking a worst inverse pivot/minor and without losing dimension when the mass is spread over many tiny minors.

## 6. One arbitrary global rank-one spectral perturbation is harmless around a physical definite triple

The previous theorem handles the mixed channel. A second exact stability statement answers a different part of the B12 assignment: one genuinely arbitrary added eigen-direction, of either sign and any magnitude, cannot destroy a physical three-coordinate definite core.

Let `B` be a real symmetric `3x3` matrix with eigenvalues

`lambda_1>=lambda_2>=L>0`,

while `lambda_3` is arbitrary. Let `0<b<1/2`.

If `|lambda_3|>=bL`, then `sigma_min(B)>=bL`, so the account02/B15 triple theorem gives

`||p||_infinity <= C_3/(bL)`.                                  (6.1)

If `|lambda_3|<bL`, then

`e_2(B)=lambda_1 lambda_2+lambda_3(lambda_1+lambda_2)`
`        >= L^2(1-2b)`.                                        (6.2)

But `e_2(B)` is the sum of the three principal `2x2` determinants. Hence one principal pair has determinant at least

`L^2(1-2b)/3`.                                                  (6.3)

By Cauchy interlacing, the largest eigenvalue of every principal pair is at least `lambda_2>=L`; therefore the pair in (6.3) is positive definite. For a definite physical pair, direct ellipsoidal shell area gives the affine-uniform bound

`||p||_infinity <= pi/sqrt(det)`,

so here

`||p||_infinity <= (pi/L) sqrt(3/(1-2b))`.                     (6.4)

Balancing (6.1) and (6.4) yields

`b_* = C_3/(C_3+sqrt(C_3^2+3pi^2))`

and

`C_* = C_3+sqrt(C_3^2+3pi^2)`
`    = 24.183038289961516...`.                                 (6.5)

Thus:

### Theorem 6.1 — `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`

If a physical principal `3x3` block has at least two eigenvalues `>=L`, or at least two eigenvalues `<=-L`, with the third eigenvalue completely arbitrary, then after conditioning every outside original coordinate,

`||p_Q||_infinity <= C_*/L`.                                   (6.6)

All outside eigenvalues, signs, magnitudes and cross couplings are arbitrary; conditioning makes cross terms affine tilts only.

### Corollary 6.2 — arbitrary one-eigen-direction perturbation

Suppose a physical `3x3` principal block `B_0` satisfies `B_0>=L I_3` (or `B_0<=-L I_3`). Add an arbitrary global rank-one quadratic perturbation

`tau (v^T x)^2`, `tau in R`,

with no restriction on `|tau|` or the support/delocalization of `v`. On the physical triple the new block is

`B=B_0+tau v_S v_S^T`.

If `tau>=0`, all three positive eigenvalues remain at least `L`. If `tau<0`, rank-one interlacing gives

`lambda_2(B)>=lambda_3(B_0)>=L`.

Hence Theorem 6.1 applies in both cases, and the completed quadratic form still obeys

`||p_Q||_infinity <= C_*/L`.                                   (6.7)

Reflection handles the negative-definite core. This is a true dependent stability theorem: the newly added square is not assumed independent of the old quadratic form.

The same conclusion allows an arbitrary additional symmetric remainder whose principal block on the smoothing triple is zero; all of that remainder is absorbed by original-coordinate conditioning as affine/outside terms.

## 7. Application of account04 mathematics

Theorem 4.1 is an actual application and strengthening of account04/B18's dependent-square theorem: its `L^infinity` hypothesis on the remainder is replaced by a quantified `L^p`, `p>2`, interface, and the regularized determinant theorem supplies exactly such an `L^p` remainder from a rank-two aggregate cross block. This turns the account04 square-pivot idea into a new mixed-overlap inequality (4.3), rather than merely citing it.

At the fresh snapshot, account04/B12 itself still has no QFORM directory/handoff. Therefore the literal assigned-partner-slot requirement could not be satisfied without inventing output; this is recorded explicitly for the owner rather than silently substituting stale FEI work.

## 8. Continuity status

Theorem 4.1 proves an essentially bounded density. The proof as written does **not** prove a continuous representative for `Q`: the final dependent square smoothing is a one-sided fractional integral estimate, not an `L^1` characteristic-function argument for `Q`.

Theorem 6.1 likewise proves `L^infinity` within its scope; continuity is not claimed in the fully coupled completion. Under the exact separator hypotheses of the completed account04/B15 theorem, continuity upgrades to `C_0(R)`, but that separator is an extra hypothesis and is not part of the unrestricted target.

## 9. What remains

The full QFORM conjecture is **OPEN / NOT PROVED**.

This run closes two concrete additional-eigenvalue questions:

1. a square pivot plus any leverage-controlled residual cross block with aggregate rank-two energy `E_2>0` yields the explicit dependent bound (4.3), and extra residual singular directions are paid monotonically through `E_2`;
2. one arbitrary global rank-one eigen-direction of either sign/magnitude cannot destroy a physical definite three-coordinate smoothing core.

The first target-level unpaid implication is now an **aggregate mixed-channel theorem**: from `M_1>=1/4` (or the analogous `M_2` resource), sum the pivot/cross payments before taking inverse powers, so that a diffuse cloud of tiny mixed minors yields a dimension-free bound. The random-color identities in Section 5 preserve the exact conserved spectral mass and avoid the already-refuted maximum-minor route.

A second unpaid implication is to splice the four channels `M_0,M_1,M_2,M_3` into a complete structural/analytic dichotomy, with the existing exterior-power cross theorem handling diffuse `M_0`, Theorem 4.1 handling local `M_1` packets, and new aggregate mechanisms required for diffuse `M_1/M_2` and principal `M_3` mass.

No full-solution claim is made.
