# Independent audit of the Whitt waiting-time counterexample

Date: 2 October 2026. Internal mathematical audit, not a claim of publication or established novelty.

## Verdict

I independently checked the model, every generator block, the exact rational root enclosure, the boundary equations, the probability normalization, the service-time convex ordering, and the handling of zero-service customers. I found no mathematical gap. Running `whitt_qbd_exact.py` succeeded. Its original pair gives a certified delay-probability decrease greater than 0.00115. A simplification below gives a decrease greater than 0.0025 using the base certificate alone and an ordinary M/M/2 formula.

The historical scope is also correct: Whitt's 1983 Conjecture 1.1 concerns iid service distributions ordered in increasing convex order, with Poisson arrivals, fixed homogeneous FCFS servers, and stationary waiting until service starts. Section 6 explicitly admits service distributions with an atom at zero. This is a counterexample to the full stochastic-order claim, not necessarily to a weaker mean-wait conjecture. A current-literature search has not located a prior refutation; that search is not proof of novelty.

Primary source: Ward Whitt, *Comparison conjectures about the M/G/s queue*, Operations Research Letters 2 (1983), 203–209, doi:10.1016/0167-6377(83)90026-3. Author-hosted PDF: https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf . Conjecture 1.1 is on p.203; zero-atom scope and insensitivity of delay probability within the zero-plus-exponential family appear on pp.207–208.

## Simpler counterexample

Let both queues have two servers and original Poisson arrival rate 11/10. Let E be exponential of mean one. The base service law is S=E/5 with probability 3/7 and S=8E/5 with probability 4/7. Its mean is one. Define U=0 with probability 3/8 and U=8E/5 with probability 5/8, also of mean one.

To couple them, sample the base class and E. Keep the large class unchanged. In the small class replace E/5 by zero with probability 7/8 and by 8E/5 with probability 1/8, independently of E. Conditionally on the base class and E, the mean replacement is exactly S. Therefore E[U|S]=S and S is smaller than U in convex order. The resulting positive mass is 4/7+(3/7)(1/8)=5/8 and the zero mass is 3/8, as stated.

Deleting zero work from the workload process preserves every positive-job start time and every virtual waiting time. Zero-service jobs still experience their original FCFS wait; they merely add no workload. The positive subsystem for U is M/M/2 with arrival rate (11/10)(5/8)=11/16 and service rate 5/8 per server. PASTA for all original arrivals gives the original delay probability equal to the busy probability of this thinned subsystem. Its utilization is 11/20. Erlang C gives

    P(W_U>0)=2(11/20)^2/(1+11/20)=121/310.

The exact base certificate gives P(W_S>0)>39287/100000, so

    P(W_S>0)-P(W_U>0)>7897/3100000>1/400.

At h=1/100000, a currently delayed base customer can begin service within h only if some service completion occurs. Both current exponential rates are at most five, so the conditional total completion hazard is at most ten and P(0<W_S<=h)<=10h. Hence

    P(W_S>h)-P(W_U>h)>7897/3100000-1/10000>0.0024.

Thus even a strictly positive tail threshold violates the conjectured stochastic order.

## Generator audit

For an M/H2/2 positive-job system let lambda be its arrival rate, p the probability of choosing a small exponential at the start of service, and mu_s,mu_l the rates. Sampling the class at service start is valid by deferred decisions: a customer's independent service mark has no effect on its own pre-service wait, and the unstarted marks of waiting customers remain iid.

With both servers busy, phase i=0,1,2 counts small jobs in service; level q>=0 counts positive customers waiting. Let M_i=lambda+i mu_s+(2-i)mu_l. The within-level block is -diag(M_i), the up block lambda I, and the down block D is

    D_ii=i mu_s p+(2-i)mu_l(1-p),
    D_i,i-1=i mu_s(1-p),
    D_i,i+1=(2-i)mu_l p.

These are precisely the completion-and-replacement events when q>=1. At q=0 a completion instead yields a single small or large job: phase 0 -> large at rate 2mu_l, phase 1 -> small at mu_l and large at mu_s, phase 2 -> small at 2mu_s. The single-job arrival transitions and source from the empty state in the verifier agree with this generator. Exit rates are uniformly bounded, so the chain is nonexplosive.

For row stationary vectors v_q=v_0 R^q, interior balance is

    v_(q-1)lambda I-v_q M+v_(q+1)D=0.

Thus the correct row-oriented quadratic is lambda I-RM+R^2D=0. Division by M on the right in the verifier is column division; its implementation is correct.

## Root enclosure audit

The verifier checks exact rational matrices L,U,W, all W_ij positive, with 0<=L<=U, L<=Phi(L), Phi(U)<=U, where Phi(X)=(lambda I+X^2D)M^-1. Phi is monotone on nonnegative matrices. On [0,U], for E=X-Y,

    X^2-Y^2=XE+EY,
    |Phi(X)-Phi(Y)|<=||E||_W (UW+WU)D M^-1.

The exact inequality (UW+WU)D M^-1<W therefore proves a strict Banach contraction on the complete box. There is a unique fixed point in the box; iteration from L is increasing, so L<=R<=U. The maximum row sum of U is less than one, giving spectral radius(R)<1 and absolute summability of the stationary matrix-geometric tail. If the minimal-root interpretation is wanted, iteration from zero is increasing, remains below U, and converges to this same fixed point. It is below every other nonnegative fixed point. However, the direct stationary-measure argument does not require citing a minimal-root theorem.

## Boundary and normalization audit

With empty-state mass one and boundary row x for (single small,single large,phase0,phase1,phase2), the verifier uses xK_R=-b, b=(lambda p,lambda(1-p),0,0,0). K_R has the correctly specified single-state rows and completion transitions, and full block RD-M, accounting for flow down from level one. Thus x=b(-K_R)^-1 is correct.

A(R)=-K_R is a Z-matrix and decreases entrywise with R. At U its exact inverse is nonnegative; z=A(U)^-1*1 is positive. For any intermediate R, A(R)z>=1. Diagonal scaling by z makes A(R) strictly row diagonally dominant, proving it is a nonsingular M-matrix with nonnegative inverse. The inverse identity then proves

    A(L)^-1<=A(R)^-1<=A(U)^-1,

and consequently x_L<=x_R<=x_U. Neumann series give (I-L)^-1<=(I-R)^-1<=(I-U)^-1. Hence total busy mass H=x_busy(I-R)^-1*1 and idle mass A=1+x_small+x_large are bounded monotonically. Bounding the ratio H/(A+H) by H_L/(A_U+H_L) and H_U/(A_L+H_U) is valid because it increases with H and decreases with A.

All nonempty balance equations hold by construction. Summing them is justified by the bounded rates and finite total mass; zero row sums of the generator give the omitted empty-state balance. The strictly positive finite stationary measure normalizes to a stationary probability measure. Irreducibility gives uniqueness and positive recurrence. It is therefore the queue's stationary distribution, not a merely formal solution of some interior equations.

## Exact rerun output for the original two-H2 pair

Base delay interval:

    [0.392872616812253851534562873661922895888448992345270776845846,
     0.392872621943210771400384443717859428973844088409107000214694]

Spread delay interval:

    [0.391709812331424374140340429690690776126439653136786843998069,
     0.391709815891175348285396281496080565490386714017916407379556]

Certified gap lower bound:

    0.00116280092107850324916659216584233039806227832735436946629087.

These decimal strings display exact rational bounds; no decimal arithmetic establishes the inequalities. The simpler U endpoint above needs only the first interval.

## Zero-service detail

The ordered two-server workload recursion adds a service requirement to the smallest workload coordinate and then reorders. A zero requirement makes no change. The arriving zero job nonetheless waits for the smallest workload to reach zero. Therefore deleting these jobs from the workload process preserves waiting times observed by all tagged arrivals, while deleting them from the observable list of arrivals would not be a valid interpretation. The proof uses the former operation. Independent Poisson marking and PASTA justify the thinning and all-arrival delay probability.

## Limits of this audit

This establishes internal mathematical validity of the proposed counterexample and agreement with the primary conjecture's assumptions. It does not establish historical originality, peer-reviewed acceptance, or resolution of the weaker mean waiting-time questions. The current search did not locate a prior full-stochastic-order refutation, but expert literature review remains appropriate.
