Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — symmetrized nonbacktracking arc covers, Hodge-Green TV cancellation, and finite-alphabet orbit drift

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorem A and Lemmas B–C below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The oriented-edge/symmetrized-nonbacktracking cutoff theorem and the Hodge-Green total-variation estimate are new to the checked repository state. Fresh bounded searches on 20 September 2026 for combinations of `symmetrized nonbacktracking random walk cutoff`, `oriented edge graph cutoff`, `directed edge graph cutoff expander`, and `arc graph random walk cutoff` did not locate this exact theorem. This is negative evidence only, not a worldwide priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.  
Pre-write master observed immediately before persistence work: `9befcc945ed8c6961a211c6f79b429aaa21c2652`.

## 0. Short continuity handoff and partner split

LIVE20 assigns NM13-01 to T08 and supersedes the old intake-only loop. The pre-LIVE P0292 handoff remains preserved and untouched.

The newest own substantive report before this run was

`2026-09-20T05-00-20Z__exact-distance-k-orbit-compression.md`.

It proved cutoff for every fixed pure exact-distance-`k` graph (`k>=3`) on suitable high-girth transitive Ramanujan bases and established an exact root-stabilizer orbit quotient preserving the full point-start TV curve, likelihood ratio, all f-divergences and varentropy. Its remaining general obstruction was that the quotient can still have high rank, so factor existence alone does not force information concentration.

The newest relevant P26 report read this run was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_07-58-10__ramanujan-spherical-set-transfer.md`.

P26 now owns a complementary spherical-shell/Green route: it proves a Ramanujan spherical-distance-set transfer and a distance-`{2,3}` application. This run does **not** repeat that mechanism. Instead it works on an oriented-edge 2-cover of a line graph and uses an exact antisymmetric Hodge decomposition plus an `L^1` Green bound. The second mechanism below returns to the stabilizer quotient and shows that its orbit-size drift has a finite alphabet depending only on the degree.

The substantive gains are:

1. a genuinely new source-valid class outside fixed long-range expansion: symmetrized nonbacktracking arc graphs of fixed-degree arc-transitive LRE bases, with a quantitative `O(sqrt(log n))` cutoff window; and
2. removal of a concrete obstruction exposed by earlier product/trace experiments: a `Theta(n)`-dimensional slow local eigenspace does **not** force a `sqrt(n)` TV penalty. For this cover, Hodge-Green cancellation reduces the point-source contribution to `O(log n)e^{-ct}`. More generally, stabilizer-orbit size growth is a bounded-jump martingale plus an additive functional taking values in a finite degree-dependent drift alphabet.

No historical/peer file, POSTED claim, shared root ledger, scheduler, permission, workflow, email/Drive object, or public surface is modified.

## 1. Source convention and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), uses the rate-one continuous-time convention
\[
P_t=e^{t(T-I)}
=e^{-t}\sum_{m\ge0}\frac{t^mT^m}{m!}.
\tag{1.1}
\]
Problem 2.3 asks to prove cutoff for all bounded-degree vertex-transitive expander sequences.

The current primary boundary was refreshed on 20 September 2026.

* Dylan J. Altschuler, `arXiv:2609.14945v1` (14 September 2026), proves Gaussian-profile cutoff for every fixed-degree fixed-constant **long-range expander**. The same paper establishes the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}
  \Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus LRE is strictly stronger than Salez's source hypothesis.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345` (6 July 2026), prove that the local-product/non-equilibrium-Poincare condition implies cutoff. No checked theorem there derives the needed condition solely from vertex transitivity plus an ordinary spectral gap.
* Salez, `arXiv:2307.10066`, proves that on sparse uniformly expanding chains cutoff is equivalent to the varentropy criterion. In particular, for bounded-degree expanders with `t_mix=Theta(log n)`, a worst-start varentropy estimate `o((log n)^2)` at mixing time is sufficient.
* Kaufman--Lubotzky, `arXiv:1108.2960`, construct explicit fixed-degree edge-transitive Ramanujan Cayley families with a cyclic local symmetry acting transitively on the generating set. Their `G semidirect T` action is transitive on oriented edges, so these supply explicit arc-transitive bases. Altschuler then supplies LRE for those Ramanujan bases.

The root `POSTED.md` exclusion for the already-written Salez Problem 2.4 Abelian-Cayley/product-condition manuscript was rechecked and is not reopened here. No posted T08 claim matching the arc-cover theorem below was found.

A bounded fresh search for a full resolution of the transitive spectral-expander conjecture again returned Altschuler's LRE theorem as the relevant September 2026 advance, not a proof for arbitrary transitive spectral expanders. This is bounded status evidence, not a proof of worldwide openness.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was `OPEN`.

Checked positive scope already included Altschuler's LRE theorem and repository classes outside fixed LRE: Cartesian/synchronous/strong products, line graphs, truncations, finite and twisted fibers, incidence-strong products, graph/distance rewiring, pure exact-distance graphs and P26's finite spherical-distance sets.

### After this run

Salez Problem 2.3 remains `OPEN`.

The proved scope expands by the following class.

> **Theorem A — cutoff for symmetrized nonbacktracking arc graphs.**  
> Fix `d>=3`, put `q=d-1`, and let `(G_n)` be a sequence of connected simple `d`-regular **arc-transitive** fixed-constant long-range expanders with `n=|V(G_n)| -> infinity`. Define `A_n` to have vertex set the oriented edges
> \[
> \vec E(G_n)=\{(u,v):uv\in E(G_n)\},
> \]
> and join `(u,v)` to
> \[
> (v,w)\quad(w\sim v,\;w\ne u)
> \]
> and to
> \[
> (w,u)\quad(w\sim u,\;w\ne v).
> \]
> Then `A_n` is a simple `2(d-1)`-regular vertex-transitive spectral-expander sequence, it is not a fixed-constant long-range-expander sequence, and Salez-convention continuous-time SRW on `A_n` has cutoff at
> \[
> \boxed{T_n=\frac{2(d-1)}{d-2}\log_{d-1}n}
> \tag{2.1}
> \]
> with window
> \[
> \boxed{O_{d,c,\varepsilon}(\sqrt{\log n})}
> =O(\sqrt{\log |V(A_n)|}).
> \tag{2.2}
> \]
> In fact, throughout every `O(sqrt(log n))` window about `T_n`, the TV curve of `A_n` differs by `o(1)` from the TV curve of the line graph `L(G_n)` under the line-graph walk from the corresponding unoriented edge.

If the base normalized SRW gap is at least `gamma`, the proof gives the explicit output bound
\[
\boxed{
\operatorname{gap}(A_n)
\ge
\min\left\{
\frac{d}{2(d-1)}\gamma,\;
\frac{d-2}{d-1}
\right\}.
}
\tag{2.3}
\]

For the explicit degree-six Kaufman--Lubotzky/Ramanujan input (`d=6,q=5`), `A_n` has degree `10` and `6n` vertices, and
\[
\boxed{
T_n=\frac52\log_5 n
=\frac52\log_5\!\left(\frac{|V(A_n)|}{6}\right)
}
\tag{2.4}
\]
with `O(sqrt(log |V(A_n)|))` window. Ramanujan gives
\[
\gamma\ge1-\frac{\sqrt5}{3},
\]
hence
\[
\boxed{
\operatorname{gap}(A_n)\ge\frac{3-\sqrt5}{5}.
}
\tag{2.5}
\]

This is source-valid movement: the output graphs themselves are bounded-degree, vertex-transitive **spectral** expanders and are proved not to satisfy any fixed LRE constant.

## 3. The arc graph is a nontrivial two-cover of the line graph

Let `G` be connected simple `d`-regular and `q=d-1`. Write `Q_A` for discrete SRW on the new arc graph and `Q_L` for discrete SRW on `L(G)`.

The projection
\[
\rho(u,v)=\{u,v\}
\tag{3.1}
\]
is a strong lumping. Indeed, from `(u,v)`, the `q` successor arcs project bijectively to the line-neighbors of `{u,v}` meeting `v`, and the `q` predecessor arcs project bijectively to those meeting `u`. Thus every one of the `2q` line-neighbors has exactly one lift among the `2q` arc-neighbors.

Therefore
\[
\rho(X_t^A)
\stackrel{d}{=}
X_t^L
\tag{3.2}
\]
in the exact source continuous-time convention, when both start above the same edge.

This is a genuine 2-cover, not a product with an independently refreshed two-point fiber: conditioned on the projected line path, the orientation sheet is transported deterministically. That is precisely why P26's finite-fiber reset argument and NM13-01's earlier twisted-fiber argument do not subsume the theorem.

Arc transitivity of `G` makes `A` vertex-transitive, because automorphisms act transitively on ordered adjacent pairs.

## 4. Exact even/odd spectral decomposition

Let `J` reverse arcs:
\[
(Jf)(u,v)=f(v,u).
\]
Then `JQ_A=Q_AJ`, so arc functions split into `J`-even and `J`-odd subspaces.

### 4.1 Even sector

Even functions are exactly lifts of functions on unoriented edges, and by the strong lumping,
\[
Q_A|_{\rm even}\cong Q_L.
\tag{4.1}
\]

If `P` is normalized SRW on `G` and `lambda` is a base eigenvalue, the corresponding line eigenvalue is
\[
\mu_+(\lambda)
=
\frac{d\lambda+d-2}{2q}
=
1-\frac{d}{2q}(1-\lambda),
\tag{4.2}
\]
with the usual extra line-graph eigenvalue `-1/q`. Thus the nonconstant even sector has gap at least `d gamma/(2q)`.

### 4.2 Odd sector and Hodge decomposition

For an odd function/flow `f(v,u)=-f(u,v)`, define divergence
\[
(Df)(u)=\sum_{v\sim u}f(u,v)
\tag{4.3}
\]
and gradient
\[
(\nabla g)(u,v)=g(v)-g(u).
\tag{4.4}
\]

A direct successor/predecessor calculation gives
\[
\begin{aligned}
(2qQ_Af)(u,v)
&=
\sum_{w\sim v,\ w\ne u}f(v,w)
+
\sum_{w\sim u,\ w\ne v}f(w,u)\\
&=Df(v)-Df(u)+2f(u,v).
\end{aligned}
\]
Hence on the odd subspace,
\[
\boxed{
Q_A
=
\frac1q I+\frac1{2q}\nabla D.
}
\tag{4.5}
\]

Also
\[
\boxed{
D\nabla=d(P-I).
}
\tag{4.6}
\]

The odd flow space splits orthogonally into gradients and divergence-free cycle flows. If `Pg=lambda g`, then
\[
Q_A\nabla g
=
\frac{d\lambda-(d-2)}{2q}\nabla g.
\tag{4.7}
\]
On `ker D`,
\[
\boxed{
Q_Af=\frac1qf.
}
\tag{4.8}
\]

Since a connected `d>=3` regular graph has cycle-space dimension
\[
|E|-|V|+1=\left(\frac d2-1\right)n+1,
\tag{4.9}
\]
this is an **extensive** eigenvalue-`1/q` sector. Nevertheless its one-sided continuous-time decay rate is the fixed constant
\[
g_o=1-\frac1q=\frac{d-2}{d-1}.
\tag{4.10}
\]
Equations (4.1)--(4.10) prove the spectral bound (2.3).

The key point is that multiplicity alone is not the TV obstruction; an `L^2` point-mass bound would insert a misleading `sqrt(n)` prefactor. The next section removes it.

## 5. Hodge-Green `L^1` cancellation removes the `sqrt(n)` penalty

Fix an oriented edge `a=(u,v)` and its reversal `\bar a=(v,u)`. Let
\[
f_0=\delta_a-\delta_{\bar a},
\tag{5.1}
\]
viewed as an odd signed flow. From (4.5),
\[
Q_A-I
=
-\frac{q-1}{q}I+\frac1{2q}\nabla D
\tag{5.2}
\]
on the odd subspace. Therefore, with `s=t/(2q)`,
\[
e^{t(Q_A-I)}f_0
=
e^{-g_ot}e^{s\nabla D}f_0.
\tag{5.3}
\]

The elementary `AB/BA` semigroup identity gives
\[
e^{s\nabla D}f_0
=
f_0+
\nabla\int_0^s e^{rD\nabla}Df_0\,dr.
\tag{5.4}
\]
Here
\[
Df_0=\delta_u-\delta_v,
\qquad
D\nabla=d(P-I),
\tag{5.5}
\]
so
\[
e^{s\nabla D}f_0
=
f_0+\nabla\psi_s,
\qquad
\psi_s
=
\int_0^s e^{rd(P-I)}(\delta_u-\delta_v)\,dr.
\tag{5.6}
\]

Now use only regularity and the base spectral gap `gamma`. For any vertex function `h`,
\[
\|\nabla h\|_{\ell^1(\vec E)}
\le2d\|h\|_{\ell^1(V)}.
\tag{5.7}
\]
The signed heat-kernel difference satisfies
\[
\left\|
e^{rd(P-I)}(\delta_u-\delta_v)
\right\|_1
\le
\min\left\{
2,\sqrt{2n}e^{-d\gamma r}
\right\}.
\tag{5.8}
\]
The first bound is trivial; the second is `L^2(pi)` contraction followed by Cauchy--Schwarz.

Integrating to infinity,
\[
\int_0^\infty
\min\left\{
2,\sqrt{2n}e^{-d\gamma r}
\right\}dr
\le
\frac{\log n+2}{d\gamma}.
\tag{5.9}
\]
Hence, uniformly in `s>=0`,
\[
\boxed{
\|e^{s\nabla D}f_0\|_1
\le
2+\frac{2(\log n+2)}{\gamma}.
}
\tag{5.10}
\]

Combining (5.3) and (5.10),
\[
\boxed{
\|e^{t(Q_A-I)}f_0\|_1
\le
2\left[
1+\frac{\log n+2}{\gamma}
\right]e^{-g_ot}.
}
\tag{5.11}
\]

This is the decisive cancellation estimate. The odd eigenspace has dimension `Theta(n)`, but the signed point-source pays only `O(log n)`, not `sqrt(n)`.

## 6. TV sandwich and proof of Theorem A

Decompose
\[
\delta_a
=
\eta_a+\nu_a,
\qquad
\eta_a=\frac12(\delta_a+\delta_{\bar a}),
\qquad
\nu_a=\frac12(\delta_a-\delta_{\bar a}).
\tag{6.1}
\]

The even law `eta_a` evolves as the uniform two-orientation lift of line-graph walk from the underlying edge `e={u,v}`. Therefore
\[
\left\|
\eta_ae^{t(Q_A-I)}-\pi_A
\right\|_{TV}
=
d_L(t).
\tag{6.2}
\]

Projection cannot increase total variation, so
\[
d_A(t)\ge d_L(t).
\tag{6.3}
\]
By the triangle inequality and (5.11),
\[
\boxed{
d_A(t)
\le
d_L(t)
+
\frac12
\left[
1+\frac{\log n+2}{\gamma}
\right]
e^{-g_ot}.
}
\tag{6.4}
\]

The prior NM13-01 line-graph theorem, proved by exact incidence intertwining from Altschuler's LRE cutoff, gives
\[
T_n=\frac{2q}{q-1}\log_q n
\tag{6.5}
\]
and `O(sqrt(log n))` line-graph window.

At that center,
\[
g_oT_n
=
\frac{q-1}{q}
\frac{2q}{q-1}\log_q n
=
2\log_q n.
\tag{6.6}
\]
For every fixed `q>=2` and fixed `C`,
\[
(\log n)
\exp\left(
-g_o[T_n-C\sqrt{\log n}]
\right)
=
n^{-2/\log q+o(1)}\log n
=o(1).
\tag{6.7}
\]
Thus the error in (6.4) is `o(1)` uniformly across every `O(sqrt(log n))` cutoff window. Together with (6.3), the arc and line TV curves agree up to `o(1)` there. The line cutoff therefore transfers with the same center and window. This proves Theorem A. `QED`

The same argument transfers any limiting profile already available for the corresponding line family; only the center/window statement is credited here because it is the dependency already certified in the preceding NM13-01 report.

## 7. The output class is provably outside fixed long-range expansion

The projection `rho:A->L(G)` is distance non-increasing and each line vertex has two arc lifts. A line-graph ball of radius `r` around an edge in a `d`-regular graph contains at most the corresponding ball in the line graph of the infinite `d`-regular tree:
\[
|B_L(e,r)|
\le
1+2\sum_{j=1}^r q^j
\le C_dq^r.
\tag{7.1}
\]
Therefore
\[
|B_A(a,r)|\le2C_dq^r.
\tag{7.2}
\]

But `A` has degree `D=2q`, so the LRE tree benchmark uses
\[
D-1=2q-1>q.
\tag{7.3}
\]
If a fixed `c'>0` made `(A_n)` a `c'`-LRE sequence, apply the singleton lower-growth requirement at
\[
r_n=\left\lfloor\frac12\log_{2q-1}|V(A_n)|\right\rfloor.
\]
Its required lower bound is on the `(2q-1)^{r_n}` scale, while (7.2) is on the `q^{r_n}` scale, and their ratio tends to zero. Contradiction.

Thus this theorem is not an application of Altschuler to the **output** graph.

## 8. A second obstruction removal: finite-alphabet drift in the canonical transitivity quotient

The preceding report's exact stabilizer-orbit quotient is now pushed one step further.

Let `X` be a connected `d`-regular vertex-transitive graph, root `o`, transitive automorphism group `Gamma`, stabilizer `H=Gamma_o`, and stabilizer orbits `O_i`. Put
\[
m_i=|O_i|,
\qquad
\bar\pi_i=\frac{m_i}{n},
\]
and let `c_ij` be the number of neighbors in `O_j` of a vertex of `O_i`. Then
\[
\bar P(i,j)=\frac{c_{ij}}d,
\qquad
m_ic_{ij}=m_jc_{ji}.
\tag{8.1}
\]

Define the orbit-size potential
\[
h(i)=\log m_i.
\tag{8.2}
\]
Whenever `c_ij>0`,
\[
h(j)-h(i)
=
\log\frac{m_j}{m_i}
=
\log\frac{c_{ij}}{c_{ji}},
\tag{8.3}
\]
so
\[
|h(j)-h(i)|\le\log d.
\tag{8.4}
\]

Let `Y_t` be the rate-one continuous-time quotient chain and
\[
b(i)
=
(\bar P-I)h(i)
=
\sum_j\frac{c_{ij}}d
\log\frac{c_{ij}}{c_{ji}}.
\tag{8.5}
\]

Because all nonzero `c_ij,c_ji` are integers in `{1,...,d}` and each row has at most `d` positive destinations, the possible values of `b(i)` form a **finite set**
\[
\mathcal B_d
\tag{8.6}
\]
depending only on `d`, not on `n` or the quotient rank.

Dynkin's formula yields the exact decomposition
\[
\boxed{
h(Y_t)
=
M_t+A_t,
\qquad
A_t=\int_0^t b(Y_s)\,ds,
}
\tag{8.7}
\]
with `M_t` a martingale (since `h(Y_0)=h(o)=0`). Its predictable quadratic variation is
\[
\langle M\rangle_t
=
\int_0^t
\sum_j\bar P(Y_s,j)
[h(j)-h(Y_s)]^2\,ds
\le
(\log d)^2t.
\tag{8.8}
\]
Consequently
\[
\boxed{
\mathbb E[M_t^2]\le(\log d)^2t.
}
\tag{8.9}
\]

Moreover
\[
A_t
=
\sum_{\beta\in\mathcal B_d}
\beta L_t(\beta),
\qquad
L_t(\beta)
=
\int_0^t\mathbf1_{\{b(Y_s)=\beta\}}\,ds.
\tag{8.10}
\]
Thus all random orbit-size drift is controlled by the occupation vector of **finitely many local drift types**, plus universal `sqrt(t)` martingale noise. High quotient rank by itself does not create arbitrary orbit-size fluctuation.

This is a purely transitivity-specific statement: (8.3) is the stabilizer edge-balance identity.

## 9. Quantitative varentropy reduction on the quotient

Let `nu_t` be the quotient law from the root and let `r` be the number of stabilizer orbits. Because the full walk is uniform within each orbit,
\[
H(X_t)
=
H(\nu_t)+\mathbb E[h(Y_t)],
\tag{9.1}
\]
and for `X_t` lying in orbit `Y_t`,
\[
-\log\mu_t(X_t)
=
h(Y_t)-\log\nu_t(Y_t).
\tag{9.2}
\]
Since the stationary law of the full graph is uniform, Salez's varentropy is exactly the variance of the right side of (9.2).

For `Z=-\log\nu_t(Y_t)`, the elementary counting bound
\[
\Pr(Z\ge s)\le\min(1,re^{-s})
\tag{9.3}
\]
gives
\[
\mathbb E[Z^2]
\le
(\log r)^2+2\log r+2.
\tag{9.4}
\]

From (8.7)--(8.9),
\[
\operatorname{Var}(h(Y_t))
\le
2(\log d)^2t+2\operatorname{Var}(A_t).
\tag{9.5}
\]
Therefore
\[
\boxed{
V_{KL}(t)
\le
4(\log d)^2t
+
4\operatorname{Var}(A_t)
+
2\left[
(\log r)^2+2\log r+2
\right].
}
\tag{9.6}
\]

This gives a concrete sufficient condition toward Salez Problem 2.3.

> **Corollary C — orbit-drift sufficient condition.**  
> Let `(X_n)` be fixed-degree vertex-transitive spectral expanders. If, at one (equivalently every fixed-`epsilon`) mixing-time scale,
> \[
> \log r_n=o(\log n)
> \tag{9.7}
> \]
> and
> \[
> \operatorname{Var}(A_{t_{\rm mix}})=o((\log n)^2),
> \tag{9.8}
> \]
> then `(X_n)` exhibits cutoff.

Indeed bounded-degree expansion gives `t_mix=Theta(log n)` and `gamma>=gamma_0>0`; (9.6) gives `V_KL=o((log n)^2)`, so Salez's criterion
\[
\gamma t_{\rm mix}\gg1+\sqrt{V_{KL}(t_{\rm mix})}
\tag{9.9}
\]
holds.

I do **not** claim (9.7)--(9.8) for every transitive expander. The gain is that the previous vague "quotient may have Theta(n) states" obstruction has been decomposed into two precise obligations: quotient-law surprisal and occupation-time concentration of a finite, degree-dependent drift alphabet. The orbit-size component itself has only `sqrt(t)` martingale noise.

This is complementary to P26's shell/Green transfer: P26 controls collision/entropy after a supplied spherical representation, whereas (8.1)--(9.6) start from arbitrary transitivity and use only stabilizer balance plus the source semigroup.

## 10. What obstruction was actually removed?

Two earlier T08 experiments showed why ambient `L^2` quantities can be misleading:

* the incidence-strong cutoff family had polynomially excessive raw output-NBRW collision trace at its entropic radius;
* finite local/fiber constructions can carry many local modes which are invisible to the macroscopic transport front.

The arc class makes this issue exact. It has a `Theta(n)`-dimensional cycle-flow eigenspace at eigenvalue `1/q`. A naive point-mass `L^2` estimate produces
\[
\sqrt n\,e^{-g_ot},
\]
which for sufficiently large fixed degree can fail to be `o(1)` at the line cutoff front. Equation (5.11) replaces this with
\[
O(\log n)e^{-g_ot},
\]
which is `o(1)` at that front for **every fixed degree**.

Therefore the general conjecture cannot be obstructed merely by high multiplicity of bounded-away-from-one local eigenmodes. What matters is whether the point-source projection onto them has a localized signed/Green representation. This is the precise obstruction removed here.

The remaining source-level obstruction is still substantial: on an arbitrary vertex-transitive spectral expander one has no canonical line-factor/Hodge cover decomposition, and Corollary C still needs occupation-time/surprisal control. No claim of full closure is made.

## 11. Exact sanity checker

The executed exact-arithmetic checker is

`2026-09-20T06-20-00Z__arc_hodge_checker.py`

with archived output

`2026-09-20T06-20-00Z__arc_hodge_checker.out`.

It verifies with exact rational/symbolic arithmetic:

* the strong arc-to-line lumping on `K4` and `K_{3,3}`;
* commutation with reversal and the complete predicted even/odd spectra;
* `D∇ = d(P-I)` and the exact odd formula
  \[
  Q_Af=q^{-1}f+(2q)^{-1}\nabla Df;
  \]
* exact divergence-free Hodge projection and cycle eigenvalue `1/q`;
* the degree-six center coefficient `5/2`, odd rate `4/5`, identity `g_o T=2 log_5 n`, explicit Ramanujan gap lower bound `(3-sqrt(5))/5`, and branching separation `9>5`;
* root-stabilizer orbit-size/neighbor-count balance on the 3-cube.

The output ends

`ALL_EXACT_CHECKS_PASS`.

These finite checks validate algebra only; the asymptotic theorem is proved on the page above.

## 12. Failed route preserved and next attack

The raw output-NBRW trace route remains retired as a necessary condition: the earlier incidence-strong family disproves it.

A first naive version of the present arc argument also failed: `L^2` contraction of the odd sheet gives a `sqrt(n)` prefactor and only proves negligibility at the line front for a restricted degree range. The materially different Hodge-Green calculation (5.4)--(5.11) removes that failure and works for every fixed degree.

The next attack is now precise and does not repeat P26:

1. apply the finite-alphabet orbit-drift representation (8.7)--(8.10) to highly symmetric non-distance-regular expander families and test whether `Var(A_t)=O(t)` follows from a bounded number of stabilizer suborbits or from a quotient conductance decomposition; and
2. abstract the Hodge-Green estimate to transitive finite covers/Schreier quotients where the fiber sector is a bounded-dimensional unitary representation rather than a two-sheet sign representation.

Either route targets a mechanism stable under local spectral multiplicity without demanding output-tree-rate collision decay.

## 13. Ledger delta

```json
{
  "slot": "NM13-01",
  "parent": "T08",
  "source": "Salez arXiv:2508.21055 Problem 2.3",
  "source_status_before": "OPEN",
  "source_status_after": "OPEN",
  "source_level_gain": "cutoff for symmetrized nonbacktracking arc graphs of fixed-degree arc-transitive LRE bases; output is vertex-transitive spectral, non-LRE; center 2(d-1)/(d-2) log_{d-1} n; O(sqrt(log n)) window",
  "mechanism_gain": "exact even/odd Hodge decomposition plus O(log n)e^(-ct) L1 Green cancellation for an extensive cycle-flow sector; finite-alphabet stabilizer-orbit drift martingale and explicit varentropy reduction",
  "obstruction_removed": "high multiplicity of bounded-away-from-one local/fiber modes does not itself delay TV; naive sqrt(n) L2 prefactor replaced by O(log n) for the arc cover",
  "remaining_obstruction": "derive orbit occupation-time/surprisal concentration, or an analogous localized representation, from arbitrary vertex transitivity plus spectral expansion",
  "failed_route_preserved": "raw output-NBRW trace is not necessary; naive odd-sector L2 contraction has a dimension prefactor",
  "checker": "2026-09-20T06-20-00Z__arc_hodge_checker.py",
  "checker_result": "ALL_EXACT_CHECKS_PASS",
  "next_attack": "finite-alphabet orbit-drift concentration and bounded-unitary-fiber Hodge-Green transfer",
  "runtime_model": "GPT-5.6 Sol",
  "runtime_reasoning": "UNVERIFIED"
}
```
