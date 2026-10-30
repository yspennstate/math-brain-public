# fleet04/B13 — balanced composition is an exact convexity law; center obstructions localize to composition-prime gates

**Run:** `B13-20260922T021402Z-fei-gate-r11`  
**Status:** `SUBSTANTIVE_AUXILIARY_THEOREM`; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target and why this run changed direction

The current owner control revision `2026-09-22.2` supersedes the older B13 all-row-stability wording and converges the FEI fleet on the all-gate formulation. The retired claim that the read-once `Gamma` / AND constraint is extremal over all gates is already refuted by a genuine balanced composition-prime ten-input gate, so I do not repeat that search.

The live structural question I attack here is: **can decomposition itself create a worse balanced-center gate margin than any of its factors?** The answer is no, exactly.

I use the gate-reformulation convention at uniform bias. If `f` is balanced, put

\[
D(f):=I(f)-1\ge 0,\qquad C_0:=\Gamma(1/2),
\]

and, when `D(f)>0`,

\[
R(f):={H(f)\over D(f)},\qquad c(f):=4\,[R(f)-C_0].
\tag{0.1}
\]

This `c(f)` is the source-correct dangerous balanced-center margin: **larger** means a gate asks for more center correction. Balanced characters have `D=H=0` and carry no defect weight.

## 1. New theorem: exact heterogeneous balanced-composition conservation

Let `G:{-1,+1}^m -> {-1,+1}` be balanced. For each `i`, let `H_i` be a balanced Boolean function on a variable block disjoint from all other blocks, and define

\[
F(x)=G(H_1(x^{(1)}),\ldots,H_m(x^{(m)})).
\]

Write

\[
a_i:=\operatorname{Inf}_i(G).
\]

### Theorem 1.1 (entropy, influence, defect, and margin conservation)

Exactly,

\[
\boxed{H(F)=H(G)+\sum_{i=1}^m a_i H(H_i)},
\tag{1.1}
\]

\[
\boxed{I(F)=\sum_{i=1}^m a_i I(H_i)},
\tag{1.2}
\]

and hence

\[
\boxed{D(F)=D(G)+\sum_{i=1}^m a_iD(H_i)}.
\tag{1.3}
\]

For every real constant `C`, define

\[
M_C(f):=H(f)-C D(f).
\]

Then

\[
\boxed{M_C(F)=M_C(G)+\sum_{i=1}^m a_i M_C(H_i)}.
\tag{1.4}
\]

In particular, if `D(F)>0`, then

\[
\boxed{
R(F)=
{D(G)R(G)+\sum_i a_iD(H_i)R(H_i)\over
 D(G)+\sum_i a_iD(H_i)}
}
\tag{1.5}
\]

with the terms having zero defect omitted. Equivalently,

\[
\boxed{
c(F)=
{D(G)c(G)+\sum_i a_iD(H_i)c(H_i)\over
 D(G)+\sum_i a_iD(H_i)}.
}
\tag{1.6}
\]

Thus the balanced-center gate margin of a heterogeneous disjoint composition is a **convex combination of the margins of its positive-defect factors**.

### Proof

Because every `H_i` is balanced, its empty Fourier coefficient vanishes. Expand

\[
G(y)=\sum_{S\subseteq[m]}\widehat G(S)\chi_S(y)
\]

and substitute `y_i=H_i`. For a fixed outer spectral set `S`, the Fourier distribution of the corresponding product is the product of the spectral distributions of the `H_i`, `i in S`. Since each selected inner spectral set is nonempty and the blocks are labelled and disjoint, the final Fourier support uniquely determines the outer active set `S`. Therefore Shannon's chain rule gives

\[
H(F)=H(G)+\sum_S\widehat G(S)^2\sum_{i\in S}H(H_i)
=H(G)+\sum_i\left(\sum_{S\ni i}\widehat G(S)^2\right)H(H_i).
\]

The parenthesized coefficient is `Inf_i(G)=a_i`, proving (1.1).

For a physical variable `x` in block `i`, flipping `x` changes `F` exactly when it changes `H_i` and the outer gate is sensitive to coordinate `i`. Under the uniform product measure the inner outputs are independent unbiased signs, so

\[
\operatorname{Inf}_x(F)=a_i\operatorname{Inf}_x(H_i).
\]

Summing over physical variables yields (1.2). Since `G` is balanced,

\[
D(G)=I(G)-1=\sum_i a_i-1.
\]

Subtracting one from (1.2) gives

\[
D(F)=\sum_i a_i(1+D(H_i))-1
=D(G)+\sum_i a_iD(H_i),
\]

which is (1.3). Equation (1.4) is (1.1) minus `C` times (1.3), and (1.5)--(1.6) follow by dividing by the nonnegative total defect. QED.

## 2. All-depth decomposition-tree form

Consider any finite rooted balanced composition tree. At an internal node `v`, let the local balanced gate be `G_v`. For a child edge `e=(v,i)` define its local transmission weight as `Inf_i(G_v)`. Let

\[
w(v):=\prod_{e\text{ on the root-to-}v\text{ path}} \operatorname{Inf}_e,
\qquad w(\mathrm{root})=1.
\]

Iterating Theorem 1.1 gives the exact source-exact telescopes

\[
\boxed{D(F)=\sum_v w(v)D(G_v)},
\qquad
\boxed{H(F)=\sum_v w(v)H(G_v)},
\tag{2.1}
\]

where character nodes contribute zero to both sums. Hence

\[
\boxed{c(F)=\sum_v \lambda_v c(G_v)},
\qquad
\lambda_v={w(v)D(G_v)\over D(F)},
\qquad
\lambda_v\ge0,\quad\sum_v\lambda_v=1.
\tag{2.2}
\]

### Corollary 2.1 (composition-prime localization)

Every positive-defect decomposable balanced gate has

\[
\min_v c(G_v)\le c(F)\le\max_v c(G_v).
\tag{2.3}
\]

Therefore any balanced-center counterexample above a proposed threshold localizes to a factor at least as bad. Recursing a nontrivial decomposition, a minimal-arity threshold violation must be composition-prime.

More generally, closing a family of balanced gates under arbitrary disjoint balanced substitution **cannot increase the supremum of the balanced-center margin** beyond the supremum already present among its composition-prime factors.

### Corollary 2.2 (equality rigidity)

If `c(F)=c_*` equals the maximum factor margin, then every factor with positive tree weight `w(v)D(G_v)>0` must itself have `c(G_v)=c_*`. Any positive-weight factor with smaller margin makes the root margin strictly smaller.

This is useful for extremizer classification: decomposition is neutral only when every positive-defect component is already extremal at the same center margin.

## 3. Newest compatible other-account result and how it changes the argument

I consumed fleet03/B13's newest compatible result

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260922T020124Z-fixed-level-tail-equivalence/REPORT.md`

(blob `59444ae2d823ebfdbb86cd84cde1a3cc88cf0a54`). It proves that for every fixed Fourier cutoff `r`, controlling only the tail `H_{>r}` at constant `C` is already equivalent, constant-for-constant, to full FEI. Its mechanism is balanced self-composition: a fixed gate obstruction can be pushed above every fixed Fourier prefix while preserving its support-deficit ratio.

That theorem changes the role of composition in the present argument. Theorem 1.1 shows that **decomposition is not the origin of a larger balanced-center obstruction**: the center margin is exactly a convex average of factor margins and therefore localizes to a composition-prime factor. Fleet03/B13 shows simultaneously that once a prime obstruction exists, **decomposition is an amplifier/transporter** that can bury the same obstruction arbitrarily high in Fourier level. Combined:

> search for the source of a balanced-center obstruction among composition-prime gates; do not expect a fixed low-level Fourier truncation to remove an obstruction once found.

This is a structural reduction, not a universal FEI proof.

## 4. Decisive finite check

I independently checked the heterogeneous identities on all 70 balanced three-input outer truth tables and one representative of each of the five distinct `(H,I)` types among balanced three-input inner gates, for every ordered inner triple. This is

\[
70\cdot5^3=8750
\]

nine-variable heterogeneous compositions.

The checker returned:

- `status=PASS`;
- exact maximum influence-identity error `0`;
- exact maximum defect-identity error `0`;
- maximum entropy-identity absolute error `0` in the enumerated dyadic cases;
- maximum `M_{6.4548}` identity floating residual `3.55271367880050093e-15`.

The analytic proof above does not depend on this finite check; the checker is a falsification/sanity harness for the heterogeneous formula.

## 5. What this resolves, and what remains open

**Resolved at the balanced center:** arbitrary disjoint balanced decomposition cannot create a new larger gate-margin obstruction than its prime factors. A minimal-arity balanced-center obstruction is composition-prime, and a whole decomposition tree carries an exact nonreusing defect-weighted margin ledger.

**Not resolved:** the all-bias all-gate inequality `(G)`. Biased inner outputs are not unbiased signs, and the clean Fourier-support decoding/defect convexity above does not by itself control the full `Gamma(p)` terms. This report therefore does **not** claim a finite universal FEI constant.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.

The earlier fleet04/B18 mixed-curvature conservation and exact zero-defect classification are preserved unchanged; nothing here replaces the `p_{ik}+4o_{ik}` bookkeeping or charges a small cube-measure error by ambient dimension.

## 6. Suggested next move

Use Corollary 2.1 as a pruning rule for the owner-selected all-gate program: balanced-center searches need only composition-prime gates. Then attack the genuinely missing step, a **biased** analogue of the convexity law or a finite-cap potential inequality on composition-prime gates. Fleet03/B13's tail-equivalence theorem warns that a proof which only separates finitely many low Fourier levels cannot lower the universal constant.

No novelty or publication-priority claim is made.
