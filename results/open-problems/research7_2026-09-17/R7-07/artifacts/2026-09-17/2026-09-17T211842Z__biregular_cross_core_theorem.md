# Biregular cross-core theorem for G0011

Date: 2026-09-17 UTC.
Track: R7-07 / G0011.
Status: proved restricted theorem; **PARTIAL** relative to the full average-degree source conjecture.

## Theorem

Fix `epsilon>0` and `theta>0`. There are constants `d_0=d_0(epsilon,theta)` and `gamma=gamma(epsilon,theta)>0` with the following property.

Let `J=(A,B;E)` range over finite simple bipartite graphs that are exactly `(R,S)`-biregular, meaning every `a in A` has degree `R` and every `b in B` has degree `S`. Let `d>=d_0` satisfy

```text
R >= d^2/2,
S >= theta d/16.
```

Retain every incidence independently with probability

```text
p=(1+epsilon)/d.
```

For every sequence of such graphs with `|A|+|B| -> infinity`, the percolated graph `J_p` contains, asymptotically almost surely, a simple cycle of length at least `gamma d`.

No codegree, pseudorandomness, expansion, or bounded-degree-ratio hypothesis is assumed.

## Proof

Write `m=|A|` and `M=|B|`. Biregularity gives

```text
mR=MS.                                              (1)
```

We prove the result by a deterministic localization, a randomized one-pair-per-witness projection, an occupancy estimate that is uniform over every codegree profile, and finally an amplification argument.

### 1. A deterministic localization into A-blocks

Set

```text
h=max(1,floor(S/d)).
```

If `h=1`, use the single block `U_1=A`. Suppose `h>=2`. Randomly color each vertex of `A` independently and uniformly with one of `h` colors, and let `U_j` be color class `j`.

For a fixed connector `b in B` and color `j`,

```text
t_{b,j}:=|N_J(b) intersect U_j| ~ Bin(S,1/h),
mu:=S/h.
```

Since `h=floor(S/d)>=2`,

```text
d <= mu <= 2d.
```

If `h=1`, then `theta d/16 <= S < 2d`. Hence in every case, with

```text
a0:=min(1,theta/16),
a:=a0/2,
beta:=4,
```

a standard Chernoff bound gives, for `h>=2`,

```text
P( t_{b,j} notin [a d,beta d] ) <= delta_d,
delta_d:=2 exp(-c_0 d)                         (2)
```

for a constant `c_0=c_0(theta)>0`. Also `m>=S`, so `m/h>=S/h>=d`, and

```text
P( |U_j|>2m/h ) <= exp(-c_1 d).                 (3)
```

For a fixed `j`, the expected number of connectors failing (2) is at most `delta_d M`. By Markov,

```text
P( more than sqrt(delta_d) M connectors fail ) <= sqrt(delta_d).
```

Choose `d_0` so large that `sqrt(delta_d)+exp(-c_1d)<1/4`. Then a random color class is, with probability at least `3/4`, simultaneously such that

```text
|U_j| <= 2m/h                                      (4)
```

and at least

```text
eta M,  eta:=1-sqrt(delta_d) >= 1/2,              (5)
```

connectors `b` satisfy

```text
a d <= t_{b,j} <= beta d.                         (6)
```

Therefore, by averaging over the random coloring, there exists a deterministic coloring for which at least `h/2` classes satisfy (4)--(6). Fix such a coloring. Call those classes good.

The elementary choice of `h` also gives, for every good class,

```text
|U_j| <= 4 m d/S.                                 (7)
```

Indeed, if `h=1`, then `S<2d`; if `h>=2`, then `h>=S/(2d)`.

### 2. One-pair-per-witness projection inside a good block

Fix a good block `U=U_j`. Use only the connectors satisfying (6); call their set `B_U`, so `|B_U|>=eta M`.

After bond percolation, for each `b in B_U` let

```text
D_b:=|N_{J_p}(b) intersect U|.
```

If `D_b<2`, do nothing. If `D_b>=2`, introduce an auxiliary independent random choice and select one unordered pair uniformly from the `C(D_b,2)` open pairs in `N_{J_p}(b) intersect U`.

Let `G_U` be the simple graph on `U` obtained by keeping every selected pair once, even if several connectors selected the same pair.

Crucially, every connector selects at most one pair in this block. Consequently every simple cycle of `G_U` uses distinct connectors and therefore lifts to a simple cycle of twice the length in `J_p`.

For `t=t_{b,j}` satisfying (6), define

```text
q_t=P(Bin(t,p)>=2).
```

For sufficiently large `d`, `p<=1/2`. Using only the probability of exactly two successes,

```text
q_t >= C(t,2) p^2 (1-p)^(t-2)
    >= q_*,
q_*:= [a^2(1+epsilon)^2/4] exp(-2 beta(1+epsilon)) >0.      (8)
```

By symmetry, conditional on selecting a pair, every base pair inside `N_J(b) intersect U` is equally likely. Thus for a fixed pair `e` supported by `b`,

```text
r_{b,e}:=P(b selects e)=q_t/C(t,2)
                       <= C_*/d^2,
C_*:=4/a^2.                                          (9)
```

Selections made by different `b` are independent.

### 3. Uniform occupancy lower bound: arbitrary overlap is harmless at this scale

For an unordered pair `e subset U`, put

```text
x_e:=sum_{b in B_U} r_{b,e}.
```

A pair can be supported by at most `R` connectors, because each endpoint has `J`-degree `R`. Hence from (9)

```text
0 <= x_e <= L:=C_* R/d^2.                           (10)
```

On the other hand, summing over pairs first within each connector gives

```text
sum_e x_e = sum_{b in B_U} q_{t_b}
          >= eta M q_*.                             (11)
```

Let `I_e` be the indicator that pair `e` appears in `G_U`. Independence across connectors and `1-z<=exp(-z)` imply

```text
E I_e = 1-prod_b(1-r_{b,e}) >= 1-exp(-x_e).         (12)
```

The function `f(x)=1-exp(-x)` is concave, increasing, and satisfies `f(0)=0`. Thus for `0<=x<=L`,

```text
f(x) >= [f(L)/L] x.                                 (13)
```

Let `Z_U=e(G_U)=sum_e I_e`. Combining (1), (10)--(13),

```text
E Z_U
 >= [1-exp(-L)]/L * eta M q_*
 =  eta q_* [1-exp(-L)] * m d^2/(C_* S).            (14)
```

Since `R>=d^2/2`,

```text
L>=C_*/2,
1-exp(-L)>=1-exp(-C_*/2)=:c_*>0.
```

Therefore

```text
E Z_U >= c_2 m d^2/S,                               (15)
```

where

```text
c_2:=eta q_* c_*/C_*>0
```

depends only on `epsilon,theta` once `d_0` has been fixed.

This is the point at which arbitrary codegree concentration disappears: only the exact mass identity (11) and the universal cap (10) are used.

### 4. Occupied-pair indicators have nonpositive covariance

For distinct pairs `e,f`, one connector can select at most one of them. Hence

```text
P(I_e=0,I_f=0)
 = prod_b (1-r_{b,e}-r_{b,f})
 <= prod_b (1-r_{b,e})(1-r_{b,f})
 = P(I_e=0)P(I_f=0).
```

Using

```text
Cov(I_e,I_f)
 =P(I_e=0,I_f=0)-P(I_e=0)P(I_f=0),
```

we obtain

```text
Cov(I_e,I_f)<=0.                                    (16)
```

Consequently

```text
Var Z_U <= sum_e Var I_e <= E Z_U.                  (17)
```

Chebyshev and (15) yield

```text
P( Z_U < (1/2) E Z_U )
 <= 4/E Z_U
 <= 4S/(c_2 m d^2)
 <= 4/(c_2 d^2).                                    (18)
```

On the complementary event, (7) and (15) imply

```text
average_degree(G_U)
 =2Z_U/|U|
 >= (E Z_U)/|U|
 >= (c_2/4)d.                                       (19)
```

Every graph of average degree `D` has a nonempty subgraph of minimum degree at least `D/2` (iteratively delete vertices below `D/2`; deleting all vertices would delete fewer edges than the graph has). A longest path in a graph of minimum degree `delta` contains a cycle of length at least `delta+1`. Thus (19) gives a cycle in `G_U` of length at least

```text
c_3 d,
c_3:=c_2/8,                                        (20)
```

for large enough `d`. By the one-pair-per-connector construction, this lifts to a simple cycle of length at least `2c_3d` in `J_p`.

### 5. Why the conclusion is a.a.s. for every host-order regime

The estimate (18) is already enough whenever `d -> infinity`.

Now suppose `d` stays bounded along a subsequence.

If

```text
h=max(1,floor(S/d)) -> infinity,
```

then the percolation variables used by different color classes are disjoint: class `U_j` only uses edges joining `B` to `U_j`. The auxiliary pair choices may also be taken independently across classes. At least `h/2` classes are good, so by (18), after increasing `d_0` so that `4/(c_2d^2)<1`,

```text
P(no good class succeeds)
 <= [4/(c_2d^2)]^(h/2) -> 0.                        (21)
```

It remains to consider sequences for which both `d` and `h` stay bounded. Then `S` stays bounded.

If `m=|A| -> infinity`, (15) gives `E Z_U -> infinity` in every good class, and (18) gives success probability tending to one.

Finally suppose `m` also stays bounded. Since the total host order tends to infinity and `M=mR/S`, necessarily `R -> infinity` and `M -> infinity`. There are only finitely many possible `S`-subsets of the bounded set `A`. Hence some neighborhood type `T subset A`, `|T|=S`, occurs for a number `L_T -> infinity` of twin connectors.

Fix a cyclic ordering of the `S` vertices of `T`. Split the `L_T` twin connectors into `S` disjoint groups of sizes tending to infinity. For each consecutive pair of vertices in the cyclic ordering, use only its assigned connector group. Every connector in that group has both required incidences open with probability `p^2`, independently across connectors. Since `p` is bounded below by a positive constant in this bounded-`d` case, the probability that a group contains no common-open witness tends to zero. A union bound over the bounded number `S` of pairs shows that `J_p` contains a simple cycle of length `2S` with probability tending to one. Since

```text
S >= theta d/16,                                   (22)
```

this is again a cycle of length `Omega_theta(d)`.

The cases above exhaust every sequence with host order tending to infinity. Taking

```text
gamma=min(2c_3,theta/8)>0
```

(after harmlessly decreasing it to cover integer roundoff) proves the theorem. `QED`

## What this proves and what it does not

This proves exactly the biregular cross-core recovery target isolated in the previous R7-07 stuck diagnosis. It removes the earlier distinct-witness/Hall obstruction in the biregular setting by delaying witness allocation until after percolation and localizing the A-side to `Theta(md/S)` blocks.

It does **not** prove G0011. The full source still begins from an arbitrary graph of average degree `d`; the cumulative structural reduction gives an irregular cross core with lower semidegree bounds, not exact biregularity. The next missing step is a lossless regularization/decomposition theorem that passes from that irregular core to enough approximately biregular cells without reintroducing the factor-two density loss or destroying the a.a.s. amplification.

No novelty claim is made here. A bounded 2026-09-17 literature search found relevant minimum-degree percolation, percolated-expander, and long-Berge-cycle theorems, but no exact theorem matching this arbitrary-overlap biregular percolation statement; a search miss is not a novelty certificate.
