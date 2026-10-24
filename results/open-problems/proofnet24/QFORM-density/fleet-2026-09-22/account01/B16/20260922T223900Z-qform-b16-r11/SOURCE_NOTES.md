# Source note for the matroid base-packing step

The only external combinatorial theorem used in `REPORT.md` is the classical matroid base-packing criterion.

A convenient modern reference is James Oxley, *Matroid Theory*, Theorem 11.3.11: a matroid `M` has `k` pairwise disjoint bases iff for every `X subseteq E(M)`,

`k r(X)+|E(M)-X| >= k r(M)`.

For `k=2` and `r(M)=3` this is exactly

`|E(M)-X| >= 2(3-r(X))`.

The theorem is attributed there to the matroid-union/base-packing theory of Edmonds; see also J. Edmonds and D. R. Fulkerson, *Transversals and matroid partition*, Journal of Research of the National Bureau of Standards B 69 (1965), 147–153.

Public verification used in this run: Oxley's theorem statement is available in the ENS-hosted PDF indexed at `https://www.math.ens.psl.eu/~benoist/refs/Oxley.pdf`; a second source states Edmonds' criterion as `tau(M)>=k iff |E-X|>=k(r(M)-r(X))` at `https://math.wvu.edu/~hlai2/Pdf/k-pm-epsilon_Disjoint_bases_2010.pdf`.

No literature novelty claim is made for this combinatorial ingredient.
