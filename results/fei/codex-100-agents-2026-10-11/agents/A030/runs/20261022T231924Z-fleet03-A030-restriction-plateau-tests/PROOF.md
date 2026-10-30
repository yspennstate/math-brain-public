# Unequal means and a new rare label

Current target, under exact checking: the general three-cut residual from A030@2 need not admit a dimension-independent local influence price, even after granting actual JS release and the actual unused least-reserve cut slack. This is a statement about the declared local transaction, not FEI.

For even r>=2 let epsilon=2^-r, t=2^(-r/2), and g(z)=(-1)^(sum_j z_(2j)z_(2j+1)) on uniform binary physical coordinates. Its normalized Walsh coefficients are +/-t, its mean is t, and g(0)=1. Let kappa_0(z)=1 if g(z)=1 and2 otherwise. Let kappa_1 differ only at z=0, where it takes label0. The full controller is kappa_s(z), where s is one extra fair physical coordinate. It is surjective. Set F=u_(kappa_s(z)) on disjoint independent data cubes, where u_0 is a two-bit point defect, u_1 is three-bit majority, and u_2 is a negative two-bit point defect. All three are nonconstant and non-flat, with means(1/2,0,-1/2), entropies(2,2,2), and influences(1,3/2,1).

The actual queried influence is d=epsilon/2. Define h_j=1-2C_j, w=(5/16,3/16,5/16), R=sum_j(1-m_j^2)phi(q_j), and E=Delta_s H(F)-sum_j w_j Delta_s H(h_j)-Delta_s R. All cuts and both physical children remain in this definition. The proposed asymptotic is

E/d = r/4 + 3/(4 ln2) - 7/4 + o(1).

The actual finite-label JS release satisfies Delta_s J/d ->3/4. Thus even E-Delta_s J has an unbounded ratio to d. The following is a self-contained analytic proof, supported by the exact checker's compact and raw-Boolean reconstructions. Independent external review is pending; no Lean certification is claimed. Equal-mean A030@2 remains at its original scope.

## 1. Exact Fourier-sector formula

For indicator C_j write c_j(S)=hat C_j(S), q_j=E C_j, and let a=sum_j m_j C_j. With V_j=1-m_j^2, disjoint independent private cores give the exact identity

H(F)=H_un(a)+sum_j V_j H_un(C_j)+sum_j q_j[H(u_j)-phi(m_j^2)]. (1)

Here H_un(v)=sum_S phi(hat v(S)^2) is allowed for a non-Boolean, unnormalized vector. This follows by expanding every coefficient with a nonempty private set: it is c_j(S)hat u_j(T), and no other private block contributes. The private-empty coefficients are exactly hat a. The product identity phi(xy)=x phi(y)+y phi(x), including zero factors, proves (1). All sums are finite. This is not an entropy comparison with a non-Boolean relaxation; F and both children are actual Boolean functions, and H_un is only an exact algebraic component.

For any means, put lambda_j=(m_j-m_l)(m_j-m_k) and use the original three-cut weights w_j=[1+m_lm_k-m_j(m_l+m_k)]/4. Then V_j-4w_j=-lambda_j. Subtracting the weighted cut entropies from (1) leaves the coherent term

H_un(a)-sum_j lambda_j H_un(C_j)

plus a scalar function of q and m and the already-retained source entropies. On nonempty controller rows, sum_j c_j=0 and (sum_j m_j c_j)^2=sum_j lambda_j c_j^2. This quadratic identity cancels common scaling logarithms but does not bound the local curvature when one cut amplitude vanishes. For this family lambda=(1/2,-1/4,1/2); the rare newly introduced label is precisely the vanishing baseline amplitude.

## 2. A uniform finite-difference estimate

Write f(x)=phi(x^2), b=1/ln2 and

Psi(a,d)=f(a+d)+f(d)-[f(a)+f(a+2d)]/2.

This is the contribution of a Fourier row whose two actual child coefficients are a and a+2d. On a nonzero interval f''(x)=-(4 ln|x|+6)/ln2. If a!=0 and |d|<=|a|/4, the interval between a and a+2d does not contain zero. The centered second-difference integral has total kernel mass d^2. For every point x in that interval,

|ln(|x|/|a|)|<=2|x-a|/|a|<=4|d|/|a|.

Consequently

|Psi(a,d)-d^2[log2(a^2/d^2)+3b]|<=8b |d|^3/|a|. (2)

This proves the remainder uniformly in the row sign; there is no Taylor expansion through zero. The d=0 case is read as zero. For a=0 the exact formula is Psi(0,d)=4d^2. For a bounded away from zero and d=O(epsilon), (2) gives Psi(a,d)=O(epsilon^2 log(1/epsilon)); constants can be fixed once r>=4. These estimates involve only finitely many amplitude types, so no limit is exchanged with an uncontrolled sum.

## 3. Actual changed rows and the asymptotic

The canonical bent Walsh law has N=1/epsilon coefficients +/-t, with counts n_+=(N+sqrt N)/2 and n_-=(N-sqrt N)/2. Its empty coefficient is +t. At s=0, C_0=0, C_1=(1+g)/2, C_2=(1-g)/2; at s=1 they are E_0,C_1-E_0,C_2, where E_0 is the indicator of z=0. Thus C_2 and h_2 do not change.

For h_1=-g the changed nonempty and empty rows all have a=+/-t and d=epsilon. For r>=4, |d/a|=t<=1/4. Equation (2), summed over EXACTLY N rows, gives

Delta H(h_1)=epsilon(r+3b)+O(epsilon t). (3)

For h_0, the N-1 nonempty rows have a=0,d=-epsilon and the empty row has a=1,d=-epsilon. Hence

Delta H(h_0)=4epsilon+O(epsilon^2 r). (4)

The exact indicator C_0 increment is epsilon: every one of its N rows has a=0,d=epsilon/2. The nonempty C_1 rows have a=+/-t/2,d=-epsilon/2, and the empty row has a=(1+t)/2,d=-epsilon/2. Thus

Delta H_un(C_1)=epsilon(r+3b)/4+O(epsilon t+epsilon^2 r). (5)

For a=m_1 C_1+m_2 C_2 at s=0, the nonempty rows have a=+/-t/4,d=epsilon/4, and the empty row has a=(t-1)/4,d=epsilon/4. Its empty baseline stays at distance at least3/16 from zero for r>=4. Hence

Delta H_un(a)=epsilon(r+3b)/16+O(epsilon t+epsilon^2 r). (6)

The q-weighted source terms in (1) are affine in the physical child probabilities and cancel in a controller decrement. Equations(5),(6), V_0=3/4 and V_1=1 give

Delta H(F)=epsilon[(5/16)(r+3b)+3/4]+O(epsilon t+epsilon^2 r). (7)

The old rarity release is 3epsilon/8+O(epsilon^2). Indeed its new-label term is exactly (3/4)[phi(epsilon/2)-phi(epsilon)/2]=3epsilon/8; the C_1 probability stays in a fixed compact subinterval of(0,1), so its scalar concavity gap is O(epsilon^2). C_2 is unchanged. Subtracting (5/16) times(4), (3/16) times(3), and this SAME rarity release from(7) yields

E=epsilon[r/8+3b/8-7/8]+O(epsilon t+epsilon^2 r). (8)

The actual coupled controller endpoints differ only at z=0. Independent core outputs u_0,u_1 disagree with probability(1-m_0m_1)/2=1/2, so d=epsilon/2 exactly. Since t->0 and r epsilon->0, dividing(8) proves

E/d=r/4+3b/4-7/4+o(1). (9)

The coefficient r/4 is therefore analytic and uniform; it is not inferred from finite ratios. Exact finite ratios differ from the limiting formula by the stated vanishing remainder.

## 4. Full cuts: actual unused reserve slack is zero

Fix C=1 and ONE own-history controller policy: query s first, then all r original controller bits in one fixed order. Supply each actual h_j with its least nonnegative Bellman reserve Q_1 for precisely that policy, retaining both actual child continuations. Define its unused root slack by

s_j=Inf_s(h_j)+Q_1(h_j)-E Q_1(h_j child)-Delta H(h_j).

For h_1, the explicit lower bound from(2) is Delta H(h_1)>=epsilon(r+3b-8bt)>epsilon for r>=4; here t<=1/4 so the bracket is at least r+b. For h_0, its nonempty rows contribute4epsilon(1-epsilon). Its empty-row Psi(1,-epsilon) is nonnegative: every real row's restriction entropy increment is a nonnegative multiple of1+h2(q)-h2(p), where h2(p)<=1. Thus Delta H(h_0)>epsilon for r>=4. Both queried cut influences are epsilon. Their raw root debt Delta H-Inf is strictly positive, and all supplied child reserves are nonnegative. The positive-part operation in the Bellman recursion is inactive; hence s_0=s_1=0 exactly. The h_2 query is a dummy and its two continuations are identical, so s_2=0 as well. The original weighted unused slack sum_j w_j s_j is ZERO, despite retaining all three complete cut reserves. It cannot absorb(9).

## 5. A029's actual JS account and the structural remainder

At every history the three sources have entropy2. Their nonempty private spectra are disjoint. For q=(q_0,q_1,q_2) the actual data-set marginal consists of one empty atom(q_0+q_2)/4, three atoms q_0/4, four atoms q_1/4 and three atoms q_2/4. Therefore

J(q)=phi((q_0+q_2)/4)+3phi(q_0/4)+4phi(q_1/4)+3phi(q_2/4)-2. (10)

The two actual child label laws are(0,p,1-p) and(epsilon,p-epsilon,1-p), p=(1+t)/2; the root is their midpoint. The new-label three-atom part of Delta J is exactly3epsilon/8. All other arguments in(10) are uniformly away from zero for r>=4, so their midpoint gaps are O(epsilon^2). Thus

Delta J/d=3/4+O(epsilon). (11)

In particular, for EVERY fixed finite K,A>=0, all sufficiently large even r satisfy

E > K d + A Delta J + sum_j w_j s_j. (12)

This does not contradict A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@1: it books signed DATA Delta J and nonnegative CONTROL Delta J while retaining the complete signed structural Lstr. In the present CONTROL query Delta T=0, and the exact remainder E=Delta J+Delta Lstr-sum w_j Delta H(h_j)-Delta R locates the divergence in the structural-to-cut conversion. Replacing Lstr by its JS component changes the bill and loses the term. Granting a constant multiple of the genuine local JS release cannot repair it. This is an obstruction to this specified local conversion, not to a global ancestor structural payment.

## 6. Reachability from the paid equal-mean slice

Replace u_0 by a*u_0 and u_2 by b*u_0 using two fresh independent fair sign tags a,b; keep u_1 as majority. Initially all three core means are zero, so the previous equal-mean theorem applies to CONTROL queries. Reveal a and b, preserving all four actual outcomes. The outcome(a,b)=(+1,-1) has physical reach1/4 and is precisely the unequal-mean family above. Each of these is a proper actual DATA exposure, not a new controller or a chosen Fourier row.

Every tag query keeps the original own-history cut reserves r_j fixed and changes only the actual core means. Their original weights w_j(m) are separately affine, so P=sum_j w_j(m)r_j is exactly harmonic through BOTH tag queries. All four history weights and full source/structural terminals are retained. Thus the bad node can be reached from the paid diagonal with the SAME cut bank; the equal-mean hypothesis cannot be assumed hereditary after even this two-query history. A separate exact finite history certificate checks the two martingale identities and all source/marginal/structural costs. It does not claim the entire mixed tree is universally paid.

## 7. This is not an FEI counterfamily

The original F has dimension n=r+8. Every z_i has baseline influence1/4 before the one-point relabeling. The relabeling changes its pivotal indicator only on the two coupled endpoints incident to the one modified controller point, a set of probability at most epsilon. Therefore Inf_(z_i)(F)>=1/4-epsilon>=3/16 for r>=4. Consequently I(F)>=3r/16 while H(F)<=r+8, giving H(F)/I(F)<=16 for r>=4. Both actual s children and all core terminal functions remain in the ledger. The equal-mean tagged predecessor also has a uniform bound, e.g. H/I<20 by the same control-edge bound and n=r+10. No actual unbounded H/I family has been produced.

## First unsupported universal line and mechanism change

The proposed local unequal-mean upgrade of A030@2 is now refuted, rather than merely unpaid. The replacement obligation is a genuinely global payment of the complete coherent structural rows from one original signed ancestor account, with all original cut continuations, DATA refunds and both physical terminal/source costs retained. A029's JS transport is usable at exactly its declared scope; its remaining U-b-J_root cannot be silently enlarged by promised frontier J or by the present cut bank. This stage retires fixed local cut/rarity/JS influence pricing for this obstruction and moves next to the full structural conversion, rather than repeating generic all-coordinate searches.
