# QFORM B01 — aggregated rank-two random-slope smoothing with a transverse quadratic gate

Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM / FULL TARGET OPEN**.

## Target and correction state

The target is the full arbitrary-product-law conjecture: independent real `X_i`, each with probability density at most one; arbitrary real symmetric `A`; at least three eigenvalues of `A` have absolute value at least one; prove a universal bound for the density of `Q=X^TAX`, ideally with a continuous representative, or give a target-valid counterexample.

The phase-aligned fragmented-support construction remains in force: bounded density alone gives no law-uniform pointwise `|t|^{-1/2}` decay for a scalar quadratic phase. The proof below uses averaged scalar smoothing and a two-dimensional random-slope marginal instead. It does not rotate the whole input into an eigenbasis and never assumes independence after a rotation.

## Partner theorem actually applied

Account02/B01 run `20260922T120355Z-account02-B01-qform-r19`, canonical report commit `fedbec07e3e8b2f9fcd2b1a65b0bb2a0137c212f`, proves the following non-normalized scalar gate. If `0<=h<=1` has mass `m` and

`F(t)=int exp(i t(a w^2+bw)) h(w)dw`, with `a!=0`,

then, uniformly in the linear tilt `b`,

`int_R |F(t)|^3 dt <= 16*pi*m/|a|`.                                  (1)

I apply (1) slice-by-slice below. I also use account02/B01 r21, commit `949dd0672776cb2f4e100fe917faaee1644b80fc`, as the two-column predecessor whose remaining debt was an arbitrary-width coordinate bank.

## External projection theorem

Livshyts--Paouris--Pivovarov prove that if a product density on `R^m` has all one-dimensional factors bounded by one, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In dimension two the cap is exactly `2`.

Hence, if `M:R^m->E` has rank two and nonzero singular values `s_1,s_2`, with `Delta=s_1s_2`, then the density of `MY` on the two-dimensional range `E` is at most `2/Delta`.

## Theorem: arbitrary-width rank-two bank plus one transverse quadratic direction

Choose any three original coordinates `I`, put `K=I^c`, and write

`B=A[I,I]`, `M=A[I,K]`.

Assume `rank(M)=2`. Let `nu` be the unit vector spanning `ker(M^T)` and put

`a=nu^T B nu`,
`Delta=s_1(M)s_2(M)`.

If `a!=0`, then `Q=X^TAX` has a bounded continuous density vanishing at infinity, with

`||p_Q||_infinity <= C_bank (|a| Delta^2)^(-1/5)`,                    (2)

where

`C_bank=5*2^(-2/5)*3^(3/5)=7.325390128958803...`.                    (3)

This theorem retains arbitrary self-blocks and all couplings in the complement. The bank `K` may have arbitrary cardinality.

## Proof

Choose an orthonormal basis of `R^I` whose third vector is `nu`; write

`x=P u+nu w`, `u in R^2`, `w in R`.

The transformed three-coordinate density

`G(u,w)=prod_{i in I} f_i((Pu+nu w)_i)`

satisfies `0<=G<=1` and `int G=1`. No independence of `u,w` is asserted.

Writing `Y=X_K`, the block decomposition of the quadratic form is

`Q=x^T Bx+2x^T M Y+Y^T A[K,K]Y`.

Since `nu^T M=0`, the random slope from `Y` acts only on `u`. In coordinates on `E=range(M)=nu^perp`, let `Z=MY`. The density of `Z` is at most `2/Delta` by the two-dimensional product-marginal theorem.

For fixed `t`, after absorbing deterministic affine terms into the notation, define

`Psi_t(z)=int exp(i t[u^T H u+2c^Tuw+a w^2+2u^Tz+ell(u,w)])G(u,w)dudw`.

The phase `Y^T A[K,K]Y` has modulus one, so

`|phi_Q(t)| <= E |Psi_t(Z)|`.

Cauchy--Schwarz against the density of `Z` yields

`|phi_Q(t)| <= (2/Delta)^(1/2) ||Psi_t||_{L^2(E)}`.                   (4)

For each `u`, put

`F_u(t)=int exp(i t[a w^2+b_u w])G(u,w)dw`,
`H_0(t)=(int_R2 |F_u(t)|^2du)^(1/2)`.

Because the Fourier frequency in `z` is `2tu`, two-dimensional Plancherel gives

`||Psi_t||_2 = pi |t|^(-1) H_0(t)`.                                 (5)

Combining (4)-(5),

`|phi_Q(t)| <= sqrt(2)*pi*Delta^(-1/2)|t|^(-1)H_0(t)`.               (6)

Now let `m(u)=int G(u,w)dw`. Then `int m(u)du=1` and `|F_u(t)|<=m(u)`. The partner scalar gate (1) applied to the non-normalized slice `w -> G(u,w)` gives

`int_R |F_u(t)|^3dt <= 16*pi*m(u)/|a|`.                              (7)

At each fixed `t`, interpolation in `u` between `L^1` and `L^3` gives

`||F_.(t)||_2 <= ||F_.(t)||_1^(1/4)||F_.(t)||_3^(3/4)`.

Since `||F_.(t)||_1<=int m=1`, after raising to the fourth power,

`H_0(t)^4 <= int |F_u(t)|^3du`.

Integrating and using (7),

`int_R H_0(t)^4dt <=16*pi/|a|`.                                     (8)

For `T>0`, use `|phi_Q|<=1` on `[-T,T]`. On each tail, Hölder with exponents `4/3` and `4`, followed by (6) and (8), gives

`int_|t|>T |phi_Q(t)|dt`
` <=4*sqrt(2)*3^(3/4)*pi^(5/4)*Delta^(-1/2)|a|^(-1/4)T^(-1/4)`.     (9)

Thus

`||phi_Q||_1 <=2T+B T^(-1/4)`,

where

`B=4*sqrt(2)*3^(3/4)*pi^(5/4)*Delta^(-1/2)|a|^(-1/4)`.

The minimum occurs at `T=(B/8)^(4/5)`, and its value is `10(B/8)^(4/5)`. Fourier inversion therefore yields

`||p_Q||_infinity <=(2*pi)^(-1)||phi_Q||_1`
` <=5*2^(-2/5)*3^(3/5) Delta^(-2/5)|a|^(-1/5)`,

which is (2). Since `phi_Q` is integrable, the inverse Fourier transform is a bounded continuous density vanishing at infinity. QED.

## Basis-free aggregate identity

Set

`S_I=M M^T=A[I,I^c]A[I,I^c]^T`.

Because `S_I` has rank two,

`adj(S_I)=Delta^2 nu nu^T`.

Therefore the gate in (2) is

`Theta_I:=|a|Delta^2=|tr(adj(S_I)B)|`.                               (10)

Cauchy--Binet gives

`Delta^2=sum_{R subset I, |R|=2} sum_{C subset I^c, |C|=2} det(A[R,C])^2`.  (11)

Thus all two-column cross minors attached to the physical triple are aggregated **before** the reciprocal fifth-root payment. This is strictly different from selecting one largest fixed minor.

## Mandatory bank-family stress test

For

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`,

whose nonzero spectrum is `{1,1,-1}`, take `I` to contain the singleton coordinate and one coordinate from each bank. Then

`a=1`, `Delta=(m-1)/m^2`,
`Theta_I=(m-1)^2/m^4 ~m^(-2)`.

The theorem therefore gives a bound growing like `m^(2/5)`, not a universal bound. Triples that omit the singleton can instead have zero transverse curvature. Hence (2) is a genuine coupled supporting theorem but does **not** prove the full conjecture.

## First unpaid full-target implication

A compact conditional route is now:

1. the existing full-spectrum diffuse theorem closes the branch where every coordinate leverage of `range(A)` is at most `1/32`;
2. (2) closes any complementary branch containing a physical triple with `rank(S_I)=2` and `Theta_I>=theta_0>0` universally;
3. the remaining task is a dimension-free aggregate mechanism for rank-one coordinate banks / multiple triples when no single `Theta_I` is bounded below. The family `A_m` above is the mandatory control.

Full QFORM remains OPEN. No novelty or full-solution claim is made.

## Checker

`CHECKER.py` and `CHECKER_OUTPUT.txt` verify (3), (10), (11) on seeded rank-two instances and the exact `A_m` scaling. Output ends `STATUS=PASS`. These computations are regression evidence; the proof is analytic.

## Sources

- Current owner programme: `yspennstate/math-research-brain`, QFORM-DENSITY-3EIG-20260922, revision 2026-09-22.5.
- account02/B01 r19: `yspennstate/math-open-problems@fedbec07e3e8b2f9fcd2b1a65b0bb2a0137c212f`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T120355Z-account02-B01-qform-r19/REPORT.md`.
- account02/B01 r21: `yspennstate/math-open-problems@949dd0672776cb2f4e100fe917faaee1644b80fc`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T140625Z-account02-B01-qform-r21/REPORT.md`.
- Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; Israel J. Math. 216 (2016), 877--889.
