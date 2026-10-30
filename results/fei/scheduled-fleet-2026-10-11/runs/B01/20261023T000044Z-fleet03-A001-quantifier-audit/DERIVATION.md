# Independent source prescriptions with one unchanged ancestor account

Full FEI remains open. This result concerns the fixed neutral AND3/Maj3 fixture, two real source-reference parameters, and all later no-reset physical histories. Every cost includes the empty atom and every full terminal reference.

## Actual source, old costs and the new prescription

On six data bits let b=+1 iff y0=y1=y2=0, and c=b except c(0)=-1. Let F choose b or c using the balanced fresh Maj3 encoder, on low physical bits 0,1,2. Both core influences are 3/4, so the original quota is 3. Query the weak data bit y3, physical bit6, keeping both outcomes with reach1/2. Its on-child, y3=0, has five remaining data bits and three encoder bits; the off-child is b restricted to those five data bits.

Begin with the actual root spectrum P. Marginalize the queried spectral coordinate to m. The previously specified A004 reset in BOTH children is Rold=7m/8+U256/8. The executed erasure is B=B_y3(F). Keep the original whole-frontier liability

    C_old=B+[CE(p_on,Rold)+CE(p_off,Rold)]/2.

This has already paid the root increment H(F)-T0 and the first reset. Neither is discarded when the next reset is booked.

Now prescribe a reference from the SOURCE geometry, independently of Rold. On five data bits take g=1-2A3, s=1/8, mu=3/4 and Pg its explicit squared spectrum. Define V(empty)=9/16 and V(T)=7/496 for all 31 nonempty data sets. For every REAL lambda in [0,1], define

    R_lambda=(1-lambda)Pg+lambda V,
    e=1/32,
    Rprime_lambda(T)=(1-e/s)R_lambda(T)
                     +(e/s)mu*1_empty(T)+2e/32.           (1)

All these data references are normalized. Indeed their total mass is 1-e/s+(e/s)mu+2e=1 because 1-mu=2s. They are strictly positive after (1).

The on-child, up to an irrelevant output sign, is g+2 psi D, where D is the data-origin indicator (t=1/32) and psi is the negative-Maj3 event, with mean p=1/2. For its actual joint law p_on(S,T), let q(T)=sum_S p_on(S,T). Direct expansion and Parseval give

    q(T)=ghat(T)^2+2e ghat(T)+2et,   e=2pt.

Each q(T)>0, checked explicitly; equivalently the point-edit private event supplies positive data energy at every set. Define the complete joint reference

    Q_lambda(S,T)=Rprime_lambda(T)*p_on(S,T)/q(T).        (2)

The conditional encoder kernel in (2) is supplied by this explicit controller/source construction, not by the inherited reference. This extends the negative-cell data-floor formula to this one known private event; it asserts no arbitrary-core construction. On active nonempty sets ghat=-2s, on dummy-containing sets ghat=0, and at empty ghat=mu. Substitution in (1) shows Rprime_0=q and therefore Q_0=p_on exactly.

For the retained off-child independently prescribe

    Qoff_alpha(S,T)=R_alpha(T)*1_{S=empty},              (3)

with a second REAL parameter alpha. Its actual spectrum is Qoff_0=Pg times the encoder-empty atom. These are normalized COMPLETE laws, including reference-only data atoms. They need not have full support: finiteness requires positivity on the ACTUAL occupied atoms. Both endpoint references satisfy it. In (2), 96 inherited-positive atoms become reference-zero, but every one is actual-zero. A global domination bound over every inherited atom would be infinite here; the actual correlated reset cost is finite. No invalid zero logarithm is evaluated.

## Exact signed ledger, without renewing a bank

For p at a reset, the signed price is Z=CE(p,Qnew)-CE(p,Qold). For the two prescribed child resets write Z_on(lambda) and Z_off(alpha). Their complete liability is

    C(lambda,alpha)=C_old+Z_on(lambda)/2+Z_off(alpha)/2
       =B+CE(p_on,Q_lambda)/2+CE(p_off,Qoff_alpha)/2.      (4)

The second line is exact cancellation of signed reference changes after booking every old debit. It is not dropping the old reset or treating an executed erasure as a pending reservation. The source checker verifies both expressions independently, as well as the original S4-(H(F)-T0) ledger. Resetting only the on-child instead leaves the off-child at Rold, with liability C_old+Z_on(lambda)/2.

For any actual queried node with law p and incoming reference R, let m be the erased marginal and r the same marginal of R. Exact amplitude restriction gives the mean child law m. Therefore

    B_i(p)+mean CE(p_child,r)
      =CE(p,R)-[D(p||R)-D(m||r)] <= CE(p,R).             (5)

The bracket is conditional KL, nonnegative on finite laws; support positivity follows from p<<R and marginalization. Finite adaptive-tree induction applies (5) separately below both retained children. Thus any frontier liability <=3 pays every later adaptive stopping policy using those reference marginals and BOTH complete terminal costs. No separately allocated nonnegative bank is claimed in each child. No further fresh reset is funded by (5) alone.

## Continuum parameters, not a grid conclusion

The laws Q_lambda and Qoff_alpha are affine in their respective parameters. Cross-entropy with a fixed actual law is convex in a positive reference, since -log is convex. Positivity on the actual support holds throughout the closed parameter ranges, including zero. Hence (4) is convex in each parameter; its maximum over a rectangle is bounded by its corner values. Moreover each endpoint family starts at the actual law, so each associated KL is minimized at parameter0. A convex function with a minimum at0 is nondecreasing on [0,1]. It is enough to certify the upper-right corner.

Exact rational log intervals establish the following:

* On-child reset only: ALL lambda in [0,1] leave more than 0.201237 bits of the ORIGINAL quota3, with the off-child still at Rold.
* Two independent source resets: ALL lambda in [0,1] and alpha in [0,3/4] leave more than 0.04217 bits of that SAME quota. The worst corner is (1,3/4).
* The wider assertion allowing both parameters1 is FALSE: C(1,1)>3+0.153188 bits. These are actual Boolean terminals and complete normalized references. The failure is a reference-payment failure, not a counterexample to FEI.

Thus the retained off-branch can receive one independently prescribed reset, provided its source spread is admitted against the DIMINISHED original reserve. Symmetric maximal spreading on both branches exceeds that reserve. The continuum conclusion uses convexity and exact endpoint certificates; the quarter-parameter evaluations are diagnostics.

## First unpaid universal implication

The universal gap is still an influence-priced source construction and a hereditary bound on prescribed reset excess after arbitrary histories. This result uses one explicit root whose original quota is already paid; its reference kernel is known from the Maj3/point geometry. After the two admitted resets, arbitrary no-reset continuations are closed by (5). The next unpaid physical step is an actual source-dependent data query followed by a fresh prescribed canonical reset, with old on/off prices, real conditional-KL refund and both full terminals retained. No fresh S4 and no second use of the original 0.555796-bit admission margin is available. In particular the failed (1,1) endpoint prevents promoting the admitted rectangle to unrestricted branchwise canonical spreading.
