# Independent checks and failure tests

## 1. Conditional growth factor

The unselected-tree argument in PROOF.md bounds each four-color product
by a product of four independent means. Independently, examine one monomial
m=x_a x_b x_c x_d. A birth of color a contributes x_b x_c x_d, and its
total rate is x_a, so the birth contribution is m. The other three colors
give the same contribution; colors absent from the monomial give zero.
Thus the birth generator is exactly 4m. Deleting the leftmost particle
after the birth subtracts a nonnegative derivative. Summing monomials gives
the separate generator derivation of the factor exp(4L).

For a birth and deletion of the same color a, the deletion derivative
equals the birth derivative, because m has degree one in x_a. The net
change is zero, as it must be. For different colors a and b in m, direct
expansion gives

    m(x+e_a-e_b)-m(x)
       = partial_a m(x)-partial_b m(x)-partial_a partial_b m(x).

This is exactly partial_a m(x)-partial_b m(x+e_a), including the cross
term. Evaluating the deletion derivative before the birth would miss that
term. Formula (4) uses the correct post-birth argument.

The generator is applied to the full positions-and-colors process, not
to an asserted Markov process of family counts alone. The identity and
conditional expectation therefore do not require a Markov assumption on
the sampled backward genealogy.

## 2. Counting the coefficient eight and the sampling coefficient

For the separated configuration the middle families are A={1,2} and
B={3,4} at the younger time. For one prescribed pairing, choose which
middle family supplies its first pair (two choices) and the order within
each pair (two choices each). The number of ordered younger-color
quadruples is 2*2*2=8. Future terminal choices multiply each by
W_1 W_2 W_3 W_4. This reproduces F=8 product_j W_j independently of the
zeta formula.

Alternatively, an unordered sample qualifies exactly when it takes one
particle from each of the four colors. There are product_j W_j such
subsets. Division by choose(N,4) gives

    P(event | forest)=24 product_j W_j/(N)_4,

equal to 3Q. This independently checks both the denominator and the
pairing factor in the sharpness calculation. There is no contribution
from low colors even if a low color has many terminal descendants: those
descendants share their younger ancestor, which the event excludes.

## 3. The Yule and weighted-tail constants

Write p=exp(-L). The Yule law is geometric on positive integers, with
generating function g(z)=pz/(1-(1-p)z). Differentiation gives

    E Y=1/p,
    E(Y)_2=2(1-p)/p^2,
    E Y^2=(2-p)/p^2.

These agree with the generator equations m_1'=m_1 and
m_2'=2m_2+2m_1. Four independent copies give
E P_L=exp(4L) and E P_L^2=exp(8L)(2-exp(-L))^4.

There is a second check of E[P_L Z]/E P_L. Weighting the four independent
geometric variables by their product makes each size-biased, independently.
Its mean is E Y^2/E Y=2exp(L)-1. The sum of four such means is
8exp(L)-4, precisely the factor in (12). An ordinary unweighted Markov
bound on P(Z>=N) would not suffice to bound E[P_L 1_{Z>=N}]; the proof
instead bounds that weighted expectation by E[P_L Z]/N.

For the short-window bound, count unordered pairs of different middle
families. Their expected unordered terminal-pair product is at most
[exp(ell)(exp(ell)-1)]^2. There are N(N-1)/2 such family pairs. Division
by choose(N,4) gives 12 exp(2ell)(exp(ell)-1)^2/((N-2)(N-3)),
independently reproducing the constant in (6).

## 4. Spatial separation and selection

For a second Brownian maximum bound, stop the martingale
exp(lambda B_t-lambda^2 t/2) at the first hit of r or at L. Nonnegativity
and bounded stopping give

    P(sup_(t<=L) B_t>=r) <= exp(-lambda r+lambda^2 L/2).

Set lambda=r/L and apply the same argument to -B. This gives
2 exp(-r^2/(2L)) for the two-sided maximum, which is stronger than the
factor-four reflection bound used in the proof. Therefore the conservative
constant 4 in b_N is valid. Substituting r=N/3 gives the denominator
2*3^2=18 in the exponent.

No independence between Brownian crossing and Yule population size is used
in the error estimate: Cauchy–Schwarz bounds their joint weighted error.
Conditional on the entire unselected branching tree, each concatenated
leaf path still has Brownian law, which suffices for the expected-leaf
counting bound.

If no leader has been removed and Z(L)<N, at least one low particle is
available at every deletion. On a leader birth the post-birth leader count
is at most Z(L)<N; on a low birth it remains at most Z(L). Since the
selected post-birth total is N+1, low particles are present in either case.
Their strict spatial separation makes the deletion low. This checks the
induction without assuming independence of the selected families.

The older and middle labels are compatible with an actual binary prefix.
The positive-probability prefix may be extremely rare; no lower bound on
its probability in the all-zero observation regime is claimed or needed
for sharpness of a bound uniform over marked configurations.

## 5. Limits, scales and numerical constants

For L_N<=(1-eta)log N the saturation error in (13) is at most 8N^(-eta).
Also b_N(L_N)<=4N^2 exp(-N^2/(18log N)). Both errors vanish, uniformly
over this range. This proves relative sharpness of exp(4L_N), rather than
just convergence at a fixed future horizon.

At L_N=log(N/16), independently compute the weighted mean saturation
ratio as

    (8(N/16)-4)/N = 1/2-4/N.

The remaining spatial error tends to zero. The ordered-sample coefficient
is 24 and the surviving fraction of its unselected expectation has liminf
at least 1/2. Therefore the probability lower bound is

    (24/2)/16^4 = 12/65536 = 3/16384.

The unordered-sample calculation in Section 2 gives the same number:
E product_j W_j has liminf after division by N^4 at least 1/(2*16^4),
and choose(N,4)/N^4 tends to 1/24.

Finally, K_N(h)=48h^2/((N-2)(N-3))+O_N(h^3). Integrating the future
factor over 0<=s<=T gives (exp(4T)-1)/4. Multiplication by 1/h in the
sliding-window argument yields the coefficient
12(exp(4T)-1)h/((N-2)(N-3)) in (8). This checks the physical clock
calculation independently of its displayed formula.

## 6. What the result does not permit

The sharpness example does not disprove an estimate averaged over the
actual long-time N-BBM spatial law. It disproves smaller universal
multiplicative propagation factors over all marked configurations. A
fixed L and a fixed rescaled s are different: the latter makes L of
order (log N)^3, where the propagation bound is useless. No interchange
of these limits occurs in the proof.

The conditional sharpness statement at a chosen younger state is also
different from an unconditional genealogy law at a fixed late observation
time. All sample times used in the example after that state are
deterministic; no random hitting-time observation is substituted.

No failure was found in the new estimates. No computational evidence,
N-BBM log-cubed asymptotic bound, convergence theorem, or rate constant
is claimed.
