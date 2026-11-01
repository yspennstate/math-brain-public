# Repeated fallback payment on the actual physical tree

All entropy units are bits. Write eta(t)=-t log2(t), Phi(a,b)=eta(a)+eta(b)-eta(a+b), with zero terms understood by continuity. All cubes and trees are finite and uniform. Distinct data cores are independent and physically disjoint. Descriptions of the same physical core must be merged.

## Independent review of A087 v1

The reviewed source is A087-OWNED-CONTROLLER-REVEAL-AND-RESOLVED-CONTINUATION@1 in run 20261014T020842Z. Its original statement, hypotheses, authors and recorded hash are retained in this run's claim record. No substantive repair is supplied.

Partition Fourier rows according to which nonempty data core they contain. If a controller query X confines a selected core to only one branch, its two X amplitudes have equal absolute values. Its spectral erasure contribution equals its variance times its unconditional selector probability. Its selector probability doubles in that branch and vanishes in the other, so this is precisely that core's contribution to kappa=R-E R_child, R=sum eta(q_j)Var(u_j). All those rows cancel from B_X-kappa. The remaining rows are exactly the Fourier transform of the real mean profile g=sum m_j C_j; no normalization is made.

One constant child, after an output sign flip, gives B_X-kappa=Var(g_live)/2+Phi((1-d)^2,d^2), d=(1-E g_live)/2. Since Var(g_live)<=4d(1-d), the residual is <=2d(1-d)+Phi((1-d)^2,d^2)<=3d. The scalar inequality follows on d<=1/4 from Phi(A,B)<=B log2(e(A+B)/B), then monotonicity of 2(1-d)+d[2log2(1/d)+1/ln2], whose endpoint is 5/2+1/(4ln2)<3. On [1/4,1/2], Phi(a^2,b^2)<=2|ab| gives 4d(1-d)<=3d; symmetry handles [1/2,1]. Endpoints follow directly.

For physically disjoint child blocks, private profile supports are disjoint. Put means mu_0,mu_1 and profile variances v_0,v_1. Then d=(1-mu_0 mu_1)/2 and B_X-kappa=(v_0+v_1)/2+Phi(((mu_0+mu_1)/2)^2,((mu_0-mu_1)/2)^2). It is nonnegative and at most 1-min(mu_0^2,mu_1^2)<=2(1-mu_0 mu_1)=4d. This product formula is used only for independent physical children.

The physical channel bound is J_X<=2d/ln2. For paired amplitudes a,b its contribution is (a^2+b^2)[1-h2(1/2+ab/(a^2+b^2))]. The natural-log scalar gap obeys ((1+t)ln(1+t)+(1-t)ln(1-t))/2 <= 1-sqrt(1-t^2): differentiate and use atanh(t)<=t/sqrt(1-t^2). Consequently each row costs at most 2min(a^2,b^2)/ln2, and summing gives the stated channel bound. Thus D_X-kappa has precisely the two source rates 3+2/ln2 and 4+2/ln2.

For completeness, Phi(a^2,b^2)<=2|ab| follows by homogeneity and monotonicity, for 0<z<=1, of [(1+z^2)ln(1+z^2)-z^2 ln(z^2)]/(2z). Its derivative numerator is (z^2-1)ln(1+z^2)-z^2 ln(z^2)>=0, from ln(1+x)<=x and -ln x>=1-x; the endpoint is ln2. This proves the scalar in bits, including zeros.

For r=s=1, controller order X,A,B makes every query one-sided or an independent-branch split, even after any actual data restrictions. The A059 signed DATA identity then telescopes on exactly that tree. Its terminal profile is H-U-R=Eraw(ghat^2)+sum q_j Var(u_j)H(Chat_j^2/q_j). At a resolved label it is eta(m_j^2)<=Var(u_j)/ln2<=I_leaf/ln2. This reconstructs the complete source theorem, with inherited U and unresolved frontiers excluded as in its statement. Verdict: HOLDS at its exact stated scope.

## Independent reconstruction of A059's override lemma

Late complete-board reconciliation located A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@1, run 20261014T025828Z, PRIORITY_PROOF equations (1)-(4). The following derivation independently reconstructs its repeated-fallback mechanism and gives a stronger intermediate factor 8-4p. It is not a new claim of priority or an essential repair of the source's valid rate 8. The source's ordered-priority result covers any number of stages; the two-core shared-X application below is narrower and is not presented as a replacement for it.

Let W be any Boolean exclusive independent-core controller on its own physical block: W=sum a_j(z)u_j(y_j), with partition indicators a_j (constants permitted). Let u be a distinct independent Boolean core. Let P be a fresh r-bit point event, r>=1, and F=P u+(1-P)W. Use the original refined selectors C_u=P and C_j=(1-P)a_j, not independent copies of W at the two query children. The core reserve is still the original R=sum eta(q_j)Var(u_j).

At an actual point-control query, let p=2^{-(r-1)} be the probability that all the other live point controls match, q=p/2, mu=Eu, nu=EW, Delta=mu-nu, V_W=1-nu^2, and Z=sum_j E a_j Var(u_j). Physical independence gives d=Inf_X(F)=p Pr(u!=W)=p(1-mu nu)/2. In particular there is no replacement of W by a fresh copy. Define

L(p)=p(1-p)/2+Phi((1-q)^2,q^2),
K(p)=eta(1-q)-(1/2)eta(1-p).

K(p)>=0 by concavity of eta. Direct selector probability conditioning gives kappa=q Var(u)+K(p)Z. Indeed the fallback selector probabilities are E a_j times 1,1-p in the two children and times 1-q at the parent; the logarithm of E a_j cancels exactly. This remains true for zero masses and constant cores.

The exact residual formula is

B_X-kappa = Phi((nu+q Delta)^2,(q Delta)^2) + p(1-p)Delta^2/2 + L(p)V_W - K(p)Z.    (1)

To verify it, the u-nonempty rows have equal X amplitudes and erasure q Var(u), canceled by kappa. On every nonempty remaining-point-control row the two amplitudes have equal magnitudes, yielding p(1-p)E[(mu-g_W)^2]/2 in the empty-data sector and the same coefficient times Z in fallback data sectors. On the empty remaining-point-control row, nonconstant fallback profile coefficients have amplitudes (1-q)ghat_W and -q ghat_W, yielding Phi((1-q)^2,q^2)Var(g_W). Fallback data rows give the same coefficient times Z. Since Var(g_W)+Z=Var(W)=V_W, these terms combine into (1). The constant row gives the first Phi term. Crucially, this is the spectrum of one W and its actual selector partition throughout.

Dropping only the nonpositive -K(p)Z gives a finite influence price, without any core slack assumption. The three remaining contributions satisfy:

1. Phi((nu+qDelta)^2,(qDelta)^2)<=2|nu+qDelta|q|Delta|<=p|mu-nu|<=p(1-mu nu)=2d. The parent mean is in [-1,1]; |mu-nu|<=1-mu nu follows from (1-mu nu)^2-(mu-nu)^2=(1-mu^2)(1-nu^2)>=0.
2. p(1-p)(Delta^2+V_W)/2<=2(1-p)d, since Delta^2+V_W=mu^2-2mu nu+1<=2(1-mu nu).
3. V_W Phi((1-q)^2,q^2)<=2q(1-q)V_W<=4(1-q)d, since V_W<=2(1-mu nu).

Therefore B_X-kappa<=(8-4p)d and

D_X-kappa<=(8-4p+2/ln2)d<=(8+2/ln2)d.    (2)

No nonnegativity of the signed residual is needed or asserted by this new lemma. At d=0 the bounds and formula are read directly; both actual children coincide. A general arbitrary controller query without point-override geometry is outside (2). Data shared between u and W is outside its independence hypothesis.

## All private widths and data-interrupted priority continuation

Consider two independent cores and events E_u=(X=sigma) AND A_r and E_v=(X=tau) AND B_s, with disjoint private point controls and r,s>=1. The priority gate selects u if E_u, else v if E_v, else +1. Respect controller order: shared X first, then the private A controls, then the private B controls, skipping irrelevant coordinates or resolved labels. Arbitrary adaptive fresh data queries may occur between any controller reveals. Conditional remaining cores can have every attainable bias, including constants.

The original selector masses are q_u=2^(-r-1); q_v=2^(-s-1)(1-2^(-r)) in the same orientation and q_v=2^(-s-1) in opposite orientation; q_default=1-q_u-q_v. Core means mu,nu are arbitrary attained numbers in [-1,1], including both endpoints. The events share exactly the ONE physical bit X: they must not be replaced by independent Bernoulli outer inputs. Core data overlap is zero; repeated cores in different query children are the same physical block, not new independent inputs. Every descendant uses its actual restricted selector probabilities, not these original masses.

If sigma=tau, X is one-sided and paid by A087. Its live child is A_r u+(1-A_r)W with W=1+B_s(v-1), physically independent of u. Every still-live A query is exactly (1), even when it is separated from the preceding A query by data exposure. If the A event fails, the remaining B queries are one-sided point activation. If it succeeds, the controller label is resolved. If sigma!=tau, the X children are independent private activations; their remaining queries are one-sided. Thus every controller query in either orientation has the uniform upper rate K_ctrl=8+2/ln2 on its actual D-kappa.

At any finite actual controller-resolved stopping frontier, the signed A059 DATA telescope and the accepted profile identity give

H(F_root)<=U_root+R_root+(3/ln2)T_data+(8+2/ln2)Pi_ctrl+E I_leaf/ln2,

where U_root=sum q_j[H(u_j)-eta((Eu_j)^2)], R_root=sum eta(q_j)Var(u_j), T_data=sum_data reach*q_j*beta_j^2<=Pi_data, and I_root=Pi_data+Pi_ctrl+E I_leaf. All quantities belong to the same physical tree. R_root<=2 I_ctrl(root) is the previously reviewed original-edge funding. It must be added to the residual debit, yielding total control funding at most (10+2/ln2)I_ctrl(root); it is not an account that can be renewed after a data query. The estimate retains inherited U_root and does not fund arbitrary core entropy.

This independently confirms A059's removal of A087's specific X,A,data,A obstruction at r=2,s=1. It does not repeat A028's already-paid control-only block theorem. Source verdict: A059 v1 HOLDS, including its any-stage ordered induction, arbitrary frontiers and retained resolved-terminal cost. Its unresolved-frontier claim is exactly the signed telescope with H-U-R retained, not a bound on that terminal.

## New later-test reveal before the first test is settled

Now consider the private two-test priority gate F=A u+(1-A)[B v+(1-B)], where A and B are point events on separate still-live control blocks and u,v are independent disjoint data cores. Query a B coordinate BEFORE A has been decided. Let a=Pr(A), q=Pr(B), mu=Eu, nu=Ev, b=1-nu, d=(1-a)q b. Here q=2^-s with s>=1; the queried B bit toggles only if all the other B bits match, so the actual influence is exactly d, after arbitrary previous core data restrictions. At every reachable nonzero A event that is not yet decided, a<=1/2. Failed A has a=0; successful A makes every B query irrelevant.

The selected u probability a is unchanged across this query, and u's nonempty data rows have no B query frequency. The v selector probability (1-a)q doubles on the live B child and vanishes on the other; its equal-magnitude query rows contribute exactly (1-a)q Var(v), equal to the fine release kappa. Thus those rows cancel without treating either child as an independent copy of the repeated u.

The empty-data profile is g=A mu+(1-A)[1-B b]. Its exact spectral erasure residual is

B_X-kappa = (q-2q^2)b^2(1-a)
              + a(1-a) Phi((mu-1+q b)^2,(q b)^2)
              + Phi((1-a(1-mu)-d)^2,d^2).             (5)

For nonempty remaining B frequencies the query amplitudes match, giving the first term by Parseval for 1-A. For the empty remaining B frequency, nonempty A frequencies have amplitudes Ahat(mu-1+qb), Ahat(qb), and sum of squared Ahat is a(1-a). The entirely empty pair has amplitudes the actual parent mean 1-a(1-mu)-d and -d. This proves (5) for every private width, including point-event endpoints and zero influence.

The first term is <=2(1-2q)d because b<=2. The second is <=4a d because |mu-1+qb|<=2 and Phi of squared amplitudes <=2 times their absolute product. The last is <=2d because the parent mean has absolute value at most one. Hence

0<=B_X-kappa<=(4-4q+4a)d<=6d,
0<=D_X-kappa<=(6+2/ln2)d.                           (6)

The final bound uses a<=1/2 when unresolved; for a=1 the physical function is u, so D=kappa=d=0 directly. All three terms of (5) are nonnegative, so the lower bounds follow as well. No child independence is used: the SAME u survives in both children.

Combine (6) with A059's original-reserve override lemma for ANY A reveal, whose fallback remains the current B activation regardless of which B bits or data have already been queried. If a B test has failed, A has a constant fallback. If A has failed, B is a simple point activation. All reachable geometries are covered. Consequently the previous same-tree stopped inequality, with coefficient 8+2/ln2 and exact unresolved terminal H-U-R retained, holds for arbitrary adaptive private controller query orders, for every r,s>=1. For the two events with one shared physical X, still query X FIRST: A087 pays that first split. Opposite orientation leaves a single point activation on each X branch. Same orientation leaves exactly the two-test priority gate above. Subsequent private controller queries and data can occur in arbitrary adaptive order. At resolved leaves use the existing I_leaf/ln2 terminal price.

This is the new authored extension. It removes the priority-order restriction for TWO private tests, after the shared X has been exposed, at the SAME uniform coefficient 8+2/ln2 and without an additional reserve. It does not remove the first-X restriction or prove arbitrary-order payment for three or more priority tests, arbitrary controllers, or overlapping data cores. Its independent reviewers are A059/A087/A064/A090.

## First unsupported universal line

There is no proved universal bound for inherited U_root or for an unresolved arbitrary-controller profile from one unused influence account. The next controller-order extension is a MIDDLE test among three unfinished private point tests. Its later fallback is a nonconstant Boolean controller/core function, rather than the constant default in (5), and its earlier guard is unresolved. Importing (5) there without the fallback rows is the first unsupported controller line. Preserve their same physical Fourier rows and fine selector release before claiming another price. Shared physical data presents a separate gap: replacing p Pr(u!=W) by p(1-mu nu)/2 would already fail. Neither gap is a full FEI conclusion.

## Actual shared-data scope guard

Let both priority output descriptions be ONE physical Boolean core h, with mean m, and default +1. Keep A a two-bit point and B a one-bit point on fresh controls. Query the first A bit; the other-A matching probability is p=1/2 and Pr(B)=b=1/2. The actual queried influence is p(1-b)(1-m)/2: if B already succeeds, both query children return the SAME h. An independent-copy substitution would give p(1-m[1-b(1-m)])/2, exceeding the actual value by p b Var(h)/2. This is strictly positive for every nonconstant h and zero at both constant endpoints. The two h labels must be merged into selector A OR B before applying any independent-core profile formula.

out/OVERLAP_GUARD.json certifies this by independent full-function FWHT and direct physical edge counts for all22 Boolean tables with n<=2, including16 nonconstant guards and6 constant descriptions. It refutes only the product-of-means equality outside its independence hypothesis, not the scoped theorem or FEI. The all-dimensional excess formula follows from the elementary mismatch computation above.
