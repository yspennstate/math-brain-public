# Independent audit of the finite inward-box argument

The independent counterexample and conditional-cost derivation in INDEPENDENT.md and ATTEMPT.md were saved before reading w444/ATTEMPT.md. This audit concerns the explicit R1, L1, L2, L2b and L3 statements, not a claimed resolution of the full problem. The designated referee remains w446.

R1: KEEP with its explicit cycle-law and finite-mean inputs. Nearest-neighbor increments make displacement integrable once duration is integrable. The integrated tail inequality and Borel-Cantelli justify the last incomplete cycle. The initial finite random shift does not need a finite expectation.

L1: KEEP. The longest all-+e_1 exit path has length at most 2r+1. Since 0 < kappa <= 1/(2d) <= 1, its probability is at least kappa^(2r+1). The geometric tail follows by conditioning at deterministic block boundaries, with the same uniform bound at each boundary. This is a valid tower argument, not an assertion of block independence. The moment comparison with a geometric variable and then 1+Exponential(p) gives the stated generous constant 2^s s!.

L2: KEEP for exactly the defined pattern. The opposite drift-sign events are disjoint only because delta > 0. Each half-box contains n_r=r(2r+1)^(d-1) sites, so iid rows give (p_+p_-)^n_r <= 4^(-n_r). The degree-d exponent beats the linear exit-cost exponent for d>=2. This says nothing about patterns not in the event.

L2b: KEEP for fixed theta > 1/2. For a=exp(lambda)-1>=0, the two half-box generating functions have product [(1+a p_+)(1+a p_-)]^n_r. Their sum is at most 2+a, so AM-GM bounds the product by ((1+exp(lambda))/2)^(2n_r). Chernoff gives the displayed entropy bound; theta=1 is the limiting case. As theta decreases to 1/2 the positive rate disappears. No uniform statement at theta=1/2 or at varying theta approaching it has been established.

L3: KEEP only with the displayed deterministic location/time budget and a genuine stopping time H in the environment-augmented filtration. Quenched strong Markov gives the uniform moment bound even after adaptive center selection. The subsequent union bound is over deterministic sites. Division by q=P_0(D=infinity)>0 is a valid inequality for nonnegative random variables and does not assert a Markov property under Q.

Full-target inference: NOT ESTABLISHED. The packet itself states this limitation correctly. The missing premise is a classification or occupation estimate for every source of a long regeneration delay, including excursions and repeated visits, together with an integrable accounting of their durations.

## Concrete obstruction to removing the deterministic search budget

Fix d>=2. At each site, independently choose one of two rows with probability 1/2 each. Set kappa=1/(4d). Every direction has probability kappa, except that the selected direction +e_1 or -e_1 has probability kappa+1/2. The probabilities sum to 1 and are uniformly elliptic. For delta=1/2 the inward-box event of L2 has probability p_r=4^(-n_r)>0 at every fixed center.

For a fixed r, take disjoint boxes centered at c_j=j(2r+1)e_1, j>=1. Their row sets are disjoint, so the inward-pattern events are independent. The chance none of the first M boxes matches is (1-p_r)^M. Let J_r be the first match. Then J_r<infinity almost surely and the environment-measurable selected center C_r=c_{J_r} satisfies P_env(A_delta(C_r,r))=1, while every fixed-center probability equals the arbitrarily small p_r. This holds simultaneously for all integer r by a countable intersection of probability-one events.

The selected centers have no deterministic location bound. This counterexample does not meet L3's bounded-center/start conditions and therefore does not refute L3. It refutes the proposed extension of fixed-center rarity to unrestricted adaptive selection. No directional-transience or non-ballisticity claim about this row law is made.

For illustration, r=1,d=2 gives n_r=3 and p_r=1/64. Searching 64 disjoint boxes raises the pattern probability to 1-(63/64)^64 > 1/2. Searching indefinitely raises it to 1. This is an exact finite calculation, not a walk simulation.

## A quantified missing premise sufficient to finish this trap route

Use Q=P_0(.|D=infinity), q=P_0(D=infinity)>0. Fix delta>0, theta>1/2, c>0 and a finite t_0. Put r(t)=floor(c log(t+2)), restricting to large enough t that r(t)>=1. A sufficient classification premise is

Q(tau_1>t) <= epsilon_t + Q(exists x in [-t,t]^d: A_delta,theta(x,r(t)))

for all integer t>=t_0, where epsilon_t>=0 and sum_t epsilon_t<infinity. The events in the union depend on the environment alone. Therefore their Q-probability is at most q^(-1)(2t+1)^d exp[-2 n_{r(t)} D(theta||1/2)]. Its logarithm is d log(2t+1) minus a positive constant times (log(t+2))^d, plus a fixed conditioning constant. For d>=2 it is eventually <=-3 log(t+2), so the series is summable. Summing the tail inequality proves E_Q tau_1<infinity.

This deduction is proved conditional on that premise; the premise itself is unproved. It is substantially stronger than the local box lemmas and must not be relabeled as their consequence. If theta is scale dependent, the needed comparison is n_{r(t)} D(theta(t)||1/2) >> log t; positivity at each individual scale is not enough.

NEXT: Prove or refute the classification premise for arbitrary low-crossing-probability regions without requiring inward drift on a fixed fraction of their rows.
