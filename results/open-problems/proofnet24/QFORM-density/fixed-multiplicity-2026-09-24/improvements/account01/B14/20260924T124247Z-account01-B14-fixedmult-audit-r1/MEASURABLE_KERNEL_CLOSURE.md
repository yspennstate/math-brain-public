# Measurable-kernel closure for rough conditional quadratic pushforwards

Run: `20260924T124247Z-account01-B14-fixedmult-audit-r1`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved rigor/exposition improvement; theorem multiplicity remains 17.**

## Lemma — domination of conditional kernels commutes with arbitrary environment mixing

Let `(Omega,F,nu)` be a probability space and let `omega -> mu_omega` be a probability kernel from `Omega` to `R`. Suppose there is a jointly measurable nonnegative function `k(omega,z)` such that, for `nu`-almost every `omega`,

\[
\int \psi(z)\,\mu_\omega(dz)
\le
\int \psi(z) k(\omega,z)\,dz
\tag{1}
\]

for every nonnegative Borel `psi`. Then the mixture

\[
\mu(B)=\int \mu_\omega(B)\,\nu(d\omega)
\]

is absolutely continuous and is dominated by the density

\[
\bar k(z)=\int k(\omega,z)\,\nu(d\omega).
\tag{2}
\]

In particular, if `bar k(z)<=C` for almost every `z`, then `mu<=C dz` and `||p_mu||_infty<=C`.

### Proof

For every nonnegative Borel test `psi`, kernel measurability and Tonelli give

\[
\int \psi\,d\mu
=
\int_\Omega\left(\int\psi\,d\mu_\omega\right)\nu(d\omega)
\le
\int_\Omega\int_\R \psi(z)k(\omega,z)\,dz\,\nu(d\omega)
=
\int_\R \psi(z)\bar k(z)\,dz.
\]

Thus `mu<=bar k(z)dz` as measures. Taking Radon–Nikodym derivatives proves the claim. QED.

## Corollary — environment-dependent exceptional output levels are harmless

Suppose a deterministic change-of-variables argument for each environment `omega` produces a density formula or upper envelope only for Lebesgue-a.e. output `z`, with an exceptional set that can depend on `omega`. If the change-of-variables proof can instead be written as (1) against arbitrary nonnegative tests with a jointly measurable explicit kernel `k(omega,z)`, then the environment-dependent null sets never need to be united. The unconditional statement follows from the lemma.

This is exactly the safe formulation for the manuscript's scalar-square and hyperbolic-pair branches.

### Scalar square fiber

For measurable parameters `a(omega)!=0`, `m(omega)`, `v(omega)`, and a cap-one input density `f`, the two inverse branches give, directly against nonnegative `psi`,

\[
\int \psi\!\left(a(\omega)(y-m(\omega))^2+v(\omega)\right)f(y)\,dy
\le
\int \psi(z)\,
\frac{\mathbf 1_{(z-v(\omega))/a(\omega)>0}}
{\sqrt{|a(\omega)|\,|z-v(\omega)|}}\,dz.
\tag{3}
\]

The right kernel is jointly measurable in `(omega,z)`. Hence any subsequent averaging over an arbitrary outside product law is legitimate even when the vertex and critical output translate without bound.

### Hyperbolic pair fiber

For an invertible indefinite symmetric `2x2` quadratic block `B` with `D=|det B|` and a measurable environment-dependent affine field, completion of the square gives a measurable critical value `v(omega)`. The hyperbolic change of variables can be performed against nonnegative tests before discarding the critical level, yielding the measure domination

\[
\mu_\omega(dz)
\le
D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v(\omega)|}\right)dz.
\tag{4}
\]

Thus the manuscript's later averaging step is not an interchange of separately chosen a.e. density versions. It is an application of (1)-(2), after which the logarithmic potential of the random `v(omega)` can be bounded.

## Corollary — arbitrary translations and unbounded supports

The proof of the kernel lemma uses only positivity and Tonelli. There is no moment condition on the environment and no bound on `m(omega)`, `v(omega)`, or other translations. Consequently all scalar/pair pivot measure-dominations in the manuscript remain valid for arbitrarily distant fragments and unbounded supports, exactly as claimed.

## Recommended manuscript patch

A short version of the kernel lemma can be inserted immediately before the pivot section, followed by the sentence:

> All conditional density envelopes below are understood as inequalities of kernels/measures against nonnegative tests. Consequently environment-dependent exceptional output levels cause no null-slice problem, and Tonelli may be applied before choosing any density version.

This makes the rough-law argument auditable without changing any theorem, constant, hypothesis, or multiplicity.

## Threshold note

I also rechecked the fresh leverage-interpolated determinant improvement from account01/B04. It yields genuine lower-multiplicity **conditional** branches (`s_13` with a fixed row-leverage gap below one, and `s_9` with maximum row leverage below `3/4`) but does not control the high-leverage endpoint. Combined with the terminal `r=4` saturation of the manuscript's interpolation step, it does not presently yield an unconditional theorem with 16 or fewer large eigenvalues. The rigorous global threshold therefore remains 17 in this run.
