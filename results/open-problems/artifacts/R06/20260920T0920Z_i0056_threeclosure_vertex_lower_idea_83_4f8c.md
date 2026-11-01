# R06 idea before proof — multiplicity-three preclosure for the tetrapentagonal vertex bound

Source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. The frozen regular/co-regular metric remains `Phi_V(H_{5,5})=sqrt(5)` with width zero. This note concerns the still-open more-general-transitive-plane-graph clause for the source-valid tetrapentagonal graph

\[
T=r\{4,5\}=M(H_{5,4}),
\]

with outer vertex boundary normalization `partial_V K=N[K]\setminus K`.

## New route before validation

The current rigorous edge lower bound is

\[
h:=\frac{4}{1+\sqrt3+\sqrt5}\le \Phi_E(T),
\qquad 0<h<1.
\]

The previous conversion to a vertex lower bound closed every outside vertex of multiplicity at least two at once and used the crude inequality `|partial_E K| <= 4 |partial_V K|`. That loses the key fact that multiplicity-three additions are free for the vertex ratio.

Try a two-stage closure instead.

1. **Multiplicity-three preclosure.** Repeatedly adjoin an outside vertex with at least three neighbors in the current set. If it has `r>=3` selected neighbors, then in a 4-regular graph
   \[
   \Delta |\partial_E|=4-2r\le-2,
   \qquad
   \Delta |\partial_V|\le(4-r)-1=3-r\le0.
   \]
   Thus this preclosure terminates after finitely many steps and never increases the vertex-boundary ratio. At its terminal set every outside vertex has multiplicity at most two, hence
   \[
   |\partial_E K|\le2|\partial_V K|.
   \]

2. **Multiplicity-two closure.** Starting from that preclosed set, continue adjoining outside vertices with at least two selected neighbors until no such vertex remains. Positive edge expansion forces termination because the edge boundary never increases while cardinality would otherwise diverge. Let `m_2` be the number of multiplicity-two additions; multiplicity-three/four additions created later do not increase vertex boundary. At the final set each boundary vertex has exactly one selected neighbor, so edge and outer-vertex boundaries coincide.

This should give two simultaneous inequalities for the preclosed set of size `n` and outer boundary `b`:

\[
b\ge h(n+m_2)-m_2,
\qquad
b\ge \frac h2(n+m_2).
\]

Optimizing over `t=m_2/n>=0` should yield

\[
\frac bn\ge\min_{t\ge0}\max\{h-(1-h)t,\tfrac h2(1+t)\}
=\frac{h}{2-h}.
\]

For the R06 edge lower bound this simplifies to

\[
\boxed{\Phi_V(T)\ge \frac{2}{\sqrt3+\sqrt5-1}}.
\]

This would improve the previous lower endpoint `1/(sqrt(3)+sqrt(5)-2)` without any sampled inference. The proof must check carefully that (i) preclosure is valid for an arbitrary finite, possibly disconnected starting set; (ii) the second closure terminates; (iii) only the multiplicity-two additions can increase the outer boundary; and (iv) the comparison back to the original set preserves the lower-bound direction.

## Section-B moves for this run

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** parameterize the closure by the multiplicity threshold (3 first, then 2) instead of using one undifferentiated closure.
- **#26 HUNT THE SPORADIC CASE:** isolate multiplicity-three/four outside vertices as the exceptional local configurations; they turn out to be beneficial rather than dangerous for vertex expansion.
- **#27 SWAP THE QUANTIFIERS:** prove a graph-level edge-to-vertex conversion valid for every finite set first, then substitute the tetrapentagonal edge constant, instead of optimizing one finite witness.

No code or finite certificate is warranted unless the proof creates a finite claim; the prospective result is a theorem-sized deterministic inequality and needs a full written proof rather than a numerical checker.
