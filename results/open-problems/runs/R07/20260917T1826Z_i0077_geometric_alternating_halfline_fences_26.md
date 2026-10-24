Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `25 -> 26` genuinely distinct nonparabolic shape families; Section-B moves actually tried: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958v4), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 26: geometric alternating one-sided parabolic fences

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and baseline

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T1721Z_i0077_additive_alternating_halfline_fences_25.md`,

which moved the metric `24 -> 25` and explicitly left **multiplicatively lacunary sign switches** outside its unit-increment proof. Its Section-B triple was `#10,#26,#30`; the present triple is different.

All thirty Section-B moves have already appeared somewhere in the preceding I0077 chain, so the literal requirement to use three moves never previously tried on this problem is exhausted. I do not invent a false history. This run uses a new combination and a genuinely new application of `#2,#18,#24`.

Before new mathematics I recovered current `master` evidence from campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/I0077.md`, the complete `runs/R07/` directory through run 25, and targeted current neighboring/ownership searches. The old R07 KPZ/FPP files remain preserved and retired, not deleted. The latest visible C29 Brownian-shapes rotation report explicitly excludes I0077 because R07 owns it and cites R07 run 25 as the active chain. R15 has long since handed off distinct Problem 7.2/I0076 and is working other sources; no I0077 collision was found.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no 7.8 exclusion. The canonical I0077 claim still literally says `PENDING_ADMISSION, not READY`, while the current owner task explicitly assigns this exact target to R07. I preserve that shared-root status rather than fabricating READY. The compact root `RESULTS.md` R07/FPP row is stale by its own warning and is not the mathematical baseline.

The large intake JSONLs and repository cannot be rendered literally byte-for-byte through the connector without truncation. I therefore record the access limitation honestly: exact I0077/source wording, ownership, posted exclusions, queue state, the full own-track directory, current neighboring ownership, and targeted intake/attempt evidence were recovered; I do not claim a byte-for-byte reread of every intake row.

Entering metric: `25`.

## 2. Source benchmark rechecked

I reopened the primary-source PDF and rechecked Definitions 2.1–2.2, Theorem 4.3, Proposition 4.4, and the open-problem page.

Definition 2.1 says that an FBM `X` has witness times `S_j -> -infinity` such that, for every fixed witness index `j`,

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces; the i.i.d. version is strongly decomposable.

Theorem 4.3 is the parabolic benchmark in terms of the principal killed-Ornstein–Uhlenbeck exponent `lambda_0(c_1,c_2)`:

1. `lambda_0>=1` gives the universal far-past normalized obstruction for every FBM;
2. `lambda_0<=1` gives a decomposable FBM with the corresponding asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0<1`, a decomposable FBM can be pointwise confined to the static parabola for every negative time.

Proposition 4.4 is especially useful here: for every `epsilon>0` there exists a **strongly decomposable** FBM satisfying

\[
\inf_{t<0}\frac{X_t}{\sqrt{|t|}}\ge1-\epsilon\quad\text{a.s.}
\tag{2.1}
\]

Reflection gives the analogous all-time lower half-line process.

Problem 7.8 is exactly the one-line request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy question is Problem 7.9 and is not part of I0077.

## 3. Fresh prior-art/status pass — 2026-09-17

Fresh bounded searches covered exact `Forward Brownian Motion` / `Problem 7.8` / `other space-time shapes` queries, later-author/citing variants, and persistence for sampled OU / Gaussian AR(1) chains with both positive and negative autoregressive coefficients.

The nearest methodological prior art is substantial and is not claimed as new:

- F. Aurzada and M. Kettner, *Persistence exponents via perturbation theory: AR(1)-processes*, J. Stat. Phys. 177 (2019), 651–665, arXiv:1810.09861, treats AR(1) with `rho in R` and persistence on a half-line;
- F. Aurzada, S. Mukherjee and O. Zeitouni, *Persistence exponents in Markov chains*, AIHP 57 (2021), 1411–1441, studies persistence exponents for Markov chains including AR processes and their parameter dependence;
- the discretely sampled stationary-Gaussian/OU persistence literature already treats sampling effects as a classical subject.

I found no later paper in this bounded dated search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the FBM geometric alternating-fence theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The AR(1) anti-persistence mechanism itself is classical.

## 4. New shape family: geometric one-sided sign fences

Fix `P>0`, `a>0`, geometric scales

\[
u_k=e^{kP},\qquad k\in\mathbb N_0,
\tag{4.1}
\]

and a deterministic sign word `sigma_k in {-1,+1}`. At negative time `-u_k`, impose the one-sided parabolic fence

\[
\boxed{\sigma_k X_{-u_k}\ge a\sqrt{u_k}.}
\tag{4.2}
\]

Thus each individual gate is an unbounded half-line. The special alternating profile is `sigma_k=(-1)^k`.

For a sign word, let

\[
N_{\rm sw}(m,n)
:=\#\{k\in\{m,\ldots,n-1\}:\sigma_{k+1}=-\sigma_k\}.
\tag{4.3}
\]

Assume a uniform lower switch-density condition: for some `delta>0`, `C_sigma<infinity`, and `k_sigma`,

\[
\boxed{
N_{\rm sw}(m,n)\ge\delta(n-m)-C_\sigma
\quad\text{for every }n>m\ge k_\sigma.
}
\tag{4.4}
\]

Alternation has `delta=1,C_sigma=0`.

Put

\[
r=e^{-P/2},\qquad s=\sqrt{1-r^2},
\tag{4.5}
\]

and define the one-switch cost

\[
q_{\rm alt}(a,P)
:=\overline\Phi\!\left(\frac{a(1+r)}{s}\right),
\tag{4.6}
\]

where `bar Phi(z)=P(Z>=z)` for `Z~N(0,1)`. Define

\[
\boxed{
\kappa_{\rm alt}(a,P,\delta)
:=\frac{\delta}{P}\bigl[-\log q_{\rm alt}(a,P)\bigr].
}
\tag{4.7}
\]

## 5. The three methods

### #2 ATTACK THE NEGATION FIRST

Run 25 left open the possibility that geometric spacing might make alternating individually favorable half-line gates feasible: its obstruction needed a sign switch over one **unit physical-time** interval at a scale comparable with the witness terminal, which geometric gates do not provide.

I attacked that proposed extension directly. It is false. For a large explicit region of `(a,P,delta)`, geometric alternating half-line gates are universally impossible even though either fixed orientation is individually feasible by Proposition 4.4 when `a<1`.

This falsifies a proposed extension mechanism, not the source's open-ended Problem 7.8.

### #18 SAY IT IN ANOTHER LANGUAGE

Lamperti normalization converts geometric Brownian samples into sampled stationary OU, i.e. a Gaussian AR(1) chain. Multiplying by the alternating sign turns its **positive** correlation coefficient `r` into the **negative** coefficient `-r`. The moving-shape problem becomes a half-line persistence problem for a negatively correlated AR(1) chain.

### #24 FIND THE EXTREMAL OBJECT

At a sign switch, conditioned on the current normalized value `x>=a`, the next opposite-oriented normalized value has mean `-rx`. Its chance to remain above `a` is maximized at the extremal boundary point `x=a`, not deep inside the allowed half-line. That gives an explicit one-step factor `q_alt` and avoids any numerical spectral problem.

## 6. Sampled-OU / negative-AR lemma

Let `B` be standard Brownian motion and

\[
Y_k=e^{-kP/2}B_{e^{kP}}.
\tag{6.1}
\]

Then `(Y_k)` is stationary Gaussian AR(1):

\[
Y_{k+1}=rY_k+s\xi_{k+1},
\qquad \xi_{k+1}\stackrel{\rm iid}{\sim}N(0,1).
\tag{6.2}
\]

Suppose the sign switches from `sigma_k` to `sigma_{k+1}=-sigma_k`, and the current gate holds. Writing `x=sigma_kY_k>=b>0`,

\[
\sigma_{k+1}Y_{k+1}
=-rx+s\eta_{k+1},
\tag{6.3}
\]

with `eta_{k+1}~N(0,1)` independent of the past. Hence

\[
\begin{aligned}
\mathbb P(\sigma_{k+1}Y_{k+1}\ge b\mid\mathcal F_k)
&=\overline\Phi\!\left(\frac{b+rx}{s}\right)\\
&\le\overline\Phi\!\left(\frac{b(1+r)}s\right)
=q_{\rm alt}(b,P).
\end{aligned}
\tag{6.4}
\]

At a non-switch step we simply bound the conditional success probability by one. Iterating the Markov property gives, for every `n>m`,

\[
\boxed{
\mathbb P\{\sigma_kY_k\ge b\ \forall k=m,\ldots,n\}
\le q_{\rm alt}(b,P)^{N_{\rm sw}(m,n)}.
}
\tag{6.5}
\]

Under (4.4), this is at most a constant times

\[
\exp\{-\delta(n-m)[-\log q_{\rm alt}(b,P)]\}.
\tag{6.6}
\]

For strict alternation, defining `Z_k=(-1)^kY_k` makes (6.2) literally the negative-correlation AR(1) recursion

\[
Z_{k+1}=-rZ_k+s\widetilde\xi_{k+1}.
\tag{6.7}
\]

## 7. Theorem I0077-R07-T27 — geometric sign-fence obstruction

Assume (4.4). If

\[
\boxed{\kappa_{\rm alt}(a,P,\delta)>1,}
\tag{T27-cond}
\]

then for **every** FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists K<\infty:\
\sigma_kX_{-e^{kP}}\ge ae^{kP/2}
\quad\forall k\ge K
\right)=0.
}
\tag{T27}
\]

When `sigma_k` is eventually constant and `0<a<1`, the opposite phenomenon occurs: Proposition 4.4 (or its reflection) gives a strongly decomposable FBM satisfying the eventual fences, indeed satisfying the corresponding one-sided parabolic inequality for **every** negative time.

Thus geometric sparsity alone does not make branch switching harmless. The relevant cost is the switch density in logarithmic index multiplied by the negative-AR one-switch persistence cost.

## 8. Proof of T27: arbitrary real Brownian terminals

The finite sampled-chain estimate (6.5) is not enough by itself because an FBM witness terminal is random and need not lie on an integer or geometric grid. The next lemma upgrades it to arbitrary real terminals without conditioning on the terminal.

Because the inequality in (T27-cond) is strict and `q_alt(b,P)` depends continuously on `b`, choose

\[
0<a_2<a_1<a
\tag{8.1}
\]

so close to `a` that

\[
\kappa_2
:=\frac\delta P[-\log q_{\rm alt}(a_2,P)]>1.
\tag{8.2}
\]

Let `W` be standard Brownian motion. For a fixed deterministic gate index `K_0`, call `T` **good** if

\[
\sigma'_k\bigl(W_T-W_{T-e^{kP}}\bigr)
\ge a_1e^{kP/2}
\tag{8.3}
\]

for every `k>=K_0` with `e^{kP}<=T`, where `sigma'_k` is any fixed sign word having the same switches as `sigma_k` (in the FBM application it will be `-sigma_k`).

For integer `n>=3`, define the unit modulus

\[
M_n:=\sup\{|W_t-W_s|:0\le s,t\le n+1,\ |t-s|\le1\}.
\tag{8.4}
\]

If `M_n>x`, then for some integer block of length two the Brownian oscillation from one endpoint exceeds `x/2`. Reflection, a Gaussian Chernoff bound, and a union bound give

\[
\mathbb P(M_n>x)\le4(n+1)e^{-x^2/16}.
\tag{8.5}
\]

Hence, with `x_n=16\sqrt{\log n}`,

\[
\sum_n\mathbb P(M_n>x_n)<\infty.
\tag{8.6}
\]

Choose

\[
C_0>\left(\frac{32}{a_1-a_2}\right)^2
\tag{8.7}
\]

and let `m_n` be the least integer with

\[
R_n:=e^{m_nP}\ge C_0\log n.
\tag{8.8}
\]

Then `R_n<=e^PC_0\log n`.

Suppose `T in [n,n+1]` is good and `M_n<=x_n`. For any geometric lag `u=e^{kP}` with `R_n<=u<=n`,

\[
\begin{aligned}
\sigma'_k(W_n-W_{n-u})
&\ge \sigma'_k(W_T-W_{T-u})-2M_n\\
&\ge a_1\sqrt u-32\sqrt{\log n}\\
&\ge a_2\sqrt u.
\end{aligned}
\tag{8.9}
\]

By Brownian time reversal, `(W_n-W_{n-u})_{0<=u<=n}` is standard Brownian motion in the variable `u`. Normalize it at the geometric lags. If

\[
K_n=\left\lfloor\frac{\log n}{P}\right\rfloor,
\tag{8.10}
\]

then (6.5), (4.4), and elementary floor/ceiling bounds imply

\[
\begin{aligned}
\mathbb P\{(8.9)\text{ holds for all }k=m_n,\ldots,K_n\}
&\le C_1q_{\rm alt}(a_2,P)^{\delta(K_n-m_n)}\\
&\le C_2\left(\frac n{R_n}\right)^{-\kappa_2}.
\end{aligned}
\tag{8.11}
\]

The constants absorb `C_sigma` and at most two endpoint indices. Because `R_n=O(\log n)` and `kappa_2>1`,

\[
\sum_n\left(rac n{R_n}\right)^{-\kappa_2}<\infty.
\tag{8.12}
\]

Combining (8.6)–(8.12),

\[
\sum_n
\mathbb P\{\exists\text{ good }T\in[n,n+1]\}<\infty.
\tag{8.13}
\]

Therefore Borel–Cantelli yields

\[
\boxed{
\mathbb P\{\exists\text{ good }T\ge A\}\longrightarrow0
\quad(A\to\infty).
}
\tag{8.14}
\]

This is a path-only Brownian statement about arbitrary real terminals.

## 9. Proof of T27: transfer to an arbitrary FBM

Suppose T27 fails for some FBM `X`. By a countable union over a deterministic eventual gate index and a deterministic bound on `|X_0|`, there are `K,M<infinity` and `q_0>0` such that

\[
E=\left\{|X_0|\le M,\ 
\sigma_kX_{-e^{kP}}\ge ae^{kP/2}\ \forall k\ge K\right\}
\tag{9.1}
\]

has probability at least `q_0`.

Increase `K` so that

\[
M\le(a-a_1)e^{kP/2}\qquad(k\ge K).
\tag{9.2}
\]

On `E`,

\[
(-\sigma_k)(X_0-X_{-e^{kP}})
=\sigma_kX_{-e^{kP}}-\sigma_kX_0
\ge a_1e^{kP/2}.
\tag{9.3}
\]

Let `S_j->-infinity` be an FBM witness sequence, put `T_j=-S_j`, and for each fixed deterministic witness index `j` let

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0.
\tag{9.4}
\]

`W_j` is standard Brownian motion. Whenever `e^{kP}<=T_j`,

\[
W_j(T_j)-W_j(T_j-e^{kP})=X_0-X_{-e^{kP}}.
\tag{9.5}
\]

Thus on `E`, every sufficiently large `T_j` is a good terminal for the fixed sign word `sigma'_k=-sigma_k`.

Choose deterministic `A` so large that the Brownian probability in (8.14) is `<q_0/2`. Since `T_j->infinity` almost surely along the witness sequence, choose a **deterministic witness index** `j` such that

\[
\mathbb P(T_j<A)<q_0/2.
\tag{9.6}
\]

Then (9.3)–(9.5) imply

\[
\mathbb P\{W_j\text{ has a good terminal }T\ge A\}
\ge q_0-\mathbb P(T_j<A)>q_0/2,
\tag{9.7}
\]

contradicting (8.14). No conditioning on the random witness time and no independence between a witness time and its Brownian witness path is used. This proves T27. `square`

## 10. Exact canonical example: alternating gates at powers of four

Take

\[
P=\log4,\qquad a=\frac34,\qquad \sigma_k=(-1)^k.
\tag{10.1}
\]

Then

\[
r=\frac12,\qquad s^2=\frac34,
\tag{10.2}
\]

and the one-switch normal threshold is

\[
z=\frac{a(1+r)}s=\frac{3\sqrt3}{4},
\qquad
\frac{z^2}{2}=\frac{27}{32}.
\tag{10.3}
\]

Mills' inequality gives

\[
q_{\rm alt}\le\frac{e^{-27/32}}{z\sqrt{2\pi}}.
\tag{10.4}
\]

Both factors are bounded exactly, without decimal numerics. First,

\[
e^{27/32}
>1+\frac{27}{32}+\frac12\left(\frac{27}{32}\right)^2
=\frac{4505}{2048}>2,
\tag{10.5}
\]

so `e^{-27/32}<1/2`. Second, using `pi>3`,

\[
(z\sqrt{2\pi})^2
=\frac{27}{16}\,2\pi
>\frac{81}{8}>4,
\tag{10.6}
\]

so `z sqrt(2 pi)>2`. Therefore

\[
\boxed{q_{\rm alt}<\frac14=e^{-P}},
\qquad
\boxed{\kappa_{\rm alt}>1}.
\tag{10.7}
\]

T27 yields the explicit theorem

\[
\boxed{
\mathbb P\left(
\exists K:\ (-1)^kX_{-4^k}\ge\frac34\,2^k
\quad\forall k\ge K
\right)=0
}
\tag{10.8}
\]

for every FBM.

Yet either frozen orientation is individually feasible for **all** negative times. Choose `epsilon<1/4` in Proposition 4.4 to obtain a strongly decomposable FBM with

\[
X_t\ge(1-\epsilon)\sqrt{|t|}>\frac34\sqrt{|t|}\qquad(t<0),
\tag{10.9}
\]

and reflect it for the opposite orientation. Thus the obstruction is not the individual half-line: it is the repeated geometric branch reversal.

This is the promised negation-first counterexample to the naive extension “geometrically sparse alternation of individually source-feasible one-sided parabolic gates should remain feasible.”

## 11. Positive-width space-time thickening (same metric family)

The discrete gates can be thickened without changing the obstruction. Around each logarithmic gate center `kP`, choose a disjoint interval

\[
G_k=(kP-\varepsilon_k,kP+\varepsilon_k),
\qquad \sum_k\varepsilon_k<\infty.
\tag{11.1}
\]

Inside `G_k`, let the allowed normalized slice be the half-line

\[
\{y:\sigma_ky\ge h_k(r)\},
\tag{11.2}
\]

where `h_k(kP)=a` and `h_k(r)->-infinity` as `r` approaches either edge of `G_k`; outside all gate intervals allow all of `R`. For example one may take

\[
h_k(r)=a-\frac{(r-kP)^2}{\varepsilon_k^2-(r-kP)^2}
\quad (r\in G_k).
\tag{11.3}
\]

The half-line then opens continuously to all finite spatial values at each gate edge. Any eventual confinement in this thickened deterministic space-time shape implies the center constraints (4.2), so T27 still forbids it whenever (T27-cond) holds. The total constrained logarithmic time `2 sum epsilon_k` can be made arbitrarily small.

This thickening is part of the **same** family and is not counted as another metric point.

## 12. Why this is a genuinely new metric family

The frozen equivalence convention does not collapse T27 into a preceding result.

- Run 24/T25 also used geometric scales, but every gate was a **bounded centered interval** and the obstruction was survival of a positive-correlation sampled OU chain inside that interval, expressed through an operator norm.
- Run 25/T26 also used alternating **unbounded half-lines**, but at additive physical times `n`, with `(n+1)/n->1`; its proof forced an order-`sqrt(n)` displacement over one physical-time unit.
- T27 has geometric scales with fixed ratio `e^P>1` **and** alternating unbounded half-lines. After Lamperti plus sign flip it becomes a negative-correlation AR(1) persistence problem. No Brownian rescaling or reflection converts bounded slices into half-lines or additive spacing into fixed-ratio geometric spacing.
- Earlier one-sided periodic barriers keep one half-line orientation; earlier moving bounded windows use a different cross-section topology and persistence mechanism.

Therefore this is not a new parameter inside a previous structural family. The frozen metric moves

\[
\boxed{25\longrightarrow26}.
\]

`unchanged_count = 0`.

## 13. Exact self-check

The finite rational core of the canonical example was executed before archiving.

Source:

`artifacts/R07/20260917T1826Z_geometric_alternation_constants.py`

creation commit `1f547000a9b8c267ecd6d9a145e155356e367cd3`.

Executed output:

`artifacts/R07/20260917T1826Z_geometric_alternation_constants.out`

creation commit `5dc59c122d802ffd03ab0c3fb88adbece9869382`.

The output ends `PASS` and exactly checks

\[
s^2=\frac34,\quad z^2=\frac{27}{16},\quad
\frac{z^2}{2}=\frac{27}{32},\quad
\frac{4505}{2048}>2,\quad
\frac{81}{8}>4.
\]

The analytic inputs Mills' inequality, `e^x>1+x+x^2/2` for `x>0`, and `pi>3` are proved/standard on the page. This is a **self-check**, not an independent audit.

## 14. Status, remaining obligations, and next research route

Theorem T27 is complete on the page in its stated sufficient-obstruction scope, including arbitrary real terminal times and the FBM witness transfer. It does not claim a sharp converse for arbitrary geometric sign words.

Problem 7.8 remains **PARTIAL**, not PROVED/closed. T27 still needs the protocol's required P26 end-to-end audit and a second independent OTHER-track audit before it can be treated as closure-grade. No paper package is created in this run.

The strongest next mathematical question is the complementary **low switch-cost regime**

\[
\kappa_{\rm alt}(a,P,\delta)\le1,
\]

especially strict alternation with `a<1`: can one build a decomposable FBM that follows the geometric branch reversals, or is the explicit one-step bound non-sharp for FBM existence? That would be genuinely new research rather than another checker on T27.

Suggested next Section-B combination (all individual moves have prior history, so this is a new combination rather than falsely “never used”): `#3 PROVE SOMETHING STRONGER`, `#11 DUALIZE`, `#28 REPLACE FOR ALL WITH TYPICAL`.

## 15. Structured ledger_delta for the authorized shared-root maintainer

```text
track: R07
allocation: CLOSABLE OUTSIDE
source: Burdzy-Scheutzow Forward Brownian Motion, Problem 7.8 / I0077
claim_owner: R07
claim_shared_status: PENDING_ADMISSION, not READY (preserved)
frozen_metric: number of genuinely distinct nonparabolic shape families with complete source-appropriate theorem
metric_before: 25
metric_after: 26
movement: +1
new_family: geometric one-sided sign fences with positive log-index switch density
new_theorem: I0077-R07-T27
canonical_example: P=log 4, a=3/4, sigma_k=(-1)^k; no FBM can satisfy (-1)^k X_{-4^k} >= (3/4)2^k eventually
self_check: PASS
artifact_source_commit: 1f547000a9b8c267ecd6d9a145e155356e367cd3
artifact_output_commit: 5dc59c122d802ffd03ab0c3fb88adbece9869382
source_status: PARTIAL
unchanged_count: 0
closure_audits_for_T27: 0/2
publication_novelty: UNVERIFIED (bounded negative search only)
old_R07_KPZ_route: RETIRED / preserved
shared_roots_modified_by_R07: none
```

## 16. Model / scheduler-control status

GPT-6 maximum was requested in prompt text, but the actual reportable runtime is **GPT-5.6 Sol with reasoning level UNVERIFIED**. I do not claim GPT-6 maximum.

The task-control surface exposed to this runtime still provides prompt/title, schedule, enablement and timing-mode fields, but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. Thus GPT-6/maximum remains prompt-only; enforcing it requires product/backend or an authorized owning/admin surface that exposes and verifies those controls.

The historical P26 `You cannot modify this task` event was authorization-context-specific: the current repository deployment record says P26 was later successfully updated from another authorized context. The legitimate workaround is the authorized owning context or platform support, not a worker-level bypass or duplicate task. No scheduler modification was attempted in this run.
