Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #14, #26, #10.**

# R09 — Blanc-Renaudie mean-field `d=7,8,9,10`: exact F2 orbit bridge and a deterministic full-chain singleton gateway

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime truth, continuity, and source/current-status check

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long execution guarantee.

The task-management surface exposed to this worker still has no binding model-family selector and no binding reasoning-effort selector. It exposes task text/title, timing/schedule, enabled state and timing mode. Therefore GPT-6/maximum remains prompt text only here. The historical P26 `You cannot modify this task` event was later superseded by a successful P26 update from another authorized context; R-series edits were denied from that P/C context. An actual denial must be resolved through the owning/authorized context, authorized admin/ownership transfer, or platform support, not by duplication or permission bypass. No scheduler modification was attempted in this run.

Before research I recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active exclusive R09 claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the newest complete own report `runs/R09/20260918T1932Z_blanc_direct_bridge_mixing_6d13a8.md`, neighboring admission reports confirming that this Blanc-Renaudie target is already R09-owned, and the `probability_1000_intake_I_20260914/problems.jsonl` ledger. The newest historical Tang handoff records `TANG-2020-Q4.11` as `RETIRED_FROZEN_REFUTED`; G0013 and the Chen-Wang Gaussian-subuniformity successor remain retired/frozen. I did not reopen any of them.

The active source remains Arthur Blanc-Renaudie, *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764v1 (submitted 2026-09-17; PDF dated 2026-09-18). The source records nearest-neighbor `d>=11` as known and `7<=d<=10` as the remaining unresolved numerical-proof regime, and Theorem 1.1 makes the critical asymptotic equivalent to a computably checkable subcritical initialization condition. A bounded dated exact-title/arXiv-ID/current-author search on 2026-09-18 recovered the source and no later source-matching resolution. This is bounded negative evidence only, not a worldwide novelty certificate.

The frozen source metric remains

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous Blanc-Renaudie Theorem 1.1(a) certificate is obtained}\}.
\]

No dimension is certified here:

\[
\boxed{M_A:0\longrightarrow0.}
\]

The stagnation count remains **UNKNOWN**; I do not reconstruct it from partial root history.

The preceding R09 report proposed methods `#16/#24/#10`, but `#16` and `#24` had already been used earlier on this same Blanc-Renaudie target. The owner's freshness rule therefore overrides that stale proposal. This run uses three genuinely fresh moves for this target: **#14 FIND THE GROUP ACTING, #26 HUNT THE SPORADIC CASE, #10 DERANDOMIZE.**

---

## 2. Source notation and the finite family F2

Work in nearest-neighbor bond percolation on `Z^d`, and write

\[
m:=\Omega=2d.
\]

A live pointed cluster is `\vec A=(A,\vec a)` with oriented boundary edge `\vec a=(a^-,a^+)` and displacement

\[
\delta(\vec A):=a^+-a^-\in\{\pm e_1,\ldots,\pm e_d\}.
\]

The source's cut relation is

\[
(\vec A,\vec B)\in C_{\rm cut}
\quad\Longleftrightarrow\quad
b^-\notin B\operatorname{off}_0(A-a^+),
\tag{2.1}
\]

where `B off_0 S` denotes the connected component of the origin in `B\setminus S`. Write

\[
R(A,B):=\mathbf 1_{(A,B)\notin C_{\rm cut}}.
\]

The iid pointed-cluster law in the source is

\[
\pi(B)=\frac{\mu_p(B)}{m\chi(p)},
\tag{2.2}
\]

where `\mu_p(B)=P_p(C(0)=B)`.

Let `F_2` be the finite family of all live pointed states whose underlying cluster has one or two vertices. Put

\[
u:=(1-p)^m,
\qquad
v:=p(1-p)^{2m-2}.
\tag{2.3}
\]

Thus a singleton cluster has raw probability `u` and a fixed nearest-neighbor two-vertex cluster has raw probability `v`.

For bookkeeping below define the raw weight

\[
w(B):=\mu_p(B),\qquad B\in F_2.
\]

---

## 3. Method #14 — FIND THE GROUP ACTING: the whole F2 bridge problem collapses to m directions

The hyperoctahedral group of the lattice acts transitively on the `m=2d` coordinate directions. The key point is stronger than generic symmetry: on `F_2` the exact source cut relation itself depends only on the source displacement direction and whether the target has its pointed tail at the nonzero cluster vertex.

### Lemma 3.1 — exact specialization of the source cut relation on F2

Let `A,B\in F_2` and put `a=\delta(A)`. If `B` is a singleton, or if `B` has two vertices and pointed tail `b^-=0`, then `R(A,B)=1`.

If `B` has two-vertex cluster `\{0,e\}` and pointed tail `b^-=e`, then

\[
\boxed{R(A,B)=0\iff e=-a.}
\tag{3.1}
\]

#### Proof

If `b^-=0`, the target tail is the origin, and the origin necessarily belongs to `B\operatorname{off}_0(A-a^+)`, so the pair is non-cut.

Now let `B=\{0,e\}` with tail `b^-=e`. Deleting vertices from a two-vertex connected cluster disconnects `e` from `0` exactly when `e` itself is deleted. Hence by (2.1)

\[
R(A,B)=0\iff e\in A-a^+
\iff a^++e\in A.
\tag{3.2}
\]

If `A=\{0\}`, then `a^-=0`, `a^+=a`, and (3.2) says `a+e=0`, i.e. `e=-a`.

If `A=\{0,f\}`, there are two possible pointed tails. If `a^-=0`, then `a^+=a`, and the condition `a+e\in\{0,f\}` cannot equal `f` because a sum of two coordinate unit vectors is never itself a coordinate unit vector; hence again it can only be `0`, giving `e=-a`. If `a^-=f`, then `a^+=f+a`, and `f+a+e\in\{0,f\}`. Equality to `0` would make a sum of three coordinate unit vectors zero, impossible in the nearest-neighbor lattice with `a\ne-f` because the pointed edge is live; equality to `f` gives `a+e=0`, hence `e=-a`. This proves (3.1). `square`

### Lemma 3.2 — exact direction mass

For every coordinate direction `b`, the total raw weight of states in `F_2` with displacement `b` is

\[
\boxed{g:=u+2(m-1)v.}
\tag{3.3}
\]

#### Proof

There is one singleton pointed state of direction `b`, contributing `u`. For each of the `m` two-vertex clusters `\{0,f\}`, there are potentially two pointed tails. Tail `0` allows direction `b` unless `b=f`; tail `f` allows direction `b` unless `b=-f`. Thus exactly `2(m-1)` live two-vertex pointed states have direction `b`, each of weight `v`. `square`

Fix a representative source direction `a`. Define the direction-lumped weighted one-step kernel

\[
K_{ab}
:=
\sum_{\substack{B\in F_2\\\delta(B)=b}}w(B)R(A,B),
\tag{3.4}
\]

where by Lemma 3.1 the row depends only on `a=\delta(A)`.

### Proposition 3.3 — rank-two directional kernel

For all directions `a,b`,

\[
\boxed{
K_{ab}=\begin{cases}
g,&a=b,\\
g-v,&a\ne b.
\end{cases}}
\tag{3.5}
\]

Equivalently,

\[
\boxed{K=(g-v)J_m+vI_m.}
\tag{3.6}
\]

Its common row sum is

\[
\boxed{r:=mg-(m-1)v=m(g-v)+v.}
\tag{3.7}
\]

#### Proof

For a fixed target direction `b`, all singleton targets and all two-vertex targets with tail `0` are non-cut. By Lemma 3.1 the only missing target can be the unique nonzero-tail two-vertex target whose tail equals `-a`. That missing state has displacement different from `a`: if its cluster edge is `e=-a`, then a nonzero-tail live pointed edge cannot point back to the origin, so its displacement is any direction except `a`. Therefore no weight is removed from the `b=a` direction class, while exactly one weight `v` is removed from every other direction class. This is (3.5). Summing a row gives (3.7). `square`

This is a complete group quotient of the two-step intermediate dynamics. In particular

\[
K^2=QJ_m+v^2I_m,
\qquad
Q:=m(g-v)^2+2v(g-v).
\tag{3.8}
\]

---

## 4. Method #26 — HUNT THE SPORADIC CASE: the unique worst orbit is the direct-cut aligned orbit

The finite direct-bridge criterion introduced in the preceding R09 report asks for pointwise control of three-transition raw bridge masses. On `F_2`, the symmetry quotient lets us solve the entire extremal problem exactly.

For an endpoint `B\in F_2`, define its raw incoming mass

\[
c(B):=\sum_{A\in F_2}w(A)R(A,B).
\tag{4.1}
\]

If `B` is a singleton or a two-vertex state with tail `0`, call it an **H endpoint**. If `B` has cluster `\{0,e\}` and tail `e\ne0`, call it an **L_e endpoint**. Lemma 3.1 gives

\[
\boxed{
c(B)=\begin{cases}
mg,&B\in H,\\
(m-1)g,&B\in L_e.
\end{cases}}
\tag{4.2}
\]

For `A,B\in F_2`, define the raw three-transition bridge mass

\[
M(A,B)
:=
\sum_{C,D\in F_2}
 w(C)w(D)R(A,C)R(C,D)R(D,B).
\tag{4.3}
\]

The source and endpoint weights cancel in the normalized bridge ratio, so define

\[
\Gamma_{F_2}(A,B)
:=\frac{M(A,B)}{r\,c(B)}.
\tag{4.4}
\]

### Proposition 4.1 — exact three-class bridge spectrum

Let `a=\delta(A)`. Then:

1. If `B\in H`,
\[
\Gamma_H=\frac{r}{mg}.
\tag{4.5}
\]

2. If `B\in L_e` and `e=-a` (the direct-cut aligned orbit),
\[
\boxed{
\Gamma_{\rm align}=\gamma_{F_2}
:=
\frac{(g-v)[m(g-v)+2v]}{gr}.
}
\tag{4.6}
\]

3. If `B\in L_e` and `e\ne-a`,
\[
\Gamma_{\rm non}
=\gamma_{F_2}+\frac{v^2}{g(m-1)r}.
\tag{4.7}
\]

Moreover

\[
\boxed{
\Gamma_H-\gamma_{F_2}=\frac{v^2}{gmr}>0,
}
\tag{4.8}
\]

so the global minimum is exactly the aligned direct-cut orbit:

\[
\boxed{
\min_{A,B\in F_2}\Gamma_{F_2}(A,B)=\gamma_{F_2},
}
\tag{4.9}
\]

with equality exactly when the endpoint is an `L_e` state with `e=-\delta(A)`.

#### Proof

For an H endpoint, the final transition `D\to B` is always non-cut, hence summing the first two transitions gives

\[
M(A,B)=r^2.
\]

Together with `c(B)=mg`, this gives (4.5).

For an `L_e` endpoint, the final transition is forbidden precisely when `\delta(D)=-e`. The total first-two-step mass landing in direction `-e` is `(K^2)_{a,-e}`. Hence

\[
M(A,B)=r^2-(K^2)_{a,-e}.
\tag{4.10}
\]

By (3.8),

\[
(K^2)_{a,-e}=Q+v^2\mathbf 1_{a=-e}.
\]

Using `c(B)=(m-1)g`, this gives two L classes. Since

\[
r^2-Q=(m-1)(g-v)[m(g-v)+2v],
\tag{4.11}
\]

the aligned class yields (4.6), and the nonaligned class exceeds it by exactly the quantity in (4.7).

Finally a direct simplification of (4.5)-(4.6) gives (4.8). All denominators are positive for `0<p<1`, so the inequalities are strict. `square`

### Corollary 4.2 — exact finite-core bridge minorization

Let `J_{F_2}(A,B)` and `\nu_{F_2}^{\uparrow},\nu_{F_2}^{\downarrow}` be the finite-core analogues of the raw three-transition joint mass and one-step endpoint masses from the preceding R09 report. Then

\[
\boxed{
J_{F_2}(A,B)
\ge
\gamma_{F_2}\,
\nu_{F_2}^{\uparrow}(A)
\nu_{F_2}^{\downarrow}(B)
\qquad(A,B\in F_2),
}
\tag{4.12}
\]

and equality occurs exactly on the aligned direct-cut orbit. Thus the normalized finite-core bridge-overlap statistic is exactly `1` when `\gamma=\gamma_{F_2}`.

This is the precise sporadic/extremal geometry that the previous run only proposed searching for: the worst bridge pair is not an exotic large cluster but, inside `F_2`, exactly the pair that is itself a one-step cut transition.

### Exact calibration values

At the deliberately noncritical calibration

\[
p=\frac1{4d}=\frac1{2m},
\]

the exact-arithmetic checker gives

\[
\begin{array}{c|c}
d&\gamma_{F_2}\\ \hline
7&0.986603505857357\ldots\\
8&0.988267405422844\ldots\\
9&0.989563849320008\ldots\\
10&0.990602407751552\ldots
\end{array}
\tag{4.13}
\]

The theorem itself is algebraic in `p` and is not restricted to these calibration values.

---

## 5. Method #10 — DERANDOMIZE: a deterministic two-singleton gateway for the full infinite chain

The finite-core result above is strong internally, but a fixed small core has vanishing stationary mass as `\chi(p)` becomes large. Before discarding the idea, it is useful to ask whether the same geometry yields a deterministic bridge in the full state space.

For each coordinate direction `c`, let `O_c` denote the live singleton pointed state with cluster `\{0\}` and pointed edge `(0,c)`. By (2.2),

\[
\pi(O_c)=\frac{u}{m\chi(p)}.
\tag{5.1}
\]

### Lemma 5.1 — at most one bad singleton predecessor for any endpoint

For every live pointed cluster `B=(B,\vec b)`, at least `m-1` directions `d` satisfy

\[
R(O_d,B)=1.
\tag{5.2}
\]

#### Proof

If `b^-=0`, all `m` singleton predecessors are non-cut because the target tail is the origin.

Assume `b^-\ne0`. Choose a shortest lattice path in the connected cluster `B` from `0` to `b^-`. A shortest path contains exactly one neighbor of the origin: its first step. Indeed, if a later vertex of the path were also adjacent to `0`, replacing the initial segment by that edge would shorten the path.

For the singleton `O_d`, the deleted translated source cluster in (2.1) is the single vertex `\{-d\}`. If `-d` is not the first step of the chosen shortest path, deleting `-d` leaves that entire path from `0` to `b^-` intact. Hence at most one direction `d` can fail (5.2), so at least `m-1` work. `square`

### Theorem 5.2 — deterministic full-chain three-transition bridge

For arbitrary live endpoints `A,B` of the full pointed-cluster chain,

\[
\boxed{
J_A(B)
\ge
\gamma_{\rm sing}(p)\,
\nu^\uparrow(A)\nu^\downarrow(B),
}
\tag{5.3}
\]

where

\[
\boxed{
\gamma_{\rm sing}(p)
=
\frac{m-1}{m}\frac{u^2}{\chi(p)^2}
=
\frac{m-1}{m}
\frac{(1-p)^{2m}}{\chi(p)^2}.
}
\tag{5.4}
\]

Consequently the direct bridge-overlap functional from the previous R09 report satisfies exactly

\[
\boxed{
\mathcal B_{\gamma_{\rm sing}}(A)
=
\gamma_{\rm sing}\,
\nu^\uparrow(A)Z
\qquad\text{for every live }A.
}
\tag{5.5}
\]

#### Proof

The transition `A\to O_c` is non-cut for every `c`, because the target tail of `O_c` is `0`. Likewise every `O_c\to O_d` is non-cut. By Lemma 5.1, for a fixed endpoint `B`, at least `m-1` choices of `d` make `O_d\to B` non-cut, and for each such `d` there are all `m` choices of `c`.

Therefore the portion of the raw three-transition joint mass using two singleton intermediate states is at least

\[
J_A(B)
\ge
\pi(A)\pi(B)\,m(m-1)
\left(\frac{u}{m\chi(p)}\right)^2
=
\pi(A)\pi(B)
\frac{m-1}{m}\frac{u^2}{\chi(p)^2}.
\tag{5.6}
\]

Since `\nu^\uparrow(A)\le\pi(A)` and `\nu^\downarrow(B)\le\pi(B)`, (5.3) follows. Then every term in the minimum defining `\mathcal B_{\gamma_{\rm sing}}` equals its second argument, which gives (5.5). `square`

This theorem is fully source-valid and does not use the unknown Perron eigenfunction, local modifications, typical-state assumptions, or truncation tails.

---

## 6. Why this still does not certify Theorem 3.14 — and why that is useful information

Theorem 3.14 requires a contraction base `c<1` depending only on the fixed source parameters `(d,L,C)` once `\chi(p)` is sufficiently large. The deterministic singleton coefficient (5.4) behaves like

\[
\gamma_{\rm sing}(p)=O(\chi(p)^{-2}),
\]

so it collapses precisely in the large-susceptibility regime where the theorem needs a uniform contraction. Thus (5.3) is a rigorous full-chain bridge, but it is too weak to replace the source's constant-mass typical-state local-modification mechanism.

The finite `F_2` coefficient, by contrast, is excellent: at the calibration above it is about `0.99`. But its total iid pointed-state mass is exactly

\[
\pi(F_2)
=
\frac{mg}{m\chi(p)}
=
\boxed{\frac{g}{\chi(p)}}.
\tag{6.1}
\]

Hence every **fixed** finite pointed-cluster family has total mass `O(1/\chi(p))` as `\chi(p)\to\infty`. This produces the central negative conclusion of the run:

> **A fixed-size cluster core cannot by itself yield the uniform regeneration required by Blanc-Renaudie's Theorem 3.14, no matter how close to one its internal bridge coefficient is.**

So simply enumerating `F_3,F_4,\ldots` at a fixed cutoff is the wrong next route. A successful finite-computation replacement must be **size-adaptive with p** or must quotient typical large clusters by a bounded-complexity signature whose mass stays order one.

This is the actual movement in understanding despite the frozen source metric: the previous abstract direct-bridge criterion now has an exactly solved smallest core, an exactly identified worst orbit, and a proof that fixed finite cores cannot solve the source's uniform-mixing requirement.

---

## 7. Exact checker

A substantive exact finite claim was isolated, so I built one checker only after the mathematics above was in place.

Artifacts:

- `artifacts/R09/20260918T2038Z_blanc_F2_orbit_bridge_81d5e3.py`
- `artifacts/R09/20260918T2038Z_blanc_F2_orbit_bridge_81d5e3.out`

The checker uses Python `Fraction` throughout. For each `d=7,8,9,10` it:

1. enumerates every live pointed state in `F_2`;
2. implements the exact source cut relation specialized to this family;
3. verifies the direction multiplicities and one-step target counts;
4. reconstructs `K=(g-v)J+vI` from enumeration;
5. verifies the two classes of incoming mass `c(B)`;
6. exhausts every source direction and every endpoint state;
7. verifies that the exact minimum bridge ratio is (4.6), with equality only on the aligned direct-cut orbit;
8. verifies the exact positive gaps (4.7)-(4.8).

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

The calibration exact rational values are preserved in the output rather than rounded in the theorem statement.

---

## 8. Prior-art and novelty discipline

The group-lumping idea, Doeblin/minorization philosophy, finite-state Perron methods, and use of symmetry to quotient Markov kernels are classical/folklore mechanisms. I do **not** claim novelty for those mechanisms.

The claims made in this report are narrower and source-specific: the exact `F_2` specialization of Blanc-Renaudie's cut relation, the closed-form bridge spectrum (4.5)-(4.8), identification of the direct-cut aligned orbit as the unique finite-core minimizer, and the deterministic full-chain singleton gateway (5.3). A bounded current-source search did not reveal these formulas, but priority remains **unverified pending independent audit and a broader literature check**.

No source-level theorem is called proved here.

---

## 9. Status and next attack

The honest state remains **PARTIAL / OPEN**:

\[
\boxed{M_A=0.}
\]

No dimension `7,8,9,10` has a complete initialization certificate, and nothing in this report is promoted to source closure.

The next obligation is no longer “enumerate a larger fixed cluster family.” It is:

\[
\boxed{
\text{find a size-adaptive or bounded-signature typical-state quotient with }\Theta(1)
\text{ mass and a uniform bridge overlap.}
}
\]

The next fresh Section-B triple is **#1/#12/#27**:

- **#1 CHANGE THE CATEGORY:** recast the typical pointed-cluster bridge problem as a finite separator/flow or information-compression problem on cluster boundary signatures rather than as cluster enumeration;
- **#12 FIND WHAT IS CONSERVED:** search for a bounded local signature of a pointed cluster whose bridge mass is stable under the killed-chain transitions and whose total `\pi`-mass does not vanish with `\chi`;
- **#27 SWAP THE QUANTIFIERS:** allow a computably growing family or quotient `F(p)` depending on the proposed subcritical initialization point while seeking one **uniform** bridge constant, rather than demanding one fixed finite family work for all large `\chi`.

If the metric remains unchanged for enough **supported** runs, the owner's stuck/retirement protocol will apply; the stagnation count itself remains UNKNOWN until supported continuity fixes it.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R09
  lane: CLOSABLE OUTSIDE
  active_source: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  source_arxiv: 2609.20764
  metric_name: M_A
  metric_before: 0
  metric_after: 0
  movement: false
  stagnation_count: UNKNOWN
  status: PARTIAL_OPEN
  methods_used: [14, 26, 10]
  methods_previous: [6, 13, 28]
  new_results:
    - exact specialization of source C_cut relation on F2
    - exact hyperoctahedral direction quotient K=(g-v)J+vI
    - exact F2 bridge spectrum and unique aligned direct-cut minimizer
    - deterministic full-chain two-singleton bridge coefficient ((m-1)/m)*(1-p)^(2m)/chi(p)^2
    - obstruction: every fixed finite pointed-cluster family has O(1/chi) iid mass, so fixed-size cores cannot supply uniform mixing
  finite_numeric_claim_this_run: true
  checker_created: true
  checker_paths:
    - artifacts/R09/20260918T2038Z_blanc_F2_orbit_bridge_81d5e3.py
    - artifacts/R09/20260918T2038Z_blanc_F2_orbit_bridge_81d5e3.out
  checker_result: ALL_EXACT_CHECKS_PASS
  dimension_certified: []
  source_closed: false
  next_methods: [1, 12, 27]
  next_obligation: size-adaptive or bounded-signature typical-state quotient with order-one mass and uniform bridge overlap
  tang_status: RETIRED_FROZEN_REFUTED
  g0013_status: RETIRED_FROZEN
  chen_wang_status: RETIRED_FROZEN_HANDOFF
  shared_root_edits: false
  peer_file_edits: false
  scheduler_change: false
  email_or_drive: false
  public_posting: false
  permission_change: false
  workflow_execution: false
```
