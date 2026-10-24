Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but there is no authenticated runtime metadata establishing that setting, so it is not claimed.

# P26 / T08 — exact line-graph entropy transfer and a transitive spectral-expander class outside long-range expansion

**Status:** `CANDIDATE_FULL` for the restricted theorem proved below; **PARTIAL** for Salez Problem 2.3. This report does not claim the full vertex-transitive-expander conjecture, publication novelty, or independent review.

## 0. Parent problem, continuity, and scope

The controlling policy is `operations/PROGRESS20_2026-09-20.md`. It replaces the old P26 audit-first assignment by T08 research and maps P26's historical C28 companion to the live slot `NM13-01`. Thus there is no live C28 dependency to wait for. I use the complementary split

- **P26 here:** exact entropy/Markov transfer through the line-graph incidence correspondence, then an explicit transitive spectral-expander application outside long-range expansion;
- **NM13-01 companion:** direct transitivity-specific attack on arbitrary spectral expanders / the missing mixing-window entropy inequality, rather than duplicating the line-graph closure mechanism.

The inherited R16/I0112 handoff (`runs/R16/2026-09-17T00-45-57Z_i0112-handoff_i0043-boundary-capacity.md`) left the full source target open. Its useful facts are preserved: synchronous tensor products had a restricted `O(sqrt(log |V|))` theorem; long-range expansion is stronger than spectral expansion; global Bakry--Emery/subcommutation routes fail already on the regular tree; and the unresolved general obstruction is a mixing-window information-concentration/entropy statement for arbitrary transitive spectral expanders. This run does **not** revive those failed global-curvature routes.

### Parent-problem before / after

- **Before:** Salez Problem 2.3 remained OPEN. Known source-valid cutoff classes included Ramanujan graphs and, as of Altschuler arXiv:2609.14945 (14 September 2026), fixed-degree long-range expanders. The historical synchronous-product theorem was another restricted family but did not address arbitrary transitive spectral expanders.
- **After this run:** the full parent remains OPEN, but there is a new proved restricted class: **line graphs of fixed-degree edge-transitive long-range expanders have continuous-time total-variation cutoff with an `O(sqrt(log |V|))` window; moreover these line graphs are vertex-transitive spectral expanders and are never a uniform long-range-expander family.** Applying this to Kaufman--Lubotzky's explicit cubic edge-transitive Ramanujan family gives an explicit **4-regular vertex-transitive spectral-expander family outside long-range expansion** with cutoff.

That is a genuine parent-scope expansion, not merely a framework or an auxiliary constant.

## 1. Exact source convention and September 2026 scope

Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1 (28 August 2025), Problem 2.3 asks for cutoff for all bounded-degree vertex-transitive expander sequences. I use Salez's exact continuous-time convention throughout: if `P` is the discrete transition matrix, then

\[
H_t=\exp\{t(P-I)\},
\]

so the walk waits independent mean-one exponentials and makes a rate-one Poisson number of ordinary SRW transitions by time `t`.

The main newer exact-scope result found in the dated 20 September 2026 search is Dylan Altschuler, *Long-range expanders: construction and cutoff*, arXiv:2609.14945v1 (submitted 14 September 2026). It proves cutoff for fixed-degree long-range expanders, proves Ramanujan `=>` long-range `=>` spectral expansion with neither converse, and explicitly presents this as intermediate progress toward the transitive spectral-expander conjecture. Its Proposition 3.1 gives the endpoint-entropy input used below:

\[
H(K_j(x,\cdot))\ge \log n-C\log\log n
\quad\text{for }j\ge j_n=\log_{d-1}n+O_d(1),
\tag{1.1}
\]

uniformly in `x`, where `K_j` is the length-`j` nonbacktracking endpoint law. Its Lemma 3.4 converts such near-maximal entropy to `o(1)` total variation after `omega(log log n)` lazy steps under a fixed absolute spectral gap.

A bounded web/repository search for `line graph random walk cutoff`, `line graph cutoff expander`, and 2026 followups did not locate the line-graph theorem below. This is only negative search evidence; **publication priority is UNVERIFIED**.

## 2. The exact incidence algebra

Let `G=(V,E)` be a finite simple `d`-regular graph, `d>=3`, with

\[
|V|=n,\qquad |E|=m=nd/2.
\]

Let `P=A/d` be SRW on vertices. Let `L(G)` be the line graph. It is `D=2(d-1)`-regular, and write

\[
Q=\frac{A_L}{2(d-1)}
\]

for its SRW transition matrix. Let `B` be the `0/1` vertex-edge incidence matrix. Then

\[
BB^T=dI+A,\qquad B^TB=2I+A_L.
\tag{2.1}
\]

Define two Markov kernels

\[
K(e,x)=\frac12\mathbf 1_{\{x\in e\}},
\qquad
J(x,e)=\frac1d\mathbf 1_{\{x\in e\}}.
\tag{2.2}
\]

Thus `K` chooses a uniform endpoint of an edge and `J` chooses a uniform incident edge from a vertex. In matrix notation, `K=B^T/2`, `J=B/d`. Put

\[
b=\frac{d}{2(d-1)},\qquad c=\frac{d}{d-1}.
\tag{2.3}
\]

From (2.1),

\[
JK=\frac{I+P}{2}=:R,
\tag{2.4}
\]

and

\[
KJ=\frac1d I+\frac{d-1}{d}Q.
\tag{2.5}
\]

Equivalently,

\[
\boxed{Q-I=c(KJ-I).}
\tag{2.6}
\]

Also

\[
QB^T=B^T\left(\frac{d-2}{2(d-1)}I+\frac{d}{2(d-1)}P\right),
\]

so

\[
\boxed{(Q-I)K=bK(P-I).}
\tag{2.7}
\]

Exponentiating (2.7) gives the exact continuous-time intertwining

\[
\boxed{\widetilde H_tK=KH_{bt}},
\qquad
\widetilde H_t=e^{t(Q-I)},\ H_s=e^{s(P-I)}.
\tag{2.8}
\]

For an initial edge `e={u,v}` this says that if `E_t` is the rate-one line-graph walk and a uniform endpoint `U_t` of `E_t` is sampled, then

\[
\mathcal L(U_t)
=\frac12(\delta_u+\delta_v)H_{bt}.
\tag{2.9}
\]

There is no hidden lazy/discrete convention here: both displayed heat kernels are Salez's rate-one continuous-time semigroups. The lazy kernel `R=(I+P)/2` occurs only as the exact algebraic factor `JK` inside the proof.

## 3. Exact entropy and varentropy transfer

Let `pi_E` and `pi_V` be uniform on `E` and `V`. For any law `mu` on edges, form the joint incidence law

\[
\widehat\mu(e,x)=\mu(e)K(e,x).
\]

Under stationarity, `\widehat\pi(e,x)=1/(nd)` on incidences. Since the likelihood ratio of the joint law is just `m mu(e)`, the KL chain rule gives

\[
D(\mu\|\pi_E)
=D(\mu K\|\pi_V)
+\mathbb E_{x\sim\mu K}
D\!\left(\mathcal L(E\mid X=x)\middle\|\operatorname{Unif}(E(x))\right).
\tag{3.1}
\]

Therefore

\[
\boxed{
0\le D(\mu\|\pi_E)-D(\mu K\|\pi_V)\le\log d.
}
\tag{3.2}
\]

Equivalently, in entropy-deficit form,

\[
0\le [\log m-H(\mu)]-[\log n-H(\mu K)]\le\log d.
\tag{3.3}
\]

This is the promised **entropy transfer criterion**: near-maximal entropy of the endpoint projection loses at most the fixed local cost `log d` when lifted back to the line graph.

A useful stronger diagnostic concerns varentropy. Under the joint incidence law,

\[
I_E(E):=\log(m\mu(E))
=I_V(X)+I_{E|X}(E,X).
\]

For a `d`-point conditional distribution `(p_i)`,

\[
\sum_i p_i\log^2(dp_i)
\le \log^2 d+\frac4{e^2};
\tag{3.4}
\]

indeed the part `dp_i>=1` is at most `log^2 d`, while `x\log^2x<=4/e^2` on `0<x<=1` and `p_i=x/d`. Minkowski in `L^2` therefore yields

\[
\boxed{
\sqrt{\operatorname{Varent}(\mu)}
\le
\sqrt{\operatorname{Varent}(\mu K)}
+\sqrt{\log^2 d+4/e^2}.
}
\tag{3.5}
\]

Thus both entropy deficit and information fluctuations transfer with only an `O_d(1)` local penalty.

## 4. Stronger quantitative TV transfer

The heat-bath factorization (2.6) yields more than entropy transfer.

For an edge `e`, define

\[
d_E^e(t)=\|\delta_e\widetilde H_t-\pi_E\|_{TV},
\]

and the adjacent-pair vertex distance

\[
d_A^e(s)=\left\|
\frac12(\delta_u+\delta_v)H_s-\pi_V
\right\|_{TV},\qquad e=\{u,v\}.
\]

### Theorem 4.1 (line-graph cutoff transfer)

For every `t,tau>=0`,

\[
\boxed{d_A^e(bt)\le d_E^e(t)}
\tag{4.1}
\]

and

\[
\boxed{d_E^e(t+\tau)\le e^{-c\tau}+d_A^e(bt)}.
\tag{4.2}
\]

#### Proof

The lower bound is data processing under `K`, using (2.8) and `pi_E K=pi_V`.

For the upper bound, (2.6) gives

\[
\widetilde H_\tau
=e^{-c\tau}\sum_{r\ge0}\frac{(c\tau)^r}{r!}(KJ)^r.
\tag{4.3}
\]

For `r>=1`, associativity and (2.4) give

\[
(KJ)^r=K(JK)^{r-1}J=KR^{r-1}J.
\tag{4.4}
\]

Put `mu=delta_e \widetilde H_t`. The `r=0` term in (4.3) contributes at most `e^{-c tau}` to total variation. For every `r>=1`, Markov-kernel contraction and stationarity give

\[
\|\mu K R^{r-1}J-\pi_E\|_{TV}
\le \|\mu K-\pi_V\|_{TV}
=d_A^e(bt).
\]

Averaging over the Poisson weights proves (4.2). QED.

Consequently, if `t_A^e(eps)` is the adjacent-pair mixing time and `t_E^e(eps)` the line-graph mixing time, then

\[
\boxed{
\frac1b t_A^e(\varepsilon)
\le t_E^e(\varepsilon)
\le \frac1b t_A^e(\varepsilon/2)
+\frac1c\log\frac2\varepsilon.
}
\tag{4.5}
\]

Hence any adjacent-pair cutoff with diverging window `w_n` transfers to the line graph with center scaled by `1/b` and the same window order. The extra heat-bath cost is only `O_{d,eps}(1)`.

This is the mechanism-level advance of the run. My first entropy-only attempt would have lost a `sqrt(log log n)` factor in the window because it forced the bad radial mass down to inverse-polynomial size before invoking (3.2). The factorization `Q-I=c(KJ-I)` removes that loss completely.

## 5. Spectral expansion transfers, but long-range expansion does not

### 5.1 Spectrum

From (2.1), if `lambda` is a normalized eigenvalue of `P`, the corresponding nonzero-incidence eigenvalue of `Q` is

\[
\theta(\lambda)
=\frac{d\lambda+d-2}{2(d-1)}
=1+b(\lambda-1),
\tag{5.1}
\]

and the remaining line-graph eigenvalues are

\[
-\frac1{d-1}.
\tag{5.2}
\]

Thus a base spectral gap `1-lambda_2(P)>=gamma>0` gives

\[
1-\lambda_2(Q)\ge b\gamma>0.
\tag{5.3}
\]

So fixed-degree spectral expansion survives the line-graph operation.

If `G` is edge-transitive, then `L(G)` is vertex-transitive because the vertices of `L(G)` are precisely the edges of `G`.

### 5.2 Uniform long-range expansion fails for every growing fixed-degree line-graph family

This is important: the application below is **not** a disguised use of Altschuler's theorem on the output graphs.

Fix an edge `e={u,v}` of a `d`-regular graph. If an edge `f` lies within line-graph distance `r` of `e`, an endpoint of `f` lies within ordinary graph distance at most `r` of `{u,v}`. Therefore, using only the degree bound,

\[
|B_{L(G)}(e,r)|\le C_d(d-1)^r
\tag{5.4}
\]

for a constant `C_d` independent of the graph size.

But `L(G)` has degree `D=2(d-1)`, so Altschuler's long-range-expansion branching base for the line graph is

\[
D-1=2d-3.
\]

Choose

\[
r_n=\left\lfloor\frac12\log_{2d-3}|E(G_n)|\right\rfloor.
\]

Then `(2d-3)^{r_n}=o(|E(G_n)|)`, while by (5.4)

\[
\frac{|B_{L(G_n)}(e,r_n)|}{(2d-3)^{r_n}}
\le C_d\left(\frac{d-1}{2d-3}\right)^{r_n}
\longrightarrow0.
\tag{5.5}
\]

For the singleton set `S={e}`, this contradicts the defining lower bound

\[
|B(S,r)|\ge \min\{3|V(L)|/4,\ c|S|(D-1)^r\}
\]

for every fixed `c>0`. Therefore

\[
\boxed{(L(G_n))\text{ is not a uniform long-range-expander sequence}.}
\tag{5.6}
\]

This proves directly, in the transitive application below, the requested distinction between spectral and long-range expansion.

## 6. Continuous-time cutoff for line graphs of edge-transitive LRE bases

Assume now that `(G_n)` is a fixed-`d` sequence of edge-transitive `c_0`-long-range expanders, with `n=|V(G_n)| -> infinity`. Set

\[
q=d-1,\qquad L_n=\log_q n,\qquad v=\frac{d-2}{d}.
\tag{6.1}
\]

### Lemma 6.1 (adjacent-pair continuous-time front)

For every edge `e={u,v}`, the rate-one continuous-time base law

\[
\nu_{e,s}=\frac12(\delta_u+\delta_v)H_s
\]

has cutoff at

\[
s_n=\frac{L_n}{v}=\frac{d}{d-2}\log_{d-1}n
\tag{6.2}
\]

with window `O(sqrt(L_n))`, uniformly in `e`.

#### Proof

Use the universal-cover representation. For rate-one continuous-time SRW on the infinite `d`-regular tree, let `R_s` be distance from the root. Conditional on `R_s=j`, projection to `G_n` has law `K_j(x,.)`. Away from the root the signed radial jump is `+1` with probability `(d-1)/d` and `-1` with probability `1/d`, and jumps arrive at rate one. The number of returns to the root has a geometric tail because the outward drift is positive. Hence `R_s` differs by a tight exponentially-tailed error from a compound-Poisson sum with mean `vs` and variance `s`. In particular,

\[
\frac{R_s-vs}{\sqrt{s}}\Longrightarrow N(0,1),
\tag{6.3}
\]

uniformly along the mixing scale `s asymp L_n`.

Altschuler Proposition 3.1 gives (1.1) for `j>=j_n=L_n+O_d(1)`. To turn entropy into mixing without a bipartiteness restriction, use the lazy kernel

\[
R=(I+P)/2.
\]

Spectral expansion gives all nonconstant eigenvalues of `R` in `[0,1-gamma/2]`. Altschuler Lemma 3.4 therefore says that, for

\[
k_n=\lceil(\log\log n)^2\rceil=o(\sqrt{L_n}),
\]

`K_j R^{k_n}` is `o(1)` from uniform for every `j>=j_n`, uniformly in the start. Since

\[
H_t=e^{t(P-I)}=e^{2t(R-I)},
\]

an additional continuous time `k_n` produces `Poisson(2k_n)` lazy steps; with probability `1-o(1)` at least `k_n` occur. Therefore the same `o(1)` mixing conclusion holds after this additional continuous time.

Decompose the walk at time `s-k_n` by its lifted radius and then run the final `k_n` units. Convexity gives

\[
\|H_s(x,\cdot)-\pi_V\|_{TV}
\le \Pr(R_{s-k_n}<j_n)+o(1).
\tag{6.4}
\]

The same upper bound holds for the average of two adjacent starts.

For the lower bound choose `r_n=L_n-k_n`. A degree bound gives

\[
|B(u,r_n)\cup B(v,r_n)|=O(q^{r_n})=o(n).
\]

Whenever the lifted radius from the corresponding start is at most `r_n`, the projected walk lies in that union. Hence

\[
\|\nu_{e,s}-\pi_V\|_{TV}
\ge \Pr(R_s\le r_n)-o(1).
\tag{6.5}
\]

At `s=s_n+z\sqrt{L_n}`, both (6.4) and (6.5), together with (6.3) and `k_n=o(sqrt(L_n))`, give the same nondegenerate Gaussian transition. In particular the window is `O(sqrt(L_n))`. QED.

(If desired, the continuous-time profile in this normalization is `Phi(-v^{3/2} z)`: the compound-Poisson radial variance rate is one. The cutoff/window claim does not need the explicit constant.)

### Theorem 6.2 (new output class)

The rate-one continuous-time SRW on `L(G_n)` has cutoff at

\[
\boxed{
T_n=\frac{s_n}{b}
=\frac{2(d-1)}{d-2}\log_{d-1}n
}
\tag{6.6}
\]

with window

\[
\boxed{O(\sqrt{\log n}).}
\tag{6.7}
\]

More precisely, the Gaussian adjacent-pair profile from Lemma 6.1 transfers after the time scaling `1/b`.

#### Proof

Apply Theorem 4.1. For the lower bound, `d_E(t)>=d_A(bt)`. For the matching upper bound at a profile-scale time `t`, choose any `tau_n -> infinity` with `tau_n=o(sqrt(L_n))`, for example `tau_n=log log n`, and use

\[
d_E(t)\le e^{-c\tau_n}+d_A(b(t-\tau_n)).
\]

The first term vanishes and `b tau_n=o(sqrt(L_n))`, so the two bounds have the same limiting profile. This proves (6.6)--(6.7). QED.

Because of Sections 5.1--5.2, if the base is edge-transitive then this gives a vertex-transitive spectral-expander cutoff theorem for an output family that lies strictly outside the long-range-expander hypothesis.

## 7. Explicit genuinely new transitive class

Kaufman--Lubotzky, arXiv:1108.2960, Theorem 3 constructs, for each fixed prime power `q` and growing `alpha` with `q^alpha>17`, a `(q+1)`-regular Ramanujan Cayley graph

\[
G_\alpha=\operatorname{Cay}(PSL_2(q^\alpha),S)
\quad\text{or}\quad
\operatorname{Cay}(PGL_2(q^\alpha),S),
\]

where `S` is one orbit of a non-split torus; in particular the graph is **edge-transitive**.

Take `q=2`. Then `(G_alpha)` is an explicit growing family of cubic edge-transitive Ramanujan graphs. Altschuler proves every Ramanujan graph is long-range expanding, so the hypotheses of Theorem 6.2 apply to the base family. Define

\[
X_\alpha=L(G_\alpha).
\]

Then:

1. `X_alpha` is **4-regular**;
2. `X_alpha` is **vertex-transitive**, because `G_alpha` is edge-transitive;
3. `X_alpha` is a **spectral expander**, by (5.1)--(5.3);
4. `(X_alpha)` is **not** a uniform long-range-expander sequence, by (5.4)--(5.6), since its ball growth is at most `O(2^r)` whereas a 4-regular LRE would demand the `3^r` branching scale;
5. nevertheless rate-one continuous-time SRW on `X_alpha` has total-variation cutoff at

\[
\boxed{T_\alpha=4\log_2 |V(G_\alpha)|}
\tag{7.1}
\]

(up to the harmless `O(1)` change obtained by writing the center in terms of `|V(X_alpha)|=3|V(G_alpha)|/2`) with window

\[
\boxed{O(\sqrt{\log |V(X_\alpha)|}).}
\tag{7.2}
\]

This is the required **proved application** of the transfer theory. It is source-valid for T08 (bounded degree, vertex transitive, uniform spectral gap) and is not already covered by Altschuler's long-range-expander theorem on the output graphs.

## 8. Sanity check actually executed

Before the proof was persisted, an exact rational-arithmetic script checked on `K_4,K_5,K_6`:

- `BB^T=dI+A`;
- `B^TB=2I+A_L`;
- `(Q-I)K=bK(P-I)`;
- `Q-I=c(KJ-I)`;
- `JK=(I+P)/2`;
- and the strict growth-base inequality `(d-1)/(2d-3)<1` for `3<=d<=10`.

Artifact:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_03-01-23__line_graph_transfer_exact.py`

creation commit `acc98a5029897f82210602ff44c3f522672df3d9`.

Archived executed output:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_03-01-23__line_graph_transfer_exact.out`

creation commit `c999d4358e892637512f72a0c3bf5af67218ffff`, terminal marker

`P26_T08_LINE_GRAPH_TRANSFER_EXACT_PASS`.

The finite check is only a sanity check of the algebra; the theorem above is symbolic and does not rely on finite enumeration.

## 9. Route comparison, failed route retained, and next attack

Three routes were compared in this run.

1. **Revive global curvature/subcommutation.** Rejected immediately because the inherited R16 handoff already proves that a uniform global subcommutation inequality fails on the regular tree; repeating it would violate the progress-first rule.
2. **Entropy deficit only.** The exact KL identity (3.1) was successful, but using it alone with a crude bad-radius mixture initially produced only an `O(sqrt(log n log log n))` window. That is a valid but unnecessarily weak transfer.
3. **Incidence heat-bath factorization.** The new identity `Q-I=c(KJ-I)` yields the sharp TV sandwich (4.1)--(4.2), removes the extra `sqrt(log log n)`, and gives the `O(sqrt(log n))` line-graph window. This is the route adopted.

### Residual obstruction

The full Salez Problem 2.3 still requires a mechanism applying to an **arbitrary** bounded-degree vertex-transitive spectral expander. The line-graph theorem enlarges the known family in a direction provably not captured by LRE, but it does not manufacture the missing NBRW endpoint entropy bound on every transitive expander.

A concise version of the remaining universal target is: prove, from transitivity plus a fixed spectral gap alone, enough entropy at the tree-front scale

\[
H(K_j(x,\cdot))=\log n-o(\sqrt{\log n})
\quad\text{for }j=\log_{d-1}n+O(\sqrt{\log n}),
\]

or replace this by a quotient-sensitive Green-function/local-Poincare statement that yields the same mixing-window control. Long-range expansion supplies a stronger `O(log log n)` entropy deficit, but spectral expansion alone currently does not.

### Next P26 attack

Generalize the exact `K,J` argument from line graphs to **bounded local incidence lifts / clique replacements** whose output remains transitive and spectrally expanding but has controlled smaller metric growth than its nominal tree branching factor. The decisive question is whether one can characterize a finite-state local Markov factorization

\[
Q_{out}-I=C(AB-I),\qquad BA=\alpha I+(1-\alpha)P_{base},
\]

that transfers a base entropy front and cutoff with `O(1)` overhead. A positive theorem would generate a much larger non-LRE closure class; a failure would isolate which local geometries destroy cutoff transfer.

The companion `NM13-01` should remain complementary by attacking the direct arbitrary-transitive entropy/Green-function front, not this local-lift closure.

## 10. ledger_delta

```yaml
ledger_delta:
  worker: P26
  parent: T08 / Salez arXiv:2508.21055 Problem 2.3
  parent_status_before: OPEN
  parent_status_after: OPEN / STRICTLY LARGER PROVED SUBCLASS
  source_level_advance:
    theorem: "continuous-time cutoff for line graphs of fixed-degree edge-transitive long-range expanders"
    output_scope: "bounded-degree vertex-transitive spectral expanders; output family provably not uniformly long-range expanding"
    cutoff_center: "[2(d-1)/(d-2)] log_{d-1} |V(base)|"
    window: "O(sqrt(log |V|))"
    explicit_class: "4-regular line graphs of Kaufman-Lubotzky cubic edge-transitive Ramanujan Cayley graphs"
  mechanism_advance:
    entropy_identity: "D(mu||pi_E)=D(mu K||pi_V)+conditional incidence KL, loss <= log d"
    varentropy_transfer: "sqrt(Varent_E)<=sqrt(Varent_V)+sqrt(log^2 d+4/e^2)"
    exact_ct_intertwining: "H_line(t) K = K H_base(b t), b=d/[2(d-1)]"
    heatbath_factorization: "Q-I=[d/(d-1)](KJ-I), JK=(I+P)/2"
    tv_transfer: "d_adj(bt)<=d_line(t); d_line(t+tau)<=exp(-d tau/(d-1))+d_adj(bt)"
  novelty: UNVERIFIED
  theorem_label: CANDIDATE_FULL_RESTRICTED / PENDING_LATER_INDEPENDENT_REVIEW
  full_parent_closed: false
  failed_route_preserved: "entropy-only transfer loses sqrt(log log n); global curvature route already obstructed on tree"
  companion_split: "P26 local-incidence transfer; NM13-01 direct arbitrary-transitive entropy/Green-function route"
```

End of substantive P26 T08 report.
