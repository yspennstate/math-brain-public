# Independent audit of the three-crossing largest-weight obstruction

Date: 2026-10-02. Audited author files:
`three_crossing_largest_weight_obstruction.md`,
`verify_three_crossing_obstruction.py`, and
`three_crossing_obstruction_checks.json`.
The author proof and checker were not edited.

**Verdict: PASS.** The construction is exactly Boolean and has exactly three
crossings of one weighted linear form, with a unique largest-weight coordinate.
The analytic lower bound proves that its entropy split increment divided by
that coordinate's influence diverges. The argument is an obstruction to this
local largest-weight induction criterion, not a counterexample to FEI.
No mathematical gap was found. The numerical checks are correctly separate
from the asymptotic proof.

## 1. Exact Boolean encoding and physical influence

Let \(N=2d+1\ge3\), \(g=\operatorname{sign}(\sum_jx_j)\), and
\(D\) be the indicator of the all-minus input. With
\(\alpha=2^{-N}\), the restrictions are
\(f^-=g\) and \(f^+=g+2D\). At the only input where \(D=1\),
majority equals \(-1\), so the latter value becomes \(+1\), not 3.
Thus both restrictions are Boolean, and
\(A=g+D\), \(B=D\) give \(f=A+zB\). A flip of \(z\) changes
the value only at that one old input, so the physical flip influence is
exactly \(I_z(f)=\alpha\), with no factor two.

For \(w=N+1\), the score \(wz+\sum_jx_j\) is always odd, while
all three thresholds \(-w,2,w\) are even. The piecewise rule has three
actual sign changes and no attained threshold ties. When \(z=-1\),
all scores are negative; their crossing of \(-w\) is exactly the
crossing of the majority score through zero. When \(z=1\), the
all-minus score is 1 and is flipped positive; every other negative-majority
score lies strictly between 2 and \(w\), and every positive-majority
score exceeds \(w\). This proves the claimed equality to the two
restrictions at every cube input. The pivot weight \(w=N+1>1\) is
uniquely largest.

The values assigned exactly at the three thresholds can be arbitrary;
they do not affect this cube function or the number of sign changes between
successive attained-score regions.

## 2. Majority Fourier coefficients and their uniform lower bound

Oddness of majority under \(x\mapsto-x\) annihilates every even-size
coefficient, including its constant coefficient. For an odd-size set
\(|S|=2\ell+1\), choose one coordinate \(i\in S\). The discrete
derivative \((g(x_i=1)-g(x_i=-1))/2\) is the central-layer indicator
on the other \(2d\) inputs. Hence the coefficient equals the central-layer
probability times the average of a \(2\ell\)-coordinate character
on that layer.

Each central-layer input has \(d\) plus and \(d\) minus coordinates,
so summing those character averages over sets produces
\((1+t)^d(1-t)^d=(1-t^2)^d\). Exchangeability then gives exactly
\[
\widehat g(S)=(-1)^\ell
 \frac{\binom{2d}{d}}{4^d}
 \frac{\binom d\ell}{\binom{2d}{2\ell}}.
\]
There is no missing derivative factor or subset multiplicity.

The central binomial coefficient is the largest of the \(2d+1\)
terms summing to \(4^d\), so its normalized value is at least
\(1/(2d+1)\). Vandermonde gives
\[
\binom{2d}{2\ell}=\sum_{j=0}^d
 \binom dj\binom d{2\ell-j}
\le(d+1)\binom d\ell^2.
\]
Terms outside the binomial row are zero. Within the row, log-concavity
implies that each symmetric product about \(\ell\) is at most the
centered product. Since \(\binom d\ell\le2^d\), this proves
\[
|\widehat g(S)|\ge
\frac{2^{-d}}{(2d+1)(d+1)}
=\frac{2^{-(N-1)/2}}{N(N+1)/2}.
\]

The ratio of this bound to \(\alpha\) is
\(2^{d+1}/[(2d+1)(d+1)]\). At \(d=7\) it is
\(256/120>2\). Its successive ratio is
\(2(2d+1)(d+1)/[(2d+3)(d+2)]>1\) for \(d\ge2\).
Thus every odd-size coefficient has magnitude at least \(2\alpha\)
for all odd \(N\ge15\), exactly the range used in the proof.

## 3. Exact entropy increment and its divergent lower bound

For every old spectral set, put
\(a_S=\widehat g(S)+b_S\),
\(b_S=\widehat D(S)=\alpha(-1)^{|S|}\),
\(P_S=a_S^2+b_S^2\),
\(q_S=b_S^2/P_S\), and
\(r_S=(a_S+b_S)^2/(2P_S)\).
The established exact real-coefficient split identity is
\[
\Delta_zH=\sum_S P_S[1+h_2(q_S)-h_2(r_S)].
\]

For an even-size set, \(\widehat g(S)=0\), so
\(a_S=b_S\), \(P_S=2\alpha^2\), \(q_S=1/2\),
\(r_S=1\). The contribution is exactly \(4\alpha^2\).
There are \(2^{N-1}\) such sets, including the empty set; their total
is exactly \(2\alpha\).

For an odd-size set with \(N\ge15\), the preceding magnitude bound
and the triangle inequality give
\(|a_S|\ge|\widehat g(S)|-\alpha
\ge|\widehat g(S)|/2\). Since \(h_2(r_S)\le1\), its increment
is at least
\[
P_Sh_2(q_S)
\ge\alpha^2\log_2(P_S/\alpha^2)
\ge\alpha^2\left[N-1-
2\log_2\frac{N(N+1)}2\right].
\]
The first inequality retains the \(q\log(1/q)\) part of binary
entropy. The second uses \(P_S\ge a_S^2\ge\widehat g(S)^2/4\).
Its exponent and factor four give exactly the displayed \(N-1\),
not \(N+1\). Counting the \(2^{N-1}\) odd sets and adding the
even contribution proves
\[
\frac{\Delta_zH}{\alpha}
\ge\frac{N+3}{2}-\log_2\frac{N(N+1)}2.
\]
This is \(N/2-O(\log N)\), so it diverges along the odd dimensions.
The result is analytic and does not depend on a plotted trend or finite
coefficient computation.

For the upper bound, the included-component part of conditional spectral
entropy equals \(\alpha[\log_2(1/\alpha)-D(Q\|P)]\), where
\(Q_S=b_S^2/\alpha\). KL nonnegativity and
\(\ln(1+t)\le t\) bound the complete conditional entropy by
\(\alpha[N+\log_2e]\). The exact split identity also obeys
\(\Delta H\le2\mathcal C\). Hence
\(\Delta_zH\le2\alpha[N+\log_2e]\). Together with the lower
bound, this proves \(\Delta_zH=\Theta(N2^{-N})\).

## 4. Audit of the author's checker and results

The checker uses exact Fraction formulas for every majority coefficient,
the minimum coefficient comparisons, and each coefficient-pair mass.
For dimensions through 11 it independently checks the formula by a direct
integer Walsh transform and checks the complete weighted encoding at every
input. Its sign correction for the bit-index Walsh convention is correct.
The reported 5,456 direct truth checks equal twice the sum of cube sizes
for odd dimensions 3 through 11.

Entropy is evaluated numerically: the whole-entropy display uses floats,
and the local split increment uses 100-digit Decimal arithmetic to avoid
catastrophic subtraction of nearly equal whole-function entropies. This
is appropriate for a finite sanity check, but the function name
`binary_entropy_exact` should not be read as an exact transcendental
certificate; the input probabilities are exact, the logarithms are not.
The author's scope statement accurately separates these displays from
the analytic asymptotic proof. Its lower-bound assertion is applied only
for \(N\ge15\). JSON rows below 15 also display the same lower-bound
expression under a `proved_lower_ratio` key; the written proof certifies
that expression only in its stated \(N\ge15\) range. This labeling does
not affect the theorem or the asserted checker results.

## 5. Additional independently written checks

New code: `independent_three_crossing_check.py`.
Output: `independent_three_crossing_checks.json`.

It directly checked 87,376 weighted truth inputs and 43,688 majority
Fourier coefficients through odd dimension 15, using integer scores and
Walsh transforms. It also checked the exact full-function/pair-spectrum
mass identity and the exact physical pivot influence. Uniform coefficient
and Vandermonde bounds passed in 250 odd dimensions from 15 through 513
with exact Fractions and integers.

Separate 400-digit local entropy calculations gave:

| \(N\) | Observed \(\Delta_zH/\alpha\) | Analytic lower bound |
|---:|---:|---:|
| 15 | 10.8119012586 | 2.0931094044 |
| 31 | 18.2521271695 | 8.0458036896 |
| 63 | 33.7249099483 | 22.0227200765 |
| 127 | 65.2117905300 | 52.0113153132 |
| 255 | 128.7053434390 | 114.0056465631 |
| 511 | 256.2021469993 | 240.0028205191 |

The even-size contribution was separately checked to be exactly
\(2\alpha\) up to the high-precision display tolerance. These finite
tests corroborate the formulas but are not the proof of divergence.

**Scope:** the unique largest-weight coordinate fails a universal local
entropy-increment/influence bound within the three-crossing class.
The construction retains a majority background with substantial influence
on the other coordinates. It neither rules out a better adaptive split
nor supplies an FEI counterexample for this function class or for general
Boolean functions.
