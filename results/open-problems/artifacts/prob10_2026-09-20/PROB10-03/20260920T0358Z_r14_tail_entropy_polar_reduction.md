Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# PROB10-03 / R14 — rigorous derivative-tail envelope, entropy-balance compiler, and radial polar obstruction

Status: **PARTIAL / SOURCE OPEN / NO RIGOROUS THRESHOLD ENDPOINT MOVED BY THIS ARTIFACT**.

Frozen source model throughout:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N -> infinity`.

The certified repository bracket entering this artifact is

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. The complete-second-lift point `alpha=12.75` remains a candidate unless and until the full stationary root, comparison sign, and source implication are enclosed rigorously.

This artifact deliberately changes method after four unchanged R14 PROB10 reports. It compares three different attacks:

1. close the previously unproved **full-line derivative tails** analytically rather than by more quadrature;
2. rewrite the delicate `H_B` sign as an exact **relative-entropy / variance balance** and identify the remaining sign burden;
3. dualize the source feasibility event into the **inradius of a Gaussian polytope**, and prove why an ordinary one-vector Farkas certificate cannot settle the sphere obstruction.

Only Attack 1 is intended as a direct input to the pending `alpha=12.75` certification. Attacks 2 and 3 are route diagnostics, not source endpoints.

---

## 1. Consumed complete-second-lift notation

Use the already-proved R14/NM13 exact reduction

`q=pD^2`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

`Y=sqrt(p) z + sqrt(1-p) H - 1`,

`f_{p,B}(z)=E_H exp[-B(Y_+)^2]`,

`u(z)=log f_{p,B}(z)`,

`I=E_Z u(Z)`, `I_B=partial_B I`, `K=E_Z u_z(Z)^2`.

On the complete interior branch,

`D^2=K/[-4p^2B^2 I_B]`,

`alpha=-c^2/[4B^2 I_B]`,

and at fixed density the stationary equations are

`H(p,B)=I-BI_B-4B^2 I_B A_0(p,D)=0`,

`alpha(p,B)=alpha_0`,

where `A_0=T_D/c_D` is the inherited deterministic source term. The source comparison value is the inherited `Psi(p,B)`.

The current `alpha=12.75` R14 certification box is

`Q={|p-p_c|<=1/2000, |B-B_c|<=1/50}`

with

`p_c=0.645767064689`, `B_c=4.9292292009`.

Throughout `Q` we may use the coarser rational bounds

`3/5 < p < 2/3`, `0 < B < 5`, `1/3 < s^2:=1-p < 2/5`.

For the outer Gaussian coordinate `|z|>=9`, writing `mu=sqrt(p)z-1`,

`|mu| <= |z|+1 <= (10/9)|z|`.

The preceding R14 report had rigorous-looking compact interval-Simpson center enclosures but correctly did **not** claim derivative tails outside `|z|<=9`. The first theorem below closes precisely that missing analytical tail layer.

---

# Attack 1 — a rigorous full-line first-Jacobian tail theorem

For fixed `(p,B,z)`, define the unnormalized positive tilted moments

`J_r=E[Y_+^r exp(-B Y_+^2)]`,

and the normalized moments

`m_r=J_r/f`.

The already-proved moment compiler gives

`u_B=-m_2`,

`u_mu=-2B m_1`,

`u_BB=m_4-m_2^2`,

`u_muB=-2m_1+2B m_3-u_mu u_B`.

It also gives

`K=p E u_mu^2`,

`K_B=2p E[u_mu u_muB]`,

`K_p=E u_mu^2+p E[u_mumu^2-2u_mu^2u_mumu]`.

## Theorem R14-T03-FIRST-JAC-TAIL

On `Q`, for every `|z|>=9`,

`m_1 <= 4|z|`,

`m_2 <= 3 z^2`,

`m_3 <= 11|z|^3`,

`m_4 <= 4 z^4`.

Consequently,

`|u| <= 7z^2`,

`|u_mu| <= 40|z|`,

`|u_B| <= 3z^2`,

`0 <= u_BB <= 4z^4`,

`|u_muB| <= 240|z|^3`,

`-3 <= u_mumu <= 0`.

Let `Tail(X)` denote the absolute contribution of `|Z|>9` to the full Gaussian expectation defining `X`. Then the following explicit bounds hold:

`Tail(I) < 3.0e-16`,

`Tail(I_B) < 1.2e-16`,

`Tail(I_BB) < 1.4e-14`,

`Tail(K) < 6.4e-14`,

`Tail(K_B) < 6.4e-11`,

`Tail(K_p) < 4.8e-13`.

Since the exact full-line OU identities are

`I_p=-K/(2p)`, `I_Bp=-K_B/(2p)`,

the uncertainty in the reconstructed full values caused by omitting `|Z|>9` is additionally bounded by

`delta_tail(I_p) < 5.4e-14`,

`delta_tail(I_Bp) < 5.4e-11`.

These are analytical full-line bounds, not floating-point quadrature estimates.

### Proof: normalized moment envelope

There are two cases.

### Case 1: `mu<0`

Then

`f >= P(Y<=0) >= 1/2`.

Also `J_r<=E|Y|^r`, so

`m_r <= 2 E|Y|^r`.

### Case 2: `mu>=0`

Set `A=1+2Bs^2`. Completing the square on `y>0` shows that

`J_r/J_0`

is the `r`-th positive moment of a Gaussian

`X~N(mu/A,s^2/A)`

conditioned on `X>0`. Since `mu/A>=0`, `P(X>0)>=1/2`; also `|mu/A|<=|mu|` and `s/sqrt(A)<=s<=1`. Since `f>=J_0`, again

`m_r <= J_r/J_0 <= 2 E|X|^r`.

Thus in both cases it suffices to bound `2E|a+bH|^r` with

`|a|<=(10/9)|z|`, `|b|<=1`, `|z|>=9`.

For `r=1`, using `E|H|<1` and `1<=|z|/9`,

`2E|a+bH| <= 2[(10/9)|z|+1] <= (22/9)|z| < 4|z|`.

For `r=2`,

`2E(a+bH)^2 <= 2[(100/81)z^2+1]`
`              <= (202/81)z^2 < 3z^2`.

For `r=3`, use `(x+y)^3<=4(x^3+y^3)` for `x,y>=0` and `E|H|^3<2`:

`2E|a+bH|^3`
` <=8[(1000/729)|z|^3+2]`
` <=(8016/729)|z|^3 < 11|z|^3`.

For `r=4`, use the exact Gaussian fourth moment:

`2E(a+bH)^4`
` <=2[(10000/6561)z^4 + (600/81)z^2 +3]`
` <=(21206/6561)z^4 <4z^4`.

This proves the four normalized-moment bounds.

### Proof: derivatives

The first four derivative bounds follow directly from the displayed moment identities and `B<5`. In particular,

`|u_muB|`
` <= 2m_1+2B m_3+|u_mu u_B|`
` <= 8|z|+110|z|^3+120|z|^3`
` < 240|z|^3`.

For `u_mumu`, first note that `y -> exp[-B(y_+)^2]` is log-concave because `(y_+)^2` is convex. Gaussian convolution preserves log-concavity, hence

`u_mumu<=0`.

On the other hand, differentiating the Gaussian location family under its tilted conditional law gives the exact score-variance identity

`u_mumu = Var_tilt(Y)/s^4 - 1/s^2 >= -1/s^2 > -3`,

because `s^2>1/3` on `Q`. Hence `|u_mumu|<=3`.

Finally Jensen gives

`u=log E exp[-B Y_+^2] >= -B E Y_+^2`,

while `u<=0`. Therefore

`|u|<=B E Y^2`
` <=5[(100/81)z^2+1]`
` <7z^2`.

### Proof: exact Gaussian tail constants

Let `phi` be the standard Gaussian density. The first six terms of the exponential series give the exact rational inequality

`e > 1+1+1/2+1/6+1/24+1/120 = 163/60`.

Also `sqrt(2pi)>2`. Hence

`phi(9)=(2pi)^(-1/2)e^(-81/2)`
`       < U := (1/2)(60/163)^40`.

Mills' inequality follows directly from `x>=9`:

`barPhi(9) < phi(9)/9 < U/9`.

For the one-sided Gaussian tail moments

`R_k=int_9^infinity x^k phi(x) dx`,

integration by parts gives

`R_k=9^(k-1)phi(9)+(k-1)R_(k-2)`.

Therefore

`int_{|z|>9} z^2 phi(z)dz`
` < T_2 := 2(82/9)U`,

`int_{|z|>9} z^4 phi(z)dz`
` < T_4 := 2(2269/3)U`.

The derivative envelopes imply

`Tail(I) <=7T_2`,

`Tail(I_B) <=3T_2`,

`Tail(I_BB) <=4T_4`,

`Tail(K) <=1600T_2`,

`Tail(K_B) <=19200T_4`.

For `K_p`, because `u_mumu<=0`,

`|u_mu^2+p(u_mumu^2-2u_mu^2u_mumu)|`
` <=1600z^2+9+9600z^2`
` <12000z^2`,

so `Tail(K_p)<=12000T_2`.

Using `p>3/5` in the exact full-value identities for `I_p,I_Bp` multiplies the omitted `K,K_B` contributions by at most `5/6`. Substituting the rational `U,T_2,T_4` gives the advertised decimal upper bounds. QED.

### What this closes and what it does not

This theorem closes a specific gap in the preceding centered-Hessian report: the derivative tails outside `|z|<=9` are no longer an unproved numerical assumption. The remaining source-moving obligation is now the **compact interval/Taylor enclosure on `[-9,9]`**, plus propagation through the deterministic reconstruction. The theorem does not by itself certify `alpha=12.75`.

---

# Attack 2 — exact entropy/variance balance for the delicate `H_B` sign

A tempting route is to try to prove `H_B>0` abstractly from log-concavity. The following exact rewrite shows both what that route gains and why it is not yet sufficient.

For fixed `(p,z)`, let `nu` be the conditional Gaussian law of `Y`, let

`X=Y_+^2`,

and define its exponential tilt

`d nu_B/d nu = exp(-BX)/f`.

Write

`m_2=E_{nu_B}X`, `v=Var_{nu_B}(X)`.

After averaging over `Z`, put

`M=E m_2=-I_B>0`,

`V=E v=I_BB>=0`,

`L=E KL(nu_B||nu)`.

## Lemma R14-T03-ENTROPY-BALANCE

One has exactly

`L=-(I-BI_B)`,

`L_B=B V`,

and therefore

`L(B)=int_0^B t V(t) dt`.

Moreover

`H=-L+4B^2 M A_0`.

At any stationary point satisfying `H=0`,

`A_0=L/(4B^2M)>0`,

and the partial derivative along the reconstructed `D=D(p,B)` satisfies

`H_B = 2L/B - B V - L V/M + L (A_{0,D}/A_0) D_B`.        (E1)

The first two terms admit the exact variance-monotonicity representation

`2L/B-BV`
`=(2/B) int_0^B t [V(t)-V(B)] dt`.                          (E2)

### Proof

Pointwise,

`KL(nu_B||nu)=E_{nu_B}[-BX-log f]=-B m_2-log f`.

Averaging gives

`L=-BM-I=-(I-BI_B)`.

For an exponential family, `partial_B m_2=-v`; differentiating the preceding identity gives

`L_B=B V`.

Since `L(0)=0`, integration yields `L(B)=int_0^B tV(t)dt`.

Because `I_B=-M`, the stationary residual is

`H=I-BI_B-4B^2I_BA_0=-L+4B^2MA_0`.

At `H=0`, solve for `A_0`. Differentiating `H` at fixed `p` along the reconstructed `D(p,B)` gives

`H_B=-BV+8BMA_0-4B^2VA_0+4B^2M A_{0,D}D_B`.

Substitution of `A_0=L/(4B^2M)` gives (E1). Formula (E2) follows by subtracting

`BV=(2/B)int_0^B tV(B)dt`

from `2L/B`. QED.

### Certified obstruction learned from this rewrite

Log-concavity alone gives `L>=0`, `M>0`, `V>=0`, but these signs do **not** determine the sign of (E1). A successful entropy proof must additionally control at least:

1. the variation of `V(t)` along the whole tilt interval `0<=t<=B` (or another lower bound for `2L/B-BV`), and
2. the reconstructed radial term `(A_{0,D}/A_0)D_B`.

Thus merely proving convexity of `I` in `B` or positivity of conditional variances cannot close `H_B>0`. This is a precise obstruction, not a request for finer numerical sampling.

At the existing numerical-only center, the four contributions to (E1) are approximately

`+0.0200662`, `-0.0160739`, `-0.0035544`, summing to `+0.0004379` after grouping the first pair as in (E1). The small final margin explains why direct dependency-losing product intervals wrapped badly. These numbers are diagnostics only and are not used as proof.

---

# Attack 3 — exact radial polar duality, and why ordinary Farkas duality is too weak

This attack moves the source problem from a nonconvex sphere feasibility statement to the inradius of a Gaussian polytope.

For a fixed realization, define

`P={x in R^N: Gx >= -1}`

and

`K=conv(0,-g_1,...,-g_M)`.

The source event is `P cap S^{N-1} != empty`.

## Lemma R14-T03-POLAR-RADIAL

For every deterministic matrix `G`,

`P^circ=K`,

where `P^circ` is the polar body. Equivalently, if

`r(K)=min_{||u||=1} h_K(u)`

is the Euclidean inradius of `K`, then

`source SAT <=> r(K)<=1`,

`source UNSAT <=> r(K)>1`,

apart from the equality boundary already included in SAT by the non-strict source inequalities.

### Proof

The inequalities defining `P` are

`<-g_a,x><=1`.

The polar of the intersection of these halfspaces, with `0 in P`, is the closed convex hull of their normals together with zero, namely `K`.

More directly,

`h_K(u)=max(0,max_a <-g_a,u>)`.

Hence `r(K)<=1` exactly when there exists a unit vector `u` such that

`<-g_a,u><=1` for every `a`,

i.e.

`<g_a,u>>=-1` for every `a`.

That is exactly the normalized source SAT event. QED.

## Corollary: a one-vector Farkas infeasibility certificate cannot prove source UNSAT

The linear inequality system `Gx>=-1` is never infeasible: `x=0` satisfies it strictly. Therefore ordinary Farkas duality for the linear constraints alone cannot certify the source UNSAT event. The entire obstruction is radial: one must show that the feasible polyhedron never reaches radius one, equivalently that **every direction** has Gaussian-polytope support exceeding one.

Thus a successful direct dual route must be intrinsically multidirectional (for example a certified inradius/facet/covering or stronger convex-geometric comparison). A single nonnegative linear combination of constraints cannot by itself encode the missing sphere-radius obstruction.

This exact polar formulation is likely standard convex duality and is **not claimed as novel**. Its value here is diagnostic: it rules out spending another run on ordinary LP-Farkas certificates and clarifies why the previously attempted facet/inradius methods were the correct dual category but need a stronger probabilistic estimate.

---

# 4. Source metric and auxiliary movement

## Source metric

Before:

`alpha_L=6.30297437506`,

`alpha_U=12.78437096216`,

width `6.48139658710`.

After this artifact: identical.

**Source movement: none.**

The `alpha=12.75` complete-second-lift point remains candidate-only.

## Auxiliary movement

1. The full-line first-Jacobian tail layer on the current `12.75` box is now analytical and explicit; the previous report's “tail derivatives not yet claimed” caveat is removed for `I,I_B,I_BB,K,K_B,K_p` and the OU-reconstructed `I_p,I_Bp`.
2. The `H_B` sign problem is rewritten exactly as the entropy/variance/radial balance (E1)-(E2), isolating the cancellations that any proof must preserve.
3. The direct dual route is localized to Gaussian-polytope inradius control; ordinary linear Farkas infeasibility is proved structurally irrelevant because `x=0` is always strictly feasible.

# 5. Remaining full-scope gap

The highest-value next step remains within the same complete-second-lift route, but is now more sharply delimited:

- rigorously enclose the **compact** one-dimensional moment integrals and their second derivatives on `|z|<=9` over the small R14 box;
- combine them with R14-T03-FIRST-JAC-TAIL rather than inventing derivative-tail numerics;
- certify either the centered-Hessian contraction hypotheses or the monotone-face conditions `H_B>0`, `alpha_p>0` plus four corner signs;
- enclose `Psi>0` on the resulting root box;
- only then invoke the already source-matched Stojnic complete-second-lift implication to move `alpha_U`.

A separate possible analytical shortcut is suggested by (E1): prove a quantitative lower bound for the variance-history term (E2) and a matching bound for the radial correction. No such sign theorem is claimed here.

Status remains **OPEN / PARTIAL**.