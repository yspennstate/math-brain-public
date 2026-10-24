Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FIXED-METRIC NO MOVEMENT / STRUCTURAL MOVEMENT: frozen `H_{5,5}` interval width `0 -> 0`; full Lyons--Peres Question 6.20 remains PARTIAL; the auxiliary radial shortcut `Phi_V(J) >= phi` moves from CONJECTURAL to REFUTED; methods #7 TAKE THE LIMIT, #15 BREAK THE SYMMETRY, #3 PROVE SOMETHING STRONGER.**

# R06 / I0056 — radial-shortcut refutation and the exact disk-turn obstruction

Repository: private `yspennstate/math-open-problems`, branch `master`.
Worker: R06.
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20, intake `I0056`.

## 1. Source continuity and why this run returns to mathematics

The canonical source statement remains:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The normalization remains the **outer** vertex boundary

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\}.
\]

The frozen regular/co-regular pair is still

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Thus the required fixed metric cannot decrease further. A solved subclass remains PARTIAL for the full source because Question 6.20 also asks for more general transitive plane graphs.

Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art for the triangular and quadrangular regular hyperbolic cases (face/codegrees 3 and 4). They are not relabelled here.

The newest owner directive on current master, `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md`, explicitly supersedes the repeated targetless-admission behavior and requires mathematical progress rather than successive no-target gate reports. I therefore do **not** repeat the preceding R06 `E_ready=0` bookkeeping run. I preserve the posted regular-tessellation result and work only on the still-open second clause, continuing the already established R06 mixed-face route.

The predecessor is

`runs/R06/20260919T2250Z_successor_gate_hard_releases_no_ready_74_e6c1.md`

(created at `5c6c20b00c9492c4ba3f7fd89a03cc8e5b6f7fda`). The exact predecessor-to-prewrite comparison against `12afbe8d13637ea85bbfa19c1b119048cf761641` was `77` commits ahead, `0` behind, with `too_large=null`. The material policy change in that delta is the progress-first directive above.

## 2. Current public-source boundary checked 2026-09-19 UTC

The maintained Lyons--Peres text still prints Question 6.20 in the full form above and annotates Haslegrave--Panagiotis only for codegrees 3 and 4. Haslegrave--Panagiotis explicitly state that their triangular and square hyperbolic equality cases answer those two branches.

Oh, *Sharp isoperimetric inequalities for infinite plane graphs with bounded vertex and face degrees*, arXiv:2009.04394, is an **edge-boundary** theorem and resolves Lyons--Peres Question 6.21; it does not state the mixed-face outer-vertex answer pursued below.

A fresh check also found the September 2026 journal version of D'Achille--Jacquier--Ruszel, *On minimal shapes and isoperimetric constants in hyperbolic lattices*, Discrete Mathematics 349(9), 115188. Its stated scope is regular `{p,q}` hyperbolic tilings and the Haggstrom--Jonasson--Lyons edge constant, not the mixed-face tetrapentagonal graph below.

Bounded exact-title / tetrapentagonal / radial-graph / Cheeger searches did not recover a primary source giving the constant below. This is **bounded negative evidence only**, not a novelty or priority certificate.

## 3. Recovered source-valid mixed-face target

Let

\[
R:=H_{5,4}=\{4,5\}
\]

be the degree-five regular quadrangulation, and let

\[
T:=M(R)=r\{4,5\}
\]

be its medial graph. Then `T` is the 4-regular vertex-transitive tetrapentagonal plane tessellation with alternating face type `[4,5,4,5]`. This is a concrete graph in the **more general transitive plane graph** clause of Question 6.20 and is not co-regular.

The earlier R06 reports proved

\[
\frac4{1+\sqrt3+\sqrt5}
\le \Phi_E(T)\le \frac2{\sqrt5}
\tag{3.1}
\]

and

\[
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)\le \frac2{\sqrt5}.
\tag{3.2}
\]

The edge interval has width about `0.0892934627`. No sampled interval is being promoted into a rigorous bound.

The preceding mixed-face report isolated the following tempting shortcut. Let

\[
J:=T^*
\]

be the radial graph of `R`; `J` is a bipartite `(4,5)`-biregular quadrangulation. If one had

\[
\Phi_V(J)\ge \varphi,
\qquad
\varphi:=\frac{1+\sqrt5}{2},
\tag{BLOCK-R06-3}
\]

then the earlier full-face Euler argument would force the exact candidate `Phi_E(T)=2/sqrt(5)`.

This run attacks the negation of that shortcut first.

## 4. Methods #7 and #15 — the radial shortcut is false

### Proposition R06-I0056-RADIAL-REFUTE

For the `(4,5)`-biregular radial graph `J=T^*`,

\[
\boxed{
\Phi_V(J)\le 1+\frac1{\sqrt3}<\varphi.
}
\tag{4.1}
\]

In particular, `BLOCK-R06-3` is false.

### Proof

The degree-four orbit of `J` consists of the faces of `R`. Adjacency of two such faces across an edge is the regular dual tessellation

\[
R^*=H_{4,5}.
\]

Take a finite connected simply connected vertex set

\[
B\subset V(R^*)
\]

and interpret the same set `B` as degree-four vertices of `J`. Equivalently, `B` is a finite simply connected patch of quadrangular faces of `R`.

Write

\[
b:=|B|,
\qquad
q:=|\partial_E^{R^*}B|.
\]

Let `E_int` be the number of primal `R`-edges shared by two selected faces. Counting selected-face/edge incidences gives

\[
4b=2E_{\rm int}+q,
\qquad
E_{\rm int}=2b-\frac q2.
\]

The union of the selected faces therefore has

\[
E=E_{\rm int}+q=2b+\frac q2
\]

primal edges. Since it is a topological disk, Euler gives

\[
V-E+b=1,
\]

hence

\[
V=b+\frac q2+1.
\tag{4.2}
\]

But the outer vertex boundary of `B` in the radial graph `J` is **exactly** the set of primal `R`-vertices incident with at least one selected face. Those are exactly the `V` vertices counted in (4.2), because `B` occupies only the degree-four bipartition of `J`. Consequently

\[
\frac{|\partial_V^J B|}{|B|}
=1+\frac{q}{2b}+\frac1b.
\tag{4.3}
\]

Haggstrom--Jonasson--Lyons (equivalently Higuchi--Shirai) give the exact edge-isoperimetric constant of the regular tessellation `H_{4,5}`:

\[
\Phi_E(H_{4,5})
=(4-2)\sqrt{1-\frac4{(4-2)(5-2)}}
=\frac2{\sqrt3}.
\tag{4.4}
\]

Their planar reduction allows connected simply connected near-minimisers. Thus there is a sequence `B_n` of such sets with

\[
|B_n|\to\infty,
\qquad
\frac{|\partial_E B_n|}{|B_n|}\to\frac2{\sqrt3}.
\]

Applying (4.3),

\[
\lim_n
\frac{|\partial_V^J B_n|}{|B_n|}
=1+\frac1{\sqrt3}.
\]

Therefore `Phi_V(J) <= 1+1/sqrt(3)`.

Finally,

\[
\varphi-\left(1+\frac1{\sqrt3}\right)
=
\frac{\sqrt5-1}{2}-\frac1{\sqrt3}>0.
\]

For an exact sign check, both sides are positive and

\[
\left(\frac{\sqrt5-1}{2}\right)^2
=\frac{3-\sqrt5}{2}
>\frac13,
\]

where the last inequality is equivalent to `7>3 sqrt(5)`, hence to `49>45` after squaring. This proves (4.1). QED.

### What the method did

- **#15 BREAK THE SYMMETRY ON PURPOSE:** the obstruction is exposed by placing the test set entirely in the degree-four orbit of the biregular radial graph. The symmetric-looking global bound fails because arbitrary radial sets may concentrate on one orbit.
- **#7 TAKE THE LIMIT:** an asymptotically extremal `H_{4,5}` edge-isoperimetric sequence converts by the exact Euler count (4.3) into an explicit radial-vertex sequence below `phi`.

This refutes only the **auxiliary shortcut**. It does not refute Lyons--Peres Question 6.20, the candidate `Phi_E(T)=2/sqrt(5)`, or any published theorem.

## 5. Method #3 — replace the false global shortcut by the stronger correct finite object

The failed route asked for an expansion bound on **all** finite vertex sets of `J`, although the mixed-face problem generates only a very special family: interiors of finite quadrilateral face patches in `J`. The counterexample above is not of that form. So I strengthened the statement in the direction that preserves the actual geometry.

Let `D` be a finite topological disk made from quadrilateral faces of `J`. Write

- `F` = number of quadrilateral faces of `D`;
- `B` = length of its boundary cycle;
- `i_4` = number of interior degree-four vertices of `J`;
- `i_5` = number of interior degree-five vertices;
- `I=i_4+i_5`.

Because the boundary alternates between the two bipartition types, it has `B/2` vertices of each type.

Quadrilateral face/edge incidence and Euler give

\[
E=2F+\frac B2,
\qquad
I=F-\frac B2+1.
\tag{5.1}
\]

For a connected hole-filled medial set `S subset V(T)`, the dual patch has

\[
F=|S|,
\qquad
B=|\partial_E^T S|,
\qquad
I=F_4+F_5,
\]

where `F_4,F_5` are the full square/pentagonal ambient faces from the earlier R06 Euler proof. Boundary pinches can be unzipped in the standard plane-map way before applying the disk calculation; the exact remaining issue is therefore a boundary-turn inequality, not unrestricted radial vertex expansion.

The candidate sharp lower bound

\[
\frac BF\ge\frac2{\sqrt5}
\tag{5.2}
\]

is, using (5.1), algebraically equivalent to

\[
\boxed{
I\le 1+\frac B\varphi.
}
\tag{R06-I0056-DISK-TARGET}
\]

Indeed `F=I+B/2-1`, so (5.2) is equivalent to

\[
I-1\le \frac{\sqrt5-1}{2}B=\frac B\varphi.
\]

This is the **correct structured replacement** for the false `Phi_V(J)>=phi` shortcut.

## 6. Exact boundary-deficit identity

The disk target can be sharpened into one explicit boundary-word inequality.

For a boundary degree-four vertex `x`, let `d_D(x)` be its degree in the disk one-skeleton, and define

\[
\Delta_4:=\sum_{x\in\partial D,\ \deg_Jx=4}(4-d_D(x)).
\]

Similarly, for boundary degree-five vertices set

\[
\Delta_5:=\sum_{y\in\partial D,\ \deg_Jy=5}(5-d_D(y)).
\]

Summing degrees over the degree-four bipartition gives

\[
E=4i_4+2B-\Delta_4,
\]

while the degree-five side gives

\[
E=5i_5+\frac{5B}{2}-\Delta_5.
\]

Substituting `E=2F+B/2`,

\[
i_4=\frac F2-\frac{3B}{8}+\frac{\Delta_4}{4},
\qquad
 i_5=\frac{2F}{5}-\frac{2B}{5}+\frac{\Delta_5}{5}.
\]

Adding these and comparing with `I=F-B/2+1` yields the exact identity

\[
\boxed{
4F+11B+40=10\Delta_4+8\Delta_5.
}
\tag{R06-I0056-DISK-IDENTITY}
\]

Consequently the finite disk target is **equivalent** to

\[
\boxed{
10\Delta_4+8\Delta_5
\le
40+(11+2\sqrt5)B.
}
\tag{R06-I0056-TURN-CAP}
\]

because `4/phi=2(sqrt(5)-1)`.

This is the main positive reduction of the run: the exact tetrapentagonal edge candidate no longer asks for an impossible global radial Cheeger bound. It asks for a weighted cap on the cumulative boundary deficits of realizable quadrangulated `(4,5)` disk patches.

No finite computation is hidden in this claim, so I did not manufacture a checker. The proof is the displayed Euler and degree double count on the page.

## 7. Why the existing separate expansion bounds stop exactly where they did

The earlier bound

\[
\Phi_E(T)\ge\frac4{1+\sqrt3+\sqrt5}
\]

uses the two interior orbit sets separately:

\[
\frac2{\sqrt3}\,i_4\le \frac B2,
\qquad
\varphi i_5\le \frac B2.
\]

These imply only

\[
I\le
\left(\frac{\sqrt3}{4}+\frac1{2\varphi}\right)B,
\]

which is precisely the old Euler lower bound after substitution. The new target needs

\[
I\le 1+\frac B\varphi,
\]

so **independent treatment of the two vertex orbits cannot supply the missing gain**. The next proof must use a coupling in the alternating boundary word: a large degree deficit on the degree-four side must constrain what can occur on the neighboring degree-five side, and conversely.

Equivalently, a counterexample disk would have to satisfy

\[
10\Delta_4+8\Delta_5
>
40+(11+2\sqrt5)B.
\]

That is now the precise refutation target for the next run.

## 8. Status and next attack

Source-level fixed metric:

\[
U-L=0\longrightarrow0
\]

for `Phi_V(H_{5,5})`; no movement is possible below zero.

Full source status: **PARTIAL -> PARTIAL**.

Mechanism-level movement:

1. the attractive auxiliary statement `Phi_V(J)>=phi` is **REFUTED** by an exact asymptotic construction;
2. the reason is identified: arbitrary radial sets can concentrate on one bipartition orbit;
3. the surviving tetrapentagonal exact-edge problem is reduced to the realizable-disk inequality `I <= 1+B/phi`, equivalently the explicit weighted boundary-deficit cap (TURN-CAP).

The next useful attack is **not** another global Cheeger estimate on `J`. It is a local-to-global boundary-word/peeling argument for `(4,5)` quadrangulated disks. In particular, one should classify which neighboring deficit pairs can occur on a simple boundary and prove that their weighted average obeys TURN-CAP, or else construct an exact disk violating it. A violation would disprove the candidate `2/sqrt(5)`; a proof would close the mixed-face **edge** constant and then leave the distinct outer-vertex conversion as the remaining Question-6.20 obligation for `T`.

## 9. Model / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning. The present runtime identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The available scheduling surface still exposes no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-model/applied-effort receipt. The newer repository deployment documents likewise describe GPT-6/maximum as a requested preference rather than a verified scheduler setting. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; an owning/authorized product/admin/API context or platform permission repair is required for such changes. No scheduler or permission mutation was attempted here.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum
  lane: CLOSABLE_OUTSIDE

  source:
    authors: "Russell Lyons and Yuval Peres"
    work: "Probability on Trees and Networks"
    locator: "Question 6.20"
    intake: I0056

  frozen_target:
    graph: "H_{5,5} / {5,5}"
    degree: 5
    face_degree: 5
    normalization: "outer vertex boundary |partial_V K|/|K|"
    value: "sqrt(5)"

  fixed_metric:
    name: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5), sqrt(5)]"
    movement: NO_MOVEMENT

  full_source_status:
    before: PARTIAL
    after: PARTIAL
    excluded_prior_art: "Haslegrave-Panagiotis DOI 10.1002/rsa.20946, codegrees 3 and 4"

  mixed_face_target:
    graph: "T=M(H_{5,4})=r{4,5}, face type [4,5,4,5]"
    inherited_edge_interval: "[4/(1+sqrt(3)+sqrt(5)), 2/sqrt(5)]"
    inherited_vertex_interval: "[1/(sqrt(3)+sqrt(5)-2), 2/sqrt(5)]"

  mechanism_progress:
    radial_shortcut:
      statement: "Phi_V(T*) >= phi"
      before: CONJECTURAL
      after: REFUTED
      certificate: "Phi_V(T*) <= 1 + 1/sqrt(3) < phi"
    replacement_target:
      statement: "I(D) <= 1 + B/phi for finite (4,5)-quadrangulated disk patches"
      status: OPEN_REDUCTION
    exact_identity:
      statement: "4F + 11B + 40 = 10 Delta_4 + 8 Delta_5"
      status: PROVED
    equivalent_turn_cap:
      statement: "10 Delta_4 + 8 Delta_5 <= 40 + (11+2sqrt(5)) B"
      status: OPEN

  tried_moves: [7, 15, 3]
  predecessor_report: "runs/R06/20260919T2250Z_successor_gate_hard_releases_no_ready_74_e6c1.md"
  predecessor_creation_commit: "5c6c20b00c9492c4ba3f7fd89a03cc8e5b6f7fda"
  prewrite_head: "12afbe8d13637ea85bbfa19c1b119048cf761641"
  predecessor_to_prewrite_delta:
    commits_ahead: 77
    commits_behind: 0
    too_large: null

  evidence:
    - "runs/R06/20260916T144133Z_i0056_edge_vertex_closure.md"
    - "runs/R06/20260916T1820Z_i0056_medial_tetrapentagonal_01.md"
    - "runs/R06/20260916T1922Z_i0056_medial_dual_euler_02.md"
    - "operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md"
    - "operations/claims/I0056.md"

  remaining_obligation: >-
    Prove or refute the realizable-disk TURN-CAP for the (4,5)-biregular
    quadrangulation. If proved, combine with the existing ball upper to obtain
    Phi_E(T)=2/sqrt(5), then separately solve the outer-vertex constant Phi_V(T).

  github_delivery: PENDING_READBACK
```
