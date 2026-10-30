SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T15:56:25Z.
attacking: moving-fold receiver localization — retain a whole product driver while paying arbitrary scalar receiver self-curvature, rather than taking a worst conditional fold or normalizing active fragments.

# fleet02/B14 r39 — moving-fold receiver localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM_AND_PROOF-ORDER_OBSTRUCTION / FULL_QFORM_OPEN`  
Continuity: separate and not claimed here.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

`QFORM-RECEIVER-CORE-COUPLING-OR-VOLUME-EXIT-v1`: in every surviving N3/no-pivot state, before active-law fragmentation, force either (i) a whole-law D'/D5/ridge/mixed-hub/grouped-bank exit, or (ii) an affine-uniform L3 core plus a scalar receiver whose moving quadratic fold is driven by a nonzero projection of a disjoint original-coordinate product bank, or (iii) a new estimate that keeps the receiver-core coupling unconditioned long enough to aggregate it. The theorem below pays arbitrary scalar receiver self-curvature exactly, so the remaining receiver debt is structural extraction and receiver-core coupling, not the scalar fold itself.

## 1. Moving-fold theorem

Let `Z=(Z_1,...,Z_m)` have mutually independent real probability densities bounded by one, let `W` be an independent scalar with density `f<=1`, and for almost every `z` let `T_z` be a real random variable built from coordinates independent of `W`, with density `q_z` satisfying

\[
\|q_z\|_3\le K
\tag{1.1}
\]

uniformly in `z`. The law of `T_z` may depend arbitrarily measurably on `z` through translations, linear terms, or other already-controlled affine parameters. Let `v\ne0` in `R^m`, and let `a,d` be arbitrary real numbers. Define

\[
Q=T_Z+aW^2+(2v^TZ+d)W.
\tag{1.2}
\]

### Theorem 1.1 — `QFORM-MOVING-FOLD-RECEIVER-LOCALIZATION-v1`

\[
\boxed{
\|p_Q\|_\infty
\le 2^{7/6}K\,\|v\|_2^{-1/3}.
}
\tag{1.3}
\]

The bound is completely independent of `a`, `d`, all translations, fragment number and separation, support diameter, tails, and moments.

### Proof: nonzero receiver self-curvature

Fix `z` and put

\[
b=2v^Tz+d,\qquad R_b=aW^2+bW.
\]

Conditional on `Z=z`, `T_z` and `R_b` are independent. Young's convolution inequality gives

\[
\|p_{Q\mid Z=z}\|_\infty
\le \|q_z\|_3\,\|p_{R_b}\|_{3/2}
\le K\|p_{R_b}\|_{3/2}.
\tag{1.4}
\]

Assume first `a!=0`, and set the critical point

\[
x_b=-{b\over2a}.
\]

Completing the square gives `R_b=a(W-x_b)^2-b^2/(4a)`. For `r>0`, the two inverse branches at distance `r` from `x_b` give

\[
p_{R_b}(y)={f(x_b+r)+f(x_b-r)\over2|a|r},
\qquad |y+b^2/(4a)|=|a|r^2
\tag{1.5}
\]

on the appropriate side of the critical value. Since `0<=f<=1`,

\[
(u+v)^{3/2}\le\sqrt2\,(u+v),\qquad 0\le u,v\le1.
\tag{1.6}
\]

Using `dy=2|a|r\,dr`, (1.5)-(1.6) imply

\[
\begin{aligned}
\|p_{R_b}\|_{3/2}^{3/2}
&\le |a|^{-1/2}
\int_0^\infty r^{-1/2}
\{f(x_b+r)+f(x_b-r)\}\,dr\\
&=|a|^{-1/2}H_f(x_b),
\end{aligned}
\tag{1.7}
\]

where

\[
H_f(x)=\int_{\mathbb R}|w-x|^{-1/2}f(w)\,dw.
\]

Therefore

\[
\|p_{R_b}\|_{3/2}
\le |a|^{-1/3}H_f(x_b)^{2/3}.
\tag{1.8}
\]

Now average the *moving* critical point rather than taking its supremum. Put

\[
B=2v^TZ+d,\qquad X=-{B\over2a}.
\]

The one-dimensional Rogozin-Ball product-projection bound gives

\[
\|p_B\|_\infty\le {1\over\sqrt2\,\|v\|_2},
\tag{1.9}
\]

hence

\[
\|p_X\|_\infty\le M:={\sqrt2|a|\over\|v\|_2}.
\tag{1.10}
\]

For any probability density bounded by `M`, symmetric decreasing rearrangement gives the cap-only half-Riesz estimate

\[
\sup_w\mathbb E|X-w|^{-1/2}
\le M\int_{-1/(2M)}^{1/(2M)}|u|^{-1/2}du
=2\sqrt2\,M^{1/2}.
\tag{1.11}
\]

Fubini and `int f=1` yield

\[
\mathbb EH_f(X)\le2\sqrt2\,M^{1/2}.
\tag{1.12}
\]

Since `s -> s^{2/3}` is concave,

\[
\mathbb EH_f(X)^{2/3}
\le(2\sqrt2\,M^{1/2})^{2/3}
=2M^{1/3}.
\tag{1.13}
\]

Combining (1.4), (1.8), (1.10), and (1.13),

\[
\begin{aligned}
\|p_Q\|_\infty
&\le K|a|^{-1/3}\,2M^{1/3}\\
&=2^{7/6}K\|v\|_2^{-1/3}.
\end{aligned}
\tag{1.14}
\]

The receiver curvature `a` cancels exactly.

### Proof: zero receiver self-curvature

If `a=0`, then

\[
\|p_{bW}\|_{3/2}\le |b|^{-1/3}
\tag{1.15}
\]

because `int f^{3/2}<=1`. The same product-projection estimate gives `B=2v^TZ+d` density cap

\[
M_B\le{1\over\sqrt2\|v\|_2}.
\]

The cap-only one-third Riesz rearrangement bound is

\[
\mathbb E|B|^{-1/3}
\le3\,2^{-2/3}M_B^{1/3}
=3\,2^{-5/6}\|v\|_2^{-1/3},
\tag{1.16}
\]

which is smaller than `2^(7/6)||v||_2^(-1/3)`. This proves (1.3) for all `a`.

## 2. Exact localization consequences

The mechanism is whole-law and translation-safe. Translating `W` changes `aW^2` only by a linear term and a constant, absorbed into `d` and `T_z`. Translating `Z` changes only `d` and the measurable affine parameters of `T_z`. Conditioning on genuinely outside original coordinates is also free when it only makes `d` and those affine parameters measurable, because (1.3) is uniform in them.

Most importantly, no active driver fragment is normalized. The moving fold `-B/(2a)` is integrated against the entire product law of `Z` before the reciprocal singularity is paid. Arbitrary distant fragments and unbounded supports are therefore admissible with no diameter or moment parameter.

The theorem also allows an arbitrary scalar receiver diagonal entry `a`. Cross terms from the chosen receiver scalar to already-conditioned receiver coordinates merely alter `d`. What is not covered is a coefficient of `W` depending on *unconditioned core variables* for which the uniform L3 certificate (1.1) is not known to survive.

## 3. Application of the designated partner fleet03/B14

The newest compatible designated-partner result used here is fleet03/B14 auto11, canonical report

`yspennstate/math-open-problems@8b9adaf929bab4d0d18a15b81055040f3313629a`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T153652Z-fleet03-B14-QFORM-auto11/REPORT.md`.

That report proves `QFORM-L2-BILINEAR-RECEIVER-LOCALIZATION-v1` and, from the fleet04/B14 affine slice-Fresnel theorem, obtains the uniform core Fourier estimate

\[
|\phi_{T_z}(t)|\le B|t|^{-3/4},
\qquad
B=2\pi^{3/4}|h|^{-1/2}|\gamma|^{-1/4},
\tag{3.1}
\]

uniformly in the conditioning-generated affine data and in an arbitrary hub phase. The partner used (3.1) only to obtain an L2 core and hence required a linear receiver. Here (3.1) is upgraded to L3.

Indeed, using also `|phi|<=1`,

\[
\int_{\mathbb R}|\phi_{T_z}(t)|^{3/2}dt
\le18B^{4/3}.
\tag{3.2}
\]

Hausdorff-Young for the inverse Fourier transform gives

\[
\boxed{
\|p_{T_z}\|_3
\le
3^{4/3}2^{8/9}
|h|^{-4/9}|\gamma|^{-2/9}.
}
\tag{3.3}
\]

Insert (3.3) into Theorem 1.1 for a scalar receiver whose coefficient is `2v^TZ+d`, now allowing an arbitrary receiver self coefficient `a`. The resulting structured branch is

\[
\boxed{
\|p_Q\|_\infty
\le
3^{4/3}2^{37/18}
|h|^{-4/9}|\gamma|^{-2/9}\|v\|_2^{-1/3}.
}
\tag{3.4}
\]

The absolute coefficient in (3.4) is

\[
17.986454066189225\ldots.
\]

At the partner's normalized active scale `|h|>=1/sqrt(2)`, `|gamma|>=1`, and `||v||_2>=1`,

\[
\|p_Q\|_\infty
\le3^{4/3}2^{41/18}
=20.981720987211656\ldots.
\tag{3.5}
\]

Thus the partner's explicit receiver-self-curvature debt is paid for one isolated scalar receiver, with arbitrary translations and rough support geometry retained. This does not prove that every full-target matrix contains such a disjoint scalar receiver.

## 4. A target-valid family and application of the required Claude source

Consider independent arbitrary cap-one variables `U_1,U_2,Z,W` and, for arbitrary `a in R`,

\[
Q_a=U_1^2+U_2^2+aW^2+2ZW.
\tag{4.1}
\]

Its matrix is the direct sum of `1`, `1`, and

\[
\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]

The latter block has eigenvalues

\[
\lambda_\pm={a\pm\sqrt{a^2+4}\over2},
\qquad \lambda_+\lambda_-=-1.
\tag{4.2}
\]

Hence at least one of `|lambda_+|,|lambda_-|` is at least one, and (4.1) has at least three eigenvalues of modulus at least one for every real `a`. It is an exact-target family, including arbitrarily large receiver self-curvature.

The diagonal two-square estimate gives

\[
\|p_{U_1^2+U_2^2}\|_\infty\le\pi,
\qquad
\|p_{U_1^2+U_2^2}\|_3\le\pi^{2/3}.
\tag{4.3}
\]

Theorem 1.1 with `v=1` therefore yields

\[
\boxed{
\|p_{Q_a}\|_\infty
\le2^{7/6}\pi^{2/3}
=4.815428181530122\ldots
}
\tag{4.4}
\]

uniformly in `a` and in every admissible product law, with no support, moment, connectedness, or translation assumption.

The required newest-Claude source was read at the pinned directory

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. A completed result is applied to the same family: Theorem B of `COUNTEREXAMPLE_SEARCH.md` states, under exactly the three-large-eigenvalue hypothesis,

\[
\|p_Q\|_\infty
\le2\sqrt{2\pi}\sum_i|Pe_i|,
\tag{4.5}
\]

where `P` is the projection onto `range(A)`. The matrix in (4.1) is invertible, so `P=I_4` and

\[
\boxed{
\|p_{Q_a}\|_\infty
\le8\sqrt{2\pi}
=20.053026197048002\ldots
}
\tag{4.6}
\]

for every `a`. This is a direct source-valid universal certificate on the exact same target family; (4.4) is a sharper localization-compatible bound obtained by exploiting the moving-fold structure.

## 5. Proof-order obstruction: worst conditional fold is the wrong interface

The cancellation of `a` in (1.14) is genuinely an averaging phenomenon. Let `W` be uniform on `[-1/2,1/2]`, take `Z` uniform on `[-1/2,1/2]`, `v=1`, `d=0`, and `a!=0`. At the legal conditioning value `z=0`, the receiver is simply `aW^2`. Its density is

\[
p(y)={1\over\sqrt{|a|y}}\,\mathbf1_{(0,|a|/4)}(y)
\tag{5.1}
\]

up to reflection when `a<0`. Consequently

\[
\boxed{
\|p_{aW^2}\|_{3/2}=2|a|^{-1/3}.
}
\tag{5.2}
\]

Thus any proof that first takes

\[
\sup_z\|p_{aW^2+(2z)W}\|_{3/2}
\tag{5.3}
\]

pays at least `2|a|^(-1/3)` and diverges as `a -> 0`, even though the whole-law bound (1.3) is independent of `a`. Embedding the same receiver in the exact-target form (4.1) shows that the divergence is purely a proof-interface artifact: the actual output density remains uniformly bounded by both (4.4) and the independent Claude bound (4.6).

This is `QFORM-WORST-FOLD-SUPREMUM-BARRIER-v1`. It is not a QFORM counterexample. It says that the scalar receiver must be averaged against the moving product-law critical point before taking the endpoint norm; worst-fiber localization destroys precisely the cancellation needed near zero curvature.

## 6. Scope and remaining debt

What is now paid:

* arbitrary translations and conditioning-generated affine parameters in the uniform L3 core;
* arbitrary fragmentation, support diameter and tails of the driver and receiver laws;
* arbitrary scalar receiver self-curvature, including the singular limit `a -> 0`;
* the codimension-one moving fold, by a cap-only half-Riesz average over a whole independent product driver.

What remains unpaid for the full theorem:

* a structural statement extracting a nontrivial driver projection `v` together with a compatible affine-uniform L3 core in every surviving N3/no-pivot matrix, or an alternative whole-law D'/D5/ridge/mixed-hub exit;
* receiver-core cross-couplings that make the receiver coefficient depend on unconditioned core variables rather than only on the independent driver;
* continuity of the final density under arbitrary rough input laws.

No bounded-diameter, fixed-fragment, moment, log-concavity, diagonal-basis, or post-rotation independence hypothesis is used.

Full QFORM: OPEN.  
Continuity: OPEN.  
Native learned-memory ingestion: NOT VERIFIED.
