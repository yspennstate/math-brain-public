Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — Wiener-norm hereditary allocation, bounded affine-flat arrangements, and a sharper two-flat quadratic certificate

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** No universal FEI constant is proved. The source-level quantity “finite universal upper bound for `C_FEI`” remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**.

This run makes three mechanism-level advances and one decisive correction.

1. **General Wiener-norm hereditary theorem.** For
   \[
   \Lambda(f):=\sum_S|\widehat f(S)|,\qquad
   J(f):=\sum_i\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
   \]
   define
   \[
   C_{\rm W}(L):=\max\{4,\;2\log_2 e+4\log_2 L\}\qquad(L\ge1).
   \]
   Then every Boolean `f` satisfies
   \[
   \boxed{H(\widehat f^{\,2})\le C_{\rm W}(\Lambda(f))\,J(f).}
   \tag{0.1}
   \]
   Moreover physical restriction never increases `Lambda`; consequently there exists a full adaptive physical restriction tree `T` with
   \[
   \boxed{R_T(f)\le C_{\rm W}(\Lambda(f))\,I(f).}
   \tag{0.2}
   \]
   This is an all-dimensional, fresh-variable-free hereditary allocation estimate. It is parameterized by spectral norm and therefore is not full FEI.

2. **Arbitrary bounded affine-flat arrangements.** If
   \[
   u=\chi\prod_{a=1}^m\sigma_{A_a},\qquad
   \sigma_A=1-2\,1_A,
   \]
   with arbitrary affine flats `A_a` and an affine character `chi`, then
   \[
   \Lambda(u)\le3^m
   \]
   and hence
   \[
   \boxed{H(u)\le C_m J(u)\le C_m I(u),\qquad
   C_m:=2\log_2e+4m\log_2 3.}
   \tag{0.3}
   \]
   The class is closed under physical restrictions, so it also has a hereditary certificate
   \[
   \boxed{R_T(u)\le C_m I(u)}
   \tag{0.4}
   \]
   for some full adaptive tree. The actual `Lambda(u)` may be far below `3^m`, so (0.1) automatically exploits exact cancellations among many flats.

3. **Sharper quadratic two-flat hereditary theorem.** A new companion NM13-02 report appearing before this write proved a uniform constant `24` for
   \[
   (-1)^q\sigma_A\sigma_B
   \]
   with `q` quadratic and arbitrary affine flats. The Wiener terminal estimate improves the same hereditary class to
   \[
   \boxed{
   R_T((-1)^q\sigma_A\sigma_B)\le C_2 I((-1)^q\sigma_A\sigma_B),
   \quad
   C_2=2\log_2e+8\log_2 3
   =15.565090087547176\ldots .
   }
   \tag{0.5}
   \]
   Combining (0.5) with P03's already-proved paid dependent-branch remainder
   \[
   S_T\le\frac2{\ln2}J_T\le\frac2{\ln2}Q_T
   \]
   gives the restricted class inequality
   \[
   \boxed{
   H(\widehat f^{\,2})
   \le18.450480169325104\ldots\, I(f)
   }
   \tag{0.6}
   \]
   for this two-flat quadratic class. This remains a restricted theorem, not full FEI.

4. **Correction to the naive many-flat extension.** Individual large codimension cannot by itself protect a quadratic polar row. Two parallel codimension-three flats can recombine into one codimension-two flat and cancel a quadratic phase exactly. More generally, `2^{r-2}` parallel codimension-`r` flats can partition a codimension-two flat. Thus any future many-flat extension must detect algebraic recombination/cancellation rather than sum componentwise perturbation costs blindly.

No previously refuted resolvent, pointwise-erasure, fixed-coefficient drift, Han absolute-overlap, derivative-degree scalar, or blind curvature claim is revived.

## Dependencies actually consumed

The progress-first directive was followed: only proof dependencies needed for this route were read.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 owns T01; approximately 90% of effort is new derivation; NM13-02 is the complementary FEI theory worker.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` uses appended controls and a density hypothesis; it is not full FEI.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the false pointwise erasure, all-fixed-coefficient drift, resolvent/interpolation, and Han absolute-overlap routes remain retired.
- Newest preceding P03 owner report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__fei-affine-flat-quadratic-hereditary.md`, blob `be68be1be01e8abbb9f45dd62c5cc238d5e6119d`: one arbitrary affine-flat sign defect under a quadratic twist has hereditary constant `4` and direct FEI constant `5.145274443580206...`.
- P03 paid-recombination report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: exact partial-tree identities and
  \[
  0\le S_T\le(2/\ln2)J_T\le(2/\ln2)Q_T.
  \]
- P03 degree theorem `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T03-31-42+0300__fei-reed-muller-hereditary-allocation.md`, blob `fbcc39447666a43d398403ad2e89b7e50c6adf1b`: degree-three phases have hereditary constant
  \[
  \kappa_3=4h_2(1/4)=3.245112497836531\ldots.
  \]
- Newest companion report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T09-08-00+0300__two-affine-flat-hereditary-recombination.md`, blob `908634d789bdb0fa5ef8b27224c8b9057a1af3d6`: independently proves the exact two-flat quadratic hereditary class with constant `24` and identifies unbounded affine-flat arrangements as the next recombination obstruction. The present run does not edit or overwrite that peer claim; it supplies a complementary Wiener-norm mechanism and a sharper constant on the same two-flat class.
- Root `POSTED.md` was checked for exact-scope exclusions. The posted entropy/singularity paper is a different restricted result; no posted unrestricted FEI theorem or exact theorem below was found.

## Current public-source scope

A fresh check of González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture*, still states the dimension-free FEI assertion as a conjecture and develops a coordinate-restriction/stopping-tree sufficient framework plus proper positive subclasses. Its key branching inequality would imply full FEI if available universally; the paper does not prove such a universal inequality.

The Friedgut--Kalai 1996 source attribution is preserved.

A bounded fresh search also recovered Arunachalam--Chakraborty--Koucky--Saurabh--de Wolf (arXiv:1809.09819), which relates **Fourier min-entropy** to approximate spectral norm. I did not recover, in this bounded search, the exact Shannon-entropy/folded-influence hereditary theorem (0.1)--(0.2). That is negative evidence only: **publication priority is UNVERIFIED**.

## 1. Notation

For a Boolean function `f` on `F_2^n`, write
\[
p_S=\widehat f(S)^2,\qquad
H(f)=\sum_S p_S\log_2(1/p_S),
\]
\[
\alpha_i(f)=\operatorname{Inf}_i(f),\qquad
I(f)=\sum_i\alpha_i(f),
\]
\[
j_i(f)=\min\{\alpha_i(f),1-\alpha_i(f)\},\qquad
J(f)=\sum_i j_i(f),
\]
and
\[
\Lambda(f)=\sum_S|\widehat f(S)|.
\]

Let `Z` be the spectral random set with `P(Z=S)=p_S`, and put
\[
B_i(f)=H(Z_i\mid Z_{-i}).
\]

For a physical restriction tree `T`, `R_T` denotes the cylinder-weighted sum of the `B_i` values at queried nodes.

We use three standard facts.

**Edge isoperimetry.** If `g` is Boolean and
\[
\varepsilon=\min\{\Pr(g=1),\Pr(g=-1)\}\le1/2,
\]
then
\[
I(g)\ge2\varepsilon\log_2(1/\varepsilon).
\tag{1.1}
\]
This is the standard edge-isoperimetric inequality
`|partial E| >= |E| log_2(2^n/|E|)` applied to the minority set; total influence counts every undirected boundary edge twice after normalization.

**Han--Shearer.**
\[
\sum_iB_i(f)\le H(f).
\tag{1.2}
\]
Indeed `B_i=H(Z)-H(Z_{-i})`, while Shearer's inequality gives
\[
\sum_iH(Z_{-i})\ge(n-1)H(Z).
\]

**One-step influence identity.** For the two restrictions at coordinate `i`,
\[
I(f)=\alpha_i(f)+\frac{I(f^+)+I(f^-)}2.
\tag{1.3}
\]

## 2. The Wiener-norm FEI estimate

### Theorem 2.1

For every Boolean `f`,
\[
\boxed{
H(f)\le C_{\rm W}(\Lambda(f))J(f),
\qquad
C_{\rm W}(L)=\max\{4,2\log_2e+4\log_2L\}.
}
\tag{2.1}
\]

### Proof

Multiplication by a physical character
\[
\chi_T(x)=\prod_{i\in T}x_i
\]
translates the Fourier spectrum. Therefore it preserves both `H` and `Lambda`. In coordinate `i`, it either preserves `alpha_i` or replaces it by `1-alpha_i`.

Choose
\[
T=\{i:\alpha_i(f)>1/2\}
\]
and put `g=chi_T f`. Then
\[
H(g)=H(f),\qquad
\Lambda(g)=\Lambda(f),\qquad
I(g)=J(f).
\tag{2.2}
\]

It remains to bound `H(g)` by `I(g)`.

Multiply `g` by a global sign if needed and write
\[
\Pr(g=-1)=\varepsilon\le1/2.
\]
Then
\[
\widehat g(\varnothing)=1-2\varepsilon.
\]
Put
\[
W=1-\widehat g(\varnothing)^2=4\varepsilon(1-\varepsilon).
\tag{2.3}
\]
If `W=0`, `g` is constant and there is nothing to prove.

Condition the spectral law on `S ne emptyset`:
\[
q_S=\frac{\widehat g(S)^2}{W},\qquad S\ne\varnothing.
\]
The entropy decomposes exactly as
\[
H(g)=h_2(W)+W H(q).
\tag{2.4}
\]

Shannon entropy is at most Renyi entropy of order `1/2`, hence
\[
H(q)
\le2\log_2\sum_{S\ne\varnothing}\sqrt{q_S}
=2\log_2\frac{\sum_{S\ne\varnothing}|\widehat g(S)|}{\sqrt W}
\le2\log_2\frac{\Lambda(g)}{\sqrt W}.
\tag{2.5}
\]

The elementary inequality
\[
h_2(x)\le x\log_2(e/x),\qquad 0<x\le1,
\tag{2.6}
\]
together with (2.4)--(2.5), gives
\[
H(g)
\le W\bigl(\log_2e+2\log_2\Lambda(g)-2\log_2W\bigr).
\tag{2.7}
\]

Let
\[
t=\log_2(1/\varepsilon)\ge1.
\]
From (2.3),
\[
2\varepsilon\le W\le4\varepsilon,
\tag{2.8}
\]
so
\[
-2\log_2W\le2t-2.
\]
Set
\[
D=\log_2e+2\log_2\Lambda(g)-2.
\]

If `D>=0`, then
\[
2t+D\le(2+D)t
=(\log_2e+2\log_2\Lambda(g))t,
\]
and therefore
\[
H(g)
\le4\varepsilon
(\log_2e+2\log_2\Lambda(g))t.
\]
Using (1.1),
\[
H(g)
\le(2\log_2e+4\log_2\Lambda(g))I(g).
\tag{2.9}
\]

If `D<0`, then the bracket in (2.7) is at most `2t`, so
\[
H(g)\le8\varepsilon t\le4I(g).
\tag{2.10}
\]

Combining (2.9)--(2.10) with (2.2) proves (2.1). QED.

### Remarks on scope

- The theorem is all-dimensional and uses no fresh variables.
- It is **not** full FEI because `Lambda(f)` is unbounded over Boolean functions. A rank-`r` quadratic phase already has `Lambda=2^{r/2}` while its true hereditary allocation is much cheaper.
- The use of `J`, rather than only `I`, is important: character multiplication folds each coordinate's influence without changing spectral entropy or spectral norm.

## 3. Physical restriction does not increase the Wiener norm

### Lemma 3.1

For every physical coordinate `i`,
\[
\boxed{\Lambda(f^+)\le\Lambda(f),\qquad
\Lambda(f^-)\le\Lambda(f).}
\tag{3.1}
\]

### Proof

For every residual Fourier label `S` not containing `i`,
\[
\widehat{f^+}(S)=\widehat f(S)+\widehat f(S\cup\{i\}),
\]
\[
\widehat{f^-}(S)=\widehat f(S)-\widehat f(S\cup\{i\}).
\]
Hence
\[
\Lambda(f^\pm)
\le\sum_{S\not\ni i}
\bigl(|\widehat f(S)|+|\widehat f(S\cup\{i\})|\bigr)
=\Lambda(f).
\]
QED.

This monotonicity is the key hereditary feature: unlike the previously refuted scalar drift quantities, the controlling parameter here cannot increase on either dependent physical branch.

### Theorem 3.2 (Wiener hereditary allocation)

For every Boolean `f`, with `L=Lambda(f)`, there exists a full adaptive physical restriction tree `T` such that
\[
\boxed{R_T(f)\le C_{\rm W}(L)I(f).}
\tag{3.2}
\]

### Proof

Induct on dimension.

Every physical restriction `g` of `f` has `Lambda(g)<=L` by Lemma 3.1, so Theorem 2.1 gives
\[
H(g)\le C_{\rm W}(L)J(g)\le C_{\rm W}(L)I(g).
\tag{3.3}
\]
By Han--Shearer,
\[
\sum_iB_i(g)\le H(g)\le C_{\rm W}(L)\sum_i\alpha_i(g).
\]
If `g` is nonconstant, some coordinate `i` therefore satisfies
\[
B_i(g)\le C_{\rm W}(L)\alpha_i(g).
\tag{3.4}
\]
Query such an `i`, apply the induction hypothesis to both children, and use (1.3):
\[
\begin{aligned}
R_T(g)
&\le C_{\rm W}(L)\alpha_i(g)
+\frac{C_{\rm W}(L)}2(I(g^+)+I(g^-))\\
&=C_{\rm W}(L)I(g).
\end{aligned}
\]
Constants are terminal. QED.

This is a genuine hereditary allocation theorem, not a direct-entropy restatement: the same root parameter controls every dependent branch because of (3.1).

## 4. Arbitrary bounded affine-flat arrangements

Let `A=a+V` be a nonempty affine subspace of density `delta`. Its indicator has
\[
\widehat{1_A}(\xi)=\delta(-1)^{\xi\cdot a}1_{\{\xi\in V^\perp\}},
\]
hence
\[
\|\widehat{1_A}\|_1=1.
\tag{4.1}
\]
For
\[
\sigma_A=1-2\,1_A
\]
we therefore have
\[
\Lambda(\sigma_A)\le1+2\|\widehat{1_A}\|_1\le3.
\tag{4.2}
\]
The empty and full flats only improve this bound.

Fourier transform converts physical products into convolution, so `l1` is submultiplicative:
\[
\Lambda(uv)\le\Lambda(u)\Lambda(v).
\tag{4.3}
\]

### Corollary 4.1 (m-flat arrangement)

For arbitrary affine flats `A_1,...,A_m` and any affine character `chi`,
\[
u=\chi\prod_{a=1}^m\sigma_{A_a}
\]
satisfies
\[
\Lambda(u)\le3^m.
\tag{4.4}
\]
Consequently
\[
\boxed{
H(u)\le C_mJ(u)\le C_mI(u),
\qquad
C_m=2\log_2e+4m\log_2 3.
}
\tag{4.5}
\]
Moreover the class is restriction-closed, and there is a full physical tree with
\[
\boxed{R_T(u)\le C_m I(u).}
\tag{4.6}
\]

### Proof

An affine character shifts Fourier labels and has spectral norm one. Equations (4.2)--(4.3) give (4.4). Theorem 2.1 gives (4.5).

Under a physical restriction an affine flat either becomes empty or another affine flat in the remaining cube, and an affine character remains an affine character or constant. Thus the class with at most `m` factors is restriction-closed. Theorem 3.2, or equivalently the Han--Shearer induction using the uniform bound `3^m`, gives (4.6). QED.

### Cancellation-sensitive gain

The `3^m` estimate is only a worst-case corollary. The stronger theorem uses the **actual** spectral norm `Lambda(u)`, which can collapse after exact algebraic recombination.

For example, fix a codimension-two flat
\[
C=\{x_1=x_2=0\}.
\]
Partition `C` into all `2^{r-2}` affine flats
\[
A_b=\{x_1=x_2=0,\ (x_3,\ldots,x_r)=b\},
\qquad b\in F_2^{r-2}.
\]
They are pairwise disjoint and each has codimension `r`, but
\[
\prod_b\sigma_{A_b}=\sigma_C.
\tag{4.7}
\]
Thus component count grows exponentially while the actual Wiener norm stays bounded by `3`. This is exactly the kind of dependent recombination that a componentwise payment misses and the actual `Lambda` detects automatically.

## 5. Sharpening the quadratic two-flat theorem

The companion NM13-02 run proved hereditary constant `24` for
\[
f=(-1)^q\sigma_A\sigma_B.
\]
The following proof sharpens the constant without using the peer theorem as a premise; it only reuses P03's already-established one-flat and degree-three bases.

Set
\[
K=C_2
=2\log_2e+8\log_2 3
=15.565090087547176\ldots,
\tag{5.1}
\]
and
\[
C_8=8h_2(1/8)=4.348515545596771\ldots<K.
\tag{5.2}
\]

### Theorem 5.1

For every quadratic `q` and every pair of affine flats `A,B`,
\[
\boxed{R_T((-1)^q\sigma_A\sigma_B)\le K I((-1)^q\sigma_A\sigma_B)}
\tag{5.3}
\]
for some full adaptive physical restriction tree.

### Proof

Induct on ambient dimension. Physical restriction preserves the class.

At a state `f=(-1)^q sigma_A sigma_B`, apply the first applicable case.

**(i) One flat is empty.** P03's one-flat theorem gives hereditary constant `4<K`.

**(ii) `A=B`.** The signs cancel and `f=(-1)^q`; the quadratic rank certificate is at most `1<K`.

**(iii) One nonempty flat has codimension at most two.** Its indicator is a polynomial of degree at most two, so absorb it into `q`. The state reduces to the one-flat theorem, constant `4`.

**(iv) Both flats have codimension three.** Each indicator has algebraic degree at most three, so
\[
q+1_A+1_B
\]
has degree at most three. P03's Reed--Muller hereditary theorem gives
\[
\kappa_3=3.2451124978\ldots<K.
\]

**(v) Both codimensions are at least three, not both three, and the quadratic polar form is nonzero.** Choose a coordinate `i` in a nonzero polar row. The pure quadratic phase has `i`-influence exactly `1/2`.

For a flat of density `delta`, its sign has coordinate influence either `0` or `2delta`. Since at least one of `A,B` has codimension at least four,
\[
\operatorname{Inf}_i(\sigma_A\sigma_B)
\le2\delta_A+2\delta_B
\le\frac14+\frac18=\frac38.
\tag{5.4}
\]
The disagreement indicator of a product is the xor of the disagreement indicators, hence
\[
\left|\alpha_i(f)-\frac12\right|
\le \operatorname{Inf}_i(\sigma_A\sigma_B)
\le\frac38.
\]
Therefore
\[
j_i(f)\ge\frac18.
\]
The spectral-bit marginal identity and conditioning give
\[
B_i(f)\le h_2(j_i(f))
\le C_8 j_i(f)
\le C_8\alpha_i(f)
\le K\alpha_i(f).
\tag{5.5}
\]
Query `i`; apply the induction hypothesis below both children and use (1.3). This pays the node and both branches with the same constant `K`.

**(vi) The quadratic polar form is zero.** Then `(-1)^q` is an affine character. Corollary 4.1 with `m=2` gives
\[
H(f)\le KJ(f)\le KI(f).
\tag{5.6}
\]
By Han--Shearer there is a coordinate with
\[
B_i(f)\le K\alpha_i(f)
\]
unless `f` is constant. Query it, use the induction hypothesis in the children, and close with (1.3).

The cases exhaust all states. QED.

### Restricted FEI consequence inside the P03 chain

For a full tree from Theorem 5.1, P03's proved dependent-branch remainder gives
\[
H(f)=R_T+S_T
\le K I(f)+\frac2{\ln2}I(f).
\]
Hence
\[
\boxed{
H(f)\le
\left(2\log_2e+8\log_23+\frac2{\ln2}\right)I(f)
=18.450480169325104\ldots I(f).
}
\tag{5.7}
\]

This improves the companion `24` hereditary constant and its `24+2/ln2` project-conditional FEI constant, but it does not affect the unknown universal source constant.

## 6. A decisive obstruction to naive componentwise polar protection

The preceding proof succeeds for two flats because the low-codimension cases can be absorbed into degree at most three and the high-codimension two-flat perturbation leaves a fixed `1/8` folded margin.

That logic cannot be extended to many flats by asserting that **each component separately** has large codimension.

Take, in `F_2^n`,
\[
A=\{x_1=x_2=x_3=0\},
\qquad
B=\{x_1=x_2=0,\ x_3=1\}.
\]
Both have codimension three, are disjoint, and their union is
\[
C=\{x_1=x_2=0\},
\]
a codimension-two flat. Therefore
\[
\sigma_A\sigma_B=\sigma_C.
\tag{6.1}
\]
But `1_C` is a quadratic polynomial, so with
\[
q=1_C
\]
we have
\[
(-1)^q\sigma_A\sigma_B=\sigma_C^2=1.
\tag{6.2}
\]
The pure quadratic phase `(-1)^q` has influence `1/2` in coordinates `1,2`, while the final function has influence zero in every coordinate.

Thus no local theorem can lower-bound the final folded influence on a nonzero quadratic polar row using only the individual assertions `codim(A),codim(B)>=3`.

The scalable version is (4.7): `2^{r-2}` parallel codimension-`r` flats can partition a codimension-two flat and collectively cancel its quadratic sign exactly. Their summed per-component perturbation budget reaches the full `1/2` cancellation threshold.

**Conclusion.** The next many-flat theorem must first normalize algebraic recombinations (or use a cancellation-sensitive quantity such as actual Wiener norm) before charging polar-row perturbations. A raw sum over components is not a viable universal mechanism.

## 7. Why the new parameter is useful but not full FEI

The Wiener norm has two properties that the retired scalar drift candidates lacked:

1. **branch monotonicity:** every physical restriction has no larger `Lambda`;
2. **recombination sensitivity:** exact cancellations among flat factors reduce the actual norm automatically.

This makes it a legitimate hereditary control parameter.

However, it cannot be the final universal FEI parameter. Quadratic phases of increasing polar rank have exponentially growing `Lambda` while their hereditary allocation is bounded by the quadratic-rank telescope. Therefore the next nonredundant route is not to prove `Lambda=O(1)`.

A plausible next target is to combine the Wiener certificate with the existing quadratic/symmetric stopping certificates through max-splicing: stop immediately on high-rank quadratic-like states, and use `C_W(Lambda)` only on branches whose nonquadratic residual has bounded spectral norm. What is still missing is a **paid normalization theorem** that extracts the quadratic part without paying its rank twice. No such theorem is asserted here.

## 8. Sanity checks actually executed

The checker
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T09-29-44+0300__check_wiener_arrangements.py`
was executed before upload.

It performs:

1. exhaustive testing of all **65,814 Boolean functions through dimension four**, including:
   - `H <= C_W(Lambda) J`,
   - Han--Shearer `sum_i B_i<=H`,
   - existence of a selector `B_i<=C_W(Lambda) alpha_i`,
   - monotonicity of `Lambda` under both physical restrictions of every coordinate;
2. exhaustive testing of all **96,980 ordered affine-flat pairs through dimension four** against the two-flat constant `C_2`;
3. **10,000** deterministic-seed sampled three- and four-flat arrangements in dimensions five and six against the `C_m` bounds and `Lambda<=3^m`;
4. the explicit parallel codimension-three cancellation (6.1)--(6.2).

Recorded status: `PASS`. Maximum numerical theorem violation was `-0.0`; the explicit cancellation produced final influence exactly `0.0` while the cancelling quadratic phase had influences `(1/2,1/2,0,0)`.

The checker is a self-check only. The all-dimensional claims rest on the proofs above.

## 9. Metrics and exact remaining obligation

- full Friedgut--Kalai FEI: `OPEN -> OPEN`;
- unrestricted universal finite source constant: `UNKNOWN -> UNKNOWN`;
- P03 native finite-dimensional atlas: `6 -> 6`;
- fresh-variable dependence in the new theorem: `none`;
- new hereditary parameter: actual Fourier/Wiener norm `Lambda`, restriction-monotone;
- bounded `m` affine-flat arrangements: hereditary constant
  \[
  C_m=2\log_2e+4m\log_23;
  \]
- quadratic two-flat hereditary constant: companion baseline `24` -> P03 strengthening `15.565090087547176...`;
- quadratic two-flat restricted FEI constant using P03 paid recombination: `26.8853900817779...` -> `18.450480169325104...`;
- independent audit of the new theorems: `pending`;
- publication priority: `UNVERIFIED`.

**Remaining full-scope obstruction.** Obtain a cancellation-aware normalization/splicing theorem whose payment is universal even when the raw Wiener norm and quadratic rank are both large. Equivalently, show how to extract a certified quadratic/symmetric leaf while charging only the genuinely nonquadratic residual complexity, or construct a family where every such normalization has diverging hereditary cost.

The fresh-control theorem remains restricted and does not alter this obligation.

## ledger_delta

```yaml
ledger_delta:
  owner: P03
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  new_claims:
    - id: P03-FEI-WIENER-HEREDITARY
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "H(f)<=C_W(Lambda(f)) J(f), restrictions do not increase Lambda, and a full tree has R_T<=C_W(Lambda(f)) I(f)"
    - id: P03-FEI-M-FLAT-ARRANGEMENT-HEREDITARY
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "affine-character twists of products of m affine-flat signs have Lambda<=3^m and hereditary constant C_m=2 log2 e + 4m log2 3"
    - id: P03-FEI-TWO-FLAT-QUADRATIC-IMPROVED
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "quadratic twists of two affine-flat signs have hereditary constant 15.565090087547176...; with the existing paid remainder, restricted FEI constant 18.450480169325104..."
    - id: P03-FEI-PARALLEL-FLAT-CANCELLATION-OBSTRUCTION
      status: PROVED
      statement: "individual flat codimension cannot by itself protect a quadratic polar row; parallel flats can recombine into and cancel a codimension-two quadratic flat"
  preserved_failures:
    - pointwise_erasure_shortcut
    - all_fixed_coefficient_affine_drift
    - resolvent_interpolation
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_root_curvature_bound
    - direct_curvature_query_ratio
  fresh_controls_used: false
  peer_coordination:
    companion: NM13-02
    peer_new_result: "two-flat quadratic hereditary constant 24"
    overlap_policy: "peer file/claim untouched; P03 proves a Wiener-norm terminal mechanism, arbitrary-m arrangement theorem, and a sharper constant"
  next_obstruction: "paid quadratic/nonquadratic normalization or max-splicing with cancellation-sensitive residual complexity"
  publication_priority: UNVERIFIED
  independent_audit: PENDING
```

**End of complete run report.**
