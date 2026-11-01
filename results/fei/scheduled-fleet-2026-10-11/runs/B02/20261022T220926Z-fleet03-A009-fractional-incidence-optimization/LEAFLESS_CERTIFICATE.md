# Complete same-reference payment on unequal leafless bipartite incidence

For every pair of integers 1<=a<=b let f=+1 exactly when at least one of a left bits and at least one of b right bits are positive. Its positive primes are precisely the ab edges of K_(a,b). Fix both endpoint orders, actual rarity pi=1/4, and one global weight lambda_e=1/b. Every left incidence row sums to1 and every right row to a/b<=1. These weights never depend on a sampled Fourier set. The nonempty-root normalizer is the SAME D=(1+1/(4b))^(ab)-1>0. All costs below are bits.

There is a family of distinct actual original queue runs, positive on every nonempty output set A, whose complete cross-entropy C satisfies

    C < (97/8) I(f) <13 I(f).                           (1)

This is an explicit certificate for the original coding mechanism on leafless unbounded-read incidence. It is not a new FEI class theorem: f has a read-once composition description. No optimality over global weights or over posteriors is asserted. Its purpose is to pay a full non-root bill after the universal root payment, with no control influence added and no private-neighbor hypothesis.

## Original queue events and all their factors

Write s=|A cap L|, t=|A cap R|. The original two-endpoint size/subset probabilities are1/4 for a specified singleton and1/6 for a pair. A root contributes lambda*pi; a zero-child gate contributes count probability1/2. A child contributes lambda and its own size/subset/count factors. All unused gates retain their absent-root factors; dividing by the original nonempty conditioning gives the common denominator D.

If t=0, give every selected left vertex an isolated singleton root, choosing ANY of its b incident edge labels. The labels are automatically distinct because the selected left endpoints differ. There are b^s distinct runs; their summed numerator is (b lambda/32)^s=32^-s. The source-SCC condition is satisfied: no chosen gate meets another owned left vertex. If s=0 the same construction gives (a lambda/32)^t=(a/(32b))^t. Shared UNUSED opposite endpoints do not create ownership arcs.

If s,t>=1, choose the first selected vertex on each side by a fixed order. Their pair is one root. Every other selected left vertex is a singleton child through the root's right endpoint; every other selected right vertex is a singleton child through the root's left endpoint. These are s+t-1 DISTINCT gates, and the ownership graph is an outgoing double-star. The chosen root is its sole source SCC. Choose one fixed permissible chronological order within each attachment slot. No permutation multiplicity is needed or claimed.

Put k=s+t and d=k-2. The root pays lambda*pi*(1/6)=lambda/24. Its child-count probability is1/[(d+1)(d+2)] and its two-slot multiset probability is1/(d+1). Each singleton child pays lambda*(1/4)*(1/2)=lambda/8. Hence the exact one-run numerator is

    N(s,t)=lambda^(k-1)/[24*8^(k-2)*(k-1)^2*k].          (2)

Together with the two one-sided numerators this defines Q(A)=N(A)/D. Events of different outputs are disjoint; within a one-sided output the gate labels distinguish events. This proves that Q is an output subprobability of the SAME queue, not an invented product reference. There is no extra root-order credit. At its conditional actual-run posterior, complete cost minus legitimate output ambiguity is -log2 Q(A). Count, subset, attachment, chronology and absent-root costs have all been retained in (2).

For d>=0, (d+1)^2(d+2)<=2*6^d. At d=0 equality holds; the adjacent ratio is at most6 (equivalently (d+2)(d+3)<=6(d+1)^2). Thus

    N(s,t)>=(lambda/48)^(k-1).                         (3)

The complete non-root cost on the two one-sided sectors is 5s and [5+log2(b/a)]t; on the mixed sector it is at most [log2 48+log2 b](k-1). In particular, after replacing log2 48 by6 and k-1 by k,

    C <= v_f log2 D + 6 I + R log2(b/a) + M log2 b,     (4)

where R and M are the actual spectral expected degrees of the right-only and mixed sectors. This is a bound on the full ledger; no ranks, leaf counts or terminal function have been silently reset. All pointwise masses arise from actual queue runs.

## Pay the two labels under the actual Boolean spectrum

Let u=2^-a and v=2^-b (v is a one-block probability, not v_f). Integer Fourier expansion of f=2(1-U)(1-V)-1 gives coefficient magnitudes 2u(1-v), 2v(1-u), 2uv on the left-only, right-only and mixed nonempty sectors, respectively. Consequently

    I_L=2a u(1-v),  I_R=2b v(1-u),  I=I_L+I_R,
    R=2b v(1-u)^2,
    M=2uv[a(1-v)+b(1-u)].                             (5)

These identities use squared Fourier coefficients for R,M and physical flips for I_L,I_R. Confusing v with v^2 would underpay the right-only sector and is explicitly checked.

If b=1 then a=1 and both extra label charges vanish. Otherwise v<=1/4. Set h=b-a>=0. The integer inequality b/a<=1+h<=2^h gives log2(b/a)<=h. Also h(h+1)/2^h<=3/2 for every h>=0: check h=0,1,2,3, then use (h+1)(h+2)<=2h(h+1) for h>=2. Thus

    R log2(b/a)/I_L
      <= (b/a)2^-h h/(1-v)
      <= (4/3) h(h+1)2^-h <=2.                        (6)

Similarly log2 b<=b and b^2/2^b<=9/8 for every integer b>=1. Check b=1,2,3; the ratio then decreases since (b+1)^2<=2b^2 for b>=3. Equation (5) yields

    M log2 b/I_L
      <= v(1+b/a)log2 b/(1-v)
      <= (8/3)b^2 2^-b <=3.                           (7)

Every denominator used here is strictly positive, and all ranges including h=0 and b=1 are handled. From (4),(6),(7), the complete non-root expectation is at most11 I, with no newly introduced controller or unused private-leaf bank.

## Same normalizer, rather than a new reference

The independently reconstructed A008 signed-implicant root lemma applies to THIS width-two table and THIS lambda: v_f log2 D <=3(1-q)I/(4 ln2)<9I/8, where q=Pr(f=-1)>0 and ln2>2/3. Substitution into (4) gives (1). A negative log D is retained exactly until this upper bound; it is never discarded and refunded again.

The all-dimensional argument is elementary; finite Walsh/queue checks are additional validation. The first unsupported extension is a certificate of comparable mass after deleting arbitrary edges or introducing a second overlapping neighborhood type. Then left-only labels no longer sum to b lambda uniformly, and a single double-star need not connect every mixed set. One cannot replace an arbitrary bipartite graph by its complete bipartite supergraph: doing so changes f, its primes, spectrum and influence.
