Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no model or reasoning selector is exposed in this runtime, so I do not claim otherwise. **NO MOVEMENT in the frozen metric: 2/2 -> 2/2; unchanged count after saturation: 3. Section-B moves tried this run: 11 (DUALIZE), 22 (READ THE FAILURES), 29 (ADD THE POINTS AT INFINITY).**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY; portfolio status remains PARTIAL / AUDIT_PENDING.** The frozen alpha=1/2 case count was already saturated at 2/2. This run does not manufacture metric movement. It instead proves a new source-scope extension: every extremal-skewness classical or free strictly stable kernel with alpha in `(0,2)\{1}` admits an initial law having *all polynomial moments* for which ordinary convolution is nonunimodal at every time. It also upgrades the classical branch to an exact all-skewness classification for every alpha != 1.

## 1. Recovery and exact source convention

I continued from current `master`, in particular from

`runs/R19/2026-09-16_17-36-54_UTC__i0084-skewness-classification.md`

rather than from chat memory. At run start I read/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- current I0084/R19 history and the existing R18 audit trail;
- newest R20/I0100 report, now the exact `p=241` package.

I0084 remains exclusively assigned to R19 in the queue. Hasebe--Ueda Problem 3.3 / Brownian sharp constants are POSTED/EXCLUDED and are not counted here. The old R19 free-group-factor assignment remains retired.

### Source wording, rechecked

The current arXiv text of Conjecture 5.5 reads, in substance:

- `S_t` is the law of a **classical or free alpha-stable process** at time `t`, alpha in `(0,2)`;
- the initial law satisfies
  \[
  \int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty;
  \]
- the claimed conclusion is that
  \[
  \mu * S_t
  \]
  is unimodal for all sufficiently large `t`.

Thus the source uses **ordinary classical convolution `*` in both branches**. I do not substitute free convolution.

For alpha != 1 I use Hasebe--Kuznetsov's common positivity parameter:
\[
\mathcal A
=
\{0<\alpha<1,\ 0\le\rho\le1\}
\cup
\{1<\alpha\le2,\ 1-\alpha^{-1}\le\rho\le\alpha^{-1}\}.
\tag{1.1}
\]
The boundary values are the extremal skewnesses. Translation/drift does not affect unimodality, and nonzero scale merely changes the scale parameter below.

## 2. The three new-method moves

### Move 29 — ADD THE POINTS AT INFINITY

The previous endpoint proof exploited literal one-sided support at alpha=1/2. I asked what replaces the missing half-line when alpha crosses 1. Hasebe--Kuznetsov's complete stable-density expansions show the answer: at an extremal classical alpha>1 law, the heavy-tail coefficient vanishes not just to first order but at **every algebraic order** on one side. For the corresponding free endpoint, duality makes that side actually compactly supported. The skewness boundary is therefore a boundary at infinity: an algebraic tail disappears there.

### Move 11 — DUALIZE

Instead of tracking derivatives of a sparse convolution, I switched to **values at the center and two shoulders of each sparse spike**. This eliminates derivative-tail assumptions entirely. The right invariant is simply: one tail of the kernel is smaller than every power. This produces C010 below.

### Move 22 — READ THE FAILURES

Hasebe--Simon--Wang explicitly say that the exact shape of free stable densities beyond their bell-shape range remains unresolved; in particular their Theorem 4 gives bell shape for `0<alpha<=3/4` in the two-sided free case but leaves the exact shape for alpha>1 open. This identifies a genuine obstruction to extending the *positive interior* theorem C008 to all free-stable parameters. I therefore separate the endpoint theorem, which needs only strict unimodality plus a light tail, from the interior theorem, which needs stronger local shape.

# R19-I0084-C010 — superpolynomial-light-tail sparse-bump theorem

**STATUS: PROVED.**

Let `k` be a bounded continuous probability density on `R`. Assume, after translation, that `0` is a strict mode in the following quantitative sense: there is `h>0` such that
\[
\Delta
:=
k(0)-\max\{k(-h),k(h)\}>0.
\tag{C010.1}
\]
Put
\[
B=\|k\|_\infty.
\]

Assume its **left tail is superpolynomially light**:
\[
K(r):=\sup_{x\le-r}k(x),
\qquad
r^N K(r)\longrightarrow0
\quad(r\to\infty)
\quad\text{for every }N>0.
\tag{C010.2}
\]

For `s>0`, let
\[
k_s(x)=s^{-1}k(x/s).
\tag{C010.3}
\]

Then there exists a probability measure `mu`, independent of `s`, such that

\[
\int |x|^p\,d\mu(x)<\infty
\qquad\text{for every finite }p>0,
\tag{C010.4}
\]
but
\[
\boxed{\mu*k_s\ \text{is nonunimodal for every }s>0.}
\tag{C010.5}
\]

The same conclusion holds with "left" replaced by "right", by reflection.

## Proof

Choose
\[
0<\varepsilon
\le
\min\left\{\frac14,\frac{\Delta}{16B}\right\}.
\tag{C010.6}
\]

We recursively choose `a_n -> infinity`, with `a_n>=2`, and define
\[
q_n=a_n^{-n}.
\tag{C010.7}
\]
Choose them so large that for every `n>=2`,
\[
a_n\ge3(a_{n-1}+nh),
\tag{C010.8}
\]
\[
q_n\le\varepsilon q_{n-1},
\tag{C010.9}
\]
and for every `n>=1`,
\[
K\!\left(\frac{a_n}{3n}\right)
\le
\frac{\Delta}{8}\,q_n.
\tag{C010.10}
\]
Also choose `a_1` so large that
\[
q_1/(1-\varepsilon)\le1/2.
\tag{C010.11}
\]

These choices are possible. The only nontrivial point is (C010.10). For fixed `n`, (C010.2) with exponent `n+1` gives
\[
K(r)=o(r^{-n-1}).
\]
Putting `a=3nr`,
\[
K(a/(3n))
=o(a^{-n}),
\]
because the extra factor `r^{-1}` beats the fixed factor `(3n)^n`. Hence (C010.10) holds for all sufficiently large `a_n`; making `a_n` still larger enforces (C010.8)--(C010.9).

By (C010.9)--(C010.11),
\[
\sum_{n\ge1}q_n
\le
\frac{q_1}{1-\varepsilon}\le\frac12.
\]
Define
\[
\mu
=
\left(1-\sum_{n\ge1}q_n\right)\delta_0
+
\sum_{n\ge1}q_n\delta_{-a_n}.
\tag{C010.12}
\]

### All moments are finite

Fix `p>0`. For every integer `n>p`,
\[
q_n a_n^p=a_n^{p-n}\le2^{p-n}.
\]
The tail is summable, and the finitely many earlier terms are finite. Thus (C010.4) holds.

### Every scale has infinitely many strict bumps

Fix arbitrary `s>0`. For every integer `n>=s`, consider
\[
c_n=-a_n,\qquad
I_{n,s}=[c_n-sh,c_n+sh].
\]
Write
\[
f_s=\mu*k_s.
\]

We compare the center `c_n` to either shoulder `c_n+\sigma sh`, `sigma in {-1,+1}`.

The `n`th atom gives
\[
\frac{q_n}{s}
\left[k(0)-k(\sigma h)\right]
\ge
\frac{\Delta q_n}{s}.
\tag{C010.13}
\]

For every atom to the **right** of `-a_n` (including the atom at zero and all indices `j<n`), (C010.8) and `s<=n` imply at all three points
\[
\frac{x+a_j}{s}
\le
-\frac{a_n}{3s}.
\]
Thus the total absolute contamination in the center-versus-shoulder difference from all those atoms is at most
\[
\frac{2}{s}
K\!\left(\frac{a_n}{3s}\right)
\le
\frac{2}{s}
K\!\left(\frac{a_n}{3n}\right)
\le
\frac{\Delta q_n}{4s}.
\tag{C010.14}
\]

For the atoms farther **left**, `j>n`, boundedness of `k` and the geometric weight decay give
\[
\sum_{j>n}q_j
\le
\frac{\varepsilon}{1-\varepsilon}q_n,
\]
hence their center-versus-shoulder contamination is at most
\[
\frac{2B}{s}
\frac{\varepsilon}{1-\varepsilon}q_n
\le
\frac{\Delta q_n}{4s}.
\tag{C010.15}
\]
(The last inequality follows from `epsilon<=1/4` and
`epsilon<=Delta/(16B)`.)

Combining (C010.13)--(C010.15),
\[
f_s(c_n)-f_s(c_n+\sigma sh)
\ge
\frac{\Delta q_n}{2s}>0
\qquad(\sigma=\pm1).
\tag{C010.16}
\]

The intervals `I_{n,s}` are pairwise disjoint for all sufficiently large `n`, by (C010.8). On each such interval continuity gives an interior local peak whose value is strictly larger than both endpoint values.

A unimodal function is nondecreasing to one mode and nonincreasing afterwards. Therefore a disjoint interval lying wholly to the left of the mode cannot have an interior value strictly above its right endpoint, and one lying wholly to the right cannot have an interior value strictly above its left endpoint. At most one of the disjoint intervals can contain the mode. Since there are infinitely many, `f_s` is not unimodal.

Since `s>0` was arbitrary, (C010.5) follows. Reflection proves the right-tail version. QED.

## Why C010 is different from the source's sparse-atom examples

Hasebe--Ueda's Cauchy and positive-half-stable examples balance a polynomial kernel derivative against sparse atoms; their own discussion shows those particular constructions hit the critical third- and `5/2`-moment walls. C010 uses a different mechanism: **the kernel itself has a superpolynomially light tail**, so a polynomially weighted sparse atom can make a local bump while retaining every polynomial moment.

The mechanism is elementary and adjacent to the source's sparse-atom philosophy; absolute novelty is not claimed.

# R19-I0084-C011 — all extremal-skewness stable endpoints fail for alpha != 1

**STATUS: PROVED from C010 plus primary stable-density formulas.**

Use Hasebe--Kuznetsov's parameter set (1.1).

For every
\[
\alpha\in(0,1)\cup(1,2),
\]
and for **each extremal admissible skewness** `rho`, the following holds for both:

1. the classical strictly alpha-stable law;
2. the free strictly alpha-stable law, used exactly as the source requests, namely as a kernel under ordinary classical convolution.

There exists a probability law `mu` satisfying
\[
\int |x|^p\,d\mu(x)<\infty
\quad\text{for every }p<\infty
\tag{C011.1}
\]
such that
\[
\boxed{
\mu*S_t
\text{ is nonunimodal for every }t>0.
}
\tag{C011.2}
\]

Translations/drifts of the stable process do not affect the conclusion.

## Classical branch, 0<alpha<1

At `rho=1` the classical stable law is one-sided positive; at `rho=0` it is the reflection. Thus one density tail is identically zero. The density has a strict mode (indeed classical stable densities are bell-shaped). C010 applies immediately.

## Classical branch, 1<alpha<2

The extremal parameters are
\[
\rho=\alpha^{-1},
\qquad
\rho=1-\alpha^{-1}.
\]

Hasebe--Kuznetsov record the classical density expansion
\[
p_{\alpha,\rho}(x)
\sim
\frac1\pi
\sum_{n\ge1}
(-1)^{n-1}
\frac{\Gamma(1+\alpha n)}{n!}
\sin(n\pi\alpha\rho)\,
x^{-\alpha n-1},
\qquad x\to+\infty,
\tag{C011.3}
\]
as a **complete asymptotic series** when `alpha>1`.

At `rho=1/alpha`,
\[
\sin(n\pi\alpha\rho)=\sin(n\pi)=0
\quad\text{for every }n.
\]
Consequently the right density tail is smaller than every power:
\[
x^N p_{\alpha,1/\alpha}(x)\to0
\quad\text{for every }N>0.
\tag{C011.4}
\]
Gawronski's bell-shape theorem supplies a strict mode. C010 therefore applies to this light right tail. The other endpoint follows by reflection.

## Free branch, 0<alpha<1

For `rho=1`, Hasebe--Kuznetsov Theorem 2 gives, on
\[
0\le x\le x_\alpha^*
=
\alpha(1-\alpha)^{1/\alpha-1},
\]
the convergent series
\[
\psi_{\alpha,1}(x)
=
\frac1\pi
\sum_{n\ge1}
(-1)^{n-1}
\frac{\Gamma(1+n/\alpha)}
{n!\Gamma(2+(1/\alpha-1)n)}
\sin(n\pi)\,x^{n-1}
=0.
\tag{C011.5}
\]
Together with positivity parameter `P(X_{\alpha,1}>0)=1`, this is the familiar positive free stable half-line support. Thus the left tail is identically zero. Strict unimodality of free stable densities is known from the Bercovici--Pata/Biane analysis and is recalled explicitly by Hasebe--Simon--Wang. C010 applies. `rho=0` follows by reflection.

## Free branch, 1<alpha<2

Take `rho=1/alpha` and put `beta=1/alpha in (0,1)`. Hasebe--Kuznetsov's free-stable duality gives, for `x>0`,
\[
\psi_{\alpha,1/\alpha}(x)
=
x^{-\alpha-1}
\psi_{\beta,1}(x^{-\alpha}).
\tag{C011.6}
\]
By (C011.5), `psi_{beta,1}(u)=0` on `[0,x_beta^*]`. Hence
\[
\psi_{\alpha,1/\alpha}(x)=0
\quad\text{whenever}\quad
x\ge (x_\beta^*)^{-1/\alpha}.
\tag{C011.7}
\]
So the free extremal alpha>1 density has an actual finite edge on its right side. This agrees with Hasebe--Simon--Wang's statement that `f_{\alpha,1/\alpha}` has negative-half-line support. Strict unimodality again supplies the strict mode, and C010 applies. The other extremal parameter follows by reflection.

## Source consequence

Every C011 witness has every finite moment, hence in particular the source-required `(2+alpha)` moment. Therefore the endpoint obstruction is not a half-stable accident: for every alpha != 1, extremal skewness defeats eventual unimodality under the source's ordinary convolution convention.

# R19-I0084-C012 — exact classical-stable skewness classification for alpha != 1

**STATUS: PROVED internally; independent audit pending.**

For the **classical** strictly stable kernel, C011 handles the boundary of the admissible skewness interval. In the interior, the source conjecture is true.

Precisely, let
\[
\alpha\in(0,1)\cup(1,2)
\]
and let `rho` lie in the interior of the Hasebe--Kuznetsov admissible interval:
\[
0<\rho<1
\quad(\alpha<1),
\]
or
\[
1-\alpha^{-1}<\rho<\alpha^{-1}
\quad(\alpha>1).
\tag{C012.1}
\]
Then for every probability measure `mu` with
\[
M_{2+\alpha}:=\int |x|^{2+\alpha}\,d\mu(x)<\infty,
\tag{C012.2}
\]
ordinary convolution with the corresponding classical alpha-stable semigroup is unimodal for all sufficiently large time.

## Proof

The retained C008 critical-tail smoothing theorem applies once its four kernel inputs are checked with
\[
p=2+\alpha.
\]

1. **Strict, nondegenerate mode.** Gawronski proved every classical stable density bell-shaped: its first derivative has exactly one simple zero. At the mode this implies
   \[
   k''(m)<0.
   \]
   After translation, C008's local strict-concavity hypothesis follows.

2. **Both density tails have positive algebraic leading terms.** Hasebe--Kuznetsov give
   \[
   k(x)\sim C_+x^{-1-\alpha},
   \qquad
   k(-x)\sim C_-x^{-1-\alpha},
   \tag{C012.3}
   \]
   with
   \[
   C_+=\frac{\Gamma(1+\alpha)}{\pi}\sin(\pi\alpha\rho)>0,
   \]
   \[
   C_-=\frac{\Gamma(1+\alpha)}{\pi}
   \sin(\pi\alpha(1-\rho))>0
   \tag{C012.4}
   \]
   exactly for the interior ranges (C012.1).

3. **Derivative-tail lower bounds follow without differentiating an asymptotic series.** Bell shape says `k''` has exactly two simple zeros. Since `k'(x)<0` to the right of the mode and `k'(x)->0`, the sign of `k''` after its last zero must be positive. Thus `k` is eventually decreasing and convex on the right. For large `x`, convexity gives
   \[
   k'(x)
   \le
   \frac{k(2x)-k(x)}{x},
   \]
   hence
   \[
   -k'(x)
   \ge
   \frac{k(x)-k(2x)}{x}
   \ge
   c_+x^{-2-\alpha}.
   \tag{C012.5}
   \]
   The reflected argument gives
   \[
   k'(-x)\ge c_-x^{-2-\alpha}.
   \tag{C012.6}
   \]

4. Stable densities are smooth with bounded first and second derivatives.

Therefore C008 gives eventual unimodality for every input satisfying (C012.2). Since a strictly alpha-stable process has spatial scale proportional to `t^{1/alpha}`, the sufficient threshold has the source-critical scaling
\[
t
\ge
C_{\alpha,\rho}
M_{2+\alpha}^{\alpha/(2+\alpha)}.
\tag{C012.7}
\]
The constant is not claimed sharp.

Combining this with C011 yields the complete classical `alpha != 1` table:
\[
\boxed{
\begin{array}{c|c}
\text{skewness} & \text{ordinary stable smoothing under finite }(2+\alpha)\text{ moment}\\
\hline
\text{extremal boundary} & \text{FALSE: one all-moments input is nonunimodal for every }t>0\\
\text{admissible interior} & \text{TRUE for every admissible input for all sufficiently large }t.
\end{array}}
\tag{C012.8}
\]

The alpha=1 skew-stable family is not silently folded into this parameterization. The source separately proves the symmetric Cauchy case; this run makes no new full alpha=1 skewness claim.

# R19-I0084-C013 — free-stable ordinary-convolution scope now proved

**STATUS: PARTIAL classification.**

For the free strictly stable density used as an **ordinary convolution kernel**:

- every extremal endpoint with `alpha in (0,1) union (1,2)` is FALSE by C011;
- for `0<alpha<=3/4` and `0<rho<1`, eventual unimodality for every finite `(2+alpha)`-moment input follows from C008, because Hasebe--Simon--Wang Theorem 4(b) proves those free stable densities bell-shaped, while Hasebe--Kuznetsov supplies the two positive algebraic tails;
- the previously frozen alpha=1/2 interior is the special case already recorded as C009.

The current method does **not** prove the free interior for
\[
3/4<\alpha<1
\quad\text{or}\quad
1<\alpha<2.
\tag{C013.1}
\]
Hasebe--Simon--Wang prove strict unimodality for all free stable densities but explicitly leave the exact shape beyond their proved bell-shape regimes unresolved. Strict unimodality alone does not supply C008's quantitative central curvature. This is now the exact analytic obstruction rather than a vague failure of the sparse-tail route.

## 3. Prior-art and status check — 2026-09-16

Fresh bounded web/arXiv checks this run included:

- exact `arXiv:1710.08240` and `Conjecture 5.5`;
- `"eventual unimodality" stable convolution finite moment`;
- `"Conjecture 5.5" Hasebe Ueda stable`;
- later Hasebe/Ueda papers and citing/related papers;
- Hasebe--Kuznetsov, *On free stable distributions* (ECP 2014, arXiv:1404.2981; current arXiv revision);
- Hasebe--Simon--Wang, *Some properties of the free stable distributions* (arXiv:1805.01133);
- Gawronski, *On the Bell-Shape of Stable Densities* (Ann. Probab. 1984);
- searches for superpolynomial-tail sparse-convolution unimodality obstructions.

No accessible later paper was found resolving Hasebe--Ueda Conjecture 5.5 or stating C010--C013 in this form. That is a bounded search, not proof of absolute novelty.

Known ingredients are separated explicitly:

- strict/bell shape and stable tail/duality formulas are literature;
- the sparse-atom philosophy is already present in Hasebe--Ueda;
- the abstract superpolynomial-tail bump theorem C010 and its endpoint/classification synthesis C011--C013 are the new candidate contributions of this track, pending independent audit.

## 4. Audit/closure state for I0084

The mathematical source conjecture is already false because its quantifier includes the source-admissible extremal half-stable endpoint. Repository closure is not yet claimed.

Located audit evidence remains:

- `R18-I0084-C001=PASS` for the classical positive half-stable endpoint finite/symbolic core;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF` for the *different later free-boxplus formulation*, not the current arXiv ordinary-convolution free kernel;
- no P26 I0084 audit located this run;
- no independent OTHER-track audit yet located for C008/C009 or the new C010--C013 ordinary-convolution claims.

Thus the closure gate remains `PARTIAL / AUDIT_PENDING`; no paper folder is created.

## 5. Directed independent audit of the newest R20 package

A genuinely new R20 package was ready:

`runs/R20/2026-09-16T17-46-41Z_i0100_p241_newmethods_c91f2e.md`.

I independently rebuilt its finite `p=241` certificate rather than merely rereading its PASS output.

Audit ID:

`R19-AUDIT-R20-I0100-P241-02 = PASS_EXACT_FINITE_CASE`.

The independent checker:

- re-derived the localized Paley nonedge representatives directly in `F_241` using primitive root `7`;
- independently verified the minimal polynomial of `2 cos(2 pi/120)`;
- reconstructed the active primal and dual solutions from 24 split finite fields by CRT and rational reconstruction;
- checked exact primal normalization and all 30 exact Fourier zero constraints;
- proved all 31 active primal weights strictly positive by exact isolating-interval signs;
- proved all 120 dual slacks nonnegative, with exactly 60 zero and 60 strictly positive;
- checked exact complementary slackness on the active support and exact equality `a=w_0`.

It reproduced
\[
\vartheta(\overline{G_{241,1}})
=
10.59549306028889149155324575505421790878\ldots
\]
and ratio
\[
0.9652229686323016568957567420955405664132\ldots
\]
to `sqrt(241/2)`.

Artifacts were executed locally as an independent check and then archived/read back:

- `artifacts/R19/2026-09-16_18-43-44_UTC__R19__audit_R20_i0100_p241.py`
  at commit `efa480d3ed9659a40f87581447fb431d21f44d8a`;
- output
  `artifacts/R19/2026-09-16_18-43-44_UTC__R19__audit_R20_i0100_p241.out`
  at commit `64263095646e94b36487386a20f3d85ffda4b83e`;
- output SHA-256
  `5c43620720f017eee4492b78686cf8597e07707911edcb91cdf5d201f1c9242c`.

This audit certifies only the finite `p=241` case, not R20's asymptotic Conjecture 26.

## 6. Failed routes / exact obstruction

1. **Derivative shielding is unnecessary and too narrow.** It obscures the alpha>1 extremal case, where there is no literal one-sided classical support. C010 replaces it by a value-based local-bump argument needing only one superpolynomially light density tail.

2. **Strict unimodality is insufficient for the free interior.** An analytic strictly unimodal density can in principle have a degenerate flat maximum. C008's central uniqueness proof uses a quantitative negative-curvature neighborhood. Hasebe--Simon--Wang's bell-shape theorem supplies it only in the currently proved free ranges.

3. **Do not infer all-alpha closure from the endpoint theorem.** C011 refutes the source globally because one admissible endpoint is enough, but it does not classify every alpha/rho pair. C012 is a full classical alpha!=1 classification; C013 is only a partial free classification.

4. **Do not count stronger-moment results as source cases.** C010 witnesses have all moments and hence are legitimate refutations. C008/C012 use exactly the source moment `2+alpha`; no stronger moment is silently inserted.

## 7. Stagnation / next-run protocol

The fixed metric remains saturated:
\[
2/2\longrightarrow2/2.
\]
This is now the **third consecutive unchanged run after saturation**.

Therefore, unless an independent closure audit lands before the next invocation, the next R19 run must follow the section-I **thinking-only stuck protocol**: no new theorem claim. The exact blocking statement is not mathematical existence of a counterexample; it is closure plus the unresolved free-interior shape if one seeks classification:
\[
\text{obtain independent source-scope/full-proof audits for the arXiv ordinary-convolution branch,}
\]
and, beyond closure,
\[
\text{establish a quantitative nondegenerate-mode condition for free stable densities in the unproved interior regimes.}
\]

The next thinking run should compare exactly these routes and choose one. Proposed fresh Section-B moves for that strategy review: **20 (find why the algorithm fails), 21 (ask who else has this shape), 30 (one scale/direction at a time)**.

## 8. Model/runtime capability

No capability change was observed. The current repository operations record still says the exposed task interface has prompt/title/schedule/timing/enabled controls but no authenticated model or reasoning selector. Thus GPT-6/maximum is a request in prompt text, not a runtime fact I can assert. The prior P26 permission failure was context-dependent; a later authorized P/C context successfully updated P26. The permitted workaround is an authorized owner/platform context, not duplication or permission bypass. No schedule was changed in this run.

```yaml
ledger_delta:
  track: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240, Conjecture 5.5 / I0084"
  source_version_scope: "arXiv convention: S_t may be classical or free stable; ordinary classical convolution mu*S_t in both branches"
  target: "eventual unimodality under exact (2+alpha)-moment assumption, beginning alpha=1/2"
  metric: "number of two alpha=1/2 classical-stable/free-stable arXiv source cases resolved for all admissible initial measures"
  metric_before: "2/2"
  metric_after: "2/2"
  movement: "NO MOVEMENT; new scope theorem proves all extremal alpha!=1 endpoints false and classifies all classical alpha!=1 skewness"
  unchanged_count_after_saturation: 3
  status: "SOURCE_REFUTED_MATHEMATICALLY; PARTIAL_AUDIT_PENDING"
  tried_moves: [11, 22, 29]
  new_claims:
    - "R19-I0084-C010 PROVED internally: any strictly peaked kernel with one superpolynomially light tail admits an all-polynomial-moment sparse input whose every scaled convolution is nonunimodal"
    - "R19-I0084-C011 PROVED internally: for every alpha in (0,1) union (1,2), every extremal classical/free stable skewness is a source-valid all-time counterexample under ordinary convolution"
    - "R19-I0084-C012 PROVED internally: classical stable branch has exact alpha!=1 classification -- endpoints false, interior eventually true under exact finite (2+alpha) moment"
    - "R19-I0084-C013 PARTIAL: free endpoints false for all alpha!=1; free interior proved true through alpha<=3/4 using known bell shape; remaining interior not claimed"
  exact_evidence:
    - "C010--C013 full proofs in this immutable report; theorem-sized analytic claims, no finite core checker manufactured"
    - "R20 p241 independent exact audit script @ efa480d3ed9659a40f87581447fb431d21f44d8a"
    - "R20 p241 independent audit output @ 64263095646e94b36487386a20f3d85ffda4b83e; sha256 5c43620720f017eee4492b78686cf8597e07707911edcb91cdf5d201f1c9242c"
  audit_ids:
    classical_halfstable: "R18-I0084-C001=PASS"
    published_free_boxplus: "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF; different formulation"
    arxiv_ordinary_C008_C013: "PENDING_OTHER_TRACK"
    p26_i0084: "PENDING_NOT_LOCATED"
    r20_p241: "R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE"
  remaining_obligation: "P26 plus distinct OTHER full source-scope audit for arXiv ordinary-convolution I0084 package; next unchanged run triggers thinking-only stuck protocol"
  next_moves: [20, 21, 30]
```

**NO CLOSURE CLAIM.**
