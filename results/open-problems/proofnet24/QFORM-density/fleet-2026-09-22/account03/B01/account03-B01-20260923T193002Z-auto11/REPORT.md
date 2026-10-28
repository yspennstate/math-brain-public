SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T19:30:02Z.
attacking: the exact projected-crossing-zero near-null leakage endpoint; classify it as diagonal plus one aligned collective square, then average the translated pair singularity against a whole-bank square-root small-ball estimate.

# account03/B01 — exact aligned near-null receiver, stable through nonzero determinant

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T193002Z-auto11`  
Role: oscillatory replacement / quantitative inequalities  
Status: **PROVED SUPPORTING TARGET-LEVEL BRANCH; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The full target is unchanged: for every finite `n`, every independent real `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density bounded by one universal constant, or exhibit a valid counterexample. No moment, support, log-concavity, centering, identical-law, or spectral-coordinate independence assumption is available.

Fresh control was read from `yspennstate/math-research-brain/main` at start commit
`12cf271a0a54404d06f9cd54cc0630bc7a0fdc68` and refreshed before publication at

The following corrections are retained throughout:

* law-uniform pointwise quadratic Fresnel decay is false for arbitrary cap-one densities;
* a rotation of the original independent coordinates does not preserve independence;
* an arbitrary bounded projection density does not by itself control an indefinite quadratic pushforward;
* small matrix coefficients cannot be discarded as small random perturbations without moment assumptions.

The result below is therefore phrased in original-coordinate scalar-completion variables and uses an averaged fractional-potential/small-ball mechanism rather than a false scalar pointwise decay estimate.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner account04/B01: singular/near-singular star identity

Source:
`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

For a physical pair

`B=[[a,b],[b,c]]`, `a!=0`,

complete the original coordinate corresponding to `a`. With

`delta=det(B)/a`,

leaf leakage vector `ell`, and leaf residual matrix `M`, the partner proves the exact identity

`W2 = a^2 sum_(k!=l) (delta M_kl-ell_k ell_l)^2`.              (2.1)

Its leakage branch gives

`L(ell):=sum_(k!=l)ell_k^2 ell_l^2 >= W2/(4a^2)`.             (2.2)

I use only this source-valid inequality and identity. I do **not** use the previously corrected stronger claim that two colored banks separately inherit the same lower bound.

### 2.2 Designated partner account04/B01: signed Fejer equivalence

Source:
`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a law `mu` with characteristic function `phi`, define

`D_T mu(y)=(1/(2 pi)) int_(-T)^T (1-|t|/T) Re(exp(-ity)phi(t)) dt`.  (2.3)

The partner proves exactly

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                   (2.4)

whenever either side is finite, in the measure-theoretic bounded-density sense. Thus every density estimate below immediately gives the requested signed averaged-frequency estimate without absolute Fourier `L^1` control.

### 2.3 Whole-bank rank-one separable small-ball theorem

Source:
`yspennstate/math-open-problems@8d0cfcc9b0b1e88eee6fba2e63187d8607ca2d0c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T080010Z-account02-B14-QFORM-r31/REPORT.md`.

Let independent cap-one `Z_i`, a unit vector `v`, `c=max_i v_i^2<1`, `lambda!=0`, and arbitrary measurable one-coordinate phases `u_i` be given. For

`W=lambda(v^T Z)^2 + sum_i u_i(Z_i)`,                          (2.5)

that theorem gives the translation-uniform square-root small-ball estimate

`sup_s P(|W-s|<=rho) <= C0 eta(c)|lambda|^(-1/2) sqrt(rho)`,   (2.6)

where

`C0=2^(3/4) sqrt(e) Gamma(1/4)=10.053118753721757...`,         (2.7)

and

`eta(c)=1` for `c<=1/2`,
`eta(c)=[4c(1-c)]^(-1/4)` for `1/2<c<1`.                      (2.8)

The source explicitly allows arbitrary diagonal quadratic and affine twists through the `u_i`.

### 2.4 Translated quadratic kernel

Source:
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Define

`Psi(s)=1+log(1/|s|)` for `0<|s|<=1`,
`Psi(s)=|s|^(-1/4)` for `|s|>=1`, and `Psi(0)=+infinity`.       (2.9)

For any cap-one probability density `f`,

`int f(x)|s-x^2|^(-1/2) dx <=8 Psi(s)`.                       (2.10)

If a random variable `V` satisfies

`P(|V|<rho)<=L sqrt(rho)` for every `rho>0`,                    (2.11)

then

`E Psi(V)<=4 sqrt(L)`.                                        (2.12)

These are the exact tools used to average the translated near-null quadratic singularity.

## 3. Scalar-completed model

After completing one original coordinate of the partner physical pair, all affine terms retained, the relevant conditional form may be written

`Q = a (X+h(Y,Z))^2 + R(Y,Z)`,                                (3.1)

where `X`, `Y`, and the leaf coordinates `Z=(Z_1,...,Z_m)` are disjoint original-coordinate variables and therefore remain mutually independent before conditioning. The translation `h` may depend arbitrarily affinely on `(Y,Z)`. The residual is

`R = delta Y^2 + 2Y(ell^T Z+beta) + Z^T M Z + q^T Z + gamma Y + d`, (3.2)

with `M=M^T`. Constants and linear terms will never be discarded.

The outer scalar-square shell estimate gives, for every interval `I` of length `|I|`, uniformly in the correlated translation `h`,

`P(Q in I) <= |I| |a|^(-1/2) H_(1/2)(R)`,                     (3.3)

where

`H_(1/2)(R)=sup_w E|R-w|^(-1/2)`.                             (3.4)

Thus the essential task is to bound the half-Riesz potential of `R` without dividing by a tiny `delta`.

## 4. First routing invariant: projected one-volume

For each leaf index `i`, let `J_i={1,...,m}\{i}`. When `ell_(J_i)!=0`, define the projected row

`C_i=M[i,J_i](I-P_(ell_(J_i)))`,                               (4.1)

and put `C_i=0` when `ell_(J_i)=0`. Define

`Gamma1(ell,M)=max_i ||ell_(J_i)||_2 ||C_i||_2`.               (4.2)

The current account02/B01 projected-crossing theorem (`QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`) applied with hub `Y`, one promoted leaf `Z_i`, and untouched bank `Z_(J_i)` gives immediately, whenever `Gamma1>0`,

`boxed: ||p_Q||_infinity <=8 |a|^(-1/2) Gamma1^(-1/4).`       (4.3)

This is already stable under arbitrary same-bank quadratic curvature and has no row-concentration or rank hypothesis. By (2.4),

`sup_(T,y) D_T law(Q)(y) <=8 |a|^(-1/2) Gamma1^(-1/4)`.       (4.4)

The genuinely new work below handles the exact endpoint `Gamma1=0` and shows that this endpoint has much more structure than the preceding diagonal-plus-rank-five description.

## 5. Exact classification of the aligned endpoint

### Theorem 5.1 — `QFORM-PROJECTED-Z1-ZERO-ALIGNED-RANK1-v1`

Assume

`L(ell)=sum_(k!=l)ell_k^2 ell_l^2>0`                           (5.1)

and

`Gamma1(ell,M)=0`.                                             (5.2)

Then there are a real scalar `tau` and a real diagonal matrix `D` such that

`boxed: M = D + tau ell ell^T.`                                (5.3)

In particular, every nonseparable leaf-leaf interaction is carried by the **same one-dimensional direction** as the hub leakage.

### Proof

Condition (5.1) says that `ell` has at least two nonzero coordinates. Therefore, for every `i`, the vector `ell_(J_i)` is nonzero. Since `Gamma1=0`, (4.1) vanishes for every `i`, so there is a scalar `alpha_i` such that

`M_ij=alpha_i ell_j` for every `j!=i`.                         (5.4)

Symmetry of `M` gives, for all `i!=j`,

`alpha_i ell_j=alpha_j ell_i`.                                (5.5)

On the support of `ell`, (5.5) implies that `alpha_i/ell_i` is one common scalar `tau`: there is always another nonzero support coordinate because the support has size at least two. If `ell_i=0`, choose `j` with `ell_j!=0`; then (5.5) gives `alpha_i ell_j=0`, hence `alpha_i=0=tau ell_i`. Therefore

`alpha_i=tau ell_i` for every `i`,                             (5.6)

and hence

`M_ij=tau ell_i ell_j` for all `i!=j`.                         (5.7)

Set `D_ii=M_ii-tau ell_i^2`. Then (5.3) follows. QED.

### Partner consequence

In the partner leakage branch with `W2>0`, (2.2) implies `L(ell)>0`, so Theorem 5.1 applies automatically at every exact `Gamma1=0` leakage state.

This improves the previous B01 exact-zero endpoint `M=diagonal+rank<=5` to `M=diagonal+one aligned rank-one square` under the actual leakage hypothesis.

## 6. Main analytic theorem: the aligned near-null branch is uniformly paid

Assume now

`delta!=0`, `Gamma1=0`, and `W2>0`.                              (6.1)

By Theorem 5.1,

`M=D+tau ell ell^T`.                                           (6.2)

Complete the original coordinate `Y` in (3.2). All `beta`, `gamma`, `q`, and constant terms only alter the translation or the resulting affine leaf phase. Thus

`R = delta (Y+g(Z))^2 + W(Z)`,                                (6.3)

where

`W(Z)=Z^T D Z + kappa (ell^T Z)^2 + r^T Z + d0`,              (6.4)

with

`kappa=tau-1/delta`.                                           (6.5)

Put

`r0=||ell||_2^2`, `v=ell/sqrt(r0)`, `c=max_i v_i^2`,
`lambda=kappa r0=((delta tau-1)/delta)r0`.                     (6.6)

Because `W2>0`, identity (2.1) in the aligned situation gives

`W2=a^2(delta tau-1)^2 L(ell)>0`.                              (6.7)

Hence `delta tau-1!=0`, `lambda!=0`, and `ell` has at least two nonzero coordinates, so `c<1`.

The whole-bank theorem (2.6) applies to `W`: the diagonal quadratic terms and affine terms in (6.4) are precisely the allowed one-coordinate phases. Therefore, uniformly in `w` and `rho`,

`P(|W-w|<rho) <= H sqrt(rho)`,                                 (6.8)

where

`H=C0 eta(c)|lambda|^(-1/2)`.                                 (6.9)

Now fix `w`. Conditional on `Z`, translate the cap-one law of `Y` in (6.3) and use (2.10):

`E_Y |R-w|^(-1/2)
 <= 8 |delta|^(-1/2) Psi((w-W)/delta).`                        (6.10)

For

`V=(w-W)/delta`,                                               (6.11)

(6.8) gives

`P(|V|<rho)<=H |delta|^(1/2) sqrt(rho)`.                       (6.12)

Apply (2.12) to (6.10):

`H_(1/2)(R)
 <=32 |delta|^(-1/2) sqrt(H |delta|^(1/2))`
` =32 sqrt(C0) |delta|^(-1/4) eta(c)^(1/2)|lambda|^(-1/4)`
` =32 sqrt(C0) eta(c)^(1/2)
      |delta tau-1|^(-1/4) r0^(-1/4).`                        (6.13)

**The dangerous factor `|delta|^(-1/4)` cancels exactly.** This is the central point of the run: the nonzero near-singular physical-pair determinant is not paid reciprocally once the aligned bank is aggregated before the pair singularity is averaged.

## 7. Exact cancellation with the partner `W2` currency

Write

`w_i=ell_i^2/r0`, `sum_i w_i=1`, `c=max_i w_i`, and
`mathcalL=1-sum_i w_i^2=L(ell)/r0^2`.                          (7.1)

From (6.7),

`|delta tau-1|^(-1/4) r0^(-1/4)
 = |a|^(1/4) W2^(-1/8) mathcalL^(1/8).`                       (7.2)

The heavy-leverage factor in (6.13) cancels against the normalized partner leakage volume:

* if `c<=1/2`, then `eta(c)=1` and `mathcalL^(1/8)<=1`;
* if `c>1/2`, then

  `eta(c)^(1/2) mathcalL^(1/8)
   =[mathcalL/(4c(1-c))]^(1/8)`.                              (7.3)

  Since

  `mathcalL=1-sum_i w_i^2 <=1-c^2=(1-c)(1+c)`,                (7.4)

  we obtain

  `mathcalL/[4c(1-c)] <=(1+c)/(4c)<=3/4<1`.                  (7.5)

Thus in every case

`eta(c)^(1/2) mathcalL^(1/8)<=1`.                             (7.6)

Combining (3.3), (6.13), (7.2), and (7.6) proves:

### Theorem 7.1 — `QFORM-ALIGNED-NEARNULL-W2-RECEIVER-v1`

Under the scalar-completed model (3.1)-(3.2), assume the account04/B01 leakage branch, `W2>0`, `delta!=0`, and `Gamma1=0`. Then the full quadratic form has an essentially bounded density with

`boxed: ||p_Q||_infinity
 <= 32 sqrt(C0) |a|^(-1/4) W2^(-1/8)
 < 101.462 |a|^(-1/4) W2^(-1/8).`                             (7.7)

Numerically,

`32 sqrt(C0)=101.46129115978704...`.                           (7.8)

No lower bound on `|delta|` appears.

At `delta=0`, the previously completed exact-singular arbitrary-curvature receiver already gives the much sharper

`||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)|a|^(-1/4)W2^(-1/8)
 =7.263544634846275... |a|^(-1/4)W2^(-1/8).`                 (7.9)

Thus the **exact aligned endpoint is now paid on both sides of `delta=0`**, with a universal `W2`-scale estimate and no reciprocal determinant blow-up.

## 8. Averaged-frequency consequence: designated partner applied to the new inequality

Apply account04/B01's exact signed-Fejer equivalence (2.4) to Theorem 7.1. For every aligned nonzero-determinant state above,

`boxed: sup_(T>0,y) D_T law(Q)(y)
 <=101.462 |a|^(-1/4)W2^(-1/8).`                              (8.1)

At the exact singular endpoint replace `101.462` by `7.264` using (7.9).

This is the required averaged-frequency replacement. It is deliberately weaker than absolute Fourier integrability and keeps signed cancellation. No scalar law-uniform `|t|^(-1/2)` assertion is made.

## 9. The phase-aligned pointwise counterexample remains valid

Fix any prescribed frequency `s>0` and `0<epsilon<pi/2`. The set

`E={x: dist(s x^2,2 pi Z)<=epsilon}`                           (9.1)

has infinite Lebesgue measure. Choose a finite measurable subset `F subset E` with Lebesgue measure one and take the admissible density `f=1_F`. Then

`Re E exp(i s X^2)>=cos(epsilon)`.                             (9.2)

Therefore no positive law-uniform pointwise power decay for a scalar quadratic phase is available. Theorem 7.1 does not weaken this correction: it first aggregates the independent leaf bank into a translation-uniform square-root small-ball estimate and only then averages the translated quadratic singularity.

## 10. Scaling and deterministic consistency checks

Under the global rescaling `A -> q A`:

`a, delta, ell, M -> q(a,delta,ell,M)`,
`Gamma1 -> |q|^2 Gamma1`,
`W2 -> |q|^6 W2`.                                              (10.1)

Consequently (4.3) and (7.7) both scale exactly as `|q|^(-1)`, as a density must.

The heavy-leverage cancellation uses only

`sup_(1/2<c<1) (1+c)/(4c)=3/4`,                                (10.2)

so no hidden dimension dependence enters. Numeric constants and these algebraic identities are recorded in sibling `CHECKS.txt`.

## 11. What remains unpaid

This run closes the **exact** projected-crossing-zero endpoint far more strongly than the previous diagonal-plus-rank-seven structural statement. The remaining B01 implication is now

`QFORM-NEARNULL-SMALL-POSITIVE-GAMMA1-INTERPOLATION-v1`.

When `Gamma1>0`, (4.3) pays the state but deteriorates like `Gamma1^(-1/4)`. When `Gamma1=0`, Theorem 7.1 gives a finite `W2`-scale bound independent of `delta`. What is still missing is a robust interpolation as `Gamma1 ->0+` under arbitrary cap-one laws and arbitrary same-bank curvature. One may not simply discard the transverse quadratic matrix as a small random perturbation, because no moments or support bounds are available.

A promising next mechanism is to keep the small transverse piece inside the signed-Fejer or half-Riesz average and prove stability of the aligned receiver at the distribution-function level. The fresh exact-rank physical-crossing theorem at `yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae` provides an independent high-cross-rank exit, but it does not by itself control this rank-one/aligned collar.

## 12. Scope and regularity

Theorem 7.1 proves **absolute continuity with an essentially bounded density** in its stated branch. It does not prove continuity of that density: the outer completed-square translation can be correlated with the same variables generating `R`, and the shell/half-Riesz argument only yields an interval domination bound.

The unrestricted three-large-eigenvalue theorem remains **OPEN**. No counterexample to QFORM was found.
