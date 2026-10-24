# Two changed shared rows, arbitrary private events, retained complete debt

All quantities are in bits; physical signs and cubes are uniform. This is the next narrow repair of the existing representation-transport packet. No universal FEI proof is asserted.

## 1. Consumed dependency and source scope

A012-DISJOINT-PRIVATE-MUX-ADMISSION@3 (statement hash 1754492604cf7370c7cc5a2a2e5a36c420e800a7cbddb58c8807457a9a5ed81a), DERIVATION Sections2-4, extends our previous one-point controller theorem to arbitrary private events and retains controller KL at coefficient1/16. Its monotone one-dimensional box argument is valid: Phi(A,B)=A log2(1/A)+B log2(1/B)-(A+B)log2(1/(A+B)) is componentwise increasing, and the stated endpoint maxima bound its arguments. Its explicit controller lift has private mass (1-mu^2)/8 and entropy-relative debt D_kappa/8 in H, then D_kappa/16 in the parent. No event-spectrum entropy is discarded from the complete CE. Our new proof contains its one-row conclusion as q=0, independently recomputes the logarithm signs with a separate arithmetic implementation, and retains its debt by the same direct normalized reference identity. Because A012 credits our earlier classification, this is consumption and reconstruction at the new application scope, not an independent full-chain acceptance or a new priority claim for one row.

## 2. Exact actual two-row identity

Take any Boolean phase c on a three-bit shared cube, distinct shared points w0,w1, and arbitrary Boolean events E0,E1 on one independent finite private cube V. The events may overlap, coincide, or be correlated; they need only be physically independent of s. Set p=Pr(E0), q=Pr(E1),

    G=c(s),
    H=c(s)(1-2[1_(s=w0)1_E0(V)+1_(s=w1)1_E1(V)]),
    F=(G+H)/2+z(G-H)/2,

where z is fresh. The two shared indicators are disjoint, so H is always an actual Boolean sign regardless of the correlation of E0,E1. Physical selector influence is d=(p+q)/8<=1/4. Conditional difference coefficients are

    k_T=[p c(w0)chi_T(w0)+q c(w1)chi_T(w1)]/8.

The parent shared-only amplitudes are chat(T)-k_T and k_T. Parseval over s gives delta=sum k_T^2=(p^2+q^2)/8. Every nonempty-private frequency belongs to H alone. Its two selector probabilities are equal, with erasure exactly their total mass. The conserved influence identity therefore gives

    B_z=2(d-delta)+sum_T Phi((chat(T)-k_T)^2,k_T^2).      (1)

No unspecified private spectrum enters this erasure formula. It still enters the complete reference cost below. Correlation between the private events is not replaced by independence.

## 3. Exhaustive finite phase reduction, with explicit symmetry

Any affine bijection of the three-bit cube maps an ordered pair of distinct points to (0,1). It permutes shared Fourier indices (with signs from translation) and leaves selector B,d invariant. This is a proof device only: the influence of the original physical shared coordinates is used in the final ledger, since affine maps need not preserve that sum.

Multiplying both branches by a shared character, or a constant sign, permutes Fourier indices and preserves B,d. The 256 phase tables split into16 orbits under these16 multipliers. Representatives are masks 0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23, with +1 when that truth-table bit is set. Exhaustive integer Walsh computation on all256 tables independently checks the reduction. For w0=0,w1=1, normalize a_T=chat(T)c(0), eta=c(0)c(1), then k_T=(p+eta*(-1)^(T_1)q)/8. Within each parity group T_1, order of a_T is immaterial. The16 representative phases have the following eight grouped profiles:

| Mask | T_1=0 coefficients | T_1=1 coefficients | eta |
|---|---|---|---|
|0|0,0,0,1|0,0,0,0|1|
|1|-3/4,1/4,1/4,1/4|1/4,1/4,1/4,1/4|-1|
|2|-1/4,-1/4,-1/4,3/4|1/4,1/4,1/4,1/4|-1|
|3|-1/2,1/2,1/2,1/2|0,0,0,0|1|
|4|-1/4,1/4,1/4,3/4|-1/4,-1/4,1/4,1/4|1|
|5|-1/2,0,0,1/2|0,0,1/2,1/2|-1|
|20|0,0,1/2,1/2|-1/2,0,0,1/2|1|
|21|-1/4,-1/4,1/4,1/4|-1/4,1/4,1/4,3/4|-1|

The full256 phases have12 raw grouped profiles, not eight: multiplication by a character with odd T_1 frequency swaps the two groups and replaces eta by -eta. This transforms each row contribution into the corresponding contribution in the other group, leaving (1) invariant for the same p,q. The independent verifier checks the full raw set equals the union of the eight displayed profiles and their swapped/negated versions. It initially omitted this normalization, failed that classification assertion, and was corrected; no failed logarithm or mathematical inequality was hidden. The table plus this exact finite classification and explicit symmetry is a complete source certificate, not an assumed extremal description.

## 4. Complete two-dimensional continuum certificate

The previously saved rare argument proves B<4d when 0<d<=1/32, and the moderate bound B<=2d+log2(5/4)<4d applies for d>=1/6. At d=0 the branches coincide and B=0. It remains to cover p,q in [0,1] with 1/4<p+q<4/3. Equation (1) gives

    4d-B_z=2d+2delta-sum_T Phi((a_T-k_T)^2,k_T^2).       (2)

For a rational rectangle p in [lp,hp], q in [lq,hq], each parity group's k has exact extrema

    kl=(lp+sigma*(lq if sigma=1 else hq))/8,
    kh=(hp+sigma*(hq if sigma=1 else lq))/8,
    sigma=eta*(-1)^group.

Since squaring a linear function is convex, A=(a-k)^2<=max((a-kl)^2,(a-kh)^2), and B=k^2<=max(kl^2,kh^2). Phi is increasing in both nonnegative arguments, including by continuity on the axes. Thus a rigorous rectangle lower bound for (2) is

    (lp+lq+lp^2+lq^2)/4
    -sum_groups sum_a Phi(max((a-kl)^2,(a-kh)^2),
                         max(kl^2,kh^2)).              (3)

Freeze16x16 seed boxes with at most four additional dyadic bisection levels in both axes. Discard a rectangle only if it lies wholly in the analytic rare or moderate domain. Certify (3) strictly positive, or split it into four children, up to the frozen depth. All eight profile jobs PASS, with no depth or runtime leftovers: 5,348 visited rectangles, 4,093 positive leaf certificates. The smallest recorded lower bound is 4759109953/281474976710656>0. Each certificate records its rational rectangle, depth and outward lower bound in out/CONTINUUM_i.json.

Author arithmetic uses exact Fraction and20-term rational atanh bounds, reduced to x in [1,2], with tail <=2u^41/(41(1-u^2)), u=(x-1)/(x+1). Bounds round outward to2^-48. The separate verifier imports no author logarithm helper: it uses80-bit integer outward interval powers and32 atanh terms with a uniform rational tail bound 2*(1/3)^65/(65*(1-1/9)), then rational division by its own ln2 bounds. It recomputes every saved leaf lower bound, checks positivity, and reconstructs the entire subdivision tree with exact rare/moderate pruning, no missing or unused leaves. All256 phases and every leaf are checked. This proves the continuum, rather than inferring signs between grid samples. Independent arithmetic reproduction by the author is not independent-agent review.

Therefore for every finite private dimension, every c, every distinct shared pair, and every pair of arbitrary private events,

    B_z<4d for d>0,
    Delta=B_z+JS_z<=(4+2/ln2)d.                         (4)

The coefficientwise scalar JS bound JS_z<=2d/ln2 is reconstructed in our prior source; it does not require the events to be independent. All inputs outside the two-row family remain outside this statement.

## 5. Complete reference, exact debt and full labels

Supply any fixed normalized finite-cost references positive on the child spectra. Calibrate every shared-only singleton atom and retain the incoming private conditional law, rescaled to its actual total mass. Calibration decreases CE by exactly categorical KL, so it is never a free erasure of conditional private entropy. G has only shared frequencies, hence its calibrated reference is P_G. Set Q(u,T)=P_F(u,T) on shared-only rows. On private H rows set Q(u,T)=R_Hcal(T)/4 in each selector sector, including off-target private reference mass. Other rows are zero. This is a fixed normalized full output reference because shared rows have mass 1-v_H/2 and private reference rows mass v_H/2, where

    v_H=4(d-delta).

Direct expansion gives

    D(P_F||Q)=D(P_H||R_Hcal)/2,
    CE_F=(CE_Gcal+CE_Hcal)/2+Delta,
    I(F)=(I(G)+I(H))/2+d.                               (5)

The shared physical coordinate charges use the original branches exactly once through their average. Thus a supplied actual child certificate of cost <=K I transports at K=4+2/ln2<7. Opaque terminals or event controllers receive no automatic certificate. Do not price E0,E1 as independent factors: their private spectra can interfere. The fixed R_Hcal retains this joint private bill.

There are16 shared (u,T) label sectors and one private-H sector of probability v_H/2. Their probabilities are P_F(u,T) on shared rows and v_H/2 on the private sector. The complete CE chain is H(labels)+(v_H/2)[1+CE(private conditional)]. The at-most17 label entropy is <=log2(17), but (5) uses its exact value, not this fixed upper bound as a small-influence surcharge.

An independent arbitrary common Boolean factor q with a prescribed normalized reference R_q tensors this reference. It adds exactly c_q to CE and D_q to KL, preserves B_z,JS_z,d, and adds I(q) to influence. Factorized incoming child references retain the same q bill in their half average. Do not calibrate away q atoms or regard its already consumed debt as a spare reserve.

## 6. Physical restrictions, explicit covers and root changes

Fixing a shared coordinate leaves at most two shared bits, or removes one/both edit rows; then the existing overlap<=2 transport applies. Fixing a private coordinate replaces E0,E1 by their actual cofactors, preserving the two-row form, including their correlation. Fixing z selects its actual certified child. Any common q cofactor requires its own actual supplied reference. No parent-to-child CE or original L,S,R contraction follows automatically.

For a concrete positive-cell cover let V have m physical bits, Nc=#positive c rows, ti=#E_i private points. Before adding z, G has Nc shared minterms of width3, H has 2^m Nc-c(w0)t0-c(w1)t1 full minterms of width3+m. The selector composition adds exactly one literal to each branch gate and no extra gates, giving total

    N=Nc(1+2^m)-c(w0)t0-c(w1)t1.

These literal widths become4 and4+m, respectively; uniform label weights1/N have physical densities pi=2^-width and root odds pi/N, root probabilities pi/(N+pi). On restriction discard incompatible gates, delete fixed literals, keep retained multiplicities, reset N_child and pi; actual probabilities become pi/(N_child+pi). They need not decrease. If N_child=0 there are no cover roots; constant spectral children use point-mass references. This explicit uncompressed cover transports truth and metadata, not a universal paid ordered-cover theorem. The stream lead's unchanged L,S,R monotonicity request was refuted in our earlier stage and remains false.

## 7. First unsupported line and next mechanism

This closes arbitrary-event perturbations of a pure shared phase supported on two rows. It does not prove all three-bit conditional means reduce to a pure phase plus two changed rows. Three or more changed shared rows and both-private branches remain outside the proof. The first unsupported line is still: every arbitrary three-shared-bit pair in 1/32<d*<1/6 has actual collision mass satisfying B_C<=2d*+2delta. The scalar relaxation alone permits a value above4. NEXT should test the signed three-row conditional profile or prove an extremal reduction to the now-certified two-row domain, keeping the same collision influence ownership and both full terminal references; one-point/private-conjunction cases are already closed.
