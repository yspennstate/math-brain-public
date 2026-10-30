SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T01:15:47Z.
attacking: collective higher-rank Schur remainder regularity and rough-input bridge; preserve third smoothing resource before conditioning.

# fleet02/B15 — sharp 2D-projection upgrade of the semidefinite Schur receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T011547Z-fleet02-B15-qform-auto11`  
Status: `QUANTITATIVE SUPPORTING IMPROVEMENT / RULED ROUGH-BRIDGE RECHECKED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact status and first unpaid implication

The owner target remains OPEN:

\[
C_*:=\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
\]

The newest designated partner fleet03/B15 (`20260924T002614Z-fleet03-B15-qform-auto29`, read from the fresh repository snapshot) sharpens the qualitative regularity picture: rank three is the exact threshold at which **every fixed cap-one product instance** is guaranteed a bounded `C_0` density. Thus the target's remaining difficulty is not qualitative absolute continuity or continuity. It is the matrix/dimension/law-uniform height constant.

The first unpaid global implication is correspondingly structural: obtain a dimension-free product-preserving way to aggregate physical-pair / Schur / grouped-crossing certificates before reciprocal payment, or route every target matrix into an already-paid receiver. A fixed physical pair is analytically manageable; the owner hypothesis does not force one pair with uniformly good determinant/condition number.

This run improves one such paid receiver quantitatively and records the exact sign obstruction preventing a naive `L^infinity` extension across an indefinite rank-two Schur remainder.

## 2. Latest partner result actually applied

The latest compatible fleet03/B15 report proves, among other things, the sharp qualitative phase diagram and the rank-two semidefinite estimate. If `S` is semidefinite rank two with nonzero eigenvalue magnitudes `sigma_1,sigma_2`, and `Z` is an arbitrary original-coordinate cap-one product vector, then for

\[
R=Z^T S Z
\]

one has

\[
\boxed{\|p_R\|_\infty\le {2\pi\over\sqrt{|\sigma_1\sigma_2|}}.}
\tag{2.1}
\]

The proof uses the two-dimensional orthogonal projection density cap `<=2`; it never asserts independence after spectral rotation. The same estimate survives an affine term lying in `Range(S)`: complete the square in the two spectral coordinates, which corresponds to a deterministic translation of the projected pair and does not change the joint density cap.

This `2` improves the earlier semidefinite Schur-bank receiver of fleet03/B14 r31, which used the older Parseval projection cap `e` and hence the remainder-height constant `K=pi e/sqrt(P)`.

## 3. Sharpened collective semidefinite-Schur theorem

Take an ORIGINAL-coordinate physical pair `U in R^2` in a quadratic form and write the matrix in pair/outside block form

\[
A=\begin{pmatrix}D&B\\B^T&C\end{pmatrix},
\]

where the physical block `D` is invertible and indefinite. Put

\[
\Delta=|\det D|,\qquad \kappa=\sigma_{\min}(D).
\]

Completing the pair, without rotating the input law,

\[
Q=(U+D^{-1}BZ)^T D(U+D^{-1}BZ)+R(Z),
\qquad
R(Z)=Z^T S Z,
\tag{3.1}
\]

with the exact Schur complement

\[
S=C-B^T D^{-1}B.
\]

More generally, after outside conditioning one may allow `R(Z)=Z^T S Z+q^T Z+c` provided the affine vector satisfies `q in Range(S)`.

Assume `S` is semidefinite of rank exactly two, with

\[
P:=|\sigma_1\sigma_2|>0.
\]

By (2.1), after the zero-cost range translation,

\[
\|p_R\|_\infty\le K,
\qquad
K={2\pi\over\sqrt P}.
\tag{3.2}
\]

The completed physical-pair logarithmic envelope gives, for every `r>0`,

\[
p_Q(t)
\le {2\sqrt2\over r}
+\Delta^{-1/2}\,
\mathbb E\log_+\!\left({2r^2\over\kappa|t-R|}\right).
\tag{3.3}
\]

For every `a>0`, the genuine density cap (3.2) implies exactly

\[
\begin{aligned}
\mathbb E\log_+(a/|t-R|)
&=\int_0^\infty
 \Pr\{|t-R|<ae^{-v}\}\,dv\\
&\le \int_0^\infty\min(1,2Kae^{-v})\,dv
=\Psi(2Ka),
\end{aligned}
\tag{3.4}
\]

where

\[
\Psi(z)=
\begin{cases}
z,&0\le z\le1,\\
1+\log z,&z\ge1.
\end{cases}
\]

Substituting `a=2r^2/kappa` gives

\[
\boxed{
\|p_Q\|_\infty
\le
\inf_{r>0}
\left[{2\sqrt2\over r}
+\Delta^{-1/2}\Psi\!\left({4Kr^2\over\kappa}\right)
\right].
}
\tag{3.5}
\]

The same elementary optimization as in the earlier B14 receiver is now available with the sharper `K=2pi/sqrt(P)`. Put

\[
\tau={KD\over\kappa}={2\pi\Delta\over\kappa\sqrt P}.
\]

Then

\[
\boxed{
\|p_Q\|_\infty\le G_2(\Delta,\kappa,P),
}
\tag{3.6}
\]

where

\[
G_2=
\begin{cases}
6\left({2\pi\over\kappa\sqrt\Delta\sqrt P}\right)^{1/3},
&\tau\le1/8,\\[1ex]
\Delta^{-1/2}
\left[3+\log\!\left({16\pi\Delta\over\kappa\sqrt P}\right)\right],
&\tau\ge1/8.
\end{cases}
\tag{3.7}
\]

The two branches agree at `tau=1/8`, both equaling `3/sqrt(Delta)`.

Compared with the previous `K=pi e/sqrt(P)` theorem, the low-branch multiplicative constant improves by

\[
(2/e)^{1/3}=0.902772\ldots,
\]

and the logarithmic branch drops by the exact amount

\[
\Delta^{-1/2}\log(2/e)
=-0.306852\ldots\,\Delta^{-1/2}.
\]

This is a quantitative supporting improvement, not a new structural closure. Its value is that it pays a **diffuse rank-two semidefinite Schur bank collectively** with the currently sharp source-pinned two-dimensional projection cap, without selecting or inverting any physical Schur entry.

If the active Schur bank itself has exactly two original coordinates, its joint density cap is actually `1`, so one may replace `K` by `pi/sqrt(P)` and obtain the corresponding further factor-two improvement inside `Psi`.

## 4. Actual target family paid by the sharpened theorem

Let `Z=(Z_1,...,Z_m)` be an arbitrary cap-one product bank and let `r,s in R^m` be any orthonormal pair, possibly completely diffuse. With independent cap-one `X,Y`, set

\[
Q=2XY+(r\cdot Z)^2+(s\cdot Z)^2.
\tag{4.1}
\]

The coefficient matrix has nonzero spectrum

\[
\{1,-1,1,1\},
\]

so it is literally in the owner target for every `m` and every orientation of `r,s`. The physical pair `(X,Y)` has

\[
D=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \Delta=\kappa=1,
\]

and the Schur remainder has `P=1`. Since `tau=2pi>1/8`, (3.7) gives the dimension- and orientation-free rough-law inequality

\[
\boxed{
\|p_Q\|_\infty
\le 3+\log(16\pi)
=6.9173186080\ldots .
}
\tag{4.2}
\]

No independence of `r dot Z` and `s dot Z` is used. Their entire two-dimensional projection is handled at once.

For `m=2` and `r,s` the coordinate basis, the sharper cap-one two-dimensional joint density gives instead

\[
\boxed{
\|p_{2XY+Z_1^2+Z_2^2}\|_\infty
\le3+\log(8\pi)
=6.2241714275\ldots .
}
\tag{4.3}
\]

These constants are not asserted optimal; they exhibit the exact zero-support-tax collective mechanism.

## 5. Sign obstruction: why a bounded Schur-density extension stops at semidefinite rank two

The same latest fleet03/B15 result proves that every rank-two **indefinite** orientation admits a cap-one product law with logarithmically unbounded output density. In the concrete diagonal case

\[
R=Z_1^2-Z_2^2,
\qquad Z_1,Z_2\stackrel{\rm iid}{\sim}{\rm Unif}[-1/2,1/2],
\]

the partner lower-bound calculation specializes to

\[
\boxed{
p_R(t)\ge \log {1\over32|t|},
\qquad 0<|t|<1/32.
}
\tag{5.1}
\]

Consequently, for `0<rho<1/32`,

\[
\boxed{
\Pr(|R|<\rho)
\ge2\rho\left[1+\log {1\over32\rho}\right].
}
\tag{5.2}
\]

Thus no sign-blind extension of Section 3 can replace the semidefinite remainder by a uniformly bounded rank-two remainder density. The logarithmic singularity is source-valid and sharp in scale.

This does **not** mean an indefinite rank-two Schur remainder is analytically unpaid: the completed rank-two affine half-Riesz theorem already supplies a weaker square-root small-ball estimate sufficient for the physical-pair logarithmic compiler. What fails is specifically the stronger `L^infinity`-remainder shortcut and its improved exponents/constants. The remaining global obstruction is still aggregation of local certificates, not existence of a fixed-matrix bound.

## 6. Required newest-Claude ruled theorem applied at a real inequality

I reread `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` at the required source commit

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Its completed ruled one-sheet theorem says that for a rank-three form of signature `(+,+,-)` with eigenvalue magnitudes `lambda_1,lambda_2,mu`, the majority-side density is bounded by

\[
C_+=
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/\lambda_1+
\cos^2\theta/\lambda_2+1/\mu}}.
\tag{6.1}
\]

For unit curvatures this is at most `pi sqrt(2)`.

Apply this to the actual target form

\[
Q=2XY+Z^2+W^2,
\tag{6.2}
\]

with four arbitrary independent cap-one marginals. Its matrix spectrum is `{1,-1,1,1}`. Condition on the ORIGINAL coordinate `W=w`. Then

\[
Q-w^2=2XY+Z^2
\]

has rank three, signature `(+,+,-)`, and all three eigenvalue magnitudes equal one. Therefore the completed ruled theorem pays the positive one-sheet submeasure:

\[
\boxed{
\Pr\{Q\in I,\ Q\ge W^2\}
\le \pi\sqrt2\,|I|
}
\tag{6.3}
\]

for every interval `I`.

Independently, Section 4 with `m=2` pays the full law by (4.3). Hence the complementary two-sheet/minority submeasure in this concrete owner-target chamber is also bounded:

\[
\Pr\{Q\in I,\ Q<W^2\}
\le[3+\log(8\pi)]|I|.
\tag{6.4}
\]

The point is methodological: the minority side is closed here by retaining the two-square Schur bank as a collective smoothing resource, not by the live-refuted generic X-ray shortcut.

## 7. Independent ruled/rough-input bridge audit

The ruled geometric calculation itself has two delicate factors, both rechecked.
After spectral scaling to

\[
q_0(z)=z_1^2+z_2^2-z_3^2,
\]
use the ruling

\[
F(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3).
\]

Direct differentiation gives

\[
F_\theta\times F_t={1\over2}\nabla q_0(F),
\]

so

\[
{d\sigma\over|\nabla q_0|}={1\over2}\,d\theta\,dt.
\tag{7.1}
\]

After undoing the spectral scaling, the line direction is

\[
v_\theta=
\left(-{\sin\theta\over\sqrt{\lambda_1}},
{\cos\theta\over\sqrt{\lambda_2}},
{1\over\sqrt\mu}\right).
\tag{7.2}
\]

The parameter `t` is not arclength, so the line integral contributes the reciprocal speed `1/|v_theta|`. The two-dimensional product-projection cap `2` cancels the coarea factor `1/2`, yielding exactly (6.1). Omitting either factor changes the constant.

For arbitrary rough cap-one active marginals, mollify only the three active ORIGINAL coordinates:

\[
f_i^{(\eta)}=f_i*\gamma_\eta.
\]

Then `f_i^(eta)<=1`, independence is preserved, and

\[
\left\|
\prod_{i=1}^3 f_i^{(\eta)}-
\prod_{i=1}^3 f_i
\right\|_1
\le\sum_{i=1}^3\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{7.3}
\]

Conditioning outside the active triple produces only deterministic affine terms. When the active physical block is invertible, square completion is a deterministic translation in the original active coordinates, so (7.3) is unchanged. Deterministic quadratic pushforward and restriction to the fixed conditional majority event contract total variation. Therefore the smooth ruled interval inequality passes to the rough product law with **the identical constant**.

At the critical cone level there is no hidden atom: the zero set of a nonzero polynomial has Lebesgue measure zero under the absolutely continuous product law. Hence (6.3) is an essential-boundedness statement for a positive submeasure under fully rough admissible inputs. No output continuity is used to obtain it.

## 8. Regularity ledger

The newest fleet03/B15 phase diagram makes the logical separation exact.

- A nonconstant quadratic pushforward of an absolutely continuous joint law is absolutely continuous; this is qualitative and supplies no universal height.
- At rank one, a cap-one product law can produce an inverse-square-root unbounded density.
- At rank two indefinite, a cap-one product law can produce the logarithmic blow-up (5.1).
- At rank two semidefinite, every cap-one product law has a bounded density, but a continuous representative can fail to exist.
- At rank at least three, every fixed cap-one product instance has a bounded `C_0` density by the completed fixed-matrix theorem, but its constant may depend badly on the matrix.

Thus continuity cannot be used to smuggle in the owner bound. In this run every height estimate is established first by interval/projection/pair-log geometry. Continuity, where desired for a rank-at-least-three full output, is a later zero-cost fixed-instance regularity conclusion.

## 9. What remains

The semidefinite Schur sharpening does not solve the global problem. The owner hypothesis `s_3(A)>=1` does not force an original-coordinate indefinite pair with `Delta`, `kappa`, and a rank-two semidefinite Schur determinant `P` simultaneously bounded below. Known diffuse bank examples make every single physical pair poorly conditioned while aggregate spectral curvature stays order one.

Therefore the useful next implication is not another continuity theorem. It is an **aggregate-before-inversion structural lemma**: combine many weak physical pairs / grouped crossings / Schur directions into one product-preserving receiver whose bound depends on spectral or volume currencies already forced by `s_3(A)>=1`, before taking reciprocals of local minors.

The full QFORM target remains OPEN.
