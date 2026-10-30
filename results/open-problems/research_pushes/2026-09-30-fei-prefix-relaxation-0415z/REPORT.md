# All-prefix suppression inequalities alone do not imply FEI

2026-09-30 UTC. Status: proved relaxation obstruction, independently checked analytically by the parent research agent. Full Boolean FEI remains open.

## Result

There are probability laws on subsets of [n] with H(P)/E_P|S| tending to infinity that satisfy every pointwise all-prefix noise inequality in the September 21 prefix-granularity argument. Consequently, those numerical necessary inequalities, their integrated prefix suppression consequences, and distributional coding identities alone cannot imply a universal entropy/influence bound. Joint physical Boolean realizability is an additional essential hypothesis.

This does not refute the original Boolean derivative granularity theorem, any actual Boolean coupling theorem, or FEI. No Boolean function, dyadic amplitude vector, or signed Boolean realization is asserted for the laws below.

## Precise inherited necessary inequalities

Consumed source:

    proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/
    20260921T174232Z-prefix-granularity-suppression/REPORT.md

Git blob: 01c1f95c1dbb03e0ff6f0e352aa41ce389f06f0b.

For a law P on subsets and a nonempty A of size a, put

    nu_A=P(A subseteq S),
    M_A(t)=sum_(S contains A) (1−t)^(|S|−a) P(S),
    r_A=4^(a−1)nu_A.

The pointwise numerical consequence of Boolean derivative granularity and hypercontractivity is

    M_A(t) <= nu_A r_A^[t/(2−t)]       for 0<=t<=1.       (1)

The original source also has the exact beta identity

    v_A=a integral_0^1 t^(a−1) M_A(t) dt,
    v_A=sum_(S contains A) P(S)/choose(|S|,a).

Thus (1) implies all its integrated suppression bounds. This note tests (1) itself, not merely a weakened asymptotic estimate.

Later neighboring sources were also inspected: fleet03/B12 20260921T194351Z-curvature-palm-nonreuse (blob ddf8baf96385418c56a91c48f62c04168633faaa) and fleet04/B12 20260921T201418Z-palm-trigger-cluster (blob 4643e5dd27cc48a508820a30413e24b9c4717fac). They retain stronger actual physical curvature/robust-row hypotheses. The construction here does not refute those results.

## Construction

For every integer n>=128 set

    d=ceil(5 ln n),       epsilon=16/n^2.

Let P give total mass 1−epsilon uniformly to the d-element subsets of [n], and mass epsilon to [n]. These two supports are disjoint. Here 0<epsilon<1 and d<n/3.

For A of size a<=d,

    nu_A=(1−epsilon) choose(n−a,d−a)/choose(n,d)+epsilon,

    M_A(t)=(1−epsilon) choose(n−a,d−a)/choose(n,d)
                (1−t)^(d−a)
             +epsilon(1−t)^(n−a).

For a>d, only the final terms remain. In all cases nu_A>=epsilon.

### Verification of every pointwise prefix inequality

If r_A>=1, then M_A(t)<=nu_A<=nu_A r_A^[t/(2−t)], so (1) is immediate.

Suppose r_A<1 and write L=ln(1/r_A)>0. Since nu_A>=16/n^2,

    L <= 2 ln n−ln16−(a−1)ln4.                           (2)

In particular a<log2(n)−1. Moreover,

    d−a−L >= 3 ln n+a(ln4−1)+ln4 >0.                   (3)

Thus a<d. Every supported set containing A has at least d−a remaining elements, so

    M_A(t) <= nu_A(1−t)^(d−a)
            <= nu_A exp[−(d−a)t]
            <= nu_A exp(−Lt)
            <= nu_A exp[−Lt/(2−t)]
             = nu_A r_A^[t/(2−t)].                      (4)

The last inequality uses t/(2−t)<=t on [0,1]; because L>0 its exponential direction is as shown. The endpoint t=1 is covered since d−a>0. This proves (1) for every nonempty A and every t in the entire closed interval, in every dimension n>=128.

Consequently all integrated inequalities F_a(r_A) and their weaker closed-form consequences from the source hold as well.

## The entropy ratio diverges

The two support layers are disjoint, hence

    H_2(P)=h_2(epsilon)+(1−epsilon)log2 choose(n,d),
    I_P=E|S|=(1−epsilon)d+epsilon n.

Using choose(n,d)>=(n/d)^d gives

    H_2(P)/I_P
      >= [(1−epsilon)d / ((1−epsilon)d+epsilon n)]
          log2(n/d).

The bracket tends to one, d=O(ln n), and log2(n/d) tends to infinity. Therefore no finite C can bound H_2(P)<=C I_P for every law satisfying (1).

The exact unordered-prefix/factorial coding identities remain valid for these laws because they are identities for arbitrary set distributions. Keeping that factorial term is necessary for a sound code, but it cannot compensate for missing joint Boolean information when the only additional constraints used are (1).

## An explicit all-shift Booleanity obstruction

This construction is not merely lacking a proposed sign choice. No assignment of real signs to its nonzero square-root amplitudes can be a Boolean spectrum.

Let a_S be any real signed square root of P(S), fix any d-set S_0, and put U=[n] symmetric_difference S_0. Then |U|=n−d>2d. A difference of two d-sets has size at most 2d. Therefore the autocorrelation at U has exactly two nonzero summands:

    sum_T a_T a_(T symmetric_difference U)
       =2 a_[n] a_(S_0) !=0.

For the Fourier coefficients of a Boolean function f, f^2=1 would make every such nonzero-shift autocorrelation vanish. Hence this law has no real Boolean sign completion.

This last calculation identifies concrete information omitted by the prefix bounds: the tiny high-degree atom must cancel cross-shifts with the main layer. Its individual prefix contributions are adequate for (1), but those cross-shifts have no cancelling partners.

## Ledger and independent check

- PROVED: all laws above satisfy all pointwise numerical prefix inequalities (1), uniformly in A and t.
- PROVED: their entropy-to-mean-size ratio diverges.
- PROVED: no real sign completion satisfies Boolean all-shift autocorrelation.
- NOT REFUTED: physical derivative granularity, the source's Boolean theorems, later mixed-curvature or robust-trigger results, or full FEI.
- NEXT CONSTRUCTIVE OBLIGATION: retain the joint signed cancellation/physical coupling across prefixes rather than adding further consequences of (1) alone.
- NOVELTY: unverified after bounded repository alias and neighboring-source searches.

The parent agent independently read the original B12 source and checked the all-a exponent inequality, its direction, the beta-integral implication, and the entropy asymptotic before publication. This is an independent analytic check, not external peer review or proof-assistant certification. The later all-shift calculation is supplied explicitly above. No executable script or numerical certificate is required for this analytic result.
