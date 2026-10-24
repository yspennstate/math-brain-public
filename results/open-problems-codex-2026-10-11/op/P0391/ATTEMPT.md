# P0391 — research record and final result, 11 October 2026

## Final result: universal finite-second-moment theorem proved

FULL_PROOF.md gives the complete proof for every positional symmetric discipline in the source, empty initial state, a fixed service law with 0<E B<infinity and E B^2<infinity, and every real beta with r(1-rho_r)->beta. Writing m=E B, m2=E B^2 and h=m2/(2m),
Q_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.)-beta*.)/h
in the J1 topology. The proof establishes sup_{s<=r^2T}|W_r(s)-h Q_r(s)|/r ->0 for every finite T.

The missing positive-discrepancy estimate is resolved by retaining original-size marks, counting large-class upcrossings over whole regenerative cycles, and applying a summable dyadic Bernstein bound. The exact reward E Y=r*p_I*pi(f) eliminates the extra stationary-conditioning factor. Finite second moment alone makes each fixed large band vanish; no regular tail envelope is required. REFEREE.md checks every potentially failing step and both independent cycle diagnostics. GridBridge.lean passed Lean with no sorry or native_decide, checking only scalar interpolation, not the stochastic theorem. There is no remaining mathematical gap identified by this audit. No exact solution in print was verified; this is a new proof recorded here, not SOLVED_IN_LITERATURE.

The sections below retain earlier approaches and their limitations as a chronological research record. Statements of an unresolved endpoint in those earlier sections describe that stage and are superseded by FULL_PROOF.md.

## Exact target and source

Zwart, *Conjectures on Symmetric Queues in Heavy Traffic*, arXiv:2202.02366v1 (4 February 2022), pp. 1–2, defines a fixed array gamma(n,i)>=0, sum_i gamma(n,i)=1. A job at position i receives service at that rate; an arrival to n jobs inserts at i with probability gamma(n+1,i). Jobs shift on insertion/deletion. Arrivals are Poisson, independent service requirements have a fixed law B, m=E B in (0,infinity), m2=E B^2<infinity, lambda_r ->1/m and r(1-lambda_r m)->beta in R. Start empty. The target is process convergence in D([0,infinity)) with J1 topology to the common continuous reflected Brownian limit.

Put h=m2/(2m). The candidate is Gamma(sqrt(m2/m) Brownian(t)-beta*t)/h, where Gamma is reflection at zero. Its drift and variance rate are -beta/h and m2/(m*h^2). The source itself does not specify a topology in the problem sentence; J1 convergence to a continuous limit is the usual diffusion interpretation.

## Earlier intermediate results

The arguments below prove:

1. Under just the target second-moment assumption, for every gamma and T,
   sup_{t<=T} (Q_r(r^2 t)/r - W_r(r^2 t)/(h r))^+ ->0 in probability.
2. Under the stronger assumption E B^4<infinity, full uniform state-space collapse, and therefore the target process limit, for every gamma.
3. Under only E B^2<infinity, all finite-dimensional distributions converge to the common RBM, using result 1 and the known empty-start marginal identity.
4. Under the same second-moment hypothesis, scaled queue lengths satisfy compact containment and converge to the RBM as random elements of L1 on every bounded time interval. This weaker topology is not the requested J1 diffusion theorem.
5. Full J1 diffusion convergence for arbitrary gamma if P(B>x)=O(x^-2 (log x)^-2). In particular this covers every finite (2+delta)-moment law, delta>0, and also some laws with no moment above two. The proof below uses the empty start to discard large ORIGINAL service requirements directly, avoiding the stationary-conditioning cost for those events.
6. Strongest full-process special case obtained: E B^2<infinity together with P(B>x)=O(x^-2 (log x)^-1). The improved proof bounds the TOTAL work of large original arrivals rather than requiring their complete absence. The tail envelope is an additional assumption, not a consequence of finite second moment.

These intermediate arguments alone did not settle the finite-second-moment process theorem; the regenerative dyadic proof in FULL_PROOF.md now does. The fourth-moment case is a restriction on service laws, not a restriction to PS or LCFS. No novelty priority is claimed for these partial results.

## Standard inputs and their precise uses

For rho=lambda m<1 the symmetric queue has stationary joint law
pi_n(dx_1...dx_n)=(1-rho)rho^n product_i G_e(dx_i),
where G_e has density g(x)=P(B>x)/m. Thus, conditional on Q=n, remaining services are independent equilibrium residuals R with mean h. This is the full residual-service product form, stronger than queue-length insensitivity alone. It is the standard symmetric-queue invariant law (Kelly, *Reversibility and Stochastic Networks*, 1979); a balance verification is included below. We also use the classical compound-Poisson functional central limit theorem and continuity of one-dimensional reflection (Whitt, *Stochastic-Process Limits*, 2002). These inputs do not assert the conjectured queue-length limit.

The reflection map is Gamma(x)(t)=x(t)-min(0,inf_{s<=t}x(s)). For identical arrivals and service marks, work conservation gives exactly W=Gamma(sum_{j<=A(t)} B_j-t). Finite m2 gives centered input variance rate lambda_r*m2 ->m2/m and scaled drift r(lambda_r*m-1)->-beta. The compound-Poisson FCLT and reflection continuity therefore give W_r(r^2 .)/r => W_*, uniformly on compact intervals in the continuous-limit sense. In particular sup_{s<=r^2T+O(r)} W_r(s)/r is tight. This holds independently of gamma.

### Product-form balance verification

First suppose B>0 almost surely. Let f_n be bounded differentiable test functions on ordered positive residual vectors, with boundary condition f_n(x with x_i=0)=f_{n-1}(delete i). The generator is
L f_n = -sum_i gamma(n,i) partial_i f_n
 + lambda sum_i gamma(n+1,i) int [f_{n+1}(insert_i(x,b))-f_n(x)] F(db).
The residual density g has g(0+)=1/m and distributional derivative dg=-F(dx)/m. Integration by parts in coordinate i gives
int -partial_i f_n product g = (1/m) int f_{n-1}(delete i) product_{j!=i}g
 - (1/m) int f_n(x) F(dx_i) product_{j!=i}g.
After multiplying by pi's count weight p_n=(1-rho)rho^n, the negative service term at level n cancels the positive arrival insertion term at level n-1, since p_n/m=lambda*p_{n-1} and their gamma(n,i) coefficients agree. The positive boundary term at n+1 sums to p_{n+1}/m times the level-n integral, cancelling the negative arrival term lambda*p_n. At n=0 there is no service term and the same cancellation holds. Hence int Lf d pi=0. This is the standard invariant-law balance calculation for this nonexplosive piecewise-deterministic queue; the stationary product-form theorem provides invariance, not merely an assertion inferred from a formal generator identity. Nonexplosion holds because every departure removes one job and finitely many arrivals occur on finite intervals.

If P(B=0)>0, remove zero-service arrivals, which change the state only instantaneously. The retained process is Poisson with rate lambda*P(B>0), positive conditional service law, the same load rho, residual distribution G_e and h. All conclusions transfer. Thus proofs may use the positive-service formulation without losing the target case with zero masses.

### The deterministic estimate that bridges sampled times

Set D(t)=W(t)-h Q(t). On every interval [u,v],
D(v)>=D(u)-(v-u)-h [A(v)-A(u)].                         (B)
Indeed, workload loses at most v-u to service, and an arrival changes D by B-h>=-h; departures increase D by h. Summing yields (B), including simultaneous departures. This uses no lower bound on any service rate and no smoothness of gamma.

If u<=t<=v are consecutive grid points and the right side budget (v-u)+h[A(v)-A(u)] is at most b, (B) applied to [u,t] and [t,v] gives
D(u)-b <= D(t) <= D(v)+b.                             (C)
Both directions matter: a rapid sequence of departures cannot invalidate (C). For a negative D excursion use the preceding grid point; for a positive D excursion use the following grid point.

For physical grid spacing delta*r and horizon r^2 T+delta*r, there are O(r) intervals. Under bounded Poisson rates choose a constant L larger than an eventual upper bound on those rates. Chernoff's bound and a union bound give
P(max grid-interval arrival count > L*delta*r)->0 exponentially fast in r, for fixed delta>0. Thus b <= (1+hL)*delta*r on an event of probability tending to one. For any error threshold epsilon choose delta so (1+hL)*delta<epsilon/4.

## Proof of the stationary concentration estimates

Let R_i be independent with law G_e, S_n=sum_{i=1}^n R_i, S_0=0. Fix A>0 and epsilon>0. All constants below may depend on A,epsilon and the fixed service law, but not on gamma or r.

### Lower deviations: only E R=h<infinity is needed

There are c>0 and C_0<infinity such that, for all r>=1,
sup_n P(S_n<=Ar, S_n-hn < -epsilon*r) <= C_0 exp(-c*r).   (L)

To prove this, fix theta_0>0. Set kappa=-log E exp(-theta_0 R)>0; equilibrium residuals are strictly positive almost surely. Choose C>2 theta_0 A/kappa. For n>Cr, exponential Markov gives
P(S_n<=Ar)<=exp(theta_0 Ar-kappa n)<=exp(-kappa n/2).
For n<=Cr, finite mean and differentiation at zero give
log E exp[-theta(R-h)]=o(theta) as theta decreases to zero.
Choose theta>0 small enough that this logarithm is <=theta*epsilon/(2C). Markov gives
P(S_n-hn<-epsilon*r)<=exp(-theta*epsilon*r+n*theta*epsilon/(2C))
<=exp(-theta*epsilon*r/2).
Together these prove (L), including n=0 where the event is empty. In particular mixing these bounds over any distribution of n preserves the exponential bound.

### Upper deviations: finite E R^3 is sufficient

If E R^3<infinity then
sup_n P(S_n<=Ar, |S_n-hn|>epsilon*r)=o(r^-2).            (U)

For n>Cr use the large-n bound just proved (increase C if necessary). For n<=Cr put y=epsilon*r/K with fixed K=4 and Z_i=R_i 1_{R_i<=y}. The probability that any R_i>y is at most
Cr P(R>y)=o(r^-2),
because y^3 P(R>y)<=E[R^3 1_{R>y}]->0. On the complementary event S_n=sum Z_i, and since E Z_i<=h, the upper-deviation event implies sum(Z_i-E Z_i)>epsilon*r.

Here is the needed exponential bound, including its proof. For 0<=z<=y, the exponential series yields
exp(theta*z)-1-theta*z <= (z^2/y^2)(exp(theta*y)-1-theta*y).
Taking expectation, using 1+u<=exp(u), and multiplying by exp(-theta E Z_i) gives
E exp[theta(Z_i-E Z_i)] <= exp[(E Z_i^2/y^2)(exp(theta*y)-1-theta*y)].
By independence, with V=n E R^2<=Cr E R^2 and x=epsilon*r, optimizing theta=log(1+xy/V)/y gives
P(sum(Z_i-E Z_i)>x)
<= exp[-(V/y^2) H(xy/V)]
<= exp[-(x/y)(log(1+xy/V)-1)],
where H(u)=(1+u)log(1+u)-u>=u(log(1+u)-1).
This is bounded by e^K(1+epsilon^2*r/(KC E R^2))^-K=O(r^-4). Cases n=0 or V=0 have zero upper-deviation probability and are handled separately. Combining this with (L) proves (U), uniformly in n. Finally, direct Tonelli integration gives
E R^3 = (1/m) int_0^infinity x^3 P(B>x) dx = E B^4/(4m).
Thus the fourth service moment is exactly the moment used here.

## From stationary concentration to empty-start path estimates

First set lambda_r^0=(1-1/r)/m, r>1. Then rho_r^0=1-1/r. Let P_stat^r denote the stationary symmetric-queue path law and P_empty^r the path law starting empty at this rate. For any future-path event E,
P_empty^r(E)=P_stat^r(E | Q(0)=0)<=r P_stat^r(E).       (E)
This is exact: P_stat^r(Q(0)=0)=1/r, the empty state has no residual marks, and the future independent primitives have their usual distributions under conditioning. No coupling monotonicity in gamma is used.

Fix a physical grid of spacing delta*r, including a point just beyond r^2T. On the event sup_{s<=r^2T+delta*r} W(s)<=Ar, if a grid point violates D>=-epsilon*r, its stationary marginal belongs to the event in (L). There are O(r) points. Union bound and (E) give an empty-start probability O(r^2 exp(-c*r))->0. Equation (C) and the Poisson interval-count bound extend the grid estimate to all times, with arbitrarily small additional error by choosing delta small. Workload tightness removes the cutoff: the limsup probability of its failure can be made arbitrarily small by increasing A. Therefore
sup_{t<=T} (h Q_r^0(r^2t)-W_r^0(r^2t))^+/r ->0.       (OS)
This proof uses only E B^2<infinity.

For clarity, with F={sup_{s<=r^2T+delta*r}W(s)<=Ar}, the actual probability bound is
P_empty(F and some bad grid point)
<=r sum_j P_stat(W(t_j)<=Ar and D(t_j)<-epsilon*r).
The cutoff event is assessed for the empty-start process, whose workload supremum is tight. We never require an empty-start workload FCLT for the unconditioned stationary path. At each grid point the sum over all n is a probability-weighted mixture of the uniform residual-sum bound, so it contributes no extra factor of r.

If E B^4<infinity, replace (L) by (U). The stationary grid failure probability is O(r)*o(r^-2)=o(r^-1). Multiplying by r in (E) still gives o(1). Both sides of (C) apply, giving
sup_{t<=T} |W_r^0(r^2t)-h Q_r^0(r^2t)|/r ->0.         (SSC4)
The Poisson interval-count failure bound is applied directly under the empty-start law, or equivalently survives (E) because it decays exponentially. The extra final grid point is essential for bounding positive D near the horizon.

### Transfer to every real beta

For the target lambda_r with r(1-lambda_r m)->beta, lambda_r-lambda_r^0=O(1/r). On the primitive path up to H_r=r^2T+delta*r, change the Poisson rate and leave service marks and insertion randomizers untouched. The likelihood ratio of the target law with respect to the base law is
L_r=exp[(lambda_r^0-lambda_r)H_r]*(lambda_r/lambda_r^0)^{A(H_r)}.
The Poisson generating function gives exactly
E_0 L_r^2 = exp[H_r (lambda_r-lambda_r^0)^2/lambda_r^0],
which is bounded for large r. Cauchy–Schwarz therefore gives P_target(E)<=sqrt(E_0 L_r^2)*sqrt(P_0(E)). Every event whose probability tends to zero under the empty-start base law also tends to zero under the target law. This proves (OS) and (SSC4) for the full range beta in R, including critical and supercritical sequences. The change of measure is on a finite horizon and asserts no global stationary law in those cases.

### Consequence under the fourth-moment hypothesis

Combining (SSC4) with the workload FCLT gives, for every work-conserving symmetric gamma,
Q_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.)-beta*.)/h.
The limit is continuous, and uniform-on-compacts error tending to zero transfers J1 convergence by the usual convergence-together theorem. This proves the complete fourth-moment special case, without restricting gamma to PS or LCFS.

The second-moment theorem (OS) says that any candidate queue-length subsequential limit cannot exceed the appropriately scaled workload at any time, in the uniform positive-error sense. It does not rule out short downward excursions of queue length below its workload proxy.

## Finite-dimensional convergence under exactly the target moment hypothesis

First work at the subcritical reference rate lambda_r^0=(1-1/r)/m, so beta=1. Use the fixed-time identity stated in Zwart, p. 2, citing Fralix and Zwart (2011): from an empty start the law of Q_r^gamma(s) is independent of gamma for each deterministic s. The already established PS diffusion theorem under finite second moment implies, for every fixed t at this reference rate, Q_r^gamma(r^2t)/r => W_*^0(t)/h. Only the subcritical PS theorem is needed here; we do not assume an extension of that paper to supercritical rates.

We can strengthen this reference-rate marginal conclusion using (OS). Fix t. The pair (Q_r(r^2t)/r, W_r(r^2t)/(hr)) under the reference-rate law is tight, and any joint subsequential limit (X,Y) satisfies X<=Y almost surely by (OS). Both marginal laws equal the law of W_*^0(t)/h. A bounded strictly increasing function, for example arctan on the nonnegative reals, gives E[arctan Y-arctan X]=0, although the integrand is nonnegative and strictly positive wherever X<Y. Thus X=Y almost surely. Every subsequential limit of the difference is zero, so
Q_r(r^2t)/r-W_r(r^2t)/(hr) ->0 in probability.
The finite-horizon likelihood-ratio bound above transfers this vanishing pointwise-difference probability to every target rate sequence with real beta. For any finite list of deterministic times, union bounding these difference probabilities under the target law and using its workload vector convergence proves convergence of the queue-length vector to the corresponding common RBM vector with the target drift. This proves ALL finite-dimensional distributions for arbitrary gamma under the exact finite-second-moment assumption and every real beta.

There is also an occupation-time consequence. For fixed epsilon,T>0, Fubini and bounded convergence give
E int_0^T 1_{|Q_r(r^2t)/r-W_r(r^2t)/(hr)|>epsilon} dt ->0,
since the integrand's expectation tends to zero at each fixed t. Hence the time spent outside any fixed-width workload band tends to zero in probability. This is weaker than uniform collapse and permits narrow downward excursions.

### Compact containment and L1 convergence

Let q_r(t)=Q_r(r^2t)/r and w_r(t)=W_r(r^2t)/(hr). The one-sided estimate gives
sup_{t<=T} q_r(t) <= sup_{t<=T} w_r(t)+sup_{t<=T}(q_r(t)-w_r(t))^+.
The first term is tight by the workload FCLT and the second tends to zero in probability. Thus sup q_r is tight, which is compact containment of the nonnegative state coordinate. Consequently M_r=sup_{t<=T}|q_r(t)-w_r(t)| is tight too.

Write O_r(epsilon)=int_0^T 1_{|q_r-w_r|>epsilon}dt, which tends to zero in probability by the preceding paragraph. Pathwise,
int_0^T |q_r(t)-w_r(t)|dt <= epsilon*T+M_r*O_r(epsilon).
For any eta>0 choose epsilon so epsilon*T<eta/2 (T=0 is trivial). Given zeta>0, tightness permits a fixed K with limsup P(M_r>K)<zeta. Then
limsup P(int |q_r-w_r|>eta)
<=zeta+limsup P(O_r(epsilon)>eta/(2K))=zeta.
Letting zeta decrease to zero proves that the L1 error tends to zero in probability. The continuous workload limit and the workload FCLT imply w_r converges in distribution in L1([0,T]); convergence together therefore gives the same L1-distributional limit for q_r. Applying the estimates on every integer T gives the corresponding L1-local conclusion. These spaces identify functions that agree almost everywhere; this statement deliberately does not assert J1 tightness.

## Stronger full diffusion theorem by truncating original arrivals

Assume that for all sufficiently large x,
P(B>x)<=C_B/(x^2 (log x)^2).                            (LT)
This condition implies E B^2<infinity by the tail integral. It is weaker than the existence of any fixed moment above two. We now prove uniform two-sided collapse and the full common RBM limit for EVERY symmetric gamma under (LT).

Fix A,epsilon,T>0. Continue at the subcritical reference rate, retaining the same physical grid of spacing delta*r. For large r define
K_r=3 log r / log log r,    y_r=epsilon*r/K_r.
Then y_r tends to infinity and log y_r / log r tends to one. Let G_r be the event that every original service requirement arriving up to H_r=r^2T+delta*r is <=y_r. Starting empty, every remaining service at every time up to H_r is <=y_r on G_r. Importantly, this is a direct statement about the empty-start primitive arrivals, not a stationary residual-tail union bound. By Poisson marking,
P_empty(G_r^c)<=lambda_r^0 H_r P(B>y_r)
<=C_T r^2 C_B/[y_r^2 (log y_r)^2]
=(C_T C_B/epsilon^2) K_r^2/(log y_r)^2 ->0.              (G)

For a stationary residual R set Z=R 1_{R<=y}. Its truncated second moment is
v_y=E[R^2 1_{R<=y}]=(1/m) int_0^y x^2 P(B>x) dx.
Split this integral at sqrt(y). On [0,sqrt(y)], x^2 P(B>x)<=E B^2, so the contribution is at most E B^2 sqrt(y). On [sqrt(y),y], for sufficiently large y, (LT) bounds the integrand by 4C_B/(log y)^2. Consequently there is a fixed C_R such that
v_y<=C_R*y/(log y)^2 for all sufficiently large y.      (V)

As in the proof of (L), choose C so that n>Cr and S_n<=Ar has exponentially small probability, uniformly in n. For n<=Cr, on the event max_i R_i<=y_r the upper-deviation event S_n-hn>epsilon*r implies
sum_i (Z_i-E Z_i)>epsilon*r,
since E Z_i<=h. The exponential bound already proved above applies with V=n*v_{y_r}<=C C_R r y_r/(log y_r)^2, x=epsilon*r and y=y_r. For n=0 the event is empty. Thus its probability is at most
exp[-K_r {log(1+c (log y_r)^2)-1}],  c=epsilon/(C C_R)>0.
The exponent divided by log r tends to -6. In particular the probability is <=r^-3 for all sufficiently large r, uniformly in n<=Cr. The lower-deviation event retains the exponential bound (L). Mixing over stationary Q therefore yields
P_stat(W<=Ar, |W-hQ|>epsilon*r, max residual<=y_r)
<=r^-3+C_0 exp(-c_0*r).                                (TC)

Let F_r={sup_{s<=H_r}W(s)<=Ar}. Condition the stationary path on Q(0)=0. On G_r every sampled state's residual maximum is <=y_r. Hence
P_empty(F_r and G_r and a bad grid point)
<=r sum_j P_stat(W(t_j)<=Ar, |D(t_j)|>epsilon*r,
                max residual at t_j<=y_r)
<=O(r^2)[r^-3+C_0 exp(-c_0*r)] ->0.
There is NO conditioning factor r in (G): that bound is computed directly under the empty-start law. The only r factor is in the displayed stationary grid estimate. This separation is the essential improvement over (U).

Use (G), workload tightness to remove F_r, and the deterministic grid interpolation (C) with delta chosen small, exactly as before. It follows that
sup_{t<=T}|W_r^0(r^2t)-hQ_r^0(r^2t)|/r ->0.
The already proved finite-horizon change of arrival-rate measure transfers this to every real beta. The workload FCLT then proves the full common RBM limit in J1 for arbitrary gamma under (LT).

### Consequences and strict limits of this extension

If E B^{2+delta}<infinity for some delta>0, Markov's inequality gives P(B>x)<=E B^{2+delta}/x^{2+delta}, which implies (LT), because x^-delta (log x)^2 is bounded for x sufficiently large. Thus every such law is covered; the earlier fourth-moment argument is subsumed but retained as a fully checked intermediate proof.

(LT) also covers a genuine finite-second-moment boundary class. For example a survival function equal to C/(x^2 (log x)^2) for x sufficiently large has finite second moment and infinite p-th moment for every p>2. Choose any monotone continuation on a bounded interval to make a probability law. The second-moment tail integral is proportional to int dx/[x (log x)^2]<infinity, whereas for p>2 the p-th moment integral is proportional to int x^{p-3}/(log x)^2 dx=infinity.

The full finite-second-moment class is still larger: tails proportional to 1/[x^2 (log x)^{1+eta}], with 0<eta<1, have finite second moment but violate (LT). The direct arrival bound (G) with the chosen y_r no longer tends to zero for these laws: its leading order is (log r)^{1-eta}/(log log r)^2. This is a limitation of this truncation scale, not a counterexample to the diffusion theorem. No claim about those excluded laws is made beyond the one-sided, finite-dimensional and L1 results already proved.

## Further improvement: bound total large-arrival work

Assume E B^2<infinity and, for all sufficiently large x,
P(B>x)<=C_B/[x^2 log x].                               (LT1)
Unlike (LT), (LT1) alone need not imply finite second moment, so BOTH assumptions are retained. We prove full uniform collapse and J1 convergence for every gamma under these hypotheses.

Fix A,epsilon,T>0. At the same reference rate and horizon H_r, put
K_r=10 log r/log log r,    y_r=epsilon*r/K_r,
and let J_r=sum_{j<=A(H_r)} B_j 1_{B_j>y_r}. Starting empty, at every time s<=H_r,
U_r(s):=sum_{jobs present at s} R_j(s) 1_{R_j(s)>y_r} <=J_r.
Indeed every present job arrived after time zero, R_j(s)<=B_j, and R_j(s)>y_r implies B_j>y_r. This is a deterministic pathwise bound with no assumptions on gamma.

The tail-integral identity and (LT1) imply, for sufficiently large y,
E[B 1_{B>y}]=y P(B>y)+int_y^infinity P(B>x)dx
<=C_B/(y log y)+C_B/(y log y)=2C_B/(y log y),
where the integral bound uses log x>=log y. Therefore
E_empty[J_r/r]=lambda_r^0 H_r E[B 1_{B>y_r}]/r
<=C_T r/(y_r log y_r)
<=C_T' K_r/(log y_r) ->0.
Markov's inequality gives P_empty(J_r>epsilon*r/2)->0.   (JW)
Again this is computed directly under the empty-start law; it carries no stationary conditioning factor.

For R with equilibrium residual law, the same split at sqrt(y) gives
v_y=E[R^2 1_{R<=y}]
<=(1/m)[E B^2 sqrt(y)+2C_B*y/log y]
<=C_R*y/log y for sufficiently large y.                (V1)

Let n<=Cr, with C chosen from the high-n workload lower-tail bound. Write Z_i=R_i 1_{R_i<=y_r}. The event sum Z_i-hn>epsilon*r/2 implies sum(Z_i-E Z_i)>epsilon*r/2 since E Z_i<=h. Apply the already proved exponential estimate with x=epsilon*r/2, y=y_r and
V=n v_{y_r}<=C C_R r y_r/log y_r.
It bounds the probability by
exp[-(K_r/2){log(1+c log y_r)-1}], c=epsilon/(2C C_R)>0.
The exponent divided by log r tends to -5, so the bound is <=r^-3 for all sufficiently large r, uniformly in n<=Cr. For n=0 the event is empty. When n>Cr and S_n<=Ar, the probability is exponentially small by the earlier lower-tail argument. Thus the stationary probability
P_stat(W<=Ar, sum_i R_i 1_{R_i<=y_r}-hQ>epsilon*r/2)
<=r^-3+C_0 exp(-c_0*r).                                (ZC)
This estimate does NOT impose max residual<=y_r.

Now work under the empty-start law. On J_r<=epsilon*r/2, if a sampled D=W-hQ exceeds epsilon*r, then
sum_i R_i 1_{R_i<=y_r}-hQ
=D-sum_i R_i 1_{R_i>y_r}>epsilon*r/2.
On the workload cutoff, condition the stationary path on being empty initially and bound this truncated-sum event at each grid point by (ZC). There are O(r) points and the conditioning cost is r. Hence the positive-D grid failure probability, intersected with both cutoffs, is O(r^2)[r^-3+exp(-c_0*r)]->0. The negative-D grid failure retains the exponential estimate (L).

Remove the J cutoff by (JW) and the workload cutoff by its empty-start tightness, then use both sides of deterministic interpolation (C). This proves two-sided uniform state-space collapse under (LT1). The finite-horizon likelihood ratio transfers it to every real beta, and the workload FCLT proves the full common RBM limit in J1 for every gamma.

### Scope and a checked excluded boundary case

Every finite (2+delta) moment implies (LT1). The new theorem also covers finite-second-moment tails proportional to 1/[x^2 (log x)^{1+eta}], for every eta>0, and even tails proportional to 1/[x^2 log x (log log x)^2]. In the last example the second moment is finite because int dx/[x log x (log log x)^2]<infinity. These may have no moment above two. They were outside the preceding (LT) theorem, but are now included; its previous limitation described the earlier truncation scale only.

There is a simple finite-second-moment corollary. If the WEIGHTED tail f(x)=x^2 P(B>x) is eventually nonincreasing, then (LT1) follows from finite second moment. Indeed, for sufficiently large x,
(log x) f(x)/2 <=int_{sqrt(x)}^x f(u)du/u
<=int_0^infinity u P(B>u)du=E B^2/2.
Hence f(x)<=E B^2/log x. This assumption is about the weighted tail, not the survival function itself (which is always nonincreasing). No claim that all finite-second-moment laws satisfy it is made.

Finite second moment does NOT imply (LT1). Here is an explicit excluded law. Let b_k=exp(k^4), p_k=1/(4 k^2 b_k^2), k>=1. Put probability p_k at b_k and all remaining probability at 1. The probabilities sum to less than one because sum p_k<=sum 1/(4k^2)<1. The second moment is
(1-sum p_k)+(1/4)sum_{k>=1}1/k^2<infinity.
At x_k=b_k/2, however,
x_k^2 log(x_k) P(B>x_k)
>= (k^4-log 2)/(16 k^2) ->infinity.
So no constant in (LT1) exists. This is a counterexample to the implication from finite second moment to our extra tail assumption, NOT a counterexample to P0391. Arbitrary such sparse finite-second-moment laws remain outside the full-process proof.

The improved argument bypasses the earlier Pareto stationary-concentration obstruction: large residuals created by pre-time-zero stationary jobs are irrelevant under the empty start, and large future arrivals are controlled through their total original work. The unresolved step is to obtain adequate pathwise control without (LT1), not to revive the false o(r^-2) untruncated stationary estimate.

## Historical gap before the regenerative dyadic proof

The gap described in this section is resolved by FULL_PROOF.md, sections 4–5; it is retained to distinguish the earlier failed truncation approach from the completed proof.

The positive part of W-hQ is not yet controlled uniformly under ONLY E B^2<infinity. It is controlled by the preceding theorem under the additional (LT1) tail envelope, which is strictly stronger for general laws. Without that envelope the present proof does not simultaneously make total large-arrival work small and truncated stationary concentration fast enough for the O(r) grid and the r conditioning factor. No unproved truncation, marginal-to-process inference, or interchange of limits is being claimed.

### A rigorous obstruction to simply reusing the fourth-moment concentration rate

Take B=(2/3)X, where P(X>x)=x^-3 for x>=1. Then m=1, E B^2=4/3, h=2/3, and E B^4=infinity. Its residual law satisfies P(R>x)=(4/27)x^-2 for x>=2/3.

Fix c,epsilon>0 and n=floor(c*r). For each j let E_j be the event that R_j lies between 2epsilon*r and 3epsilon*r, every other residual is <=2epsilon*r, and the sum of the others differs from h(n-1) by at most epsilon*r/2. These E_j are disjoint, since exactly one residual exceeds 2epsilon*r. The probability of the condition on the other residuals tends to one: their sum has the finite-mean law of large numbers, and (n-1)P(R>2epsilon*r)=O(1/r)->0. Independence gives
P(union_j E_j)=n * (5/(243 epsilon^2 r^2)) * (1-o(1))
~5c/(243 epsilon^2 r).
On E_j, S_n-hn is between 1.5epsilon*r-h and 3.5epsilon*r-h. For large r it exceeds epsilon*r and S_n<=(hc+4epsilon)r. Therefore the conditional stationary concentration probability appearing in (U), with A=hc+4epsilon, is at least a constant times 1/r. It is not o(r^-2).

This is a counterexample to the required concentration RATE under just finite second moment, not a counterexample to the queueing diffusion conjecture. A successful proof needs a different way to count or control the rare upper-residual events along an empty-start path.

## Hostile-referee checklist

- Definition: insertion probabilities must match positional service shares. The generator cancellations use exactly that matching. An arbitrary work-conserving discipline lacking it is outside the theorem.
- Initial condition: conditioning is on a truly empty stationary state. Its probability 1/r is included explicitly, not silently treated as bounded below.
- Number of grid points: physical spacing is delta*r, not a constant and not delta*r^2. It gives O(r) points, which together with the conditioning factor accounts for the required o(r^-2) stationary error rate.
- Fast departures: they increase D. Inequality (C) uses the preceding grid point for negative D and the following grid point for positive D; there is no assumed bound on instantaneous departure counts.
- High queue lengths: the workload cutoff does not imply a deterministic queue-length cutoff. The n>Cr region is bounded separately by an exponential lower-tail estimate.
- Finite-moment uses: finite E B^2 gives finite E R and the one-sided bound. Finite E B^4 gives finite E R^3, used in nP(R>epsilon*r/K)=o(r^-2). The exact little-o is essential at the fourth-moment boundary.
- Upper concentration: the exponential truncation estimate uses E R^2 and nonnegative bounded Z_i; it does not require an exponential moment of R.
- beta<=0: no stationary law is used for the target rate. The likelihood ratio is evaluated at a subcritical reference rate and its second moment is bounded on each finite scaled horizon.
- Marginals versus paths: common marginal laws are used only after proving a joint ordering with workload. They yield finite-dimensional convergence, not tightness.
- Topology: the earlier moment and tail-restricted arguments alone did not yield the universal J1 theorem. FULL_PROOF.md now proves uniform collapse and J1 convergence under exactly finite second moment.
- Compact containment and L1: both follow from the proved one-sided estimate and the finite-dimensional argument. They do not eliminate short, narrow downward excursions and are explicitly distinguished from J1 convergence.
- Original-arrival truncation: in the improved proof the direct bound concerns total work J_r brought by large original service requirements, not the maximum stationary residual. Empty start is essential for the pathwise U_r<=J_r bound. The probability of J_r being large is bounded directly with no factor r; only the truncated stationary-snapshot estimate pays the conditioning factor.
- Tail scope: the final full-process theorem retains BOTH finite second moment and (LT1). The tail envelope alone may have infinite second moment. The sparse atomic example proves that the envelope is not a consequence of the target moment assumption. Earlier limitations of the stronger (LT) truncation scale are superseded for logarithmic tails, not for all finite-second-moment laws.
- Simulations: checks.py runs 288 empty-start paths, with deterministic services or the above Pareto law, for PS, middle-position-only service, alternating end-position service, and equal end shares. It tests matching insertion and service rules and inequality (B). Floating-point deviations of the inequality below zero were at most 3.6e-15. These are diagnostics, not probabilistic proofs.
- Lean: GridBridge.lean checks only the deterministic scalar interpolation implication (C), not the stochastic arguments. Its check result is recorded separately in lean_check.txt; no sorry or native_decide is used.

At this earlier stage, the remaining task was to exclude narrow downward queue-length excursions under finite second moment; FULL_PROOF.md now resolves it. All finite-dimensional limits and the one-sided uniform bound are already identified; the positive workload-minus-queue discrepancy is the precise gap.

### Why the established weak conclusions do not imply J1 convergence

Here is an abstract deterministic example, not a queueing counterexample. On [0,1] let w(t)=t, tau_n=1/2+3/n (n>=8), phi_n(t)=max(0,1-n|t-tau_n|), and x_n(t)=t(1-phi_n(t)). Both paths start at zero and are continuous and nonnegative; x_n<=w everywhere. Their suprema are bounded by one. For each fixed t!=1/2, the support of phi_n eventually avoids t; it also avoids t=1/2 because |tau_n-1/2|=3/n>1/n. Thus every deterministic-time vector of x_n converges to that of w. Also int_0^1|x_n-w|dt<=2/n. Nevertheless |x_n(tau_n)-w(tau_n)|=tau_n>=1/2. Hence there is no uniform convergence and no J1 convergence to the continuous path w (J1 convergence to a continuous path implies uniform convergence). The discrepancy d_n=w-x_n even satisfies d_n(v)>=d_n(u)-n(v-u): its derivative is bounded below by -n wherever it exists, and it is absolutely continuous. This is the order of the scaled service-only budget in (B). The example satisfies all four weak properties proved above and shows why they cannot be promoted to the requested result without a further tightness argument. It does not purport to realize the queueing dynamics or their Poisson input law.
