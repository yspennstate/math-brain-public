Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.**

# NM13-01 / LIVE20 T08 — noncommuting switched-fiber cutoff

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run and after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--C and the explicit degree-15 class below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The class and transfer are new relative to the repository state read in this run. The elementary common-gap contraction used in the proof belongs to the broader literature on time-inhomogeneous reversible chains; bounded searches recovered, for example, Gorokhovsky `arXiv:2405.11435` and work on reversible random walks on dynamic graphs. No publication-priority claim is made for that contraction lemma or for the exact class.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Prewrite master observed before this run's persistence work: `c99daf654d55c904e55f8d053fd9571e9f7d31b7`; concurrent LIVE20 commits may advance master independently.

## 0. Short handoff and partner split

The latest complete own report read was

`2026-09-20T11-24-00Z__rotating-lamp-occupation-cutoff.md`.

That report proved cutoff for a genuinely nonnormalizing `C_3` rotating-lamp semidirect product because the three conjugate hidden semigroups act on disjoint direct-product coordinates and hence commute. It explicitly left **noncommuting conjugate hidden dynamics** as the next obstruction: path ordering could no longer be compressed to occupation times.

This run attacks that obstruction directly. The new mechanism is not an occupation-time factorization. Instead, every switched hidden kernel is reversible with respect to the same uniform law and has the same one-sided spectral gap. Differentiating the `L^2` energy along the actual time-ordered inhomogeneous evolution proves pathwise contraction without commuting the kernels. An explicit `S_3` factor makes the two hidden kernels have a commutator of fixed nonzero operator norm, uniformly in the growing graph size.

The newest relevant P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_13-00-56__all-distance-spherical-green-transfer.md`.

P26 is developing the complementary weighted Green/spherical-shell mechanism and now treats all fixed exact distances on the EFMP biregular Cayley bigraphs. The present argument is algebraic/transitivity-specific and uses neither NBRW shell entropy nor weighted Green estimates.

The root `POSTED.md` registry was read. In particular, the already-posted Salez Problem 2.4 Abelian-Cayley product-condition claim is not reopened.

## 1. Source convention and current primary boundary

Salez `arXiv:2508.21055v1`, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, defines continuous time by inserting independent mean-one exponential waiting times between discrete jumps. Thus for a discrete transition kernel `P`,

\[
H_t=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}=e^{t(P-I)}.
\tag{1.1}
\]

Problem 2.3 in those notes asks exactly to prove that all vertex-transitive expanders exhibit cutoff. Here the target is bounded degree, diverging size and a fixed ordinary spectral gap.

Fresh primary-source screening on 20 September 2026 leaves the general problem open. Dylan Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence and proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
\]

with neither converse. His Definition 1.3 requires tree-rate growth

\[
|B(S,r)|\ge \min\{3n/4,c|S|(d-1)^r\}
\tag{1.2}
\]

with one fixed `c>0` over the sequence. Therefore LRE is not equivalent to the arbitrary spectral-expander hypothesis in Salez Problem 2.3. Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, prove a local-product/non-equilibrium-Poincare window theorem, but the checked statement does not derive the needed non-equilibrium constant merely from vertex transitivity plus an ordinary spectral gap.

For explicit inputs below we use Kaufman--Lubotzky `arXiv:1108.2960`, Theorem 3: for every prime power `q` and suitable field extensions they construct `(q+1)`-regular edge-transitive Ramanujan Cayley graphs on `PSL_2/PGL_2` type groups. We take `q=5` and the `PSL_2` branches. Lubetzky--Peres `arXiv:1507.04725` prove simple-walk cutoff on every Ramanujan graph at `d/(d-2) log_{d-1} n` with a square-root logarithmic window; Altschuler's Theorem 1.7 also supplies LRE for the same graphs.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. NM13-01 had several bounded-degree vertex-transitive spectral-but-not-LRE cutoff classes. The immediately preceding `11:24` theorem went beyond normalizing monodromy, but only when the switched hidden semigroups commute. It left persistent noncommutation/path ordering as a concrete structural obstruction.

### After

Salez Problem 2.3 remains `OPEN`; no general transitivity-plus-gap implication is claimed.

The restricted proved scope now contains a **persistently noncommuting switched-fiber semidirect Cayley class**. There is an explicit sequence of 15-regular vertex-transitive spectral expanders `H_j` with

\[
\boxed{\operatorname{gap}(H_j)\ge \frac1{15}},
\tag{2.1}
\]

whose two hidden kernels satisfy the size-independent noncommutation certificate

\[
\boxed{\|[P_0,P_1]\|_{2\to2}=\frac{\sqrt3}{64}>0},
\tag{2.2}
\]

and whose source-convention continuous-time SRW cuts off at

\[
\boxed{T_j=\frac{15}{4}\log_5 n_j
      =\frac{75}{22}\log_5 N_j+O(1)}
\tag{2.3}
\]

with

\[
\boxed{O(\sqrt{\log N_j})}
\tag{2.4}
\]

window. The sequence fails every fixed positive LRE constant.

## 3. The path-ordered common-gap contraction

The key observation is intentionally more general than the Cayley construction.

### Lemma 3.1 — common-gap inhomogeneous `L^2` contraction

Let `K` be a finite set with uniform law `pi`. Let `(P_s)_{s>=0}` be any measurable path of self-adjoint Markov kernels on `K`, each preserving `pi`, and suppose that every `P_s` has one-sided spectral gap at least `eta>0`:

\[
\langle g,(I-P_s)g\rangle_\pi\ge \eta\|g\|_{2,\pi}^2
\quad\text{whenever }\pi(g)=0.
\tag{3.1}
\]

For `b>0`, let `mu_t` solve the time-inhomogeneous forward equation

\[
\partial_t\mu_t=b\mu_t(P_t-I).
\tag{3.2}
\]

Then, writing `f_t=d mu_t/d pi`,

\[
\boxed{
\|f_t-1\|_{2,\pi}\le e^{-b\eta t}\|f_0-1\|_{2,\pi}.
}
\tag{3.3}
\]

In particular, from a point mass,

\[
\boxed{
\|\mu_t-\pi\|_{TV}
\le \frac12\sqrt{|K|-1}\,e^{-b\eta t}.
}
\tag{3.4}
\]

No pair of the kernels is assumed to commute.

### Proof

Put `g_t=f_t-1`. Uniform stationarity gives `pi(g_t)=0`. On every interval on which the kernel path is constant, self-adjointness gives

\[
\frac{d}{dt}\|g_t\|_{2,\pi}^2
=2b\langle g_t,(P_t-I)g_t\rangle_\pi
\le -2b\eta\|g_t\|_{2,\pi}^2.
\]

The same inequality holds almost everywhere for a measurable piecewise path, and Gronwall yields (3.3). For a point mass, `\|f_0-1\|_2^2=|K|-1`; Cauchy--Schwarz gives `TV <= (1/2)||f-1||_2`, proving (3.4). The argument never rearranges the time-ordered product, so commutators are irrelevant to this energy bound. `QED`

This lemma is compatible with the existing literature on time-inhomogeneous reversible chains; the new T08 content below is the semidirect cutoff transfer and explicit non-LRE class.

## 4. A noncommuting switched-fiber transfer theorem

Let

\[
G=\operatorname{Cay}(\Gamma,S),\qquad |S|=d,
\]

be a finite connected undirected Cayley graph. Let `K` be a finite group and `U=U^{-1}\subset K` a generating set of size `r`; write

\[
F=\operatorname{Cay}(K,U),\qquad P_U\text{ its normalized SRW kernel},
\]

and assume `gap(P_U)>=eta`. Let `alpha` be an involutive automorphism of `K`; **do not** assume `alpha(U)=U`. Form `K rtimes_alpha C_2`, with phase generator `tau`.

On

\[
\Omega=\Gamma\times(K\rtimes_\alpha C_2)
\]

take the inverse-closed generating set

\[
\Sigma=
\{(s,e,\tau):s\in S\}
\cup\{(e,u,e):u\in U\}
\cup\{(e,e,\tau)\}.
\tag{4.1}
\]

Let `H=Cay(Omega,Sigma)`. Its degree is

\[
D=d+r+1,
\qquad
 a=\frac dD,\quad b=\frac rD,\quad c=\frac1D.
\tag{4.2}
\]

The graph is connected because multiplying a cross generator by the pure phase generator gives a pure visible generator `(s,e,e)`, while `U` generates `K` and `tau` generates the phase.

At phase `i in {0,1}`, a vertical move acts on `K` using the conjugate set

\[
U_i=\alpha^i(U),
\tag{4.3}
\]

with kernel `P_i`. Since `alpha` is a permutation of `K`, `P_0,P_1` are unitarily conjugate, hence both are self-adjoint with uniform stationary law and gap at least `eta`; they need not commute.

### Theorem A — exact TV sandwich without commutation

For the source rate-one continuous-time SRWs on `G` and `H`, from the identities,

\[
\boxed{
 d_G(at)
 \le d_H(t)
 \le d_G(at)
 +\frac12e^{-2ct}
 +\frac12\sqrt{|K|-1}\,e^{-b\eta t}.
}
\tag{4.4}
\]

### Proof

Poisson thinning separates the three generator types. Cross events have rate `a`, vertical events rate `b`, and pure phase events rate `c`.

The visible coordinate changes only at cross events; its label at each such event is uniform in `S`. Hence its marginal is exactly source rate-one SRW on `G` run for time `at`. Projection therefore gives the lower bound in (4.4).

Now condition on the entire phase path, and also on all visible cross labels if desired. Vertical event times remain a rate-`b` Poisson process independent of that conditioning. At time `s` the hidden coordinate evolves with kernel `P_{I_s}`. Lemma 3.1 therefore applies pathwise and gives

\[
\|\mathcal L(K_t\mid I_{[0,t]},\text{cross labels})-\pi_K\|_{TV}
\le \frac12\sqrt{|K|-1}e^{-b\eta t}.
\tag{4.5}
\]

Replace the conditional hidden law by `pi_K` and average; this costs at most the last term in (4.4).

It remains to compare the joint visible/phase law to `law(X_t) x pi_{C_2}`. Let `N_x` be the cross-event count and `N_p` the pure-phase-event count. The parity

\[
A=N_x\pmod2
\]

may be strongly correlated with the visible endpoint. But

\[
B=N_p\pmod2
\]

is independent of the entire cross process, and the terminal phase is `A+B mod 2`. For a Poisson variable of mean `ct`,

\[
\|\mathcal L(B)-\mathrm{Unif}(C_2)\|_{TV}=\frac12e^{-2ct}.
\tag{4.6}
\]

Conditioning on the visible cross history merely translates `B`, so the same bound holds for the joint visible/phase law relative to `law(X_t) x Unif(C_2)`. Finally the visible marginal has distance exactly `d_G(at)` from its uniform law. Triangle inequality gives the upper bound. `QED`

### Theorem B — spectral-gap transfer

If `gamma_G=gap(G)`, then

\[
\boxed{
\operatorname{gap}(H)
\ge \min\{b\eta,\,a\gamma_G,\,2c\}.
}
\tag{4.7}
\]

### Proof

For a function `f(g,k,i)`, let `bar f(g,i)` be its average over `k`. Variance decomposes as

\[
\operatorname{Var}(f)=\mathbb E_{g,i}\operatorname{Var}_k(f)+\operatorname{Var}(\bar f).
\tag{4.8}
\]

The vertical Dirichlet form is at least

\[
b\eta\,\mathbb E_{g,i}\operatorname{Var}_k(f).
\tag{4.9}
\]

For cross and pure-phase edges, Jensen averaging over `k` can only decrease squared differences, so their Dirichlet form is at least the Dirichlet form of `bar f` for the quotient kernel

\[
Q_{quot}=a(P_G\otimes R)+c(I\otimes R)+(1-a-c)I,
\tag{4.10}
\]

where `R` flips `C_2`. Diagonalize simultaneously in a base eigenfunction with eigenvalue `lambda` and a phase character `sigma in {+1,-1}`. The generator energy is

\[
a(1-\sigma\lambda)+c(1-\sigma).
\tag{4.11}
\]

For `sigma=+1` and a nonconstant base mode this is at least `a gamma_G`. For `sigma=-1` it is at least `2c`, since `lambda>=-1`. Therefore the quotient gap is at least `min{a gamma_G,2c}`. Combine with (4.8)--(4.9). `QED`

### Corollary 4.3 — cutoff transfer

Let `(G_n)` have source-continuous-time cutoff at centers `T_n -> infinity` with windows `w_n=o(T_n)`. Let `(K_n,U_n,alpha_n)` satisfy the hypotheses above with fixed `d,r` and gaps `eta_n`. If

\[
\boxed{
\frac{b\eta_n}{a}T_n-\frac12\log|K_n|\longrightarrow+\infty,
}
\tag{4.12}
\]

then `(H_n)` has cutoff at `T_n/a` with window `O(w_n/a)`. Indeed the two error terms in (4.4) are already `o(1)` at the center; the post-cutoff error only decreases, while the lower side follows from projection.

This is deliberately an `L^2`-budget criterion. It does not claim that (4.12) is necessary; the previous rotating-lamp theorem showed that commuting switched systems can go well beyond such a budget by resolving separate hidden cutoff fronts.

## 5. Explicit degree-15 family with persistent noncommutation

Take the Kaufman--Lubotzky degree-six Ramanujan Cayley families at `q=5`. For large integers `j`, choose

\[
G_j=\operatorname{Cay}(\Gamma_j,S_j),
\qquad
\Gamma_j=PSL_2(5^{10j}),
\qquad |S_j|=6,
\tag{5.1}
\]

and independently

\[
L_j=\operatorname{Cay}(\Lambda_j,V_j),
\qquad
\Lambda_j=PSL_2(5^j),
\qquad |V_j|=6.
\tag{5.2}
\]

Write

\[
n_j=|\Gamma_j|,\qquad m_j=|\Lambda_j|.
\]

Since for odd `q`,

\[
|PSL_2(q)|=\frac12q(q^2-1),
\tag{5.3}
\]

we have

\[
\log m_j=\frac1{10}\log n_j+O(1).
\tag{5.4}
\]

The normalized Ramanujan one-sided gap is at least

\[
\gamma_R=1-\frac{2\sqrt5}{6}=\frac{3-\sqrt5}{3}.
\tag{5.5}
\]

The `PSL_2` groups here have no index-two subgroup, so the connected Cayley bases are nonbipartite.

Now let

\[
S_3=\langle x=(12),y=(23)\rangle,
\qquad z=(13)=xyx,
\]

and set

\[
A=\{x,y\},\qquad B=\{x,z\}.
\tag{5.6}
\]

Both `Cay(S_3,A)` and `Cay(S_3,B)` are 6-cycles, hence have normalized gap `1/2`. Conjugation by `x` is an involutive automorphism and sends `A` to `B`.

Define

\[
K_j=\Lambda_j\times S_3,
\qquad
U_j=(V_j\times\{e\})\cup(\{e\}\times A).
\tag{5.7}
\]

Then `|U_j|=8`. Let `alpha` act trivially on `Lambda_j` and by conjugation by `x` on `S_3`. The two phase-dependent hidden kernels are

\[
P_0=\frac34P_{L_j}\otimes I+\frac14I\otimes P_A,
\qquad
P_1=\frac34P_{L_j}\otimes I+\frac14I\otimes P_B.
\tag{5.8}
\]

Their common gap is at least

\[
\eta
\ge \min\left\{\frac34\gamma_R,\frac14\cdot\frac12\right\}
=\boxed{\frac18}.
\tag{5.9}
\]

The switching is genuinely noncommuting. Exact `S_3` regular-representation algebra gives

\[
\|[P_A,P_B]\|_{2\to2}=\frac{\sqrt3}{4},
\tag{5.10}
\]

so

\[
\boxed{
\|[P_0,P_1]\|_{2\to2}
=\frac1{16}\|[P_A,P_B]\|_{2\to2}
=\frac{\sqrt3}{64}.
}
\tag{5.11}
\]

In particular the commutator does not decay with `j`; this is not an asymptotically commuting perturbation.

Apply Theorems A--B with `d=6`, `r=8`, hence

\[
D=15,\qquad a=\frac25,\quad b=\frac8{15},\quad c=\frac1{15}.
\tag{5.12}
\]

Let `H_j` be the resulting Cayley graph. It is connected, simple, 15-regular and vertex-transitive. Its size is

\[
N_j=|V(H_j)|=2n_j|K_j|=12n_jm_j=n_j^{11/10+o(1)}.
\tag{5.13}
\]

The spectral-gap bound is

\[
\operatorname{gap}(H_j)
\ge
\min\left\{\frac8{15}\frac18,
\frac25\frac{3-\sqrt5}{3},
\frac2{15}\right\}
=\boxed{\frac1{15}}.
\tag{5.14}
\]

The middle term exceeds `1/15` because `2(3-sqrt(5))>1`, equivalently `25>20` after squaring the positive sides.

## 6. Source-continuous-time cutoff and its window

For the visible degree-six Ramanujan graph `G_j`, the simple discrete walk cuts off at

\[
T_j^G=\frac{6}{6-2}\log_5 n_j
=\frac32\log_5 n_j
\tag{6.1}
\]

with `Theta(sqrt(log n_j))` window. The same center and square-root order hold in Salez's source continuous time. For completeness: condition on the rate-one Poisson jump count. The discrete TV upper bound and Markov contraction give the continuous post-cutoff side after only an additional `O(sqrt(T_j^G))` fluctuation. For the lower side, lift to the 6-regular tree. Its continuous radial process has drift `2/3` away from the root, martingale quadratic variation `O(t)`, and only tight root-local-time correction; at time `T_j^G-C sqrt(log n_j)` it lies, with probability tending to one as `C->infinity`, inside a graph ball of radius `log_5 n_j-Theta(C sqrt(log n_j))`, whose stationary mass is `o(1)`. Thus the source-continuous base has the same square-root cutoff window.

Theorem A gives here

\[
\boxed{
 d_{G_j}\!\left(\frac25t\right)
 \le d_{H_j}(t)
 \le d_{G_j}\!\left(\frac25t\right)
 +\frac12e^{-2t/15}
 +\frac12\sqrt{6m_j-1}\,e^{-t/15}.
}
\tag{6.2}
\]

Therefore the candidate output center is

\[
T_j^H=\frac52T_j^G
=\boxed{\frac{15}{4}\log_5 n_j}.
\tag{6.3}
\]

At this time the hidden error satisfies

\[
\frac12\sqrt{6m_j-1}\,e^{-T_j^H/15}
=n_j^{\frac1{20}-\frac1{4\log 5}+o(1)}
=n_j^{-0.1053337336\ldots+o(1)}=o(1),
\tag{6.4}
\]

where `log 5` in the exponent is the natural logarithm. The phase error is

\[
\frac12e^{-2T_j^H/15}
=\frac12 n_j^{-1/(2\log5)}=o(1).
\tag{6.5}
\]

Both remain `o(1)` uniformly throughout every fixed multiple of the base `sqrt(log n_j)` window. The lower bound in (6.2) transfers the pre-cutoff side and the upper bound transfers the post-cutoff side. Hence

\[
\boxed{
H_j\text{ has source-continuous-time cutoff at }
\frac{15}{4}\log_5 n_j
\text{ with }O(\sqrt{\log n_j})\text{ window}.
}
\tag{6.6}
\]

Using (5.13),

\[
\log_5 N_j=\frac{11}{10}\log_5n_j+O(1),
\]

so equivalently

\[
\boxed{
T_j^H=\frac{75}{22}\log_5N_j+O(1),
\qquad
w_j=O(\sqrt{\log N_j}).
}
\tag{6.7}
\]

No finite computation is used to infer this asymptotic statement.

## 7. The degree-15 family is not long-range expanding

The output degree is 15, so the LRE branching benchmark is `14^r`. In any output path of length `r`, only cross moves change the visible `Gamma_j` coordinate. Therefore the visible coordinate of a radius-`r` output ball lies in a radius-`r` ball of a degree-six graph, which has at most `C 5^r` vertices. Forgetting all restrictions on the hidden/phase coordinates gives the deterministic upper bound

\[
|B_{H_j}(x,r)|\le C\,(2|K_j|)5^r
\le C' m_j5^r.
\tag{7.1}
\]

Take

\[
r_j=\left\lfloor\frac12\log_{14}N_j\right\rfloor.
\tag{7.2}
\]

Since `m_j=N_j^{1/11+o(1)}`,

\[
\frac{|B_{H_j}(x,r_j)|}{14^{r_j}}
\le N_j^{-\beta+o(1)},
\qquad
\beta=\frac12\left(1-\frac{\log5}{\log14}\right)-\frac1{11}
=0.1041642418\ldots>0.
\tag{7.3}
\]

An exact sign certificate is

\[
5^{11}=48,828,125<20,661,046,784=14^9.
\tag{7.4}
\]

At radius `r_j`, the LRE lower branch `c14^{r_j}` is still `o(N_j)` for every fixed `c`, while (7.3) makes the actual ball smaller than `c14^{r_j}` for all large `j`. Thus no fixed positive LRE constant exists. This separates the class quantitatively from Altschuler's hypothesis.

## 8. Mechanism-level obstruction removed

The `11:24` report isolated **noncommuting monodromy/path ordering** as the next obstruction after commuting rotating lamps. The new result removes that obstruction in a precise regime:

> If every time-ordered hidden kernel is reversible for one common stationary law and has a common positive one-sided spectral gap, then arbitrary switching and arbitrary pairwise commutators do not reduce `L^2` dissipation. The hidden point-mass information decays at the same exponential rate pathwise.

The explicit degree-15 family is not merely formally noncommuting: its switched hidden kernels have fixed commutator norm `sqrt(3)/64`, yet cutoff survives with a square-root window and the output remains a uniform spectral expander outside LRE.

This narrows the unresolved T08 obstruction again. Two genuinely harder regimes remain:

1. **Supercritical noncommuting hidden information.** The common-gap estimate still carries the `sqrt(|K|)` point-mass `L^2` cost. In the commuting rotating-lamp case exact factor fronts removed that cost; for genuinely noncommuting switching there is not yet an exact conditional TV decomposition that survives when `0.5 log|K|` is comparable to or exceeds the available dissipation before the visible front.
2. **No finite switching/factor representation.** An arbitrary bounded-degree vertex-transitive spectral expander need not expose a visible cutoff quotient plus a common-gap hidden fiber. A general proof still needs a transitivity mechanism that manufactures a sharp information frontier internally, plausibly through stabilizer representations or another canonical quotient, without assuming product geometry.

This is complementary to P26: P26 attacks the distribution of long nonbacktracking/spherical paths through Green estimates; the present route shows that substantial nonabelian, path-ordered local memory can be harmless before one ever invokes those shell estimates.

## 9. Sanity checker and exact certificates

Executed code is archived as

`2026-09-20T12-50-00Z__noncommuting_switch_cutoff_check.py`

with executed output

`2026-09-20T12-50-00Z__noncommuting_switch_cutoff_check.out`.

The checker does four things.

* It computes the `S_3` regular-representation matrices exactly with SymPy and verifies that `[P_A,P_B]^*[P_A,P_B]` has eigenvalues `3/16` with multiplicity four and `0` with multiplicity two, hence `||[P_A,P_B]||=sqrt(3)/4` and the hidden switched commutator norm is exactly `sqrt(3)/64`.
* It verifies the exact center coefficient `75/22`, the gap lower bound `1/15`, the negative hidden/phase error exponents, and the positive non-LRE exponent, together with the integer certificate `5^11<14^9`.
* It builds a 588-state finite semidirect toy with visible `K_7`, hidden `Z_7 x S_3`, and the same `C_2` switching. The transition matrix is symmetric/stochastic, visible lumping is exact, and its numerical output gap `0.096677704315` exceeds the theorem lower bound `1/15`.
* It checks the TV sandwich numerically at five times. These finite checks are sanity checks only, not substitutes for the asymptotic proofs above.

The archived output ends `ALL_CHECKS_PASS`.

## 10. Compact ledger delta / next attack

* **Parent before/after:** Salez Problem 2.3 `OPEN -> OPEN`.
* **Restricted theorem gain:** new degree-15 vertex-transitive spectral-expander class outside LRE; source-CT cutoff center `(75/22) log_5 N+O(1)`, window `O(sqrt(log N))`, output gap at least `1/15`.
* **Mechanism gain:** pathwise common-gap `L^2` dissipation removes noncommuting path ordering as an obstruction; explicit switched kernels have persistent commutator norm `sqrt(3)/64`.
* **Not claimed:** no general transitivity-plus-gap theorem; no publication novelty certificate; no inference of an asymptotic theorem from the finite checker.
* **Residual obstruction:** supercritical genuinely noncommuting hidden information, and arbitrary transitive expanders with no exposed finite switching/factor decomposition.
* **Next materially distinct attack:** use the root stabilizer representation decomposition to ask whether bounded-degree transitivity itself supplies a finite-or-low-complexity family of conditional kernels with a common stationary law. The target is a dimension-free contraction for the likelihood-ratio component orthogonal to the orbit quotient, strong enough to avoid the `sqrt(|K|)` initialization cost. If that fails, construct a transitive spectral-expander stress family in which stabilizer isotypic multiplicity is large and show exactly where the common-gap fiber picture breaks.
