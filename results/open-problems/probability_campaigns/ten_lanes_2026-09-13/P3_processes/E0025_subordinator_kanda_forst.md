# E0025 - An explicit pure-jump subordinator whose Kanda-Forst ratio is unbounded

Continuous-time stochastic processes, 13 September 2026.

## The problem and its source

Corpus id `E0025`, source `hunts_hypothesis_survey_2019`, locator "Question 5, PDF p. 25". The
source is Z.-C. Hu and W. Sun, *Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond*,
arXiv:1908.06825 (2019). Its Question 5, as printed:

> Does any pure jump subordinator with infinite Levy measure satisfy (H)? More generally, does any
> pure jump n-dimensional Levy process satisfy (H)? The latter question has been presented in [23].

("Any" here reads as "every" in the surrounding usage; the survey also says, of the narrower
type-(alpha,beta) class of Definition 2.28, that "it is still unknown if any pure jump subordinator
of type-(alpha,beta) satisfies (H)", which is the weaker "even one" reading. I attack neither
reading directly; what follows is about the standard *route* to (H).)

Every classical sufficient condition for (H) - Kanda-Forst, Rao, and the survey's own extensions -
is a statement controlling Im(psi) by 1 + Re(psi), where psi is the Levy-Khintchine exponent. The
Kanda-Forst condition is

    |Im psi(z)| <= M (1 + Re psi(z))   for all z in R, some M < infinity.

The previous attempt in the ledger (`E0025-A001`) argued that for a driftless subordinator
with a genuine stable-like scaling exponent the ratio is bounded (hence (H) holds), and that the
open case is a Levy density with oscillating scaling, where "the ratio can be unbounded". That was
asserted, not constructed. The theorem below constructs one.

## Result

**Theorem.** Let

    x_m = 4^(-m^2),    a_m = 2^(-m) 4^(m^2)    (m = 1, 2, 3, ...),
    nu  = sum_m a_m delta_{x_m}.

Then nu is the Levy measure of a driftless subordinator with infinite Levy measure (so the process
is pure jump, of infinite activity), because

    integral (1 and x) nu(dx) = sum_m a_m x_m = sum_m 2^(-m) = 1 < infinity,
    nu((0,infinity)) = sum_m a_m = infinity      (a_m -> infinity),

and its exponent psi(z) = integral (1 - e^{izx}) nu(dx) satisfies

    sup_z |Im psi(z)| / (1 + Re psi(z)) = infinity.

More precisely, along z_m = 1/(m x_m) = 4^(m^2)/m,

    |Im psi(z_m)| / (1 + Re psi(z_m)) = 4m + O(1).

So the Kanda-Forst condition fails for this process, and with it the route through Rao's condition
(which contains Kanda-Forst and is likewise a pointwise bound of |Im psi| by an increasing function
of 1 + Re psi - the same mechanism defeats both).

## Proof

Everything converges absolutely: |1 - e^{izx}| <= min(2, |z| x), so
integral |1 - e^{izx}| nu(dx) <= |z| integral x nu(dx) = |z| < infinity. Hence

    Re psi(z) = sum_m a_m (1 - cos(z x_m)) >= 0,   Im psi(z) = - sum_m a_m sin(z x_m).

Fix m and put z = z_m = 1/(m x_m). Split the sum at index m.

*Fine blocks (j >= m).* Here z_m x_j = (1/m)(x_j / x_m) <= 1/m. The j = m term gives
a_m sin(1/m) in Im and a_m (1 - cos(1/m)) in Re. For j > m, x_j / x_m = 4^{-(j^2 - m^2)} is
astronomically small, so sin and 1 - cos are replaced by their leading terms to any accuracy. Hence

    Im contribution = -( a_m sin(1/m) + z_m sum_{j>m} a_j x_j ) + tiny
                    = -2^{-m} 4^{m^2} ( sin(1/m) + 1/m ) + tiny,
    Re contribution =  a_m (1 - cos(1/m)) + (z_m^2/2) sum_{j>m} a_j x_j^2 + tiny.

Since a_j x_j = 2^{-j}, the first is 2^{-m} 4^{m^2} (sin(1/m) + 1/m) ~ 2 a_m / m; and since
a_j x_j^2 = 2^{-j} x_j <= 2^{-j} x_{m+1}, the second sum is negligible against
a_m (1 - cos(1/m)) ~ a_m/(2 m^2). Ratio of the two: (2/m) / (1/(2 m^2)) = 4m.

*Coarse blocks (j < m).* Here |sin| <= 1 and 0 <= 1 - cos <= 2, so the whole coarse contribution is
bounded in modulus by 2 sum_{j<m} a_j <= 4 a_{m-1} = 4 * 2^{-(m-1)} 4^{(m-1)^2}. Compare with the
fine Im contribution ~ 2 a_m / m:

    (2 a_m / m) / (4 a_{m-1}) = (1/(2m)) * 2^{-1} * 4^{m^2 - (m-1)^2} = 2^{3m - 2} / m -> infinity,

so the coarse blocks are negligible on both sides. Therefore
|Im psi(z_m)| / (1 + Re psi(z_m)) = 4m (1 + o(1)).                                          QED

## Numerical verification

Computed at 4000-digit precision (the phases z_m x_j for j < m are exact rationals
4^{m^2 - j^2}/m of enormous size, so ordinary double precision is useless here), summing 400 blocks
(the tail is controlled by a_j x_j = 2^{-j}):

    m      z_m            Re psi        |Im psi|      |Im|/(1+Re)
    1      4.0            0.927212      3.6829         1.911
    2      128            8.17018       63.7861        6.9558
    3      8.7381e4       1898.19       21699.3       11.4256
    4      1.0737e9       8.3515e6      1.33501e8     15.9853
    5      2.2518e14      7.01701e11    1.40272e13    19.9903
    6      7.8706e20      1.02251e18    2.45388e19    23.9987
    7      4.5273e28      2.52213e25    7.06193e26    27.99989
    8      4.2535e37      1.03711e34    3.31875e35    32.000008
   10      1.6069e59      7.83984e54    3.13594e56    40.000005
   12      4.1444e85      4.21342e80    2.02244e82    48.000003

The measured ratio converges to 4m to eight digits, exactly as the proof predicts, and
sum_m a_m x_m came out as 1.0 to twelve digits.

## Why a single scale is not enough

It is worth saying what the multi-scale structure buys, because the failure looks easy from a
distance. A one-atom measure nu = a delta_x with a x = 1 gives ratio
a |sin(theta)| / (1 + a(1 - cos theta)), theta = z x, whose supremum over z is about sqrt(a/2) -
large, but finite. A *fixed* process has an unbounded ratio only if arbitrarily large a_m appear,
and a_m -> infinity together with sum a_m x_m < infinity forces x_m -> 0 fast. The construction
above is just the cheapest way to arrange that. The process is, in effect, a drift of rate 1 built
out of ever-smaller jumps; uniform motion x -> x + t is the textbook Levy process that fails both
Kanda-Forst and (H), and this is its pure-jump approximation.

## Does it settle Question 5? No

The natural hope is that this process also fails (H), which would answer Question 5 negatively.
It does not look that way. By the Kesten-Bretagnolle criterion, singletons are non-polar for a
one-dimensional Levy process that is not compound Poisson exactly when
integral Re(1/(1 + psi(z))) dz < infinity. Estimating that integral octave by octave (z from
1/x_m to 1/x_{m+1}, substituting z = s/x_m) gives a contribution of order 1/(a_m x_m) = 2^m per
octave, which diverges. So the integral is infinite, points are polar, and the tiny-jump
approximation to a drift is *not* the drift in the way that matters for (H): the frequencies where
Re psi is small are too sparse to make hitting cheap.

That octave estimate is a calculation, not a proof: it uses a "typical" size for Re psi on each
octave, and no lower bound on Re psi off the exceptional frequencies is proved. Label it
**numerical/heuristic**. The exact obligation is below.

## Status

- The construction and the identity ratio = 4m + O(1): **proved**, and confirmed numerically.
- Points are polar for this process: **estimated, not proved**.
- Whether the process satisfies (H): **unknown**. Question 5 is untouched.

## Literature check

Searches run 2026-09-13: "Kanda Forst condition subordinator", "Hunt's hypothesis subordinator Kanda
condition fails", "Levy process Kanda-Forst unbounded imaginary part", "Rao's condition Levy process
Hunt hypothesis", "Getoor's conjecture Hunt hypothesis semipolar polar", plus post-2019 sweeps
("Hu Sun Hunt's hypothesis independent sum 2023 2024 2025", "pure jump subordinator Hunt's hypothesis
2020-2024"). No published explicit process with an unbounded Kanda-Forst ratio was found, and
nothing since 2019 resolves Questions 5, 6 or 7 or the type-(alpha,beta) problem.

That such processes exist is clearly *known* rather than new: the survey's Theorem 2.8 (the extended
Kanda-Forst-Rao condition) is built precisely for them, and its Remark 2.21 says outright that the
condition "does not require any controllability of Im(psi) by 1 + Re(psi)". So the value here is a
concrete, checkable witness with a computed rate, not a discovery.

## Remaining obligation

1. Prove the polarity claim: a lower bound Re psi(z) >= c a_m for z in the m-th octave outside a
   sparse exceptional set, which turns the octave estimate into a proof that
   integral Re(1/(1 + psi)) dz = infinity.
2. Decide (H) for this process - e.g. test it against the survey's Theorem 2.8 (EKFR). If it
   satisfies (H), it is a clean example that (H) holds far outside Kanda-Forst and Rao; if it fails,
   Question 5 is answered negatively. Either outcome is worth having, and the process is explicit
   enough that both directions are computable.
3. Make the example a *density*, not atoms: the survey's type-(alpha,beta) class (Definition 2.28)
   requires a Levy density with c^{-1} x^{-(1+alpha)} <= rho(x) <= c x^{-(1+beta)} on (0,1]. A
   density smears the phases, and whether the ratio can still be unbounded inside that class is the
   question the survey actually cares about. The atomic construction does not answer it.
