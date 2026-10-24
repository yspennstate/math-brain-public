# Independent reconstruction of A079's fixed nonfair sibling

Verdict: HOLDS at the exact scope of
A079-FIXED-NONFAIR-SIBLING-SEED-TRANSPORT@1, statement SHA256
9f459612f7674cd2e65de549e8fd7f36450f149c912b9a5381dd6fbb64da82b6.
No repair to that claim is needed. A032's additional controller theorem
is separate and has no independent external acceptance yet.

Starting from the displayed a truth row, rather than the author's code,
direct character sums recover raw arrays

    A=[2,2,2,2,2,2,2,2,4,-4,-4,-4,-4,4,4,4],
    B=[6,-2,-2,-2,6,-2,-2,-2,0,0,0,0,0,0,0,0].

Parseval gives masses 5/8,3/8 and spectral degree contributions 23/16,
5/16 on u. z contributes 3/8. A's normalized law has three fair marginals
and last marginal4/5. B's law has two3/8 atoms and six1/24 atoms; its
u marginal is nonproduct, so tensoring any seed never makes it product.
This is a direct marginal obstruction and needs no pending norm theorem.

The separate z frequency labels give full entropy
5-(9/16)log2(3)+(3/8)H(h), and full influence
17/8+(3/8)I(h), for ALL Boolean seeds, including constants and biased seeds.
Conditioning on z removes exactly h2(3/8); it removes no seed entropy.
The L1 Walsh sums are3 and3/2, giving conditional Renyi entropies
log2(72/5) and log2(6)+R(h). Substitution into the signed gap yields
3/4-2log2(3)-(3/8)R(h). The seed Renyi terms cancel, and its Shannon
term remains. The checker verifies these identities as prime-log vectors.

For a nonconstant seed f, h_t=ell*product_{j=1}^t f(x_j) has zero constant
Fourier coefficient, H(h_t)=tH(f), I(h_t)=1+tI(f). The balancing bit is
fresh and costs3/8 in F. The seed-frequency set is empty exactly when
the z frequency is0. The mutual information is therefore h2(3/8), and
the full joint and conditional/data-influence ratios tend to H(f)/I(f).
I(f)>0 follows from connectedness of the cube; constants have H=I=0
and are handled without division. Hence the claimed FEI-strength reduction
is correct and provides no divergent seed or FEI counterexample.

Tests that could have broken this review were constant/bias effects,
missing selector or balancing energy, false productness after tensoring,
and an omitted Renyi or Shannon terminal. Exact direct transforms and
physical edges cover all22 seeds on0..2 bits and1782 state/seed fixtures;
the all-dimensional conclusion is the displayed tensor derivation, not
an extrapolation from those fixtures. The author implementation is never
imported or executed. The earlier September ONE_BIT_ENDPOINT source already
contains the dyadic norm mechanism; neither this review nor A032's prior
rediscovery establishes novelty for that mechanism.
