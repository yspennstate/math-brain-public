# A cheap parent source can have an exponentially complex physical child

Bits throughout. Full FEI remains OPEN. This is a paid reference-inheritance obstruction, not a high entropy/influence family.

## 1. Actual Boolean family and original owner

For every integer m>=2 let L=2^m, u=L^-2, and take disjoint m-bit blocks x,y and one selector t. Define

    G(x,y)=1-2*1[x=y], H(x,y)=(-1)^(x dot y),
    F(+1,x,y)=G(x,y), F(-1,x,y)=H(x,y).

The bit dot product is over F_2. G has squared Fourier law P_G supported on the diagonal (s,s), s in F_2^m. At the empty atom its probability is p0=(L-2)^2/L^2; every other diagonal atom has probability4u. H is the actual inner-product bent sign, with P_H(s,v)=u on all L^2 DATA atoms. Both branches are nonconstant. Direct Fourier sums give

    I(G)=4m/L, I(H)=m, E(GH)=1/L,
    Inf_t(F)=(1-1/L)/2,
    I(F)=(m+1)/2+(4m-1)/(2L).                          (1)

For E(GH), E H=1/L and the sum of H on x=y is the alternating binomial sum sum_x(-1)^|x|=0. The support formula for G follows by Fourier-transforming the diagonal indicator. No arbitrary real spectral law is substituted for a Boolean function.

Supply the ORIGINAL uniform full reference Q on all 2L^2 parent Fourier atoms. It is ONE product law across t,x,y, with no vacuum correction. Its complete CE is 2m+1. The SAME original owner U=4I(F), with old unrelated booking b=1/8, has exact reserve

    U-b-CE(P_F,Q)=7/8+(8m-2)/L >7/8.                 (2)

Thus neither an initial entropy conjecture nor a fresh child source grant is hidden in this family.

## 2. True physical inheritance of BOTH children

Query the actual selector t. Let q=(P_G+P_H)/2 be the true erased DATA marginal. The merged reference is uniform u. The ACTUAL Boolean pair kernel has branch probabilities

    K_G(S)=P_G(S)/(P_G(S)+u), K_H(S)=u/(P_G(S)+u).

The denominator is everywhere positive because P_H=u. There are no ghost-completion choices at this query. Write

    A=(L-2)^2/((L-2)^2+1), D=A+4(L-1)/5,
    r_G=D/L^2, r_H=1-r_G.                             (3)

These are reference branch masses, not physical reaches, which remain1/2. Both r values are strictly positive. The inherited G reference is

    Q_G(empty)=A/D,
    Q_G(s,s)=4/(5D) for s!=empty,
    Q_G(s,v)=0 for s!=v.                              (4)

The inherited H reference is the normalized law

    Q_H(S)=u/[r_H*(1+P_G(S)/u)].                       (5)

It covers H on every DATA atom, including all off-diagonal positions. Retaining this full sibling and its true normalizer is essential. Averaging child bill with reference probabilities r_G,r_H instead of physical probabilities1/2 would be wrong.

## 3. Exponential rank growth is unavoidable in the claimed representation

View a DATA law as an L-by-L matrix across the ORIGINAL x/y split. Each product law nu(x)mu(y) has real matrix rank at most1. A signed vacuum correction c delta_(empty,empty) has rank at most1. In (4) every diagonal entry is positive. Remove the empty row and column: the remaining (L-1)-by-(L-1) diagonal minor is invertible.

Therefore ANY representation

    Q_G=sum_(r=1)^R w_r nu_r(x) mu_r(y)+c delta_empty

requires R>=L-1=2^m-1. This remains true even allowing arbitrary REAL signed component weights, not merely A028's w_r>=0. A single uniform product root has become exponentially many required product components after ONE physical query. This does NOT refute A028's tensor-Boolean theorem: F here is not asserted to factor across the original t,x,y blocks, and the local-kernel cancellation in A028 section2 is exactly what is absent. Merging all DATA coordinates into one giant block evades the rank statement only by changing the representation interface.

The bound is attained: use the L-1 nonempty diagonal point products with weights4/(5D) and the single vacuum slot A/D. Thus the minimum R is EXACTLY2^m-1. It is also a lower bound for mixtures of coordinatewise products, since those are a subclass of products across the x/y split.

Every finite strictly positive cardinality tilt multiplies matrix entries by a positive row factor times a positive column factor. Matching the vacuum can then change only its empty entry. If the inherited nonempty profile remains positive, the same (L-1)-minor remains invertible. Repeated finite moment/vacuum calibrations therefore do not repair this component-count growth. Extreme support conditioning and arbitrary new nonempty profiles are excluded from this corollary.

## 4. The bad physical child is still paid by the original account

For m>=2, A>=4/5 and D>=4L/5. Consequently every atom of Q_G is at most5/(4L), so

    CE(P_G,Q_G)>=m-log2(5/4)>m-1/2,
    CE(P_G,Q_G)/I(G)>(L/4)*(1-1/(2m)).                (6)

The strict bound uses (5/4)^2<2. Thus no uniform inherited-child CE/I bound follows from this rate4 parent source. This is a reference deficit, not an FEI deficit: H(G)/I(G) stays bounded.

Let E be the true pair-kernel KL contraction, O=D((1/2,1/2)||(r_G,r_H)), and DeltaH=H(F)-[H(G)+H(H)]/2. Chain rule gives EXACTLY

    CE(P_F,Q)=DeltaH+E+O
                       +[CE(P_G,Q_G)+CE(P_H,Q_H)]/2.   (7)

All three query charges are retained; E,O>=0. This is a FULL true-kernel transaction identity, unlike an endpoint-only row-reset formula. Define the actual signed reference deficits d_G=CE(P_G,Q_G)-4I(G), d_H=CE(P_H,Q_H)-4I(H), and let d_F=CE(P_F,Q)-4I(F). Then

    d_F=(d_G+d_H)/2+DeltaH+E+O-4 Inf_t(F).             (8)

The root reserve in (2) and (7) pay BOTH complete terminals and the query bill at the SAME original4I after old1/8. If d_G>0, its real sibling and query influence capacity compensate it according to (8); d_G is not clipped, and no new4I(G) grant is issued. Descendant expansions REPLACE these inherited bills and release actual KL; they cannot add the old child slack again. This family exhibits the assignment's difficult child without making any unsupported claim that a child bound is hereditary.

The difficult child is actual, not hypothetical: for every m>=5, 4I(G)=16m/L<=m/2, so d_G>m/2-1/2>0. Its sibling has CE(P_H,Q_H)<2m+1 and hence d_H<1-2m<0. To see the CE bound, direct substitution in (5) gives CE_H=2m+log2(r_H)+L^-2[log2(1+(L-2)^2)+(L-1)log2(5)]. The last bracket/L^2 is less than (2m+3L)/L^2<=4/L<=1, using2m<=L for m>=2. The negative log2(r_H) only improves this bound. BOTH signs are retained in (8).

## 5. Projection avoids the collapse, but conversion back is not free

If one had prescribed spectral-projection inheritance, both children would instead receive the uniform product law u. It has positive mass at every off-diagonal DATA atom. Since (4) is zero there,

    D(Uniform(DATA)||Q_G)=infinity.                    (9)

This is the FORWARD conversion fee of the projected target relative to the inherited true-kernel source. Replacing true-kernel inheritance by projection may be a valid ORIGINAL design, as A012 proves, but it cannot be inserted as a finite-fee repair after this child has already inherited Q_G. Conversely D(P_G||Q_G) is finite. The support direction in (9) must not be reversed. A hypothetical arbitrary signed CE-difference reset is a different transaction convention and is not covered by the forward-fee assertion.

There is also an exact SAME-owner limit if projection is selected at the original query. Its full transaction bill is CE(root)+JS(P_G,P_H), by A012's query identity, not merely CE(root). Let B be the fair child label and classify B as G on the diagonal and H off the diagonal. Its error probability is1/(2L). The error bit and B are in bijection conditional on the observed atom, so H(B|S)<=h2(1/(2L))<(m+3)/(2L), using -ln(1-p)<=p/(1-p) and ln2>1/2. Hence

    JS>1-(m+3)/(2L),
    [projection bill + old1/8]-4I(F)
         >1/8-(17m-1)/(2L)>0 for EVERY m>=10.           (10)

The last sign follows from2^10>68*10-4 and induction. At m10 the excess is rigorously >87/2048. Thus original true-kernel inheritance is paid but exponentially complex, while one-product projection inheritance violates THIS SAME rate4 account with its retained old debit. Without that old1/8 commitment, projection is paid: its JS<=1 and the original margin before the booking is1+(8m-2)/L>1. The obstruction must not be generalized to the zero-old-debit case or to every possible reference/interface policy.

## 6. A structured repair that retains the SAME original payment

The rank obstruction concerns product mixtures, not all compact descriptions. Formula (4) has the exact TWO-term structured description

    Q_G=[4L/(5D)] Uniform(V)+[(A-4/5)/D] delta_empty,
    V={(s,s):s in F_2^m}.                              (11)

Both initial coefficients are nonnegative. V is described by a binary linear system, rather than enumerating L product atoms. More generally let g=1-2*1[E] for a nonempty affine event E on the remaining physical cube, with its orthogonal frequency subspace V, and supply a covering nonnegative complete reference lambda Uniform(V)+c delta_empty. The coefficient c may be signed, but the WHOLE reference is a probability law. This class is closed under every physical coordinate query using the actual pair kernel with fair zero-pair completion, and under any subsequent vacuum calibration.

Proof of physical closure: the nonempty Fourier coefficients of g on V have one absolute value and a character phase determined by the affine event. If e_i is not in V, deleting coordinate i is injective on V. Every occupied pair has at most one true atom, so each branch kernel is1/2. The reference is pushed to lambda Uniform(pi_i V)+c delta_empty. If e_i is in V, deletion has two-to-one fibers. On every NONEMPTY projected fiber the two true coefficients have the same fixed relative phase, so one branch has kernel1 and the other0. Only the empty projected fiber is exceptional; its normalization and kernel are retained explicitly. The active branch therefore has constant reference mass on the nonempty part of pi_i V plus a possibly different vacuum mass, while the inactive branch is constant with reference delta_empty. If pi_i V={empty}, both laws are constants and are treated directly. Reference branch masses are positive by coverage. An impossible restricted event is also a constant case. On a zero-true vacuum fiber the fair completion preserves the asserted shape; there is no reference support outside V.

Vacuum calibration preserves the uniform nonempty profile. For this affine-event class the TRUE nonempty profile is also uniform, so matching vacuum mass sets the FULL reference to P_g. Its fee D(P_g||Q_g) equals exactly the released CE(P_g,Q_g)-H(g), and remains charged. Later true-kernel inheritance from the exact law is exact again; no new original source is issued. Equivalently arbitrary interleavings before calibration stay in the two-term class, with every signed c and full branch normalizer retained. Influence-moment tilts are NOT claimed to preserve uniformity on V, and arbitrary core phases are NOT included.

Thus (11) gives a compact selected-child repair through ALL finite DATA-query/vacuum-calibration histories while the entire H sibling is retained as a full terminal. Equation (7) extended by the actual query and calibration identities pays that whole root tree at original4I, old1/8 and the SAME reserve>7/8. This is an explicit structured-residual inheritance result beyond the product-mixture interface. It does not grant a useful arbitrary-core initial source, nor certify arbitrary terminals merely from a representation.

## 7. Reviews, precise open line, next action

A028 section1-4 compact local-tensor inheritance and full true-kernel transaction ledger are independently reconstructed at their STATED hypotheses. The rank witness blocks an arbitrary-core extension, not that theorem. A012 sections1-4 projection ledger is also reconstructed: its additive2/ln2 term pays actual JS and query contraction for that DIFFERENT inheritance convention. Neither source supplies an original O(I) reference for all Boolean cores.

The new obstruction is product-component closure under true physical inheritance beyond tensor factors, with actual original rate4 and both children already paid; section6 supplies its concrete affine-residual repair on the selected branch. The first unsupported universal line remains a noncircular original arbitrary-core source plus a useful stopping/interface rule. NEXT should test the first NECESSARY non-affine residual or physical branch outside the uniform-affine reference carrier while retaining (7), and determine whether its ORIGINAL source admits a structured description without an infinite forward handoff fee. Another finite calibration inside the now closed affine-event branch cannot address that line.
