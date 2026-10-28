SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T01:20:32Z.
attacking: the det R=0 aligned-carrier survivor — convert a rank-one normalized carrier plus a diffuse two-arm physical frame into a one-hub/one-child mixed-Fresnel estimate without Schur inversion, and route the weak-currency remainder through a physical deletion child.

# r47 addendum — rank-one carrier physical-hub Fresnel compiler

Programme: `QFORM-DENSITY-3EIG-20260922`. Status: **NEW SUPPORTING THEOREM / FULL TARGET OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

This addendum is intentionally additive to the already-published r47 cancelled-twist shear report. It treats a different rank-one-carrier subregime: no large diagonal twist is needed. Everything stays in ORIGINAL independent coordinates and assumes only `0<=f_i<=1`.


## 1. Source-valid inputs

Use the exact aligned normal form from r46/r47
\[
A=\begin{pmatrix}B&M\\M^T&M^TRM+D\end{pmatrix},
\qquad G=MM^T>0,
\]
with `M` a physical `2 x m` full-row-rank arm and `D` arbitrary diagonal. Define physical arm leverage
\[
\ell_j=m_j^TG^{-1}m_j,
\qquad \mu=\max_j\ell_j.
\]

The analytic receiver is account03/B08 r37, theorem `QFORM-MULTIHUB-TRANSVERSE-FRESNEL-v1`, at
`yspennstate/math-open-problems@58b2a0752f409dd48ae5e39851ac84f13be4470b`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T122051Z-account03-B08-qform-diffuse-r37/REPORT.md`.
Its one-hub/one-child specialization says: if the light block is `D+lambda ss^T`, `||s||=1`, the retained physical hub-light vector is `g`, `h=(I-ss^T)g`, `tau=||h||>0`, and
\[
\max_j\left(s_j^2+h_j^2/\tau^2\right)\le1/2,
\]
then the full conditional form has a continuous `C_0` density with
\[
\|p\|_\infty\le 3\,4^{2/3}|\lambda|^{-1/3}\tau^{-2/3}.
\tag{1.1}
\]
Arbitrary hub square, diagonal light curvature, affine terms, constants, and conditioned outside coordinates are retained.

## 2. Exact rank-one normalized-carrier geometry

Assume
\[
R=\rho uu^T,\qquad \|u\|_2=1,\qquad \rho\ne0.
\tag{2.1}
\]
Put
\[
U_0=M^TG^{-1/2},\qquad U_0^TU_0=I_2.
\tag{2.2}
\]
Let
\[
a=u^TGu>0,
\qquad v=G^{1/2}u/\sqrt a,
\qquad \kappa=\rho a,
\tag{2.3}
\]
so `||v||=1` and
\[
G^{1/2}RG^{1/2}=\kappa vv^T.
\tag{2.4}
\]
Choose unit `w` perpendicular to `v` and define physical light vectors
\[
z=U_0v,\qquad y=U_0w.
\tag{2.5}
\]
Then `z,y` are orthonormal and, row by row,
\[
\boxed{z_j^2+y_j^2=\ell_j.}
\tag{2.6}
\]
Moreover
\[
\boxed{M^TRM=\kappa zz^T.}
\tag{2.7}
\]

For each ACTUAL physical hub `h=1,2`, its light arm is
\[
g_h=M^Te_h=U_0G^{1/2}e_h=\alpha_hz+\beta_hy,
\qquad \beta_h=w^TG^{1/2}e_h.
\tag{2.8}
\]
Therefore the transverse component relative to the child direction `z` is exactly `beta_h y`, and
\[
\beta_1^2+\beta_2^2=w^TGw.
\tag{2.9}
\]
Choose a physical hub `h_*` with
\[
\tau_{h_*}^2:=\beta_{h_*}^2\ge\frac12 w^TGw.
\tag{2.10}
\]
No linear combination of random hub coordinates is introduced.

The key invariant identity is
\[
\boxed{|\kappa|\,w^TGw=|\rho|\det G.}
\tag{2.11}
\]
Indeed, `v^TG^{-1}v=1/a`, while for a positive definite `2 x 2` matrix and orthonormal `(v,w)`,
`w^TGw=det(G)v^TG^{-1}v`; combine this with `|kappa|=|rho|a`.

## 3. Main theorem

### `QFORM-RANK1-CARRIER-PHYSICAL-HUB-FRESNEL-v1`

Assume the aligned normal form above, `rank M=2`, `rank R=1`, and
\[
\mu=\max_j\ell_j\le\frac12.
\tag{3.1}
\]
Let `rho` be the nonzero eigenvalue of `R`. Then every admissible cap-one product input has a continuous `C_0` output density and
\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
3\,2^{5/3}\bigl(|\rho|\det(MM^T)\bigr)^{-1/3}.
}
\tag{3.2}
\]
Numerically `3*2^(5/3)=9.524406311809198...`.

**Proof.** Choose the physical hub `h_*` from (2.10) and condition only on the other ORIGINAL hub coordinate. Independence and all one-dimensional density caps of the retained variables are unchanged. The light block is exactly
\[
D+\kappa zz^T,
\]
and the retained hub-light vector is `g_{h_*}`. Its normalized transverse row contribution is `y_j`, hence the r37 augmented leverage is
\[
z_j^2+\frac{(\beta_{h_*}y_j)^2}{\tau_{h_*}^2}
=z_j^2+y_j^2
=\ell_j\le1/2.
\tag{3.3}
\]
Thus r37 gives
\[
\|p_{Q\mid X_{3-h_*}}\|_\infty
\le3\,4^{2/3}|\kappa|^{-1/3}\tau_{h_*}^{-2/3}.
\tag{3.4}
\]
By (2.10)-(2.11),
\[
|\kappa|\tau_{h_*}^2
\ge\frac12|\rho|\det G.
\tag{3.5}
\]
Substitution gives exactly (3.2). The bound is uniform in the conditioned hub value, so mixing gives the same bound for the full form. The conditional characteristic-function envelope is integrable uniformly, and the r37 output is `C_0`; dominated convergence gives a continuous `C_0` mixture. QED.

## 4. Scale form and singular-carrier split

Let
\[
\Gamma_2=\sqrt{\det(MM^T)}=s_1(M)s_2(M).
\]
If at target scale `L>0`
\[
|\rho|\ge\eta/L,
\qquad \Gamma_2\ge\gamma L^2,
\tag{4.1}
\]
then
\[
\boxed{
\|p_Q\|_\infty
\le9.524407\,\eta^{-1/3}\gamma^{-2/3}L^{-1},
\qquad p_Q\in C_0.
}
\tag{4.2}
\]
Equivalently, define
\[
\Xi_1:=|\rho|\det(MM^T).
\tag{4.3}
\]
Any gate `Xi_1 >= xi L^3` yields
\[
\boxed{\|p_Q\|_\infty\le9.524407\,\xi^{-1/3}L^{-1}.}
\tag{4.4}
\]

The exact `R=0` endpoint is already covered by r37's two-hub/no-child theorem under the same `mu<=1/2`:
\[
\boxed{
\|p_Q\|_\infty\le4\det(MM^T)^{-1/4}=4\Gamma_2^{-1/2},
\qquad p_Q\in C_0.
}
\tag{4.5}
\]
Thus diffuse `det R=0` is no longer one undifferentiated endpoint: `R=0` is paid by arm area, rank-one `R` is paid by the product currency `Xi_1`, and only weak rank-one currency remains.

## 5. Designated account04/B08 theorem applied on the same physical hub

Move the selected physical hub `h_*` first:
\[
A=\begin{pmatrix}a_*&b_*^T\\b_*&C_*\end{pmatrix}.
\tag{5.1}
\]
Apply account04/B08 r2, theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`, at
`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`.
If
\[
s_3(C_*)\ge L/64
\tag{5.2}
\]
and the physical diagonal of the child spectral projection onto
`|lambda(C_*)|>=L/4096` is everywhere at most `1/32`, then taking `m_0=L/64` in the partner theorem gives the actual inequality
\[
\boxed{\|p_Q\|_\infty<4096/L,\qquad p_Q\in C_0.}
\tag{5.3}
\]
This is on the SAME selected physical hub and retains the parent scalar, full cross vector, all signs, arbitrary diagonal twists, and all additional child coefficients.

Consequently, for any fixed `xi>0`, an unpaid rank-one-carrier survivor at target scale must satisfy BOTH
\[
\Xi_1<\xi L^3
\tag{5.4}
\]
and partner failure: either
\[
s_3(C_*)<L/64,
\tag{5.5}
\]
or some actual original child coordinate has high-window leverage
\[
(P_{C_*}(|\lambda|\ge L/4096))_{jj}>1/32.
\tag{5.6}
\]
So failure of the new diffuse receiver is routed to a concrete weak-carrier plus child spectral-loss/localization certificate.

## 6. Checks and remaining debt

A seeded regression check over 3000 random full-row-rank `2 x m` arms and random signed rank-one carriers verified (2.6), (2.7), (2.10), and (2.11): maximum factorization error `3.01e-13`, maximum row-leverage identity error `4.45e-16`, zero hub-energy violations, and minimum observed ratio `max_h beta_h^2 / ((w^TGw)/2) = 1.0001674391`. The computations are regression evidence only; the proof above is analytic.

The unrestricted conjecture remains OPEN; global continuity remains OPEN, although the new rank-one-carrier branch and partner branch are continuous `C_0`.

The next B08 implication is
`QFORM-WEAK-RANK1-CARRIER-PLUS-CHILDLOSS-LOCALIZED-COMPILER-v1`: consume (5.4) together with (5.5) or (5.6) while retaining arbitrary diagonal twists and the weak aligned rank-one carrier. A second unresolved algebraic state is a rank-two carrier with extremely small nonzero determinant where r46's reciprocal-determinant currency degenerates; the present theorem suggests splitting strong and weak carrier eigendirections before any Schur division.

No counterexample is claimed.
