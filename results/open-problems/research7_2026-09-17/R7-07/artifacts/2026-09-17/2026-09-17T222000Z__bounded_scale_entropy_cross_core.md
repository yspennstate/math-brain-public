# G0011 artifact — bounded-ratio and bounded scale-entropy cross cores

Date: 2026-09-17 UTC / 2026-09-18 Asia/Jerusalem.
Owner: R7-07, native ID `6aabe8413f60819197825dd81ca138ae`.
Target: `G0011`, the Krivelevich–Samotij long-cycle conjecture as restated by Christoph–Morawski–Wigderson, arXiv:2608.19145v1.
Status of this artifact: **restricted theorem / PARTIAL**, not a proof of the full source conjecture. No novelty claim is made.

This note proves two cumulative statements needed by the current R7-07 reduction. First, the preceding exact-biregular cross-core theorem remains true under arbitrary but fixed degree ratios on both sides. Second, in the fully irregular cross core, any dyadic degree-pair cell which is a fixed fraction of both its row and its column can be peeled to such a bounded-ratio core. As a consequence, the remaining obstruction must have genuinely divergent *bidirectional conditional degree-scale entropy*; an exact one-parameter collision functional makes this obstruction quantitative.

## 1. Bounded-ratio cross-core theorem

### Theorem 1.1

Fix constants

`epsilon>0`, `r_0>0`, `s_0>0`, and `Lambda>=1`.

There exist `d_0=d_0(epsilon,r_0,s_0,Lambda)` and `gamma=gamma(epsilon,r_0,s_0,Lambda)>0` with the following property.

For every `d>=d_0`, let `J=(A,B;E)` be a finite bipartite graph for which there are numbers `R,S` satisfying

```text
R >= r_0 d^2,
S >= s_0 d,
R <= deg_J(a) <= Lambda R       for every a in A,
S <= deg_J(b) <= Lambda S       for every b in B.
```

Let `J_p` retain every incidence independently with

```text
p=(1+epsilon)/d.
```

Along every sequence of such instances with `|A|+|B| -> infinity`, `J_p` contains a simple cycle of length at least `gamma d` asymptotically almost surely.

No codegree, expansion, pseudorandomness, girth, or upper bound on `R/d^2` is assumed.

### Proof

Write

```text
m=|A|,   M=|B|,   e=e(J).
```

Degree comparison gives

```text
mR <= e <= m Lambda R,
MS <= e <= M Lambda S,
```

and hence

```text
M >= mR/(Lambda S).                                      (1.1)
```

We localize the `A` side at the scale of the `B` degrees. Put

```text
h=max(1,floor(S/d)).                                     (1.2)
```

If `h=1`, take the single block `U=A`. If `h>=2`, independently and uniformly color every vertex of `A` with one of `h` colors and write `U_j` for color class `j`.

Set

```text
a_0=min(s_0,1),
a=a_0/2,
b_0=4 Lambda.                                            (1.3)
```

For a fixed connector `b` and a fixed block `U_j`, the localized host degree

```text
t_{b,j}=|N_J(b) intersect U_j|
```

is binomial with mean `mu=deg_J(b)/h` when `h>=2`. Since `h=floor(S/d)` and `h>=2`,

```text
S/h >= d,
S/h <= 2d,
```

and therefore

```text
d <= mu <= 2 Lambda d.
```

When `h=1`, instead `S<2d`, so deterministically

```text
s_0 d <= t_{b,1}=deg_J(b) < 2 Lambda d.
```

Thus, by standard Chernoff bounds, for `h>=2`,

```text
P(t_{b,j} notin [a d,b_0 d]) <= delta_d,
delta_d := 2 exp(-a_0 d/12).                              (1.4)
```

Also, because every `b` has degree at least `S`, we have `m>=S`; hence for `h>=2`,

```text
m/h >= m d/S >= d.
```

A further Chernoff bound gives

```text
P(|U_j|>2m/h) <= exp(-d/3).                              (1.5)
```

For a fixed block, the expected number of connectors violating (1.4) is at most `delta_d M`. By Markov,

```text
P(number of bad connectors > sqrt(delta_d) M)
   <= sqrt(delta_d).                                      (1.6)
```

Choose `d_0` large enough that the right sides of (1.5) and (1.6) are small. Averaging over the coloring, there is a deterministic coloring for which at least `h/2` classes are *good*, meaning

```text
|U| <= 2m/h,
```

and at least `eta M` connectors, with `eta>=1/2`, have localized degree in `[ad,b_0d]`. For `h=1` the single block is good deterministically. In every case a good block satisfies the uniform size bound

```text
|U| <= 4 m d/S.                                          (1.7)
```

Indeed, for `h>=2`, `h>=S/(2d)`, and when `h=1`, `S<2d`.

Fix one good block `U` and its set `C_U` of at least `eta M` good connectors. Now expose percolation. For each `b in C_U`, let

```text
D_b=|N_{J_p}(b) intersect U|.
```

If `D_b<2`, select nothing. If `D_b>=2`, select one unordered pair of open neighbors uniformly from the `binom(D_b,2)` available pairs. Make these auxiliary choices independently over connectors and, when needed, independently over blocks. Let `G_U` be the simple graph on `U` consisting of all selected pairs, with duplicate pairs collapsed.

Crucially, one connector selects at most one pair *inside this block*. Hence every simple cycle of `G_U` has distinct connector witnesses and lifts to a simple cycle of twice the length in `J_p`.

For a connector with localized host degree `t in [ad,b_0d]`, put

```text
q_t=P(Bin(t,p)>=2).
```

For all sufficiently large `d`, the exactly-two term and `log(1-p)>=-2p` give

```text
q_t
 >= binom(t,2) p^2 (1-p)^(t-2)
 >= q_*,                                                (1.8)
```

where the positive constant

```text
q_* := [a^2(1+epsilon)^2/4] exp(-2b_0(1+epsilon))
```

depends only on the fixed parameters.

By exchangeability, every base pair `f subset N_J(b) intersect U` has unconditional selection probability

```text
r_{b,f}=q_t/binom(t,2) <= C_*/d^2,
C_*:=4/a^2.                                             (1.9)
```

For a pair `f subset U`, define its total selection load

```text
x_f=sum_b r_{b,f}.
```

A pair has at most `Lambda R` common connectors, because either endpoint has total `J`-degree at most `Lambda R`. Thus

```text
x_f <= L:=C_* Lambda R/d^2.                            (1.10)
```

On the other hand, summing connector-first yields

```text
sum_f x_f
 =sum_{b in C_U} q_{t_b}
 >= eta M q_*
 >= eta q_* mR/(Lambda S),                             (1.11)
```

where the last step is (1.1).

Let `I_f` indicate that pair `f` occurs in the simple graph `G_U`, and let `Z_U=e(G_U)`. Independence across connectors gives

```text
E I_f
 =1-prod_b(1-r_{b,f})
 >=1-exp(-x_f).                                        (1.12)
```

For `0<=x<=L`, concavity and the chord from `0` to `L` give

```text
1-exp(-x) >= [(1-exp(-L))/L] x.                       (1.13)
```

Using (1.10)--(1.13),

```text
E Z_U
 >= [1-exp(-L)]/L * eta q_* mR/(Lambda S)
 = eta q_* [1-exp(-L)] m d^2/(C_* Lambda^2 S).        (1.14)
```

Since `R>=r_0d^2`,

```text
L>=C_* Lambda r_0,
```

so `1-exp(-L)` is bounded below by a fixed positive constant. Consequently there is

```text
c_2=c_2(epsilon,r_0,s_0,Lambda)>0
```

such that

```text
E Z_U >= c_2 m d^2/S.                                 (1.15)
```

This is where the potentially unbounded magnitude of `R/d^2` cancels: very concentrated pair loads reduce the occupancy factor, but the number of connector opportunities increases in exactly the compensating proportion.

For distinct pairs `f,g`, a single connector cannot select both. Therefore

```text
P(I_f=0,I_g=0)
 =prod_b(1-r_{b,f}-r_{b,g})
 <=prod_b(1-r_{b,f})(1-r_{b,g})
 =P(I_f=0)P(I_g=0).
```

For Bernoulli indicators this is equivalent to

```text
Cov(I_f,I_g)<=0.
```

Hence

```text
Var Z_U <= E Z_U.                                      (1.16)
```

Chebyshev and (1.15) now give

```text
P(Z_U<(1/2)E Z_U)
 <=4/E Z_U
 <=4S/(c_2 m d^2)
 <=4/(c_2 d^2),                                       (1.17)
```

because `S<=m`.

On the success event, (1.7) and (1.15) imply

```text
average_degree(G_U) >= (c_2/4)d.                      (1.18)
```

Every graph of average degree `D` has a nonempty subgraph of minimum degree at least `D/2`; a longest-path argument then gives a cycle of length at least `D/2+1`. Thus `G_U` has a cycle of length at least `c_3d` for a fixed `c_3>0`, and this lifts to a simple cycle of length at least `2c_3d` in `J_p`.

It remains to make the probability statement uniform over all host-order sequences.

- If `d->infinity`, (1.17) tends to zero for a single good block.
- If `d` stays bounded but `h->infinity`, there are at least `h/2` disjoint good `A`-blocks. Their percolation variables are disjoint even if they share connector vertices, so the block-success events are independent. Choosing `d_0` so that the right side of (1.17) is below one, failure in all blocks tends to zero exponentially in `h`.
- If `d` and `h` stay bounded while `m->infinity`, the sharper bound `4S/(c_2md^2)` in (1.17) tends to zero because then `S` is bounded.
- Finally suppose `d,h,m` are all bounded while `|A|+|B|->infinity`. Then `M->infinity`. In a good block at least `eta M` connectors have a localized neighborhood `T` of cardinality in `[ad,b_0d]`. Only finitely many such subsets of the bounded block exist, so one neighborhood type `T` occurs for `L_T->infinity` connectors. Cyclically order the vertices of `T`, split these twin connectors into `|T|` disjoint growing groups, and assign one group to each consecutive pair. Since `p>0` is fixed in this bounded-`d` regime, each group contains a connector whose two assigned incidences both survive with probability tending to one. The groups give distinct connector witnesses for a simple cycle of length `2|T|>=2ad=Omega(d)`.

Every sequence has a subsequence in one of these regimes, so the failure probability must tend to zero along the original sequence. This proves Theorem 1.1. `QED`

## 2. A degree-scale transport lemma

We now return to an arbitrary irregular bipartite cross core `J=(A,B)` with only lower semidegree bounds

```text
deg_J(a) >= R_0 := r_0 d^2,
deg_J(b) >= S_0 := s_0 d.                               (2.1)
```

Partition the two sides by dyadic *total* degrees:

```text
A_i={a: 2^i R_0 <= deg_J(a) < 2^(i+1)R_0},
B_j={b: 2^j S_0 <= deg_J(b) < 2^(j+1)S_0}.             (2.2)
```

Write

```text
R_i=2^iR_0,  S_j=2^jS_0,
e_ij=e_J(A_i,B_j),
e_i=sum_j e_ij,
f_j=sum_i e_ij.
```

### Lemma 2.1 — balanced-cell peeling

Fix constants `alpha,beta>0`. If some cell `(i,j)` satisfies

```text
e_ij >= alpha e_i,
e_ij >= beta f_j,                                           (2.3)
```

then the cell contains a nonempty subgraph `H=(A',B')` with more than `e_ij/2` edges and

```text
(alpha/4) R_i <= deg_H(a) < 2R_i       for all a in A',
(beta /4) S_j <= deg_H(b) < 2S_j       for all b in B'.     (2.4)
```

In particular the two sidewise degree ratios are bounded by `8/alpha` and `8/beta`.

#### Proof

Start with the cell graph `J[A_i,B_j]`. Repeatedly delete

```text
an A_i vertex of current cell-degree < (alpha/4)R_i,
or a B_j vertex of current cell-degree < (beta/4)S_j.
```

Since every `a in A_i` has total degree at least `R_i`,

```text
|A_i| R_i <= e_i.
```

Thus all deletions made on the `A` side remove altogether fewer than

```text
(alpha/4)|A_i|R_i
 <= (alpha/4)e_i
 <= e_ij/4.                                               (2.5)
```

Similarly `|B_j|S_j<=f_j`, so all `B`-side deletions remove fewer than `e_ij/4` edges. Therefore more than `e_ij/2` cell edges survive. Every surviving vertex satisfies the stated lower threshold, while the dyadic definition (2.2) supplies the upper bounds in (2.4). `QED`

### Corollary 2.2

For fixed `alpha,beta>0`, any sequence of balanced cells satisfying (2.3), whose surviving cell order tends to infinity, has an `Omega(d)` simple cycle after percolation at `p=(1+epsilon)/d` a.a.s.

Indeed, apply Theorem 1.1 with

```text
r_0'=(alpha/4)r_0,
s_0'=(beta /4)s_0,
Lambda=max(8/alpha,8/beta).
```

This is the exact transport formulation of the irregular-to-biregular transfer: a cell need not contain a fixed fraction of *all* cross edges. It is enough that the same cell captures fixed conditional fractions from both endpoint degree scales.

## 3. B28: the only remaining irregular obstruction has divergent bidirectional scale entropy

Normalize the dyadic cell matrix by total cross-edge mass `E=e(J)`:

```text
P_ij=e_ij/E,
P_i =e_i/E,
Q_j =f_j/E.                                               (3.1)
```

Choose an incidence uniformly from the `E` host incidences and let `(I,J)` be the dyadic degree-bin indices of its endpoints. Define the row and column conditional weights

```text
alpha_ij=P_ij/P_i=P(J=j | I=i),
beta_ij =P_ij/Q_j=P(I=i | J=j).                           (3.2)
```

The balanced-cell condition of Lemma 2.1 is precisely

```text
alpha_ij >= alpha,
beta_ij  >= beta.                                         (3.3)
```

Define the *bidirectional conditional scale entropy*

```text
H_bi
 := H(J|I)+H(I|J)
  = sum_{ij} P_ij[-log alpha_ij-log beta_ij].              (3.4)
```

### Theorem 3.1 — bounded conditional scale entropy closes the cross-core branch

Consider a sequence of the G0011 irregular cross cores from the cumulative R7-07 reduction, so in addition to (2.1) there is a fixed `c>0` with total cross-edge mass

```text
E >= c n d,                                               (3.5)
```

where `n` is the order of the ambient host and `n->infinity`.

If

```text
sup H_bi < infinity,                                      (3.6)
```

then percolation at `p=(1+epsilon)/d` contains a simple cycle of length `Omega(d)` a.a.s. in this cross core.

#### Proof

Suppose `H_bi<=H_0`. Under the edge-size-biased law `P_ij`, the nonnegative random variable

```text
X_ij=-log(alpha_ij beta_ij)
```

has expectation at most `H_0`. Markov's inequality gives

```text
P(X_ij <= 2H_0) >= 1/2.                                  (3.7)
```

On this event, because both conditional probabilities lie in `[0,1]`,

```text
alpha_ij >= exp(-2H_0),
beta_ij  >= exp(-2H_0).                                  (3.8)
```

Thus at least half the cross-edge mass lies in cells satisfying Lemma 2.1 with the same fixed constants

```text
alpha=beta=exp(-2H_0).                                   (3.9)
```

There are at most `O((log n)^2)` occupied dyadic degree cells, because every degree is at most `n-1`. Hence some balanced cell contains at least

```text
Omega(E/(log n)^2)=Omega(nd/(log n)^2) -> infinity       (3.10)
```

edges, using (3.5). Its peeled subgraph therefore has order tending to infinity. Corollary 2.2 applies and gives the required `Omega(d)` cycle a.a.s. `QED`

Consequently, a genuinely unresolved sequence in this cross branch must satisfy

```text
H(J|I)+H(I|J) -> infinity.                               (3.11)
```

This is substantially sharper than merely saying that many dyadic degree bins are present. For example, a graph may use arbitrarily many matched degree scales while each scale talks essentially only to its corresponding scale; then both conditional entropies stay small, and Theorem 3.1 still closes the branch. The remaining obstruction requires increasingly diffuse *cross-scale mixing seen from both endpoints of a typical incidence*.

## 4. B5: a parameter whose derivative is the blocker

The entropy obstruction has a useful exact one-parameter form. For `q>=1`, define

```text
Phi(q)
 := sum_{ij} P_ij (alpha_ij beta_ij)^(q-1).              (4.1)
```

Then

```text
Phi(1)=1,                                                 (4.2)
```

and differentiating at `q=1` gives

```text
Phi'(1)
 =sum_{ij}P_ij log(alpha_ij beta_ij)
 =-[H(J|I)+H(I|J)]
 =-H_bi.                                                  (4.3)
```

At `q=2`,

```text
Phi(2)
 =sum_{ij} P_ij alpha_ij beta_ij
 =sum_{ij} P_ij^3/(P_iQ_j).                              (4.4)
```

This quantity is a bidirectional collision statistic for the dyadic transport matrix.

### Proposition 4.1 — positive collision mass closes the branch

If along a sequence

```text
liminf Phi(2) > 0,                                       (4.5)
```

then the cross-core branch is solved at the source probability.

#### Proof

Let `Y=alpha_IJ beta_IJ in [0,1]` under the law `P`. If `E Y=Phi(2)>=c>0`, then

```text
P(Y>=c/2) >= (c/2)/(1-c/2) >= c/2.                       (4.6)
```

On `Y>=c/2`, each of `alpha_IJ` and `beta_IJ` is at least `c/2`, because both are at most one. Thus a fixed positive fraction of cross-edge mass lies in balanced cells with fixed constants. There are only `O((log n)^2)` dyadic cells, so one such balanced cell has a growing number of edges by (3.5). Lemma 2.1 and Theorem 1.1 finish. `QED`

Therefore every sequence that survives all the theorems in this artifact must satisfy the exact scalar degeneration

```text
Phi(2) -> 0.                                             (4.7)
```

Moreover Jensen's inequality applied to `Y` gives

```text
H_bi=E[-log Y] >= -log E[Y] = -log Phi(2).               (4.8)
```

Hence (4.7) forces the entropy divergence (3.11). The derivative identity (4.3) and endpoint statistic (4.4) put the irregularity blocker into a single parameterized family rather than an informal statement about many degree scales.

## 5. What is and is not proved

Proved here:

1. Exact biregularity is unnecessary; any fixed two-sided degree ratio in the cross core still gives an `Omega(d)` cycle a.a.s. at `p=(1+epsilon)/d`.
2. Any dyadic degree-pair cell carrying fixed conditional fractions of both its row and its column peels to such a bounded-ratio core.
3. In the cumulative G0011 cross-core reduction, bounded `H(J|I)+H(I|J)` closes the branch.
4. More sharply, `liminf Phi(2)>0` closes the branch; therefore a surviving obstruction must have `Phi(2)->0` and divergent bidirectional conditional scale entropy.

Not proved here:

- There is no universal lower bound on `Phi(2)` derived from the present semidegree hypotheses.
- The diffuse regime `Phi(2)->0` is not eliminated.
- The full G0011 source conjecture is therefore **not** proved, and the fixed source metric `K_long` does not move in this artifact.

The next mathematical problem is now sharply stated: exploit the original cross-core semidegree and edge-mass inequalities to rule out, or directly solve, the multiscale transport regime in which a typical incidence sees increasingly many degree scales in both directions and `Phi(2)->0`.