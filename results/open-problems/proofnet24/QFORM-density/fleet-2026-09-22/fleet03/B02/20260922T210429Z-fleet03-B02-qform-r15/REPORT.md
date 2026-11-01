SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-22T21:04:29Z.
attacking: the exact integrated-Fourier route after the normalized-copy logarithmic obstruction, by keeping a third physical square inside an L3 vector-valued amplitude before the rank-two bilinear Plancherel step.

# fleet03/B02 QFORM r15 — one-sided square plus exact-rank-two integrated Fourier closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T210429Z-fleet03-B02-qform-r15`  
**Assignment:** Integrated Fourier estimate  
**Startup owner control:** revision `2026-09-22.15`, QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** proved on the new theorem's stated branch because its characteristic function is in `L1`; not proved for the full target.

## 1. Exact target and what this run changes

The parent target is unchanged: for every finite dimension, every vector of independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal constant, or produce a target-valid counterexample. Continuity is a separate desired conclusion.

The live correction state still rules out law-uniform pointwise quadratic-phase decay. It also records a logarithmic loss in the obvious normalized independent-copy implementation. I found no source-valid counterexample to the exact target-wide criterion `int |phi_Q(t)| dt < infinity`, and therefore do not mark that criterion false.

This run first isolates why the phase-space copy kernel alone does not close the one-dimensional time trace, then changes mechanism on the same target: keep a genuine third physical square inside an `L3_t` amplitude and combine it with a genuine rank-two physical cross block by bilinear Plancherel. The result below gives an actual `L1_t` characteristic-function estimate and therefore a bounded continuous density. It is not a full-target theorem because it assumes a one-sided isolation relation and an exact rank-two cross block.

## 2. Source-valid dependencies actually used

### 2.1 Designated partner fleet04/B02

Completed partner theorem `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`:

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

If a nonsingular physical principal `3x3` block `D` has one zero diagonal entry, then the full ambient form, with arbitrary outside spectrum/couplings, has a continuous density and

`||p_Q||_infinity <= 3*2^(2/3)|det D|^(-1/3)`.                 (2.1)

It also proves the branchwise integrated estimate

`int_R |phi_Q(t)|^2 dt <= 6*pi*2^(2/3)|det D|^(-1/3)`.         (2.2)

I apply (2.2) to an actual low-frequency inequality in Section 8.

### 2.2 Rectangular cross-block Plancherel theorem

Fleet01/B03 `QFORM-COPY-RECTANGULAR-CROSS-v1`, canonical source

`yspennstate/math-open-problems@3d6fefe9c92674dff38c97ef8a502787ec3426a2`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/fleet01-B03-20260922T144815Z/REPORT.md`.

Its proof establishes the dependence-safe bilinear Plancherel mechanism with arbitrary same-bank phases. I rederive the two-dimensional instance below because here one bank amplitude carries the new physical-square `L3_t` weight.

### 2.3 Projection density cap

For an orthogonal two-dimensional projection of a product law with one-dimensional density caps one, the Livshyts--Paouris--Pivovarov marginal theorem gives density cap at most `2`. If the active bank itself consists of exactly two original coordinates, an orthogonal change of those two coordinates preserves the joint-density cap `1`.

No post-rotation independence is asserted: projected variables are used only through their joint marginal density caps.

## 3. A small copy-kernel observation and why it is not enough by itself

For one coordinate density `f<=1`, define

`kappa_f(u,v)=1/2 f((v+u)/2) f((v-u)/2)`,

`K_f(u,s)=int_R exp(i s v) kappa_f(u,v) dv`.

Then `kappa_f<=1/2`, `int int kappa_f=1`, and for every finite `q>=2`, Hausdorff--Young plus `kappa<=1/2` gives

`int_R int_R |K_f(u,s)|^q ds du <= pi`.                         (3.1)

Indeed, for fixed `u`,

`||K_f(u,.)||_q <= (2*pi)^(1/q)||kappa_f(u,.)||_(q/(q-1))`,

and after raising to `q`,

`||K_f(u,.)||_q^q <= 2*pi int kappa_f(u,v)^(q/(q-1)) dv
                 <= pi int kappa_f(u,v) dv`.

Integrating `u` yields (3.1). More generally, for every measurable scalar `a(u)`, change variables `s=t a(u)` to obtain the exact weighted trace estimate

`int int |a(u)| |K_f(u,t a(u))|^q du dt <= pi`.                (3.2)

This is a useful phase-space endpoint, but it does not itself control the one-dimensional time trace. For `f=1_[0,1]`,

`K_f(0,s)=exp(i s) sin(s)/s`,

so the individual slice has infinite `L1_s` norm. Thus one must retain a genuinely joint third smoothing mechanism before taking absolute values. This is a mechanism obstruction, not a counterexample to the target-wide `int|phi_Q|` criterion.

## 4. Scalar physical-square `L3` lemma

### Lemma 4.1

Let `Z` be a real random variable with probability density `f_Z<=1`. For arbitrary real `ell` and `d!=0`, put

`g_(d,ell)(t)=E exp(i t(d Z^2+2 ell Z))`.

Then

`boxed( ||g_(d,ell)||_3 <= 2(2*pi)^(1/3)|d|^(-1/3). )`        (4.1)

The bound is uniform in the affine coefficient `ell`.

### Proof

Complete the square. Translation of `Z` preserves the cap one, so it suffices first to take `d=1`, `ell=0`. If `Y` has density `f<=1`, the density of `Y^2` is

`h(w)=[f(sqrt(w))+f(-sqrt(w))]/[2 sqrt(w)]`, `w>0`.

Using `(a+b)^(3/2)<=sqrt(2)(a^(3/2)+b^(3/2))`, changing variables `w=x^2`, and `f^(3/2)<=f`,

`int_0^infinity h(w)^(3/2) dw
 <= int_R f(x)|x|^(-1/2) dx`.                                  (4.2)

Among probability densities bounded by one, the right side is maximized by filling the unit amount of mass closest to zero, namely on `[-1/2,1/2]`; hence

`int_R f(x)|x|^(-1/2) dx <= 2 sqrt(2)`.                         (4.3)

Therefore `||h||_(3/2)<=2`. Hausdorff--Young, with the Fourier convention used throughout this programme, gives

`||hat h||_3 <= (2*pi)^(1/3)||h||_(3/2) <=2(2*pi)^(1/3)`.      (4.4)

Scaling the time variable by `d` gives (4.1). QED.

This lemma is an integrated statement; no pointwise decay of `g_(d,ell)(t)` is asserted.

## 5. Main theorem — `QFORM-ONE-SIDED-SQUARE-RANK2-FOURIER-v1`

Partition original coordinates into four disjoint blocks

`{Z} union I union J union W`.

Let `d=A_ZZ!=0`. Assume

1. the selected physical coordinate `Z` has **no quadratic coupling to the right bank** `J`:

   `A[Z,J]=0`;                                                   (5.1)

   coupling of `Z` to `I` and to the outside block `W` is arbitrary;

2. the physical cross block

   `B=A[I,J]`                                                     (5.2)

   has exact rank two, with nonzero singular values `sigma_1,sigma_2` and

   `Delta=sigma_1 sigma_2>0`;

3. for a thin SVD `B=L Sigma R^T`, the two-dimensional projection densities of

   `P=L^T X_I`, `S=R^T X_J`

   obey

   `||p_P||_infinity<=M_L`, `||p_S||_infinity<=M_R`.            (5.3)

Then the full ambient quadratic form, allowing arbitrary same-bank quadratic terms, arbitrary outside spectrum, and arbitrary couplings not forbidden by (5.1), has an integrable characteristic function and therefore a bounded continuous density satisfying

`boxed(
 ||p_Q||_infinity
 <= [16/6^(3/4)] (M_L M_R)^(3/8)
    |d|^(-1/4) Delta^(-3/8).
)`                                                              (5.4)

Numerically,

`16/6^(3/4)=4.173558880...`.                                    (5.5)

For arbitrary product cap-one banks, (5.3) holds with `M_L,M_R<=2`, giving

`boxed(
 ||p_Q||_infinity
 <7.019062 |d|^(-1/4) Delta^(-3/8).
)`                                                              (5.6)

If both active banks consist of exactly two original physical coordinates, `M_L=M_R=1`, so the prefactor is `<4.173559`.

### Remarks on scope

The exact-rank-two condition is real: higher cross directions cannot simply be deleted from the phase. Likewise, (5.1) is a physical-coordinate one-sided isolation condition, not an eigenbasis assumption. The theorem is supporting progress, not a claim that the spectral hypothesis `s_3(A)>=1` forces this configuration.

## 6. Proof of the main theorem

Condition on all outside original coordinates `W=w`. Independence of the original inputs is preserved. By (5.1), after absorbing the outside values into affine terms, the conditional polynomial can be written

`Q_w(z,x,y)
 = d z^2 +2 z ell_w(x)+F_w(x)+G_w(y)+2 x^T B y+c_w`,            (6.1)

where `ell_w` is affine in the left-bank original coordinates, while `F_w,G_w` are arbitrary quadratic-affine functions. The same-bank curvature is retained exactly.

Disintegrate the left bank over `P=L^T X_I` and define

`a_(t,w)(p)
 =p_P(p) E[ exp(i t F_w(X_I))
             g_(d,ell_w(X_I))(t) | P=p ]`.                      (6.2)

Disintegrate the right bank over `S=R^T X_J` and define

`b_(t,w)(s)
 =p_S(s) E[exp(i t G_w(X_J)) | S=s]`.                           (6.3)

Set

`A_w(t)=||a_(t,w)||_2`.                                         (6.4)

Because `|b_(t,w)|<=p_S`,

`||b_(t,w)||_2<=sqrt(M_R)`.                                     (6.5)

For the left amplitude, Jensen and `p_P^2<=M_L p_P` give

`A_w(t)^2
 <= M_L E_X |g_(d,ell_w(X))(t)|^2`.                            (6.6)

Taking the `L^(3/2)` norm of the square, Minkowski, and Lemma 4.1 yield

`||A_w||_3
 <= sqrt(M_L) * 2(2*pi)^(1/3)|d|^(-1/3),`                     (6.7)

uniformly in `w`.

The conditional characteristic function is now the genuine two-dimensional bilinear integral

`phi_w(t)
 =exp(i t c_w) int int a_(t,w)(p)b_(t,w)(s)
       exp(i 2t p^T Sigma s) dp ds`.                             (6.8)

Bilinear Plancherel in dimension two gives

`|phi_w(t)|
 <= pi |t|^(-1) Delta^(-1/2)
    A_w(t) sqrt(M_R)`.                                          (6.9)

Indeed, integration in `p`, Cauchy--Schwarz in `s`, the change `xi=2t Sigma s`, and ordinary two-dimensional Plancherel produce exactly the factor `pi/(|t|sqrt(Delta))`.

Average over `W` and set

`Abar(t)=E_W A_w(t)`.                                           (6.10)

Then

`|phi_Q(t)|
 <= min{1, pi sqrt(M_R) Delta^(-1/2)|t|^(-1) Abar(t)},`         (6.11)

and Minkowski together with (6.7) gives

`||Abar||_3
 <=2(2*pi)^(1/3)sqrt(M_L)|d|^(-1/3).`                         (6.12)

For any `T>0`, split frequency. On the central interval,

`int_(|t|<=T)|phi_Q(t)|dt <=2T`.                                (6.13)

On the tails, Holder with exponents `3` and `3/2` gives

`int_(|t|>T)|phi_Q(t)|dt
 <= H T^(-1/3)`,                                                (6.14)

where

`H=2^(8/3) pi^(4/3)(M_L M_R)^(1/2)
   |d|^(-1/3) Delta^(-1/2)`.                                   (6.15)

Here we used

`[int_(|t|>T)|t|^(-3/2)dt]^(2/3)
 =4^(2/3)T^(-1/3)`.                                             (6.16)

Optimizing `2T+H T^(-1/3)` gives

`T=(H/6)^(3/4)` and

`boxed( ||phi_Q||_1 <=8(H/6)^(3/4). )`                         (6.17)

Substituting (6.15), dividing by `2*pi`, and simplifying gives exactly (5.4). Because `phi_Q` is integrable, Fourier inversion gives a continuous density vanishing at infinity, not merely an essential `L^infinity` representative. QED.

## 7. Why this avoids the live corrections

The proof never assumes:

- pointwise `|t|^(-1/2)` scalar Fresnel decay;
- moments, Gaussianity, log-concavity, compact or connected support;
- independence after rotating the random vector;
- a cap on a conditional sum/difference density;
- a universally good fixed physical minor from `s_3(A)>=1`;
- the refuted arbitrary-joint rank-three coarea theorem;
- a conditional projection-height positive moment.

The only rotated objects `P,S` are marginal projections, used through source-valid joint density caps. The time integration is joint: the third square's `L3_t` resource is kept inside the left complex amplitude until after the rank-two cross-bank Plancherel step.

## 8. Actual application of designated partner fleet04/B02

There is a useful overlap where the designated partner gives a second low-frequency resource. Suppose the hypotheses of Theorem 5 also hold and, elsewhere in the same ambient form, there is a nonsingular physical principal `3x3` block `D` having an exact zero diagonal. Then fleet04/B02 gives (2.2). By Cauchy--Schwarz,

`int_(|t|<=T)|phi_Q(t)|dt
 <= A_0 T^(1/2)`,                                               (8.1)

where

`A_0=2^(1/3)sqrt(12*pi)|det D|^(-1/6)`.                         (8.2)

The high-frequency estimate (6.14) remains available. Hence

`||phi_Q||_1 <= A_0 T^(1/2)+H T^(-1/3)`.                        (8.3)

Optimizing at

`T=[2H/(3A_0)]^(6/5)`                                          (8.4)

gives

`||phi_Q||_1
 <=(5/2)(2/3)^(3/5) A_0^(2/5) H^(3/5)`.                       (8.5)

Therefore the partner-plus-new-Fourier hybrid yields the continuous-density estimate

`boxed(
 ||p_Q||_infinity
 <= 5*2^(11/15)*3^(-2/5)
    |det D|^(-1/15)(M_L M_R)^(3/10)
    |d|^(-1/5) Delta^(-3/10).
)`                                                              (8.6)

The numerical prefactor is

`5*2^(11/15)*3^(-2/5)=5.356447253...`.                          (8.7)

This is an actual use of the completed designated partner theorem in the frequency integral. On the same overlap one may of course also retain the partner's direct continuous-density bound (2.1); the best available estimate is the minimum of (2.1), (5.4), and (8.6).

At the exact endpoint `d=0`, Theorem 5 does not apply. If the relevant physical triple satisfies the partner hypotheses, (2.1) is the correct endpoint statement; no near-zero conclusion is inferred by continuity.

## 9. Relation to existing rank-two square smoothing

Fleet03/B06 previously proved a dependence-safe physical-space theorem for a genuine square plus an exact rank-two cross residual, with scale `|d|^(-1/2)Delta^(-1/4)` and essential boundedness. The theorem here is complementary:

- it proves the characteristic function itself is `L1` and therefore supplies continuity;
- it has the different interpolation scale `|d|^(-1/4)Delta^(-3/8)`;
- it allows the selected square coordinate to couple arbitrarily to the left bank while forbidding only coupling to the right bank.

Neither theorem should be promoted beyond its stated interface.

## 10. Full-target status and first unpaid implication

The full conjecture remains OPEN. No exact-target counterexample to target-wide unweighted `int|phi_Q|` control has been proved here.

The new theorem closes a concrete joint-Fourier `1+2` packet. The first unpaid implication for this B02 route is now structural and quantitative:

> Starting from only `s_3(A)>=1`, prove that either a completed localized/diffuse/grouped certificate fires, or after a product-preserving physical partition one can obtain a quantitative one-sided square plus exact-rank-two cross packet with the scale `|d|^(1/4) Delta^(3/8)` bounded below; otherwise extend the vector-valued `L3_t` argument so that nonzero coupling of the square coordinate to both cross banks is retained rather than conditioned away.

The most promising analytic successor is the second option: a **two-sided square / rank-two bilinear vector-valued estimate** in which the third-square coefficient depends on both bank variables, while keeping all original-coordinate product provenance. That is exactly where the present proof uses (5.1).

## 11. Integrity / quantifier audit

Used: independent original coordinates; one-dimensional density caps one; arbitrary dimension; arbitrary signs; arbitrary same-bank quadratic curvature; arbitrary outside spectrum and couplings except the explicit one-sided zero block; exact rank-two physical cross block; source-valid projection caps.

Not used: moments, identical distributions, support regularity, Gaussian/log-concave hypotheses, diagonal-basis independence, pointwise scalar phase decay, Monte Carlo evidence, arbitrary-joint coarea, worst-fiber supremum, or hidden compactness.

The conclusion on the new theorem's branch is a **bounded continuous density** because `phi_Q in L1`. The full-target continuity claim remains OPEN.
