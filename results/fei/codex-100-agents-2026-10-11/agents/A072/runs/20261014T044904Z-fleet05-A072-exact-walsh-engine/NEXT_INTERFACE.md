# Exact terminal correction after a physical core query

This is a concrete handoff to A075/A089, not an absolute FEI inequality or an assertion that a child reserve is available.

For a fixed Boolean outer gate k and arbitrary independent inner Boolean cores g_l with p_l=P(g_l=-1), define

    v_l=4p_l(1-p_l), q_l=P_{p}(l pivotal for k),
    C(p)=H_p(k)-sum_l q_l h2(v_l).

The same unique occupied-block argument used in INDEPENDENT_PROOF.md gives

    H(F)=sum_l q_l H(g_l)+C(p),
    I(F)=sum_l q_l I(g_l).

Now query one actual uniform physical coordinate i in block j, producing g_j^+ and g_j^- and probability vectors p^+,p^-. The queried coordinate is averaged with its TRUE weights1/2, not weights proportional to outer influence. One has (p_j^++p_j^-)/2=p_j. The pivotal probability q_j is independent of p_j, while each q_l, l!=j, is affine in p_j. Consequently

    q_j^+=q_j^-=q_j,   (q_l^++q_l^-)/2=q_l,
    Inf_{j,i}(F)=q_j Inf_i(g_j).

It follows exactly, retaining every other core,

    Delta_i H(F)=q_j Delta_i H(g_j)+Delta_i C,
    Delta_i C=C(p)-[C(p^+)+C(p^-)]/2.                 (A)

For a proposed rate K, put S_K(g)=K I(g)-H(g). The corresponding signed query excess is

    Delta_i H(F)-K Inf_{j,i}(F)
       =q_j[Delta_i H(g_j)-K Inf_i(g_j)]+Delta_i C.   (B)

The complete parent slack is sum_l q_l S_K(g_l)-C(p), and the complete average child slack is q_j average S_K(g_j^+-)+sum_{l!=j}q_l S_K(g_l)-average C(p^+-). Equations (A)-(B) show exactly where a signed C correction must be paid; positivity of I-h2(p) or the composition-level mu budget alone does not assign it a physical child owner. Endpoint p_j^+=0 is valid by continuity: the corresponding child core is constant, its H,I and h2(v) all vanish, and direct centered coefficients avoid divisions by v.

## Frozen exact non-flat boundary cases

Take the actual six-bit core negative on {0,1,2}, p=3/64. For each k in {h,J}, query i=0 or2 in block j=0 or1. These are exactly8 tagged physical queries of actual36-bit functions. Coordinate0 has two nonconstant children with biases1/16 and1/32; coordinate2 has a nonconstant child with bias3/32 and a constant child with bias0. J's blocks0 and1 have different dominant pivotal statuses, so a common-q symmetry is not used.

The checker certifies inner/child integer Walsh Parseval, inverse signs, direct character sums and edges; outer rational Parseval and all64 inverse signs even at p_j=0; spectral-vs-independent pivotal identities; affine q transport; and physical edge influence by separately summing all32 inner fibers and all32 other-outer assignments. Every entropy comparison follows these structural checks. Full parent and both child entropies are retained in (A); enclosing zero is only an identity diagnostic, whose proof is the coefficient decomposition above.

All eight exact intervals for Delta_i C have a strict sign, including positive and negative cases. They are saved in out/boundary_case_*.json, with a summary in out/boundary_validation.json. The positive cases show that blindly discarding this correction is not valid even in a legal rare-input non-flat core. In addition, the saved full-query intervals certify Delta_i H(F)>4 Inf_{j,i}(F) in ALL EIGHT tagged cases, including the six negative-curvature cases. Thus the inherited core decrement also needs payment; a nonpositive Delta C alone does not make a physical query good at rate4. This is the true entropy decrement Delta H, not conditional erasure B_i, and only the eight stated queries are certified. It does not refute a paid physical policy or a full FEI bound: the signed inherited child term and terminal entropy must be considered together.

The next noncircular step is to select and certify ONE unused child surplus that pays the positive Delta_i C in (B), while retaining the existing q-weighted core bills and all remaining outer constraints. The constant-child cases isolate the endpoint without an unproved continuum extrapolation or a huge truth-table search.
