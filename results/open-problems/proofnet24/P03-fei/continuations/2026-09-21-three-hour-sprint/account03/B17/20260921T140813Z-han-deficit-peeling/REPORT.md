# B17 FEI new proof mechanism: Han-deficit / local-credit block peeling

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical-brain retrieval or receiver-context use occurred.  
**Role:** account03/B17, FEI new proof mechanisms.  
**Live sprint assignment:** higher-order face-boundary / rare-pair information.  
**Route:** new continuation — **Han-deficit / local-credit multiscale face-channel recursion**. This changes method from the preceding search for sharper large-block face-channel constants, which was refuted by the bent/one-vertex-flip family.

Mandated scientific entry was read in order from `TASKS_2026-09-21.md`, `REPORT.md`, then `APPROACHES.md` at scientific head `9f484968924b02bb3ed0e49efddedb831a449a44`. The current owner correction was respected: unrestricted FEI has an externally recovered lower bound above `6.521845710923046575`, so the older `6.4547837...` read-once scale is not used as the unrestricted target. No read-once audit, old `n<=5` FEI sweep, or unchanged face-state constant search was performed.

## 1. Setup and previous inputs used

Let `f:{-1,1}^n->{-1,1}` and let `S` be its Fourier spectral sample,

\[
\Pr(S=A)=\widehat f(A)^2,
\qquad H(f)=H(S),
\qquad I(f)=\mathbb E|S|.
\]

For a coordinate block `R subseteq [n]`, `|R|=r`, and an outside assignment `y`, let `f_y` be the Boolean restriction to the physical `R`-face. Define

\[
F_f(R):=\mathbb E_y H(f_y).
\]

The previous B17 face-channel theorem proves that the local-spectrum channel has output law exactly `S cap R` and hence

\[
J_f(R):=H(S\cap R)-F_f(R)=I(Y;T)\ge0. \tag{1.1}
\]

The sharper finite-state transport theorem then proves

\[
J_f(R)\le C_r I_{R^c}(f), \tag{1.2}
\]

where `C_r` is the optimal Boolean `r`-face transport constant. In particular

\[
C_1=2,
\qquad C_2=8-\frac52\log_2 5=2.195179762781594\ldots,
\qquad C_r\le c_\infty:=\frac2{\ln2}=2.885390081777927\ldots . \tag{1.3}
\]

The preceding B17 run also proved that the large-block hope `sup_r C_r<c_infty` is false: even block sizes approach `c_infty` through an exact Boolean bent-face/one-vertex-flip construction. Therefore this run does not try to improve the large-block coefficient again.

For a uniformly random `r`-subset `R`, the exact influence averaging identity is

\[
\mathbb E_R I_R(f)=\frac rn I(f),
\qquad
\mathbb E_R I_{R^c}(f)=\left(1-\frac rn\right)I(f). \tag{1.4}
\]

## 2. PROVED: a finite-dimensional block recurrence

Let

\[
M_r:=\sup\left\{\frac{H(g)}{I(g)}:g\text{ Boolean on }r\text{ variables},\ I(g)>0\right\}.
\]

### Theorem 2.1

For every `1<=r<n`,

\[
\boxed{
M_n\le M_r+C_r\left(\frac nr-1\right).
} \tag{2.1}
\]

### Proof

For an arbitrary discrete random vector `X=(X_1,...,X_n)`, Han/Shearer projection entropy gives

\[
H(X)\le\frac nr\,\mathbb E_{|R|=r}H(X_R). \tag{2.2}
\]

Apply this to the membership vector of `S`. By (1.1),

\[
H(S_R)=F_f(R)+J_f(R).
\]

Each face `f_y` is Boolean on `r` variables, so

\[
F_f(R)=\mathbb E_y H(f_y)
\le M_r\,\mathbb E_y I(f_y)
=M_r I_R(f). \tag{2.3}
\]

The last equality is the physical/Fourier restriction identity for influences inside `R`. By (1.2),

\[
J_f(R)\le C_r I_{R^c}(f). \tag{2.4}
\]

Average (2.3)-(2.4) over `R`, use (1.4), multiply by `n/r`, and obtain

\[
H(f)\le\left[M_r+C_r\left(\frac nr-1\right)\right]I(f).
\]

Taking the supremum proves (2.1). □

### What this does and does not do

This is a universal recurrence, but iterating it naively over fixed-ratio blocks accumulates a logarithmic number of channel charges. It is therefore **not** a proof of FEI. Its value is that it exposes exactly what must cancel in a successful multiscale recursion.

## 3. PROVED: exact Han-deficit slack identity

Define the nonnegative Han projection deficit

\[
D_r(f):=\frac nr\,\mathbb E_{|R|=r}H(S\cap R)-H(S)\ge0. \tag{3.1}
\]

For any target constant `C`, define the usual FEI slack

\[
\operatorname{Slack}_C(f):=C I(f)-H(f).
\]

### Theorem 3.1 — exact block slack decomposition

For every Boolean `f` and every `1<=r<n`,

\[
\boxed{
\operatorname{Slack}_C(f)
=\frac nr\,\mathbb E_{R,y}\operatorname{Slack}_C(f_y)
+D_r(f)
-\frac nr\,\mathbb E_R J_f(R).
} \tag{3.2}
\]

### Proof

By (1.1),

\[
\mathbb E_R H(S_R)=\mathbb E_{R,y}H(f_y)+\mathbb E_R J_f(R). \tag{3.3}
\]

Also by (1.4),

\[
C I(f)=\frac nr\,\mathbb E_R C I_R(f)
=\frac nr\,\mathbb E_{R,y} C I(f_y). \tag{3.4}
\]

From the definition of `D_r`,

\[
H(f)=\frac nr\,\mathbb E_R H(S_R)-D_r(f).
\]

Substitute (3.3)-(3.4) and rearrange. □

Equation (3.2) is the main structural advance of this run. It shows that repeated face-channel information has **two distinct refund mechanisms**:

1. local FEI slack already present inside the lower-dimensional faces;
2. the global Han projection deficit `D_r`.

The preceding hierarchy proposal charged the channel term but did not isolate these refunds exactly.

## 4. REFUTED-LEMMA: Han projection deficit alone cannot pay the channel

The strongest scalar-only version of the new mechanism would be a universal inequality

\[
D_r(f)\ge\kappa\frac nr\,\mathbb E_R J_f(R) \tag{4.1}
\]

for some fixed `kappa>0`. This is false, even for exactly Boolean functions and with arbitrarily large `J`.

Take the standard quadratic bent phase on `n=2m` variables,

\[
b(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{2m-1}x_{2m}}. \tag{4.2}
\]

Its spectral law is uniform on all `2^n` subsets, so for every `r`-subset `R`,

\[
H(S_R)=r,
\qquad H(S)=n,
\qquad D_r(b)=\frac nr r-n=0. \tag{4.3}
\]

Now choose `R` to contain one endpoint from each of `r` distinct quadratic pairs. After the complementary endpoints are fixed, every physical `R`-face is a character. Therefore

\[
F_b(R)=0,
\qquad J_b(R)=H(S_R)=r. \tag{4.4}
\]

Thus `D_r=0` while `J_r=r>0`. No positive `kappa` in (4.1) can work.

This **does not refute FEI**: the same bent function has

\[
H(b)=n,
\qquad I(b)=n/2,
\qquad H/I=2.
\]

The missing payment sits entirely in the local face slack, exactly as (3.2) predicts. This stress test rules out a false simplification while preserving the combined mechanism.

## 5. PROVED: a block-peeling inequality and a low-influence reduction

Write

\[
p_j:=\Pr(j\in S)=\operatorname{Inf}_j(f).
\]

### Theorem 5.1 — fixed-block peeling

For every fixed `R`, `|R|=r`,

\[
\boxed{
H(f)
\le M_r I_R(f)
+\sum_{j\notin R}\bigl[h_2(p_j)+C_r p_j\bigr].
} \tag{5.1}
\]

### Proof

Entropy subadditivity conditioned only at the level of the spectral membership vector gives

\[
H(S)\le H(S_R)+\sum_{j\notin R}H(1_{j\in S})
=H(S_R)+\sum_{j\notin R}h_2(p_j). \tag{5.2}
\]

The face-channel theorem and the `r`-dimensional FEI constant give

\[
H(S_R)=F_f(R)+J_f(R)
\le M_r I_R(f)+C_r I_{R^c}(f).
\]

Since `I_{R^c}=sum_{j notin R}p_j`, combine with (5.2). □

### Corollary 5.2 — peeling criterion

If `M_r<=C` and every `j notin R` satisfies

\[
h_2(p_j)\le(C-C_r)p_j, \tag{5.3}
\]

then `H(f)<=C I(f)`.

For `r=2`, `M_2=2` and the exact `C_2` from (1.3) apply. Consequently, at any target `C> C_2`, all but at most two coordinates of a counterexample must lie in the "dangerous" marginal range

\[
\frac{h_2(p)}p>C-C_2. \tag{5.4}
\]

At the currently recovered unrestricted lower-bound scale

\[
C_{\rm ext}=6.521845710923046575,
\]

(5.4) is equivalent on `0<p<=1/2` to approximately

\[
\boxed{p<0.126783898620952}. \tag{5.5}
\]

Thus any counterexample at that scale must have at least three genuinely low-influence coordinates. This is not closure, but it is an exact structural reduction.

### Corollary 5.3 — minimal-dimensional counterexamples are uniformly low-influence

Assume FEI with constant `C` is already known for all Boolean functions on fewer than `n` variables, and suppose `f` is an `n`-variable minimal counterexample. Choose `R=[n]\setminus\{j\}` in (5.1). Then `M_{n-1}<=C` and `C_{n-1}<=c_infty=2/ln2`, so every coordinate must satisfy

\[
\boxed{
\frac{h_2(p_j)}{p_j}>C-c_\infty.
} \tag{5.6}
\]

At `C=C_ext`, this forces

\[
\boxed{p_j<0.196692512551412\quad\text{for every }j.} \tag{5.7}
\]

At `C=7`, it forces

\[
\boxed{p_j<0.145363943515672\quad\text{for every }j.} \tag{5.8}
\]

This isolates the genuinely hard regime: any minimal counterexample must have *all* coordinates rare. That is exactly the regime where the owner's higher-order face-boundary assignment should concentrate.

## 6. PROVED exact one-point profile: Han deficit nearly cancels the channel debt

The one-point Boolean family is a useful boundary test because small blocks make the raw block-channel recurrence look catastrophically expensive.

Let `f_n` be `+1` except at one cube vertex where it is `-1`, and put

\[
a=2^{1-n}.
\]

Every physical influence is exactly `a`, so `I(f_n)=na`.

For a fixed `r`-block `R`, every nonempty atom of the marginal spectral law `S cap R` has mass

\[
b=2^{2-n-r}=a\,2^{1-r},
\]

and the empty atom has mass `1-(2^r-1)b`. Hence

\[
H_R:=H(S\cap R)
=\phi(1-(2^r-1)b)+(2^r-1)\phi(b), \tag{6.1}
\]

where `phi(x)=x log_2(1/x)`.

A nonconstant physical `R`-face appears only when all outside coordinates equal the exceptional outside pattern, an event of probability `2^{r-n}`. Therefore

\[
F_f(R)=2^{r-n} H(f_r),
\qquad
J_f(R)=H_R-F_f(R). \tag{6.2}
\]

These formulas are exact.

If `r=alpha n` with fixed `0<alpha<1`, direct expansion gives

\[
\frac{H(f_n)}{I(f_n)}\to4,
\qquad
\frac{H_R}{I(f_n)}\to2(1+\alpha),
\qquad
\frac{F_R}{I(f_n)}\to4\alpha,
\qquad
\frac{J_R}{I(f_n)}\to2(1-\alpha), \tag{6.3}
\]

and therefore

\[
\frac{D_r(f_n)}{I(f_n)}\to2\left(\frac1\alpha-1\right),
\qquad
\frac nr\frac{J_R}{I(f_n)}\to2\left(\frac1\alpha-1\right). \tag{6.4}
\]

So on this exact low-influence family the Han deficit asymptotically refunds **all** of the scaled channel information. This is the opposite boundary behavior from the bent family, where `D=0` and local face slack pays everything. The combined identity (3.2) captures both extremes without case-specific assumptions.

At `n=64,r=32`, the exact/high-precision checker gives

```text
H/I                 = 3.982584220
H(S_R)/I            = 2.982584219
F_R/I               = 1.982584220
J_R/I               = 1.000000000
D_r/I               = 1.982584219
(n/r) J_R/I         = 2.000000000
(n/r) H(S_R)/I      = 5.965168439
```

At `n=128,r=64` these converge further to `4,3,2,1,2,2,6`. This is a decisive diagnostic: a proof that separately upper-bounds every scale's channel term throws away an almost exact cancellation already visible on one-point functions.

## 7. CONDITIONAL route: local marginal credits plus Han deficit

For an `r`-bit Boolean face `g`, define the nonnegative marginal credit at target `C`

\[
A_C(g):=\max\left\{0,
\sum_{i=1}^r\bigl[C\operatorname{Inf}_i(g)-h_2(\operatorname{Inf}_i(g))\bigr]
\right\}. \tag{7.1}
\]

If FEI with constant `C` is already known in dimension `r`, then

\[
\operatorname{Slack}_C(g)\ge A_C(g). \tag{7.2}
\]

Indeed FEI gives `Slack_C(g)>=0`, while spectral entropy subadditivity gives

\[
H(g)\le\sum_i h_2(\operatorname{Inf}_i(g)),
\]

so

\[
\operatorname{Slack}_C(g)
\ge\sum_i[C\operatorname{Inf}_i(g)-h_2(\operatorname{Inf}_i(g))].
\]

Combining (7.2) with the exact identity (3.2) yields the following **sufficient**, currently OPEN, block-refund inequality:

\[
\boxed{
D_r(f)+\frac nr\mathbb E_{R,y}A_C(f_y)
\ge\frac nr\mathbb E_R J_f(R).
} \tag{7.3}
\]

If (7.3) held at some lower dimension `r<n` for every Boolean `f`, it would propagate FEI(C) from dimension `r` to dimension `n`.

This is **not claimed proved**. It is the precise universal lemma that this run proposes after the previous large-block-constant route died.

### Why (7.3) survives the two exact obstructions

- **Bent phase:** `D_r=0` can coexist with large `J_r`, refuting a deficit-only proof. But the relevant character faces have enormous positive local credit/slack for every target `C>2`, so the combined mechanism is not refuted.
- **One-point family:** local credits can be small on rare faces, but (6.4) shows `D_r` asymptotically pays the entire scaled `J_r` debt.

Thus the two boundary families stress complementary terms rather than killing the combined inequality.

## 8. Targeted exact computation, not an exhaustive FEI sweep

A new checker `block_profile_check.py` was written specifically for (7.3). It uses integer Walsh transforms and exact `Fraction` probabilities for finite Boolean examples; high-precision Decimal arithmetic is used for the analytic one-point profiles. Floating-point logs are used only for displayed Shannon values.

It tests a small adversarial panel, not a known exhaustive sweep:

- one-point functions (`n=4,6`);
- standard quadratic bent phases (`n=4,6`);
- majority (`n=5`);
- width-2 tribes (`n=6,8`);
- block sizes about `n/2` and `n-1`;
- target constants `C_ext=6.521845710923046575` and `C=7`.

No violation of (7.3) was found in this targeted panel. This is evidence only, not a universal proof.

At `C_ext`, the smallest displayed gap was the six-bit one-point function with `r=5`:

\[
H=0.701205753356,
\qquad
\text{refund-RHS}=0.890427195891,
\qquad
\text{gap}=0.189221442535>0.
\]

For width-2 tribes on eight bits:

```text
r=4: H=5.543984600917  RHS=10.770393156511  gap=5.226408555595
r=7: H=5.543984600917  RHS=10.532955548593  gap=4.988970947676
```

The exact bent obstruction is also emitted by the checker as a symbolic family statement: for `n=2m` and `R` choosing one endpoint from `r` distinct quadratic pairs, `D_r=0`, `F_R=0`, `J_R=r`, and `H/I=2` exactly.

Local pre-commit SHA-256 values from the native run:

- `block_profile_check.py`: `510f10e94d4d5848d85c7760296ebd6181c9edc25378a9041e08ae8651f36a92`
- `OUTPUT.txt`: `c0be1a88d7999fc8e54715e170f2dc90f4eca5c599f71372e2f0bb1992373f4f`

## 9. Claim ledger

### PROVED

1. The finite-dimensional recurrence `M_n <= M_r + C_r(n/r-1)`.
2. The exact Han-deficit FEI-slack identity (3.2).
3. The fixed-block peeling inequality (5.1).
4. The dangerous-influence criterion (5.3)-(5.5), including the exact use of the sharp pair constant.
5. The minimal-dimensional low-influence reduction (5.6), giving the concrete thresholds (5.7)-(5.8).
6. Exact formulas (6.1)-(6.2) for the one-point family and the asymptotics (6.3)-(6.4), showing the Han deficit asymptotically refunds the scaled channel debt at proportional block size.

### REFUTED-LEMMA

A positive universal comparison `D_r >= kappa (n/r) E_R J_R` cannot hold. Exact Boolean quadratic bent phases have `D_r=0` while selected physical faces have `J_r=r>0`.

### CONDITIONAL / OPEN

1. Full FEI remains **OPEN / NOT PROVED**.
2. The combined block-refund inequality (7.3) is a sufficient induction lemma, but it is not proved universally.
3. The targeted finite examples are only stress tests; they do not establish (7.3).
4. No novelty or publication-priority claim is made for the new formulation without a dedicated literature search.

## 10. Next attack

Do **not** return to searching for a dimension-uniform improvement of `C_r`; the bent/one-vertex-flip family already killed that route.

The next B17 attack should focus on the all-low-influence regime isolated by (5.7): try to prove or refute (7.3) for Boolean functions whose every influence satisfies

\[
p_i<0.196692512551412
\]

at the current lower-bound scale, using higher-order face geometry rather than another marginal-only inequality. A promising precise target is a stability version of Han's inequality in which small projection deficit forces the physical face channel to be close to an affine/bent tensor structure; in that structured regime the local credit term should be explicitly large. If an exact Boolean counterexample to (7.3) appears, record it and change mechanism rather than patching the same checker.

The central new dichotomy to exploit is now concrete:

> large Han deficit pays cross-face information globally; tiny Han deficit should force enough near-product structure that lower-dimensional face slack pays it locally.

Proving that dichotomy, rather than improving a one-shot transport constant, is the next universal gap.
