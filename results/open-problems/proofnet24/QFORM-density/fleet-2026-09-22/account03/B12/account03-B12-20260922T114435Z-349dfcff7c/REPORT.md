# account03/B12 — flat-mode fourth-eigenvalue stability by pair/triple stitching

**Run:** `account03-B12-20260922T114435Z-349dfcff7c`  
**Live programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Classification:** `PROVED_SUPPORTING_THEOREM / TARGET_LEVEL_SUBCLASS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport was used, but no authenticated native brain receiver/context retrieval occurred.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 1. Why this run changed target

The scheduled prompt still named FEI, but the fresh protected owner control at the start of this invocation explicitly suspends FEI and assigns all eighty workers to the quadratic-form bounded-density conjecture. I therefore did no new FEI mathematics.

The active target is: for independent real `X_i` with densities bounded by `1`, and real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove a dimension- and law-independent bound on the density of `X^T A X`.

My current assignment is **additional eigenvalue control**: prove a valid reduction/stability result for arbitrary extra eigenvalues of either sign, without pretending that a rotated quadratic remainder is independent.

## 2. Named peer result consumed

I applied the completed peer artifact

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

At the exact scope used here it proves:

1. **definite pair theorem.** If a `2 x 2` principal quadratic block `C` is positive or negative definite, then after arbitrary linear tilts the output density is at most
   \[
   \pi/\sqrt{|\det C|};
   \]
2. **nonsingular triple theorem.** If a symmetric `3 x 3` principal block `C` has smallest singular value `\kappa>0`, then after arbitrary linear tilts the output density is at most
   \[
   C_3/\kappa,\qquad C_3:=2\pi+3\sqrt3.
   \]
3. both estimates extend to a full high-dimensional form by conditioning all coordinates outside the selected original-coordinate block; outside quadratic terms become constants and cross couplings become linear tilts. No convolution independence is assumed.

The current correction inbox contains no challenge to these statements. I checked the algebra below independently at the needed scope.

## 3. A four-coordinate family where each local mechanism separately degenerates

Let
\[
v={1\over2}(s_1,s_2,s_3,s_4)^T,\qquad s_i\in\{\pm1\},
\]
so `||v||_2=1`. Let `\lambda>=1`, `\epsilon in {+1,-1}`, and let `\mu in R` be completely arbitrary. Consider the four-coordinate symmetric block
\[
B=\epsilon\lambda I_4+(\mu-\epsilon\lambda)vv^T.
\tag{3.1}
\]
Its eigenvalues are
\[
\boxed{\epsilon\lambda,\epsilon\lambda,\epsilon\lambda,\mu}.
\tag{3.2}
\]
Thus three eigenvalues already have magnitude at least one, while the fourth eigenvalue may be smaller, larger, zero, or of either sign.

Coordinate sign flips send `v` to `(1,1,1,1)/2` and preserve independence and the density cap. Reflecting the scalar output if necessary handles `\epsilon=+1`. After scaling the output by `\lambda`, it is therefore enough to study
\[
B_r=-I_4+(1+r){J_4\over4},\qquad r\in\mathbb R,
\tag{3.3}
\]
where the spectrum is `(-1,-1,-1,r)`.

The point of this family is that it crosses two genuine local degeneracies:

* at `r=1/3`, every `3 x 3` principal block is singular;
* at `r=1`, every `2 x 2` principal block is singular.

A one-block proof using only one of the two peer mechanisms therefore blows up, even though the full four-variable family should remain regular. The result below stitches the mechanisms with no gap.

## 4. Exact pair and triple spectra

Every `2 x 2` principal block of `B_r` is
\[
C_2(r)=
\begin{pmatrix}
(r-3)/4&(r+1)/4\\
(r+1)/4&(r-3)/4
\end{pmatrix}
\tag{4.1}
\]
and has eigenvalues
\[
-1,\qquad {r-1\over2}.
\tag{4.2}
\]
Hence for `r<1` it is negative definite and
\[
\boxed{\det C_2(r)={1-r\over2}.}
\tag{4.3}
\]

Every `3 x 3` principal block is
\[
C_3(r)=-I_3+(1+r){J_3\over4}
\tag{4.4}
\]
and has eigenvalues
\[
-1,-1,{3r-1\over4}.
\tag{4.5}
\]
Therefore
\[
\boxed{\sigma_{\min}(C_3(r))=
\min\left(1,{|3r-1|\over4}\right).}
\tag{4.6}
\]

These formulas make the two degeneracies complementary: the triple collapses at `r=1/3` while the pair is then uniformly definite; the pair collapses at `r=1` while the triple is then uniformly nonsingular.

## 5. Main theorem — arbitrary fourth eigenvalue, one universal constant

### Theorem 5.1 — `QFORM-FLAT-FOURTH-EIGENVALUE-STABILITY-v1`

Let `Y_1,...,Y_4` be independent real random variables with probability densities bounded by `1`. Let `B` be as in (3.1), with `\lambda>=1`, arbitrary `\mu in R`, arbitrary sign `\epsilon`, and arbitrary flat sign vector `v` with `|v_i|=1/2`. Then for every linear tilt `ell in R^4` and scalar `c`,
\[
T=Y^TBY+\ell^TY+c
\]
has an essentially bounded density and
\[
\boxed{
\|p_T\|_\infty
\le {C_*\over\lambda},
\qquad
C_*:=\max\left\{{20\pi\over\sqrt7},
{800(2\pi+3\sqrt3)\over379}\right\}
<24.231.
}
\tag{5.1}
\]
In particular the bound is completely independent of the fourth eigenvalue `\mu`, including its sign and size.

#### Proof

After the reductions above, take `\lambda=1`, `\epsilon=-1`, and write the free eigenvalue as `r`.

Set the rational switch point
\[
r_0={193\over200}.
\tag{5.2}
\]

**Case 1: `r<=r_0`.** Since `r_0<1`, the `2 x 2` block (4.1) is negative definite and
\[
\det C_2(r)={1-r\over2}
\ge {1-r_0\over2}
={7\over400}.
\]
The peer definite-pair theorem, which already permits arbitrary linear tilts from the other two coordinates, gives
\[
\|p_T\|_\infty
\le {\pi\over\sqrt{7/400}}
={20\pi\over\sqrt7}
<23.749.
\tag{5.3}
\]

**Case 2: `r>=r_0`.** Then `3r-1>0` and every `3 x 3` principal block obeys
\[
\sigma_{\min}(C_3(r))
\ge \min\left(1,{3r_0-1\over4}\right)
={379\over800}.
\]
The peer nonsingular-triple theorem gives
\[
\|p_T\|_\infty
\le {2\pi+3\sqrt3\over379/800}
={800(2\pi+3\sqrt3)\over379}
<24.231.
\tag{5.4}
\]

The larger of (5.3) and (5.4) is the displayed `C_*`. Restoring scale multiplies the density bound by `1/\lambda`. Coordinate reflections and scalar output reflection preserve the density norm. QED.

### Critical-point check

At the most obvious principal-triple failure,
\[
r={1\over3},
\]
all four `3 x 3` principal blocks have eigenvalues `(-1,-1,0)`. Nevertheless every `2 x 2` principal block has determinant `1/3`, so
\[
\boxed{\|p_T\|_\infty\le\pi\sqrt3<5.442.}
\tag{5.5}
\]
Thus the singular triple is a failure of that reduction, not a singularity of the four-variable law.

At the pair failure `r=1`, every `2 x 2` principal block has a zero eigenvalue, but every `3 x 3` principal block has smallest singular value `1/2`, giving
\[
\boxed{\|p_T\|_\infty\le2(2\pi+3\sqrt3)<22.959.}
\tag{5.6}
\]

## 6. High-dimensional extension: arbitrary outside eigenvalues and couplings cost nothing

### Corollary 6.1 — `QFORM-FLAT-CORE-EXTENSION-v1`

Let `X_1,...,X_n` be independent with densities bounded by `1`. Suppose a four-element set of original coordinates `I` has principal block `A_{I,I}=B` of the form (3.1). No restriction is placed on

* the remaining principal block `A_{I^c,I^c}`;
* its eigenvalues, which may be arbitrarily small or large and of either sign;
* the cross block `A_{I,I^c}`.

Then
\[
\boxed{\|p_{X^TAX}\|_\infty\le C_*/\lambda<24.231.}
\tag{6.1}
\]

#### Proof

Condition on `X_{I^c}=w`. The four selected original coordinates retain independence and their density caps. The conditional polynomial is
\[
x_I^TBx_I+\ell(w)^Tx_I+c(w),
\]
with exactly the same quadratic block `B`. Theorem 5.1 is uniform in the linear tilt and constant, so every conditional output density has the same cap `C_*/\lambda`. Averaging those conditional densities preserves the cap. QED.

This is the correct way to control the extra quadratic remainder. It is **not** treated as an independent convolution after rotating the matrix. All dependence created by the outside variables is handled by conditioning in the original independent coordinates.

By Cauchy interlacing, the full matrix automatically has at least three eigenvalues of magnitude at least `\lambda`, because the displayed principal block has three equal eigenvalues `\epsilon\lambda`. Hence Corollary 6.1 is a genuine target-level subclass.

## 7. Quantitative consequence versus the current one-block theorem

The peer principal-triple theorem alone gives a bound proportional to
\[
{1\over |3r-1|}
\]
and therefore becomes useless at `r=1/3`. The present stitched theorem replaces that artificial blow-up by a uniform number below `24.231`, valid through the exact degeneracy and for every fourth eigenvalue `r`.

Conversely the definite-pair theorem alone blows up like `(1-r)^{-1/2}` as `r\uparrow1`; the triple branch removes that second artificial singularity.

Thus this run proves a concrete **additional-eigenvalue stability theorem**: in the flat one-mode four-coordinate family, adding an arbitrary fourth eigenvalue cannot destroy the universal density bound, even though it can make every principal triple singular at one parameter and every principal pair singular at another.

## 8. What this does and does not prove

**PROVED:** Theorems 5.1 and Corollary 6.1, conditional only on the cited peer pair/triple estimates whose proofs were read at their exact source and whose needed algebra was independently checked here.

**NOT PROVED:** the full arbitrary-eigenvector conjecture. A generic four-coordinate block with three large eigenvalues need not have the rank-one-flat form (3.1), and a delocalized high-dimensional large-eigenspace need not expose any fixed four-coordinate core of this shape.

**New remaining implication for B12:** replace the exact flat sign vector by a quantitatively nonflat unit vector, or more generally control a rank-one perturbation of `\epsilon\lambda I_4` uniformly in the perturbing eigenvalue using a finite collection of pair/triple minors. The present proof suggests looking for a covering principle in which zeros of one principal-minor family are quantitatively separated from zeros of another.

## 9. Source pins

* live control read before delivery: `yspennstate/math-research-brain@83f34aa729ecda8c9332539d5e91d054d9ffafae`, revision `2026-09-22.5`;
* consumed peer theorem: `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`;
* partner `account04/B12`: no current QFORM-compatible completed artifact was observed before this delivery; older FEI B12 artifacts were not reused after the owner target switch.

No novelty or publication-priority claim is made. Full QFORM conjecture remains **OPEN**.
