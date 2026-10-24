SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T02:29:19Z.
attacking: sharpness of the proved qualitative C0 regularity — test whether any target-uniform continuity, Hölder, Sobolev, or BV modulus can be added to the universal-height programme.

# account03/B15 r24 — no uniform regularity modulus, even in the diagonal analytic-Schwartz subclass

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Run:** `20260923T022919Z-account03-B15-qform-r24`  
**Status:** `ESSENTIAL_STEP_APPLIED / UNIFORM_REGULARITY_UPGRADE_REFUTED / UNIVERSAL_HEIGHT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result

The full universal QFORM density-height conjecture remains **OPEN**. The fixed-instance B15 chain gives a bounded `C_0` density for each target instance, but this run proves that this qualitative continuity statement is essentially sharp: there is **no target-uniform modulus of continuity**, no uniform positive Hölder bound, no uniform positive Sobolev bound, and no uniform BV bound, even in the completely separable matrix `A=I_3`, with smooth cap-one input densities and uniformly bounded output height.

The failure persists after replacing the marginals by strictly positive real-analytic Schwartz densities with cap at most one. Thus a compactness argument for the missing universal height cannot legitimately insert a target-uniform equicontinuity/BV/positive-Sobolev estimate. The remaining universal-height estimate must control the positive heat/tent functional directly at each scale, or exploit another structure that does not require such a modulus.

This is a counterexample to a **possible regularity upgrade**, not to the QFORM conjecture itself.

## 2. A phase-aligned smooth cap-one marginal

Fix `s>=2` and let

`alpha = arccos(3/4)`, `theta = alpha/pi`.

On `(1,10)` define the open phase-good set

`G_s = {x : cos(s x^2)>3/4}`.

Put `u=x^2`. On `u in (1,100)`, `dx=du/(2 sqrt(u)) >= du/20`. In each full `u`-period of length `2pi/s`, the set on which `cos(su)>3/4` occupies the fraction `theta`. Removing at most two partial periods from an interval of length 99 gives

`|G_s| >= theta (99-4pi/s)/20`.

At `s=2` the right side is already greater than `1.06`, and it increases with `s`. Hence `|G_s|>1` for every `s>=2`.

Because `G_s` is open and has measure greater than one, there is a function

`f_s^0 in C_c^infinity(G_s)`, `0<=f_s^0<=1`, `integral f_s^0=1`.

Indeed, approximate `1_{G_s}` from below by a compactly supported smooth function with integral greater than one and then divide by its integral.

Let `Y_s` have density `f_s^0` and define

`g_s(t)=E exp(i t Y_s^2)`.

Since the support lies in `G_s`,

`Re g_s(s) >= 3/4`.

Also `1<Y_s<10`, so

`|g_s'(t)| <= E Y_s^2 <=100`.

Consequently, whenever `|t-s|<=1/400`,

`Re g_s(t) >= 1/2`.

## 3. Target output and a high-frequency Fourier spike

Take three independent copies `Y_{s,1},Y_{s,2},Y_{s,3}` and the fixed target matrix

`A=I_3`.

Then

`Q_s^0=Y_{s,1}^2+Y_{s,2}^2+Y_{s,3}^2`

is a legitimate QFORM target with exactly three eigenvalues equal to one. Its characteristic function is

`phi_s^0(t)=g_s(t)^3`.

Therefore

`|phi_s^0(s)| >= (3/4)^3 = 27/64`,

and on `|t-s|<=1/400`,

`|phi_s^0(t)| >= (1/2)^3 =1/8`.

The density of `Y_s^2` is

`h_s(y)=f_s^0(sqrt(y))/(2 sqrt(y))`

on `(1,100)`. Hence `h_s in C_c^infinity((1,100))`, it is a probability density, and `||h_s||_infinity<=1/2`. Thus

`p_s^0=h_s*h_s*h_s`

lies in `C_c^infinity((3,300))`, with `||p_s^0||_infinity<=1/2` (and, independently, the standard diagonal QFORM bound gives `<=pi`).

So this is an especially benign family: the matrix is fixed, the three marginals are smooth and compactly supported, the output supports all lie in one fixed compact interval, and the output heights are uniformly bounded.

## 4. No common modulus of continuity

For `h=pi/s`, Fourier translation gives

`||p_s^0(.+h)-p_s^0||_1
 >= |exp(i s h)-1| |phi_s^0(s)|
 =2|phi_s^0(s)|
 >=27/32`.

The two translated supports lie in an interval of length at most `297+h<300`. Therefore

`sup_x |p_s^0(x+pi/s)-p_s^0(x)| >= (27/32)/300 =27/9600`.

Since `pi/s ->0`, the family `{p_s^0}` is not equicontinuous. In particular, there is no deterministic modulus `omega(r)->0` such that every target density obeys

`|p_Q(x+r)-p_Q(x)| <= omega(|r|)`.

This remains false even if one restricts to the fixed matrix `I_3` and smooth compactly supported cap-one marginals.

For every `0<beta<=1`, the same estimate yields the quantitative lower bound

`[p_s^0]_{C^{0,beta}} >= (27/9600)(s/pi)^beta`,

whenever the seminorm is finite. Hence there is no uniform positive Hölder estimate.

## 5. No uniform BV or positive Sobolev control

If `p_s^0` is regarded as a BV function, then

`TV(p_s^0)=||(p_s^0)'||_1 >= |widehat{(p_s^0)'}(s)| = s |phi_s^0(s)| >= 27s/64`.

Thus BV norms diverge at least linearly.

With the Fourier convention for which

`||p||_{H^beta}^2=(1/(2pi)) integral (1+t^2)^beta |hat p(t)|^2 dt`,

the interval `|t-s|<=1/400` gives, for every `beta>0`,

`||p_s^0||_{H^beta}^2
 >= (1/(25600 pi)) [1+(s-1/400)^2]^beta`.

Hence no positive Sobolev norm can be bounded uniformly over the target class either.

These failures do not contradict individual smoothness: every `p_s^0` is `C_c^infinity`; its derivatives simply oscillate faster as `s` grows.

## 6. Strengthening to the analytic-Schwartz normal form

The completed B15 source chain reduces sharp universal height to a class with strictly positive real-analytic Schwartz marginals. The preceding obstruction survives in that class.

Assume `s>=20`, set `eta_s=s^{-3}`, let `Z~N(0,1)` be independent of `Y_s`, and put

`X_s=Y_s+eta_s Z`.

Its density

`F_s=f_s^0 * gamma_{eta_s}`

is strictly positive, real analytic, Schwartz, integrates to one, and satisfies `||F_s||_infinity<=1` because Gaussian convolution is an `L^infinity` contraction.

Moreover

`|E exp(i s X_s^2)-E exp(i s Y_s^2)|
 <= s E|X_s^2-Y_s^2|
 <=20/s^2+1/s^5`.

For `s>=20` this is less than `0.051`, so

`Re E exp(i s X_s^2) >=2/3`.

Also `E X_s^2<=101`, hence the one-coordinate phase characteristic function changes by at most `101|t-s|`. Thus on `|t-s|<=1/1000` its real part remains greater than `1/2`.

For three iid copies and again `A=I_3`, let `p_s` be the density of

`Q_s=X_{s,1}^2+X_{s,2}^2+X_{s,3}^2`.

Then

`|widehat p_s(s)| >= (2/3)^3=8/27`,

and

`|widehat p_s(t)|>=1/8` for `|t-s|<=1/1000`.

The diagonal theorem still gives

`||p_s||_infinity<=pi`.

Although the marginals now have Gaussian tails, they remain uniformly tight at a fixed output scale. Since `|Y_s|<=10`,

`P(|X_s|>11) <= P(eta_s |Z|>1) <= eta_s^2=s^{-6}`.

Thus

`delta_s:=P(Q_s notin [0,363]) <=3s^{-6}`.

Again set `h=pi/s` and write

`omega_s(h)=sup_x |p_s(x+h)-p_s(x)|`.

Fourier translation gives

`||p_s(.+h)-p_s||_1 >=2|widehat p_s(s)|>=16/27`.

Let `K=[0,363]`. Outside `K union (K-h)`, both translated tail integrals total at most `2 delta_s`; on this union, whose length is `363+h`, the difference is at most `omega_s(h)`. Hence

`omega_s(pi/s)
 >= [16/27-6s^{-6}]/[363+pi/s]`.

For every `s>=20` the right side exceeds `10^{-3}`. Therefore **even the strictly positive analytic-Schwartz normalized target subclass is not equicontinuous**.

The same Fourier spike gives, if finite,

`TV(p_s)>= (8/27)s`,

and for every `beta>0`,

`||p_s||_{H^beta}^2
 >= (1/(64000 pi))[1+(s-1/1000)^2]^beta`.

Thus the analytic-Schwartz reduction does not secretly supply a uniform regularity modulus.

## 7. Actual application of the assigned partner account04/B15 result

The completed assigned partner result is

- `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

For every probability law `mu`, it proves

`sup_{epsilon>0,y} (mu*gamma_epsilon)(y)=||p_mu||_infinity`,

with the extended value `+infinity` if no bounded density exists.

Apply it to the analytic-Schwartz diagonal targets above. Since the diagonal theorem gives `||p_s||_infinity<=pi`, the partner theorem yields the actual all-scale inequality

`H_{s,epsilon}(y):=(p_s*gamma_epsilon)(y) <= pi`

for every `epsilon>0`, every `y`, and every `s>=20`.

Now take the natural heat scale `epsilon=1/s`. Its Fourier transform is

`widehat H_s(t)=widehat p_s(t) exp(-t^2/(2s^2))`.

At the phase-aligned frequency `t=s`,

`|widehat H_s(s)| >= (8/27)e^{-1/2}`.

Because `H_s'=p_s*gamma_{1/s}'` lies in `L^1`, Fourier differentiation gives

`||H_s'||_1 >= s |widehat H_s(s)| >= 8s/(27 sqrt(e))`.

Therefore we have the concrete simultaneous pair of inequalities

`boxed{ ||H_s||_infinity <= pi,   ||H_s'||_1 >= 8s/(27 sqrt(e)). }`

So even the exact positive heat profiles whose heights characterize the target constant can have uniformly bounded height while their total variation diverges linearly as the heat scale tends to zero. This is the required direct application of the partner theorem to an actual inequality.

## 8. Consequence for the full proof strategy

The B15 qualitative regularity conclusion and the central universal-height problem must remain separate:

- fixed target instances may have `p_Q in C_0 cap L^infinity`;
- a universal density-height theorem, if true, does **not** come with any target-uniform continuity modulus merely from the stated hypotheses;
- no proof may obtain the missing universal height by first asserting a uniform Hölder, BV, or positive-Sobolev compactness estimate for all target densities or for their shrinking-scale heat profiles.

The constructive obstruction already occurs for `A=I_3`, so it is unrelated to rotated-coordinate dependence, indefinite signs, small physical minors, or high dimension. It is exactly the known fragmented phase-alignment phenomenon expressed on the output-density side.

The first unpaid implication therefore remains the uniform **height** estimate itself: bound the positive heat/tent functional scale by scale while allowing arbitrarily rapid output oscillation.

## 9. Scope and corrections

This report does not use or revive any refuted intermediate mechanism. In particular it does not assume law-uniform pointwise van-der-Corput decay, an arbitrary-joint rank-three coarea theorem, positive moments of conditional projection caps, post-rotation independence, fiber-supremum dimension-free control, or a uniformly conditioned physical minor.

The construction is fully within the original product class and the target eigenvalue hypothesis. It does not challenge the diagonal `L^infinity` theorem; indeed its output heights stay uniformly bounded. It challenges only a stronger **uniform regularity-modulus** assertion that is not part of the central conjecture.
