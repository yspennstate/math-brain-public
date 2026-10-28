# MOC4 account02/B08 — exact boundary support faces for repeated spectra and common reducing blocks

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B08  
**Run:** `B08-20260922T023618Z-7e3c2a`  
**Candidate:** `MOC4-BOUNDARY-SUPPORT-FACE-REDUCTION-v3`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source-bound inputs

For every pair of complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]


This run read and applies the following exact completed peer artifacts at science snapshot `8113b8fa4fa802e11d1777202ce1bab7d50dba61`:

1. **Campaign lead account03/B07 r11**, `proofnet24/collective-MOC4/account03/B07/20260922T013930Z-account03-B07-MOC4-r11/REPORT.md`, blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It gives a true-unitary zero-entry counterexample to the proposed common second-compound permutation lift. Hence no generic zero-entry boundary argument below is allowed to smuggle in that false lift.
2. **Campaign lead account03/B07 r12**, `MOC4-PARITY-SLACK-v1`, `proofnet24/collective-MOC4/account03/B07/20260922T012650Z-account03-B07-MOC4-r12/REPORT.md`, blob `5e5e58b067d5e546e34a97119893ebe5a7198881`. It reduces the generic core to the exact six-fiber signed standard-representation inequality and the structured parity-slack payment.
3. **Named partner account03/B09 r11**, `proofnet24/collective-MOC4/account03/B09/20260922T011607Z-account03-B09-MOC4-r11/REPORT.md`, blob `2579d56a3defc034105c55c87e1c6f7830725d1d`. It proves complementary-minor orientation rigidity and the `6 kappa` support certificate: if the pair-class assignment has a unique maximizer with gap `gamma` and coupling mismatch `kappa`, then `gamma >= 6 kappa` already proves the exact MOC4 support inequality for every unitary.
4. **This worker's preceding result**, `MOC4-REPEATED-MINIMAL-LIFT-v2`, `proofnet24/collective-MOC4/account02/B08/B08-20260922T014005Z-27fb8b/REPORT.md`. It proves all repeated-spectrum pairs by a minimal fractional orientation lift and gave a sufficient open collar assuming all entries of the two nonrepeated rows are nonzero. An earlier B08 report proved a `2+2` common-block collar but explicitly left the `1+3` collar unresolved.

The new work has two parts: (i) an **exact**, not merely sufficient, support description for the repeated-face lift in terms of tight Hall cuts; and (ii) a support-positive blockwise convex representation for **every proper common reducing decomposition**, including the previously missing `1+3` case.

## 2. Compact conditional end-to-end reduction after this run

The current all-pairs route is now:

1. If either spectrum is repeated, `MOC4-REPEATED-MINIMAL-LIFT-v2` gives an exact convex representation. Section 3 below identifies the exact support face of that representation and therefore the exact obstruction to an open collar.
2. If `A,B` have a nontrivial common reducing subspace, section 4 below gives an exact convex representation supported on the block-preserving permutation vertices, with strictly positive weight on every block-preserving vertex allowed by the true unitary support. This covers `1+3`, `2+2`, and refinements.
3. The exact opposite-scalar gauge `(A,B)->(A+tI,B-tI)` preserves `A+B` and every comparison vertex, so a finite choice of forbidden `t` can be avoided and the residual pair can be taken individually invertible without changing the problem.
4. Thus a hypothetical counterexample may be restricted to the simple-spectrum, individually-invertible, irreducible core. Moreover, a counterexample sequence can approach either solved boundary only through the explicit **collinear supported-face** degeneracies isolated below.
5. On the remaining generic core, named partner account03/B09 r11 gives a further exact necessary condition: whenever the pair-class maximizer is unique, a counterexample must satisfy `gamma < 6 kappa`. The lead's six-fiber/parity-slack inequality remains the exact fallback in the near-tie regime.

The first boundary-specific unpaid implication after this run is therefore not a missing representation theorem. It is the much narrower problem `MOC4-COLLINEAR-BOUNDARY-v1`: control counterexample sequences whose limiting repeated/common-block support face is one-dimensional in the complex plane.

## 3. Repeated spectrum: exact Hall-tight support face

Diagonalize `A` and write

\[
A=\operatorname{diag}(a_1,a_2,a_3,a_4),\qquad
B=U\operatorname{diag}(b_1,b_2,b_3,b_4)U^*.
\]

Assume after relabeling that `a_1=a_2`. The preceding B08 theorem defines, for unordered column pairs,

\[
r_{jk}=\left|\det U[\{3,4\},\{j,k\}]\right|^2,
\qquad p_j=|u_{3j}|^2,
\]

and proves that there exists a fractional orientation `z` satisfying

\[
z_{j\to k}+z_{k\to j}=r_{jk},\qquad
\sum_{k\ne j}z_{j\to k}=p_j.\tag{1}
\]

For any such `z`, the measure

\[
\mu_z(\sigma)=\frac12 z_{\sigma(3)\to\sigma(4)}\tag{2}
\]

is a probability measure on `S_4` and exactly represents the determinant:

\[
\det(A+B)=\sum_{\sigma\in S_4}\mu_z(\sigma)
\prod_{i=1}^4(a_i+b_{\sigma(i)}).\tag{3}
\]

The new point is to characterize **exactly which directed edges can be positive in some feasible orientation**.

For `S subset {1,2,3,4}`, let

\[
h(S):=p(S)-r(E(S)),\qquad
p(S)=\sum_{j\in S}p_j,
\]

where `r(E(S))` is the total weight of edges having both endpoints in `S`. Since (1) holds,

\[
\boxed{h(S)=\sum_{j\in S,\ k\notin S}z_{j\to k}}\tag{4}
\]

for **every** feasible orientation `z`. In particular `h(S)>=0`; these are precisely the Hall inequalities used in the preceding existence proof.

### Lemma 1 — exact admissible-arc criterion

Fix an edge `r_{jk}>0`. There exists a feasible orientation with `z_{j->k}>0` if and only if there is **no** Hall-tight set `S` with

\[
j\in S,\qquad k\notin S,\qquad h(S)=0.\tag{5}
\]

#### Proof

If a tight set as in (5) exists, (4) forces every arc leaving `S`, and in particular `j->k`, to be zero in every feasible orientation.

Conversely choose any feasible orientation `z`. If `z_{j->k}>0`, there is nothing to prove. Suppose `z_{j->k}=0`; since `r_{jk}>0`, necessarily `z_{k->j}=r_{jk}>0`. Consider the directed graph of arcs having positive `z`-mass.

If `k` is reachable from `j` along a positive directed path

`j=v_0 -> v_1 -> ... -> v_m=k`,

choose `epsilon>0` smaller than every path-arc mass and than `z_{k->j}`. Increase `z_{j->k}` by `epsilon`, decrease `z_{k->j}` by `epsilon`, and reverse `epsilon` units of mass along the path: on each path edge decrease the forward orientation by `epsilon` and increase the reverse orientation by `epsilon`. Every undirected edge total is unchanged. At `j`, the new direct arc contributes `+epsilon` to outdegree while the first path arc contributes `-epsilon`; at `k` the last reversed path arc contributes `+epsilon` while `k->j` contributes `-epsilon`; every internal path vertex receives one `+epsilon` and one `-epsilon`. Thus all outdegrees remain `p`, and the modified feasible orientation has `z_{j->k}>0`.

If `k` is not reachable from `j`, let `S` be the set reachable from `j`. Then `j in S`, `k notin S`, and by maximality no positive arc leaves `S`. Equation (4) gives `h(S)=0`, which is exactly (5). `QED`

Call a directed edge **admissible** when it satisfies Lemma 1. Because there are finitely many admissible arcs, choose for each one a feasible orientation in which that arc is positive and average all those orientations. This proves:

### Corollary 2 — simultaneous maximal support

There is one feasible orientation `z*` such that

\[
z^*_{j->k}>0\quad\Longleftrightarrow\quad j->k\text{ is admissible}.\tag{6}
\]

Nonadmissible arcs are zero in every feasible orientation by a tight cut; admissible arcs are simultaneously made positive by finite averaging.

Thus (2) gives an exact supported permutation set

\[
\Omega_{\rm rep}:=\{\sigma:\sigma(3)->\sigma(4)\text{ is admissible}\},\tag{7}
\]

with

\[
\mu_{z^*}(\sigma)>0\quad\Longleftrightarrow\quad\sigma\in\Omega_{\rm rep}.\tag{8}
\]

This strictly sharpens the previous sufficient criterion requiring all entries in rows 3 and 4 to be nonzero.

### True-unitary formulas for every possible tight cut

Because there are only four column labels, the Hall slacks are explicit unitary degeneracies.

For a singleton,

\[
h(\{j\})=|u_{3j}|^2.\tag{9}
\]

For a three-set with complement `{ell}`, the row-pair degree identity gives

\[
h([4]\setminus\{\ell\})=|u_{4\ell}|^2.\tag{10}
\]

For a two-set `S={j,k}`, let `x=(u_{3j},u_{3k})` and `y=(u_{4j},u_{4k})`. Lagrange's identity gives

\[
r_{jk}=\|x\|^2\|y\|^2-|\langle x,y\rangle|^2,
\]

hence

\[
\boxed{
h(S)=\|x\|^2(1-\|y\|^2)+|\langle x,y\rangle|^2.}
\tag{11}
\]

So the support collapse is described directly by zeros/orthogonality/concentration in the **same true unitary**. No arbitrary bistochastic surrogate occurs.

### Corollary 3 — exact repeated-face collar criterion

Let

\[
v_\sigma=\prod_i(a_i+b_{\sigma(i)}).
\]

If the supported set `{v_sigma: sigma in Omega_rep}` is not collinear in `C`, then `det(A+B)` is an ordinary interior point of its convex hull, hence of the full 24-vertex hull.

Indeed (3) and (8) express the determinant with strictly positive coefficient on every generator in the supported face. If a proper supporting line passed through that convex combination, positivity would force every supported generator onto the line, contradicting noncollinearity. Continuity of the determinant and of all 24 vertices then gives an open MOC4-safe neighborhood, including perturbations that split the repeated eigenvalue.

Therefore any counterexample sequence converging to a repeated-spectrum point must have a **collinear maximal Hall-admissible support face**. This is an exact replacement for the older sufficient list of zero-entry/zero-minor degeneracies.

## 4. Every proper common reducing block: support-positive exact representation

Now suppose `A,B` have a nontrivial common reducing decomposition. Choose a common orthogonal decomposition into blocks and diagonalize the restrictions of `A` and `B` inside each block. After relabeling spectral coordinates, the relative unitary has block form

\[
U=\operatorname{diag}(V_1,\ldots,V_m),\qquad n_s:=\dim V_s\le3,
\tag{12}
\]

because every block is proper and the ambient dimension is four. Let `I_s` and `J_s` be the row and column spectral labels of block `s`, and put

\[
P^{(s)}=(|v^{(s)}_{ij}|^2)_{i\in I_s,j\in J_s}.
\]

Each `P^(s)` is doubly stochastic.

### Lemma 4 — in dimensions at most three, any Birkhoff law is determinant-exact

Let `n<=3`, `V in U(n)`, `P=|V|^2`, and let

\[
P=\sum_{\tau\in S_n}\lambda_\tau P_\tau,
\qquad \lambda_\tau\ge0,\quad\sum\lambda_\tau=1.\tag{13}
\]

Then for arbitrary complex spectral lists `alpha_1,...,alpha_n` and `beta_1,...,beta_n`,

\[
\boxed{
\det(\operatorname{diag}(\alpha)+V\operatorname{diag}(\beta)V^*)
=\sum_\tau\lambda_\tau\prod_i(\alpha_i+\beta_{\tau(i)}).
}\tag{14}
\]

#### Proof

Expand the determinant by principal minors and Cauchy–Binet. The coefficient attached to row set `I` and column set `J`, `|I|=|J|`, is `|det V[I,J]|^2`.

For `|I|=0,n` the coefficient is automatic. For `|I|=1`, it is exactly `P_{ij}`, reproduced by (13) as `Pr[tau(i)=j]`. When `n<=3`, the only remaining nontrivial size is `|I|=n-1`. Jacobi complementarity for a unitary gives

\[
|\det V[I,J]|^2=|v_{i^c,j^c}|^2=P_{i^c,j^c},\tag{15}
\]

where `I^c={i^c}` and `J^c={j^c}`. But the permutation event `tau(I)=J` is equivalent to `tau(i^c)=j^c`, whose probability under (13) is exactly the same entry of `P`. Thus every coefficient in the Cauchy–Binet expansion agrees with the expectation of the permutation product. `QED`

This is stronger than merely invoking the known `n<=3` MOC theorem: it identifies a whole family of exact representing measures determined only by the true one-point unitary marginals.

### Lemma 5 — a Birkhoff law positive on every supported block permutation

For a doubly stochastic matrix `P`, let

\[
\Omega(P):=\{\tau\in S_n:P_{i,\tau(i)}>0\text{ for every }i\}.\tag{16}
\]

There is a decomposition (13) with `lambda_tau>0` for **every** `tau in Omega(P)` and `lambda_tau=0` outside `Omega(P)`.

#### Proof

Birkhoff's theorem implies every positive entry of `P` belongs to at least one permutation in some decomposition, so the union of the permutation graphs in `Omega(P)` is exactly the positive support of `P`. Let `Q` be the average of `P_tau` over `Omega(P)`. Then `Q_ij>0` exactly where `P_ij>0`. Choose

\[
0<\varepsilon<\min_{P_{ij}>0}\frac{P_{ij}}{Q_{ij}}.
\]

Then `P-epsilon Q` is entrywise nonnegative and has every row and column sum `1-epsilon`; hence

\[
P'=\frac{P-\varepsilon Q}{1-\varepsilon}
\]

is doubly stochastic. Birkhoff-decompose `P'`. In

\[
P=\varepsilon Q+(1-\varepsilon)P',
\]

every permutation in `Omega(P)` already has positive coefficient `epsilon/|Omega(P)|`. `QED`

Apply Lemmas 4–5 to every block. Let `lambda^(s)` be support-positive on `Omega(P^(s))`. The block determinant is

\[
D_s=\sum_{\tau_s\in\Omega(P^{(s)})}\lambda^{(s)}_{\tau_s}
\prod_{i\in I_s}(a_i+b_{\tau_s(i)}).
\tag{17}
\]

Since `A+B` is block diagonal,

\[
\det(A+B)=\prod_sD_s.
\]

Multiplying (17) gives a probability measure on the block-preserving global permutations

\[
\Omega_{\rm blk}:=\prod_s\Omega(P^{(s)}),\tag{18}
\]

with

\[
\boxed{
\det(A+B)=\sum_{\sigma\in\Omega_{\rm blk}}\mu_{\rm blk}(\sigma)v_\sigma,
\qquad
\mu_{\rm blk}(\sigma)=\prod_s\lambda^{(s)}_{\sigma|_{I_s}}>0.
}\tag{19}
\]

### Corollary 6 — common-block collar, including `1+3`

If `{v_sigma:sigma in Omega_blk}` is not collinear, then (19) puts the determinant in the ordinary interior of its supported block-permutation hull and therefore in the interior of the full 24-vertex hull. Continuity supplies an open MOC4-safe neighborhood even when nearby pairs no longer have a common reducing subspace.

This proves the previously missing `1+3` collar and simultaneously subsumes the older `2+2` collar. Zero entries inside a block are harmless unless they reduce the **supported block-permutation products themselves** to a collinear set.

## 5. Combined boundary reduction and partner integration

Sections 3–4 turn two solved boundary classes into exact support-face statements.

**Repeated boundary.** The maximal support is `Omega_rep`, determined by the tight Hall cuts (9)–(11). A counterexample sequence can meet this boundary only where its supported permutation products are collinear.

**Common-block boundary.** The maximal blockwise support is `Omega_blk`, determined by positive entries in the actual block unitaries. A counterexample sequence can meet this boundary only where the block-preserving supported products are collinear.

These statements are compatible with, and materially use, named partner account03/B09 r11. In the residual simple-spectrum irreducible core, its exact theorem removes every unique-pair-gap support direction with `gamma >= 6 kappa`; any counterexample in that regime must satisfy `gamma < 6 kappa`. The present run supplies the complementary boundary exclusion: generic approaches to repeated/common-block faces are impossible unless the corresponding supported product face loses planar dimension.

They are also compatible with the latest lead r11 no-go result. The false assertion refuted there is a **generic** common subset-permutation lift for all second-compound marginals at a zero-entry unitary. The measures (2) and (19) are used only where repeated spectral coefficients or genuine reducing-block factorization collapse the required marginal data. Nothing here extends those special representations to the generic zero-entry core.

## 6. What failed / what remains unpaid

1. The lead's exact rational zero-entry witness rules out using the old common-compound-lift shortcut on a generic zero-entry boundary. I did not attempt to repair that false statement.
2. The exact support-face theorems above do **not** prove an open collar when the supported products are collinear. In that case a positive representing measure may lie only in a line segment, so the two-dimensional support margin can vanish under perturbation.
3. The result does not pay the lead's generic six-fiber parity-slack implication and does not improve the partner's constant `6` in the `gamma >= 6 kappa` certificate.
4. No numerical experiment or arbitrary bistochastic relaxation is used. There is therefore no code/output artifact in this run: the new claims are theorem-sized and the proofs are written above.

The next boundary lemma is now sharply named:

> **`MOC4-COLLINEAR-BOUNDARY-v1`.** Classify or control simple-spectrum irreducible counterexample sequences whose limit is a solved repeated/common-block pair but whose maximal supported permutation-product face is collinear. Any useful proof must exploit the structured spectral products or the lead/partner exact support functional; a common compound-marginal lift is forbidden by the lead's true-unitary counterexample.

## 7. Status and nonclaims

- `MOC4-REPEATED-TIGHT-CUT-SUPPORT-v3`: **PROVED here**, conditional only on the preceding already-proved minimal repeated-face representation (equations (1)–(3), whose proof is in the cited prior B08 report).
- `MOC4-COMMON-BLOCK-SUPPORT-POSITIVE-v1`: **PROVED here** for every proper common reducing decomposition in dimension four.
- `MOC4-BOUNDARY-SUPPORT-FACE-REDUCTION-v3`: **ESSENTIAL_STEP_APPLIED** as a reduction/collar theorem.
- Full MOC4: **OPEN**. This is not a full-proof candidate and has not received the two independent end-to-end reviews required for promotion.
- No benchmark work or benchmark gold was read or modified.
- No brain-assisted mathematical claim is made; execution remained `WITHOUT_VERIFIED_BRAIN`.
