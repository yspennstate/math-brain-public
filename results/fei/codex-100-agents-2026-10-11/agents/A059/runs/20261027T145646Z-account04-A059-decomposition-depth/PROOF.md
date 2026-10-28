# Full terminal entropy under tensor-reservoir liquidation

Finite uniform Boolean cubes; H is squared-Fourier entropy in bits and I is total physical influence. All accounts below use A058's expected-resource scope, including explicit mean-zero branch innovations and BOTH full children. No full FEI source is assumed.

## 1. The received-cash action, independently reconstructed

At a physical query i of a current Boolean core g, write g_0,g_1 for its actual restrictions, d=H(g)-(H(g_0)+H(g_1))/2, p=Inf_i(g), and J_a=I(g_a), E_a=H(g_a). Suppose the ACTUAL cash eligible for a pending influence account of rate A>0 is R, after old debits and protected reserves. Require R>=d; otherwise this local action is inadmissible. Let q_a be survival probabilities after the query. Its expected new principal is (A/2)sum_a q_a J_a and cannot exceed R-d.

Put w_a=1-q_a. Required discarded capacity is

  e=max(0, (A/2)(J_0+J_1)-(R-d)).                     (1)

The newly frozen FULL entropy is F=(1/2)sum_a w_a E_a. It must stay in the stopped bill. When e>0 the ideal minimum discards capacity in increasing order of E_a/(A J_a); J_a=0 contributes no capacity, while Boolean I=0 implies a constant and E_a=0. For two positive capacities and e<=min_a(AJ_a/2), only the cheaper outcome is used and

  F_opt=e min_a E_a/(A J_a).                          (2)

This follows directly from F=sum_a (Aw_aJ_a/2)*(E_a/(AJ_a)), with nonnegative terms summing to at least e. Allocating exactly e in the cheapest outcome attains the lower bound under the stated capacity condition. This reconstructs A058's local LP at this scope; it does not independently accept every source premise or claim global policy optimality.

## 2. Tensor reservoir theorem: exact unavoidable price

Let h be ANY nonconstant finite Boolean sign with j=I(h)>0, s=H(h)>0. Let g be ANY finite Boolean sign, select one physical coordinate i of g, and tensor N disjoint fresh copies of h:

  G_N=g * product_{r=1}^N h_r,             N>=1.

Physical query i acts only in g. Parseval products give exactly

  H(G_N|i=a)=H(g_a)+Ns=:E_a(N),
  I(G_N|i=a)=I(g_a)+Nj=:J_a(N),
  D_iH(G_N)=d,                  Inf_i(G_N)=p.          (3)

These are actual Boolean products, not independent copies of shared variables. Fix A>0 and an old eligible depletion u>=0 independent of N; take actual RECEIVED cash R_N=A I(G_N)-u. This is a conditional received-state assertion, not a claim that every such u has already been produced by a physical history. Original source labels and old u are retained, never reset. Equations (1) and influence conservation give the N-INDEPENDENT mandatory liquidation

  e=(u+d-Ap)_+.                                      (4)

For all sufficiently large N, R_N>=d and e<=min_a AJ_a(N)/2. In fact J_a(N)>=Nj, so the latter follows from N>=2e/(Aj); also R_N>=d follows under that condition because R_N-d=A average(J_a(N))-e when e>0. At e=0, check R_N>=d separately. For e>0, set r=s/j and M=max_a |H(g_a)-rI(g_a)|. Then exact (2) gives

  F_opt(N)=e min_a (H(g_a)+Ns)/(A(I(g_a)+Nj)),
  |F_opt(N)-er/A|<= e M/(A N j).                     (5)

Indeed E_a(N)=rJ_a(N)+c_a with |c_a|<=M. Both denominators are positive; no sign reversal is hidden. Thus

  lim_N F_opt(N)= e H(h)/(A I(h))>0.                 (6)

The limit is positive whenever e>0. A reservoir of arbitrary Boolean factors therefore leaves a definite frozen entropy price even for the IDEALLY optimal outcome-sensitive action. Outcome adaptivity does not make that price vanish.

For comparison the best common survival probability has

  F_common(N)= e (E_0(N)+E_1(N))/(A(J_0(N)+J_1(N))),
  0<=F_common-F_opt<=2eM/(ANj).                       (7)

The common ratio is a capacity-weighted average of the two outcome ratios. Thus the entire outcome-adaptive advantage is O(1/N), while the unavoidable bill tends to a strictly positive constant. This refutes neither A058's optimum nor feasibility of another full-source policy. It quantifies a mandatory bill that any universal Bellman inequality must carry.

## 3. Physical coin precision costs real terminal entropy

Assume each q_a is implemented after seeing the core answer by at most b fresh independent fair physical dummy bits (not variables used by G_N). Then w_a is a multiple of 2^-b. If e>0, some w_a>=2^-b. Consequently every feasible such policy, optimal or not, satisfies

  F_physical(N,b)>= (Ns)/2^(b+1).                    (8)

This lower bound uses BOTH actual query outcomes, each of probability1/2. It holds for arbitrary events on b bits and for adaptive early decisions using at most b bits. Fixed b forces a frozen bill linear in N, even though the ideal optimum remains bounded. If F_physical<=B for a fixed B>0, necessarily 2^b>=Ns/(2B). Thus bounded physical liquidation requires logarithmically growing coin precision. This is a statement about dummy-decision resolution, not an assertion that these dummy coordinates cost function influence or entropy.

Conversely round each ideal q_a DOWN to the nearest multiple of2^-b. Feasibility is preserved; the extra entropy obeys

  0<=F_rounded-F_opt <= (E_0(N)+E_1(N))/2^(b+1).       (9)

For example choose b_N=ceil(2log2(N+1))+b0 for a fixed integer b0>=0. Then (9)=O(1/N), so the actual physical frozen bill has the same positive limit (6). This is sufficient precision, not a necessary sharp precision for every near-optimal sequence. Fixed-width coins cannot be used to claim the ideal asymptote.

There is no corresponding logarithmic lower bound on EXPECTED coin work. For a dyadic threshold k/2^b with 0<k<2^b, expose uniform bits only until their word differs from the b-bit word for k. The first differing bit determines whether the sampled integer is below k; if all b bits match, it is not below k. Before the (j+1)-st query there is only one undecided j-bit prefix, of probability2^-j. Hence the exact expected number of queried dummy bits is

  E T_b=sum_(j=0)^(b-1)2^-j=2(1-2^-b)<2.             (9a)

Thresholds0 and1 use no coin queries. This implements EVERY dyadic outcome action with its exact probability, all early-stop cylinders and both full core entropy sectors retained. Thus b_N growing like2log2(N+1) attains the ideal positive entropy limit with fewer than TWO expected dummy queries per liquidation, although maximum coin depth grows. Across any finite adaptive policy, conditional expectation bounds total dummy queries by twice the expected number of nontrivial liquidation decisions. There is no assumption on formula depth. The dummy bits are irrelevant to the Boolean function, so this implementational efficiency supplies no entropy payment and no new influence owner.

## 4. Actual positive-excess source, beyond rate9/2

Take A=6 and u=0. On m=8 physical exterior signs x_j use binary coordinates v_j=(1+x_j)/2. Let b=(-1)^(sum_{l=1}^4 v_(2l-1)v_(2l)), C=1_(x=1^8), c=2^-8, and K=b-C. Define g=K+Cz with fresh sign tag z, and query z. This is an actual Boolean9-bit core; b=+1 on the selected point. It has p=c. For every exterior frequency, |Khat|>=sqrt(c)-c, whereas |Chat|=c. The erasure alone is sum Phi(Khat^2,Chat^2)>=c log2(((sqrt(c)-c)/c)^2)>=7c. The Jensen-Shannon packet is nonnegative, so d>=7c. Hence e=d-6c>=c>0.

Let h be AND2 (a sign negative only at one point). It has H(h)=2,I(h)=1 by its four equal squared Fourier coefficients. The padded cores G_N have growing depth and dimension9+2N and satisfy exactly

  lim_N F_opt(N)=e/3>=1/768.                         (10)

This is a positive entropy floor even at a rate6 received state, rather than another attempt to fully fund arbitrary cores at the already refuted rate9/2. Full terminal children, their biases and the old depletion u remain literal. Exact check scripts certify the actual seed, capacities, both entropy sectors, and physical rounding. The all-N statement follows from (3)-(9), not extrapolation from the checked N range.

## 5. All adaptive stopping: distinct-factor occupation

For P_N=product_{j=1}^N AND2(a_j,b_j), consider ANY finite adaptive physical restriction tree, including repetitions on a previously touched factor's remaining coordinate, arbitrary stopping and fair dummy queries. At every leaf, a factor never touched by a query remains AND2, entropy2. A touched factor is a constant or a dictator, entropy0, even if its other coordinate is later exposed. Therefore, writing T for the number of distinct touched factors,

  H((P_N)_leaf)=2(N-T),
  E H((P_N)_leaf)=2(N-E T).                           (11)

This permits outcome-dependent continuation, unlike the earlier independent-schedule law. A sufficient bill bound or unbounded possible depth cannot imply exhaustion unless E T/N->1. On any terminal event of probability alpha where T<=r, terminal entropy is at least2alpha(N-r).

The same lower bound transports through ANY coherent source F=K(Z)+C(Z)P_N with physical KC=0 and sign off C, including arbitrary exterior/tag interleavings and core biases. Let t_v=E(C|current exterior restrictions), and U_v count untouched core factors. The core-frequency marginal implies H(F_v)>=t_v H((P_N)_v)>=2t_vU_v. Exterior queries preserve t_v U_v in conditional mean; dummy and already-touched-factor queries preserve it; a first-touch query decreases it by t_v. Thus with c=E C and J=sum_first-touch v w_v t_v,

  E H(F_leaf)>=2(cN-J).                              (12)

No independent survival assumption, empty-coefficient omission or current-density reset is used. This lower bound is not an equality for a changing coherent profile, and no claim that J<=a fixed multiple of influence follows. It gives a necessary masked distinct-touch payment target for any arbitrary adaptive terminal-decay proposal.

## 6. Exact unpaid line

Equations (5)-(12) price frozen entropy that current received-cash actions cannot silently delete. They do not prove or disprove FEI. What remains is a Bellman inequality that pays the ACCUMULATED full frozen bills and removes the live entropy using a sufficiently large SAME original influence owner, with all old depletions and siblings. Another cheap local ticket or ideal coin without its finite-resolution cost does not supply that inequality. A058's local optimum is accepted at scope; a global source/termination theorem remains open.
