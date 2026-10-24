# B15 — exact gate-margin barycenter under Boolean block composition

**Run:** `20260922T004054Z-account04-B15-gate-r36`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** **ESSENTIAL_STEP_APPLIED**. Full unrestricted uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Live target:** OWNER CONTROL `2026-09-22.2`: converge on the universal gate inequality and either prove decomposable/AND extremality or find a gate whose required margin exceeds the two-input AND margin.

## 0. What changed

The newest owner message supersedes the older interface-D-only wording for this slot and asks every FEI worker to work the gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i I^t_i(G;p)\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

The source report proves that existence of one symmetric nonnegative \(\Gamma\) satisfying (G) for every Boolean gate and every bias vector is equivalent to FEI.  The current numerical candidate has \(C_0=\Gamma(1/2)=6.4548\); the owner asks workers to compare the *required margin*

\[
c_G(p)=-\frac{D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})},
\tag{0.1}
\]

not the unnormalised slack \(D_G\).

This run proves an exact composition law for that margin.  A decomposable gate cannot create a larger required margin than the largest margin of its factors at the induced biases.  Therefore any minimal counterexample to a proposed universal margin threshold is **composition-prime**.  This does not yet prove that every prime gate is below AND; it removes all decomposable gates from the genuinely new extremal search.

Before changing target, I consumed the newest account02/B15 arithmetic handoff

`account02/B15/20260922T000114Z-harmonic-delete-kl-valuation/REPORT.md`.

Its source-exact harmonic residual is

\[
D_{\rm del}=\beta H_2(\rho)-\mathbb E\log_2(K!)-\mathcal K_\rho,
\qquad \mathcal K_\rho\ge0,
\tag{0.2}
\]

with one-time signed valuation reserve \(R(f)\le2J(f)\le2I(f)\).  It rigorously shows that repeating an unbounded valuation price at every deletion step fails on Boolean addressing.  Those negative KL/factorial credits are retained in the archive; nothing below replaces them by packet integrality or a credit-free interpolation.  The newer owner control simply makes (G), rather than (0.2), the live common missing implication.

The other direct predecessor is this slot's exact block-composition report

`account04/B15/20260921T231202Z-composition-coherence-transfer/REPORT.md`,

which proves the biased spectral factorisation used below.

## 1. Definitions

Fix any symmetric potential \(\Gamma:(0,1)\to\mathbb R\).  Put

\[
A_\Gamma(p)=\Gamma(p)+h_2(V_p),\qquad V_p=4p(1-p).
\tag{1.1}
\]

For a Boolean gate \(G\) under a full-support product bias vector \(p=(p_1,\ldots,p_k)\), let \(q_S\) be its squared biased-Fourier law, \(H_t(G;p)=H(q)\), and

\[
I_i^t(G;p)=\sum_{S\ni i}q_S,\qquad I(G;p)=\sum_i I_i^t(G;p).
\tag{1.2}
\]

Write \(p_{\rm out}=\Pr[G=-1]\) (the choice of the Boolean sign convention is immaterial because \(\Gamma\) is symmetric). Define

\[
\boxed{
D_G^\Gamma(p)
:=
\sum_i\frac{I_i^t(G;p)}{V_{p_i}}A_\Gamma(p_i)
-\Gamma(p_{\rm out})-H_t(G;p)
}
\tag{1.3}
\]

and the Poincare gap in the exact units used by the owner's margin,

\[
\boxed{
Q_G(p):=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})
=\frac{I(G;p)-V_{p_{\rm out}}}{4}.
}
\tag{1.4}
\]

Biased Parseval gives

\[
\boxed{
Q_G(p)=\frac14\sum_{|S|\ge2}(|S|-1)q_S\ge0.
}
\tag{1.5}
\]

Whenever \(Q_G>0\), define the required extra quadratic margin

\[
\boxed{c_G^\Gamma(p):=-D_G^\Gamma(p)/Q_G(p).}
\tag{1.6}
\]

Indeed replacing \(\Gamma\) by \(\Gamma_c(p)=\Gamma(p)+c\,p(1-p)\) changes the slack by exactly

\[
\boxed{D_G^{\Gamma_c}=D_G^\Gamma+cQ_G.}
\tag{1.7}
\]

Thus \(c_G^\Gamma\) is precisely the least added quadratic coefficient required to make this gate/bias instance nonnegative.

## 2. Exact composition theorem for the slack

Let

\[
F=A(B_1,\ldots,B_m)
\tag{2.1}
\]

be a Boolean gate composition in which the \(B_i\)'s use pairwise disjoint input blocks.  Give all leaf variables full-support product biases.  Let \(p_i\in(0,1)\) be the induced output bias of \(B_i\), and set \(v_i=V_{p_i}\).  For the outer gate define

\[
\beta_i=I_i^t(A;p_1,\ldots,p_m),
\qquad
\lambda_i=\frac{\beta_i}{v_i}\ge0.
\tag{2.2}
\]

The biased-Fourier composition factorisation gives two exact identities:

\[
H_t(F)=H_t(A)+\sum_i\lambda_i\bigl(H_t(B_i)-h_2(v_i)\bigr),
\tag{2.3}
\]

and, for each leaf coordinate \(j\) in block \(i\),

\[
I_{ij}^t(F)=\lambda_i I_j^t(B_i).
\tag{2.4}
\]

Substituting (2.3)--(2.4) into (1.3), all branch terms cancel exactly:

### Theorem 2.1 — slack is additive with physical composition weights

\[
\boxed{
D_F^\Gamma
=D_A^\Gamma+\sum_{i=1}^m\lambda_iD_{B_i}^\Gamma.
}
\tag{2.5}
\]

No entropy term, coordinate-label fee, or hidden branch cost is omitted.  In particular the \(h_2(v_i)\) terms in (2.3) are exactly what converts the outer contribution \(A_\Gamma(p_i)\) into the inner gate slack.

**Proof.** The global right side of (G) is, by (2.4),

\[
\sum_i\lambda_i
\sum_j\frac{I_j^t(B_i)}{V_{p_{ij}}}A_\Gamma(p_{ij}).
\]

For each inner gate, the bracket equals

\[
D_{B_i}^\Gamma+\Gamma(p_i)+H_t(B_i).
\]

Subtracting \(\Gamma(p_{\rm out})+H_t(F)\) and using (2.3) leaves

\[
\sum_i\lambda_iD_{B_i}^\Gamma+
\left[
\sum_i\lambda_i\bigl(\Gamma(p_i)+h_2(v_i)\bigr)
-\Gamma(p_{\rm out})-H_t(A)
\right],
\]

and the square bracket is exactly \(D_A^\Gamma\). QED.

## 3. Exact composition theorem for the Poincare gap

The same weights also decompose the margin denominator. From (2.4),

\[
I(F)=\sum_i\lambda_iI(B_i).
\tag{3.1}
\]

For the outer gate,

\[
I(A)=\sum_i\beta_i=\sum_i\lambda_i v_i.
\tag{3.2}
\]

Because \(F\) and \(A\) have the same output bias, subtracting output variance gives:

### Theorem 3.1 — Poincare gap is additive with the same weights

\[
\boxed{
Q_F=Q_A+\sum_{i=1}^m\lambda_iQ_{B_i}.
}
\tag{3.3}
\]

This is the key point: numerator and denominator of the owner's margin propagate with **identical nonnegative physical weights**.

## 4. Margin barycenter and prime-counterexample reduction

Assume \(Q_F>0\).  For every factor with positive gap write \(-D=Qc\).  A full-support Boolean gate with \(Q=0\) has biased Fourier degree at most one by (1.5); Booleanity then forces it to be constant or unary.  A nonconstant unary projection/negation has \(D=0\) for symmetric \(\Gamma\), so zero-gap factors contribute neither numerator nor denominator.

Combining (2.5) and (3.3) yields the exact formula

### Theorem 4.1 — required margin is a convex barycenter of factor margins

\[
\boxed{
 c_F^\Gamma
=
\frac{
Q_Ac_A^\Gamma+
\sum_i\lambda_iQ_{B_i}c_{B_i}^\Gamma
}{
Q_A+\sum_i\lambda_iQ_{B_i}
}.
}
\tag{4.1}
\]

Therefore

\[
\boxed{
\min\{c_A,c_{B_i}:\text{positive weight}\}
\le c_F\le
\max\{c_A,c_{B_i}:\text{positive weight}\}.
}
\tag{4.2}
\]

Equivalently, for any proposed margin threshold \(c_*\),

\[
D_A^\Gamma+c_*Q_A\ge0
\quad\text{and}\quad
D_{B_i}^\Gamma+c_*Q_{B_i}\ge0\ \forall i
\Longrightarrow
D_F^\Gamma+c_*Q_F\ge0.
\tag{4.3}
\]

This gives the following exact reduction.

### Corollary 4.2 — a minimal violating gate is composition-prime

Fix \(\Gamma\) and \(c_*\). If a gate/bias instance violates

\[
D_G^\Gamma+c_*Q_G\ge0,
\tag{4.4}
\]

choose one with minimal arity after deleting dummy inputs.  It cannot admit a nontrivial disjoint block decomposition into smaller nonconstant gates. Otherwise (4.1) says one of its factors already has margin greater than \(c_*\), contradicting minimality.

So the owner's gate-extremality problem may be restricted to **composition-prime gates**. Decomposable gates cannot be new extremizers; they only average the already-present factor margins.

### Corollary 4.3 — equality rigidity

If all factor margins are at most \(c_*\) and \(c_F=c_*\), then every factor carrying positive weight \(Q_A\) or \(\lambda_iQ_{B_i}\) must itself have margin exactly \(c_*\).  Thus a decomposable extremizer recursively consists only of extremal factors.  This supplies an exact mechanism for the observed persistence of AND-chain tightness.

## 5. Consequence for read-once gates and the current arity-five search

Every binary read-once Boolean formula is an iterated disjoint composition of two-input gates.  Up to input/output negations and permutations, the only nondegenerate two-input Boolean types are AND/OR and XOR.  Hence once the candidate potential plus margin is certified for all two-input gates, (4.3) certifies **every binary read-once composition with no additional loss**.  More sharply, its required margin lies in the convex hull of the required margins of the internal gate instances at their induced biases.

This analytically explains why the gate-reformulation sweep's READONCE category cannot produce a margin above its worst binary factor.  It also explains why a decomposable gate approaching equality must have its active factors approaching the same binding binary constraint rather than generating a new high-arity loss.

The remaining owner target is therefore genuinely about composition-prime gates. Two concurrent exact arity-five results further narrow the first untouched arity:

- account04/B17 proves that at uniform input biases every balanced five-input gate satisfies \(H\le6(I-1)\), giving \(c_G\le-1.8192\) for every non-dictator;
- account03/B17 proves that at uniform input biases and output measure \(1/4\), every five-input gate satisfies \(H\le6I-4\), so \(c_G\le0\), and every genuinely five-input gate on that slice has \(c_G\le-0.9096\).

Thus a five-input falsifier, if one exists, must avoid those exact slices; after the present theorem it may also be taken composition-prime.  The highest-value next search/proof region is therefore a composition-prime gate with nonuniform input biases (or a different unbalanced uniform-bias output slice), and the quantity to compare is \(c_G\), not raw \(D_G\).

## 6. Independent implementation check

`check_gate_margin_composition.py` is standard-library only. It computes biased Walsh coefficients directly from definitions, constructs random actual Boolean block compositions with 2--3 outer inputs and inner arities 1--3, and tests an arbitrary symmetric endpoint-zero polynomial potential unrelated to the FEI certificate.  This deliberately tests the algebraic identity rather than a special property of the read-once fixed point.

Deterministic seed: `20260922004054`.

Result:

```text
PASS
compositions_checked = 448
margin_barycenters_checked = 377
max_abs_D_identity_error = 5.385e-15
max_abs_Q_identity_error = 6.384e-16
max_abs_c_barycenter_error = 2.043e-13
```

Checker SHA-256:

`6ff4b6b9da929d2a325047c920bd055159e6fbe393543effd631c1fffe3835c7`

Captured stdout SHA-256:

`b69497c3630db8d71af92b381d7197a222a2502def05107f12e452c64a2e3042`

The numerical run is a self-check only. The all-dimensional statements (2.5), (3.3), and (4.1) are algebraic proofs.

## 7. Literature and claim scope

O'Donnell--Tan's composition theorem (arXiv:1304.1347) already establishes the general biased-product Fourier composition framework and proves FEI closure for read-once bounded-arity formulas when the relevant component inequalities hold.  Accordingly I make **no novelty or publication-priority claim** for the composition factorisation itself.  The contribution here is the exact project-target quantitative refinement: the owner's normalized required margin itself is a convex barycenter because its Poincare-gap denominator obeys the same physical composition law as the gate slack.

The current literature check still leaves unrestricted FEI open.  González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) present further restriction/stopping-tree evidence and explicitly state a key general inequality whose universal validity would imply FEI; Hod's 2017 lexicographic construction gives the familiar lower bound above 6.454784.  No search miss is used as a novelty claim.

## 8. Exact status and next implication

**Proved in this run:**

\[
\boxed{
D_{A(B_1,\ldots,B_m)}
=D_A+\sum_i\lambda_iD_{B_i},
\qquad
Q_{A(B_1,\ldots,B_m)}
=Q_A+\sum_i\lambda_iQ_{B_i},
}
\]

and hence the exact margin barycenter (4.1).

**Target-level consequence:** every minimal counterexample to a proposed universal gate-margin threshold is composition-prime.  Decomposable gates cannot demand a larger margin than a factor.

**Still missing:** prove every composition-prime gate has required margin at most the two-input AND maximum for the candidate \(\Gamma\), or exhibit a composition-prime gate and bias vector above it.  This is now the exact surviving owner target.

**Full FEI:** OPEN / NOT PROVED.

No benchmark gold, mocks, paid or remote compute, workflow dispatch, email/Drive data, unrelated private data, permission changes, or notification changes were used. A scoped manual content review found only mathematical formulas, logical account/slot labels, repository-relative paths, and nonsecret hashes suitable for the assigned private research archive.
