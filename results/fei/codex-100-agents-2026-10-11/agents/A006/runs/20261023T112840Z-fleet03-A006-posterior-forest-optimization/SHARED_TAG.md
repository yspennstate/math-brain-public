# A paid once-per-set clause anchor with its actual posterior refund

All costs are in bits. This is a NEW normalized joint-set reference, not the original positive/negative-prime queue and not a claimed canonical partition-forest subfamily. The change of mechanism is necessary after the source queue obstructions. The reference is built only from a supplied disjoint clause decomposition and its widths, not by copying the target Fourier law or borrowing its entropy.

## 1. Boolean family and the new sampler

Fix ANY finite nonempty list of positive integers w_1,...,w_r. On independent X and Y copies of these physical clauses let

    U(X)=product_j OR_(w_j)(X_j),
    V(Y)=1-U(-Y),  F=2U(X)V(Y)-1.

Write t_j=2^-w_j, p_j=1-t_j, q=product p_j,
rho=sum t_j, D=sum w_j*t_j/p_j. For each of the2r labelled physical clauses define a probability on its local Fourier subset: empty with probability p_j, each particular nonempty subset with probability t_j^2/p_j. These probabilities sum to1 because there are(1-t_j)/t_j nonempty subsets. Let mu be their independent product on all clauses.

The NEW actual sampler first chooses an anchor J among2r labelled clauses, with probability t_j/(2rho). Its selected subset is uniform nonempty; every other clause independently uses its local law just defined. Draw other clauses in a fixed canonical order, once each. The actual run is the chosen anchor plus this fixed tuple of local draws. There is no arbitrary draw-order/shuffle choice and no second description of one run. The selected nonempty output A is the union of the local subsets. Every sampler run produces an output, so no success or nonempty conditioning is hidden.

If K(A) counts active physical clauses, the EXACT joint mass for each allowed actual anchor J is

    q_new(J,A)=mu(A)/(2rho),  J active in A.

Thus the complete output law is

    Q_new(A)=K(A)mu(A)/(2rho),  A nonempty.               (1)

It is normalized: E_mu K=2rho, so sum_(A nonempty)Q_new(A)=1. One can also normalize by summing each actual anchor's prior and conditional law. The r parameter is not bounded and all clauses have positive prior. Distinct anchors are distinct actual FIRST random choices; alternative notations or permutations of the fixed later draws are not additional runs.

## 2. Optimal posterior, not a fictitious witness discount

For a fixed nonempty output A, the actual posterior is uniform on its K(A) possible anchors. It has entropy log2 K(A). Consequently

    inf_eta [E_eta(-log q_new(J,A))-H(eta)]
       =-log mu(A)+log(2rho)-log K(A)=-log Q_new(A).     (2)

The exact identity follows also by adding KL(eta||uniform_K) to the right side. In particular the refund is earned by distinct real first draws; the root tag is paid once per set. The dictionary is a new clause-subset dictionary; its tags are generally NOT implicants of F. Equation(1) does not establish success of an unrestricted mixture of original prime queues, which remains a separate question.

The normalization mechanism extends to ANY supplied finite family of nonempty
physical supports, even overlapping ones. Give each support the same local mask
law with t=2^-width. Let z be the tuple of independently sampled local masks,
mu(z) their product law, K(z) its number of nonempty masks and rho=sum t over
this single support family. Choose anchor j with prior t_j/rho and force its
mask nonempty. Actual run(j,z) has mass mu(z)/rho whenever z_j is nonempty.
Its physical output is the UNION of local masks. Thus the complete law is

    Q_overlap(A)=sum_(z:union z=A) K(z)mu(z)/rho.         (2a)

This is normalized since E_mu K=rho. The posterior is the normalized actual
mass on ALL pairs(j,z) producing A. Both the anchor and allocation ambiguity
must be refunded; no two symbolic descriptions of one local draw tuple are
counted separately. Provided the supports cover every relevant variable, the
law is positive on every nonempty physical output set. This closes reference
normalization, NOT influence payment, for arbitrary finite support covers.
The disjoint paired case above has total activity2rho and a unique allocation
z per physical output, reducing exactly to(1),(2).

Equation(2a) is computable without listing anchor histories. Maintain two
exact probability arrays a(A),b(A) over physical unions, initially a(empty)=1
and b=0. On a local mask S of probability m_j(S), update

    a_next(A union S) += a(A)m_j(S),
    b_next(A union S) += [b(A)+1_(S nonempty)a(A)]m_j(S).

Then a is the union pushforward of mu and b is the K-weighted pushforward;
Q_overlap=b/rho on nonempty sets. This costs O(2^n sum_j2^width_j) exact
rational operations and two arrays of size2^n. Its additions combine distinct
actual local-draw events rather than counting aliases of one event. For a
finite actual Boolean truth table, an integer Walsh transform followed by
rigorous log intervals therefore gives computable exact-mass and certified
cost intervals for this new whole-set variational objective. No polynomial
runtime or universal influence payment is asserted.

## 3. Direct physical Fourier and influence payment

For indicator U, the empty local coefficient of a clause is p_j and every nonempty local coefficient has magnitude t_j. For V, nonempty global coefficient magnitudes agree with those of U; its empty coefficient is1-q. F has nonempty coefficients2 Uhat(A_X)Vhat(A_Y), up to signs irrelevant to squares. All these statements follow by expanding the actual indicators, with no FEI assumption.

For each j let M_j=sum_(A nonempty) Fhat(A)^2 [1_(A_Xj nonempty)+1_(A_Yj nonempty)]. Parseval for the other factors gives the EXACT identities

    M_j=4q t_j,
    I(F)=2q sum_j w_j*t_j/p_j=2qD.                      (3)

One may independently check influence physically: a pivot inside U's jth clause requires all its other bits zero and all other clauses true, giving2t_j q/p_j per coordinate. The X pivot is further gated by V with probability1-q, and the Y pivot by U with probability q. Their sum gives(3). If a clause is active, its nonempty subset is uniformly distributed in the actual squared spectrum, with conditional mean size w_j/(2p_j); this gives the same influence identity from M_j. The exact nonempty squared mass is v=4q(1-q)[1-q(1-q)]<=4q.

Put a_j=-log p_j>=0 and b_j=log(p_j/t_j)>=0. The FULL output cost, with its optimal actual-anchor posterior, is exactly

    C_new=v[2sum_j a_j+log(2rho)]
              +2sum_j b_j M_j
              -sum_(A nonempty) Fhat(A)^2 log K(A).     (4)

No term is an unpriced entropy of F. All local masks, the paid anchor, and the posterior ambiguity appear in(4).

## 4. Uniform constant, including unequal widths and arbitrary clause count

Using v<=4q, a_j>=0 and M_j=4qt_j, the base plus occupied-clause terms in(4) are at most

    8q sum_j [a_j+t_j b_j]=8q sum_j h2(t_j).            (5)

For t=2^-w, w>=1, ln2>2/3 and -ln(1-t)<t/(1-t) imply

    h2(t)<(w+3/2)t.

Moreover

    (1-t)(1+3/(2w))<=4/3.

For w=1,2,3,4 the left sides are5/4,21/16,21/16,165/128; for w>=5 they are at most13/10. Therefore h2(t)<(4/3)w*t/(1-t). Dividing(5) by I=2qD pays these terms by<16I/3.

If log(2rho)<=0 its contribution in(4) is nonpositive and may simply be retained or omitted for an upper bound. Otherwise, v<=4q and D>=2rho give

    v log(2rho)/I <=log(2rho)/rho.

The bound D>=2rho follows termwise from w/(1-2^-w)>=2: equality at w=1 and immediate for w>=2. Elementary calculus gives sup_(x>0) ln x/x=1/e, so

    log2(2rho)/rho<=2/(e ln2)<9/8,

using e>8/3 (already its first five series terms suffice) and ln2>2/3 (positive atanh series). Dropping only the NONNEGATIVE actual refund in(4) now yields

    C_new < (16/3+9/8)I=(155/24)I<7I.                 (6)

This holds for every list of clause widths and every finite r>=1. In particular on the actual source obstruction r=2^w it replaces the growing original-queue cost by a paid once-per-set code with an absolute constant. The source obstruction remains correct: this sampler has different dictionaries and local laws and is outside its refuted class. No novelty claim for FEI on these formula families is made.

## 5. Universal frontier

The COST proof needs disjoint physical clauses and the explicit product Fourier occupancy identities(3). For arbitrary overlapping supports, equation(2a) already supplies a normalized actual-run law, but its physical-output posterior must include allocations and no influence payment analogous to(3)--(5) is proved. The first unsupported universal line is an influence-paid occupancy/compatibility bound for this full pushforward law, with the tag and allocation refunds retained. Replacing that premise by FEI, using an output-dependent prior, or copying the target spectrum would be circular. A separate open question is whether sufficiently many ORIGINAL clause-specialized prime queues succeed; the new sampler neither answers that nor contradicts the source lower bounds.
