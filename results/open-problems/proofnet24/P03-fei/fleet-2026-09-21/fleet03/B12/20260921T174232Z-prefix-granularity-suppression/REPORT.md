# B12 FEI creative attempt: hypercontractive suppression of rare unordered spectral prefixes

**Status:** full uniform-cube Fourier entropy-influence (FEI) conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), with the physical derivative structure behind #3.  
**Provenance:** no novelty or publication-priority claim is made. This is a private proof-route artifact.

Before substantive mathematics this run read, in the owner-required order, `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` from fresh `math-open-problems` master. It also consumed the immediately relevant B12 uniform-prefix/shadow handoff and B12 two-local sensitivity-coupling handoff, plus fleet02/B17's weak-overlap face-boundary theorem. It did not re-audit the read-once certificate or repeat a settled FEI sweep.

The current source state includes the corrected external lower bound `C_FEI > 6.521845710923046575`; Hod's `6.4547837...` is no longer a valid universal sharp target. Full FEI still asks only for some absolute dimension-free constant.

## 1. Exact universal statement attempted

Let

\[
\mu(B)=\widehat f(B)^2,\qquad S\sim\mu,
\]

for a Boolean `f:{-1,+1}^n -> {-1,+1}`. For a nonempty set `A` of size `a`, write

\[
\nu_A:=\Pr(A\subseteq S)=\sum_{B\supseteq A}\mu(B)
\]

and recall the unordered uniform-prefix shadow mass

\[
v_A:=\sum_{B\supseteq A}\frac{\mu(B)}{\binom{|B|}{a}}.
\]

Thus `v_A` is the probability that, after sampling `S` and uniformly ordering its elements, the unordered first `a` elements are exactly `A` (with the event requiring `|S|>=a`). The previous B12 handoff proved the exact beta-noise representation

\[
 v_A
 =a\int_0^1 t^{a-1}
 \left\|T_{\sqrt{1-t}}D_Af\right\|_2^2\,dt. \tag{1.1}
\]

The universal target attempted in this run was:

> **PREFIX-SUPPRESSION.** Can Booleanity force `v_A/nu_A` to become small whenever the inclusion event `A subseteq S` is rare, with a logarithmic gain whose power grows with `|A|`?

This run proves such a bound. It is not FEI by itself, but it gives a genuine all-dimensional Boolean constraint directly on the exact sequential-compression process.

## 2. PROVED: derivative granularity at every prefix

With the standard normalized iterated derivative,

\[
D_Af(y)=2^{-a}\sum_{z\in\{-1,+1\}^A}\chi_A(z)f(z,y),
\]

Parseval gives

\[
\|D_Af\|_2^2=\nu_A. \tag{2.1}
\]

Because the numerator in the display for `D_A f` is an even integer, every nonzero value of `D_A f` has magnitude at least

\[
2^{1-a}. \tag{2.2}
\]

Also `|D_A f|<=1`. Hence pointwise

\[
|D_Af|\le 2^{a-1}|D_Af|^2,
\]

and therefore

\[
\boxed{\|D_Af\|_1\le 2^{a-1}\nu_A.} \tag{2.3}
\]

This elementary arithmetic fact is the part that survives after the first derivative ceases to be `{0,+-1}`-valued.

## 3. PROVED: all-prefix hypercontractive suppression

Put `h=D_A f`. In (1.1), set `rho=sqrt(1-t)`. Bonami--Beckner gives

\[
\|T_{\rho}h\|_2\le \|h\|_{1+\rho^2}=\|h\|_{2-t}. \tag{3.1}
\]

For `s=2-t`, interpolate between `L_1` and `L_2`. If

\[
\theta=\frac{t}{2-t},
\]

then `1/s=theta+(1-theta)/2`, so by (2.1)--(2.3)

\[
\begin{aligned}
\|h\|_{2-t}^2
&\le \|h\|_1^{2\theta}\|h\|_2^{2(1-\theta)}\\
&\le (2^{a-1}\nu_A)^{2\theta}\nu_A^{1-\theta}\\
&=\nu_A\bigl(4^{a-1}\nu_A\bigr)^{t/(2-t)}.
\end{aligned} \tag{3.2}
\]

Insert this into (1.1):

\[
\boxed{
\frac{v_A}{\nu_A}
\le
F_a(4^{a-1}\nu_A),
\qquad
F_a(r):=a\int_0^1t^{a-1}r^{t/(2-t)}dt.
} \tag{3.3}
\]

Of course `v_A<=nu_A`, so the right side may always be replaced by `min(1,F_a(...))`.

This is already an explicit universal prefix bound. A cleaner closed form follows. Substitute

\[
u=\frac{t}{2-t},\qquad t=\frac{2u}{1+u},\qquad dt=\frac{2\,du}{(1+u)^2}.
\]

Then

\[
F_a(r)
=a2^a\int_0^1
\frac{u^{a-1}r^u}{(1+u)^{a+1}}\,du. \tag{3.4}
\]

Concavity of `ln(1+u)` on `[0,1]` gives

\[
\ln(1+u)\ge u\ln2.
\]

Define

\[
\Lambda_A
:=\ln\frac1{\nu_A}+(3-a)\ln2. \tag{3.5}
\]

When `Lambda_A>0`, (3.4), the preceding inequality, and extension of the integral to `[0,infinity)` yield

\[
\boxed{
 v_A
 \le
 \nu_A\min\left\{1,
 a!\left(\frac{2}{\Lambda_A}\right)^a
 \right\}.
} \tag{3.6}
\]

So rare `a`-fold spectral inclusion is suppressed in the unordered-prefix process by an `a`th power of a logarithm (up to the unavoidable derivative-granularity shift).

Two particularly transparent cases are

\[
\boxed{
 v_i\le p_i\min\left\{1,
 \frac{2}{\ln(1/p_i)+\ln4}
 \right\},
 \qquad p_i=\operatorname{Inf}_i(f),
} \tag{3.7}
\]

and

\[
\boxed{
 v_{ij}\le q_{ij}\min\left\{1,
 \frac{8}{\ln^2(2/q_{ij})}
 \right\},
 \qquad q_{ij}=\Pr(i,j\in S).
} \tag{3.8}
\]

By the previous B12 two-local theorem, `q_ij` is also exactly the probability that `i` and `j` are simultaneously sensitive at a uniform physical input. Thus (3.8) is an explicit route-1/route-3 bridge: a rare physical two-direction sensitivity event is even rarer as an early unordered spectral prefix, with a squared-log rebate.

For triples,

\[
 v_{ijk}\le \nu_{ijk}\min\left\{1,
 \frac{48}{\ln^3(1/\nu_{ijk})}
 \right\} \tag{3.9}
\]

whenever `0<nu_ijk<1`.

## 4. PROVED: the first branching stage of the exact prefix code costs at most `3.018075 I` bits

Let

\[
r=\Pr(S\ne\varnothing)=1-\widehat f(\varnothing)^2.
\]

Because

\[
\sum_i v_i
=\sum_{S\ne\varnothing}\mu(S)\sum_{i\in S}\frac1{|S|}
=r,
\]

the first coordinate in a uniformly ordered nonempty spectral sample has distribution `v_i/r`. Its exact contribution to the branching term in the B12 prefix-chain identity is

\[
B_0:=rH_2((v_i/r)_i)
=\sum_i v_i\log_2\frac r{v_i}. \tag{4.1}
\]

Since `r<=1`,

\[
B_0\le\sum_i v_i\log_2\frac1{v_i}. \tag{4.2}
\]

For a fixed marginal `p`, let `L=ln(1/p)` and use (3.7):

\[
v\le \min\left\{p,\frac{2p}{L+\ln4}\right\}. \tag{4.3}
\]

A one-variable maximization gives

\[
 v\ln\frac1v
 \le
 \left(2+\frac1{4e}\right)p. \tag{4.4}
\]

For completeness: in the active logarithmic-cap regime, put `c=ln4` and `b=2p/(L+c)`. Once `b<=1/e`, the ratio is

\[
\frac{b\ln(1/b)}p
=
\frac{2[L+\ln((L+c)/2)]}{L+c}.
\]

Its derivative vanishes at `L+c=8e`, where the value is exactly `2+1/(4e)`; the complementary regimes, handled by `v<=p` and the maximum `x ln(1/x)<=1/e`, are smaller.

Therefore

\[
\boxed{
B_0\le C_{\rm root} I(f),
\qquad
C_{\rm root}
=\frac{2+1/(4e)}{\ln2}
=3.018074543133688\ldots .
} \tag{4.5}
\]

This is a dimension-free payment for the **entire first branching stage** of the exact sequential spectral code. It is substantially different from bounding the entropy of the global influence profile: the latter is unbounded per unit influence on one-point defects, while the prefix reach weights `v_i` receive the logarithmic hypercontractive suppression in (3.7).

This is still not FEI. The deeper prefix transitions plus stop/continue terms and the factorial rebate remain to be controlled.

## 5. Stress numbers (not a finite proof of FEI)

The attached checker evaluates only a few deliberate stress families for the new root payment; it is not an exhaustive FEI sweep.

| family | `I` | root branching bits `B0` | `B0/I` |
|---|---:|---:|---:|
| one-point defect, `n=16` | `0.00048828125` | `0.000244136899709702` | `0.499992370605469` |
| majority, `n=15` | `3.14208984375` | `3.90689059560852` | `1.24340511885101` |
| width-2 tribes, 7 tribes (`n=14`) | `1.245849609375` | `1.76152512417472` | `1.41391473811868` |

All are comfortably below the proved `3.018074543...` constant. The largest ratio `v_i` / right side of (3.7) among coordinates of these examples was respectively `0.73646`, `0.46935`, and `0.70662`.

These numbers are diagnostics only. The theorem is the analytic argument above.

## 6. REFUTED: one cannot simply delete the derivative-granularity factor

A tempting stronger version of (3.3) would replace `4^{a-1} nu_A` by `nu_A`, pretending every iterated derivative behaves like a `{0,+-1}` first derivative. This is false already for `a=2`.

Take the two-bit one-defect Boolean function with truth table `(-1,+1,+1,+1)`. Then

\[
\nu_{\{1,2\}}=v_{\{1,2\}}=\frac14,
\]

and `D_{12}f` is the constant `+-1/2`, so the inequality `||D_{12}f||_1<=2||D_{12}f||_2^2` is attained with equality.

If the factor `4` were illegally removed from the hypercontractive integrand, it would predict

\[
\frac{v_{12}}{\nu_{12}}
\le
2\int_0^1 t(1/4)^{t/(2-t)}dt
=0.500839429892228\ldots,
\]

hence `v_12<=0.12520985747...`, contradicting the exact `v_12=1/4`.

So the stronger no-granularity statement is **REFUTED**, and the `4^{a-1}` loss in (3.3) reflects a real higher-derivative obstruction rather than a proof artifact that can simply be erased.

## 7. What this changes in the FEI route

The previous B12 run found a sharp three-local spectral/sensitivity transport but also showed that a one-shot global sensitivity coupling is wrong. The present theorem suggests a more compatible organization:

1. keep the exact uniform-prefix code, which already retains the crucial `E log K!` rebate;
2. use (3.7) to pay the first branching stage universally by `3.018075 I`;
3. at level two use the exact physical identity `q_ij=Pr(i,j both sensitive)` together with the squared-log suppression (3.8), rather than converting a small transport defect into an entropy-continuity term;
4. at deeper levels use (3.6): the arithmetic granularity of `D_A f` degrades with `a`, but genuinely rare inclusion events receive a matching higher power of logarithmic prefix suppression;
5. treat high-`nu_A` prefixes as clusters, where the factorial rebate should be retained instead of paying their labels independently.

This is precisely a weak-overlap / cluster split, but now the weak-overlap side has a **direct sequential-code rarity estimate** and need not rely only on summing physical boundary certificates that can be double-counted.

## 8. Exact remaining gap and next attack

The full FEI conjecture remains **OPEN**. The next target is not another local certificate. It is the following global summation statement for the exact prefix process.

Write the previous B12 identity

\[
H(S)=J+\mathrm{Br}-\mathbb E\log_2(K!),
\]

split `Br=B0+Br_{>=1}`, and retain the previously proved terminal-shadow payment `B_sh<=log_2(e)I`. The present theorem now pays `B0<=3.018075 I`. The unsolved object is therefore the genuinely deeper residual

\[
 (J-B_{sh})+\mathrm{Br}_{\ge1}-\mathbb E\log_2(K!). \tag{8.1}
\]

**Next attack:** partition visited prefixes by whether `Lambda_A` in (3.5) is large (rare-prefix regime) or small (cluster regime). Sum (3.6) directly on the rare side; on the cluster side keep the whole block and charge its common activation once, using the factorial rebate rather than coordinatewise entropy continuity. The technical target is a charging lemma showing that the total rare-prefix code length plus the number of cluster activations is `O(I)` without reusing the same influence mass across depths.

If such a charging lemma is proved, (8.1) becomes dimension-free and FEI follows with an explicit, not necessarily sharp, constant. If the charging lemma fails, its extremizer should identify the next missing Boolean constraint.

## 9. Classification

- **PROVED:** all-prefix derivative granularity `||D_A f||_1 <= 2^{|A|-1} ||D_A f||_2^2`.
- **PROVED:** hypercontractive prefix suppression (3.3).
- **PROVED:** logarithmic closed-form prefix suppression (3.6), including the pair and triple corollaries.
- **PROVED:** the entire root branching cost of the exact prefix code satisfies `B0 <= 3.0180745432 I`.
- **REFUTED:** deleting the higher-derivative granularity factor from (3.3), by the two-bit one-defect function.
- **OPEN:** the global rare-prefix / cluster charging lemma, the deeper residual (8.1), and full uniform-cube FEI.
- **NOT CLAIMED:** novelty or publication priority.

Reproducible stress code is `prefix_suppression_stress.py`; its captured output is `verification.txt` in this directory.
