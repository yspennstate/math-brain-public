SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T07:30:14Z.
attacking: a Fourier-tail-to-quantitative-regularity compiler at the critical t^-2 endpoint, applied to the new four-latent product-preserving receiver.

# account03/B15 — Fourier-tail regularity compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW QUANTITATIVE REGULARITY LEMMA / EXISTING QFORM BRANCH STRENGTHENED / PARTNER APPLIED / FULL QFORM OPEN**.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval is verified; native mathematical-receiver ingestion is not.

## 1. Exact target and scope

The owner target remains: for every `n`, every independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with universal `L^infinity` norm, or give a valid counterexample. Continuity is stronger and is recorded separately.

This report does **not** prove the missing universal height bound. It proves a quantitative regularity compiler for any branch in which a product-preserving Fourier estimate has already been paid, and applies it to the newest four-latent receiver from account03/B19. No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation independence assumption is introduced.

Fresh dependency actually read:

- account03/B19 r52, `yspennstate/math-open-problems@5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T070220Z-account03-B19-QFORM-r52/REPORT.md`.
- its analytic Theorem H source, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
- designated partner account04/B15 r8 handoff, whose completed same-constant `C_0` closure uses the fixed-matrix rank>=3 theorem at `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`.

The live corrections prohibiting law-uniform one-dimensional van der Corput decay, naive fiber-supremum integration, independence after spectral rotation, and arbitrary-joint coarea are all respected. The Fourier bounds used below are already joint, product-preserving bounds.

## 2. A general height formula from a polynomial Fourier tail

Let `mu` be a probability measure on `R` with characteristic function `phi`, and assume for some `beta>1` and `K>0`

`|phi(t)| <= min(1, K |t|^{-beta})` for every `t!=0`.                         (2.1)

Put

`a=K^(1/beta)`.

Then `phi in L^1(R)`, hence Fourier inversion gives a canonical density

`p(x)=(2pi)^(-1) integral_R exp(-itx) phi(t) dt`

with `p in C_0(R)`. Moreover

`integral_R min(1,K|t|^{-beta}) dt`
`=2[a + K integral_a^infinity t^{-beta}dt]`
`=2a beta/(beta-1)`.

Therefore

`boxed: ||p||_infinity <= [beta/(pi(beta-1))] K^(1/beta).`          (2.2)

This is only a Fourier-tail compiler. It does not assert that every owner-target instance has such a pointwise tail; the source corrections show that naive law-uniform pointwise phase decay is false.

## 3. Exact critical regularity at beta=2

The first new point is that the borderline `t^-2` tail has a quantitative log-Lipschitz output modulus with exact elementary constants.

Assume

`|phi(t)| <= min(1,K t^-2)`, `t!=0`,                               (3.1)

and write

`a=sqrt(K)`, `h=|z|`, `u=ha`.

For every `x,z`,

`|p(x+z)-p(x)|`
`<= (2pi)^(-1) integral_R |exp(-itz)-1| |phi(t)| dt`
`<= pi^(-1) integral_0^infinity min(2,ht) min(1,Kt^-2) dt`.         (3.2)

### Case 0<u<=2

Split the last integral at `a` and `2/h`. Since `a<=2/h`,

`integral_0^a ht dt = h a^2/2`,

`integral_a^(2/h) ht Kt^-2 dt = hK log(2/(ha))`,

`integral_(2/h)^infinity 2K t^-2 dt = hK`.

Thus

`boxed: ||tau_z p-p||_infinity`
` <= (K h/pi) [3/2 + log(2/(h sqrt(K)))]`,
` 0<h sqrt(K)<=2.`                                                 (3.3)

### Case u>=2

Now `2/h<=a`. Splitting at `2/h` and `a` gives

`integral_0^(2/h) ht dt = 2/h`,

`integral_(2/h)^a 2 dt = 2a-4/h`,

`integral_a^infinity 2K t^-2 dt = 2a`.

Hence

`boxed: ||tau_z p-p||_infinity <= pi^(-1)(4sqrt(K)-2/h),`
` h sqrt(K)>=2.`                                                   (3.4)

At the junction `h sqrt(K)=2`, (3.3) and (3.4) both equal `3sqrt(K)/pi`. In particular the density is uniformly continuous for each paid instance, with the sharp qualitative scale `O(h log(1/h))` supplied by the `t^-2` envelope.

The height formula (2.2) at `beta=2` is

`boxed: ||p||_infinity <= 2sqrt(K)/pi.`                            (3.5)

## 4. Exact beta=3/2 Hölder compiler

The other exponent occurring repeatedly in the QFORM Fresnel/Brascamp--Lieb receivers is `beta=3/2`. Let

`|phi(t)|<=min(1,K |t|^-3/2)`.

Here `a=K^(2/3)`. For `u=ha<=2`, the same three-piece integration gives exactly

`pi ||tau_z p-p||_infinity`
`<= a[4sqrt(2)sqrt(u) - (3/2)u]`
`<=4sqrt(2) K sqrt(h)`.                                           (4.1)

For `u>=2`, the trivial estimate `||tau_zp-p||_infinity<=2||p||_infinity=6a/pi` is dominated by the right-hand side of (4.1), because at `u=2` that right-hand side equals `8a/pi` and then grows with `h`.

Therefore globally

`boxed: ||tau_z p-p||_infinity <= [4sqrt(2)/pi] K |z|^(1/2).`       (4.2)

The corresponding height bound is

`boxed: ||p||_infinity <= 3 K^(2/3)/pi.`                           (4.3)

Thus a genuine joint `t^-3/2` QFORM Fourier estimate yields not merely continuity but a quantitative global `1/2`-Hölder modulus. This does **not** contradict the earlier B15 obstruction to a target-uniform continuity modulus: here the Hölder constant depends on the structural Fourier coefficient `K`, which is not uniformly controlled by the bare three-large-eigenvalue hypothesis.

## 5. Application to the account03/B19 four-latent receiver

The completed r52 theorem assumes a literal original-coordinate block

`A[I,I]=D+W H W^T`,

where `D` is physical diagonal, `W^T W=I_4`, every physical row leverage satisfies `||W_i||^2<=1/2`, and `H` is an invertible real symmetric `4x4` coefficient-space matrix. Arbitrary outside curvature, outside couplings and affine terms are allowed. Its product-preserving Theorem-H application gives

`|phi_Q(t)| <= min(1, 16 pi^2 |det H|^-1/2 |t|^-2).`              (5.1)

Let

`Delta=|det H|`.

Then in the notation of Section 3,

`K=16pi^2 Delta^-1/2`, `sqrt(K)=4pi Delta^-1/4`.

The height formula recovers exactly the r52 constant

`boxed: ||p_Q||_infinity <= 8 Delta^-1/4.`                         (5.2)

The new quantitative regularity conclusion is: for

`0<h<=Delta^(1/4)/(2pi)`,

`boxed: ||tau_h p_Q-p_Q||_infinity`
` <=16pi h Delta^-1/2 [3/2 + log(Delta^(1/4)/(2pi h))].`           (5.3)

For

`h>=Delta^(1/4)/(2pi)`,

`boxed: ||tau_h p_Q-p_Q||_infinity`
` <=16 Delta^-1/4 - 2/(pi h).`                                    (5.4)

Hence this exact four-latent branch has an explicit log-Lipschitz `C_0` representative. No continuity modulus uniform in `Delta` is asserted.

At the concrete r52 determinant gate `Delta>=2^-40`, the previously obtained height is at most `8192`. The present formula additionally gives, uniformly inside that gated branch,

`||tau_h p_Q-p_Q||_infinity`
` <= 16pi 2^20 h [3/2 + log(2^-10/(2pi h))]`

whenever `0<h<=2^-10/(2pi)`. This is a genuinely uniform modulus on the **gated branch only**, not on the full target class.

## 6. Application to the rank-three Fresnel/Brascamp--Lieb receiver

Theorem F in the source-pinned Fresnel/Brascamp--Lieb report gives, on its exact product-preserving leverage scope,

`|phi_Q(t)| <= (4pi)^(3/2) R^-1/2 |t|^-3/2`,                     (6.1)

where

`R=|lambda_1 lambda_2 lambda_3| det G_I`.

Thus `K=(4pi)^(3/2)R^-1/2`. Formula (4.3) reproduces its height exactly:

`3/pi * K^(2/3)=12 R^-1/3`.

The new regularity estimate is

`boxed: ||tau_h p_Q-p_Q||_infinity`
` <=32 sqrt(2pi) R^-1/2 sqrt(|h|),` for every real `h`.            (6.2)

So every already-paid rank-three BL receiver of this type is globally `1/2`-Hölder, with a completely explicit constant. Again `R` need not have a target-uniform lower bound.

## 7. Designated partner account04/B15 applied to an actual inequality

The completed account04/B15 r8 result states: for any fixed QFORM instance with `rank(A)>=3`, once a separate interval estimate

`P(Q in J)<=M |J|`                                                (7.1)

has been paid, the law has a canonical representative `p_Q in C_0(R)` with the **same** height `||p_Q||_infinity<=M`; no universal modulus is inferred.

Apply it to the r52 four-latent owner-target branch. From (5.2),

`P(Q in J)<=8 Delta^-1/4 |J|`.                                   (7.2)

Since every owner-target matrix has rank at least three, the account04/B15 compiler yields

`p_Q in C_0(R)`, `||p_Q||_infinity<=8Delta^-1/4`                  (7.3)

with zero loss. The present Fourier calculation independently recovers (7.3) and strengthens it to the explicit log-Lipschitz bounds (5.3)-(5.4). This is the required actual use of the designated partner result, not a nominal citation.

Similarly, on the exact Theorem-F branch, the interval bound `P(Q in J)<=12R^-1/3|J|` is upgraded by the partner theorem to the same-height `C_0` conclusion, while (6.2) supplies the additional Hölder modulus.

## 8. Absolute continuity remains strictly weaker

For completeness, the absolute-continuity statement needs neither rank three nor product structure. If `A!=0` and the joint input law is absolutely continuous on `R^n`, then `q(x)=x^TAx` has an absolutely continuous pushforward. Indeed for a one-dimensional null set `N`, coarea on

`E_k={|x|<=k, |grad q(x)|>=1/k}`

shows `Leb(E_k intersect q^-1(N))=0`, while the critical set `ker A` is a proper linear subspace and hence null. Therefore `Leb(q^-1(N))=0` and the pushforward charges no null set.

This gives existence of a density but no height. The full owner problem is precisely the dimension- and matrix-uniform `L^infinity` estimate.

## 9. What this run does and does not close

Proved here:

1. an exact `t^-2` Fourier-tail to log-Lipschitz `C_0` compiler with explicit constants;
2. an exact `t^-3/2` Fourier-tail to global `1/2`-Hölder compiler;
3. the explicit log-Lipschitz upgrade of the newest four-latent QFORM receiver;
4. the explicit `1/2`-Hölder upgrade of the rank-three BL receiver;
5. same-constant partner closure applied to the actual height inequalities.

Not proved:

- no uniform Fourier coefficient `K` was obtained from only `s_3(A)>=1`;
- the retained diffuse residual/tail in the r52 determinant-collapse survivor is still unpaid;
- no target-uniform continuity modulus is claimed;
- the universal height conjecture remains OPEN.

The first useful structural implication remains the r52 one: combine the almost-rank-three latent carrier with the retained diffuse third source/tail, or force another completed product-preserving exit. Once any such branch produces an integrable Fourier envelope, the present compiler supplies its exact regularity for free.
