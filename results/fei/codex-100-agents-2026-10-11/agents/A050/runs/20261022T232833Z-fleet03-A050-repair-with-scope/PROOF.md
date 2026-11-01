# A priced lift that preserves core correlations

All inputs are uniform, signs are Boolean, and entropy, cross-entropy and KL use bits. Full FEI is open. The changed hypothesis is a supplied complete core-reference certificate. It replaces the failed requirement to pay the full coordinate-product canonical projection on every core.

## 1. Root calibration and the normalized lift

Let h be any Boolean sign on a finite data cube, p its squared Fourier law, mu=E h, u=mu^2=p(empty), and v=1-u. Let q be any normalized law dominating p. If v>0, domination gives q(empty)<1; define

    q*(empty)=u,
    q*(s)=v q(s)/(1-q(empty)), s!=empty.

If v=0 set q*=delta_empty. With the standard zero-mass conventions the KL chain rule gives

    CE(p,q*)=CE(p,q)-D_2(Ber(u)||Ber(q(empty))).            (1)

Write B for the nonnegative binary KL in (1). Calibration never increases price. If u=0, q* has no empty mass; this removes only a root reference-only atom. If u=1 the calibrated price is zero. All denominators used in the nonconstant case are positive. This is a specified INITIAL calibration, with B subtracted once. It is not permission for free descendant resets.

Define F_h(x,a,b,z)=(-1)^a at x=0, h(z) at x=b=1, and+1 otherwise. In Fourier-mask coordinates x,a,b,z, its two a-containing atoms a,xa have masses1/4. Its zero-data control atoms empty,x have masses(1+mu)^2/16, and b,xb have masses(1-mu)^2/16. For each nonempty data frequency s it has four atoms, at control masks0,x,b,xb, each of mass p(s)/16. Zero masses are omitted.

Define Q by copying the six actual zero-data/a-sector masses and replacing p(s)/16 by q*(s)/16 in those four copies for s nonempty. Its total mass is

    1/2+(1+mu^2)/4+(1-mu^2)/4=1.

It dominates the source, and all its reference-only rows are kept after this definition. Exact sectorwise likelihoods give

    A:=D(P_F||Q)=D(p||q*)/4.                            (2)

Thus this reference preserves the supplied joint core law. It is generally neither a product of singleton marginals nor the canonical occupancy projection falsified by A047/A049.

## 2. The control price is at most three bits

Put g(b,z)=+1 on b0,h(z) on b1. The a-character supports are disjoint from all g supports, so exact Fourier expansion gives

    H(F_h)=2+H(g)/2.

Erasing the b frequency from the spectrum of g gives the mixture (delta_empty+p)/2. The entropy of this erased law is at most1+H(h)/2, by including the fair mixture label. The erased b label has conditional entropy at most1. Therefore

    H(g)<=2+H(h)/2,
    gamma(mu):=H(F_h)-H(h)/4<=3.

This proof uses finite entropy chain rules only. It does not use FEI. Equations (1)-(2) imply the exact identity and its bound

    CE(P_F,Q)=gamma(mu)+(CE(p,q)-B)/4
             <=3+CE(p,q*)/4.                            (3)

Let t=Pr(h=-1). Direct physical pivotal probabilities give

    I(F_h)=1+t/2+I(h)/4.                                (4)

Consequently a SUPPLIED certificate CE(p,q*)<=C I(h), for any C>=4, yields

    C I(F_h)-CE(P_F,Q)>=C-3+C t/2.                      (5)

The simpler certificate CE(p,q)<=C I(h) suffices by (1). The calibrated certificate is weaker. There is no assertion that either is available for every Boolean h. Substituting q=p and assuming H(h)<=C I(h) would only restate a class/composition consequence; the explicit application below instead supplies a distinct, nonmatching reference and checks its complete price.

## 3. Same inherited source and signed payment

At each fresh physical query erase its frequency from both source and reference and use the SAME actual coherent branch kernel. On an erased source-zero/reference-positive row use the fair fallback. Normalize each inherited reference by its own branch probability. Reference-only rows stay in every normalization.

At one query the product of the conditional erasure likelihood, branch-outcome likelihood and inherited child likelihood equals the original source/reference likelihood on every source-positive atom and possible branch. Averaging logarithms and iterating proves

    A=sum_reached(erasure KL+outcome KL)+mean_terminal inherited KL. (6)

The initial calibration credit B has already been used in Q and is not released a second time. A is one complete source account, not an account plus a second copy of its decomposition.

For any finite stopping tree, let Hf,If be the physical mean terminal entropy/influence, R=I0-If, e=H0-Hf-C R and S=C If-Hf. Influence telescoping makes R>=0, and exact algebra gives

    S-(A+e)=C I0-CE(P_F,Q).                             (7)

The signed liability is J=[A+e]_+. Hence

    S-J=min(S,C I0-CE(P_F,Q)).                          (8)

This formula requires the actual negative query edges to stay available in the same account. It does not imply payment of the stronger A+[e]_+, which discards those edges. This is precisely the signed repair identified by A036 and retained in A047's obstruction analysis.

Query b first, then any finite adaptive tree of fresh data queries only in b1, retaining b0 and keeping x,a unqueried. Suppose each actual terminal core g has a supplied certificate H(g)<=C I(g). The exact selector formulas H=2+H(g)/2 and I=1+I(g)/2 give S>=C-2. Combining (5),(8) yields

    S-J>=min(C-2,C-3+C t/2)>=C-3.                       (9)

In particular at C=4 the SAME signed owner has at least1 bit remaining. An already booked conservative overpayment 0<=omega<=1/4 leaves at least3/4 bit. It is subtracted once, never renewed at a descendant. All final entropy and reference KL bills remain in (6). The newly added hypothesis is a complete supplied core price plus actual frontier certificates and retained signed query credit; it is not an entropy-only payment assumption.

### One actual mixed controller exposure, at rate four

There is a useful continuation beyond data-only stopping. At ANY selected active data-frontier leaves in b1, query x or a once, then stop those new pairs; retain b0 and every complementary data leaf. Each pre-query leaf is the selector of the independent a-character and its certified core g.

For an x query the children are the character and g. Their mean surplus is [4+(4I(g)-H(g))]/2>=2. For an a query, its physical influence is1/2. The entropy decrement is nonnegative: writing p_e=(p_0+p_1)/2, the parent drop is H(S_a|S_rest)+H(p_e)-[H(p_0)+H(p_1)]/2, a sum of nonnegative conditional entropy and Jensen-Shannon divergence. Thus the mean child surplus is at least the parent surplus minus4*(1/2), hence at least0. This is an AGGREGATE pair certificate; no claim that either a-child individually has nonnegative surplus is needed.

The retained b0 terminal has reach1/2 and surplus2, contributing1. Unchanged active terminals have nonnegative surplus, and every newly exposed a-pair has nonnegative mean surplus. Hence the complete mixed frontier has S>=1, and S>=2 if only x pairs are exposed. The original complete-reference margin is still at least1, because Q is inherited without a reset. Equation (8) therefore keeps SAME-owner margin>=1 through this mixed exposure, and>=3/4 after the old quarter. This closes a real controller query after a paid prefix while retaining the complementary branch, not merely another data-only class. The statement is at C=4 and stops at the new pairs; it does not supply a fresh descendant reset or arbitrary divergent data histories after a.

## 4. A nonmatching reference for the canonical counterfamily

For a width-r point-defect sign, r>=2, put delta=2^-r and v_r=4delta(1-delta). Its spectrum has p_r(empty)=(1-2delta)^2 and equal masses4delta^2 at every nonempty subset. Define the normalized nonmatching reference

    q_r(empty)=p_r(empty),
    q_r(s)=(7/8)p_r(s)+(v_r/8)1_{s=full block}, s!=empty.

It is positive at every source atom, has the same empty mass, and differs from p_r because there is more than one nonempty frequency. Thus KL is strictly positive. The likelihood bound q_r(s)>=(7/8)p_r(s) gives

    A_r<=v_r log2(8/7)<v_r/4.

The strict rational logarithm sign follows from 8^4<2*7^4. Also ln2>2/3 follows from the first positive term and remaining positive tail of the atanh expansion. The point spectrum has exact nonempty entropy8(r-1)delta(1-delta); its empty contribution is at most v_r/ln2<3v_r/2. Thus

    CE(p_r,q_r)<[8r-1]delta(1-delta)
               <8r delta-delta=4I(point_r)-delta.        (10)

All inequalities are strict for r>=2. A width0 restriction is constant and a width1 restriction is a character; both have entropy zero. The elementary point-defect H<=4I certificate and tensor additivity supply all required frontier certificates.

Take h as a product of m disjoint width-r point signs for ANY m>=1,r>=2, and q=product q_r. Empty mass matches because both products have empty probability product p_r(empty). Entropy, cross-entropy, KL and influence add on these disjoint blocks. Equation (10) gives the genuine supplier certificate

    CE(h,q)<4I(h)-m delta.

The lifted Q therefore satisfies

    4I(F_h)-CE(P_F,Q)>1+2t+m delta/4.                   (11)

Equations (8)-(9) pay this full inherited source through EVERY stated data-only history, at unchanged rate4, leaving at least1 before omega and at least3/4 after omega<=1/4. This includes A047's all-width family m=2^(r+2), A047's (m,r)=(64,2), and A049's 30-variable (9,3) witness. Those witnesses falsify the unchanged singleton reference, not this new lift. The general theorem is analytic in m,r; no large truth table or extrapolation is used.

Signed-credit boundary: at r=2, A_r=(1/4)log2(256/245)>0. For m=512 the lifted root source is A=32log2(256/245)>2, because256^16>2*245^16. After all data are exposed, the actual final S is exactly2. Thus even this improved Q cannot be paid by A alone from that terminal owner; A+[e]_+ also fails. Equation (11) gives root margin>33, so the exact net A+e=2-rootmargin<-31 and its positive part is zero. The negative query credit remains in the same source account. This control prevents confusing the new signed theorem with the stronger conservative assertion that has just failed. After old omega=1/4 the same final owner retains7/4 in this example.

## 5. Scope, comparisons and next unpaid line

The prior G<2 canonical repair remains valid and was independently accepted by A047 and A048. Their newer exact-entropy admission above G<2 is already done; it is not repeated here. A047/A049 show why no exact-estimate improvement can make complete singleton-canonical pricing universal. The present repair changes the reference and retains the same full-source/terminal accounting.

This is a comparison of INITIAL references at the same Boolean reached root. It does not retire an already owed canonical source bill or convert a previous canonical reference to Q for free. The retained omega allowance concerns eligible bookings against the newly specified lifted account. If an earlier physical history arrives with a different reference, its actual signed conversion and old source liability must be paid before invoking this root construction as a continuation.

An ordered comparison at this interface is: (i) assuming a small singleton marginal gap is sufficient for the old canonical reference but excludes the large tensors; (ii) testing its exact CE admits further small cores but fails at every fixed rate on A047's family; (iii) a supplied complete correlated core certificate, with one explicit root calibration and retained signed account, admits all the tensor witnesses at rate4. These conditions concern different references; no globally weakest sufficient hypothesis is claimed. Within the new lift, calibrated price is weaker than raw supplied price by exactly the binary KL refund. The price is a core certificate, not assumed free information about an arbitrary Boolean spectrum.

Excluded operations are renewing the reference at a descendant, deleting the b0 terminal, spending an ancestor booking twice, or asserting arbitrary terminal certificates. The one mixed exposure above has an explicit paired certificate; further mixed histories are permitted by algebra (7) only if their ACTUAL frontier S is certified. The data-only lower bound S>=C-2 cannot be carried across such histories without proof. Similarly, a fresh correlation-preserving reset still needs its signed likelihood/conversion cost. The supplied core reference and its price remain the first unpaid universal line. Constructing them for an arbitrary Boolean core would already contain the missing FEI content; this result proves no dimension-independent universal FEI constant.
