Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — certificate-valued quadratic-core max-splicing and a direct character-child decrement

## 0. Parent status and exact movement

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No restricted theorem below is promoted to full FEI.

**New mechanism-level movement.** The preceding P03 report reduced arbitrary quadratic coupling between disjoint high-degree ANF components using the quadratic-normalized Wiener norm `Lambda_2`, but its quantitative leaf certificate still depended on the residual Wiener parameter. This run removes that dependence from the recombination step itself:

1. a **certificate-valued quadratic product max-splicing theorem** shows that arbitrary quadratic coupling among disjoint cores preserves the worst hereditary core constant up to a universal floor `2`, and preserves the worst direct FEI core constant up to a universal floor `4`;
2. the theorem is parameter-free: the cores may be certified by any mechanism, not necessarily Wiener norm;
3. a new exact **character-child full entropy decrement formula** gives the clean local estimate
   \[
   H(f)-\frac{H(f^+)+H(f^-)}2\le5\,j_i(f)
   \]
   whenever one child is a signed character;
4. combining the new max-splicing theorem with P03's arbitrary-child allocation theorem gives an all-dimensional restricted class: an arbitrary quadratic twist of a product of arbitrarily many disjoint nested-canalizing cores satisfies
   \[
   R_{\mathcal T}(f)\le3I(f),
   \qquad
   H(\widehat f^{\,2})\le C_* I(f),
   \]
   where
   \[
   C_*:=2+\frac1{\sqrt e\ln2}+\frac2{\ln2}
   =5.760428856692455\ldots .
   \]
   If the quadratic phase has no within-core quadratic edges (only affine terms inside cores and arbitrary quadratic edges between cores), the direct constant improves to `5`.

This is a genuine fresh-variable-free dependent-branch recombination result. It does not solve a single arbitrary connected high-degree core, which remains the source-level obstruction.

## 1. Dependencies actually consumed

The progress-first directive was followed; no whole-repository scan was performed.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains T01 FEI owner; derive new mathematics first; restricted classes are not full closure.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` needs appended controls and `2^{-c}M_0(f)<=1`; it is not used as a fixed-domain theorem here.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open and the false pointwise-erasure, resolvent/interpolation, fixed-affine-drift and Han absolute-overlap routes remain retired.
- Newest prior P03 substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T10-27-34+0300__fei-quadratic-product-wiener-recombination.md`, blob `b6a4a006b7747fb222b9895f29f6a156f1f5cf28`: supplies the exact cross-block quadratic half-influence mechanism and the `Omega_2`/connected-core reduction. The theorem below strictly generalizes its recombination layer from a Wiener certificate to arbitrary hereditary/direct core certificates.
- P03 `2026-09-20T05-32-22+0300__fei-minor-child-allocation.md`, blob `7e12f35a9c2fae61f3c63e8434a493762a0e8081`: for every physical split,
  \[
  B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\},
  \quad C_\chi=2+\frac1{\sqrt e\ln2}.
  \]
- P03 `2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: exact tree telescopes and
  \[
  0\le J_i^{\rm rec}(f)\le\frac2{\ln2}j_i(f).
  \]
- Companion NM13-02 `2026-09-20T08-08-34+0300__hybrid-decision-tree-hereditary.md`: already proves a sharper hereditary recursion for arbitrary quadratic twists of decision-tree cores, including uniform `<3` along a one-live-child spine. I do not relabel that as new P03 work. The new result here is the parameter-free **cross-core** max-splicing theorem and the direct entropy-decrement refinement.
- Companion newest NM13-02 `2026-09-20T10-08-55+0300__quadratic-normalized-wiener-hereditary.md`, blob `aec413db2f0dca3b1733e40ba9fc22807bc909b8`: supplies the independent `Lambda_2` normalization theorem. The present proof does not require bounded `Lambda_2`.
- `POSTED.md` was checked for exact-scope exclusions. No posted unrestricted FEI result or matching certified-core max-splicing theorem is being reintroduced.

## 2. Current source scope and bounded prior-art check

A fresh 20 September 2026 check of González--MacManus--Pereyra, arXiv:2606.00246, still finds the universal FEI statement presented as a conjecture. Their current abstract says their branching inequality would imply full FEI if it held universally, and they prove only classes fitting their stopping-tree framework. The Friedgut--Kalai 1996 attribution remains standard in current FEI literature.

A bounded search for `nested canalizing + Fourier entropy/influence`, `quadratic twist + nested canalizing + Fourier entropy`, and close variants did not return a matching theorem. This is only bounded negative evidence. **Publication priority is UNVERIFIED.**

## 3. Notation and two exact one-step inputs

Let `Z` have the squared Fourier law of a Boolean function `f`. For a physical coordinate `i`, let `f^+,f^-` be the two restrictions and

\[
B_i(f):=H(Z_i\mid Z_{-i}),
\qquad
j_i(f):=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

Write the full one-step entropy decrement

\[
\Delta_i H(f):=
H(f)-\frac{H(f^+)+H(f^-)}2.
\]

The exact erasure/recombination identity is

\[
\Delta_iH(f)=B_i(f)+J_i^{\rm rec}(f),
\tag{3.1}
\]
with

\[
0\le J_i^{\rm rec}(f)\le\frac2{\ln2}j_i(f).
\tag{3.2}
\]

The arbitrary-child allocation theorem gives

\[
B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\}.
\tag{3.3}
\]

Combining (3.1)--(3.3), with

\[
C_*:=C_\chi+\frac2{\ln2}=5.760428856692455\ldots,
\]
we will repeatedly use

\[
\boxed{
\Delta_iH(f)
\le C_*j_i(f)+\min\{I(f^+),I(f^-)\}.
}
\tag{3.4}
\]

No fresh variables or branch-independence assumption is present.

## 4. New exact character-child full-decrement theorem

### Theorem 4.1

If one restriction at coordinate `i` is a signed character on the remaining variables, then

\[
\boxed{
\Delta_iH(f)\le5\,j_i(f).
}
\tag{4.1}
\]

The constant `5` is a proved clean bound, not claimed optimal. The executed scalar check places the maximum of the exact ratio near `4.87232107177`, but that numerical value is not promoted to a theorem.

### Proof: exact formula

Multiplying both children by the signed character only translates residual Fourier labels, so it preserves `Delta_iH` and queried influence. Multiplying the parent by `x_i` exchanges mismatch density `delta` with `1-delta` while preserving all three Fourier entropies in `Delta_iH`. Therefore normalize the character child to `g\equiv1` and

\[
\delta:=j_i(f)=\Pr[g\ne h]\in[0,1/2].
\]

Then

\[
\mu:=\mathbb Eh=1-2\delta,
\qquad
W:=1-\mu^2=4\delta(1-\delta),
\qquad
q:=(1-\delta)^2+\delta^2=1-W/2.
\]

The already-derived character-child fiber calculation gives

\[
B_i(f)
=2\delta(1-\delta)
+q\,h_2\!\left(\frac{\delta^2}{q}\right).
\tag{4.2}
\]

For completeness, the Jensen--Shannon term can also be computed exactly and loses all dependence on the shape of the nonconstant spectrum of `h`. Let `r` be that spectrum normalized to total mass one. The child `g` has spectral law `delta_empty`, while the spectral law of `h` has zero-atom mass `1-W` and nonzero part `Wr`. Their mixture has nonzero mass `W/2`, so

\[
H\!\left(\frac{P_g+P_h}{2}\right)
=h_2(W/2)+\frac W2 H(r),
\]
while

\[
H(P_h)=h_2(W)+W H(r).
\]
Thus

\[
J_i^{\rm rec}(f)
=h_2(W/2)-\frac12h_2(W).
\tag{4.3}
\]

Combining (4.2)--(4.3), define the exact scalar function

\[
F(\delta):=
2\delta(1-\delta)
+q h_2(\delta^2/q)
+h_2(W/2)-\frac12h_2(W).
\tag{4.4}
\]
Then `Delta_iH(f)=F(delta)`.

### Proof that `F(delta)<=5 delta`

Work in natural logarithms and set

\[
G(\delta):=(5\delta-F(\delta))\ln2.
\]
A direct differentiation and cancellation of the binary-entropy terms gives

\[
\boxed{
G''(\delta)
=4\ln\!\left(
\frac{4\delta(1-\delta)}{(1-2\delta)^2}
\right).
}
\tag{4.5}
\]

Let

\[
\delta_0:=\frac{1-1/\sqrt2}{2}.
\]
Then `4 delta(1-delta)=(1-2delta)^2` exactly at `delta_0`; hence `G''<=0` on `(0,delta_0]` and `G''>=0` on `[delta_0,1/2)`.

We next record two exact scalar facts. First, `G(0)=0`. Second, direct substitution at `delta_0` gives the tangent identity

\[
\boxed{
G(\delta_0)+(1/2-\delta_0)G'(\delta_0)=0.
}
\tag{4.6}
\]
Indeed eight times the logarithm of the left-side multiplicative factor reduces to

\[
2\ln(2-\sqrt2)-\ln2+\ln(3+2\sqrt2)
=\ln\!\left(\frac{(2-\sqrt2)^2(3+2\sqrt2)}2\right)=0.
\]

Finally `G'(delta_0)<0`. Since `delta_0>1/8` and `G'` is decreasing up to `delta_0`, it suffices to evaluate

\[
G'(1/8)=\ln\!\left(\frac{864\sqrt7}{2401}\right)<0,
\]
where the last inequality follows after squaring from

\[
7\cdot864^2=5,225,472<5,764,801=2401^2.
\]

Equation (4.6) now implies `G(delta_0)>0`.

On `[0,delta_0]`, `G` is concave, so it lies above the chord joining `(0,0)` and `(delta_0,G(delta_0))`; hence `G>=0`. On `[delta_0,1/2]`, `G` is convex, so it lies above its tangent at `delta_0`. By (4.6) that tangent decreases from the positive value `G(delta_0)` to zero at `1/2`, and is therefore nonnegative throughout the interval. Thus `G>=0` on `[0,1/2]`, proving (4.1). QED.

### Corollary 4.2: affine-twist nested-canalizing functions

Suppose a Boolean `h` has a one-live-child nested-canalizing physical spine: at each internal node one child is constant and the other continues, and the terminal child is constant. Let `chi` be any signed character. Then

\[
\boxed{H(\chi h)\le5I(\chi h).}
\tag{4.7}
\]

Indeed each stopped side child of `chi h` is a signed character. Apply Theorem 4.1 at every internal node and telescope the full entropy decrements. All stopping leaves have Fourier entropy zero, and the queried influence budget is at most the root influence. QED.

This is stronger than paying `B_i` and `J_i^{rec}` separately on this class.

## 5. Certificate-valued quadratic product max-splicing

The next theorem is the main structural advance of the run.

Let the variables be partitioned into disjoint blocks `B_1,...,B_m`, let `u_a` be Boolean on `B_a`, and let `q` be an arbitrary quadratic polynomial over `F_2` on all variables. Put

\[
f=(-1)^q\prod_{a=1}^m u_a.
\tag{5.1}
\]

We need a restriction-stable notion of a core certificate.

**Quadratic-hereditary allocation certificate.** Core `u_a` has constant `A_a` if every physical restriction `v` of `u_a` and every quadratic polynomial `p` on the remaining variables admits a full physical restriction tree with

\[
R_{\mathcal T}((-1)^p v)\le A_a I((-1)^p v).
\tag{5.2}
\]

**Quadratic-stable direct FEI certificate.** Core `u_a` has constant `D_a` if every such `(-1)^p v` satisfies

\[
H((-1)^pv)\le D_a I((-1)^pv).
\tag{5.3}
\]

### Lemma 5.1: disjoint products preserve the worst certificate

If `g_a` live on disjoint variable blocks, then

\[
H\!\left(\prod_ag_a\right)=\sum_aH(g_a),
\qquad
I\!\left(\prod_ag_a\right)=\sum_aI(g_a).
\tag{5.4}
\]

Therefore direct FEI constants combine by `max_a D_a`.

Hereditary allocation constants also combine by the maximum. To see this, run a full certificate tree for the first factor while leaving all other blocks unqueried. Because the squared Fourier law of a disjoint product is the product of the squared Fourier laws, a query in that factor has exactly the same conditional spectral-bit entropy as it has in the factor alone. Once that block is fully fixed, run a certificate tree for the next factor on every leaf, and continue. The total allocation is the sum of the factor allocations, so

\[
R\le\sum_aA_aI(g_a)
\le(\max_aA_a)I\!\left(\prod_ag_a\right).
\tag{5.5}
\]

### Lemma 5.2: an active cross-block quadratic edge has exact half influence

Suppose the current restricted representation still has a quadratic monomial `x_i x_j` in `q`, with `i` and `j` belonging to different core blocks. Then

\[
\boxed{\operatorname{Inf}_i(f)=1/2.}
\tag{5.6}
\]

Indeed the multiplicative derivative in coordinate `i` is

\[
D_if=(-1)^{\partial_iq}\,D_iu_a,
\]
where `D_iu_a` depends only on the variables in block `a`, while `partial_i q` contains the outside variable `x_j` with coefficient one. Conditional on every variable except `x_j`, the derivative sign is therefore equally likely to be `+1` and `-1`. This remains true after any preceding physical restrictions as long as the cross edge is still live. QED.

### Theorem 5.3: certificate-valued max-splicing

Under (5.1)--(5.3),

\[
\boxed{
\exists\,\mathcal T:\quad
R_{\mathcal T}(f)
\le \max\{2,\sup_aA_a\}\,I(f),
}
\tag{5.7}
\]
and

\[
\boxed{
H(f)
\le \max\{4,\sup_aD_a\}\,I(f).
}
\tag{5.8}
\]

### Proof

Build a finite stopping tree as follows. As long as the current quadratic phase contains a live edge joining two distinct current core blocks, query one endpoint. By Lemma 5.2, every such queried coordinate has influence exactly `1/2`.

For hereditary allocation, every queried node has `B_i<=1`, hence

\[
B_i\le2\operatorname{Inf}_i.
\tag{5.9}
\]

For the full entropy decrement, both `B_i` and the Jensen--Shannon term are at most one bit, hence

\[
\Delta_iH\le2=4\operatorname{Inf}_i.
\tag{5.10}
\]

The process terminates because every query deletes a physical variable. At a stopping leaf the surviving quadratic polynomial has no cross-block quadratic term, so, up to an affine character and constant sign, it decomposes as a sum of within-block quadratics. Thus the leaf function factors on disjoint residual blocks as

\[
f_\ell=\prod_a(-1)^{q_{a,\ell}}u_{a,\ell},
\tag{5.11}
\]
where `u_{a,ell}` is a physical restriction of `u_a`. Lemma 5.1 and the hypotheses give leaf hereditary constant at most `A:=sup A_a` and direct FEI constant at most `D:=sup D_a`.

Let `Q` denote the weighted queried influence of the stopping tree and `I_L` the weighted residual leaf influence. The exact influence telescope gives

\[
I(f)=Q+I_L.
\tag{5.12}
\]

Grafting the hereditary leaf certificates onto the stopping tree and using (5.9),

\[
R_{\mathcal T}(f)\le2Q+A I_L
\le\max\{2,A\}I(f).
\]
This proves (5.7).

For the direct estimate, telescope the full entropy decrements and use (5.10) and the direct leaf certificates:

\[
H(f)\le4Q+D I_L
\le\max\{4,D\}I(f).
\]
This proves (5.8). QED.

### What Theorem 5.3 changes

The preceding `Omega_2` theorem supplied the leaf certificate using a bounded quadratic-normalized Wiener norm. Theorem 5.3 shows that **Wiener control is not part of the cross-component recombination cost at all**. Any restriction-stable quadratic-twist certificate can be inserted, and only the worst component constant is paid. The number of blocks, their dimensions, the rank/density of the cross-block quadratic graph, and the order in which cross edges are removed do not enter the final constant.

This is the precise parameter-free version of the preceding report's statement that the unresolved difficulty lies inside a single connected high-degree core.

## 6. New all-dimensional class: quadratic twists of products of nested-canalizing cores

A Boolean core `h` is **nested-canalizing** here if it has a one-live-child physical restriction spine ending in a constant: at every internal node one branch is constant and the other continues. Arbitrary physical restrictions of such a core are again nested-canalizing or constant, by deleting the fixed variable from the same recursive description.

### Proposition 6.1: one arbitrary quadratic twist of one nested core

For every quadratic `q` and nested-canalizing `h`,

\[
\boxed{
R_{\mathcal T}((-1)^qh)\le3I((-1)^qh)
}
\tag{6.1}
\]
for an explicit full physical tree, and

\[
\boxed{
H((-1)^qh)\le C_*I((-1)^qh),
\qquad C_*=5.760428856692455\ldots .
}
\tag{6.2}
\]

The hereditary statement is compatible with, but slightly coarser than, NM13-02's sharper branch recursion; it is rederived only so the later cross-core composition is self-contained.

### Proof of (6.1)

Follow the canalizing spine. At each internal node, stop the canalized side branch; after the quadratic twist that side child is a quadratic phase. Let `Q` be weighted queried influence, `I_side` the weighted total influence of all stopped side leaves, and `I_end` that of the terminal leaf. The exact influence telescope is

\[
I=Q+I_{side}+I_{end}.
\tag{6.3}
\]

From (3.3), choosing the stopped side child as an upper bound for the minimum,

\[
B_i\le C_\chi\operatorname{Inf}_i+I(\text{side child}).
\]
A side child at a node of weight `w` becomes a leaf of weight `w/2`, so summing the side-child term contributes exactly `2 I_side`. Hence the spine allocation is at most

\[
C_\chi Q+2I_{side}.
\]
Quadratic phases have a full hereditary allocation certificate at most their total influence, so completing all quadratic leaves adds at most `I_side+I_end`. Therefore

\[
R\le C_\chi Q+3I_{side}+I_{end}
\le3I
\]
because `C_chi<3`. QED.

### Proof of (6.2)

Use the full-decrement estimate (3.4) instead. At each spine node,

\[
\Delta_iH
\le C_*\operatorname{Inf}_i+I(\text{side child}).
\]
After weighted summation, the internal-node contribution is at most

\[
C_*Q+2I_{side}.
\]
Every stopped side leaf and the terminal leaf is quadratic. If a quadratic phase has polar rank `r`, its squared Fourier law is uniform on `2^r` points, so `H=r`, while its total influence is at least `r/2`; hence `H<=2I`. The weighted leaf entropy is therefore at most

\[
2(I_{side}+I_{end}).
\]
Consequently

\[
H(f)
\le C_*Q+4I_{side}+2I_{end}
\le C_*(Q+I_{side}+I_{end})
=C_*I(f),
\]
since `C_*>4`. QED.

### Theorem 6.2: arbitrary products and arbitrary quadratic coupling

Let `h_a` be nested-canalizing Boolean cores on pairwise disjoint blocks and let `q` be an arbitrary quadratic polynomial on all variables. Then

\[
\boxed{
\exists\mathcal T:\quad R_{\mathcal T}\!\left((-1)^q\prod_ah_a\right)\le3I\!\left((-1)^q\prod_ah_a\right),
}
\tag{6.4}
\]

\[
\boxed{
H\!\left((-1)^q\prod_ah_a\right)
\le5.760428856692455\ldots\,
I\!\left((-1)^q\prod_ah_a\right).
}
\tag{6.5}
\]

This follows immediately from Proposition 6.1, restriction stability of nested canalization, and Theorem 5.3: `max{2,3}=3` for hereditary allocation, and `max{4,C_*}=C_*` for direct FEI.

The constants are independent of the number of cores, their depths and dimensions, and the rank or density of the global quadratic phase.

### Corollary 6.3: cross-core quadratic couplings only

Assume in addition that the quadratic part of `q` has no edge with both endpoints inside the same core block. Affine terms are allowed everywhere. Cross-edge restrictions can create only affine within-block terms, never a new within-block quadratic edge. Hence every stopping-leaf factor is an affine character times a restricted nested-canalizing core and satisfies the `5I` estimate from Corollary 4.2. Theorem 5.3 therefore gives

\[
\boxed{
H\!\left((-1)^q\prod_ah_a\right)\le5I\!\left((-1)^q\prod_ah_a\right).
}
\tag{6.6}
\]

This is the cleanest direct manifestation of the new recombination theorem: arbitrarily many dependent quadratic cross-couplings cost no more than the local constant `4`, below the intrinsic character-canalizing constant `5`.

## 7. Attempts compared and routes not revived

Three materially different approaches were considered before fixing the theorem above.

1. **Separator-width attack on the connected ANF core.** For primal hypergraph treewidth this collapses to bounded algebraic degree because every high-degree monomial induces a clique; P03's earlier Reed--Muller degree theorem already controls that regime. Incidence-treewidth leaf peeling, by contrast, repeatedly exposes a hard surviving child and the generic minor-child estimate accumulates a depth cost. No universal separator theorem was claimed from that route.
2. **Strengthen the arbitrary-child estimate by multiplying the minor-child influence by the mismatch `j_i`.** Exhaustive small-dimensional checks made a bound of the schematic form `B_i <= C j_i + O(j_i I_child)` plausible, but a proof would require controlling Fourier information of a sparse signed difference and appears to run directly into FEI-type spectral complexity. I did not promote it.
3. **Jointly analyze erasure and recombination at a character child.** This succeeds because the Jensen--Shannon term has an exact scalar formula in the mismatch density and all dependence on the nonconstant spectrum cancels. That gives Theorem 4.1 and then feeds the certificate-valued max-splicing theorem.

The false pointwise-erasure shortcut, fixed-coefficient affine drift, resolvent/interpolation route, Han all-coordinate absolute-overlap selector, derivative-degree scalar scheduler, blind root-curvature bound, and fixed-`s<2` Clarkson/Renyi route remain retired. None is used above.

## 8. Sanity checker

Executed checker:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__check_certified_core_max_splicing.py`

Creation commit `bb508517f2354fbce6e708f7e454e6b8509ae8d1`, read-back blob `4c6f1038bbdac69d631d32cf12a5d35ce690ce6d`.

Output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__certified_core_max_splicing_check.json`

Creation commit `77879265b6a669c88b7a664ac1c8ea8afa7d7070`, read-back blob `0b04cbb77c945e5459a0bff63f96d177c58b1da3`.

The checker status is `PASS`. It performed:

- exhaustive character-child Walsh checks through residual dimension four: **65,814** cases;
- exact-formula discrepancy at most `1.11e-15`;
- maximum violation of `Delta H <= 5 delta`: exactly `0.0` at floating precision;
- a **200,000**-point scalar scan, whose largest observed exact ratio was `4.872321071767738` near `delta=0.2294425`;
- **2,500** deterministic-seed arbitrary quadratic twists of nested-canalizing cores through dimension nine, with maximum `H/I = 3.4024755512` and zero violation of (6.2);
- **2,500** deterministic-seed products of two or three nested cores under arbitrary global quadratic twists through dimension nine, with maximum `H/I = 2.1084585933` and zero violation of (6.5);
- **10,298** live endpoints of cross-block quadratic edges, all having influence exactly `1/2` at floating precision.

These checks are self-checks only, not independent audits. The scalar theorem (4.1) rests on the analytic proof in Section 4, not the grid.

## 9. Source-level interpretation and next obstruction

The universal FEI conjecture is not closed. The gain is that **cross-component quadratic dependence is now completely certificate-agnostic**: once individual cores have a restriction-stable quadratic-twist certificate, recombining arbitrarily many of them costs only a fixed floor `2` for hereditary allocation or `4` for direct FEI. The preceding Wiener parameter is therefore one possible core certificate, not part of the recombination mechanism itself.

The exact remaining full-scope obstruction is correspondingly sharper:

> prove a universal restriction-stable hereditary/direct certificate for a **single connected degree-`>=3` ANF interaction core under arbitrary quadratic twist**, or construct a connected-core family forcing every proposed certificate to diverge.

A useful next attack is not another disconnected-product argument. It should work inside one connected core, preferably by a structure-sensitive selector or by finding a decomposition whose side certificates are paid in the sense of Theorem 5.3. Incidence-separator peeling without a new amortization is not enough.

## 10. Ledger delta

```yaml
ledger_delta:
  track: P03
  source: Friedgut--Kalai Fourier entropy-influence conjecture
  source_status_before: OPEN
  source_status_after: OPEN
  universal_finite_C_before: UNKNOWN
  universal_finite_C_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  new_results:
    - CERTIFIED_CORE_QUADRATIC_MAX_SPLICING:
        status: PROVED_INTERNAL_PENDING_INDEPENDENT_REVIEW
        hereditary_bound: max(2, sup_core_A)
        direct_FEI_bound: max(4, sup_core_D)
        fresh_variables: false
        all_dimensions: true
    - CHARACTER_CHILD_FULL_DECREMENT:
        status: PROVED_INTERNAL_PENDING_INDEPENDENT_REVIEW
        bound: Delta_i_H <= 5 j_i
        exact_scalar_formula: true
        fresh_variables: false
    - QUADRATIC_PRODUCT_NESTED_CANALIZING:
        status: PROVED_INTERNAL_PENDING_INDEPENDENT_REVIEW
        hereditary_constant: 3
        direct_FEI_constant: 5.760428856692455
        arbitrary_number_of_cores: true
        arbitrary_global_quadratic_twist: true
    - CROSS_ONLY_QUADRATIC_PRODUCT_NESTED_CANALIZING:
        status: PROVED_INTERNAL_PENDING_INDEPENDENT_REVIEW
        direct_FEI_constant: 5
  mechanism_gain:
    previous: quadratic cross-component recombination paid through Omega_2 / Lambda_2 leaf certificates
    now: cross-component quadratic recombination accepts arbitrary restriction-stable hereditary/direct core certificates and pays only max floors 2/4
  checker:
    status: PASS
    path: proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__check_certified_core_max_splicing.py
    creation_commit: bb508517f2354fbce6e708f7e454e6b8509ae8d1
    blob: 4c6f1038bbdac69d631d32cf12a5d35ce690ce6d
  checker_output:
    path: proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__certified_core_max_splicing_check.json
    creation_commit: 77879265b6a669c88b7a664ac1c8ea8afa7d7070
    blob: 0b04cbb77c945e5459a0bff63f96d177c58b1da3
  independent_review: PENDING
  publication_priority: UNVERIFIED
  failed_routes_preserved:
    - pointwise_erasure
    - fixed_affine_drift
    - resolvent_interpolation
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_curvature_payment
    - fixed_Renyi_exponent_below_2
  remaining_obstruction: universal restriction-stable certificate for one connected degree>=3 ANF core under arbitrary quadratic twist
```

**End of complete run report.**
