# Independent checks of the rank-occupation identity

## 1. A direct monomial calculation

Consider h(x)=product_(j=1)^k x_(a_j) at a state with a unique spatial
minimum of color b. If b is outside the k root colors, deleting a minimum
does not change h. Summing births in those k colors gives generator h=kh,
which agrees with (1).

If b is one of the k colors, assume first all k counts are positive and
write h/x_b for partial_b h. Births of color b make no net change. A birth
in another included color a has change

    h * [1/x_a-1/x_b-1/(x_a*x_b)].

There are x_a such parents, so this contributes
h*[1-(x_a+1)/x_b]. A birth in an excluded color contributes -h/x_b per
parent. Summing, and using that all counts add to N, gives

    (k-1)h - (h/x_b)*[(N-x_b)+(k-1)]
      = kh-(N+k-1)partial_b h.

If an included count is zero, that color is extinct and cannot be the
minimum color. It stays zero forever. Both h and partial_b h are zero,
so the same identity holds. Linearity proves the formula for F. This
does not use Euler's identity, which was the proof's derivation.

For k=4, comparison with round 5 gives R=(N+3)partial_b F. Thus the
coefficient is independently fixed before invoking any auxiliary law.

## 2. Generator check of the marked-history proof

Fix k different initial root colors. At a colored population configuration
xi, let Bf(xi) be the sum of f over all tuples with one distinguished
current individual of each specified root color. There are
product_j W_(a_j) such tuples. Extend f by zero at the cemetery state.
Let L be the original generator and K the killed marked generator.

At a birth, any post-birth distinguished tuple has a unique pre-birth
tuple: trace a distinguished daughter to her parent. A pre-birth tuple
has one possible continuation if the parent is undistinguished and two
possible continuations if the parent is distinguished, before deletions
are imposed. The two latter outcomes have coefficient one each under K,
since each has rate 2 times daughter probability 1/2. A removed mark
contributes zero. These observations identify all off-diagonal terms of
L Bf and B Kf. The original waiting rate is N and the killed marked
waiting rate is N+k. Therefore

    L Bf = B Kf + k Bf.

Diffusion commutes with B since each summand assigns labels to existing
particles without changing their Brownian motion. Integrating the
intertwining identity gives

    S_L Bf = exp(kL) B T_L f,

where S and T are the original and killed semigroups. For example,
differentiate S_s B T_(L-s)f in s: its derivative is k times itself.
This can first be done on admissible bounded diffusion test functions;
the bounded-rate path expansion gives the extension to bounded measurable
f. Counts are bounded by N and all event rates by N+k. There is no
unbounded offspring count in this calculation.

At the initial time there is only one possible distinguished tuple.
Taking f=1 on live states gives exactly (4). This check obtains the
exp(kL) factor from generator diagonals, independently of the proof's
history-density ratio.

Taking f=the indicator that the minimum is distinguished yields the
conditional-survival interpretation of rho. For a current colored
configuration, Bf=partial_b h: fixing the actual leftmost individual
removes its one color factor from the tuple count. Sum this identity
over the admissible quadruples, keeping their multiplicities. Dividing
the resulting terminal-function identity by its f=1 version gives the
rho formula in (9).

## 3. Checks which expose wrong killing constants

With k=N and one particle of each root color, the original product of
all root counts is one until the first color extinction, and zero
forever afterward. A branch of the current minimum leaves every color
present. A branch of any of the N-1 other particles causes extinction.
The extinction hazard is therefore N-1 at all times, regardless of
positions or crossings, and

    E product_(j=1)^N W_j(L) = exp(-(N-1)L).

In the conservative marked process every particle is distinguished.
All births are suppressed, A_L=L deterministically, and (6) gives

    exp(NL)*exp(-(2N-1)L) = exp(-(N-1)L).

The two derivations agree. In particular N=k=4 gives exp(-3L). A
killing coefficient N, or N+k instead of N+k-1, fails this example.
The case N=k=1 gives the constant product one as it should.

For a second infinitesimal check, start at distinct positions and take
k root particles with count one. If the minimum is not among them,
the initial derivative of the product expectation is k. If the minimum
is among them, its own branch leaves the product one; each of the
other N-1 branches changes it from one to zero. The derivative is
-(N-1). The killed representation gives respectively k-0 and
k-(N+k-1)=-(N-1). This checks both the rate-two rule and the half-probability
death at a distinguished minimum's own branch.

## 4. An exact one-mark normalization

Choose one initial root uniformly among the N particles, independently
of their positions. Under the original process,

    E W_(uniform root)(L) = (1/N) E sum_v W_v(L) = 1.

Formula (6) with k=1 therefore gives, under the corresponding mixture
of conservative single-mark laws,

    E^circ exp(-N A_L) = exp(-L).

The same equality follows from the aggregate polynomial
F(x)=sum_v x_v=N: generator F=F-N*partial_b F=N-N=0.
Consequently the minimum is marked with probability exactly 1/N under
the uniform-root killed law conditional on survival, at every positive
time. This is an identity for that particular mixture, not permission
to replace rho by k/N for an ancestral-filtered mixture.

Indeed, for a specified tuple at a separated initial configuration, the
initial marked-minimum indicator can be zero or one. The filtered
quadruples need not choose spatially uniform marks. The separated-leader
example from round 5 chooses marks far from the minimum and is consistent
with survival nearly one on a fixed horizon. Thus the representation
does not bypass that obstruction to uniform propagation improvements.

## 5. Occupation lower tail and restored weights

The product bound used in (10) is pointwise. If all k counts are
positive, their sum is at most N and their arithmetic mean bounds
their geometric mean by N/k; if a count is zero the conclusion is
automatic. Restoring exp(kL) in (6) verifies the direction of (10).
On A_L<=a, exp(-(N+k-1)A_L) is bounded below, not above, by
exp(-(N+k-1)a). Dividing verifies (11) and substitution verifies (12).

Another check uses Jensen's inequality in the direction

    exp(-(N+k-1) E^circ A_L)
      <= E^circ exp(-(N+k-1) A_L)
      <= (N/k)^k exp(-kL).

It implies the consistent mean constraint

    E^circ A_L >= max(0, [kL-k log(N/k)]/(N+k-1)).

This is weaker than exponential occupation control for the required
kernel. Knowing a mean occupation cannot upper-bound its negative
exponential moment; Jensen gives the reverse direction. A small lower
tail can dominate that moment after multiplication by exp(kL).

The bound in (10) is exactly the original elementary bound in new
variables. It cannot prove decay of the filtered statistic by itself.
No estimate under the true younger-configuration law has been proved.

## 6. Boundary cases and limits of the statement

- At L=0, A_L=0 and the kernel is one. At the sampling endpoint, (7)
  is exactly |C|/(N)_4, with no terminal propagation.
- If C is empty, the filtered polynomial is identically zero and the
  sum in (7) is empty. No division by |C| is made.
- Loss of one root color makes that monomial identically zero forever.
  The killed-history formulation represents this without resurrecting a
  mark or introducing correlations by an independence assumption.
- Ordinary particles may share a root color with a distinguished particle.
  Killing concerns the individual carrying the mark, not every deletion
  of its color. Summing over all possible distinguished individuals is
  what recovers the product of counts.
- Daughter tie decisions must not consult auxiliary marks. At other times
  pre-birth spatial ties have probability zero. Collision times have zero
  occupation measure, so the definition of A_L there is immaterial.
- Suppression at a distinguished minimum applies only to the conservative
  auxiliary law. It is not a modification of the original N-BBM.
- The outer expectation in (13) is indispensable: the original frozen
  forest determines both C and the positions. Uniform unfiltered marks,
  stationary particle assumptions or ordinary N-BBM rank probabilities
  cannot be substituted without an additional proof.

These checks establish the finite-N representation. They supply neither
the log-cubed-time averaged estimate nor a genealogy convergence theorem.
