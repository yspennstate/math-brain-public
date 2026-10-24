# Independent heat/entropy audit: finitely many nonsymmetric Hamming layers

2 October 2026. I read the entire
[almost-symmetric candidate](stripe_extension_almost_symmetric_candidate.md),
the referenced entropy and adjacency proofs in
[hamming_band_fei.md](../2026-10-02-hamming-band/hamming_band_fei.md), and the full
[union/chain checker](stripe_extension_verify_union_and_chains.py).
I also read the [union lemma](stripe_extension_union_lemma.md) to verify
the checker's separate union assertions. The candidate was not edited.

**Verdict:** analytic PASS for the candidate's complete stated scope and
constant. No monotonicity, nested-comparator, or layer-contiguity assumption
has inadvertently remained in the proof. The finite checker passes, but
the justification below is analytic and does not infer a theorem from
the examples. External mathematical review and novelty certification
remain separate matters.

## 1. Uniform maximal-chain points and edges

For a fixed r-subset S, exactly r!(n−r)! permutations have S as their
first r elements. Thus X_r is uniform on its layer. For a fixed adjacent
pair (S,S∪{j}), exactly r!(n−r−1)! permutations produce that edge at
step r. Therefore its probability is

1/[binom(n,r)(n−r)],

so the chain edge is uniform among all edges between those two layers.
Total physical influence is 2^(1−n) times the number of changing undirected
cube edges. Averaging the symmetric comparator's contribution
2(n−r)2^(−n)binom(n,r) over the chain therefore recovers exactly the
changing-edge count of f. This proves E I(g)=I(f) without any monotonicity.

If f is constant on a layer, every chain takes that same constant label
there, so d=f−g is supported on the stated exceptional layer set Λ.
The quadratic real-function influence satisfies
I(f−g)≤2I(f)+2I(g); averaging yields E I(d)≤4I(f), as used in the draft.

## 2. Disagreement and the small-dimension variance calculation

Let q_r be the positive fraction of f on layer r. At this layer the
chain comparator's label has probability q_r of being positive. Averaging
over the uniform layer point x gives disagreement 2q_r(1−q_r).
Two independent chain labels also disagree with probability 2q_r(1−q_r).
Summing with binomial layer masses proves E δ=E D. Only independence of
the two chains at a fixed layer is needed; labels on different layers
may be arbitrarily correlated.

Moreover, E_chain E_x g=E_x f. Hence

E_chain Var_x(d)=4E δ−Var_chain(E_x g).

For any two Boolean comparators, whether nested or not,
|E g−E g'|≤E|g−g'|=2D. The independent-copy variance identity therefore
gives Var_chain(Eg)≤2E D²≤2E D=2E δ. Consequently

E Var(d)≥2E δ.

Poincaré I(d)≥Var(d), followed by E I(d)≤4I(f), implies E δ≤2I(f).
Multiplication by n<(k+1)² gives exactly the proposed small-dimension
bound nEδ≤2(k+1)²I(f). The variance argument requires an average over
comparators; no false pointwise disagreement bound is asserted.

## 3. Arbitrary exceptional layers and the large-dimension bound

For a real function u supported on Λ, let
v_r²=2^(−n)Σ_{x in layer r}u(x)². Cauchy–Schwarz over the bipartite edges
between layers r and r+1 gives

<u,A_cube u>≤2Σ_r sqrt((n−r)(r+1)) v_r v_(r+1)
≤(n+1)Σ_r v_r v_(r+1).

Terms with either layer outside Λ vanish. The induced path on the retained
layer indices is a disjoint union of consecutive blocks. Each block has
at most k vertices and top path-adjacency eigenvalue at most
2cos(π/(k+1)). Therefore

<u,A_cube u>≤(n+1)cos(π/(k+1))||u||².

This handles noncontiguous layers directly. For k≥1 write q=k+1.
The identity I(u)=[n||u||²−<u,A_cube u>]/2 and
1−cos(π/q)≥2/q² imply

n−(n+1)cos(π/q)≥2(n+1)/q²−1≥n/q²

when n≥q². Hence I(u)≥n||u||²/(2q²), precisely as stated. Applied
to d, whose squared norm is 4δ, this and the averaged energy bound yield
nEδ≤2q²I(f). If fewer than k layers are actually exceptional, the
upper bound k only weakens the estimate. The k=0 symmetric case is
treated separately and does not require this inequality.

## 4. Entropy comparison and the final constant

The reused comparison H(f)≤2H(g)+32nδ is valid for arbitrary Boolean
functions. In the referenced derivation, fhat²≤2(1+4δ)P for a probability
mixture P. Entropy concavity and nonnegativity give the required upper
bound in the correct direction. Its simplification uses δ≥2^(−n) when
δ>0 on the finite cube, δ≤1, and n≥1. Thus it applies to every chain
comparator, not only thresholds or monotone functions.

Each comparator is symmetric with arbitrary layer labels. The established
symmetric-function FEI theorem therefore applies as H(g)≤12.04I(g).
Averaging and using the exact expected influence and disagreement bound
gives

H(f)≤24.08I(f)+64(k+1)²I(f)
≤[25+64(k+1)²]I(f).

This verifies the constant and all normalization factors in the candidate.
Constants, n=0, and singleton endpoint Hamming layers cause no exception.

## 5. Finite crossings and total deviation from equal weights

After the stated coordinate sign changes and removal of zero weights,
the normalized score differs from 2r−n by at most
A=Σ_i|w_i/c−1|. If a layer's entire closed score interval avoids every
crossing, F is constant on that interval and therefore on the layer.
Thus every nonsymmetric layer is included among the eligible layers for
some crossing.

For one crossing τ in normalized score space, eligible centers lie in
[τ−A,τ+A]. They are spaced by 2, so an interval of length 2A contains
at most floor(A)+1 centers, including both endpoints when applicable.
Union bounding m crossings proves k≤m(floor(A)+1). This uses a superset
of possibly nonsymmetric layers and is valid for attained crossings and
either endpoint convention. If A=0 every score is determined exactly
by its layer and the function is symmetric, as the candidate states.
No monotonicity, crossing-spacing, or bias hypothesis is needed here.
The consequence is dimension independent only when m and A are bounded
independently of dimension; it does not cover arbitrary finite-crossing
weighted functions.

## 6. Static and runtime audit of the checker

The Walsh–Hadamard transform normalizes by the truth-table size and acts
on the last axis, so it handles both individual functions and batches.
The influence routine uses E[(u(x)−u(x^flip))²]/4 for arbitrary real u,
matching the analytic convention. Layer labels, chain indices and full
permutations correctly realize all maximal chains for dimensions 1–6.
The checker does not assume monotonic labels or contiguous exceptional
layers; its random larger-dimensional assignments may vary on arbitrary
selected layers.

For the separate union assertions, fhat(S)=Σ_j gjhat(S) at every nonempty
S. Cauchy–Schwarz gives a≤rΣb_j. The proved entropy inequality
e(a)≤rΣe(b_j)+(log₂e/e)Σb_j is valid in both cases Σb_j≤1 and Σb_j>1.
The empty term is at most (log₂e)Var(f), and disjointness gives
Var(f)≤ΣVar(g_j). This exactly matches the checker's union bound.
For a joining edge between different nonzero components, two component
boundaries and no union boundary occur. The script's directed edge
probability is the physical influence normalization, so its identity
ΣI(g_j)−I(f)=2(crossing probability) has the correct factor of two.

I ran the unchanged script successfully. Its deterministic output records
3,200 union examples, 616 chain functions and 47,172 full permutations.
Chain mean-influence error was zero; maximum disagreement error was
5.56e−17 and the projection-energy identity error was 1.34e−15. These
are finite floating-point checks only. The asymptotic claim is justified
by Sections 1–5 above.

## 7. Optional stronger analytic identity

The script checks a stronger identity than the candidate uses. It also
has a direct proof. Let P_sym be averaging over all coordinate
permutations, so P_sym f is the real layer-mean function. This is an
orthogonal projection commuting with the cube Laplacian and therefore
with its Dirichlet quadratic form. Since E_chain g=P_sym f,

E_chain I(f−g)=I(f)+E I(g)−2< f,P_sym f >_Dirichlet
=2[I(f)−I(P_sym f)]≤2I(f).

Combining this sharper energy bound with the same large-dimension
adjacency estimate and small-dimension variance calculation would give
nEδ≤(k+1)²I(f) and then

H(f)≤[25+32(k+1)²]I(f).

This optional improvement is an analytic consequence, not an inference
from the numerical test. It is not needed for the unchanged candidate's
PASS verdict and was not silently substituted into its proof.

## Assessment

No analytic gap found in the complete almost-symmetric theorem, its
constant, its finite-crossing consequence, or the specified checker.
The result remains a restricted FEI theorem for arbitrary assignments on
finitely many Hamming layers. Novelty and external specialist review
are not established by this audit.
