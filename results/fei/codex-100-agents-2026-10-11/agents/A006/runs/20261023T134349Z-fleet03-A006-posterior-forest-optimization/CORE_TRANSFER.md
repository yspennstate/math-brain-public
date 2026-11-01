# Paid core lifting: a conditional all-inner-function code identity

This is an explicit normalization and payment rule for NEW references, not a new FEI theorem for read-once composition and not a free change of an already spent history. Let V be ANY nonconstant Boolean indicator on physical coordinates disjoint from a core Z of size k>=1. Put h=2V-1, b=EV, t=2^-k, G=2[OR(Z) OR V]-1. Let q be ANY supplied fixed positive normalized reference on the nonempty inner Fourier sets, with complete nonempty cost C_q(h). The reference may itself be a pushforward of actual runs; retain all its actual-run posterior ambiguity.

Construct a normalized reference R by ONE fair first branch:

* Core branch: sample a uniform nonempty subset of Z.
* Lift branch: run q once to obtain a nonempty inner set A, sample a uniform subset D of Z (including empty), and output A union D.

All these are real draws with canonical order. Core and lift output classes are disjoint; the lift posterior over q's real underlying runs is preserved EXACTLY, rather than replaced with artificial descriptions. In particular

    R(D)=1/[2(2^k-1)] for nonempty core-only D,
    R(A union D)=q(A)/2^(k+1) for A nonempty inner and D subset Z.

Direct physical pivots give

    I(G)=I_core+t I(h), I_core=2tk(1-b).                    (1)

The expansion G=1-2 d_Z(1-V), with every core coefficient of d_Z having magnitude t, gives core-only spectral mass4t(1-t)(1-b)^2. Each particular A nonempty inner, combined with each D subset Z, has squared mass t^2 hhat(A)^2. Hence EXACT complete nonempty cost is

    C_R(G)=4t(1-t)(1-b)^2[1+log(2^k-1)]
               +t(k+1)Var(h)+t C_q(h).                   (2)

No target entropy bound occurs in this identity. As Var(h)=4b(1-b) and 1+log(2^k-1)<=k+1, the first two terms combined are at most

    4t(k+1)(1-b)[(1-t)(1-b)+b]
       <=4t(k+1)(1-b)<=4 I_core.                         (3)

The last inequality uses k+1<=2k. Thus, for EVERY supplied K>=0,

    C_q(h)<=K I(h)  implies  C_R(G)<=max(4,K) I(G).       (4)

This is a CONDITIONAL transfer law, valid for every Boolean inner h, not a proof that a universally paid q exists. The cost identity is computable from b, Var(h), C_q(h), k, and contains all branch/subset probabilities and any existing allocation entropy refund. It does not allow applying independent-component identities across physical overlaps.

## Explicit repair of this stage's genuinely intersecting two-core counterfamily

In CORE_CLOSURE.md section4, V=T_1T_2 on independent component coordinates. Section1 supplies each actual component reference at cost<=17I/2; section3's actual three-sector reference q has C_q(h)<(17/2+log3)I(h)<11I(h). Apply (4) with k=1 and public common coordinate x to obtain a normalized fixed hierarchical reference R with C_R(G)<11I(G). The full binary wrapper gives<13I(G), if desired. This reference really samples the necessary combination {z,y} and its x-lift, instead of adding only a dictionary whose outputs stay inside either individual core or their intersection.

Thus this stage both falsifies the individual-core-plus-intersection interface and gives a completely paid replacement on its actual intersecting Boolean witness. The success uses a common-core factorization followed by independent components. The universal first unsupported line is an influence-paid representation for interacting cores that admit NEITHER this common-core/independent decomposition NOR another proved paid compilation. Finding a larger dictionary without paying its selector does not supply that line. Universal FEI remains OPEN; this new transfer/reference construction awaits independent review.
