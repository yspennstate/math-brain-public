SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T01:26:40Z.
attacking: nested translation-uniform indefinite-pair logarithmic smoothing on two disjoint physical pairs.

# fleet01/B14 r25 — nested pair-log localization

Status: `NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: translations/localization. No moment, bounded-support, connected-support, centering, fragment-count, or post-rotation independence assumption is used.

## 1. Source-pinned dependency actually used

The completed fleet02/B14 r22 report is

`yspennstate/math-open-problems@84093fddd5e3d3c692449d49c8b01537b28eb8d8`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T230003Z-fleet02-B14-QFORM-r22/REPORT.md`.

It proves the exact one-dimensional logarithmic averaging lemma and the optimized `C_log(D,kappa,H)` compiler. It also source-pins the original-coordinate indefinite-pair density envelope to

`yspennstate/math-open-problems@b873b2b52f4c75c331153c9227d0a7fae0f02979`

at

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

I read both reports. The pair envelope states that if an invertible indefinite original-coordinate pair has matrix `B`, `D=|det B|`, `kappa=sigma_min(B)`, and exact completed remainder `R`, then for every `r>0`,

`p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+( 2 r^2/(kappa |t-R|) ).`  (1.1)

The bound is uniform in the affine translation of the pair and requires no moments or support control.

## 2. New theorem: two nested indefinite pairs smooth each other's logarithms

Let the original coordinates be split into disjoint sets

`P1 union P2 union R`, `|P1|=|P2|=2`.

Write the selected four-coordinate principal block as

`[[B1,F],[F^T,E]]`.

Assume `B1` is invertible indefinite and its exact two-coordinate Schur complement

`B2 = E - F^T B1^(-1) F`                                      (2.1)

is also invertible indefinite. Define

`D_i=|det B_i|`, `kappa_i=sigma_min(B_i)`, `i=1,2`.

All coefficients involving the remaining coordinates `R` are arbitrary.

### Theorem 2.1 — `QFORM-NESTED-PAIRLOG-L2-v1`

For every independent cap-one product input law,

`||p_(X^T A X)||_infinity
 <= C0 D1^(-1/5) D2^(-1/10) kappa1^(-3/10) kappa2^(-1/10)`, (2.2)

where

`C0 = 5*2^(11/5)/3^(3/5) < 11.885`.                            (2.3)

The same estimate holds with arbitrary affine terms. It is uniform in arbitrary translations, arbitrarily distant support fragments, unbounded supports, and all outside quadratic/cross coefficients. No output-density cap for the first Schur remainder is assumed.

### Proof

Condition only on the remaining ORIGINAL coordinates `Z=X_R=z`. The four-variable polynomial has the exact form

`Q_z(x,y)=x^T B1 x + 2 x^T F y + 2 u(z)^T x
          + y^T E y + 2 v(z)^T y + c(z)`,                     (2.4)

with `x=X_P1`, `y=X_P2`. The two pairs remain independent, each with coordinate densities at most one.

Complete only the first pair:

`x -> x + B1^(-1)(F y+u(z))`.

The critical-value remainder is

`T_z(y)=y^T B2 y + 2 w(z)^T y + c2(z)`,                        (2.5)

where `B2` is exactly (2.1). The translation of `x` may depend arbitrarily on `(y,z)`, but (1.1) is uniform in that translation. Hence, for any `r1>0`,

`p_(Q|z)(t)
 <= a1 + D1^(-1/2) E_y L_R1(t-T_z(y))`,                       (2.6)

where

`a1=2sqrt(2)/r1`, `R1=2r1^2/kappa1`,
`L_R(s)=log_+(R/|s|)`.

Now apply the same source-pinned pair envelope to the second ORIGINAL coordinate pair `y`. Since after conditioning `z` there is no random variable outside `y`, for every `r2>0`,

`p_(T_z)(s)
 <= a2 + D2^(-1/2) L_R2(s-c2(z))`,                             (2.7)

with

`a2=2sqrt(2)/r2`, `R2=2r2^2/kappa2`.

The logarithmic kernels have exact norms

`||L_R||_1 = 2R`,
`||L_R||_2^2 = 4R`.                                            (2.8)

Indeed, after `x=Ru`,

`int_0^R log(R/x) dx = R`,
`int_0^R log(R/x)^2 dx = 2R`.

Insert (2.7) into (2.6). The constant part costs

`D1^(-1/2) a2 ||L_R1||_1
 = 8sqrt(2) r1^2/(sqrt(D1) kappa1 r2)`.                         (2.9)

For the two logarithmic singularities, Cauchy-Schwarz convolution and (2.8) give

`||L_R1*L_R2||_infinity
 <= ||L_R1||_2 ||L_R2||_2
 = 4 sqrt(R1 R2)`.                                              (2.10)

Thus, uniformly in `z,t`,

`p_(Q|z)(t)
 <= A/r1 + B r1^2/r2 + C r1 r2`,                               (2.11)

where

`A=2sqrt(2)`,
`B=8sqrt(2)/(sqrt(D1) kappa1)`,
`C=8/sqrt(D1 D2 kappa1 kappa2)`.                               (2.12)

For fixed `r1`, the last two terms are minimized at

`r2=sqrt(B r1/C)`,                                              (2.13)

and their sum becomes `2sqrt(BC) r1^(3/2)`. Therefore

`p_(Q|z)(t) <= A/r1 + 2sqrt(BC) r1^(3/2)`.                     (2.14)

The optimum satisfies

`r1^(5/2)=A/(3sqrt(BC))`,                                      (2.15)

and the minimum is

`5*3^(-3/5) A^(3/5) (BC)^(1/5)`.                              (2.16)

Substituting (2.12) yields exactly (2.2)-(2.3). Since the bound is uniform in `z`, averaging the conditional laws proves the unconditional estimate. No step normalizes support fragments or uses a moment. QED.

## 3. A full Young-family refinement

The `L^2-L^2` choice above is only the cleanest member of a continuum. For every `1<p<infinity` and conjugate `q=p/(p-1)`,

`||L_R||_p^p = 2 R Gamma(p+1)`.                                (3.1)

Young therefore gives

`||L_R1*L_R2||_infinity
 <= (2R1 Gamma(p+1))^(1/p) (2R2 Gamma(q+1))^(1/q)`.            (3.2)

Consequently (2.11) may be replaced by

`A/r1 + B r1^2/r2 + C_p r1^(2/p) r2^(2/q)`,                   (3.3)

where

`C_p = 4 Gamma(p+1)^(1/p) Gamma(q+1)^(1/q)
       /(sqrt(D1D2) kappa1^(1/p) kappa2^(1/q))`.               (3.4)

Put `beta=2/q` and `gamma=(beta+2)/(beta+1)`. Exact two-step minimization gives

`M_p=(beta+1) beta^(-beta/(beta+1))
      B^(beta/(beta+1)) C_p^(1/(beta+1))`,                     (3.5)

and

`||p_Q||_infinity
 <= (gamma+1) gamma^(-gamma/(gamma+1))
    A^(gamma/(gamma+1)) M_p^(1/(gamma+1))`.                    (3.6)

This lets one trade quantitative burden between the first and second pair. If both pairs are scaled by the same factor, every member of the family has the correct overall homogeneity `scale^(-1)`. For the clean symmetric choice `p=q=2`, (3.6) is exactly Theorem 2.1.

## 4. Actual application of fleet02/B14 r22

The partner's r22 theorem is not merely cited. Suppose the second pair itself has an additional exact completed remainder `R3` (from a further disjoint original-coordinate bank) with a true density cap `H`. Define the partner compiler

`H2 := C_log(D2,kappa2,H)`,                                    (4.1)

using fleet02/B14 r22 Theorem 4.1. Then the entire second-stage output has density cap `H2`. Applying the same completed partner theorem to the first pair gives the actual nested inequality

`boxed: ||p_Q||_infinity <= C_log(D1,kappa1,H2)
      = C_log(D1,kappa1,C_log(D2,kappa2,H)).`                   (4.2)

All conditioning is on disjoint original-coordinate blocks, so the independence hypotheses are genuine. Equation (4.2) is a direct two-level application of the assigned partner result. Theorem 2.1 is complementary: it removes the need for any finite cap `H` by convolving the two logarithmic envelopes directly when the second pair has deterministic critical value after outside conditioning.

## 5. Genuine target-class example and quantitative gain

Let

`J=[[0,1],[1,0]]`

and

`A_* = 3 [[J,I_2],[I_2,2J]]`.                                  (5.1)

The four eigenvalue magnitudes are

`3(3+sqrt(5))/2` (twice) and `3(3-sqrt(5))/2` (twice).          (5.2)

The smaller value is `1.145898...>1`, so `A_*` is inside the full target class (indeed all four eigenvalues have modulus above one).

For the first pair,

`B1=3J`, `D1=9`, `kappa1=3`.

Here `F=3I_2`, `E=6J`, so

`B2=6J-(3I)(3J)^(-1)(3I)=3J`,                                  (5.3)

and again `D2=9`, `kappa2=3`. Theorem 2.1 yields

`boxed: ||p_(X^T A_* X)||_infinity <= C0/3 < 3.962`             (5.4)

for every independent cap-one input law.

For comparison, the already available one-pair arbitrary-rank theorem from the same source gives approximately `8.65` on this matrix when fed its exact `s3(A_*)`; the new nested logarithmic smoothing more than halves that supporting constant on this genuinely coupled target example.

Moreover, arbitrary additional coordinates, arbitrary additional quadratic terms, and arbitrary couplings to the selected four coordinates may be appended without changing (2.2): condition first on those added ORIGINAL coordinates. They produce only affine terms in the selected four variables, and the proof above is uniform in all such affine shifts. The selected `A_*` principal block also keeps the enlarged matrix in the target class by interlacing.

## 6. Scope and remaining implication

This does NOT prove the full QFORM conjecture. The bare three-large-eigenvalue hypothesis does not force two quantitatively good nested indefinite coordinate pairs; diffuse bank examples remain the obstruction. The new theorem is a localization/smoothing module for the branch where two such pair stages exist. Its structural value is that it pays a logarithmically singular moving critical value by a second logarithmically singular pair, rather than requiring a bounded-density Schur remainder.

The next unpaid implication is to connect this nested-pair module to an aggregate-before-inversion structural decomposition: either expose two nested indefinite pair stages with a dimension-free product of the scales in (2.2)/(3.6), or route the matrix to the already-paid diffuse/ridge/cross-bank branch without selecting a tiny physical minor first.

No uniform pointwise quadratic Fourier decay, arbitrary-joint coarea, conditional projection-density moment, coefficient-perturbation continuity, or bounded-fragment localization is used.

Manual changed-file review: this report contains only mathematical statements, source pins, and nonsecret run metadata; no credentials, personal archives, scheduler IDs, signed URLs, or public-release action are included.
