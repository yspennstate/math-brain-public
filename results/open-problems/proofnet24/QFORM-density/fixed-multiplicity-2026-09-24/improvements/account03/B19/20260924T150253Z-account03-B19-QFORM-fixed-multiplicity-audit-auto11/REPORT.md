# account03/B19 — independent nine-400 audit and a complete multiplicity-eight candidate

Run: `20260924T150253Z-account03-B19-QFORM-fixed-multiplicity-audit-auto11`

Objective followed: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, the later owner objective that supersedes older mathematical-focus instructions while preserving the QFORM target, privacy, quiet-delivery and task-identity controls.

Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Status

1. **Independent end-to-end audit of the active nine-eigenvalue / constant-400 paper: PASS after one local notation repair.** I read all 955 lines of the pinned source, not just theorem statements. The repair is the same harmless positive-tail/negative-tail coordinate-label issue independently identified by account03/B02: the negative hyperbolic tail should choose its own original coordinate `i_-`; since `|u|=|w|`, no estimate or constant changes.
2. **New mathematics:** the previously unresolved robust-pair terminal collar at multiplicity eight is contradictory. Combining this with the already-paid pivot branches gives a complete candidate theorem

\[
\boxed{
 s_8(A)\ge s>0
 \Longrightarrow
 \operatorname*{ess\,sup}_t p_{X^TAX+b^TX+c}(t)
 < 2510\,{K^2\over s}
}
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine terms, and arbitrary independent real coordinate laws with densities bounded by `K`.

This is a **new full fixed-multiplicity candidate**, not yet promoted to independently validated/release status. The owner requires two independent end-to-end reviews of a full candidate. The unrestricted three-eigenvalue conjecture remains OPEN. Global continuity at multiplicity eight is not claimed; the no-pivot branch below is continuous, but the pivot assembly is only used for essential boundedness.

---

# I. Source pins actually read

## Active nine-400 paper

- repository: `yspennstate/math-open-problems`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- package completion commit: `af592913ccfc4a87dfbf7c3a49bf2c5d4bbae359`

I read every source range `1--955`, plus the package handoff and author self-audit.

## Multiplicity-eight dependencies actually applied

### Robust two-anchor extraction

`yspennstate/math-open-problems@0408c579bcda638e72c010ff99892a22b9049796`

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B17/20260924T141823Z-account03-B17-fixedmult-auto11/ROBUST_TWO_ANCHOR.md`

In the normalized old-baseline no-`eta`-pivot chamber, with

\[
\eta=10^{-2},\qquad \kappa=80^{-2}=1/6400,
\]

if `s_8(A)>=1` and `V_3(A)<kappa^3`, it supplies a literal pair `H` such that, with `L=H^c`, `C=A[H,L]`,

\[
 g:=\det(CC^T)\ge d_0={\delta_*^2\over2},
\]

where

\[
\delta_*={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}.
\]

### Leverage-corrected completion identities

`yspennstate/math-open-problems@ec3774c580549a87abb70b0778e72dcb97706401`

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B09/20260924T144758Z-account01-B09-FIXMULT-auto11-r12/LOW_LEVERAGE_ROBUST_PAIR.md`

The exact anchored third-minor identity and leverage-corrected completion are used below. I extend that argument to the previously open case of exactly one high-leverage complement coordinate.

### Designated partner account04/B19

`yspennstate/math-open-problems@ec3774c580549a87abb70b0778e72dcb97706401`

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B19/20260924T151552Z-account04-B19-fixedmult-improvement-r1/REPORT.md`

The partner proves the sharpened quarter-power coefficient `C_q<3.99649` and, in the audited `eta=10^-2` pivot architecture, a scalar-pivot density bound `<2510`; the other relevant reviewed branches are below `2371`, `32`, and `251`. I apply that result to the actual `s_8` pivot sector after checking that the scalar branch needs fewer than eight surviving Schur directions.

### Independent threshold accounting

`yspennstate/math-open-problems@ec3774c580549a87abb70b0778e72dcb97706401`

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B12/20260924T144749Z-account01-B12-FIXMULT-auto11/NINE_REVIEW_AND_S8_TRANSVERSE_RESERVE.md`

This independently records that the scalar-pivot sector already closes under only `s_6(A)>=s`; hence the obstruction at multiplicity eight is entirely the no-pivot geometry. I also checked this directly in the branch tree: one scalar Schur loss from `s_8` leaves at least seven unit-scale directions, more than the five-direction half-potential receiver requires; any second scalar/pair pivot still leaves the one nonzero direction required by the logarithmic-potential step. A two-coordinate pivot loses at most two directions, so its indefinite remainder retains at least six.

---

# II. Independent audit of the active nine-400 paper

The verdict is **PASS after one local notation repair**. The following is my end-to-end map.

- **Lines 1--85:** theorem quantifiers, normalization, architecture — PASS. Scaling gives exactly `K^2/s`; no random rotation is used.
- **Lines 87--203:** Fourier identities, envelope integration, half-Riesz representation, rank perturbation and Schur spectral count — PASS, including the singular Schur regularization.
- **Lines 204--320:** diagonal dominance, geometric Brascamp--Lieb, product-projection density, scalar integrated Fourier powers and decoupling — PASS. Product structure is consumed before modulus is taken; no projected-coordinate independence is asserted.
- **Lines 321--396:** regularized determinant/crossing-volume theorem — PASS. The graph-frame BL constants reduce to `det(I+t^2M^TM/(pi^2 e^2))^{-1/8}`.
- **Lines 397--527:** grouped product-Fourier theorem and physical row promotion — PASS. Jensen is applied to mollified `L^2`; weighted Holder is over a finite measure; the row-Gram determinant and entropy terms have the displayed powers; promoted hubs are literal original coordinates.
- **Lines 528--662:** scalar square, definite/indefinite pair and quarter-power concentration — PASS after a notation repair in the hyperbolic negative tail. There choose a coordinate `i_-` with `|w_{i_-}|>=|w|/sqrt2`, rather than reusing the positive-tail symbol `i`; `|u|=|w|` keeps every cutoff and constant unchanged.
- **Lines 663--766:** volume sampling, nonsymmetric completion and no-pivot spectral-to-volume theorem — PASS. The global rank is `<=3r`, while the exterior `L x L` rank is `<=r`; the proof uses the correct restricted rank in the diagonal-dominance contradiction.
- **Lines 767--860:** full pair half potential, five-direction half potential, and the main `s_9 => 400 K^2/s` assembly — PASS. The indefinite pair is treated through a logarithmic envelope plus a non-atomic remainder, not through false post-rotation independence.
- **Lines 861--935:** spectral-tail/overlap theorem — PASS. Frobenius orthogonality of diagonal `D` and zero-diagonal `E` is exact; same-index bordered minors give the overlap term.
- **Lines 936--955:** threshold accounting and scope — PASS. The paper correctly leaves multiplicity eight and the unrestricted three-eigenvalue problem open.

The active paper proves essential boundedness at multiplicity nine. It does not prove a continuous representative in every pivot branch.

---

# III. New theorem: the multiplicity-eight terminal collar is empty

## Theorem `QFORM-S8-HIGHLEVERAGE-TERMINAL-CLOSURE-v1`

Work in the normalized old-baseline no-`eta`-pivot chamber with

\[
\eta={1\over100},\qquad \kappa={1\over6400},\qquad s_8(A)\ge1.
\]

Then

\[
\boxed{V_3(A)\ge\kappa^3.}
\]

Consequently the marginal-free order-three crossing receiver gives the full ambient quadratic form a continuous density with

\[
\boxed{\|p_Q\|_\infty<2400}
\]

in the no-pivot branch.

### Proof

Assume for contradiction that

\[
V_3(A)<\kappa^3.
\tag{3.1}
\]

The robust two-anchor theorem supplies a literal pair `H`, complement `L`, and

\[
C=A[H,L],\qquad G=CC^T,\qquad g=\det G\ge {\delta_*^2\over2}.
\tag{3.2}
\]

The elementary estimates `sqrt(2)<3/2` and `sqrt(202)<15` give

\[
\delta_*
>{97\over100}-{981\over8000}
={6779\over8000}>{4\over5},
\]

hence

\[
\boxed{g>{8\over25}.}
\tag{3.3}
\]

Normalize the anchor row space by

\[
Q_C=C^T(CC^T)^{-1}C,\qquad P=I_L-Q_C.
\]

Thus `Q_C` is a rank-two orthogonal projection. Put

\[
q_i=(Q_C)_{ii},\qquad p_i=P_{ii}=1-q_i.
\]

Since `tr Q_C=2`, at most two coordinates satisfy `q_i>2/3`.

### Step 1: two high-leverage coordinates are impossible

For `i<j`, Cauchy--Binet and the determinantal marginal identity give

\[
w_{ij}:={\det(C_{\{i,j\}})^2\over g},\qquad
\sum_{i<j}w_{ij}=1,\qquad
q_i=\sum_{j\ne i}w_{ij}.
\tag{3.4}
\]

If distinct `i,j` both have `q_i,q_j>2/3`, then

\[
w_{ij}\ge q_i+q_j-1>{1\over3},
\]

so by (3.3)

\[
\det(C_{\{i,j\}})^2>{g\over3}>{8\over75}.
\tag{3.5}
\]

But no `eta`-pivot implies, for all distinct physical coordinates,

\[
|A_{ab}|^2<\eta^2+\eta={101\over10000}.
\tag{3.6}
\]

Every entry of the literal `2 x 2` matrix `C_{\{i,j\}}` therefore has modulus less than `sqrt(101)/100`, and

\[
|\det C_{\{i,j\}}|
<2{101\over10000}={101\over5000}.
\]

Thus

\[
\det(C_{\{i,j\}})^2<{10201\over25000000}<{8\over75},
\]

contradicting (3.5). Therefore the high-leverage set

\[
E:=\{i:q_i>2/3\}
\]

has size `h=|E|<=1`.

### Step 2: leverage-corrected completion with one exceptional row

Let `D=A[L,L]`, and let `d_i` be row `i` of `D`. Put

\[
r_i=d_iP.
\]

For every light coordinate `i in L_0:=L\setminus E`, define the literal anchored disjoint third-minor mass

\[
W_i=
\sum_{\substack{T\subset L\setminus\{i\}\\|T|=3}}
\det A[H\cup\{i\},T]^2.
\]

The exact Gram/Cauchy--Binet identity from the low-leverage theorem is

\[
W_i=g\bigl(p_i\|r_i\|_2^2-r_{ii}^2\bigr).
\tag{3.7}
\]

For light `i`, `p_i>=1/3`. Define

\[
\lambda_i={r_{ii}\over p_i}\quad(i\in L_0),
\qquad \lambda_i=0\quad(i\in E),
\qquad \Lambda=\operatorname{diag}(\lambda_i).
\]

Let `M_0` be the diagonal mask of `L_0` and set

\[
E_0=M_0(D-\Lambda)P.
\tag{3.8}
\]

The exceptional row of `E_0` is zero. For every light `i`, orthogonal projection onto the line generated by `e_i^TP` gives

\[
(E_0)_{ii}=0,
\qquad
\|e_i^TE_0\|_2^2
={W_i\over gp_i}
\le {3W_i\over g}.
\tag{3.9}
\]

All terms in `W_i` are disjoint `3 x 3` minors, so

\[
\sum_{i\in L_0}W_i\le V_3(A).
\]

Hence, writing `epsilon=||E_0||_F`,

\[
\epsilon^2
\le {3V_3(A)\over g}
<{3\kappa^3\over g}
<{75\over8\,6400^3}
<10^{-6}.
\tag{3.10}
\]

Thus

\[
\boxed{\epsilon<10^{-3}.}
\tag{3.11}
\]

Extend `Lambda` by zeros on `H` and put

\[
D_0=0_H\oplus\Lambda,
\qquad
R=A-D_0-(0_H\oplus E_0).
\tag{3.12}
\]

For every light bottom row, the `L`-part of `R` is

\[
(d_i-\lambda_i e_i)Q_C,
\]

which lies in the two-dimensional row space of `C`. The two top `H` rows also lie in the direct sum of the two physical `H` directions and `row(C)`. The sole exceptional bottom row, if present, adds at most one more row-space direction. Therefore

\[
\boxed{\operatorname{rank}R\le4+h\le5.}
\tag{3.13}
\]

Moreover, restricting to the light indices,

\[
\boxed{\operatorname{rank}R[L_0,L_0]\le2,}
\tag{3.14}
\]

because its rows factor through `Q_C`.

### Step 3: the eighth singular direction contradicts restricted rank two

Since

\[
A-(0_H\oplus E_0)=D_0+R,
\]

Weyl gives

\[
s_8(D_0+R)>1-10^{-3}={999\over1000}.
\tag{3.15}
\]

A rank-`(4+h)` perturbation of the diagonal matrix `D_0` implies

\[
s_{8-(4+h)}(D_0)>{999\over1000}.
\tag{3.16}
\]

For `h=0`, this is `s_4(D_0)>999/1000`; for `h=1`, it is `s_3(D_0)>999/1000`. In either case there are at least three light coordinates `J_0` for which

\[
|\lambda_i|>{999\over1000}.
\tag{3.17}
\]

The error `E_0` has zero diagonal. Since the physical matrix has no scalar pivot,

\[
|A_{ii}|<{1\over100},
\]

so for `i in J_0`,

\[
|R_{ii}|
=|A_{ii}-\lambda_i|
>{989\over1000}.
\tag{3.18}
\]

Also (3.6) and `sqrt(101)<11` give

\[
|A_{ij}|<{11\over100}\qquad(i\ne j).
\]

For distinct `i,j in J_0`,

\[
|R_{ij}|=|A_{ij}-(E_0)_{ij}|
<{11\over100}+{1\over1000}
={111\over1000}.
\tag{3.19}
\]

Thus each row of the `3 x 3` matrix `R[J_0,J_0]` has diagonal magnitude greater than `989/1000`, while the sum of its two off-diagonal magnitudes is less than

\[
{222\over1000}<{989\over1000}.
\]

Strict row diagonal dominance makes `R[J_0,J_0]` invertible. This contradicts (3.14), which says its rank is at most two.

The contradiction proves `V_3(A)>=kappa^3`.

### Step 4: pay the no-pivot branch analytically

The fair original-coordinate cut identity gives a literal cross block `M=A[I,J]` with

\[
Z_3(M)\ge {V_3(A)\over64}\ge {\kappa^3\over64}.
\]

The completed marginal-free order-three receiver has constant `C_3<15`, so

\[
\|p_Q\|_\infty
\le C_3 Z_3(M)^{-1/6}
<15\left({\kappa^3\over64}\right)^{-1/6}
=30\kappa^{-1/2}
=2400.
\]

Its characteristic-function majorant has exponent `3/2`, so this no-pivot branch has a continuous `C_0` density. QED.

---

# IV. Full multiplicity-eight assembly

Normalize first to coordinate density caps one and `s_8(A)>=1`, and classify pivots with the same audited old-baseline threshold `eta=10^-2` used by the robust-anchor theorem and the designated partner's `2510` ledger.

1. **No pivot.** The theorem above gives `||p_Q||_infinity<2400` and a continuous `C_0` representative.
2. **Scalar pivot.** A one-coordinate Schur complement loses at most one unit-scale spectral direction, hence retains at least seven. The audited scalar branch needs at most five directions in its no-child-pivot half-potential branch; if a child pivot occurs, the remaining logarithmic-potential argument requires only a nonzero spectral direction. The designated `account04/B19` exact certificate therefore applies without change and gives
   \[
   \|p_Q\|_\infty<2510.
   \]
3. **Definite two-coordinate pivot.** The direct coarea bound is far below `2510` and needs no remainder spectral hypothesis.
4. **Indefinite two-coordinate pivot.** Its Schur remainder retains at least six unit-scale directions. The audited hyperbolic/logarithmic-potential branch needs only one, and the designated partner ledger is below `251`.

Therefore

\[
\boxed{
 s_8(A)\ge1
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}<2510.
}
\tag{4.1}
\]

For general density cap `K>0` and `s_8(A)>=s>0`, put `Y=KX` and scale the quadratic coefficient matrix by `1/s`, exactly as in the active manuscript. Scalar output scaling yields

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}<2510\,{K^2\over s}.
}
\tag{4.2}
\]

No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, sign restriction, exact-rank assumption, or post-rotation independence is used. All affine terms and all extra spectrum are retained.

## Continuity status

- no-pivot `s_8` branch: continuous `C_0` density;
- full `s_8` theorem assembled above: **essential bounded density proved by this candidate; global continuity not yet proved**.

## Review status

This report is the authoring/reconstruction proof of the new `s_8` candidate. It has **not** yet received the two independent end-to-end reviews required by the owner for a full candidate. Do not mark multiplicity eight as independently validated or released solely from this report.

The unrestricted three-eigenvalue theorem remains OPEN / NOT PROVED / NOT DISPROVED.

---

# V. Designated partner result applied to an actual inequality

The `account04/B19` certificate `C_q<3.99649` also sharpens the active nine-400 paper's quarter-power/logarithmic potential directly. Replacing the active paper's coarse constant five by `C_q<4` gives

\[
L_0<4+4\log4=4+8\log2<{48\over5},
\]

using `log2<7/10`. In the active paper's `d=3/40`, `p=1/400` ledger this changes the scalar/scalar branch to

\[
 d^{-1/2}+{J_0+2L_0\over d}<351
\]

and the indefinite-pair branch to

\[
20(6+\log16+L_0)+1/e<369.
\]

The active no-pivot branch has the exact coefficient

\[
25C_3,\qquad C_3^6=26244e^6.
\]

The elementary series estimate

\[
e< {163\over60}+{7\over4320}< {68\over25}
\]

and direct integer arithmetic show `25C_3<371`. Hence the same active nine-eigenvalue proof can be sharpened from `400` to

\[
\boxed{\|p_Q\|_\infty<371 K^2/s}
\]

without changing any hypothesis. This is secondary to the threshold-eight closure above, but it is an actual numerical application of the designated partner's completed result.

---

# VI. Remaining target

The fixed-multiplicity frontier is now, subject to independent review of Section III--IV, `8 -> 7`; the owner’s unrestricted target remains multiplicity three. The next exact mathematical obligation is to independently audit the high-leverage terminal closure above and, if it passes, attack multiplicity seven without weakening the product-law quantifiers.
