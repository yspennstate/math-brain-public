# Shift-stable joint L² bound for hub products and dependent leakage

Status: **proved supporting invariant; the curved-trace density estimate remains open**. This sharp inequality extends the ordinary independent-product `L²` calculation to an arbitrary light-dependent hub shift, so it applies to the canonical `βL²+2εLP` terms without treating `P` as independent.

## Theorem

Let `H` be independent of an arbitrary random triple `(L,V,P)`. Assume `H` has density `f_H≤1`, `∫f_H=1`, and `(L,V)` has joint density `g(l,v)≤M` of total mass one, where `M>0`. For **any** measurable real-valued `u=u(l,p)`, define
```
Z=L[H+u(L,P)].
```
Then `(Z,V)` has a joint density `k(z,v)` satisfying
```
∥k∥²_{L²(R²)} ≤ 4M.                                      (1)
```
The constant 4 is sharp for `M=1`: take independent `H,L,V` uniform on `[−1/2,1/2]`, take `u=0`, and use the product density `p_{HL}(z)=−2log(4|z|)` for `|z|<1/4`, whose squared `L²` norm is 4.

In particular, for any `β,ε∈R`, with `u(l,p)=βl/2+εp`, the pair
```
(Z,V)=(HL+(β/2)L²+εLP,V)
```
has a uniform joint `L²` bound regardless of the dependence of `P` on `(L,V)`. Original-coordinate product laws imply a universal `M` via the two-dimensional orthogonal projection cap, but this theorem needs only the displayed joint cap and hub independence.

## Proof

Disintegrate the light law over its `(L,V)` marginal. Write `ν_{l,v}(dp)` for a conditional probability law of `P`, defined for almost every `(l,v)`. Since `L=0` has probability zero, the ordinary change of variables in the independent hub gives the nonnegative measurable joint density
```
k(z,v)=∫_R [g(l,v)/|l|] ∫ f_H(z/l−u(l,p)) ν_{l,v}(dp) dl.
```
Tonelli justifies the density formula even if its pointwise integral is initially infinite on a null set.

Expand `∫k(z,v)² dz,dv` by Tonelli. For any nonzero `l,l'` and any two shifts `a,a'`,
```
∫_R f_H(z/l−a) f_H(z/l'−a') dz
    ≤ min(|l|,|l'|),                                      (2)
```
because one factor is at most one and the other has integral `|l|` or `|l'|` after the change of variables. The key point is that the bound is **independent of both shifts**. Integrating the conditional `P` variables out of (2) yields
```
∥k∥²_2
 ≤ ∫_{R³} g(l,v)g(l',v)/max(|l|,|l'|) dl,dl',dv.          (3)
```

For a fixed `v`, put `m(v)=∫g(l,v)dl` and `F_v(r)=∫_{|l|≤r}g(l,v)dl`. The cap `g≤M` implies `F_v(r)≤min(m(v),2Mr)`. The identity `1/max(a,b)=∫_{max(a,b)}^∞r^{-2}dr` gives
```
∫_{R²} g(l,v)g(l',v)/max(|l|,|l'|) dl,dl'
 =∫_0^∞ F_v(r)²/r² dr
 ≤∫_0^{m(v)/(2M)}4M² dr
   +∫_{m(v)/(2M)}^∞m(v)²/r² dr
 =4M m(v).
```
The zero-mass case is immediate. Finally `∫m(v)dv=1`, proving (1). For the equality example, `p_{HL}(z)=−2log(4|z|)` on `|z|<1/4` gives `∥p_{HL}∥²_2=4`, while `V` is independent uniform on a unit interval, proving sharpness.

For `u=0`, adjoin an independent `V` uniform on `[0,1]`: then `g_{L,V}(l,v)=f_L(l)1_{[0,1]}(v)≤1`, while `∥k∥²_2=∥p_{HL}∥²_2`, recovering the sharp one-dimensional result `∥p_{HL}∥²_2≤4` for independent cap-one `H,L`. Plancherel under `\hat f(t)=∫e^{itx}f(x)dx` yields `∫|E e^{itHL}|²dt≤8π`, with the factor `4π` for `e^{2itHL}`. A separate [Mellin resonance construction](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T194654Z-bilinear-fourier-resonance/REPORT.md) shows no uniform Fourier `L^p` bound for `p<2` without an additional structural assumption.

## Finite-p extension (same arbitrary shifts)

The same hypotheses also give, for every real `1≤p<∞`,
```
∥k∥_{L^p(R²)} ≤ p(2M)^{1−1/p}.                            (4)
```
Indeed `∥f_H∥_p≤1`. For fixed `v`, Minkowski's inequality in `z`, followed by the conditional `P` integration, gives
```
∥k(·,v)∥_p ≤ ∫ g(l,v)|l|^{−1+1/p} dl
              ≤ 2M∫_0^{m(v)/(2M)}r^{−1+1/p}dr
              = p(2M)^{1−1/p}m(v)^{1/p}.
```
The second step is one-dimensional decreasing-kernel rearrangement under `g(l,v)≤M` and total mass `m(v)`. Raise to the `p`th power and integrate `v`, using `∫m(v)dv=1`. At `p=1` this is the probability normalization; at `p=2` the sharp collision estimate (1) improves the displayed constant by `√2`.

The growth proportional to `p` is qualitatively necessary: for independent `H,L,V` each uniform on `[−1/2,1/2]` and `u=0`,
```
∥k∥_p^p=2^{p−1} Γ(p+1),
```
so `∥k∥_p∼2p/e`. Even simultaneous bounds (4) for every finite `p` do not control restriction to the output parabola; the dependent-light fake exploits that missing trace control.

## Exact analytic gap

For the canonical output `Q=2Z+V²`, formally
```
p_Q(s)=(1/2)∫_R k((s−v²)/2,v)dv.
```
An `L²(R²)` bound alone does not control this restriction to a parabola: `k` may concentrate in arbitrarily thin curved strips. Thus (1) is an ε- and β-stable product-compatible invariant, **not** a proof that `p_Q` is bounded. The existing dependent-light fake construction confirms that a marginal-cap-only intermediate density theorem fails; the remaining argument must exploit original-coordinate product provenance beyond the `(L,V)` cap and the joint `L²` bound.
