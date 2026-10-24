# PROB10-08 artifact — cutoff from a large long-range-expander quotient

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not authenticated GPT-6 maximum.** GPT-6 maximum was requested in the owner prompt, but no authenticated applied-model/reasoning telemetry is available in this runtime.

Status: **NEW REPOSITORY THEOREM / PARTIAL FOR SALEZ PROBLEM 2.3 / PUBLICATION NOVELTY UNVERIFIED / NOT INDEPENDENTLY AUDITED.**

This artifact is the complete mathematical proof package for the R16 / PROB10-08 iteration at `2026-09-20T00-47-46Z`. It does **not** claim the full source conjecture, and it does not treat an unproved quotient criterion as source progress: the theorem below has a complete proof under explicit hypotheses.

## 0. Frozen source and conventions

Source: Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3.

The source target is cutoff for every sequence of finite undirected vertex-transitive graphs with size tending to infinity, uniformly bounded degree and spectral gap bounded away from zero.

Throughout, simple random walk is the **rate-one continuous-time** walk

\[
H_t=\exp\{t(P-I)\},
\]

where `P` is the ordinary discrete SRW kernel. No lazy-time normalization is silently substituted.

Primary external input: Dylan J. Altschuler, *Long-range expanders: construction and cutoff*, arXiv:2609.14945v1 (submitted 14 September 2026). For fixed degree `d>=3` and fixed long-range-expansion constant `c>0`, the proof of his Proposition 3.1 supplies a uniform nonbacktracking endpoint-entropy estimate

\[
H(K_j^H(y,\cdot))\ge \log |V(H)|-C_{d,c}\log\log |V(H)|
\tag{0.1}
\]

for every start `y` and every `j` at least the entropic radius

\[
j_H:=\min\{j\ge1:d(d-1)^{j-1}\ge |V(H)|\}.
\tag{0.2}
\]

Only this endpoint-entropy input is imported from Altschuler below. The output graph in the new theorem need not itself be a long-range expander.

## 1. New idea, written before code

The previous R16 quantitative extension weakened Altschuler by allowing the **same graph** to have an LRE constant `c_n -> 0`. The new route instead changes category:

> A source graph may have poor long-range growth itself while possessing a large quotient, through an exact graph covering, whose nonbacktracking dynamics are long-range expanding. Because nonbacktracking paths project exactly under graph covers, the quotient's endpoint entropy is inherited upstairs with only the logarithm of the covering-fiber size as a possible information deficit. The source graph's own spectral gap can then dissipate that inherited deficit in continuous time.

This is not the line-graph transfer proved contemporaneously by the NM13/P26 cutoff workers: there the state space is the edge set and an incidence intertwining transfers a base-chain cutoff. Here the top graph and quotient have the **same degree**, the map is an exact graph covering, and only endpoint entropy is transferred; the top graph's own semigroup then does the final mixing.

No code is needed for the theorem; its core is analytic.

## 2. Definitions

Fix an integer `d>=3` and write

\[
q=d-1,\qquad v=\frac{d-2}{d}.
\tag{2.1}
\]

A map `pi:G->H` between connected simple `d`-regular graphs is a graph covering if for every `x in V(G)`, `pi` maps the `d` neighbors of `x` bijectively onto the `d` neighbors of `pi(x)`. For connected finite regular covers, every fiber has the same cardinality `k`; hence

\[
N:=|V(G)|=kM,\qquad M:=|V(H)|.
\tag{2.2}
\]

Let `K_j^G(x,.)` denote the endpoint law after `j` steps of nonbacktracking random walk (NBRW) on `G`, begun at `x` by choosing the first neighbor uniformly and thereafter choosing uniformly among the `q=d-1` edges not immediately reversing the previous edge. Define `K_j^H` analogously.

For a probability law `mu` on a finite set, `H(mu)=-sum mu log mu` denotes Shannon entropy with natural logarithms.

## 3. Exact cover projection for NBRW

### Lemma 3.1 — nonbacktracking path lifting

Let `pi:G->H` be a graph covering of connected `d`-regular graphs. Then for every `x in V(G)` and every `j>=0`,

\[
\boxed{\pi_*K_j^G(x,\cdot)=K_j^H(\pi x,\cdot).}
\tag{3.1}
\]

#### Proof

For `j=0` this is immediate. For `j>=1`, a covering is locally bijective at every vertex. Thus a first step from `x` is carried bijectively to a first step from `pi x`. If a path has already lifted through vertices `x_0,...,x_i`, then the allowed next vertices are the `d-1` neighbors of `x_i` other than `x_{i-1}`. Local bijectivity maps those allowed neighbors bijectively to the `d-1` neighbors of `pi x_i` other than `pi x_{i-1}`. Therefore projection maps the uniform NBRW path measure from `x` exactly to the uniform NBRW path measure from `pi x`. Taking endpoints gives (3.1). `QED`

### Lemma 3.2 — quotient endpoint entropy lifts without loss

Under the same hypotheses,

\[
\boxed{H(K_j^G(x,\cdot))\ge H(K_j^H(\pi x,\cdot)).}
\tag{3.2}
\]

#### Proof

Let `Y` have law `K_j^G(x,.)`. By Lemma 3.1, `pi(Y)` has law `K_j^H(pi x,.)`. The entropy chain rule gives

\[
H(Y)=H(\pi Y)+H(Y\mid \pi Y)\ge H(\pi Y).
\]

This is exactly (3.2). `QED`

The important point is that no conditional uniformity inside fibers is assumed or needed.

## 4. Main theorem

### Theorem 4.1 — cutoff from a large fixed-LRE quotient

Fix `d>=3`, `c>0`, and `gamma>0`. Let `(G_n)` be connected simple `d`-regular graphs with

\[
N_n:=|V(G_n)|\longrightarrow\infty
\]

and one-sided normalized spectral gap

\[
1-\lambda_2(P_{G_n})\ge \gamma.
\tag{4.1}
\]

Suppose that for each `n` there is a connected simple `d`-regular graph `H_n` and a graph covering

\[
\pi_n:G_n\longrightarrow H_n
\]

with constant fiber size `k_n`, so

\[
M_n:=|V(H_n)|=N_n/k_n,
\tag{4.2}
\]

and suppose `(H_n)` is a fixed-`c` long-range-expander family in Altschuler's sense:

\[
|B_{H_n}(S,r)|\ge
\min\left\{\frac{3M_n}{4},\ c|S|(d-1)^r\right\}
\tag{4.3}
\]

for every nonempty `S subset V(H_n)` and every integer `r>=0`.

Define

\[
L_n:=\log_{d-1}N_n,
\qquad
T_n:=\frac{1}{v}L_n=\frac{d}{d-2}\log_{d-1}N_n.
\tag{4.4}
\]

Then there is `C=C(d,c)` such that, uniformly over starts `x in V(G_n)`, the NBRW endpoint entropy satisfies

\[
H(K_j^{G_n}(x,\cdot))
\ge \log N_n-\Delta_n
\tag{4.5}
\]

for every

\[
j\ge j_n:=\min\{j:d(d-1)^{j-1}\ge N_n\},
\]

where

\[
\boxed{
\Delta_n:=\log k_n+C\log\log M_n+C.
}
\tag{4.6}
\]

Consequently, for every fixed `epsilon in (0,1/2)`,

\[
\boxed{
|t_{mix}^{G_n}(\epsilon)-T_n|
\le
C_{d,c,\gamma,\epsilon}
\left(\sqrt{L_n}+\Delta_n+1\right).
}
\tag{4.7}
\]

In particular, if

\[
\boxed{\log k_n=o(\log N_n),}
\tag{4.8}
\]

then rate-one continuous-time SRW on `(G_n)` exhibits total-variation cutoff and

\[
\boxed{
\frac{t_{mix}(\epsilon)-t_{mix}(1-\epsilon)}{t_{mix}(1/2)}
=O_{d,c,\gamma,\epsilon}\left(
(\log N_n)^{-1/2}
+\frac{\log k_n+\log\log M_n}{\log N_n}
\right)=o(1).
}
\tag{4.9}
\]

If additionally `(G_n)` is vertex-transitive, this is a complete source-admissible class for Salez Problem 2.3.

Moreover, if the stronger fiber condition

\[
\boxed{\log k_n=o(\sqrt{\log N_n})}
\tag{4.10}
\]

holds, then the total-variation profile is Gaussian on the optimal square-root scale: for every fixed real `z`, uniformly over starts,

\[
\boxed{
\left\|\delta_x H^{G_n}_{T_n+z\sqrt{L_n}}-\pi_n\right\|_{TV}
\longrightarrow
\Phi(-v^{3/2}z),
}
\tag{4.11}
\]

where `Phi` is the standard normal distribution function.

The theorem does **not** assume that `G_n` itself is a long-range expander.

## 5. Proof of the endpoint-entropy estimate

Let

\[
j_H(n)=\min\{j:dq^{j-1}\ge M_n\}.
\]

Since `M_n<=N_n`,

\[
j_n\ge j_H(n).
\tag{5.1}
\]

Altschuler's Proposition 3.1, with fixed `d,c`, gives for every `y in H_n` and every `j>=j_H(n)`,

\[
H(K_j^{H_n}(y,\cdot))
\ge \log M_n-C_{d,c}\log\log M_n-C_{d,c}.
\tag{5.2}
\]

For `j>=j_n`, Lemma 3.2 and (5.2) give

\[
H(K_j^{G_n}(x,\cdot))
\ge \log M_n-C\log\log M_n-C.
\tag{5.3}
\]

Since `N_n=k_nM_n`,

\[
\log M_n=\log N_n-\log k_n.
\]

Substituting into (5.3) yields (4.5)-(4.6). `QED`

This is the exact quantitative price of passing from the LRE quotient back to the top graph: at worst `log k_n` bits/nats of endpoint entropy are unavailable from the quotient.

## 6. Continuous-time entropy dissipation on the top graph

The final mixing argument uses only the **top graph's own one-sided spectral gap**, not an LRE property upstairs.

### Lemma 6.1 — entropy deficit to TV under a one-sided gap

Let `G` be a finite regular graph, `P` its SRW kernel, `pi` uniform, and suppose

\[
1-\lambda_2(P)\ge\gamma>0.
\]

For any initial law `mu`, let `mu_s=mu e^{s(P-I)}`. Then

\[
\boxed{
\|\mu_s-\pi\|_{TV}
\le
\sqrt{\frac{D(\mu\|\pi)}{4\gamma s}}
\qquad(s>0).
}
\tag{6.1}
\]

#### Proof

Write `f_s=mu_s/pi`. For the reversible rate-one semigroup,

\[
-\frac d{ds}D(\mu_s\|\pi)
=\mathcal E_P(f_s,\log f_s).
\tag{6.2}
\]

The pointwise inequality

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2
\]

gives

\[
\mathcal E_P(f_s,\log f_s)
\ge4\mathcal E_P(\sqrt{f_s},\sqrt{f_s}).
\tag{6.3}
\]

Poincare gives

\[
\mathcal E_P(\sqrt{f_s},\sqrt{f_s})
\ge\gamma\operatorname{Var}_\pi(\sqrt{f_s}).
\tag{6.4}
\]

Finally, by Cauchy-Schwarz,

\[
\|\mu_s-\pi\|_{TV}^2
\le\operatorname{Var}_\pi(\sqrt{f_s}).
\tag{6.5}
\]

Indeed, with `m=E_pi sqrt(f_s)`,

\[
\frac12E_\pi|f_s-1|
\le\frac12\sqrt{E(\sqrt f-1)^2 E(\sqrt f+1)^2}
=\sqrt{1-m^2}.
\]

Combining (6.2)-(6.5), integrating from `0` to `s`, and using monotonicity of TV under a Markov semigroup,

\[
D(\mu\|\pi)
\ge4\gamma\int_0^s\|\mu_u-\pi\|_{TV}^2du
\ge4\gamma s\|\mu_s-\pi\|_{TV}^2.
\]

This proves (6.1). `QED`

For `mu=K_j^{G_n}(x,.)`, (4.5) says

\[
D(\mu\|\pi_n)=\log N_n-H(\mu)\le\Delta_n.
\tag{6.6}
\]

Thus after

\[
s_{n,\epsilon}:=\frac{\Delta_n+1}{\gamma\epsilon^2},
\tag{6.7}
\]

all such endpoint laws with `j>=j_n` are within `epsilon/2` of stationarity (the harmless `+1` absorbs finite-small cases and constants).

Continuous time is useful here: the argument needs only `1-lambda_2>=gamma`; no lower bound on the most negative eigenvalue is required.

## 7. Covering-tree representation and radial CLT

Let `R_t` be the graph distance from the root of rate-one continuous-time SRW on the infinite `d`-regular tree. Projection through the universal cover gives the exact mixture

\[
\boxed{
H_t^{G_n}(x,\cdot)
=\sum_{j\ge0}\Pr(R_t=j)K_j^{G_n}(x,\cdot).
}
\tag{7.1}
\]

The radial chain has positive-level increments `+1` with probability `q/d` and `-1` with probability `1/d`, with drift

\[
v=\frac{d-2}{d}.
\]

The number of returns to the root is tight (indeed geometrically tailed), so it changes the iid-increment approximation by `O_P(1)`. Poissonizing the increments gives the standard continuous-time CLT

\[
\boxed{
\frac{R_t-vt}{\sqrt t}\Rightarrow N(0,1).
}
\tag{7.2}
\]

The variance parameter is `E xi^2=1` for the rate-one compound-Poisson walk. This normalization is what produces the constant `v^{3/2}` in (4.11).

Also, every `d`-regular graph ball satisfies

\[
|B(x,r)|\le C_dq^r.
\tag{7.3}
\]

## 8. Upper mixing bound

Use the semigroup split

\[
H^{G_n}_{t+s}=H^{G_n}_tH^{G_n}_s.
\]

Conditioning in (7.1), every radial term with `j>=j_n` has entropy deficit at most `Delta_n`; after applying `H_{s_{n,epsilon}}`, Lemma 6.1 makes it at most `epsilon/2` from stationarity. Therefore

\[
d_{G_n}(t+s_{n,\epsilon})
\le\Pr(R_t<j_n)+\epsilon/2,
\tag{8.1}
\]

where `d_G` denotes worst-start TV distance (the bound is uniform in starts even without transitivity).

Since

\[
j_n=L_n+O_d(1),
\tag{8.2}
\]

put

\[
t=T_n+A\sqrt{L_n}
=\frac{L_n}{v}+A\sqrt{L_n}.
\]

Then by (7.2), for every fixed `epsilon`, an `A=A(d,epsilon)` can be chosen so that

\[
\limsup_n\Pr(R_t<j_n)\le\epsilon/2.
\tag{8.3}
\]

Thus

\[
t_{mix}(\epsilon)
\le T_n+C_{d,\epsilon}\sqrt{L_n}+s_{n,\epsilon}.
\tag{8.4}
\]

Using (6.7) proves the upper half of (4.7).

## 9. Lower mixing bound

Set

\[
t=T_n-A\sqrt{L_n}
\]

and choose

\[
r_n=L_n-\frac{vA}{2}\sqrt{L_n}.
\tag{9.1}
\]

By the radial CLT, for `A=A(d,epsilon)` sufficiently large,

\[
\liminf_n\Pr(R_t\le r_n)\ge1-\epsilon.
\tag{9.2}
\]

On the event `R_t<=r_n`, the projected walk lies in the graph ball `B(x,r_n)`. Its stationary mass is, by (7.3),

\[
\pi_n(B(x,r_n))
\le\frac{C_dq^{r_n}}{N_n}
\le C_dq^{-vA\sqrt{L_n}/2}\longrightarrow0.
\tag{9.3}
\]

Hence

\[
\|\delta_xH_t-\pi_n\|_{TV}
\ge1-\epsilon-o(1),
\tag{9.4}
\]

uniformly in `x`. Therefore

\[
t_{mix}(1-\epsilon)
\ge T_n-C_{d,\epsilon}\sqrt{L_n}.
\tag{9.5}
\]

Combining (8.4) and (9.5) proves (4.7).

If `log k_n=o(log N_n)`, then `Delta_n=o(L_n)`, so (4.7) gives

\[
t_{mix}(1/2)=T_n+o(L_n)\sim T_n.
\tag{9.6}
\]

Subtracting the two fixed-accuracy bounds and dividing by (9.6) yields (4.9). This proves cutoff under (4.8). `QED`

## 10. Gaussian profile under sub-square-root fiber entropy

Assume now

\[
\Delta_n=o(\sqrt{L_n}),
\]

which follows from (4.10). Define

\[
s_n:=\sqrt{(\Delta_n+1)\sqrt{L_n}}.
\tag{10.1}
\]

Then

\[
s_n\to\infty,\qquad s_n=o(\sqrt{L_n}),\qquad \Delta_n/s_n\to0.
\tag{10.2}
\]

For fixed `z`, apply (8.1) with total time

\[
T_n+z\sqrt{L_n}
\]

and split off `s_n`. Lemma 6.1 makes the entropy-deficient terms `o(1)` in TV, while subtracting `s_n=o(sqrt L_n)` does not affect the radial CLT. From (7.2),

\[
\Pr(R_{T_n+z\sqrt{L_n}-s_n}<j_n)
\longrightarrow
\Phi(-v^{3/2}z).
\tag{10.3}
\]

This gives the upper profile bound.

For the lower profile, choose any `a_n->infinity` with `a_n=o(sqrt L_n)`, e.g. `a_n=L_n^{1/4}`, and use the ball

\[
B(x,L_n-a_n).
\]

Its stationary mass is `O(q^{-a_n})=o(1)`, while the radial CLT gives

\[
\Pr(R_{T_n+z\sqrt{L_n}}\le L_n-a_n)
\longrightarrow\Phi(-v^{3/2}z).
\tag{10.4}
\]

Therefore the TV liminf is at least the same Gaussian tail. Combined with (10.3), this proves (4.11). `QED`

## 11. What this proves and what it does not

### Proved graph class

The theorem covers any fixed-degree regular spectral-expander sequence admitting a fixed-LRE graph-cover quotient whose fiber size satisfies

\[
k_n=N_n^{o(1)}.
\]

For the Salez source, take the vertex-transitive subfamily. The top graphs themselves are **not assumed LRE**, so this is structurally weaker than applying Altschuler directly to the top graph.

A stronger quantitative conclusion holds if `log k_n=o(sqrt(log N_n))`: the source-continuous-time Gaussian cutoff profile and optimal `Theta(sqrt(log N_n))` window are recovered.

### Not proved

1. It is **not proved** that every bounded-degree vertex-transitive spectral expander admits such a quotient.
2. It is **not proved** that the theorem's graph class is disjoint from every previously published cutoff class. Publication priority/class novelty is therefore **UNVERIFIED**.
3. No explicit source-valid counterexample to Salez Problem 2.3 is produced.
4. No assertion is made that finite mixing plots decide an asymptotic sequence claim.
5. This theorem does not replace the canonical parent claim or close Problem 2.3.

## 12. Three approaches compared in this run

### A. Large LRE quotient through a finite graph cover — SUCCESS

This is Theorem 4.1. It replaces long-range expansion of the **top graph** by two weaker ingredients living in different places:

- endpoint entropy from a large fixed-LRE quotient;
- entropy dissipation from the top graph's own spectral gap.

The exact price is `log k_n` in entropy, leading to the explicit window ratio (4.9).

### B. Improve the cubic `c^3` loss inside Altschuler's Lemma 3.2 — ARCHITECTURAL BARRIER

The previous R16 run retained constants in Altschuler's graph-to-oriented-edge transfer and found directed growth constant `a=Omega_d(c^3)`. Re-reading the full proof shows why the exponent is built into that exact subtraction architecture.

The proof chooses `k` so that the exceptional terminal set from short nonbacktracking collisions satisfies

\[
q^{-k}\lesssim c.
\]

It then pays a path-length overhead `2k` before invoking graph LRE. A directed growth constant therefore contains the factor

\[
cq^{-2k}=\Theta_d(c^3).
\]

Without replacing either the collision estimate or the two-sided `2k` synchronization, constant optimization inside the same argument cannot remove the cubic scale. This is a precise reason not to spend the run shaving constants on the already-used vanishing-LRE route.

### C. Transitivity-only NBRW collision / spectral-density route — PRIOR-ART PRUNE + REMAINING GAP

On a vertex-transitive graph the diagonal of polynomial kernels such as `K_jK_j^*` is constant, so a Renyi-entropy lower bound from collision probabilities is tempting. Spectrally, this becomes control of nonbacktracking polynomials across the adjacency spectrum.

However, the corresponding strong spectral-density hypothesis is already close to the Sarnak--Xue density framework used by Golubev--Kamber to prove cutoff for vertex-transitive graphs. Thus merely proving a density-conditioned statement would mostly repackage a known positive regime, not move the arbitrary spectral-expander source.

The real missing implication remains:

> Does vertex transitivity plus a fixed ordinary spectral gap force enough **entropic-scale nonbacktracking collision control**, without a Sarnak--Xue-type spectral density assumption?

Nothing in this run proves that implication, so it is not recorded as source progress.

## 13. Exact self-checks / tests actually performed

No finite numerical checker was created, because no finite-enumeration claim is used. The analytic self-checks were:

1. **Fiber-one check:** `k_n=1` reduces (4.6) to the standard fixed-LRE endpoint entropy deficit `O(log log N)`, and Theorem 4.1 recovers a continuous-time cutoff theorem consistent with Altschuler after normalization.
2. **Entropy direction check:** entropy goes **up** when lifting from quotient to cover, because `H(Y)=H(piY)+H(Y|piY)`; no false fiber-uniformity assumption occurs.
3. **Normalization check:** rate-one continuous-time tree drift is `v=(d-2)/d`, so the center is `L_n/v=d/(d-2) log_{d-1}N_n`, matching the source convention used in the previous R16 artifact.
4. **Variance check:** compound-Poisson radial variance parameter is `E xi^2=1`, giving profile `Phi(-v^(3/2)z)` on the `sqrt(L_n)` time scale.
5. **Spectral-sign check:** Lemma 6.1 uses only `1-lambda_2>=gamma`; no absolute spectral gap is smuggled in, so near-bipartite top graphs are allowed in continuous time.
6. **Known-peer collision check:** the contemporaneous line-graph theorem uses incidence kernels between edge and vertex walks; Theorem 4.1 uses same-degree graph covers and NBRW path lifting. The mechanisms and hypotheses are distinct.

## 14. Remaining full-scope gap

The source-level obstruction is now sharply expressible. To settle Salez Problem 2.3 using this mechanism, one would need to prove that every bounded-degree vertex-transitive spectral expander has a sufficiently large entropically good quotient/structure—or replace the quotient by a direct transitivity-based estimate giving

\[
\log N-H(K_{j_N}(x,\cdot))=o(\log N)
\]

uniformly at the entropic radius. Ordinary spectral expansion alone does not currently provide such a statement through the known nonbacktracking spectral-density technology.

A source-valid counterexample family, if one exists, must in particular evade the theorem above: it cannot have both a uniform top spectral gap and a fixed-LRE graph-cover quotient of size `N^{1-o(1)}`.

## 15. Consumed repository history

This artifact was derived only after recovering the controlling and neighboring state, including:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/I0112.md`;
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`;
- `runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md`;
- `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`;
- `runs/R16/2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction.md`;
- `runs/R16/2026-09-16T21-42-29Z_i0112-hecke-information-curvature-obstruction.md`;
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`;
- `runs/R16/2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction.md`;
- `runs/prob10_2026-09-20/PROB10-08/2026-09-20T00-12-25Z_vanishing-lre-continuous-cutoff_6e4b.md`;
- `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T00-00-13Z__line-graph-lre-transfer.md`;
- `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_03-01-23__line-graph-entropy-transfer.md`.

The posted Abelian Cayley/product-condition target remains excluded and was not reopened.
