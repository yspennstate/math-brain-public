# Lead review: C014/C015 v1 stopped birth forest

The exact joint proof is SHA256
29593274c1dd79d14dfee5963e41bd24c26b2d51febaf77f5753bc8bb47e26d7.
I rederived the all-size argument, independently of its finite graph checks.
PASS for the stated sufficient finite positive-core bounds, with the exact
constant calculation in T186_UPPER_CONSTANTS_RECEIPT.json. Priority and
the exact finite onset are not asserted.

The peeling invariant preserves every strong subset of the black set: a
selected vertex touching one would have at least k black neighbours. Terminal
black is therefore the unique maximal strong core. Newly nonblack vertices
have a birth parent or are new red roots; acyclicity follows from birth time.
Each red vertex has at most k-1 children; a blue vertex has no children until
it is selected red. At the first nonblack-size crossing, only k consecutive
sizes are possible. The rational n0 ensures each is within theta_plus*n.

For a FIXED coloured rooted forest on T, the e required forest edges are
internal and the r(n-|T|) forbidden red-to-outside edges are external. Thus
their Bernoulli edge variables are distinct, giving the single witness
probability p^e(1-p)^[r(n-|T|)]. No dependent per-vertex red probabilities are
multiplied. Including impossible witnesses and ignoring extra internal edges
only enlarges the union bound.

Labelled unordered children give A=x z E_(k-1)(p(x+A)); unordered red-rooted
components give exp(A), including both necessary factorials. At x=nu, height
truncations divided by n iterate a -> u z E_(k-1)(c(u+a)). Criterion A keeps
them below R. Monotone convergence justifies the complete series evaluation.
Nonnegative coefficient extraction yields (n)_i n^(-i)u^(-i)exp(nR).

The polynomial inequality x E_m'(x)<=m E_m(x) makes exp[-c(1-theta_plus)]
E_m(c(u+R)) nonincreasing throughout c>=c0. This supplies uniformity in c
without assuming edge-monotonicity of the strong core. For decreasing
f(x)=log(1-x), the left Riemann sum exceeds the integral by at most
f(0)-f(i/n), giving the prefactor 1/(1-i/n). H'(t)=log(u/(1-t))>0 on the
whole stopped range. Criterion B then supplies exp(-delta*n), and the union
over at most k stopped sizes gives the exact stated constants. The rounding
n-ceil(theta*n)=floor((1-theta)*n) gives the claimed strict density event.
The complete-graph endpoint c=n also satisfies the static witness bound.

My own 200-bit Arb calculation uses exact rational inputs and no author
solver imports. Both strict inequalities, both n0 conditions and both rational
prefactors pass. It agrees with the independently saved w683 512-bit bounds
and w679's different Fraction-series check. Their exact-version PASS records
are reconciled in T186_UPPER_RECONCILIATION.json. w683's saved text saying a
separate review was pending is superseded by the independently located w679
PASS receipts on this same complete proof hash.

No tree fixed point or conditional WP transfer is a premise of this upper
bound. Its conclusion does not lower the separate circumference cutoff
c=13.962, establish an exact strong-core threshold, or prove complement tails.
