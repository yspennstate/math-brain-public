Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — cutoff for non-LRE truncations of arc-transitive expanders

**Status:** `CANDIDATE_FULL` for the restricted theorem proved here, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.
Frozen pre-write master observed during the run: `a723982ca9debab68095e3f5e059be2a5654abd3` (the fleet was committing concurrently).

## 0. Continuity, coordination, and the deliberate route change

The pre-LIVE20 NM13-01 admission history and its terminal P0292 handoff are preserved and not rewritten. LIVE20 assigns this slot to T08.

The first T08 NM13-01 run proved a complete restricted theorem for line graphs of fixed-degree edge-transitive long-range expanders: the outputs are vertex-transitive spectral expanders, are not uniform long-range expanders, and have Salez-convention continuous-time cutoff with an `O(sqrt(log n))` window. Its mechanism was an incidence intertwining plus constant-rate decay of endpoint-invisible modes.

A subsequent NM13-01 ledger recorded a lexicographic finite-fiber transfer. However, the current P26 partner report independently developed essentially the same finite-fiber/lexicographic mechanism, including an exact semigroup decomposition and entropy/TV transfer. Continuing that route here would duplicate P26 rather than complement it.

Therefore this run executes a materially different attack:

> replace exact lumping / rapidly killed fibers by a **non-lumpable finite port memory**.  The local state persists and is essential for moving between macroscopic vertices.  Arc transitivity makes this memory analyzable as a two-state Markov-additive radial process on the universal cover.

This is the transitivity-specific complement requested by LIVE20.

## 1. Source target and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), uses the rate-one continuous-time convention

\[
H_t=\exp\{t(P-I)\}
=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\]

Problem 2.3 asks:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and spectral gap bounded away from zero.

The most relevant newer primary result is Dylan Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026.  It proves cutoff with an explicit Gaussian profile for every fixed-degree long-range-expander sequence and proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{long-range expansion}
\Longrightarrow\text{spectral expansion},
\]

with neither converse.  Thus arbitrary spectral expansion in Salez Problem 2.3 is strictly broader than long-range expansion.

The other relevant current input is Pedrotti--Salez, `arXiv:2607.05345` (6 July 2026), which proves cutoff from the local-product condition / its non-equilibrium spectral quantity.  That criterion does not currently derive the needed bound from vertex transitivity plus spectral expansion alone.

For the theorem below I use one quantitative input from Altschuler's proof: for a fixed-degree fixed-`c` long-range expander `G` on `n` vertices, the endpoint law `K_j^G(x,.)` of nonbacktracking random walk satisfies, uniformly in the start,

\[
H(K_j^G(x,\cdot))\ge \log n-C_{d,c}\log\log n
\tag{1.1}
\]

for all `j` at least the entropic radius

\[
j_n:=\min\{j\ge1:d(d-1)^{j-1}\ge n\}
=\log_{d-1}n+O_d(1).
\tag{1.2}
\]

No claim is made that (1.1) holds for arbitrary spectral expanders.

### Bounded prior-art check, 20 September 2026

I searched combinations of `truncation graph random walk cutoff`, `truncation of a graph mixing time`, `replacement product random walk cutoff`, `replacement product mixing time expander`, and `arc-transitive Ramanujan graph family`.  I found the classical replacement-product literature and general mixing applications, but did not locate this exact cutoff theorem or radial-speed computation.  Negative search evidence is not a priority certificate, so the novelty label remains **NEW REPOSITORY THEOREM / PUBLICATION NOVELTY UNVERIFIED**.

Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, gives explicit fixed-degree Ramanujan Cayley graphs `Cay(G,S)` where `S` is one orbit of a fixed torus action.  Their semidirect-product action is vertex-transitive and the stabilizer is transitive on `S`, hence these graphs are arc-transitive.  Combined with Altschuler's Ramanujan => LRE theorem, they show that the base class used below is nonempty in explicit infinite families.

## 2. Source-level before / after

### Before this run

Salez Problem 2.3 was OPEN.  NM13-01 had a line-graph special-class theorem and a lexicographic finite-fiber transfer recorded; P26 had independently reached the overlapping lexicographic/fiber mechanism.  The repository also had an LRE-quotient theorem and a vanishing-LRE extension.  None settled arbitrary vertex-transitive spectral expanders.

### After this run

Salez Problem 2.3 remains OPEN, but the proved scope is enlarged by a structurally different class.

### Theorem T08-NM01-TRUNC — truncation/replacement-product cutoff

Fix `d>=3` and `c>0`.  Let `(G_n)` be connected simple `d`-regular **arc-transitive `c`-long-range expanders**, with

\[
n=|V(G_n)|\to\infty.
\]

Define the **graph truncation** `H_n=Tr(G_n)` as follows.  Its vertices are directed edges (arcs)

\[
A(G_n)=\{(x,y):x\sim y\}.
\]

For every arc `(x,y)`, join it to

1. the reversed arc `(y,x)`, and
2. every `(x,z)` with `z\sim x`, `z\ne y`.

Equivalently, each base vertex is replaced by a clique `K_d`, while each base edge becomes a matching edge between the corresponding ports.  This is the classical `K_d` replacement product / truncation.

Then:

1. `H_n` is connected, simple, `d`-regular and vertex-transitive, with `|V(H_n)|=dn`.
2. `H_n` is a spectral-expander sequence.  If the base normalized one-sided spectral gap is at least `gamma`, then
   \[
   \operatorname{gap}(H_n)\ge \frac{\gamma}{\gamma+2d}.
   \tag{2.1}
   \]
3. `H_n` is **not** a uniform long-range-expander sequence.  In fact a singleton-ball test forces any admissible LRE constant `c_n'` to obey
   \[
   c_n'=O_d(|V(H_n)|^{-1/4}).
   \tag{2.2}
   \]
4. For rate-one continuous-time simple random walk on `H_n`, in Salez's convention,
   \[
   T_n=\frac{d(d+2)}{d-2}\log_{d-1}n
   \tag{2.3}
   \]
   is a cutoff location with window `O(sqrt(log n))`.  More precisely, for every fixed `epsilon in (0,1)`,
   \[
   t_{\rm mix}^{H_n}(\epsilon)
   =T_n+O_{d,c,\epsilon}(\sqrt{\log n}).
   \tag{2.4}
   \]
   Since `|V(H_n)|=dn`, this is equivalently
   \[
   T_n=\frac{d(d+2)}{d-2}\log_{d-1}|V(H_n)|+O_d(1),
   \]
   with window `O(sqrt(log |V(H_n)|))`.

The proof occupies Sections 3--9.

The source-level gain is therefore a new bounded-degree vertex-transitive **spectral-expander** class outside fixed-constant LRE, with a quantitative cutoff window.  It does not close the parent conjecture.

## 3. Why this is not the P26 finite-fiber transfer

There is an obvious projection

\[
\rho:A(G)\to V(G),\qquad \rho(x,y)=x.
\]

But it is **not a Markov lumping** for SRW on `Tr(G)`.  From `(x,y)`, the unique transition leaving the fiber over `x` goes specifically to `(y,x)`.  Which neighboring base vertex is chosen therefore remembers the current port `y`; it is not a function only of the tail `x`.

Likewise `rho` is not a graph covering: the `d-1` clique edges at `(x,y)` collapse under `rho`, while the single flip edge projects to a base edge.  Thus neither the exact lexicographic semigroup decomposition in P26 nor the current ordinary-cover/LRE-quotient theorem applies.

The local `d`-state port memory is not rapidly erased: it is exactly what determines the next macroscopic move.  The new point is that **arc transitivity synchronizes the entropy of all directional sectors**, while the universal-cover dynamics of that port memory collapses to a two-state orientation chain.

## 4. Vertex transitivity and spectral expansion

### 4.1 Transitivity

An automorphism `sigma` of `G` acts on arcs by

\[
(x,y)\mapsto(\sigma x,\sigma y).
\]

It preserves both clique edges and flip edges of `Tr(G)`.  If `G` is arc-transitive, this action is transitive on `A(G)`, hence `Tr(G)` is vertex-transitive.

Each arc has `d-1` clique neighbors and one flip neighbor, so `Tr(G)` is `d`-regular.

### 4.2 A direct Poincare transfer

Let `Q` be SRW on `H=Tr(G)`, and write `pi_A` for the uniform law on arcs.  For `f:A(G)->R`, define the tail average

\[
g(x)=\frac1d\sum_{y\sim x}f(x,y),
\qquad
h(x,y)=f(x,y)-g(x).
\tag{4.1}
\]

Then

\[
\operatorname{Var}_{\pi_A}(f)
=\operatorname{Var}_{\pi_V}(g)
+V_{\rm fib},
\qquad
V_{\rm fib}:=\frac1{nd}\sum_{x\sim y}h(x,y)^2.
\tag{4.2}
\]

Split the Dirichlet form of `Q` into clique and flip parts:

\[
\mathcal E_Q(f,f)=E_{\rm int}+E_{\rm flip}.
\]

Inside each tail clique, the complete-graph identity gives exactly

\[
E_{\rm int}=V_{\rm fib}.
\tag{4.3}
\]

For a base edge `{x,y}`,

\[
g(x)-g(y)
=[f(x,y)-f(y,x)]-[h(x,y)-h(y,x)].
\]

Using `(a-b)^2<=2a^2+2b^2`, summing over base edges, and keeping the normalizations explicit gives

\[
\mathcal E_P(g,g)
\le 2d E_{\rm flip}+4V_{\rm fib}
\le 2d\mathcal E_Q(f,f),
\tag{4.4}
\]

where the last inequality uses `d>=2`.

If the base gap is at least `gamma`, Poincare on `G` and (4.2)--(4.4) yield

\[
\begin{aligned}
\operatorname{Var}_{\pi_A}(f)
&\le \gamma^{-1}\mathcal E_P(g,g)+V_{\rm fib}\\
&\le \left(\frac{2d}{\gamma}+1\right)\mathcal E_Q(f,f).
\end{aligned}
\]

Therefore

\[
\boxed{\operatorname{gap}(Tr(G))\ge \frac{\gamma}{\gamma+2d}.}
\tag{4.5}
\]

This proves the spectral-expander assertion.

## 5. Severe failure of long-range expansion

A path in `Tr(G)` alternates between two kinds of moves:

- a clique move changes the head/port but leaves the tail fixed;
- a flip move moves the tail across the currently selected base edge and reverses the port.

Two consecutive flip moves simply undo each other.  Hence, along any truncation path of length `r`, the base-tail distance from its initial tail is at most

\[
\left\lceil\frac r2\right\rceil.
\tag{5.1}
\]

Consequently, for every arc `a=(x,y)`,

\[
|B_{Tr(G)}(a,r)|
\le d\,|B_G(x,\lceil r/2\rceil)|
\le C_d(d-1)^{r/2+1}.
\tag{5.2}
\]

The truncation itself is `d`-regular, so an LRE lower bound with constant `c'` would demand, for a singleton and before saturation,

\[
|B_{Tr(G)}(a,r)|\ge c'(d-1)^r.
\tag{5.3}
\]

Take

\[
r_n=\left\lfloor\frac12\log_{d-1}|V(Tr(G_n))|\right\rfloor.
\]

Then the right side of (5.3) is of order `c'|V(H_n)|^{1/2}`, while (5.2) is only `O_d(|V(H_n)|^{1/4})`.  Therefore no fixed `c'>0` is possible, and any sequence of admissible constants must satisfy (2.2).

This is much more severe than the current repository's vanishing-LRE regime: the available quantitative LRE extension requires a decay slow enough that a negative power of the LRE constant is still sublogarithmic, whereas here the singleton test permits at best a polynomially small constant.

## 6. Universal truncation and the two-state radial chain

Fix a start arc `a_0=(o,o_1)` in the universal truncation `Tr(T_d)` of the `d`-regular tree.  Let `(V_m,W_m)` denote the discrete truncation walk after `m` jumps and

\[
R_m=d_{T_d}(o,V_m).
\]

Away from the root there are two orientation types:

- `+`: the head `W_m` is a child of the tail `V_m`;
- `-`: the head is the parent of the tail.

For `R_m>0`, the transition table is exact:

\[
\begin{array}{c|c|c}
\text{current type}&\text{next type}&\Delta R\\ \hline
+&-&+1\ \text{with probability }1/d\\
+&-&0\ \text{with probability }1/d\\
+&+&0\ \text{with probability }(d-2)/d\\
-&+&-1\ \text{with probability }1/d\\
-&+&0\ \text{with probability }(d-1)/d.
\end{array}
\tag{6.1}
\]

Thus the type transition matrix, in order `(+,-)`, is

\[
M=\begin{pmatrix}
(d-2)/d&2/d\\
1&0
\end{pmatrix}.
\tag{6.2}
\]

Its stationary law is

\[
\pi_+=\frac d{d+2},\qquad
\pi_-=\frac2{d+2}.
\tag{6.3}
\]

The conditional radial drifts are `m(+)=1/d` and `m(-)=-1/d`, so the stationary radial speed per jump is

\[
\boxed{
v_*:=\pi_+m(+)+\pi_-m(-)
=\frac{d-2}{d(d+2)}.
}
\tag{6.4}
\]

Since Salez's continuous-time walk makes a rate-one Poisson number of discrete jumps, `v_*` is also the macroscopic radial speed per unit continuous time.

### 6.1 Exact Poisson corrector

Set

\[
g(+)=\frac2{d+2},\qquad g(-)=0.
\tag{6.5}
\]

A direct calculation gives

\[
(I-M)g=m-v_*.
\tag{6.6}
\]

At the tree root the same expression has a fixed defect

\[
b_0=\frac2{d(d+2)}.
\tag{6.7}
\]

Let `L_m` count discrete times before step `m` at which the tail is at the root.  Then

\[
M_m:=R_m-v_*m+g(S_m)-g(S_0)-b_0L_m
\tag{6.8}
\]

is a martingale with increments bounded by a constant depending only on `d` (in fact an absolute constant suffices).

### 6.2 Root local time has an exponential tail

Starting from radius `1` in the inward type, let `h_-(1)` be the probability ever to hit the root.  The harmonic equations away from zero have a decaying solution

\[
h_+(r)=Az^r,\qquad h_-(r)=Bz^r,
\]

where

\[
(d-1)z^2-dz+1=0.
\]

The decaying root is `z=1/(d-1)`, and the equations give

\[
\frac BA=\frac{2(d-1)}d.
\]

With `h_+(0)=1`,

\[
\boxed{h_-(1)=\frac2d<1.}
\tag{6.9}
\]

Each visit to the root has a geometric number of holding-in-the-root clique moves before the next flip departure, and after departure the return probability is `2/d`.  Therefore the total root occupation `L_\infty` has an exponential tail:

\[
\Pr(L_\infty\ge u)\le C_de^{-c_du}.
\tag{6.10}
\]

### 6.3 Quantitative radial hitting concentration

Let `N_t~Pois(t)` be independent and define the continuous-time radial process `R(t)=R_{N_t}`.  For

\[
\tau_r=\inf\{t:R(t)=r\},
\]

Azuma's maximal inequality applied to (6.8), the exponential tail (6.10), and Poisson Chernoff bounds imply constants `C_d,c_d>0` such that for all large `r` and all `A>=1`,

\[
\Pr\!\left(\tau_r\le \frac r{v_*}-A\sqrt r\right)
\le C_de^{-c_dA^2}+C_de^{-c_dA\sqrt r},
\tag{6.11}
\]

and

\[
\Pr\!\left(\tau_r> \frac r{v_*}+A\sqrt r\right)
\le C_de^{-c_dA^2}+C_de^{-c_dA\sqrt r}.
\tag{6.12}
\]

For completeness, the deduction is as follows.  On the event that the Poisson clock differs from its mean by at most a fixed small multiple of `A sqrt(r)`, an early hit forces either the running maximum of the martingale in (6.8) or `L_\infty` to be of order `A sqrt(r)`; maximal Azuma and (6.10) give (6.11).  For the late tail, `tau_r>t` implies `R(t)<r`; on the typical Poisson-clock event, (6.8) then forces a negative martingale deviation of order `A sqrt(r)`, yielding (6.12).  The complement of the typical clock event has `exp(-c_dA^2)` probability by Poisson Chernoff.

Thus the entropic radius is reached in a `Theta(sqrt(log n))` time window around `j_n/v_*`.

## 7. Arc transitivity converts base NBRW entropy into truncation hitting entropy

This is the central transitivity-specific step.

For a directed base edge `e=(x,y)`, let

\[
K_j^{e}
\]

be the endpoint law of length-`j` nonbacktracking walk conditioned to take `e` as its first directed edge.  Because `G` is arc-transitive, the entropy

\[
h_j:=H(K_j^e)
\tag{7.1}
\]

is independent of `e`.

Ordinary NBRW from `x` is the equal mixture over its `d` first-edge sectors:

\[
K_j^G(x,\cdot)=\frac1d\sum_{y\sim x}K_j^{(x,y)}.
\]

The entropy of a mixture is at most the entropy of the component label plus the average component entropy, hence

\[
H(K_j^G(x,\cdot))\le \log d+h_j.
\]

Combining with (1.1) yields, for `j>=j_n`,

\[
\boxed{
h_j\ge \log n-C_{d,c}\log\log n-\log d.
}
\tag{7.2}
\]

Now lift the truncation walk from `H=Tr(G)` to `Tr(T_d)`.  At the **first** hitting of radius `j`, the lifted state necessarily has inward orientation `(v_j,v_{j-1})`.  Conditional on

- the first tree-edge sector out of the root, and
- the discrete hitting jump number (and hence also after conditioning on the continuous hitting time),

tree automorphisms fixing that sector act transitively on the depth-`j` vertices in the sector.  Therefore the tail is uniform on the nonbacktracking tree paths of length `j` with that first edge.  Projecting to `G` gives exactly the fixed-first-edge NBRW endpoint law `K_j^e`.

The full truncation state contains at least as much information as its tail.  Concavity of entropy over the sector mixture therefore gives, for every regular conditional hitting-state law `nu_s` at `tau_j=s`,

\[
H(\nu_s)\ge h_j.
\tag{7.3}
\]

Since the stationary law of `Tr(G)` is uniform on `nd` arcs, (7.2)--(7.3) imply the uniform KL-deficit bound

\[
\boxed{
D(\nu_s\|\pi_H)
\le C_{d,c}\log\log n+2\log d.
}
\tag{7.4}
\]

This is exactly where arc transitivity is used.  Without it, different first-edge sectors can have different endpoint entropies, and the ordinary NBRW entropy lower bound does not force each sector to be good.

## 8. Entropy deficit dissipates on the spectral-expander truncation

We need only a short standard lemma, included to keep the argument self-contained.

### Lemma 8.1

Let a finite regular reversible chain with kernel `Q` have one-sided gap at least `eta>0`, and let `H_s=e^{s(Q-I)}`.  For any initial law `mu`,

\[
\boxed{
\|\mu H_s-\pi\|_{TV}
\le \sqrt{\frac{D(\mu\|\pi)}{4\eta s}}.
}
\tag{8.1}
\]

#### Proof

Write `f_s=(\mu H_s)/\pi`.  Entropy dissipation gives

\[
-\frac d{ds}D(\mu H_s\|\pi)
=\mathcal E_Q(f_s,\log f_s).
\]

The pointwise inequality

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2
\]

and Poincare imply

\[
\mathcal E_Q(f_s,\log f_s)
\ge4\eta\operatorname{Var}_\pi(\sqrt{f_s}).
\]

Cauchy--Schwarz gives

\[
\|\mu H_s-\pi\|_{TV}^2
\le \operatorname{Var}_\pi(\sqrt{f_s}).
\]

Total variation is nonincreasing under the semigroup, so integrating from `0` to `s` yields

\[
D(\mu\|\pi)
\ge4\eta s\,\|\mu H_s-\pi\|_{TV}^2.
\]

This is (8.1). `QED`

By (4.5), the truncation gap has a uniform positive lower bound `eta=eta(d,c)`.  Combining (7.4) and (8.1), any truncation hitting law at radius `j_n` becomes `o(1)`-mixed after the deterministic buffer

\[
b_n=(\log\log n)^2,
\tag{8.2}
\]

because

\[
\sqrt{\frac{O(\log\log n)}{b_n}}=o(1).
\tag{8.3}
\]

Crucially, `b_n=o(\sqrt{\log n})`, so this cleanup does not enlarge the claimed window.

## 9. Upper and lower cutoff bounds

Put

\[
L_n=\log_{d-1}n,
\qquad
T_n=\frac{L_n}{v_*}
=\frac{d(d+2)}{d-2}L_n.
\tag{9.1}
\]

Since `j_n=L_n+O_d(1)`, the typical hitting time `j_n/v_*` differs from `T_n` by only `O_d(1)`.

### 9.1 Upper bound

Fix `A>0` and set

\[
t=T_n+A\sqrt{L_n}.
\]

Let `tau=\tau_{j_n}` for the lifted walk.  From (6.12), because `b_n=o(\sqrt{L_n})`,

\[
\limsup_{n\to\infty}
\Pr(\tau>t-b_n)
\le C_de^{-c_dA^2}.
\tag{9.2}
\]

On `{tau=s<=t-b_n}`, the strong Markov property says that the remaining law at time `t` is `nu_s H_{t-s}`.  Equations (7.4), (8.1), and `t-s>=b_n` make its TV distance `o(1)`, uniformly in `s`.  Hence

\[
\limsup_{n\to\infty}d_{H_n}(T_n+A\sqrt{L_n})
\le C_de^{-c_dA^2}.
\tag{9.3}
\]

Letting `A->infinity` proves the post-cutoff side.

### 9.2 Lower bound

Set

\[
r_n=\left\lfloor
j_n-\frac{v_*A}{2}\sqrt{L_n}
\right\rfloor
\]

and

\[
t=T_n-A\sqrt{L_n}.
\]

Then

\[
\frac{r_n}{v_*}-t
=\frac A2\sqrt{L_n}+O_d(1).
\tag{9.4}
\]

The early-hitting estimate (6.11) therefore gives

\[
\limsup_{n\to\infty}\Pr(\tau_{r_n}\le t)
\le C_de^{-c_d'A^2}.
\tag{9.5}
\]

On the complementary event, the lifted tail has not reached tree radius `r_n`, so the projected truncation state lies in

\[
S_n=\{(u,w):u\in B_{G_n}(x,r_n)\}.
\]

Using only the degree bound,

\[
\pi_{H_n}(S_n)
=\frac{|B_{G_n}(x,r_n)|}{n}
\le C_d\frac{(d-1)^{r_n}}n
\le C_d(d-1)^{-(v_*A/2)\sqrt{L_n}+O_d(1)}
\longrightarrow0.
\tag{9.6}
\]

Therefore

\[
\liminf_{n\to\infty}d_{H_n}(T_n-A\sqrt{L_n})
\ge1-C_de^{-c_d'A^2}.
\tag{9.7}
\]

Letting `A->infinity` proves the pre-cutoff side.

Equations (9.3) and (9.7) establish cutoff at `T_n` with an `O(sqrt(log n))` window, and immediately give (2.4) for every fixed `epsilon`.

## 10. What obstruction was actually removed?

The previous NM13/P26 line-graph and lexicographic mechanisms could be summarized as:

> the logarithmic-time transport lives in a quotient/base component, while the local fiber discrepancy dies on `O(1)` time.

The truncation class violates the cleanest version of that picture.  The port variable does **not** die independently and the tail projection is not Markov.  A port must be retained to know the next base direction.

The theorem shows a larger harmless-local-complexity mechanism:

> a persistent finite local memory can coexist with cutoff if transitivity makes the tree-lift dynamics a finite-state Markov-additive process with positive radial speed, a bounded Poisson corrector, and uniformly synchronized directional endpoint entropy.

This removes a concrete obstruction to pushing T08 beyond exact finite-fiber decompositions.  Local cliques, polynomial failure of the LRE constant, and a non-lumpable matching between clouds do not prevent a square-root cutoff window.

The remaining obstruction to Salez Problem 2.3 is genuine: an arbitrary vertex-transitive spectral expander need not possess an arc-transitive LRE ancestor, a fixed replacement-product representation, or any obvious finite-state radial quotient.

## 11. Sanity check and exact arithmetic

Before the theorem was saved, the exact checker

`2026-09-20T01-22-00Z__truncation_radial_checker.py`

was executed.  Its archived output is

`2026-09-20T01-22-00Z__truncation_radial_checker.out`.

It verifies with rational arithmetic on `Tr(K4)` and `Tr(K3,3)`:

- the truncation transition matrix and degree;
- the exact variance decomposition (4.2);
- `E_int=V_fib`;
- the inequality `E_base(g)<=2d E_flip+4V_fib<=2d E_H`;
- the two-state stationary law and radial speed `v_*`;
- the Poisson corrector (6.5)--(6.6);
- the decaying harmonic root and return probability `2/d`;
- the root martingale defect `b_0`.

The output terminates `ALL_EXACT_CHECKS_PASS`.

This checker is a sanity check for the finite algebra.  It is not being misrepresented as a proof of the asymptotic cutoff theorem; Sections 4--9 are the proof.

## 12. Ledger delta and next attack

The compact structured delta is saved as

`2026-09-20T01-22-00Z__ledger_delta.json`.

### Parent source

- before: OPEN;
- after: OPEN / PARTIAL, with the new truncation class proved;
- no invented numerical baseline or closure claim.

### New restricted theorem

- class: `Tr(G_n)` for fixed-degree arc-transitive fixed-`c` LRE bases;
- output degree: `d`;
- output size: `dn`;
- gap lower bound: `gamma/(gamma+2d)`;
- cutoff center: `d(d+2)/(d-2) log_{d-1} n`;
- window: `O(sqrt(log n))`;
- output LRE constant: at best `O(N^{-1/4})` by the singleton test.

### Next attack

Full arc transitivity was used only to equalize the entropy of fixed-first-edge NBRW sectors.  The next distinct route is therefore to weaken it to **finitely many directed-edge orbit types**.  The universal-cover port process then becomes matrix-valued rather than two-state.  A useful next theorem would identify an irreducibility/drift condition on that finite orbital chain which, together with a quantitative lower bound on every sector entropy, still gives cutoff.  If that condition can be forced directly by vertex transitivity plus spectral expansion, it would attack the general conjecture without any LRE ancestry.
