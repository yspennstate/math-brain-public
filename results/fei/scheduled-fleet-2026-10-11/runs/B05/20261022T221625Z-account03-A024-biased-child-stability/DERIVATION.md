# First core query: retain both controller accounts

The corrected normalization used throughout is Eplus_mu(g)=sum_{S nonempty} phat_mu(S) log2[product_{i in S}(1-mu_i^2)/phat_mu(S)], where phat_mu(S)=ghat_mu(S)^2. There is NO output-variance factor in the numerator. On physical uniform coordinates H(g)=Eplus(g)+e((E g)^2). Contract deterministic inputs before using a biased normalized basis. None of the following erasure or face formulas requires such a basis or divides by any variance. A signed-dictator outer gate has no new transport remainder; r=1 below is exactly that endpoint, while r=0 is constant. The bound (C) is uniform as a approaches zero or beta approaches zero, so near-dictator and stationary-mean limits introduce no hidden 1/a factor.

Let w(z),h(u) be arbitrary disjoint Boolean signs on uniform physical cubes. Put t=Pr(w=-1), r=Pr(h=-1), J=I(h), and F=1-(1-w)(1-h)/2. Fix an actual controller tree T, with original physical reaches p_v; it may depend on controller answers, but it does not depend on a core answer. At its node v put d_v=Inf_x(w_v), q_v=I(w_v0 w_v1)/2. The inherited stage-2 identities are reconstructed by partitioning same-block and mixed-block faces:

    d_x(F_v)=r d_v,
    q_x(F_v)=r q_v+J d_v/2.

The exact erasure is r B_x(w_v)+R_r(a_v,beta_v), where

    R_r(a,b)=L(1-r+r a,r b)+r(1-r)L(1-a,b)-r L(a,b),
    L(a,b)=e(a^2)+e(b^2)-e(a^2+b^2), e(s)=-s log2(s).

Take e(0)=0. No variance is divided out. At r=0 the lifted function is constant and all strict-bad indicators are zero; r=1 returns w.

For a chosen K define E(r)={v:B_x(F_v)>K r d_v}. Define the actual lifted-prefix bill

    C(r,J)=sum_v p_v 1_E(r)(v) [r q_v+J d_v/2].

Now query a physical coordinate y of h FIRST. Let its two actual children be h_0,h_1, and let r_b=Pr(h_b=-1), J_b=I(h_b), d=Inf_y(h), q=I(h_0 h_1)/2. Uniform restriction gives (r_0+r_1)/2=r and (J_0+J_1)/2=J-d. The actual current query costs d_y(F)=t d, q_y(F)=t q+I(w)d/2. A fair query does not bias any unqueried physical input.

Write E=E(r), E_b=E(r_b), and define the SIGNED migration amount

    M=sum_{v,b} (p_v/2)(1_Eb(v)-1_E(v))[r_b q_v+J_b d_v/2].

Then, exactly,

    (C(r_0,J_0)+C(r_1,J_1))/2
       =C(r,J)-d P_w(E)/2+M,                 (A)
    P_w(E)=sum_{v in E}p_v d_v.

Proof: replace every child indicator by the parent indicator plus its signed change, then use the two averaging identities. In particular, a disappearing bad node contributes NEGATIVELY to M. Deleting that rebate is not an equality. Original p_v are used in both children; their joint physical reaches are p_v/2.

If epsilon denotes whether the current core query itself is K-bad in F, the whole prefix with this query inserted costs

    C_new=C(r,J)+epsilon[t q+I(w)d/2]-d P_w(E)/2+M.   (B)

If the inserted query is good and membership is unchanged, the prefix bill DECREASES by d P_w(E)/2. If it is bad and membership is unchanged, the increase is exactly t q+d[I(w)-P_w(E)]/2. The latter complement is the ORIGINAL good-controller pivot exposure, not a new controller influence allowance. These conclusions concern the odd-face bill, not an entropy bound by themselves.

After T finishes in either branch, w=-1 with its original probability t. Hence the two active terminal functions are the ACTUAL h_0,h_1 with weights t/2 each; all other terminals are constant. Retained terminal entropy is t[H(h_0)+H(h_1)]/2, retained influence t(J-d), and retained Q is t[Q(h_0)+Q(h_1)]/2. Including the first query spends exactly t d+r I(w) influence and leaves that terminal influence. No t H(h) is silently consumed or replaced by a new reference.

For the UNFILTERED controller tree E=T the migration is zero and P_w(E)=I(w). Consequently first-core insertion plus the full controller prefix plus both terminal Q gives precisely Q(F), in either order. This independently checks the mixed-face factor 1/2 and is also valid for a stopping controller tree with its actual leaf Q terms retained.

The first unsupported universal line is a dimension-independent payment for the positive part of M together with any current bad-query cost from one unused inherited account, for a selected policy. Formula (A) alone does not pay M. Existing individually paid controller trees do not supply it. Hard threshold membership must be recomputed in both children; using E in their place only proves the frozen-mask identity and is not a restriction-tree theorem.

## A uniform bound for the complete scalar erasure remainder

The signed mean-log remainder itself has a universal local price for this binary activation gate:

    R_r(a,b) <= (6/ln 2) r |b| <= 9 r d.          (C)

Here 0<=r<=1, -1<=a<=1 and |b|<=d are all that is used. In fact (C) holds for arbitrary real b under the first two conditions, before the final |b|<=d substitution. Both signs of b and a, deterministic r=0,1 and b=0 are included. This is an upper bound, not an assertion that R is nonnegative.

For x>=0, log(1+x)<=sqrt(x): set x=s^2, then the derivative of s-log(1+s^2) is (s-1)^2/(1+s^2)>=0, and the function vanishes at s=0. Hence L(u,b)<=2|u b|/ln2, including u=0 or b=0 by continuity. Drop only the nonpositive term -r L(a,b) in R. Since |1-r+ra|<=1 and |1-a|<=2,

    R <= (2/ln2)r|b|[|1-r+ra|+(1-r)|1-a|]
      <= (6/ln2)r|b|.

Finally ln2>2/3, from log2=2[1/3+(1/3)^3/3+...] with positive terms, gives the conservative rational constant 9. Sharper constants are not needed for the present account.

Consequently B_x(F)<=r B_x(w)+9 r d_x(w). Every controller node with B_x(w)<=K0 d_x(w) stays (K0+9)-good in EVERY core child, for arbitrary output mean and arbitrary core history while the blocks remain disjoint. Any newly (K0+9)-bad controller node lies in the fixed tighter mask E0={B_x(w)>K0 d_x(w)}. This pays all scalar mean logarithms for binary activation, including near-deterministic limits. It does not extend (C) to an arbitrary multi-input outer gate.

For a FIXED controller tree and this slackened threshold, all interleaved core-first children therefore have prefix bill bounded by r Q_w(E0)+J P_w(E0)/2, with the corresponding -d P_w(E0)/2 release after a core query. The hard-mask migration can be avoided by a valid fixed-mask upper bound, but its mixed pivot term J P_w(E0)/2 remains unpaid. The earlier K4 obstruction explicitly shows why an own Q_bad(w) bound cannot pay that term. This identifies the remaining credit more narrowly: the scalar residual has an influence price here; selected mixed-face pivot exposure is the universal gap.

## One potential for every interleaving of two prescribed component trees

Fix arbitrary complete fair physical trees T_w,T_h. At each component subtree let Q_w^0 be its expected own K0-bad odd-face bill and P_w^0 its own K0-bad pivot mass; define Q_h^0,P_h^0 likewise. These are subtree accounts of the ORIGINAL prescribed trees; they are not refilled after a query. All components remain uniform at every actual rectangular history. Put

    Phi(w,h)=r Q_w^0+t Q_h^0
       +[I(h) P_w^0+I(w) P_h^0-P_w^0 P_h^0]/2.       (D)

The negative product term is essential: it is the overlap rebate for pairs whose two endpoints are both designated bad. Since 0<=P_w^0<=I(w) and 0<=P_h^0<=I(h), Phi>=0.

At a query x prescribed by T_w, let e_w indicate whether this query is K0-bad in w itself. The component subtree recurrences give, EXACTLY,

    Phi(w,h)-average_b Phi(w_b,h)
      =e_w[r q_x(w)+I(h)d_x(w)/2]
           +(1-e_w)P_h^0 d_x(w)/2.                  (E)

To check (E), use Q_w^0=e_w q_x(w)+avg Q_wb^0, P_w^0=e_w d_x(w)+avg P_wb^0, I(w)=d_x(w)+avg I(w_b), and t=avg t_b. Core quantities stay fixed. The product P_w^0 P_h^0 is linear in the changing account because the other factor is fixed. The h-query formula is symmetric. This proof does not assume a predetermined schedule of which block moves next.

By (C), any (K0+9)-bad query of F must have e_w=1 (or e_h=1 in the other block). Its odd-face cost is exactly the bracket in (E). Hence, for EVERY adaptive interleaving respecting the two prescribed component trees and EVERY stopping cut,

    sum_actual_(K0+9)-bad_nodes physical_reach*q_x(F)
          +E Phi(actual terminal pair) <= Phi(original w,h).       (F)

For constant terminal F, Phi is zero: either an inactive component is constant +1, annihilating the other component's accounts, or all active components are resolved. For nonconstant terminals, keep both Phi and their FULL physical spectral entropy; (F) does not certify their FEI cost. The definition also includes zero-influence/dummy queries.

Thus arbitrary interleaving does not require renewing either bad-pivot account, and all scalar mean logs are paid once by the threshold slack. Individually linearly paid component Q accounts do not imply a linear raw root price: on the prior tensor seeds with their prescribed selectors-first trees, P_w^0=P_h^0=L/16, I(w)=I(h)=37L/16, and the mixed term is 73L^2/512. For w=-G_L,h=G_L one has I(F)=37L/16, so Phi/I=4/37+73L/1184. The same fixed-module controller-first K13 trees have no actual bad nodes; this diagnoses overcharge in the envelope, not an FEI counterexample. The root-only O(I) claim for EVERY prescribed individually paid tree pair is therefore FALSE. This does not rule out selecting different component trees. The sharper next target prices only mixed exposure still needed after slackening the actual threshold, using a policy dependent on the current pair.

More precisely, there is no reason to discard the unused positive releases in (E). Define D_T as the physical-reach-weighted sum of (i) P_other^0*d/2 at every own-K0-GOOD query, and (ii) q_x(F) at every own-K0-BAD query that is actually (K0+9)-GOOD after lifting. Then

    actual bad bill + E Phi(terminal) + D_T = Phi(root).       (G)

All terms in D_T are nonnegative and are disjoint debits of the SAME original Phi. There is no rebanking or additional influence owner. On complete trees, the universal next step is to choose component trees and an interleaving with Phi(root)-D_T<=C I(F), rather than the already false demand Phi(root)<=C I(F). For K0>=log2(e), the lead's localization gives H(F)<=(K0+9+2/ln2)I(F)+Phi(root)-D_T. This does not solve full FEI: an arbitrary Boolean function need not arrive with a useful nontrivial disjoint binary-activation decomposition, and the net mixed credit is still unpaid even on this interface. The contribution is exact nonrenewing history transfer and a paid scalar remainder, not a new universal entropy constant.
