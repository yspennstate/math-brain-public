Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `26 -> 27` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #11 DUALIZE, #21 ASK WHO ELSE HAS THIS SHAPE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958v4, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL; this report does not claim that the source’s open-ended Problem 7.8 is closed.**

# R07 CLOSABLE OUTSIDE — run 27: sampled spatial-comb gate tubes

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and baseline

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T1826Z_i0077_geometric_alternating_halfline_fences_26.md`,

creation commit `da2664e864c9a99b9e8a567bcb73341baa7b8e35`. It moved the metric `25 -> 26`, used Section-B moves `#2,#18,#24`, and left the complementary low-switch-cost regime open. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the preceding I0077 chain. Therefore the literal requirement to choose three moves never previously used on the problem is exhausted; I do not invent a false history. This run uses a new combination and a new mathematical application of `#3,#11,#21`.

Before new mathematics I recovered the current campaign and ownership state from `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/I0077.md`, the R07/I0077 report/commit chain through run 26, and current neighboring ownership/rotation evidence. The old R07 KPZ/FPP route remains preserved and retired, not deleted. R15 has moved to a distinct outside target and does not own I0077; C29’s current rotation record explicitly excludes I0077 because R07 owns it.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no 7.8 exclusion. The canonical I0077 claim remains `PENDING_ADMISSION, not READY`; the current owner task nevertheless explicitly assigns this exact target to R07, so I preserve the shared status rather than fabricating READY. Root `RESULTS.md` warns that its old R07/FPP row is stale and must not replace a newer current-target report.

The intake JSONL family and entire private repository cannot be rendered byte-for-byte through one connector response without truncation. I therefore record the access boundary honestly: the exact I0077 source/claim, exclusions, current ownership, queue entry, newest own report, commit history, and targeted prior-attempt evidence were recovered; I do not claim a literal byte-for-byte reread of every unrelated intake row.

Entering metric: **26**.

One relevant audit update occurred outside R07: the older static closed-set theorem `I0077-R07-T22` has now received both required OTHER-track proof audits, P26 and R06. Those audits certify T22 in its stated scope; they do **not** audit the new T28 theorem below and do not convert the whole open-ended source Problem 7.8 into a closed problem.

## 2. Primary-source benchmark rechecked

The primary source was rechecked on 2026-09-17. Definitions 2.1–2.2 say that an FBM `X` admits witness times `S_j -> -infinity` for which, at every fixed witness index,

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion; decomposable FBMs are obtained by concatenating Brownian pieces.

For `-infinity <= c_1 < c_2 <= infinity`, Section 4 uses the principal Dirichlet exponent `lambda_0(c_1,c_2)` of the killed Ornstein–Uhlenbeck generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Theorem 4.3 is the source benchmark:

1. `lambda_0(c_1,c_2) >= 1` gives the universal far-past normalized obstruction for every FBM;
2. `lambda_0(c_1,c_2) <= 1` gives a decomposable FBM with the corresponding normalized liminf/limsup confinement;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM is pointwise confined to the static parabolic strip for all negative times.

Remark 4.2 gives the exact critical identities

\[
\lambda_0(-\infty,-1)=\lambda_0(-1,1)=\lambda_0(1,\infty)=1.
\]

Problem 7.8 is exactly the one-line request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy question is Problem 7.9 and is not part of I0077.

## 3. Fresh prior-art/status pass — 2026-09-17

Fresh bounded searches included the exact source title/problem wording, later-author/citing variants, sampled Ornstein–Uhlenbeck persistence, Gaussian AR(1) persistence, periodic target sets, and “comb” constraints.

Nearest methodological prior art includes:

- G. C. M. A. Ehrhardt, A. J. Bray and S. N. Majumdar, *Persistence of a Continuous Stochastic Process with Discrete-Time Sampling: Non-Markov Processes*, Phys. Rev. E 65 (2002), 041102, on discrete sampling of Gaussian stationary processes;
- G. C. M. A. Ehrhardt, S. N. Majumdar and A. J. Bray, *Persistence Exponents and the Statistics of Crossings and Occupation Times for Gaussian Stationary Processes*, Phys. Rev. E 69 (2004), 016106, including discretely sampled OU;
- F. Aurzada and M. Kettner, *Persistence exponents via perturbation theory: AR(1)-processes*, J. Stat. Phys. 177 (2019), 651–665, arXiv:1810.09861.

There is also physics literature using “comb” for a different topological diffusion model. That is not the present problem: here the process is ordinary one-dimensional Brownian/FBM and the comb is a periodic **allowed spatial set at selected space-time gates**.

I found no later paper in this bounded dated search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the FBM sampled spatial-comb theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Sampled-Gaussian persistence and Markov-operator contraction are classical mechanisms and are not claimed as new.

## 4. New family: geometric spatial-comb gates

For spacing `L>0` and tooth half-width `0<eta<L/2`, define the periodic closed spatial comb

\[
D_{L,\eta}:=\bigcup_{j\in\mathbb Z}[jL-\eta,jL+\eta].
\tag{4.1}
\]

Fix a logarithmic gate spacing `P>0`, with physical gate times

\[
u_k=e^{kP}.
\tag{4.2}
\]

The sampled comb constraint is

\[
\boxed{
\frac{X_{-u_k}}{\sqrt{u_k}}\in D_{L,\eta}
\qquad\text{for every sufficiently large }k.
}
\tag{4.3}
\]

Between gate times the path is unconstrained. Hence, unlike the continuous static comb of run 18, a continuous path is free to migrate between different teeth between successive gates. The branch/component label is no longer conserved.

The discrete gates can be thickened to an honest positive-width deterministic space-time shape without changing the obstruction; Section 11 records that construction. The thickening is part of the same metric family, not another count.

## 5. The three new-method moves

### #3 PROVE SOMETHING STRONGER

Rather than prove only one numerical example, I proved a general sampled-set contraction compiler for every periodic comb satisfying an explicit one-step mass inequality. The canonical rational example is then a corollary.

### #11 DUALIZE

Instead of trying to follow which tooth the path occupies, pass to the sampled OU Markov operator

\[
(K_Df)(x)=\int_D p_P(x,y)f(y)\,dy.
\]

The relevant quantity is its elementary `L^infinity -> L^infinity` contraction

\[
\|K_D\|_{\infty\to\infty}
=\sup_x Q_P(x,D).
\]

This automatically sums over **all possible tooth migrations**. The combinatorial explosion of branch choices disappears into one operator norm.

### #21 ASK WHO ELSE HAS THIS SHAPE

The sampled-stationary-Gaussian and AR(1) persistence literature confirms that geometric Brownian sampling should be treated as a Markov persistence problem, while the “comb diffusion” literature confirms that the word comb is already used for a different model. The useful imported idea here is the sampled Markov contraction, not any claimed new OU formalism.

## 6. A periodic-comb one-step bound

Let sampled OU have one-step correlation

\[
r=e^{-P/2},\qquad s^2=1-r^2=1-e^{-P}.
\tag{6.1}
\]

Given the current sampled value `x`, the next one is Gaussian

\[
Y'=rx+sZ,\qquad Z\sim N(0,1).
\tag{6.2}
\]

For any mean `mu` and any `0<eta<L/2`, choose a nearest lattice center `jL` to `mu`. The probability that `N(mu,s^2)` lands in that nearest tooth is at most

\[
\frac{2\eta}{s\sqrt{2\pi}}.
\tag{6.3}
\]

Every other tooth is at distance at least `L/2-eta` from `mu`, even in the tie case. Hence the union of all other teeth is contained in

\[
\{|N(\mu,s^2)-\mu|\ge L/2-\eta\},
\]

and the Gaussian Chernoff bound gives

\[
\boxed{
\sup_{\mu\in\mathbb R}
\mathbb P\{N(\mu,s^2)\in D_{L,\eta}\}
\le
Q(P,L,\eta)
:=
\frac{2\eta}{s\sqrt{2\pi}}
+2\exp\!\left[-\frac{(L/2-\eta)^2}{2s^2}\right].
}
\tag{6.4}
\]

This bound is deliberately crude but uniform in the current state and therefore ideal for an FBM obstruction.

If `Y_k=e^{-kP/2}B_{e^{kP}}`, then `(Y_k)` is stationary sampled OU and

\[
Y_{k+1}=rY_k+sZ_{k+1}.
\tag{6.5}
\]

Consequently, for every `n>m`,

\[
\boxed{
\mathbb P\{Y_m,\ldots,Y_n\in D_{L,\eta}\}
\le Q(P,L,\eta)^{n-m}.
}
\tag{6.6}
\]

In operator language this is simply repeated use of `||K_D||_{infinity->infinity} <= Q`.

## 7. Theorem I0077-R07-T28 — sampled spatial-comb obstruction

Fix `P,L>0` and

\[
0<\eta_0<\eta_2<L/2.
\]

Assume

\[
\boxed{Q(P,L,\eta_2)<e^{-P}.}
\tag{T28-cond}
\]

Then for **every** forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists K<\infty:\
\frac{X_{-e^{kP}}}{e^{kP/2}}
\in D_{L,\eta_0}
\quad\forall k\ge K
\right)=0.
}
\tag{T28}
\]

Thus an FBM cannot eventually hit a sufficiently thin infinite periodic comb at every geometric scale, even though it is allowed to choose a different tooth at every gate and is completely unconstrained between gates.

There is also a source-side positive regime within the same geometric comb family. If the central tooth is strictly source-subcritical,

\[
\lambda_0(-\eta_0,\eta_0)<1,
\tag{7.1}
\]

then Theorem 4.3(iii) supplies a decomposable FBM with

\[
|X_t|\le\eta_0\sqrt{|t|}\qquad(t<0),
\]

so in particular it satisfies every comb gate. By the exact critical identity `lambda_0(-1,1)=1` and strict domain monotonicity, this positive condition holds for every `eta_0>1`. For, say, `L=6` and `1<eta_0<3`, the comb remains genuinely disconnected while a decomposable FBM can remain in its central tooth for every negative time.

The theorem deliberately does **not** claim a sharp threshold between the small-tooth obstruction regime and the `eta_0>1` existence regime.

## 8. Exact canonical example

Take

\[
P=\log4,\qquad L=6,\qquad
\eta_0=\frac1{100},\quad
\eta_1=\frac3{200},\quad
\eta_2=\frac1{50}.
\tag{8.1}
\]

Then

\[
r=\frac12,\qquad s^2=\frac34.
\tag{8.2}
\]

The nearest relaxed tooth has length

\[
2\eta_2=\frac1{25}.
\tag{8.3}
\]

Because

\[
(s\sqrt{2\pi})^2=\frac32\pi>1,
\]

the maximum Gaussian density is `<1`, so the nearest-tooth probability is `<1/25`.

Every other tooth is at distance at least

\[
3-\frac1{50}=\frac{149}{50}.
\tag{8.4}
\]

The normalized Chernoff exponent is exactly

\[
\frac{(149/50)^2}{2(3/4)}
=\frac{22201}{3750}>5.
\tag{8.5}
\]

Since

\[
e^5>1+5+\frac{25}{2}=\frac{37}{2}>10,
\]

the total Gaussian mass of all non-nearest teeth is `<2e^{-5}<1/5`. Therefore

\[
\boxed{
Q(\log4,6,1/50)<\frac1{25}+\frac15=\frac6{25}<\frac14=e^{-P}.
}
\tag{8.6}
\]

Hence T28 gives the explicit result

\[
\boxed{
\mathbb P\left(
\exists K:\
\frac{X_{-4^k}}{2^k}
\in
\bigcup_{j\in\mathbb Z}
\left[6j-\frac1{100},6j+\frac1{100}\right]
\quad\forall k\ge K
\right)=0
}
\tag{8.7}
\]

for every FBM.

The finite rational inequalities in (8.1)–(8.6) were checked exactly; see Section 13.

## 9. Proof of T28 for arbitrary real Brownian terminals

A finite sampled-chain bound is not enough for an FBM witness, because the Brownian witness terminal is random and need not lie on the gate grid. This section removes that dependence issue pathwise.

Choose an intermediate width

\[
\eta_0<\eta_1<\eta_2.
\tag{9.1}
\]

For the canonical example the two slacks are exactly `1/200`.

Let `W` be standard Brownian motion. Fix a deterministic gate index `K_0`. Call a real terminal `T` **comb-good** if

\[
\frac{W_T-W_{T-e^{kP}}}{e^{kP/2}}
\in D_{L,\eta_1}
\tag{9.2}
\]

for every `k>=K_0` with `e^{kP}<=T`.

For integer `n>=3`, put

\[
M_n:=\sup\{|W_t-W_s|:0\le s,t\le n+1,\ |t-s|\le1\}.
\tag{9.3}
\]

The standard reflection-principle/union-bound estimate used in the preceding R07 fence proofs gives

\[
\mathbb P(M_n>x)\le4(n+1)e^{-x^2/16}.
\tag{9.4}
\]

Thus with `x_n=16 sqrt(log n)`,

\[
\sum_n\mathbb P(M_n>x_n)<\infty.
\tag{9.5}
\]

Choose `C_0` so large that

\[
\frac{32}{\sqrt{C_0}}\le\eta_2-\eta_1,
\tag{9.6}
\]

and let `R_n=e^{m_nP}` be the least gate lag at least `C_0 log n`; then `R_n=O(log n)`.

If `T in [n,n+1]` is comb-good and `M_n<=x_n`, then for every gate lag `u=e^{kP}` with `R_n<=u<=n`,

\[
\left|
\frac{(W_n-W_{n-u})-(W_T-W_{T-u})}{\sqrt u}
\right|
\le\frac{2M_n}{\sqrt u}
\le\eta_2-\eta_1.
\tag{9.7}
\]

Therefore the integer-terminal reversed increments satisfy

\[
\frac{W_n-W_{n-u}}{\sqrt u}\in D_{L,\eta_2}
\tag{9.8}
\]

at every such geometric lag. Brownian time reversal makes `(W_n-W_{n-u})_{0<=u<=n}` a standard Brownian motion in the lag variable `u`. Applying (6.6), with

\[
K_n=\left\lfloor\frac{\log n}{P}\right\rfloor,
\]

gives

\[
\mathbb P\{(9.8)\text{ at every gate }k=m_n,\ldots,K_n\}
\le C_1Q^{K_n-m_n}
\le C_2\left(\frac n{R_n}\right)^{-\kappa},
\tag{9.9}
\]

where

\[
\kappa=-\frac{\log Q(P,L,\eta_2)}P>1
\tag{9.10}
\]

by (T28-cond). Since `R_n=O(log n)`, the right side of (9.9) is summable in `n`. Combining with (9.5),

\[
\sum_n
\mathbb P\{\exists\text{ comb-good }T\in[n,n+1]\}<\infty.
\tag{9.11}
\]

Borel–Cantelli yields the path-only conclusion

\[
\boxed{
\mathbb P\{\exists\text{ comb-good }T\ge A\}\to0
\quad(A\to\infty).
}
\tag{9.12}
\]

No random terminal has been conditioned upon.

## 10. Transfer from Brownian paths to an arbitrary FBM

Suppose T28 fails for some FBM `X`. By countable unions over the eventual gate index and an integer bound for `|X_0|`, there exist deterministic `K,M<infinity` and `q_0>0` such that the event

\[
E=\left\{|X_0|\le M,\quad
X_{-e^{kP}}/e^{kP/2}\in D_{L,\eta_0}
\ \forall k\ge K\right\}
\tag{10.1}
\]

has probability at least `q_0`.

Increase `K` so that

\[
\frac M{e^{kP/2}}\le\eta_1-\eta_0
\qquad(k\ge K).
\tag{10.2}
\]

Because `D_{L,eta}` is symmetric, on `E`

\[
\frac{X_0-X_{-e^{kP}}}{e^{kP/2}}
\in D_{L,\eta_1}
\qquad(k\ge K).
\tag{10.3}
\]

Let `S_j->-infinity` be an FBM witness sequence and put `T_j=-S_j`. For each fixed deterministic witness index `j`,

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. Whenever `e^{kP}<=T_j`,

\[
W_j(T_j)-W_j(T_j-e^{kP})
=X_0-X_{-e^{kP}}.
\tag{10.4}
\]

Thus on `E`, every sufficiently large `T_j` is comb-good for the Brownian path `W_j`.

Choose deterministic `A` so large that the Brownian probability in (9.12) is `<q_0/2`. Since `T_j->infinity` almost surely, choose a **deterministic witness index** `j` such that

\[
\mathbb P(T_j<A)<q_0/2.
\tag{10.5}
\]

Then (10.3)–(10.4) imply

\[
\mathbb P\{W_j\text{ has a comb-good terminal }T\ge A\}
>q_0/2,
\]

contradicting (9.12). This proves T28. No conditioning on a random witness time and no independence between a witness time and its Brownian witness path is used. `square`

## 11. Positive-width space-time thickening — same metric family

To make the geometry a bona fide positive-width space-time tube rather than isolated time slices, work in logarithmic time `r=log u`. Around gate center `kP`, choose pairwise disjoint windows

\[
G_k=(kP-\varepsilon_k,kP+\varepsilon_k),
\qquad \sum_k\varepsilon_k<\infty.
\]

Inside `G_k` let the allowed normalized cross-section be

\[
D_{L,\eta_k(r)},
\qquad
\eta_k(r)
=\eta_0+\left(\frac L2-\eta_0\right)
\frac{|r-kP|}{\varepsilon_k}.
\tag{11.1}
\]

At the center this is exactly `D_{L,eta0}`. At either window edge `eta_k=L/2`, so adjacent teeth meet and the cross-section becomes all of `R`; outside all windows allow all of `R`.

Any eventual confinement to this deterministic thickened shape implies the center-gate constraints and is therefore impossible under T28. The total nontrivial logarithmic time `2 sum epsilon_k` can be made arbitrarily small. This thickening is **not** counted as a second family.

## 12. Why this is genuinely new under the frozen equivalence convention

The new family is not a parameter variant of earlier R07 shapes.

- Run 18/T19 studied a continuous-time infinite parabolic comb. Continuity trapped the normalized path in one connected component forever. Here the path is unconstrained between geometric gates and may migrate between teeth; the proof must sum over every migration.
- Run 24/T25 used geometric gates, but each gate was one **bounded connected centered interval**. Here every gate is an unbounded periodic set with countably infinitely many bounded components and infinite total Lebesgue measure.
- Run 26/T27 used geometric **unbounded half-lines** with alternating orientation and a negative-AR switch cost. Here the sampled correlation remains positive and the obstruction is the total OU transition mass of a periodic multicomponent target.
- Brownian rescaling changes logarithmic phase/coefficient conventions but does not turn an infinite periodic disconnected cross-section into a single interval or half-line, nor does it turn a sampled gate family into a continuously imposed static comb.

Thus the structural invariants differ: gate-time sparsity, cross-section component count/topology, and the persistence operator are all different. The frozen metric moves

\[
\boxed{26\longrightarrow27}.
\]

`unchanged_count = 0`.

## 13. Exact self-check

The finite rational core of the canonical example was executed before the report was archived.

Source:

`artifacts/R07/20260917T1925Z_sampled_spatial_comb_constants.py`

creation commit `9fa350ac73628304646c88c2d400b5163804616d`.

Executed output:

`artifacts/R07/20260917T1925Z_sampled_spatial_comb_constants.out`

creation commit `b5c50fc0d9b700582db39fa4150b1707bea5e2fb`.

The output ends `PASS` and checks exactly

\[
s^2=\frac34,\quad
\eta_1-\eta_0=\eta_2-\eta_1=\frac1{200},\quad
2\eta_2=\frac1{25},
\]

\[
3-\eta_2=\frac{149}{50},\qquad
\frac{(149/50)^2}{2(3/4)}=\frac{22201}{3750}>5,
\]

\[
1+5+\frac{25}{2}=\frac{37}{2}>10,\qquad
\frac1{25}+\frac15=\frac6{25}<\frac14,\qquad
\frac{25}{6}>4.
\]

The Gaussian density and Chernoff inequalities are analytic inputs proved/standard on the page. This artifact is a **self-check**, not an independent audit.

## 14. What failed / what remains

The first attempted shortcut was to reuse run 18’s “connected tail chooses one tooth forever.” It fails completely for sampled gates because the path may cross every gap while unconstrained between gates. That failure is precisely why the sampled Markov-operator route is needed.

A second tempting shortcut was to classify the comb by its convex hull. Its convex hull is all of `R`, which would predict no obstruction and therefore loses the phenomenon entirely.

The third attempted simplification was to bound only the probability of returning to the **same** tooth. That is insufficient because the path can move to any of infinitely many teeth. The uniform total transition-mass bound (6.4) is the step that closes the argument.

T28 does not settle the sharp tooth-width threshold. In the canonical `L=6,P=log4` family we now have an explicit universal-impossibility point at `eta=1/100` and a source-driven decomposable existence regime for every `eta>1` (while `eta<3` keeps the comb disconnected). The intermediate regime is open.

Problem 7.8 remains **PARTIAL**. T28 has a full theorem-sized argument on this page and an exact self-check for its finite rational core, but it has **0/2 independent closure audits**. No closure or paper package is claimed.

The strongest next route is not another checker. It is to attack the gap between the sampled-set contraction threshold and the source subcritical central-tooth existence regime, possibly by the exact spectral radius of the periodic-target sampled OU operator rather than the crude `L^infinity` bound.

Suggested next method combination: `#5 ADD A PARAMETER`, `#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE`, `#27 SWAP THE QUANTIFIERS`.

## 15. Structured ledger_delta for the authorized shared-root maintainer

```text
track: R07
allocation: CLOSABLE OUTSIDE
source: Burdzy-Scheutzow Forward Brownian Motion, Problem 7.8 / I0077
claim_owner: R07
claim_shared_status: PENDING_ADMISSION, not READY (preserved)
frozen_metric: number of genuinely distinct nonparabolic shape families with complete source-appropriate theorem
metric_before: 26
metric_after: 27
movement: +1
new_family: geometric sampled spatial-comb gate tubes
new_theorem: I0077-R07-T28
canonical_example: P=log 4, L=6, eta0=1/100; no FBM can hit D_{6,1/100} at every sufficiently large power-of-four gate
positive_regime: for eta>1 (and eta<L/2), source Theorem 4.3(iii) gives decomposable pointwise confinement in the central tooth
self_check: PASS
artifact_source_commit: 9fa350ac73628304646c88c2d400b5163804616d
artifact_output_commit: b5c50fc0d9b700582db39fa4150b1707bea5e2fb
source_status: PARTIAL
unchanged_count: 0
closure_audits_for_T28: 0/2
older_T22_audits: 2/2 scoped PASS; does not audit T28 or close whole source problem
publication_novelty: UNVERIFIED (bounded negative search only)
old_R07_KPZ_route: RETIRED / preserved
shared_roots_modified_by_R07: none
```

## 16. Model / scheduler-control status

GPT-6 maximum was requested in prompt text, but the actual reportable runtime is **GPT-5.6 Sol with reasoning level UNVERIFIED**. I do not claim GPT-6 maximum.

The exposed task-control surface still provides prompt/title, schedule/start-offset, enablement, and timing-mode fields but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains prompt-only. Enforcing it requires product/backend support or an authorized owning/admin surface that exposes and verifies those controls.

The historical `You cannot modify this task` event for P26 was authorization-context-specific: the current repository ledger records a later successful P26 update from another authorized context. The legitimate workaround is that authorized owning context or platform support, not a worker-level bypass or duplicate task. No scheduler modification was attempted in this run.
