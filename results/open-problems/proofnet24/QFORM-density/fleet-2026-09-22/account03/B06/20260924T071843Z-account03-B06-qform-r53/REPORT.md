SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T07:18:43Z.
attacking: `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`; after the new account02/B06 obstruction to a normal-floor argument, change mechanism and aggregate the whole three-hub-plus-one-tail determinant bank before selecting a tail coordinate.

# account03/B06 r53 — singular three-hub four-minor bank and localized exit

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Fresh start control: `yspennstate/math-research-brain@1ad7e714584d8283e6ebb5a848092c9c31ec75df`, OWNER CONTROL revision `2026-09-22.15`.  
Immediate B06 input: `QFORM-NORMAL-INNOVATION-COMPENSATED-CROSS-VOLUME-v1`, `yspennstate/math-open-problems@8e9f088eb1496f376287e67731b7906818ccd703`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T062005Z-account03-B06-qform-r52/REPORT.md`.  
Fresh peer obstruction consumed: account02/B06 `account02-B06-20260924T065158Z-auto11-r14/EARLY_CALC.md` on current master.  
Designated partner actually applied below: account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport is not native learned-memory ingestion.

The full QFORM conjecture remains OPEN. This run proves a new exact bank identity and a target-level heavy-bank receiver on the singular localized face. It does not claim to close the remaining diffuse bilinear face.

## 1. Why the mechanism changes here

The r52 theorem gives, in its selected three-hub normal form,

\[
a^2\det(NN^T)=W(D+d\theta)^2+d^2H,
\qquad
\chi=\frac{H}{W\theta^2}.
\]

The unpaid positive-normal collar is `0<chi<1/64`. A fresh account02/B06 calculation supplies a strict target family with `chi=8 epsilon^2 ->0`, exact tangential cancellation `D+d theta=0`, and uniformly positive layer-0/1/2 Pluecker mass. Its literal three-hub block is nevertheless uniformly invertible, with spectrum `{2,2,-1}`. Thus the collar plus retained layer mass does **not** force a positive normal floor. The right compiler must allow a localized three-hub exit and, on the truly singular three-hub face, spend a different bank currency.

The first exit is immediate from the completed physical-triple theorem. If the actual literal three-hub block `F` satisfies

\[
|\det F|\ge \eta>0,
\]

then conditioning on every other ORIGINAL coordinate and applying `QFORM-PHYSICAL-TRIPLE-DETERMINANT-RECEIVER-v1` gives

\[
\boxed{\|p_Q\|_\infty<102\,\eta^{-1/3}.} \tag{1.1}
\]

For the fresh account02/B06 family, `|det F|=4`, hence this existing receiver already gives

\[
\|p_Q\|_\infty<102\,4^{-1/3}=64.25597355\ldots . \tag{1.2}
\]

So that family is an obstruction to the proposed normal-floor implication, not an obstruction to QFORM.

## 2. Exact setup for the singular localized face

The following identity is purely algebraic and keeps all tail coordinates together.

Let `B=B^T` be an invertible `3 x 3` real matrix and let

\[
Z=(z_1\ \cdots\ z_m)\in\mathbb R^{3\times m}.
\]

Consider the exact rank-three core plus arbitrary coordinate-separable diagonal perturbation

\[
A=[I_3\ Z]^T B[I_3\ Z]
 +\operatorname{diag}(d_1,d_2,d_3,\delta_1,\ldots,\delta_m). \tag{2.1}
\]

Here `[I_3\ Z]` denotes the `3 x (3+m)` matrix obtained by adjoining the columns of `Z` to `I_3`. Put

\[
D_H=\operatorname{diag}(d_1,d_2,d_3),
\qquad F=B+D_H. \tag{2.2}
\]

Thus `F` is the ACTUAL literal physical three-hub principal block. For a tail coordinate `j`, the ACTUAL physical four-coordinate principal block is

\[
M_j=
\begin{pmatrix}
F&Bz_j\\
z_j^TB&z_j^TBz_j+\delta_j
\end{pmatrix}. \tag{2.3}
\]

No restriction is placed on any `delta_j`.

## 3. `QFORM-THREEHUB-FOURMINOR-DIAGONAL-COMPENSATION-v1`

### Theorem 3.1

For every tail coordinate `j`,

\[
\boxed{
\det M_j
=\delta_j\det F
+z_j^T\Bigl[(\det F)D_H-D_H\operatorname{adj}(F)D_H\Bigr]z_j.
} \tag{3.1}
\]

### Proof

Use the determinant-one congruence corresponding to the literal change `x=u-z_j t`:

\[
S_j=
\begin{pmatrix}
I_3&-z_j\\0&1
\end{pmatrix}.
\]

A direct multiplication gives

\[
S_j^TM_jS_j=
\begin{pmatrix}
F&-D_Hz_j\\
-z_j^TD_H&z_j^TD_Hz_j+\delta_j
\end{pmatrix}. \tag{3.2}
\]

For every square `F`, singular or not,

\[
\det\begin{pmatrix}F&r\\r^T&s\end{pmatrix}
=s\det F-r^T\operatorname{adj}(F)r. \tag{3.3}
\]

Insert `r=-D_H z_j` and `s=z_j^TD_Hz_j+delta_j` into (3.3). This is exactly (3.1). QED.

This formula is the desired compensation: the coordinate-separable tail coefficient appears only multiplied by the **whole** hub determinant. Consequently it disappears identically on the singular three-hub face.

## 4. `QFORM-HUBSINGULAR-FOURMINOR-BANK-v1`

Assume now

\[
\det F=0,\qquad \operatorname{rank}F=2. \tag{4.1}
\]

Let `v` be a unit null vector of `F`, and let the two nonzero eigenvalues of `F` be `mu_1,mu_2`. Put

\[
\kappa_F:=|\mu_1\mu_2|>0,
\qquad
\omega:=Z^TD_Hv\in\mathbb R^m. \tag{4.2}
\]

Since `F` is symmetric rank two,

\[
\operatorname{adj}(F)=(\mu_1\mu_2)vv^T. \tag{4.3}
\]

Therefore Theorem 3.1 collapses to the exact perfect-square identity

\[
\boxed{
\det M_j=-(\mu_1\mu_2)\,\omega_j^2.
} \tag{4.4}
\]

In particular all arbitrary tail diagonal coefficients `delta_j` have disappeared. Summing the complete bank **before taking any reciprocal minor** gives

\[
\boxed{
\sum_{j=1}^m|\det M_j|
=\kappa_F\|\omega\|_2^2.
} \tag{4.5}
\]

This is the new weighted replacement for the singular localized collar.

There is also an exact geometric meaning. From `Fv=0` one has

\[
Bv=-D_Hv.
\]

For the full matrix (2.1),

\[
A\binom v0
=inom 0{-Z^TD_Hv}
=inom0{-\omega}. \tag{4.6}
\]

Hence

\[
\boxed{
\omega=0
\iff
(v,0)\in\ker A.
} \tag{4.7}
\]

Thus the bank currency is exactly the coupling of the physical hub-null direction to the tail. It is not an arbitrary norm introduced for the proof.

### Selected-hub specialization

If only the selected hub has diagonal perturbation, `D_H=d e_he_h^T`, normalize the null vector so its selected component is one. Then `omega=d z_h`. In the exact double-resonance subcase of the r52 notation, `det F=0` and `D+d theta=0` imply `det C !=0`, `q adj(C)b=0`, and

\[
\operatorname{adj}(F)=\det(C)\,zz^T,
\qquad z=(1,-C^{-1}b)^T.
\]

Equation (4.4) becomes

\[
\det M_j=-\det(C)d^2(z_h)_j^2,
\]

recovering the singular-face bank without any tail-diagonal contamination.

## 5. A target-level heavy-bank payment

Assume `omega !=0`. If one literal tail coordinate carries at least `1/64` of the bank energy,

\[
\omega_j^2\ge\frac1{64}\|\omega\|_2^2, \tag{5.1}
\]

then (4.4) gives

\[
|\det M_j|
\ge \frac{\kappa_F\|\omega\|_2^2}{64}. \tag{5.2}
\]

Condition on every original coordinate outside these four literal coordinates. The conditioned polynomial has the same `4 x 4` quadratic block `M_j` and arbitrary affine terms. The completed `QFORM-PHYSICAL-FOUR-DETERMINANT-RECEIVER-v1` therefore gives

\[
\boxed{
\|p_Q\|_\infty
<93\left(\frac{64}{\kappa_F\|\omega\|_2^2}\right)^{1/4}
=263.0437227\ldots\,[\kappa_F\|\omega\|_2^2]^{-1/4}.
} \tag{5.3}
\]

This is an essential-boundedness statement for the full ambient scalar output on the stated branch. Continuity is not claimed from the four-coordinate determinant proof.

## 6. The complementary bank is a genuine diffuse fresh smoother

If (5.1) fails for every `j`, set

\[
r_j=\omega_j/\|\omega\|_2.
\]

Then

\[
\sum_jr_j^2=1,
\qquad
\max_jr_j^2<\frac1{64}<\frac12. \tag{6.1}
\]

Let

\[
W_\omega=\sum_jr_jX_j
\]

on the tail original-coordinate bank. The account01/B06 translation-uniform product Fourier/Brascamp--Lieb estimate in dimension one applies to the Parseval frame `(r_j)` and gives

\[
\int_{\mathbb R}|\phi_{W_\omega}(t)|dt\le4\pi. \tag{6.2}
\]

Consequently `W_omega` has a continuous `C_0` density with

\[
\boxed{\|p_{W_\omega}\|_\infty\le2.} \tag{6.3}
\]

Moreover this scalar is independent of all three hub ORIGINAL coordinates. Therefore failure of the heavy four-minor exit does not leave a dimension-dependent cloud of tiny minors: it produces one normalized, diffuse, fresh independent linear smoother with a dimension-free density cap. The unpaid operation is now to combine this fresh scalar bilinear coupling with the rank-two curved hub sheet without taking `E|W_omega|^{-1}` or another fiber maximum; the two-opposite-sign logarithmic control shows why that last operation must still be joint.

## 7. Actual designated-partner application

The freshest completed designated partner result is account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1` at

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.

Take the exact tangential subface of the live B06 packet, where after whitening the two strong tail rows the shared statistic produced by the singular-hub coupling lies in their span:

\[
B_{\rm sh}=\alpha L+\gamma V,
\qquad
\max_k(w_k^2+v_k^2)\le\frac12. \tag{7.1}
\]

For the actual curved output

\[
Y=\lambda_*(V-v_0)^2+\beta B_{\rm sh}+c,
\]

the partner theorem completes the square in `V`, performs its determinant-one output shear, and on the live off-fold scale `r=1/64` gives the concrete inequality

\[
\boxed{
\|g_{\rm off}\|_\infty
\le\frac{256}{|\lambda_*|}.
} \tag{7.2}
\]

This is a continuous `C_0` two-output density estimate in precisely the partner theorem's scope. I do not promote (7.2) through a genuinely normal shared component. The new Section 4 bank identity is what replaces that forbidden promotion on the singular three-hub face.

## 8. Relation to the 64/65 collar and exact remaining debt

The new peer family proves that `chi<1/64` does not itself imply a quantitative normal floor. The compiler now has three explicit exits:

1. **localized invertible hub:** `|det F|>=eta` is paid by (1.1);
2. **exact singular rank-two hub, heavy tail coupling:** paid by (5.3);
3. **exact singular rank-two hub, diffuse tail coupling:** the whole four-minor bank is converted before inversion into the fresh scalar smoother (6.3); exact tangential curved leakage is paid by the designated partner at (7.2).

What remains is not the old `64/65` normal-floor claim. It is the genuinely joint diffuse-bilinear endpoint:

`QFORM-HUBSINGULAR-DIFFUSE-BILINEAR-CURVED-RECEIVER-v1`:

> on the rank-two singular three-hub face with `omega !=0` and `max_j omega_j^2 < ||omega||^2/64`, combine the fresh cap-two scalar `W_omega` with the curved rank-two hub sheet and the complete same-bank tail remainder before any reciprocal `|W_omega|`, fiber maximum, or pointwise Fresnel estimate is taken.

The near-singular but nonzero `det F` transition, `rank F<=1`, and the previously listed zero physical pivot / `rank Z<=1` endpoints remain explicit separate debts. No easy subclass is promoted to full progress.

## 9. Sanity checks and status

Two independent finite calculations were performed during this run on 10,000 random instances. The general compensated four-minor identity (3.1), evaluated in equivalent block form, had maximum normalized discrepancy below `2.44e-14`. On random exact rank-two singular hub instances, the perfect-square bank identity (4.4) and `adj(F)=(mu_1 mu_2)vv^T` had maximum normalized discrepancy below `5.44e-14`. These are diagnostics only; Sections 3--6 are exact proofs.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full continuity:** OPEN.  
**This run:** exact singular-face bank theorem + full-scalar heavy-bank essential bound + diffuse fresh-smoother certificate; partner tangential branch continuous `C_0`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.
