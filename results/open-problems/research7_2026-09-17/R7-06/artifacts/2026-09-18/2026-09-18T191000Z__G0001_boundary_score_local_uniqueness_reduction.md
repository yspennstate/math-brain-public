Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# G0001: boundary-score reduction, mass transport, and a finite local-uniqueness obstruction

Target: Raphaël Cerf, *$\theta(p_c,{\mathbb Z}^d)=0?$* (2026), arXiv:2608.23661v1, Conjecture 1.4.

Status: **PARTIAL / OPEN**. Nothing below proves `theta(p_c)=0` in a new dimension.

## 0. Mathematical idea before any finite check

Assume the negation in one unresolved dimension: `theta(p_c)>0`. Cerf's Theorem 1.2 then forces the finite-cluster volume tail to be slower than every stretched exponential along a subsequence. Instead of trying to bound all finite clusters at once, compare the exact probability of a fixed finite cluster at `p=p_c` with the probability of the *same* cluster at `q>p_c`. This eliminates, exponentially in volume, every cluster whose external vertex-boundary density is below a sharp likelihood-ratio threshold. Hence any hypothetical slow critical tail must be carried by highly exposed clusters. Translation symmetry then converts that high boundary density into an exact positive density of closed boundary witnesses by mass transport. Finally, a separate finite-box decomposition shows that a large finite cluster can exist only through either a macroscopic hole in the infinite cluster or a two-macroscopic-cluster local-uniqueness failure.

This gives two concrete gluing targets for a future attack: turn the abundant closed boundary witnesses into gateways to the infinite cluster, or obtain a stretched-exponential bound on the finite hole/two-cluster obstruction.

## 1. Notation

Work in Bernoulli site percolation on `Z^d`, `d>=3`, with parameter `p`. Let `C(0)` be the open cluster of the origin. For a finite connected set `A` containing `0`, let

`partial A = { y notin A : y is nearest-neighbour adjacent to some x in A }`

be its external vertex boundary. Put `k(A)=|A|` and `m(A)=|partial A|`.

Because `C(0)=A` iff every site of `A` is open and every site of `partial A` is closed,

`P_p(C(0)=A) = p^{k(A)} (1-p)^{m(A)}`.                                      (1.1)

No state outside `A union partial A` is constrained.

Write

`T_p(n)=P_p(n <= |C(0)| < infinity)`.

## 2. B2 — attack the negation first: exact likelihood-ratio elimination of low-boundary clusters

### Theorem 2.1 (low boundary density is exponentially negligible)

Fix `0<p<q<1`. Define

`r_*(p,q) = log(q/p) / log((1-p)/(1-q))`.

For every `0<=r<r_*(p,q)`, set

`kappa(p,q,r)=log(q/p)-r log((1-p)/(1-q))>0`.

Then for every integer `n>=1`,

`P_p( n<=|C(0)|<infinity, |partial C(0)| <= r |C(0)| ) <= exp(-kappa n)`.       (2.1)

#### Proof

For every finite connected `A` containing the origin with `m(A)<=r k(A)`, (1.1) at parameters `p` and `q` gives

`P_p(C(0)=A) / P_q(C(0)=A)`
`= (p/q)^{k(A)} ((1-p)/(1-q))^{m(A)}`
`<= exp[-k(A){log(q/p)-r log((1-p)/(1-q))}]`
`= exp[-kappa k(A)]`.

Summing over all such `A` with `k(A)>=n`,

`P_p(...) <= exp(-kappa n) sum_A P_q(C(0)=A) <= exp(-kappa n)`.

The last sum is at most the probability that `C(0)` is finite at parameter `q`, hence at most one. QED.

### Sharp infinitesimal threshold

By l'Hopital,

`lim_{q downarrow p} r_*(p,q) = (1-p)/p`.                                    (2.2)

Therefore for every fixed

`r < (1-p)/p`,

one may choose `q>p` sufficiently close to `p` so that (2.1) holds with some `kappa>0`.

### Corollary 2.2 (what Cerf's negation forces)

Now put `p=p_c` in an unresolved dimension and assume `theta(p_c)>0`. Cerf's Theorem 1.2 then gives

`liminf_{n->infinity} [log log(1/T_{p_c}(n))]/log n = 0`.                     (2.3)

For every `r<(1-p_c)/p_c`, define the high-boundary tail

`T^{hi}_{p_c,r}(n) = P_{p_c}( n<=|C(0)|<infinity, |partial C(0)| > r|C(0)| )`.

Then

`liminf_{n->infinity} [log log(1/T^{hi}_{p_c,r}(n))]/log n = 0`.              (2.4)

#### Proof

Choose `q>p_c` with `r<r_*(p_c,q)`. The complementary low-boundary tail is at most `exp(-kappa n)` by Theorem 2.1. If the high-boundary tail had any positive stretched-exponential exponent eventually, their sum `T_{p_c}(n)` would also have a positive stretched-exponential exponent, contradicting (2.3). QED.

**Interpretation.** Under the negation of the source conjecture, the slow tail cannot be carried by Wulff-like compact droplets. For every boundary density strictly below `(1-p_c)/p_c`, that part is already exponentially small in volume. Any surviving obstruction is forced into the highly exposed/ramified part of cluster space.

## 3. B14 — exploit translation symmetry: exact mass-transport boundary witness identity

For `n>=1` and a site `y`, let `N_n(y)` denote the number of *distinct* finite open clusters `K` satisfying `|K|>=n` and having at least one nearest-neighbour site adjacent to `y`. Set `N_n(y)=0` when `y` is open. Plainly `0<=N_n(y)<=2d`.

### Theorem 3.1 (boundary mass transport)

For every `p` and `n`,

`E_p[ (|partial C(0)|/|C(0)|) 1_{n<=|C(0)|<infinity} ]`
`= E_p[ 1_{0 closed} N_n(0) ]`.                                               (3.1)

#### Proof

Use the translation-covariant mass transport in which each vertex `x` belonging to a finite open cluster `K` of size at least `n` sends mass `1/|K|` to each site of `partial K`.

The total mass sent from the origin is exactly

`(|partial C(0)|/|C(0)|) 1_{n<=|C(0)|<infinity}`.

If `y` is a closed site in the boundary of a qualifying cluster `K`, every vertex of `K` sends `1/|K|` to `y`, hence `K` contributes total received mass one. Summing over distinct qualifying clusters adjacent to `y` gives `N_n(y)`. Translation invariance and the mass-transport principle equate expected sent and received mass, proving (3.1). QED.

### Corollary 3.2 (slow volume tail forces a comparable density of closed witnesses)

Take `0<p<q<1` and `r<r_*(p,q)`, and let `kappa` be as in Theorem 2.1. Then

`E_p[1_{0 closed} N_n(0)] >= r( T_p(n)-exp(-kappa n) )`.                      (3.2)

Consequently, with

`Q_p(n)=P_p(0 is closed and N_n(0)>=1)`,                                    (3.3)

we have

`Q_p(n) >= [r/(2d)] ( T_p(n)-exp(-kappa n) )`.                               (3.4)

#### Proof

Outside the exponentially small low-boundary event of Theorem 2.1, every cluster counted by `T_p(n)` has boundary/volume ratio strictly bigger than `r`. Thus the left side of (3.1) is at least `r(T_p(n)-e^{-kappa n})`. Since `N_n(0)<=2d`, its expectation is at most `2d Q_p(n)`. QED.

At hypothetical critical percolation, (2.3)-(2.4) imply that these local closed boundary witnesses themselves occur with non-stretched-exponentially-small probability along the same obstruction scales. A proof must therefore explain why a positive fraction of them become *gateways* to the infinite cluster (or otherwise create enough pivotal structure); merely counting the external boundary is no longer the missing step.

## 4. B2/B16 finite local obstruction: hole versus two-cluster failure

Let

`B_R={x in Z^d: ||x||_infinity <= R}`.

Let `H_R` be the event that no infinite open cluster intersects `B_R`. Let `U_R` be the finite event that the induced open configuration in `B_{2R}` contains at least two distinct open connected components, each intersecting both `B_R` and `partial B_{2R}`.

Put

`n_R=(4R+1)^d+1=|B_{2R}|+1`.

### Theorem 4.1 (exact large-finite-cluster decomposition)

For every `p` and `R>=1`,

`T_p(n_R) <= P_p(H_R)+P_p(U_R)`.                                             (4.1)

#### Proof

If `C(0)` is finite and has at least `n_R` vertices, it cannot be contained in `B_{2R}`, because `|B_{2R}|=(4R+1)^d`. Hence the component of `0` in the induced configuration on `B_{2R}` intersects both `B_R` and `partial B_{2R}`.

If `H_R` does not occur, some vertex of `B_R` belongs to an infinite open cluster. That infinite cluster also exits `B_{2R}` and therefore has a component in the induced configuration on `B_{2R}` intersecting both `B_R` and `partial B_{2R}`. It is distinct from the finite cluster of the origin. Hence `U_R` occurs. This proves the event inclusion underlying (4.1). QED.

The hole event has the exact finite-volume approximation

`P_p(H_R)=lim_{L->infinity} P_p(B_R not connected to partial B_L)`.           (4.2)

For `x!=y` in `B_R`, let `A_{x,y}^{(R)}` be the finite event that, inside `B_{2R}`, `x` and `y` lie in distinct open components and each component touches `partial B_{2R}`. Then

`P_p(U_R) <= sum_{x!=y in B_R} P_p(A_{x,y}^{(R)})`
`<= |B_R|^2 a_2(R)`,                                                         (4.3)

where `a_2(R)=sup_{x!=y in B_R}P_p(A_{x,y}^{(R)})`.

Thus, in any fixed dimension, *any* stretched-exponential control in `R` of both the infinite-cluster hole probability and the finite two-component quantity `a_2(R)` implies a stretched-exponential volume tail in `n` via `R asymp n^{1/d}`, and therefore proves the source conjecture in that dimension. Conversely, under `theta(p_c)>0` plus Cerf's Theorem 1.2, at least one of these two local-geometry quantities must fail every such stretched-exponential bound along a sequence of scales.

This is a finite-volume certificate route: `U_R` and every `A_{x,y}^{(R)}` are exactly finite events; `H_R` is a monotone limit of finite connection events.

## 5. B16 — exact small clusters, with an executed enumeration check

The first three rooted finite-cluster sizes can be counted exactly.

### Size 1

There is one rooted animal and `m=2d`, hence

`P_p(|C(0)|=1)=p(1-p)^{2d}`.                                                 (5.1)

### Size 2

There are `2d` rooted animals, each an edge from the origin. Its external vertex boundary has size `4d-2`, so

`P_p(|C(0)|=2)=2d p^2(1-p)^{4d-2}`.                                         (5.2)

### Size 3

Every three-site connected animal is a path. Among rooted animals:

- `3d` are straight and have boundary `6d-4`;
- `6d(d-1)` are bent and have boundary `6d-5`.

Therefore

`P_p(|C(0)|=3)`
`=3d p^3(1-p)^{6d-4}+6d(d-1)p^3(1-p)^{6d-5}`.                               (5.3)

A direct finite enumeration was executed for every `d=3,...,10` and reproduced these counts exactly. For example:

- `d=3`: size 3 has 45 rooted animals: 36 with boundary 13 and 9 with boundary 14;
- `d=4`: 84 rooted animals: 72 with boundary 19 and 12 with boundary 20;
- `d=10`: 570 rooted animals: 540 with boundary 55 and 30 with boundary 56.

The standard nonbacktracking-path comparison gives `p_c >= 1/(2d-1)`, hence

`(1-p_c)/p_c <= 2d-2`.                                                       (5.4)

But the smallest boundary/volume ratio among all clusters of sizes `1,2,3` is

`(6d-5)/3 = 2d-5/3 > 2d-2`.                                                 (5.5)

So every exact cluster of size at most three lies on the **high-boundary side** forced by Corollary 2.2. This is a sanity check on the structural reduction: the low-boundary sector only appears after clusters become geometrically compact enough.

## 6. What has and has not moved

Frozen source metric:

`D_closed = # {d in {3,...,10}: theta(p_c,Z^d)=0 proved completely in this campaign}`.

Before this run: `0`.
After this run: `0`.

**No metric movement.** The source remains OPEN / PARTIAL.

What did move mathematically is the shape of the obstruction:

1. low external-boundary density is already exponentially negligible by an exact change-of-parameter argument;
2. any hypothetical slow critical tail must be concentrated on clusters with boundary density arbitrarily close from below to `(1-p_c)/p_c` or larger;
3. translation symmetry converts this into a quantitative density of closed boundary witnesses;
4. large finite clusters also force either an infinite-cluster hole or a finite two-macroscopic-component local-uniqueness failure.

The missing gluing theorem is now explicit: prove that, in Bernoulli site percolation at a hypothetical `theta(p_c)>0`, the abundant high-boundary witnesses cannot remain screened from the infinite cluster across many scales, equivalently obtain a stretched-exponential bound for the hole/two-component obstruction in Theorem 4.1.

## 7. Failed route / noncircularity warning

Positive density, translation invariance, and global uniqueness of an infinite cluster are **not by themselves** enough to supply a quantitative hole or local-uniqueness rate. Any future proof must use Bernoulli independence/finite energy and genuine geometry, not simply ergodicity. Likewise, applying the classical supercritical local-uniqueness theorem at `p=p_c` would be circular: those results assume `p>p_c`, exactly what Cerf's Theorem 1.3 is designed to infer from a tail estimate.

## 8. Next nonrepeating attack

Do not reuse B2/B14/B16 next ordinary run. The most promising next triple is:

- **B5**: differentiate the exact cluster-animal weights in `p`; the score is `|C|/p-|partial C|/(1-p)`, whose zero set is exactly the boundary-density threshold found above;
- **B20**: isolate the minimal bad configuration in which many closed boundary witnesses fail to be gateways to the infinite cluster;
- **B21**: import the local-uniqueness / truncated-connectivity mechanism from strictly supercritical Bernoulli percolation, identifying precisely which use of `p>p_c` must be replaced at the endpoint.

A successful next lemma should quantify gateway density or a one-scale contraction for `H_R+U_R`; another generic animal count without a new inequality should be rejected as checker churn.
