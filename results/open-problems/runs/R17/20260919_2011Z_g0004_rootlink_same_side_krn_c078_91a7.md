Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; post-recovery-2 substantive unchanged count `1 -> 2`; methods #9 RANDOMIZE / #19 MAKE IT AN ALGORITHM / #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R17 C078 — G0004: root-link recursion, a realizable mixture obstruction, and the same-side `K_{r,n+1}` theorem

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Status: **OPEN / PARTIAL.** Recovery 2/2 was already consumed in C077. This run gives a new source-valid nonplanar family theorem and an exact recursive inequality, but it does not move the fixed source-wide metric.

## 0. Continuity, ownership, required reading, and fresh source check

The canonical claim `operations/claims/G0004.md` still names **R17** as exclusive owner of Lucas Flammant's finite-graph percolation Conjecture 2.2. The original Chvatal--Sankoff binary-LCS target remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and the later Rhodes--Vargas `D0064` target remains terminal at `R_class=0/3`. Neither predecessor is reopened.

At run start I reread or rechecked the required current surfaces: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; canonical claim `operations/claims/G0004.md`; newest own report C077 and the preceding G0004 chain; the canonical intake identity `flammant_finite_graph_2026::conjecture_2.2`; and the current neighboring admission/search traces. A repository-wide recent-commit check found no newer R17 report than C077 and no newer competing G0004 owner.

Fresh primary-source search on 2026-09-19 again found arXiv:2609.03492 as the current Flammant source. Its current public abstract still presents the arbitrary finite-graph statement as a conjecture and says the proved case is finite planar graphs with origin and boundary vertices on the outer-face boundary, with success lower bound `1-2 sqrt(epsilon)`. Exact-title/arXiv searches combined with `K_{3,n}`, complete-bipartite, and Conjecture 2.2 language found no later primary source claiming the unrestricted theorem or the complete-bipartite theorem below. This is bounded negative evidence, not a worldwide novelty certificate.

The fixed source-wide metric is still

\[
U_F:=\inf\Bigl\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under all source quantifiers}\Bigr\}.
\]

Before: `U_F=1`. After: `U_F=1`.

C077 was the first substantive unchanged run after recovery 2/2. This is the second. One more substantive G0004 run with no movement of `U_F` reaches the third Section-I stuck episode, at which point HARD policy requires handoff and rotation; there is no third recovery.

All G0004 method numbers except #9, #19, #23 had already been used in C069--C077. Therefore this run uses exactly the three remaining untried methods on this source rather than repeating the exhausted C077 suggestion.

## 1. Source-normalized setup inherited from the track

Let Bernoulli bond percolation with parameter `p` live on a finite graph `G=(V,E)`, with origin `o` and boundary `B`. For `b in B`, after eliminating auxiliary randomness write

\[
q_b(\omega):=1-\Pr(E_b\mid\pi=\omega),
\]

so each `q_b` is decreasing and

\[
\mathbb E q_b\le\varepsilon.
\]

Let

\[
S(\omega)=\{b\in B:o\leftrightarrow b\},
\qquad C=\{S\ne\varnothing\},
\qquad N=|S|,
\]

and on `C` set

\[
m(\omega)=\min_{b\in S(\omega)}q_b(\omega),
\]

with `m=0` off `C`. The source failure ratio is bounded by

\[
R_G(q)=\frac{\mathbb E m}{\Pr(C)}.
\tag{1.1}
\]

C074 proved the general contact-tail reduction. If

\[
M=\mathbb E[N\mid C],
\]

then for every `a>0`,

\[
\boxed{
R_G(q)\le
\Pr(N\le aM\mid C)+\frac{\varepsilon}{a}.
}
\tag{1.2}
\]

C077 proved the one-dimensional conditional-binomial lemma used again below. Put

\[
c_0:=1-e^{-1}.
\]

If `D~Bin(d,s)`, `mu=E[D|D>0]`, and `0<t<=c_0/2`, then

\[
\boxed{
\Pr(D\le t\mu\mid D>0)
\le
c_0^{-1}\exp\!\left(-\frac{c_0}{8t}\right).
}
\tag{1.3}
\]

These are inherited results, not new claims of C078.

## 2. Method #9 — RANDOMIZE: exact root-link recursion

The first attempt was to randomize the choice of a connected boundary owner. Uniform random priorities merely recreate the uniform-contact selector and do not remove the contact multiplicity; this is the same failure mechanism identified earlier. The useful random object is instead the set of **active open root branches**.

Let the edges incident to `o` be

\[
e_i=\{o,v_i\},\qquad i=1,\dots,d,
\]

with root-edge indicators `X_i`. Delete `o` and all root edges, and write `xi` for the remaining percolation configuration. Define

\[
S_i(\xi):=\{b\in B:v_i\leftrightarrow b\text{ in }G-o\},
\qquad
J_i(\xi):={\bf1}_{\{S_i(\xi)\ne\varnothing\}}.
\]

The number of open root edges that actually lead into a boundary-reaching component is

\[
K:=\sum_{i=1}^d X_iJ_i.
\tag{2.1}
\]

A simple path from `o` to `B` leaves `o` exactly once, so

\[
\boxed{C=\{K>0\}.}
\tag{2.2}
\]

For an integer `n>=1`, let

\[
\mathcal R_n(\varepsilon)
\]

denote the supremum of (1.1) over source-admissible instances with at most `n` vertices. No claim is made that this supremum is attained.

### Theorem 2.1 (root-link recursive moment inequality)

For every finite source-admissible instance `G` with `|V|=n`,

\[
\boxed{
\mathbb E[K m]
\le
\mathcal R_{n-1}(\varepsilon)\,\mathbb E K.
}
\tag{2.3}
\]

Consequently, if

\[
M_K:=\mathbb E[K\mid C],
\]

then for every `a>0`,

\[
\boxed{
R_G(q)
\le
\Pr(K\le aM_K\mid C)
+
\frac{\mathcal R_{n-1}(\varepsilon)}{a}.
}
\tag{2.4}
\]

#### Proof

Fix `i`. Condition on `X_i=1` and on the non-root configuration `xi`, and average only over the other root-edge indicators `X_{-i}`. For each `b in B` define

\[
r_{i,b}(\xi)
:=
\mathbb E_{X_{-i}}
\bigl[q_b(1,X_{-i},\xi)\bigr].
\tag{2.5}
\]

Because `q_b` is decreasing in every edge coordinate, `r_{i,b}` is decreasing as a function of `xi`. Moreover

\[
\mathbb E_\xi r_{i,b}(\xi)
=
\mathbb E[q_b\mid X_i=1]
\le
\mathbb E q_b
\le\varepsilon,
\tag{2.6}
\]

where the middle inequality is Harris--FKG, since `{X_i=1}` is increasing and `q_b` is decreasing.

If `J_i(\xi)=1`, then every `b in S_i(\xi)` is connected to `o` whenever `X_i=1`, regardless of the other root edges. Hence pointwise in `xi`,

\[
\mathbb E_{X_{-i}}[m\mid X_i=1,\xi]
\le
\min_{b\in S_i(\xi)}r_{i,b}(\xi).
\tag{2.7}
\]

The right-hand side is exactly a source-valid kernel failure functional on the strictly smaller graph `G-o`, rooted at `v_i`, with boundary `B` and decreasing kernels `(r_{i,b})` satisfying the same `epsilon` budget. Therefore, by the definition of `mathcal R_{n-1}`,

\[
\mathbb E_\xi
\left[
J_i\min_{b\in S_i}r_{i,b}
\right]
\le
\mathcal R_{n-1}(\varepsilon)\Pr(J_i=1).
\tag{2.8}
\]

Using independence of `X_i` from `xi` and summing over root edges,

\[
\begin{aligned}
\mathbb E[K m]
&=
\sum_i\mathbb E[J_iX_i m]\\
&\le
p\sum_i
\mathbb E_\xi
\left[J_i\min_{b\in S_i}r_{i,b}\right]\\
&\le
\mathcal R_{n-1}(\varepsilon)
\,p\sum_i\Pr(J_i=1)\\
&=
\mathcal R_{n-1}(\varepsilon)\mathbb E K.
\end{aligned}
\]

This proves (2.3). For (2.4), split `C` into `{K<=aM_K}` and its complement. On the complement,

\[
m\le\frac{Km}{aM_K}.
\]

Then (2.3) and `E K=M_K P(C)` give (2.4). `square`

### Why this matters

This is the cleanest self-similar recursion found so far on the unrestricted graph class. The price of deleting the root is not an enlarged epsilon budget: the same `epsilon` survives exactly. The remaining obstruction is concentrated entirely in the conditional lower tail of `K`.

Unfortunately, unlike the direct-edge count in C077, `K` is a mixture of binomials because the random active-branch count `sum_i J_i(xi)` is itself generated by the rest of the graph. The next section proves that this mixture problem is genuine and can be arbitrarily violent even in honest Bernoulli percolation.

## 3. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: try to turn the branch mixture into a counterexample

The counterexample attempt was deliberately aimed at the exact weak point of (2.4): create configurations where only one root branch is active with constant conditional probability, but many branches are active in another mode, so that `M_K` diverges while `K=1` retains positive conditional mass.

This can be realized exactly at the level of the root-branch statistic.

Fix `p=1/2`. Give the root neighbors

\[
v_0,v_1,\dots,v_M.
\]

Put `v_0` itself in the boundary, so `J_0=1` deterministically after deleting `o`. For each `i>=1`, join `v_i` to a common hub `h` by `L` internally vertex-disjoint two-edge paths. Let

\[
r_L=1-(3/4)^L
\]

be the exact probability that at least one such two-edge path is open. Add one common edge `g={h,b_*}` to a second boundary vertex `b_*`, and add no other route from the `v_i`, `i>=1`, to the boundary.

Then after deleting `o`,

\[
J_0=1,
\qquad
J_i=G H_i\quad (1\le i\le M),
\tag{3.1}
\]

where `G~Bernoulli(1/2)` is the common-gate indicator and the `H_i` are independent `Bernoulli(r_L)`, independent of `G`. Thus

\[
\sum_iJ_i
=
1+G\sum_{i=1}^M H_i.
\tag{3.2}
\]

The root-edge variables remain iid `Bernoulli(1/2)`, so when `G=0`,

\[
K=X_0,
\]

whereas when `G=1` and `L` is large, `K` is close to a `Binomial(M+1,1/2)` variable.

Choose any sequence `L=L(M)` with `M(3/4)^{L(M)}->0`, so with probability `1-o(1)` all `H_i=1`. Then

\[
\Pr(C)\to
\frac12\cdot\frac12
+
\frac12\cdot1
=
\frac34,
\tag{3.3}
\]

while

\[
\Pr(G=0,K=1\mid C)\to\frac{1/4}{3/4}=\frac13.
\tag{3.4}
\]

At the same time

\[
M_K=\mathbb E[K\mid C]=\Theta(M).
\tag{3.5}
\]

Therefore, for every fixed `a>0` small enough,

\[
\liminf_{M\to\infty}
\Pr(K\le aM_K\mid C)
\ge\frac13.
\tag{3.6}
\]

So **no universal lower-tail estimate for the root-branch count `K` can close (2.4)**. This is not a counterexample to Flammant's conjecture: no admissible failure kernels have been constructed that exploit the small-`K` mode at nonvanishing source failure ratio. It is instead an exact obstruction to the tempting recursive proof architecture.

The attempt therefore failed as a refutation but succeeded in identifying what an unrestricted proof must add: it must carry some information about the *quality / boundary mass* of active branches, not merely how many root branches are active.

No finite numerical assertion is needed here; (3.1)--(3.6) follow analytically from independent Bernoulli edges and the exact reliability `r_L=1-(3/4)^L`.

## 4. Method #19 — MAKE IT AN ALGORITHM: solve the smallest genuinely shared complete-bipartite core

C077 solved complete bipartite graphs when the boundary is the side opposite the root. That geometry has direct boundary neighbors. The natural next algorithmic state is the opposite placement:

\[
G=K_{r,n+1},
\]

with bipartition

\[
H\sqcup(\{o\}\cup B),
\qquad |H|=r,\quad |B|=n.
\]

Thus the root and every boundary vertex lie on the **same** side. For `r>=3` and `n+1>=3` this is nonplanar, and the connected boundary set may be enlarged by hub-to-hub communication through other boundary vertices. The C077 theorem does not apply because the root neighborhood is `H`, not `B`.

The first algorithmic impulse is to track the full `2^r` column type of every boundary vertex. That is unnecessary. The correct statistic is the number of boundary vertices hit **directly** through the root-open hub set.

Let

\[
A:=\{h\in H:\{o,h\}\text{ is open}\},
\qquad K_0:=|A|.
\]

For a boundary vertex `b`, call `b` a direct contact if at least one edge `{h,b}` with `h in A` is open. Let

\[
N_0:=\#\{b\in B:b\text{ is a direct contact}\}.
\tag{4.1}
\]

A simple path from `o` to any boundary vertex must first go from `o` to some `h in H`, and its next new vertex is already in `B`. Hence

\[
\boxed{C=\{N_0>0\}.}
\tag{4.2}
\]

The full connected boundary count can be larger than `N_0`, because already connected boundary vertices can bridge different hubs, but always

\[
N_0\le N.
\tag{4.3}
\]

Let `T` be the total number of open edges between `H` and `B`. Every connected boundary vertex uses at least one such open incident edge, and distinct boundary vertices use distinct incident edge endpoints, so

\[
N\le T.
\tag{4.4}
\]

Conditional on `K_0=k>=1`, a fixed boundary vertex is a direct contact with probability

\[
s_k:=1-(1-p)^k,
\]

independently across boundary vertices. Therefore

\[
N_0\mid(K_0=k)\sim\operatorname{Bin}(n,s_k).
\tag{4.5}
\]

Put

\[
c_k:=1-(1-s_k)^n,
\qquad
\mu_k:=\mathbb E[N_0\mid C,K_0=k]
=\frac{ns_k}{c_k}.
\tag{4.6}
\]

### Lemma 4.1 (actual contact mean versus direct-contact mean)

Let

\[
M=\mathbb E[N\mid C],
\qquad
M_0=\mathbb E[N_0\mid C].
\]

Then

\[
\boxed{M\le rM_0.}
\tag{4.7}
\]

#### Proof

Fix `A` with `|A|=k>=1`. Split

\[
T=T_A+T_{A^c},
\]

according to whether the `H` endpoint lies in `A`. Since `C={N_0>0}` is exactly `{T_A>0}` on this slice,

\[
\mathbb E[T_A\mid C,A]
=
\frac{nkp}{c_k}.
\]

Using `s_k>=p`,

\[
\frac{nkp}{c_k}
=
\frac{kp}{s_k}\mu_k
\le k\mu_k.
\tag{4.8}
\]

The edges counted by `T_{A^c}` are independent of `C` conditional on `A`, so

\[
\mathbb E[T_{A^c}\mid C,A]
=n(r-k)p
\le(r-k)ns_k
\le(r-k)\mu_k.
\tag{4.9}
\]

Thus by (4.4),

\[
\mathbb E[N\mid C,A]
\le r\mu_k.
\]

Average over `A` under the conditional law given `C`. The corresponding average of `mu_k` is exactly `M_0`, proving (4.7). `square`

### Lemma 4.2 (bounded spread of the direct-contact conditional means)

For every `1<=k<=r`,

\[
\boxed{
\mu_1\le\mu_k\le r\mu_1.
}
\tag{4.10}
\]

Consequently

\[
\boxed{M_0\le r\mu_k\quad\text{for every }k>=1.}
\tag{4.11}
\]

#### Proof

The map

\[
s\mapsto\frac{ns}{1-(1-s)^n}
\]

is increasing on `(0,1]`. Indeed its derivative has the sign of

\[
1-(1-s)^n-ns(1-s)^{n-1}
=
1-nx^{n-1}+(n-1)x^n,
\qquad x=1-s,
\]

which is nonnegative on `[0,1]`.

Since `s_k` is increasing in `k`, this gives `mu_k>=mu_1`. Also

\[
s_k=1-(1-p)^k\le kp\le rp=rs_1,
\]

while `c_k>=c_1`; hence

\[
\frac{\mu_k}{\mu_1}
=
\frac{s_k}{s_1}\frac{c_1}{c_k}
\le r.
\]

This proves (4.10). Since `M_0` is a convex combination of the `mu_k` under the conditional law of `K_0` given `C`, `M_0<=max_k mu_k<=r mu_1<=r mu_k`, proving (4.11). `square`

### Theorem 4.3 (same-side complete-bipartite Flammant bound)

For `G=K_{r,n+1}` with root `o` and all `n` boundary vertices on the same bipartition side, under iid Bernoulli bond percolation of arbitrary parameter `p`, and under the **full original Flammant quantifiers** on the auxiliary event family, one has for every

\[
0<\varepsilon\le e^{-1}
\]

the uniform estimate

\[
\boxed{
R_{K_{r,n+1}}(\varepsilon)
\le
\frac{\varepsilon}{1-e^{-1}}
\left(
1+8r^2\log\frac1\varepsilon
\right).
}
\tag{4.12}
\]

In particular, for every fixed `r`,

\[
R_{K_{r,n+1}}(\varepsilon)\longrightarrow0
\]

uniformly in `n` and `p`. More generally the same conclusion holds along any family satisfying

\[
r(\varepsilon)^2\varepsilon\log(1/\varepsilon)\to0.
\tag{4.13}
\]

The smallest genuinely nonplanar shared-core family `K_{3,n+1}` therefore obeys

\[
\boxed{
R_{K_{3,n+1}}(\varepsilon)
\le
\frac{\varepsilon}{1-e^{-1}}
\left(
1+72\log\frac1\varepsilon
\right).
}
\tag{4.14}
\]

#### Proof

Fix `a>0`. From the inherited tail reduction (1.2),

\[
R
\le
\Pr(N\le aM\mid C)+\frac\varepsilon a.
\tag{4.15}
\]

Condition on `K_0=k>=1`. By (4.3), (4.7), and (4.11),

\[
\{N\le aM\}
\subseteq
\{N_0\le aM\}
\subseteq
\{N_0\le arM_0\}
\subseteq
\{N_0\le ar^2\mu_k\}.
\tag{4.16}
\]

Given `K_0=k` and `C`, `N_0` is a `Bin(n,s_k)` variable conditioned to be positive, with conditional mean `mu_k`. Therefore, whenever

\[
ar^2\le c_0/2,
\]

Lemma (1.3) gives

\[
\Pr(N\le aM\mid C,K_0=k)
\le
c_0^{-1}
\exp\!\left(-\frac{c_0}{8ar^2}\right).
\tag{4.17}
\]

The bound is independent of `k`, so it survives averaging over `K_0` under the law conditioned on `C`.

Let

\[
L=\log(1/\varepsilon)\ge1,
\qquad
 a=\frac{c_0}{8r^2L}.
\tag{4.18}
\]

Then `ar^2=c_0/(8L)<=c_0/2`, and the exponential in (4.17) is exactly `epsilon`. Substituting into (4.15),

\[
R
\le
\frac\varepsilon{c_0}
+
\frac{8r^2L}{c_0}\varepsilon,
\]

which is (4.12). `square`

### Scope and significance

Theorem 4.3 is not a bounded-`|B|` statement: `n` is arbitrary and the bound is uniform in `n`. It is not the C077 opposite-side theorem: here the root neighborhood is the hidden hub set `H`, while the boundary lies with the root on the other bipartition side, so boundary vertices can bridge hubs and create additional connections. It is genuinely nonplanar for `r>=3`, `n+1>=3`.

The theorem also explains why the high-`rho` counterexample search in method #23 did not immediately succeed on the smallest shared core. In this family the potentially huge number of hidden edges is not by itself the obstruction; the number `r` of root-side hub channels is the relevant parameter, and fixed `r` gives an explicit modulus.

## 5. What changed conceptually

Two facts now sit side by side.

1. **Recursive deletion of the root is exact at the epsilon level.** The kernels induced after forcing one root edge open remain decreasing and keep the same expectation budget. This yields (2.3) without any topology assumption.
2. **Raw branch count is not enough.** The common-gate construction (3.1)--(3.6) shows that the active-root-branch count can have a constant small-branch mode while its conditional mean diverges. Therefore any full recursive proof needs a richer state than `K`.

The complete-bipartite same-side theorem identifies one such richer state that does close: the direct-contact count `N_0`. It is a binomial statistic on each finite hub state, and the possible conditional means differ by only a factor `r`. This is precisely what blocks the pathological mixture from Section 3.

A plausible unrestricted recursive state would therefore have to track **branch boundary mass**, not merely branch existence. One candidate is a weighted branch statistic

\[
W=\sum_{i:X_i=1} w_i(\xi),
\]

where `w_i` measures a robust amount of boundary mass reachable through branch `i` and must satisfy three simultaneous properties: it lower-controls the actual contact count on `C`, its conditional means cannot have arbitrarily separated scales, and forcing root edge `i` open must preserve the `epsilon` budget in the recursive subproblem. C078 does not yet construct such a universal `W`.

## 6. Honest metric/status and next obligation

The strict source-wide metric does **not** move:

\[
U_F:1\longrightarrow1.
\]

The new complete-bipartite theorem is PARTIAL, and the root-link inequality is a reduction rather than closure. No source-level refutation was found.

Post-recovery-2 substantive unchanged count:

\[
1\longrightarrow2.
\]

Therefore one more substantive G0004 run with `U_F` unchanged reaches the third Section-I stuck episode. Under HARD policy there is no recovery 3/3: the next stuck episode must leave a handoff and rotate to an ownership-clear HARD OUTSIDE successor.

All thirty Section-B method numbers have now been exercised at least once on G0004 across C069--C078. If one final substantive run occurs before the mandatory handoff, it must reuse an old number only with a genuinely different route rather than replaying the previous argument. The natural final attack is the new weighted-root-branch state suggested above, using a refreshed triple distinct from #9/#19/#23.

## 7. Prior-art / source-status note

Queries used this run included the exact title, exact arXiv id `2609.03492`, `Conjecture 2.2`, `K_{3,n}`, and complete-bipartite / percolation combinations. The current arXiv abstract still states the arbitrary finite-graph claim as a conjecture and advertises the outer-face planar theorem. No later source-matching full solution or same-side complete-bipartite theorem was found in the bounded search. This is not proof of novelty and must not be represented as one.

## 8. Model / scheduler / permission reality

Actual model metadata available to this run identifies **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so reasoning level is **UNVERIFIED**. This is not GPT-6 maximum and is not represented as such.

The scheduler interface exposed to this worker still offers title, prompt, schedule, enablement and timing-mode controls; it exposes no bindable model-family selector, no reasoning-effort selector, and no authenticated runtime-model attestation. Enforcing GPT-6 maximum would require an authorized product/API/admin surface that actually exposes those fields and execution telemetry.

The historical P26 `You cannot modify this task` result remains an authorization-context issue. The legitimate workaround is the owning/admin-authorized scheduler context or platform support. Duplicating a task or bypassing permissions is not an acceptable substitute. This run made no scheduler, workflow, permission, email, Drive, public-posting, purchase, or shared-root mutation.

## ledger_delta

```json
{
  "worker": "R17",
  "target": "G0004 / Flammant Conjecture 2.2",
  "allocation": "HARD OUTSIDE",
  "status": "OPEN / PARTIAL",
  "metric": "U_F",
  "before": 1,
  "after": 1,
  "movement": "no movement",
  "post_recovery_2_unchanged_count_before": 1,
  "post_recovery_2_unchanged_count_after": 2,
  "recovery_count": "2/2 exhausted",
  "methods": [9, 19, 23],
  "new_results": [
    "exact root-link recursive moment inequality E[K m] <= R_{n-1}(epsilon) E[K]",
    "honest Bernoulli common-gate family showing root-branch lower-tail concentration can fail badly",
    "full-source-event quantitative theorem on same-side K_{r,n+1}: R <= epsilon/(1-e^-1) * (1 + 8 r^2 log(1/epsilon))"
  ],
  "source_verdict": "OPEN",
  "next_trigger": "one further substantive unchanged run causes third stuck episode and mandatory handoff/rotation"
}
```
