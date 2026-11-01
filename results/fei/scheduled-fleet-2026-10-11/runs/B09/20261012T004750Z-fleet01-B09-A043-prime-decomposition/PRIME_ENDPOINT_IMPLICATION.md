# A043 prime-gate implication with exact constant

All logarithms are base two. Let `Q_2` be the dyadic probabilities in
`[0,1]`, put

\[
V_p=4p(1-p),
\qquad
W_\Gamma(p)=\frac{\Gamma(p)+h_2(V_p)}{V_p}
\]

for interior `p`, and contract deterministic inputs before applying these
formulas.

## Exact composition ledger

Let `F=G(g_1,...,g_k)` with disjoint uniform input blocks. Write

\[
p_i=\Pr(g_i=1),\quad V_i=4p_i(1-p_i),\quad
\alpha_i=\mathcal I_i^\nu(G),
\]

where `nu` is the product law of the child outputs. The exact squared-spectrum
factorization gives

\[
\mathcal H(F)=\mathcal H_\nu(G)
+\sum_i\frac{\alpha_i}{V_i}
  [\mathcal H(g_i)-h_2(V_i)],                         \tag{1}
\]

\[
\mathcal I(F)=\sum_i\frac{\alpha_i}{V_i}\mathcal I(g_i). \tag{2}
\]

Equivalently, for the constant-`C` FEI deficit
`D_C(f)=C I(f)-H(f)`,

\[
D_C(F)=
\sum_i\frac{\alpha_i}{V_i}
  [D_C(g_i)+h_2(V_i)]-\mathcal H_\nu(G).              \tag{3}
\]

Equation (3) is the exact unpaid gate obligation. Positivity of child
deficits alone is insufficient; the outer product-biased spectral entropy
must be paid by their weighted values plus the binary normalization refunds.

## Prime gate-potential theorem

Fix `C<infinity`. Uniform FEI holds with constant `C` if and only if there is
a symmetric function

\[
\Gamma:\mathcal Q_2\to[0,\infty),\qquad
\Gamma(0)=\Gamma(1)=0,\qquad \Gamma(1/2)\le C,
\]

such that every disjoint-prime gate `G` and every vector of interior dyadic
input probabilities satisfies

\[
\boxed{
\Gamma(p_{\rm out})+\mathcal H_\nu(G)
\le \sum_i\mathcal I_i^\nu(G)W_\Gamma(p_i).
}                                                        \tag{PG}
\]

The same condition is required for binary prime gates. Signed literals obey
it with equality by symmetry of `Gamma`; constants obey it through the
endpoint values.

### Sufficiency and depth independence

Take a prime composition tree from `PRIME_GATE_DEFINITION.tex`. Suppose the
gate condition has already been propagated through every child gate `H_i`:

\[
\Gamma(p_i)+\mathcal H(H_i)
\le\sum_j\mathcal I_j(H_i)W_\Gamma(q_{ij}).            \tag{4}
\]

For an outer gate `G`, (PG) and the exact raw-entropy composition formula give

\[
\begin{aligned}
\Gamma(p_{\rm out})+\mathcal H(G(H_1,\ldots,H_k))
&\le \sum_i\frac{\alpha_i}{V_i}
      [\Gamma(p_i)+\mathcal H(H_i)]\\
&\le \sum_{i,j}\frac{\alpha_i}{V_i}
      \mathcal I_j(H_i)W_\Gamma(q_{ij}).
\end{aligned}
\]

By exact influence composition, the last coefficient is the physical input
influence in the composed gate. Thus (PG) is closed under honest disjoint
composition with **no addition to `C` and no dependence on depth or fan-in**.

At the root of a uniform Boolean function every leaf probability is `1/2`.
Since `V_(1/2)=1` and `h_2(1)=0`,

\[
\Gamma(p_{\rm out})+\mathcal H(f)
\le\Gamma(1/2)\mathcal I(f)\le C\mathcal I(f).
\]

Dropping the nonnegative potential proves FEI with the same constant `C`.

All inherited internal probabilities are dyadic: every subtree is itself a
finite uniform Boolean function on its underlying leaves. No all-real
extension is needed for this implication. If (PG) is used instead for
arbitrary external product biases, A045's separate continuity requirement and
endpoint contraction must be supplied.

### Necessity

If uniform FEI holds with constant `C`, use the source-exact deficit potential

\[
\Gamma_C(p)=\inf_{\Pr(g=1)=p}
  \{C\mathcal I(g)-\mathcal H(g)\}
\]

over finite uniform Boolean encoders. The exact composition argument proves
the gate inequality for every finite gate, hence for every prime gate.

## Exact scope

This is an equivalence/reduction, not a solution of FEI. The prime hypothesis
still quantifies over unbounded arity and every inherited dyadic bias. A gate
may itself be prime, so the condition cannot be treated as automatically
easier. What has been gained is a rigorous exclusion of decomposable and
canalizing redundancy, plus an exact lossless induction rule for any new prime
class theorem.

The weighted-threshold no-go families remain relevant to any attempted
all-real extension. They do not invalidate the exact dyadic prime reduction,
and the reduction does not turn those auxiliary failures into FEI
counterexamples.
