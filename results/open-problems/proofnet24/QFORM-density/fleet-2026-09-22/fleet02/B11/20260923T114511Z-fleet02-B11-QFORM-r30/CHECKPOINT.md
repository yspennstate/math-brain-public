SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T11:45:11Z.
attacking: the exact two-bank near-null/null-sum endpoint; preserve product provenance through the rank-two logarithmic receiver.

# Early checkpoint — arbitrary planar caps do not suffice at the null-sum endpoint

Status: PROVED COUNTEREXAMPLE TO AN INTERMEDIATE RECEIVER / FULL QFORM OPEN.

The completed fleet03/B11 r29 addendum reduces its exact cross-rank-one, shared-curvature-zero endpoint to the proposed statement `QFORM-TWOPLANAR-NULLSUM-RECEIVER-v1`: for two independent planar random vectors `(U,Z)` and `(V,W)` having bounded joint densities, control

    beta U^2 + 2 alpha V(Z+W) + 2 gamma UV + delta V^2 + affine

under `alpha beta != 0`. As stated with only planar joint-density caps, this proposed receiver is false.

Fix `0<eps<=1/3`. Let `(U,Z)` have density one on

    L_eps=[0,eps] x [0,eps^{-1}],

whose area is one. Independently, let `(V,W)` have density one on

    R_eps={ (v,w): a_eps<=v<=eps^2, 0<=w<=eps^2/v },
    a_eps=eps^2 exp(-eps^{-2}).

Again the area is exactly

    int_{a_eps}^{eps^2} eps^2/v dv
      =eps^2 log(eps^2/a_eps)=1.

Thus both planar probability densities have `L^infinity` norm exactly one. Put

    T_eps = U^2 + 2 V(Z+W).

This is the proposed null-sum form with `alpha=beta=1`, `gamma=delta=0`. On the full support,

    0<=U^2<=eps^2,
    0<=2VZ<=2 eps,
    0<=2VW<=2 eps^2,

so

    P(0<=T_eps<=2eps+3eps^2)=1.

For `eps<=1/3`, the interval has length at most `3eps`. Hence any density of `T_eps`, if it exists, satisfies

    ||p_{T_eps}||_infinity >= 1/(3eps),

and in small-ball form the ratio is already

    P(T_eps in [0,3eps])/(3eps)=1/(3eps) -> infinity.

Therefore no dimension-free density bound can follow from the two planar joint caps and `alpha beta !=0` alone.

The quadratic matrix of `T_eps` in coordinates `(U,Z,V,W)` is

    [[1,0,0,0],
     [0,0,1,0],
     [0,1,0,1],
     [0,0,1,0]],

whose spectrum is `{1,sqrt(2),0,-sqrt(2)}`. Thus the obstruction even has the exact three-large-eigenvalue indefinite spectral shape. It is NOT a counterexample to QFORM: `U` and `Z` are dependent, and `V` and `W` are dependent. It refutes only the loss of original product-projection provenance in the proposed abstract receiver. The unbounded `W` support is deliberate and legal under the proposed cap-only hypotheses; no hidden moment/support assumption can repair the statement.

The repaired first unpaid implication is therefore `QFORM-TWOPLANAR-NULLSUM-PRODUCT-PROJECTION-v1`: exploit the fact that each planar bank in the actual QFORM reduction is an orthogonal projection of a product of cap-one one-dimensional laws, rather than an arbitrary planar cap-one density.
