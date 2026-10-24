SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-22T20:12:16Z.
attacking: ambient physical-pivot collision energy, the rank-one endpoint splice, and a dependence-safe correction using the latest account03/B03 cross-bank theorem.

# account02/B03 r12 — ambient pivot collision energy and the critical rank-one endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Control source at derivation start: `yspennstate/math-research-brain@634fdbcb1dbac8330117f165cca73666c1f7e8e1`; fresh pre-publication refresh: `e1c830c5a4d618f25cd5bab07b64fd33ce950052`; OWNER CONTROL revision `2026-09-22.15`.

## 1. Exact target and correction boundary

The owner target remains the unrestricted statement: for arbitrary independent original-coordinate real inputs with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `Q=X^TAX`, or give a target-valid counterexample.

This report does not use law-uniform pointwise scalar Fresnel decay, post-rotation independence, the false conditional cap for a sum/difference conjugate pair, the false arbitrary-joint rank-three coarea lemma, the false positive conditional-projection-density moment, or a fixed-good-minor / single-Schur extraction assertion. All conditioning below is on original coordinates, and the independent-copy transform is used only through exact characteristic-function identities.

The newest designated partner result actually consumed is account03/B03 run `20260922T190034Z-account03-B03-QFORM-r18`, canonical mathematics

`yspennstate/math-open-problems@d18302d55f907552185a42994d48b09f39737cbd`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T190034Z-account03-B03-QFORM-r18/REPORT.md`.

Its source-valid cross-bank collision consequence is recorded explicitly in Section 5 below.

I also use the completed account01/B03 all-exponent square-collision theorem, current source-read at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/account01-B03-20260922T195138Z-r15/REPORT.md`,

which proves translation-uniform square collision energy for every exponent `0<alpha<1`. The new step is to lift that one-coordinate estimate through an *arbitrary ambient quadratic form* by conditional Jensen, and at `alpha=1/2` to sharpen the constant by a separate `L^3` argument.

## 2. Sharp-enough `L^3` budget for one shifted square

### Lemma 2.1 — square `L^{3/2}` density and `L^3` characteristic norm

Let `X` have a probability density `f` with `0<=f<=M`, let `b` be arbitrary, and let

`Y=a(X-b)^2`, `a!=0`.

Then the density `g_Y` satisfies

`||g_Y||_(3/2) <= 2 M^(2/3) |a|^(-1/3)`,                         (2.1)

and with `psi(t)=E exp(itY)`,

`||psi||_3 <= 2(2pi)^(1/3) M^(2/3)|a|^(-1/3)`.                  (2.2)

Proof. By translation and scaling it is enough first to take `a=1`, `b=0`. For `r>0` put

`h(r)=f(r)+f(-r)`.

Then `0<=h<=2M`, `int_0^infinity h=1`, and the density of `X^2` obeys

`g(r^2)=h(r)/(2r)`.

Therefore

`int_0^infinity g(y)^(3/2)dy
 =2^(-1/2) int_0^infinity h(r)^(3/2)r^(-1/2)dr`

`<=2^(-1/2)(2M)^(1/2) int h(r)r^(-1/2)dr`.

The decreasing-weight bathtub principle under `h<=2M`, `int h=1` gives

`int h(r)r^(-1/2)dr <=2M int_0^(1/(2M)) r^(-1/2)dr=2sqrt(2M)`.

Hence `int g^(3/2)<=2sqrt(2)M`, and raising to the `2/3` power gives `||g||_(3/2)<=2M^(2/3)`. Scaling `y` by `a` gives (2.1). Hausdorff--Young in the convention `hat g(t)=int e^(ity)g(y)dy` gives (2.2). QED.

This is an integrated statement only; it does not contradict the live correction that no law-uniform pointwise quadratic Fresnel decay exists.

## 3. Improved half-collision constant for one square

### Lemma 3.1 — `QFORM-SQUARE-HALF-COLLISION-L3-v1`

Under the hypotheses of Lemma 2.1, let `X'` be an independent copy. Then

`E |a[(X-b)^2-(X'-b)^2]|^(-1/2)
 <= C_* M |a|^(-1/2)`,                                           (3.1)

where

`C_* = 16 sqrt(2)/3^(3/4) = 9.9264518304...`.                    (3.2)

Equivalently,

`int_R |t|^(-1/2)|psi(t)|^2 dt
 <= sqrt(2pi) C_* M |a|^(-1/2)`.                                (3.3)

Proof. Put `A=||psi||_3`. For `T>0`, use `|psi|<=1` on `|t|<=T` and Holder with exponents `3/2` and `3` on the tail:

`int |t|^(-1/2)|psi(t)|^2dt`
`<=4sqrt(T)+4^(1/3) A^2 T^(-1/6)`.                              (3.4)

The right side is minimized when `T^(2/3)=4^(1/3)A^2/12`, and the minimum is

`[8/3^(3/4)] A^(3/2)`.                                           (3.5)

Insert (2.2):

`A^(3/2)<=4sqrt(pi) M |a|^(-1/2)`,

so (3.3) follows. The positive one-dimensional Riesz identity

`E|Y-Y'|^(-1/2)=(2pi)^(-1/2)int |t|^(-1/2)|psi(t)|^2dt`

then gives (3.1). QED.

This improves the previously source-valid constant `14.2950...` in the same half-collision scope; the improvement is not itself a claim about the full QFORM density constant.

## 4. Main new theorem: one physical pivot controls the collision energy of the full ambient form

### Theorem 4.1 — `QFORM-AMBIENT-PIVOT-FRACTIONAL-COLLISION-v1`

Let `Z` be one original coordinate of an arbitrary product input vector and suppose its density is at most one. After exact physical square completion write the full quadratic form as

`Q=a(Z+h(W))^2+R(W)`, `a!=0`,                                    (4.1)

where `W` consists of all other original coordinates. No restriction is imposed on `h`, on `R`, on the dimension, signs, remaining spectrum, or couplings inside `W`.

For every `0<alpha<1`, let `C_alpha` be the explicit constant from account01/B03 `QFORM-SQUARE-COLLISION-RIESZ-ALL-ALPHA-v1`. Then

`boxed{
 int_R |t|^(alpha-1)|phi_Q(t)|^2dt
 <=2 Gamma(alpha) cos(pi alpha/2) C_alpha |a|^(-alpha).
}`                                                                  (4.2)

In particular the improved half-order estimate is

`boxed{
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <=sqrt(2pi) C_* |a|^(-1/2),
}`                                                                  (4.3)

and hence, for an independent copy `Q'`,

`boxed{
 E|Q-Q'|^(-1/2)<=C_* |a|^(-1/2),
 C_*=16sqrt(2)/3^(3/4)<9.927.
}`                                                                  (4.4)

Proof. Conditional on `W=w`, define

`psi_w(t)=E_Z exp(it a(Z+h(w))^2)`.

Then

`phi_Q(t)=E_W[exp(itR(W)) psi_W(t)]`.

By Jensen,

`|phi_Q(t)|^2<=E_W |psi_W(t)|^2`.                                 (4.5)

Multiply by the positive weight `|t|^(alpha-1)`, integrate, and use Tonelli. The account01/B03 all-exponent square theorem is uniform in the translation `h(w)`, so it yields (4.2). At `alpha=1/2`, Lemma 3.1 uniformly replaces its older constant by `C_*`, giving (4.3). The Riesz identity gives (4.4). QED.

### Matrix form

For an arbitrary symmetric matrix `A`, if `A_ii=a!=0`, physical completion in the original coordinate `X_i` gives exactly (4.1):

`Q=a(X_i+a^(-1)A_(i,-i)X_(-i))^2
  +X_(-i)^T[A_(-i,-i)-A_(-i,i)A_(i,-i)/a]X_(-i)`.

Thus (4.2)--(4.4) hold for the *entire* quadratic form whenever a nonzero physical diagonal is selected. This is not a conditional density assertion: it is a full-law collision estimate, and the shift/residual may remain arbitrarily dependent through `W`.

## 5. Actual application of the designated account03/B03 result

The partner report `QFORM-ISOTROPIC-CROSSBANK-HALF-RIESZ-v1` also reconciles the completed dependence-safe rectangular-cross theorem at collision level. If the same full quadratic form contains a physical original-coordinate cross block `B` of rank `r>=1` with positive singular-value product

`Delta_r=prod_{j=1}^r sigma_j(B)`,

then its independent-copy collision satisfies

`E|Q-Q'|^(-1/2)
 <= [8r/(2r-1)] Delta_r^(-1/(2r)).`                                (5.1)

This retains each copy pair jointly and does not condition a sum on a difference.

Combining the partner's actual inequality (5.1) with Theorem 4.1 gives the new hybrid certificate

`boxed{
 E|Q-Q'|^(-1/2)
 <= min{
   C_* |A_ii|^(-1/2),
   [8r/(2r-1)] Delta_r^(-1/(2r))
 }.
}`                                                                  (5.2)

For a rank-one cross block of singular value `sigma`,

`E|Q-Q'|^(-1/2)
 <= min{9.927 |A_ii|^(-1/2), 8 sigma^(-1/2)}.`                      (5.3)

This is an actual full-form inequality, not a comparison of unrelated packets. It gives two independent original-coordinate ways to pay the same collision potential.

For `r>=2`, the stronger one-copy half-Riesz consequence of the rectangular-cross theorem is already available and should be used; (5.2) is mainly informative at the critical `r=1` boundary.

## 6. Decisive endpoint obstruction: the rank-one splice cannot be completed from these certificates alone

A tempting next implication is false:

> critical pointwise decay `|phi(t)|=O(|t|^(-1/2))` plus all subcritical weighted collision energies `int |t|^(alpha-1)|phi(t)|^2<infinity`, `alpha<1`, should force `int |t|^(-1/2)|phi(t)|dt<infinity`.

It does not, even for the characteristic function of an admissible cap-one square law.

Take

`X ~ Uniform[-1/2,1/2]`, `Y=X^2`,

and let `psi(t)=E exp(itY)`. Then:

1. `Y` has density `g(y)=y^(-1/2) 1_(0,1/4)(y)`, so

`E Y^(-1/2)=int_0^(1/4) y^(-1)dy=infinity`.                        (6.1)

Thus the one-copy half-Riesz potential at zero is infinite, equivalently its signed/absolute critical-time upgrade cannot be obtained by a generic positive majorant.

2. Nevertheless `psi` obeys a genuine critical pointwise envelope. For `|t|>=1`, after `u=sqrt(|t|)x`,

`|psi(t)|<=2|t|^(-1/2) sup_(R>=0)|int_0^R exp(iu^2)du|`.

Splitting the Fresnel integral at `1` and integrating by parts on `[1,R]` gives the elementary uniform bound `sup_R |int_0^R exp(iu^2)du|<=5/2`; hence

`|psi(t)|<=5|t|^(-1/2)` for `|t|>=1`.                              (6.2)

3. Therefore for every `0<alpha<1`,

`int |t|^(alpha-1)|psi(t)|^2dt<infinity`,                           (6.3)

since the tail is bounded by a constant times `int_1^infinity t^(alpha-2)dt`. The stronger uniform square-collision theorem supplies quantitative versions of (6.3).

So (6.1)--(6.3) give an actual characteristic-function counterexample to the *functional-analytic splice*. This is not a counterexample to QFORM: it has only one quadratic spectral direction. It proves that at the rank-one endpoint one must retain additional product geometry, not merely combine the critical cross decay with the whole family of subcritical pivot-collision estimates.

This also explains why the designated partner's rank-one isotropic-bank theorem is genuinely stronger than an interpolation of its collision estimate: that proof averages the exact original-coordinate linear coefficient before taking the half-Riesz potential.

## 7. Corrected sufficient statement and first unpaid implication

The corrected picture is now:

- a physical scalar pivot by itself gives the ambient all-subcritical collision family (4.2), with the explicit half-order bound (4.4);
- a rank-one physical cross resource gives another half-order collision certificate via the partner, but the combination remains critical and cannot generically be upgraded to a one-copy half-Riesz bound;
- a rank-two physical cross resource *does* cross the threshold and already gives a finite one-copy half-Riesz potential; the newest fleet work also pays broad pivot-plus-rank-two residual branches;
- the partner's rank-one **isotropic-side** theorem crosses the endpoint by preserving the exact product coefficient average rather than by abstract interpolation.

Therefore the first unpaid B03 implication in the genuine rank-one survivor is not another Holder interpolation. It is:

> preserve enough original-coordinate structure in the rank-one/star residual to average the random linear coefficient as in account03/B03, or prove a product-preserving decomposition that exposes a second effective cross direction / independent smoothing packet before taking absolute values.

The full three-large-eigenvalue conjecture remains OPEN. No target-level counterexample has been produced here.

## 8. Status

- `QFORM-SQUARE-HALF-COLLISION-L3-v1`: **PROVED**, with constant `C_*<9.927`.
- `QFORM-AMBIENT-PIVOT-FRACTIONAL-COLLISION-v1`: **PROVED**, all `0<alpha<1`; arbitrary ambient residual/couplings retained.
- hybrid partner inequality (5.2): **PROVED FROM COMPLETED PARTNER RESULT**.
- abstract rank-one endpoint interpolation mechanism: **REFUTED by an actual cap-one square characteristic function**.
- full QFORM universal density theorem: **OPEN**.
- continuity for the full target: **OPEN**.

No numerical experiment is used as a proof. A small arithmetic checker is saved with this run only to verify displayed constants.