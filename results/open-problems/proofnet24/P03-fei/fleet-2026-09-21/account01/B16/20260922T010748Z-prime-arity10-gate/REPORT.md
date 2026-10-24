# account01/B16 — the arity-10 FEI gate obstruction is composition-prime

**Outcome:** `CANDIDATE_REFUTED`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. This run used authenticated repository sources and current owner control, but no native authenticated research-brain retrieval/context.

## 0. Latest target and compact end-to-end conditional argument

The live owner control asks the FEI fleet to converge on the all-gate inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}. \tag{G}
\]

The gate-reformulation report proves that a symmetric nonnegative \(\Gamma\) satisfying (G) for every Boolean gate and every product bias, with \(\Gamma(1/2)\le C\), implies \(H(f)\le C I(f)\) for every Boolean \(f\). Conversely, FEI at constant \(C\) produces such a potential.

For the current read-once base potential \(\Gamma_{RO}\), write

\[
D_\Gamma(G;p)=\text{RHS(G)}-\text{LHS(G)},\qquad
M(G;p)=\frac14\sum_i \operatorname{It}_i(G;p)-p_{\rm out}(1-p_{\rm out})\ge0.
\]

Adding \(c p(1-p)\) to the potential changes the slack by \(cM\), so whenever \(M>0\)

\[
c_G(p)=-D_\Gamma(G;p)/M(G;p).
\]

Thus the owner candidate “the AND/decomposable constraints are extremal” would close this particular universal extension if every gate had required margin at most the globally certified AND margin. The already-proved read-once certificate pays every AND constraint with \(c=0.01\).

That candidate is false. Account03/B12 produced an explicit genuine balanced monotone arity-10 gate with

\[
I(G)=\frac{257}{128},\qquad
6.509836127588151479 < H(G) < 6.509836127588151480,
\]

and therefore, at uniform bias,

\[
\frac{H(G)}{I(G)-1}>6.459372281637855731,
\qquad
c_G>0.018289126551422926>0.01.
\tag{1}
\]

The first remaining structural question was whether this excess could still be blamed on a nontrivial disjoint functional decomposition. Account02/B17 proved the exact composition cocycle

\[
D(K)=D(F)+\sum_j b_jD(G_j),\qquad
M(K)=M(F)+\sum_j b_jM(G_j),\qquad b_j\ge0,
\]

so normalized margin is a convex average of factor margins. It follows abstractly that some composition-prime factor of any violating gate must violate. This run makes that obstruction explicit: **the arity-10 gate in (1) is itself composition-prime.**

## 1. Exact peer versions consumed

1. `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`, blob `d12fe592f4fa6db16cb571557f6cc41392dd5860`. It supplies the source-exact 10-input truth table, exact influences, interval-enclosed entropy, and the strict margin bound (1).

2. `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`, with source-bound brain handoff blob `f6fd4945acb3aa61f5020c6f906652fe4c886e90`. It proves the exact slack/Poincare cocycle and prime-factor reduction for disjoint gate composition.

3. For the target-level interpretation, `proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T003238Z-balanced-uniform-gate-slice/REPORT.md`, blob `cb99a17793db7919af1cfe21248198f1a6fb2f24`, proves that the uniform balanced slice of (G) is constant-for-constant FEI-complete and records the stronger current balanced lower bound \(6.521850083658612\ldots\). That stronger bound is not re-proved here.

## 2. A complete module criterion for composition-primality

Let \(G:\{-1,1\}^n\to\{-1,1\}\). For a nonempty proper coordinate set \(A\), write \(B=A^c\), and for each assignment \(a\in\{-1,1\}^A\) define its **row**

\[
R_a:\{-1,1\}^B\to\{-1,1\},\qquad R_a(b)=G(a,b).
\]

### Lemma 2.1

For \(2\le |A|\le n-1\), the following are equivalent.

1. There exist Boolean maps \(g_A:\{-1,1\}^A\to\{-1,1\}\) and \(F:\{-1,1\}^{1+|B|}\to\{-1,1\}\) such that
   \[
   G(a,b)=F(g_A(a),b).
   \]
2. The family \(\{R_a:a\in\{-1,1\}^A\}\) contains at most two distinct rows.

**Proof.** If (1) holds, then for fixed \(a\), the row is one of the two functions \(b\mapsto F(+1,b)\) and \(b\mapsto F(-1,b)\), so there are at most two row types. Conversely, if there are at most two row types, label the two types by \(\pm1\) (or use one label if only one occurs), set \(g_A(a)\) equal to the label of the row \(R_a\), and define \(F(s,b)\) to be that row's value at \(b\). Then \(G(a,b)=F(g_A(a),b)\). QED.

### Corollary 2.2

A gate is composition-prime in the account02/B17 sense if and only if **no** coordinate set \(A\) with \(2\le |A|\le n-1\) has at most two row types.

Indeed, every nontrivial disjoint composition with outer arity strictly below \(n\) has at least one inner block of size at least two, to which Lemma 2.1 applies. Conversely, such an \(A\) immediately gives a disjoint composition whose outer arity is \(n-|A|+1<n\).

This criterion handles arbitrary Boolean inner and outer gates, not only AND/OR/NOT read-once formulas.

## 3. Exact certificate for the inherited 10-input gate

The checker reconstructs the exact parent used by account03/B12 and applies the same fixed-coordinate restriction. The witness truth-table SHA-256 is

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

There are exactly

\[
\sum_{r=2}^{9}\binom{10}{r}=1012
\]

candidate nontrivial inner blocks. For every one, the checker forms the full row family from Lemma 2.1 and counts distinct row types. The result is

\[
\boxed{\min_{2\le |A|\le9}\#\{R_a:a\in\{-1,1\}^A\}=3.}
\tag{2}
\]

No candidate block has one or two row types. Exactly 18 blocks attain the minimum three. The complete row-type histogram is

```text
3:18, 4:46, 5:44, 6:48, 7:56, 8:104, 9:52, 10:94,
11:148, 12:82, 13:104, 14:132, 15:48, 16:20, 17:16.
```

By Corollary 2.2 the gate is therefore **composition-prime**.

The exact checker executed successfully. Source SHA-256:
`bac58cb5e7f477eae3f730ed088d8848becd0dab4020f1425a35b87bf1c48e1b`.

## 4. Applied consequence: the owner candidate fails already on a prime gate

Combining (1) and (2) gives an explicit Boolean gate with all of the following properties simultaneously:

* arity 10;
* balanced and monotone;
* every input essential;
* composition-prime for arbitrary disjoint Boolean functional composition;
* \(I=257/128\);
* \(H/(I-1)>6.459372281637855731\);
* read-once-base required margin \(c_G>0.018289126551422926\).

Since the complete AND family is certified with quadratic correction \(c=0.01\), the claim that the current read-once potential's worst gate is decomposable/AND is refuted **even after restricting the comparison to composition-prime gates**. This strengthens the prior refutation: the excess is not an artifact of composing smaller gates, and the composition cocycle cannot push it back onto an AND factor.

Equivalently, any successor potential of the form

\[
\Gamma_{RO}(p)+a p(1-p)
\]

must have at least \(a>0.018289126551422926\) merely to pay this explicit prime gate. The stronger inherited 162-input balanced construction forces a much larger cap/lift, but its prime obstruction was previously only existential through the cocycle; this report's contribution is the explicit small prime witness.

## 5. An explicit recursive FEI lower-bound family from the prime seed

Let \(G_1=G\), and define \(G_{d+1}\) by feeding ten disjoint fresh copies of \(G_d\) into the ten inputs of \(G\). Because \(G\) is balanced, every level is balanced. The standard disjoint spectral composition identities give

\[
I(G_{d+1})=I(G)I(G_d),
\qquad
H(G_{d+1})=H(G)+I(G)H(G_d).
\]

Hence, with \(I=257/128>1\) and \(H=H(G)\),

\[
I(G_d)=I^d,
\qquad
H(G_d)=H\frac{I^d-1}{I-1},
\]

so

\[
\frac{H(G_d)}{I(G_d)}
=\frac{H}{I-1}(1-I^{-d})
\longrightarrow \frac{H}{I-1}
>6.459372281637855731.
\tag{3}
\]

Thus this explicit composition-prime arity-10 seed alone generates an all-dimensional Boolean lower-bound family at constant greater than 6.45937. This is **not** the best known lower bound in the repository: the inherited shared-core construction gives the stronger 6.52185008... value. Equation (3) is included because it identifies exactly what the small prime obstruction means for FEI, not as a record claim.

## 6. Old/new missing implications and status

**Old decisive implication:** for the read-once base potential, every Boolean gate's margin is at most the decomposable/AND margin.

**New result:** **false**, with an explicit composition-prime 10-input Boolean gate requiring more than the globally certified AND correction.

**What survives:** the account02/B17 composition cocycle and prime-gate reduction are valid. They show decomposable gates cannot amplify normalized margin; therefore any fixed potential only needs to be tested/proved on composition-prime gates.

**Replacement obligation:** find a new finite-cap potential and prove its corrected slack nonnegative on every composition-prime gate at every product bias, or produce a further prime obstruction. On the balanced-uniform slice, account03/B13 proves this is already constant-for-constant equivalent to FEI, so this is not being presented as a solved reduction.

**Classification:** `CANDIDATE_REFUTED`.

Full FEI remains **OPEN / NOT PROVED**. No finite test, auxiliary theorem, or reformulation in this report is claimed to settle it.
