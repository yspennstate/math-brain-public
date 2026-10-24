Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — reversal-augmented arc cutoff and exact stabilizer-likelihood cancellation

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorem A and Lemmas B–C below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The checked repository contains line-graph, symmetrized nonbacktracking-arc, product, finite-fiber, truncation, exact-distance and spherical-set cutoff transfers, but not the reversal-augmented graph below. Bounded web searches on 20 September 2026 for combinations of `oriented edge graph`, `arc graph`, `reversal matching`, `nonbacktracking successors predecessors`, `random walk cutoff`, and `expander` did not locate this exact cutoff theorem. This is negative evidence only, not a worldwide priority certificate; graph-theoretic arc/dart constructions exist in the literature.

Repository/branch: `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.  
Pre-write master observed immediately before persistence work: `265e0acef4a8f3719a23d8327090585f32317807`.

## 0. Continuity handoff and partner split

LIVE20 remains the controlling owner instruction. The old NM13-01 intake/P0292 state is preserved and not rewritten. The newest own substantive report before this run was

`2026-09-20T06-20-00Z__arc-cover-hodge-orbit-drift.md`.

That report proved cutoff for a symmetrized nonbacktracking arc graph over **arc-transitive** LRE bases, with a two-sheet Hodge/Green cancellation estimate. It also decomposed root-stabilizer orbit-size growth into a bounded-jump martingale and a finite-alphabet additive functional, but its final varentropy estimate still contained a crude `(log r)^2` penalty where `r` is the stabilizer quotient rank.

The newest committed P26 report checked in this run is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_08-57-05__trimmed-green-bipartite-spherical-transfer.md`.

P26 now develops a complementary trimmed Green/spherical mechanism allowing exceptional spectral modes and gives a mixed-distance `{3,4}` application on a bipartite Ramanujan cover. This run does not duplicate spherical distance kernels. It instead adds a reversal matching to the oriented-edge construction and then returns to arbitrary transitivity to remove the stabilizer-rank term exactly.

The essential earlier dependency also re-read is

`2026-09-20T00-00-13Z__line-graph-lre-transfer.md`.

For a fixed `d`-regular edge-transitive LRE base `G_n` on `n` vertices, that theorem gives source-convention cutoff for `L(G_n)` at

\[
T_L=\frac{2(d-1)}{d-2}\log_{d-1}n
\]

with `O(sqrt(log n))` window. The proof there is by exact incidence intertwining plus Altschuler's LRE theorem; it is used as a proved dependency below rather than re-derived.

## 1. Source statement and current primary boundary

Justin Salez, `arXiv:2508.21055`, uses the rate-one continuous-time convention

\[
P_t=e^{t(T-I)}
=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!}.
\tag{1.1}
\]

Problem 2.3 is literally:

> Prove that all vertex-transitive expanders exhibit cutoff.

The primary status was refreshed on 20 September 2026.

* Dylan J. Altschuler, `arXiv:2609.14945` (submitted 14 September 2026), proves Gaussian-profile cutoff for every fixed-degree fixed-constant **long-range expander** and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Hence LRE is strictly stronger than Salez's source hypothesis.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345` (6 July 2026), prove the local-product/non-equilibrium-Poincare cutoff criterion. The checked result does not derive that criterion solely from vertex transitivity plus an ordinary spectral gap.
* Salez, `arXiv:2307.10066`, proves that on sparse fast-mixing chains the varentropy criterion is sharp. This is used only to interpret the obstruction reduction in Sections 8–10; the new special-class cutoff theorem does not need it.

Fresh bounded searches for a later theorem settling all vertex-transitive spectral expanders did not surface one; Altschuler's LRE result remained the relevant September 2026 advance. This is bounded status evidence, not proof of worldwide openness.

The POSTED exclusion concerning Salez Problem 2.4 (the Abelian-Cayley/product-condition material) remains untouched.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was `OPEN`. NM13-01 had already proved several explicit non-LRE source-valid cutoff families, most recently the degree-`2(d-1)` symmetrized nonbacktracking arc graph over an **arc-transitive** LRE base.

### After this run

Salez Problem 2.3 remains `OPEN`.

The proved source-valid scope expands to the following distinct oriented-edge graph. The base symmetry assumption is weakened from arc transitivity to **edge transitivity**, while the output graph acquires an additional reversal matching and a different exact cutoff constant.

> **Theorem A — reversal-augmented arc cutoff.**  
> Fix `d>=3`, put `q=d-1`, and let `(G_n)` be connected simple `d`-regular **edge-transitive** fixed-constant long-range expanders with `n=|V(G_n)| -> infinity`. Define `B_n=B(G_n)` on the oriented edges `a=(u,v)` of `G_n`. Join `(u,v)` to
> \[
> (v,w)\quad(w\sim v,\;w\ne u),
> \]
> to
> \[
> (w,u)\quad(w\sim u,\;w\ne v),
> \]
> and also to its reversal `(v,u)`.
> Then `B_n` is a simple `(2d-1)`-regular vertex-transitive spectral-expander sequence, is not a fixed-constant long-range-expander sequence, and Salez-convention continuous-time SRW on `B_n` has cutoff at
> \[
> \boxed{
> T_B=\frac{2d-1}{d-2}\log_{d-1}n
> }
> \tag{2.1}
> \]
> with window
> \[
> \boxed{O_{d,c,\varepsilon}(\sqrt{\log n})}
> =O(\sqrt{\log |V(B_n)|}).}
> \tag{2.2}
> \]
> Since `|V(B_n)|=dn`, the center is equivalently
> \[
> T_B=\frac{2d-1}{d-2}
> \log_{d-1}\!\left(\frac{|V(B_n)|}{d}\right).
> \tag{2.3}
> \]

If the normalized base SRW gap is at least `gamma`, then

\[
\boxed{
\operatorname{gap}(B_n)
\ge
\min\left\{
\frac{d\gamma}{2d-1},
\frac{2(d-1)}{2d-1}
\right\}.
}
\tag{2.4}
\]

For a degree-six edge-transitive Ramanujan/LRE base, the output has degree `11` and `6n` vertices and

\[
\boxed{T_B=\frac{11}{4}\log_5 n}
\tag{2.5}
\]

with `O(sqrt(log n))` window, while the Ramanujan bound gives

\[
\boxed{
\operatorname{gap}(B_n)
\ge \frac{6-2\sqrt5}{11}.
}
\tag{2.6}
\]

The class is source-valid because the **output** graphs themselves are bounded-degree vertex-transitive spectral expanders and are proved below to fail every fixed LRE constant.

## 3. Exact construction and why edge transitivity is enough

Let `A(G)` denote the preceding report's symmetrized nonbacktracking arc graph, with discrete SRW kernel `Q_A`. Let `J` reverse orientation:

\[
J(u,v)=(v,u).
\]

Every vertex of `A(G)` has `2q` nonbacktracking predecessor/successor neighbors. `B(G)` adds exactly the one reversal neighbor, so its kernel is

\[
\boxed{
Q_B=\alpha Q_A+\beta J,
\qquad
\alpha=\frac{2q}{2q+1},
\quad
\beta=\frac1{2q+1}.
}
\tag{3.1}
\]

The three neighbor sets are disjoint, so `B(G)` is simple and `(2q+1)=(2d-1)` regular.

Unlike the preceding arc theorem, the base need not be arc-transitive. If `G` is edge-transitive, an automorphism sends the underlying edge of any oriented arc `a` to the underlying edge of any target oriented arc `b`. If the orientation comes out reversed, compose with `J`. Since `J` is visibly an automorphism of `B(G)`, the group generated by `Aut(G)` and `J` acts transitively on oriented edges. Hence `B(G)` is vertex-transitive under **edge transitivity alone**.

## 4. Strong lumping onto a lazy line graph

Project an oriented edge to its underlying unoriented edge:

\[
\rho(u,v)=\{u,v\}.
\tag{4.1}
\]

From `(u,v)`, the `2q` nonbacktracking predecessor/successor moves project bijectively to the `2q` neighbors of `{u,v}` in `L(G)`, while the reversal move projects to a hold at `{u,v}`. Therefore `rho` is a strong lumping and the projected kernel is

\[
\boxed{
Q_{\rm proj}
=\beta I+\alpha Q_L,
}
\tag{4.2}
\]

where `Q_L` is ordinary SRW on `L(G)`.

In the exact source continuous-time convention,

\[
Q_{\rm proj}-I
=\alpha(Q_L-I),
\tag{4.3}
\]

so the projected TV curve at time `t` is exactly the line-graph TV curve at time `alpha t`.

The earlier line-graph theorem therefore predicts the candidate center

\[
\frac{T_L}{\alpha}
=
\frac{2q}{q-1}\log_qn\,
\frac{2q+1}{2q}
=
\boxed{\frac{2q+1}{q-1}\log_qn},
\tag{4.4}
\]

which is (2.1). It remains only to prove that the hidden orientation sheet is negligible throughout that window.

## 5. Odd Hodge sector with the reversal matching

The reversal involution commutes with both `Q_A` and `Q_B`, so arc functions split into even and odd sectors.

On the odd sector, the preceding report proved the exact identity

\[
Q_A
=\frac1qI+\frac1{2q}\nabla D,
\tag{5.1}
\]

where for an odd flow `f`

\[
(Df)(u)=\sum_{v\sim u}f(u,v),
\qquad
(\nabla g)(u,v)=g(v)-g(u),
\tag{5.2}
\]

and

\[
D\nabla=d(P-I)
\tag{5.3}
\]

for normalized base SRW `P`.

On odd functions `J=-I`. Multiplying (5.1) by `2q` and inserting it into (3.1) yields the new exact formula

\[
\boxed{
Q_B\big|_{\rm odd}
=\frac1{2q+1}(I+\nabla D).
}
\tag{5.4}
\]

Hence

\[
Q_B-I
=-g_BI+\frac1{2q+1}\nabla D,
\qquad
g_B=\frac{2q}{2q+1}.
\tag{5.5}
\]

In particular, every divergence-free cycle flow is now an eigenvector of `Q_B` with eigenvalue `1/(2q+1)`. The extensive cycle space still exists, but its continuous-time decay rate is the fixed constant `g_B`.

On a gradient `\nabla g` with `Pg=lambda g`, (5.3) gives

\[
Q_B\nabla g
=\frac{d\lambda-q}{2q+1}\nabla g.
\tag{5.6}
\]

Every nonzero gradient has `lambda<1`, so every odd eigenvalue is at most `1/(2q+1)`. Thus the odd-sector gap is at least `2q/(2q+1)`.

On the even sector, (4.2) applies. The preceding line-graph spectrum gives line gap at least `d gamma/(2q)`, so lazification multiplies that gap by `alpha=2q/(2q+1)`. Therefore the even gap is at least

\[
\frac{d\gamma}{2q+1}.
\]

This proves (2.4).

## 6. Hodge-Green `L^1` cancellation with the new decay rate

Fix `a=(u,v)` and `\bar a=(v,u)`, and put

\[
f_0=\delta_a-\delta_{\bar a}.
\tag{6.1}
\]

From (5.5), with `s=t/(2q+1)`,

\[
e^{t(Q_B-I)}f_0
=e^{-g_Bt}e^{s\nabla D}f_0.
\tag{6.2}
\]

The same elementary `AB/BA` identity as in the preceding report gives

\[
e^{s\nabla D}f_0
=f_0+\nabla\int_0^s e^{rD\nabla}Df_0\,dr.
\tag{6.3}
\]

Here

\[
Df_0=\delta_u-\delta_v,
\qquad
D\nabla=d(P-I).
\tag{6.4}
\]

For any vertex function `h`,

\[
\|\nabla h\|_{\ell^1(\vec E)}
\le2d\|h\|_{\ell^1(V)}.
\tag{6.5}
\]

If the base normalized gap is at least `gamma`, then the signed heat-kernel difference obeys

\[
\|e^{rd(P-I)}(\delta_u-\delta_v)\|_1
\le
\min\{2,\sqrt{2n}\,e^{-d\gamma r}\}.
\tag{6.6}
\]

Integrating the right side over `[0,infinity)` gives at most

\[
\frac{\log n+2}{d\gamma}.
\tag{6.7}
\]

Combining (6.3)–(6.7), uniformly in `s>=0`,

\[
\|e^{s\nabla D}f_0\|_1
\le
2+\frac{2(\log n+2)}\gamma.
\tag{6.8}
\]

Therefore

\[
\boxed{
\|e^{t(Q_B-I)}f_0\|_1
\le
2\left(1+\frac{\log n+2}\gamma\right)
 e^{-g_Bt}.
}
\tag{6.9}
\]

Again the point-source cost is only `O(log n)` despite an extensive local eigenspace.

## 7. TV sandwich and completion of Theorem A

Decompose

\[
\delta_a
=\frac12(\delta_a+\delta_{\bar a})
 +\frac12(\delta_a-\delta_{\bar a}).
\tag{7.1}
\]

The even part is the uniform two-orientation lift of the projected lazy line walk. Projection cannot increase TV, while the odd part is controlled by (6.9). Thus, writing `d_L` for the ordinary line-graph continuous-time TV curve,

\[
\boxed{
 d_L(\alpha t)
 \le d_B(t)
 \le d_L(\alpha t)
 +\frac12\left(1+\frac{\log n+2}\gamma\right)e^{-g_Bt}.
}
\tag{7.2}
\]

Let

\[
T_B=\frac{2q+1}{q-1}\log_qn.
\]

At this center,

\[
g_BT_B
=\frac{2q}{2q+1}\frac{2q+1}{q-1}\log_qn
=\frac{2q}{q-1}\log_qn.
\tag{7.3}
\]

Hence for every fixed `C`, uniformly for

\[
|t-T_B|\le C\sqrt{\log n},
\]

the error term in (7.2) is

\[
(\log n)\exp\{-g_Bt\}
=n^{-2q/((q-1)\log q)+o(1)}\log n=o(1).
\tag{7.4}
\]

Meanwhile `alpha t` ranges over an `O(sqrt(log n))` window about the line center `T_L`. The earlier line theorem therefore transfers directly through (7.2), proving cutoff at (2.1) with the claimed window. `QED`

## 8. The output is not a fixed-constant long-range expander

Every `B(G)` step either projects to one line-graph step or to a hold. Therefore

\[
\rho(B_{B(G)}(a,r))
\subseteq B_{L(G)}(\rho(a),r).
\tag{8.1}
\]

Each line vertex has exactly two oriented lifts. For a `d`-regular base,

\[
|B_{L(G)}(e,r)|
\le1+2\sum_{j=1}^r q^j
\le C_dq^r,
\tag{8.2}
\]

so

\[
|B_{B(G)}(a,r)|\le2C_dq^r.
\tag{8.3}
\]

But `B(G)` has degree `D=2q+1`, hence its LRE tree benchmark grows as

\[
(D-1)^r=(2q)^r.
\tag{8.4}
\]

Taking, for example,

\[
r_n=\left\lfloor\frac12\log_{2q}|V(B_n)|\right\rfloor,
\]

the ratio of (8.3) to any fixed positive multiple of `(2q)^{r_n}` tends to zero. Thus no fixed LRE constant is possible for the output sequence.

This is why Theorem A is not an application of Altschuler's theorem to `B_n` itself.

## 9. The previous stabilizer-rank obstruction was partly artificial

The preceding run ended with the concern that the canonical root-stabilizer quotient can have `Theta(n)` states. Its crude varentropy estimate separately bounded orbit-size fluctuation and quotient-law surprisal, producing a `(log r)^2` term. The following two lemmas show that **rank and orbit-size heterogeneity are not themselves the information obstruction**.

Let `X` be a connected `d`-regular vertex-transitive graph on `n` vertices, let `Gamma` be a transitive automorphism group, root `o`, and `H=Gamma_o`. Let `O_i` be the `H`-orbits, with

\[
m_i=|O_i|.
\]

If `c_{ij}` is the number of neighbors in `O_j` of a vertex in `O_i`, edge counting gives

\[
\boxed{m_ic_{ij}=m_jc_{ji}.}
\tag{9.1}
\]

Whenever two orbits are adjacent, both counts are integers in `{1,...,d}`, so for

\[
h(i)=\log m_i
\]

we have

\[
\boxed{|h(i)-h(j)|\le\log d.}
\tag{9.2}
\]

### Lemma B — uniform stationary concentration of stabilizer-orbit sizes

Assume the normalized one-sided spectral gap of `X` is at least `gamma>0`. Let `U` be uniform on `V(X)` and write `h(U)=log|H U|`. Put

\[
L=\log d,
\qquad
\kappa=\gamma/2,
\qquad
R=1+\kappa.
\]

Then for a median `a` of `h(U)` and every integer `k>=1`,

\[
\boxed{
\Pr(|h(U)-a|\ge kL)
\le R^{-(k-1)}.
}
\tag{9.3}
\]

Consequently

\[
\boxed{
\operatorname{Var}_\pi(h)
\le C_{d,\gamma}
:=L^2\left(1+\frac{2R^2}{\kappa^2}+\frac{R}{\kappa}\right).
}
\tag{9.4}
\]

**Proof.** For any vertex set `S` with stationary mass `p<=1/2`, the spectral gap gives

\[
Q(S,S^c)
=\langle1_S,(I-P)1_S\rangle_\pi
\ge\gamma p(1-p)
\ge\frac\gamma2p.
\tag{9.5}
\]

Every crossing edge terminates in the external vertex boundary, and each boundary vertex receives at most `d` crossing edges, hence

\[
\pi(N[S]\setminus S)\ge Q(S,S^c).
\tag{9.6}
\]

Therefore

\[
\boxed{\pi(N[S])\ge(1+\gamma/2)\pi(S)=R\pi(S).}
\tag{9.7}
\]

For the sublevel set `A_s={h<=s}`, (9.2) implies

\[
N[A_s]\subseteq A_{s+L}.
\tag{9.8}
\]

Choose `a` so that `Pr(h<a)<=1/2` and `Pr(h>a)<=1/2`. Starting from `A_{a-kL}` and iterating (9.7)–(9.8) through `A_{a-L}` gives

\[
\Pr(h\le a-kL)
\le\frac12R^{-(k-1)}.
\tag{9.9}
\]

Apply the same argument to upper sets `B_s={h>=s}`, for which `N[B_s]` is contained in `B_{s-L}`, to get

\[
\Pr(h\ge a+kL)
\le\frac12R^{-(k-1)}.
\tag{9.10}
\]

This proves (9.3). Finally

\[
\operatorname{Var}(h)
\le\mathbb E[(h-a)^2]
=\int_0^\infty2t\Pr(|h-a|\ge t)\,dt.
\]

Using (9.3) on successive intervals of length `L`,

\[
\mathbb E[(h-a)^2]
\le L^2\left[1+\sum_{k\ge1}(2k+1)R^{-(k-1)}\right],
\]

and the geometric sums equal `2R^2/kappa^2+R/kappa`. This gives (9.4). `QED`

If `\bar\pi_i=m_i/n` is the stationary law of the stabilizer quotient, then

\[
\log\frac1{\bar\pi_i}=\log n-h(i),
\]

so Lemma B immediately yields

\[
\boxed{
\operatorname{Var}_{\bar\pi}
\left(\log\frac1{\bar\pi}\right)
\le C_{d,\gamma}.
}
\tag{9.11}
\]

Thus a quotient may have enormous rank while its **stationary surprisal** still has uniformly bounded variance.

## 10. Exact likelihood cancellation: quotient rank disappears from varentropy

The more decisive point is dynamic and exact.

Let `mu_t` be SRW on `X` started from the root `o`, and `nu_t(i)=mu_t(O_i)` its stabilizer-orbit quotient law. Root-start invariance under `H` makes `mu_t` uniform inside each orbit, hence for `x in O_i`,

\[
\mu_t(x)=\frac{\nu_t(i)}{m_i}.
\tag{10.1}
\]

Define the quotient density relative to its stationary law

\[
f_t(i)=\frac{\nu_t(i)}{\bar\pi_i}
=\frac{n\nu_t(i)}{m_i}.
\tag{10.2}
\]

Then (10.1) becomes the exact identity

\[
\boxed{\mu_t(x)=\frac{f_t(i)}n.}
\tag{10.3}
\]

Therefore the full-chain likelihood ratio against uniform equilibrium is simply

\[
\boxed{
\frac{\mu_t(x)}{1/n}=f_t(i).
}
\tag{10.4}
\]

In particular Salez's information random variable and varentropy are preserved **without any separate orbit-size term**:

\[
\boxed{
V_{KL}(t)
=
\operatorname{Var}_{\nu_t}
\bigl(\log f_t(Y_t)\bigr).
}
\tag{10.5}
\]

This is stronger than the preceding run's inequality that separately bounded `h(Y_t)` and `-log nu_t(Y_t)`. In fact those two quantities cancel:

\[
h(i)-\log\nu_t(i)
=\log n-\log f_t(i).
\tag{10.6}
\]

### Lemma C — the true quotient obstruction

For root-start walk on any finite vertex-transitive graph, the stabilizer quotient preserves the entire point-start likelihood-ratio random variable. Consequently:

1. the number `r` of stabilizer orbits never needs to appear in a varentropy bound merely because the quotient has `r` states;
2. orbit-size fluctuation does not need to be controlled separately from quotient surprisal; and
3. for fixed-degree spectral expanders, Lemma B shows even the stationary orbit-size surprisal has `O_{d,gamma}(1)` variance.

The remaining task for the full conjecture is therefore sharply localized to

\[
\boxed{
\operatorname{Var}_{\nu_{t_{mix}}}
\left(\log\frac{\nu_{t_{mix}}}{\bar\pi}(Y_{t_{mix}})\right)
=o((\log n)^2),
}
\tag{10.7}
\]

or to a different mechanism proving cutoff. No quotient-rank hypothesis such as `log r=o(log n)` is intrinsically required by this reduction.

This does **not** prove (10.7) from transitivity plus a spectral gap. It removes the earlier false sub-obstruction and identifies the correct dynamic quantity.

## 11. What moved, and what did not

### Source-level movement

The parent conjecture remains `OPEN -> OPEN`. The theorem scope strictly enlarges by Theorem A: reversal-augmented oriented-edge outputs of edge-transitive LRE bases have source-convention cutoff with explicit center (2.1) and `O(sqrt(log N))` window, are vertex-transitive spectral expanders, and are not LRE.

### Mechanism-level movement

Two obstructions are removed.

1. The orientation sector survives adding a reversal matching and still admits exact `L^1` Hodge-Green cancellation. This also lets edge transitivity, rather than arc transitivity, suffice for output transitivity.
2. The previous `(log r)^2` stabilizer-rank penalty is an artifact of separating two exactly cancelling terms. Equations (10.3)–(10.6) show that the correct dynamic object is the quotient likelihood ratio `nu_t/barpi`, while Lemma B proves that stationary orbit-size heterogeneity itself is uniformly concentrated under spectral expansion.

The general conjecture is not relabeled solved. Arbitrary transitive spectral expanders need not expose a line/Hodge factor, and no proof here bounds (10.7) universally.

## 12. Exact executed sanity checks

The exact checker is

`2026-09-20T07-22-00Z__reversal_arc_orbit_checker.py`

with archived output

`2026-09-20T07-22-00Z__reversal_arc_orbit_checker.out`.

It verifies with exact rational/symbolic arithmetic:

* simplicity and degree `2q+1` of `B(G)` on `K4` and `K_{3,3}`;
* exact strong lumping to `beta I + alpha Q_L`;
* commutation with reversal;
* the odd identity
  \[
  (2q+1)Q_B=I+\nabla D
  \]
  on the odd sector and `D nabla=d(P-I)`;
* the complete `B(K4)` and `B(K_{3,3})` spectra and the spectral-gap lower bound;
* the degree-six constants `11/4`, `10/11`, the product `5/2`, and the Ramanujan output-gap expression `(6-2 sqrt(5))/11`;
* stabilizer orbit balance and the vertex-expansion inequality on the 3-cube.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

These finite checks validate algebra and constants only; the asymptotic theorem and orbit concentration are proved on the page above.

## 13. Failed/retired routes and next attack

The raw output-NBRW collision trace remains retired as a necessary condition: the earlier incidence-strong family violates it polynomially while having cutoff. Ambient `L^2` control of local eigenspaces also remains inadequate because of dimension prefactors; the Hodge-Green `L^1` calculation is the successful replacement when a suitable signed representation exists.

The preceding attempt to control stabilizer varentropy by separately bounding orbit-size drift and quotient surprisal is now superseded: exact likelihood cancellation shows those terms should not be estimated separately.

The next transitivity-specific attack is to work directly with the quotient density `f_t=nu_t/barpi`: derive either an `L^1` Green/log-likelihood gradient estimate or an occupation/Dirichlet bound for `log f_t` that depends only on fixed degree and the inherited spectral gap. The first stress tests should be high-rank transitive expanders where ambient `L^2` and raw NBRW trace are already known to be misleading.

## 14. Ledger delta

```json
{
  "slot": "NM13-01",
  "parent": "T08",
  "source": "Salez arXiv:2508.21055 Problem 2.3",
  "source_status_before": "OPEN",
  "source_status_after": "OPEN",
  "source_level_gain": "cutoff for reversal-augmented symmetrized arc graphs of fixed-degree edge-transitive LRE bases; center ((2d-1)/(d-2)) log_{d-1} n; O(sqrt(log N)) window; output vertex-transitive spectral and non-LRE",
  "mechanism_gain": "lazy line lumping plus odd Hodge-Green L1 cancellation; uniform stationary stabilizer-orbit-size concentration; exact dynamic quotient-likelihood identity eliminating rank/orbit-size terms from varentropy",
  "obstruction_removed": "the previous (log r)^2 stabilizer quotient rank penalty and separate orbit-size occupation obligation are artifacts of breaking an exact likelihood cancellation",
  "remaining_obstruction": "bound Var_nu(log(nu/barpi)) at mixing time from arbitrary vertex transitivity plus spectral expansion, or find a different universal transport mechanism",
  "checker_result": "ALL_EXACT_CHECKS_PASS",
  "publication_novelty": "UNVERIFIED",
  "runtime_model": "GPT-5.6 Sol",
  "runtime_reasoning": "UNVERIFIED"
}
```
