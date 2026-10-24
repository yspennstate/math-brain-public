Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated runtime metadata establishes a maximum-effort setting.**

# NM13-01 / LIVE20 T08 — rotating-lamp cutoff beyond normalizing monodromy

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run and after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorem A and the explicit degree-eight class below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The result is new relative to the repository state read in this run. Bounded external searches found standard wreath-product/lamplighter and semidirect-product random-walk literature, but did not establish either priority or non-priority for the exact fixed-switching expander theorem below.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Prewrite master observed before this run's writes: `8456dd3899cb5cc4e456da541916e801027a21e3`.

## 0. Short handoff and partner split

The latest complete NM13-01 report read was

`2026-09-20T10-30-00Z__normalizing-voltage-two-front-cutoff.md`.

It proved an exact TV transfer for voltage lifts when every voltage **normalizes** the hidden generating set. That removed the preceding hidden-cardinality budget and left the following structural obstruction explicitly unresolved: a nonnormalizing monodromy can rotate the hidden geometry so that its true TV profile can no longer be pulled unchanged through the path.

This run attacks exactly that obstruction, rather than taking another normalizing/fiber product. The new construction deliberately violates the normalizer condition. Its phase rotates one active generating set through three distinct coordinate copies. The reason cutoff survives is different: the three conjugate hidden semigroups commute because they act on different direct-product coordinates, and the only remaining randomness is the occupation time of a fixed three-state switch chain. Those occupation times fluctuate on the same square-root scale as the hidden cutoff window.

The newest relevant P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_13-00-56__all-distance-spherical-green-transfer.md`.

P26 has extended its weighted Green/spherical-shell argument to all fixed exact distances on the EFMP biregular Cayley bigraphs. The argument below is complementary: it is a semidirect-product/transitivity/occupation-time argument and does not use NBRW entropy, Green functions or shell estimates.

The root `POSTED.md` registry was read. In particular, the posted Salez Problem 2.4 Abelian-Cayley product-condition claim is not reopened.

## 1. Source convention and current primary boundary

Justin Salez, `arXiv:2508.21055v1`, defines the continuous-time process by inserting independent mean-one exponential waiting times between discrete transitions. Thus for a discrete kernel `T`,

\[
P_t=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!}=e^{t(T-I)}.
\tag{1.1}
\]

Problem 2.3 in those notes asks exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and spectral gaps bounded away from zero.

The current checked primary boundary on 20 September 2026 is still narrower:

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus LRE is not equivalent to the hypothesis in Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a general local-product/non-equilibrium-Poincare window theorem. The checked theorem does not derive its non-equilibrium constant from vertex transitivity plus an ordinary fixed spectral gap alone.
* Tali Kaufman and Alexander Lubotzky, `arXiv:1108.2960`, Theorem 3, give for every prime power `q` edge-transitive `(q+1)`-regular Ramanujan Cayley graphs on `PSL_2/PGL_2` type groups. We use `q=5`, hence degree six. Their `PGL` branch may be bipartite; this causes no problem in Salez continuous time.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. NM13-01 had already proved several spectral-but-not-LRE cutoff classes. The immediately preceding theorem handled growing two-front voltage lifts under an exact normalizer relation. It did **not** cover a generator which conjugates the vertical generating set to a genuinely different set.

### After

Salez Problem 2.3 remains `OPEN`.

The restricted proved scope now contains a nonnormalizing semidirect Cayley class. From any degree-six Ramanujan Cayley family `L_n=Cay(K_n,U_n)`, construct a degree-eight Cayley graph on

\[
K_n^3\rtimes C_3.
\]

The source continuous-time walk has cutoff at

\[
\boxed{6\log_5 |K_n|=2\log_5 |V(H_n)|+O(1)}
\tag{2.1}
\]

with

\[
\boxed{O(\sqrt{\log |V(H_n)|})}
\tag{2.2}
\]

window. The output family is a uniform spectral expander with the explicit bound

\[
\boxed{\operatorname{gap}(H_n)\ge \frac{3-\sqrt5}{148}}
\tag{2.3}
\]

and fails every fixed positive long-range-expansion constant.

## 3. The rotating-lamp semidirect Cayley graph

Let

\[
L_n=\operatorname{Cay}(K_n,U_n),\qquad |U_n|=6,
\]

be a connected undirected degree-six Ramanujan Cayley graph. Put

\[
\mathcal K_n=K_n\times K_n\times K_n.
\]

Let `C_3=<c>` act on `\mathcal K_n` by cyclic coordinate rotation. Fix the convention

\[
c(x_0,x_1,x_2)c^{-1}=(x_2,x_0,x_1).
\]

Form the semidirect product

\[
\Gamma_n=\mathcal K_n\rtimes C_3.
\]

For `u in U_n`, write `u_0=(u,e,e)`. Define

\[
\Sigma_n=\{c,c^{-1}\}\cup\{u_0:u\in U_n\}
\tag{3.1}
\]

and

\[
H_n=\operatorname{Cay}(\Gamma_n,\Sigma_n).
\tag{3.2}
\]

The set is inverse closed. It generates the whole semidirect product because conjugating `u_0` by powers of `c` supplies the generators in coordinates one and two. Thus `H_n` is connected, simple, 8-regular and vertex-transitive. Its size is

\[
N_n=3|K_n|^3.
\tag{3.3}
\]

The construction is genuinely outside the preceding normalizing-voltage theorem: if `U_0={u_0:u in U_n}`, then

\[
cU_0c^{-1}=U_1\ne U_0.
\tag{3.4}
\]

So the active hidden generating set is not normalized by the switch generator.

## 4. Exact conditional switching identity

Run the rate-one continuous-time SRW on `H_n` from the identity. Let `I_t in C_3` be its phase coordinate. Poisson thinning gives two independent event streams:

* phase events have total rate `2/8=1/4`; at each such event the phase moves by `c` or `c^{-1}` with equal probability;
* lamp events have total rate `6/8=3/4`; at each such event the chosen label is uniform in `U_n`.

Let

\[
A_j(t)=\int_0^t \mathbf 1_{\{I_s=j\}}\,ds,
\qquad
B_j(t)=\frac34A_j(t),
\qquad j=0,1,2.
\tag{4.1}
\]

### Lemma 4.1 — conditional product law

Conditioned on the entire phase path `(I_s)_{0<=s<=t}`, the three lamp coordinates at time `t` are independent, and coordinate `j` has exactly the law of source rate-one continuous-time SRW on `L_n` run for time `B_j(t)`.

### Proof

Condition on the phase path. The lamp Poisson process of rate `3/4`, restricted to the three disjoint measurable time sets `{s:I_s=j}`, splits into independent Poisson processes of respective means `(3/4)A_j(t)`. When the phase is `j`, right multiplication by a generator `u_0` acts on the `j`-th direct-product coordinate because the current semidirect phase conjugates coordinate zero to coordinate `j`. The labels remain iid uniform in `U_n`. Hence each restricted process is exactly the source continuous-time walk on one copy of `L_n`, run for operational time `B_j(t)`, and the restrictions are independent. `QED`

This is where nonnormalizing monodromy becomes manageable. The conjugate vertical kernels are different, but they act on disjoint coordinates and therefore commute.

Let `d_L(s)` be the point-start TV distance of source continuous-time SRW on `L_n`; Cayley transitivity removes the start dependence. Let `d_H(t)` be the corresponding distance on `H_n`.

### Corollary 4.2 — switched-product upper bound

\[
\boxed{
 d_H(t)
 \le d_{C_3}^{(1/4)}(t)
 +\sum_{j=0}^2 \mathbb E\,d_L(B_j(t)).
}
\tag{4.2}
\]

Here `d_{C_3}^{(1/4)}` is the TV distance of the phase chain whose total jump rate is `1/4`.

### Proof

For each conditioned phase path, replace the three conditional lamp laws one at a time by uniform measure. The TV cost is at most the sum of their three TV distances. After all three replacements, the hidden coordinate is uniform and independent of the terminal phase; the remaining distance is exactly that of the phase marginal. Average over phase paths. `QED`

For this three-state chain the global-time generator has off-diagonal entries `1/8`, diagonal entries `-1/4`, and nonzero eigenvalues `-3/8`. In particular its TV term is exponentially negligible on logarithmic time scales.

## 5. Occupation-time concentration on the switch

For a fixed phase `j`, set

\[
f_j(i)=\mathbf 1_{\{i=j\}}-\frac13.
\]

The phase generator `Q` acts by `Qf_j=-(3/8)f_j`. Hence

\[
g_j=\frac83 f_j
\]

solves `Qg_j=-f_j`. Dynkin's martingale formula gives

\[
A_j(t)-\frac t3=g_j(I_0)-g_j(I_t)+M_j(t).
\tag{5.1}
\]

The oscillation of `g_j` is `8/3`. Phase jumps occur at rate `1/4`, so a crude predictable-quadratic-variation bound is

\[
\langle M_j\rangle_t\le \frac{16}{9}t.
\]

Consequently

\[
\mathbb E\left(A_j(t)-\frac t3\right)^2
\le \frac{128}{9}+\frac{32}{9}t,
\tag{5.2}
\]

and, multiplying by `(3/4)^2`,

\[
\boxed{
\mathbb E\left(B_j(t)-\frac t4\right)^2\le 8+2t.
}
\tag{5.3}
\]

The constants are deliberately crude; the key point is the uniform `O(t)` bound. Thus each operational clock equals `t/4+O_P(\sqrt t)`.

## 6. Hidden post-cutoff bound in the source convention

Put

\[
M_n=|K_n|,\qquad L_n^*=\log_5 M_n.
\]

A degree-six Ramanujan graph is long-range expanding by Altschuler's Theorem 1.7. His Corollary 1.13 gives lazy discrete-time cutoff at

\[
3L_n^*
\]

with `O(sqrt(L_n^*))` window, including the bipartite case.

Let `P` be nonlazy SRW and `Q=(I+P)/2`. The source nonlazy continuous-time semigroup satisfies

\[
e^{s(P-I)}=e^{2s(Q-I)}.
\tag{6.1}
\]

Poissonizing a discrete cutoff with a square-root window changes the window only by another square-root fluctuation. In particular, for every `epsilon>0` there is `K_epsilon<infinity` such that, uniformly for all large `n`,

\[
\boxed{
 d_L\left(\frac32L_n^*+K_\epsilon\sqrt{L_n^*}\right)\le\epsilon.
}
\tag{6.2}
\]

For completeness, only this upper half is needed below: at continuous lazy time `3L_n^*+2K sqrt(L_n^*)`, the number of lazy steps is Poisson with that mean. A standard Poisson lower-tail bound puts it beyond the discrete post-cutoff front except with probability tending to a quantity made arbitrarily small by increasing `K`; convexity of TV then proves (6.2).

## 7. Upper side of cutoff for the rotating-lamp graph

Set

\[
t_n^*=6L_n^*.
\tag{7.1}
\]

Take

\[
t=t_n^*+C\sqrt{L_n^*}.
\]

Then `t/4=(3/2)L_n^*+(C/4)sqrt(L_n^*)`. Fix `epsilon>0` and choose `K_epsilon` from (6.2). By (5.3), if `C>4K_epsilon`,

\[
\Pr\left(B_j(t)<\frac32L_n^*+K_\epsilon\sqrt{L_n^*}\right)
\le
\frac{8+2t}{(C/4-K_\epsilon)^2L_n^*}.
\tag{7.2}
\]

Thus the limsup of this probability is `O((C/4-K_epsilon)^{-2})`, uniformly in `j`. Monotonicity of continuous-time TV and (6.2) give

\[
\mathbb E d_L(B_j(t))
\le \epsilon+O((C/4-K_\epsilon)^{-2}).
\]

The phase term in (4.2) is `O(exp(-3t/8))`. Therefore

\[
\lim_{C\to\infty}\limsup_{n\to\infty}
 d_H(t_n^*+C\sqrt{L_n^*})=0.
\tag{7.3}
\]

## 8. Lower side: a common tree-ball witness

A mixture of pre-cutoff laws cannot safely be lower-bounded by mixing the individual TV distances, because different witnesses could cancel. We instead use one common metric ball.

Lift source continuous-time SRW on a degree-six graph to the 6-regular tree. Let `R_s` be the radial distance from the root. Away from zero its drift is

\[
v=\frac{6-2}{6}=\frac23.
\]

At zero the drift is one. Hence

\[
R_s=\frac23s+M_s+\frac13\mathcal L_s^0,
\tag{8.1}
\]

where `M_s` is a martingale with predictable quadratic variation at most `s`, and `\mathcal L_s^0` is the total holding time at the root. Starting after a departure from the root, the probability ever to return is `1/5`; therefore the number of root visits is geometric and the exponential holding times imply that `\mathcal L_\infty^0` has an exponential tail.

Now take

\[
t=t_n^*-C\sqrt{L_n^*}.
\]

By (5.3), for each fixed coordinate, with probability `1-O(C^{-2})`,

\[
B_j(t)\le s_{\max}:=rac32L_n^*-rac C8\sqrt{L_n^*}.
\tag{8.2}
\]

For every `s<=s_max`,

\[
\frac23s\le L_n^*-rac C{12}\sqrt{L_n^*}.
\]

Set

\[
r_n=\left\lfloor L_n^*-rac C{24}\sqrt{L_n^*}\right\rfloor.
\tag{8.3}
\]

Using (8.1), split the event `{R_s>r_n}` according to whether `\mathcal L_s^0` exceeds `(C/16)sqrt(L_n^*)`. The root-local-time term then has exponentially small probability, while Chebyshev for `M_s` gives, uniformly in `s<=s_max`,

\[
\Pr(R_s>r_n)=O(C^{-2})+o_n(1).
\tag{8.4}
\]

The endpoint in the finite graph cannot be farther from its start than its covering-tree lift. Hence all operational times in (8.2) share the same witness ball `B_{L_n}(e,r_n)`.

A degree-six graph has

\[
|B(e,r)|\le 1+6\sum_{k=0}^{r-1}5^k\le C_0 5^r.
\]

Therefore uniform measure gives

\[
\pi_n(B(e,r_n))
\le C_0 5^{-C\sqrt{L_n^*}/24}=o_n(1).
\tag{8.5}
\]

Project the full walk to, say, lamp coordinate zero. Combining (8.2)--(8.5), its law assigns the ball probability `1-O(C^{-2})-o_n(1)` while equilibrium assigns `o_n(1)`. Projection contracts TV, so

\[
\lim_{C\to\infty}\liminf_{n\to\infty}
 d_H(t_n^*-C\sqrt{L_n^*})=1.
\tag{8.6}
\]

Together, (7.3) and (8.6) prove cutoff at `t_n^*` with `O(sqrt(L_n^*))` window in the exact Salez convention.

Since `N_n=3M_n^3`,

\[
6\log_5M_n=2\log_5N_n-2\log_5 3,
\]

so the center is exactly the form stated in (2.1), and the window is `O(sqrt(log N_n))`.

## 9. Uniform spectral expansion

The cutoff proof above does not by itself show that the output lies in Salez's expander class, so we record a direct quantitative comparison.

Let `ell=|U_n|` temporarily. On the same state space `K_n^3 x C_3`, consider the reference Cartesian Cayley graph which allows phase moves and lamp moves in **all three** coordinates. Its degree is

\[
D_R=2+3\ell.
\]

Its normalized spectral gap is

\[
\gamma_R=rac{\min\{3,\ell\gamma_L\}}{2+3\ell},
\tag{9.1}
\]

where `gamma_L` is the normalized gap of the hidden graph. Indeed, the normalized `C_3` kernel has gap `3/2`, is selected with weight `2/D_R`, and each hidden coordinate is selected with weight `ell/D_R`.

Compare every directed reference edge with a path in `H_n`:

* a phase edge is already present;
* a lamp update in the currently active coordinate is already present;
* to update coordinate `j` while the phase is `i!=j`, move phase `i->j`, make the lamp update, and move phase back.

All comparison paths have length at most three. For an `H_n` lamp edge, the sum of path lengths of reference edges routed through it is at most `1+3+3=7`. For an `H_n` phase edge, it is at most

\[
1+6\ell:
\]

one direct phase edge, `ell` possible lamp labels using it as a first leg, and `ell` using it as a last leg, each latter path carrying length factor three. Thus the standard path comparison gives

\[
\mathcal E_R(f,f)
\le
\frac{(\ell+2)(6\ell+1)}{3\ell+2}\,\mathcal E_H(f,f).
\tag{9.2}
\]

Combining (9.1) and (9.2),

\[
\boxed{
\operatorname{gap}(H_n)
\ge
\frac{\min\{3,\ell\gamma_L\}}{(\ell+2)(6\ell+1)}.
}
\tag{9.3}
\]

For `ell=6`, Ramanujan gives

\[
\gamma_L\ge 1-\frac{2\sqrt5}{6}=\frac{3-\sqrt5}{3}.
\]

Hence `ell gamma_L>=6-2sqrt5<3` and

\[
\boxed{
\operatorname{gap}(H_n)
\ge\frac{6-2\sqrt5}{8\cdot37}
=\frac{3-\sqrt5}{148}>0.
}
\tag{9.4}
\]

Thus the new cutoff class is a bounded-degree vertex-transitive **spectral expander** sequence.

## 10. The output is not long-range expanding

The output degree is eight, so Altschuler's LRE branching benchmark is `7^r`.

A word of length `r` in the generators of `H_n` makes at most `r` lamp moves. If the three final lamp-coordinate distances in `L_n` are `r_0,r_1,r_2`, then

\[
r_0+r_1+r_2\le r.
\]

The degree-six bound on spheres gives, uniformly in `n`,

\[
|B_{H_n}(x,r)|
\le C(r+1)^3 5^r.
\tag{10.1}
\]

Choose

\[
r=\left\lfloor\frac12\log_7N_n\right\rfloor.
\]

Then `7^r=N_n^{1/2+o(1)}`, so the singleton alternative in the LRE definition would require a fixed positive multiple of `7^r`; but (10.1) gives

\[
\frac{|B_{H_n}(x,r)|}{7^r}
\le (\log N_n)^{O(1)}N_n^{-\beta+o(1)},
\qquad
\boxed{
\beta=\frac12\left(1-\frac{\log5}{\log7}\right)
=0.0864562623\ldots>0.
}
\tag{10.2}
\]

Therefore no fixed positive LRE constant works. This explicitly separates the new theorem from Altschuler's class.

## 11. Mechanism-level obstruction removed

The source-level verdict did not change. The mechanism-level verdict did.

The previous NM13-01 report isolated **nonnormalizing monodromy** as the next obstruction to its exact voltage-TV transfer. The present class violates normality in the strongest elementary way:

\[
cU_0c^{-1}=U_1,
\qquad
c^2U_0c^{-2}=U_2,
\]

with three distinct generating sets. Nevertheless cutoff survives because their Markov generators commute. Conditioning on the switch path reduces the full chain to three ordinary hidden walks run at random occupation clocks, and fixed-state transitivity makes those clocks concentrate on the square-root scale.

Thus the correct obstruction is narrower than "nonnormalizing monodromy": nonnormality alone is harmless when the conjugate semigroups commute and the switch has `O(t)` occupation variance. A genuinely new obstruction must involve **noncommuting** conjugate hidden dynamics (or absence of any finite switching/factor representation), where path ordering cannot be compressed to occupation times.

This suggests the next T08 target: establish an approximate version for bounded-dimensional noncommuting conjugate semigroups, perhaps by controlling time-ordered commutator error in `L^1`, or show by a source-valid transitive construction that such commutator accumulation can persist on the `Theta(log n)` mixing scale.

## 12. Essential sanity checks

The executed checker

`2026-09-20T11-24-00Z__rotating_lamp_checker.py`

builds the 192-state finite model with hidden `K_4=Cay(Z_4,{1,2,3})`, verifies degree five and adjacency symmetry, diagonalizes the full kernel, checks the canonical-path gap lower bound, checks the exact three-state phase eigenvalues and occupation-time variance constants, and records the degree-six Ramanujan constants used above. Its archived output ends

`ALL_CHECKS_PASS`.

The finite diagonalization is only a sanity check. No finite experiment is used as evidence for the asymptotic cutoff theorem.

## 13. Verdict

**Original problem:** `OPEN -> OPEN`.

**New restricted theorem:** source-continuous-time cutoff for the degree-eight rotating-lamp semidirect Cayley family at

\[
2\log_5N_n+O(1)
\]

with `O(sqrt(log N_n))` window, explicit spectral gap at least `(3-sqrt5)/148`, and quantitative failure of LRE.

**Mechanism advance:** exact conditional occupation-time factorization removes normalizer membership as a necessary transfer hypothesis in the commuting-conjugate case.

**Still unresolved:** arbitrary bounded-degree vertex-transitive spectral expanders may have no such finite switch decomposition, and genuinely noncommuting conjugate dynamics remain untreated.
