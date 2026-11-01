# Balanced-core admission beyond the marginal threshold two

All entropies and KL divergences are in bits. This refines the sufficient admission criterion in A050-NONPOINT-CANONICAL-GAP-REPAIR@1. It does not assert a universal FEI bound or an unconditional certificate for arbitrary cores.

Let h be a balanced uniform Boolean core, with an actual supplied certificate H(h)<=4I(h). Put F_h=(-1)^a on x=0, h on x=b=1, and +1 otherwise, with fresh independent controls x,a,b. Let M be the original completed canonical occupancy reference: M(empty)=P(empty), and its nonempty law is the matched-marginal maximum-entropy law Q_r. The actual root spectral law P and M have the same empty mass and all inclusion marginals. Since log M on nonempty atoms is affine in membership, A=D(P||M)=H(M)-H(P)=v K_occ, with v=15/16. No ordinary full-product reference is substituted for M.

Query b first, then any finite adaptive fresh data-only stopping continuation in b=1, retaining the b=0 branch and keeping x,a unqueried. Suppose each terminal core g has a supplied certificate H(g)<=4I(g). All reference-only rows use the fair zero-source extension of the actual coherent physical kernel. The same original M is transported throughout; descendants are never freshly projected.

Write H0=H(F_h), I0=I(F_h), Hf=E H(leaf), If=E I(leaf), R=I0-If, D=H0-Hf. Define the one whole source liability and the actual final owner by

    L = A + [D-4R]_+,       S = 4If-Hf.

This charges the entire original source KL, including all erasure, outcome, conditional and terminal reference KL, once. Prior genuinely booked conservative overpayment omega must be added as L+omega; none is silently discarded or funded by a renewed bank.

For completeness, the one-node source account follows directly by two finite KL chain rules. If p,q are the incoming source/reference and bar p,bar q their frequency-erased laws, set E=sum_T bar p(T) D(p(bit|T)||q(bit|T))>=0. Then D(p||q)=E+D(bar p||bar q). Apply the SAME stochastic actual channel k(s|T) to both erased laws; the joint output KL is D(bar p||bar q), because the conditional channel cancels in the likelihood ratio. Its outcome/conditional decomposition is O+sum_s p(s)D(p_s||q_s). The physical source outcomes have probability1/2 and p_s is exactly the squared spectrum of the physical child. Thus incoming KL equals E+O+mean child KL. Source-zero rows contribute zero source expectation but retain their reference mass in bar q, outcome normalization and all descendant references. Iterating over the actual finite history probabilities gives A=sum_reached weighted(E+O)+mean terminal KL. This uses a derived common-channel structure, not an independence assumption.

The canonical reference exists without an extra square-sum condition. Here all r_i lie in (0,1), and sum r_i>1 because the xa coefficient contributes positive mass at degree2. For c>0 the equation phi(c)=[1-product_i(1-cr_i)]/c=sum_i r_i product_{j<i}(1-cr_j)=1 has exactly one root in (0,1): phi is strictly decreasing, phi(0)=sum r_i>1, and phi(1)<1. Set M(nonempty)=(v/c)product_i(cr_i)^{s_i}(1-cr_i)^{1-s_i}. Its normalization and marginals follow from the root equation; all source atoms are dominated. On nonempty atoms log M is affine in membership, while the empty atom has its separately matched mass. Matching these expectations proves CE(P,M)=H(M) and hence A=H(M)-H(P).

## 1. The stronger eligibility criterion

For every balanced h, exact disjoint Fourier sectors give

    H0 = 3 + H(h)/4,       I0 = (5+I(h))/4.

Indeed a and xa each have mass1/4; the four constant-control atoms each have mass1/16; the remaining atoms are four disjoint copies of the nonempty h-spectrum, each with mass hhat(S)^2/16. Balance excludes overlap with the constant-control atoms. These masses give the displayed entropy, while the root marginals are 1/2,1/2,1/4 and Inf_j(h)/4.

Hence the ACTUAL supplied root certificate implies

    Sroot=4I0-H0=2+I(h)-H(h)/4 >= 2.

At each terminal in b=1 the remaining function selects the independent character (-1)^a and g by x. Its exact entropy and influence are 2+H(g)/2 and 1+I(g)/2. Thus its actual price-four surplus is 2+2I(g)-H(g)/2>=2. The retained b=0 terminal has H=2,I=1 and surplus2. Consequently S>=2. No arbitrary-core FEI statement supplies either certificate.

Define

    G(h)=h2(1/4)+sum_j h2(Inf_j(h)/4).

Entropy subadditivity for M, whose marginals match the root, gives

    H(M)<=2+G(h),
    A<=G(h)-1-H(h)/4.                         (1)

The key payment identity is purely algebraic:

    S-L = min(S-A, Sroot-A).                  (2)

To verify it, expand L=max(A,A+D-4R) and note S-D+4R=4I0-H0=Sroot. Thus the SAME final owner S pays the complete L whenever A<2, with margin at least2-A. Sroot is a side condition on eligibility, not a second spendable bank.

Combining (1)-(2), the improved sufficient condition is

    G(h)<3+H(h)/4,

and the retained margin is at least

    3+H(h)/4-G(h)>0.                          (3)

In particular G(h)<3 suffices under the stated root and terminal certificates. This improves the old G<2 sufficient test at BALANCED cores with the extra explicit root certificate. It does not compare the two criteria after deleting hypotheses. Previously booked omega smaller than the margin in (3) is paid from this same owner. There is no claim about unpaid earlier ancestor work or fresh-reference resets.

## 2. A genuinely non-flat all-width instantiation

For every integer m>=3, let

    h_m(z,y)=(-1)^z [1-2*1(y_1=...=y_m=0)].

The core is balanced. Its positive squared Fourier masses are (1-2^(1-m))^2 and 2^(2-2m), which differ for m>=3, so it is genuinely non-flat. The z influence is1 and each y influence is2^(1-m). Therefore

    G(h_m)=2h2(1/4)+m h2(2^(-m-1)).           (4)

Every restriction of h_m is, up to sign, a character times a point defect, a point defect, a character or a constant, on disjoint surviving coordinates. Fourier entropy and influence tensor-add. For a k-bit point defect, put epsilon=2^-k. Its nonempty entropy is8(k-1)epsilon(1-epsilon); its empty contribution is at most4epsilon(1-epsilon)/ln2. Since ln2>1/2, H<=8k epsilon=4I for k>=2. k=0,1 are constant or character and have zero entropy. This supplies all actual root and terminal certificates, including adaptive histories that query z.

For u in (0,1), h2(u)<=u log2(e/u), and log2(e)<3/2 because ln2>2/3. The latter lower bound follows directly from ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3. Thus

    m h2(2^(-m-1)) < m(m+5/2)/2^(m+1).

For m>=3 the right side decreases: the denominator minus numerator in its successive-ratio comparison is m^2+m/2-7/2>0. Its m=3 value is33/32. Also h2(1/4)<13/16 because3^12>2^19. Hence, for ALL m>=3,

    G(h_m)<13/8+33/32=85/32<3,
    A<53/32-H(h_m)/4,
    S-L>11/32+H(h_m)/4 >=11/32.              (5)

Every finite adaptive data-only continuation after b is therefore paid from the same original final owner, keeping all terminal entropy and all inherited reference bills. An old conservative booking0<=omega<=11/32 remains paid with strictly positive residual margin; it is added once as L+omega.

The first point-coordinate exposure has two nonconstant core children: one retains the character z and the other retains that character times an (m-1)-bit point defect. This does not use an immediate constant collapse. At m=3, (4) is strictly greater than2 by the exact logarithm certificate, so this family actually crosses the retired sufficient threshold rather than merely re-proving its old admitted region.

## 3. Validation and precise open frontier

The all-m bound and all-finite-tree quantifiers follow from the displayed proof and source-compatible finite KL chain rule, not from extrapolation. code/balanced_check.py checks the constants, the decreasing rational envelope and finite boundary laws independently. code/check.py --nonflat4 checks the m=3 actual seven-bit root, positive inherited reference mass on source-zero rows, coherent next-query rows, actual non-flat core masses, full terminal H/I and exact canonical whole liability at the alternative a-then-y0 policy. That separate fixed a-first certificate is not used to assert arbitrary a-first histories.

The first unsupported universal line remains supplying actual root/terminal entropy-influence certificates for arbitrary cores and maintaining eligibility through mixed control queries or fresh reference resets with earlier spent accounts. The supplied certificates here are proved only for the stated character/point-defect restriction family. This does not solve full FEI.
