# C031 v1: explicit exponential moments for canonical history weights

Status: proof (unaudited), conditional auxiliary target-3 bound. This is
the standard subcritical branching-process exponential-moment method,
applied to C009/C023. No novelty or finite strong-core threshold is claimed.

Assume C009's finite-type stationary change branching process is valid.
Let its column-parent mean matrix be T, with rho(T)<1. Choose a positive
left weight vector h with h_i>=1 and

   sum_j h_j T[j,i] <= h_i-1,  H>=max_i h_i.

Such weights exist, for example h^T=1^T(I-T)^(-1). They can be made
rational with the displayed non-strict unit gap by first scaling this
vector upward and then taking a sufficiently close rational approximation.
Let p>0 be a lower bound on every conditioning probability pi_d in C009,
with p<=1. Choose C>=c, C>0, and H>=1. A parent's number of children is
bounded by its number K of other incoming tree neighbors; this K has the
Poisson(c) law conditioned on its baseline reverse-message event, whose
probability is at least p. Joint dependence among siblings is allowed.

Define

   A = (3 H^2/p) (9 C^2+9 C+1) 3^(ceil(2C)),
   s = 1/A,  theta=s/2,  gamma=s/12.

If H,p,C are rational, all four constants have exact rational encodings.
No decimal evaluation or uncertified matrix bound is needed to state
this implication. Applying it numerically still requires certified h,H,p,C
for the intended fixed point; none is asserted by this file alone.

For total cascade progeny T_i starting from type i, including its root,

   E exp(theta T_i) <= exp(s h_i) <= e.                 (1)

Proof. Explore the branching process in any predictable active-particle
order. Its queue weight changes by Delta=sum_child h_j-h_i, with
E[Delta|past]<=-1 and |Delta|<=H(K+1). Since A>=3H^2, sH<=1. Taylor's
theorem gives

   exp(s Delta) <= 1+s Delta+(s^2/2)Delta^2 exp(s|Delta|).

Conditionally on the parent type,

   E[Delta^2 exp(s|Delta|)]
      <= (H^2/p) E_Pois(c)[(K+1)^2 exp(K+1)]
      = (H^2/p) e [(ce)^2+3ce+1] exp(c(e-1))
      <= A.

The Poisson identity follows by differentiating its probability generating
function twice. The last bound uses e<3, c<=C and exp(2C)<=3^ceil(2C).
For completeness e<3 follows from its positive series and j!>=2^(j-1)
for j>=2, with strict inequality for j>=3. Consequently

   E[exp(s Delta)|past] <= 1-s+s^2 A/2
                         = 1-s/2 <= exp(-s/2).

Let Q_r be queue weight after r processed particles and tau its emptying
time. Then exp(s Q_(r wedge tau)+(s/2)(r wedge tau)) is a nonnegative
supermartingale with initial value exp(s h_i). On {tau>r} its value is
at least exp(sr/2), so Pr(tau>r)<=exp(s h_i-sr/2). In particular tau is
finite almost surely. At emptying Q_tau=0. Fatou's lemma applied to the
stopped supermartingale proves (1). Since tau=T_i, this proves the claim.
No multiplication of marginal offspring probabilities is used.

## Consequences for C023 and C024

Every C_ab is a mixture of root types, so (1) also holds with T_i
replaced by C_ab. For any sigma-field F, Jensen's inequality gives

   E exp(theta E[C_ab|F]) <= E exp(theta C_ab) <= e.

For S=sum_(a>b) C_ab over the six four-state pairs, convexity applied to
the average of six exponential terms gives

   E exp(gamma S) <= (1/6) sum_(a>b) E exp(theta C_ab) <= e.

This does not require independence among the six costs. Thus C023's
canonical weights and their sum v_t=E[S|H_t] obey the same appropriate
exponential-moment bounds uniformly in the finite history length t.

For any nonnegative X with E exp(gamma X)<=e and any R>=0,

   E[X 1{X>R}] <= (2/gamma) exp(-gamma R/2).

Indeed x exp(-gamma x/2)<=2/(e gamma); on x>R multiply this by
exp(gamma x) exp(-gamma R/2) and take expectations. C024's inventory
tail function therefore has the explicit bound

   A_inventory(L)=2c E[S 1{S>L/2}]
       <= (4c/gamma) exp(-gamma L/4).                  (2)

For a prescribed epsilon>0 it is sufficient to take
L>=max(1,(4/gamma)log(16c/(gamma epsilon))) to get
A_inventory(L)<=epsilon/4. C024's cardinality allowance can then be
epsilon/(4L), independent of t; its finite-n concentration rate may
still depend on t. This is a quantitative strengthening of its
uniform-integrability tail estimate, not a new finite-model theorem.

The bound is intentionally crude. C031 supplies no useful numerical rate
until the subinvariant inputs are explicitly enclosed, and it does not
compare the initial late-seed cost with every history-dependent class
depletion gate. C030 bounds duplicate multiplicity but not how many sites
are hit twice. Those probabilistic bounds and the planted-to-ER transfer
remain open. No new c_1 follows.

Sources: own C009's stationary conditioned offspring law and C023's
conditional-expectation weights; standard exponential-supermartingale
derivation displayed in full. Exact rational controls in the companion
script exercise the Taylor step, negative drift and Jensen inequality,
not a numerical certificate for any T186 fixed point.
