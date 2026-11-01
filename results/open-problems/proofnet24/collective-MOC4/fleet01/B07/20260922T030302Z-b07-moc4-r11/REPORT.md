# MOC4 fleet01/B07 — Cartan radial-frame Hessian packing

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker/run:** fleet01/B07, `20260922T030302Z-b07-moc4-r11`  
**Assignment:** exact `4 x 4` exterior-power/minor expansion and the mixed-minor inequality needed for the common hull bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and inherited exact reduction

For complex normal `4 x 4` matrices, after diagonalizing one matrix and writing the relative eigenbasis as `U in U(4)`, the target is

\[
 h_\eta(U):=\Re\!\left(\eta\det(D_a+UD_bU^*)\right)
 \le M_\eta:=\max_{\sigma\in S_4}\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right)
\tag{1}
\]

for every support direction `eta`.

The earlier fleet01/B07 exterior-power reduction is retained. With the three complementary-pair classes, the actual middle-compound data are encoded by

\[
 D=(d_{\alpha\beta}),\qquad R=(r_{\alpha\beta}),
\]

where `R` is doubly stochastic and

\[
 d_{\alpha\beta}=\frac14 h_\alpha^T |U|^2 h_\beta.
\tag{2}
\]

For structured spectral support arrays `(K,X)`, the nonconstant part of (1) is exactly

\[
 s(U)=k+x,\qquad
 k=\langle D,K\rangle,
 \qquad x=\frac12\langle R,X\rangle.
\tag{3}
\]

Equivalently, in the actual exterior-square `SO(6)` realization, split the matrix into nine real `2 x 2` blocks and write each block as `z -> m z+n\bar z`. Then

\[
 s(U)=\sum_{\alpha,\beta}
 \left[
 \left(\frac{X_{\alpha\beta}}2+K_{\alpha\beta}\right)|m_{\alpha\beta}|^2+
 \left(\frac{X_{\alpha\beta}}2-K_{\alpha\beta}\right)|n_{\alpha\beta}|^2
 \right].
\tag{4}
\]

The parent support problem is therefore a structured mixed-minor inequality on one common unitary, not an arbitrary bistochastic relaxation.

## 2. Exact peer mathematics consumed

This run directly applies the assigned OTHER-account partner **fleet02/B08**, newest compatible result `MOC4-BOUNDARY-SUPPORT-FACE-REDUCTION-v3` (run `B08-20260922T023618Z-7e3c2a`). It proves exact source-valid determinant laws on repeated-eigenvalue faces and all proper common reducing-block faces, including the `3+1` boundary; the unresolved all-pairs core can be taken simple-spectrum, individually invertible and irreducible, with only explicit collinear supported-face degeneracies left on those solved boundaries.

I also use two newer exact OTHER-account inputs.

1. **fleet02/B09, `MOC4-CARTAN-POLARIZATION-v1`.** For every chosen entry `(i,j)`, there is a genuine rank-one CS path `U(t)`, `0<=t<=1`, through `U(c)` with `c=|u_ij|`, such that `U(0)` has the chosen entry zero, `U(1)` has a `3+1` common reducing block, and at an interior global support maximizer
   \[
   h(t)=h(c)-\Gamma_{ij}(t-c)^2,
   \qquad \Gamma_{ij}\ge0.
   \tag{5}
   \]
   In particular the endpoint drops are exact:
   \[
   h(c)-h(0)=\Gamma_{ij}c^2,
   \qquad
   h(c)-h(1)=\Gamma_{ij}(1-c)^2.
   \tag{6}
   \]
2. **fleet02/B07, `MOC4-PAIR-HESSIAN-TRACE-v1`.** At a pair-stationary point, if
   \[
   \bar c:=\frac16\langle {\bf1}_{3\times3},X\rangle,
   \tag{7}
   \]
   then the exact trace over the twelve real off-diagonal column-pair tangent directions is
   \[
   \boxed{\operatorname{Tr}H_{\rm pair}
   =-8\{2k+3(x-\bar c)\}.}
   \tag{8}
   \]
   At a local maximum this only gave the qualitative necessary condition `2k+3(x-\bar c)>=0`.

The new step below upgrades (8) to a **quantitative gap-dependent inequality** on the branch where the sixteen zero-entry endpoints are target-safe.

## 3. New theorem — `MOC4-CARTAN-HESSIAN-PACKING-v1`

### Theorem

Fix spectra `a,b`, a support direction `eta`, and let `U` be a global maximizer of `h_eta` with a positive target support gap

\[
 h_\eta(U)=M_\eta+\gamma,
 \qquad \gamma>0.
\tag{9}
\]

Assume that for every entry `(i,j)`, the zero-entry endpoint in the exact one-entry Cartan path of (5) is target-safe:

\[
 h_\eta(U_{ij}(0))\le M_\eta.
\tag{10}
\]

Then every selected entry satisfies the radial curvature bound

\[
 \boxed{
 -\frac{d^2}{d\theta^2}
 h_\eta\!\left(U\exp(\theta K_{ij})\right)\Big|_{\theta=0}
 \ge 6\gamma,
 }
\tag{11}
\]

for the unit-norm rank-one Cartan generator `K_ij` defined below. Moreover the sixteen generators form a weighted real frame strong enough to force

\[
 \boxed{-\operatorname{Tr}H_{\rm pair}\ge36\gamma.}
\tag{12}
\]

Combining with (8), any such violating maximizer must obey the strictly stronger necessary condition

\[
 \boxed{
 2k+3(x-\bar c)\ge\frac92\,\gamma.
 }
\tag{13}
\]

Thus a hypothetical MOC4 support violation has the following exact dichotomy:

- **zero-face escape:** at least one genuine one-entry zero endpoint is itself a target support violation; or
- **strict interior Hessian payment:** all zero endpoints are safe and the mixed-minor support data satisfy (13), not merely the previously known nonnegativity condition.

### Proof, step 1: every safe Cartan segment pays at least `6 gamma` curvature

For one entry put `c=|u_ij|`. The common-block endpoint `t=1` is target-safe: this follows directly from the known `n=3` determinant-hull theorem and is also contained in the partner's common-block boundary result. Under (10), both endpoints of (5) therefore satisfy `h(0),h(1)<=M_eta`.

Using (6) and (9),

\[
 \Gamma_{ij}c^2\ge\gamma,
 \qquad
 \Gamma_{ij}(1-c)^2\ge\gamma.
\tag{14}
\]

A positive-gap point cannot have `c=0` or `c=1` on this branch, so `0<c<1`.

Parameterize the same rank-one Cartan circle by an angle `theta` through the maximizer. If `c=cos theta_0`, then along the radial direction `t(theta)=cos(theta_0-theta)` and `t'(0)=sqrt(1-c^2)`. Since `h_t'(c)=0`, (5) gives

\[
 -h''(0)=2\Gamma_{ij}(1-c^2).
\tag{15}
\]

From (14),

\[
 \Gamma_{ij}(1-c^2)
 \ge \gamma\max\left\{
 \frac{1-c^2}{c^2},
 \frac{1-c^2}{(1-c)^2}
 \right\}.
\tag{16}
\]

The two displayed functions cross at `c=1/2`; their maximum has global minimum `3`. Hence

\[
 \Gamma_{ij}(1-c^2)\ge3\gamma,
\tag{17}
\]

which proves (11).

### Proof, step 2: the sixteen radial directions form a weighted frame

Use the real Hilbert-space inner product on skew-Hermitian tangent matrices

\[
 \langle A,B\rangle_0:=\frac12\Re\operatorname{tr}(A^*B).
\tag{18}
\]

Fix a column `j`. For each row `i`, multiply `U^*e_i` by a harmless scalar phase so that its `j`th coordinate is the nonnegative number `c_ij=|u_ij|`. The resulting vectors `q_i` remain an orthonormal basis and have the form

\[
 q_i=c_{ij}e_j+s_{ij}y_{ij},
 \qquad
 s_{ij}=\sqrt{1-c_{ij}^2},
 \qquad y_{ij}\perp e_j,\quad \|y_{ij}\|=1.
\tag{19}
\]

Projecting the completeness identity `sum_i q_i q_i^*=I` to `e_j^perp` gives the exact complex tight-frame identity

\[
 \boxed{
 \sum_i s_{ij}^2 y_{ij}y_{ij}^*=I_{e_j^\perp}.
 }
\tag{20}
\]

Define

\[
 K_{ij}:=y_{ij}e_j^*-e_jy_{ij}^*.
\tag{21}
\]

Then `K_ij` is skew-Hermitian and has unit norm for (18). It is exactly the right-trivialized radial Cartan tangent used in step 1. Let `V_j` be the six-real-dimensional subspace consisting of all such matrices `K(z)=ze_j^*-e_jz^*` with `z perp e_j`.

For `X=K(z) in V_j`,

\[
 \langle X,K_{ij}\rangle_0=\Re\langle z,y_{ij}\rangle.
\tag{22}
\]

Therefore (20) implies

\[
 \sum_i s_{ij}^2\langle X,K_{ij}\rangle_0^2
 \le
 \sum_i s_{ij}^2|\langle z,y_{ij}\rangle|^2
 =\|z\|^2
 =\|X\|_0^2.
\tag{23}
\]

In operator language, if

\[
 S_j:=\sum_i s_{ij}^2 K_{ij}\otimes K_{ij},
\tag{24}
\]

then

\[
 0\le S_j\le P_{V_j}.
\tag{25}
\]

The off-diagonal tangent space is the orthogonal sum of the six two-real-dimensional coordinate-pair planes. Each such pair plane occurs in exactly two of `V_1,...,V_4`; hence

\[
 \sum_{j=1}^4P_{V_j}=2P_{\rm off}.
\tag{26}
\]

With `S=sum_j S_j`, equations (25)-(26) give

\[
 \boxed{0\le S\le2P_{\rm off}.}
\tag{27}
\]

### Proof, step 3: pack the sixteen curvature payments into the pair-Hessian trace

At a global maximizer the negative Hessian `A:=-H` is positive semidefinite. By (11),

\[
 A(K_{ij},K_{ij})\ge6\gamma
\tag{28}
\]

for every entry. Since every column of a unitary has squared norm one,

\[
 \sum_{i,j}s_{ij}^2
 =\sum_{i,j}(1-|u_{ij}|^2)
 =16-4=12.
\tag{29}
\]

Thus

\[
 \operatorname{tr}(AS)
 =\sum_{i,j}s_{ij}^2A(K_{ij},K_{ij})
 \ge72\gamma.
\tag{30}
\]

On the other hand, positivity of `A` and (27) imply

\[
 \operatorname{tr}(AS)
 \le2\operatorname{tr}(AP_{\rm off})
 =-2\operatorname{Tr}H_{\rm pair}.
\tag{31}
\]

Combining (30)-(31) proves (12). Finally insert the exact trace identity (8):

\[
 72\gamma
 \le -2\operatorname{Tr}H_{\rm pair}
 =16\{2k+3(x-\bar c)\},
\]

which is exactly (13). QED.

## 4. Why this is a genuine strengthening of the current interior route

The preceding stationarity theorem only forced

\[
2k+3(x-\bar c)\ge0.
\]

That qualitative inequality can remain true arbitrarily close to a flat interior stationary point. The new result says that a **gap-positive** global maximizer whose zero-entry endpoints are all safe must have a quantitatively nonflat off-diagonal Hessian whose trace is at least linear in the actual target gap. This uses all sixteen common-unitary entry directions simultaneously; it cannot be seen from one independent scalar Cartan inequality.

The argument also retains the source model throughout: every direction is a genuine unitary variation, the common-block endpoint is a genuine `3+1` boundary point, and the frame identity comes from the same unitary's orthonormal rows. No arbitrary bistochastic or independent compound-minor array is introduced.

## 5. Updated compact conditional end-to-end chain

Assume MOC4 fails in one support direction. Take a gap-positive global true-unitary maximizer.

1. The assigned partner fleet02/B08 removes the repeated-spectrum and proper common reducing-block faces from the residual core, modulo its explicitly recorded collinear supported-face degeneration.
2. fleet02/B07 removes every tight odd-Weyl equality face and gives the quantitative odd-overlap collar; its singular-safe pair-Hessian identity remains valid.
3. fleet02/B09 supplies the exact one-entry Cartan polarization.
4. This report proves: either the failure descends to a genuine zero-entry endpoint, or the residual strict interior maximizer satisfies the new quantitative condition (13).

Hence the first surviving all-interior implication can be sharpened to:

> **`MOC4-STRICT-INTERIOR-GAP-PAYMENT-v1`.**  
> For a structured spectral support pair `(K,X)` and a true exterior-square point arising from a global unitary maximizer with target gap `gamma>0`, strict odd-overlap constraints, no violating zero-entry endpoint, and the exact stationarity equations, rule out simultaneous satisfaction of
> \[
> k\ge0,
> \qquad
> 2k+3(x-\bar c)\ge\frac92\gamma.
> \tag{32}
> \]
> Equivalently, derive a structured upper bound on the same Hessian trace that is strictly smaller than the lower bound forced by (12).

The separate zero-entry support branch remains a real obligation; this report does not solve it and makes no full-proof claim.

## 6. Boundary, singular and provenance notes

- Repeated spectra and proper common reducing blocks are not silently discarded; the assigned partner result is used to isolate them.
- No inverse of `D_a+UD_bU^*` appears, so the Hessian packing argument itself is safe at singular determinant points.
- If an entry equals zero or one, the dichotomy is already on a boundary branch; the strict-interior proof above assumes `0<c_ij<1` only after the two endpoint inequalities force it.
- No benchmark data, held-out answers, credentials, machine-local data, email/Drive material, public posting, paid model/API/Codex, remote workflow or permission change was used.
- This is an exact analytic proof step. No numerical experiment is used as evidence for (11)-(13).
