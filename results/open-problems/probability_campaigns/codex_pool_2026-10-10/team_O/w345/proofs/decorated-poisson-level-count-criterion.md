# C0005: Conditional deep-level law from truncated marked-Poisson moments

Label: proof; author checked only. Independent audit: PENDING w347.

Fix alpha>0 and z>=0 finite. Let heights h_i form a Poisson process on R of intensity z*exp(-alpha*h) dh, carrying independent identically distributed measurable nonnegative marks K_i(s), s>=0, independent of the heights. Suppose exp(-alpha*s)*E K(s)->c in (0,infinity) and E K(s)^2<=C*exp(2*alpha*s) for every s>=0. Set S_t=sum_(h_i>=-t) K_i(t+h_i). Then S_t/(t*exp(alpha*t))->c*z in probability as t->infinity. The same conclusion holds with a finite almost-sure random intensity Z conditionally on Z and unconditionally, without assuming E Z<infinity. This is a conditional criterion for the limiting DGFF cluster process, not a proof of its moment hypotheses or the finite-N limit.

Assumptions: A marked Poisson process with the stated intensity and independent identically distributed decorations; alpha>0 and finite z (or a.s. finite random Z); The two explicit first and second decoration moment hypotheses

For a fixed upper cutoff H and t+H>=0 define S_t^H using -t<=h_i<=H. Poisson integration and the change of variable s=t+h give E S_t^H=z*exp(alpha*t)*integral_0^(t+H) exp(-alpha*s)*E K(s) ds. Cesaro averaging implies this divided by t*exp(alpha*t) tends to c*z. Its variance divided by t^2*exp(2*alpha*t) is at most z*C*exp(alpha*H)/(alpha*t^2), so the truncated variable converges in L2 for fixed H. The probability that the full and truncated sums differ is at most the probability of any height above H, namely 1-exp(-z*exp(-alpha*H)/alpha). First send t to infinity, then H to infinity, to prove convergence in probability. For random finite Z, these conditional error probabilities tend to zero and are bounded by one, so dominated convergence applies; E Z is not required. For finitely many disjoint spatial sets the same argument and a finite union bound give joint convergence with their respective intensity masses. Notice that E S_t is infinite whenever z>0 under the stated first-moment asymptotic: its integral extends over s in [0,infinity). Thus full-sum L2 convergence or uniform integrability must not be silently assumed. The earlier intake integral with exp(+alpha*s) inside reverses the change-of-variable sign.

Limits: The moment hypotheses and the exchange or iterated use of the finite-N and deep-level limits are not verified for DGFF. The full limiting sum can have infinite expectation even while its normalized values converge in probability.

Existing card: math:probability.gaussian:open-problem-c0005-size-of-deep-extremal-level-sets-of-the-2d-dgff-converges-to-the-extre
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:8541
