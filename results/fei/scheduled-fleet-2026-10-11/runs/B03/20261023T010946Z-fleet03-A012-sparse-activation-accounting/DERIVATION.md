# Full signed-row payment through affine Fourier dimension three

All Fourier coefficients use the uniform probability normalization. Entropy, CE and KL are in bits. Ideal probability costs are used. Full FEI remains open; the new theorem is a structural closure with a required certified actual child.

## 1. Exact pure-child identity, in arbitrary physical dimension

Let S,V be disjoint uniform physical coordinate blocks, let c(S) be Boolean, let H(S,V) be any Boolean sign, and let z be fresh. Write H=c(1-2E), where E is the actual disagreement event; for each shared assignment s set q(s)=Pr_V(E|s), with no independence between different rows. Define F=mux_z(c,H), d=Pr(E), a_T=chat(T), b_T=Fourier_S(cq)(T), delta=sum_T b_T^2=E q^2. Let Phi(A,B)=A log2((A+B)/A)+B log2((A+B)/B), continuously extended to the axes. The shared-only selector amplitudes are a-b and b (up to an irrelevant common sign on the second sector). Nonempty-private H frequencies split equally between selector sectors. Their total parent mass is 2(d-delta), since the private mass of H is 4(d-delta). Thus exactly

    B_z=2(d-delta)+sum_T Phi((a_T-b_T)^2,b_T^2).

If a_T=0 then Phi(b_T^2,b_T^2)=2b_T^2. These terms cancel, giving the critical identity

    B_z=2d+sum_{T:a_T!=0}[Phi((a_T-b_T)^2,b_T^2)-2b_T^2].       (1)

Only the active Fourier frequencies of the pure child survive in (1). The full true entropy and reference cost of all other frequencies remain in the terminals below. Also sum a_T b_T=d, and every |b_T|<=d because q>=0. The physical identity is I(F)=(I(c)+I(H))/2+d, on the ORIGINAL coordinates.

Replacing H by -H complements q, takes d to1-d and exchanges selector sectors; B_z is unchanged. It suffices to prove B_z<4d for every d>0, then apply the same theorem to the complemented profile to obtain B_z<4d*,d*=min(d,1-d), when d*>0. At d*=0 the branches agree or are opposite pointwise, so B_z=0. No division by d is used on those boundaries.

## 2. Analytic sparse-support payment

Suppose a has at most four nonzero coefficients, in ANY number of shared coordinates. Put eta=sum_{a_T!=0}b_T^2. Then eta<=min(d,4d^2): the first bound follows from eta<=E q^2<=d, the second from |b_T|<=d. Moreover sum_active(a-b)^2=1-2d+eta. Concavity and homogeneity of Phi give

    sum_active Phi((a-b)^2,b^2)<=Phi(1-2d+eta,eta)<=h2(eta),

since eta<=d and Phi increases in either nonnegative argument. Hence B_z<=2d+h2(eta)-2eta.

For 0<d<=1/4, the function u log2(e/u)-2u is increasing on[0,1/4]. Using h2(u)<=u log2(e/u), eta<=4d^2 and x=4d gives

    B_z/d<=2+x[1/ln2-2log2 x]
           <=2+2/(sqrt(e)ln2)<4.

The maximum follows by one derivative; e>9/4 and ln2>2/3 suffice for the strict final comparison. For d>=1/4 the universal bound h2(u)-2u<=log2(5/4)<1/3 gives B_z<2d+1/3<4d. Both constants are certified by the elementary atanh series/cube checks in fixtures. Thus all sparse phases are paid analytically, with no physical-overlap bound.

## 3. Exhaustive three-bit phase classification

All256 sign tables on three bits have exactly1,4 or8 nonzero Walsh coefficients, in counts16,112,128. The one/four-support cases use Section2. Every eight-support phase is a common sign/character multiple of one point defect. CLASSIFICATION.json checks each table and supplies its unique tuple(sign,character,defect point), not just a histogram. Its coefficient magnitudes are one3/4 and seven1/4. Translation moves the defect to0 and common character/sign multiplication permutes/signs Fourier coefficients. These operations preserve B,d and permit arbitrary permutations of the row events; they do not replace the original physical influence ledger.

For the canonical point phase c(0)=-1,c(s)=1 otherwise, put a=(6,-2,...,-2)/8, M_Ts=c(s)chi_T(s). For any of the EIGHT independently varying probabilities q_s in[0,1], b_T=sum_s M_Ts q_s/8 and d=sum q_s/8. The old common-event or three-row rank-one assumptions are absent.

## 4. Exact complete eight-probability certificate

The Gibbs tangent Phi(A,B)<=lambda A+mu B uses fixed r in(0,1),lambda=-log2(1-r),mu=-log2 r. Since lambda+mu>=2,

    Phi((a-b)^2,b^2)-2b^2
      <=lambda a^2-2lambda ab+(lambda+mu-2)b^2.

For b linear in q, the right side is a convex quadratic. Subtracting2d and summing bounds B_z-4d by a convex quadratic whose maximum on each box occurs at a corner. Tangent parameters are fixed from the box center; zero amplitudes use the fixed rational clipping1/4096 or4095/4096. Upper rounding of both log weights preserves the inequality and nonnegative quadratic coefficient.

Partition[0,1]^8 into256 side1/2 seed boxes. If at least three coordinates have lower endpoint1/2, then d>=3/16>1/6. Such219 boxes are paid by the analytic moderate bound B_z<=2d+log2(5/4)<4d. GL(3,2), fixing the defect0, acts transitively on the one- and two-element subsets of the seven nonzero rows. The other37 seed boxes therefore reduce to FIVE representatives: no high coordinate; one nonzero high; two nonzero high; zero-row high; zero-row and one nonzero high. Their multiplicities are1,7,21,1,7. All168 invertible maps and all256 seed-box maps are explicitly checked in CLASSIFICATION.json.

Each representative is covered by an exact binary split tree on denominator128 coordinates. A leaf is either paid by the analytic rare bound (sum q<=1/4), by the moderate bound(sum q>=4/3), or by strictly negative tangent maxima at all256 corners. All5 jobs PASS:332 positive leaves,8 analytic leaves,335 splits,675 total nodes, no unresolved boxes. Integer Gray-code evaluation is used by the author, with outward80-bit24-term atanh logarithms and a proved tail.

The verifier imports no author module. It uses A013's credited160-bit binary-squaring logarithm enclosure,64-bit upper weights, DIRECT character sums at every one of the256 corners, and exact recursive tree reconstruction. Every node is reached exactly once; no missing child, duplicate, extra record or unverified seed map is allowed. Its minimum positive gap and assertion counts are in EXACT_RESULTS.json. Sparse-support analysis plus these finite phase/symmetry reductions and complete continuum covers prove

    B_z<4min(d,1-d), when0<d<1, for EVERY three-bit pure phase
    and ALL EIGHT arbitrary, possibly correlated, private row events.        (2)

The analytic rare bound used in the point jobs is the already reconstructed B<=2d+h2(delta)-2delta with delta<=min(d,8d^2). For0<d<=1/32 it gives B/d<=2+(5+1/ln2)/4<4. The moderate bound comes from maximizing h2(u)-2u at u=1/5; (5/4)^3<2. These are bounds on the exact Boolean family, not presumed realizability of a relaxed spectrum.

The attempted two-total log-sum relaxation is NOT used. PILOT.json records a numerical upper ratio about4.066: grouping the seven small Fourier rows loses signed information. The full signed-row certificate repairs that loss; it does not assert a Boolean counterexample to the relaxation's target or FEI.

## 5. Parity quotient: unbounded physical overlap

Define affine Fourier dimension as dim span_{F2}{T xor R:T in supp(chat)}, for any R in that support. Suppose it is r<=3. Choose independent characters L1,...,Lr spanning those differences. The expansion is

    c(s)=chi_R(s) g(L1(s),...,Lr(s)),

where g is a Boolean sign on r uniform parity coordinates. Booleanity holds because chi_R c takes values+-1 and depends only on these parities; linear independence makes their map onto the full r-cube. The character R may be outside their span.

Set qbar(y)=E[q(s)|L(s)=y]. For every active T=R xor L_U, the two character factors cancel:

    a_T=ghat(U), b_T=E_y[g(y)qbar(y)chi_U(y)], d=E_y qbar(y).

Equation(1) is therefore IDENTICAL to the r-bit pure-child erasure formula with row probabilities qbar. Pad with dummy parity coordinates if r<3; the all-eight-row theorem covers repeated row values. This is an exact reduction, not a lossy entropy bound, and proves(2) in arbitrarily many physical shared coordinates whenever the pure child has affine Fourier dimension<=3. No coordinate-influence invariance under parity changes is assumed. In particular physical overlap can grow without changing K.

## 6. Complete reference and noncircular structural admission

The scalar channel dependency JS_z<=2d*/ln2 now yields Delta_z=H(F)-(H(c)+H(H))/2<=K d*, K=4+2/ln2<7. Supply normalized finite-cost references positive on the actual child spectra. Calibrate each shared-only singleton atom to its true mass and retain/rescale the complete private conditional reference, including off-target mass. CE decreases by categorical KL. The pure child's calibrated reference is its spectrum. Let Q equal the true parent law on shared-only atoms, and assign R_Hcal(T,U)/4 to BOTH selector sectors for U!=empty. Then

    sum Q=1, D_F=D_Hcal/2,
    CE_F=(CE_c+CE_Hcal)/2+Delta_z.

These equalities retain the full true joint private entropy. Arbitrary row events are never assigned an independent product reference. The rho=0 private category is removed without dividing by zero. An independent common terminal factor adds all of its CE/KL; it is not a spare reserve.

Add the following to the v5 grammar: exact-spectrum leaves c of affine Fourier dimension<=3, and fresh-selector nodes with such a pure shared child and ANY actual H on shared/private coordinates, provided BOTH ACTUAL CHILDREN already carry structural certificates. A nonconstant such leaf has at most8 Fourier atoms and H(c)<=3. If chi_R is outside the parity span, its mean is0; otherwise a nonconstant r<=3 parity truth table has |mean|<=3/4. Thus Var(c)>=7/16, I(c)>=Var(c), and H(c)<=48I(c)/7<K I(c), since ln2<7/10. Constants have entropy0. This certifies the leaf without assuming full FEI or an opaque terminal bound.

Restrictions project Fourier supports, so affine Fourier dimension cannot increase. Private/shared restrictions keep the new form with the actual event cofactors; selector restriction chooses its certified child. Structural induction supplies the restricted child certificates. Earlier signs, disjoint products, balancing and fresh point activations remain closed. Conversely restrictions of a fresh balanced tensor or rare activation recover its original seed up to sign. Thus membership still reflects to a hidden seed: arbitrary difficult cores do not receive admission by rarity.

The enlarged grammar is proper. The five-bit at-least-two sign has affine Fourier dimension5; every one-bit cofactor has ALL16 Fourier coefficients nonzero, hence affine dimension4. Such roots cannot be new leaves or pure-child nodes. The old overlap<=2 roots are excluded by the four-variable intersections, activation roots by the absence of a constant cofactor, and all15 disjoint product roots by nonzero2x2 minors. These stronger affine-dimension witnesses replace the earlier insufficient support-size-only argument for the new grammar. This is a nonmember of the syntax, not a FEI counterexample.

## 7. Exact remaining bridge

The previous four-to-eight-row three-bit gap is CLOSED for a pure child, including arbitrary private correlations and its rank3 parity lifts. What is not proved is a corresponding payment when BOTH branches have private fluctuations: the active pure-spectrum cancellation used in(1) is then unavailable. Affine dimension4 cannot simply inherit the same selector-only constant: A013's actual four-bit bent origin edit has Delta>7d. The shortest next route is one both-private rank3 collision paid from genuinely unused inherited child/shared surplus, with both full terminal references retained, or a selected rank4 query using that surplus. No original L/S/R contraction, universal representation existence, all-history fresh-reference reset or full FEI is claimed. New v6 proof is pending independent-agent review.
