Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 maximum, and I do not claim otherwise.**

# HARD7-06 F0095 — binary-cascade tail route before code

Target remains the owned external F0095 problem: convergence to a constant location of the ordinary sparse Erdos--Renyi 3-colourability threshold. The incoming certified bracket is `L_3=4.03`, `U_3=4.6865076260769`, hence `W_3=0.6565076260769`. The preceding run used B1/B13/B29, so this run uses a new F0095 triple: **B16 / B23 / B25**. Repository searches recovered no earlier F0095 section headings for those three moves.

The point of this run is not another decimal shave. It asks what the exact two-input multiplicative sector forces on any putative infinite-support cavity fixed point.

## B16 — compute the small active-input sectors exactly

Use the established cavity coordinate `t=(1-x)/3 in [0,1/3]` and

`R(N)=(A-2B+C)/(3A-3B+C)` with `A=prod(1-t_i)`, `B=prod(1-2t_i)`, `C=prod(1-3t_i)`.

For zero or one positive message the output is zero. For exactly two positive messages `s,t`, the previous run proved `R({s,t})=2st`. In the rescaled variable

`Y=2T in [0,2/3]`,

the exactly-two-positive-input sector is therefore the exact multiplicative rule

`Y_out=Y_1 Y_2`.

For exactly three positive messages direct expansion gives the additional closed formula

`R({s,t,u}) = 2(st+su+tu-6stu)/(1-6stu)`.

The binary sector is special because it turns the lower tail into an exact multiplicative cascade rather than merely an inequality.

## B23 — assume the infinite-support fixed point exists and ask what it must look like

Let `mu` be a nontrivial cavity fixed point at degree `d`, let

`q=mu((0,2/3])`,

and write its lower-tail function

`G(y)=mu((0,y])`, `0<y<=2/3`.

Zero messages are neutral. The positive incoming messages form a Poisson point process of total intensity `d q`. Restrict the fixed-point output to the event that there are exactly two positive incoming messages and no other positive messages. By the exact binary rule,

`G(y) >= c * int int 1_{uv<=y} mu(du) mu(dv)`,

where

`c = exp(-d q) d^2/2`.

In particular, restricting further to `u,v<=sqrt(y)` yields the nonlinear tail inequality

`G(y) >= c G(sqrt(y))^2`.                                    (A)

Set `y_n=(2/3)^(2^n)`. Since `G(2/3)=q`, iteration of (A) gives

`G(y_n) >= c^(2^n-1) q^(2^n) = c^(-1) (c q)^(2^n)`.

Thus, with

`beta_bin = log(c q)/log(2/3)`,

we obtain the explicit dyadic-sequence lower-tail barrier

`G(y_n) >= c^(-1) y_n^(beta_bin)` for every `n>=0`.             (B)

This is not an assumed power law: it is a rigorous lower bound along an explicit doubly-exponential sequence forced solely by the exactly-two-input sector.

The fixed-point zero-atom equation already proved on this track is

`q = 1-exp(-d q)(1+d q)`.

Hence the exponential disappears from the cascade coefficient:

`c q = d^2 q(1-q) / [2(1+d q)]`.                              (C)

At the current degree the large branch has previously been isolated near `q in (0.9319,0.9320)`; this run will re-certify that bracket at the current slightly smaller `d` before using it.

## B25 — count the same binary sector as a negative moment

For `s>0` define the unnormalised negative moment

`M_s = E[Y^{-s}; Y>0]` in `[0,infinity]`.

On exactly two positive inputs, `Y_out=Y_1Y_2`. Campbell/Poisson counting therefore gives the exact sector contribution

`E[Y_out^{-s}; K_+=2] = c M_s^2`.

Fixed-point equality implies

`M_s >= c M_s^2`.

If `M_s<infinity`, then necessarily

`M_s <= 1/c = 2 exp(dq)/d^2`.

But `Y<=2/3` on the positive support, so

`M_s >= q (3/2)^s`.

Consequently

`q(3/2)^s > 2 exp(dq)/d^2  =>  M_s=infinity`.                 (D)

Equations (C) and (D) identify the same critical binary-cascade exponent `beta_bin`: every `s>beta_bin` has infinite negative moment.

The exact checker will do only the finite arithmetic/transcendental certification needed at the current degree: re-bracket the large scalar root by `0.9319<q<0.9320`, certify `5.03<beta_bin<5.04` by rational power comparisons after using (C), and certify in particular `M_6=infinity`. The analytic tail and moment statements belong in the run report and do not depend on numerical sampling.