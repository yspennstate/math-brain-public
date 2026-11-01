# A transitive mod-8 family defeats favorable-coordinate and aggregate restriction

Status: proved below and self-checked; novelty **UNVERIFIED**. This is an
obstruction to using the unequal-NAND potential in any constant-charge
coordinate-restriction induction. It is not a counterexample to FEI.

All logarithms are base two unless `ln` is written. For an indicator `A`, let

    W_c(A)=U(A)+c Q_A,

with `U,Q_A` as in `UNEQUAL_NAND_CONTRACTION_2026-09-18.md`. The contracting
NAND potential is `V=W_{2/ln2}`.

## 1. The theorem

For `n` divisible by 8, define the symmetric indicator

    A_n(x)=1{|x| mod 8 is in {0,1,2}}.                 (1)

For any coordinate `i`, let

    D_i(A_n)=W_c(A_n)
       -[W_c((A_n)_{i=0})+W_c((A_n)_{i=1})]/2.         (2)

For every fixed real `c`, there is an explicit constant

    gamma=(3 sqrt(2)/8) sin^2(pi/8)
             log_2(cot^2(pi/8)) > 0                   (3)

such that

    D_i(A_n)/Inf_i(1-2A_n)=gamma n+o(n).               (4)

Numerically, `gamma` is about `0.19751`. Since (1) is invariant under every
permutation of the coordinates, all coordinate defects and influences are
equal. It follows that no finite `C` can make either of the following true for
all Boolean indicators:

    some i satisfies D_i(A)<=C Inf_i(1-2A),            (5)

or

    sum_i D_i(A)<=C sum_i Inf_i(1-2A).                 (6)

Thus the favorable-coordinate and aggregate versions left open by the bent
marker both fail for every fixed singleton correction `c`. In particular they
fail for the unequal-NAND potential.

This does **not** say `W_c(A_n)/I(A_n)` is unbounded. Restriction defect is a
difference between parent and child potentials, and (4) is a barrier to a
specific induction mechanism, not to FEI itself.

## 2. Fourier coefficients by an eighth-root filter

Put `omega=exp(pi i/4)`. For the period-eight sequence

    a_w=1{w mod 8 in {0,1,2}},

write

    alpha_r=(1+omega^(-r)+omega^(-2r))/8.              (7)

The Fourier coefficient of `A_n` at every set of size `k` is

    c_{n,k}=sum_{r=0}^7 alpha_r
       ((1+omega^r)/2)^(n-k)
       ((1-omega^r)/2)^k.                              (8)

Indeed, insert the root-of-unity filter
`a_w=sum_r alpha_r omega^(rw)` and factor the sum over the `n` input bits;
bits outside the Fourier set contribute `1+omega^r`, while bits inside it
contribute `1-omega^r`. This proves (8) exactly.

Set

    a=cos(pi/8),  b=sin(pi/8),
    q=b^2,        R=a^2/b^2=cot^2(pi/8),
    L=log_2 R.                                          (9)

The `r=1,7` pair is concentrated spectrally at levels `k=qn+O(sqrt n)`;
the `r=3,5` pair is concentrated at `(1-q)n+O(sqrt n)`; and the `r=2,6`
pair is concentrated at `n/2+O(sqrt n)`. These three windows are linearly
separated. Contributions from the wrong pair in any one fixed-width-linear
window are exponentially small by (8), and binomial tails outside the three
windows are exponentially small. Hence the limiting edge cost is the sum of
the three separate pair calculations below. This separation can equivalently
be made formal by taking windows of width `n^(2/3)` and applying the elementary
binomial Chernoff bound. For completeness, no hidden logarithmic factor spoils
this truncation: every coefficient is an integer multiple of `2^-n`, so every
nonzero squared-mass ratio has logarithm at most `2n` in absolute value. The
total degree of an endpoint is at most `n`. Thus an exponentially small tail
of squared spectral mass contributes at most `O(n^2 exp(-eta n))=o(n)` to the
edge functional. Inside each window the dominant conjugate pair is bounded
away from zero relative to its own envelope, so the other pairs change both
the masses and their logarithms by an exponentially small relative amount.

The endpoint terms `r=0,4` occur only at `k=0,n` and do not affect the internal
edge asymptotics.

## 3. Parent potential

Directly from (7),

    |alpha_1|=(sqrt(2)+1)/8,
    |alpha_3|=(sqrt(2)-1)/8,
    |alpha_1|^2+|alpha_3|^2=3/32.                      (10)

For `n=0 mod 8`, the conjugate `r=1,7` pair gives

    |c_{n,k}|=(sqrt(2)|alpha_1|+o(1)) a^(n-k)b^k       (11)

uniformly on its `qn+O(n^(2/3))` window: the phase cosine always has absolute
value `1/sqrt(2)`. Consecutive squared coefficients have ratio `b^2/a^2=1/R`.
After multiplication by the number `binom(n,k)(n-k)` of upward edges from
level `k`, the binomial identity gives

    K_low(A_n)/n -> 2|alpha_1|^2 q L.                  (12)

The `r=3,5` window gives the same formula with `alpha_3`. For `r=2,6`,

    c_{n,k}=2^(-n/2-2) sin((n-2k)pi/4),                (13)

up to the already separated exponentially smaller pairs. This vanishes at
every even level and has constant magnitude at every odd level. Every edge in
that limiting band therefore has a zero endpoint, so its logarithmic edge
cost is zero. Equations (10)--(13) yield

    W_c(A_n)/n -> kappa
       =2(|alpha_1|^2+|alpha_3|^2)qL
       =(3/16)qL.                                      (14)

The singleton coefficient is exponentially small, so both its entropy term
and `cQ_A`, for fixed `c`, are `o(n)`.

## 4. The two restrictions

Both restrictions live in dimension `N=n-1`. Their symmetric value sequences
are respectively `a_w` and `a_{w+1}`. Shifting the sequence multiplies
`alpha_r` by `omega^r`.

In the low `r=1,7` band of either child, the phase magnitudes alternate between
`b` and `a`. On one parity of `k`, consecutive squared masses are equal and
the edge cost is zero. On the other parity, the ratio is `R^2`, so the
logarithmic contrast is `2L`. The two parities have asymptotic binomial mass
`1/2` each. The resulting low-band limit for either child is

    K_low(child)/N -> 4|alpha_1|^2 b^4 L.              (15)

The high band gives `4|alpha_3|^2 b^4L`. In the middle `r=2,6` band, the
dimension shift changes (13) into a sequence of constant squared magnitude;
all consecutive edge costs are zero. Again the singleton corrections are
`o(n)`. Therefore both children have the same limit

    W_c(child)/N -> kappa_child
      =4(|alpha_1|^2+|alpha_3|^2)b^4L
      =(3/8)q^2L.                                      (16)

Subtracting (16) from (14), noting `N/n->1`, gives

    D_i(A_n)/n -> (3/16)q(1-2q)L.                      (17)

Since `q=sin^2(pi/8)` and `1-2q=1/sqrt(2)`, this limit is positive.

## 5. Influence and the normalized defect

Along any fixed coordinate, disagreement occurs exactly when the Hamming
weight of the other `n-1` bits is congruent to `2` or `7` modulo 8. Thus

    Inf_i(1-2A_n)
       =Pr[Bin(n-1,1/2) mod 8 is in {2,7}] -> 1/4.     (18)

The convergence follows immediately from the same root-of-unity filter; every
nonconstant Fourier mode has modulus strictly below one. Dividing (17) by
(18) gives (3)--(4).

Because symmetry makes every summand identical,

    [sum_i D_i]/[sum_i Inf_i]=D_1/Inf_1,

so (5) and (6) both fail.

## 6. Exact checks and consequence

`check_symmetric_mod8_restriction.py` computes the symmetric Walsh coefficients
as exact rationals using Krawtchouk sums, encloses every logarithm by 160-bit
outward rational intervals, compares the symmetric formula with full truth
table transforms in small dimensions, and verifies growing ratios through
`n=64`. The asymptotic theorem is proved by the root-of-unity calculation, not
by the finite data. The check is not an independent audit.

The unequal-NAND potential now has an exact boundary:

- it contracts under arbitrary unequal disjoint NAND composition;
- every-coordinate restriction fails on bent markers;
- even favorable-coordinate and aggregate restriction fail on the transitive
  mod-8 family.

Any continuation must use a genuinely different global payment, a nonlocal
block mechanism not reducible to summed one-coordinate defects, or the signed
Boolean convolution identities directly.
