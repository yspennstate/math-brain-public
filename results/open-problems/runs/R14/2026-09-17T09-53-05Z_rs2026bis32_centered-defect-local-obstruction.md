Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `D_bis: 2 -> 2`; unchanged count `1 -> 2`. Methods actually tried: #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# R14 — RS-2026-BIS32: exact centered complement duality, LDGM shell reformulation, and the induced-edge obstruction to local reflection

Status: **OPEN / PARTIAL**. Current exclusive target remains `RS-2026-BIS32`, Afonso S. Bandeira's Randomstrasse 101 Conjecture 32 (Min and Max Bisections), tracing to Zdeborova--Boettcher. The original negative-margin spherical-perceptron target remains handed off and is not reopened; its last supported rigorous bracket remains

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

The intervening I0089 target also remains handed off. I continued from `runs/R14/2026-09-17T08-51-44Z_rs2026bis32_simple_annealed_kl.md`.

## 1. Continuity, source status, and current literature check

I recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, current `QUEUE.md` / claim state, `operations/NEW_METHODS_2026-09-16.md`, the newest R14 report, the newest visible neighboring R15 report, and the historical intake/attempt hit `E0053` for this same bisection problem. The very large intake JSONL collection cannot be rendered row-by-row through the connector without truncation; the intake portion of the requested whole-repository read is therefore **ACCESS-LIMITED / targeted**, not falsely reported complete.

The live Randomstrasse page, checked again on 2026-09-17, still states for every fixed integer `d>=3`, even `n`, and uniform simple `d`-regular `G_d`,

\[
\frac{\mathbf E\,\mathrm{MinBis}(G_d)+\mathbf E\,\mathrm{MaxBis}(G_d)}{n}
=\frac d2+o(1).
\tag{BIS32}
\]

Fresh bounded searches on 2026-09-17 for `MinBis MaxBis random regular 2026`, `Zdeborova Boettcher bisection random regular 2025 2026`, and `minimum bisection random regular 2026 fixed degree max bisection` recovered the live source, Harangi's 2025 2-RSB **MaxCut** upper bounds, Lichev--Mitsche's rigorous cubic **minimum**-bisection bounds, and the large-degree/local-algorithm literature, but no primary theorem closing (BIS32) at any fixed source degree. Gheissari--Perkins--Yap's 2025 fixed-magnetization result remains positive-temperature/up-to-reconstruction, not the zero-temperature statement here. This is bounded negative evidence, not a novelty certificate.

Current fixed metric:

\[
D_{\rm bis}:=\sup\{D\ge2:\text{(BIS32) is proved for every fixed }3\le d\le D\}.
\]

Before this run `D_bis=2`; after this run it remains `2`.

## 2. Preserved spin formulation

For a balanced spin vector

\[
\Omega_n=\{\sigma\in\{-1,+1\}^n:\sum_i\sigma_i=0\},
\qquad
H_G(\sigma)=\sum_{\{i,j\}\in E(G)}\sigma_i\sigma_j,
\]

write

\[
M_+(G)=\max_{\Omega_n}H_G(\sigma),\qquad
M_-(G)=\min_{\Omega_n}H_G(\sigma).
\]

Then

\[
\mathrm{MinBis}(G)=\frac{dn/2-M_+(G)}2,
\qquad
\mathrm{MaxBis}(G)=\frac{dn/2-M_-(G)}2,
\]

so (BIS32) is equivalent to

\[
\frac1n\mathbf E[M_+(G_d)+M_-(G_d)]\to0.
\tag{2.1}
\]

The previous run proved that the **annealed** balanced pressure in the actual simple regular ensemble is even at leading exponential order and rewrote the remaining obstruction as equality of the zero-temperature reverse-KL slopes of the `+beta` and `-beta` balanced planted models. This run attacks what remains after that annealed symmetry.

## 3. Method #12 — FIND WHAT IS CONSERVED: exact finite-n centered complement antisymmetry

There is an exact finite-`n` centering that was hidden by the source's asymptotic `d/2` normalization.

For every balanced `sigma`,

\[
\sum_{1\le i<j\le n}\sigma_i\sigma_j
=\frac{(\sum_i\sigma_i)^2-n}{2}
=-\frac n2.
\tag{3.1}
\]

Therefore, for the graph complement `\bar G`,

\[
H_{\bar G}(\sigma)=-\frac n2-H_G(\sigma).
\tag{3.2}
\]

Taking extrema gives the **pointwise** identities

\[
M_+(\bar G)=-\frac n2-M_-(G),
\qquad
M_-(\bar G)=-\frac n2-M_+(G).
\tag{3.3}
\]

Let

\[
F_{n,d}:=\mathbf E_{G_d}[M_+(G_d)+M_-(G_d)].
\]

Complementation is a bijection from labeled simple `d`-regular graphs to labeled simple `(n-1-d)`-regular graphs. Hence

\[
\boxed{F_{n,d}+F_{n,n-1-d}=-n.}
\tag{C199.1}
\]

For any fixed balanced `sigma`, permutation symmetry of the uniform regular graph gives

\[
\mu_{n,d}:=\mathbf E H_{G_d}(\sigma)
=\frac d{n-1}\sum_{i<j}\sigma_i\sigma_j
=-\frac{dn}{2(n-1)}.
\tag{3.4}
\]

Define the exactly centered spin defect

\[
\Delta_{n,d}:=F_{n,d}-2\mu_{n,d}
=F_{n,d}+\frac{dn}{n-1}.
\tag{3.5}
\]

Then (C199.1) becomes the exact antisymmetry

\[
\boxed{\Delta_{n,d}=-\Delta_{n,n-1-d}.}
\tag{C199.2}
\]

In cut language the exact ensemble mean of one fixed balanced cut is

\[
c_{n,d}=\frac{dn^2}{4(n-1)}.
\]

Thus with

\[
B_{n,d}:=
\mathbf E[\mathrm{MinBis}(G_d)+\mathrm{MaxBis}(G_d)]
-\frac{dn^2}{2(n-1)},
\tag{3.6}
\]

we have

\[
B_{n,d}=-\frac12\Delta_{n,d},
\qquad
\boxed{B_{n,d}=-B_{n,n-1-d}.}
\tag{C199.3}
\]

Since

\[
\frac{dn^2}{2(n-1)}=\frac{dn}{2}+O_d(1),
\]

Conjecture 32 is equivalently

\[
\boxed{B_{n,d}=o(n)\quad\text{for every fixed }d\ge3.}
\tag{3.7}
\]

A stronger `B_{n,d}=O_d(1)` theorem would therefore settle the source at degree `d`.

This exact invariant explains a feature of the earlier finite enumeration without changing its status. Re-centering the already exact-checked values gives

\[
B_{4,3}=0,\quad B_{6,3}=-\frac8{35},\quad
B_{8,3}=\frac8{79},\quad
B_{6,4}=-\frac25,\quad B_{8,4}=-\frac8{79}.
\]

The last pair is an exact complement pair because `3+4=8-1`. These are finite observations only, not asymptotic endpoints.

**Why this does not move `D_bis`.** For fixed sparse `d`, the complementary degree `n-1-d` grows with `n`; C199 relates the sparse problem to a near-complete one, not to another fixed source degree. It is nevertheless an exact conserved centering that any successful interpolation has to respect.

## 4. Method #20 — FIND WHY THE ALGORITHM FAILS: the problem is a quenched constant-weight LDGM shell problem

The incidence matrix gives a category change that precisely diagnoses the failure of the annealed route.

Let `A_G in F_2^{n x m}` be the vertex-edge incidence matrix, where `m=dn/2`. Every column has two ones and every row has `d` ones. For an indicator vector `x in F_2^n`,

\[
y=A_G^T x\in\mathbb F_2^m
\]

has

\[
y_e=1\iff e\text{ crosses }(\operatorname{supp}x,\operatorname{supp}x^c).
\]

Hence

\[
|A_G^Tx|=\mathrm{cut}_G(\operatorname{supp}x).
\tag{C200.1}
\]

The bisection constraint is exactly the constant-input-weight shell `|x|=n/2`. Therefore MinBis and MaxBis are the two support endpoints of the random input-output weight enumerator

\[
A_G(h):=\#\{x\in\{0,1\}^n:|x|=n/2,\ |A_G^Tx|=h\}.
\tag{4.1}
\]

This is a `(d,2)` regular LDGM-type factor graph, with the extra conditioning that the degree-2 output nodes encode a **simple** graph. The coding-theory connection is not new folklore invented here: Yano--Wadayama (IEICE Trans. Fundamentals E99-A, 2016, DOI 10.1587/transfun.E99.A.2218) explicitly relate graph cut spaces to column-weight-2 LDGM ensembles, and the standard regular-LDGM average input-output weight enumerator has the coefficient formula involving

\[
f_-(z,r)=\frac{(1+z)^r-(1-z)^r}{2},\qquad
f_+(z,r)=\frac{(1+z)^r+(1-z)^r}{2}.
\]

At output/check degree `r=2`,

\[
f_-(z,2)=2z,\qquad f_+(z,2)=1+z^2,
\]

and the average IOWE on the half-input shell reduces to the same first-moment pairing count already obtained by R14. Thus the annealed reflection symmetry is not an isolated spin-glass accident: it is exactly the symmetry of the **average shell weight enumerator**.

This identifies why the previous algorithm fails. The source asks for the endpoints of the support of `A_G(h)` for a **typical graph/code**. The previous pairing count and C197 control `\mathbf E A_G(h)` instead. Rare graphs can dominate an average enumerator at the edge, exactly as average weight enumerators need not determine the typical minimum distance of a sparse code.

A clean sufficient theorem is now visible. If one could prove a deterministic quenched shell exponent `phi_d(q)` such that, uniformly down to both support edges,

\[
\frac1n\log A_{G_d}(qdn/2)\to\phi_d(q)
\quad\text{in probability}
\tag{4.2}
\]

and show

\[
\phi_d(q)=\phi_d(1-q),
\tag{4.3}
\]

then the lower and upper support edges would be reflected and (BIS32) would follow. Current first-moment/annealed machinery proves neither the quenched convergence at the zero-complexity edge nor (4.3) there. The bounded coding-literature search found average-IOWE machinery and graph/LDGM connections, but no theorem for this exact **regular, simple-graph, input-weight-1/2 quenched support** that closes the source.

So #20 did not solve `d=3`, but it converts the vague “quenched correlations” obstruction into a specific missing object: **typical shell spectral support, not average shell spectral shape**.

## 5. Method #30 — ONE SCALE AT A TIME: exact equal-size swap identity and the induced-edge obstruction

There is a second exact structural identity which says precisely where a local min/max reflection can fail.

Fix any `d`-regular graph and a bisection `(S,T)`. For each vertex let `r_v` be its number of crossing neighbors. Choose equal-size sets

\[
U\subset S,\qquad V\subset T,\qquad |U|=|V|=p,
\]

and swap the sides of all vertices in `W=U\cup V`. Let

- `e_cross(W)` be the number of edges of `G[W]` joining `U` to `V` (crossing before the swap),
- `e_same(W)` be the number of edges of `G[W]` internal to `U` or internal to `V` (noncrossing before the swap).

Boundary same-edges become crossing and boundary cross-edges become same. Since

\[
\#\partial W\text{ same}=2pd-\sum_{w\in W}r_w-2e_{\rm same}(W),
\]

and

\[
\#\partial W\text{ cross}=\sum_{w\in W}r_w-2e_{\rm cross}(W),
\]

the exact cut change is

\[
\boxed{
\Delta\mathrm{cut}
=2pd-2\sum_{w\in W}r_w
+2e_{\rm cross}(W)-2e_{\rm same}(W).
}
\tag{C201.1}
\]

Therefore every global minimum bisection satisfies

\[
\sum_{w\in W}r_w
\le pd+e_{\rm cross}(W)-e_{\rm same}(W),
\tag{C201.2}
\]

and every global maximum bisection satisfies the reverse inequality.

The crucial special case is when `G[W]` is empty. Then

\[
\boxed{
\text{minimum: }\sum_{w\in W}r_w\le pd,
\qquad
\text{maximum: }\sum_{w\in W}r_w\ge pd.
}
\tag{C201.3}
\]

These two local optimality constraints are **perfect reflections** under `r -> d-r`. All asymmetry at this swap scale is therefore carried by the signed induced-edge correction

\[
e_{\rm cross}(W)-e_{\rm same}(W).
\tag{5.1}
\]

For `p=1`, if `u in S` and `v in T` are nonadjacent, minimum optimality gives

\[
r_u+r_v\le d,
\]

while maximum optimality gives

\[
r_u+r_v\ge d.
\]

If `uv` is an edge, the threshold shifts to `d+1`. Thus a degree-profile-only or independent-swap argument is forced to be symmetric; it can distinguish MinBis from MaxBis only through the adjacency/incidence information among the vertices selected for repair.

This is the precise obstruction to the obvious local-search algorithm. For a random *chosen* fixed-size `W`, induced edges are rare, but an extremizing bisection chooses `W` adversarially from exponentially many possibilities. Replacing that adversarial quantifier by a typical-`W` estimate is invalid. A successful local-to-global proof therefore needs either (i) uniform control of the signed induced-edge correction over all improving swap sets up to a scale `p=p(n)`, or (ii) a macroscopic interpolation where the correction becomes an explicitly controlled energy term.

### Exact self-check

Because C199 and C201 are finite identities, I added one substantive exact checker rather than a decorative certificate. It exhaustively enumerates **all labeled simple graphs on `n=4` and `n=6`**, filters all 180 regular graphs, and for every such graph checks C199 plus C201 for every balanced cut and every admissible equal-size swap. The executed output ends

`R14_C199_C201_EXACT_CHECK_PASS`.

Artifacts:

- `artifacts/R14/2026-09-17T09-53-05Z_rs2026bis32_c199_c201_exact_check.py`
- `artifacts/R14/2026-09-17T09-53-05Z_rs2026bis32_c199_c201_exact_check.out`

The checker is a self-check, not an independent audit; the displayed algebraic proofs are the actual theorem arguments.

## 6. What actually changed, and what did not

The source metric did **not** move:

\[
\boxed{D_{\rm bis}:2\to2.}
\]

But the route is narrower than one run ago:

1. the correct finite-`n` center is now exact, and its defect is complement-antisymmetric (C199);
2. the annealed pairing calculation is identified as the standard average input-output spectrum of a `(d,2)` LDGM shell, so repeating first-moment enumerator work cannot close the source (C200);
3. every induced-edge-free balanced swap is exactly min/max reflection-symmetric, and the first local obstruction is the signed induced-edge term (C201).

The new strongest plausible route is therefore **not** another annealed pressure calculation. It is to control one of two genuinely quenched objects:

- the typical constant-weight LDGM shell support down to its two zero-complexity edges; or
- the cumulative signed induced-edge correction in a growing-scale balanced-swap hierarchy.

A theorem such as `B_{n,3}=O(1)` would already move the metric `2 -> 3`. Nothing in this run establishes it.

The next distinct method triple, if the metric has not moved before the next R14 invocation, is **#1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS**: formally import the quenched sparse-code support viewpoint; optimize the worst possible local cross-degree/induced-edge profile; and compare “for every extremal bisection there exists an improving swap” against a probabilistic statement uniform over all candidate swaps.

Current unchanged count is `2`. One additional unchanged active research run reaches the three-run stagnation trigger; the following run must obey the hard-task stuck-recovery rule rather than manufacture another incremental lemma.

## 7. Model / reasoning selector and protected-task status

The model-control limitation is still true in the interface exposed to this run. The available task update fields are title, prompt, schedule / relative start, enablement, and timing mode. There is **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt text only; this report truthfully records GPT-5.6 Sol with reasoning `UNVERIFIED`.

Actually forcing and verifying GPT-6/maximum would require an authorized scheduler/product/API surface that exposes explicit model and reasoning fields and completed-run telemetry, or a platform-side change/support intervention.

The controlling repository policy records that native modification probes for P26, P01 and P03 returned `You cannot modify this task`. I did not attempt a forbidden scheduler modification in this run. The legitimate workaround is to act from the authorized owning account/workspace context, transfer/fix ownership through an authorized surface, or use platform support. Creating a duplicate job or bypassing permissions is not valid.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  target: RS-2026-BIS32
  source: "Randomstrasse 101 Conjecture 32 — Min and Max Bisections"
  source_status: OPEN
  category: HARD_OUTSIDE
  metric:
    name: D_bis
    before: 2
    after: 2
    unchanged_count_before: 1
    unchanged_count_after: 2
  status: OPEN_PARTIAL
  methods_this_run: [12, 20, 30]
  claims:
    C199:
      statement: "exact finite-n centered complement antisymmetry B_{n,d}=-B_{n,n-1-d}"
      status: PROVED_ON_PAGE_SELF_CHECK
      audits_other_tracks: 0
    C200:
      statement: "bisection extrema are endpoints of the input-weight-n/2 output spectrum of the graph incidence (d,2)-LDGM map"
      status: EXACT_REFORMULATION
      audits_other_tracks: 0
    C201:
      statement: "exact equal-size swap identity; induced-edge-free swaps are min/max reflection symmetric"
      status: PROVED_ON_PAGE_SELF_CHECK
      audits_other_tracks: 0
  exact_checker:
    source: artifacts/R14/2026-09-17T09-53-05Z_rs2026bis32_c199_c201_exact_check.py
    output: artifacts/R14/2026-09-17T09-53-05Z_rs2026bis32_c199_c201_exact_check.out
    result: R14_C199_C201_EXACT_CHECK_PASS
    regular_graphs_exhaustively_checked: 180
  remaining_obligation: "prove B_{n,3}=o(n) (or stronger O(1)) for the uniform simple cubic graph; then D_bis moves 2->3"
  next_methods: [1, 24, 27]
```

No shared-root ledger, peer-track file, email, Drive item, public post, purchase, permission setting, workflow, or scheduler was changed.