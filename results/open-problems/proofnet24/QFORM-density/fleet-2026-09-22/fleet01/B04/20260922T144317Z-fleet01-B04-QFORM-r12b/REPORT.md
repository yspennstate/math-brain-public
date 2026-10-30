# fleet01/B04 — quarter-power product rearrangement and an indefinite-face bridge

**Run:** `20260922T144317Z-fleet01-B04-QFORM-r12b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and conditional end-to-end route

The full target remains open: for every dimension, every family of independent real random variables with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density bounded by one universal constant, or give a target-valid counterexample. Continuity is a separate stronger requested conclusion and is not established by the new local branches below.

The current compact route is:

1. diffuse range / regularized-determinant branches are already paid at their proved leverage thresholds;
2. fleet02/B04 pays a scalar pivot whenever its Schur complement has two quantitatively large cross singular directions with suitable cross-range leverage;
3. the present run pays every invertible physical `3 x 3` block having an indefinite physical `2 x 2` face, with an explicit determinant/diagonal bound, and pays the exact zero-diagonal endpoint by the completed fleet02/B04 product rearrangement theorem;
4. applied to the newest fleet03/B19 one-effective-direction normal form, this closes the branch whenever the pair Schur complement has one moderately large physical diagonal, and otherwise forces a quantitative original-coordinate **one-cross-direction** certificate;
5. the first remaining implication in that branch is therefore an indefinite-pair + one-cross product-preserving splice, rather than a generic rotated aggregate-compression problem.

No law-uniform pointwise Fresnel decay, post-rotation independence, naive fiber supremum, generic conditional-density cap, fixed-minor dichotomy, finite fragment-count localization, or absolute phase-Wiener bound is used.

## 2. Completed partner results actually consumed

### 2.1 fleet02/B04 product-density rearrangement

Source:

`yspennstate/math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T122057Z-01c809a1/REPORT.md`.

For independent `U,V` with densities at most one, the proved estimate is

`p_{UV}(s) <= 4 log(1+1/(2 sqrt(|s|)))`, `s != 0`.

The same report proves the all-zero-diagonal physical-triple theorem. The present report applies that theorem at the exact endpoint `m=0` of Theorem 5.1 below; it is therefore an actual branch inequality, not a citation-only dependency.

### 2.2 latest fleet02/B04 two-cross Schur bridge

Source:

`yspennstate/math-open-problems@8a6b40dc9b492b6ec05a16d58d68dffd4f590e50`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260922T141554Z-fleet02-B04-QFORM-r11/REPORT.md`.

If an original scalar pivot `a != 0` has a Schur complement with two cross singular values at least `sigma` and cross-range leverage at most `q/2`, `1 <= q < 3/2`, then

`||p_Q||_infinity <= C_piv(q)/sqrt(|a| sigma)`

with

`C_piv(q)=2^(5/4) e^(1/2) pi^(1/4) q^(-1/4)
 [Gamma(3/(4q)-1/2)/Gamma(3/(4q))]^(1/2)`.

For `q=1`, `C_piv(1)=8.979886417...`. This remains one of the two analytic exits in the conditional route; the present run targets the complementary one-effective-direction geometry where only one cross direction can presently be forced.

## 3. A quarter-power rearrangement lemma

### Lemma 3.1 — `QFORM-QUARTER-POWER-QUADRATIC-BATHTUB-v1`

Let `h` be any probability density on `R` with `0 <= h <= 1`. For every `Delta>0` and every nonzero `beta`,

`integral h(u) |Delta u^2+beta|^(-1/2) du
 <= 4 Delta^(-1/4) |beta|^(-1/4).`                        (3.1)

#### Proof

If `beta>0`, the kernel is even and decreasing in `|u|`. The bathtub principle gives

`I <= integral_{-1/2}^{1/2} (Delta u^2+beta)^(-1/2) du`
`   = (2/sqrt(Delta)) asinh( sqrt(Delta)/(2 sqrt(beta)) ).`

Using `asinh z <= 2 sqrt(z)` for `z>=0`,

`I <= 2 sqrt(2) Delta^(-1/4) beta^(-1/4)`,

which is stronger than (3.1).

If `beta<0`, put `a=sqrt(|beta|/Delta)`. Then

`|Delta u^2+beta|^(-1/2)
 = Delta^(-1/2)(|u-a||u+a|)^(-1/2).`

For `A=|u-a|`, `B=|u+a|`, we have `A+B>=2a`, hence

`(AB)^(-1/2)
 <= (A^(-1/2)+B^(-1/2))/sqrt(2a)`.

For every translate `r`, a second bathtub estimate gives

`integral h(u)|u-r|^(-1/2)du <= 2 sqrt(2)`.

Therefore

`I <= Delta^(-1/2) (4 sqrt(2))/sqrt(2a)
   =4 Delta^(-1/4)|beta|^(-1/4).`

QED.

This lemma deliberately integrates a singular kernel against the product marginal. It is not a pointwise oscillatory-decay assertion.

## 4. Fully explicit binary-indefinite L3 constant

The completed fleet01/B11 binary theorem established a determinant-scale `L^3` density bound but its large-diagonal case was expressed using an unspecified one-dimensional HLS norm. Lemma 3.1 removes that unspecified constant.

Consider independent `X,Y`, densities at most one, and

`R=alpha X^2+2aXY+beta Y^2+rX+sY+c`,

with

`D=a^2-alpha beta>0`.

Because the binary Hessian is invertible, coordinatewise translation removes the affine terms without changing independence or density caps.

### Case A: one diagonal is at least `sqrt(D)/5`

Assume `|beta|>=sqrt(D)/5`. For fixed `X=x`, the quadratic equation in `Y` has discriminant

`4(Dx^2+beta t)`.

Summing the two inverse-Jacobian contributions and using the cap on the density of `Y` gives

`p_R(t) <= integral f_X(x)(Dx^2+beta t)_+^(-1/2)dx`
`       <= integral f_X(x)|Dx^2+beta t|^(-1/2)dx.`

Lemma 3.1 yields

`p_R(t)
 <=4 D^(-1/4)|beta|^(-1/4)|t|^(-1/4)
 <=K D^(-3/8)|t|^(-1/4),`                                    (4.1)

where `K=4*5^(1/4)`.

We now use only normalization, not HLS. If a probability density `p` satisfies `p(t)<=A|t|^(-1/4)`, then for every `R0>0`,

`integral p^3
 <=8A^3 R0^(1/4)+A^2 R0^(-1/2).`

Optimizing at `R0^(1/4)=(4A)^(-1/3)` gives

`||p||_3 <=3^(1/3)2^(4/9) A^(8/9).`                            (4.2)

Substituting `A=K D^(-3/8)` gives

`||p_R||_3 <= C_A D^(-1/3),`

`C_A=3^(1/3)2^(20/9)5^(2/9)=9.623269132... .`                  (4.3)

The same proof applies when `|alpha|>=sqrt(D)/5` after swapping the coordinates.

### Case B: both diagonals are small

The elementary sector proof already completed in fleet01/B11 applies verbatim and gives

`||p_R||_3 <= C_B D^(-1/3),`

`C_B=6*2^(2/3)*(25/24)^(1/3)=900^(1/3)=9.654893846... .`       (4.4)

Since

`C_A^3=192*10^(2/3)<900=C_B^3`,

we obtain the completely explicit uniform theorem

`boxed( ||p_R||_3 <= 900^(1/3) D^(-1/3). )`                    (4.5)

Thus the HLS norm can be removed from that binary-indefinite branch.

Combining (4.5) with fleet01/B11's already proved fresh-original-coordinate dependent-square smoothing lemma gives the explicit scalar-pivot consequence

`boxed(
 ||p_Q||_infinity
 <=4 sqrt(30) (|d| |det M|)^(-1/4)
 <21.909 (|d| |det M|)^(-1/4),
)`                                                            (4.6)

whenever the physical scalar pivot `d` has an indefinite binary Schur complement. This is a constant sharpening of an existing source-valid branch, not a full-target claim.

## 5. Main new theorem: every invertible triple with an indefinite physical face

### Theorem 5.1 — `QFORM-INDEFINITE-FACE-QUARTERPOWER-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let

`M=[[d,a,b],[a,alpha,c],[b,c,beta]]`

be real symmetric and invertible. Assume the physical face

`H=[[alpha,c],[c,beta]]`

is indefinite, i.e.

`Delta=c^2-alpha beta>0`.

Put

`m=max(|alpha|,|beta|)`.

If `m>0`, then `Q=(X,Y,Z)^T M (X,Y,Z)` has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <=2^(15/4) (m |det M|)^(-1/4)
 <13.455 (m |det M|)^(-1/4).
)`                                                            (5.1)

The same estimate holds after arbitrary affine terms in the three selected coordinates. Consequently it holds conditionally inside an ambient quadratic form after conditioning on all coordinates outside this physical triple.

If `m=0`, then `alpha=beta=0` and `c!=0`; the completed fleet02/B04 product-rearrangement theorem, via the determinant theorem already proved by fleet01/B04, gives instead

`boxed(
 ||p_Q||_infinity
 <=12 e^(-2/3)|det M|^(-1/3).
)`                                                            (5.2)

Thus every invertible physical triple with an indefinite physical face has an explicit product-coordinate density estimate. No spectral rotation is used.

#### Proof for `m>0`

Condition on `X=x` and put `ell=(a,b)^T`. Since `H` is invertible,

`Q
 =( (Y,Z)^T + x ell^T H^(-1) )
    H
   ( (Y,Z)+H^(-1)ell x )
 +kappa x^2,`

where

`kappa=d-ell^T H^(-1)ell
       =det(M)/det(H)
       =-det(M)/Delta.`                                       (5.3)

For fixed `x`, the translated `Y,Z` are still independent and each density remains bounded by one.

Assume first `m=|beta|`; the other case follows by swapping `Y,Z`. Applying Lemma 3.1 to the conditional binary density exactly as in Section 4 gives, uniformly in the translations,

`p_{H,x}(s)
 <=4 Delta^(-1/4) m^(-1/4)|s|^(-1/4).`                       (5.4)

Therefore

`p_Q(t)
 <=4 Delta^(-1/4)m^(-1/4)
   integral f_X(x)|t-kappa x^2|^(-1/4)dx.`                    (5.5)

It remains to integrate one quarter-power quadratic singularity. The uniform sublevel estimate

`|{x: |x^2-u|<delta}| <=2 sqrt(2 delta)`                        (5.6)

gives by layer cake, for every probability density `f<=1`,

`integral f(x)|x^2-u|^(-1/4)dx`
` <= integral_0^infinity min(1,2 sqrt(2) s^(-2)) ds`
` =2^(7/4).`                                                   (5.7)

After scaling by `|kappa|`, (5.5) becomes

`p_Q(t)
 <=2^(15/4)(Delta m |kappa|)^(-1/4)`
` =2^(15/4)(m|det M|)^(-1/4),`

using `Delta|kappa|=|det M|`. This proves (5.1).

For affine terms, invertibility of `M` permits a deterministic coordinatewise translation of the three original coordinates. Such translations preserve independence and density caps. Ambient conditioning produces only these affine and constant terms. QED.

#### Endpoint `m=0` and actual partner application

Here `alpha=beta=0`; the matrix has exactly two zero diagonal entries. The fleet02/B04 product logarithmic envelope applies to the translated `Y,Z` product inside the conditional formula. The fleet01/B04 determinant interpolation theorem then gives (5.2). This is the named partner result applied at the actual endpoint excluded by division by `m` in (5.1).

## 6. Explicit genuinely rotated indefinite target instance

Let

`P=I-(2/3) 11^T
  =[[1/3,-2/3,-2/3],[-2/3,1/3,-2/3],[-2/3,-2/3,1/3]]`.

`P` is orthogonal. Set

`M=P diag(3,1,-2) P^T`

so explicitly

`M=[[-1/9,-16/9,2/9],
   [-16/9,5/9,14/9],
   [2/9,14/9,14/9]].`

Every off-diagonal entry is nonzero and the eigenvalues are exactly `3,1,-2`, so this is a genuinely rotated indefinite instance satisfying the exact three-large-eigenvalue threshold. Also

`det M=-6`,

and on the lower physical face

`Delta=(14/9)^2-(5/9)(14/9)=14/9`,

`m=14/9`.

Theorem 5.1 therefore gives, for **every** independent input law with densities bounded by one,

`boxed( ||p_Q||_infinity <= 7.697563666... . )`                 (6.1)

This is an explicit rotated indefinite estimate obtained without any post-rotation independence assumption.

## 7. Applying the theorem to the newest one-effective-direction residual

I now apply Theorem 5.1 to the completed fleet03/B19 structural reduction

`yspennstate/math-open-problems@143e97c42cdbccb14fe847efb6abd3f6c3d349dc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T143049Z-fleet03-B19-QFORM-r11b/REPORT.md`.

In its one-effective-direction branch there are physical coordinates `p,q` such that their principal pair

`B=A[{p,q},{p,q}]`

has opposite-sign diagonal entries with magnitudes at least `7/8`, while `|A_pq|<=1/4`. Hence `B` is indefinite and

`|det B|>=49/64`,

`m_B=max(|A_pp|,|A_qq|)>=7/8`.                                (7.1)

Let `T` be the remaining coordinate bank and let `S` be the Schur complement of `B` in `A`. The same B19 theorem produces a unit vector `w` supported on `T` such that the compression of the **actual full matrix** to

`span(e_p,e_q,w)`

has

`s_min(A_E)>eta:=9/280`.                                      (7.2)

### 7.1 The compression forces a Schur Rayleigh coefficient

In the basis `(e_p,e_q,w)`, the scalar Schur complement of `B` in `A_E` is exactly

`s_w=w^T S w`.

Since `A_E` and `B` are invertible,

`(A_E^(-1))_33 =1/s_w`.

Equation (7.2) implies

`|1/s_w| <= ||A_E^(-1)||op < eta^(-1)`,

so

`boxed( |w^T S w|>eta=9/280. )`                               (7.3)

### 7.2 A large physical Schur diagonal closes immediately

Put

`rho=eta/2=9/560`.

If some `k in T` satisfies `|S_kk|>=rho`, the physical principal triple `M_k=A[{p,q,k},{p,q,k}]` obeys the exact Schur determinant identity

`|det M_k|=|det B| |S_kk| >=(49/64)rho.`                       (7.4)

Its physical `p,q` face is indefinite and has `m_B>=7/8`. Theorem 5.1 therefore gives

`||p_Q||infinity
 <=2^(15/4)[(7/8)(49/64)(9/560)]^(-1/4)`
` <41.768.`                                                     (7.5)

This closes that whole subbranch after conditioning on every coordinate outside `{p,q,k}`.

### 7.3 Otherwise a quantitative one-cross direction is forced

Assume now

`|S_kk|<rho` for every `k in T`.

Since `sum w_k^2=1`,

`|w^T diag(S) w|<rho`.

Together with (7.3),

`|w^T(S-diag S)w|>eta-rho=eta/2.`                              (7.6)

Randomly bipartition `T=I union J`. Define

`Z_I=w_I^T S[I,J] w_J`.

Each ordered off-diagonal pair lands from `I` to `J` with probability `1/4`, so

`E Z_I=(1/4)w^T(S-diag S)w`.

Hence some deterministic cut satisfies

`|w_I^T S[I,J]w_J|>eta/8.`                                    (7.7)

Because `||w_I|| ||w_J||<=1/2`,

`|w_I^T S[I,J]w_J|
 <=sigma_1(S[I,J]) ||w_I|| ||w_J||
 <=(1/2)sigma_1(S[I,J]).`

Therefore

`boxed( sigma_1(S[I,J])>eta/4=9/1120. )`                       (7.8)

Thus the current one-effective-direction residual has been reduced to the following strict dichotomy:

- a physical Schur diagonal at least `9/560`, in which case (7.5) gives a universal density bound; or
- an original-coordinate cut of the pair Schur complement carrying one cross singular value strictly larger than `9/1120`.

This is stronger than retaining only the mixed aggregate compression. It does **not** claim a second cross singular direction, and therefore does not misuse the latest fleet02/B04 two-cross theorem.

## 8. First unpaid implication

The first local missing step is now:

### `QFORM-INDEFINITE-PAIR-ONE-CROSS-SPLICE-v1` — OPEN

Given a uniformly nondegenerate physical indefinite pair `B` and its Schur complement `S`, assume an original-coordinate cut of `S` has one cross singular value bounded below universally. Prove a universal linear small-ball / `L^infinity` estimate for the full quadratic form while preserving the original product law; or show that every failure forces a physical Schur diagonal large enough for Theorem 5.1, or a second cross direction with leverage control so that fleet02/B04's two-cross bridge applies.

The remaining problem cannot be solved by conditioning on a rotated singular coordinate or on an orthogonal complement: the live corrections explicitly prohibit treating those conditional marginals as density-capped independent coordinates.

At the full-target level, the complementary `s_2(A-diag A)>1/8` branch also still requires product-preserving extraction/aggregation. The full conjecture therefore remains open.

## 9. Status and nonclaims

**Proved here:**

- quarter-power quadratic bathtub Lemma 3.1;
- a fully explicit binary-indefinite `L^3` constant `900^(1/3)` replacing the unspecified HLS constant in the existing binary theorem;
- explicit scalar-pivot constant `4 sqrt(30)` for an indefinite binary Schur complement;
- Theorem 5.1 for every invertible physical triple with an indefinite physical face, with explicit constant `2^(15/4)` when `m>0` and the completed fleet02/B04 endpoint bound when `m=0`;
- explicit genuinely rotated indefinite example with target spectrum `{3,1,-2}` and density bound `<7.698`;
- in fleet03/B19's newest one-effective branch, either immediate density bound `<41.768` or a Schur cross singular value `>9/1120`.

**Not proved:** the one-cross splice, the complementary global structural branch, the full conjecture, or continuity in the new quarter-power branches.

**Provenance / integrity:** current owner controls and the live correction inbox were refreshed before publication. No pointwise scalar oscillatory-decay claim or post-rotation independence is used. Only mathematical repository reads/writes were performed. No email, Drive action, public release, scheduler mutation, notification change, remote workflow, paid model/API/Codex call, permission expansion, credentials, machine paths, or unrelated private data were used.
