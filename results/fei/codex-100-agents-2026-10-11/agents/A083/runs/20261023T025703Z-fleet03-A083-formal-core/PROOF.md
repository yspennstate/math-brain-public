# Balanced-core residual and a fixed-influence reference obstruction

All inputs are uniform independent bits; Fourier entropy and KL are in bits. No reference is silently renewed. This stage analyzes F_h=h(A) when x=0, and otherwise 2y-1 when b=1 and +1 when b=0, where h is ANY balanced Boolean sign on a disjoint finite block A. This places the arbitrary core in the branch that was the character in stage17; it differs from A038/A050's priority gate, which keeps a character there and inserts the core in the other branch.

## 1. Exact arbitrary balanced-core identities

Write p for the core spectrum and I_h,H_h for its influence and entropy. Balance says p(empty)=0. The root spectrum has mass p(S)/4 at each of S,S+x for every nonempty core mask S, and mass1/16 at the eight masks contained in {x,b,y}. Therefore

    H0=3+H_h/2,             I0=1+I_h/2.

Query b; retain b0 and query y only in b1. The b-child entropies are both2+H_h/2, and influences are1/2+I_h/2 and1+I_h/2. Every final leaf has H=2+H_h/2 and I=1/2+I_h/2. The original mean b-child rate-four owner and the conservative continuation energy debit are

    U=1+2I_h-H_h/2,         debit=1.

The untouched terminal and both y terminals have physical reaches1/2,1/4,1/4. Thus the complete terminal entropy H_h/2+2 remains present, including the arbitrary seed entropy.

For ANY incoming normalized dominating root reference Q, transport it with the SAME actual spectral kernels and fair fallback at every source-zero erased row. The two y-child spectra in b1 coincide: their mean-sector amplitudes have opposite signs but equal squared magnitudes1/4; the other masses are p(S)/4 at S,S+x. Hence the source-positive y channel is fair, and the prescribed fallback makes it fair on reference-only rows as well. Both reference outcome probabilities are1/2, their outcome KL is zero, and the two final references coincide with erase_y Q_1. There may now be reference-only rows: the full-support claim of the literal-character stage is NOT carried over.

The finite KL chain rule gives the exact full-tree account

    D(P_F||Q)=E_b+O_b+D_0/2+E_y/2+D_y/2,

where D_y is the mean full final KL inside b1. No terminal or reference ghost is omitted. Subtracting that bill and energy1 from the SAME original U leaves the exact residual

    R(Q)=2I_h-H_h/2-D(P_F||Q).                         (1)

This identity does not assert R(Q)>=0. If an old conditional booking is part of the complete KL, it is included in (1), not added a second time.

## 2. Canonical incoming reference and the unchanged old booking

Let M match P_F's empty mass1/16 and all inclusion marginals. On nonempty sets it is the normalized maximum-entropy occupancy law: v=15/16, r_i=Inf_i(F)/v, and

    M(S)=(v/c) product_i (c r_i)^(S_i)(1-c r_i)^(1-S_i), S!=empty,
    1-c=product_i(1-c r_i).

Dummy coordinates are fixed absent. All relevant r_i lie in(0,1), and sum r_i>1 because the x,b pair contributes positive degree-two mass. Existence and uniqueness follow from the strictly decreasing function [1-product(1-c r_i)]/c=sum_i r_i product_(j<i)(1-c r_j), whose endpoint values straddle1. The source and M have the same moments, and log M is affine in membership on nonempty sets. Thus CE(P_F,M)=H(M) and

    D(P_F||M)=H(M)-3-H_h/2,
    R(M)=3+2I_h-H(M).                                  (2)

This is an EXACT cancellation of the core entropy, not an entropy estimate. It is the sharp nonnegative-owner criterion for this prescribed conservative transaction. Negative R(M) refutes this transaction, not every signed restriction ledger.

At both b children, condition on the retained x/core mask and retain y as spectator. Source-occupied nonempty core rows have y frequency zero and reference Bernoulli parameter t=4c/15; their actual weight is1/2. The core-empty occupied rows have deterministic matching y frequency. Therefore the previously used mean conditional booking is still

    C=-(1/2)log2(1-4c/15).

Its two halves are untouched-terminal C/2 and second-query erasure C/2. All other terms are retained quotient, erasure or outcome bills. For a general core c need not lie below13/16, so stage17's bound C<3/16 does NOT carry over; instead c<1 gives C<1/4, since15^2<2*11^2. These bounds concern different source families.

## 3. Actual balanced family with fixed influence and positive unspent owner

Let r=2^k, k>=4, delta=2^-r, m=2^r/r, and let d_r be the width-r point sign, negative at the all-zero input and positive elsewhere. Define

    h_r(z,A_1,...,A_m)=(-1)^z product_(j=1..m) d_r(A_j).

This is balanced. Each point coordinate has influence2delta; z has influence1, so I_h=1+2mr delta=3. Its dimension is2^r+1, and F_h has dimension2^r+4. These are actual finite Boolean functions; no large truth table is enumerated.

The point spectrum has empty mass(1-2delta)^2 and equal nonempty masses4delta^2. Its nonempty entropy is8(r-1)delta(1-delta). For L(u)=-u log2 u, the bound L(u)<(1-u)/ln2 and ln2>1/2 give H(d_r)<8r delta. Tensor additivity proves H_h=m H(d_r)<8. In particular H_h<4I_h, root H0<7 with I0=5/2, U>3, and U-1>2. The old booking C<1/4 is initially payable with ample slack. No arbitrary-core FEI hypothesis is used.

The root marginals are1/2 at x,z, 1/4 at b,y, and delta at each of the mr=2^r point coordinates. At c0=3/4 the four control-factor product is(3/5)^2(4/5)^2, and

    1/4-(3/5)^2(4/5)^2=49/2500>0.

The extra data factors are strictly less than1, so the canonical normalizer satisfies3/4<c<1. All factors remain positive. In the exact entropy formula for M, omit only nonnegative terms to get

    H(M) >= 1/4-v log2(v/c)
             +mr delta log2(15/(16c delta)).

Here v/c<5/4 and mr delta=1. Since (5/4)^3<2 and (16/15)^8<2,

    1/4-v log2(v/c)>-1/16,
    log2(15/(16c delta))>r-1/8.

Consequently

    H(M)>r-3/16,
    R(M)=9-H(M)<9-r+3/16<=-109/16.                    (3)

This is an all-k proof, not extrapolation from r=16,32,64. The owner starts positive, the core satisfies its rate-four entropy certificate, and the canonical reference still exhausts it. The unpaid line is the universal canonical complete-price admission, not a missing terminal FEI bound on these cores. This refines the known A047/A050 canonical-reference obstruction at a different gate, with fixed total influence and the old next-y booking explicitly retained; no novelty for the broad canonical no-go is claimed.

Keeping the actual signed query refund does not remove this obstruction. Over the WHOLE b-then-y history, H0-Hf=1 and I0-If=1/2, so the rate-four signed edge sum is e=-1. The actual final surplus is S=2I_h-H_h/2. Its standard net-source ledger is

    S-[D(P_F||M)-1]_+ = min(S,4+2I_h-H(M)).

For the family this signed remainder is less than10-r+3/16<=-93/16. Thus even the available whole-history signed refund1 has been retained; the failure is not manufactured by discarding negative edges. Again this refutes the fixed canonical complete-price account, not a universal FEI inequality or every correlated-reference strategy.

## 4. A supplied joint reference repairs this family as an INITIAL choice

For any balanced h let q be a normalized dominating core law with q(empty)=0. Lift it to a root law Q^lift by copying the eight control masses1/16, and replacing p(S)/4 at S,S+x by q(S)/4. Sector masses sum to1, source domination holds, and

    D(P_F||Q^lift)=D(p||q)/2,
    CE(P_F,Q^lift)=3+CE(p,q)/2,
    R(Q^lift)=(4I_h-CE(p,q))/2.                       (4)

Thus a supplied complete core-price certificate suffices. It is not claimed available for arbitrary cores. In particular q=p plus an assumed FEI bound would not advance full FEI.

For the explicit point family take z forced present and q=product q_r, with q_r(empty)=p_r(empty) and q_r(S)=(7/8)p_r(S)+(Var(d_r)/8)1[S=full] for S nonempty. This nonmatching correlation-preserving reference is normalized and dominates p_r. Its KL is at most Var log2(8/7)<Var/4, since8^4<2*7^4. Using the stronger ln2>2/3 in the point-entropy estimate gives

    CE(p_r,q_r)<(8r-1)delta(1-delta)<8r delta-delta.

The inequality ln2>2/3 is the first positive term plus the remaining positive tail of its atanh series. Therefore CE(p_h,q)<8-1/r, and (4) gives

    R(Q^lift)>2+1/(2r).

This is a comparison of INITIAL references. It does not authorize retiring the already-owed canonical source bill or replacing an inherited M by Q^lift for free. Any genuine descendant conversion must keep its actual signed likelihood ratio, old bookings, both full terminals and reference-only normalization. The supplier mechanism agrees with A050's already reviewed repair, with a factor1/2 rather than its different gate's factor1/4.

## 5. Checks that could fail and formal scope

The certificate exhausts all78 balanced signs on1,2,3 variables, independently comparing direct character sums with FWHT. It checks root and all terminal H/I identities, identical y spectra, lift normalization, complete source KL factor and cross-entropy identity using exact prime-log vectors. Four actual same-reference fixtures check C, fair channels on ALL rows, and the old-booking partition. Changing ONLY the second ghost fallback to deterministic zero creates positive outcome KL whenever ghost mass is positive. Thus equal physical spectra alone do not justify erasing reference outcome debt. Endpoints, actual denominators, canonical lower bracket and all integer logarithm signs are checked. Factored r=16,32,64 certificates independently bound the point entropy and explicit alternate supplier; the all-r theorem is analytic.

EqualKernel.lean formalizes only the rational consequence of equal normalized channel weights. It does not formalize Fourier analysis, entropy, canonical optimization, or source-price funding. Its actual admission/compiler result is in out/LEAN_RESULT.json; compilation or a saved draft must not be promoted to a proof of the prose claim. Full FEI remains OPEN. The first unsupported universal line is supplying a dimension-independent complete joint core-price certificate AND paying its actual inherited conversion after a mixed query, without renewing the source or assuming the desired FEI conclusion for that core.
