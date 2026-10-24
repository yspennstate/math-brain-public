Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# G0008 — exact first-step defect identity and explicit low/high-density certificates

Target: Campos--de Lima / intake `G0008`, Bernoulli bond percolation on `Z^2`,

`tau_n(p) = P_p(0 <-> n e_1)`.

This artifact is an internal mathematical derivation. It does **not** claim novelty. It does **not** settle the all-`p`, all-`n` source problem.

Frozen R7-06 metric: `M_axis`, the largest `N>=1` for which all inequalities `tau_{n+1}(p)<=tau_n(p)` are proved simultaneously for every `p in (0,1)` and `1<=n<=N`. The metric remains `UNKNOWN/UNMEASURED` because the present run does not prove the first inequality for every `p`.

## 1. B2 — attack the negation by deleting the two axial edges

The first unresolved source-valid milestone is

`tau_1(p) >= tau_2(p)` for every `0<p<1`.

Let

- `x=0`, `y=e_1`, `z=2e_1`;
- `G=Z^2`;
- `e_1^*={x,y}` and `e_2^*={y,z}`;
- `H=G \ {e_1^*,e_2^*}`.

Run parameter-`p` Bernoulli percolation first on `H`, and then independently restore each of the two deleted edges with probability `p`. Put `q=1-p`.

For the restriction of the open-cluster partition to `{x,y,z}`, write

- `c = P_H(x,y,z all in one open cluster)`;
- `a = P_H(x~y, z separate from that cluster)`;
- `a' = P_H(y~z, x separate)`;
- `b = P_H(x~z, y separate)`;
- `s = P_H(x,y,z pairwise in distinct clusters)`.

These five events partition the sample space.

### Lemma 1 — exact two-edge deletion identity

For any countable graph `G` containing the path edges `xy,yz`, not only for `Z^2`,

`P_G(x~y)-P_G(x~z) = q [ a - q b + p s ]`.

Equivalently, if

`Delta_H = P_H(x~y)-P_H(x~z)`

and

`D_H = P_H(x !~ y AND y !~ z)`,

then

`boxed:  P_G(x~y)-P_G(x~z) = q [ Delta_H + p D_H ].`

#### Proof

Condition on the five possible partitions in `H`.

1. `xyz` already connected: both target indicators are one; contribution `0`.
2. `xy|z`: `x~y` is certain; `x~z` occurs exactly when the restored edge `yz` is open; conditional difference `1-p=q`.
3. `yz|x`: after restoration, `x~y` and `x~z` are the same event, namely that `xy` is restored; contribution `0`.
4. `xz|y`: `x~z` is already certain. The vertex `y` joins that common cluster if at least one of `xy,yz` is restored, with probability `1-q^2`; conditional difference `(1-q^2)-1=-q^2`.
5. `x|y|z`: `x~y` requires `xy` open, probability `p`; `x~z` requires both restored edges open, probability `p^2`; conditional difference `p-p^2=pq`.

Summing gives

`q a - q^2 b + p q s = q[a-qb+ps]`.

Also `Delta_H=(c+a)-(c+b)=a-b`, while `D_H=b+s`; hence

`a-qb+ps=(a-b)+p(b+s)=Delta_H+pD_H`.

This proves both forms. QED.

### Consequence: what a first-step counterexample would have to do

Since `D_H>=0`, any violation `tau_2(p)>tau_1(p)` forces

`Delta_H < -p D_H <= 0`.

Thus a square-lattice counterexample at separation `1 -> 2` cannot be caused merely by the two obvious axial edges. After those edges are removed, the defect lattice must already reverse the adjacent/far ordering, and must reverse it by at least the positive margin `p D_H`.

This is a strictly stronger obstruction than `Delta_H<0`.

## 2. B14 — reflection symmetry compresses the defect geometry

The defect graph `H=Z^2\{xy,yz}` is invariant under reflection in the vertical line through `y`, which exchanges `x` and `z` and fixes `y`. Therefore

`a=a'`.

No symmetry assumption was needed for Lemma 1, but in this source geometry the whole first-step problem is reduced to four scalar partition masses `c,a,b,s` satisfying

`c+2a+b+s=1`,

with

`tau_1^H=c+a`, `tau_2^H=c+b`.

The exact full-lattice difference is therefore

`boxed: tau_1-tau_2 = q[(a-b)+p(b+s)].`

The term `p(b+s)` is a nonnegative correction created solely by restoring the two axial edges. A counterexample must overcome this correction through the genuinely two-dimensional detour term `b-a`.

This also exposes why a naive path-count ratio is insufficient: the sign is governed by **terminal partition probabilities in the slit lattice**, not by termwise comparison of path-length series.

## 3. B16 — exact first-separation certificates

This section gives two rigorous parameter intervals where the first inequality is certified. They are restricted results only.

### 3.1 Explicit low-density certificate

A direct open edge gives

`tau_1(p) >= p`.

Any connection from `0` to `2e_1` contains a self-avoiding open path. Because `Z^2` is bipartite, every such path has even length. There is exactly one length-2 path. For every length `m>=1`, the total number of self-avoiding paths of length `m` starting at the origin is at most the number of non-backtracking paths,

`4*3^(m-1)`.

Therefore, for `p<1/3`,

`tau_2(p)`
` <= p^2 + sum_{j>=2} 4*3^(2j-1) p^(2j)`
` = p^2 + 108 p^4/(1-9p^2)`.

Hence `tau_2(p)<=tau_1(p)` whenever

`p^2 + 108p^4/(1-9p^2) <= p`,

which, for `0<p<1/3`, is equivalent to

`99p^3+9p^2+p-1 <= 0`.

The polynomial on the left is strictly increasing on `[0,infinity)`, so it has one positive root

`p_- = 0.176409928591824...`.

Thus

`boxed: tau_1(p) >= tau_2(p) for 0<p<=p_- .`

This is a self-contained explicit certificate. It is not advertised as novel; the 2015 de Lima--Procacci--Sanchis paper already proves a stronger qualitative sufficiently-small-`p` monotonicity theorem for all separations.

### 3.2 Explicit high-density certificate for the full, not truncated, connectivity

Now put `q=1-p` and assume `p>1/2`. Let

`F_n(q)=P_p(0 !~ n e_1)=1-tau_n(p)`.

For supercritical bond percolation on `Z^2`, the infinite open cluster is almost surely unique. Therefore, if two fixed vertices are disconnected, at least one lies in a finite open component. The closed edge boundary of a finite component contains a finite minimal cutset separating the two vertices. By planar duality, a minimal cutset is a simple closed dual circuit separating the two terminals.

A dual circuit of length `k` is closed with probability `q^k`.

#### Small cutsets for distance one

For terminals `0,e_1`:

- length `4`: exactly two minimal circuits, isolating either endpoint;
- length `6`: a simple square-lattice dual hexagon encloses a two-vertex domino. It separates the adjacent terminals iff the domino contains exactly one endpoint. Each endpoint has three admissible neighboring dominoes (the fourth domino contains both endpoints), so there are exactly `6`.

Thus the sum of the length-4 and length-6 circuit probabilities is

`S_1(q)=2q^4+6q^6`.

#### Small cutsets for distance two

For terminals `0,2e_1`:

- length `4`: again exactly two;
- length `6`: every domino containing either endpoint contains exactly one of the two terminals, since the terminals are not adjacent. There are four dominoes at each endpoint, hence `8` total.

Thus

`S_2(q)=2q^4+8q^6`.

In particular

`S_2(q)-S_1(q)=2q^6`.

#### Rigorous error bound

For either separation, there are at most ten length-4/6 circuits. Distinct minimal cutsets among these have union size at least `7`; otherwise one would contain another, contradicting minimality (the extremal square/domino pair shares three edges and has union size seven). Bonferroni therefore gives

`|P(at least one length-4/6 cutset is closed)-S_n(q)| <= 45 q^7`.

For longer minimal cutsets, any separating dual circuit must cross the straight primal segment joining the terminals. For separation `n in {1,2}`, there are at most `n` possible straight-segment crossing edges. Once one oriented dual edge is fixed, a crude non-backtracking count gives at most `2*3^(k-1)` dual circuits of length `k` containing it. Therefore, for `3q<1`,

`L_n(q) := P(a closed separating dual circuit of length >=8 exists)`
` <= sum_{k>=8} 2n 3^(k-1) q^k`
` = (2n/3) (3q)^8/(1-3q)`.

Consequently

`|F_n(q)-S_n(q)| <= 45q^7 + L_n(q)`.

Subtracting the `n=1` estimate from the `n=2` estimate gives

`tau_1(p)-tau_2(p)`
` = F_2(q)-F_1(q)`
` >= 2q^6 - 90q^7 - 2(3q)^8/(1-3q)`
` = q^6 [ 2 - 90q - 2*3^8 q^2/(1-3q) ].`

At `q=1/200`, the bracket is

`2 - 90/200 - 13122/39400 > 1.21 > 0`,

and it only improves as `q` decreases. Hence

`boxed: tau_1(p) > tau_2(p) for 199/200 <= p < 1.`

At `p=1`, both probabilities equal one.

This is a full-connectivity estimate, not merely the truncated-connectivity high-density theorem in de Lima--Procacci--Sanchis. Prior-art novelty of this particular elementary fixed-separation estimate has **not** been certified.

## 4. Exact remaining band for the first milestone

The present self-contained arguments exclude a first-step counterexample outside

`boxed: p in (p_-, 199/200),  p_-=0.176409928591824... .`

Within that band the exact obstruction is

`Delta_H + p D_H < 0`

on the two-edge-deleted defect lattice.

So the most useful next object is not another raw path-count expansion. It is a lower bound on

`Delta_H = P_H(x~y)-P_H(x~z)`

relative to the disconnection mass

`D_H = P_H(x !~ y AND y !~ z)`.

A proof of

`Delta_H >= -p D_H`

for every `p` would settle `M_axis>=1` exactly.

## 5. Failure modes explicitly ruled out

1. The withdrawn intake argument compared path-length series but did not control endpoint-distance dependence. Nothing here reuses that step.
2. The high-density argument does not infer full connectivity monotonicity from the known truncated-connectivity theorem; it separately counts primal separating cutsets through dual circuits.
3. The finite cutset expansion proves only the fixed first comparison. It does not give a uniform-in-`n` high-density threshold.
4. The low/high intervals do not move the frozen metric, because `M_axis` requires **all** `p` for the first comparison.
5. No negative literature search is treated as a novelty certificate.

## 6. Next mathematical attack suggested by this run

The new canonical blocker is the slit-lattice inequality

`P_H(x~y)-P_H(x~z) + p P_H(x !~ y, y !~ z) >= 0`.

Three promising nonrepeating next methods are:

- **B11 (dualize):** express the three terminal partitions of the slit lattice through primal/dual boundary connectivities;
- **B30 (localize/gluing failure):** truncate the slit to a finite box with free/wired boundary conditions and determine whether the signed inequality has a finite exact certificate plus a rigorous boundary tail;
- **B21 (import analogous technique):** adapt the König--Richthammer layered-state Markov operator specifically to the two-edge slit, where only three terminal partitions are needed.
