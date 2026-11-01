Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Candidate movement route: `T_corr=0 -> 1` if the argument below survives verification. Methods: B6/B11/B29. This checkpoint records the mathematical idea before any checker is written.**

# HARD7-02 idea checkpoint — phase-Mahler peeling defeats the nonnormal reattachment obstruction

The active source target is Campbell--O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices* (EJP 2022), Question 1.9: how the tail of `mu_{alpha,theta_d}` varies with `theta_d`. The frozen slice is `alpha=1` and

`eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`,

`vartheta_x=(eta_x+tau#eta_x)/2`,

first at `x=1/4`. Write `kappa_x=(x(1-x))^(1/4)` and `g_x=kappa_x^2=sqrt(x(1-x))`.

The previous STUCK1 report isolated the circular potential

`V_x(r)=int log^+(|z|/r) mu_x(dz)=int_r^infinity F_x(u) du/u`,

where `F_x(r)=mu_x(|z|>r)`, as the correct scalar observable. The new observation is that the independent uniform phase on each reciprocal heavy edge gives an exact **Mahler-measure lower bound** for this potential which is completely insensitive to the nonnormal background.

## 1. Single-edge determinant peeling

Use the exact Pareto representative already verified for the source class: `P(R>r)=r^{-1}` for `r>=1`, independent uniform phase `u=e^{i phi}`, and angular atom from `vartheta_x`. For `A_n=X_n/n`, fix an unordered edge `e={i,j}` and condition on every variable except its phase and radial overshoot.

For fixed radial size and swap choice, the two directed entries are of the form `a u` and `b u^{-1}`, with

`ab = g_x (R_e/n)^2 =: q`.

In the characteristic determinant `D(u)=det(zI-A_n)`, the Leibniz expansion uses neither, one, or both directed entries. Hence

`D(u)=c_{-1}u^{-1}+c_0+c_1u`,

and the zero Fourier coefficient is exactly

`c_0=A_0-qB`,

where `A_0` is the determinant after zeroing both directed entries of `e`, and

`B=det(zI-A_n^{\setminus{i,j}})`

is the principal minor after deleting the two endpoints. The transposition sign is the minus sign in `A_0-qB`.

Multiplying by `u` produces a quadratic polynomial. For any quadratic `h(u)=d_0+d_1u+d_2u^2`, its logarithmic Mahler measure satisfies

`exp((1/(2pi)) int log|h(e^{i theta})| dtheta) >= |d_1|/2`.

Indeed, if `h=d_2(u-r_1)(u-r_2)`, then `|d_1|=|d_2||r_1+r_2| <= 2 |d_2| max(1,|r_1|)max(1,|r_2|)`; degenerate degrees follow by continuity. Therefore

`E_phi log|det(zI-A_n)| >= log|A_0-qB|-log 2`.  (1)

This is the B6 deformation mechanism: it holds for **arbitrary background entries**, hence in particular uniformly if the background is multiplied by a deformation parameter `tau in [0,1]`. The estimate starts at the block/skeleton point `tau=0` and survives unchanged at the full matrix `tau=1`.

## 2. Pareto overshoot anti-concentration

Condition on `R_e>sn`. Then `R_e=sn Y`, where `P(Y>y)=y^{-1}` for `y>=1`. Put `X=Y^2`; it has density `(1/2)x^{-3/2}` on `[1,infinity)`. Thus

`q=QX`, `Q=g_x s^2`.

For every complex `c`,

`E log|X-c| >= -1`.  (2)

Reason: `|X-c|>=|X-Re c|`. The negative part occurs only where `|x-Re c|<1`; on `[1,infinity)` the density is at most `1/2`, and

`int_{-1}^1 log|t| dt=-2`.

Hence the negative contribution is at least `-1`, while the rest is nonnegative.

Factoring `QB` in (1) and averaging the overshoot gives, for a.e. `z` with `B(z) != 0`,

`E_{phi,Y} log|det(zI-A_n)|`
`>= log Q + log|det(zI-A_n^{\setminus{i,j}})| -(1+log 2)`.  (3)

Zeros of the principal-minor characteristic polynomial on a fixed circle form a finite set; standard logarithmic truncation justifies the circle integral.

## 3. Peel a positive density of exceedance edges

For fixed `s>=1`, form the exceedance graph `G_s` from unordered pairs with `R_e>sn`. It is exactly `G(n,1/(sn))`. Let `M_s` be all isolated edges of this graph and `m_s=|M_s|`. These edges are disjoint. Conditional on the indicator graph, their phases and Pareto overshoots remain independent, so (3) can be iterated over every `e in M_s`:

`E_selected log|det(zI-A_n)|`
`>= m_s(log(g_x s^2)-(1+log2))`
`   + log|det(zI-A_n^{\setminus V(M_s)})|`.  (4)

No spectral perturbation or reattachment inequality is used.

## 4. B11 dualize and circular-average

For every finite matrix `M`, Jensen's formula gives

`(1/(2pi)) int log|det(r e^{i theta}I-M)| dtheta`
`= sum_j log max(r,|lambda_j(M)|)`.

Apply this to (4), and lower-bound the minor's circle average by `(n-2m_s)log r`. After subtracting `n log r` and dividing by `n`,

`E V_n(r) >= (E m_s/n) [log(g_x s^2/r^2)-(1+log2)]`,  (5)

where

`V_n(r)=(1/n)sum_j log^+(|lambda_j(A_n)|/r)`.

The isolated-edge expectation is exact:

`E m_s/n = ((n-1)/(2sn))(1-1/(sn))^(2(n-2))`
` -> e^{-2/s}/(2s)`.  (6)

Choose

`r=c_x s`, `c_x=kappa_x/(2e)`.

Then the bracket in (5) is exactly

`log(4e^2)-(1+log2)=1+log2`.

Therefore

`liminf_n E V_n(c_x s) >= (1+log2)e^{-2/s}/(2s)`.  (7)

The already-proved uniform finite-`n` `p<1` moment bounds give uniform integrability of `log^+(|z|/r)`. Campbell--O'Rourke's deterministic ESD convergence therefore transfers (7) to the limiting law:

`V_x(c_x s) >= (1+log2)e^{-2/s}/(2s)`.  (8)

Equivalently, for `r>=c_x`,

`V_x(r) >= ((1+log2)kappa_x/(4er)) exp(-kappa_x/(er))`
`>= A_x/r`,

with

`A_x=(1+log2)kappa_x/(4e^3)>0`.  (9)

This is B29: infinity is now a boundary point `rho=1/r=0`, and (9) supplies a positive first-order boundary coefficient.

## 5. Convert integrated tail to the actual tail exponent

The previous theorem gives the uniform `p=1/2` moment bound

`int |z|^(1/2) mu_x(dz) <= 5`.

Let `F_x(r)=mu_x(|z|>r)`. Since

`V_x(r)=int_r^infinity F_x(u) du/u`,

for `r>1`,

`V_x(r)`
`<= int_r^{r^3} F_x(u)du/u + int_{r^3}^infinity 5u^{-1/2}du/u`
`<= 2F_x(r)log r + 10 r^{-3/2}`.  (10)

Combine (9) and (10). For all sufficiently large `r`, `10r^{-3/2}<=A_x/(2r)`, hence

`F_x(r) >= A_x/(4r log r)`.  (11)

Thus

`limsup_{r->infinity}[-log F_x(r)]/log r <= 1`.

The already-proved finite `p<1` moments imply the reverse inequality on `liminf`, by Markov and `p upward 1`. Therefore

`lim_{r->infinity}[-log F_x(r)]/log r = 1`  (12)

for every fixed interior `0<x<1` with `x != 1/2`; in particular for the required non-Hermitian point `x=1/4`.

If verification finds no gap, this increments the frozen metric conservatively from `T_corr=0` to `T_corr=1`: one explicit non-i.i.d., non-Hermitian C2 one-parameter family now has its radial power exponent determined. This remains a PARTIAL answer to the full source Question 1.9, not source closure, and requires independent audits before any paper-level closure claim.