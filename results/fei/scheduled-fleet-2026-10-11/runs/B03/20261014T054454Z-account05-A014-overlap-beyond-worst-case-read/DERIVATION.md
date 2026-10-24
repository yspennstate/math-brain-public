# Paid separator conversion and occupation/reference comparison

All logarithms are base two, functions are Boolean +/-1 on finite uniform cubes. The stage-4 interface is copied unchanged into PREVIOUS_INTERFACE.md for equation locators. This stage pays a specific reference excess; it does not pay the full terminal/gate entropy in that interface.

## A. Separator reference conversion costs at most 2I

Let C(x,Y,Z)=h_x(Y)k_x(Z) be as in the previous interface, with nested Boolean blockers and disjoint private cubes. Set a_i=E h_i,b_i=E k_i,A_i=a_i b_i,s=(A0+A1)/2 and v=4s(1-s). Use the EXACT normalized component blocker spectra as the terminal references in previous equation (6). Then R is the actual private-row distribution, and Q_C(T,xi)=R(T)/2. For 0<s<1 let q_e=Q_C(empty) and Q_prod be previous equation (8), conditioned to nonempty output with empty output mass 1-v.

At the empty private row z_i=A_i, so

    q_e=(A0^2+A1^2)/(4s)>=s/2.                              (11)

The actual normalized blocker spectrum P_C has a selector-bit conditional probability in [0,1]. Consequently P_C(A)<=2Q_C(A) at every A. After nonempty conditioning,

    P_C(A|nonempty)/Q_C(A|nonempty)
       <=2(1-q_e)/(1-s)<=(2-s)/(1-s).

Thus, from the exact conditional KL formula (10),

    0<=CE(f,Q_prod)-H(f)
      <=v log2[(2-s)/(1-s)]<=2I(f).                         (12)

Here is the proof of the last bound, including its only geometric ingredient. If s<=1/2, (2-s)/(1-s)<=3<4, so the right side is at most 2v<=2I by Parseval (each nonempty set has size>=1). If s>1/2, put epsilon=1-s. Concavity of ln gives

    s ln(1+epsilon)+epsilon ln epsilon
      <=ln[s(1+epsilon)+epsilon^2]=0.

Therefore s log2[(1+epsilon)/epsilon]<=log2(1/epsilon). The bound in (12) is <=4epsilon log2(1/epsilon). Cube edge isoperimetry applied to 1-C gives I(f)>=2epsilon log2(1/epsilon), completing (12). Constants s=0 or 1 use an empty point mass and have zero reference excess. No hypothesis on dimension or read is used in this conversion. This is not H(f)<=2I: H(f), including all four terminal entropies and gate-collision cost, remains in the comparison.

For completeness the needed cube isoperimetric inequality has an elementary induction. For an event of mass p, prove I(1-2event)>=2F(p), F(p)=p log2(1/p). Split along one bit into masses p0,p1. With t=p0/(p0+p1), the Jensen gap is

    F((p0+p1)/2)-(F(p0)+F(p1))/2
       =(p0+p1)[1-h2(t)]/2<=|p0-p1|/2,

using h2(t)>=2min(t,1-t) from concavity. The shared-bit influence is at least |p0-p1|, and private influence is the average of the two branch influences. The induction and constant base cases prove I>=2F(p). Applying the same inequality to the complement gives the version used above.

This pays the excess only for exact component spectra. Arbitrary component reference KL debts are not replaced by zero. Applying the result in a recursive proof requires retaining those debts or an already-certified terminal law, as well as the interface's exact B+D formula.

## B. Match complete occupation mass to the same output law

Let M(A)>0 on every nonempty actual spectral set be a fixed complete output subprobability, 0<Z=sum_nonempty M(A)<=1. In the graph application M(A) is A008's sum of complete maximal-matching occupation masses at one globally fixed positive feasible edge-weight vector. Define

    Q_occ(empty)=1-v,
    Q_occ(A)=v M(A)/Z, A nonempty.

Then Q_occ is normalized and

    CE(f,Q_occ)=h2(v)+sum_nonempty p_f(A)log2[1/M(A)]+v log2 Z. (13)

Retain the normalizer; it is nonpositive here only because the complete mass has Z<=1. Its induced blocker reference is

    Q_C,occ(empty)=s,
    Q_C,occ(A)=(1-s)M(A)/Z, A nonempty.

Substitution into the general full-output formula (9) gives EXACTLY (13). It follows that

    CE(f,Q_occ)-H(f)=v KL(P_C(.|nonempty)||M/Z).               (14)

The occupation law and the product law now concern the same physical Fourier set, same activation mass and same empty-row refund. Root, label, subset, count and factorial factors remain inside M; none are substituted by a cheaper ideal determinant. B relies on the complete-queue subprobability hypothesis, not on an assumption that the occupation mass is already influence-paid.

For one globally fixed prior theta in (0,1), mix the CONDITIONAL nonempty laws, with the same empty mass:

    Q_mix(empty)=1-v,
    Q_mix(A)=theta Q_occ(A)+(1-theta)Q_prod(A), A nonempty.

Pointwise domination on the nonempty sector proves

    CE(f,Q_mix)<=min(CE(f,Q_occ)+v log2(1/theta),
                    CE(f,Q_prod)+v log2(1/(1-theta))).        (15)

At theta=1/2, the once-paid reference-selection surcharge is v<=I. This is the known fixed-prior mixture principle applied after the output/blocker normalization match; it is not a new general mixture lemma. The joint bound here is CE(f,Q_mix)<=min(CE(f,Q_occ),H(f)+2I)+I. A choice of reference separately for each Fourier set is not authorized by (15).

## C. Exact graph implementation and scope

For each connected labelled graph with a cut vertex x, choose its least cut vertex, let Y be the first component of G-x (ordered by least vertex), and Z the remaining components. Split the graph's independent-set indicator C into h_x(Y)k_x(Z). Both blockers are decreasing in x, so the previous nested interface applies. The reference in A uses exact normalized component spectra, with every terminal entropy retained.

For B use lambda_e=1/Delta, pi_e=1/4, both endpoint orders, D=product_e(1+lambda_e/4)-1. For each inclusion-maximal matching M of G[A], let U be unmatched coordinates and form A008's polynomial

    P_M(z)=product_(u in U)[sum_(v outside A,uv edge)lambda_uv/32
                           +sum_(v matched,uv edge)lambda_uv z_v/8].

Apply J(z^h)=product_(e={v,w} in M) h_v!h_w!/[(c_e+1)^2(c_e+2)], c_e=h_v+h_w. Then M(A)=sum_M D^-1 product_(e in M)(lambda_e/24) J(P_M). This uses corrected actual subset factors, retaining all complete queue costs. Our independent implementation additionally enumerates individual unmatched choices and compares it against polynomial convolution. It verifies all nonempty sets, including zero actual spectrum, before normalizing. The finite tests do not independently reconstruct the original queue's all-dimensional decodability; that premise remains source-bound to A008's reviewed occupation theorem.

## First unsupported line

For arbitrary overlapping blockers/graphs, obtain a globally feasible reference whose retained full occupation expectation and all inherited component reference debts are O(I), uniformly over arbitrary density and adjacent degree scales. (12) closes the exact-component separator conversion excess, and (13)-(15) close the normalization/prior mismatch in the proposed occupation comparison. They do not pay H(f) or the unrestricted occupation expectation. The shortest next action is an overlapping graph component without a one-bit separator, using the same normalized complete occupation law and tracking signed row KL with all actual terminal debts. That addresses the source of non-product congestion instead of extending the already-known separator class.
