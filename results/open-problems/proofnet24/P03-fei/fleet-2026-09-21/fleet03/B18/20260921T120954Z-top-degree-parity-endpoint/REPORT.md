# B18 FEI proof integration — top-degree parity eliminates the exact scalar hard-core endpoint

**Date:** 2026-09-21  
**Role:** fleet03/B18, FEI proof integration  
**Model:** GPT-5.6 Sol (self-report). **Reasoning level configured:** `UNKNOWN_NOT_EXPOSED`; maximum actually supported was requested.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`. Native probing in this run found neither `math_brain` nor the cognitive `brain` package, so no authenticated brain retrieval/context was used.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**New result:** **PROVED conditional only on the already-proved B14 exact scalar-frontier endpoint reduction.** It is not a proof of FEI and has not received independent closure review. No novelty/priority claim is made.

## 0. Fresh state integrated

The owner-required `TASKS_2026-09-21.md`, then continuation `REPORT.md`, then `APPROACHES.md` were read before this derivation. I then integrated the newest compatible FEI state rather than restarting an older handoff.

The key incoming B14 chain is:

1. For a restriction-critical Boolean function with ratio `r>4`, the sharp one-coordinate scalar theorem gives
   \[
   B_i\ge b(r)\alpha_i,\qquad b(r)=\beta(\tau(r)),\qquad \kappa(\tau(r))=r,
   \]
   where equality, together with the critical equality `Delta_i H=r alpha_i`, forces every positive fibre posterior to equal one common `tau`.
2. If this exact scalar endpoint is attained at every relevant coordinate, the squared Fourier law has the uniform-activity hard-core form
   \[
   p_S=\widehat f(S)^2=p_\varnothing\theta^{|S|}\mathbf 1_{\{S\in\mathcal F\}},
   \qquad \theta=\frac{\tau}{1-\tau},
   \tag{0.1}
   \]
   with `mathcal F` a downward-closed family.
3. The newest signed-link arithmetic theorem further proves, at any exact Boolean endpoint, that
   \[
   \sqrt\theta=\frac1m,\qquad m\in\{2,3,4,\ldots\}.
   \tag{0.2}
   \]
4. A subsequent B14 addendum used global entropy/influence arithmetic to reduce the surviving exact *critical* candidate to `m=3`, `theta=1/9`, `tau=1/10`, degree divisible by five and at least fifteen.

A fresh check of the current public optimization-constants record also matters: the best listed lower bound for the FEI constant is now the starred/certificate-based
\[
C_{\rm FEI}>6.521845710923046575,
\]
not Hod's `6.4547837...`. I did not independently replay that external certificate, so this number is used only as a calibration, not as a proved dependency of the theorem below.

The mechanism used here is a route-13 Booleanity/integrality move not present in the exact endpoint addendum: **look at the highest nonzero Fourier level, where an iterated physical derivative has a parity quantization that is much coarser than ordinary dyadic Fourier integrality.**

## 1. Exact statement attempted

> **Target.** Rule out the simultaneous exact scalar-frontier hard-core endpoint itself, rather than merely restricting its activity/degree arithmetic.

The result is stronger than the newest B14 addendum.

### Theorem 1 — top-degree granularity

Let `f:{-1,1}^n->{-1,1}` have Fourier degree `d>=1`. If `S` has `|S|=d` and `hat f(S) != 0`, then
\[
\boxed{
\widehat f(S)\in 2^{1-d}\mathbb Z,
\qquad
|\widehat f(S)|\ge 2^{1-d}.
}
\tag{1.1}
\]

#### Proof

For a physical coordinate let
\[
D_i f(x)=\frac{f(x)-f(x^{\oplus i})}{2}.
\]
On Walsh characters, `D_i chi_T = chi_T` if `i in T` and zero otherwise. Hence for `S={i_1,...,i_d}`,
\[
D_Sf:=D_{i_1}\cdots D_{i_d}f
=\sum_{T\supseteq S}\widehat f(T)\chi_T.
\]
Since `d` is the Fourier degree and `|S|=d`, the only possible `T` is `S`, so
\[
D_Sf(x)=\widehat f(S)\chi_S(x).
\tag{1.2}
\]

On the other hand, expanding the iterated difference gives
\[
D_Sf(x)
=2^{-d}\sum_{A\subseteq S}(-1)^{|A|}f(x^{\oplus A}).
\tag{1.3}
\]
The numerator is a sum of `2^d` numbers in `{+1,-1}`. For `d>=1` there are an even number of summands, so the numerator is an even integer. Thus every value of `D_Sf` lies in `2^{1-d} Z`. Equation (1.2) and `chi_S(x) in {+-1}` imply (1.1). `QED`

This quantization depends on the **Fourier degree `d`**, not on the ambient dimension `n`; that is the useful point.

### Theorem 2 — any exact hard-core endpoint must have activity above one quarter

Let `f` be nonconstant Boolean and suppose its nonzero squared Fourier law has the exact form (0.1), with `0<theta<1` and downward-closed support `mathcal F`. Let
\[
d:=\max\{|S|:S\in\mathcal F\}\ge1.
\]
Then
\[
\boxed{
\sqrt\theta\ge 2^{-1+1/d}>\frac12,
\qquad
\theta>\frac14.
}
\tag{2.1}
\]

#### Proof

Choose `S in mathcal F` of size `d`. The endpoint law gives
\[
|\widehat f(S)|
=|\widehat f(\varnothing)|\,\theta^{d/2}
\le \theta^{d/2},
\tag{2.2}
\]
because `|hat f(emptyset)|<=1`. By Theorem 1,
\[
2^{1-d}\le |\widehat f(S)|.
\]
Combining with (2.2),
\[
2^{1-d}\le \theta^{d/2},
\]
so
\[
\sqrt\theta\ge (2^{1-d})^{1/d}=2^{-1+1/d}>1/2.
\]
`QED`

Equivalently, along any full support chain from `emptyset` to a top set, the geometric mean of adjacent Fourier-amplitude ratios is strictly greater than `1/2`. An exact endpoint with every ratio at most `1/2` therefore cannot be Boolean.

## 2. Main integration: the B14 exact endpoint is impossible

B14's signed-link theorem (0.2) says exact Booleanity at the scalar endpoint forces
\[
\sqrt\theta=1/m
\]
for an integer `m>=2`. Therefore
\[
\sqrt\theta\le1/2,
\]
while Theorem 2 forces `sqrt(theta)>1/2`. Contradiction.

### Corollary 2.1 — no nonconstant simultaneous exact endpoint

Under the exact all-coordinate scalar-frontier endpoint hypotheses recovered by B14, **there is no nonconstant Boolean function at all**.

In particular, the newest B14 global candidate
\[
m=3,\quad \theta=1/9,\quad \tau=1/10,\quad d\in\{15,20,25,\ldots\}
\]
is eliminated immediately: a top coefficient would satisfy
\[
|\widehat f(S)|=|\widehat f(\varnothing)|3^{-d}\le3^{-d},
\]
whereas Booleanity forces
\[
|\widehat f(S)|\ge2^{1-d}.
\]
Since `3^{-d}<2^{1-d}` for every `d>=1`, no surviving degree exists.

This proof uses neither the global entropy formula nor the degree-5/10 arithmetic in the addendum. It attacks the endpoint at a different place: **highest-order physical differences.**

## 3. A version that does not use the signed-link arithmetic

The same top-degree lemma already kills all exact scalar endpoints in the ratio range relevant to the current lower bound.

At a scalar endpoint,
\[
\theta=\frac{\tau}{1-\tau}.
\]
Thus `theta<=1/4` exactly when `tau<=1/5`. The B14 scalar analysis proves `kappa` is strictly decreasing on `(0,1/2]`, so putting
\[
r_2:=\kappa(1/5)=6.2646625064904056\ldots,
\]
we obtain:

### Corollary 3.1

For every exact simultaneous scalar endpoint with
\[
r\ge r_2=6.2646625064904056\ldots,
\]
Theorem 2 gives a contradiction **without using** the later rational-root/signed-link theorem.

For calibration, at the current public lower-bound value
\[
r_*=6.521845710923046575
\]
the scalar equation `kappa(tau)=r_*` gives
\[
\tau=0.1740316570325050\ldots,
\qquad
\theta=0.2107001539638352\ldots,
\qquad
\sqrt\theta=0.4590208644101433\ldots<1/2.
\tag{3.1}
\]
So an exact critical endpoint at any currently interesting hard ratio lies on the forbidden side of the parity barrier.

## 4. PROVED consequence for a restriction-critical descendant: strict existential scalar payment

Let `g` be a restriction descendant maximizing
\[
r(g)=H(g)/I(g)>4.
\]
Write `alpha_i=Inf_i(g)`. The recovered restriction-criticality theorem gives for every relevant coordinate
\[
\Delta_iH(g)\ge r(g)\alpha_i,
\]
and B14's sharp scalar theorem gives
\[
B_i(g)\ge b(r(g))\alpha_i.
\tag{4.1}
\]

The scalar supporting-line proof actually yields, with `lambda(r)>0`,
\[
\frac{B_i}{\alpha_i}
\ge b(r)+\lambda(r)
\left(\frac{\Delta_iH}{\alpha_i}-r\right).
\tag{4.2}
\]
If equality held in (4.1), then (4.2) and `Delta_iH/alpha_i>=r` would force
\[
\Delta_iH=r\alpha_i,
\]
and the strict equality characterization would force every positive fibre posterior for that coordinate to equal `tau(r)`. If equality in (4.1) held for **every** relevant coordinate, B14's hard-core endpoint reduction would apply, contradicting Corollary 2.1.

Hence:

### Corollary 4.1 — exact existential rebate

Every nonconstant restriction-critical descendant with `r>4` has at least one relevant coordinate `i` satisfying
\[
\boxed{
B_i(g)>b(r(g))\,\alpha_i(g).
}
\tag{4.3}
\]

This is a genuine universal existential strictness statement. It is **not yet a dimension-free quantitative rebate**: the amount by which (4.3) is strict may a priori tend to zero along a sequence of functions of increasing degree.

## 5. Refutation attempts and boundary checks

I attacked the proof at the points where the endpoint could conceivably evade the parity argument.

1. **Ambient dimension larger than Fourier degree.** This does not weaken Theorem 1. Taking the `d`-fold derivative in a top set kills every Fourier term not containing `S`; Fourier degree `d` guarantees no strict superset survives. The resulting derivative is exactly one character times one coefficient.
2. **Degree one.** The quantization says a nonzero top coefficient has magnitude at least one. An endpoint with `sqrt(theta)<=1/2` predicts magnitude at most one half. The contradiction is already present in the smallest nonconstant degree.
3. **The boundary `m=2`.** This is the weakest endpoint contradiction. The endpoint upper bound is `2^{-d}`, while Boolean top-degree granularity is `2^{1-d}`: a factor-of-two gap for every `d`. Every `m>2` is even farther away.
4. **Could `hat f(emptyset)=0` rescue the endpoint?** No. In the hard-core law every spectral mass is `p_emptyset theta^{|S|}` on the support; `p_emptyset=0` would make the whole spectrum zero, contradicting Parseval normalization.
5. **Could ordinary dyadic Fourier integrality be too weak?** Yes, ordinary `2^n hat f(S) in Z` alone is much weaker in large ambient dimension. That is why the proof uses the *top-degree iterated derivative*, which upgrades the denominator to `2^{d-1}` independent of `n`.

The accompanying numerical script is only a self-check/calibration, not a Boolean-function sweep. It verifies the current-record scalar calibration and the exact factor-two endpoint/top-degree gap for representative degrees. Its output ends with `exact_endpoint_contradiction_check=PASS`.

## 6. Dead route identified: exact nonattainment is still not a uniform FEI closure

The tempting inference

> “the endpoint is impossible, therefore the scalar inequality has a fixed dimension-free positive slack”

is **NOT PROVED** and should not be used.

The top-degree obstruction forces at least one adjacent amplitude ratio on a top-support chain to reach
\[
2^{-1+1/d}>1/2,
\]
whereas the current hard scalar target wants `sqrt(theta)=0.4590...`. This is a fixed amplitude separation in the offending fibre. But the Fourier mass of a particular top fibre can be exponentially small in `d`, so its contribution to the size-biased scalar moment may vanish. Exact nonattainment therefore does not by itself provide the uniform weighted payment needed for FEI.

This kills the **naive stability shortcut**, not the endpoint theorem.

## 7. Next attack: weighted top-degree stability

The next missing implication is now sharper than “classify exact endpoints.” Exact endpoints are gone.

For a critical core at ratio `r` let `tau=tau(r)` and let
\[
q_i(T)=\frac{p_{T\cup\{i\}}}{p_T+p_{T\cup\{i\}}}.
\]
At the present lower-bound calibration, `tau=0.174031657...`, while an amplitude ratio `>=1/2` corresponds to
\[
q\ge1/5=0.2.
\]
Thus top-degree parity forces a fixed posterior separation of at least
\[
0.2-0.1740316570325050\ldots
=0.0259683429674950\ldots
\]
somewhere on every endpoint-like top chain.

The needed universal theorem is now a **weighted stability/propagation lemma**: prove that the mandatory `q>=1/5` defect cannot hide on negligible spectral mass simultaneously across all top chains. One concrete target is a dichotomy of the form

\[
\sum_i\sum_{T:\,q_i(T)\ge1/5} p_{T\cup\{i\}}
\ge c\,I(f)
\tag{7.1}
\]
for a universal `c>0` in a restriction-critical hard core, **or else** the collection of low-mass exceptional fibres forces a block/additive-collision structure that can be charged by the existing B18 Sidon/block selector mechanism or B16 signed transport bank.

If (7.1), or an appropriate block replacement, can be proved, strict convexity of B14's scalar supporting curve converts the fixed posterior separation into a dimension-free scalar payment. That is the next route; another exact-endpoint classification is no longer needed.

## 8. Claim ledger

**PROVED in this run**

- Top Fourier degree quantization: every nonzero degree-`d` coefficient of a Boolean function is an integer multiple of `2^{1-d}`.
- Any exact hard-core law `p_S=p_empty theta^{|S|}` on a down-set must satisfy `sqrt(theta)>=2^{-1+1/d}>1/2`.
- Therefore every exact simultaneous scalar endpoint with `r>=kappa(1/5)=6.26466250649...` is impossible without using signed-link arithmetic.
- Combining with B14's proved exact-endpoint arithmetic `sqrt(theta)=1/m`, `m>=2`, eliminates **all** nonconstant simultaneous exact scalar-frontier endpoints for `r>4` under those inherited hypotheses.
- Consequently every nonconstant restriction-critical descendant has at least one coordinate with strict scalar payment `B_i>b(r) alpha_i`.

**CONDITIONAL / dependency-sensitive**

- The endpoint-elimination corollary uses B14's previously proved scalar endpoint reduction; the all-`r>4` version additionally uses B14's signed-link reciprocal-square theorem. These dependencies have not been independently re-audited in this run because the owner forbids FEI audit-only work.
- The public `6.521845710923046575` record is externally listed with an asterisk/certificate status; it was not independently replayed here and is not needed for the exact theorem.

**REFUTED / dead closure shortcut**

- Exact endpoint nonattainment alone does not imply a known dimension-free scalar slack; an obligatory defective top fibre may have very small spectral weight.

**OPEN**

- Weighted top-degree stability / propagation sufficient to turn exact nonattainment into a universal quantitative rebate.
- The full uniform-cube Fourier entropy-influence conjecture.

**Brain assistance:** `WITHOUT_VERIFIED_BRAIN`.
