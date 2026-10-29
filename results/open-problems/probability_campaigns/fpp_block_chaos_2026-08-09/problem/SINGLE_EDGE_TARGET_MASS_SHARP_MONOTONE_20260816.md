# A sharp monotone-kernel bound for the single-edge target mass

Date: 2026-08-16  
Status: exact edge-level refinement proved; independent audit required before use

This note sharpens the constant in
`SINGLE_EDGE_TARGET_MASS_DIRECT_20260816.md`, SHA-256
`4eea505ef965591bf4c06eb03f5915111e745725d7f4423ca26d593d4e39b923`.
The earlier note bounded the target-pair kernel pointwise by `1/4`.  The kernel
is actually the Green kernel of a Brownian bridge, while the threshold survival
function is decreasing.  That extra shape gives the sharp constant `1/9`.

Let the iid edge weights have density `rho` on `[a,b]`, with

`rho(t)>=alpha>0` for almost every `t in [a,b]`.                 (1)

For the geodesic from `0` to `v`, write

`p_e=P(e belongs to gamma(0,v)).`                               (2)

With `C_edge` and `P_edge` as in the direct-target note, the refined estimate is

`C_edge+P_edge <= (1/(9 alpha^2)) sum_e p_e^2.`                 (3)

Thus the previously proved `1/(4 alpha^2)` coefficient can be multiplied by
are unchanged.


Fix an edge.  Condition on every weight except its target weight and let

`T_e=(best cost avoiding e)-(best through-e cost with w_e removed).`

For an independent replacement `w_e'`, put `z_e=(X^e-X)^+` and

`q_e(t)=P(T_e>t).`

The direct-target calculation gives

`m_e(w,w'):=E[z_e|w_e=w,w_e'=w']
 =1_(w'>w) integral_w^(w') q_e(t) dt`                          (4)

and therefore

`E[m_e(w_e,w_e')^2]
 =integral_a^b integral_a^b q_e(s)q_e(t)
   F(min{s,t})[1-F(max{s,t})] ds dt.`                          (5)

Use the generalized quantile of `F` and put

`q_tilde(u)=q_e(F^(-1)(u)),       0<u<1,`

`K(u,v)=min(u,v)-uv.`

For `u<=v`, `K(u,v)=u(1-v)`, so changing variables in (5) gives

`E[m_e^2]
 =integral_0^1 integral_0^1
   q_tilde(u)q_tilde(v) K(u,v)
   /[rho(F^(-1)(u))rho(F^(-1)(v))] du dv.`                    (6)

The kernel is nonnegative.  By (1),

`E[m_e^2]
 <=alpha^(-2) integral_0^1 integral_0^1
   q_tilde(u)q_tilde(v)K(u,v) du dv.`                         (7)

Moreover, `q_tilde` is nonnegative and decreasing, and

`integral_0^1 q_tilde(u)du
 =integral_a^b q_e(t)rho(t)dt=p_e.`                           (8)

It remains to use the shape of `q_tilde`, rather than only the pointwise
maximum of `K`.

## 2. Sharp decreasing-function lemma

**Lemma.** If `f:[0,1]->[0,infinity)` is decreasing and integrable, then

`integral_0^1 integral_0^1 f(u)f(v)K(u,v)du dv
 <=(1/9)(integral_0^1 f(u)du)^2.`                             (9)

The constant `1/9` is sharp.

**Proof.** Let `p=integral f`; the zero case is immediate.  Normalize
`h=f/p`, let `U` have decreasing density `h`, and define its survival function

`H(t)=P(U>t)=integral_t^1 h(u)du.`

For iid `U,V`, Tonelli gives

`integral integral h(u)h(v)K(u,v)du dv
 =E[min(U,V)]-(E U)^2
 =integral_0^1 H(t)^2dt-(integral_0^1 H(t)dt)^2.`              (10)

A decreasing density is a mixture of densities uniform on initial intervals:
there is a probability measure `mu` on `(0,1]` such that, almost everywhere,

`h(u)=integral_[u,1] a^(-1) mu(da).`                          (11)

This follows directly by applying the Stieltjes/layer-cake decomposition to
`h` and normalizing with `integral h=1`.  Consequently

`H(t)=integral_(0,1] (1-t/a)_+ mu(da).`                       (12)

Write `A=integral H`.  Jensen's inequality, followed by integration, yields

`integral_0^1 H(t)^2dt
 <=integral mu(da) integral_0^a (1-t/a)^2dt
 =integral (a/3)mu(da),`

while

`A=integral mu(da) integral_0^a(1-t/a)dt
 =integral (a/2)mu(da).`

Hence

`integral H^2-A^2 <=(2/3)A-A^2<=1/9.`                        (13)

Multiplying by `p^2` proves (9).  Equality is attained when
`mu=delta_(2/3)`, equivalently when `f` is a positive multiple of
`1_[0,2/3]`.  This also proves sharpness.  QED

Applying (9) to `f=q_tilde` in (7), then using (8), gives

`E[m_e(w_e,w_e')^2] <=p_e^2/(9 alpha^2).`                    (14)

The exact spectral identity from the direct-target note is

`C_edge+P_edge=sum_e E[m_e(w_e,w_e')^2].`                    (15)

Summing (14) proves (3).

## 3. Published consequence and exact scope

Corollary 1.3 of Dembin--Elboim--Peled,
[On the influence of edges in first-passage percolation on
`Z^d`](https://arxiv.org/abs/2307.01162v2), gives under (1)

`sum_e p_e^2
 <=C_(d,G)||v||^(2/(d+1))(log ||v||)^d.`                     (16)

Therefore

`C_edge+P_edge
 <=C_(d,G)/(9alpha^2) ||v||^(2/(d+1))(log ||v||)^d.`         (17)

The distribution-dependent constant in (16) can of course absorb
`1/(9alpha^2)`; equation (17) records the exact contribution from this lemma.

Nothing here controls the outside ANOVA mass `V_z`, its revealment, or the
large-block analogue.  In particular, (3) is not a variance theorem and is not
a block-chaos estimate.

## 4. Independent break checks

1. For `f=1_[0,c]`, direct polynomial integration gives
   `integral integral f(u)f(v)K(u,v)du dv=c^3(4-3c)/12`.
   Dividing by `(integral f)^2=c^2` gives `c(4-3c)/12`, whose maximum is
   exactly `1/9` at `c=2/3`.
2. For constant `f`, the ratio is `integral integral K=1/12`, below `1/9`.
   This rules out accidentally replacing the sharp monotone constant by the
   constant-function value.
3. The density comparison is pointwise in (6): each reciprocal density costs
   one factor `alpha^(-1)`.  No density upper bound is used.
4. The Brownian-bridge operator-norm estimate would instead involve an `L^2`
   norm of `q_tilde`; for rare edges it need not improve the squared-influence
   bound.  The lemma above is an `L^1` inequality using monotonicity.
5. Equality in the abstract kernel lemma is compatible with a survival
   function: any `c 1_[0,2/3]`, `0<c<=1`, is the survival function of a
   two-point threshold law.  Thus `1/9` cannot be lowered under shape alone.

An independent referee should verify (6), the mixture representation (11),
and the equality case before this refinement replaces the `1/4` dependency.
