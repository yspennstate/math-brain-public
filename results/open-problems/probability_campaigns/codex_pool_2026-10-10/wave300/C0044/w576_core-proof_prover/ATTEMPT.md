# C0044 core proof attempt: invariant environment law

Scope: the exact statement is in STATEMENT.md. This packet does not claim the full directional zero-one law. Current openness is UNKNOWN because a September 2026 primary manuscript claims a proof, and its mathematical dependencies are not yet checked here.

## Proved reduction L1: exclude coexistence of opposite escapes

For deterministic nonzero l, A_l and A_-l are disjoint. The iid elliptic union zero-one theorem gives P_0(A_l union A_-l) in {0,1}. Consequently the individual zero-one target is equivalent to ruling out P_0(A_l)>0 and P_0(A_-l)>0 simultaneously: if P_0(A_l)>0 the union has probability one, and absence of negative escape makes P_0(A_l)=1. Conversely a binary positive P_0(A_l) equals one and excludes negative escape. The disjointness statement itself is elementary and does not solve the coexistence problem.

## Proved conditional lemma L2: an equivalent stationary environment law suffices

Let theta_x shift an environment by x and let Kf(omega)=sum_e omega(0,e) f(theta_e omega). Assume the environment law P is shift ergodic, is supported on strictly elliptic nearest-neighbor environments, and there exists a K-invariant probability Q equivalent to P. For a fixed l define q(omega)=P_omega^0(A_l). The Markov property and invariance of A_l under removing a finite path prefix give Kq=q.

Since 0<=q<=1, Q-invariance gives

 integral sum_e omega(0,e)[q(theta_e omega)-q(omega)]^2 dQ
 = integral [K(q^2)-q^2] dQ = 0.

Every summand is nonnegative, and every omega(0,e) is positive Q-almost surely. Thus q(theta_e omega)=q(omega) for every neighbor e, Q-almost surely and, by equivalence, P-almost surely. Countably many translations propagate this equality to all lattice shifts. Shift ergodicity implies q=c P-almost surely for some constant c. For P-almost every omega this holds at every translate visited by the walk.

For fixed such omega and the path filtration F_n, the quenched Markov property gives E_omega[1_{A_l}|F_n]=q(theta_{X_n}omega)=c. The increasing F_n generate the full path sigma-field, so conditional-expectation convergence gives c=1_{A_l} almost surely. Hence c is 0 or 1 and P_0(A_l)=c.

This argument uses stationarity only under Q; it does not assume that P itself is invariant for the environment seen from the particle.

## Proved lemma L3: absolute continuity gives equivalence here

Assume P is shift invariant and ergodic and strictly elliptic, and Q=fP is a K-invariant probability with f>=0 and integral f dP=1. A change of variables gives the adjoint formula

 K* f(omega) = sum_e omega(-e,e) f(theta_-e omega).

Invariance implies f=K*f P-almost surely. On Z={f=0}, positivity of every incoming transition implies f(theta_-e omega)=0 for every e. Thus Z is contained, modulo null sets, in every neighboring translate of Z. Those sets have the same P-measure by shift invariance, so the inclusions are equalities modulo null sets. Ergodicity gives P(Z)=0 or 1. Integral f=1 excludes P(Z)=1. Therefore f>0 P-almost surely and Q is equivalent to P. Null exceptional sets can be removed at all countably many translates. Combining with L2 gives the directional zero-one law under absolute continuity alone.

## Proved lemma L4: a precise sufficient incoming-mass condition

For n>=0 put f_n(omega)=sum_x P_omega^x(X_n=0), where only |x|_1<=n can contribute. The law of theta_{X_n}omega under the original annealed law is f_n P: for bounded g, change variables eta=theta_x omega in sum_x integral P_omega^0(X_n=x)g(theta_x omega)dP. The resulting transition probability is P_eta^-x(X_n=0). Thus f_0=1, f_n>=0, integral f_n=1, and f_{n+1}=K*f_n.

Put H_N=(1/N)sum_{n=0}^{N-1} f_n. If the family H_N is uniformly integrable in L1(P), the Dunford-Pettis compactness theorem gives a weakly L1-convergent subsequence with limit f>=0 and integral f=1. Further,

 ||K*H_N-H_N||_1 = ||(f_N-1)/N||_1 <= 2/N.

For every bounded measurable g, weak L1 convergence applies to both g and Kg. The displayed bound implies integral f Kg=integral f g. Hence fP is K-invariant. L3 and L2 give the directional zero-one law. This is a sufficient criterion, not a consequence yet of iid ellipticity.

## Source-backed counterexample C1: the general sufficient input is false

Take d=3 and iid Dirichlet rows with parameters alpha=(1/10,1/50,1/50,1/50,1/50,1/50), ordered (+e1,+e2,+e3,-e1,-e2,-e3). Every parameter is positive, so every row is strictly positive almost surely. Countably many sites preserve almost-sure strict ellipticity. These laws are not uniformly elliptic.

Here sum alpha=1/5; the largest opposite-pair sum is 3/25; and Sabot's trap exponent is

 kappa_D=2 sum alpha-max_i(alpha_i+alpha_{i+3})=7/25<=1.

Sabot, arXiv:1007.2565v3, Theorem 1(ii), printed page 4 (PDF page index 3), states that at kappa_D<=1 there is no absolutely continuous invariant probability for the environment viewed from the particle. Its generator is K-I, so this is exactly nonexistence for K. Therefore such an invariant probability cannot be inferred from the full C0044 assumptions. By L4, H_N is not uniformly integrable for this example. This counterexample refutes the proposed blanket invariant-probability/UI input, not C0044. The nonzero mean drift (2/5)e1 is only parameter arithmetic here; no transience claim is inferred from mean drift.

The uniformly elliptic subtarget is not refuted by this nonuniform example. We have no derivation of the required invariant probability for that subtarget either.

## Proved lemma L5: exact energy balance without a stationary law

Keep the original P, without assuming K-invariance or uniform integrability. For q(omega)=P_omega^0(A_l), define

 D_l(omega)=sum_e omega(0,e)[q(theta_e omega)-q(omega)]^2 = K(q^2)(omega)-q(omega)^2.

The equality follows from Kq=q. D_l is measurable, nonnegative, and bounded by 1. The quenched conditional-expectation martingale q(theta_{X_n}omega) converges almost surely to 1_{A_l}; bounded convergence gives integral f_N q^2 -> p, where p=P_0(A_l)=integral q dP.

Adjointness gives for every n

 integral f_n D_l dP = integral f_{n+1}q^2 dP-integral f_n q^2 dP.

Telescoping and then monotone convergence yield the exact identity

 sum_{n=0}^infinity integral f_n D_l dP = p-integral q^2 dP = integral q(1-q)dP.

In particular, integral H_N D_l dP <= integral q(1-q)dP/N <= 1/(4N). This is an exact analytic bound, not an experimental rate. It is valid for strict and uniform ellipticity and does not multiply any conditional probabilities.

## Proved lemma L6: full target reduced to one flux covariance

Let s(omega)=sum_e omega(-e,e)=K*1(omega). Shift invariance gives integral s dP=1, and 0<=s<=2d. The exact identity is

 integral D_l dP = integral (s-1)q^2 dP = Cov_P(s,q^2) >=0.

If this covariance is zero, D_l=0 P-almost surely. Strict positivity then gives q(theta_e omega)=q(omega) at every neighbor almost surely; shift ergodicity and the martingale argument in L2 imply p in {0,1}. Conversely, if p is zero or one, the bounded variable q with mean p is that same constant P-almost surely, so the covariance and energy vanish. Hence the fixed-direction target is equivalent to this covariance vanishing.

## Single hardest remaining gap G1

Prove Cov_P(s,q_l^2)=0 for the specific directional escape harmonic function q_l in arbitrary iid strictly elliptic environments on Z^d, d>=3. Equivalently, prove that positive original-law energy cannot be lost by the incoming-mass averages: if integral D_l dP>0, then limsup_N integral H_N D_l dP>0. L5 forces the latter limsup to be zero, so this non-starvation statement would close the target.

The iid rows do not justify independence of s and q_l^2: s uses neighboring incoming rows and q_l uses the entire environment, including those rows. Replacing their joint expectation by a product is precisely the unproved step. Uniform integrability was a sufficient way to close it, but C1 proves that blanket input false in the strict-ellipticity class. Nothing here establishes G1, and G1 is a reformulation of the unresolved target rather than a newly solved input.

All L1-L6 and C1 are author proofs or a source-backed deduction pending w578 review. No formal proof, served-model receipt, independent check, or full-target success is claimed.
