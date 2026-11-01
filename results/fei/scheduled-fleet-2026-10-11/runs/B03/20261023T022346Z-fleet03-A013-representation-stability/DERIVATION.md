# Rank-three collision review and exact physical quotient transport

The new A012 v6 pure-child collision/quotient increment holds at its stated scope. The parity rank alone does not specify how its probability profile changes under a physical restriction. The exact update below retains the original disagreement event and shows what information must travel with the representation. Neither result proves full FEI.

## 1. Independent review of the new v6 increment

Let c(S) be a pure Boolean child, H(S,V)=c(S)(1-2E(S,V)) any actual Boolean child, V independent of S, and z a fresh physical selector. Write q(s)=Pr_V(E|S=s), d=E q, a_T=chat(T), b_T=Fourier(cq)(T), delta=E q^2. On the private-zero Fourier sector the parent amplitudes are a-b and b. Every nonempty-private frequency belongs to H only and splits into equal squared parent amplitudes. Its combined parent mass is 2(d-delta). Therefore

    B_z=2(d-delta)+sum_T Phi((a_T-b_T)^2,b_T^2)
       =2d+sum_{a_T!=0}[Phi((a_T-b_T)^2,b_T^2)-2b_T^2].       (1)

Here Phi(A,B)=(A+B)log2(A+B)-Alog2 A-Blog2 B, continuously extended to zero. The second equality is exact because a_T=0 makes Phi(b_T^2,b_T^2)=2b_T^2. No private event independence is used, and the entropy of inactive frequencies stays in the complete terminal cost. Physical influence remains I(F)=average child I+d on ORIGINAL coordinates.

If at most four a_T are nonzero, let eta=sum_active b_T^2. Then |b_T|<=d, eta<=min(d,4d^2), sum_active(a-b)^2=1-2d+eta, and concavity gives B<=2d+h2(eta)-2eta. For d<=1/4 this yields B/d<=2+2/(sqrt(e)ln2)<4. Indeed u log2(e/u)-2u increases on[0,1/4], and x(1/ln2-2log2 x), x=4d, has maximum2/(sqrt(e)ln2). The elementary bounds e>9/4 and ln2>2/3 make that constant strictly less than2. For d>=1/4, h2(u)-2u<=log2(5/4)<1/3 yields B<4d. The endpoints are treated without division by d.

The exact classification of all256 three-bit phases gives Fourier-support counts1,4,8 in multiplicities16,112,128. All full-support phases are common sign/character multiples of one translated point defect, with coefficient magnitudes3/4 and seven1/4. Classification and all168 GL(3,2) maps are recomputed. Of the256 half-cube probability seeds,219 are entirely in d>=1/6. The other37 reduce to five seed orbits with multiplicities1,7,21,1,7.

All five source trees are independently reconstructed:675 nodes,332 positive tangent leaves,8 analytic leaves,335 binary splits. Every leaf is verified with EXACT Fraction32-term atanh logarithms, a proved rational remainder, and outward64-bit weights. This differs from the author's fixed-point Gray-code calculation and from the source's verifier, which reused A013 binary-squaring logarithms. No source module is imported. Direct evaluation of every one of the256 corners checks each convex majorant. The majorant is valid because, with lambda=-log2(1-r), mu=-log2 r, Gibbs gives Phi(A,B)<=lambda A+mu B and lambda+mu>=2. After subtracting2b^2 its coefficient of b^2 is nonnegative. Complete tree reconstruction checks both children of every split and rejects duplicate, unreachable or missing nodes. Thus this is a continuum certificate, not sampling.

It follows that B_z<4d for d>0 in the full eight-row pure-child family. Replacing H by -H exchanges the selector sectors, preserves erasure and child entropies, and takes d to1-d. Consequently B_z<4min(d,1-d) when0<d<1; B_z=0 at both endpoints.

## 2. Exact affine Fourier quotient and retained reference

Suppose the pure child has affine Fourier dimension r<=3: its nonzero frequencies lie in R+W, with W spanned by independent masks L1,...,Lr. Then

    c(s)=chi_R(s) g(L(s)),       Y=L(S) uniform on F2^r.

For T=R+L_U in the active coset, character factors cancel:

    a_T=ghat(U),  b_T=E[g(Y) qbar(Y) chi_U(Y)],
    qbar(y)=E[q(S)|Y=y],  d=E qbar(Y).

Equation(1), not the full spectrum, reduces exactly to this quotient. Padding dummy coordinates uses the full eight-row theorem. It follows that the SAME local K=4+2/ln2<7 works for arbitrarily many physical shared coordinates when the pure child has affine rank<=3. There is no assertion that a parity change preserves physical influence.

For supplied normalized child references, calibrate shared-only singleton masses and keep the complete joint private conditional law, including off-target reference mass. The pure child becomes its true spectrum; calibration decreases CE by categorical KL. On parent private-zero atoms take Q=P_F; on every nonempty-private H atom assign R_Hcal/4 to each selector sector. If rho is the true H private mass, these pieces have masses1-rho/2 and rho/2, so Q is normalized. Direct log expansion gives

    D(P_F||Q)=D(P_H||R_Hcal)/2,
    CE_F=average calibrated child CE+Delta_z.

No private terminal bill is discarded. The rho=0 category is removed, never divided by. Scalar C005 gives Delta_z<=K min(d,1-d)<=K d. Thus two already certified ACTUAL children give a certified parent; arbitrary opaque H is not admitted for free.

For a nonconstant pure rank<=3 leaf, H(c)<=3 and Var(c)>=7/16: if the carrier R lies outside W the mean is zero; otherwise a nonconstant at-most-three-bit truth table has mean magnitude at most3/4. Poincare gives H(c)<=48I(c)/7<K I(c), using ln2<7/10. Constants use the vacuum. Restriction projects the affine support, so rank cannot increase. These leaf/reference/new-node conclusions are independently reconstructed; this is not independent acceptance of the entire inherited v1-v5 syntax or all old nonmember claims, because earlier A013 inputs were credited and those chains are not re-audited here.

## 3. New exact block cofactor law

This statement holds for ANY finite uniform cube X in F2^n and any function q:X->[0,1], not only rank3 or a Boolean phase. One may use q=1_E on the whole shared/private data cube; doing so retains the correlations needed for later private queries. Let L have independent rows spanning W of rank r, Y=LX, and let A be a set of physical coordinates exposed to the assignment a. Put

    C_A=span{e_i:i in A},       t=dim(W intersect C_A),
    m_K(y)=E[q(X) chi_K(X)|Y=y],       K subset A.

Define the compatible affine coset C_a by requiring chi_U(y)=chi_K(a) whenever L_U=K belongs to W intersect C_A. Its codimension in F2^r is t. Then:

1. Y conditioned on X_A=a is uniform on C_a, which has2^(r-t) points. Equivalently, the rank of L after removing columns A is r-t.
2. For y in C_a, Pr[X_A=a|Y=y]=2^(-(|A|-t)). It is zero off C_a.
3. The ACTUAL restricted profile is

       qbar_a(y)=2^(-t) sum_{K subset A} chi_K(a) m_K(y),  y in C_a.       (2)

Proof: conditioning a uniform cube on Y=y gives a uniform affine fiber. The |A| coordinate constraints have t linear consequences already fixed by Y; their remaining |A|-t independent constraints cut every compatible fiber by exactly2^(|A|-t). This proves1-2 and the rank identity. Expand the physical indicator as

    1_(X_A=a)=2^(-|A|) sum_{K subset A} chi_K(a) chi_K(X).

Taking its q-weighted conditional expectation given Y=y and dividing by the POSITIVE probability in2 gives(2). Incompatible rows are not assigned a quotient and no zero denominator is canceled. Repeating this law along a history uses the SAME original event and its conditional moments; Bayes conditioning on the union of exposed coordinates gives the same result as successive updates. No new entropy/influence account is created by that identity.

For one exposed coordinate i, there are two distinct cases. If e_i belongs to W, the surviving rows satisfy chi_alpha(y)=(-1)^a for the unique L_alpha=e_i, rank drops by one, and qbar_a is the restriction of qbar. If e_i is outside W, rank is unchanged, every old label survives, and

    qbar_a(y)=qbar(y)+(-1)^a E[q(X)chi_i(X)|Y=y].                 (3)

The extra moment is necessary even when the rank is preserved. A marginal row profile alone does not carry it. This is the first new mathematical transport statement of this stage; it fills in the precise profile operation behind the new parity-rank closure.

## 4. Label, fiber-cell and root metadata

For a full parity-fiber representation of c include the carrier chi_R in the label map if it is independent of W, then choose an independent basis Z of that map. Its rank k is at most r+1. The function c is constant on each Z fiber. Retain those fibers on which c=+1; these form an exact positive-fiber cover. They are parity cells, not a newly asserted cover by regular AND gates.

Apply Section3 to Z. If t_Z=dim(span(Z) intersect C_A), surviving labels are uniform on an affine coset of size2^(k-t_Z). Thus their label entropy is EXACTLY k-t_Z bits, with loss t_Z, and each surviving cell density is pi'=2^t_Z pi, where pi=2^-k. Incompatible cells disappear. The number N' of surviving positive cells is at most N; there are no extra cells. If all or none of the compatible labels are positive, the physical child is constant and uses the vacuum reference. Otherwise the declared uniform-weight root-reference parameter changes from pi/(N+pi) to pi'/(N'+pi'). More general inherited lambda gives lambda*pi'/(1+lambda*pi') until a separately declared reweighting.

These are explicit transformed representation/count/label/density facts. They do NOT say that root-reference renormalization or replacement of a prescribed full reference is free. A reference Bernoulli parameter is not a physical witness-root probability. Full nonroot costs and original L,S,R monotonicity are not inferred from these metadata. Transport of a prescribed historical CE/KL bank remains a separate C024 obligation.

## 5. Actual stale-profile counterexample

Use four shared physical bits s1,s2,s3,s4, parity map Y=(s1 xor s4,s2,s3), and the three-bit point phase g(0)=-1,g(y)=1 otherwise. Let c(s)=g(Y), H(s)=-c(s)chi_4(s), and select them with a fresh z. The disagreement event is s4=0. Every parent parity fiber has qbar=1/2, and the pure child has affine Fourier rank3. The active pairs in(1) give B_z=1.

Expose the PHYSICAL coordinate s4. Since e4 is outside span(L), rank remains3 in both actual children. But the event is now constant: qbar_0=1 and qbar_1=0. Hence H=-c or H=c respectively, and both child erasures B_z are zero. Keeping the old qbar=1/2 would incorrectly predict B_z=1 in both children. Direct integer Walsh/prime-log checks confirm the three erasures and both child ranks. This counterexample refutes only stale-profile transport, not the v6 theorem or FEI.

## 6. Exact validation and unpaid line

The continuum/classification jobs make6,816 exact assertions. The384 parity-lifted Boolean parents on4,5,6 physical shared bits and2 private bits make111,736 assertions, checking full-reference KL, actual physical influence, active cancellation, quotient identity and singleton cofactor updates in BOTH rank cases. All1,944 declared block restrictions on four shared bits, ranks1..4 and six actual dyadic event profiles make30,172 further assertions. Total148,724 PASS. The fixtures support the general proofs; the proofs above and exact full-cube certificate supply the all-dimensional/all-real conclusions. All jobs are below50s and120MB estimates. memok refused compiler admission with physical2.8GB below4.0GB, despite sufficient commit headroom; no Lean check is claimed.

The immediate remaining line is payment of one BOTH-private rank3 collision from genuinely unused inherited shared/child surplus with both full references retained. Equations(2)-(3) specify how its physical row profile must change, but do not supply that surplus. The prior four-shared-bit bent edit already has Delta>7d, so rank growth cannot simply inherit the pure rank3 selector-only constant. Original-queue contraction and universal witness-cover existence remain unproved. Full FEI stays open.
