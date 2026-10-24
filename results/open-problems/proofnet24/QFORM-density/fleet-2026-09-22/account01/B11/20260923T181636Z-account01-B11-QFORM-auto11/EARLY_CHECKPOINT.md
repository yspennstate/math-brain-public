SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T18:16:36Z.
attacking: the rough hidden-projection zero-pivot endpoint; condition away an exact source cocircuit and recover the pure-hub transverse-square bound without a small-random-perturbation step.

# Early calculation — homogeneous pure-hub receiver and a conditionable hidden direction

Status at this checkpoint: calculation in progress; full QFORM remains OPEN.

## 1. A single homogeneous envelope extracted from the proved pure-hub theorem

The current proved pure-hub result states for

`Q0=2 X_h(L+beta)+mu(V-v_c(L))^2+F_c(L)`,

with `L,V` orthonormal product projections and arbitrary cap-one source laws,

`||p_Q0||inf <= 2 sqrt(2)+sqrt(2) log(1/3+4sqrt(2)/mu)` for `0<mu<=6sqrt(2)`,

and the newest exact evaluation gives `(192/mu)^(1/3)` for `mu>=6sqrt(2)`.

The first branch is also at most `(192/mu)^(1/3)`. Set

`y=(6sqrt(2)/mu)^(1/3)>=1`.

After dividing by `sqrt(2)`, this is exactly

`2+log((1+2y^3)/3) <=2y`.

At `y=1` equality holds, while the derivative of the right side minus the left side is

`2-6y^2/(1+2y^3)
 =2(2y^3-3y^2+1)/(1+2y^3)
 =2(y-1)^2(2y+1)/(1+2y^3)>=0`.

Therefore, for every `mu>0`,

`||p_Q0||inf <=192^(1/3) mu^(-1/3)`.

By scaling, for arbitrary nonzero `a,b`,

`Q=2a X_h(L+beta)+b(V-v_c(L))^2+F_c(L)`

satisfies

`||p_Q||inf <=192^(1/3) |a|^(-2/3)|b|^(-1/3)
                  =192^(1/3)(a^2|b|)^(-1/3)`.

No support or regularity assumption is added.

## 2. Exact source conditioning candidate

Let the light original-coordinate coefficient vectors be `l,v,p`; write `L=l.X`, `V=v.X`, `P=p.X`. In the zero-hub-pivot canonical state the quadratic form has the algebraic form

`Q=2 kappa L X_0 + gamma L^2+2delta LV+lambda V^2+2theta LP + affine terms`,

where `X_0` is an original coordinate independent of all light coordinates and `kappa*lambda !=0`.

Choose an ORIGINAL-coordinate set `K`, put `R=K^c` inside the light bank, and assume

`Delta_R=||l_R||^2||v_R||^2-<l_R,v_R>^2>0`,

`p_R in span{l_R,v_R}`.

Condition on `X_K`. Then the hidden term `LP` contributes only `L_R^2`, `L_R V_R`, and affine terms. It does not alter the `V_R^2` coefficient `lambda`.

Let

`g=||l_R||^2`,
`v_perp=v_R-(<l_R,v_R>/g)l_R`,
`||v_perp||^2=Delta_R/g`,
`L1=(l_R.X_R)/sqrt(g)`,
`V1=(v_perp.X_R)/sqrt(Delta_R/g)`.

The coefficient vectors of `L1,V1` are orthonormal, so they are exactly in the scope of the pure-hub theorem; no independence between `L1,V1` is asserted. After completing the `V1` square, the conditioned form is

`2 a (L1+beta_K) X_0 + b(V1-v_c(L1))^2+F_K(L1)`

with

`a=kappa sqrt(g)`,
`b=lambda Delta_R/g`,

and hence the exact cancellation

`a^2|b|=kappa^2|lambda| Delta_R`.

If the source theorem's hypotheses remain exactly as stated after the affine conditioning (to be checked against the immutable proof before publication), this yields

`||p_(Q|X_K)||inf <=192^(1/3)(kappa^2|lambda|Delta_R)^(-1/3)`,

uniformly in the conditioned values. Averaging would give the same unconditional bound.

The next step is to audit every affine/source-provenance detail against the proved Proposition S, then apply the completed account02/B11 dominant-atom inequality to obtain a literal bound in the near-null-ruling single-spike branch.
