# Padding-stable degree tilt: reset payment without a mask-count floor

All information is in bits. This is an extension of A056 v6, conditional on the v5 activation/mux reference transport and supplied initial source prices. It does not construct universally cheap initial references and does not prove FEI.

## 1. A pure prescribed law and its exact signed price

For a Boolean phase f on any finite uniform cube let P(T)=fhat(T)^2, V=1-P(empty), and J=I(f)=sum |T|P(T). When V>0 define the fresh degree-tilted law

    S(empty)=P(empty),   S(T)=V |T|P(T)/J  (T nonempty).       (1)

When V=0 set S=P. This is normalized, supports every positive true atom, is empty-calibrated, and is invariant under adjoining dummy coordinates. It is a full replacement, determined by the actual current phase, not an interpolation with the inherited reference R. Reference-only atoms may be discarded. No positive lower bound relative to R on those zero-true-mass atoms is asserted or required.

Writing p=P/V on the nonempty sets and r=J/V>=1 gives exactly

    D(P||S)=V log2 r - sum_(T nonempty) P(T)log2 |T|.       (2)

For every normalized inherited reference R supporting P and with the same empty atom,

    Delta c=CE(P,S)-CE(P,R)=D(P||S)-D(P||R).                (3)

In particular, by KL nonnegativity and |T|>=1,

    Delta c <= V log2 r <= J.                             (4)

For the final inequality, differentiation gives (ln r/r)'=(1-ln r)/r^2, so the maximum on r>=1 is1/e, attained at r=e. Thus (log2 r)/r<=1/(e ln2)<1. The strict numerical comparison follows from e>5/2 and ln2>1/2, giving e ln2>5/4. The simpler allocation constant1 in(4) is used throughout; the sharper constant is not needed for any finite sign certificate.

Equations(2),(3) retain the entire old reference bill. If the exact true spectrum is used as R then the fresh reset can have strictly positive cost whenever nonempty spectral degrees are not all equal. Conversely the reset can refund an inherited discrepancy. No sign is replaced by an absolute value in the final identity.

## 2. Same original allowance and complete physical ledger

Use v5's two phases u,v, private disjoint point events of probabilities a,b, and fair mux (possibly already selected). At a reached state write wu=pi*a and wv=(1-pi)*b. Its compatible root reference has

    KLroot=wu(1-a)Du+wv(1-b)Dv,
    CEroot<=wu cu+wv cv+Icore+7Icontrol.                  (5)

A pure reset of source j has exact root excess

    ej=wj(1-aj) Delta cj,   max(ej,0)<=wj I(j).           (6)

The weighted source influence Xj=wj I(j) is nonnegative, harmonic at private/selector queries and a supermartingale at shared queries. Reserve qj ORIGINAL units Xj,root, where qj is a nonnegative integer. Each actual reset consumes one unit of its source's remaining counter. Finite optional stopping applied to counter*Xj, or separately to each ordinal reset frontier, gives

    sum reached positive reset bookings <=sum qj Xj,root. (7)

Counters are carried on both actual outcomes and never replenished. Any finite adaptive physical tree may decide when to reset, whether to reset, and when to stop, but has at most qj resets of source j on each path. Complete terminal references are the actual carried or newly prescribed references, not automatically reissued cheap source certificates.

For the actual physical CE releases Cphys, including erasure, Boolean channel, outcome KL, conditional KL and category calibration, and the FULL expected terminal CE T, the exact signed telescope is

    Cphys+T=CEroot+sum reach*ej
           <=Broot+sum qj Xj,root.                       (8)

All old query debits, opposite children and full H+KL terminal costs remain. If initial cj<=Cj I(j), then the right side is bounded by K Iroot with

    K=max(Cu+1+qu,Cv+1+qv,7).                            (9)

Thus initial Cj<=3 allows THREE genuine degree-tilted replacements per source at the SAME rate7, in arbitrary phase dimension, after arbitrary permitted mixed physical histories. More generally supplied Cj<=5 allows one replacement at rate7. The theorem is conditional on the supplied source price; no cheap price is inferred merely from writing down S.

## 3. Why this is a useful interface and not the missing supplier

The previous stage's ordered mask floor failed under dummy padding. Law(1) removes that obstruction and removes the two-bit restriction for the reset-payment step. It really changes the conditional nonempty profile on mixed-degree phases. Its definition uses the full true spectrum, and its price still contains H(f): CE(P,S)=H(f)+D(P||S). Therefore a universal influence-price for S is equivalent up to the additive constant in(4) to FEI itself: FEI(C) implies CE(P,S)<=(C+1)I, while CE(P,S)<=K I implies H<=K I. The reset theorem does not independently solve that equivalent initial-source problem.

It also does NOT imply that any other canonical law is affordable, does NOT control actual pivotal-set entropy on the physical cube, does NOT establish arbitrary repeated-reset payment from a single counter, and does NOT extend to an unbounded number of unbudgeted replacements. Set-size bias is spectral; no spectral/pivotal equality is assumed.

## 4. Adversarial boundaries and validation design

A character has all nonempty degree mass at one level and S=P, so its reset is free under dummy padding. A mixed-degree function has D(P||S)>0 by strict KL unless the size tilt is constant P-almost surely. Exact checks use every three-bit Boolean phase with R=P and with an oversupported equal-nonempty R, the eight specified five-bit phases, and dummy-padded copies. Direct character sums independently reconstruct selected Fourier spectra and literal edges independently reconstruct influences.

The physical fixtures start with five shared bits, exact initial phase references, private widths(1,1) or(2,1), and a fair mux. They query shared0; reset both phases; query a private/selector control on both outcomes; query shared0; reset both; query shared0; reset both; query shared0 then stop. Thus the first two rounds occur with four and three remaining shared coordinates. All outcomes are retained, including constant/zero-variance boundaries. Positive bookings are charged separately per source and per ordinal counter, and their weighted total is compared to the SAME original3 Icore. The signed telescoping identity is checked separately from that upper bound. This finite domain does not prove the arbitrary-dimension/frontier theorem; sections1-2 do.

## 5. First unpaid universal line

Supply initial normalized support-dominating references with CE<=C I for arbitrary Boolean phases, or derive a genuinely new physical-energy bound replacing that supplied hypothesis. The degree-tilted fresh law itself cannot supply this for free, since its universal price is FEI-equivalent. Independent reconstruction of the v5-v7 transport chain remains pending. Full FEI is OPEN.
