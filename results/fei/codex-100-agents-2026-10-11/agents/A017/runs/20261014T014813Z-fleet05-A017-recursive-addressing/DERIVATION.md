# Two coherent point edits: a terminal-inclusive stopping proof

All entropies are in bits. Controls are x in F_2^n and distinct data coordinates y_z are independent uniform signs. Let q be any degree-at-most-two polynomial, with linear part ell and alternating polar matrix Q, let M be any binary matrix, and let E={u,v}, u!=v, with Mu=Mv. Put b(x)=(-1)^q(x) and F(x,y)=b(x)(1-2*1_E(x))y_(Mx). Constants in q have no effect on the ledgers. The result also holds for zero or one edited point and, by the same proof, for two points in different fibers; the packet claim keeps the shared-fiber hypothesis.

## 1. Exact coherent entropy and influence ledgers

Writing delta=2^-n, z0=Mu=Mv, and a_z(S)=2^-n sum_(Mx=z) b(x)chi_S(x), the only changed coefficients are

    a'_z(S)=a_z(S)-2 delta 1_(z=z0)[b(u)chi_S(u)+b(v)chi_S(v)].

No probabilistic mixing replaces this signed amplitude sum. The exact spectrum is p_(S,z)=a'_z(S)^2, and H=-sum p log2 p. Let r=rank M, K=ker M and k=rank(Q|K). Every fiber has mass 2^-r and its control Fourier distribution consists of 2^r identical copies of its kernel-coordinate Fourier distribution. Thus

    H(F)=2r+k+2^-r[H(b(1-2*1_E)|_(z0+K))-k].

The restricted quadratic on every unedited fiber has a flat spectrum of size 2^k. Indeed its autocorrelation at h vanishes unless h is in the radical of its polar form; on that radical it is a character. Fourier transformation of this autocorrelation makes the squared spectrum uniform on the corresponding affine coset of the annihilator, of cardinality 2^k. The 2r term counts the data label and the repeated control coefficients once each. A linear choice of coordinates on K is valid for entropy; it is not used to change physical influence.

For h=u+v, controls with Me_i!=0 have influence 1/2, including after editing, because the two endpoints use independent named data bits. For Me_i=0, write d_i(w)=ell_i+(Qw)_i. The exact change from the unedited function is

    Inf_i(F)-Inf_i(by_Mx) = 0                         if h=e_i,
                            2delta[(-1)^d_i(u)+(-1)^d_i(v)] otherwise.

The first case flips both endpoints of the same edge. In the second case the two changed undirected edges are distinct. An unedited inactive control has influence 1/2 if Qe_i!=0, otherwise ell_i. The total data influence is exactly 1. Therefore I(F)=1+sum_i Inf_i(F), even when many address labels are shared across levels. Conditional ledgers have the same form with their actual restricted phase, edited points and physical dimension.

For an arbitrary current node with amplitudes a'_z(S), the physical derivative boundary reserve is exactly

    C_i=2I(D_i)=2 sum_(z,S contains i) |S| a'_z(S)^2.

The |S| includes the extra data-coordinate contribution to |S union {y_z}|-1. Equivalently C_i=2[Inf_i+sum_(j!=i) sum_(z,S contains i,j) p_(S,z)]. This is a local reserve, not an asserted global payment.

## 2. A hereditary K=4 good-pivot rule

Query every physical control with a nonzero column of M first, in any fixed order. Each has conditional influence 1/2. Once all are fixed, there is exactly one remaining named data sign. On a branch with no edited point, stop at its quadratic phase. On an edited branch, query any remaining coordinate whose row in the restricted polar matrix is nonzero. Stop when this matrix is zero. Actual irrelevant pivots are allowed; both children are then the same actual function and the entropy decrement and influence are zero. The algorithm terminates because each query removes a physical coordinate; its quadratic representation remains degree two and at most two edited points remain on every branch.

At a phase pivot with D remaining controls, the unedited quadratic influence is 1/2. Each edited point changes its influence by at most 2^(1-D), so

    Inf_i >= 1/2-2^(2-D).

For D>=4 this is at least 1/4. For D<=3 a nonzero influence of any Boolean phase is an integer multiple of 2^(1-D), hence at least 1/4. This is a statement about the actual pivot, including cancellations. For B_i=H(1_(i in spectral set) | spectral set minus i), B_i<=1 always; if Inf_i=0 then B_i=0. Thus B_i<=4 Inf_i at EVERY queried node. The exact localized bad-node bill sum_(B_i>4Inf_i) w_i C_i is zero. Neither a summed root second moment nor the terminal data bit is spent as a boundary reserve.

## 3. Terminal payment, including characters and both edits

A cleaned leaf is quadratic times its data sign. If its polar rank is k, its entropy is k and its phase influence is at least k/2: the number of nonzero polar rows is at least k and each contributes 1/2.

An edited leaf has a linear phase, so its phase is a character times phi=1-2*1_E, with |E|<=2. If E is one point, phi has the spectrum of a point defect in D dimensions. If E is two points, E is an affine line and phi has the spectrum of a point defect in d=D-1 dimensions under a linear quotient. Let rho=2^-d, t=1-(1-2rho)^2=4rho(1-rho). For d>=2,

    H(phi)=h2(t)+t log2(2^d-1) <= 8d rho.

Here is an elementary proof of the bound rather than a reliance on a plotted ratio. The d=2 spectrum is uniform on four atoms, giving H=2<=8d rho=4. For d>=3, write the entropy exactly as

    H=-(1-2rho)^2 log2((1-2rho)^2)
       +(2^d-1)4rho^2(2d-2).

Using -s ln s <=1-s, the first term is <=4rho/ln2. The second is <=8rho(d-1). Since ln2>=1/2, their sum is <=8d rho. For d=0,1 the sign is a character or constant and entropy is zero.

Every physical direction crossing the affine edit cell has influence 2rho; the number c of such directions is at least its quotient dimension d. Consequently H(phi)<=4 I(phi). For a one-point edit with D>=2, or a two-point edit with D>=3, every physical influence of phi is <=1/2. Multiplication by a character changes each chosen influence a to 1-a, so cannot decrease total influence. In the remaining small dimensions phi itself is a character, making entropy zero after character multiplication. Hence every edited terminal satisfies H<=4 I_phase. This includes dummy directions made relevant by editing and every conditional linear term.

## 4. Entropy decrement and one conserved influence budget

For any Boolean node and control i, H_parent-average H_children=B_i+JS, by erasing i from the squared spectrum and comparing the mixture of the child spectra. For nonnegative p,q,

    [p ln(2p/(p+q))+q ln(2q/(p+q))]/2
       <= (sqrt(p)-sqrt(q))^2/2.

To check this inequality, set x=(p-q)/(p+q). It is equivalent to (1+x)ln(1+x)+(1-x)ln(1-x)<=2(1-sqrt(1-x^2)); both sides vanish at zero, and derivative domination follows from atanh(x)<=x/sqrt(1-x^2), whose derivative difference is nonnegative. Endpoints follow by continuity. Applying this atomwise to the child spectral amplitudes gives JS<=2 Inf_i/ln2 (signed amplitudes only increase the squared difference). Thus every queried node has

    Delta_i H <= (4+2/ln2) Inf_i.

For a full stopping tree, exact influence telescoping is

    I(F)=sum_internal w_i Inf_i + sum_leaves w_leaf I(F_leaf).

There is exactly one data-coordinate influence at each leaf; its total weighted cost is 1. Entropy telescoping, the node inequality and the terminal bound therefore yield

    H(F) <= (4+2/ln2) [I(F)-1] < 7[I(F)-1].

No independence of child phases or edit spectra was assumed. All constants are dimension-independent. This proof is author-complete, pending A091/A090 independent reconstruction; it does not prove universal FEI. For an iterated address update M_t=A_t M_(t-1)+B_t and a quadratic phase update q_t=q_(t-1)+p_t on the same physical controls, reuse is allowed at every level. The exact stage entropy and influence are the displayed root ledgers evaluated at (M_t,q_t,E); increments are their differences, including rank and signed-amplitude cancellations. The shared-fiber condition is M_t(u+v)=0 at each claimed stage. A repeated address value uses the SAME y_z coordinate, while different address values must use independent data signs. This rule counts the terminal label once, irrespective of the number of addressing levels.

## 5. K=2 is not stable under a shared separator

Take four controls, q=x0x1+x0x2+x1x2, M=0, and edits {0,e0}. Query x0. Its influence is 1/2. In the child x0=1, there are D=3 controls and the phase is (-1)^(x1x2+x1+x2) with its origin flipped, with x3 a dummy of the original quadratic. For the next polar pivot x1,

    Inf=1/4, B=1+(5/8)log2(5)-(9/8)log2(3), C=1.

B>2 Inf is exactly the integer inequality 16*5^5>3^9 (50000>19683). This queried node has global weight 1/2, so the displayed tree's K=2 bad-boundary bill is 1/2. This refutes only the hereditary K=2 rule for this specified quadratic-representation pivot tree. It does not rule out a different stopping rule: this particular child can also be recognized as a signed point defect and stopped immediately. A six-control rank-four descendant, saved separately, shows the same gradient problem beyond that low-rank simplification. There q=x0(x1+x2+x3+x4)+x1x2+x3x4 and E={0,e0}; after x0=1 all four polar controls have influence 7/16, erasure entropy 1-(9/32)log2(3)-(25/32)log2(5)+(17/32)log2(17)>7/8, and boundary charge 2. Its remaining quadratic dummy has influence 1/16 and erasure entropy exceeding 1/4, so it is even K=4-bad. The rule queries the polar controls and stops with that dummy paid in the terminal; it never queries this dummy. CERTIFICATE_AUDIT.json checks all these signs from the saved rational intervals. Thus zero queried bad-node bill is an adaptive stopping statement, not an assertion that every coordinate is good.

## 6. Independent source-bound review: A069 S1-S5 only

A069's subcube edit has delta=-2*1_(z=z*)h(y), hence deltahat(U,V)=-2rho chi_U(z*) hhat(V). Its normalized difference spectrum factors into uniform U and the FULL spectrum of h. The empty-atom probability is rho*(E h)^2. Summing the root occupancy and each fixed subtree occupancy separately reproduces S1 exactly. Averaging the physical restrictions gives S2 by Parseval in the Z coordinates; nonnegativity gives the single-core bound S3. The pointwise squared inequality (a+b)^2<=2a^2+2b^2 proves S4 with its coherent cross term bounded, not discarded. On a Y-edge both endpoints flip together, so influence is unchanged; on each Z-edge crossing the edited cell, exactly one of f,g is pivotal. The directed crossing probability is 2rho, proving S5. This is an independent reconstruction of this interface only, not acceptance of A069's complete hierarchy/addressing claim or its earlier prefix-code dependencies.

## 7. Exact first unsupported universal line

To apply this stopping rule to arbitrary Boolean functions, one would need a representation and refinement preserving a bounded number of coherent edits at every node, or a conserved boundary reserve paying nodes whose positive influence is below 1/4. Neither is supplied. With three edits, the simple lower bound becomes 1/2-6*2^-D; D=4 allows a positive influence 1/8, so B<=1 no longer proves the K=4 good-node condition. This is the shortest next ownership test, not an assertion that a three-edit counterexample exists.
