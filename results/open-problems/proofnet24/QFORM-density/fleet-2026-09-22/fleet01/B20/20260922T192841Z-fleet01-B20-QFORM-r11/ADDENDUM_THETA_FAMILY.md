# Addendum — full triple-collision exponent family and optimized pivot constant

This addendum strengthens the fixed `theta=15/16` choice in `REPORT.md`. No new hypothesis is introduced.

## 1. All subcritical determinant moments

In the notation of Theorem 3.1 of the report, the proof before the choice of `theta` gives, for every `0<theta<1`,

`p^3 <= M_theta beta^(-2theta) h^(2theta)`,

where

`M_theta = 2^(theta+1) pi^(theta/2) e^(2theta) / [(1-theta)(2-theta)].`

Hence the rank-two physical cross packet satisfies the whole family

`boxed( L_Q(h) <= min(1, M_theta^(1/3) beta^(-2theta/3) h^(2theta/3)) )`.

Thus every concentration exponent `alpha<2/3` is available, with arbitrary self blocks and outside couplings retained. The restriction `theta<1` is exactly the scalar negative-moment integrability threshold in the determinant factorization; no endpoint `alpha=2/3` is claimed.

## 2. Every theta>3/4 closes after one physical square pivot

Let `alpha=2theta/3`. If `theta>3/4`, then `alpha>1/2`. The concentration-to-half-Riesz calculation gives

`sup_t E[1_{R<t}(t-R)^(-1/2)]`
` <= [2alpha/(2alpha-1)] [M_theta^(1/3) beta^(-alpha)]^(1/(2alpha))`
` = C_theta beta^(-1/2),`

where

`boxed( C_theta
 = [4theta/(4theta-3)]
   2^((theta+1)/(4theta)) pi^(1/8) e^(1/2)
   [(1-theta)(2-theta)]^(-1/(4theta)). )`

Therefore the physical-pivot theorem strengthens to

`boxed( ||p_Q||_infinity <= C_theta / sqrt(|a| beta),  3/4<theta<1. )`

The fixed choice in the main report, `theta=15/16`, gives `C_theta=28.0459887515...`.

A slightly better convenient rational choice is

`theta=189/200`, `alpha=63/100`,

for which

`M_theta = 754.4111144724...`,
`M_theta^(1/3) = 9.1033804390...`,
`C_theta = 27.9685000295... <27.969.`

Thus one may replace the main-report pivot constant by

`boxed( ||p_Q||_infinity < 27.969 / sqrt(|a| beta). )`

At the two numerical gates used there this gives

- `|a|>=3501/8000`, `beta>=499/8000`: `||p_Q||_infinity <169.283`;
- `|a|>=3501/8000`, `beta>=1/64`: `||p_Q||_infinity <338.227`.

The optimization is not logically important; the structural point is that the three-copy argument supplies a continuum of exponents strictly above the half-Riesz threshold, so every physical nonzero square pivot plus a quantitatively rank-two Schur cross bank is paid.

## 3. Verification snippet

```python
import math

def Ctheta(th):
    M = 2**(th+1)*math.pi**(th/2)*math.e**(2*th)/((1-th)*(2-th))
    return M, M**(1/3), (4*th/(4*th-3))*M**(1/(4*th))

th = 189/200
M,K,C = Ctheta(th)
m = 3501/8000
print(th, 2*th/3, M, K, C)
print(C/math.sqrt(m*(499/8000)))
print(C/math.sqrt(m*(1/64)))
```

Output:

```text
0.945 0.63 754.4111144724884 9.103380439023919 27.96850002955541
169.28280018239408
338.2268653121285
```

This is only a constant check; the proof is the symbolic argument above plus Theorem 3.1 of `REPORT.md`.
