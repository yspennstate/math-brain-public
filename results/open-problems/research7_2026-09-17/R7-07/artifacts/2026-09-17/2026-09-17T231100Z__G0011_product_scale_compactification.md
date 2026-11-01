# G0011 artifact — product-scale compactification of the diffuse cross-core obstruction

Date: 2026-09-17 UTC / 2026-09-18 Asia/Jerusalem.
Owner: R7-07, native ID `6aabe8413f60819197825dd81ca138ae`.
Target: `G0011`, the Krivelevich–Samotij long-cycle conjecture as restated by Christoph–Morawski–Wigderson, arXiv:2608.19145v1.
Status: **restricted structural theorem / PARTIAL**, not a proof of the full source conjecture. No novelty claim is made.

This note continues from the previously proved R7-07 cross-core theorem in

`research7_2026-09-17/R7-07/artifacts/2026-09-17/2026-09-17T222000Z__bounded_scale_entropy_cross_core.md`

created at commit `816044766505d48898f4dcdb534aa40b08eb5452`.

The standing cross-core hypotheses are the following. For fixed positive constants `epsilon,r_0,s_0,c_0`, let

`J=(A,B;E_J)`

be a finite bipartite graph, write `E=|E_J|`, and suppose

```text
deg_J(a) >= r_0 d^2             for every a in A,
deg_J(b) >= s_0 d               for every b in B,
E >= c_0 n d,
```

where `n -> infinity` is the ambient host order and `d>=d_0` is the source average-degree scale. Percolate every incidence independently with

```text
p=(1+epsilon)/d.
```

The preceding artifact proves, among other things, that if a dyadic degree-pair cell contains fixed conditional fractions of both its row and its column, then that cell peels to a bounded-ratio cross core and `J_p` has a simple cycle of length `Omega(d)` asymptotically almost surely. The present note finds a new invariant and uses it to classify every cross-core sequence not already covered by that theorem.

## 1. B12 — an exact likelihood-ratio invariant on a uniformly sampled incidence

Let `nu` be the uniform probability law on the `E` incidences of `J`:

```text
nu(a,b)=1/E        if ab is an edge,
nu(a,b)=0          otherwise.
```

Let the size-biased endpoint laws be

```text
mu_A(a)=deg(a)/E,
mu_B(b)=deg(b)/E.
```

Under the product law `mu_A tensor mu_B`, define

```text
L(a,b)= E/(deg(a)deg(b))       if ab is an edge,
L(a,b)= 0                      otherwise.                 (1.1)
```

### Lemma 1.1 — exact Radon–Nikodym identity

We have

```text
d nu / d(mu_A tensor mu_B) = L.                          (1.2)
```

In particular,

```text
E_{mu_A tensor mu_B}[L]=1.                               (1.3)
```

#### Proof

For an edge `ab`,

```text
(mu_A tensor mu_B)(a,b)
   =deg(a)deg(b)/E^2,
```

so multiplying by `L(a,b)=E/(deg(a)deg(b))` gives exactly `1/E=nu(a,b)`. Off the edge set both sides of (1.2) are zero. Summing proves (1.3). `QED`

The invariant is useful because it gives an exact capacity bound on incidences whose two endpoint degrees are simultaneously large.

### Corollary 1.2 — universal double-hub tail bound

For every `M>=1`,

```text
nu{ deg(a)deg(b) >= M E } <= 1/M.                        (1.4)
```

#### Proof

On the displayed event, `L<=1/M`. Therefore, by (1.2),

```text
nu(S)= integral_S L d(mu_A tensor mu_B)
     <= (1/M)(mu_A tensor mu_B)(S)
     <= 1/M.
```

`QED`

Thus a positive proportion of incidences can never escape to arbitrarily large values of the normalized degree product

```text
U(ab):=deg(a)deg(b)/E.                                   (1.5)
```

There is also a spectral interpretation that will be useful below. Let `N` be the normalized rectangular incidence matrix

```text
N_ab = 1/sqrt(deg(a)deg(b))       if ab is an edge,
N_ab = 0                           otherwise.
```

Then

```text
Xi(J):=||N||_F^2
      =sum_{ab in E_J} 1/(deg(a)deg(b))
      =E_nu[L].                                             (1.6)
```

For every nonempty `J`, `||N||_op=1`: the vectors `sqrt(deg_A)` and `sqrt(deg_B)` give singular value one, while Cauchy–Schwarz gives operator norm at most one. Hence

```text
Xi(J)=stable-rank(N).                                      (1.7)
```

Moreover, from (1.2),

```text
Xi(J)
 = E_{mu_A tensor mu_B}[L^2]
 >= (E_{mu_A tensor mu_B}[L])^2
 =1.                                                       (1.8)
```

No probabilistic approximation enters these identities.

## 2. Dyadic degree transport and a fixed-width product band

Use the same dyadic degree bins as in the preceding artifact:

```text
R_0=r_0d^2,          S_0=s_0d,
R_i=2^iR_0,          S_j=2^jS_0,
A_i={a: R_i <= deg(a) < 2R_i},
B_j={b: S_j <= deg(b) < 2S_j}.
```

Write

```text
e_ij=e(A_i,B_j),
P_ij=e_ij/E,
P_i=sum_j P_ij,
Q_j=sum_i P_ij.                                           (2.1)
```

For each occupied cell define the integer product-scale index

```text
sigma_ij := floor(log_2(R_i S_j/E)).                      (2.2)
```

Because `R_iS_j=2^(i+j)R_0S_0`, there is an integer `c_E` depending on the instance but not on `i,j` such that

```text
sigma_ij=i+j+c_E.                                         (2.3)
```

Consequently a band consisting of `L` consecutive values of `sigma` meets at most `L` cells in every row and at most `L` cells in every column.

### Theorem 2.1 — any fixed product-scale window closes the cross-core branch

Fix constants

```text
0 < delta < M < infinity,
eta > 0.
```

Consider a sequence of cross cores satisfying the standing hypotheses. Suppose along a subsequence

```text
nu{ delta <= deg(a)deg(b)/E <= M } >= eta.                (2.4)
```

Then, along that subsequence, percolation at `p=(1+epsilon)/d` contains a simple cycle of length `Omega(d)` asymptotically almost surely.

#### Proof

If an edge `ab` lies in dyadic cell `(i,j)`, then

```text
R_i S_j <= deg(a)deg(b) < 4 R_i S_j.                      (2.5)
```

Thus every edge counted in (2.4) belongs to a cell satisfying

```text
delta/4 < R_iS_j/E <= M.                                 (2.6)
```

The possible values of `sigma_ij` in (2.6) lie in a fixed interval of integers whose length

```text
L <= 3 + ceil(log_2(M/delta))                             (2.7)
```

depends only on `delta,M`, not on the graph, `n`, or `d`. Let `S` denote the set of all cells in that consecutive `sigma`-band. Its total transport mass satisfies

```text
m(S):=sum_{(i,j) in S} P_ij >= eta.                       (2.8)
```

The issue is that `S` might be only a tiny fraction of the total mass of many of its rows or columns. We remove exactly that leakage by a two-sided weighted peeling.

Set

```text
tau=eta/8.                                                (2.9)
```

Starting from the cell set `S`, repeatedly perform either of the following operations whenever possible:

1. delete an entire current row `i` if its current surviving band mass is `< tau P_i`;
2. delete an entire current column `j` if its current surviving band mass is `< tau Q_j`.

Every row is deleted at most once, and at its deletion it removes less than `tau P_i`. Hence all row deletions together remove less than

```text
tau sum_i P_i <= tau.                                    (2.10)
```

Likewise all column deletions together remove less than `tau`. Therefore the terminal cell set `T` has mass

```text
m_T:=sum_{(i,j) in T}P_ij
    >= eta-2tau
    =3eta/4.                                              (2.11)
```

Every surviving row and column satisfies

```text
r_i:=sum_{j:(i,j) in T}P_ij >= tau P_i,
c_j:=sum_{i:(i,j) in T}P_ij >= tau Q_j.                  (2.12)
```

Normalize the terminal mass:

```text
tilde P_ij=P_ij/m_T,          (i,j) in T.                (2.13)
```

Under `tilde P`, define the row and column conditional weights

```text
tilde alpha_ij=P_ij/r_i,
tilde beta_ij =P_ij/c_j.                                  (2.14)
```

The support of every conditional row and column has cardinality at most `L`, by (2.3). Put `C=max(2,L)`. Therefore

```text
H_tilde(J|I) <= log C,
H_tilde(I|J) <= log C.                                   (2.15)
```

Equivalently, under a random cell drawn from `tilde P`,

```text
E[-log(tilde alpha_ij tilde beta_ij)] <= 2 log C.         (2.16)
```

Markov's inequality gives `tilde P`-mass at least `1/2` to cells satisfying

```text
-log(tilde alpha_ij tilde beta_ij) <= 4 log C.            (2.17)
```

On every such cell,

```text
tilde alpha_ij tilde beta_ij >= C^(-4).                  (2.18)
```

Since both factors are at most one, each factor separately is at least `C^(-4)`. Combining this with (2.12), the corresponding *global* transport conditionals satisfy

```text
alpha_ij:=P_ij/P_i
          =tilde alpha_ij (r_i/P_i)
          >= tau C^(-4),

beta_ij:=P_ij/Q_j
         =tilde beta_ij (c_j/Q_j)
         >= tau C^(-4).                                  (2.19)
```

The cells satisfying (2.17) carry total original mass at least

```text
m_T/2 >= 3eta/8.                                         (2.20)
```

There are at most `(1+ceil(log_2 n))^2` occupied dyadic degree cells in a simple `n`-vertex host. Hence one cell satisfying (2.19) has

```text
e_ij
 >= [3eta/(8(1+ceil(log_2 n))^2)] E
 >= c_eta n d/(log n)^2
 -> infinity.                                             (2.21)
```

The balanced-cell peeling lemma in the preceding R7-07 artifact now applies with the fixed constants

```text
alpha=beta=tau C^(-4)>0.                                 (2.22)
```

It leaves more than `e_ij/2` edges in a bipartite subgraph whose `A`-side degrees lie between a fixed positive multiple of `d^2` and a fixed multiple of that lower scale, and whose `B`-side degrees lie between a fixed positive multiple of `d` and a fixed multiple of that lower scale. By (2.21), the surviving subgraph order tends to infinity. The previously proved bounded-ratio cross-core theorem therefore yields a simple cycle of length `Omega(d)` in the percolated graph asymptotically almost surely. `QED`

The proof is lossless in the sense relevant to the source probability: no factor is inserted into `p`. Constants deteriorate with `delta,M,eta`, but all are fixed along the subsequence.

## 3. B7 — the only possible limiting product-scale law is escape to minus infinity

Theorem 2.1 and the exact tail bound (1.4) together completely classify the normalized endpoint-degree product along any putative counterexample sequence to the current cross-core theorem.

### Theorem 3.1 — product-scale escape theorem

Let `(J_n)` be any sequence satisfying the standing cross-core hypotheses for which the desired `Omega(d)` long-cycle conclusion at

```text
p=(1+epsilon)/d
```

fails to hold asymptotically almost surely. Sample a host incidence uniformly and define

```text
U_n=deg(a)deg(b)/E_n.                                    (3.1)
```

Then

```text
U_n -> 0 in nu_n-probability.                            (3.2)
```

Equivalently,

```text
Z_n:=log_2 U_n -> -infinity in probability.              (3.3)
```

#### Proof

Suppose (3.2) fails. Then for some fixed `delta>0`, some `eta>0`, and a subsequence,

```text
nu_n{U_n>=delta} >= eta.                                 (3.4)
```

Choose a fixed

```text
M>max(1,2/eta).
```

By Corollary 1.2,

```text
nu_n{U_n>=M} <= 1/M < eta/2.                             (3.5)
```

Hence along the same subsequence

```text
nu_n{delta <= U_n < M} >= eta/2.                         (3.6)
```

Theorem 2.1 applies and gives the desired `Omega(d)` cycle a.a.s., contradicting the assumption on the sequence. Thus (3.2) holds, and (3.3) is equivalent. `QED`

This is a genuine limiting-measure classification. If one compactifies the product coordinate to the extended line `[-infinity,+infinity]`, the edge-size-biased law of `Z_n` for every counterexample sequence converges weakly to

```text
delta_{-infinity}.                                       (3.7)
```

The `+infinity` boundary cannot carry positive mass because of the exact `2^{-t}` upper tail inherited from (1.4), while Theorem 2.1 excludes every fixed finite window.

## 4. B29 — compactify the log-degree plane and identify the only surviving face

The preceding theorem can be viewed geometrically in the two-dimensional log-degree plane. An edge in cell `(i,j)` has coordinates approximately

```text
x=log_2(deg(a)/(r_0d^2)),
y=log_2(deg(b)/(s_0d)).                                  (4.1)
```

After centering by the total edge mass, the product coordinate is

```text
x+y - log_2(E/(r_0s_0d^3))
   = log_2(deg(a)deg(b)/E) + O(1).                       (4.2)
```

A fixed-width strip transverse to the direction `(1,-1)` is exactly a fixed product-scale band. Theorem 2.1 says that positive incidence mass in any such strip is already solvable by the bounded-ratio theorem. Corollary 1.2 says positive mass cannot run off to the high-product face. Therefore every counterexample sequence must put asymptotically all incidence mass on the *low-product boundary face* (4.2) `-> -infinity`.

This has a clean operator consequence.

### Corollary 4.1 — normalized-incidence stable rank must diverge

Along every counterexample sequence to the cross-core statement,

```text
Xi(J_n)
 =sum_{ab in E(J_n)}1/(deg(a)deg(b))
 =stable-rank(N_n)
 -> infinity.                                             (4.3)
```

#### Proof

By Theorem 3.1,

```text
L_n=1/U_n=E_n/(deg(a)deg(b)) -> infinity
```

in `nu_n`-probability. For any fixed `T>0`,

```text
Xi(J_n)=E_{nu_n}[L_n]
        >= T nu_n{L_n>=T}
        -> T.                                             (4.4)
```

Since `T` is arbitrary, `Xi(J_n)->infinity`. The stable-rank identity is (1.7). `QED`

Thus the previous informal idea that the remaining obstruction might simply be a double-hub or complete-bipartite boundary is wrong. A complete-bipartite/biregular concentration has bounded product-scale complexity and was already solved by the earlier theorem. The only still-possible cross-core obstruction must be simultaneously:

1. **bidirectionally diffuse across dyadic degree scales**, so the previous collision statistic satisfies `Phi(2)->0` and `H(J|I)+H(I|J)->infinity`;
2. **low product on a typical incidence**, so `deg(a)deg(b)/E ->0` in edge probability;
3. **high normalized-incidence stable rank**, so `Xi(J)->infinity`.

These are necessary conditions on any counterexample sequence; they are not asserted sufficient for a counterexample.

## 5. Relation to the previous transport obstruction

The current run therefore sharpens the earlier blocker

```text
Phi(2) -> 0,
H_bi -> infinity
```

to the four-part necessary regime

```text
Phi(2) -> 0,
H_bi -> infinity,
U=deg(a)deg(b)/E -> 0 in edge probability,
Xi(J)=sum_edges 1/(deg(a)deg(b)) -> infinity.             (5.1)
```

There is also an elementary cell-capacity inequality explaining why the low-product face is the one on which highly diffuse transport can hide. Since

```text
|A_i| <= E P_i/R_i,
|B_j| <= E Q_j/S_j,
```

simplicity gives

```text
E P_ij=e_ij <= |A_i||B_j|
               <= E^2 P_iQ_j/(R_iS_j).
```

Hence

```text
P_ij/(P_iQ_j) <= E/(R_iS_j).                             (5.2)
```

The right-hand side is precisely the reciprocal dyadic product scale. At finite or high product scale, the transport density relative to the independent endpoint law has bounded capacity and Theorem 2.1 forces a balanced cell. Only when `R_iS_j/E` tends to zero can the admissible transport density become arbitrarily large while the row and column conditionals themselves spread over more and more scales.

Equation (5.2) is only a structural inequality; it does not by itself close the low-product regime.

## 6. Exact remaining gap

Nothing in this note changes the source metric `K_long`; the full source conjecture remains open in this track. In particular, the argument does **not** prove that a high-stable-rank normalized incidence matrix produces a long percolated cycle at the source probability. It only proves that every counterexample to the surviving cross-core branch would have to have exactly that high-stable-rank/low-product form.

The next mathematical obstruction is therefore much narrower than generic degree irregularity:

> Can a bipartite cross core with `delta_A=Omega(d^2)`, `delta_B=Omega(d)`, `E=Omega(nd)`, `Phi(2)->0`, and normalized-incidence stable rank `Xi->infinity`, while a typical edge has `deg(a)deg(b)=o(E)`, avoid an `Omega(d)` cycle after percolation at `p=(1+epsilon)/d`?

The next protocol invocation is required to be the second and final thinking-only stuck recovery if the frozen metric has remained unchanged for the third ordinary post-recovery run. This artifact deliberately does not select that recovery action in advance.