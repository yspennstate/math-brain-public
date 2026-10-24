# account02/B12 — arbitrary-orientation exceptional-eigenvalue stability

**Run:** `20260922T115433Z-account02-B12`  
**Live programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Additional eigenvalue control`  
**Classification:** `PROVED_SUPPORTING_THEOREMS / TARGET_LEVEL_SUBCLASSES / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub retrieval was used, but no native learned-memory receiver/context ingestion was verified.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 1. Control pivot and exact target

Fresh protected controls supersede the scheduled FEI wording: all eighty workers now work only on the quadratic-form bounded-density conjecture. The live target is to prove one universal finite `C` such that, for every dimension `n`, independent real `X_i` with densities bounded by `1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, the law of `X^T A X` has an essentially bounded density of norm at most `C`.

The current B12 assignment is to control **additional eigenvalues** without treating the rotated remainder as an independent convolution.

## 2. Completed partner result actually consumed

I consumed the latest compatible completed result from the assigned partner `account03/B12`:

`yspennstate/math-open-problems@08f387da860f00c13f30de170286a82eb13108e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/account03-B12-20260922T114435Z-349dfcff7c/REPORT.md`.

That report proves a uniform bound below `24.231` for the four-variable family

`epsilon*lambda*I_4 + (mu-epsilon*lambda) v v^T`

when the exceptional eigenvector is **flat**, `|v_i|=1/2`, by stitching a definite principal pair to a nonsingular principal triple. Its exact remaining implication is to remove flatness / control a nonflat rank-one perturbation by a finite pair/triple cover.

I also read the immutable source theorem underlying that stitching:

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

At the scope used below it proves:

* if a `2 x 2` original-coordinate principal block `C` is positive or negative definite, then after arbitrary linear tilts the output density is at most `pi/sqrt(|det C|)`;
* if a `3 x 3` original-coordinate principal block `C` has smallest singular value `kappa>0`, then after arbitrary linear tilts the output density is at most `(2*pi+3*sqrt(3))/kappa`;
* conditioning all other original independent coordinates is legitimate and turns cross terms only into linear tilts, so no false convolution independence is used.

The live correction inbox was empty at the source-bound control read.

## 3. Pair/triple covering lemma for an arbitrary exceptional eigenvector

After output reflection and scaling it suffices to consider

\[
B=-I_4+s vv^T,
\qquad v\in S^3,
\qquad s\in\mathbb R
\tag{3.1}
\]

with completely arbitrary `s`. Write

\[
w_i=v_i^2,
\qquad w_1\le w_2\le w_3\le w_4,
\qquad \sum_i w_i=1,
\tag{3.2}
\]

after relabeling coordinates, and put

\[
a=w_1+w_2,
\qquad b=1-w_1.
\tag{3.3}
\]

Two elementary inequalities are the entire nonflatness input:

\[
a\le {1\over2},
\qquad
{b\over a}\ge {3\over2}
\quad(a>0).
\tag{3.4}
\]

Indeed `w_3+w_4 >= 2w_2 >= w_1+w_2=a`, so `a<=1/2`; also `w_1<=a/2`, hence

\[
{b\over a}={1-w_1\over a}\ge {1\over a}-{1\over2}\ge {3\over2}.
\]

For a coordinate set `J`, the principal block is

\[
B_J=-I_{|J|}+s v_Jv_J^T,
\tag{3.5}
\]

whose eigenvalues are `-1` with multiplicity `|J|-1` and

\[
-1+s\|v_J\|_2^2.
\tag{3.6}
\]

Choose the rational threshold

\[
\theta={983\over1000}.
\tag{3.7}
\]

### Branch P: a uniformly definite pair

If

\[
sa\le\theta,
\tag{3.8}
\]

then the principal pair on coordinates `{1,2}` is negative definite. Its eigenvalues are `-1` and `-1+sa`, so

\[
\det B_{\{1,2\}}=1-sa\ge {17\over1000}.
\tag{3.9}
\]

The definite-pair theorem gives

\[
\|p\|_\infty\le \pi\sqrt{1000\over17}.
\tag{3.10}
\]

### Branch T: a uniformly nonsingular triple

If (3.8) fails, then `sa>983/1000`; in particular `s>0` and `a>0`. Take the triple complementary to the smallest coordinate, namely `{2,3,4}`. Its squared exceptional-vector mass is `b`. By (3.4),

\[
sb={b\over a}sa
>{3\over2}{983\over1000}
={2949\over2000}.
\tag{3.11}
\]

Hence the nontrivial eigenvalue of that principal triple obeys

\[
-1+sb>{949\over2000}.
\tag{3.12}
\]

The other two eigenvalues are exactly `-1`, therefore

\[
\sigma_{\min}(B_{\{2,3,4\}})
\ge {949\over2000}.
\tag{3.13}
\]

The principal-triple theorem gives

\[
\|p\|_\infty
\le {2000\over949}(2\pi+3\sqrt3).
\tag{3.14}
\]

Thus the pair and triple bad sets cannot coincide, for **any** orientation `v` and **any** exceptional eigenvalue parameter `s`.

## 4. Main theorem: flatness removed completely

### Theorem 4.1 — `QFORM-ARBITRARY-ORIENTATION-ONE-EXCEPTION-v1`

Let `Y_1,...,Y_4` be independent real random variables with probability densities bounded by `1`. Let `lambda>=1`, `epsilon in {+1,-1}`, `mu in R`, and let `v in S^3` be arbitrary. Set

\[
B=\epsilon\lambda I_4+(\mu-\epsilon\lambda)vv^T.
\tag{4.1}
\]

Then for every linear tilt `ell in R^4` and scalar `c`,

\[
T=Y^TBY+\ell^TY+c
\]

has an essentially bounded density satisfying

\[
\boxed{
\|p_T\|_\infty
\le {C_{\rm orient}\over\lambda},
\qquad
C_{\rm orient}:=
\max\left\{
\pi\sqrt{1000\over17},
{2000\over949}(2\pi+3\sqrt3)
\right\}
<24.193.
}
\tag{4.2}
\]

#### Proof

If `epsilon=+1`, reflect the scalar output, replacing `B` by `-B`; this preserves the density norm and reduces to baseline sign `-1`. Scale the scalar output by `lambda`. The normalized quadratic block is exactly of the form (3.1), with arbitrary real `s`. Sections 3P and 3T show that either a definite original-coordinate pair has determinant at least `17/1000`, or an original-coordinate triple has smallest singular value at least `949/2000`. Both source theorems already allow arbitrary linear tilts. Taking the worse constant gives (4.2), and restoring scale contributes the factor `1/lambda`. QED.

This strictly removes the flat-sign-vector hypothesis of the consumed partner theorem. The numerical constant is also slightly smaller because the switch point was reoptimized for the orientation-free argument.

## 5. High-dimensional consequence: one completely arbitrary extra eigenvalue

### Corollary 5.1 — `QFORM-CODIMENSION-ONE-SPECTRAL-STABILITY-v1`

Let `n>=4`, let `X_1,...,X_n` be independent with densities bounded by `1`, and suppose

\[
A=\epsilon\lambda I_n+(\mu-\epsilon\lambda)vv^T
\tag{5.1}
\]

for some `lambda>=1`, `epsilon in {+1,-1}`, arbitrary `mu in R`, and arbitrary unit `v in R^n`. Equivalently, `A` has `n-1` eigenvalues equal to `epsilon*lambda` and one completely arbitrary exceptional eigenvalue `mu`, with arbitrary exceptional eigenvector. Then

\[
\boxed{
\|p_{X^TAX}\|_\infty\le {C_{\rm orient}\over\lambda}< {24.193\over\lambda}.
}
\tag{5.2}
\]

#### Proof

Choose any four original coordinates `J` and condition on all coordinates outside `J`. If `v_J=0`, the selected quadratic block is simply `epsilon*lambda I_4` and the pair theorem is immediate. Otherwise write `v_J=rho*w` with `w in S^3`. The selected principal block is

\[
\epsilon\lambda I_4+(\mu-\epsilon\lambda)\rho^2 ww^T,
\]

which is again of the form (4.1), with an arbitrary effective fourth eigenvalue. Cross couplings to conditioned coordinates become linear tilts. Theorem 4.1 applies uniformly in the outside variables, and averaging the conditional densities preserves the same cap. QED.

This is a genuine target-level subclass: it allows the added eigenvalue to be zero, tiny, huge, or of the opposite sign, and it does not assume the exceptional eigendirection is aligned with the independent coordinates.

## 6. Quantitative stability under a 1 percent cluster

The exact-equality theorem has a robust version.

### Theorem 6.1 — `QFORM-ONE-EXCEPTION-ONE-PERCENT-STABILITY-v1`

Let `B` be a real symmetric `4 x 4` matrix. Suppose that for some `lambda>0` and `epsilon in {+1,-1}`, three eigenvalues of `B` satisfy

\[
|\beta_j-\epsilon\lambda|\le {\lambda\over100},
\qquad j=1,2,3,
\tag{6.1}
\]

while the fourth eigenvalue is arbitrary. For independent `Y_1,...,Y_4` with densities bounded by `1`, and every linear tilt and constant, the corresponding affine quadratic output has density bounded by

\[
\boxed{
\|p\|_\infty
\le {C_{1\%}\over\lambda},
\qquad
C_{1\%}:={100(2\pi+3\sqrt3)\over43}
<26.697.
}
\tag{6.2}
\]

#### Proof

Reflect and scale so that `epsilon=-1` and `lambda=1`. Let `v` be a unit eigenvector for the arbitrary fourth eigenvalue. Then

\[
B=B_0+E,
\qquad
B_0=-I_4+s vv^T,
\qquad
\|E\|_{op}\le {1\over100},
\tag{6.3}
\]

for some real `s`.

Repeat Section 3 with the less aggressive threshold

\[
\theta={24\over25}.
\tag{6.4}
\]

If `sa<=24/25`, the selected base pair has eigenvalues at most `-1` and `-1/25`. The principal restriction of `E` has operator norm at most `1/100`, so Weyl's inequality leaves the perturbed pair negative definite with eigenvalue magnitudes at least `99/100` and `3/100`. Therefore

\[
\det|B_{pair}|\ge {297\over10000}
\]

and the pair theorem gives

\[
\|p\|_\infty\le {100\pi\over\sqrt{297}}<18.230.
\tag{6.5}
\]

If `sa>24/25`, the triple complementary to the smallest coordinate has base smallest singular value at least

\[
{3\over2}{24\over25}-1={11\over25}.
\]

Singular-value perturbation by at most `1/100` leaves

\[
\sigma_{min}(B_{triple})\ge {11\over25}-{1\over100}={43\over100}.
\]

The triple theorem gives

\[
\|p\|_\infty\le {100(2\pi+3\sqrt3)\over43}<26.697.
\tag{6.6}
\]

The latter dominates (6.5). QED.

By conditioning outside a four-coordinate principal block, the same statement holds in arbitrary dimension whenever such a block has three same-sign eigenvalues in a one-percent cluster around magnitude `lambda`; outside eigenvalues and cross couplings are unrestricted.

A global spectral special case is immediate: if

\[
A=\epsilon\lambda I_n+R+E,
\qquad \operatorname{rank}R\le1,
\qquad \|E\|_{op}\le\lambda/100,
\]

then every four-coordinate principal block has the required decomposition, so for `n>=4` the full quadratic output obeys the bound (6.2), regardless of the one exceptional eigenvalue represented by `R`.

## 7. Exact mechanism change and remaining implication

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No universal theorem for arbitrary matrices with merely three large eigenvalues has been proved.

**MECHANISM CHANGE / SUPPORTING MOVEMENT:** the partner's flat exceptional eigenvector is no longer needed. The new pair/triple cover uses only the order statistics of the actual coordinate weights `v_i^2`, yielding a source-valid orientation-free theorem and a quantitative perturbation-stability theorem. The extra eigenvalue is never separated as an independent convolution; arbitrary outside terms are handled by conditioning in the original independent coordinates.

**First unpaid implication:** the target hypothesis gives only three large eigenvalues, not a codimension-one same-sign cluster. A next theorem must either (i) extract, possibly after averaging rather than selecting, a four-coordinate block admitting a quantitative pair/triple cover from three arbitrary large spectral directions; or (ii) use the aggregate principal-minor mass (Cauchy-Binet type) without paying for a single tiny coordinate minor. The delocalized rank-three projector obstruction in the underlying B15 source shows why a one-fixed-triple argument cannot suffice.

## 8. Source pins and correction status

* fresh live control before write: `yspennstate/math-research-brain@0a3aca1999f48e33c318c809477ade8feac096ae`, owner revision `2026-09-22.5`;
* consumed partner: `yspennstate/math-open-problems@08f387da860f00c13f30de170286a82eb13108e1:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/account03-B12-20260922T114435Z-349dfcff7c/REPORT.md`;
* underlying pair/triple source: `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`;
* correction inbox at the source-bound control read: empty.

No novelty or publication-priority claim is made. The full quadratic-form conjecture remains **OPEN**.
