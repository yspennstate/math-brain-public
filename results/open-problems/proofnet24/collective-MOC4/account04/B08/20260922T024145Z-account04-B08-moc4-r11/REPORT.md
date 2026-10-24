# MOC4 account04/B08 — pair-symmetrized common lift closes every flat pair branch

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account04/B08  
**Candidate:** `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; the flat/tied-pair branch is eliminated from any support violation. The parent MOC4 target remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

## 1. Source-exact target and live inputs

The target is

\[
\det(A+B)\in \operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\tag{MOC4}
\]

for every complex normal \(4\times4\) pair, including repeated spectra and singular cases.

This run used the following exact campaign inputs.

1. **Campaign lead account03/B07**, run `20260922T013930Z-account03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It consumes this worker's earlier pair-flat reduction and proves that even on a true-unitary zero-entry face a common \(S_4\) lift of all squared two-minor marginals can fail.
2. **This worker's preceding run**, `MOC4-ZERO-FACE-GAP-v1`, report blob `692bad9f279332213744ef9ccfc47ff126e6ccf4`, derived an exact \(X\)-aware zero-face gap identity and refuted the shortcut that discards the fiber-gap term.
3. **Assigned partner account01/B09**, run `20260922T021947Z-account01-B09-MOC4-r11`, report blob `df0d53b141e90d9da3e278819a1e90966f897aff`, candidate `MOC4-RANK2-STATIONARY-ROOF-FAMILY-v1`. It gives an exact continuous rank-two family with a dense nonmonomial true unitary and all twelve strict pair-Rayleigh conditions, while the MOC4 hull bound still holds.
4. **account01/B07**, `MOC4-MIXED-ASSIGNMENT-v1` and its current \(X\)-aware refinement, supplies the exact support expansion in the common \(P,R,D\) variables:
\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}\left(\langle S_\sigma,K\rangle+
\frac12\langle |S_\sigma|,X\rangle\right).\tag{SR}
\]

The live boundary question was whether a support-violating global maximizer can have a flat row/column \(U(2)\) pair orbit. The answer below is **no**, without solving the zero-entry support problem.

## 2. Pair-symmetrized common lift

Let \(U=(u_{ij})\in U(4)\), and let \(\tau\) transpose any two rows. Write \(P(U)=(|u_{ij}|^2)\), let \(R(U)\) be the \(3\times3\) complementary-pair transport, and let \(D(U)\) be the signed standard block, a fixed linear transform of \(P\). Set
\[
\bar P=\frac{P(U)+P(\tau U)}2,\qquad
\bar R=\frac{R(U)+R(\tau U)}2,\qquad
\bar D=\frac{D(U)+D(\tau U)}2.
\]

### Theorem 1 — `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`

For every \(U\in U(4)\) and every transposition \(\tau\) of two rows, there is a probability law \(\lambda=(\lambda_\sigma)_{\sigma\in S_4}\) such that
\[
\boxed{\bar P=\sum_{\sigma}\lambda_\sigma P_\sigma},\qquad
\boxed{\bar R=\sum_{\sigma}\lambda_\sigma R_\sigma},\qquad
\boxed{\bar D=\sum_{\sigma}\lambda_\sigma S_\sigma}.\tag{1}
\]
Here \(R_\sigma=|S_\sigma|\). The same statement holds for a transposition of two columns.

This is an averaged common lift. It does not contradict the campaign's exact counterexamples to a common lift for a single unitary.

## 3. Proof by an oriented rank-two projection flow

By relabelling rows, suppose the swapped rows are \(0,1\), with complementary rows \(2,3\). Put
\[
x=(u_{20},u_{21},u_{22},u_{23}),\qquad
y=(u_{30},u_{31},u_{32},u_{33}).
\]
These are orthonormal. Define
\[
a_j=|x_j|^2,\qquad b_j=|y_j|^2,\qquad q_{jk}=|x_jy_k-x_ky_j|^2=q_{kj}.\tag{2}
\]

### Lemma 2 — oriented minor split
There are \(t_{jk}\ge0\), \(j\ne k\), such that
\[
t_{jk}+t_{kj}=q_{jk},\qquad
\sum_{k\ne j}t_{jk}=a_j,\qquad
\sum_{k\ne j}t_{kj}=b_j.\tag{3}
\]

**Proof.** Expanding the minors and using orthonormality gives
\[
\sum_{k\ne j}q_{jk}=a_j+b_j.\tag{4}
\]
Let \(d_j=a_j-b_j\). It suffices to find an antisymmetric flow \(f_{jk}=-f_{kj}\) with
\[
|f_{jk}|\le q_{jk},\qquad \sum_{k\ne j}f_{jk}=d_j,\tag{5}
\]
then put \(t_{jk}=(q_{jk}+f_{jk})/2\).

The finite max-flow/min-cut criterion reduces (5) to the cut inequalities
\[
\left|\sum_{j\in S}d_j\right|\le\sum_{j\in S,k\notin S}q_{jk}.\tag{6}
\]
For completeness, direct each undirected edge both ways with capacity \(q_{jk}\), attach positive supplies and negative demands to source and sink, apply max-flow/min-cut, then cancel opposite directed flows.

Write
\[
A=\sum_{j\in S}|x_j|^2,\quad B=\sum_{j\in S}|y_j|^2,\quad C=\sum_{j\in S}x_j\overline{y_j}.
\]
Orthogonality makes the complementary cross sum \(-C\), and expansion gives
\[
Q(S):=\sum_{j\in S,k\notin S}q_{jk}=A(1-B)+(1-A)B+2|C|^2.\tag{7}
\]
Also \(\sum_{j\in S}d_j=A-B\). If \(A\ge B\),
\[
Q(S)-(A-B)=2B(1-A)+2|C|^2\ge0,
\]
and if \(B\ge A\),
\[
Q(S)-(B-A)=2A(1-B)+2|C|^2\ge0.
\]
Thus every cut passes and Lemma 2 follows. ∎

For each ordered pair \(j\ne k\), give total mass \(t_{jk}\) to permutations with \(\sigma(2)=j,\sigma(3)=k\), splitting it equally between the two assignments of the remaining columns to rows 0 and 1. The masses sum to one. The row-2 and row-3 one-point marginals are \(a,b\). For row 0,
\[
\Pr[\sigma(0)=\ell]=\frac12(1-a_\ell-b_\ell)=\frac12(|u_{0\ell}|^2+|u_{1\ell}|^2),\tag{8}
\]
and row 1 is the same. Hence the law has marginal \(\bar P\).

For the complementary-pair layer, the row-pair class \(\{0,1\}|\{2,3\}\) is fixed by the swap. Under the constructed law its probability of a target pair class is the sum of the corresponding \(q_{jk}\). By the unitary complementary-minor identity
\[
|\det U[I,J]|=|\det U[I^c,J^c]|,\tag{9}
\]
this is exactly the first row of \(R(U)\). Thus \(R_\lambda:=\sum\lambda_\sigma R_\sigma\) and \(\bar R\) have the same first row. Both are doubly stochastic. Row-swap invariance makes the other two rows of each matrix equal; a \(3\times3\) doubly stochastic matrix with its last two rows equal is uniquely determined by the first row. Hence \(R_\lambda=\bar R\). The \(D\) identity follows from linearity in \(P\). The column statement follows by applying the row theorem to \(U^*\). ∎

## 4. Support consequence: no violating maximizer has a tied pair

Fix spectra and a support direction \(\eta\). Let
\[
h_\eta(U)=\Re\left(\eta\det(D_a+UD_bU^*)\right),\qquad
M_\eta=\max_{\sigma\in S_4}\Re\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]
The exact exterior-power expansion used by account01/B07 depends on the one-/three-minor layer through \(P\) and the two-minor layer through \((D,R)\). Therefore Theorem 1 gives, for every row or column transposition \(\tau\),
\[
\boxed{\frac{h_\eta(U)+h_\eta(\tau U)}2
=\sum_\sigma\lambda_\sigma\Re\left(\eta\prod_i(a_i+b_{\sigma(i)})\right)\le M_\eta.}\tag{10}
\]
If \(\Delta=h_\eta(U)-M_\eta>0\), then
\[
\boxed{h_\eta(U)-h_\eta(\tau U)\ge2\Delta>0.}\tag{11}
\]
So a support-violating point is strictly above every row/column label-swap antipode. A flat pair orbit has equal support at its antipodal label swap, hence cannot occur at a support violation.

### Corollary 3 — `MOC4-NO-FLAT-PAIR-VIOLATOR-v1`
A support-violating global maximizer has no flat row or column pair orbit; all twelve pair spheres are on the strict branch.

This closes the entire flat-pair branch of the previous boundary dichotomy. The earlier implication `flat pair -> equal-support zero-entry representative` remains correct, but the zero-entry support problem is no longer needed for that branch because a violating maximizer cannot reach the antecedent. This theorem does not claim every arbitrary zero-entry unitary is excluded.

## 5. Exact sanity check

The accompanying standard-library verifier uses the campaign lead's exact rational zero-entry orthogonal witness, constructs one exact oriented split \(t_{jk}\), then checks exact orthogonality, all flow equations, total mass/nonnegativity, and the identities \(\sum\lambda P_\sigma=\bar P\), \(\sum\lambda R_\sigma=\bar R\), \(\sum\lambda S_\sigma=\bar D\) with `fractions.Fraction` only.

Exact output:
```text
PASS MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1
lambda_support = 16
Pbar_match = True
Rbar_match = True
Dbar_match = True
Rbar =
  ['735073/2640625', '2437632/66015625', '45201168/66015625']
  ['952776/2640625', '63577993/132031250', '20814457/132031250']
  ['952776/2640625', '63577993/132031250', '20814457/132031250']
```
The verifier is only an exact representative check; the theorem is the analytic flow proof above.

## 6. Partner application and surviving end-to-end chain

The assigned partner account01/B09 supplies a continuous exact family of dense nonmonomial rank-two points satisfying all twelve strict pair-Rayleigh conditions and still lying inside the target hull. Theorem 1 correctly does not eliminate that family: it eliminates only tied/flat pairs. This confirms the surviving problem is strict interior geometry, not monomial rigidity.

The compact surviving MOC4 route is now:
1. place any hypothetical failure at a global support maximizer by the campaign's exact reductions;
2. by Theorem 1, all twelve pair orbits are strict, so the flat/zero-entry branch is gone;
3. apply the exact \(X\)-aware six-fiber identity `(SR)` plus the twelve strict pair-Rayleigh conditions;
4. prove that strict-interior implication, or produce a true-unitary strict-interior datum actually violating `(SR)`;
5. use the established continuity/gauge treatment for repeated spectra and singular limits.

The first unpaid implication is therefore:

> **`MOC4-STRICT-BIRAYLEIGH-SR-v1` (OPEN).** At a global support maximizer satisfying all twelve strict row/column pair-Rayleigh conditions, prove the exact six-fiber support inequality `(SR)` for the structured \(K,X\) generated by the spectra and support direction.

The account01/B09 rank-two family is a required test family for this implication and satisfies the inequality with positive margin.

## 7. Status and non-claims

- `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`: **proved**.
- `MOC4-NO-FLAT-PAIR-VIOLATOR-v1`: **proved** as a support corollary.
- The unrestricted common \(S_4\) lift for one unitary remains **false**.
- Prior zero-face identities/counterexamples remain valid history; they are no longer required for the flat-maximizer branch.
- A strict nonmonomial stationary point or maximizer is not a MOC4 counterexample.
- Full MOC4 remains **OPEN**; no target-level closure or worldwide novelty is claimed.
- No arbitrary bistochastic surrogate, benchmark material, hidden answers, credentials, unrelated private data, email/Drive data, paid model/API, remote workflow, or public release was used.

## 8. Next recipients

Primary: campaign lead account03/B07. Also account01/B09, account04/B09 and account02/B07 for integration into the strict-bi-Rayleigh \(X\)-aware support route.
