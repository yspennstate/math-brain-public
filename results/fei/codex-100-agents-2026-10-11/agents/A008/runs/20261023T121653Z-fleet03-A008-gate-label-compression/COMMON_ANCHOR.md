# Physical overlap: an obstruction to the clause law and a paid core dictionary

All costs are ideal base-two cross-entropies. Fix r>=1 disjoint private blocks X_j of arbitrary widths w_j>=1 and ONE additional physical variable z, shared by every clause. Indicators use z in {0,1}. Put

    U(X)=prod_j OR_(w_j)(X_j), T=z OR U(X), f=2T-1,
    epsilon_j=2^-w_j, p_j=1-epsilon_j, a=prod_j p_j,
    J=a sum_j w_j epsilon_j/p_j.

Equivalently T=prod_j OR(z,X_j). Thus the supplied supports C_j={z} union X_j genuinely overlap; their read at z grows with r. They are a fixed physical clause dictionary, not independent copies of z. Direct pivotal counting gives

    Inf_z(f)=1-a, I(f)=1-a+J.                         (1)

Every private coordinate in block j has influence epsilon_j a/p_j: it is queried with z=0, all other clauses true, and the other w_j-1 private bits false. No independent-block influence formula is substituted for (1).

## The original normalized tag law, including allocation ambiguity

Use EXACTLY A006's anchor-mask law Q on the supplied supports C_j, with

    t_j=2^-(w_j+1)=epsilon_j/2, rho=sum_j t_j,
    c_j=t_j^2/(1-t_j).

A local empty mask has mass1-t_j and every particular nonempty mask has mass c_j. Choose anchor j with prior t_j/rho, force its local mask uniform nonempty, and draw all others in fixed order. Actual run mass is mu(tuple)/rho for every active anchor, and Q(A)=rho^-1 sum_{union tuple=A} K(tuple)mu(tuple). The sampler is normalized on nonempty physical outputs even under overlap. Its decoder reads each local mask once and takes the physical union; repeated occurrences of z decode to the same single coordinate. The optimal posterior refunds all DISTINCT actual (anchor,tuple) descriptions of that output. We do not replace this posterior by only an anchor count when allocations overlap.

For a nonempty PRIVATE set B, let B_j=B cap X_j and L(B)=#{j:B_j!=empty}. Since absence of z forces every local draw to omit z, its tuple is unique and

    Q(B)=[L(B)/rho] prod_(B_j!=empty)c_j
                            prod_(B_j=empty)(1-t_j).  (2)

For every active private block one can include or omit z in its local nonempty mask at the same mass c_j. The2^L-1 nonempty choices of those inclusions are distinct actual tuples, all with the same anchor choices. Consequently

    Q(B union {z}) >=(2^L-1)Q(B)>=Q(B).               (3)

Inactive blocks may also select {z}; these only increase the left side. Equations (2),(3) retain the physical allocation refund without claiming that z copies are independent Fourier coordinates.

## Exact obstruction to influence payment of Q on overlapping clauses

Set every private width equal to2. Then t=1/8, c=1/56 and d=(1-t)+c=25/28. For output {z}, every local mask is either empty or {z}, so the K-weighted tuple sum is r c d^(r-1). Hence

    Q({z})=(1/7)(25/28)^(r-1).                       (4)

The actual physical spectrum has P_f({z})=(1-a)^2 with a=(3/4)^r. For r>=4, a<1/2, so this mass exceeds1/4. Also I(f)=1-a+(r/2)(3/4)^(r-1)<2. The final bound follows since r(3/4)^(r-1) has maximum27/16 at r=3,4, and is decreasing from r=4. As ln(28/25)>=3/28 and ln2<1,

    C_Q(f)/I(f)>3(r-1)/224 -> infinity.              (5)

All other output costs are nonnegative, so the single atom already proves (5). This refutes ONLY an influence-paid extension of A006's supplied clause reference to arbitrary physical overlap. Its normalization, disjoint payment and source theorem remain correct.

It is not an FEI counterexample. The squared coefficients of U, divided by a, form the true independent PRIVATE-block law nu: local empty probability p=3/4, and each of three nonempty private subsets has mass1/12. Thus H(nu)=r[2-(1/2)log3]<2r. Writing the sign coordinate as zeta=2z-1, direct expansion f=(1+g)/2+zeta(1-g)/2 for sign g=2U-1 gives

    H(f)=2a H(nu)+2(1-a)h2(a)
          <4ra+2(1-a)<6I(f).                         (6)

The last inequality uses J=(2/3)ra. Neither (5) nor the repair below uses an assumed FEI inequality.

## Repair: pay one whole-set dictionary label

Fix the NEW normalized nonempty reference

    R(A)=(1/2)1_(A={z})+(1/2)Q(A)                    (7)

BEFORE sampling the spectral set. The first random bit chooses the shared-core dictionary or the original clause dictionary; in the core branch output {z}. The coordinate z is fixed in the supplied representation, and for r>=2 it is the unique intersection of all supports, so no output-dependent coordinate name is silently chosen. In the clause branch run the unchanged normalized sampler. This is one paid whole-set dictionary choice, not a free reference reset, an output-dependent prior, or a modification of the old source after restriction. Its complete output probability sums both branches where they coincide; for the following upper bound it suffices that R({z})>=1/2 and R(B),R(B+z)>=Q(B)/2. Every nonempty set has positive R probability. Finite tuples and the branch label decode uniquely to their union. An arithmetic code for this finite alphabet has asymptotic rate equal to its full logarithmic cost; no unpriced integer-prefix rounding claim is made.

For B nonempty private, (2) implies

    -log R(B), -log R(B+z)
       <=1+log(rho/L)+sum_(B_j!=empty)log(1/c_j)
                                +sum_(B_j=empty)log(1/(1-t_j))
       <=1+log_+(rho)+sum_(B_j!=empty)(2w_j+2)+3rho.   (8)

Here log_+(x)=max(0,log x), t_j<=1/4, c_j>=t_j^2, and -log(1-t_j)<=3t_j, since ln2>2/3 and 1/(1-t_j)<=4/3. The negative log(rho/L) is not omitted before establishing the exact expression (2). It is then bounded above legitimately by log_+(rho). Counts and inactive masks remain paid.

## True physical occupation moments pay the repaired law

For every private B!=empty, the actual Fourier masses at B and B+z BOTH equal hat U(B)^2. The total mass of these pairs is2a(1-a). Under nu=hat U^2/a, block j is active with probability epsilon_j. Thus the exact physical moments, already including both z choices, are

    sum_(private pairs) P_f=2a(1-a),
    sum_A P_f(A)1_(A cap X_j!=empty)=2a epsilon_j.    (9)

These are not the false moments from treating the r copies of z independently. In particular they remain valid for arbitrary unequal private widths.

Let S=sum_j epsilon_j=2rho. Then 1-a<=S and J>=aS. Furthermore log_+(rho)<=(3/2)rho and sum_j(w_j+1)epsilon_j<=2sum_j w_j epsilon_j. Apply (8),(9), plus the core atom's cost<=1. The resulting complete nonempty expectation is at most

    (1-a)^2
      +2a(1-a)[1+log_+(rho)+3rho]
      +4a sum_j(w_j+1)epsilon_j

    <=(1-a)+[2+3/2+3+8]J
    =(1-a)+(29/2)J <=(29/2)I(f).                    (10)

Each bracketed debit is separately justified: the constant term uses1-a<=S; the log term uses rho=S/2; the3rho term has the same S relation; and the occupation term uses w_j+1<=2w_j and p_j<=1. No debit is reused and no entropy of f pays a cost. The standard h2(Var f)<=2I(f) binary empty/nonempty wrapper gives full cost<=(33/2)I(f). Formula (7) itself is a normalized NEW root reference; no claim of a paid conversion from a previously spent reference is made.

## Universal frontier

The all-overlap normalization in A006 is correct but insufficient: common shared coordinates can carry almost all spectral mass while the clause prior spends exponentially little there. The one-bit core augmentation repairs every common-anchor instance above, including unequal widths and arbitrary r, at a dimension-independent COMPLETE reference cost. For arbitrary overlapping supports, finding and paying a finite or hierarchical family of shared-core dictionaries, including their global selector and physical allocation moments, is still unproved. That universal representation/occupation line, rather than another independent-clause calculation, is the next C020 target. Full FEI remains OPEN.
