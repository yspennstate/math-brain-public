# G0011 artifact — one-sided witness projection eliminates the multiscale-A laboratory

Date: 2026-09-18 UTC.
Target: `G0011` (Krivelevich–Samotij long-cycle conjecture as restated by Christoph–Morawski–Wigderson).
Scope: **restricted cross-core theorem / PARTIAL for the source**.
Methods executed: **B8 / B20 / B27**.

## 1. New theorem

The final-recovery diagnosis isolated a bipartite laboratory in which the `B` side is one-scale but the `A` side may be arbitrarily multiscale. The point of this artifact is that the `A`-multiscale obstruction is not real: one can eliminate it without any upper bound on the `A` degrees.

### Theorem 1 — one-sided bounded-scale witness theorem

Fix constants

```text
c>0, r>0, s_0>0, Lambda>=1.
```

For all sufficiently large `d`, let `J=(A,B)` be a finite simple bipartite graph satisfying

```text
deg_J(a) >= r d^2                         for every a in A,      (1.1)
S <= deg_J(b) <= Lambda S                  for every b in B,      (1.2)
S >= s_0 d.                                                        (1.3)
```

There is **no upper bound at all** on the degrees on the `A` side. The scale `S` is also allowed to be much larger than `d`.

Let

```text
p=c/d
```

(for large `d`, so `p<=1`) and form the independent bond-percolated graph `J_p`.

Then there exists a constant

```text
gamma=gamma(c,r,s_0,Lambda)>0
```

such that, along every sequence of such graphs for which `|A|+|B| -> infinity`, `J_p` contains a simple cycle of length at least `gamma d` with probability tending to one.

In particular, the theorem applies to the exact final-recovery laboratory

```text
deg(b)=s d,
deg(a)>=r d^2,
```

with arbitrarily many `A`-degree classes `k=k(d)->infinity`, arbitrary values of those degrees, and without either of the diagnostic assumptions `max_i R_i/M->0` or `Phi(2)->0`.

The rest of the artifact proves the theorem from first principles.

---

## 2. Auxiliary representative projection

A simple cycle in a bipartite graph may be regarded as a cycle on `A` whose consecutive pairs have pairwise distinct witnesses in `B`. We build that distinctness into the auxiliary object from the start.

For the moment suppose a `B`-vertex `b` has a specified set `U_b subseteq N_J(b)` of host neighbors. Expose the percolation edges from `b` to `U_b`. If at least two of these edges are open, choose **one** unordered pair uniformly from the open neighbors and call it `e_b`; otherwise set `e_b=empty`.

If `t=|U_b|`, let

```text
theta_t = P(Bin(t,p)>=2).
```

By symmetry, for every host pair `e subseteq U_b`,

```text
P(e_b=e)=theta_t / binom(t,2).                            (2.1)
```

Indeed, conditional on the event that a pair is selected, all `binom(t,2)` host pairs have equal probability and exactly one is selected.

### Lemma 2.1 — cycle lifting

Let `Gamma` be any simple graph on a subset of `A` obtained by taking the union of pairs selected by the `B`-vertices, with each `b` selecting at most one pair **inside the particular block containing the cycle under consideration**. Every simple cycle

```text
a_1 a_2 ... a_l a_1
```

of `Gamma` lifts to the simple bipartite cycle

```text
a_1 b_1 a_2 b_2 ... a_l b_l a_1
```

in `J_p`, of length `2l`.

#### Proof

For each projected cycle edge `{a_i,a_{i+1}}`, choose a `B`-vertex `b_i` that selected precisely that pair. Distinct projected edges cannot have the same selecting `B`-vertex, because one `B`-vertex selected at most one pair inside the block. Hence the `b_i` are distinct. The `a_i` are distinct because the projected cycle is simple. Both percolation edges incident to each selected pair are open by construction. `QED`

This removes the Hall/SDR issue from the cycle that is eventually used.

---

## 3. B8 — discretize the `B` scale, not the `A` scales

The diagnosis proposed discretizing the `k` `A`-degree classes. The useful discretization is different: localize every `B`-vertex to `Theta(d)` host neighbors while leaving every `A`-degree completely untouched.

Set

```text
h = ceil(S/d).                                            (3.1)
```

Color the vertices of `A` independently and uniformly with colors `1,...,h`. For a `B`-vertex `b` and a color `j`, put

```text
t_{b,j}=|N_J(b) cap A_j|.                                (3.2)
```

Fix an incidence `ab` and condition on the color of `a` being `j`. Then

```text
t_{b,j}=1+Bin(deg_J(b)-1,1/h).                           (3.3)
```

Because

```text
S <= deg_J(b) <= Lambda S,
h = ceil(S/d),
S >= s_0 d,
```

there are constants

```text
0<alpha<beta<infinity,
zeta>0                                                     (3.4)
```

depending only on `s_0,Lambda` such that, uniformly in every incidence `ab`,

```text
P(alpha d <= t_{b,color(a)} <= beta d | color(a))
    >= 1-2 exp(-zeta d).                                  (3.5)
```

For completeness, one may take constants after observing

```text
(deg(b)-1)/h >= c_1 d,
(deg(b)-1)/h <= Lambda d
```

for some `c_1=c_1(s_0)>0` and all large `d`, then apply the standard multiplicative Chernoff bound to (3.3).

Call an incidence `ab` **localized for a** when the block containing `a` satisfies the interval in (3.5). For a fixed `a`, let `Y_a` be the number of its incident `B`-vertices that are not localized for `a`. Linearity of expectation gives

```text
E_color Y_a <= 2 exp(-zeta d) deg_J(a).                  (3.6)
```

No independence among the terms of `Y_a` is needed. Markov gives

```text
P_color(Y_a > deg_J(a)/2) <= 4 exp(-zeta d).             (3.7)
```

Call `a` **color-good** when at least half its incident `B`-vertices are localized for it. Therefore

```text
E_color #{a: a is not color-good}
   <= 4 exp(-zeta d)|A|.                                 (3.8)
```

For sufficiently large `d`, the right-hand coefficient is below `1/4`. Hence there exists a deterministic coloring of `A` for which at least `3|A|/4` vertices are color-good. Fix such a coloring for the rest of the proof.

The important point is that this coloring uses only the single `B` degree scale `S`; it does **not** use, truncate, or pigeonhole the `A` degrees. Consequently the argument is uniform in the number `k` of `A`-degree classes.

---

## 4. Pair selection inside every color block

For every color `j`, expose only the percolation edges between `B` and `A_j`. These edge sets are disjoint across colors. If

```text
alpha d <= t_{b,j} <= beta d,                            (4.1)
```

then, when `b` has at least two open neighbors in `A_j`, choose one open pair uniformly and insert it into a simple projected graph `Gamma_j` on `A_j`.

A single `b` is allowed to make a selection in several different color blocks. This causes no lifting problem: the graph

```text
Gamma = disjoint union_j Gamma_j                         (4.2)
```

has no edges between color classes, so any cycle of `Gamma` lies in one single `Gamma_j`; inside that block each `b` selected at most one pair and Lemma 2.1 applies.

The percolation edge sets used by different color blocks are disjoint, so the random constructions of the `Gamma_j` are independent across `j` once the host coloring is fixed.

### Uniform pair-selection lower bound

For every localized block degree `t in [alpha d,beta d]`,

```text
theta_t=P(Bin(t,p)>=2).
```

There is a constant `theta_*>0`, depending only on `alpha,beta,c`, such that for all large `d`,

```text
theta_t >= theta_*.                                     (4.3)
```

For example, the exactly-two term gives

```text
theta_t
 >= binom(t,2)(c/d)^2(1-c/d)^(t-2),                     (4.4)
```

whose infimum over `t in [alpha d,beta d]` stays positive for large `d`.

By (2.1), every fixed host pair inside a localized `b` is therefore selected with probability at least

```text
q := q_0/d^2                                             (4.5)
```

for some `q_0=q_0(alpha,beta,c)>0`.

---

## 5. B20 — exact collision analysis of the natural greedy representative process

The natural one-pair-per-witness process can fail only if many witnesses repeatedly choose the same projected pair. The following calculation shows that even the **worst possible codegree concentration** cannot reduce the one-sided model below `Theta(d)` distinct projected degree.

Fix a color-good vertex `a`, lying in block `A_j`. Let

```text
R_a = number of localized B-neighbors of a in block j.
```

By color-goodness and (1.1),

```text
R_a >= deg_J(a)/2 >= (r/2)d^2.                          (5.1)
```

For each other vertex `u in A_j`, let

```text
c_u = #{ localized b : a,u in N_J(b) cap A_j }.         (5.2)
```

Two deterministic facts hold:

```text
0 <= c_u <= R_a,                                        (5.3)
```

and, because every localized `b` containing `a` has at least `alpha d` vertices in this color block,

```text
sum_u c_u
 = sum_{localized b containing a}(t_{b,j}-1)
 >= R_a(alpha d-1).                                     (5.4)
```

Let `I_u` be the indicator that at least one localized witness selects the pair `{a,u}`. Since each relevant witness selects that pair with probability at least `q=q_0/d^2`, independently across distinct witnesses,

```text
E I_u >= 1-(1-q)^{c_u}.                                 (5.5)
```

Set

```text
f(x)=1-(1-q)^x.
```

The function `f` is increasing, concave, and `f(0)=0`. Therefore for `0<=x<=R_a`, the chord inequality gives

```text
f(x) >= (x/R_a) f(R_a).                                 (5.6)
```

Summing (5.5), then using (5.4)-(5.6),

```text
E deg_Gamma(a)
 >= sum_u f(c_u)
 >= (f(R_a)/R_a) sum_u c_u
 >= (alpha d-1) f(R_a).                                 (5.7)
```

By (5.1),

```text
f(R_a)
 >= 1-(1-q_0/d^2)^{(r/2)d^2}
 >= 1-exp(-q_0r/2).                                     (5.8)
```

Hence there exists

```text
kappa=kappa(c,r,s_0,Lambda)>0                           (5.9)
```

such that every color-good `a` satisfies

```text
E deg_Gamma(a) >= kappa d.                              (5.10)
```

This is the exact answer to the B20 greedy-stall question in the one-sided model. Concentrating all codegree mass as aggressively as the simple graph allows only pushes the vector `(c_u)` toward the extreme point with roughly `alpha d` fully loaded partner bins. Each fully loaded bin is then hit with fixed positive probability, so the number of distinct partners remains linear in `d`. There is **no `1/k` loss** from the number of `A`-degree scales.

---

## 6. Negative correlation of occupied projected pairs

Let `mathcal P` be the set of all unordered `A`-pairs lying within one color class. For `e in mathcal P`, let `I_e` indicate that at least one eligible `B`-vertex in that color block selected `e`.

### Lemma 6.1 — pair occupancies are pairwise negatively correlated

For distinct projected pairs `e!=f`,

```text
Cov(I_e,I_f) <= 0.                                      (6.1)
```

#### Proof

For each eligible block-witness `(b,j)`, write

```text
x_{b,e}=P((b,j) selects e),
x_{b,f}=P((b,j) selects f).
```

The two outcomes are mutually exclusive for the same `(b,j)`. Independence across `b` and across disjoint color-block edge sets gives

```text
P(I_e=0,I_f=0)
 = product_{b,j}(1-x_{b,e}-x_{b,f})
 <= product_{b,j}(1-x_{b,e})(1-x_{b,f})
 = P(I_e=0)P(I_f=0).                                    (6.2)
```

Expanding the probabilities that both indicators equal one yields

```text
P(I_e=1,I_f=1) <= P(I_e=1)P(I_f=1),
```

which is (6.1). `QED`

Let

```text
X=e(Gamma)=sum_{e in mathcal P} I_e.                    (6.3)
```

Lemma 6.1 gives

```text
Var(X) <= sum_e Var(I_e) <= E X.                         (6.4)
```

---

## 7. Linear projected average degree and a long cycle

At least `3|A|/4` vertices are color-good. Summing (5.10) over those vertices,

```text
2 E X
 = sum_{a in A} E deg_Gamma(a)
 >= (3/4)|A| kappa d.                                   (7.1)
```

Hence

```text
E X >= (3kappa/8)|A|d.                                  (7.2)
```

Chebyshev and (6.4) imply

```text
P(X < (1/2)E X)
 <= 4 Var(X)/(E X)^2
 <= 4/E X
 <= 32/(3kappa |A|d).                                   (7.3)
```

On the complementary event,

```text
e(Gamma)=X >= (3kappa/16)|A|d,                          (7.4)
```

so the average degree of the disjoint union `Gamma` is at least

```text
(3kappa/8)d.                                             (7.5)
```

Because `Gamma` is the disjoint union of the color graphs `Gamma_j`, at least one color graph has average degree at least `(3kappa/8)d`.

Use the standard deterministic pruning lemma: every finite graph of average degree at least `D` contains a nonempty subgraph of minimum degree at least `D/2`. Applying it inside that color graph gives minimum degree at least

```text
(3kappa/16)d.                                            (7.6)
```

A longest-path argument then gives a simple projected cycle of length at least

```text
(3kappa/16)d + 1.                                       (7.7)
```

By Lemma 2.1, this lifts to a simple cycle of `J_p` of length at least

```text
(3kappa/8)d.                                             (7.8)
```

Thus one may take, for example,

```text
gamma = 3kappa/16                                       (7.9)
```

after harmlessly weakening the constant.

Whenever either `d->infinity` or `|A|->infinity`, the failure probability in (7.3) tends to zero.

---

## 8. The fixed-`d`, bounded-`A` tail of the a.a.s. quantifier

The source formulation takes `|G|->infinity`, so one must also cover sequences on which `d` and `|A|` remain bounded while `|B|->infinity`.

In this case `S<=|A|` is bounded, and there are only finitely many possible neighborhoods `N_J(b) subseteq A`. Some exact neighborhood type

```text
T subseteq A,
|T|>=S>=s_0d,                                           (8.1)
```

therefore occurs for `k->infinity` distinct `B`-vertices along a subsequence.

For each fixed pair `e subseteq T`, every such twin witness selects `e` with one fixed probability

```text
q_T>0                                                    (8.2)
```

after percolation and representative choice. The twin witnesses are independent. Hence

```text
P(no twin selects e)=(1-q_T)^k -> 0.                    (8.3)
```

There are only finitely many pairs of `T`, so a union bound shows that the projected graph contains the full clique `K_T` with probability tending to one. For large enough `d_0`, `|T|>=3`, and `K_T` contains a cycle of length `|T|>=s_0d`. Lemma 2.1 lifts it to a bipartite cycle of length at least `2s_0d`.

Together with Section 7, this proves Theorem 1 along every host-order-divergent sequence.

---

## 9. B27 — swap the witness quantifier

The historical obstruction was phrased as follows: first find a projected cycle, then prove that its edges admit pairwise distinct `B` representatives. That creates a Hall/SDR problem.

The proof above reverses the order in a way that preserves the source event.

For each realized percolated graph `H=J_p`, let `R(H)` be the finite family of representative maps that, in each relevant color block, choose one open pair from a witness having at least two open neighbors. Sample `rho in R(H)` by the uniform local rule above and let `Gamma_rho` be the resulting projected graph.

The joint calculation proves

```text
P_{H,rho}(Gamma_rho has an Omega(d) cycle) -> 1.        (9.1)
```

But whenever `Gamma_rho` has such a cycle, `H` itself has the lifted bipartite cycle. Therefore

```text
P_H(H has an Omega(d) cycle)
 >= P_{H,rho}(Gamma_rho has an Omega(d) cycle)
 -> 1.                                                   (9.2)
```

Thus one never needs to certify Hall after a cycle is found. Auxiliary random representatives are chosen after the open neighborhoods are known, and success of one representative map is already enough for the existential source event.

This is the B27 quantifier swap in exact form.

---

## 10. Corollary for the final-recovery `k`-class model

Recall the exact one-sided diffuse laboratory from the preceding stuck diagnosis:

```text
B is S=s d regular,
A=A_1 union ... union A_k,
deg(a)=R_i>=r d^2 on A_i,
k=k(d)->infinity,
|A_i|R_i=|B|S/k,
```

possibly with

```text
Phi(2)=1/k->0,
H(J|I)+H(I|J)=log k->infinity,
max_i R_i/|B|->0,
stable-rank -> infinity.
```

Theorem 1 applies with `Lambda=1` and does not use `k`, the `R_i`, `Phi`, the low-product limit, or stable rank. Hence this entire laboratory has an `Omega(d)` cycle a.a.s. at `p=c/d` for every fixed `c>0` (and therefore at the source value `c=1+epsilon`).

So the four previously isolated degenerations can coexist in a **solved** family. They diagnose where the bounded-cell proof stops; they are not themselves a counterexample mechanism.

The surviving obstruction must involve genuine multiscale behavior on the **witness/B side**, not merely arbitrary degree dispersion on `A`.

---

## 11. A useful structural corollary: fixed positive mass on one `B` scale is impossible in a counterexample

Return to the cumulative cross core with

```text
deg_J(a)>=r_0d^2,
deg_J(b)>=s_0d.
```

Dyadically bin `B` by its total `J`-degree:

```text
B_j={b:S_j<=deg_J(b)<2S_j},
E_j=e(A,B_j),
Q_j=E_j/E.                                               (11.1)
```

### Corollary 11.1

If there exists a fixed `delta>0` and an infinite subsequence on which

```text
Q_j >= delta                                             (11.2)
```

for some degree bin `j` (which may vary with the graph), then the cross core is source-solvable on that subsequence.

#### Proof

Let `m=|A|`. Since every `A` vertex has degree at least `r_0d^2`,

```text
E/m >= r_0d^2,
E_j/m >= delta r_0d^2.                                  (11.3)
```

Inside `J[A,B_j]`, repeatedly delete

```text
A-vertices of degree < E_j/(4m)
```

or

```text
B_j-vertices of degree < S_j/4.
```

If every edge disappeared, all `A` deletions would remove fewer than `E_j/4` edges. Also `|B_j|<=E_j/S_j`, so all `B` deletions would remove fewer than

```text
|B_j|S_j/4 <= E_j/4.                                    (11.4)
```

That cannot account for all `E_j` edges. A nonempty subgraph remains with

```text
min_A degree >= E_j/(4m) >= (delta r_0/4)d^2,
S_j/4 <= B-degree < 2S_j.                               (11.5)
```

The `B` degrees have ratio at most `8` and lower scale at least `(s_0/4)d`. Theorem 1 applies. `QED`

Consequently every still-unresolved cross-core sequence must satisfy

```text
max_j Q_j -> 0,                                         (11.6)
```

and hence also

```text
sum_j Q_j^2 -> 0,
H(B-scale) -> infinity.                                 (11.7)
```

This is a strictly more targeted residual condition than the previous bidirectional conditional-entropy degeneration: the witness-side degree marginal itself must escape through an unbounded number of scales.

---

## 12. What is and is not proved

### Proved in this artifact

1. The exact one-sided diffuse final-recovery laboratory is source-solvable.
2. More generally, `A` may have completely arbitrary degrees above `r d^2`; only the `B` side must lie in one fixed multiplicative degree window, at any scale `S>=s_0d`.
3. The proof is uniform in the number of `A`-degree scales and in arbitrary codegree overlap.
4. The Hall/SDR witness problem disappears by auxiliary representative randomization and cycle lifting.
5. Any unresolved cumulative cross core must have vanishing incidence mass in every single fixed-width dyadic `B`-degree scale: `max_j Q_j->0`.

### Not proved

1. The full arbitrary-average-degree source conjecture is **not** closed.
2. The frozen metric remains `1 <= K_long <= 2`.
3. The remaining cross-core case permits `B`-incidence mass to drift over an unbounded number of degree scales, with `max_jQ_j->0`; this artifact does not glue those scales.
4. No novelty claim follows from a bounded literature search.

The correct status is therefore **PARTIAL / source OPEN**.

---

## 13. Method outcomes

### B8 — discretize

**Success.** Localizing only the `B` scale into `Theta(d)`-sized color blocks produces constants independent of the number `k` of `A` scales. The one-sided `k->infinity` model is solved uniformly.

### B20 — why the greedy algorithm fails

**Success in the one-sided model.** The exact occupancy inequality (5.7) shows that even maximally concentrated codegrees leave `Omega(d)` distinct projected degree. Pair occupancy is negatively correlated, so the projected graph has `Omega(|A|d)` distinct edges with high probability. There is no greedy-stall obstruction left in this class.

### B27 — swap quantifiers

**Success.** Choose representatives from the fully exposed open neighborhoods as auxiliary randomness and find the cycle afterward. Joint success implies the original percolated graph contains the lifted cycle, eliminating the need for a post-cycle Hall assignment.

The new blocker is therefore not one-sided multiscale `A` geometry. It is the genuinely multiscale `B`-witness marginal (11.6).