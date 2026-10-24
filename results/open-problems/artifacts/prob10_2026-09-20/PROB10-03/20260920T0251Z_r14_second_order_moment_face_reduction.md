Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# PROB10-03 / R14 — second-order tilted-moment compiler, monotone-face reduction, and the transverse `B=0` seed

Status: **PARTIAL / SOURCE OPEN / NEW ANALYTICAL REDUCTIONS / NO RIGOROUS THRESHOLD ENDPOINT MOVED**.

Frozen source model throughout: `M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`, and `<g_a,sigma> >= -sqrt(N)` for every `a<=M`, with fixed `alpha` and `N->infinity`.

The certified repository bracket entering and leaving this artifact is

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. The `alpha=12.75` complete-second-lift point remains a candidate until the stationary root and positive comparison value are enclosed continuously.

## 1. Consumed exact reduction

Use the already-proved complete-second-lift reduction

`q=p D^2`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

`f_{p,B}(z)=E_H exp[-B(sqrt(p)z+sqrt(1-p)H-1)_+^2]`,

`u(z)=log f_{p,B}(z)`,

`I=E_Z u(Z)`, `I_B=partial_B I`, and `K=E_Z u_z(Z)^2`.

On the complete interior branch,

`D^2=K/[-4p^2B^2I_B]`,

`alpha=-c^2/[4B^2I_B]`,

and stationarity at fixed density is equivalent to

`H(p,B)=I-BI_B-4B^2I_B A_0(p,D)=0`,

where `A_0=T_D/c_D` is the inherited deterministic algebraic source term, together with `alpha(p,B)=alpha_0`. The source comparison value is `Psi(p,B)` from the same inherited reduction.

The companion T03 report already proved a first-derivative tilted-moment compiler. The purpose here is to close the **second derivative layer analytically**, because the remaining R14 centered-Hessian certificate was blocked by numerical/interval differentiation.

## 2. Attack A — exact second-order tilted-moment compiler

Fix `0<p<1`, `B>0`, and a Gaussian outer coordinate `z`. Put

`mu=sqrt(p)z-1`, `s=sqrt(1-p)`, `Y~N(mu,s^2)`.

For `r>=0` define the unnormalized tilted positive moments

`J_r=E[Y_+^r exp(-B Y_+^2)]`.

Also set

`f=P(Y<=0)+J_0`, `u=log f`, and `rho_0=phi(mu/s)/s`,

where `phi` is the standard normal density.

The already-proved recurrence is

`J_1=(mu J_0+s phi(mu/s))/(1+2Bs^2)`,

`J_r=(mu J_{r-1}+(r-1)s^2 J_{r-2})/(1+2Bs^2)`, `r>=2`,

and `partial_B J_r=-J_{r+2}`.

### Theorem R14-T03-SECOND-MOMENT-COMPILER

The raw derivatives needed through total order three are

`f_B=-J_2`,

`f_BB=J_4`,

`f_BBB=-J_6`,

`f_mu=-2B J_1`,

`f_muB=-2J_1+2B J_3`,

`f_muBB=4J_3-2B J_5`,

`f_mumu=-2B J_0+4B^2 J_2`,

`f_mumuB=-2J_0+10B J_2-4B^2 J_4`,

`f_mumumu=-2B rho_0+12B^2 J_1-8B^3 J_3`.

Consequently every logarithmic derivative

`u_B,u_BB,u_BBB,u_mu,u_muB,u_muBB,u_mumu,u_mumuB,u_mumumu`

is an explicit rational expression in `f`, the displayed raw derivatives, hence in `J_0,...,J_6` and `rho_0` only. Explicitly,

`u_BBB=f_BBB/f-3 f_BB f_B/f^2+2(f_B/f)^3`,

`u_muBB=f_muBB/f-f_mu f_BB/f^2-2 f_B f_muB/f^2+2 f_mu f_B^2/f^3`,

`u_mumuB=f_mumuB/f-f_mumu f_B/f^2-2 f_mu f_muB/f^2+2 f_mu^2 f_B/f^3`,

`u_mumumu=f_mumumu/f-3 f_mumu f_mu/f^2+2(f_mu/f)^3`.

The integrated stochastic derivatives satisfy

`I_BB=E u_BB`, `I_BBB=E u_BBB`,

`K=p E u_mu^2`,

`K_B=2p E[u_mu u_muB]`,

`K_BB=2p E[u_muB^2+u_mu u_muBB]`,

`K_p=E u_mu^2+p E[u_mumu^2-2u_mu^2u_mumu]`,

`K_pB=2E[u_mu u_muB]`
`      +p E[2u_mumu u_mumuB-4u_mu u_muB u_mumu-2u_mu^2u_mumuB]`,

and

`K_pp = p E[u_mumumu^2] + 2E[u_mumu^2] - 4pE[u_mumu^3]`
`       -6pE[u_mu u_mumu u_mumumu] -4E[u_mu^2u_mumu]`
`       +6pE[u_mu^2u_mumu^2] +2pE[u_mu^3u_mumumu]`.

Finally the OU identities imply

`I_p=-K/(2p)`,

`I_Bp=-K_B/(2p)`,

`I_Bpp=-K_pB/(2p)+K_B/(2p^2)`,

`I_BBp=-K_BB/(2p)`.

Thus **all stochastic derivatives needed for the Hessians of `H(p,B)` and `alpha(p,B)` are one-dimensional Gaussian expectations of explicit functions of `J_0,...,J_6` and `rho_0`; no finite difference, nested Gaussian quadrature, or automatic differentiation is mathematically necessary.** The remaining differentiation of `c(p,D)` and the inherited `A_0(p,D)` is purely algebraic once `D(p,B)` is differentiated from

`D^2=K/[-4p^2B^2I_B]`.

### Proof

The `B` derivatives follow from `partial_B J_r=-J_{r+2}`. The first `mu` derivative of the full kernel has the already-proved boundary cancellation `f_mu=-2BJ_1`. Differentiating this identity in `B` twice gives `f_muB` and `f_muBB`.

For the second `mu` derivative, `partial_mu J_1=J_0-2BJ_2`, hence `f_mumu=-2BJ_0+4B^2J_2`; differentiating in `B` gives `f_mumuB`. For the third `mu` derivative one must retain the kink contribution at zero:

`partial_mu J_0=rho_0-2BJ_1`,

while `partial_mu J_2=2J_1-2BJ_3`. Therefore

`f_mumumu=-2B(rho_0-2BJ_1)+4B^2(2J_1-2BJ_3)`
`           =-2B rho_0+12B^2J_1-8B^3J_3`.

The displayed logarithmic identities are direct differentiation of `u=log f`.

The formulas for `K_B,K_BB,K_pB` follow by differentiating under the Gaussian integral; domination holds uniformly on compact interior `(p,B)` boxes because all derivatives are bounded by Gaussian-integrable polynomial envelopes.

It remains to prove the `K_pp` identity. Write `p=e^{-2t}` and view `u(t,z)=log P_t h_B(z)` under the Ornstein--Uhlenbeck semigroup. With `v=u_z` and `L=partial_zz-z partial_z`,

`u_t=Lu+v^2`,

`v_t=Lv-v+2v v_z`.

Gaussian integration by parts gives `E[a Lb]=-E[a_z b_z]`. Put

`A=E v_z^2`, `C=E v^2 v_z`.

Then

`K_t=-2A-2K+4C`.

A second differentiation gives

`A_t=-2E v_zz^2-4A+4E v_z^3+4E[v v_z v_zz]`,

`C_t=-2E v_z^3-4E[v v_z v_zz]-4C`
`    +6E[v^2v_z^2]+2E[v^3v_zz]`.

Hence

`K_tt=4E v_zz^2+12E v_z^2+4K-16E v_z^3`
`     -24E[v v_z v_zz]-24E[v^2v_z]`
`     +24E[v^2v_z^2]+8E[v^3v_zz]`.

Since `K_t=-2pK_p`,

`K_tt=4pK_p+4p^2K_pp`.

Substitute

`v=sqrt(p)u_mu`, `v_z=p u_mumu`, `v_zz=p^(3/2)u_mumumu`

and the already-proved formula for `K_p`; cancellation yields exactly the displayed `K_pp` formula. QED.

### Consequence for the R14 centered-Hessian certificate

The preceding R14 certificate required rigorous bounds on

`H_pp,H_pB,H_BB, alpha_pp,alpha_pB,alpha_BB`

on a small rectangle. Before this theorem, the second stochastic derivative layer was being scouted by finite differences. After this theorem, every such quantity is obtained by ordinary chain rule from a finite set of **closed one-dimensional Gaussian expectations**. The analytical order of the missing numerical differentiation is therefore reduced from `2` to `0`.

This is auxiliary mechanism movement, not a source endpoint.

## 3. Attack B — monotone-face reduction for the `alpha=12.75` Miranda rectangle

The companion T03 report found a numerical-only rectangle

`R=[p_-,p_+] x [B_-,B_+]`

with opposite signs of `H` on the two `p`-faces and of `alpha-12.75` on the two `B`-faces. A full interval enclosure of four continuous faces is sufficient but unnecessarily strong.

### Lemma R14-T03-MONOTONE-FACE

Let `H,alpha` be continuous on `R`, continuously differentiable in its interior, and suppose

`H_B>0` and `alpha_p>0` everywhere on `R`.

If the four corner inequalities

`H(p_-,B_-)>0`,

`H(p_+,B_+)<0`,

`alpha(p_-,B_-)>alpha_0`,

`alpha(p_+,B_+)<alpha_0`

hold, then `F=(H,alpha-alpha_0)` satisfies the Poincare--Miranda face-sign hypotheses on `R`. Hence there exists `(p*,B*) in R` with

`H(p*,B*)=0`, `alpha(p*,B*)=alpha_0`.

#### Proof

On the left face `p=p_-`, positivity of `H_B` makes the minimum occur at `B_-`, so the first corner inequality gives `H>0` on that face. On the right face `p=p_+`, the maximum occurs at `B_+`, so the second corner inequality gives `H<0` there. Likewise `alpha_p>0` makes the minimum of `alpha` on `B=B_-` occur at `p_-` and the maximum on `B=B_+` occur at `p_+`. The last two corner inequalities therefore give the required opposite signs of `alpha-alpha_0`. Apply Poincare--Miranda. QED.

For objective positivity, no monotonicity is needed: if a rectangular mesh has maximum coordinate half-spacings `delta_p,delta_B`, every mesh value satisfies `Psi>=m`, and globally

`|Psi_p|<=L_p`, `|Psi_B|<=L_B`,

then

`Psi >= m-L_p delta_p-L_B delta_B`

everywhere. This is the mean-value theorem.

### Why this is useful

The continuum obligation can therefore be reorganized from

`four whole-face interval signs + whole-rectangle Psi enclosure`

to

`four certified corner values + two robust derivative signs + a coarse Lipschitz bound for Psi`.

The companion numerical scouts put `H_B` safely positive and `alpha_p` safely positive near the candidate, so this is a plausible reduction; those scouts are **not** a proof of the two sign hypotheses.

## 4. Attack C — nondegeneracy of the `B=0` OU boundary seed

The preceding R14 run proved that any complete-second-lift stationary branch with

`B->0`, `D->1`, `p->p_* in (0,1)`

must satisfy

`F(p):=E[(T_{sqrt(p)}u(G))^2]-p E[u(G)^2]=0`,

for `u(x)=(x-1)_+`, and that this equation has a unique root `p_*` in `(0,1)`.

The remaining concern for perturbative continuation is whether this root could be tangent/degenerate.

### Lemma R14-T03-B0-TRANSVERSE

The unique interior root is simple:

`F'(p_*)<0`.

#### Proof

Let

`s_k=(E[u(G)He_k(G)])^2/k! >=0`.

OU spectral calculus gives

`F(p)=sum_{k>=0}s_k p^k-p sum_{k>=0}s_k`.

For `0<=p<1`,

`F(p)=(1-p) G(p)`,

where

`G(p)=s_0-sum_{k>=2}s_k p(1+p+...+p^{k-2})`.

At least one `s_k` with `k>=2` is strictly positive because `(x-1)_+` is not affine in Gaussian `L^2`. Hence `G'(p)<0` for every `0<p<1`. At the interior root, `G(p_*)=0`, so

`F'(p_*)=(1-p_*)G'(p_*)<0`.

Thus the `B=0` scalar seed is transverse. QED.

This removes one possible perturbative obstruction but does not prove that the boundary branch connects to the source-relevant interior branch near the `alpha=12.75` candidate.

## 5. Falsification / self-check notes

The raw third-derivative formula deliberately retains the boundary density term

`-2B rho_0`

in `f_mumumu`. Omitting this term is a tempting but false differentiation through the kink at zero and changes the resulting `K_pp`; this was explicitly checked rather than silently smoothing the hinge.

The matching executable performs two exact symbolic checks:

1. the OU `K_tt -> K_pp` algebra reduces exactly to the displayed `K_pp` formula;
2. finite Hermite truncations satisfy exactly `F=(1-p)G`, the algebra behind the transversality lemma.

It then uses the closed kernel at the candidate center only as a **NUMERICAL_ONLY falsification test**. At 80-point Gauss--Hermite order it obtains

`K = 0.16069992652999146`,

`K_B = 0.01937436910425818`,

`K_BB = -0.003781416544143028`,

`K_p = 1.0459566331396992`,

`K_pB = 0.1430341822163802`,

`K_pp = 8.106289492195577`,

and centered finite differences with step `2e-4` disagree by only

`5.28e-7, 3.15e-6, 7.84e-12, 4.47e-9, 1.03e-7`

for `(K_p,K_pp,K_B,K_BB,K_pB)` respectively. These numbers do not certify any source endpoint.

## 6. What moved and what remains

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**No source-level movement.**

### Auxiliary movement

1. The second stochastic derivative layer is now exact and closed with `J_0,...,J_6`; numerical differentiation is removed from the Hessian proof obligation.
2. The Miranda continuum obligation can be reduced, conditional on two derivative signs, to four corner values rather than four full face enclosures.
3. The unique `B=0` OU boundary seed is proved transverse, so tangent degeneracy is not the reason a perturbative continuation might fail.

### Remaining full-scope gap

The shortest source-moving route is now:

1. use the second-order moment compiler to obtain directed bounds proving `H_B>0` and `alpha_p>0` on the candidate rectangle (or directly the broader Jacobian bounds from the companion contraction theorem);
2. rigorously enclose the four corner values with the closed one-dimensional kernel;
3. prove `Psi>0` on the stationary root box via a directed derivative/Lipschitz enclosure;
4. only then invoke the already-source-matched complete-second-lift comparison theorem to promote `alpha_U` from `12.78437096216` to `12.75`.

Until those enclosures are completed, `12.75` remains a candidate and status remains **OPEN / PARTIAL**.