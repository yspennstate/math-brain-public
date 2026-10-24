SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-24T03:38:44.693971Z.
attacking: an exact six-variable symmetric Householder rotation of the two-per-bank cube source: derive an exact cone-tip integral and a certified finite-dimensional lower witness, then apply the completed account02/B17 theorem to a concrete dense three-variable target inequality.

# QFORM-SYMMETRIC-HOUSEHOLDER-SIX-CONE-TIP-v1

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.  
Worker: `account01/B17`.  
Run: `20260924T033844Z-account01-B17-QFORM-auto11`.  
Status: **PROVED SUPPORTING SHARP-WITNESS THEOREM / FULL TARGET OPEN**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is separate. This report gives a new exact fixed-dimension rotated stress family and a rigorous finite lower certificate. It does not claim that the displayed orientation is globally optimal among six-variable forms, nor that `3 sqrt(2)` is the unrestricted sharp constant.

Fresh controls and the live correction inbox were consumed before the proof. In particular, no post-rotation independence is used, no arbitrary-joint rank-three coarea cap is used, and no pointwise law-uniform oscillatory-decay claim is used.

## 1. Exact six-variable target matrix

Let `X_1,...,X_6` be independent `Unif[-1/2,1/2]` variables and define three disjoint normalized bank sums

\[
Y_1={X_1+X_2\over\sqrt2},\qquad
Y_2={X_3+X_4\over\sqrt2},\qquad
Y_3={X_5+X_6\over\sqrt2}.
\tag{1.1}
\]

The three `Y_j` are genuinely independent because they depend on disjoint original-coordinate banks. Their common density is the triangular density

\[
g(y)=\sqrt2\,(1-\sqrt2|y|)_+,\qquad |y|\le1/\sqrt2.
\tag{1.2}
\]

Let

\[
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T
={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.3}
\]

Then `B^2=I_3` and

\[
\operatorname{spec}(B)=\{1,1,-1\}.
\tag{1.4}
\]

Let `R` be the `6 x 3` bank matrix whose first two rows are `(1/sqrt2,0,0)`, whose next two rows are `(0,1/sqrt2,0)`, and whose final two rows are `(0,0,1/sqrt2)`. Thus `R^T R=I_3` and `Y=R^T X`. Set

\[
A=RBR^T.
\tag{1.5}
\]

Explicitly,

\[
\boxed{
A=
\begin{pmatrix}
1/6&1/6&-1/3&-1/3&-1/3&-1/3\\
1/6&1/6&-1/3&-1/3&-1/3&-1/3\\
-1/3&-1/3&1/6&1/6&-1/3&-1/3\\
-1/3&-1/3&1/6&1/6&-1/3&-1/3\\
-1/3&-1/3&-1/3&-1/3&1/6&1/6\\
-1/3&-1/3&-1/3&-1/3&1/6&1/6
\end{pmatrix}.
}
\tag{1.6}
\]

Every one of the `36` physical entries is nonzero and

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}.}
\tag{1.7}
\]

Hence this is an exact target matrix with three eigenvalues at the threshold. It is entrywise dense in the original independent-coordinate basis; it is not a diagonal or sparse physical control.

There is also no hidden uniformly good three-coordinate principal block. Any principal triple containing two coordinates from the same bank has duplicate rows/columns and is singular. A triple containing exactly one coordinate from each bank equals `B/2`, so its nonzero eigenvalues have magnitude exactly `1/2`. Thus this witness forces any localized-principal-block proof to aggregate coordinates before paying the spectral threshold.

## 2. Exact cone-tip formula

Write

\[
Q=X^TAX=Y^TBY.
\tag{2.1}
\]

The latent density is

\[
\rho(y)=g(y_1)g(y_2)g(y_3)
=2\sqrt2\prod_{j=1}^3(1-\sqrt2|y_j|)_+.
\tag{2.2}
\]

The quadratic form is

\[
q(y)=y^TBy=|y|^2-2(n\cdot y)^2.
\tag{2.3}
\]

For a bounded output density `p_Q`, the essential norm always dominates the centered small-ball derivative:

\[
\|p_Q\|_\infty\ge
\limsup_{h\downarrow0}{\mathbb P(|Q|\le h)\over2h}.
\tag{2.4}
\]

For the present compact Lipschitz `rho`, spherical coarea/dominated convergence gives an actual limit. Parameterize one null-cone sheet on `S^2` by

\[
\omega(\theta)
={n+\cos\theta\,e_1+\sin\theta\,e_2\over\sqrt2},
\quad
 e_1={1\over\sqrt2}(1,-1,0),
\quad
 e_2={1\over\sqrt6}(1,1,-2).
\tag{2.5}
\]

The other sheet contributes equally because `rho(-y)=rho(y)`. On the spherical null circle,

\[
|\nabla_{S^2}q|=2,
\qquad d\ell={d\theta\over\sqrt2}.
\tag{2.6}
\]

Consequently

\[
\lim_{h\downarrow0}{\mathbb P(|Q|\le h)\over2h}
={1\over\sqrt2}
\int_0^{2\pi}\int_0^\infty \rho(r\omega(\theta))\,dr\,d\theta.
\tag{2.7}
\]

Put

\[
a_j(\theta)=|\omega_j(\theta)|,
\qquad m(\theta)=\max_j a_j(\theta).
\tag{2.8}
\]

After `t=sqrt(2) r`, define

\[
P(a)=\int_0^\infty\prod_{j=1}^3(1-ta_j)_+\,dt.
\tag{2.9}
\]

Because the product vanishes once `t>1/m`, if

\[
s_1=a_1+a_2+a_3,
\quad s_2=a_1a_2+a_1a_3+a_2a_3,
\quad s_3=a_1a_2a_3,
\tag{2.10}
\]

then

\[
\boxed{
P(a)={1\over m}-{s_1\over2m^2}+{s_2\over3m^3}-{s_3\over4m^4}.
}
\tag{2.11}
\]

Therefore the exact cone-tip small-ball derivative is

\[
\boxed{
I_*:=\lim_{h\downarrow0}{\mathbb P(|Q|\le h)\over2h}
=\sqrt2\int_0^{2\pi}P(a(\theta))\,d\theta.
}
\tag{2.12}
\]

The coordinates used in the computation are

\[
\begin{aligned}
\omega_1(\theta)&={1\over\sqrt6}+{\cos\theta\over2}+{\sin\theta\over2\sqrt3},\\
\omega_2(\theta)&={1\over\sqrt6}-{\cos\theta\over2}+{\sin\theta\over2\sqrt3},\\
\omega_3(\theta)&={1\over\sqrt6}-{\sin\theta\over\sqrt3}.
\end{aligned}
\tag{2.13}
\]

No independence is asserted after any spectral rotation; the only independence used is the original disjoint-bank independence in (1.1).

## 3. Deterministic Lipschitz certificate

The integral in (2.12) can be certified without any histogram or Monte Carlo step. For unit nonnegative vectors `a,b`, write

\[
F_a(t)=\prod_j(1-ta_j)_+.
\]

Since every unit vector has `max_j a_j>=1/sqrt(3)`, both `F_a` and `F_b` vanish for `t>=sqrt(3)`. Also `x -> x_+` is one-Lipschitz, hence

\[
|F_a(t)-F_b(t)|\le t\|a-b\|_1.
\]

Integration gives

\[
\boxed{|P(a)-P(b)|\le{3\over2}\|a-b\|_1.}
\tag{3.1}
\]

Along the circle (2.5), `||omega'(theta)||_2=1/sqrt(2)`, so almost everywhere

\[
\left\|{d\over d\theta}|\omega(\theta)|\right\|_1
\le\sqrt3\,\|\omega'(\theta)\|_2
=\sqrt{3/2}.
\tag{3.2}
\]

Thus

\[
G(\theta):=\sqrt2 P(a(\theta))
\]

is globally Lipschitz with

\[
\boxed{\operatorname{Lip}(G)\le L={3\sqrt3\over2}.}
\tag{3.3}
\]

For the composite `N`-point midpoint rule on `[0,2pi]`, this gives the deterministic error estimate

\[
\boxed{
\left|\int_0^{2\pi}G(\theta)d\theta
-{2\pi\over N}\sum_{k=0}^{N-1}
G\!\left({2\pi(k+1/2)\over N}\right)
\right|
\le {L(2\pi)^2\over4N}.
}
\tag{3.4}
\]

The authoritative checker is `CHECK_v2.py`. It keeps the trigonometric and quadrature arithmetic interval-valued, verifies the unique maximum coordinate at each midpoint by interval separation, and then enlarges the midpoint interval by the analytic Lipschitz error. With `N=50000`, it returns

\[
\text{midpoint interval}
\subset[4.0630706167200960621,\,4.0630706167353691782],
\tag{3.5}
\]

\[
\text{Lipschitz error}
\subset[0.00051283968819876475393,\,0.00051283968819876540445],
\tag{3.6}
\]

and therefore

\[
\boxed{
I_*\in
[4.0625577770318965776,\,4.0635834564235686628].
}
\tag{3.7}
\]

In particular,

\[
\boxed{
\|p_{X^TAX}\|_\infty\ge I_*>4.0625.
}
\tag{3.8}
\]

The first checker file `CHECK.py` converted interval endpoints to ordinary floats only for the final displayed subtraction. It is retained immutably as audit history but is not used as the rigorous certificate. `CHECK_v2.py` keeps the final enclosure interval-valued and is the authoritative check.

## 4. Rotation genuinely raises the finite cone-tip stress

For the aligned two-per-bank control

\[
Q_{\rm aligned}=Y_1^2+Y_2^2-Y_3^2,
\]

the exact cone-tip value is

\[
\|p_{Q_{\rm aligned}}\|_\infty=p_{Q_{\rm aligned}}(0)
=2\pi-{7\over3}
=3.949851973846252\ldots
\tag{4.1}
\]

(the global-tip equality is supplied by the completed aligned-bank theorem; the tip integral itself is elementary). The new symmetric Householder orientation therefore satisfies the strict certified finite-dimensional gain

\[
I_*-(2\pi-7/3)>0.1126480261.
\tag{4.2}
\]

Thus at fixed dimension six, a nontrivial spectral rotation of the same independent triangular-bank source raises concentration substantially. This is not a tiny perturbative effect and is not a diagonal/pi calculation.

The strongest already source-valid unrestricted obstruction remains

\[
\boxed{C_{\rm univ}\ge3\sqrt2=4.242640687119\ldots,}
\tag{4.3}
\]

coming from the diffuse three-bank limit. The present theorem is weaker numerically as a universal lower bound, but stronger as a finite exact stress test: all physical matrix entries are nonzero and of order one, yet every physical three-coordinate principal block is singular or has spectral scale only `1/2`.

No claim is made that the symmetric normal `n=(1,1,1)/sqrt(3)` globally maximizes the six-variable orientation problem.

## 5. Completed account02/B17 theorem applied to an actual target inequality

The designated partner dependency was read from

`yspennstate/math-open-problems@65de099fa0faecebc62cf5c10b6e5b1f4aea9c41`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260924T024313Z-account02-B17-QFORM-auto11/REPORT.md`.

Its completed theorem states that for arbitrary independent cap-one `X,Y,Z`,

\[
Q_{\kappa,\beta,a}
=\beta Y^2+2aXY+2aYZ+\kappa(X-Z)^2
\]

satisfies globally

\[
\boxed{\|p_Q\|_\infty\le {2\sqrt2\over\sqrt{\kappa|a|}}.}
\tag{5.1}
\]

Apply it with

\[
\kappa=1,\qquad \beta=1,\qquad a=1.
\]

Then

\[
A_{\rm partner}
=\begin{pmatrix}
1&1&-1\\
1&1&1\\
-1&1&1
\end{pmatrix},
\qquad
\operatorname{spec}(A_{\rm partner})=\{2,2,-1\}.
\tag{5.2}
\]

Every entry is nonzero and all three eigenvalue magnitudes satisfy the target threshold. The partner result gives the concrete arbitrary-law inequality

\[
\boxed{
\left\|p_{X^2+Y^2+Z^2+2XY+2YZ-2XZ}\right\|_\infty
\le2\sqrt2
=2.828427124746\ldots
<3\sqrt2.
}
\tag{5.3}
\]

This is an actual application of the completed partner theorem, not a restatement. It also emphasizes that dense physical coupling by itself is not a near-sharpness mechanism: the six-variable bank aggregation above is much more concentrated even though both examples have all physical entries nonzero.

## 6. Consequence for proposed proof architectures

The new witness imposes three simultaneous constraints on a sharp proof:

1. **Local three-coordinate curvature may be uniformly below threshold.** The target spectrum `{1,1,-1}` can arise entirely from bank aggregation while every physical principal triple is singular or has spectral magnitudes `1/2`.
2. **Entrywise physical density is not suppressive.** All `36` entries are nonzero and bounded away from zero in magnitude by `1/6`, yet the cone-tip derivative exceeds `4.0625`.
3. **Rotation at fixed finite dimension materially changes concentration.** The same two-per-bank triangular source rises from the aligned value `2pi-7/3` to above `4.0625` under the symmetric Householder spectral orientation.

Accordingly, a proof aiming near the sharp constant cannot reduce to diagonal/pi estimates, cannot require one target-scale physical principal triple, and cannot regard generic dense coupling as automatically subcritical. It must preserve grouped-coordinate aggregation and the full product provenance through the spectral mixing.

The remaining witness frontier is the gap from `4.0625` to the diffuse obstruction `3sqrt(2)`: larger finite banks, nonuniform/fragmented cap-one inputs, intermediate-leverage shared rows, off-zero/two-sheet peaks, and additional active spectrum. A finite peak above `3sqrt(2)` would refute only that proposed sharp constant; a counterexample to the owner's theorem must destroy every finite universal bound.

## 7. Sources, corrections, and computation status

Fresh owner/control source was resolved from `yspennstate/math-research-brain` main during this run, with OWNER CONTROL revision `2026-09-22.15`; no later B17 pause or stop was observed before publication. The current research state continues to mark `QFORM-FULL` open and full continuity open.

Corrections explicitly preserved include at least: law-uniform pointwise oscillatory decay is false; arbitrary-joint rank-three coarea bounds of the previously proposed type are false; conditional projection positive-moment gates are false; fiber-sup dimension-free reduction is false; and spectral rotation does not preserve independence. None is a premise here.

Authoritative computation files in this immutable run directory:

- `CHECK_v2.py`: exact symbolic spectrum/matrix check plus interval quadrature and analytic midpoint-error certificate;
- `CHECK_OUTPUT_v2.txt`: executed output, ending `QFORM_B17_SYMMETRIC_HOUSEHOLDER_CHECK_V2_PASS`;
- `CHECK.py` and `CHECK_OUTPUT.txt`: retained first-pass audit history, not the final rigorous endpoint certificate.

No public release, permission expansion, paid/remote execution, scheduler mutation, task creation, cross-account authentication, email, or push notification was performed.
