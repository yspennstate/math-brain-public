# Shared-phase countersearch: selection and the physical credit are essential

All inputs below are uniform independent binary coordinates. Outputs are signs. Entropy uses log2; I is total physical influence. For a split, d=Pr[g!=h], W=I(gh)/2, B is true Fourier coordinate erasure, M=h2(d)-B, R=W-d log2(1/d), and sigma=log2(e)d-(1-d)log2(1/(1-d)). The A031 identity is B=W+log2(e)d-R-M-sigma. Every sum below retains physical weights; W is already a signed convolution square, not a triangle-inequality replacement.

**Prior obstruction credited:** A021 stage 2 REPORT.md sections 4-6 already proves failure of EVERY-tree raw localized odd-face payment at every fixed threshold, using tensor activations and unrevealed point controls. We do not claim that broad conclusion as new. The delta here is a distinct non-rare shared-parity family with exact retained-M/retained-sigma versus missing-R separation, an explicit constant-bill complete good order, and the unchanged true joint-credit prefix. It tests A031's new full-credit currency on shared phase reuse rather than reopening A021's quantifier result.

## 1. The Boolean family

For even t, put b_t(v)=(-1)^(v1*v2+...+v_(t-1)*v_t). Let r>=4 be even, let m>=2 be even, and let L>=1. On fresh r-bit blocks x_j and fresh selector bits z_j, define

    q=2^-r, A_j=1_{x_j=0}, p(y)=(1-chi_[m](y))/2,
    h_j(x_j,z_j)=b_r(x_j)(-1)^(A_j z_j),
    B0(x)=product_j b_r(x_j), T(x,z)=product_j h_j(x_j,z_j),
    f(y,x,z)=b_m(y) B0(x) (-1)^[p(y) sum_j A_j z_j].             (1)

Thus f=b_m B0 when p=0, and f=b_m T when p=1. It is manifestly Boolean in dimension m+L(r+1). We use L=m for the unbounded order obstruction. No physical variable is duplicated: only the parity p is explicitly shared by the modules.

## 2. Two disjoint Fourier rows, derived before taking squares

The quadratic bent Fourier amplitudes are b_mhat(U)=2^-m/2 (-1)^(Q(U)). Translation by the all-coordinate character changes their sign by (-1)^(|U|+m/2). Hence c_+=b_m(1+chi_[m])/2 and c_-=b_m(1-chi_[m])/2 have disjoint Fourier supports, each of size 2^(m-1), and each occupied amplitude has magnitude 2^-m/2. In

    f=c_+ B0+c_- T,

the cross terms vanish exactly because no Fourier address U occurs in both rows. This is a Boolean phase cancellation, not a generic incoherent-mixture assumption. The core marginal is uniform on all 2^m U, and the conditional laws are the squared spectra of B0 or T. Therefore

    H(f)=m+L[r+H(h_1)]/2.                                     (2)

At an x_j coordinate, conditional on physical p, the boundary is that of b_r or h_j. Since the bent origin has zero boundary degree, flipping it changes each influence from 1/2 to 1/2+2q. Thus each x coordinate has influence 1/2+q/2. Each z_j has influence q/2. At y_i, reversing the bit reverses parity p and multiplies b_m by the partner coordinate character. That partner is fair and independent of the module variables, so each y_i has influence 1/2. In total

    I(f)=m/2+L[r/2+(r+1)q/2].                                 (3)

The support bound H(h_1)<=r+1 gives H(f)/I(f)<=2+1/r<=9/4, uniformly in m,L. For r=4 the sharper exact module entropy below gives H(f)<=2 I(f). The countersearch family is therefore not a candidate FEI disproof.

## 3. A genuinely bad selector at every prefix history

Let beta_r=B_z(h_1). In the module, u_S=epsilon_S sqrt(q)-q and v_S=q, with epsilon=+1 on (2^r+2^(r/2))/2 addresses and -1 on the rest. Consequently

    beta_r=sum_S phi((epsilon_S sqrt(q)-q)^2,q^2),
    phi(a,b)=a log2((a+b)/a)+b log2((a+b)/b).                   (4)

Disjoint Fourier rows in (2) show that a z_j split at the root has

    d=q/2, B=beta_r/2.                                        (5)

The same formulas hold after ANY previously queried z coordinates, with ANY outcomes: the positive row has no remaining selector dependence, the negative row factors over the remaining modules, and the other (already fixed) factors have normalized Boolean spectra. Tensor factors cannot change the selected module's erasure. This proves invariance over every prefix history, rather than replacing differently signed contexts by a histogram without justification.

The physical child product is (-1)^(A_j p). Its disagreement set is D={x_j=0, chi_[m](y)=-1}, with density q/2. Every one of the r constrained x coordinates and m parity coordinates cuts D with probability q. All other directions cut no edge. Thus

    W=q(r+m)/2, R=q(m-1)/2, M=h2(q/2)-beta_r/2.                (6)

The W formula preserves the full signed convolution through the exactly Boolean child product. No sign or triangle inequality is lost in (6).

For r=4, direct exact pairing gives

    beta=1+(39/64)log2 13-(45/64)log2 3-(25/32)log2 5,
    H(h_1)=8-(45/64)log2 3-(75/64)log2 5.                     (7)

The signs beta>1/4 and H(h_1)<37/8 are exactly certified, respectively, by

    2^48*13^39 > 3^45*5^50,
    3^45*5^75 > 2^216.

The rational log enclosures give 0.326522370791<beta<0.326522370792, hence B/d=16 beta>5.224357932670. Every selector-first prefix node is strictly bad at threshold K=4.

## 4. Refutation of order-independent localized payments

Take r=4 and L=m even. Equation (3) gives I(f)=85m/32. Query all L selectors before any core or x coordinate. Since each depth has total reach weight one and the same selector quantities, the prefix raw bad-node odd-face bill is

    P_raw=sum_prefix w W=m(m+4)/32,
    P_raw/I=(m+4)/85 -> infinity.                             (8)

Every node in (8) is genuinely bad (B>4d). Completing the tree by any further queries can only increase the nonnegative bill. Therefore no constant C bounds the K=4 raw localized bill by C I(f) for EVERY complete restriction tree, even on this explicit bounded-H/I Boolean family. The B05 bridge quantifies SOME tree, so it is not refuted.

Removing R but keeping the other credits also fails:

    P_noR=sum_prefix w [W-M-sigma-(4-log2(e))d]_+
         =m[(beta-1/4)/2+(m-1)/32].                          (9)

The equality follows because the bracket is B-4d+R and B-4d>0. Thus P_noR/I also diverges, although spectral KL credit and scalar slack were both retained. Localizing to actually bad splits cannot replace the physical isoperimetric credit.

With ALL credits retained, the true positive-excess prefix is instead

    P_joint=sum_prefix w [B-4d]_+=m(beta-1/4)/2,
    P_joint/I=(16/85)(beta-1/4)<0.014404210973.                (10)

It is bounded and independent of m. The exact retained physical credit is m(m-1)/32. This separates an actual obstruction to (8)/(9) from a failed upper-bound proof or an obstruction to the true joint-credit target.

There is also an all-threshold extension of the negative statement. For the general r module, the sector/reference chi-square divergence is 4q^2/(1+4q^2): indeed the imaginary conditional law is uniform, the signed bent counts give sum_S q^2/[u_S^2+v_S^2]=(1+4q)/(1+4q^2), and multiplying its excess over one by q/(1-q) gives the stated divergence. Jensen on the likelihood ratio yields M_z<=4q^2 log2(e). Consequently beta_r/q>=r-4q log2(e)>r-1 for r>=4 (log2(e)<2). Given ANY fixed finite K>=0, choose even r>=4 with r>K+1. Every selector prefix is then bad at threshold K. At L=m,

    P_raw/I=q(r+m)/[(r+1)(1+q)] -> infinity.                 (11)

Since P_noR=P_joint+L q(m-1)/2 on the bad prefix, retaining only M and sigma likewise cannot yield an EVERY-tree universal bound for ANY fixed threshold. The family retains the bound H/I<=9/4 from (2)-(3). No universal existential-selection failure follows from (11).

## 5. A complete good order, with terminal accounting

For r=4, L=m>=8, query all m shared core bits first. Put mu_L=[1-(15/16)^L]/2. At any such node, the queried bit's partner is either still free, giving d=1/2, or already fixed, giving d=mu_L or 1-mu_L. This follows directly by averaging C=product_j(-1)^(A_j z_j), whose mean is (1-q)^L. It is unaffected by how the other core bits have been fixed.

The integer inequality 3*16^8>5*15^8 proves mu_L>1/5 for all L>=8. The ratio h2(d)/d is decreasing, and 5^5<2^12 proves h2(1/5)<4/5. Thus every core query obeys B<=h2(d)<4d and incurs no bad-node bill.

After the core is fixed, p=0 or p=1 each with total reach probability 1/2. In the p=0 branches all selectors are irrelevant. In p=1 branches the function is a product of the independent h_j modules, so each selector has B=beta, d=q, W=4q and R=0, independently of all preceding outcomes. Query all selectors next. The raw and true joint bills are exactly

    P_raw_good=L*4q/2=L/8, P_raw_good/I=4/85,
    P_joint_good=L(beta-4q)/2=P_joint.                        (12)

At this stopping boundary the nonconstant leaves are products of b_4 or b_4 with its origin value flipped. They are not silently erased. Their exact average influence and entropy are

    E I_leaf=17L/8,
    E H_leaf=L[3+H(b_4')/4],
    H(b_4')=6-(27/16)log2 3,
    I_root-E I_leaf=m/2+L/32.                                (13)

Every leaf satisfies H_leaf<=2 I_leaf: b_4 has (H,I)=(4,2), b_4' has I=5/2 and H<=4 by support, and tensor sums preserve the bound. Formula (13), not zero terminal entropy, is used in the stopping inequality.

To complete the tree to constant leaves without adding any bad-node bill, query the remaining four-bit modules one at a time. At each four-bit module root all influences are 1/2 for b_4 and 5/8 for b_4'. After any first query the remaining dimension is at most three, and every positive coordinate influence is at least 2^(1-3)=1/4. Hence B<=h2(d)<=1<=4d. Irrelevant coordinates have B=d=0. Tensor factors do not change B_i or d_i. This proves every tail node is good under arbitrary subsequent module-coordinate orders. The complete good tree retains exactly the raw bill 4 I/85 in (12).

The apparent m-growing shared parity boundary is charged at good core nodes when the order exposes the common phase first. A selector-first order charges it repeatedly at bad selectors. This is genuine order dependence of the larger W currency; in the exact joint-credit bill those physical deficits already cancel it.

For every complete tree on this family, the true joint bill also obeys sum_v w_v[B_v-Kd_v]_+<=sum_v w_v B_v<=H(f), since Delta H=B+JS and JS>=0. Thus it is <=9I/4 in the general-r family and <=2I in the r=4 subfamily. This uses the explicit class entropy bound in (2)-(3); it is not a new universal ownership argument. The exact small selector-prefix and good-order joint bills in (10)-(12) are stronger source-specific information.

## 6. What is and is not closed

The EVERY-tree raw or R-dropped payment is false, at every fixed threshold. The existential B05/C019 bridge survives, and this family has an explicit complete good tree. The exact joint-credit ledger is validated, not refuted. No new universal FEI constant is obtained. The first unsupported universal line is still existence of an influence-paid selection/ownership rule for arbitrary Boolean nodes; general overlapping nonlinear phases do not have the two disjoint Fourier rows used in (2).

The shortest next test is to replace the shared character phase by a versioned nonlinear phase (for example a one-point surgery of that character), retain the newly colliding signed rows and terminal phase entropy, and test whether the exact joint-credit correction or a paid exposure order survives. An uncharged reduction to an arbitrary Boolean phase is forbidden: it would contain the full FEI problem.

## 7. Exact shared-core exposure criterion (new policy interface)

The fresh-point-control exposure formula in A021 section 5 motivates, but is not a premise for, this counterpart with shared parity. Consider any adaptive prefix that queries selectors and exposes complete original quadratic core pairs; a selector may be queried only between completed pairs. No x_j coordinate is queried until this prefix ends. Every selector is queried once, even if its function is already irrelevant; queries can then be contracted without changing the bill. Let U_j be the number of still-free shared-core bits when selector j is queried, as a random variable under the physical input. Stop the prefix after all shared core bits and selectors have been queried, preserving the x_j leaves.

If U_j>0, the remaining core is an even-dimensional nondegenerate quadratic bent sign up to a constant, and its two parity rows again have disjoint Fourier support. Thus B=beta/2, d=q/2 and W=q(4+U_j)/2 at that selector. It is bad, independent of previously queried selectors and their outcomes. If U_j=0, the revealed parity p is fixed: the selector is irrelevant when p=0, and has (B,d,W)=(beta,q,4q) when p=1. The quantities are therefore B=P(p=1|history)beta and d=P(p=1|history)q at all allowed selector histories. Their ratio beta/q is either unchanged or irrelevant.

The tower property at the stopping history of each selector gives E P(p=1|history)=1/2, including adaptive choices of the next selector. The extra W term exists only for U_j>0, where the conditional parity is fair. Consequently the exact selector-only bills are

    P_raw_selectors = q/2 [4L + sum_j E U_j],
    P_joint_selectors = L(beta-4q)/2.                         (14)

The latter is unchanged by these policies even though the former sees repeated unexposed shared phase bits. For an asserted raw selector payment P_raw_selectors<=C I(f), its exact necessary and sufficient condition within this prefix class is

    sum_j E U_j <= (2C/q) I(f)-4L.                            (15)

This isolates shared-phase reuse as a physical exposure sum, with exact signed Fourier admission. It is not a whole-tree adaptive theorem: intervening core nodes can become bad after selected selector outcomes, and their bill and all terminal entropy remain separate. Fully exposing the core first is the proved good order in section 5. Removing the pair-boundary admission introduces overlapping Fourier rows, so (14)'s proof cannot be extended by treating those rows as a mixture.
