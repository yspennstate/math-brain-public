Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED (GPT-6 / maximum was requested, but this scheduler exposes no model selector or reasoning-effort selector; I do not claim otherwise).

Problem: Takahiro Hasebe, Yuki Ueda and Jiun-Chau Wang (2020 preprint; 2022 journal), *Log-unimodality for free positive multiplicative Brownian motion*, arXiv:2009.13848, Problem 4.11; intake I0080.

Tracked quantity MOVED: **UNMEASURED -> certified endpoint**
\[
T_*:=\frac{125}{585344\pi}=6.79749\ldots\times 10^{-5},
\]
with one explicit witness scheme proving failure of \(\boxtimes\)-strong log-unimodality for **every** \(0<t\le T_*\). Exact checker certifies \(0.000067<T_*<0.000069\).

Run status: **PARTIAL**. The source Problem 4.11 remains **OPEN** beyond the certified interval; nothing here claims the all-\(t\) classification.

# 1. Repository continuity, exact scope, and retired Salem handoff

I began from current `master` and read the required campaign state: root `README.md`, `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, the exact I0080 intake/search state, the newest relevant P20 report on the distinct Problem 4.3, and current R19 ownership/search state.

The authoritative fleet row now assigns R18 to Hasebe--Ueda--Wang Problem 4.11, not the former Salem Bernoulli-convolution project. Root `RESULTS.md` records the metric baseline as `UNMEASURED -> UNMEASURED` before this run and explicitly says to recover the source small-time range and retire the Salem route.

The old Salem project is preserved, not deleted or overwritten. Its stable handoff remains under

`proofnet24/R18-salem-bernoulli-convolutions/`

with cumulative ledger commit

`2274925de658dde2f5ca7bd5f26f1d6e4e8e2c5c`

and the last substantive exact-trinomial/Baker report commit

`894870d09b49ad44e89bfbda8f110eac0fa4ba85`.

No Salem file was edited in this run. This report is the canonical restart on I0080 under the revised R18 assignment.

A repository-wide search for `I0080`, the exact Problem 4.11 wording, and R18 commits found the intake/ownership records but **no previous dedicated I0080 proof report**. Thus there was no prior quantitative I0080 endpoint to inherit. The source itself, however, already proves a nonquantitative small-time interval; that theorem is recovered below and is treated as prior art rather than rederived as a new result.

The neighboring P20 track is **not** this problem: P20 concerns Hasebe--Ueda--Wang Problem 4.3 (arbitrary multiplicatively symmetric log-unimodal free convolution). Problem 4.7 and additive Problem 3.3 are also excluded. I do not import their closure labels into I0080.

R19 audit state: the revised fleet assigns R19 to Hasebe--Ueda 2018 Conjecture 5.5 / I0084. Current repository searches found only the older pre-reassignment R19 free-group-factor package/commits and no new I0084 package ready for an end-to-end audit. I therefore did **not** audit a stale wrong-target package. `R19_AUDIT=NOT_READY` for this run.

# 2. Primary source and current-status verification

Primary source verified on 2026-09-16:

- Takahiro Hasebe, Yuki Ueda, Jiun-Chau Wang, arXiv:2009.13848, submitted 29 September 2020.
- Journal version: *Colloquium Mathematicum* 169 (2022), 209--226, DOI `10.4064/cm8413-6-2021`, published online 22 February 2022.
- Exact Problem 4.11 in the source:

> Is it true that \(\sigma_t\) is not \(\boxtimes\)-strongly log-unimodal for any \(t>0\)?

The source definition immediately before Theorem 4.9 is: a probability measure \(\mu\) on \(\mathbb R_+\) is \(\boxtimes\)-strongly log-unimodal if \(\mu\boxtimes\nu\) is log-unimodal for every log-unimodal distribution \(\nu\).

The exact already-proved small-time statement is source Theorem 4.9:

> There exists \(t_0>0\) such that \(\sigma_t\) is not \(\boxtimes\)-strongly log-unimodal for any \(t\in(0,t_0]\).

The source proof first obtains one time \(t_1\) from failure of classical strong log-unimodality of \(\lambda_1\), then uses the semigroup relation and a closed-set/maximal-good-time argument to infer existence of a whole interval. It does **not** give a numerical value of \(t_0\). For the fleet's fixed quantitative metric this is therefore a genuine `UNMEASURED` baseline, not zero.

Dated bounded novelty/status search, 2026-09-16: I searched the exact Problem 4.11 wording, `boxtimes-strongly log-unimodal`, `strong log-unimodality` with `sigma_t`, the arXiv identifier, author names, and later papers/citations through 2026. The search recovered the source and later work on free positive multiplicative Brownian motion (including Martin Auer, *Free Positive Multiplicative Brownian Motion and the Free Additive Convolution of Semicircle and Uniform Distributions*, J. Theor. Probab. 39 (2026), article 51), but no later paper claiming a resolution of exact Problem 4.11. This is a bounded current-status pass, not an exhaustive novelty certificate. Accordingly exact Problem 4.11 is treated as currently **OPEN**.

# 3. Source criterion to be used

For \(b\in(0,\pi)\), the source defines
\[
\lambda_b(dx)=\frac{c_b}{1-2x\cos b+x^2}\,dx,
\qquad
c_b=\frac{\sin b}{\pi-b}.
\tag{3.1}
\]

Its log-pushforward has the even density
\[
h_b(x)
=\frac{c_b}{2(\cosh x-\cos b)}.
\tag{3.2}
\]

Source Lemma 4.1 says that \(\sigma_t\boxtimes\nu\) is log-unimodal iff, for every \(a\in(0,1/t)\), the equation
\[
\frac{r}{c_{a\pi t}}
\frac{d(\lambda_{a\pi t}\circledast\nu^{-1})}{dx}(r)
=
\frac{a\pi}{\sin(a\pi t)}
\tag{3.3}
\]
has at most two positive solutions \(r\). Thus four certified crossings of one level in the log-density of \(\lambda_b\circledast\nu^{-1}\) give a direct witness against strong log-unimodality.

# 4. Explicit log-unimodal witness family

Set the exact constants
\[
p=\frac3{50},\qquad \ell=19,\qquad
D=\frac{4573}{100000},\qquad b_0=\frac1{320}.
\tag{4.1}
\]

For each \(b\in(0,b_0]\), define \(\nu_b\) by its logarithmic pushforward
\[
\log_*\nu_b
=
 p\,\delta_0
 +\frac{1-p}{\ell b}\mathbf 1_{[-\ell b,0]}(y)\,dy.
\tag{4.2}
\]
Equivalently,
\[
\nu_b
=p\,\delta_1
+\frac{1-p}{\ell b\,x}
\mathbf 1_{[e^{-\ell b},1]}(x)\,dx.
\tag{4.3}
\]

This is log-unimodal with mode \(1\): on the log line it consists of an atom at the mode plus a density which is nondecreasing on the left of the mode and zero on the right. Its inverse has
\[
\log_*\nu_b^{-1}
=
 p\,\delta_0
 +\frac{1-p}{\ell b}\mathbf 1_{[0,\ell b]}(y)\,dy.
\tag{4.4}
\]

Let \(q_b\) be the density of
\[
\log_*(\lambda_b\circledast\nu_b^{-1}).
\]
Because logarithm converts classical multiplicative convolution to additive convolution,
\[
q_b(x)
=
 p h_b(x)
 +\frac{1-p}{\ell b}
 \int_0^{\ell b}h_b(x-y)\,dy.
\tag{4.5}
\]

# 5. Normalized small-b kernel and exact uniform error

Define
\[
A_b:=\frac{\pi}{\pi-b},
\qquad
K_b(v):=\frac{b}{A_b}h_b(bv)
=
\frac{b\sin b}{2\pi(\cosh(bv)-\cos b)}.
\tag{5.1}
\]
Its \(b\downarrow0\) limit is the standard Cauchy kernel
\[
K_0(v)=\frac1{\pi(1+v^2)}.
\tag{5.2}
\]

The exact factorization is
\[
\frac{K_b(v)}{K_0(v)}
=
B_b C_b(v),
\tag{5.3}
\]
where
\[
B_b=\frac{\sin b}{b},
\qquad
C_b(v)
=
\frac{b^2(1+v^2)}{2(\cosh(bv)-\cos b)}.
\tag{5.4}
\]

## Claim R18-I0080-C001 — PROVED

For every
\[
0<b\le\frac1{320},\qquad |v|\le19,
\]
we have
\[
\boxed{|K_b(v)-K_0(v)|<\frac1{1600}.}
\tag{5.5}
\]

### Proof

The elementary Taylor inequalities give
\[
1-\frac{b^2}{6}\le B_b\le1.
\tag{5.6}
\]
For the denominator in \(C_b\), use
\[
\cosh x-1\ge\frac{x^2}{2},
\qquad
1-\cos b\ge\frac{b^2}{2}-\frac{b^4}{24},
\]
to obtain
\[
C_b(v)
\le
\frac1{1-b^2/[12(1+v^2)]}
\le
\frac{1228800}{1228799}.
\tag{5.7}
\]

For the opposite direction, the identity
\(\cosh x-1=2\sinh^2(x/2)\), together with \(\tanh u\le u\), gives
\[
\cosh x-1\le \frac{x^2}{2}\cosh x.
\tag{5.8}
\]
Also \(1-\cos b\le b^2/2\). Since \(|bv|\le19/320\), the series comparison
\[
\cosh x
=\sum_{n\ge0}\frac{x^{2n}}{(2n)!}
\le
\sum_{n\ge0}\left(\frac{x^2}{2}\right)^n
=\frac1{1-x^2/2}
\]
yields
\[
C_b(v)\ge\frac{204439}{204800}.
\tag{5.9}
\]
Finally
\[
B_b\ge1-\frac1{614400}.
\tag{5.10}
\]

The exact rational checker verifies
\[
1-\left(1-\frac1{614400}\right)\frac{204439}{204800}
=
\frac{222002839}{125829120000}
<\frac3{1600},
\tag{5.11}
\]
and
\[
\frac{1228800}{1228799}-1
=\frac1{1228799}
<\frac3{1600}.
\tag{5.12}
\]
Thus
\[
\left|\frac{K_b(v)}{K_0(v)}-1\right|<\frac3{1600}.
\]
Since \(K_0(v)<1/3\), (5.5) follows. QED.

# 6. Three exact limiting inequalities

Define the normalized moving-average profile
\[
S_b(y)
:=
\frac{b}{A_b}q_b(by)
=
 pK_b(y)
 +\frac{1-p}{\ell}
 \int_{y-\ell}^{y}K_b(v)\,dv.
\tag{6.1}
\]
Its limit is
\[
Q(y)
=
\frac{p}{\pi(1+y^2)}
+
\frac{1-p}{\ell\pi}
\big(\arctan y-\arctan(y-\ell)\big).
\tag{6.2}
\]

For the three sample points
\[
y_1=\frac12,
\qquad y_2=2,
\qquad y_3=\frac{35}{4},
\tag{6.3}
\]
the integration intervals \([y_i-19,y_i]\) lie inside \([-19,19]\). Claim C001 therefore gives
\[
|S_b(y_i)-Q(y_i)|<\frac1{1600}.
\tag{6.4}
\]

## Claim R18-I0080-C002 — PROVED / EXACT FINITE CORE

With \(D=4573/100000\),
\[
\boxed{
Q(1/2)>D+1/1600,
\quad
Q(2)<D-1/1600,
\quad
Q(35/4)>D+1/1600.
}
\tag{6.5}
\]

The run-specific checker proves (6.5) using **only exact rational arithmetic**. It first encloses \(\pi\) from Machin's identity
\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]
with alternating rational series, then encloses all required arctangents similarly. No floating-point value enters the certificate.

For orientation only, the limiting values are approximately
\[
Q(1/2)=0.0464668\ldots,
\quad
Q(2)=0.0450666\ldots,
\quad
Q(35/4)=0.0463964\ldots,
\]
while \(D=0.04573\). The exact checker, not these decimals, is the proof.

Combining C001 and C002 gives, for every \(0<b\le b_0\),
\[
\boxed{
S_b(1/2)>D,
\quad
S_b(2)<D,
\quad
S_b(35/4)>D.
}
\tag{6.6}
\]

# 7. Four level crossings and exact time matching

Set
\[
d_b:=\frac{A_bD}{b}
=
\frac{\pi D}{b(\pi-b)}.
\tag{7.1}
\]
Since \(q_b(by)=(A_b/b)S_b(y)\), (6.6) says
\[
q_b(b/2)>d_b,
\qquad
q_b(2b)<d_b,
\qquad
q_b(35b/4)>d_b.
\tag{7.2}
\]
Moreover \(q_b(x)\to0\) as \(x\to\pm\infty\). By continuity, the equation
\[
q_b(x)=d_b
\tag{7.3}
\]
has at least four distinct real solutions: one left of \(b/2\), one between \(b/2\) and \(2b\), one between \(2b\) and \(35b/4\), and one right of \(35b/4\).

If \(f_b\) is the density of \(\lambda_b\circledast\nu_b^{-1}\) on \(\mathbb R_+\), then
\[
q_b(\log r)=r f_b(r).
\tag{7.4}
\]
Hence
\[
r f_b(r)=d_b
\]
has at least four positive solutions.

Now define
\[
\boxed{
t(b):=\frac{b^2}{\pi D},
\qquad
a(b):=\frac{D}{b}.}
\tag{7.5}
\]
Then
\[
a(b)\pi t(b)=b
\tag{7.6}
\]
and, because \(c_b=\sin b/(\pi-b)\),
\[
\frac{d_b}{c_b}
=
\frac{\pi D}{b\sin b}
=
\frac{a(b)\pi}{\sin(a(b)\pi t(b))}.
\tag{7.7}
\]
Also \(a(b)<1/t(b)\) because \(b<\pi\).

Thus source Lemma 4.1(2) applies at the admissible parameter \(a(b)\), and the four solutions above prove
\[
\boxed{\sigma_{t(b)}\boxtimes\nu_b\text{ is not log-unimodal}.}
\tag{7.8}
\]
Since \(\nu_b\) is log-unimodal, \(\sigma_{t(b)}\) is not \(\boxtimes\)-strongly log-unimodal.

# 8. Interval theorem and metric movement

The map
\[
b\longmapsto t(b)=\frac{b^2}{\pi D}
\]
is a strictly increasing bijection from \((0,b_0]\) onto \((0,T_*]\), where
\[
\boxed{
T_*=\frac{b_0^2}{\pi D}
=\frac{125}{585344\pi}.}
\tag{8.1}
\]

Therefore:

## Theorem R18-I0080-C003 — PROVED

For every
\[
\boxed{0<t\le T_*=\frac{125}{585344\pi},}
\]
there is an explicit log-unimodal probability measure \(\nu_b\), with
\[
b=\sqrt{\pi Dt},
\]
such that
\[
\boxed{\sigma_t\boxtimes\nu_b\text{ is not log-unimodal}.}
\]
Equivalently,
\[
\boxed{\sigma_t\text{ is not }\boxtimes\text{-strongly log-unimodal for every }0<t\le T_*.}
\tag{8.2}
\]

The exact checker proves the numerical enclosure
\[
0.000067<T_*<0.000069.
\tag{8.3}
\]

This is a **quantitative partial result** toward Problem 4.11. It makes the fleet metric measurable and positive; it does not replace the source's open all-time question.

# 9. Counterexample-first search and failed routes preserved

This was the first run on the revised I0080 target, so I followed the fleet rule and searched for explicit counterexamples before attempting an all-time theorem.

1. **Source semigroup propagation is nonquantitative for the fleet metric.** Source Theorem 4.9 proves existence of some \(t_0>0\), but Step 3 defines a maximal strong-good time \(t_2\) and obtains \(t_0=t_1-t_2\). No explicit lower bound on \(t_1-t_2\) is supplied. This route establishes existence but leaves the endpoint `UNMEASURED`.

2. **An isolated nonunimodal time is not enough.** The fleet metric requires one scheme covering every time from zero to the endpoint. I therefore rejected numerical witnesses at isolated \(t\)'s as insufficient.

3. **Symmetric log-uniform inputs are the wrong classical witness for this step.** Convolution of the even unimodal \(h_b\) with a centered uniform density remains symmetric unimodal; this cannot witness classical failure. The successful family uses an atom at the mode plus a one-sided uniform log-density, which is still unimodal but asymmetric.

4. **Numerical exploration was discovery only.** It suggested the simple rational constants \(p=3/50\), \(\ell=19\) and three scaled sample points. The final theorem does not depend on sampled numerics: the finite margins and \(\pi\) enclosure are certified in exact rational arithmetic, and the continuum \(b\)-dependence is controlled analytically by C001.

5. **Problem exclusions respected.** No argument from the already-refuted multiplicative Problem 4.7 is used as a solution of Problem 4.11; P20's Problem 4.3 is distinct; additive Problem 3.3 is not this track.

# 10. Reproducibility and exact evidence

Run-specific exact checker:

`artifacts/R18/2026-09-16_13-31-00_UTC__R18__i0080-explicit-smalltime__checker.py`

GitHub commit:

`d419c0b23cd2eb8cb9e27e2b1f75609fd64db491`

Archived checker output:

`artifacts/R18/2026-09-16_13-31-00_UTC__R18__i0080-explicit-smalltime__checker-output.txt`

GitHub commit:

`2ed78d9dfe806a86c1e568c9f86a347b991fe582`

Local executed-output SHA-256:

`328db7263b0f11981864904e4ec7d0d3a53c3b4e8ad6beb2d5979d177cfd04c0`

Both GitHub artifact writes were read back at their returned commit SHAs before this report was committed.

# 11. What remains open / next attack

The fixed metric should now be optimized, not reset. Current rigorous endpoint:
\[
T_{\rm cert}\ge T_*=\frac{125}{585344\pi}.
\]

The next obligation is to enlarge the certified \(b\)-range for the **same explicit witness architecture**, because that monotonically enlarges the full time interval. The present proof deliberately uses a very crude uniform bound
\(|v|\le19\) and the inequality \(K_0<1/3\). There is substantial slack available by integrating the pointwise kernel error rather than taking its worst value, and by replacing the global \(\cosh\) bound with a piecewise rational enclosure. That route can improve \(b_0\), hence \(T\propto b_0^2\), without changing the source criterion or requiring an isolated-time patchwork.

A second route is to optimize \((p,\ell,D)\) with exact rational certification after the analytic form is fixed. Any proposed improvement must still certify **one continuous interval** \((0,T]\), not sampled times.

Full Problem 4.11 remains open for large times; no claim of closure is made.

# 12. Structured ledger_delta for P26

```json
{
  "worker": "R18",
  "source": "Takahiro Hasebe, Yuki Ueda, Jiun-Chau Wang, Log-unimodality for free positive multiplicative Brownian motion, arXiv:2009.13848 (2020), Colloq. Math. 169 (2022), Problem 4.11; intake I0080",
  "target": "Determine whether sigma_t fails boxtimes-strong log-unimodality for every t>0",
  "metric": "largest rigorously certified endpoint T for one witness scheme covering every 0<t<=T",
  "before": "UNMEASURED (source Theorem 4.9 proves existence of some t0>0 but gives no explicit endpoint)",
  "after": "T_cert >= 125/(585344*pi), with exact checker proving 0.000067 < T_* < 0.000069",
  "status": "PARTIAL; source problem OPEN",
  "unchanged_count": 0,
  "exact_evidence": [
    "artifacts/R18/2026-09-16_13-31-00_UTC__R18__i0080-explicit-smalltime__checker.py @ d419c0b23cd2eb8cb9e27e2b1f75609fd64db491",
    "artifacts/R18/2026-09-16_13-31-00_UTC__R18__i0080-explicit-smalltime__checker-output.txt @ 2ed78d9dfe806a86c1e568c9f86a347b991fe582",
    "output_sha256=328db7263b0f11981864904e4ec7d0d3a53c3b4e8ad6beb2d5979d177cfd04c0"
  ],
  "claims": [
    "R18-I0080-C001 PROVED: uniform normalized-kernel error <1/1600 for 0<b<=1/320, |v|<=19",
    "R18-I0080-C002 PROVED EXACT CORE: three limiting rational witness inequalities",
    "R18-I0080-C003 PROVED PARTIAL: explicit witness family covers every 0<t<=125/(585344*pi)"
  ],
  "audit_ids": [
    "P26:PENDING",
    "OTHER_TRACK:PENDING"
  ],
  "directed_R19_audit": "NOT_READY: no revised I0084 R19 package found; only stale pre-reassignment R19 commits were visible",
  "retired_assignment_handoff": "proofnet24/R18-salem-bernoulli-convolutions preserved; cumulative ledger commit 2274925de658dde2f5ca7bd5f26f1d6e4e8e2c5c; substantive report commit 894870d09b49ad44e89bfbda8f110eac0fa4ba85"
}
```
