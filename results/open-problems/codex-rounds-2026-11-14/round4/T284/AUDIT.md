# Audit of the vertex-row amplification

## The inherited result

The round-3 theorem was independently re-derived before extending it, and its unmodified verifier was run with this folder as cwd. It passed. The posterior parameter delta d/n, the negative-moment sign, the dyadic choice, and the repair exponent were checked. The new argument does not contradict that theorem; it replaces its edge-refresh method by adaptive computational concentration in larger blocks.

## Counting the right coordinates

An edge-by-edge product has binom(n,2) coordinates and would only give an O(n sqrt(log n)) distance bound, which is useless for the desired sublinear vertex loss. The proof groups disjoint edge sets into n-1 rows, assigning each unordered edge to its smaller endpoint. All edges are represented exactly once, so the rows really are independent. The solver's entire random tape is one additional block, giving exactly n blocks. A block can contain polynomially many bits; the imported theorem's polynomial time is in their total representation length.

There is no assumption that the solver is stable, label-invariant, or deterministic. Fixing its tape makes the success predicate deterministic. The concentration algorithm can change the tape; this incurs at most one block change and no repair loss. A single block containing every graph edge would fail: changing that block has no one-vertex repair rule.

## Repair, checked in two forms

The row proof shows that if both endpoints i<j survive deletion of changed-row owners, row i agrees, so the edge agrees. Independently, changed-row owners are the smaller endpoints of the symmetric-difference edges and therefore cover that symmetric difference. Removing a cover leaves identical induced graphs. Both forms show that repair works for arbitrary adaptively selected H and I. No independence claim about the selected output is required.

The exact verifier compares the two constructions of the author set for every ordered graph pair on up to four vertices, checks agreement of the full induced graphs after deletion, and checks every independent set of H. It includes I empty, I the full vertex set when allowed, all rows changed, no rows changed, and a tape-only change. The 20-vertex star illustrates that a row containing 19 modified edges costs only one vertex deletion.

The exhaustive counts can be derived separately. With m=binom(n,2), the number of ordered graph pairs is 2^(2m). The number of triples (G,H,I) with I independent in H is

    2^m sum_{k=0}^n binom(n,k) 2^(m-binom(k,2)).

Summing these formulas for n=1,...,4 gives 4165 and 35256, respectively. These match the loop counters. Thus the audit checks the coverage of the enumeration, not only its assertions.

## Sampling and success probability

The rounding bound is derived first by coupling each edge using a common uniform variable. A separate exact calculation sums graph likelihood differences and confirms that half their absolute sum equals the maximizing event-probability difference and is at most binom(n,2)(p-q). The toy seeded success predicates have probability differences no larger than this exact total variation.

The success lower bound c n^(-s) becomes n^(-S) for any fixed integer S>s, eventually. No estimation of c, s or the actual success probability is claimed. The transformation is allowed to depend on a suitable fixed S. In particular, it does not retain the round-3 algorithm's fixed runtime exponent independent of all inverse-polynomial success exponents.

For w=(S+ell+6)ceil(log_2 n), two elementary inequalities give the full budget:

    eta <= (n^2/2)2^(-w) <= (1/2)n^(-(S+ell+4)),
    delta+eta <= (1/2)n^(-ell)+(1/2)n^(-ell) = n^(-ell).

The verifier checks these with exact fractions over 153 parameter cases, including symbolic n=2^512. It also checks the lower success-measure budget and the identity 1/(epsilon delta)=4n^(S+ell). These checks allocate no large graphs.

Rounding the measure once avoids a potentially incorrect finite-bit union bound over an unspecified adaptive query count. The input laws are coupled before the algorithm runs. The two computations then use identical random bits, so agreement of inputs forces agreement of the whole transcript. This gives the same transfer directly as contraction of total variation under the randomized map from the input to its full transcript. Samplers used inside the map are exact for q, regardless of its input law.

## Imported theorem and its parameter display

The concentration theorem is an external mathematical input. Theorem 1.1 states the lower-bound-on-measure formulation. Theorem 3.2 specifies polynomial time in total representation length, and Remark 3.3 identifies the untampered product sample with the original input. The paper's definition of tampering budget is an almost-sure bound; using only the theorem's joint high-probability closeness and success would also suffice.

The final worst-case parameter display in Section 3.2 gives a budget involving the product log(8/delta) log(2/epsilon), while the main theorem states a bound involving log(1/(epsilon delta)). The reduction invokes the main theorem as stated, not this final parameter choice. Its constant C is not computed here. The publisher's abstract also states the sharp computational concentration result.

As an algebraic cross-check of the scale, the preceding tail display in Section 3.2 has an exponential factor exp(n lambda^2-k lambda) divided by an initial-probability estimate, plus oracle errors. Completing the square gives

    n lambda^2-k lambda = n(lambda-k/(2n))^2-k^2/(4n).

At lambda=k/(2n), a k of order sqrt(n log(1/(epsilon delta))) therefore makes this factor of order epsilon delta before division. This checks that the stated scale is compatible with that bound; it is not a new proof that all approximate-oracle and abort estimates hold simultaneously. No independent proof or implementation of MUCIO is supplied.

## Asymptotic size and remaining limitations

Substitution gives log(1/(epsilon delta))=log 4+(S+ell)log n, proving the asserted square-root-log loss. Independently, at n=exp(t) its ratio to n/log n is a constant times t^(3/2)exp(-t/2), which tends to zero. Thus the result does answer the preceding report's weaker O(n/log n) target; it does not depend on a guessed finite-n comparison or a fitted constant.

The proof needs only eventually n>d and 0<q<1. Finitely many exceptional inputs return the empty set. The case k_n=1 is allowed; the bound may be vacuous at small n. An impossible premise, such as polynomial success for k_n=n at fixed d>0, gives no contradictory conclusion. A success lower bound holding only on a subsequence yields guarantees only on that subsequence.

The source theorem, rather than any computation in this folder, supplies the adaptive polynomial-time search for a nearby success point. The verifier tests the reduction and bit budgets only. The work does not prove an all-algorithm obstruction, name an independent average-case hardness reduction, or produce an algorithm above log(d)/d. It still loses O(sqrt(n log n)) vertices and establishes no exact-k_n amplification or optimality lower bound.
