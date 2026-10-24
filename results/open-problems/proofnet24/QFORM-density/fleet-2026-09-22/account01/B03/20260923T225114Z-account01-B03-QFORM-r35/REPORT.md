SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T22:51:14Z.
attacking: a phase-space ambiguity-function Brascamp--Lieb receiver which keeps each independent-copy sum/difference pair jointly intact; derive an L1 time envelope and linear small-ball bound from its exact Moyal budget, then splice the newest account02/B03 grouped theorem on a family where the phase-space BL constant is infinite.

# account01/B03 r35 — phase-space Moyal/BL receiver for the whole dependent pair

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control revision: `2026-09-22.15`. Status: **NEW SUPPORTING THEOREM / CONTINUOUS-DENSITY BRANCH / PARTNER COMPLEMENT APPLIED / FULL QFORM OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

The purpose of this run is to avoid the obstruction found in r34. There, the exact conditional Hausdorff--Young budget for `S_i | D_i=d_i` was valid, but paying the reciprocal coefficient `|(Ad)_i|^{-1/q}` before averaging could diverge for fragmented supports. Here the pair `(D_i,S_i)` is never split. It is packaged as a two-dimensional phase-space factor, whose exact `L^2` mass has a universal bound. A rank-two Brascamp--Lieb inequality is then applied only after all difference coordinates have been assembled.

## 1. Exact phase-space factor and Moyal budget

Let `X,X'` be iid with density `0<=f<=1`, `int f=1`, and put

\[
D=X-X',\qquad S=X+X'.
\]

Define the unnormalised conditional Fourier factor

\[
F(d,u):=h(d)\psi_d(u)
=\int_{\mathbb R} f(x)f(x-d)e^{iu(2x-d)}\,dx,
\tag{1.1}
\]

where `h` is the density of `D` and `psi_d` is the characteristic function of the actual conditional law `S|D=d`. Thus all dependence between `D` and `S` is retained inside `F`.

For fixed `d`, let

\[
a_d(x)=f(x)f(x-d).
\]

With Fourier convention `hat a(xi)=int e^{i xi x}a(x)dx`, (1.1) is

\[
F(d,u)=e^{-iud}\,\widehat{a_d}(2u).
\]

Plancherel therefore gives the exact identity

\[
\int_{\mathbb R}|F(d,u)|^2\,du
=\pi\int_{\mathbb R} f(x)^2f(x-d)^2\,dx.
\tag{1.2}
\]

Integrating in `d`,

\[
\boxed{
\iint_{\mathbb R^2}|F(d,u)|^2\,dd\,du
=\pi\left(\int f^2\right)^2\le\pi.}
\tag{1.3}
\]

The final inequality uses only `0<=f<=1` and `int f=1`. No conditional `L^infinity` bound is asserted.

I will call (1.3) the **pair Moyal budget**.

## 2. Exact independent-copy identity in phase space

Let now

\[
Q(x)=x^TAx+b^Tx+c
\]

on `m` independent coordinates with cap-one densities. Let `(X',Q')` be an independent copy and put coordinatewise

\[
D_i=X_i-X_i',\qquad S_i=X_i+X_i'.
\]

Since `A` is symmetric,

\[
Q(X)-Q(X')=D^TAS+b^TD.
\tag{2.1}
\]

The coordinate pairs `(D_i,S_i)` are independent across `i`, although `D_i,S_i` are generally dependent within a pair. If `F_i` denotes (1.1) for the `i`th input law, then (2.1) gives the exact identity

\[
\boxed{
|\phi_Q(t)|^2
=\int_{\mathbb R^m}e^{itb^Td}
\prod_{i=1}^m F_i\bigl(d_i,t(Ad)_i\bigr)\,dd.}
\tag{2.2}
\]

Hence

\[
|\phi_Q(t)|^2
\le\int_{\mathbb R^m}
\prod_{i=1}^m\left|F_i\bigl(d_i,t(Ad)_i\bigr)\right|\,dd.
\tag{2.3}
\]

This is the requested independent-copy route with no sum/difference independence shortcut.

## 3. Phase-space Brascamp--Lieb constant

For `i=1,...,m`, define the rank-at-most-two linear map

\[
L_i^A:\mathbb R^m\to\mathbb R^2,
\qquad
L_i^A d=(d_i,(Ad)_i).
\tag{3.1}
\]

Let

\[
\mathcal B(A)
:=\operatorname{BL}\left((L_i^A)_{i=1}^m;(1/2,\ldots,1/2)\right)\in(0,\infty]
\tag{3.2}
\]

be the best constant in

\[
\int_{\mathbb R^m}\prod_{i=1}^m G_i(L_i^A d)^{1/2}\,dd
\le \mathcal B(A)\prod_{i=1}^m\left(\int_{\mathbb R^2}G_i\right)^{1/2}
\tag{3.3}
\]

for nonnegative integrable `G_i`. The value `+infinity` is allowed; finiteness is a genuine geometric condition and will not be silently inferred from the spectral hypothesis.

For `t!=0`, put

\[
L_i^{A,t}d=(d_i,t(Ad)_i)=S_tL_i^Ad,
\qquad S_t=\operatorname{diag}(1,t).
\]

Brascamp--Lieb covariance under invertible postcomposition gives

\[
\operatorname{BL}\left((L_i^{A,t});(1/2)_i\right)
=|t|^{-m/2}\mathcal B(A),
\tag{3.4}
\]

because `|det S_t|=|t|` for every factor and each exponent is `1/2`.

Apply (3.3)--(3.4) to

\[
G_i(d,u)=|F_i(d,u)|^2.
\]

By (1.3), `int G_i<=pi`, so (2.3) yields

\[
\boxed{
|\phi_Q(t)|^2
\le \pi^{m/2}\mathcal B(A)|t|^{-m/2}.}
\tag{3.5}
\]

Equivalently,

\[
\boxed{
|\phi_Q(t)|
\le \min\left\{1,
\pi^{m/4}\mathcal B(A)^{1/2}|t|^{-m/4}
\right\}.}
\tag{3.6}
\]

This is a law-uniform time envelope obtained only after pairing each dependent `(D_i,S_i)` as one two-dimensional object. It does not contradict the live pointwise one-dimensional van-der-Corput correction.

## 4. Linear small-ball and continuity once m>=5

Assume `m>=5` and `mathcal B(A)<infinity`. Set

\[
K=\pi^{m/4}\mathcal B(A)^{1/2},
\qquad
\alpha=m/4>1.
\]

The crossing point in (3.6) is

\[
t_0=K^{1/\alpha}=\pi\mathcal B(A)^{2/m}.
\]

Therefore

\[
\int_{\mathbb R}|\phi_Q(t)|\,dt
\le 2\int_0^\infty\min\{1,Kt^{-\alpha}\}\,dt
=2\pi\frac{m}{m-4}\mathcal B(A)^{2/m}.
\tag{4.1}
\]

Fourier inversion now gives a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty
\le \frac{m}{m-4}\mathcal B(A)^{2/m}.}
\tag{4.2}
\]

Consequently every interval `I` obeys the genuine linear small-ball bound

\[
\boxed{
\Pr(Q\in I)
\le \frac{m}{m-4}\mathcal B(A)^{2/m}|I|.}
\tag{4.3}
\]

Thus the pair Moyal budget does recover the desired linear scaling whenever the associated phase-space BL datum is quantitatively nondegenerate.

The assignment's weighted whole-copy time integral is also explicit. Squaring (3.6) and integrating at the same threshold gives

\[
\boxed{
\int_{\mathbb R}|t|^{-1/2}|\phi_Q(t)|^2\,dt
\le
\frac{4m}{m-1}\sqrt\pi\,\mathcal B(A)^{1/m}.}
\tag{4.4}
\]

No conditional density cap or reciprocal individual coefficient occurs in (4.1)--(4.4).

## 5. Conditional principal-block compiler

The theorem is useful inside a full ambient form. Let `S` be a set of `m>=5` original coordinates and let

\[
B=A_{S,S}.
\]

Condition on all original coordinates outside `S`. The remaining variables are still independent with their original cap-one densities, and the conditional phase is

\[
X_S^T B X_S+\ell^T X_S+c
\]

for an arbitrary conditioning-dependent affine vector `ell`. Formula (2.2) already allows arbitrary affine terms and all estimates above are uniform in them. Therefore

\[
\boxed{
\|p_Q\|_\infty
\le \frac{m}{m-4}\mathcal B(B)^{2/m}}
\tag{5.1}
\]

whenever `mathcal B(B)<infinity`. Moreover the same integrable characteristic-function envelope is uniform in the conditioning, so the unconditional law has a continuous `C_0` density.

This is a product-preserving principal-block criterion, not a rotated-eigenbasis argument.

## 6. Exact geometric branch: zero-diagonal symmetric orthogonal blocks

The BL constant can be computed exactly in a nontrivial target branch. Suppose

\[
A=cU,
\qquad U^T=U,\quad U^2=I_m,\quad U_{ii}=0\ \text{for all }i.
\tag{6.1}
\]

First take `c=1`. Let `u_i^T` be row `i` of `U`. Then

\[
L_i^U d=(e_i^Td,u_i^Td).
\]

Because `U` is orthogonal and has zero diagonal,

\[
L_i^U(L_i^U)^T=I_2
\]

for every `i`: the two rows `e_i^T,u_i^T` have unit norm and inner product `U_ii=0`. Also

\[
\frac12\sum_i (L_i^U)^T L_i^U
=\frac12(I+U^TU)=I_m.
\]

Thus this is geometric Brascamp--Lieb data and

\[
\mathcal B(U)=1.
\tag{6.2}
\]

Scaling the second output coordinate by `c` gives

\[
\boxed{\mathcal B(cU)=|c|^{-m/2}.}
\tag{6.3}
\]

Hence for `m>=5`,

\[
\boxed{
\|p_Q\|_\infty
\le \frac{m}{m-4}|c|^{-1},
\qquad
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le\frac{4m}{m-1}\sqrt\pi\,|c|^{-1/2}.}
\tag{6.4}
\]

The density is continuous `C_0`.

A concrete six-variable target-valid example is

\[
U=\begin{pmatrix}0&I_3\\I_3&0\end{pmatrix},
\qquad
Q=2c(X_1X_4+X_2X_5+X_3X_6).
\]

Its spectrum is `{+c,+c,+c,-c,-c,-c}`. For `|c|>=1`, it satisfies the owner target and (6.4) gives

\[
\boxed{\|p_Q\|_\infty\le3/|c|\le3,}
\tag{6.5}
\]

with a continuous `C_0` density, and

\[
\boxed{
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le \frac{24}{5}\sqrt\pi\,|c|^{-1/2}
=8.5077784843\ldots |c|^{-1/2}.}
\tag{6.6}
\]

This is not a diagonal special case: all six physical diagonal entries vanish.

## 7. Designated partner account02/B03 applied to the complementary degeneration

The newest completed designated-partner run is account02/B03 `20260923T223109Z-account02-B03-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@4c12c8389b0cd750c8050dff29c6f6438d886dfd:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T223109Z-account02-B03-QFORM-auto11/REPORT.md`.

For

\[
A_m(a,b)=
\begin{pmatrix}
0&(a/\sqrt m){\bf1}^T&0\\
(a/\sqrt m){\bf1}&0_m&0\\
0&0&(b/m)J_m
\end{pmatrix},
\tag{7.1}
\]

its nonzero spectrum is `{+|a|,-|a|,b}`. The partner proves, by the grouped hub/Fresnel theorem,

\[
\boxed{
\|p_Q\|_\infty
\le3\,4^{2/3}|a|^{-2/3}|b|^{-1/3}
\le7.5595262994}
\tag{7.2}
\]

when `|a|,|b|>=1`, and

\[
\boxed{
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le\frac{24}{5}4^{1/3}\sqrt\pi\,
|a|^{-1/3}|b|^{-1/6}
\le13.5052565160.}
\tag{7.3}
\]

This is an actual complementary application, not a duplicate of the new theorem: the phase-space BL constant (3.2) is **infinite** for (7.1) when `m>=2`.

Indeed let `W` be the `m`-dimensional difference subspace supported only on the star-leaf bank. For each of the `m` leaf maps `L_i`, the image `L_i(W)` is one-dimensional; for the hub map it is one-dimensional; every map from the rank-one `V` bank vanishes on `W`. Hence

\[
\frac12\sum_i\dim L_i(W)=\frac{m+1}{2}<m=\dim W
\qquad(m>1).
\tag{7.4}
\]

The Brascamp--Lieb dimension condition fails, so `mathcal B(A_m)=infinity`. Nevertheless the partner's grouped nonlocal receiver gives the uniform target-scale bounds (7.2)--(7.3). This proves that a complete structural argument must combine phase-space BL branches with grouped hub/low-rank-carrier branches; neither can replace the other.

## 8. What is proved and what remains open

Proved here:

1. the exact pair Moyal budget (1.3), which keeps the true dependence of every `(X_i-X_i',X_i+X_i')` pair;
2. the phase-space Brascamp--Lieb characteristic-function estimate (3.5)--(3.6);
3. for every original-coordinate block of size `m>=5` with finite quantitative `mathcal B`, the continuous density and linear small-ball bounds (4.2)--(5.1);
4. exact constant `mathcal B(cU)=|c|^{-m/2}` for zero-diagonal symmetric orthogonal blocks, including the six-variable target bound `||p||_infinity<=3`;
5. an explicit partner splice showing that the grouped account02/B03 mechanism controls a target family for which `mathcal B=+infinity`.

Not proved:

- that the bare assumption `s_3(A)>=1` forces a principal block with `m>=5` and uniformly controlled `mathcal B`;
- that every phase-space-BL-degenerate matrix falls into a currently paid grouped-hub/ridge/pivot/cross-volume branch;
- the unrestricted QFORM density theorem;
- unrestricted continuity.

The next structural implication suggested by this run is a BL-dimension-defect routing theorem: if the data `d -> (d_i,(Ad)_i)` fail the Brascamp--Lieb dimension condition, use the offending subspace `W` to identify a low-rank grouped carrier/hub decomposition and feed it to Theorem H or the existing ridge/grouped receivers. If the data have a uniform BL constant on some original-coordinate block of size at least five, (5.1) pays the branch immediately. The partner family (7.1) is the model defect that such a routing must recognize.

## 9. Source integrity

Fresh brain control, current research, claims, live corrections, memory protocol, fleet, roles, protocol and account01/B03 assignment were read before this proof. The current owner control is revision `2026-09-22.15`; full QFORM remains OPEN in the shared claims. The exact grouped source used by the partner is `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` (Theorem H).

No Gaussianity, moments, log-concavity, compact/connected support, diagonal-basis independence, conditional cap, or uniform one-dimensional pointwise quadratic decay is used. No schedule, task, email, notification, account binding, permission, installation, remote workflow, paid model/API, or public-release change is part of this run.
