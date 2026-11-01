# G0007 — second attempt, 2026-10-11

STATE of this note: work in progress; no new endpoint-derivative claim proved.

## Two approaches not pursued in the first attempt

A. **Parameter change versus independent noise.** Read the Broman--Steif stochastic-movability comparison for upper invariant contact-process measures. Determine its exact direction and whether it converts theta_H(c-h) into percolation after independent site enhancement of the critical healthy field. Seek a linear lower bound via a susceptibility/sharpness theorem for this enhancement; such a bound would refute continuous differentiability at the healthy threshold. Never reverse stochastic domination or assume that a critical parameter for lambda is also critical for independent enhancement.

B. **Exact stationary healthy-cluster hierarchy.** Apply the stationary generator to all-healthy connected sets, starting with one vertex, an edge, and a three-vertex path, then higher shapes. Derive finite-dimensional probabilities and branch covariances exactly, and identify the quantity controlling the derivative of an infinite healthy component. Try a controlled large-degree or finite-shape special case instead of assuming spatial Markov independence.

Approach A is the more direct route to the derivative gap and will be tested first. Approach B provides exact contact-process checks for any comparison or branching approximation.

The previous ATTEMPT.md establishes both endpoint continuities but has no estimate theta_H(c-h)=o(h), no existence of derivatives on a one-sided neighborhood, and no positive infected one-sided slope. Those are the remaining obligations. Prior continuity proofs will also be audited; no earlier claim is accepted merely because it was written down.
## Preliminary audit and an obstruction to Approach A

The previous continuity proof was reread. Its sample-dependent Poisson insertion uses a joint Lebesgue density, not deterministic inserted times; the null-set calculation via factorial Campbell--Mecke remains valid. The infected surgery restores every internal path vertex after the infection wave and occurs after all original incident marks, so the final outside state is unchanged. The continuous reciprocal-cluster-size observable and the finite-bridge/unique-cluster transports were checked again. No mathematical correction found at this stage. The previous Lean result was not captured; its old session handle is no longer available, so it is still not called checked.

The prospective noise argument requires more than a stochastic comparison. If H_lambda denotes the healthy law, a comparison H_(c-h) >= enhancement_epsilon(H_c) can only help when H_c is itself at the threshold for independent enhancement. That identification is not implied by parameter criticality. A concrete countermodel is being constructed on T_d, d>=4:

- Give the tree an invariant proper d-edge coloring, remove one color, obtaining infinite (d-1)-regular components.
- Give each component an independent uniform label; call it selected if the label is <=t_+.
- Given these labels, occupy sites independently with probability a(t) on unselected components and b(t) on selected components, where a(t)=a0+k*t, b(t)=b0+k*t, a0<1/(d-1), b0>1/(d-2), and all probabilities stay uniformly inside (0,1).

At t=0 this is independent subcritical percolation, so its independent-enhancement threshold is strictly positive and susceptibility finite. For every t>0, a selected component has supercritical independent percolation internally, giving theta(t)>=const*t. The family is monotone, weakly continuous, invariant, and uniformly finite energy. It also has parameter/noise comparisons with noise at least proportional to |t-s| because every conditional site probability increases by at least k(t-s). This would show exactly why Approach A cannot infer the desired derivative from stochastic movability alone. Full invariance and ergodicity details, and all domination directions, remain to be verified before claiming the countermodel.
## Revised explicit obstruction (actual construction uses T_3)

The initial colored-forest idea is replaced by independent bond percolation with r=3/4, which makes invariance, ergodicity and positive association transparent. Give every bond cluster an iid Uniform[0,1] label. Select it when its label is <=t_+, with -1/10<=t<=1/10. Given these labels, occupy vertices independently with probabilities

  a(t)=1/10+t/10, b(t)=3/4+t/10

on unselected and selected bond clusters respectively. This is NOT a stationary contact-process law.

The following are proved in the forthcoming full write-up: uniform two-sided finite energy (all conditional probabilities in [9/100,19/25]); full tree invariance; exponential mixing and hence ergodicity; positive association via the hidden two-state broadcast chain; weak continuity and monotonicity; thinning and enhancement comparisons with epsilon=(t-s)/10; zero percolation for t<=0 and (193/486)t<=theta(t)<=2t for t>0; endpoint independent-enhancement threshold 4/9; finite endpoint susceptibility 11/80. Thus parameter criticality cannot be identified with independent-noise criticality even under these stronger qualitative hypotheses.

This is a proved method obstruction once the complete details below are checked, not a counterexample to G0007. The CP derivative gap remains unchanged.
## Approach B: exact stationary healthy probabilities (proved algebra, 2026-10-11)

Let h=nu_lambda(o healthy), q=1-h, lambda>lambda_1, and let Z(A) be the probability every vertex in finite A is healthy. The cylinder generator gives exactly

  sum_(x in A) [Z(A\{x})-Z(A)]
    = lambda sum_(x in A,y adjacent x,y not in A) [Z(A)-Z(A union {y})].

Recoveries enter the all-healthy event only when x is its sole infected vertex; infection arrows leave it only from outside A. All involved rates are bounded, so stationarity justifies this identity without an infinite-cluster generator.

For an edge and a three-vertex path write P2 and P3. Singleton and edge equations yield

  P2=h-q/(lambda*d),
  P3=h-q/(lambda*d)-q/[lambda^2*d*(d-1)].

If D is the number of healthy neighbors conditional on the root being healthy, put m=E D. Then

  m=d*P2/h,
  E[D(D-1)]=d*(d-1)*P3/h,
  Var(D)=(d-m)*(m-1/lambda).

For two different neighbors y,z,

  Cov(1{y healthy},1{z healthy} | o healthy)
   =(d-m)*[lambda*(d-1)*m-d]/[lambda*d^2*(d-1)].

second_symbolic_checks.json confirms both algebraic identities. Their probability derivation above is the proof, not the symbolic output.

At the next path equation the hierarchy fails to close. Let Z02 be the healthy probability for two vertices at distance two, P4 that for a four-vertex path, and S4 that for the four-vertex three-leaf star. Stationarity of the three-vertex path gives

  2*P2+Z02-3*P3
   = lambda*[(3*d-4)*P3-2*(d-1)*P4-(d-2)*S4].

Z02 is disconnected and P4,S4 are different shapes. Treating all size-four sets as having the same probability, or factoring Z02, would be unjustified. Thus the exact local moments are new proved facts in this attempt, but do not yet control theta_H(c-h)/h.
## New rigorous healthy-threshold bound

The general-graph downward-FKG property of upper invariant contact-process measures is explicitly recalled in Liggett--Steif, arXiv:math/0504530, PDF p. 7, equation (5), citing van den Berg--Haggstrom--Kahn (2005). Thus the conditional covariance of two healthy neighbors given a healthy root is nonnegative. The exact covariance identity above gives

  m >= d/[lambda*(d-1)],
  h >= 1/[lambda*d-1/(d-1)].

(The denominator is positive when lambda>lambda_1>=1/(d-1).)

If all healthy clusters were finite, the invariant-tree identity in ATTEMPT.md gives

  m = 2 - 2 E[1/|C_o^H| | o healthy] < 2.

The expectation is strictly positive because conditioned on a healthy root its finite cluster has finite positive size. Therefore healthy percolation occurs whenever lambda<=L_d=d/[2(d-1)] (lambda<=lambda_1 has all sites healthy). Combining this with the already proved critical healthy nonpercolation gives lambda_p^c > L_d.

For d=4,5 one can improve this quantitatively. Put U=L_d+1/100,

  q0 = 1-1/[L_d*(d-2)] > 0,
  K = q0^d/[2*(2*d*(1+U)+1)],
  delta = L_d*K/2,
  lambda*=L_d+delta.

The exact rational checks show delta<1/100. Source Lemma 4.1 and subtree monotonicity give q(lambda*)>=q0. Start the stationary process at time -tau, where tau=1/[2*d*(1+U)]. By ordinary FKG, all d neighbors are infected then with probability at least q0^d. Require no neighbor recovery, no infection arrow directed into the root, and at least one root recovery during this interval. These future marks are independent of the initial state. At time zero the root is healthy and all neighbors infected; the event's probability is at least

  q0^d * exp[-d*(1+lambda*)*tau] * (1-exp[-tau])
   >= q0^d*(1/2)*tau/(1+tau) = K.

The inequalities use exp(-x)>=1-x and exp(tau)>=1+tau. Source's invariant-tree identity then yields

  B_H/h >= m-2+2K >= 2L_d/lambda*-2+2K >= K > 0,

where h<=1 and delta=L_d*K/2 were used. Thus healthy percolation occurs at lambda*, and critical nonpercolation implies lambda_p^c>lambda*. The exact fractions are saved in second_threshold_bounds.json. This argument supplies a bound, not a derivative estimate.


## Final audit and disposition

Complete proofs are in SECOND_PROOFS.md. Both approaches were pursued: the initially more promising noise approach led to an explicit countermodel to its missing inference; the hierarchy approach yielded rigorous new threshold bounds. All four finite/algebraic check scripts completed successfully. These checks support the written proofs and do not certify the infinite-volume derivative assertions.

Correction to the denominator note above: no external lambda_1 lower bound is needed. Algebra gives h[lambda*d-1/(d-1)]>=1 directly, hence positivity of the bracket. This is the argument used in the complete proof.

Both derivative clauses remain open in this work. Future work needs an actual contact-process enhancement/response theorem or uniform large-radius correlation control. Closing this second attempt with STATE: DONE and VERDICT: PARTIAL records completion of the attempt, not solution of the full problem.
