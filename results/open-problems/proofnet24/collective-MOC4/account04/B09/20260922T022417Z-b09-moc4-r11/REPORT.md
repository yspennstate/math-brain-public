# MOC4 account04/B09 — flat-pair Haar-twirl permutation lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus-de Oliveira target  
**Worker:** account04/B09  
**Candidate:** `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; the entire flat row/column pair branch is closed exactly. The parent MOC4 target remains **OPEN** because the pair-strict interior branch remains unpaid.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and current complete lead state

For all complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.\tag{MOC4}
\]

The newest complete campaign-lead report present at the start and rechecked during this run is **account03/B07**, run `20260922T013930Z-account03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It keeps MOC4 open, refutes a zero-entry common-subset-permutation lift, and identifies the zero-face support branch plus the pair-strict interior branch as the surviving split.

This run directly consumes the named OTHER-account result **account01/B07**, run `20260922T020412Z-b07-moc4-r11`, report blob `f569427535050fa80aa4fa079c380b1e3035c68f`, candidate `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`. That report gives the exact `SO(6)` block objective and the complete first-order stationarity equations for a genuine support maximizer. It leaves, on the pair-strict interior, the exact six-witness inequality

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le \max_{\rho\in S_3}\{c_\rho-2m_\rho(K)\}.\tag{I}
\]

I also apply the exact pair-flat theorem **account04/B08**, `MOC4-PAIR-FLAT-BOUNDARY-v1`, report blob `3c71dc6a046f699b3248957d660b2c02fe968efb`: at a global support maximizer, equality with the opposite endpoint on one genuine row/column `SU(2)` pair orbit forces the *entire* pair orbit to have the same support value. Its previous conclusion was that such a flat orbit can be rotated to a zero-entry representative. The newer account04/B08 report `MOC4-ZERO-FACE-GAP-v1`, blob `692bad9f279332213744ef9ccfc47ff126e6ccf4`, shows that the zero-entry rank-one factorization by itself is not enough and that an `X`-dependent payment is necessary if one insists on the zero-face route.

The result below bypasses that unpaid zero-face inequality completely: the Haar average of the **whole exterior-minor data** along a row/column `SU(2)` pair orbit has an exact classical permutation lift. Therefore a flat pair orbit can never be support-violating.

## 2. Exterior-minor notation

After diagonalizing `A`, write

\[
A=\operatorname{diag}(a),\qquad B=U\operatorname{diag}(b)U^*,\qquad U\in U(4).
\]

For equal-cardinality subsets `S,T` put

\[
q^{(k)}_{S,T}=|\det U[S,T]|^2,\qquad |S|=|T|=k.
\]

The exact exterior expansion is

\[
D_U(a,b):=\det(A+B)
=\sum_{S\subset[4]}a_{S^c}\sum_{|T|=|S|}b_T q^{(|S|)}_{S,T}.\tag{1}
\]

For `k=1`, `q^{(1)}_{\{i\},\{j\}}=p_{ij}=|u_{ij}|^2`. For `k=3`, Jacobi complementarity gives

\[
q^{(3)}_{S,T}=p_{S^c,T^c}.\tag{2}
\]

Thus matching the one-set and two-set squared-minor data matches every layer of (1).

## 3. Haar twirl on one row pair

Fix the row pair `I={1,2}` and let `G in SU(2)` act on these two rows. Let an overbar denote Haar averaging over that embedded `SU(2)` orbit.

For the one-set data,

\[
\bar p_{1j}=\bar p_{2j}=\frac{p_{1j}+p_{2j}}2,\qquad
\bar p_{3j}=p_{3j},\quad \bar p_{4j}=p_{4j}.\tag{3}
\]

For two-set row labels, the row subset `I` and its complement `I^c={3,4}` are invariant in `\Lambda^2`, while each pair of cross row labels forms an `SU(2)` doublet. Hence

\[
\bar q_{I,T}=q_{I,T},\qquad
\bar q_{I^c,T}=q_{I^c,T},\tag{4}
\]

and, for example,

\[
\bar q_{\{1,3\},T}=\bar q_{\{2,3\},T}
=\frac{q_{\{1,3\},T}+q_{\{2,3\},T}}2,\tag{5}
\]

with the analogous identity for rows `4`.

The theorem is that this twirled full minor-square vector is always classical.

## 4. Theorem — exact permutation lift of the pair twirl

### `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`

For every `U in U(4)` and every row pair `I`, the Haar-twirled exterior-minor data `\bar q` lie in the convex hull of the exterior-minor data of the 24 permutation matrices. Equivalently, there is a probability law `\mu` on `S_4` such that simultaneously

\[
\bar p_{ij}=\Pr_{\mu}[\sigma(i)=j]\tag{6}
\]

and for every two-row set `S` and two-column set `T`,

\[
\bar q_{S,T}=\Pr_{\mu}[\sigma(S)=T].\tag{7}
\]

Consequently all `k=3` marginals also match by complements.

### Proof

Relabel so `I={1,2}`. Put

\[
q_{jk}:=q^{(2)}_{\{1,2\},\{j,k\}},\qquad 1\le j<k\le4.
\]

The `2 x 4` matrix formed by rows `1,2` has orthonormal rows. Cauchy--Binet plus the one-column inclusion identity gives

\[
\sum_{k\ne j}q_{jk}=p_{1j}+p_{2j}.\tag{8}
\]

Orient every unordered edge symmetrically:

\[
x_{j\to k}=x_{k\to j}=\frac{q_{jk}}2.\tag{9}
\]

Then (8) says

\[
\sum_{k\ne j}x_{j\to k}=\bar p_{1j}=\bar p_{2j}.\tag{10}
\]

For the bottom row pair `{3,4}`, define unordered edge masses

\[
r_{jk}:=q^{(2)}_{\{3,4\},\{j,k\}}.
\]

Jacobi complementarity gives

\[
r_{jk}=q_{\{1,2\},\{j,k\}^c}.\tag{11}
\]

We need a fractional orientation `z_{j\to k}` of these bottom edge masses with

\[
z_{j\to k}+z_{k\to j}=r_{jk},\qquad
\sum_{k\ne j}z_{j\to k}=p_{3j}.\tag{12}
\]

The standard fractional-orientation/max-flow criterion requires

\[
r(E(S))\le p_3(S)\tag{13}
\]

for all vertex subsets `S`, with equality for the full set. These inequalities follow directly from the true unitary.

- `|S|=1`: trivial.
- `S={j,k}`: Hadamard's determinant bound gives
  \[
  r_{jk}\le(p_{3j}+p_{3k})(p_{4j}+p_{4k})\le p_{3j}+p_{3k}.
  \]
- `|S|=3`, with complement `{\ell}`: by the two-row inclusion identity,
  \[
  r(E(S))=1-\sum_{k\ne\ell}r_{\ell k}
  =1-p_{3\ell}-p_{4\ell}\le1-p_{3\ell}=p_3(S).
  \]
- `S=[4]`: both sides equal `1`.

Thus an orientation `z` satisfying (12) exists, with no genericity or positivity hypothesis.

Now fix a permutation `\sigma`, let

\[
J=\{\sigma(1),\sigma(2)\},
\]

and define, whenever `q_J>0`,

\[
\mu(\sigma)
=\frac{x_{\sigma(1)\to\sigma(2)}
       z_{\sigma(3)\to\sigma(4)}}{q_J};\tag{14}
\]

if `q_J=0`, set all four permutations with top unordered image pair `J` to mass zero. This is consistent because then, by (11), the complementary bottom edge mass is also zero.

For fixed top unordered pair `J`, summing (14) over its two top orientations and the two bottom orientations gives

\[
\frac{q_J\,r_{J^c}}{q_J}=q_J,
\]

so `\sum_\sigma\mu(\sigma)=1`. Summing only over bottom orientations shows that the ordered top-pair law is exactly `x`; summing only over top orientations shows that the ordered bottom-pair law is exactly `z`. Therefore all four one-point marginals equal `\bar p`.

The top two-set marginal is `q_J` by construction and the bottom two-set marginal is `r`. It remains to identify the four cross row-pair marginals. The law `\mu` is invariant under swapping rows `1,2` because `x_{j\to k}=x_{k\to j}`. Hence, for every column pair `T`,

\[
Q^\mu_{\{1,3\},T}=Q^\mu_{\{2,3\},T}.\tag{15}
\]

For every permutation law, the elementary inclusion identity

\[
Q^\mu_{\{1,3\},T}+Q^\mu_{\{2,3\},T}
+Q^\mu_{\{3,4\},T}
=\sum_{j\in T}P^\mu_{3j}\tag{16}
\]

holds pointwise before averaging: if row `3` lands in `T`, exactly one of the other three rows lands at the other element of `T`. Equations (15)-(16) therefore determine the cross marginal uniquely:

\[
Q^\mu_{\{1,3\},T}
=Q^\mu_{\{2,3\},T}
=\frac12\left(\sum_{j\in T}\bar p_{3j}-r_T\right).\tag{17}
\]

The Haar-twirled true-unitary data satisfy the same inclusion identity and the same row-pair symmetry (5), so their cross marginals equal (17). Repeating with row `4` matches the other two cross pairs. Thus every two-set marginal agrees with `\bar q`, proving (7).

By (2), the three-set marginals are complements of the one-set marginals for both the true-unitary twirl and every permutation. Therefore all exterior layers match. QED.

## 5. Corollary — the flat-pair branch is impossible for a violating support maximizer

Fix any complex spectra `a,b` and support direction `eta`. Let

\[
h_\eta(U)=\Re\bigl(\eta D_U(a,b)\bigr).
\]

Suppose a row-pair orbit through `U` is flat:

\[
h_\eta(GU)=h_\eta(U)\qquad\text{for every embedded }G\in SU(2).\tag{18}
\]

Average (1) over this orbit. By the theorem there is a probability law `\mu` on `S_4` such that

\[
\int_{SU(2)}D_{GU}(a,b)\,dG
=\sum_{\sigma\in S_4}\mu(\sigma)
  \prod_i(a_i+b_{\sigma(i)}).\tag{19}
\]

Taking the support functional and using flatness,

\[
\begin{aligned}
h_\eta(U)
&=\Re\left(\eta\int D_{GU}(a,b)\,dG\right)\\
&=\sum_\sigma\mu(\sigma)
  \Re\left(\eta\prod_i(a_i+b_{\sigma(i)})\right)\\
&\le\max_{\sigma\in S_4}
  \Re\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\end{aligned}\tag{20}
\]

Thus a flat row pair can **never** occur at a support-violating point. The column-pair statement follows by the identical argument applied to `U^*` (equivalently exchange the roles of `a,b`).

Combining this with account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1` closes the branch that had previously been sent to a zero-entry representative. One no longer needs to prove `MOC4-ZERO-FACE-SUPPORT-v1` merely to dispose of a flat-pair violating maximizer: averaging the flat orbit already lands exactly in the permutation hull at the level needed by the support functional.

This is stronger and cleaner than the zero-entry common-lift attempt refuted by the campaign lead. It does **not** assert that an individual zero-entry unitary has a common permutation lift; it asserts a common lift only after the source-valid `SU(2)` Haar twirl forced by the flat-orbit hypothesis.

## 6. Updated compact end-to-end chain and exact remaining implication

The current conditional proof chain can now be shortened.

1. Repeated-spectrum and common-reducing-block boundaries are already closed by account02/B08; individual singularity can be removed by its opposite scalar-shift gauge.
2. Take a hypothetical MOC4 support violation and a global support maximizer.
3. If any genuine row/column pair orbit is non-strict, account04/B08 makes that orbit flat; (20) then proves the target support inequality, contradiction.
4. Therefore every hypothetical violating global maximizer is **strict on all twelve row/column pair spheres**.
5. At such a pair-strict maximizer, consume account01/B07's exact `SO(6)` block representation and complete stationarity equations. The first remaining target-level implication is precisely its `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`, equation (I), restricted to genuine global maximizers (not arbitrary stationary saddles).

So after this run there is no unpaid flat/zero branch in the contradiction chain. The only remaining universal branch is the pair-strict global-maximizer interior.

The theorem includes all degeneracies on the flat branch: zeros among the minors merely give zero edge masses in (14), and no inverse, strict positivity, simple spectrum, or nonsingular determinant is used. Thus no separate limiting argument is required for this branch.

## 7. Exact verifier

`verify_flat_pair_twirl.py` uses only Python standard-library `fractions.Fraction`. On the exact rational orthogonal datum used in current zero-face work it:

- verifies orthogonality exactly;
- forms the row-pair Haar-twirled one- and two-set data;
- finds an exact feasible bottom fractional orientation;
- constructs the 24-state law `mu`;
- checks all 16 one-point marginals and all 36 two-set marginals exactly;
- checks a full exterior-power determinant expansion for a simple rational spectral pair against the 24-vertex mixture.

Captured output in `VERIFICATION.txt` is:

```text
PASS exact orthogonality
PASS twirled one-point marginals
PASS all 36 twirled two-set marginals
PASS 24-state probability law, total = 1
bottom_orientation = [0, 9216/15625, 784/15625, 0, 512/15625, 0]
positive_mu_count = 16
exterior_average = -37876916/390625
permutation_mixture = -37876916/390625
PASS full exterior-power twirl lift
```

The finite verifier is only a check of the algebra on one exact source datum; the theorem above is the proof for arbitrary `U in U(4)`.

## 8. Source/provenance and non-claims

Internal exact sources consumed:

- account03/B07 `20260922T013930Z-account03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`;
- **OTHER-account partner** account01/B07 `20260922T020412Z-b07-moc4-r11`, report blob `f569427535050fa80aa4fa079c380b1e3035c68f`;
- OTHER-account account02/B08 repeated-face/fractional-orientation work, including `MOC4-DOUBLE-EIGENVALUE-LIFT-v1` as summarized in its r11 boundary report;
- account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, blob `3c71dc6a046f699b3248957d660b2c02fe968efb`;
- account04/B08 `MOC4-ZERO-FACE-GAP-v1`, blob `692bad9f279332213744ef9ccfc47ff126e6ccf4`.

Campaign literature/status references remain the scoped sources recorded in `TARGETS.md`: S. W. Drury, *The external vertices conjecture in case n=4*, ELA 11 (2004), DOI `10.13001/1081-3810.1131`; N. Bebiano and J. da Providencia, *Revisiting the Marcus-de Oliveira Conjecture*, Mathematics 13 (2025), 711, DOI `10.3390/math13050711`; and J. I. Mulero-Martinez, *A variational framework for determinantal inequalities of normal matrices: Successes and obstructions*, LAA 740 (2026), 19--38, DOI `10.1016/j.laa.2026.03.019`.

**Non-claims:** full MOC4 is not yet proved; the pair-strict interior inequality remains open. No individual zero-entry common lift is claimed. No arbitrary bistochastic surrogate is used. No benchmark material, held-out answer, encryption key, credential, scheduler identifier, machine path, email/Drive material, public posting, paid API/model, Codex, remote workflow, or permission bypass was used.
