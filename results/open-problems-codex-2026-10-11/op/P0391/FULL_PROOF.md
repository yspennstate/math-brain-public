# Complete proof of P0391 — finite second moment

This file proves the empty-start universal symmetric-queue diffusion theorem by a regenerative dyadic argument. The completed hostile audit is in REFEREE.md. Earlier intermediate results are retained in ATTEMPT.md. Standard inputs are the symmetric-queue stationary product form and the compound-Poisson workload FCLT; no queue-length diffusion theorem is assumed in this proof.

## Theorem and notation

Let B be a fixed nonnegative service law with 0<m=E B<infinity and m2=E B^2<infinity. Arrivals have Poisson rate lambda_r, independently marked by iid requirements B. At queue size n a fixed symmetric rule gamma assigns service shares gamma(n,i)>=0 summing to one, and inserts new arrivals with the matching probabilities gamma(n+1,i). Start empty. If r(1-lambda_r m)->beta in R, then in D([0,infinity)) with J1 topology,
Q_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.)-beta*.)/h,
where h=m2/(2m).

Zero-service arrivals may be thinned, as explained in ATTEMPT.md. They restore all positions on immediate deletion and do not change the right-continuous state. The positive conditional law and retained Poisson rate have the same load, h and variance ratio m2/m. Accordingly assume B>0 almost surely throughout the proof.

We first prove uniform state-space collapse at the reference rate lambda_r^0=(1-1/r)/m, r>1, so rho_r^0=1-1/r. All path estimates below refer to that rate until the final change of measure. Constants may depend on a finite horizon T, error tolerances and the fixed law, but never on gamma or r. The original requirement B_i is retained as an immutable label of each present job, with remaining service R_i in (0,B_i].

## 1. Stationary augmented product law and regeneration

The standard symmetric-queue product law, with original requirements retained, is
pi_n(d(b_1,x_1)...d(b_n,x_n))=(1-rho)rho^n product_i H(db_i,dx_i),
H(db,dx)=F(db) 1_{0<x<b} dx/m.                          (1)
H is a probability measure because int b F(db)=m. Its residual marginal has density P(B>x)/m. For every original-size class I,
E_H[X_I]=E[B^2 1_{B in I}]/(2m),
where X_I=x 1_{b in I}; if I is contained in (a,2a], then 0<=X_I<=2a and E_H[X_I^2]<=2a E_H[X_I].

Here is the augmented balance check, valid also for atomic F. For a bounded smooth boundary-compatible test function f_n, the service term in a job's coordinate integrates as
int F(db)/m int_0^b -partial_x f_n(...,(b,x),...) dx
=int F(db)/m [f_{n-1}(delete that job)-f_n(...,(b,b),...)].
The negative endpoint term at level n, weighted by gamma(n,i), cancels the arrival-insertion term from level n-1 because p_n/m=lambda p_{n-1}. The positive deletion term from level n+1 sums its gamma(n+1,i) coefficients to one and cancels the negative arrival term at level n. Thus (1) is the usual invariant product form for the augmented symmetric queue, not an assumption of iid residuals along a transient path. We use the standard product-form invariance theorem; this computation verifies its measure, marks and matching insertion rates.

The empty-to-empty cycle consists of an exponential idle interval followed by a busy period. Its mean is
E C_r=1/[lambda_r^0(1-rho_r^0)]=r/lambda_r^0.            (2)
To check finiteness and the formula without relying on gamma, the busy-period workload path is the same for every work-conserving discipline. In an FCFS realization its total service is the total progeny work of a subcritical mixed-Poisson branching tree: each job of service b has Poisson(lambda*b) children. Generation k has expected size rho^k and expected work m rho^k. Tonelli gives mean busy duration m/(1-rho), and subcritical extinction gives a finite busy cycle almost surely. Adding mean idle duration 1/lambda proves (2). Regeneration at empty makes cycles iid. The augmented stationary law (1) is the regenerative stationary occupation law; uniqueness follows from the recurrent empty regeneration state and finite mean cycle length.

For a marked class I with p_I=P(B in I) and any nonnegative state predicate f<=1, let Y_I(f) count arrivals with B in I and f(prearrival state)=1 during one whole cycle. Poisson compensation and regenerative occupation give the exact identity
E Y_I(f)=lambda_r^0 p_I E int_0^{C_r} f(X(s-))ds
=lambda_r^0 p_I E C_r pi_r(f)=r p_I pi_r(f).             (3)
No extra factor for conditioning on an empty start appears in (3). Compensation at the integrable cycle stopping time follows by bounded stopping and L2 uniform integrability: the marked counting martingale stopped at C_r has expected quadratic variation at most lambda_r^0 p_I E C_r<infinity. Event times have zero Lebesgue measure, so the occupation identity applies to prearrival states as well.

## 2. Workload, compact containment, and number of cycles

Work conservation gives W_r=Gamma(sum_{j<=A_r(.)}B_j-identity). The classical compound-Poisson FCLT and continuity of reflection give
W_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.)-identity)
at the reference rate, and convergence of the associated scaled idle regulator I_r(r^2 .)/r. In particular workload suprema and I_r(r^2T)/r are tight.

The finite-second-moment one-sided collapse, proved in the appendix below, uses only the residual marginal of (1) and reads
sup_{s<=r^2T}(h Q_r(s)-W_r(s))^+/r ->0.                 (4)
For completeness, the ingredients are: exponential lower deviations of iid nonnegative residuals with mean h; a workload cutoff handling n>Cr; stationary conditioning cost P_pi(Q(0)=0)^-1=r; O(r) deterministic time samples separated by delta*r; and the pathwise bridge W(v)-hQ(v)>=W(u)-hQ(u)-(v-u)-h[A(v)-A(u)]. Every detail appears in ATTEMPT.md, including the lower-deviation proof and all constants. It follows directly from (4) and workload tightness that
sup_{s<=r^2T} Q_r(s)/r is tight.                        (5)

Let N_r(t) count busy-period starts by time t. Since B>0 and we start empty,
N_r(t)=int_0^t 1_{W_r(s-)=0} dA_r(s).
Its compensator is lambda_r^0 I_r(t), where I_r(t)=int_0^t 1_{W_r(s)=0}ds is unused service capacity. The martingale M_r=N_r-lambda_r^0 I_r has predictable quadratic variation lambda_r^0 I_r. Localize at the first time I_r reaches a*r. At this stopped time horizon the variance is at most lambda_r^0 a*r, so Chebyshev gives M_r(r^2T)/r->0 after first taking r to infinity and then a to infinity, using tightness of I_r/r. Therefore
N_r(r^2T)/r is tight.                                 (6)
This is a workload argument, not an assumed queue-length diffusion limit. The same conclusions hold on r^2T+delta*r by bounding that horizon by r^2(T+1) for large r.

## 3. Uniform concentration for bounded original requirements

Fix L>0. For r sufficiently large let J_r=floor(log_2(r/L)) and ell_r=r 2^-J_r in [L,2L). Define
V_small(s)=sum_{jobs present} R_i(s) 1_{B_i<=ell_r},
mu_small=E[B^2 1_{B<=ell_r}]/(2m),
D_small(s)=V_small(s)-mu_small Q_r(s).

Between arrivals/departures V_small decreases at rate at most one. An arrival changes D_small by B 1_{B<=ell_r}-mu_small>=-mu_small. A departure removes zero residual work and increases D_small by mu_small. Thus for every u<=v,
D_small(v)>=D_small(u)-(v-u)-h[A(v)-A(u)],               (7)
since mu_small<=h. The two-sided scalar grid interpolation proved in ATTEMPT.md applies.

At a stationary snapshot conditional on Q=n, the summands are iid in [0,2L] with mean mu_small by (1). For n<=Cr, Hoeffding gives, uniformly over ell_r in [L,2L),
P_pi(|D_small|>epsilon*r, Q<=Cr)
<=2 exp[-epsilon^2 r/(2 C L^2)].                        (8)
n=0 is immediate. On the empty-start event sup Q<=Cr, each bad grid point belongs to the event in (8). Condition the stationary path on being empty initially and union over O(r) points: the bound is O(r^2 exp(-c*r))->0. Poisson interval-count bounds and (7) extend it to all times. Compact containment (5) removes the queue cutoff, first holding C fixed while r tends to infinity and then sending C to infinity. Consequently, for every fixed L and epsilon>0,
P_empty(sup_{s<=r^2T}|D_small(s)|>epsilon*r)->0.          (9)
The cutoff ell_r may vary in [L,2L); the bound is uniform, so no limiting moment formula for ell_r is required.

## 4. Dyadic original-size classes: rare upcrossings per cycle

For j=0,...,J_r-1 let
b_{r,j}=r 2^{-(j+1)},   I_{r,j}=(b_{r,j},2b_{r,j}],
p_{r,j}=P(B in I_{r,j}),
w_{r,j}=E[B^2 1_{B in I_{r,j}}],
mu_{r,j}=w_{r,j}/(2m),
V_{r,j}(s)=sum_{jobs present} R_i(s) 1_{B_i in I_{r,j}}.
The classes partition (ell_r,r]. Set q=2^(-1/4) and a_j=(1-q)q^j, so sum_{j>=0}a_j=1 by the geometric series formula. Thus a_j=(1-2^(-1/4))*2^(-j/4). Fix C,A,epsilon>0 and define
M_{r,j}=Cr mu_{r,j}+epsilon*r*a_j,
x_{r,j}=epsilon*r*a_j.

During every cycle V_{r,j} starts at zero, decreases under service, and can increase only at an arrival in I_{r,j}, with jump at most 2b_{r,j}. If it exceeds M_{r,j} at a time when the whole preceding path has Q<=Cr, then some class-I arrival has prearrival state satisfying
Q<=Cr,   V_{r,j}>M_{r,j}-2b_{r,j}.                     (10)
Use the predicate in (10), replacing > by >= if desired. This is a state predicate independent of the new arrival mark, so (3) applies.

For j greater than a fixed j_0(epsilon), x_{r,j}>=4b_{r,j}, because x/(4b)=epsilon(1-q)*2^(3j/4-1). At a stationary snapshot with n<=Cr, (10) implies
V_{r,j}-n mu_{r,j}>=x_{r,j}/2.
The summands are iid bounded by 2b and have second moment at most 2b mu by (1). The elementary Bernstein bound gives
P_pi((10))<=exp[-x^2/{8(V+b*x/3)}],
V=n E_H[X_I^2]<=(C/m) r b w_{r,j}.
To check the bound: for centered bounded nonnegative summands, the exponential-series estimate in ATTEMPT.md implies log mgf<=V theta^2/[2(1-theta*(2b)/3)] for theta*(2b)<3. Choosing theta=z/(V+(2b)z/3), z=x/2, yields exponent -z^2/[2(V+(2b)z/3)]. Zero-variance and n=0 cases have zero upper-tail probability.

Since w_{r,j}<=m2 and a_j<=1, the displayed exponent is bounded below in absolute value by c 2^{j/2}, with a fixed c=c(C,epsilon,m,m2)>0. Explicitly,
x^2/[8(V+b*x/3)]
>=epsilon^2 r a_j^2/[8b((C/m)m2+epsilon/3)]
=c_1 2^j a_j^2=c 2^{j/2}.
Thus for all j>=j_0,
pi_r((10))<=exp(-c 2^{j/2}).                           (11)
For j<j_0 simply use pi_r((10))<=1.

If N_r(r^2T)<=Ar, every positive-class upcrossing by the horizon occurs in one of the first ceil(Ar)+1 whole cycles; idle parts of a not-yet-started cycle carry zero marked work. Union bound over these cycles, Markov's inequality for the number of arrivals satisfying (10), and (3) give
P_empty(any class-j upcrossing by r^2T, sup Q<=Cr,
        N_r(r^2T)<=Ar)
<= (ceil(Ar)+1) r p_{r,j} pi_r((10))
<= C_A r^2 p_{r,j} pi_r((10)).                          (12)
The cycles can extend beyond the horizon: enlarging to whole cycles only increases the event. Their laws are identical, so the union bound requires no independence between the horizon's cycle count and individual cycle rewards. This is exactly where the earlier stationary-conditioning factor r is avoided.

Because B>b on the class, r^2 p_{r,j}<=2^{2j+2} w_{r,j}. For each fixed j, w_{r,j}->0 as r->infinity by E B^2<infinity. For j>=j_0, (11)–(12) are dominated by
C_A m2 2^{2j+2} exp(-c 2^{j/2}),
a summable sequence in j. For the finitely many j<j_0 the bounds tend to zero directly. Dominated convergence for this countable sum, extending by zero for j>=J_r, proves
P_empty(any dyadic class exceeds M_{r,j} by the horizon,
        sup Q<=Cr, N_r(r^2T)<=Ar)->0.                   (13)
No rate of convergence of the second-moment tail is assumed.

## 5. Sum the classes and finish collapse

Let V_big(s)=sum R_i(s) 1_{B_i>r}. Starting empty,
sup_{s<=r^2T} V_big(s)<=sum_{k<=A_r(r^2T)} B_k 1_{B_k>r}.
The expectation of the right side divided by r is
lambda_r^0 r T E[B 1_{B>r}]
<=lambda_r^0 T E[B^2 1_{B>r}]->0.                       (14)
Thus V_big/r vanishes uniformly in probability.

On the complement of the class upcrossing events,
sum_{j<J_r} V_{r,j}(s)/r
<=C sum_j mu_{r,j}+epsilon sum_j a_j
<= C E[B^2 1_{B>L}]/(2m)+epsilon,
uniformly in s. Use compact containment (5) and cycle-count tightness (6) to choose C,A large, then choose L large so the remaining second-moment tail is small. Equations (13)–(14) give the double-limit statement
lim_{L->infinity} limsup_{r->infinity}
P_empty(sup_{s<=r^2T} sum R_i(s) 1_{B_i>ell_r}/r >eta)=0
for every eta>0.                                        (15)

Finally,
W_r-hQ_r
=D_small + sum R_i 1_{B_i>ell_r} -(h-mu_small)Q_r
<= |D_small|+sum R_i 1_{B_i>ell_r}.
Use (9) for each fixed L, followed by (15), to conclude
sup_{s<=r^2T}(W_r(s)-hQ_r(s))^+/r ->0.
Combine with (4) to obtain two-sided uniform collapse
sup_{s<=r^2T}|W_r(s)-hQ_r(s)|/r ->0.                    (16)
Only finite second service moment has been used.

## 6. All real beta and diffusion convergence

For target lambda_r with r(1-lambda_r m)->beta, the difference from lambda_r^0 is O(1/r). On a finite primitive-path horizon H=r^2T the target/reference likelihood ratio is
L_r=exp[(lambda_r^0-lambda_r)H]*(lambda_r/lambda_r^0)^{A_r(H)}.
Exactly E_0 L_r^2=exp[H(lambda_r-lambda_r^0)^2/lambda_r^0], which remains bounded. Cauchy–Schwarz transfers the vanishing probabilities in (16) to every real beta. Service marks and insertion uniforms are unchanged under this rate change.

At the target rates the workload FCLT has drift -beta and variance rate m2/m. Reflection is continuous at its continuous Brownian limit. Uniform collapse (16) and convergence together therefore yield the stated queue-length convergence in J1 on every compact time interval, and hence in D([0,infinity)). The reflected process has drift -beta/h and variance rate m2/(m h^2). This proves the theorem. The cycle identity, summable upcrossing bound, limit order and noncircular inputs have been checked in REFEREE.md.

## Appendix: one-sided collapse and grid interpolation, in full

Let R have the equilibrium residual marginal of H. It is strictly positive almost surely, and E R=h<infinity. For independent copies let S_n=sum_{i<=n}R_i, S_0=0. Fix K,eta>0. We first show, uniformly over all nonnegative integers n,
P(S_n<=Kr, S_n-hn<-eta*r)<=c_0 exp(-c_1 r).            (17)

Choose theta_0>0 and kappa=-log E exp(-theta_0 R)>0. Choose C>2 theta_0 K/kappa. If n>Cr, exponential Markov bounds P(S_n<=Kr) by exp(theta_0 Kr-kappa n)<=exp(-kappa n/2). If n<=Cr, finite mean gives log E exp[-theta(R-h)]=o(theta) as theta decreases to zero. Indeed, (1-exp(-theta R))/theta is bounded by R and converges to R, so dominated convergence gives E exp(-theta R)=1-theta*h+o(theta); centering cancels its linear term. Choose theta small enough that the centered logarithm is at most theta*eta/(2C). Markov bounds the deviation by exp(-theta*eta*r+n*theta*eta/(2C))<=exp(-theta*eta*r/2). The n=0 event is empty. This proves (17).

For D=W-hQ, service decreases workload at rate at most one, an arrival changes D by B-h>=-h, and a departure increases D by h. Thus for u<=v,
D(v)>=D(u)-(v-u)-h[A(v)-A(u)].                         (18)
Simultaneous deletions also increase D and do not invalidate the inequality. If u<=t<=v and b=(v-u)+h[A(v)-A(u)], applying (18) to [u,t] and [t,v] gives
D(u)-b<=D(t)<=D(v)+b.                                 (19)
The same implication holds for D_small: its service derivative is at least -1, each arrival jump is at least -mu_small>=-h, and each departure jump is mu_small>=0.

Take a grid t_k=k*delta*r through the first point at or beyond r^2T, with horizon H_r<=r^2T+delta*r. There are O(r) intervals. For an eventual upper bound lambda_max on the rates choose M>lambda_max. For a Poisson variable Z of mean at most lambda_max*delta*r, exponential Markov gives
P(Z>M*delta*r)<=exp[-delta*r*(M log(M/lambda_max)-M+lambda_max)].
The bracket is positive. Union bounding O(r) intervals shows that, with probability tending to one, every interpolation budget is at most (1+hM)*delta*r. These counts are bounded directly under the empty-start law.

For every future-path event E, stationarity and the empty probability 1/r give
P_empty(E)=P_pi(E | Q(0)=0)<=r P_pi(E).                (20)
On the cutoff sup_{s<=H_r}W(s)<=Kr, a grid violation D(t_k)<-eta*r belongs to the event in (17). Conditional on stationary Q(t_k)=n, W(t_k)=S_n. Mixing (17) over the count law costs no extra factor. Therefore
P_empty(workload cutoff and some such grid violation)
<=r sum_k P_pi(W(t_k)<=Kr,D(t_k)<-eta*r)
<=O(r^2 exp(-c_1 r))->0.                              (21)

Fix epsilon>0, choose eta=epsilon/2 and delta so (1+hM)*delta<=epsilon/2. Equations (19) and (21) bound D(t)>=-epsilon*r throughout [0,r^2T] on the cutoffs, outside a probability tending to zero. Workload FCLT makes sup W/r tight on the slightly enlarged horizon, bounded by r^2(T+1) for large r. Take K large to remove the cutoff. This proves (4), using only finite E R, hence only finite E B^2.

For (9), use the same grid, budget and (20). The stationary bad-grid estimate is (8), restricted to Q<=Cr; its empty-start union bound is O(r^2 exp(-c r)). Apply (19) to D_small for both signs, using the preceding grid point for the lower bound and the following point for the upper bound. Choose delta and the grid tolerance as above. Compact containment already follows from (4); use it on the enlarged horizon and then let C increase. This proves (9) without assuming the conclusion of the dyadic argument.
