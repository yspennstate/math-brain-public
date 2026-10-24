# MOC4 account03/B20 — exact assignment-defect LP dual removes the Birkhoff decomposition

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and fresh inputs

For complex normal `4 x 4` matrices, after diagonalizing one matrix the target is

\[
\det(D_a+UD_bU^*)\in\operatorname{conv}\{z_\sigma:\sigma\in S_4\},
\qquad
z_\sigma=\prod_{i=0}^3(a_i+b_{\sigma(i)}),
\]
for every true unitary `U`. For a real support functional `H_sigma=Re(eta z_sigma)`, put `M=max H_sigma` and suppose a genuine global support maximizer had

\[
h(U)=M+\gamma,\qquad \gamma>0.
\]

The newest complete campaign-lead result consumed is account03/B07 run `20260922T043708Z-account03-B07-MOC4-r11`, `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`. It proves exact subgroup roofs for true unitary relabeling orbits and leaves `MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`: eliminate a positive maximizer after imposing the subgroup roofs, bidirectional pair roofs, same-unitary compatibility, stationarity and Hessian constraints.

The named OTHER-account result applied directly is account02/B09 run `20260922T0444Z-account02-B09-MOC4-r15`, `MOC4-STANDARD-HAMMING-DEFECT-v1`. It uses account04/B09's exact standard-channel identity. With Klein-fiber means `B_rho`,

\[
Q=\max_\rho B_\rho,\qquad \Delta=M-Q,
\qquad \kappa_\sigma=H_\sigma-B_{\rho_\sigma},
\qquad K=\max_\sigma\kappa_\sigma,
\]
account02/B09 proves that for the actual unistochastic `P=(|u_{ij}|^2)` and **every** Birkhoff decomposition

\[
P=\sum_\sigma\lambda_\sigma P_\sigma,
\qquad
k(U)=\sum_\sigma\lambda_\sigma\kappa_\sigma.
\tag{1}
\]
A positive support gap obeys

\[
k\ge\gamma+\Delta,
\qquad
K-k\le r-\gamma,
\qquad r:=K-\Delta.
\tag{2}
\]
If the maximum `K` is unique at `sigma_*`, the same run also proves a genuine-unitary Cartan/Hessian collar

\[
1-P_{i,\sigma_*(i)}
\ge q_i(\gamma)
:=\Phi_{U(\gamma)}(\gamma+\beta_i),
\tag{3}
\]
where

\[
\beta_i=M-\max_{\sigma:\sigma(i)=\sigma_*(i)}H_\sigma,
\quad
U(\gamma)=3(M-m)+2\gamma-\Delta,
\]
\[
\Phi_T(s)=\frac{16Ts}{(4T+s)^2}.
\tag{4}
\]
Its scalar use of (3) retained only the uniform Hamming slope `c_*`. The present run removes that loss by keeping the complete 24-permutation defect table.

## 2. Exact assignment-defect LP theorem

Assume `sigma_*` is the unique maximizer of `kappa`. Define the exact permutation defect

\[
d_\sigma:=K-\kappa_\sigma\ge0,
\qquad
d_{\sigma_*}=0,
\]
and mismatch indicators

\[
a_{i\sigma}:={\bf1}\{\sigma(i)\ne\sigma_*(i)\}.
\]
For a nonnegative vector `q=(q_0,...,q_3)`, define the finite primal problem

\[
C(q):=
\min_{\lambda\ge0}
\left\{
\sum_\sigma d_\sigma\lambda_\sigma:
\sum_\sigma\lambda_\sigma=1,
\quad
\sum_\sigma a_{i\sigma}\lambda_\sigma\ge q_i\ (0\le i<4)
\right\}.
\tag{5}
\]
Its exact dual is

\[
C(q)=
\max_{\alpha\in\mathbb R,\ y_i\ge0}
\left\{
\alpha+\sum_i y_iq_i:
\alpha+\sum_i a_{i\sigma}y_i\le d_\sigma
\text{ for all }\sigma\in S_4
\right\}.
\tag{6}
\]
(The identity permutation relative to `sigma_*` forces `alpha<=0`; `alpha=0,y=0` is always feasible.)

### Theorem — `MOC4-STANDARD-DEFECT-LP-DUAL-v1`

At every genuine positive-gap global maximizer for which the account02/B09 collar (3) applies,

\[
\boxed{
 r-\gamma\ge C(q(\gamma)).
}
\tag{7}
\]
Equivalently, every single dual-feasible pair `(alpha,y)` gives the explicit necessary inequality

\[
\boxed{
 r-\gamma\ge
 \alpha+\sum_i y_i\Phi_{U(\gamma)}(\gamma+\beta_i).
}
\tag{8}
\]

### Proof

Take any Birkhoff decomposition in (1). Its mismatch marginal is exact:

\[
\sum_\sigma a_{i\sigma}\lambda_\sigma
=1-P_{i,\sigma_*(i)}.
\tag{9}
\]
By the genuine-unitary Cartan/Hessian collar (3), (9) is at least `q_i(gamma)`. Thus the **actual** decomposition is feasible for the primal (5). Moreover, by (1),

\[
K-k
=\sum_\sigma\lambda_\sigma(K-\kappa_\sigma)
=\sum_\sigma d_\sigma\lambda_\sigma
\ge C(q(\gamma)).
\tag{10}
\]
Using (2), `K-k<=r-gamma`, proving (7). Finite-dimensional LP duality gives (6) and therefore (8). No arbitrary bistochastic middle compound and no independent common permutation lift is introduced: `P` is the first compound of the same true unitary, and the only decomposition used is an ordinary Birkhoff decomposition of that actual `P`. QED.

## 3. Why this strictly contains the previous Hamming bound

Account02/B09 defined

\[
c_*=
\min_{\sigma\ne\sigma_*}
\frac{d_\sigma}{d_H(\sigma,\sigma_*)}.
\]
Then `alpha=0` and `y_i=c_*` is feasible in (6), because

\[
\sum_i a_{i\sigma}c_*=c_*d_H(\sigma,\sigma_*)\le d_\sigma.
\]
Hence

\[
C(q)\ge c_*\sum_iq_i.
\tag{11}
\]
So (7) never weakens `MOC4-STANDARD-HAMMING-DEFECT-v1`; it retains all anisotropy in the exact 24-value defect table. The remaining `P`-dependence of that route has been eliminated to a four-constraint finite LP whose data are endpoint-computable.

If `U(0)>2\max_i\beta_i`, then each ratio `(gamma+beta_i)/(4U(gamma))` increases for `gamma>=0`; while it remains in `[0,1]`, every `q_i(gamma)` increases. Since (6) is a maximum of affine functions with nonnegative `y`, `C(q(gamma))` is nondecreasing, whereas `r-gamma` strictly decreases. Therefore one exact sign change gives a rigorous one-sided cutoff; if (7) already fails at `gamma=0`, the entire support direction is closed.

## 4. Exact genuinely-complex application: `<180` improves to `<174`

Apply the theorem to account02/B09's exact datum

\[
a=(-6i,5i,3+5i,1),
\qquad
b=(7+4i,1+7i,1-5i,-3),
\qquad
\eta=-1+2i.
\tag{12}
\]
That run already verifies that the signed spectral set is not a common-circle reduction and gives

\[
M=7470,\quad m=-108,\quad d=7578,
\]
\[
Q=\frac{7643}{2},\quad
\Delta=\frac{7297}{2},\quad
K=\frac{7825}{2},\quad r=264,
\tag{13}
\]
with unique standard maximizer

\[
\sigma_*=(1,2,0,3)
\]
and

\[
(\beta_0,\beta_1,\beta_2,\beta_3)=(7054,7062,0,0).
\tag{14}
\]
The previous uniform slope is `c_*=132` and yielded `gamma<180`.

The companion exact verifier checks all 24 inequalities in (6) for the stronger dual-feasible point

\[
\boxed{
\alpha=0,
\qquad
y=\left(0,264,\frac{1125}{2},\frac{615}{2}\right).
}
\tag{15}
\]
Thus every hypothetical positive-gap maximizer must satisfy

\[
264-\gamma
\ge
264q_1(\gamma)
+\frac{1125}{2}q_2(\gamma)
+\frac{615}{2}q_3(\gamma).
\tag{16}
\]
Here

\[
U(0)=\frac{38171}{2}>2\max_i\beta_i,
\]
so the right side is nondecreasing and the left side decreases. Exact Fraction arithmetic gives

\[
F(173):=
264-173-\text{RHS}(173)
=
\frac{44721002882415194611}{43802913306687009721}>0,
\tag{17}
\]
while

\[
F(174)
=-\frac{17138174777403444}{684723721361319025}<0.
\tag{18}
\]
Therefore

\[
\boxed{0<\gamma<174}
\tag{19}
\]
for every hypothetical positive-gap global maximizer on this exact genuinely-complex datum satisfying the already-proved same-unitary standard/Cartan/Hessian hypotheses. This strictly improves account02/B09's `<180` cutoff without any numerical optimization assumption; (15), (17), and (18) are exact rational certificates.

The latest campaign-lead subgroup roof is much stronger on its own canonical hard datum (`gamma<=289/3`) but much weaker on the datum (12), where the subgroup gaps are `866` and `4765/3`. Thus the mechanisms are complementary rather than redundant.

## 5. Updated smallest missing implication

This run resolves one concrete part of account02/B09's requested next move: the Birkhoff-decomposition uncertainty in the standard transport/collar mechanism can be eliminated exactly by (5)-(8). A surviving counterexample direction with unique standard maximizer must now satisfy simultaneously:

1. the campaign lead's two transposition-subgroup cubature roofs and bidirectional pair roof;
2. the standard reserve `gamma<=K-Delta`;
3. the exact defect-LP inequality (7), not merely its uniform-Hamming relaxation;
4. the genuine common-unitary pair-Rayleigh, Cartan/Hessian and `P/R/D` compatibility constraints.

The next genuinely unpaid step is therefore narrower:

> **`MOC4-DEFECT-LP-BIORIENTATION-EXCLUSION-v1` (OPEN).**  
> Combine the exact assignment-defect dual (6) with the six bi-orientation `P/R` gates and subgroup-cubature residual. Either prove that every positive residual is infeasible for one true unitary, or construct a genuine normal-matrix witness satisfying all those constraints and violating the target support inequality.

A promising exact route is to add the bi-orientation gate inequalities as further linear constraints on Birkhoff mismatch statistics wherever they can be expressed in the same `lambda` variables; if that is impossible because the `R` channel carries genuinely additional common-minor information, the obstruction itself identifies the precise nonlinear true-unitary compatibility still missing. The finite LP theorem above should be retained as a mandatory first filter in either case.

## 6. Status and non-claims

- `MOC4-STANDARD-DEFECT-LP-DUAL-v1`: **PROVED**.
- Exact dual certificate (15): **VERIFIED over all 24 permutations**.
- Exact datum cutoff: previous `<180` improved to **`<174`**.
- Campaign-lead subgroup theorem and account02/B09 transport theorem were consumed source-bound, not restated as this run's work.
- Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
- No arbitrary bistochastic surrogate, mock common lift, benchmark work, paid model/API/Codex, email/Drive delivery, public posting, credentials, scheduler identifiers, machine paths, or unrelated private transcript was used.
