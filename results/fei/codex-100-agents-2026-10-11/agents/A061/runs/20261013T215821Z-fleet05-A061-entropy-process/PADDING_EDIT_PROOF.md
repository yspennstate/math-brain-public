# Arbitrary-core single-edit admission: three exact local limits

Let g be any Boolean sign on r>=0 uniform coordinates, append q>=4 dummy coordinates, and write n=r+q. At any vertex v, flip its value to obtain F. Put delta=2^{-n}, d=2delta=2^{1-n}, s=g(v_old), and K=|supp(ghat)|. Every previously irrelevant coordinate (in g or newly appended) becomes relevant with influence d. Every Fourier coefficient of F is nonzero: old nonzero coefficients lie in 2^{-r}Z and have magnitude at least 2^{-r}; the edit changes every coefficient by a signed d, smaller by 2^{1-q}. Previously zero coefficients become signed d. For r>=1 the sharper parity granularity 2^{1-r} is available, but the zero-dimensional constant core requires the stated weaker universal normalization. Full-support admission was already established by A002; the new content is the exact local information and drift it introduces.

## 1. Exact packets at every newly relevant coordinate

Fix any coordinate j that was irrelevant before the edit. Reflect physical inputs so that the edited vertex is zero, retaining its core sign s. On residual Fourier labels T, let c_T be the old padded coefficient, so exactly K of the 2^{n-1}=1/d residual labels are occupied. Define u_T=c_T/(s d). Its nonzero values are integer multiples of 2^{q-1}, so |u_T|>=8. The parent paired coefficients are

    a_T=s d(u_T-1), b_T=-s d,
    q_T=d^2[(u_T-1)^2+1], b_T^2=d^2.

The physical children have coefficients s d u_T and s d(u_T-2), in an order determined by the reflection. These are actual Boolean children, not a spectral mixture. All previously irrelevant coordinates give the SAME multiset of u_T: deleting an absent Fourier coordinate does not change the old support and vertex phases. Hence all three local rates are identical at all newly relevant coordinates.

For A(u)=(u-1)^2+1, write

    ell(u)=log2 A(u),
    beta(u)=A(u)log2 A(u)-(u-1)^2 log2((u-1)^2),
    gamma(u)= [u^2 log2(u^2)+(u-2)^2 log2((u-2)^2)]/2
              -(u-1)^2 log2((u-1)^2),

with zero log terms zero. For the 1/d-K unoccupied labels u=0, these values are respectively 1,2,4. The exact formulas are therefore

    lambda_j(F)/d = 1+d sum_{T:c_T!=0}[ell(u_T)-1],
    B_j(F)/d      = 2+d sum_{T:c_T!=0}[beta(u_T)-2],
    D_j(F)/d      = 4+d sum_{T:c_T!=0}[gamma(u_T)-4].       (1)

The logarithms of d cancel in the entropy-decrement formula because each packet's parent mass equals the average child mass. This cancellation is algebraic and does not assert that a packet itself is a normalized Boolean spectrum.

## 2. Uniform bounds, including the signs

Put kappa=Kd<=2^{1-q}. Every |c_T|<=1, so |u_T|<=1/d and A(u_T)<= (1/d+1)^2+1 <=9/d^2. Thus ell(u_T)<=2log2(3/d). All occupied |u_T|>=8 imply |u_T-1|>1, hence ell(u_T)>1 and beta(u_T)>2: the function Phi(x,1)=(x+1)log2(x+1)-xlog2 x is increasing in x>0.

For the drift sign define x=|u-1|>=1 and

    G(x)=[(x+1)^2 log2((x+1)^2)+(x-1)^2 log2((x-1)^2)]/2
             -x^2 log2(x^2).

Then gamma(u)=G(|u-1|). Its derivative on x>1 is

    G'(x)=(2/ln2)[(x+1)ln(x+1)+(x-1)ln(x-1)-2xln x]>0,

by strict convexity of x ln x on positive x; its endpoint limit is continuous and G(1)=4. Therefore gamma(u)>4 on occupied labels, and all three ratios in (1) exceed their limiting values strictly.

The earlier proved scalar JS bound gives the packet bound J/d^2<=2/ln2, since min(a_T^2,b_T^2)<=d^2. The binary-entropy bound beta(u)<=ell(u)+1/ln2 follows from the already reviewed log compensation. Consequently, using log2 3<2 and 1/ln2<3/2,

    1 <= lambda_j/d <= 1+2 kappa(n+1),
    2 <= B_j/d      <= 2+kappa(2n+4),
    4 <= D_j/d      <= 4+kappa(2n+7).                       (2)

The lower inequalities are strict for finite q because K>=1, and the upper inequalities allow dropping negative baseline terms. In particular every newly relevant coordinate has rates tending to (1,2,4) as q->infinity at fixed arbitrary core g. Its exact derivative-packet law nu is uniform over all 1/d residual labels, so the lead's KL form becomes

    KL_2(nu_j||q_j)=n-1-lambda_j/d = n-2-O(Kd n).           (3)

This is an arbitrary-core exact KL certificate, rather than another pure-point class estimate.

## 3. Continuity of the three unnormalized local quantities

The following continuity proof treats a Boolean output edit of any probability delta, independently of the padding construction. Parseval and Cauchy--Schwarz imply total variation of the squared Fourier laws <=2sqrt(delta). At a fixed physical query, the corresponding joint law (fair physical child, residual spectral sample) has total variation <=2sqrt(delta) as well: if child edit probabilities are delta_+,delta_- then their average is delta, and the average of 2sqrt(delta_sigma) is at most 2sqrt(delta). For a one-point edit only one child changes, giving the even sharper sqrt(2delta), which is not needed.

If two laws on a binary Z and an arbitrary finite Y have TV e, write their common-part decompositions p=(1-e)r+e p', q=(1-e)r+e q'. Conditional entropy lies between the component average and that average plus h2(e); the residual conditional entropies lie in [0,1]. Therefore |H_p(Z|Y)-H_q(Z|Y)|<=h2(e)+e.

The SAME bound holds for the one-sided conditional entropy functional

    Lambda(p)=sum_y p(1,y)log2((p(0,y)+p(1,y))/p(1,y)).

To see it, each of its two single-Z components is a homogeneous concave perspective. Explicitly h(x,y)=y ln((x+y)/y) has Hessian

    -1/[y(x+y)^2] * [[y^2,-xy],[-xy,x^2]],

which is negative semidefinite for y>0, and the boundary follows by continuity. Both component Jensen gaps are nonnegative and their sum is the conditional entropy mixture gap I(L;Z|Y)<=h2(e), where L is the component label. Each residual component is between zero and one. The common-part argument thus applies to Lambda separately; no ambient alphabet factor is introduced. Applied to the full squared spectrum with Z the queried spectral bit, Lambda is exactly lambda_i.

For epsilon=2sqrt(delta)<=1/2, h2(e)+e is increasing over 0<=e<=epsilon. Let omega(epsilon)=h2(epsilon)+epsilon. Since B_i is a binary conditional entropy and J_i=1-H(physical sign|spectral remainder), we obtain

    |B_i(F)-B_i(g)|<=omega(epsilon),
    |lambda_i(F)-lambda_i(g)|<=omega(epsilon),
    |D_i(F)-D_i(g)|<=2omega(epsilon).                       (4)

The physical influence changes by at most 2delta for a one-point sign edit. Hence for any old relevant i with d_i(g)>2delta and any A_i in {B_i,lambda_i,D_i}, writing a_i=A_i(g)/d_i(g),

    |A_i(F)/d_i(F)-a_i|
       <= [c_A omega(epsilon)+2delta a_i]/[d_i(g)-2delta],  (5)

where c_B=c_lambda=1 and c_D=2. These bounds are for the same physical coordinate and are not a continuity argument for newly relevant zero-denominator coordinates.

## 4. Exact all-core admission operator limits

For each fixed core g, all its finitely many old relevant coordinates satisfy (5), so their ratios converge to their original values. All previously irrelevant coordinates obey (2). Thus, writing each minimum only over relevant coordinates and defining a minimum over the empty set as +infinity,

    lim_{q->infinity} min_i B_i(F_q)/d_i(F_q)
           =min(2, min_{i relevant in g} B_i(g)/d_i(g)),
    lim_{q->infinity} min_i lambda_i(F_q)/d_i(F_q)
           =min(1, min_{i relevant in g} lambda_i(g)/d_i(g)),
    lim_{q->infinity} min_i D_i(F_q)/d_i(F_q)
           =min(4, min_{i relevant in g} D_i(g)/d_i(g)).    (6)

The flipped old vertex may be any fixed vertex and the added coordinates may have any edited assignment: physical reflections preserve all quantities, and (2)--(5) are uniform in these choices. Thus the same limits hold even if the edited vertex varies with q at fixed g.

This is a universal obstruction to using single-point full-support admission to preserve existential high-erasure, high-lambda or high-drift witnesses above the caps (2,1,4). The construction DOES preserve the usual full-FEI H/I endpoint at fixed nonconstant g: TV<=2sqrt(delta) and the finite-alphabet entropy continuity bound |H(F_q)-H(g)|<=h2(epsilon)+epsilon*n tends to zero, while |I(F_q)-I(g)|<=2n delta. Consequently high H/I can survive while these three minimum coordinate ratios are lowered. There is no contradiction with FEI-equivalent selection: cheap coordinates can lead to uncertified descendants carrying the original entropy.

## 5. Exact terminal ownership after querying the added coordinates

Reveal the q added coordinates by any fair adaptive rule and stop before querying the original r-coordinate core. Write g^v for g with its value at the edited old vertex flipped. Precisely one of the 2^q assignments leaves g^v, and every other assignment leaves g. Thus

    E H(terminal)=(1-2^-q)H(g)+2^-q H(g^v),
    E I(terminal)=(1-2^-q)I(g)+2^-q I(g^v).                 (7)

The q original dummy labels each have root influence d after the edit. Their labelled influence accounts preserve expected influence until queried, so the exactly spent queried influence is qd. This is not the terminal data influence. The terminal entropy tends to H(g), independently of the vanishing edit and the cheaply queried new coordinates. In particular the complete terminal deficit is

    E[H(terminal)-C I(terminal)]
       =(1-2^-q)[H(g)-C I(g)]+2^-q[H(g^v)-C I(g^v)],      (8)

which retains the arbitrary core's possible violation. Dropping it would falsely turn root-local admission into a universal C019 payment.

## First unsupported universal line

No theorem here bounds the complete tree's cumulative charge or arbitrary terminal core entropy. An admission that preserves a high local witness must either prevent all newly relevant cheap directions or supply a child-slack/terminal reserve explaining why querying them leaves the original hard core. The shortest remaining universal obligation is a signed descendant/terminal correction for those cheap coordinates, not a root-only continuity or full-support assertion. Repeated padding and full-support censuses cannot pay that correction.
