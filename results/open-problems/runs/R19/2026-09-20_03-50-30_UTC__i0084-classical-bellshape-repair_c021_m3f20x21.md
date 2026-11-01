Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 headline metric); genuine theorem progress: the previously withheld arbitrary-alpha classical interior range is now repaired internally, so both frozen arXiv ordinary-`*` branches are structurally classified for every `0<alpha<2`. Section-B moves: #3 PROVE SOMETHING STRONGER, #20 FIND WHY THE ALGORITHM FAILS, #21 ASK WHO ELSE HAS THIS SHAPE. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C020 triple was #7/#18/#23, so this does not repeat the preceding triple.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at `alpha=1/2` because extremal skewness is allowed; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C021A/C021B are PROVED INTERNALLY / AUDIT PENDING and repair the general classical-stable interior theorem without relying on the erroneous 1984 all-alpha bell-shape proof.**

# 1. Continuity, source convention, and inherited state

I resumed from the actual latest R19 report

`runs/R19/2026-09-20_02-35-35_UTC__i0084-free-all-interior_c020_m7l18p23.md`

at creation commit `a5f981dbbbc08675d24ca6af2560f88a9974d491`.

An exact Git comparison from that commit to the current pre-write `master` was ahead-only (`behind_by=0`) and the complete returned changed-file set contained no later R19 report. The last pre-write head observed immediately before this report was `616a9cc58c136f650ddf7d8535cb872027273d06`. Thus C020 is the inherited R19 checkpoint and no peer R19 file is being overwritten.

I re-read the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the newest R19 report, and the controlling later directive `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md`. That directive supersedes repetitive admission/audit-only waiting, keeps the 90/10 mathematics-first budget, and explicitly says that an unchanged headline metric does not erase a genuine structural theorem.

The frozen primary source was checked again directly in arXiv v2, Section 5.2. Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\]

Accordingly, `*` below is **ordinary classical convolution even when `S_t` is the law of a free stable process**. I do not replace it by `\boxplus`.

The fixed `alpha=1/2` metric remains `2/2`: C009 already settles the two frozen source branches in the full input-measure class and full skewness convention. No new metric credit is claimed.

The useful retained engine is R19-I0084-C008, independently audited as

`R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`.

In the needed form, C008 says: if a fixed density `k`, translated to its mode, has bounded first two derivatives, strict derivative signs away from the mode, strict negative second derivative on a mode neighborhood, and two derivative-tail lower bounds of order `|x|^{-p}`, then every probability measure with finite `p`-th absolute moment becomes unimodal after sufficiently large dilation by `k`. For an alpha-stable kernel the source-critical exponent is `p=2+alpha`.

C020 completed the free-stable interior for all alpha. The remaining supported mathematical gap after C020 was deliberately recorded as follows: old C012 had asserted the arbitrary-alpha **classical** interior theorem using Gawronski's 1984 broad all-stable bell-shape claim, but later literature records a gap in that proof. C020 therefore refused to promote C012 until a replacement central-shape argument was found. This run supplies that replacement.

# 2. Three new-method moves

## Move #20 — FIND WHY THE ALGORITHM FAILS

The old C012 proof did not fail in its critical-tail estimate or in C008. It failed at one exact input: it treated Gawronski's 1984 statement "all classical stable densities are bell-shaped with simple derivative zeros" as available for every stability index. The proof of that broad statement contains an error. The correct replacement must provide only the weaker facts C008 actually needs: strict first-derivative signs, a nondegenerate mode, and eventual convexity of both tails.

## Move #21 — ASK WHO ELSE HAS THIS SHAPE

Mateusz Kwaśnicki, *A new class of bell-shaped functions*, arXiv:1710.11023, Trans. Amer. Math. Soc. 373 (2020), 2255--2280, explicitly explains the error in the 1984 proof and gives a correct theorem whose class includes **all stable density functions**. His definition is by sign changes: the `n`-th derivative changes sign exactly `n` times. It does **not** hand us the stronger "all zeros simple" assertion. The task is therefore to translate Kwaśnicki's sign-count information into exactly the C008 shape hypotheses.

## Move #3 — PROVE SOMETHING STRONGER

Instead of proving only a stable-density fact, I prove an abstract bridge: for an analytic bell-shaped density whose derivatives vanish at infinity, the first three bell-shape sign counts already force the C008 central/tail geometry. Applying the bridge to Kwaśnicki's stable densities repairs C012 for every `alpha != 1` and completes the classical branch together with C019.

# 3. Literature correction: what Kwaśnicki proves and what is not assumed

Kwaśnicki's paper states that a smooth function vanishing at both infinities is bell-shaped when its `n`-th derivative changes sign exactly `n` times for every `n`. The introduction explicitly says Gawronski's earlier all-stable proof contained an error and that this left an open problem for more than 30 years; the new result supplies a correct proof in a much larger class. The abstract and Corollary 1.3 identify all stable density functions as bell-shaped.

This matters because I do **not** infer that every derivative zero is simple. C021A below derives the weaker strictness/nondegeneracy facts needed by C008 using only:

- analyticity (to rule out zero intervals and infinite-order isolated degeneracy),
- `k^{(j)}(x) -> 0` as `x -> +/- infinity`, and
- the exact sign-change counts for `k'`, `k''`, and `k'''`.

Classical stable densities have the needed analyticity/smoothness in the two-sided interior, and in any event their derivatives of every order are bounded and vanish at infinity directly from Fourier inversion because the characteristic function has modulus `exp(-c|xi|^alpha)` and `|xi|^j exp(-c|xi|^alpha)` is integrable for every fixed `j`.

# 4. R19-I0084-C021A — bell shape implies the C008 shape geometry

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `k` be a nonzero real-analytic probability density on `R` such that

\[
k^{(j)}(x)\to0\qquad(x\to\pm\infty),\qquad j=0,1,2,3.
\tag{C021.1}
\]

Assume that, in the bell-shape sense, `k'` changes sign exactly once, `k''` changes sign exactly twice, and `k'''` changes sign exactly three times. Then there is a unique mode `m` such that

\[
k'(x)>0\ (x<m),\qquad k'(x)<0\ (x>m),
\tag{C021.2}
\]

and

\[
k''(m)<0.
\tag{C021.3}
\]

Moreover `k''(x)>0` for all sufficiently large `|x|`; hence both tails are eventually convex.

## Proof

Because `k>=0`, `k` is nonzero, and `k(x)->0` at both infinities, `k'` must be positive somewhere and negative somewhere. Since it changes sign exactly once, its sole sign transition is from `+` to `-`; denote the transition point by `m`.

### Step 1: no extra tangential zero of `k'`

Suppose first that `z<m` is an additional zero of `k'` at which `k'` does not change sign. On the left side of `m`, the sign of `k'` is nonnegative, and real analyticity implies that an isolated tangential zero has even finite multiplicity. Hence `z` is a strict local minimum of `k'`: `k''<0` immediately before `z` and `k''>0` immediately after `z` (after shrinking the neighborhood if needed).

On the other hand `k'(-infinity)=0` and `k'>0` somewhere before `z`. By the mean-value theorem there is a point still farther left where `k''>0`. Thus before and through `z`, `k''` already exhibits the sign pattern

\[
+\ ,\ -\ ,\ +.
\]

Since `k'>0` after `z` but `k'(m)=0`, another mean-value argument supplies a later point with `k''<0`. Therefore `k''` has sign samples

\[
+\ ,\ -\ ,\ +\ ,\ -
\]

in increasing order, forcing at least three sign changes. This contradicts the bell-shape count of exactly two. Thus `k'` has no tangential zero left of `m`. Reflection gives the same conclusion right of `m`.

Analyticity rules out a nontrivial zero interval of `k'`. Consequently (C021.2) holds strictly.

### Step 2: the two tails of `k''` are positive

For large positive `x`, (C021.2) gives `k'(x)<0` while (C021.1) gives `k'(x)->0`. The eventual sign of `k''` therefore cannot be negative: if `k''<=0` eventually, `k'` would be eventually nonincreasing below zero and could not converge upward to `0`. Since `k''` has only two sign changes, its eventual right-hand sign is positive.

Likewise on the far left, `k'(x)>0` and `k'(x)->0` as `x->-infinity`; moving from `-infinity` to the right, `k'` must initially increase, so the eventual far-left sign of `k''` is positive. Thus the two outer signs of `k''` are positive. Since `k''` changes sign exactly twice, its sign pattern is

\[
+\ ,\ -\ ,\ +.
\tag{C021.4}
\]

except at its isolated zeros. In particular `k''<=0` in the central region containing the mode.

### Step 3: the mode cannot be degenerate

It remains to exclude `k''(m)=0`. If that equality held, (C021.4) shows that `m` would be a tangential zero of `k''` inside its negative central sign region. Real analyticity makes this a finite even-order contact.

Now read the sign changes of `k'''`. Because `k''` tends to `0` at `-infinity` and becomes positive before its first `+ -> -` transition, the mean-value theorem gives a point on the far-left rise with `k'''>0`; crossing toward the negative central region gives a later point with `k'''<0`. Thus one `+ -> -` sign change of `k'''` is already forced on the left.

A tangential zero of `k''` at `m` inside the negative region is a local maximum at level zero, so immediately before `m`, `k'''>0`, while immediately after `m`, `k'''<0`. Starting from the negative `k'''` sign obtained after the left transition, this forces a second sign change to `+` before `m` and a third sign change back to `-` after `m`.

Finally, `k''` must rise from its negative central region to its positive right tail. The mean-value theorem supplies a later point with `k'''>0`, forcing a fourth sign change. Hence `k'''` would change sign at least four times, contradicting the bell-shape count of exactly three.

Therefore `k''(m) != 0`. Since `m` is a `+ -> -` mode and `k''` lies in the negative central sign region, (C021.3) follows. Continuity then gives `epsilon,c0>0` with

\[
k''(x)\le-c_0<0\qquad(|x-m|\le2\epsilon).
\tag{C021.5}
\]

Together with Step 2, this proves the lemma. QED.

# 5. R19-I0084-C021B — repaired all-alpha classical interior theorem

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let

\[
\alpha\in(0,1)\cup(1,2),
\]

and let `rho` be in the interior of the classical strictly stable admissible range in the Hasebe--Kuznetsov positivity convention:

\[
0<\rho<1\qquad(0<\alpha<1),
\tag{C021.6}
\]

or

\[
1-\alpha^{-1}<\rho<\alpha^{-1}\qquad(1<\alpha<2).
\tag{C021.7}
\]

Let `S_t` be the corresponding classical strictly alpha-stable process. If `mu` is any probability measure satisfying exactly the source condition

\[
M_{2+\alpha}:=\int_{\mathbb R}|y|^{2+\alpha}\,d\mu(y)<\infty,
\tag{C021.8}
\]

then

\[
\boxed{\mu*S_t\text{ is unimodal for all sufficiently large }t.}
\tag{C021.9}
\]

No compact-support hypothesis and no moment stronger than `2+alpha` is used.

## Proof

Let `k=k_{alpha,rho}` be the time-one classical stable density.

### 5.1 Central shape

Kwaśnicki's correct all-stable bell-shape theorem applies to `k`. Classical stable Fourier inversion gives smoothness, bounded derivatives and (C021.1). Therefore C021A applies: after translating its unique mode to zero,

\[
k'(x)>0\ (x<0),\qquad k'(x)<0\ (x>0),
\]

and there are `epsilon,c0>0` such that

\[
k''(x)\le-c_0<0\qquad(|x|\le2\epsilon).
\tag{C021.10}
\]

In addition `k` is convex on both sufficiently remote tails.

### 5.2 Two positive density tails in the interior

The standard classical stable tail asymptotic in the same `(alpha,rho)` normalization is

\[
k(x)\sim C_+x^{-1-\alpha},\qquad
k(-x)\sim C_-x^{-1-\alpha},
\qquad x\to+\infty,
\tag{C021.11}
\]

where

\[
C_+=\frac{\Gamma(1+\alpha)}{\pi}\sin(\pi\alpha\rho),
\qquad
C_-=\frac{\Gamma(1+\alpha)}{\pi}\sin(\pi\alpha(1-\rho)).
\tag{C021.12}
\]

Both constants are strictly positive exactly in the interior ranges (C021.6)--(C021.7). Hasebe--Kuznetsov record the common `(alpha,rho)` convention and the corresponding classical series machinery; the same leading tail formula is also standard in modern stable-distribution references.

### 5.3 Derivative-tail lower bounds without differentiating an asymptotic equivalence

By C021A, `k` is decreasing and convex on the far right. Hence for all sufficiently large `x`, convexity gives

\[
k'(x)\le\frac{k(2x)-k(x)}{x},
\]

and therefore

\[
-k'(x)\ge\frac{k(x)-k(2x)}{x}.
\tag{C021.13}
\]

Using (C021.11),

\[
\frac{k(x)-k(2x)}{x}
\sim
C_+\bigl(1-2^{-1-\alpha}\bigr)x^{-2-\alpha}.
\]

Thus there are `R,c_+>0` such that

\[
-k'(x)\ge c_+x^{-2-\alpha}\qquad(x\ge R).
\tag{C021.14}
\]

For the left tail apply the same argument to `g(x)=k(-x)`, which is eventually decreasing and convex for `x>0`. Since `-g'(x)=k'(-x)`,

\[
k'(-x)\ge\frac{k(-x)-k(-2x)}{x}
\ge c_-x^{-2-\alpha}
\qquad(x\ge R)
\tag{C021.15}
\]

for some `c_->0`.

This secant argument is useful because it does not differentiate the tail asymptotic and therefore avoids a hidden regularity exchange.

### 5.4 Apply the retained critical-tail theorem

All C008 hypotheses now hold with

\[
p=2+\alpha.
\]

Hence `mu*k_s` is unimodal whenever

\[
s^{2+\alpha}\ge C_{\alpha,\rho}M_{2+\alpha}.
\tag{C021.16}
\]

A strictly alpha-stable semigroup has spatial scale `s=t^{1/alpha}` up to its harmless location convention for `alpha != 1`. Therefore a sufficient time threshold has the source-critical scaling

\[
\boxed{
t\ge C'_{\alpha,\rho}
M_{2+\alpha}^{\alpha/(2+\alpha)}.}
\tag{C021.17}
\]

The constant is not claimed sharp. This proves (C021.9). QED.

# 6. Consequence — both frozen ordinary-* stable-law branches are now internally classified for every alpha

The classical branch can now be assembled without the defective Gawronski citation:

- C021B: every classical `alpha != 1` **interior** skewness is eventually unimodal for every input with the exact finite `(2+alpha)` moment;
- C019: every classical `alpha=1` nonendpoint skewness is eventually unimodal under the exact finite third moment;
- C011: every classical `alpha != 1` extremal endpoint admits one initial law with all polynomial moments for which ordinary convolution is nonunimodal for every time;
- C017: the exceptional classical `alpha=1` endpoints have the same all-moment, all-time obstruction.

The free branch was already completed internally by C018/C020 plus C011/C017. Consequently the frozen arXiv ordinary-`*` problem has the following **internal candidate classification, pending independent audit**:

\[
\boxed{
\begin{array}{c|c}
\text{stable-law skewness} & \text{ordinary }\mu*S_t\text{ under finite }(2+\alpha)\text{ moment}\\
\hline
\text{two-sided interior} & \text{TRUE eventually for every source-admissible }\mu\\
\text{extremal boundary} & \text{FALSE: one all-moments }\mu\text{ is nonunimodal for every }t>0
\end{array}}
\tag{C021.18}
\]

for both the classical-stable and free-stable-law branches and every `0<alpha<2`, with the standard logarithmic-centering convention at `alpha=1`.

This does **not** change the frozen metric `2/2`, which was already saturated at `alpha=1/2`, and it does not change the source-level verdict: Conjecture 5.5 as printed on arXiv is false because its quantifier includes extremal skewness. What changes is that the entire skewness/alpha phase diagram is now supported internally rather than leaving the classical arbitrary-alpha interior behind the 1984 proof gap.

# 7. What failed, and why the repair is genuinely different

The failed route was not "bell shape" itself; it was assuming a stronger historical proof than the literature supports. Kwaśnicki supplies the correct modern bell-shape theorem but only in a sign-change formulation. C021A is the missing bridge from that formulation to the quantitative geometry C008 uses.

The bridge is also stronger than this one application: it shows that, for analytic densities with derivative decay, one does not need simple zeros of every derivative to obtain a unique strict mode, negative curvature there, and convex tails. Bell-shape sign counts through order three suffice.

No finite-arithmetic claim was introduced in this run, so no checker was manufactured merely to produce activity. The validation is the theorem-sized analytic proof above plus source/literature checks.

# 8. Prior-art and source-status search — 2026-09-20

Fresh bounded searches/rechecks this run included:

- exact arXiv:1710.08240v2 Conjecture 5.5 and the literal `mu*S_t` line;
- `"A new class of bell-shaped functions" Kwasnicki stable distributions Corollary 1.3`;
- `"All stable distributions on R have bell-shaped density functions"`;
- the history of Gawronski's 1984 bell-shape proof and the later correction;
- `"On free stable distributions" Hasebe Kuznetsov classical rho stable density`;
- `Gamma(1+alpha) sin(pi alpha rho) stable density x^{-1-alpha}`;
- `"Conjecture 5.5" Hasebe Ueda stable unimodality` and later Hasebe/Ueda work.

Primary/current evidence located:

- Hasebe--Ueda arXiv v2, lines around Conjecture 5.5, literally uses ordinary `*` and exact `(2+alpha)` moment;
- Kwaśnicki arXiv:1710.11023 / Trans. AMS 2020 states that the old general proof contained an error and proves a class including all stable densities; its bell-shape definition is exact sign-change count, not an imported simple-zero assertion;
- Hasebe--Kuznetsov arXiv:1404.2981 gives the common stable `(alpha,rho)` framework and classical/free density series machinery;
- standard modern stable-distribution references give the two tail constants in (C021.12).

I did **not** locate a later primary theorem explicitly resolving the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5, nor a paper stating the C021A bridge/C021B classification in this form. That is bounded negative evidence only and is **not** claimed to certify novelty or priority.

Access limit: web/arXiv/public primary-source search plus repository citation graph; no exhaustive subscription citation database was available. The absence of a hit is therefore not treated as proof of novelty.

# 9. Audit / closure state

The fixed source metric remains

\[
\boxed{2/2\to2/2.}
\]

The mathematical source statement is already refuted, but repository closure remains **PARTIAL / AUDIT_PENDING** under the owner's closure protocol.

Located audit evidence includes:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF` for the retained critical-tail engine;
- historical R18/P26 PASSes for the later ALEA/free-`boxplus` formulation or narrower abstract pieces, which are **not** substitutes for the frozen arXiv ordinary-`*` package;
- no version-matching P26 end-to-end PASS for the frozen arXiv ordinary-`*` I0084 package located this run;
- no distinct OTHER-track version-matching end-to-end PASS for that same frozen package located this run.

Thus the frozen full-package audit gate remains unfilled. C021A/C021B themselves also need independent mathematical checking before external representation as established results.

No paper folder is created yet.

# 10. Next concrete attack

The highest-value verification target is now sharply local: independently reconstruct C021A from Kwaśnicki's exact sign-change definition, then check the secant-tail step and parameter signs in C021B. In parallel, a direct classical-stable Fourier/ODE proof of `k''(m)<0` would provide a methodologically independent cross-check rather than merely rereading the same bell-shape argument.

There is no currently known mathematical source-scope gap after C021 when combined with C011/C017/C018/C019/C020; what remains before repository closure is independent verification and the protocol-required frozen-package audits.

# 11. Model / scheduler truth

The owner requests GPT-6 with maximum reasoning. The exposed scheduler/control surface available to this worker still has task identity/title, prompt, schedule/timing mode, enabled state and ordinary update controls, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed full-hour duration field. GPT-6/maximum is therefore a prompt preference rather than a verified runtime setting here.

The historical P26 `"You cannot modify this task"` event is recorded as authorization-context-specific: later updates succeeded from an authorized context. The supported remedy is the owning/authorized context, ordinary permission/ownership repair or transfer, or platform support; never a bypass. No scheduler change was attempted in this R19 run.

# 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  frozen_convolution: "ordinary classical mu * S_t in both the classical-stable and free-stable-law branches"
  fixed_metric: "number of complete alpha=1/2 classical-stable/free-stable source cases proved in full input-measure class and original skewness convention"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO_MOVEMENT"
  structural_obligation_before: "general classical alpha != 1 interior theorem withheld because old C012 relied on the erroneous broad Gawronski bell-shape proof"
  structural_obligation_after: "REPAIRED INTERNALLY: C021A bridges Kwasnicki sign-change bell shape to C008 geometry; C021B proves exact-(2+alpha)-moment classical interior theorem for all alpha != 1"
  source_status: "REFUTED_MATHEMATICALLY"
  repository_status: "PARTIAL_AUDIT_PENDING"
  unchanged_count: "UNKNOWN; not reconstructed synthetically from commits"
  substantive_stagnation_this_run: 0
  tried_moves: [3, 20, 21]
  move_cycle_note: "all 30 moves exhausted historically; second-cycle reuse; preceding C020 triple was [7,18,23]"
  new_claims:
    - "R19-I0084-C021A: analytic bell-shape sign counts for k',k'',k''' plus derivative decay force strict first-derivative signs, k''(mode)<0, and eventual convexity of both tails"
    - "R19-I0084-C021B: every interior classical strictly alpha-stable kernel, alpha != 1, yields eventual ordinary-convolution unimodality for every mu with exactly finite (2+alpha)-moment"
    - "C011/C017/C018/C019/C020/C021 together internally classify both frozen ordinary-* branches for every alpha in (0,2): interior TRUE eventually, extremal boundary FALSE even for an all-moments witness"
  preserved_claims:
    - "C008 critical-tail smoothing theorem with R18 independent mathematical audit"
    - "C009 complete frozen alpha=1/2 classification and fixed metric 2/2"
    - "C011/C017 endpoint all-moment all-time counterexamples"
    - "C018/C020 free-stable interior all-alpha classification"
    - "C019 classical alpha=1 interior theorem"
  evidence:
    - "predecessor C020 creation commit a5f981dbbbc08675d24ca6af2560f88a9974d491"
    - "Mateusz Kwasnicki, A new class of bell-shaped functions, arXiv:1710.11023; Trans. AMS 373 (2020), 2255-2280"
    - "Hasebe-Kuznetsov, On free stable distributions, arXiv:1404.2981 / ECP 19 (2014), common (alpha,rho) conventions and stable series"
    - "Hasebe-Ueda arXiv:1710.08240v2 Conjecture 5.5 literal ordinary-* source"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_other: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    c021: "AUDIT_PENDING"
  remaining_obligation: "independent mathematical audit of C021A/C021B and protocol-required P26 plus distinct OTHER-track end-to-end audits of the frozen arXiv ordinary-* package before closure/paper packaging"
  next_attack: "independently reconstruct C021A from Kwasnicki's sign-change definition and seek a direct classical-stable curvature proof as a methodologically independent cross-check"
```
