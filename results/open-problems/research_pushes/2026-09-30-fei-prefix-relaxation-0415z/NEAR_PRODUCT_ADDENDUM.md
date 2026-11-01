# The all-prefix relaxation remains insufficient arbitrarily near a product law

2026-09-30 UTC. Joint extension from the parent research agent and the regular-core worker's mixed-log-Sobolev precursor; independently checked by this report's author. This is an abstract probability-law obstruction. No Boolean spectrum or dyadic amplitude realization is asserted. Full FEI remains open.

## Stronger construction

For n>=64 put d=ceil(5 ln n), q=d/n, and epsilon=16/n^2. Let Q be the independent Bernoulli-q law on subsets of [n], and let

    P=(1−epsilon)Q+epsilon delta_[n].                    (1)

This law satisfies every pointwise all-prefix necessary inequality used in the companion report, while simultaneously

    TC(P) ->0,           H(P)/E_P|S| ->infinity.         (2)

Thus adding near-product total-correlation control to those scalar inequalities still does not recover Boolean realizability or FEI.

## Every prefix and every noise parameter

For a nonempty A of size a, define nu_A, M_A(t), and r_A exactly as in the companion report. Direct computation gives

    nu_A=(1−epsilon)q^a+epsilon,
    M_A(t)=(1−epsilon)q^a(1−qt)^(n−a)
              +epsilon(1−t)^(n−a).                    (3)

If r_A=4^(a−1)nu_A>=1, then M_A(t)<=nu_A proves the required bound.

If r_A<1, set L=ln(1/r_A)>0. Since nu_A>=16/n^2,

    a<log2(n)−1<n/2,
    L<=2 ln n−ln16−(a−1)ln4 <2 ln n.

Consequently q(n−a)>=d/2>=2.5 ln n>L. Both components in (3) are at most their initial mass times exp[−q(n−a)t], so

    M_A(t)<=nu_A exp[−q(n−a)t]
            <=nu_A exp(−Lt)
            <=nu_A r_A^[t/(2−t)]                        (4)

for every t in [0,1]. At t=1 the second component vanishes in this case because a<n. This is the complete pointwise prefix inequality, not only its integrated form.

The beta-integral prefix bounds follow exactly as in the original B12 source. Differentiating (4) at the equality endpoint t=0 also gives all corresponding mixed scalar logarithmic-Sobolev consequences:

    2 sum_(S contains A)(|S|−a)P(S)
       >=nu_A ln[1/(4^(a−1)nu_A)].                       (5)

The right side may be negative. Neither (4) nor (5) asserts existence of actual physical derivatives.

## Vanishing total correlation

Let Q' be the product of P's own coordinate marginals. The product I-projection identity gives TC(P)=D_2(P||Q')<=D_2(P||Q). Convexity of KL in its first argument then gives

    TC(P)<=epsilon D_2(delta_[n]||Q)
          =epsilon n log2(1/q)
          =(16/n)log2(n/d) ->0.                         (6)

The exact marginals of P are q'=q+epsilon(1−q). Also TV(P,Q)<=epsilon, though TV closeness alone is not being substituted for (6).

## Divergent entropy ratio

Entropy concavity yields H(P)>=(1−epsilon)n h_2(q). Meanwhile

    I_P=E_P|S|=(1−epsilon)d+epsilon n=d+O(1/n).

Since h_2(q)>=q log2(1/q),

    H(P)/I_P
      >=[(1−epsilon)d/((1−epsilon)d+epsilon n)]
           log2(n/d) ->infinity.                        (7)

In particular both scalar all-prefix hypercontractivity and arbitrarily small total correlation coexist with an unbounded abstract entropy/mean-size ratio.

## Exact scope

The original Boolean derivative-granularity theorem, all-shift Booleanity, lattice restrictions, and actual physical coupling constraints remain valid. This example says those joint requirements cannot be replaced by the numerical inequalities (4)–(5) plus TC(P) being small. It is not a counterexample to a theorem whose hypotheses include a genuine Boolean function or exact dyadic-amplitude realization.

The parent supplied and checked the product-mixture strengthening; the regular-core worker supplied the preceding mixed-LS near-product comparison; this worker independently checked (3)–(7). The source B12 hypothesis remains pinned at blob 01c1f95c1dbb03e0ff6f0e352aa41ce389f06f0b. No executable file or numerical interval certificate is needed. Novelty is unverified.
