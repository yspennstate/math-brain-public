Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no model selector or reasoning-effort selector; I do not claim otherwise.

NO MOVEMENT — Problem: Takahiro Hasebe, Yuki Ueda and Jiun-Chau Wang (2020 preprint; journal version 2022), *Log-unimodality for free positive multiplicative Brownian motion*, arXiv:2009.13848, Problem 4.11; intake I0080. Frozen metric remains **`+infinity -> +infinity`**. This run replaces the previous three-branch all-time proof by a single explicit global witness formula, with a much smaller exact certificate and no interval subdivision.

Run ID: `2026-09-16_15-06-33_UTC__R18__i0080-single-global-witness`.

Operational status: **PROVED CANDIDATE / FLEET CLOSURE PENDING**. The mathematical source statement has a complete proof below, but the protocol still requires P26 and one distinct OTHER-track full-proof audit before the track can be called closed. The earlier R17 audit covers only the old small-time finite core, not this all-time theorem.

# 1. Repository continuity and current source status

I resumed from current `master`, not from chat state. The required repository reads for this run included:

- root `README.md`;
- `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- the I0080 intake/search records;
- newest own report `runs/R18/2026-09-16_14-28-50_UTC__R18__i0080-alltime.md`;
- newest directed-auditor R17 package visible on master, `runs/R17/20260916_1425Z_blockmgf_9f2c.md`;
- R19's current I0084 package `runs/R19/2026-09-16_13-40-24_UTC__i0084-halfstable-lefttail.md`;
- the same-source neighboring P20 report `proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_17-11-23__run-report.md`.

The old Salem assignment remains preserved under `proofnet24/R18-salem-bernoulli-convolutions/`; no file in that retired track was touched.

The newest own report had already saturated the metric:

\[
T_{\mathrm{cert}}=+\infty.
\]

It did so with three overlapping branches C003--C005 and concluded C006. This run does **not** count a new metric movement. Its purpose is to replace that relatively elaborate proof with one formula that works for every `t>0`, independently of the interval-arithmetic branch C004 and independently of the old tiny-time theorem C003.

Current-source check, dated 2026-09-16:

- arXiv `2009.13848` lists Takahiro Hasebe, Yuki Ueda and Jiun-Chau Wang, submitted 29 September 2020;
- the journal version is *Colloquium Mathematicum* 169 (2022), 209--226, DOI `10.4064/cm8413-6-2021`, publisher page online date 22 February 2022;
- source Problem 4.11 asks whether `sigma_t` fails `boxtimes`-strong log-unimodality for every `t>0`;
- exact-phrase searches on `Problem 4.11`, `boxtimes-strongly log-unimodal`, the title/arXiv identifier and author names found no later claimed resolution;
- I checked the accessible citation graph and later free-positive-multiplicative-Brownian papers, including Auer--Voit (2025) and Auer (2026); neither accessible abstract/search record claims a resolution of Problem 4.11.

This is a bounded public-literature pass, not a substitute for the protocol's independent closure audit. The source problem was therefore still treated as open prior to the present candidate proof.

The already-posted additive Problem 3.3, the settled multiplicative Problem 4.7, and P20's distinct Problem 4.3 are excluded.

# 2. Source criterion and normalization

For `b in (0,pi)`, retain the source measure `lambda_b`; after logarithm its density is

\[
h_b(x)=\frac{c_b}{2(\cosh x-\cos b)},
\qquad
c_b=\frac{\sin b}{\pi-b}.
\tag{2.1}
\]

Put

\[
A_b=\frac{\pi}{\pi-b},
\qquad
K_b(v)=\frac b{A_b}h_b(bv)
=\frac{b\sin b}{2\pi(\cosh(bv)-\cos b)}.
\tag{2.2}
\]

For parameters `b>0`, `ell>0`, `p in [0,1]`, define the probability measure `nu_{b,p,ell}` by

\[
\boxed{
\log_*\nu_{b,p,\ell}
=p\,\delta_0+
\frac{1-p}{\ell b}\mathbf 1_{[-\ell b,0]}(y)\,dy.
}
\tag{2.3}
\]

It is log-unimodal with mode `1`: on the logarithmic line the absolutely continuous part is constant on an interval ending at the mode, zero elsewhere, and the only atom is at the mode.

The inverse has its uniform log-density on `[0,ell b]`. Hence the logarithmic density of the classical multiplicative convolution `lambda_b circledast nu^{-1}` is

\[
q_{b,p,\ell}(x)
=p h_b(x)+\frac{1-p}{\ell b}\int_0^{\ell b}h_b(x-y)\,dy.
\tag{2.4}
\]

Normalize at the `b` scale:

\[
S_{b,p,\ell}(y)
:=\frac b{A_b}q_{b,p,\ell}(by)
=pK_b(y)+\frac{1-p}{\ell}\int_{y-\ell}^{y}K_b(v)\,dv.
\tag{2.5}
\]

Source Lemma 4.1 says that, for fixed `t`, log-unimodality of `sigma_t boxtimes nu` forces the source level equation to have at most two positive roots for every `a in (0,1/t)`. In the notation above, if `S(y)=D` has four distinct roots and we choose

\[
\boxed{
t=\frac{b^2}{\pi D},\qquad a=\frac Db,}
\tag{2.6}
\]

then

\[
a\pi t=b,
\qquad a<1/t\quad\text{because }b<\pi,
\tag{2.7}
\]

and the normalized level matches the source exactly:

\[
\frac{(A_bD/b)}{c_b}
=\frac{\pi D}{b\sin b}
=\frac{a\pi}{\sin(a\pi t)}.
\tag{2.8}
\]

Thus four roots of `S(y)=D` give a direct witness that `sigma_t boxtimes nu` is not log-unimodal.

# 3. R18-I0080-C007a — the normalized kernel decreases with b

**STATUS: PROVED.**

For every fixed real `v`,

\[
\boxed{0<b_1<b_2<\pi\implies K_{b_1}(v)\ge K_{b_2}(v).}
\tag{3.1}
\]

Moreover

\[
\boxed{K_b(v)\le K_0(v):=\frac1{\pi(1+v^2)}.}
\tag{3.2}
\]

## Proof

Write

\[
K_b(v)=\frac1{2\pi G_v(b)},
\qquad
G_v(b)=\frac{\cosh(bv)-\cos b}{b\sin b}.
\tag{3.3}
\]

Decompose

\[
G_v(b)
=\frac{\cosh(bv)-1}{b^2}\frac b{\sin b}
+\frac{\tan(b/2)}b.
\tag{3.4}
\]

Each factor in the first product is nonnegative and nondecreasing on `(0,pi)`.
For

\[
\phi(x)=\frac{\cosh x-1}{x^2},
\]

we have

\[
\phi'(x)=\frac{x\sinh x-2(\cosh x-1)}{x^3}.
\]
If `g(x)=x sinh x-2(cosh x-1)`, then

\[
g'(x)=x\cosh x-\sinh x,
\qquad
g''(x)=x\sinh x\ge0,
\]

with `g(0)=g'(0)=0`, so `phi` is nondecreasing. Also

\[
\left(\frac b{\sin b}\right)'
=\frac{\sin b-b\cos b}{\sin^2b}>0,
\]

because the numerator has derivative `b sin b>0` and vanishes at zero.
Finally `tan x/x` is increasing on `(0,pi/2)` since the numerator of its derivative,

\[
x\sec^2x-\tan x,
\]

has derivative `2x sec^2 x tan x>0`. Therefore `tan(b/2)/b` is increasing too.
Hence `G_v` is nondecreasing and `K_b` is nonincreasing.

The limit `b downarrow0` in (2.2) is

\[
K_0(v)=\frac1{\pi(1+v^2)},
\]

which proves (3.2). QED.

# 4. Exact primitive

Direct differentiation gives

\[
\boxed{
\int_u^v K_b(w)\,dw
=\frac{\Phi_b(v)-\Phi_b(u)}\pi,
}
\tag{4.1}
\]

where

\[
\Phi_b(v)
=\arctan\!\left(
\cot\frac b2\,\tanh\frac{bv}{2}
\right).
\tag{4.2}
\]

This identity is used only at the fixed value `b=1/10` below.

# 5. R18-I0080-C007b — three uniform crossings for every b<=1/10 and ell>=100

**STATUS: PROVED, with exact finite arithmetic certificate.**

Fix

\[
\boxed{
B=\frac1{10},\qquad
\kappa=\frac85,\qquad
d=\frac{19}{20}.}
\tag{5.1}
\]

For arbitrary

\[
0<b\le B,
\qquad \ell\ge100,
\tag{5.2}
\]

set

\[
p=\frac\kappa\ell
\tag{5.3}
\]

and multiply (2.5) by `ell`:

\[
R_{b,\ell}(y)
:=\ell S_{b,p,\ell}(y)
=\kappa K_b(y)
+\left(1-\frac\kappa\ell\right)
\int_{y-\ell}^{y}K_b(v)\,dv.
\tag{5.4}
\]

Since `ell>=100`,

\[
1-\frac\kappa\ell\ge\frac{123}{125}.
\tag{5.5}
\]

We prove

\[
\boxed{
R_{b,\ell}(0)>d,
\qquad
R_{b,\ell}(3)<d,
\qquad
R_{b,\ell}(\ell/2)>d.}
\tag{5.6}
\]

## 5.1 High point at y=0

C007a and interval inclusion give

\[
R_{b,\ell}(0)
\ge\frac85K_B(0)
+\frac{123}{125}\int_{-100}^{0}K_B(v)\,dv.
\tag{5.7}
\]

Elementary Taylor inequalities yield

\[
K_B(0)
=\frac{B\sin B}{2\pi(1-\cos B)}
>\frac{599}{600\pi}
>\frac{4193}{13200},
\tag{5.8}
\]

where the last inequality uses `pi<22/7`.

For the integral, (4.1) gives

\[
\int_{-100}^{0}K_B
=\frac1\pi
\arctan\!\left(
\cot\frac1{20}\,\tanh5
\right).
\tag{5.9}
\]

Using

\[
\cot\frac1{20}>\frac{799}{40},
\qquad
\tanh5>\frac9{10},
\tag{5.10}
\]

its arctangent argument exceeds `16`. The first bound follows from
`cos x>1-x^2/2` and `sin x<x`; the second follows from `e^10>61>19`.
Therefore

\[
\arctan(16)
=\frac\pi2-\arctan(1/16)
>\frac\pi2-\frac1{16}
>\frac{12\pi}{25},
\tag{5.11}
\]

using `pi>25/8`. Consequently

\[
\int_{-100}^{0}K_B>\frac{12}{25}.
\tag{5.12}
\]

The exact rational lower bound is then

\[
R_{b,\ell}(0)
>
\frac85\frac{4193}{13200}
+\frac{123}{125}\frac{12}{25}
=\frac{202241}{206250}
>\frac{19}{20}.
\tag{5.13}
\]

## 5.2 Low point at y=3

By C007a, `K_b<=K_0`, while the averaging coefficient is at most one. Hence

\[
R_{b,\ell}(3)
\le
\frac85K_0(3)
+\int_{-\infty}^{3}K_0(v)\,dv.
\tag{5.14}
\]

Since `K_0(v)=1/[pi(1+v^2)]`,

\[
R_{b,\ell}(3)
\le
1-\frac{\arctan(1/3)}\pi
+\frac4{25\pi}.
\tag{5.15}
\]

The alternating arctangent series gives

\[
\arctan(1/3)
>\frac13-\frac{(1/3)^3}{3}
=\frac{26}{81}.
\tag{5.16}
\]

Also

\[
\frac\pi{20}+\frac4{25}
<\frac{11}{70}+\frac4{25}
=\frac{111}{350},
\tag{5.17}
\]

and the exact certificate checks

\[
\frac{26}{81}-\frac{111}{350}
=\frac{109}{28350}>0.
\tag{5.18}
\]

Thus

\[
\arctan(1/3)>\frac\pi{20}+\frac4{25},
\]

which is exactly (5.15) `<19/20`.

## 5.3 High point at y=ell/2

Drop the nonnegative atom term. Since `ell>=100`, C007a gives

\[
R_{b,\ell}(\ell/2)
\ge
\frac{123}{125}
\int_{-50}^{50}K_B(v)\,dv.
\tag{5.19}
\]

By (4.1),

\[
\int_{-50}^{50}K_B
=\frac2\pi
\arctan\!\left(
\cot\frac1{20}\,\tanh\frac52
\right).
\tag{5.20}
\]

We already have `cot(1/20)>799/40`. Also

\[
\tanh(5/2)>\frac{29}{30}
\tag{5.21}
\]

because this is equivalent to `e^5>59`, while the first five positive exponential-series terms give

\[
e^5>1+5+\frac{25}{2}+\frac{125}{6}+\frac{625}{24}
=\frac{523}{8}>59.
\tag{5.22}
\]

Thus the arctangent argument exceeds

\[
\frac{23171}{1200}.
\tag{5.23}
\]

Using `atan x>pi/2-1/x`,

\[
\int_{-50}^{50}K_B
>
1-\frac{2400}{23171\pi}
>\frac{967}{1000}.
\tag{5.24}
\]

The final strict inequality follows from

\[
\pi>\frac{333}{106}>
\frac{800000}{254881},
\tag{5.25}
\]

with the rational comparison certified exactly.
Hence

\[
R_{b,\ell}(\ell/2)
>
\frac{123}{125}\frac{967}{1000}
=\frac{118941}{125000}
>\frac{19}{20}.
\tag{5.26}
\]

This completes (5.6).

# 6. R18-I0080-C007 — one explicit witness formula for every t>0

**STATUS: PROVED CANDIDATE.**

For arbitrary `t>0`, define

\[
\boxed{
\ell(t)=\max\{100,95\pi t\},
\qquad
d=\frac{19}{20},
\qquad
b(t)=\sqrt{\frac{\pi d t}{\ell(t)}}.
}
\tag{6.1}
\]

Then set

\[
\boxed{
p(t)=\frac{8}{5\ell(t)},
\qquad
D(t)=\frac{19}{20\ell(t)}.}
\tag{6.2}
\]

Finally define the witness directly by

\[
\boxed{
\log_*\nu_t
=
p(t)\,\delta_0
+
\frac{1-p(t)}{\ell(t)b(t)}
\mathbf 1_{[-\ell(t)b(t),0]}(y)\,dy.}
\tag{6.3}
\]

This is a probability law and is log-unimodal.

We first check the uniform parameter range. Since

\[
\frac d{(1/10)^2}=95,
\tag{6.4}
\]

if `ell(t)=95 pi t` then `b(t)=1/10`. If `ell(t)=100`, the defining inequality `95 pi t<=100` gives

\[
b(t)^2=\frac{\pi d t}{100}\le\frac1{100}.
\tag{6.5}
\]

Thus for every `t>0`,

\[
0<b(t)\le\frac1{10},
\qquad
\ell(t)\ge100,
\qquad
0<p(t)\le\frac2{125}<1.
\tag{6.6}
\]

C007b therefore applies. Since `0<3<ell(t)/2`, it gives

\[
S_t(0)>D(t),
\qquad
S_t(3)<D(t),
\qquad
S_t(\ell(t)/2)>D(t).
\tag{6.7}
\]

For fixed `t`, `S_t(y)->0` at both tails. Since `D(t)>0`, continuity yields four distinct roots of

\[
S_t(y)=D(t):
\]

one left of `0`, one in `(0,3)`, one in `(3,ell/2)`, and one right of `ell/2`.

Now observe that the time identity is automatic:

\[
\frac{b(t)^2}{\pi D(t)}
=\frac{\pi d t/\ell(t)}{\pi d/\ell(t)}
=t.
\tag{6.8}
\]

Set

\[
a(t)=\frac{D(t)}{b(t)}.
\tag{6.9}
\]

Then

\[
a(t)\pi t=b(t)<\pi,
\]

so `a(t) in (0,1/t)`, and the source level match (2.8) holds. The four roots therefore violate the necessary source criterion for log-unimodality of

\[
\sigma_t\boxtimes\nu_t.
\]

Since `nu_t` is log-unimodal, we conclude

\[
\boxed{
\sigma_t\text{ is not }\boxtimes\text{-strongly log-unimodal for every }t>0.
}
\tag{6.10}
\]

This answers source Problem 4.11 **YES**, subject to the fleet's required independent audits.

The fixed metric remains

\[
\boxed{T=+\infty.}
\tag{6.11}
\]

The improvement over C006 is structural rather than metric: C007 is one closed-form parameterization for all times, uses only three coarse rational inequalities, and has no interval subdivision or intermediate-value branch.

# 7. Exact certificate

Run-specific exact checker:

`artifacts/R18/2026-09-16_15-06-33_UTC__R18__i0080-single-global-witness__checker.py`

create commit:

`911e611727f962864cdafd5f348110b654189b60`.

Archived executed output:

`artifacts/R18/2026-09-16_15-06-33_UTC__R18__i0080-single-global-witness__checker-output.txt`

create commit:

`5c98e24f556af403c02cdb796c436fd11e11ad8d`.

Executed-output SHA-256:

`31b9eaaf17891f037b2fa13ce1f39a4b7b6d786fc292a9be4562c862775b7f72`.

Both GitHub files were read back at their returned commit SHAs before this report was committed.

The checker uses exact `Fraction` arithmetic only. It certifies the Machin-derived coarse bounds

\[
\frac{333}{106}<\pi<\frac{22}{7},
\]

the low-point margin `109/28350`, the high-zero margin `12607/412500`, the high-midpoint margin `191/125000`, the exponential-series cores for the two `tanh` bounds, and the exact global parameter algebra `d/B^2=95`.

# 8. Self-adversarial checks and failed routes

1. **No numerical time sampling.** C007 is quantified over every real `t>0`.
2. **No interval image argument.** The previous Branch B and its 3325 interval boxes are no longer needed.
3. **No dependency on the old tiny-time theorem.** C007 directly covers arbitrarily small `t` by letting `b(t) downarrow0` while keeping `ell=100`.
4. **No hidden discreteness.** `ell(t)` is allowed to be any real number at least 100; it is merely the width parameter of a uniform density.
5. **The atom mass is always admissible.** `p(t)<=2/125<1`.
6. **The source parameter is admissible.** `a pi t=b<=1/10<pi`, hence `a<1/t`.
7. **All four crossings are distinct.** Their bracketing intervals are disjoint because `0<3<ell/2`, and both tails lie below the positive crossing level.
8. **The normalized kernel is not a probability density for finite b.** The proof never assumes it is; only the exact pointwise and interval formulas are used.
9. **Problem-number hygiene.** No statement from additive Problem 3.3, multiplicative Problem 4.7, or P20 Problem 4.3 is substituted for Problem 4.11.

The route which became obsolete is the three-branch patching from C006. It remains valid evidence but is no longer the cleanest proof. The key simplification is to co-vary the width and kernel scale:

\[
\ell(t)=\max\{100,95\pi t\},
\qquad
b(t)^2=\pi d t/\ell(t).
\]

This keeps `b<=1/10` at every time while making the source time identity exact.

# 9. Independent-audit state

Repository search at the start of this run found **no P26 full-proof audit of C006/C007**.

The newest R17 report contains

`R17-AUDIT-R18-I0080-FINITECORE-001=PASS`,

but R17 explicitly labels it a finite-core audit of the old small-time package, **not** the required full end-to-end closure audit. It predates C006 and C007.

Accordingly the closure audit state is still:

- `P26: PENDING`;
- `R17-or-qualified-distinct-track full C007 audit: PENDING`.

C007 is deliberately written to make that full audit substantially smaller: the auditor only needs the source Lemma 4.1 normalization, kernel monotonicity C007a, the three exact inequalities C007b, and the explicit substitution (6.1)--(6.9).

Directed R18 -> R19 duty was already completed in the preceding R18 run:

`R18-AUDIT-R19-I0084-C001=PASS`.

No newer R19 package was found in the current `runs/R19` listing, so that audit was not redundantly repeated.

**Explicit audit request:** P26 and the next eligible distinct R-series auditor should audit claim `R18-I0080-C007` from this immutable report, not merely the older finite-core package.

# 10. Prior-art state

A dedicated bounded 2026-09-16 search was repeated after obtaining C007. Queries included the exact title and arXiv identifier, `Problem 4.11`, `boxtimes-strongly log-unimodal`, and combinations of the three authors with `strong log-unimodality` and later years.

The accessible citation graph for the 2022 article lists only a small number of related/citing works. I checked the accessible records for the 2019/2021 unit-circle paper of Hasebe--Ueda, Auer--Voit (2025) on explicit formulas for free multiplicative Brownian motion, and Auer (2026) on free positive multiplicative Brownian motion and semicircle/uniform free additive convolution. No accessible record claims the all-time positive-line strong-log-unimodality result of Problem 4.11.

Therefore no prior resolution was found in this bounded pass. Because repository closure requires independent prior-art verification as well as mathematical audits, I leave the operational label `PROVED CANDIDATE / CLOSURE PENDING`.

# 11. Cumulative ledger

| Claim | Status | Scope |
|---|---|---|
| R18-I0080-C001--C003 | PROVED | previous explicit small-time interval |
| R18-I0080-C004--C006 | PROVED CANDIDATE | previous three-branch all-time solution |
| R18-I0080-C007a | **PROVED NEW** | pointwise monotonicity `K_b(v)` in `b` |
| R18-I0080-C007b | **PROVED NEW** | uniform high/low/high inequalities for all `b<=1/10`, `ell>=100` |
| R18-I0080-C007 | **PROVED NEW CANDIDATE** | one explicit global witness formula covers every `t>0` |
| fixed metric | **NO MOVEMENT** | `+infinity -> +infinity`, already saturated last run |
| P26 full audit | PENDING | required for fleet closure |
| distinct OTHER full audit | PENDING | R17 old finite-core PASS is insufficient |
| R18 audit of R19-I0084-C001 | PASS (prior run) | classical positive half-stable claim only |

# 12. Remaining obligation

The mathematical target itself no longer has an uncovered time range. The next obligation is **not another lemma**. It is closure validation:

\[
\boxed{
\text{independently audit C007 end to end against source Lemma 4.1 and its normalizations.}
\]

If P26 and one distinct OTHER-track audit both pass, the next R18 run should package the self-contained paper folder required by the protocol and then retire/rotate the closable slot. Until then, no schedule or assignment is changed.

# 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: R18
  source: "Takahiro Hasebe, Yuki Ueda, Jiun-Chau Wang, Log-unimodality for free positive multiplicative Brownian motion, arXiv:2009.13848 (2020), Colloq. Math. 169 (2022), Problem 4.11; intake I0080"
  target: "Determine whether sigma_t fails boxtimes-strong log-unimodality for every t>0"
  metric: "supremum T such that one rigorously verified witness scheme covers every 0<t<=T"
  before: "+infinity (R18-I0080-C006 in previous run)"
  after: "+infinity"
  movement: "NO MOVEMENT; metric already saturated. Proof architecture strengthened to one closed-form all-time witness."
  status: "PROVED CANDIDATE mathematically; fleet closure pending P26 + distinct OTHER full-proof audits"
  unchanged_count: 1
  exact_evidence:
    - "runs/R18/2026-09-16_14-28-50_UTC__R18__i0080-alltime.md (prior all-time proof)"
    - "artifacts/R18/2026-09-16_15-06-33_UTC__R18__i0080-single-global-witness__checker.py @ 911e611727f962864cdafd5f348110b654189b60"
    - "artifacts/R18/2026-09-16_15-06-33_UTC__R18__i0080-single-global-witness__checker-output.txt @ 5c98e24f556af403c02cdb796c436fd11e11ad8d"
    - "output_sha256=31b9eaaf17891f037b2fa13ce1f39a4b7b6d786fc292a9be4562c862775b7f72"
  claims:
    - "R18-I0080-C007a PROVED: K_b(v) decreases in b on (0,pi) for each fixed v"
    - "R18-I0080-C007b PROVED: one high/low/high certificate holds uniformly for b<=1/10 and ell>=100"
    - "R18-I0080-C007 PROVED CANDIDATE: ell(t)=max(100,95*pi*t) and b(t)=sqrt(pi*(19/20)*t/ell(t)) give a single explicit witness family for every t>0"
  audit_ids:
    - "P26:C007_FULL_PENDING"
    - "R17-or-qualified-other:C007_FULL_PENDING"
    - "R17-AUDIT-R18-I0080-FINITECORE-001=PASS_ONLY_OLD_SMALLTIME_CORE"
  directed_audit_performed:
    id: "R18-AUDIT-R19-I0084-C001"
    verdict: "PASS in prior R18 run; no newer R19 package found"
  retired_assignment_handoff: "proofnet24/R18-salem-bernoulli-convolutions preserved; no retired-track file modified"
```
