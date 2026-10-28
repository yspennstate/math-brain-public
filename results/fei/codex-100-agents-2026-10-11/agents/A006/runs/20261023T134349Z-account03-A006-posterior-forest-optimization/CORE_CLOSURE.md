# A paid shared-core dictionary, and why separate core branches do not close

All logarithms are base two. The local samplers below are NEW normalized references, not original-prime queues or canonical partition forests. Every run consists of actual first branch/anchor choices and canonically ordered local subset draws. The output is the physical union. Only these events, never aliases or arbitrary draw permutations, are summed in the posterior. For each output A, with actual run probabilities q(r), Q(A)=sum_(r->A)q(r), the minimum of sum_r theta(r)log(1/q(r))-H(theta) is exactly -log Q(A), attained at theta(r)=q(r)/Q(A). Its excess for any other theta is KL(theta || q/Q(A)). Thus every output-probability lower bound below retains the FULL posterior refund, including branch, anchor AND local-allocation ambiguity. Lower bounds on output cost cannot be evaded by choosing another posterior.

## 1. Arbitrarily large common cores cost a constant

Fix a nonempty physical core Z of size k>=1, disjoint private blocks X_j of widths w_j>=1, and

    U=product_j OR(X_j), T=OR(Z) OR U, f=2T-1.
    t=2^-k, epsilon_j=2^-w_j, p_j=1-epsilon_j,
    a=product p_j, S=sum epsilon_j, W=sum w_j epsilon_j,
    J=a sum w_j epsilon_j/p_j.

Physical pivotal counting gives I=I_core+I_private, where

    I_core=2tk(1-a), I_private=2tJ.                         (1)

Take the unchanged A006 anchor sampler Q on E_j=Z union X_j, with local activity beta_j=t epsilon_j, local empty mass 1-beta_j, mass c_j=beta_j^2/(1-beta_j) at EACH particular nonempty mask, rho=tS, and anchor prior beta_j/rho. Let Q_Z be uniform on the 2^k-1 nonempty subsets of Z. Fix once for the whole output

    R=(Q_Z+Q)/2.                                           (2)

This pays the branch and every core subset. Z is public in the supplied representation, not chosen after observing the output. It is not free to change a previously spent reference.

For B a nonempty private set meeting L blocks, absence of core coordinates leaves exactly one local-mask tuple. Thus

    Q(B)=(L/rho) product_active c_j product_inactive(1-beta_j).

For each D subset Z, adding D to the first active local mask preserves its probability and its L actual anchor choices. This injects actual runs for B into actual runs for B union D, so Q(B union D)>=Q(B). There may be many other allocations; these increase the exact probability and are never counted as aliases. Consequently

    -log R(B union D)
      <=1+log_+(rho)+2 sum_active(k+w_j)+3rho.              (3)

Here beta_j<=1/4, -log(1-beta_j)<=3beta_j and c_j>=beta_j^2. The exact negative term log(rho/L) was present before upper bounding by log_+rho.

Write d(Z)=indicator(all Z zero). Since f=1-2d(1-U), each nonempty core-only set D has squared coefficient 4t^2(1-a)^2. For each B nonempty private and each D subset Z, the squared coefficient is 4t^2 Uhat(B)^2. The product PRIVATE spectral distribution Uhat^2/a has block occupation epsilon_j. Therefore

    core-only mass =4t(1-t)(1-a)^2,
    private-bearing mass =4ta(1-a),
    mass of outputs meeting X_j =4ta epsilon_j.            (4)

These are physical Fourier moments, not cloned-core surrogates. For the core-only outputs (2) gives length <=1+log(2^k-1)<=k+1. Their expected cost is <=(5/2)I_core: indeed (1-2^-k)(1+1/k)<=5/4, checked directly for k=1,2,3 and bounded by 1+1/k<=5/4 for k>=4, and (1-a)<=1.

Average (3). The constant costs <=2I_core. The part 2k per active block costs 8takS<=4I_core because aS<=1-a. To verify that inequality without a spectral assumption, the disjoint events in which exactly block j fails have total probability a sum epsilon_j/p_j<=1-a, which dominates aS. The 2w_j part costs 8taW<=4I_private. Finally log_+rho<=3rho/2, so logarithm plus inactive-mask debit costs

    <=18ta(1-a)rho=18t^2a(1-a)S<=(9/2)I_private,

using t<=1/2 and J>=aS. Thus the complete nonempty output cost obeys

    C_R(f) <= (17/2)I_core+(17/2)I_private=(17/2)I(f).      (5)

The standard binary empty/nonempty wrapper adds at most 2I, so full cost <=21I/2, using the established binary-wrapper inequality h2(Var f)<=2I. The main theorem (5) concerns complete NONEMPTY cost and needs no wrapper lemma. No entropy bound for f paid (5).

## 2. Two separate incomparable core branches still fail

Let U_X,U_Y each be products of r disjoint width-two OR clauses on independent private coordinates; z,y are separate physical bits. Let T_1=z OR U_X, T_2=y OR U_Y, and F=2T_1T_2-1. Their supplied clause supports have incomparable maximal repeated cores {z} and {y}. Put a=(3/4)^r. The physical quantities are

    I_star=1-a+(r/2)(3/4)^(r-1),
    I(F)=(1+a)I_star,
    P_F({z,y})=(1-a)^4/4.                                (6)

Run the ONE unchanged global anchor sampler Q on all 2r supplied supports. For output {z,y} every local mask must be empty or its group's core singleton, with at least one singleton in each group. Put beta=1/8,c=1/56,e=7/8,d=e+c=25/28. Summing the actual anchor-weighted tuples gives

    Q({z,y})=(c/beta)d^(r-1)(d^r-e^r)
             <=(1/7)d^(2r-1).                            (7)

Now augment by the TWO individual core dictionaries, with any fixed global mixture

    R=lambda_0 Q+lambda_1 delta_z+lambda_2 delta_y,
    lambda_i>=0, sum lambda_i=1.

At {z,y} neither individual branch contributes, so R({z,y})<=Q({z,y}). For r>=4, a<1/2, P_F({z,y})>1/64, I_star<2 and I(F)<3. Since log(28/25)>3/28,

    C_R(F)/I(F)>(2r-1)/1792 -> infinity.                  (8)

The assertion includes lambda_0=0 as infinite cost. It even allows optimizing these fixed priors separately for every function, or convex mixtures of such R: the pointwise ceiling (7) survives. All allocation and anchor posterior refunds are already inside Q. No chosen witness can beat its exact physical output probability. This is a reference-family obstruction, not an FEI counterexample.

These F have H(F)<10I(F). To see boundedness independently, the source single-star proof gives H(f_i)<6I(f_i). Let q_i be its true nonempty conditional spectrum (only for this entropy comparison, not for constructing (2)). For any independent sign components g,h, means b_1=E[(1+g)/2], b_2=E[(1+h)/2], and supplied normalized nonempty q_1,q_2, choose uniformly X-only,Y-only,both and draw the indicated references. Direct disjoint Fourier expansion gives complete nonempty cost

    C=Var(F)log3+b_2 C_1+b_1 C_2,
    I(F)=b_2 I(g)+b_1 I(h).                              (9)

For example total spectral weight with nonempty X is b_2 I-free mass Var(g), so its logarithmic q_1 contribution is b_2 C_1; this follows from coefficients 2 Uhat(A)Vhat(B) and Parseval sum Vhat^2=b_2. Each C_i<=H(f_i), Var(F)<=I(F), and the wrapper adds <=2I(F), proving H(F)<(8+log3)I(F)<10I(F). Thus (8) cannot disprove FEI.

## 3. What repairs the interaction, and what is not proved

Applying (9) to the explicit two component references (2) yields a different, normalized once-sector code with C< (17/2+log3)I<11I and wrapper <13I. Its both-sector genuinely generates the union {z,y}. This is not an unpaid conversion from the failed global Q. The actual sector and both component draws are recorded once, and their full posterior is over these events. It is a concrete repair for these disjoint components, not a representation theorem for intersecting cores.

The precise universal first unsupported line is: find a fixed influence-paid closure of the core/intersection dictionaries under the combinations required by the physical spectrum, with selector/attachment/allocation cost <=K I on the SAME physical influence account. Merely listing all individual repeated cores, optimizing their priors, or optimizing the old activation probabilities cannot establish it. Core unions may require a growing family of joint events, and arbitrary overlapping components invalidate (9).

## 4. The same failure with genuinely intersecting cores, even after adding their intersection

Keep the independent width-two stars from section2 and add one physical coordinate x. Put

    G=2[x OR (T_1 AND T_2)]-1.

The actual CNF supports are {x,z} union X_j and {x,y} union Y_j. The two repeated cores C_1={x,z}, C_2={x,y} are incomparable and have the NONEMPTY intersection {x}. Let Q be the unchanged ONE global anchor law on these full supports. Permit ANY mixture of Q and ANY normalized dictionary branches supported on nonempty subsets of C_1, C_2 or their intersection. Priors and these local dictionary laws may be optimized separately for every function, but are fixed before the final output. This is more general than uniform core dictionaries and includes all individual core and intersection atoms.

For A={z,y}, every such core/intersection branch has probability ZERO because A is contained in neither core. A clause run producing A must omit x and all private coordinates. Put beta=1/16, c=1/240, e=15/16, d=e+c=113/120. Exactly the actual-event enumeration in (7) gives

    Q({z,y})=(1/15)d^(r-1)(d^r-e^r)<=(1/15)d^(2r-1).      (10)

Writing h=2T_1T_2-1, the physical expansion G=(1+h)/2+(2x-1)(1-h)/2 yields

    P_G({z,y})=(1-a)^4/16,
    I(G)=1-(1+a)^2/4+I(h)/2.                              (11)

For r>=4 these give P_G({z,y})>1/256 and I(G)<3, since I(h)<3 and the extra core influence is<1. As log2(120/113)>ln(120/113)>7/120, EVERY permitted mixture R satisfies

    C_R(G)/I(G)>7(2r-1)/92160 -> infinity.                (12)

The result is unchanged by convex mixtures over such references or by choosing the best full actual-run posterior: all their output probabilities obey (10). It rules out ALL dictionaries whose individual outputs stay within one of the two cores or their intersection, not a branch that actually samples their joint combinations. Such a joint branch is precisely the missing closure.

These are still bounded-FEI functions. The Fourier coefficients on A nonempty from h appear twice in G with one-half amplitude. Their entropy contribution is (1/2)H_nonempty(h)+Var(h). The two empty/core singleton coefficients have squared masses b^2,(1-b)^2, b=(1+a)^2/4; each p log(1/p)<1. Thus H(G)<H(h)/2+3. For r>=4, I(G)>1-b>7/16 and I(G)>=I(h)/2. Section2 proved H(h)<10I(h), so H(G)<[10+48/7]I(G)<17I(G). This is an actual Boolean reference obstruction on NONEMPTY physically intersecting cores, not a disproof of FEI.

The INTERSECTING_SPEC search is separately frozen after the first main search. Its direct character sums, direct physical edge counting and actual target-event probabilities use a fresh implementation with no source-agent imports. The joint-core closure remains unproved; adding only the pairwise intersection does not pay it.
