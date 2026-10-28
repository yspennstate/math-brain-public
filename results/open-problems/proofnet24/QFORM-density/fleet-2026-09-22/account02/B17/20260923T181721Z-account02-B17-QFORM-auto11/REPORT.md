SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T18:17:21Z.
attacking: irrational cone-aligned remote fragmentation in the exact dense Householder witness; prove whether finitely many genuinely null remote cells can create a sharp-constant overshoot.

# QFORM B17 — irrational null-cone fragmentation is transverse, not resonant

Run: `20260923T181721Z-account02-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC WITNESS CONSTRAINT; FULL QFORM OPEN**  
Continuity: not claimed for the full target.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN / NOT PROVED / NOT DISPROVED.  This report concerns one exact six-variable target matrix and a broad fixed-finite fragmented source class.  It assumes no moments, support bound, log-concavity or connected support in the full conjecture.  Log-concavity appears only as an explicit property of one particular triangular control density in Section 6.  No independence after spectral rotation is asserted.


## 1. Exact source-valid Householder matrix

Put

\[
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.1}
\]

Then `B^2=I`, `tr B=1`, and `det B=-1`, so

\[
\operatorname{spec}(B)=\{1,1,-1\}.
\tag{1.2}
\]

Let `C` be the `6 x 3` synthesis matrix with two rows `e_j/sqrt(2)` for each `j=1,2,3`.  Thus `C^T C=I_3`.  The physical matrix

\[
A=CBC^T
\tag{1.3}
\]

has exact nonzero spectrum

\[
\boxed{\{1,1,-1\}}
\tag{1.4}
\]

for every choice of the six independent input laws below.  Writing

\[
S_j={X_{j,1}+X_{j,2}\over\sqrt2},
\qquad S=(S_1,S_2,S_3),
\]

the physical quadratic form is exactly

\[
Q=S^TBS.
\tag{1.5}
\]

No spectral rotation is used to create independence: the only independent objects are the six original physical coordinates.

## 2. Latest designated-partner result and the unpaid experiment

The latest compatible `account03/B17` result used here is

`yspennstate/math-open-problems@0335944c2b08a13b9094368494320c8780940785`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T180123Z-account03-B17-QFORM-auto11/REPORT.md`.

For (1.1), it proves the arithmetic lemma that the null cone

\[
q(d):=d^TBd=0
\tag{2.1}
\]

has no nonzero rational point.  Therefore fixed finite *rational* remote cells are eventually separated from the cone unless their bank center is exactly zero.  It also proves pointwise domination for matched zero-center fragments and identifies the next sharp experiment explicitly: use **irrational centers tuned exactly to the real null cone**.

That is the experiment settled below.  The new mechanism is different: a cone-aligned remote cell is not separated from `q=0`, but its gradient is of order `R`, so its entire output density is `O(1/R)`.

The partner's connected six-variable control has the exact cone-tip value

\[
p_*(0)=4.06307061680603726012548442259349995675\ldots
<3\sqrt2,
\tag{2.2}
\]

with exact radical/log formula reproduced by `CHECK.py` from the completed source.

## 3. General nonzero remote cell: a global `O(1/R)` density bound

Consider a product fragment cell in which, after the three pair sums, the bank center is `R d`, `d in R^3`, and write the bank coordinate as

\[
S=Rd+u.
\]

Every physical fragment has length at most one.  Therefore each bank deviation lies in an interval of half-width at most `1/sqrt(2)`, so

\[
|u_j|\le {1\over\sqrt2},
\qquad
\|u\|_2\le L:=\sqrt{3/2}.
\tag{3.1}
\]

For a selected pair of physical intervals, each of unit density, the corresponding bank subdensity is a scaled interval convolution.  Its height is at most `sqrt(2)`.  Hence the three-bank subdensity `g_cell` obeys

\[
0\le g_{\rm cell}\le(\sqrt2)^3=2\sqrt2,
\tag{3.2}
\]

and the projection of its support onto any two bank coordinates has area at most

\[
(\sqrt2)^2=2.
\tag{3.3}
\]

Assume `d != 0`.  Since `B` is orthogonal, some coordinate `k` satisfies

\[
|(Bd)_k|\ge {\|d\|\over\sqrt3}.
\tag{3.4}
\]

If

\[
R\|d\|\ge3\sqrt2,
\tag{3.5}
\]

then (3.1) gives throughout the whole cell

\[
|R(Bd)_k+(Bu)_k|
\ge {R\|d\|\over\sqrt3}-L
\ge {R\|d\|\over2\sqrt3}.
\tag{3.6}
\]

For `q(y)=y^TBy`,

\[
|\partial_{u_k}q(Rd+u)|
=2|R(Bd)_k+(Bu)_k|
\ge {R\|d\|\over\sqrt3}.
\tag{3.7}
\]

The derivative has one fixed sign on the cell.  Thus for each fixed pair of the other bank coordinates the equation `q(Rd+u)=s` has at most one root in `u_k`.  One-dimensional coarea, (3.2), (3.3) and (3.7) give, **uniformly over every output level `s`**,

\[
\boxed{
\|p_{\rm cell}\|_\infty
\le {4\sqrt6\over R\|d\|}.
}
\tag{3.8}
\]

The crucial point is that (3.8) contains no factor `q(d)`.  It remains valid when

\[
q(d)=0
\tag{3.9}
\]

exactly.  Irrational null alignment cancels the `R^2 q(d)` displacement but cannot cancel the transverse derivative `2RBd`, because `B` is invertible.

For any **fixed finite** fragmentation plan, let `D` be its finite multiset of nonzero bank-center vectors.  Once (3.5) holds for all of them,

\[
\boxed{
\sup_s p_{\ne0,R}(s)
\le {C_{\mathcal F}\over R},
\qquad
C_{\mathcal F}:=4\sqrt6\sum_{d\in D}{1\over\|d\|}<\infty.
}
\tag{3.10}
\]

This is the first unpaid implication: fixed finite irrational cone-aligned cells are globally small, not resonant.

## 4. Explicit irrational null-cone translated cube

There is a particularly clean exact candidate which defeats the partner's rational-separation premise but is paid by (3.8).  Set

\[
d_0=(1,1,4-3\sqrt2)^T.
\tag{4.1}
\]

Direct exact arithmetic gives

\[
q(d_0)=0,
\qquad
Bd_0=(-3+2\sqrt2,-3+2\sqrt2,-\sqrt2)^T.
\tag{4.2}
\]

For bank `j`, take

\[
X_{j,1}\sim \operatorname{Unif}
[\sqrt2 R(d_0)_j-1/2,\sqrt2 R(d_0)_j+1/2],
\qquad
X_{j,2}\sim\operatorname{Unif}[-1/2,1/2],
\tag{4.3}
\]

all six variables independent.  Every physical density is exactly one on a unit interval, so this satisfies the source cap with no moment or support assumption imported into the theorem.  Its bank vector is `S=R d_0+u`, where `u` has the product triangular density and support (3.1).

Use the third coordinate in (4.2).  On the entire support,

\[
|\partial_{u_3}q(Rd_0+u)|
\ge2\left(R\sqrt2-\sqrt{3/2}\right).
\tag{4.4}
\]

Combining the same height/projection bounds gives the sharper global estimate

\[
\boxed{
\|p_{Q_R}\|_\infty
\le {2\over R-\sqrt3/2},
\qquad R>\sqrt3/2.
}
\tag{4.5}
\]

In particular, for every `R>=2`,

\[
\|p_{Q_R}\|_\infty<2<3\sqrt2.
\tag{4.6}
\]

So the most literal irrational null-cone teleportation attack does the opposite of creating a sharp witness: its entire density decays like `2/R`.

## 5. Zero-center cells are dominated by the connected triangular source

Now take a fixed finite fragmented law in each physical coordinate of the form

\[
f_{j,a,R}=\mathbf 1_{\cup_k I_{j,a,k}(R)},
\qquad
|I_{j,a,k}(R)|=\ell_{j,a,k},
\qquad
\sum_k\ell_{j,a,k}=1,
\tag{5.1}
\]

where the interval centers are `R c_{j,a,k}` with fixed real numbers `c_{j,a,k}`.  Assume the interval representation is reduced (distinct fixed centers in a given marginal); for all sufficiently large `R` the pieces are disjoint.  This includes arbitrary irrational fixed center ratios.

A zero-center bank cell pairs a fragment centered at `Rc` in the first physical coordinate with one centered at `-Rc` in the second.  If their lengths are `a,b`, the unscaled centered-sum overlap kernel is

\[
k_{a,b}(t)=
\left|[-a/2,a/2]\cap[t-b/2,t+b/2]\right|.
\tag{5.2}
\]

Writing `D=(a+b)/2`, elementary interval geometry gives

\[
k_{a,b}(t)\le(D-|t|)_+.
\tag{5.3}
\]

Because each physical marginal has total fragment length one, the matched pairs in one bank satisfy

\[
\sum_i D_i={1\over2}\sum_i(a_i+b_i)\le1.
\tag{5.4}
\]

For `t>=0`, if the active set `{i:D_i>t}` is nonempty,

\[
\sum_i(D_i-t)_+
=\sum_{i:D_i>t}D_i-\#\{i:D_i>t\}\,t
\le1-t;
\tag{5.5}
\]

otherwise the left side is zero.  Therefore the total zero-center bank subdensity satisfies

\[
\boxed{
h_{j,0}(s)
\le \sqrt2(1-\sqrt2|s|)_+
=:h_*(s).
}
\tag{5.6}
\]

The three banks use disjoint original coordinates, so the complete zero-center joint subdensity factorizes and is pointwise bounded by

\[
g_*(s_1,s_2,s_3)=\prod_{j=1}^3 h_*(s_j).
\tag{5.7}
\]

Consequently the pushforward measures satisfy domination for every Borel set, and hence their densities satisfy

\[
\boxed{
p_{0,R}(s)\le p_*(s)\quad\text{for a.e. }s.}
\tag{5.8}
\]

Combining (3.10) and (5.8), for every fixed finite fragmentation plan,

\[
\boxed{
\|p_R\|_\infty
\le \|p_*\|_\infty+{C_{\mathcal F}\over R}
}
\tag{5.9}
\]

whenever `R` is large enough for all nonzero-center cell estimates.  Thus **finite remote fragmentation cannot create a new order-one global peak beyond the connected base witness**.  Any remaining global sharp-constant issue in this architecture is inherited from the base two-sheet profile, not created by remote irrational cells.

This does not cover fragment count growing with `R`, center vectors `d=d_R` tending to zero fast enough to defeat (3.10), or arbitrary non-indicator rough laws.  Those scopes are intentionally left open.

## 6. Required pinned-source application: the entire one-sheet side is maximized at the cone tip

This section applies an actual completed result from the required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its proved Theorem C gives an **exact ruled-surface identity** for signature `(1,1,-1)` on the majority-sign side.  In the unit-eigenvalue case, after diagonalizing `B` orthogonally and denoting the resulting three-dimensional joint density by `rho`, for `s>=0`

\[
p_*(s)={\pi\over\sqrt2}
\operatorname{avg}_{\theta}
\rho_\theta(\sqrt{s}\,e_\theta),
\tag{6.1}
\]

where every `rho_theta` is the relevant two-dimensional marginal density of `rho`.  The same identity at `s=0` evaluates the marginals at the origin.  This uses the joint rotated density directly; it does **not** assert that rotated coordinates are independent.

For the specific connected control (5.7), `h_*` is even and log-concave.  Hence `g_*` is centrally symmetric and log-concave.  Orthogonal rotation preserves both properties, and Prékopa's theorem makes every two-dimensional marginal `rho_theta` centrally symmetric and log-concave.  Therefore

\[
\rho_\theta(z)\le\rho_\theta(0)
\tag{6.2}
\]

for every `z`: indeed log-concavity and central symmetry give
`rho_theta(0)>=sqrt(rho_theta(z)rho_theta(-z))=rho_theta(z)`.

Applying (6.2) inside the exact ruled identity (6.1) gives the real inequality

\[
\boxed{
p_*(s)\le p_*(0),\qquad s\ge0.}
\tag{6.3}
\]

This sharpens the generic Theorem-C estimate `p(s)<=pi sqrt(2)` for this actual witness.  Using the completed partner value (2.2),

\[
\boxed{
\sup_{s\ge0}p_*(s)=p_*(0)
=4.063070616806037\ldots<3\sqrt2.
}
\tag{6.4}
\]

Now (3.10), (5.8), and (6.4) imply

\[
\boxed{
\sup_{s\ge0}p_R(s)
\le p_*(0)+{C_{\mathcal F}\over R}.
}
\tag{6.5}
\]

Since

\[
3\sqrt2-p_*(0)
=0.17957007031324788627958\ldots>0,
\tag{6.6}
\]

every fixed finite real-center fragmentation plan — rational, irrational, or exactly cone-aligned — has its **entire positive one-sheet half-line strictly below `3sqrt(2)` for all sufficiently large `R`**.

This is where the required pinned source is used at an actual obstruction: Theorem C plus the explicit log-concavity of this control turns the generic one-sheet ruling into the global positive-side mode theorem (6.3).  The generic constant `pi sqrt(2)>3sqrt(2)` alone would not prove this sharp-constant exclusion; that is a limitation of that proof constant, not a counterexample to QFORM.

## 7. What is now excluded and what remains unpaid

The latest partner report showed that rational remote cells cannot hit the Householder null cone except at the origin and proposed irrational null alignment as the next dangerous finite-fragment construction.  Sections 3-6 close that mechanism:

- an arbitrary fixed nonzero remote cell, even with `q(d)=0`, contributes only `O(1/R)` **globally in the output level**;
- the explicit irrational null direction `d_0=(1,1,4-3sqrt(2))` gives a source-valid translated-cube family with the global bound (4.5), already `<2` for `R>=2`;
- all zero-center cells of a fixed finite unit-height fragmentation are pointwise dominated by the connected triangular source;
- the connected source has its entire majority-sign / one-sheet side maximized at zero, below `3sqrt(2)`.

Therefore no fixed finite real-center fragmentation of this six-variable dense Householder architecture can manufacture a new asymptotic positive-side sharp witness.  Globally, fragmentation can add only `O(1/R)` to the base connected profile.

The first genuinely unpaid implication in this architecture is now the **minority-sign / two-sheet side of the connected base profile**:

\[
\boxed{
\sup_{s<0}p_*(s)\stackrel{?}{\le}3\sqrt2
\quad\text{(or preferably }\le p_*(0)\text{).}
}
\tag{7.1}
\]

The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is respected: a line-X-ray bound by itself cannot prove (7.1).  Beyond fixed finite fragmentation, growing fragment count, center scales depending on `R`, and genuinely multiscale rough laws remain possible stress mechanisms.

A future density above `3sqrt(2)` in any valid family would refute that **candidate sharp constant** only.  It would not by itself refute the existence of some larger universal QFORM bound.  No such example is produced here.

## 8. Verification and source integrity

`CHECK.py` verifies exactly `B^2=I`, `tr B=1`, `det B=-1`, the irrational null identity `q(d_0)=0`, the exact vector `Bd_0`, the explicit translated-cube bound at `R=2`, and the partner's exact cone-tip formula/gap.  `CHECK_OUTPUT.txt` records the executed output.  The early gradient calculation was saved before this report as `EARLY_CALC.md`.

Only this worker-owned run directory is changed in math-open-problems.  No unrelated data, credentials, permissions, public release action, account crossing, task creation or scheduler mutation is involved.
