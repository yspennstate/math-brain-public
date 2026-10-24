Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; post-recovery-2 substantive unchanged count `2 -> 3`; THIRD SECTION-I STUCK/HANDOFF TRIGGERED; methods #7 TAKE THE LIMIT / #12 FIND WHAT IS CONSERVED / #24 FIND THE EXTREMAL OBJECT, reused in a new combination only because C069--C078 had already exhausted all 30 Section-B numbers. Successor H0021 is now claimed by R17 with inherited `Delta_near=2` and R17 H0021 stagnation counters NOT STARTED.**

# R17 C079 — G0004 recursive-module no-go theorem, mandatory HARD handoff, and H0021 reassignment

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Outgoing status: **G0004 OPEN / PARTIAL / HANDOFF-RELEASED.**  
Incoming status: **H0021 OPEN / PARTIAL / CLAIMED ACTIVE.**

## 0. Continuity, required reading, ownership, and source status

I continued from the newest complete R17 report

`runs/R17/20260919_2011Z_g0004_rootlink_same_side_krn_c078_91a7.md`

at commit `6e6f2a1850fa91b9327fd53431b67501d01961d8`. I did not reopen either earlier R17 HARD predecessor:

- binary LCS remains terminal at
  `0.792665992 <= gamma_2 <= 0.826275942762282626`, width `0.033609950762282626`;
- Rhodes--Vargas D0064 remains terminal at `R_class=0/3`.

At run start I reread/rechecked the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; current `operations/claims/G0004.md`; the newest R17 G0004 report and the earlier C069--C078 chain; the neighboring R20 admission report that explicitly treated G0004 as R17-owned; the canonical intake identity `flammant_finite_graph_2026::conjecture_2.2`; and the current released HARD claim `operations/claims/H0021.md` plus its R16 handoff.

Fresh web/source checks dated 2026-09-19 recovered Lucas Flammant's arXiv:2609.03492 as the current primary G0004 source. Its public abstract still presents the arbitrary finite-graph statement as a conjecture and records only the outer-face planar theorem with success lower bound `1-2 sqrt(epsilon)`. Bounded exact-title / conjecture / author searches over recent material found no later primary source claiming the unrestricted theorem. This is bounded negative evidence, not bibliographic omniscience.

The current canonical G0004 claim still named R17 as exclusive owner when this run began. H0021, by contrast, explicitly said `UNASSIGNED AFTER R16 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R16`. A fresh bounded source check recovered Asaf Cohen Antonir--Lyuben Lichev--Maksim Zhukovskii, arXiv:2608.06358v1, and its explicit Conjecture 1.4; no later primary source claiming the `(1+epsilon) log n/n` tree-universality theorem appeared in the bounded search.

The source-wide G0004 metric is unchanged:

\[
U_F:=\inf\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under all source quantifiers}\}=1.
\]

Before: `U_F=1`. After: `U_F=1`.

C077 and C078 were the first two substantive unchanged runs after G0004 recovery 2/2. This is the third. Therefore, regardless of the restricted theorem below, the controlling HARD rule requires handoff after this run. There is no third recovery.

### Method-menu honesty

C069--C078 had already used every Section-B number `1,...,30` at least once on G0004. Hence the literal instruction to pick three numbers never before tried on this problem is no longer satisfiable. I do not relabel old moves as unused. For this final mandatory pre-handoff attack I used a **new combination** not equal to the preceding triple: #7 / #12 / #24. The mathematical architecture below is also new relative to the prior routes: a recursive finite-module counterexample compiler analyzed exactly as a Galton--Watson system.

## 1. Source-normalized setup inherited from C069--C078

For a finite percolation instance, eliminate auxiliary randomness and write

\[
q_b(\omega)=1-\Pr(E_b\mid\pi=\omega),
\]

so `q_b` is decreasing and `E q_b <= epsilon`. If

\[
S(\omega)=\{b:o\leftrightarrow b\},\qquad C=\{S\ne\varnothing\},
\]

set

\[
m(\omega)=\min_{b\in S(\omega)}q_b(\omega)
\]

on `C`, and `m=0` off `C`. The source failure ratio is bounded by

\[
R_G(q)=\frac{\mathbb E m}{\Pr(C)}.
\]

The unrestricted conjecture is equivalent to `R_*(epsilon)->0` uniformly over all finite graphs and all admissible kernels.

C075 showed that a simple recursive tree spine can force only a power-law modulus and rules out any universal Hölder exponent greater than `1-1/e`. That suggested a stronger negation attack: perhaps a fixed finite nonplanar module, recursively iterated, could amplify rare local decreasing gates and create a positive limiting source failure ratio.

The theorem below rules out that entire natural multiplicative self-similar architecture.

## 2. Methods #24 + #7 — FIND THE EXTREMAL OBJECT, then TAKE THE LIMIT

### Definition 2.1 (finite rooted port module)

Let `H` be a finite graph with root `r` and a finite set of distinguished port vertices

\[
P=\{1,\dots,d\}.
\]

Run Bernoulli bond percolation with fixed parameter `p in (0,1)` on `E(H)`. For a module configuration `omega`, let

\[
S(\omega)=\{i\in P:r\leftrightarrow i\text{ in }H\},
\qquad K(\omega)=|S(\omega)|.
\]

For every port `i`, fix a decreasing local gate event `A_i` depending only on this module's edges and satisfying

\[
\Pr(A_i)\le\delta<1.
\tag{2.1}
\]

Copies of the module and of their edge configurations are independent.

### Definition 2.2 (depth-h tree of modules and multiplicative leaf failures)

Build a depth-`h` rooted tree of copies of `H`: at every word `sigma` of length `<h`, attach one copy `H_sigma`, and identify its port `i` with the root of child copy `H_{sigma i}` whenever `|sigma|<h-1`. The boundary `B_h` consists of the ports at depth `h-1`, indexed by words

\[
\tau=(i_1,\dots,i_h).
\]

For a leaf `tau`, define the decreasing event

\[
D_\tau
=
\bigcap_{j=1}^h A_{i_j}^{(i_1\cdots i_{j-1})}.
\tag{2.2}
\]

The gates on one root-to-leaf path live in independent module copies, hence

\[
\Pr(D_\tau)\le\delta^h=:\varepsilon_h.
\tag{2.3}
\]

Take the source success event

\[
E_\tau=D_\tau^c.
\]

This is increasing, deterministic given the percolation configuration, and satisfies `P(E_tau)>=1-epsilon_h`, so it is a fully source-admissible event family.

Let `C_h` be the event that the root reaches at least one boundary leaf. Let `F_h` be the source failure event: `C_h` occurs and **every** connected boundary leaf `tau` satisfies `D_tau`. Put

\[
c_h=\Pr(C_h),\qquad f_h=\Pr(F_h),\qquad R_h=f_h/c_h
\]

whenever `c_h>0`.

The counterexample hope is that one can choose a finite module and local gates so that `epsilon_h=delta^h ->0` but `R_h` stays bounded away from zero.

## 3. Exact recursion

Put

\[
G(x)=\mathbb E[x^K],\qquad \mu=\mathbb E K,\qquad \sigma^2=\operatorname{Var}(K).
\]

Use the depth-zero convention `c_0=f_0=1`, `q_0:=1-c_0=0`. Then the no-connection probability satisfies the exact Galton--Watson recursion

\[
q_{h+1}=G(q_h).
\tag{3.1}
\]

For a top-module configuration, write

\[
a_i={\bf1}_{A_i},\qquad L=\sum_{i\in S}a_i.
\]

A connected top port `i` is harmless for global failure if its child subtree has no depth-`h` boundary connection (probability `q_h`). If the child does connect, it must itself fail (probability `f_h`) **and** the top gate `A_i` must occur. Independence of the child copies therefore gives the exact recursion

\[
\boxed{
 f_{h+1}
 =
 \mathbb E\left[
 \prod_{i\in S}(q_h+a_i f_h)-q_h^K
 \right].
}
\tag{3.2}
\]

The subtraction removes the case in which every active child has no boundary connection.

This identity is the finite-state boundary process for the recursive-module counterexample compiler; no simulation enters.

## 4. Method #12 — the conserved quantity is the offspring mean plus Harris gate mass

### Theorem 4.1 (recursive multiplicative-gate no-go)

For every finite rooted port module `H`, every `p in (0,1)`, and every local decreasing gate family satisfying (2.1),

\[
\boxed{R_h\longrightarrow0\qquad(h\to\infty).}
\tag{4.1}
\]

Thus this entire self-similar multiplicative-gate architecture cannot refute Flammant's conjecture.

More quantitatively:

1. If `0<mu<1`, then
   \[
   R_h
   \le
   \delta^h\left[
   \mu^h+\frac{\sigma^2(1-\mu^h)}{\mu(1-\mu)}
   \right].
   \tag{4.2}
   \]
2. If `mu=1`, then
   \[
   R_h\le\delta^h(1+h\sigma^2).
   \tag{4.3}
   \]
3. If `mu>1`, then there exist constants `C<infinity` and `beta in (0,1)`, depending only on the finite module and the local gates, such that
   \[
   R_h\le C\,\beta^h.
   \tag{4.4}
   \]
   Since `epsilon_h=delta^h`, this is equivalently a positive-power bound
   \[
   R_h\le C'\,\varepsilon_h^{\kappa},
   \qquad
   \kappa=\frac{\log\beta}{\log\delta}>0.
   \tag{4.5}
   \]

If `mu=0`, then there is no positive-depth boundary connection and the source conditional statement is vacuous.

### Proof: subcritical and critical cases

Because `f_h<=c_h=1-q_h`, every factor in (3.2) satisfies

\[
0\le q_h+a_i f_h\le q_h+f_h\le1.
\]

Telescoping the product gives pointwise

\[
\prod_{i\in S}(q_h+a_i f_h)-q_h^K
\le
f_h\sum_{i\in S}a_i.
\tag{4.6}
\]

For each port `i`, `{i in S}` is increasing and `A_i` is decreasing. Harris therefore gives

\[
\Pr(i\in S, A_i)
\le
\Pr(i\in S)\Pr(A_i)
\le
\delta\Pr(i\in S).
\tag{4.7}
\]

Summing over ports,

\[
\mathbb E L\le\delta\mathbb E K=\delta\mu.
\tag{4.8}
\]

Combining (3.2), (4.6), and (4.8),

\[
\boxed{f_{h+1}\le\delta\mu f_h,}
\qquad
f_h\le(\delta\mu)^h.
\tag{4.9}
\]

Now interpret `c_h` as the survival probability to generation `h` of the Galton--Watson process with offspring law `K`, started from one particle. Let `Z_h` be its population. Then

\[
\mathbb E Z_h=\mu^h.
\]

If `0<mu<1`, the standard second-moment recursion, obtained directly from conditioning on generation `h`, gives

\[
\operatorname{Var}(Z_h)
=
\sigma^2\mu^{h-1}\frac{1-\mu^h}{1-\mu}.
\tag{4.10}
\]

Paley--Zygmund at threshold zero yields

\[
c_h=\Pr(Z_h>0)
\ge
\frac{(\mathbb E Z_h)^2}{\mathbb E Z_h^2}.
\tag{4.11}
\]

Insert (4.9)--(4.10) into `R_h=f_h/c_h` to obtain exactly (4.2), which tends to zero because `delta<1`.

If `mu=1`, then

\[
\operatorname{Var}(Z_h)=h\sigma^2,
\]

so (4.11) gives

\[
c_h\ge\frac1{1+h\sigma^2}.
\]

Together with `f_h<=delta^h`, this proves (4.3).

### Proof: supercritical case

Assume `mu>1`. Let `q<1` be the extinction probability, the smallest fixed point of

\[
G(q)=q,
\]

and put

\[
c=1-q>0.
\]

The finite-depth extinction probabilities satisfy `q_h ↑ q`, hence `c_h ↓ c`.

For `u,t>=0`, define

\[
\Phi_u(t)
=
\mathbb E\left[
 (u+t)^L u^{K-L}-u^K
\right].
\tag{4.12}
\]

Equation (3.2) is

\[
f_{h+1}=\Phi_{q_h}(f_h).
\tag{4.13}
\]

For fixed `K,L,t`, the summand

\[
u^{K-L}\big((u+t)^L-u^L\big)
\tag{4.14}
\]

is nondecreasing in `u>=0`: both factors are nonnegative and nondecreasing. Therefore

\[
f_{h+1}\le\Phi_q(f_h).
\tag{4.15}
\]

As a function of `t`, `Phi_q(t)` is a polynomial with nonnegative coefficients and zero constant term. Thus it is convex, and `Phi_q(t)/t` is nondecreasing for `t>0`.

At the survival scale `t=c=1-q`,

\[
\Phi_q(c)
=
\mathbb E[q^{K-L}-q^K].
\tag{4.16}
\]

Since `G(q)=q`,

\[
c=1-q=\mathbb E[1-q^K].
\tag{4.17}
\]

Hence, with the natural convention `0^0=1`,

\[
c-\Phi_q(c)
=
\mathbb E[1-q^{K-L}].
\tag{4.18}
\]

This quantity is strictly positive. Indeed, `mu>1` implies that some port `i` has `P(i in S)>0`. Because `P(A_i)<=delta<1`, the complement `A_i^c` has positive probability and is increasing. Both `{i in S}` and `A_i^c` are increasing, so Harris gives

\[
\Pr(i\in S,A_i^c)
\ge
\Pr(i\in S)\Pr(A_i^c)>0.
\tag{4.19}
\]

On this event `K-L>=1`, making the expectation in (4.18) positive (for `q=0`, (4.16)--(4.18) reduce to the same statement that not all connected-port gates are always true).

Therefore

\[
\alpha:=\frac{\Phi_q(c)}c<1.
\tag{4.20}
\]

By continuity choose `eta>0` so small that

\[
\beta:=\frac{\Phi_q(c+\eta)}{c+\eta}<1.
\tag{4.21}
\]

Because `Phi_q(t)/t` is nondecreasing,

\[
\Phi_q(t)\le\beta t
\qquad(0\le t\le c+\eta).
\tag{4.22}
\]

Also `f_h<=c_h` and `c_h->c`, so for all sufficiently large `h`, `f_h<=c+eta`. Then (4.15) and (4.22) give

\[
f_{h+1}\le\beta f_h.
\]

Thus `f_h<=C beta^h` after absorbing the finite initial segment into `C`. Since `c_h>=c>0`, (4.4) follows. Equation (4.5) is just `beta^h=(delta^h)^{log beta/log delta}`. This proves the theorem. `square`

## 5. What the theorem does and does not say

This is **not** a proof of Flammant's conjecture on recursively constructed graphs with arbitrary admissible kernels. It treats a large, natural counterexample compiler: fixed independent copies of a finite module, with each leaf's rare decreasing failure equal to a product/intersection of local decreasing gates along its ancestral module path.

That distinction matters. The full source permits `q_b` to depend globally on all graph edges. C073 already showed that projecting a general increasing observable onto a connected cluster can destroy monotonicity. C078 showed separately that a raw root-branch count can have a bad constant lower-tail mode under common-gate dependence. Those global/shared dependencies lie outside Theorem 4.1.

The theorem nevertheless rules out the most obvious way to turn C075's recursive tree-spine power obstruction into an actual counterexample. **Independent self-similar module amplification cannot maintain positive conditional failure.** In subcritical/critical recursion Harris kills failure by a factor `delta` per level; in supercritical recursion the fixed-point survival mass creates a strict convex contraction because at least one reachable port sometimes has its local bad gate fail.

So any future source-valid counterexample must exploit dependence that does not factor through independent module levels: shared edges/gates across levels, nonlocal label switching, or some other global mechanism. Conversely, a proof may try to show that arbitrary global kernels admit a controlled approximation by a finite number of such hierarchical pieces, but C073's projection counterexample shows that this approximation must retain more state than the root cluster alone.

No exact-arithmetic artifact is added in this run because there is no finite enumerative or numerical claim to certify: Theorem 4.1 is an all-finite-module analytic theorem and its full proof is on the page. This is deliberately not another checker-only run.

## 6. G0004 lifecycle: third stuck episode means mandatory handoff

Despite Theorem 4.1, the fixed source-wide quantity has not moved:

\[
U_F:1\to1.
\]

After recovery 2/2, the substantive sequence is therefore:

- C077: unchanged count 1;
- C078: unchanged count 2;
- C079: unchanged count 3.

This is the third Section-I stuck episode on G0004. The owner protocol explicitly permits at most two recoveries on the same HARD assignment. I therefore **do not** open `STUCK_RECOVERY_3`, do not write another G0004 lemma, and do not leave the canonical claim falsely active.

I released G0004 in `operations/claims/G0004.md` at commit

`70155fb23bac6ef0f0ed9c7a068cb6b969b61208`.

The release preserves the full C069--C079 chain, the exact remaining obstruction, and the frozen metric `U_F=1` for future reassignment.

## 7. Lawful HARD successor: H0021 is released, source-current-looking, and ownership-clear

The current queue itself has no blanket READY inventory, so I did not promote a PENDING row by fiat. Instead I used an already canonical released HARD claim whose source and metric are frozen:

**H0021 — Cohen Antonir, Lichev, Zhukovskii, Conjecture 1.4, sharp bounded-degree tree universality.**

The canonical H0021 history says:

- `UNASSIGNED AFTER R16 HANDOFF` before this run;
- source OPEN/PARTIAL in bounded checks;
- exact target: for every fixed `epsilon>0` and `Delta>=2`, whp `G(n,(1+epsilon) log n/n)` contains every `n`-vertex tree of maximum degree at most `Delta`;
- frozen metric `Delta_near=2`;
- first unresolved milestone `Delta_near>=3`;
- R16 exhausted its own two recoveries and released the target for future reassignment with a genuinely fresh route.

I reread the complete R16 handoff

`runs/R16/2026-09-18T00-46-50Z_h0021-spread-capacity-handoff-h0022_91e4.md`

at commit `0f75de572f7fe23d01f011bb0204f54a5a2b7dd8` rather than restarting from the source paper.

Durable inherited state includes the sharp-density almost-spanning reduction, the `q>=m/|X|` spread-capacity lemma, the full-tree spread obstruction, the fixed-Hamilton-skeleton support obstruction, and the surviving fact that a genuinely global residual support has enough first-moment spread capacity in principle.

A fresh 2026-09-19 source check again found arXiv:2608.06358 and its explicit Conjecture 1.4, with no later primary source found in the bounded exact-title / author / conjecture search claiming the sharp theorem.

I reassigned the released claim to R17 at commit

`9e43552284fb230961e070c03fcaec0be79f1734`.

The inherited metric is **not reset**:

\[
\boxed{\Delta_{\rm near}=2.}
\]

R16's historical six-run unchanged streak and two recoveries remain preserved as R16 history. R17's own H0021 substantive stagnation/recovery counters are **NOT STARTED** until its first substantive H0021 research run.

## 8. Fresh H0021 route reserved for the next R17 run

R16 used H0021 method numbers

`{1,2,3,4,5,6,7,9,10,11,12,13,18,19,20,21,22,24,25,27,30}`.

The unused numbers are

`{8,14,15,16,17,23,26,28,29}`.

The first R17/H0021 substantive run is therefore reserved as **#8 / #23 / #28**:

- **#8 DISCRETIZE:** formulate a finite bucketed state for a leaf-stripped subcubic tree plus a reservoir boundary, rather than another fixed Hamilton-block or linking-system state.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** deliberately avoid the source paper's linking-system machinery; stress-test a Posa-rotation / reservoir-absorption embedding architecture and try to construct a bounded-degree tree family that breaks it before proving anything.
- **#28 FOR TYPICAL:** seek a typical-embedding/reservoir statement whose failure entropy is low enough to union over a compressed family of subcubic cores, then identify exactly what must be strengthened to recover simultaneous universality.

The standing counterexample-first rule remains mandatory even though R16 already used method #2 on a different architecture.

## 9. Model / reasoning / scheduler-control truth

Actual model visible in this run: **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort telemetry, so reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The scheduler/task-control surface exposed to this runtime provides task identity/title, prompt, schedule/timing, enabled-state operations and ordinary task updates, but it exposes **no bindable model-family selector, no bindable reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guarantee of hour-long execution**. Thus the requested `GPT-6 / maximum` remains prompt text only on this surface. Changing that would require a product/API/admin scheduler surface that actually exposes those fields and runtime attestation.

The historical P26 `You cannot modify this task` event is not a current universal impossibility: root `RESULTS.md` records that a later full P26 update succeeded from another authorized context. The lawful workaround for a protected task is therefore the owning/authorized account/workspace/admin/API context, an explicit ownership transfer, or platform support — not task duplication or permission bypass.

Per the present deployment boundary I made **no scheduler change**, no workflow execution, no permission change, no email/Drive action, no purchase, and no public posting.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R17
  lane: HARD OUTSIDE
  actual_model: "GPT-5.6 Sol"
  reasoning: "UNVERIFIED"
  outgoing_target: G0004
  outgoing_source: "Flammant arXiv:2609.03492, Conjecture 2.2"
  outgoing_metric: U_F
  metric_before: 1
  metric_after: 1
  movement: false
  post_recovery2_substantive_unchanged_before: 2
  post_recovery2_substantive_unchanged_after: 3
  recoveries_consumed: "2/2"
  lifecycle_after: "HANDOFF_RELEASED"
  methods_this_run: [7, 12, 24]
  method_note: "all 30 G0004 Section-B numbers had already been used; this is a new combination, not falsely labelled unused"
  new_partial_result: "recursive finite-module multiplicative local-gate architecture has R_h -> 0; cannot produce a Flammant counterexample"
  g0004_release_commit: "70155fb23bac6ef0f0ed9c7a068cb6b969b61208"
  incoming_target: H0021
  incoming_source: "Cohen Antonir--Lichev--Zhukovskii arXiv:2608.06358v1, Conjecture 1.4"
  incoming_metric: Delta_near
  inherited_value: 2
  first_unresolved_milestone: 3
  r17_h0021_stagnation: "NOT STARTED"
  r17_h0021_recoveries: "NOT STARTED"
  h0021_claim_commit: "9e43552284fb230961e070c03fcaec0be79f1734"
  next_methods: [8, 23, 28]
  predecessor_frozen:
    binary_lcs_width: "0.033609950762282626"
    d0064_R_class: "0/3"
  shared_root_ledgers_edited: false
  peer_files_edited: false
  scheduler_modified: false
  email_or_drive: false
  public_posting: false
```

## 11. Next invocation

Do not return to G0004 unless it is later explicitly reassigned after this release. Start from the R16 H0021 handoff and the R17 H0021 claim above. The first research action is to **try to break** the new Posa/reservoir architecture on adversarial subcubic tree families; only after that exact obstruction search fails should the run attempt a sharp-density embedding theorem. Track only `Delta_near`, with inherited value `2`, and do not count an almost-spanning theorem or a theorem at coefficient `C>1` as movement.
