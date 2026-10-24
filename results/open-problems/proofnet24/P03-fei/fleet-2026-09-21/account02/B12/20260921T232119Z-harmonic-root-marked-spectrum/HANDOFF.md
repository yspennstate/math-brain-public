# B12 compact joint handoff — one-source harmonic prefix target

**Full FEI:** OPEN / NOT PROVED.

## Proved in this run

For the Boolean spectral sample `S` with `p_B=hat f(B)^2`, choose a uniform random ordering of nonempty `S` and let `J` be its first coordinate, with `J=bot` on `S=emptyset`. Put

`v_i=sum_{B contains i} p_B/|B|`.

Then

`P(J=i)=v_i`, `P(J=bot)=p_empty`, and

`H(J) <= 4.8588229680899335 I(f)`.

The proof is hypercontractive and uses the genuine Boolean derivative `D_i f in {0,+/-1}`:

`v_i/j_i <= min(1,2/ln(1/j_i))`.

The exact continuation is

`H(f)=H(J)+sum_i v_i H(q_i^H)-E[1_{|S|>0} log2|S|]`,

where

`q_i^H(T)=p_{T union {i}}/((|T|+1)v_i)`.

Thus a sufficient exact remaining implication is

`sum_i v_i H(q_i^H)-E log2|S| <= C_cont I(f)`

for one finite universal `C_cont`.

## Higher-prefix constraint from the same Boolean source

For nonempty `A`, `a=|A|`, `w_A=||D_A f||_2^2` and

`v_A=sum_{B superset A}p_B/C(|B|,a)`,

Boolean quantization `D_A f in 2^(1-a) Z intersect [-1,1]` plus Bonami gives

`sum_T t^|T| hat f(A union T)^2 <= w_A [4^(a-1)w_A]^((1-t)/(1+t))`.

If `theta_A=4^(a-1)w_A<1`, `lambda_A=ln(1/theta_A)`, then

`v_A/w_A <= min(1, a!(2/lambda_A)^a)`.

In particular `lambda_A>=4a` implies `v_A<=2^-a w_A`.

## Route killed inside a genuine Boolean source

A row-by-row harmonic FEI is false. For odd `m=2r+1`, let `g=(1+Maj_m)/2` and

`f_m(x0,y)=1-g(y)+x0 g(y)`, so `D_0 f_m=g`.

For row harmonic masses `r_T=hat g(T)^2/(|T|+1)`, total `V`, harmonic depth `J_H`, and unnormalized entropy `H_H`,

`V+J_H<=1`, but

`H_H >= (1/16) log2(2r) -> infinity`.

Therefore the continuation cannot be paid by independent derivative-row inequalities; it must exploit common-source cross-row compatibility.

## Peer result consumed

account01/B12 `20260921T231256Z-conditional-count-code/REPORT.md`, commit `ffcc39e48292c19a053da6741586e0165a6b72b5`, pays all fine closed component count/macro entropy and leaves non-fine/nonclosed singleton address costs. The root theorem above replaces the first such global address layer by an `O(I)` one-source code whenever the residual is still a Boolean squared spectrum.

## Next recipient / target

Primary: joint interface B / B12-B13. Build a global Kraft/Carleson code on the exact prefix tree

`P(stop at A|A)=p_A/v_A`,

`P(next i|A)=v_{A union {i}}/((|A|+1)v_A)`,

using the factorial order refund once, sparse-prefix bound above, and actual cross-row Boolean compatibility. Do not retry a rowwise harmonic entropy bound.
