# P0083 proof-capable follow-up idea — triangle plus one pendant leaf for all `1 <= p <= 3`

This is the single proof-capable follow-up selected by stuck recovery #2. It is not a new recovery episode and does not by itself move the universal metric `A_whisker_cert`.

Let `s=p+1`, `h=p/(p+1)=(s-1)/s`. On the support consisting of a triangle `r-a-b-r` plus one pendant leaf `ell` at `r`, write `q=A_r/A_ell`, `u=A_a/A_r`, `v=A_b/A_r`. The leaf equation gives

`K=A_r^(-p)=(1+q)^s/q^(s-1)`.

The root incidences on `ra,rb` are

`x=K/(1+u)^s`, `z=K/(1+v)^s`, `x+z=1-q`.

Two complementary regimes appear.

## Regime I: `1 <= p <= 2`

Since `x,z<1`, the leaf/root equations imply `u,v>1`. Hence the two root-triangle conductances satisfy

`c_ra > x/2`, `c_rb > z/2`,

while the pendant conductance is `d=q/(1+q)`. Therefore the total conductance incident to `r` is

`S > q/(1+q)+(1-q)/2 > 1/2`.

The mean-zero vector `(-3,1,1,1)` (root versus the other three vertices) has Laplacian Rayleigh quotient `4S/3>2/3`. Since the WARM non-instability ceiling is `h=p/(p+1)<=2/3`, this proves instability throughout this regime, with no symmetry assumption.

## Regime II: `2 <= p <= 3`

Here `s in [3,4]`. Because `x<1-q`,

`1+u > (1+q)/(q^((s-1)/s)(1-q)^(1/s))`.

Weighted AM-GM gives

`q^((s-1)/s)(1-q)^(1/s) <= [1+(s-2)q]/s`,

so `1+u>8/3` and similarly `1+v>8/3`; hence `u,v>5/3`.

At `a,b`, after dividing the equilibrium equations by `K`, both `u` and `v` are roots of

`G_S(t)=t/(1+t)^s+t/S^s`, where `S=u+v`.

For `t>=5/3` and the complementary variable also at least `5/3`, one has `G_S'(t)<0`. A sufficient exact inequality is

`(1+t)^4 < (2t-1)(t+5/3)^3`,

whose difference is

`(27t^4+135t^3+153t^2-83t-152)/27`.

At `t=5/3` this equals `968/27`, and its derivative is positive for every `t>=5/3`. Thus `u=v=:t`: reflection symmetry is forced rather than assumed.

Now `x=z=(1-q)/2`, and full support on the triangle gives `t(1-q)/2<1`. Combining this with

`(1+t)^s=2(1+q)^s/[q^(s-1)(1-q)]`

is equivalent to `Phi_s(q)>1`, where

`Phi_s(q)=q^(s-1)(3-q)^s/[2(1+q)^s(1-q)^(s-1)]`.

One has `Phi_s(1/3)=1`; moreover

`d/dq log Phi_s(q)`

has, after multiplication by the positive denominator `q(q-3)(q-1)(q+1)`, numerator

`s(3q^2-2q+3)+(q^2-2q-3)>0`

for `0<q<1`, `s>=3`. Hence full support forces `q>1/3`.

For the test vector `(1,0,0,-1)` on `(r,a,b,ell)`, the Laplacian Rayleigh quotient is

`R=a+2d`,

where `a=t(1-q)/[2(1+t)]` and `d=q/(1+q)`. Using the root relation and setting `x=q/(1-q)>1/2`, the inequality `R>3/4` reduces exactly to

`2x^2+3x-1>(2x)^h`.

With `y=2x>1`, this is

`(y^2+3y-2)/2 > y^h`.

Equality holds at `y=1`, while the derivative of the left side minus the right side is

`y+3/2-h y^(h-1) >= 7/4>0`

because `y>=1` and `h<=3/4`. Thus `R>3/4>=h`, again forcing instability.

## Expected theorem and lifecycle consequence

The argument should prove: every full-support WARM equilibrium on a triangle with one pendant leaf is linearly unstable for every `1<=p<=3`, equivalently every `alpha>=4/3` in this parametrization. This extends the predecessor's exact endpoint theorem to the whole source-relevant interval but still does not establish a universal pendant-pruning theorem for arbitrary odd unicycles or branched trees.

If the proof checks, `A_whisker_cert` remains `2`. Because recovery episodes 1 and 2 are already consumed and this is the one explicitly authorized post-recovery proof-capable follow-up, the same universal blocker then triggers a terminal P0083 handoff and rotation. All thirty Section-B methods have already been genuinely used on P0083, so no fresh numbered triple exists to claim honestly on this source.