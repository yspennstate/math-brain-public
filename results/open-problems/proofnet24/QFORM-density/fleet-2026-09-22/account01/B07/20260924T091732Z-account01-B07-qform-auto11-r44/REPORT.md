SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-24T09:17:32Z.
attacking: the r43 four-bank actual rainbow E2 packet; prove a dimension-free determinant-weight router giving either one physical hub with constant star mass or THREE mutually source-disjoint rainbow packets, then compile the hub exactly into slope-mismatch/transverse currencies.

# account01/B07 r44 — weighted rainbow minor selection

## Status

Full unrestricted QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. This report proves supporting coordinate-selection statements only. No Gaussian, log-concave, moment, compact-support, connected-support, diagonal-basis, or rotated-independence assumption is used.

Startup brain source: `yspennstate/math-research-brain@73744cbaa87b2f743c0f20efe496b499903b583b`. OWNER CONTROL read from `scheduled_tasks/README.md`: revision `2026-09-22.15`, active programme `QFORM-DENSITY-3EIG-20260922`, no pause/reassignment of account01/B07.

Input from account01/B07 r43: on the actual rank-two-separator branch there are four mutually disjoint original-coordinate banks `R,S,C,D` and a physical pair `K` disjoint from all four, with

`W := sum_{r in R,s in S,c in C,d in D} Delta(r,s;c,d)^2 > W0`,

where

`Delta(r,s;c,d)=det M[{r,s},{c,d}]`

and

`W0 = 0.029938528464044364`.

The result below uses only this weighted four-bank packet and therefore keeps the actual determinant weights; it does not choose a largest tiny minor.

## Theorem 1 — QFORM-RAINBOW-E2-HUB-OR-THREE-DISJOINT-PACKETS-v1

Let `R,S,C,D` be pairwise disjoint finite coordinate sets and let nonnegative weights

`w_e = Delta(r,s;c,d)^2`,  `e=(r,s,c,d) in R x S x C x D`,

have total mass `W=sum_e w_e>0`. For a coordinate `x` define its inclusion marginal

`mu_x = W^{-1} sum_{e: x in e} w_e`.

Fix `0<theta<1/24` and put

`H_theta={x: mu_x>theta}`.

Then `|H_theta|<4/theta`, and at least one of the following holds.

### (HUB)
There is one literal physical coordinate `h in H_theta` whose determinant star has

`W_h := sum_{e: h in e} w_e > (theta/8) W`.

### (THREE-DISJOINT)
There are partitions of each bank into three physical subbanks,

`R=R_1 sqcup R_2 sqcup R_3`, and similarly `S,C,D`,

such that the three restricted packets

`W_j := sum_{r in R_j,s in S_j,c in C_j,d in D_j} Delta(r,s;c,d)^2`

satisfy, simultaneously,

`W_j >= c_theta W` for `j=1,2,3`,

where

`c_theta = (1-24 theta)/(8*3^12)`.

In particular, the twelve physical banks `R_j,S_j,C_j,D_j` are mutually disjoint across `j`; hence the three determinant packets use three disjoint sets of source coordinates.

### Proof

Normalize `p_e=w_e/W`. Every edge uses exactly four coordinates, so

`sum_x mu_x = 4`.

Therefore `|H_theta| theta < 4`, proving `|H_theta|<4/theta`.

Let `I` be the event that a `p`-distributed edge meets `H_theta`.

If `P(I)>1/2`, then

`sum_{h in H_theta} W_h = sum_e w_e |e cap H_theta| >= sum_{e:e cap H_theta != empty} w_e > W/2`.

Since `|H_theta|<4/theta`, one `h` has

`W_h > W/(2|H_theta|) > (theta/8)W`.

This is (HUB).

Assume now `q:=P(I^c)>=1/2` and condition the edge law on avoiding `H_theta`. Let `mu'_x` be the conditioned coordinate marginals. For every residual coordinate,

`mu'_x <= mu_x/q <= 2 theta`,

and still `sum_x mu'_x=4`.

For two independent conditioned edges `E,E'`, a union bound over coordinates gives

`P(E cap E' != empty) <= sum_x (mu'_x)^2 <= (max_x mu'_x) sum_x mu'_x <= 8 theta`.

For three independent conditioned edges `E_1,E_2,E_3`, another union bound over the three pairs yields

`P(E_1,E_2,E_3 pairwise disjoint) >= 1-24 theta`.

Consequently the ordered disjoint-triple determinant currency

`M_3 := sum_{e_1,e_2,e_3 pairwise disjoint} w_{e_1} w_{e_2} w_{e_3}`

obeys

`M_3 >= (qW)^3 (1-24 theta) >= W^3 (1-24 theta)/8`.      (1)

Now independently color every coordinate in each of the four banks uniformly with colors `1,2,3`. Let `W_j` be the weight of edges whose four coordinates all receive color `j`. Expanding `W_1W_2W_3`, a triple with any shared coordinate contributes zero because that coordinate cannot simultaneously have two different colors. A pairwise-disjoint ordered triple contributes with probability exactly `3^{-12}`. Hence the exact expectation identity

`E[W_1 W_2 W_3] = 3^{-12} M_3`.                         (2)

By (1)-(2), some coloring has

`W_1W_2W_3 >= [(1-24 theta)/(8*3^12)] W^3 = c_theta W^3`.

Each `W_j<=W`; therefore for every `j`,

`W_j W^2 >= W_1W_2W_3 >= c_theta W^3`,

so `W_j>=c_theta W`. This proves (THREE-DISJOINT). QED.

## Live constants

Take `theta=1/96`. Then

`|H_theta|<384`.

The HUB branch gives

`W_h > W/768 > W0/768 = 3.8982458937557764e-5`.

The THREE-DISJOINT branch has

`c_theta = (3/4)/(8*3^12) = 1/(32*3^11) = 1/5668704`,

so each of the three source-disjoint actual packets obeys

`W_j > W0/5668704 = 5.28137092076855e-9`.

The constants are intentionally crude but dimension-free. The point is the structural trichotomy in source coordinates, not optimization.

## Theorem 2 — QFORM-RAINBOW-HUB-SLOPE-OR-TRANSVERSE-v1

Suppose the HUB coordinate lies in `R`; the other three locations are symmetric. Put

`a=(M_{h,c})_{c in C}`, `b=(M_{h,d})_{d in D}`,

and for `s in S` put

`c_s=(M_{s,c})_{c in C}`, `d_s=(M_{s,d})_{d in D}`.

Then the entire hub star is

`W_h = sum_s [ ||a||^2 ||d_s||^2 + ||b||^2 ||c_s||^2 - 2 <a,c_s><b,d_s> ]`.    (3)

If `a` and `b` are both nonzero, define

`alpha_s=<a,c_s>/||a||^2`, `beta_s=<b,d_s>/||b||^2`,

`r_s=c_s-alpha_s a`, `t_s=d_s-beta_s b`.

Then the exact orthogonal decomposition is

`W_h = ||a||^2||b||^2 sum_s (alpha_s-beta_s)^2
       + ||a||^2 sum_s ||t_s||^2
       + ||b||^2 sum_s ||r_s||^2`.                         (4)

Thus at least one of the three displayed nonnegative currencies is at least `W_h/3`.

If `a=0`, then necessarily `b!=0` on a positive hub star and (3) reduces exactly to

`W_h=||b||^2 sum_s ||c_s||^2`.

If `b=0`, symmetrically

`W_h=||a||^2 sum_s ||d_s||^2`.

### Proof

For each `s`, expand

`sum_{c,d} (a_c d_{s,d} - b_d c_{s,c})^2`

and sum over `s` to obtain (3). For nonzero `a,b`, substitute

`c_s=alpha_s a+r_s`, `d_s=beta_s b+t_s`,

with `r_s perp a`, `t_s perp b`. Then

`||a||^2||d_s||^2 + ||b||^2||c_s||^2 -2<a,c_s><b,d_s>`

`=||a||^2||b||^2(alpha_s-beta_s)^2 + ||a||^2||t_s||^2 + ||b||^2||r_s||^2`.

Summation gives (4). The zero-vector cases follow directly from (3). QED.

At the live `theta=1/96` HUB scale, at least one of the three currencies in (4), or the corresponding degenerate product, is strictly larger than

`W0/2304 = 1.2994152979185922e-5`.

This is an exact aggregate compiler: the hub branch cannot consist solely of individually tiny unexplained minors; it becomes either a bank-to-bank slope mismatch or a transverse residual-energy packet.

## Designated partner account02/B07 applied to an actual inequality

Latest completed compatible designated-partner handoff read at startup:

`math-research-brain/scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B07/20260924T073847Z-account02-B07-qform-r50.md`.

Its completed `QFORM-PAIRBLOCK-RANK-CANCELLATION-CORE-v1` states that for a literal physical pair-block diagonal `B`, rank-`r` correction, and operator tail `eta`, at least `r+3` pair-block singular directions at scale `d>eta` force an actual principal core on at most `2(r+3)` coordinates with `s_3>=d-eta`, and hence

`||p_Q||_infinity <= 2 sqrt(12 pi (r+3))/(d-eta)`.

Apply it at the live partner values

`r=24`, `eta=D0=5.438340267613160e-4`, `d=2D0`.

If the pair-block compiler has at least 27 threshold directions, then a literal physical core of at most 54 coordinates has

`s_3 >= D0`,

and the full ambient essential-density bound is

`||p_Q||_infinity <= 2 sqrt(12 pi*27)/D0 = 117330.53742994918 < 117331`.

Thus that bounded-support pair-block failure mode is genuinely paid. The new weighted-rainbow theorem is aimed at the complementary determinant-diffuse/hub geometry; it does not silently infer 27 pair directions from rainbow mass alone.

Partner source records: account02 canonical math commit `09dc85f76cccfd0668da416f6f0d4ded36e6dcf9`; source-refresh addendum `d2dab4035cc3df2405f67bf7b586d050bd14086b`.

## What this changes

The r43 packet `W>0.0299385` is no longer merely one aggregate four-bank number. Dimension-free coordinate selection now gives exactly two robust outcomes:

1. a physical hub with determinant-star mass `>3.898e-5`, further decomposed exactly into slope mismatch / transverse energy; or
2. three mutually source-disjoint actual rainbow determinant packets, each carrying at least `5.281e-9` mass.

The second outcome is particularly aligned with the owner target: it produces three determinant resources on three disjoint groups of independent source coordinates without rotating the product law. It is not yet a density receiver; arbitrary same-bank curvature and cross-couplings between the three groups remain and must be retained.

## Next obligation

`QFORM-THREE-SOURCE-DISJOINT-RAINBOW-PACKETS-RECEIVER-v1`: use the three disjoint determinant packets in a dependence-safe Fourier/coarea receiver, or prove that failure of such a receiver regenerates a paid physical principal core/cross-E3 branch.

Parallel HUB obligation: combine the exact slope/transverse decomposition (4) with the existing physical-hub receivers without taking a worst slice that discards the determinant-star scale.

No continuity claim is made from either new theorem. Full QFORM remains OPEN.
