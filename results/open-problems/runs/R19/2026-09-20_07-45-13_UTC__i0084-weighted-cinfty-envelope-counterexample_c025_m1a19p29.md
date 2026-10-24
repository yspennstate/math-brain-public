Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: the endpoint counterexample can be chosen in an arbitrarily thin prescribed weighted-C-infinity tail class, and the abstract one-sided-kernel compiler no longer needs a globally bounded kernel derivative. Section-B moves: #1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #29 ADD THE POINTS AT INFINITY. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C024 triple was #3/#15/#27, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY internally already at alpha=1/2 because the frozen source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C025A/B/C are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity, repository state, and exact frozen source

I resumed from the actual newest R19 report

`runs/R19/2026-09-20_06-40-46_UTC__i0084-ultralight-smooth-common-counterexample_c024_m3b15q27.md`

created at commit

`1162a36d749190b0e8500af3527c846c727774d1`.

I reread the required current repository state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, targeted I0084 history, and current neighboring Hasebe-Ueda/Hasebe-Ueda-Wang activity. The append-only intake corpus is too large for a useful byte-for-byte model-visible reread through this connector, so I do not pretend otherwise; targeted history identifies the canonical row in `probability_1000_intake_I_20260914/problems.jsonl`, and the exact repository delta supplies the continuity check.

An exact Git comparison from the C024 commit to the frozen pre-write head `b800cf1c906fc004c44199414449108334214c56` found **137 commits ahead, zero behind, `too_large=null`**. The complete changed-path response contained no later `runs/R19/` report and no root `QUEUE.md` or intake-JSONL mutation. I0084 therefore remains the current R19 assignment and C024 is the newest own theorem state to preserve. Posted additive Brownian/free-Brownian results remain excluded and earn no new fixed-metric credit.

The original arXiv-v2 source was reopened directly. Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\tag{1.1}
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\tag{1.2}
\]

The star is the ordinary classical convolution symbol in the frozen arXiv-v2 statement even when `S_t` is a free-stable law. I do **not** replace it by `\boxplus`.

For alpha=`1/2`, Section 5.2 gives the positive classical half-stable kernel

\[
L_t(dx)=\frac{t}{\sqrt{2\pi}}x^{-3/2}e^{-t^2/(2x)}\mathbf 1_{(0,\infty)}(x)\,dx,
\tag{1.3}
\]

and Proposition 5.4 gives the source's sparse atomic below-`5/2`-moment counterexample. The retained R19 chain C010/C011 and especially C024 already strengthens that to smooth ultra-light counterexamples. This run asks a sharper question:

> Can the bad initial density be forced below an **arbitrarily prescribed pointwise tail envelope, simultaneously for every derivative**, while keeping unbounded support and all-time nonunimodality?

The answer is yes.

# 2. The three new-method moves

## Move #1 — CHANGE THE CATEGORY

C024 phrased tail lightness through integrals such as

\[
\int G(|x|)g(x)\,dx<\infty.
\]

That is only a measure-theoretic category. I moved the problem into a weighted `C^\infty` function-space category: prescribe pointwise upper envelopes for `g,g',g'',...` at infinity and ask whether the support-boundary obstruction survives inside an arbitrarily small weighted smooth class.

It does. The obstruction is topological/geometric, not a failure of tail regularity.

## Move #19 — MAKE IT AN ALGORITHM

Instead of choosing the sparse weights qualitatively, I wrote a deterministic stage-by-stage compiler. At stage `n`, the next bump mass is chosen below a finite list of constraints:

1. all weighted-`C^\infty` envelope constraints with derivative order and envelope index at most `n`;
2. a summability cap;
3. a recursive derivative-tail budget that makes all later bumps negligible compared with the active `n`th bump.

Because every constraint is a strictly positive upper bound, the recursive choice never gets stuck.

## Move #29 — ADD THE POINTS AT INFINITY

The natural boundary object is not a moment exponent but the point `|x|=infinity`. I allow **any countable collection of strictly positive decreasing boundary envelopes** there. The construction can approach zero faster than every one of them and still fail eventual unimodality at every scale.

This isolates compact support as a genuinely singular boundary condition: an envelope that is identically zero beyond a finite point is not covered, while every positive tail envelope, however tiny, can be defeated.

# 3. R19-I0084-C025A — arbitrary weighted-C-infinity envelope compiler

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `k_r`, `r=1,2,...`, be a finite or countable family of probability densities on `R`. Assume only that for each `r`:

1. there is a finite `ell_r` such that
   \[
   k_r(x)=0\qquad(x<\ell_r);
   \tag{C025.1}
   \]
2. there are points
   \[
   \ell_r<u_r<v_r
   \tag{C025.2}
   \]
   and open neighborhoods of `u_r,v_r` on which `k_r` is `C^1`, with
   \[
   k_r'(u_r)>0,\qquad k_r'(v_r)<0.
   \tag{C025.3}
   \]

No boundedness assumption on `k_r'` over the whole right tail is needed.

For `s>0`, put

\[
k_{r,s}(x)=s^{-1}k_r(x/s).
\tag{C025.4}
\]

For every derivative order `d>=0` and every envelope index `m>=1`, let

\[
\eta_{d,m}:[0,\infty)\to(0,\infty)
\tag{C025.5}
\]

be an arbitrary finite-valued nonincreasing function.

Then there exists a **symmetric nonnegative `C^\infty` probability density `g` with unbounded support in both directions** such that:

### (i) Every prescribed pointwise smooth tail envelope holds

For every fixed pair `(d,m)` there is `R_{d,m}<\infty` such that

\[
\boxed{
|g^{(d)}(x)|\le \eta_{d,m}(|x|)
\qquad (|x|\ge R_{d,m}).
}
\tag{C025.6}
\]

### (ii) Every one-sided kernel at every scale remains nonunimodal

For every `r` and every `s>0`,

\[
\boxed{g*k_{r,s}\text{ is nonunimodal}.}
\tag{C025.7}
\]

By symmetry of `g`, the same statement holds for every reflected kernel. Any translation of a kernel merely translates the convolution and also preserves the conclusion.

This strictly strengthens C024A in two directions: it gives pointwise control of **all derivatives**, not merely countably many tail integrals, and it removes C024A's global right-tail boundedness assumption on `k_r'`.

# 4. Construction

Choose an even nonnegative bump

\[
\phi\in C_c^\infty((-1,1)),
\qquad
\int_{\mathbb R}\phi=1.
\tag{C025.8}
\]

Let

\[
C_d=\|\phi^{(d)}\|_\infty,
\qquad
A_n=(n+2)^2,
\qquad
\varepsilon_n=2^{-n-6}.
\tag{C025.9}
\]

For a center `a`, write

\[
\phi_{a,n}(x)=\varepsilon_n^{-1}\phi\!\left(\frac{x-a}{\varepsilon_n}\right).
\tag{C025.10}
\]

The supports around `\pm A_n` are pairwise disjoint and escape to infinity; moreover

\[
A_{n+1}-A_n=2n+5\longrightarrow\infty.
\tag{C025.11}
\]

Define

\[
\delta_n=2^{-n-4}.
\tag{C025.12}
\]

We now choose positive masses `a_n` recursively. Require

\[
a_n\le 2^{-n-4}
\tag{C025.13}
\]

and, for `n>=2`,

\[
a_n\varepsilon_n^{-2}\le \delta_{n-1}a_{n-1}.
\tag{C025.14}
\]

At stage `n` also impose the finite family of smooth-envelope inequalities

\[
\frac{a_n}{2}\,C_d\,\varepsilon_n^{-(d+1)}
\le
\eta_{d,m}(A_n+1),
\qquad 0\le d\le n,\quad1\le m\le n.
\tag{C025.15}
\]

There are only finitely many constraints at each stage and every right-hand side is strictly positive. Thus we may simply take `a_n` to be one half of the minimum of all applicable positive upper bounds. The construction is deterministic and never fails.

Set

\[
A:=\sum_{n\ge1}a_n.
\tag{C025.16}
\]

By (C025.13), `A<1`. Define

\[
\boxed{
 g(x)=(1-A)\phi(x)
 +\sum_{n\ge1}\frac{a_n}{2}
 \bigl[\phi_{A_n,n}(x)+\phi_{-A_n,n}(x)\bigr].
}
\tag{C025.17}
\]

The remote supports are locally finite, so the sum is `C^\infty`; it is even, nonnegative, integrates to one, and has unbounded support because every `a_n>0`.

# 5. Proof of the arbitrary derivative-envelope property

Fix `(d,m)`. For all

\[
n\ge N:=\max\{d,m\},
\tag{C025.18}
\]

inequality (C025.15) is present in the stage-`n` constraints.

On either support near `\pm A_n`, local finiteness and disjointness give

\[
|g^{(d)}(x)|
\le
\frac{a_n}{2}C_d\varepsilon_n^{-(d+1)}
\le
\eta_{d,m}(A_n+1).
\tag{C025.19}
\]

Since `|x|<=A_n+\varepsilon_n<A_n+1` there and `\eta_{d,m}` is nonincreasing,

\[
\eta_{d,m}(A_n+1)\le\eta_{d,m}(|x|).
\tag{C025.20}
\]

Outside those remote supports, `g^{(d)}` is exactly zero once `|x|` is beyond the compact central bump. Hence (C025.6) follows.

The conclusion is substantially stronger than Schwartz decay. For example, choosing the same envelope

\[
\eta_{d,1}(R)=e^{-e^R}
\tag{C025.21}
\]

for every `d` gives a bad density satisfying

\[
|g^{(d)}(x)|\le e^{-e^{|x|}}
\tag{C025.22}
\]

for all sufficiently large `|x|`, separately for every derivative order `d`. In particular `g` is Schwartz and

\[
\int e^{c|x|^q}g(x)\,dx<\infty
\qquad(c,q>0),
\tag{C025.23}
\]

recovering and strengthening the C024B tail conclusion.

More generally, because the family `\eta_{d,m}` is arbitrary and countable, one can force the derivatives below any prescribed countable menu of positive boundary profiles, no matter how rapidly those profiles tend to zero.

# 6. The recursive derivative-tail budget

The main improvement over C024 is that we no longer try to bound `k_r'` on the whole right tail.

Put

\[
b_n:=a_n\varepsilon_n^{-2}.
\tag{C025.24}
\]

From (C025.14),

\[
b_{n+1}\le\delta_n a_n.
\tag{C025.25}
\]

Also `\varepsilon_n<1`, so (C025.14) implies `a_{n+1}<a_n`; hence the masses decrease. Therefore, for every `j>n`,

\[
b_j\le\delta_{j-1}a_{j-1}\le\delta_{j-1}a_n.
\tag{C025.26}
\]

Consequently

\[
B_n:=\sum_{j>n}a_j\varepsilon_j^{-2}
\le a_n\sum_{k\ge n}\delta_k
=2\delta_n a_n,
\tag{C025.27}
\]

and so

\[
\boxed{\frac{B_n}{a_n}\longrightarrow0.}
\tag{C025.28}
\]

This is the exact replacement for C024's kernel-tail derivative bound.

Indeed, because `k_{r,s}` is a probability density,

\[
\left\|\frac{d}{dx}(\phi_{a,j}*k_{r,s})\right\|_\infty
=
\|\phi_{a,j}'*k_{r,s}\|_\infty
\le
\|\phi_{a,j}'\|_\infty\|k_{r,s}\|_1
=
C_1\varepsilon_j^{-2}.
\tag{C025.29}
\]

Thus the entire derivative contribution from all more-remote bumps is controlled purely from the **initial bump derivative**, uniformly over the kernel's far right tail.

For completeness, (C025.27) also implies that the remote part of `g'` has finite `L^1` norm: since `\varepsilon_j<1`,

\[
\sum_j a_j\varepsilon_j^{-1}
\le
\sum_j a_j\varepsilon_j^{-2}<\infty.
\tag{C025.30}
\]

Hence `g*k_{r,s}` is `C^1`, so the derivative-sign argument below is legitimate.

# 7. Active-bump derivative signs

Fix one kernel `r` and one scale `s>0`. Set

\[
d_r^+=k_r'(u_r)>0,
\qquad
d_r^-=-k_r'(v_r)>0.
\tag{C025.31}
\]

By local `C^1` regularity, choose `\theta_r>0` so that

\[
k_r'(z)\ge d_r^+/2
\quad\text{when }|z-u_r|\le\theta_r,
\tag{C025.32}
\]

and

\[
k_r'(z)\le-d_r^-/2
\quad\text{when }|z-v_r|\le\theta_r.
\tag{C025.33}
\]

Attach two test points to the negative bump centered at `-A_n`:

\[
x_{n,u}=-A_n+s u_r,
\qquad
x_{n,v}=-A_n+s v_r.
\tag{C025.34}
\]

For sufficiently large `n`:

1. `\varepsilon_n/s<\theta_r`;
2. the diverging gap (C025.11) is larger than `s(v_r-\ell_r)+1`;
3. the derivative-tail ratio in (C025.28) is as small as desired.

At either test point, every bump whose center lies to the **right** of `-A_n` contributes exactly zero. To see this, a bump centered at `c` has convolution support contained in

\[
[c-\varepsilon+s\ell_r,\infty),
\tag{C025.35}
\]

and the gap condition puts both test points strictly to the left of that support for all older negative bumps, all positive bumps, and the central bump. This is the hard one-sided-support mechanism from C024.

For the active `n`th negative bump, all arguments stay in the local `C^1` neighborhood of `u_r` or `v_r`. Therefore differentiation under the compact bump integral gives

\[
\frac{d}{dx}\left[rac{a_n}{2}\phi_{-A_n,n}*k_{r,s}\right](x_{n,u})
\ge
\frac{a_n}{4s^2}d_r^+,
\tag{C025.36}
\]

and

\[
\frac{d}{dx}\left[rac{a_n}{2}\phi_{-A_n,n}*k_{r,s}\right](x_{n,v})
\le
-\frac{a_n}{4s^2}d_r^-.
\tag{C025.37}
\]

The only possible contamination comes from the more-negative bumps with indices `j>n`. By (C025.29), its absolute derivative is at most

\[
\frac{C_1}{2}\sum_{j>n}a_j\varepsilon_j^{-2}
=
\frac{C_1}{2}B_n.
\tag{C025.38}
\]

Using (C025.28), for all sufficiently large `n` this is smaller than

\[
\frac{a_n}{8s^2}\min\{d_r^+,d_r^-\}.
\tag{C025.39}
\]

Combining (C025.36)--(C025.39) yields

\[
(g*k_{r,s})'(x_{n,u})>0,
\qquad
(g*k_{r,s})'(x_{n,v})<0.
\tag{C025.40}
\]

Thus **every sufficiently remote negative bump still creates a full local `+` then `-` derivative transition**, despite the density and every derivative being arbitrarily small there.

# 8. Why this forces nonunimodality at every scale

Because `A_{n+1}-A_n\to\infty`, for two consecutive sufficiently large indices we also have

\[
x_{n+1,u}<x_{n+1,v}<x_{n,u}<x_{n,v}.
\tag{C025.41}
\]

The derivative signs along the real line are therefore

\[
+,-,+,-.
\tag{C025.42}
\]

A `C^1` unimodal density is nondecreasing up to a mode and nonincreasing afterward. Its derivative cannot be negative and later become positive. Hence (C025.42) is impossible under unimodality.

The proof fixed arbitrary `r` and arbitrary `s>0`; therefore the same `g` defeats every kernel in the countable family at **every positive scale**.

Because `g` is symmetric,

\[
(g*\widetilde k_{r,s})(x)=(g*k_{r,s})(-x)
\tag{C025.43}
\]

for the reflected kernel `\widetilde k_r(x)=k_r(-x)`, so reflection is defeated too. This proves C025A.

# 9. R19-I0084-C025B — arbitrarily thin smooth tails still defeat all alpha=1/2 endpoints

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

C024B already verified the two positive endpoint kernels needed for the frozen alpha=`1/2` source case.

The classical unit-scale half-stable density is

\[
k_{\mathrm{cl}}(x)
=\frac1{\sqrt{2\pi}}x^{-3/2}e^{-1/(2x)}\mathbf1_{(0,\infty)}(x),
\tag{C025.44}
\]

with

\[
\frac{k_{\mathrm{cl}}'(x)}{k_{\mathrm{cl}}(x)}
=\frac{1-3x}{2x^2}.
\tag{C025.45}
\]

The positive free half-stable unit law has density

\[
k_{\mathrm{fr}}(x)
=\frac{\sqrt{4x-1}}{2\pi x^2}\mathbf1_{[1/4,\infty)}(x),
\tag{C025.46}
\]

with

\[
\frac{k_{\mathrm{fr}}'(x)}{k_{\mathrm{fr}}(x)}
=\frac{2(1-3x)}{x(4x-1)}.
\tag{C025.47}
\]

Both have their mode at `1/3`, so the common choices

\[
u=3/10,
\qquad
v=2/5
\tag{C025.48}
\]

satisfy the local hypotheses of C025A. Notice that C025A does **not** need the free kernel derivative to be bounded near its hard support edge `1/4`; only the neighborhoods of `u,v` are used.

Therefore, given **any** countable family of positive decreasing derivative envelopes `\eta_{d,m}`, there is one symmetric `C^\infty` initial density `g` satisfying all of them and such that, for every `t>0`,

\[
\boxed{g*L_t\text{ is nonunimodal},}
\tag{C025.49}
\]

and, writing `F_t` for the positive free half-stable law,

\[
\boxed{g*F_t\text{ is nonunimodal}.}
\tag{C025.50}
\]

Both stars in (C025.49)--(C025.50) are ordinary classical convolutions. Reflection plus symmetry of `g` gives the negative-skew endpoint laws for the **same** initial density.

A concrete striking choice is

\[
\eta_{d,1}(R)=e^{-e^R}
\qquad(d=0,1,2,\ldots).
\tag{C025.51}
\]

Then one single symmetric `C^\infty` probability density, with every derivative eventually bounded by the doubly-exponential envelope `e^{-e^{|x|}}`, still defeats all four alpha=`1/2` endpoint combinations (classical/free and positive/negative skewness) for every `t>0`.

Thus the frozen source fails at the extremal half-stable boundary even inside a class far smaller than the ordinary Schwartz class.

# 10. R19-I0084-C025C — what tail hypotheses can and cannot rescue the conjecture

**STATUS: COROLLARY OF C025A / AUDIT PENDING.**

Fix either positive alpha=`1/2` endpoint kernel, or the two-kernel classical/free family simultaneously. Consider any proposed sufficient hypothesis on the initial density that consists solely of a **countable collection of eventual pointwise upper bounds**

\[
|g^{(d)}(x)|\le\eta_{d,m}(|x|),
\tag{C025.52}
\]

where every envelope remains strictly positive at finite radius.

C025A constructs a counterexample satisfying every one of those bounds. Therefore no such purely countable tail-envelope criterion can, by itself, guarantee eventual unimodality for the endpoint kernels over the full class of input densities.

This statement deliberately does **not** cover:

- compact support, because the corresponding boundary envelope is exactly zero past a finite point;
- shape hypotheses such as initial unimodality, log-concavity, total positivity, or monotone hazard structure;
- uncountably many independent constraints not reducible to a countable family.

So the correct conceptual lesson is precise:

\[
\boxed{\text{arbitrarily strong positive tail decay and smoothness do not repair the endpoint failure.}}
\tag{C025.53}
\]

Any positive theorem at extremal skewness must use a genuinely structural condition, not merely stronger decay of an otherwise arbitrary initial density.

# 11. Relation to C024 and why this is not bookkeeping

C024 already showed that one smooth initial density may have every stretched-exponential moment while defeating all endpoint kernels. C025 proves a qualitatively stronger statement:

1. **integrated tail control -> pointwise `C^\infty` tail control:** every derivative may be prescribed to lie below an arbitrary positive envelope;
2. **kernel-tail regularity is removed:** future-bump contamination is bounded through `\phi' * k`, using only `\|k\|_1=1`, rather than through a global bound on `k'`;
3. **compact support is isolated as a singular boundary:** any positive envelope can be beaten, but an eventually zero envelope changes the geometry fundamentally.

The tracked source-case count is already saturated at `2/2`, so it cannot increase numerically. This is nevertheless genuine theorem movement rather than another audit/checker cycle.

# 12. Current literature / prior-art check, 2026-09-20

Fresh bounded searches were run for combinations of:

- `Schwartz density convolution nonunimodal one-sided stable kernel counterexample`;
- `eventual unimodality stable convolution smooth density counterexample`;
- `Conjecture 5.5 Hasebe Ueda stable unimodality`;
- `positive stable convolution nonunimodal smooth density`;
- `one-sided stable convolution unimodal counterexample`;
- `arbitrarily light tails unimodality convolution stable`;
- later Hasebe/Ueda papers and the free-stable shape literature.

The searches recovered:

1. Hasebe--Ueda, arXiv:1710.08240 / ALEA 15 (2018), the original source;
2. Hasebe--Simon--Wang, *Some properties of the free stable distributions*, AIHP 56 (2020), including the one-sided whale-shape result and the explicit positive free half-stable density;
3. later Hasebe--Ueda work on multiplicative unimodality and unrelated later additive/free convolution topics;
4. the classical strong-unimodality/log-concavity literature, which reinforces that shape structure is distinct from mere tail lightness.

I did **not** locate a later primary theorem that states C025A/B/C or resolves the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5 in this scope. This is bounded negative search evidence only, not a novelty or priority certificate. Search-engine coverage is not a substitute for a full citation-graph review.

The original source itself already contains nearby ideas that must be acknowledged: Proposition 5.4 uses sparse atoms for the positive classical half-stable kernel below the `5/2` threshold, and the same paper contains very-light-tail counterexample phenomena elsewhere for Brownian/free-Brownian questions. C025's specific new internal contribution is the **arbitrary pointwise derivative-envelope compiler for the one-sided stable support-boundary mechanism**, simultaneous across countably many kernels and scales.

# 13. Validation and checker policy

C025 introduces no finite enumeration or finite arithmetic claim. The validation object is the complete analytic proof above. I therefore did **not** manufacture a checker merely to create activity.

The two fragile points were checked explicitly on the page:

1. future-bump contamination uses the identity
   \[
   (\phi_{a,j}*k_{r,s})'=\phi_{a,j}'*k_{r,s}
   \]
   and the probability-density norm `\|k_{r,s}\|_1=1`, which removes any need for global control of `k_r'`;
2. the recursive inequality (C025.14) gives the quantitative tail ratio (C025.28), so later derivative contributions are `o(a_n)` uniformly enough for every fixed kernel and scale.

No unchecked finite certificate is being promoted.

# 14. Audit state

The version-matching full-package closure gate remains unfilled.

Relevant retained independent evidence includes:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the abstract smoothing/sufficiency engine;
- narrower R18 audits of C010 and earlier cores;
- a historical P26 PASS explicitly scoped to the later published ALEA free-`boxplus` formulation, not to the frozen arXiv ordinary-`*` package.

A fresh repository search this run still did **not** locate:

1. a P26 end-to-end PASS for the frozen arXiv-v2 ordinary-`*` I0084 package;
2. a distinct OTHER-track end-to-end PASS for that same frozen package.

C021--C025 also await theorem-level independent review. Therefore the honest repository status remains

`PARTIAL / AUDIT_PENDING`

even though the frozen source statement is internally mathematically refuted by the endpoint construction.

# 15. Model-control / scheduler limitation

The documented interface limitation remains unchanged. The exposed task controls provide prompt/title, timing/schedule, enabled state, and ordinary update controls, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort attestation, and no guaranteed full-hour execution field. GPT-6/maximum therefore remains a prompt request rather than an enforceable runtime setting here.

Making it enforceable would require the scheduler/product/API layer to expose persistent model and reasoning-effort fields and to return per-run attestation of what actually executed.

The historical P26 `You cannot modify this task` event remains documented as an authorization-context boundary. A later authorized context successfully updated P26, so the supported remedies are the owning/authorized context, supported permission/ownership repair or transfer, or platform support. There is no legitimate bypass. This worker made no scheduler or permission changes.

# 16. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  lane: CLOSABLE_OUTSIDE
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen arXiv v2: ordinary classical convolution mu*S_t for both classical-stable and free-stable kernel laws; original skewness conventions retained"
  fixed_metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO MOVEMENT"
  unchanged_count: "UNKNOWN for the saturated headline metric; do not infer from repeated 2/2"
  substantive_stagnation_this_run: 0
  status: "PARTIAL / AUDIT_PENDING; source statement REFUTED MATHEMATICALLY internally because extremal skewness is allowed"
  tried_moves: [1, 19, 29]
  previous_triple: [3, 15, 27]
  new_claims:
    - "C025A: for any countable one-sided probability-kernel family with only local C1 rise/fall points, and any countable family of positive decreasing pointwise envelopes for every derivative order, one symmetric C-infinity density lies eventually below every envelope yet makes every scaled kernel convolution nonunimodal; no global kernel-derivative bound is needed"
    - "C025B: the same construction applies simultaneously to classical and free alpha=1/2 positive endpoint laws under ordinary *, and by reflection to both negative endpoints; one may force every derivative to decay at least as fast as exp(-exp(|x|))"
    - "C025C: no countable sufficient criterion consisting solely of strictly-positive eventual pointwise upper envelopes on the initial density and its derivatives can rescue endpoint eventual unimodality over the full input class"
  evidence:
    - "arXiv:1710.08240v2 Conjecture 5.5: literal ordinary mu*S_t conclusion after allowing classical or free alpha-stable S_t"
    - "arXiv:1710.08240v2 Section 5.2 / Proposition 5.4: positive classical half-stable source kernel and original sparse-atom obstruction"
    - "Hasebe-Simon-Wang, AIHP 56 (2020): one-sided free stable shape and explicit free alpha=1/2 density"
    - "latest own report C024 at 1162a36d749190b0e8500af3527c846c727774d1 preserved"
    - "exact C024-to-prewrite-head comparison: 137 commits ahead, 0 behind, too_large=null; no later R19 report or root QUEUE/intake mutation in changed paths"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_second: "NOT_LOCATED / distinct end-to-end gate unfilled"
    c025: "SELF-PROOF ONLY / INDEPENDENT AUDIT PENDING"
  remaining_obligation:
    - "independent theorem-level audit of C021--C025, especially C025's derivative-tail compiler and frozen ordinary-* convention"
    - "P26 frozen-arXiv ordinary-* end-to-end PASS"
    - "one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS"
  posted_exclusions:
    - "posted additive Brownian/free-Brownian unimodality work earns no new credit"
    - "known stable special cases earn no new fixed-metric credit"
  model_runtime: "GPT-5.6 Sol; reasoning UNVERIFIED; not GPT-6 maximum"
```

# 17. Bottom line

The fixed source-case metric cannot move beyond `2/2`, but the endpoint obstruction has now crossed another qualitative boundary. It is not merely compatible with every polynomial moment, not merely with every stretched-exponential moment, and not merely with a smooth density. For the one-sided half-stable kernels it survives inside **any prescribed countable positive weighted-`C^\infty` tail envelope class**.

The remaining work is verification, not another missing mathematical source case: independent theorem-level audit of the newer C021--C025 chain and the two required end-to-end frozen-arXiv ordinary-`*` audits before repository closure may be claimed.
