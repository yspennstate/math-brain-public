# B17 — quantitative plaquette factorization stability and a spectral-product Hellinger bridge

**Status:** PARTIAL / PROVED_AUXILIARY_BRIDGE. **Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used.  
**Route:** APPROACH 7/14 with an input-side Boolean interaction reformulation: approximate multiplicative composition + coding/point-process comparison.  
**Publication priority:** UNVERIFIED; no novelty claim.

## 0. Method change and named cross-account result consumed

The preceding fleet01/B17 run killed the maximum-influence specialization of the dimension-cooling selector and replaced it by a local derivative-depth inequality. This run does **not** optimize that same selector or sum raw derivative depth again. It changes category to approximate multiplicative factorization across physical coordinate cuts.

The named other-account result used substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260921T204329Z-interaction-companion-factorization/REPORT.md`

as read at scientific master `5969da93a73d060992e0710850c569479afc9ffd`, Git blob `67abacfe5dba4cc84722d12c6b505e9f88304090`.

That report proves that the Boolean plaquette defect

\[
p_{ij}:=\Pr\big[f(x)f(x\oplus e_i)f(x\oplus e_j)f(x\oplus e_i\oplus e_j)=-1\big]
\tag{0.1}
\]

is the exact support-interaction weight, and that zero cross-plaquette interaction is equivalent to exact disjoint multiplicative factorization (up to affine/character factors). It also connects these weights to a sparse interaction skeleton and the companion-flow code. The present run turns its **zero-cut** statement into a quantitative approximate-factorization theorem and then transports that approximation to the spectral-sample law.

A second compatible result used for interpretation is fleet02/B14's crossing-information selector report

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T210915Z-crossing-information-selector/REPORT.md`, blob `673dbf5d2bc162fc43b7931e88a5449fce2a219a`,

which shows that logarithmic rarity of a pivotality event must be paid by physical information/influence. The singleton theorem below recovers the same Shannon scale directly from plaquette interaction and identifies it with approximate multiplicative factorization error.

## 1. Quantitative cut setup

Partition the physical coordinates into two disjoint blocks `A` and `B`. For Boolean

\[
f:\{0,1\}^{A\sqcup B}\to\{-1,+1\},
\]

define the distance to a rank-one multiplicative sign table across the cut by

\[
\delta_{A\mid B}(f)
:=\min_{g:\{0,1\}^A\to\{\pm1\},\;h:\{0,1\}^B\to\{\pm1\}}
\Pr[f(X,Y)\ne g(X)h(Y)].
\tag{1.1}
\]

Put

\[
W_{A\mid B}(f):=\sum_{i\in A}\sum_{j\in B}p_{ij}.
\tag{1.2}
\]

Fleet02/B17 gives the exact endpoint `W=0 => delta=0`. The first theorem gives a dimension-free quantitative stability bound with no Fourier assumptions beyond Booleanity.

## 2. PROVED: arbitrary cut interaction controls distance to a product sign table

### Theorem 2.1 — anchored rectangle factorization

For every Boolean `f` and every coordinate cut `A|B`,

\[
\boxed{\delta_{A\mid B}(f)\le \frac14 W_{A\mid B}(f).}
\tag{2.1}
\]

Equivalently,

\[
\boxed{4\delta_{A\mid B}(f)\le\sum_{i\in A,j\in B}p_{ij}.}
\tag{2.2}
\]

### Proof

Write `f(x,y)=(-1)^{P(x,y)}` with `P` taking values in `F_2`. Let independent uniform anchors `(X',Y')` be given. Define

\[
g_{X',Y'}(x):=f(x,Y'),\qquad
h_{X',Y'}(y):=f(X',y)f(X',Y').
\tag{2.3}
\]

Then

\[
f(x,y)\ne g_{X',Y'}(x)h_{X',Y'}(y)
\]

if and only if the rectangle phase

\[
R=P(x,y)+P(X',y)+P(x,Y')+P(X',Y')\pmod2
\tag{2.4}
\]

is one.

Fix an order on the coordinates of `A` and `B`. Repeated discrete differentiation gives an exact telescoping identity for the rectangle phase:

\[
R=\bigoplus_{\substack{i\in A:\,x_i\ne X'_i\\ j\in B:\,y_j\ne Y'_j}}
(\Delta_i\Delta_jP)(Z_{ij}),
\tag{2.5}
\]

where each `Z_{ij}` is a corner determined by the endpoint pair and the chosen orders. Therefore, pointwise,

\[
\mathbf 1_{\{R=1\}}
\le
\sum_{i,j}
\mathbf 1_{\{x_i\ne X'_i\}}
\mathbf 1_{\{y_j\ne Y'_j\}}
\mathbf 1_{\{(\Delta_i\Delta_jP)(Z_{ij})=1\}}.
\tag{2.6}
\]

For every fixed pair `(i,j)`, independent uniform endpoints disagree in those two coordinates with probability `1/4`; conditional on that event, the corner `Z_{ij}` is uniform on the cube. Hence averaging (2.6) gives

\[
\Pr[R=1]\le\frac14\sum_{i\in A,j\in B}p_{ij}
=\frac14W_{A\mid B}.
\tag{2.7}
\]

The left side is the average, over anchors `(X',Y')`, of the Hamming error of the product candidate (2.3). Some anchor has error at most that average, proving (2.1). QED.

The theorem is sharp already on a `1+1` cut: changing one entry of a rank-one `2x2` sign table gives `delta=1/4` and `W=1`.

## 3. PROVED: low physical cross-interaction gives a nearby product spectral law

Let `g,h` attain (or merely satisfy) the bound in Theorem 2.1 and write

\[
a_S=\widehat f(S),\qquad
b_S=\widehat{(gh)}(S)
=\widehat g(S\cap A)\widehat h(S\cap B).
\]

Let

\[
\mu_f(S)=a_S^2,
\qquad
\nu_{g,h}(S)=b_S^2.
\]

The second law is an actual **product spectral-sample law** across `A|B`.

### Corollary 3.1 — spectral Hellinger bridge

With the convention

\[
\mathsf H^2(\mu,\nu):=
\sum_S(\sqrt{\mu(S)}-\sqrt{\nu(S)})^2,
\tag{3.1}
\]

one has

\[
\boxed{
\mathsf H^2(\mu_f,\nu_{g,h})
\le 4\delta_{A\mid B}(f)
\le W_{A\mid B}(f).
}
\tag{3.2}
\]

### Proof

Normalized Parseval gives

\[
\sum_S(a_S-b_S)^2
=\mathbb E(f-gh)^2
=4\Pr[f\ne gh].
\tag{3.3}
\]

Since `||u|-|v||<=|u-v|`,

\[
\mathsf H^2(\mu_f,\nu_{g,h})
=\sum_S(|a_S|-|b_S|)^2
\le\sum_S(a_S-b_S)^2.
\]

Apply Theorem 2.1. QED.

This is the new coding/point-process interface: **small physical plaquette interaction across a cut forces the actual spectral sample to be Hellinger-close to a product random set across that cut.** It upgrades the exact factorization detector of fleet02/B17 to a stable spectral statement.

A generic entropy-continuity inequality cannot finish FEI from (3.2), because it introduces `log |supp|`, hence an ambient-dimension loss. The next bridge must use Boolean/product structure, the companion/factorial negative credits, or a recursively nonreusing cut code rather than generic finite-alphabet continuity.

## 4. PROVED: singleton cuts have the correct logarithmic stability scale

Take a single coordinate `i` and write the two physical rows as `f_0(y),f_1(y)`. Put

\[
q_i=\operatorname{Inf}_i(f)
=\Pr[f_0(Y)\ne f_1(Y)],
\qquad
j_i=\min(q_i,1-q_i).
\tag{4.1}
\]

Let

\[
P_i:=\sum_{k\ne i}p_{ik}.
\tag{4.2}
\]

### Proposition 4.1 — exact singleton product distance

\[
\boxed{
\delta_{\{i\}\mid-i}(f)=\frac12j_i.
}
\tag{4.3}
\]

### Proof

A product sign table across this cut imposes one fixed relation `f_1=cf_0`, with `c=+1` or `-1`. For a given `y`, when the actual relation disagrees with `c`, at least one of the two entries must be changed, and changing one suffices. Thus the optimum error is one half of the smaller of the agreement and disagreement probabilities, namely `j_i/2`. QED.

Now let

\[
\eta_i(y):=\mathbf1_{\{f_0(y)\ne f_1(y)\}}.
\]

For every `k!=i`, the plaquette is defective exactly when `eta_i` changes in direction `k`, so

\[
p_{ik}=\operatorname{Inf}_k(\eta_i).
\tag{4.4}
\]

If `q_i>1/2`, replace `eta_i` by its complement; the transverse influences are unchanged and its density becomes `j_i<=1/2`. Cube edge-isoperimetry therefore gives

\[
\boxed{
P_i\ge2j_i\log_2\frac1{j_i}.
}
\tag{4.5}
\]

Combining with (4.3),

\[
\boxed{
P_i
\ge4\delta_i\log_2\frac1{2\delta_i},
\qquad \delta_i:=\delta_{\{i\}\mid-i}(f).
}
\tag{4.6}
\]

Thus a rare failure of multiplicative independence has a **logarithmic** plaquette price, not merely the linear price supplied by Theorem 2.1.

A Shannon corollary is

\[
\boxed{
h_2(j_i)
\le \frac12P_i+(\log_2 e)j_i.}
\tag{4.7}
\]

Indeed `h_2(j)<=j log_2(1/j)+(log_2 e)j`, then use (4.5). The one-point sensitivity support saturates the logarithmic term in (4.5), so this is on the same sharp rare-event scale as the preceding B17 bent-flip obstruction and fleet02/B14's crossing-information theorem, but now the cost is carried by the **physical multiplicative-interaction graph** used in the factor-first composition route.

## 5. A stronger all-cut logarithmic inequality survives every exact small case tested, but is OPEN

The singleton result suggests the following natural quantitative strengthening of (2.2):

\[
\boxed{\textbf{OPEN CUT CONJECTURE:}\qquad
W_{A\mid B}(f)
\stackrel{?}{\ge}
2\delta_{A\mid B}(f)\log_2\frac1{\delta_{A\mid B}(f)}.}
\tag{5.1}
\]

This is **not** claimed proved. It would be a projective/rank-one analogue of cube edge-isoperimetry for Boolean sign matrices.

The deterministic checker exhaustively tested every Boolean sign table on cuts `1+1`, `1+2`, and `2+2`, i.e. `65,808` functions total. It found:

- zero violations of the proved exact inequality `4 delta <= W`;
- zero violations of the proved singleton logarithmic inequality;
- zero finite violations of (5.1);
- minimum observed ratio
  \[
  \frac{W}{\delta\log_2(1/\delta)}=2
  \]
  in every tested partition, attained at `delta=1/4, W=1`.

The last bullet is finite evidence only. No extrapolation to arbitrary dimension is made.

Checker SHA-256: `bbff0dbd45a351980cccfde43f5d1f9e447b308d2000abf11689de66fdce10c4`.  
Captured output SHA-256: `0370a5d49e726543c10ad7af4092108c72a0f55703a9e58e036008d0c337fefb`.

## 6. What this changes for the full FEI programme

Before this run, the factor-first route had only an exact statement: zero plaquette cross-interaction gives an exact multiplicative component split. That is too brittle for an adaptive proof because a hard primitive core need not have an exactly zero cut.

After this run there is a stable replacement:

\[
W_{A\mid B}\ll1
\quad\Longrightarrow\quad
f\text{ is Hamming-close to }g(A)h(B)
\quad\Longrightarrow\quad
\widehat f^2\text{ is Hellinger-close to a product spectral law},
\tag{6.1}
\]

with the same dimension-free physical budget `W` and explicit constants. For singleton cuts, the stability improves to the correct rare-event logarithmic scale and directly pays `h_2(j_i)` through (4.7).

This does **not** prove full FEI. The key unpaid arrow is now more concrete and belongs to Approaches 7/14:

> Convert spectral Hellinger closeness to a product law, together with the already available companion/factorial negative credits, into a **dimension-free nonreusing entropy code**, or prove the all-cut logarithmic inequality (5.1) and combine it with a recursively paid cut decomposition.

Generic Shannon continuity is not sufficient because of its alphabet-size factor. Likewise, summing all plaquette degrees is not allowed: the all-pairs interaction bank can have second-order congestion. A successful continuation must either select cuts nonreusably, retain the fleet01/B12 companion flow, or build an explicit Boolean counterfamily to (5.1).

## 7. Claim ledger

- `B17-PLAQUETTE-CUT-STABILITY-01`: `delta_{A|B} <= W_{A|B}/4` for every Boolean function and every coordinate cut. **PROVED**.
- `B17-SPECTRAL-PRODUCT-HELLINGER-02`: there is a product spectral law across the cut with squared-root distance at most `W_{A|B}`. **PROVED**.
- `B17-SINGLETON-EXACT-DISTANCE-03`: `delta_i=j_i/2`. **PROVED**.
- `B17-SINGLETON-LOG-INTERACTION-04`: `P_i>=2 j_i log_2(1/j_i)` and hence `h_2(j_i)<=P_i/2+(log_2 e)j_i`. **PROVED**.
- `B17-ALL-CUT-LOG-CONJECTURE-05`: `W>=2 delta log_2(1/delta)` for arbitrary cuts. **OPEN; finite evidence only through 2+2**.
- Full FEI. **OPEN / NOT PROVED**.

## 8. Exact next obligation

First try to prove or refute (5.1) by treating Boolean sign tables modulo row/column sign flips as a quotient cube and deriving an edge-isoperimetric inequality for distance to the rank-one code. If it fails, preserve the smallest exact counterexample and immediately pivot to the already proved Hellinger bridge (3.2): combine a low-interaction cut with the one-companion/factorial code so that the entropy defect from replacing `mu_f` by the nearby product law is paid by an actual nonreused companion-flow quantity rather than `log |supp|`.
