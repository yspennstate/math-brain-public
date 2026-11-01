Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT in the fixed Tang periodic-tree curvature metric: UNBOUNDED ABOVE -> UNBOUNDED ABOVE; supported unchanged count 4. Section-B moves actually tried: B4 PROVE SOMETHING WEAKER, COMPLETELY; B18 SAY IT IN ANOTHER LANGUAGE; B26 HUNT THE SPORADIC CASE.** The exposed task-control interface still has no model selector or reasoning-effort selector, so the requested GPT-6/maximum setting remains prompt text only and is not claimed as runtime fact.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), PDF **Question 4.11**: for a transitive graph or a periodic rooted tree, is the Bernoulli bond-percolation probability `theta(p)` concave on `(p_c,1)`?

Run ID: `20260916T2232Z_tang_c2c4_recovery`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Current mathematical status: periodic-tree universal assertion **REFUTED mathematically / P26 closure-audit still missing**; transitive-graph-only variant **OPEN**.  
Frozen metric: greatest rigorous lower bound for `theta''(p)` at a certified admissible parameter in the fixed periodic-tree candidate family.  
Metric before / after: `UNBOUNDED_ABOVE -> UNBOUNDED_ABOVE`.

This is the research recovery selected by the preceding STUCK1 report: port the exact free-product branching/reliability compiler to the simplest still-unproved transitive example `C2*C4`. The recovery succeeds as a complete special-case theorem, but it does not move the already-saturated periodic-tree curvature metric and does not solve the transitive class.

# 1. Continuity / repository / ownership recovery

I continued from the newest own immutable state

`runs/R09/20260916T213030Z_tang_stuck1_strategy.md`

rather than restarting. Its selected recovery was explicitly to port the nearest solved free-product method to

`G_4 = Cay(C2*C4,{a,b,b^{-1}})`

in the simple-graph convention.

Before new research I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/TANG-2020-Q4.11.md`, newest own R09 report, Tang-related R08 audits, current R10/I0070 state, and targeted P26/Tang and R10-package searches. I also searched the repository by the Tang arXiv identifier and exact concavity wording. The very large intake JSONL files cannot be rendered row-for-row through this connector before truncation; I do not claim a byte-for-byte visible reread of all roughly 780 rows.

The canonical claim remains R09-owned but still literally says `PENDING_ADMISSION, not READY`. `POSTED.md` does not exclude Tang Question 4.11. No conflicting Tang owner surfaced in the bounded repository search. The old R09 critical-site-percolation route remains retired from this slot, not solved.

# 2. Current source / literature check, dated 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC

Primary source rechecked:

- arXiv `2012.01135v2`, submitted 2 December 2020, last revised 1 March 2023;
- title: *A note on some critical thresholds of Bernoulli percolation*;
- source model: Bernoulli **bond** percolation;
- PDF locator: Question 4.11, the concavity question for transitive graphs or periodic rooted trees.

Fresh bounded web queries included the exact title + Question 4.11 + concavity, exact phrases involving `theta(p)` and periodic trees, Tang later percolation work, and free-product percolation. No later primary source resolving this exact concavity question surfaced. This is a dated bounded negative search, **not** a novelty certificate.

Relevant prior art recovered again:

Iva Kozakova, *Critical percolation of free product of groups*, Int. J. Algebra Comput. 18 (2008), 683--704, arXiv:math/0611668. Kozakova obtains the critical probability of a free product from expected cluster sizes of the factors; for finite factors the critical equation is polynomial. Therefore the free-product branching/cluster compiler used below is not claimed as a new mechanism. The new content of this run is the complete curvature calculation for the specific simple transitive `C2*C4` Cayley graph.

# 3. B18 — SAY IT IN ANOTHER LANGUAGE: cycle-factor reliability PGF

The useful language is not a graph-by-graph path count but the finite-factor cluster probability generating function.

For the cycle `C_m`, `m>=3`, enter the factor block at a distinguished vertex and let `X_m` be the number of **other** vertices of that cycle in the open cluster of the entry vertex. Then

\[
F_m(p,t):=E_p[t^{X_m}]
=(1-p)^2\sum_{k=0}^{m-2}(k+1)(pt)^k
+p^{m-1}(m-(m-1)p)t^{m-1}.
\tag{3.1}
\]

## Proof of (3.1)

For `0<=k<=m-2`, a root cluster containing exactly `k+1` cycle vertices is a proper interval around the root. There are exactly `k+1` choices for how the `k` non-root vertices split between the clockwise and counterclockwise directions. The `k` internal edges of that interval must be open and its two boundary edges must be closed; all remaining cycle edges are irrelevant. Hence

\[
P(X_m=k)=(k+1)p^k(1-p)^2.
\]

The remaining probability is the event that all `m` vertices are connected to the root. Summing the preceding probabilities, or equivalently counting the configurations with at most one closed cycle edge, gives

\[
P(X_m=m-1)=p^{m-1}(m-(m-1)p).
\]

This proves (3.1).

Differentiating at `t=1` gives the exact factor mean

\[
\mu_m(p)=E[X_m]
=2\sum_{j=1}^{m-1}p^j-(m-1)p^m.
\tag{3.2}
\]

For the order-two factor in the **simple** Cayley graph, the block is one edge, not a two-edge cycle, so

\[
F_2(p,t)=1-p+pt,\qquad \mu_2(p)=p.
\tag{3.3}
\]

For `C2*C_m`, the factor-coset incidence is tree-like. Entering a `C2` block produces `X_2` new vertices, each of which starts an independent `C_m` block; entering a `C_m` block produces `X_m` new vertices, each of which starts an independent `C2` block. Thus the percolation exploration is an irreducible two-type Galton--Watson process with mean matrix off-diagonal entries `mu_2,mu_m`, and

\[
p_c\text{ is the unique solution of }p\mu_m(p)=1.
\tag{3.4}
\]

This is the finite-factor/free-product mechanism already represented in Kozakova's prior work; I use it here as a compiler, not as a novelty claim.

# 4. B4 + B26 — complete the first unresolved sporadic scale: `C2*C4`

Let

\[
G_4=\operatorname{Cay}(C_2*C_4,\{a,b,b^{-1}\}),
\qquad a^2=e,\ b^4=e,
\]

with the simple-graph convention. This is a connected simple degree-three vertex-transitive graph. Every vertex belongs to one involution-edge block and one square block.

For the square block, (3.1) gives

\[
\begin{aligned}
P(X_4=0)&=(1-p)^2,\\
P(X_4=1)&=2p(1-p)^2,\\
P(X_4=2)&=3p^2(1-p)^2,\\
P(X_4=3)&=p^3(4-3p),
\end{aligned}
\tag{4.1}
\]

and

\[
\mu_4(p)=p(2+2p+2p^2-3p^3).
\tag{4.2}
\]

Therefore `p_c` is the unique root in `(0,1)` of

\[
H(p):=p\mu_4(p)-1
=-3p^5+2p^4+2p^3+2p^2-1.
\tag{4.3}
\]

The product `p mu_4(p)` is strictly increasing because the finite-factor cluster size is stochastically increasing in `p`. Exact arithmetic gives

\[
H(11151/20000)<0<H(13939/25000),
\]

so

\[
0.55755<p_c<0.55756.
\tag{4.4}
\]

## 4.1 Physical extinction branch, not a spurious algebraic fixed point

Let `u` be extinction after entering a `C2` block and `v` extinction after entering a `C4` block. The exact recursion is

\[
u=1-p+pv,\qquad v=F_4(p,u).
\tag{4.5}
\]

The trivial subcritical algebraic fixed point `(u,v)=(1,1)` exists for every `p`; it must not be confused with the physical supercritical branch.

Eliminating `v` gives

\[
F_4(p,u)-\frac{u-1+p}{p}
=-\frac{u-1}{p}Q_p(u),
\tag{4.6}
\]

where

\[
Q_p(u)=p^4(3p-4)u^2+p^3(2p-3)u+(p^3-2p^2+1).
\tag{4.7}
\]

For `0<p<1`, the quadratic coefficient and linear coefficient are negative while

\[
p^3-2p^2+1=(p-1)(p^2-p-1)>0.
\]

Hence the two roots of `Q_p` have opposite signs. Moreover

\[
Q_p(0)>0,\qquad Q_p(1)=-H(p).
\]

For `p>p_c`, `H(p)>0`, so `Q_p(1)<0`. Thus `Q_p` has exactly one positive root and it lies in `(0,1)`.

The two-type Galton--Watson process is irreducible and supercritical when `p>p_c`, hence its physical extinction vector lies in `[0,1)^2`. Its `u`-coordinate must therefore be the unique positive nontrivial root just isolated. Thus branch selection is rigorous before any differentiation.

The root is

\[
u_*(p)=
-\frac{2p^2-3p+\sqrt{D(p)}}{2p^2(3p-4)},
\tag{4.8}
\]

where

\[
D(p)=-8p^4+28p^3-23p^2-12p+16,
\tag{4.9}
\]

and

\[
v_*(p)=\frac{u_*(p)-1+p}{p}.
\tag{4.10}
\]

The root percolates unless both initial independent factor explorations die, so the actual percolation probability is

\[
\theta_{G_4}(p)=1-u_*(p)v_*(p),\qquad p_c<p<1.
\tag{4.11}
\]

## 4.2 Complete curvature sign

Direct exact differentiation of (4.11) simplifies to

\[
\theta_{G_4}''(p)
=
\frac{D(p)^2A(p)+pB(p)\sqrt{D(p)}}
{p^7(3p-4)^4D(p)^2},
\tag{4.12}
\]

where

\[
\begin{aligned}
A(p)={}&54p^8-477p^7+1674p^6-3288p^5+3841p^4\\
&-1338p^3-3360p^2+4800p-1920,
\end{aligned}
\tag{4.13}
\]

and

\[
\begin{aligned}
B(p)={}&1728p^{13}-25632p^{12}+150606p^{11}-437346p^{10}
+546471p^9+294186p^8\\
&-1911180p^7+2300491p^6-370272p^5-1577694p^4
+1281040p^3\\
&-480p^2-374784p+122880.
\end{aligned}
\tag{4.14}
\]

To determine the sign without floating-point root sampling, use the Bernstein basis

\[
B_{j,n}(p)=\binom nj p^j(1-p)^{n-j}.
\]

The exact Bernstein coefficient lists on `[0,1]` are:

`D`:

`[16, 13, 37/6, 5/2, 1]`;

`-A`:

`[1920, 1320, 840, 14109/28, 2807/10, 1003/7, 471/7, 239/8, 14]`;

`B`:

`[122880, 1222656/13, 847792/13, 5841848/143, 16613026/715, 5208854/429, 10140883/1716, 4656649/1716, 170077/143, 359522/715, 59255/286, 2187/26, 443/13, 14]`.

Every coefficient is positive, so on `(0,1)`

\[
D>0,\qquad A<0,\qquad B>0.
\tag{4.15}
\]

Finally define

\[
\begin{aligned}
T(p)={}&13824p^{23}-315648p^{22}+3123072p^{21}-17394720p^{20}
+58539929p^{19}-113818081p^{18}\\
&+84186710p^{17}+136515571p^{16}-365453213p^{15}+150787765p^{14}
+418270231p^{13}\\
&-397180184p^{12}-446325581p^{11}+674284977p^{10}+421102215p^9
-1098358635p^8\\
&+153376275p^7+846351135p^6-511305216p^5-214036224p^4
+280304640p^3\\
&-29491200p^2-47923200p+14745600.
\end{aligned}
\tag{4.16}
\]

Its exact Bernstein coefficients on `[0,1]` are

`[14745600, 291225600/23, 2646835200/253, 2100741120/253, 55969464576/8855, 155073078528/33649, 108199884981/33649, 175387812022/81719, 224040838335/163438, 342694392129/408595, 14825984862/30107, 14461835204/52003, 204780719743/1352078, 13038824559/163438, 33312790603/817190, 9937699135/490314, 803722742/81719, 471677431/100947, 73364188/33649, 1775649/1771, 115384/253, 52126/253, 2136/23, 42]`.

Hence `T(p)>0` for `0<p<1`. Exact expansion gives the identity

\[
D(p)^3A(p)^2-p^2B(p)^2
=-4(p-1)(3p-4)^4T(p).
\tag{4.17}
\]

For `0<p<1` the right-hand side is strictly positive. Combining (4.15) and (4.17),

\[
D^{3/2}(-A)>pB,
\]

and therefore

\[
D^2A+pB\sqrt D<0.
\]

The denominator in (4.12) is positive, so

\[
\boxed{\theta_{G_4}''(p)<0\quad\text{for every }p\in(p_c,1).}
\tag{4.18}
\]

Thus the first post-`C2*C3` sporadic free-product scale is also **strictly concave on its full supercritical interval**. This is a complete theorem for this transitive graph, but only a PARTIAL result toward the transitive half of Tang Question 4.11.

# 5. What the three new methods did

## B4 — PROVE SOMETHING WEAKER, COMPLETELY

Instead of attacking all transitive graphs, I proved the entire supercritical curvature sign for the concrete transitive graph `Cay(C2*C4,{a,b,b^{-1}})`. It is strictly concave. This is complete for that graph and does not overclaim the source.

## B18 — SAY IT IN ANOTHER LANGUAGE

I rewrote the free-product problem in factor-cluster PGF language and derived the general exact cycle formula (3.1). This makes branch selection and the critical equation systematic for `C2*C_m`, while preserving the actual physical percolation branch.

## B26 — HUNT THE SPORADIC CASE

The simplest unsolved next member `m=4` was the intended sporadic candidate after `m=3`. The hunt failed to produce positive curvature: exact algebra instead proves strict concavity on `(p_c,1)`. The failure is informative because the locally asymmetric transitive free-product route continues to resist the positive-curvature root-decoration mechanism.

# 6. Exact checker / self-check scope

A substantive exact symbolic checker was warranted because this run produced a new all-parameter special-case theorem with a sizable polynomial sign core.

Artifacts:

- `artifacts/R09/20260916T2232Z_tang_c2c4_recovery_checker.py`
- `artifacts/R09/20260916T2232Z_tang_c2c4_recovery_checker.out`

The checker:

1. enumerates all `2^4` C4 bond states exactly and reconstructs (4.1);
2. verifies `F4`, `mu4`, the critical polynomial and exact rational bracket;
3. verifies the fixed-point elimination and explicit physical-root residual;
4. symbolically differentiates the closed physical branch and checks (4.12)--(4.14);
5. reconstructs the Bernstein expansions of `D,-A,B,T` from exact rational coefficients and checks all coefficients are positive;
6. verifies the square-domination identity (4.17).

Archived output ends in `PASS`. Local execution-output SHA-256 before GitHub upload:

`e4ef400fbefb18fde6b9f703191b683dcda47517cfd1a6a2209607aa20cfbe90`.

GitHub creation/readback commits:

- checker source: `27e2858bd333061afe26054d9b779730938153fd`;
- checker output: `9b79edc1d206cd3ee03988cbd5ca1c6d7dea31e0`.

The checker is a self-check of the finite algebraic core; the theorem proof is written on the page above.

# 7. What remains / obstruction update

The periodic-tree disjunct is already mathematically refuted and the frozen curvature metric is already unbounded above, so this run cannot move that metric numerically.

For the transitive class, two exact free-product laboratories now survive the strongest source-valid tests performed by R09:

- `C2*C3`: strictly concave on `(p_c,1)`;
- `C2*C4`: strictly concave on `(p_c,1)` by the complete proof above.

Earlier `C3*C3` is also strictly concave. Thus the most obvious finite-factor free-product symmetrizations have all destroyed, rather than preserved, the positive-curvature finite-stem phenomenon. This is evidence only, not a universal theorem.

The next high-value question is whether the factor-PGF language yields a structural concavity theorem for an entire class such as `C2*C_m`, or whether a more complicated finite factor supplies the first sporadic positive-curvature transitive example.

# 8. Audit / package state

Distinct independent auditor count for the source-matching periodic-tree refutation remains **1**: R08 has multiple PASS certificates, but repeated R08 checks count as one auditor.

Recovered R08 identifiers include:

- `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`;
- `R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02 = PASS`;
- later R08 PASS checks on R09 Cayley/free-product finite cores.

A fresh targeted repository search still found no `P26-AUDIT-R09` / Tang-Q4.11 end-to-end PASS. Therefore the owner-defined closure condition is still unmet, and no `paper_...` folder is created.

The newest R10/I0070 report recovered this run is still `PARTIAL / RECOVERY2 / author-side full-source proof candidate strengthened; external closure audits still missing`. A targeted `paper_I0070` search still returns no closure-ready paper package. The instruction is to audit R10 when such a package is ready, so no R10 audit is invented here.

# 9. Model / task-control / permission escalation

The limitation remains real in this run. The exposed task-control interface offers title, prompt, schedule, enabled state and timing mode, but **no model field and no reasoning-effort field**. Therefore R09 cannot set or verify GPT-6/maximum through that interface; prompt text is not runtime telemetry.

A real fix requires product/API support exposing model and reasoning-effort selectors plus authenticated runtime metadata, or use of the native task's owning workspace/UI if those controls exist there.

The repository records historical `You cannot modify this task` responses for some native IDs and also records that P26 was later editable from a different authorized context. The legitimate workaround is the authorized owning account/workspace/interface or platform support. Do not create duplicate jobs or bypass the permission boundary.

No scheduler modification was attempted in this run because current deployment policy prohibits scheduler changes.

# 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), PDF Question 4.11"
  target: "decide concavity of theta(p) on (p_c,1); periodic-tree disjunct first, transitive variant retained separately"
  metric: "greatest rigorous lower bound for theta''(p) at a certified admissible parameter in the fixed periodic-tree candidate family"
  before: UNBOUNDED_ABOVE
  after: UNBOUNDED_ABOVE
  movement: false
  supported_unchanged_count: 4
  stuck_episode: "recovery after STUCK1"
  methods: [4, 18, 26]
  status:
    periodic_tree_source_disjunct: "REFUTED mathematically; P26 closure audit pending"
    transitive_graph_only_variant: "OPEN; PARTIAL exact concave examples C2*C3, C2*C4, C3*C3"
  new_claims:
    - id: R09-TANG-C2C4-CONCAVITY-05
      status: PROVED_SPECIAL_CASE
      statement: "For the simple transitive Cayley graph Cay(C2*C4,{a,b,b^{-1}}), theta''(p)<0 for every p in (p_c,1), with 0.55755<p_c<0.55756."
    - id: R09-TANG-CYCLE-PGF-06
      status: PROVED_COMPILER
      statement: "Exact factor-cluster PGF F_m(p,t) for a cycle C_m, m>=3, as equation (3.1)."
  exact_evidence:
    source: "artifacts/R09/20260916T2232Z_tang_c2c4_recovery_checker.py"
    source_commit: "27e2858bd333061afe26054d9b779730938153fd"
    output: "artifacts/R09/20260916T2232Z_tang_c2c4_recovery_checker.out"
    output_commit: "9b79edc1d206cd3ee03988cbd5ca1c6d7dea31e0"
    output_sha256: "e4ef400fbefb18fde6b9f703191b683dcda47517cfd1a6a2209607aa20cfbe90"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS"
    - "R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02=PASS"
  distinct_auditor_count: 1
  missing_audit: "P26 end-to-end Tang Q4.11 periodic-tree audit"
  ownership: "operations/claims/TANG-2020-Q4.11.md; owner R09; coordinator label remains PENDING_ADMISSION"
  next_methods: [11, 21, 27]
```

# 11. Next attack

The fixed metric did not move, so this run is not represented as metric progress. The recovery did, however, settle the simplest previously unproved transitive free-product member.

If the Tang slot remains active before the six-unchanged closable retirement threshold, the next genuinely different methods are:

- **B11 DUALIZE:** express factor PGF curvature through extinction/survival dual variables and search for a sign-preserving transform;
- **B21 ASK WHO ELSE HAS THIS SHAPE:** compare the `C2*C_m` extinction recursion with reliability-polynomial / branching-process concavity criteria in the literature;
- **B27 SWAP THE QUANTIFIERS:** instead of testing graphs one by one, ask whether one can prove concavity for every `m` in the explicit transitive family `C2*C_m`, then identify precisely which finite-factor property would have to fail for a counterexample.

No source closure is claimed beyond the already-refuted periodic-tree disjunct, and fleet closure still awaits the required distinct P26 audit.
