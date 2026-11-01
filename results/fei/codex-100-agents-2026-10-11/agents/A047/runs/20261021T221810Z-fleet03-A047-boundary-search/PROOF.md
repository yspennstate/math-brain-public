# Exact canonical payment crosses the rate-four boundary

The full FEI conjecture remains open. The prescribed canonical reference cannot always be paid from the entire rate-four surplus, even on a tensor of two-bit point defects. A smaller example passes the exact test after the marginal bound has failed. All quantities below use bits and uniform Boolean inputs.

## 1. Scope and one source account

Write h as a Boolean sign on data z, t=Pr(h=-1), d_j=Inf_j(h), and

    F_h(x,a,b,z)=(-1)^a on x=0; h(z) on x=b=1; +1 otherwise.

The reference is fixed at this reached root. Its empty mass is p0=(1-t)^2/4, v=1-p0; its marginals are d=(1/2,1/2,t/2,d_j/4). With dummy coordinates contracted, put theta_i=c d_i/v and choose the unique c in (0,1) satisfying

    1-c=product_i(1-c d_i/v).

Set Q(0)=p0, Q(s)=(v/c) product_i theta_i^s_i(1-theta_i)^(1-s_i) on nonempty s. The normalizer identity proves both total mass one and the stated marginals. For existence and uniqueness, [1-product_i(1-cr_i)]/c=sum_i r_i product_{j<i}(1-cr_j), r_i=d_i/v, is strictly decreasing on [0,1]. Its endpoint values straddle one: sum r_i>1 because F_h has an xa atom of mass1/4 and degree2; product(1-r_i)>0. All surviving r_i lie strictly between zero and one. Thus the intermediate value theorem applies; no square-sum condition is needed.

The source P and Q agree in empty mass and all marginals. Since log Q on nonempty atoms is affine in coordinate membership,

    CE(P,Q)=H(Q)
      =-p0 log p0-v log(v/c)
       -sum_i[d_i log(c d_i/v)+(v-d_i)log(1-c d_i/v)].       (1)

This evaluates the actual algebraic reference. Rational sign brackets of c enclose it; endpoint laws are not substituted for it.

Query b and then the first data bit only in b=1. Retain b=0 and both data children, keeping x,a unqueried. Under the same actual coherent kernels (fair fallback on source-zero rows), let A=KL(P||Q), R=I0-If, e=H0-Hf-4R, S=4If-Hf. The complete source account telescopes into all erasure, outcome and inherited terminal KL. Its conservative full liability is L=A+max(e,0). There is no fresh reference, no renewed bank, no earlier booked debit in this newly reached-root fixture.

The exact identity is

    S-(A+e)=4I0-CE(P,Q).                                (2)

Consequently CE>4I0 implies L>S for EVERY stopping continuation with this root and reference, even if all S is unused. A036's new signed recovery repair replaces L by J=max(A+e,0). For S>=0, J<=S is EXACTLY equivalent to CE<=4I0 by (2). Thus CE>4I0 also defeats this sharper rule. This is stronger than failure of the sufficient bound G<2 or of conservative payment alone. It is an obstruction to this prescribed reference at rate4, not an obstruction to FEI with an arbitrary absolute constant.

## 2. Tensor spectra and complete terminal accounting

Let h_{m,r} be the product of m point-defect signs on disjoint width-r blocks: each factor is -1 on the all-one assignment and +1 elsewhere. Put delta=2^-r, mu=(1-2delta)^m, t=(1-mu)/2. A point factor has empty squared coefficient (1-2delta)^2 and 2^r-1 nonempty squared coefficients 4delta^2. Tensor convolution is a product on disjoint coordinates, hence

    Hh=m H(point_r), Ih=2mr delta,
    root marginals=(1/2,1/2,t/2,delta/2 repeated mr times),
    I0=1+t/2+mr delta/2.

The two a-containing atoms of F have mass1/4; empty and x atoms each have mass p0; b and xb each have mass t^2/4; every nonempty core atom has four copies of one-sixteenth its mass. Therefore

    H0=1-2p0 log p0-2(t^2/4)log(t^2/4)
         +(Hh+mu^2 log(mu^2))/4+1-mu^2.                 (3)

Every selector of an independent character and a core g has H=2+H(g)/2 and I=1+I(g)/2; character-containing supports and core supports are disjoint. The first data restriction kills one point block at zero and reduces its width by one at one. Including the b=0 terminal with reach1/2 and each data child with reach1/4 gives

    Hf=2+(m-1)H(point_r)/4+H(point_(r-1))/8,
    If=1+(mr-1)delta/2, R=t/2+delta/2.                  (4)

For m,r>=2 both data cores remain nonconstant. Each point factor has H<=4I: its nonempty entropy is 8(r-1)delta(1-delta), and its empty entropy is at most4delta(1-delta)/ln2; ln2>1/2 suffices. Width0,1 are constant/character. Tensor additivity proves the same hereditary certificate for all restrictions. Thus every final selector has genuine certified surplus>=2; none of its terminal entropy has been dropped. These source facts independently reconstruct A050's hereditary premise.

## 3. An exact passing case beyond marginal admission

For (m,r)=(2,3), the exact interval certificate gives

    G=h2(t/2)+mr h2(delta/2) > S,
    S-L > 1 bit.

For orientation only, G is about2.521768, S about2.445771, L about1.030018, leaving about1.415752. Thus even the stronger marginal sufficient test G<=actual S fails, while the exact canonical liability passes. The signed query deficit is positive, about0.149500, and is INCLUDED. This uses all three actual terminals and one original unused owner. It does not merely replace the marginal bound by a different entropy floor.

## 4. A certified failure on a simple Boolean tensor

Take r=2. Each factor is a Boolean sign on two bits with four Fourier masses1/4, H=2, I=1. All tensor and restriction certificates are elementary. Here mu=2^-m,

    I0=1+t/2+m/4,
    Hf=(m+3)/2, If=(2m+7)/8, S=2+m/2.               (5)

At m=64, i.e.131 physical variables, a 56-step rational sign bracket and outward rational logarithms certify

    CE(P,Q)-4I0 > 1 bit,
    S-L < -1 bit.                                   (6)

Decimal displays are approximately1.971765856 for the excess, S=34 and L=35.971765856. Source/erasure/outcome/terminal KL are one telescoped A; the failure is not caused by duplicating them or discarding a branch. Even every bit of this actual terminal owner is insufficient. No truth table of 131 bits is constructed: (1),(3)-(5) are exact tensor certificates. Minimality is not claimed.

## 5. The all-dimensional boundary and its scale

For r=2,m>=2, v=(15-2mu-mu^2)/16<=15/16 and c>1/2. Indeed at c=1/2 the product is at most (11/15)^2(14/15)^4<1/2; hence the unique positive solution is larger. The normalizer equation then gives

    0<1-c <=(15/16)^(2m).

Thus c tends to1 and v tends to15/16. The control and empty terms of (1), divided by m, vanish: their arguments converge to strictly positive numbers, so they are bounded. Only the repeated data term remains. Continuity of log on positive arguments proves

    CE(P,Q)/m -> alpha
      = (1/4)log2(15/2)+(13/8)log2(15/13),
    I0/m ->1/4, H0/m ->1/2.

The term mu^2 log(mu^2)/m=-2mu^2 vanishes explicitly; no limit/sum interchange over growing dimension is needed after grouping the repeated term. Rational-log intervals certify alpha>21/20 (display1.0622053247866974). Therefore

    CE(P,Q)/I0 ->4alpha>21/5,
    H(F_h)/I0 ->2.

All sufficiently large m fail whole-owner payment at rate4. Any method demanding CE<=C I for THIS canonical reference must allow C>=4alpha. This lower floor is scoped to the prescribed reference; it is neither a lower bound on the FEI constant nor a claim against all reference mechanisms. A different fixed rate can still pay this family.

## 6. Review and exact remaining line

A050-NONPOINT-CANONICAL-GAP-REPAIR@1 is accepted unchanged at its stated scope. Sections1-2 reconstruct the normalization, source identity, entropy floor and hereditary terminal certificates without executing A050's helper. For its r>=8,2<=m<=r family, h2(u)<=u log2(e/u), log2(e)<3/2 and t<=m delta give G<m(r+1)(r+5/2)/2^(r+1)<=189/128; the last rational envelope decreases from r=8 since its successive ratio has numerator/denominator difference r^2-r/2-7>0. This is below its unused certified S>=2. The new obstruction has r=2 and large m, so it violates the source's G<2 hypothesis and does NOT refute that accepted theorem.

Checks that can fail: Fourier normalization and physical influence, tensor entropy, physical reach factors, both nonconstant children, existence/nonzero normalizers, support domination, signed query deficit, full-source versus conditional-only cost, and rigor of logarithm signs. The checker tests small actual truth tables by integer Walsh and direct edges, verifies (3)-(4), brackets the algebraic reference, and encloses the full bill. The continuum step is the grouped analytic limit above. The failed first pilot asked for a2^-60 interval width despite a56-bit root bracket; that numerical-resolution assertion was changed to2^-35, far below the unit strict-sign margins, and no failed run is counted.

FIRST UNSUPPORTED UNIVERSAL LINE: replace the canonical product-occupancy price by one that preserves the disjoint tensor/core correlations, or raise and prove a dimension-independent payment rate while carrying actual inherited source costs and both terminal bills after mixed queries and earlier bookings. An arbitrary-core supply theorem at rate4 with the unchanged Q is false. Full FEI remains OPEN. Independent review of this new obstruction and the stated asymptotic floor is pending.


## 7. Alternate representation and current peer objection

The separate conditional-law check uses c>=1-(15/16)^128 and H(Q)=h2(v)+(v/c)[sum_i h2(theta_i)-h2(c)]. Concavity bounds each entropy below by the smaller endpoint value, h2(c)<=h2(c_lower), and v/c>=v. Its exact lower bound gives CE-4I>3/2 (display1.95726836), without bisection. It shares the rational logarithm primitive, so it is a different mathematical reconstruction, not independent arithmetic software. Its sign agrees with the tighter excess1.971765856; the different displayed lower bound is intentional.

A036 run20261021T185858Z distinguishes conservative failure from actual signed payment failure; its parity-times-two-point example pays the sharp signed rule even when L>S. Equation(2) independently reconstructs that distinction. Here CE>4I, so J>S as well. A036's all-k theorem is not imported or claimed independently reviewed. The next mechanism must change the actual source/reference price, not merely take the positive part later.

A fresh memok receipt admitted a single-thread scalar Lean check. It returned RUNTIME_UNVERIFIED after40 seconds with no compiler output, target or axiom verification. The submitted rational implication says that S-(A+e)=4I-CE and CE>4I imply S<A+e. It does not formalize Fourier spectra or entropy; no formal acceptance is claimed. No retry or compiler job remains pending.
