# Deterministic checks — fleet01/B09 20260923T102117Z

All checks here are arithmetic/linear-algebra sanity checks for `REPORT.md`; they are not evidence for the unrestricted conjecture.

## 1. Raw Theorem-H density constant

Let

`alpha=h+r/2=(r+2h)/2`,

and suppose

`|phi(t)| <= min(1,K|t|^(-alpha))`,

`K=2^(-h)(4pi)^alpha R^(-1/2)`.

Then

`int_R min(1,K|t|^(-alpha))dt = 2 alpha/(alpha-1) K^(1/alpha)`.

After division by `2pi`,

`||p||inf
 <= [alpha/(pi(alpha-1))] 2^(-h/alpha)(4pi) R^(-1/(2alpha))
 = 4(r+2h)/(r+2h-2) 2^(-2h/(r+2h)) R^(-1/(r+2h)).`

This is the constant `C_H(h,r)` in the report.

## 2. Determinant puncture inequality

For PSD eigenvalues `0<=s_j<1` with `sum_j s_j=theta<1`,

`prod_j(1-s_j) >= 1-sum_j s_j=1-theta`.

Proof by expansion/induction: `(1-a)(1-b)=1-a-b+ab>=1-a-b`, then iterate.

Thus, for `R_K>=0`, `tr R_K=theta<1`,

`det(I-R_K)>=1-theta`.

Also `I-R_K >=(1-theta)I`, so

`u_i^T(I-R_K)^(-1)u_i <= ||u_i||^2/(1-theta)`.

## 3. Thirty-one-square / two-hub stress test

Here `r=31`, `h=2`, so `r+2h=35` and

`C_H=4*(35/33)*2^(-4/35)
    =3.9193194949577905... <3.920`.

The frame has `d=r+h=33` mutually orthonormal coefficient columns, each flat on its own 32-coordinate support. Hence every physical row leverage is exactly `1/32` and

`theta+dq=33/32>1`,

so the preceding union-bound Pluecker puncture gate fails, while the new half-leverage gate `q<=1/2` holds.

The active matrix is an orthogonal direct sum of 31 one-dimensional `+1` square blocks and two matrices

`[[0,1],[1,0]]`,

so its nonzero spectrum is `1` (multiplicity 31) plus two copies of `{1,-1}`. There are 35 eigenvalues of modulus one.

## 4. High-leverage designated-partner example

For `v_1`, squared coordinate weights are one copy of `0.7` and thirty copies of `0.01`, summing to one. Therefore the probability that two independent volume-sampling choices on this support are distinct is

`1-[0.7^2+30*(0.01)^2]
 =1-(0.49+0.003)
 =0.507`.

For each flat 100-coordinate support the corresponding probability is

`1-100*(0.01)^2=0.99`.

With three disjoint supports,

`rho=0.507*(0.99)^2=0.4969107`.

The partner one-hub theorem with `r=2`, `det G=1`, `lambda_1=lambda_2=1` gives

`2*exp(3/4)*rho^(-1/4)
 =5.042910609783801... <5.043`.

The raw half-leverage gate fails because the heavy physical row has leverage `0.7>1/2`.

The active matrix is the orthogonal direct sum of two `+1` square directions and one hub/coupling block `[[0,1],[1,0]]`, hence spectrum `{1,1,1,-1}`.

## 5. Localized-collar count

After the fleet02/B09 zero-disjoint-five-volume reduction, `r<=4` and with one hub the augmented frame dimension is

`d=r+1<=5`.

If `theta<1/2` but the new half-leverage condition fails, then some surviving original leverage satisfies

`p_i>(1-theta)/2>1/4`.

Because `sum_i p_i=d<=5`, the number of rows satisfying `p_i>1/4` is strictly less than `4d<=20`, hence at most 19. Adding the at-most-eight pivot coordinates gives at most 27 leaf coordinates in the localized collar.
