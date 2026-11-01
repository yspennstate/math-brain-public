Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/task interface has no model selector, no reasoning-effort selector, and no authenticated completed-run telemetry establishing GPT-6/maximum, so I do not claim otherwise. **NO MOVEMENT: active R19/I0110 `M_9 = 9/9 -> 9/9`; unchanged count `0 -> 1`; Section-B methods used: #3 PROVE SOMETHING STRONGER, #22 READ THE FAILURES NOT THE SUCCESSES, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

Problem/source: **Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.1 (Derandomization), intake I0110.**

Status: **PARTIAL / 9-OF-9 COMMON-CERTIFICATE CANDIDATE / SOURCE OPEN / AUDIT PENDING.** Metric saturation is not source closure.

# 1. Continuity and why this run does not reopen I0084

The scheduled prompt still names Hasebe--Ueda I0084. The controlling immutable R19 history already reached the six-unchanged-run CLOSABLE rotation on I0084 and explicitly says that no seventh unchanged I0084 research run should be produced. The complete handoff remains at

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

All supported I0084 progress remains preserved, including the exact arXiv-v2 convention that Conjecture 5.5 uses **ordinary classical convolution** `mu*S_t` even when `S_t` is the law of a free-stable distribution. I did not replace `*` by free convolution and did not restart that problem.

R19's create-only successor claim is

`operations/claims/I0110.md`.

The immediately preceding R19 report is

`runs/R19/2026-09-17_03-36-35_UTC__i0110-ele9.md`.

It froze one Entropic Lift-Extraction (ELE) certificate, verified the same definition against all nine Salez source families, and saturated the metric at `M_9=9/9`, but deliberately retained status **PARTIAL / SOURCE OPEN / AUDIT PENDING** because the source asks for a `structural property` and ELE may be only a common proof certificate.

Before the argument below I reread/rechecked the current campaign index/ranking, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operations follow-up manifest, the latest own report, the frozen ELE artifact, the audit request, the current P26 daily reports, and the visible R18 report/search state. Root `RESULTS.md` is explicitly stale for the R-series and directs readers to recover newer complete reports, so the immutable R19 reports control continuity here.

# 2. Audit gate checked first: still absent

The preceding run requested two end-to-end audits at

`artifacts/R19/2026-09-17_03-36-35_UTC__i0110_audit_request.md`.

The request separates:

1. mathematical verification of C008/C009/C010/C013 and all nine frozen ELE matches;
2. the source-scope verdict: whether ELE really qualifies as Salez's requested `structural property`, rather than only a procedural common certificate.

I searched the current repository for `P26-AUDIT-R19-I0110`, `R18-AUDIT-R19-I0110`, `AUDIT-R19-I0110`, `I0110 ELE`, and the exact audit-request path. I also inspected the current P26 run directory through the newest visible reports. No end-to-end P26 I0110 audit and no end-to-end R18 I0110 audit were found. Therefore:

- P26 end-to-end audit: **NOT FOUND**;
- distinct R18 end-to-end audit: **NOT FOUND**;
- closure condition: **NOT MET**.

No paper folder is created in this run.

# 3. Fresh source/literature check -- 17 September 2026 UTC

The exact source target remains Salez, arXiv:2508.21055v1, Problem 2.1:

> Find a structural property which is almost-surely satisfied by the various random graphs considered above, and which deterministically triggers cutoff.

The nine cited source families remain `[80,16,14,21,13,61,22,52,62]`.

A fresh bounded search included the exact Problem 2.1 wording, `Salez derandomization structural property cutoff random graphs`, later Salez papers, citing papers, and `local product condition cutoff`.

The most relevant later primary result remains Pedrotti--Salez, arXiv:2607.05345 (6 July 2026), _The local product condition implies cutoff_. It gives an intrinsic sufficient criterion through a non-equilibrium/local Poincare constant, and its restricted-constant remark explicitly points toward a more flexible future criterion. Previous R19 work already showed that the **global-infimum** version cannot be the common nine-family answer: early tree geometry forces its constant too small on fixed-degree random regular graphs. I therefore did not restart that failed global route.

No primary source located in this bounded search claimed a resolution of Salez Problem 2.1 across all nine source models. A bounded negative search is not a novelty certificate.

# 4. Idea before code: test whether the semantic repair is even possible

The last report identified one question as higher-value than another optional lemma:

> Can ELE be rewritten as an intrinsic graph/transition-kernel property, with the model-specific lift names erased, while retaining all nine cases?

Before attempting such a rewrite, I attacked the **failure mode**. The result is decisive: the obvious lift-free projection of ELE collapses to a statement **equivalent to cutoff itself**. Thus simply hiding the auxiliary lifts behind state-space notation would not repair the source-scope problem; it would make the proposed `structural property` tautological.

This is the new theorem of the run.

# 5. R19-I0110-C014 -- the intrinsic lift-free projection is exactly cutoff

Let `(P_{n,t})` be finite Markov semigroups, with stationary laws `pi_n`, source-relevant initial laws, and time-`t` distributions `p_{n,t}`. Let

\[
d_n(t)=\|p_{n,t}-\pi_n\|_{\rm TV}.
\]

Fix times `t_n^-<t_n^+` with

\[
\frac{t_n^+}{t_n^-}\to1.
\tag{5.1}
\]

Define the following **intrinsic smooth certificate**, involving only the actual state-space laws.

### ISC-L

There are sets `A_n` such that

\[
p_{n,t_n^-}(A_n)\to1,
\qquad
\pi_n(A_n)\to0.
\tag{5.2}
\]

### ISC-U

There are subprobabilities `s_n\le p_{n,t_n^+}` with masses

\[
m_n:=\sum_xs_n(x)\to1
\tag{5.3}
\]

and centered weighted collision defects

\[
\Delta_n:=
\sum_x\frac{(s_n(x)-m_n\pi_n(x))^2}{\pi_n(x)}
\to0.
\tag{5.4}
\]

Here states with `pi_n(x)=0` are absent because the source chains are finite irreducible chains.

## Theorem C014

Under (5.1), the sequence has cutoff across the window `[t_n^-,t_n^+]`, namely

\[
d_n(t_n^-)	o1,
\qquad
d_n(t_n^+)	o0,
\tag{5.5}
\]

**if and only if** it has ISC-L and ISC-U.

In particular, ISC is not an independent structural explanation of cutoff; it is an intrinsic reformulation of the cutoff endpoints.

## Proof: ISC implies cutoff

From ISC-L,

\[
d_n(t_n^-)
\ge p_{n,t_n^-}(A_n)-\pi_n(A_n)
\to1.
\tag{5.6}
\]

For ISC-U write

\[
p_{n,t_n^+}=s_n+u_n,
\qquad
u_n:=1-m_n=\sum_xu_n(x).
\]

Then

\[
p_{n,t_n^+}-\pi_n
=(s_n-m_n\pi_n)+(u_n-\nu_n\pi_n).
\]

The total-variation distance between two subprobabilities of common mass `nu_n` is at most `nu_n`, while Cauchy--Schwarz gives

\[
\begin{aligned}
\|s_n-m_n\pi_n\|_{\rm TV}
&=\frac12\sum_x|s_n(x)-m_n\pi_n(x)|\\
&\le\frac12
\left(\sum_x\pi_n(x)\right)^{1/2}
\left(\sum_x\frac{(s_n(x)-m_n\pi_n(x))^2}{\pi_n(x)}\right)^{1/2}\\
&=\frac12\sqrt{\Delta_n}.
\end{aligned}
\]

Hence

\[
d_n(t_n^+)
\le (1-m_n)+\frac12\sqrt{\Delta_n}
\to0.
\tag{5.7}
\]

Together with (5.1) and monotonicity of total variation under the Markov semigroup, this is cutoff. `QED` for this direction.

## Proof: cutoff implies ISC-L

Assume `d_n(t_n^-)\to1`. Because the state space is finite, choose `A_n` attaining the variational characterization

\[
d_n(t_n^-)
=p_{n,t_n^-}(A_n)-\pi_n(A_n).
\tag{5.8}
\]

Both quantities on the right lie in `[0,1]`. If their difference tends to one, necessarily

\[
p_{n,t_n^-}(A_n)\to1,
\qquad
\pi_n(A_n)\to0.
\tag{5.9}
\]

Thus ISC-L holds.

## Proof: cutoff implies ISC-U by clipping

Set

\[
p_n:=p_{n,t_n^+},
\qquad
d_n:=\|p_n-\pi_n\|_{\rm TV}\to0.
\]

Choose any `delta_n->0`, for example `delta_n=sqrt(d_n)` when `d_n>0` and `delta_n=0` when `d_n=0`. Define the subprobability

\[
s_n(x):=\min\{p_n(x),(1+\delta_n)\pi_n(x)\}.
\tag{5.10}
\]

Plainly `s_n\le p_n`. Its lost mass is

\[
\begin{aligned}
1-m_n
&=\sum_x\bigl(p_n(x)-(1+\delta_n)\pi_n(x)\bigr)_+\\
&\le\sum_x(p_n(x)-\pi_n(x))_+\\
&=d_n\to0.
\end{aligned}
\tag{5.11}
\]

So `m_n->1`.

Put

\[
f_n(x):=\frac{s_n(x)}{\pi_n(x)}.
\]

Then

\[
0\le f_n\le1+\delta_n,
\qquad
\mathbb E_{\pi_n}f_n=m_n.
\tag{5.12}
\]

Therefore

\[
f_n^2\le(1+\delta_n)f_n,
\]

and consequently

\[
\begin{aligned}
\Delta_n
&=\mathbb E_{\pi_n}(f_n-m_n)^2\\
&=\mathbb E_{\pi_n}f_n^2-m_n^2\\
&\le(1+\delta_n)m_n-m_n^2\\
&=m_n(1+\delta_n-m_n)\\
&\le\delta_n+(1-m_n)\\
&\le\delta_n+d_n\to0.
\end{aligned}
\tag{5.13}
\]

Thus ISC-U holds. This completes the converse and proves C014. `QED`

# 6. Method #3: stronger consequence for the frozen ELE package

The theorem above is stronger than merely saying that one attempted reformulation fails.

The frozen ELE package already proves

\[
\mathrm{ELE}\Longrightarrow\mathrm{cutoff}.
\]

C014 proves

\[
\mathrm{cutoff}\Longleftrightarrow\mathrm{ISC}.
\]

Hence every ELE certificate automatically has a completely lift-free intrinsic shadow, ISC. But that shadow cannot be what Salez is asking for: it is equivalent to the phenomenon one is supposed to explain.

This identifies the exact role of the model-generated lift restriction in ELE. The lift restriction is not cosmetic metadata. It is the only part preventing the certificate from becoming tautological.

Therefore an acceptable source-level repair must impose a **genuinely prior structural restriction** on the extractor/lift/stopping construction. Merely replacing model-specific lift names by existential state-space objects is not enough.

# 7. Method #22: read the failure rather than polishing the success

This run tried three obvious ways to make ELE look more intrinsic and records why each fails.

### Failure A: erase the lifts and keep only concentration plus smooth extraction

This is exactly ISC, and C014 shows it is equivalent to cutoff. It fails the source-intent test by tautology.

### Failure B: allow an arbitrary path-space typical event

One can put the actual trajectory law on the canonical path space, let `Phi` be the endpoint map, and write ELE there. But if the retained event is allowed to be an arbitrary path event depending on endpoint identities, the same clipping construction can be encoded through the endpoint. The apparent path structure then buys nothing.

### Failure C: define the property using the mixing time itself

A restricted local-Poincare or extraction condition imposed specifically on `[t_mix(1-eps),t_mix(eps)]` can be mathematically useful, but as a proposed answer to a derandomization problem it risks baking the desired transition into the hypothesis. Pedrotti--Salez avoid the worst form of this problem by giving a quantitative local-product inequality, but the R19 tree-ball obstruction shows that the global infimum is too strong for at least the random-regular model.

The failure diagnosis therefore narrows the search: the common property must be intrinsic enough to be graph/chain structural, but constrained enough that it cannot be selected *after* observing the cutoff transition.

# 8. Method #28: replace unrestricted existence by a typical, canonical construction

I do **not** claim the following candidate is proved across all nine families. It is the next non-tautological route.

Use the chain's **actual trajectory path space** and require the retained event to be generated by a fixed, endpoint-blind structural rule: for example a local exploration/stopping rule, an information-density shell, a cover/backbone stopping rule, or another rule invariant under relabeling of terminal states and fixed before any total-variation calculation.

The lower half then has a canonical information interpretation. If a `1-o(1)` path event satisfies a likelihood/information inequality of the form

\[
\log\frac{q_n(\omega)}{\pi_n(\Phi_n\omega)}\ge a_n,
\qquad a_n\to\infty,
\tag{8.1}
\]

then choosing one representative trajectory per endpoint immediately bounds the stationary mass of the endpoint image by `e^{-a_n}`. This is a real structural compression statement, not an arbitrary TV witness set.

For the upper half, two independent retained trajectories give the exact collision functional

\[
\sum_x\frac{r_n(x)^2}{\pi_n(x)}
=
\mathbb E\left[
\frac{\mathbf1_{\{\Phi_n(\omega)=\Phi_n(\omega')\}}}
{\pi_n(\Phi_n(\omega))}
\,;
\omega,\omega'\in E_n
\right].
\tag{8.2}
\]

Thus a canonical structural path rule plus a collision estimate is enough for ELE-U.

The unresolved point is **the admissible-rule class**. If it is too broad, C014's tautology returns. If it is too narrow (for example only raw path-weight shells), it will likely fail on models whose proofs require a stopped backbone, quasi-tree reduction, or a community-coordinate smoothing step. The next run should search for the weakest *predeclared invariant stopping/exploration class* that contains the nine known constructions. This is now a sharply defined semantic/mathematical obligation rather than a request to rename ELE.

No metric credit is awarded for this candidate.

# 9. Validation discipline

C014 is theorem-sized and its full proof is on the page. It has no finite combinatorial core, so I did **not** manufacture an exact-arithmetic checker merely to create a certificate commit. That would violate the current 90/10 instruction: the theorem is an elementary analytic equivalence, and the useful validation is the explicit inequality chain (5.6)--(5.13), not a finite numerical atlas.

I also did not modify shared roots or peer-track files and did not create a paper folder while the required outside audits remain absent.

# 10. Model/scheduler control status

The implementation limitation remains unchanged. The exposed scheduler controls provide prompt/title/schedule/timing/enabled state but no model selector and no reasoning-effort selector. `GPT-6 / maximum` therefore remains a prompt request rather than an enforceable runtime setting, and this run's reasoning level is UNVERIFIED.

The historical P26 scheduler ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one scheduler context; repository deployment evidence later records a successful update from a different authorized P/C context. The legitimate workaround is an authorized owner/admin/platform context exposing the relevant permission. It is not duplication, task replacement, or permission bypass. No scheduler modification was attempted here.

# 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R19
  active_intake: I0110
  source: "Justin Salez, Modern aspects of Markov chains, arXiv:2508.21055v1, Problem 2.1"
  target: "one common structural property a.s./w.h.p. satisfied by the nine cited random-graph ensembles and deterministically triggering cutoff"
  fixed_metric: "M_9 = number of the nine source families covered by the one frozen common candidate"
  before: "9/9"
  after: "9/9"
  movement: "NO MOVEMENT"
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [3, 22, 28]
  status: "PARTIAL / 9-OF-9 COMMON-CERTIFICATE CANDIDATE / SOURCE OPEN / AUDIT PENDING"
  new_claims:
    - "R19-I0110-C014: the lift-free intrinsic smooth certificate ISC is equivalent to the cutoff endpoint statement"
    - "Consequently, erasing ELE's model-generated lift restriction makes the proposed structural property tautological"
  covered_references: [80, 16, 14, 21, 13, 61, 22, 52, 62]
  uncovered_references: []
  audit_ids:
    p26_i0110: "NOT FOUND"
    r18_i0110: "NOT FOUND"
  remaining_obligation: "Obtain P26 and distinct OTHER-track end-to-end audits. Independently of the audits, replace ELE's informal model-generated-lift clause by a predeclared non-tautological structural class (likely canonical path/exploration/stopping rules) and verify the same precise class across all nine families before claiming Salez source closure."
  evidence:
    - "artifacts/R19/2026-09-17_01-37-22_UTC__i0110_ele_certificate.md"
    - "artifacts/R19/2026-09-17_02-40-33_UTC__i0110_proxy_to_ele_bridge.md"
    - "artifacts/R19/2026-09-17_03-36-35_UTC__i0110_nbrw_ele_completion.md"
    - "artifacts/R19/2026-09-17_03-36-35_UTC__i0110_audit_request.md"
    - "this report, C014"
```

# 12. Next obligation

The fixed metric is saturated and has one unchanged run after saturation. The next run must first look again for the P26 and R18 audits. If an audit finds a mathematical defect, repair that exact defect rather than adding optional lemmas.

If audits remain absent, the highest-value research route is **not** another abstract ELE variant. Formalize one non-tautological admissible class of canonical path/exploration/stopping rules, prove that membership in the class is checkable without knowing the mixing profile, and then test the unchanged definition against the structurally opposite random-regular `[80]`, Abelian `[52]`, and nonreversible-digraph `[21]` families before attempting all nine.

Suggested next Section-B moves: **#12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE/DIRECTION AT A TIME.**
