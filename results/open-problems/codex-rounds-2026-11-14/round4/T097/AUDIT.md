# Independent checks and attempted failures

## The predecessor's assertions

For the shell minimization, Lagrange multipliers give the reciprocal
resistance sum directly, independently of its Cauchy-Schwarz proof.
With v=k(k+1), the denominator product in its telescoping identity is
144v^2+24v+13; the subtracted product is 144v^2+24v-3. The difference
16 is positive. Thus its asymptotic coefficient 4, correction 1/3, and
the scope of its restricted optimality are correct.

Its crossover coefficient can be checked by solving the leading constraint
from Holder rather than its normal-tail estimate. At capacity coefficient
4 and arm upper logarithmic exponent 2, the negative logarithm of the
probability ratio at R=c t^-2/log(1/t) is bounded above asymptotically by
sqrt(32c). Equating that expression with log 2 gives (log 2)^2/32.
The q>4 restriction in Muirhead's theorem is respected by retaining an
epsilon until the final limit.

## The unit-cell transfer in a second form

Define the averaging operator AF(y)=integral_Q F(y+z) dz. The fundamental
theorem along e_i gives

    AF(x+e_i)-AF(x) = integral_0^1 A(partial_i F)(x+u e_i) du.

Cauchy-Schwarz first in u, then Jensen in the cell, bounds its square by
the integral over Q times [0,1] of |partial_i F|^2. Summing x gives the
continuum integral because the cells at each fixed u form a tiling.
This recovers (7) independently by treating averaging and the line
derivative as successive contractions. There is no extra factor from
overlapping shifted cells: for fixed u they do not overlap except on
boundaries, and the u interval has length one.

Check with a slowly varying plane function in one coordinate: the
discrete sum approaches its continuum integral with coefficient one.
Thus a factor 1/2 or 2 in the transfer would be inconsistent. The energy
factor 1/6 is also fixed by expansion: each vertex has six incident
edges, giving coefficient one on sum f(x)^2 and coefficient -1/3 on
the unordered nearest-neighbor products, as required for I-P.

A cube of half-side R, without the enlargement by 1/2, does not suffice.
The cells centered at boundary vertices extend outside it and their
averages need not equal one. This potential missing case is the source
of the explicit additive C_cube/2 in the new bound.

## Geometry checked by parallel volume instead of gradient integration

The solid parallel body at distance s from [-a,a]^3 decomposes into:

    cube:             volume 8a^3;
    six face slabs:   volume 24a^2 s;
    twelve wedges:    volume 12*(2a)*(pi s^2/4)=6pi a s^2;
    eight corners:   volume 4pi s^3/3.

Differentiating its volume gives

    S_a(s)=24a^2+12pi a s+4pi s^2,

agreeing with the direct face/edge/corner integration in PROOF.md.
The large-s term is the full sphere area 4pi s^2, and S_a(0)=24a^2 is
the cube area. Both endpoints have the expected units of length squared.
Its reciprocal integral has units of inverse length; capacity therefore
scales linearly, rather than quadratically, with a.

## Optimization and exact integral checked separately

For a fixed T, Euler's equation for minimizing integral S_a u'^2 gives
(S_a u')'=0. The boundary values u(0)=1, u(T)=0 force
`u'=-1/(I_{a,T} S_a)`, giving energy 1/I_{a,T}. Strict convexity in u'
shows uniqueness. This checks the Cauchy-Schwarz calculation.

To verify J without partial fractions in v, complete the square and put
w=2v+3. Then

    24+12pi v+4pi v^2 = pi(w^2-delta^2),
    J = (1/(2pi)) integral_3^infinity dw/(w^2-delta^2)
      = log((3+delta)/(3-delta))/(4pi delta).

Multiplication by 6 and inversion gives precisely C_cube in (1).
The logarithm has positive argument greater than one, so C_cube>0.
No value of delta was obtained by floating-point arithmetic.

As a magnitude check, for v>=0,

    24+12pi v+4pi v^2 >= 4pi(1+v)^2.

It follows that J<=1/(4pi) and C_cube>=2pi/3. Together with C_cube<3,
this places the coefficient in a reasonable range and checks the sign
of the reciprocal. It does not identify the actual cube capacity.

For another check on the upper bound, minimize the rational trial-family
energy in PROOF.md (11) directly over lambda>0. The minimizing value is
lambda=sqrt(6/pi), with energy coefficient

    pi/3 + sqrt(32pi/27).

It is at most the value at lambda=3/2, namely 8/9+2pi/3. The optimized
distance-profile coefficient C_cube is no larger than either value.
This check uses differentiation of an explicit trial family, separately
from the exact logarithmic integral. The three elementary integrals
in (11) can also be obtained by substituting z=v/(lambda+v); their
dimensionless factors are respectively 1/3, 1/6, and 1/3.

## Infinite tails and nonsmooth pieces

The limiting profile behaves as a constant times 1/s, so it need not be
square integrable in three dimensions. It is not inserted directly into
the finite-support lattice variational problem. Each finite-T optimized
profile is admissible first, and the limit of its energy is then taken.
The rational trial family is likewise truncated and renormalized before
being used. This avoids a hidden assumption about approximation in L^2.

The distance function and its finite-T profile are Lipschitz. They are
differentiable almost everywhere; the exceptional sets at the cube and
outer boundary do not contribute to the line integrals or energy. There
is no jump at either boundary. Absolute continuity along lines justifies
the unit-cell transfer without assuming a smooth rounded boundary.

## The new crossover coefficient from normal tails

As an independent check of the Holder proof, the Gaussian likelihood-ratio
rearrangement gives

    p_R(h+t) >= Q(b+s),
    Q(b)=p_R(h), s=t sqrt(cap(B_R)).

For b>=0, Jensen gives
`Q(b+s)/Q(b)>=exp[-s^2/2-s lambda(b)]` with lambda=varphi/Q.
Integration by parts gives lambda(b)<=b+1/b for b>0, and consequently
lambda(b)<=b+2 for all b>=0. Also b<=sqrt(2 log(1/p)). At h=h_* we
have p_R(h_*)<1/2 since h_*>0, so this applies. Set H=log(1/t) and
R<=c/(t^2H). The leading upper bounds are

    s^2 <= C_cube c/H+O(t^2),
    log(1/p_R(h_*)) <= (4+2epsilon)H.

Thus the maximal leading loss is sqrt(4 C_cube c (2+epsilon)). The
remaining +2s and s^2/2 vanish. Letting epsilon decrease to zero gives
sqrt(8 C_cube c), and hence (log 2)^2/(8 C_cube), agreeing with Holder.

The new coefficient divided by the old one is 4/C_cube>4/3. This checks
the direction: a smaller capacity upper bound gives a larger guaranteed
relative radius. Finite R, floor errors, and the uniform check over all
smaller radii are explicitly handled in PROOF.md. No monotonicity of
the probability ratio in R is assumed.

## Attempts to obtain a stronger conclusion

Setting R=c t^-2 makes the loss s sqrt(log(1/p_R(h_*))) grow in this
argument. The smaller constant does not remove that divergence. The
predecessor's increasing half-space example still obstructs an improvement
valid for all increasing events. No connection-specific estimate was found.

The averaging construction gives an upper bound, not a matching lower
bound on capacity, and no exact value for its true leading coefficient.
The optimization is only over distance profiles before averaging; further
angular variation could improve it. Neither exact lattice exponents nor
an equivalence with a conventional correlation length follows.

No numerical script, simulation, decimal evaluation, or heavy computation
was run. All load-bearing factors were re-derived algebraically or by an
independent analytic argument.
