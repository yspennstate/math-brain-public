# P0072 — loop-erased losange with both non-geodesic terminal edges replaced by arbitrary series chains

Status: **restricted theorem / PROVED CANDIDATE after exact symbolic verification and self-review; full canonical P0072 remains OPEN; publication novelty UNVERIFIED.**

This note continues the R7-02 recovery program for canonical P0072. It extends the previous one-series-chain theorem to a two-parameter family and isolates the first simple graph modification where the current reduction genuinely stops closing.

## 1. Graph family and theorem

Start from the five-edge losange with vertices `s,a,b,t` and edges `s-a`, `a-t`, `s-b`, `b-t`, `a-b`. Replace `s-a` by a simple chain of length `m` and replace `a-t` by a simple chain of length `k`, where `m,k>=2` are integers. All source edge weights start at one. Keep the other three edges unchanged.

The unique `s-t` geodesic is still `R=s-b-t`, of length two. Every edge in the two substituted chains and the bridge `a-b` is non-geodesic.

**Theorem.** For every pair of integers `m,k>=2`, under the source loop-erased reinforcement rule, almost surely every non-geodesic edge has `o(n)` weight after `n` ants, while both edges of `R` have normalized weight tending to one.

Combined with the preceding R7-02 theorem for one arbitrary series subdivision (and its reflected copy), plus the already established five-edge `m=k=1` loop-erased result in this own root, the cumulative R7-02 argument covers the entire integer two-parameter family obtained by replacing `s-a` and `a-t` by arbitrary positive finite series chains.

This is not a proof of canonical P0072 on arbitrary finite graphs and does not address the source uniform-geodesic rule on this whole family.

## 2. Four path counts and exact series suppression

There are exactly four simple `s-t` path types. Write their counts after `n` ants as `L,A,B,R`, with `L+A+B+R=n`:

- `L`: first chain, then second chain;
- `A`: first chain, then bridge `a-b`, then `b-t`;
- `B`: `s-b`, then bridge `b-a`, then second chain;
- `R`: `s-b-t`.

Because every traversal of either substituted chain uses every edge of that chain, unit initialization implies that all edges within each chain retain a common weight. Define

`X=1+L+A`, `Y=1+L+B`, `w=1+A+B`, `d=1+R+B`, `e=1+R+A`.

The first and second chains have effective conductances

`g=X/m`, `h=Y/k`.

The identities

`X+d=t`, `Y+e=t`, `t=n+2`

hold exactly.

For the loop-erased rule, Wilson's weighted spanning-tree identity gives the law of the simple `s-t` path as the `s-t` path in a weighted UST. On the reduced four-vertex network, direct spanning-tree enumeration gives

`Z = ghw + ghd + ghe + gwe + gde + hwd + hde + wde`,

and

`q_L = gh(w+d+e)/Z`,

`q_A = gwe/Z`,

`q_B = hwd/Z`,

`q_R = de(g+h+w)/Z`.

Each formula is simply the total weight of spanning trees whose unique `s-t` path is the indicated path. Their numerators partition all spanning trees, hence they sum to one.

## 3. B3 — stronger two-parameter Lyapunov theorem

Let

`S=X+Y+w` and `V=S/t`.

Every non-geodesic path increments exactly two of `X,Y,w`, while `R` increments none. Therefore

`S=3+2(L+A+B)=2n+3-2R`

and

`V = 2-(2R+1)/t`.

Let

`Delta_{m,k}=q_R-(R+1/2)/t`.

A direct one-step calculation yields

`E[V_{n+1}-V_n | F_n] = -2 Delta_{m,k}/(t+1)`.

Substituting the exact UST formula gives

`Delta_{m,k}=N_{m,k}/(2 m k t Z)`,

where `N_{m,k}` is a polynomial in `L,A,B,R,m,k`. The exact checker verifies the bilinear decomposition around `(m,k)=(2,2)`:

`N_{m,k}=N_{2,2}+(m-2)P_m+(k-2)P_k+(m-2)(k-2)P_{mk}`.

Every coefficient of `N_{2,2}`, `P_m`, `P_k`, and `P_{mk}` is strictly positive. The checker records:

- `N22`: 54 monomials, minimum coefficient 4;
- `Pm`: 54 monomials, minimum coefficient 2;
- `Pk`: 54 monomials, minimum coefficient 2;
- `Pmk`: 46 monomials, minimum coefficient 2.

Moreover

`P_{mk}=(A+B+1)(A+R+1)(B+R+1)(2A+2B+2L+3)`,

and `P_m`, `P_k` factor into a positive linear factor times a positive-coefficient polynomial; their exact expansions are checked symbolically in the archived script. Consequently

`N_{m,k}>0`

for every finite state and every real `m,k>=2`, hence in particular for all integer series lengths in the theorem.

Thus `V_n` is a bounded nonnegative strict supermartingale and converges almost surely. Also

`sum_n Delta_{m,k}(n)/t_n < infinity`

almost surely. Since

`q_R > (R+1/2)/t >= 1/(2t)`,

conditional Borel-Cantelli gives `R_n -> infinity` almost surely.

## 4. Projective zero set

Let normalized path counts converge along a subsequence to

`(ell,alpha,beta,rho)=(L/t,A/t,B/t,R/t)`

on the simplex. Let `N_4` be the degree-four homogeneous part of `N_{m,k}`. The exact symbolic factorization on the face `rho=0` is

`N_4|_{R=0} = 2 A B (A+B+L) (Akm+Ak+Bkm+Bm+Lk+Lm)`.

For positive `m,k`, the final factor is positive away from the origin. Hence on `rho=0` the only projective zeros are `alpha=0` or `beta=0`.

When `rho>0` and at least one of `ell,alpha,beta` is positive, the positive-coefficient form contains a strictly positive degree-four monomial: respectively an `L^2R^2`, `A^3R`, or `B^3R` term. Thus the only other projective zero is the pure `R` vertex `rho=1`.

The compensator summability and the fact that normalized coordinates move by `O(1/t)` per step imply that every projective limit point lies in this zero set. Indeed, on a compact neighborhood separated from the zero set, `Delta_{m,k}` is bounded below by a positive constant; a visit to such a neighborhood lasts `Theta(t)` steps and contributes a fixed positive amount to `sum Delta/t`, so infinitely many such visits are impossible.

Since `V_n` converges and `V=2-(2R+1)/t`, its only possible limits are `0` and `2`. The bad alternative is therefore

`R/t -> 0`,

with projective approach to one of the two faces `rho=0, beta=0` or `rho=0, alpha=0`, including their intersection.

## 5. B5 — continuous anisotropy and the exact invasion lower bound

The algebra above makes sense for real `m,k>=2`, so treat the series lengths as continuous anisotropy parameters. This is useful because the rare-geodesic invasion coefficient is monotone in those parameters and the worst case is the smallest one.

### Face beta=0

Suppose `B/R -> x>=0` along a bad-boundary sequence and `alpha` is the limiting `A/t` coordinate. Exact expansion gives

`t q_R/R -> (x+1) F_beta(alpha;m,k)`,

where

`F_beta(a;m,k) = [a m(k-1)+k+m]/[2+a(k-2)]`.

For `0<=a<=1` and `m,k>=2`,

`partial_m F_beta = [a k-a+1]/[2+a(k-2)] > 0`,

`partial_k F_beta = (1-a)(a m+2)/[2+a(k-2)]^2 >= 0`.

Hence the minimum occurs at `m=k=2`, where

`F_beta(a;2,2)=2+a>=2`.

Thus every approach to this face satisfies

`liminf t q_R/R >= 2`.

### Face alpha=0

By symmetry, with `A/R -> x` and `beta=B/t`,

`t q_R/R -> (x+1) [beta k m-beta k+k+m]/[2+beta(m-2)] >= 2`.

### Pure-L intersection

If `A/R -> x` and `B/R -> y`, then

`t q_R/R -> (k+m)(x+1)(y+1)/[2(x+y+1)]`.

Since `m+k>=4` and

`(x+1)(y+1)-(x+y+1)=xy>=0`,

this is again at least two. The same bound persists under infinite ratio limits by compactification/subsequence extraction.

Therefore, under the bad alternative `R/t->0`, eventually

`q_R >= c R/t`

for any fixed `1<c<2`.

## 6. Supercritical-birth exclusion

We use the same self-contained stochastic lemma as in the preceding one-series theorem.

Let `N_n` be integer-valued, nondecreasing, with Bernoulli increment `Y_{n+1}` of conditional probability `p_n`, and let `t_n=n+O(1)`. There is no event on which simultaneously

1. `N_n -> infinity`;
2. `N_n/t_n -> 0`;
3. eventually `p_n >= c N_n/t_n` for a constant `c>1`.

Proof. Let `H_j=sum_{r=1}^j 1/r`. Then

`H_{N_{n+1}}-H_{N_n}=Y_{n+1}/(N_n+1)`.

Therefore

`H_{N_n}=H_{N_0}+M_n+sum_{r<n} p_r/(N_r+1)`,

where the martingale increments are `(Y_{r+1}-p_r)/(N_r+1)`. Their total quadratic variation is finite almost surely because

`E sum_r p_r/(N_r+1)^2 = E sum_r Y_{r+1}/(N_r+1)^2 <= sum_{j>=N_0} 1/(j+1)^2 < infinity`.

Thus `M_n` converges. Choose `1<c'<c`. Since `N_n->infinity`, eventually

`p_n/(N_n+1) >= c'/t_n`.

Hence `H_{N_n} >= c' log n+O(1)`. But `N_n<=N_0+n` implies `H_{N_n}<=log n+O(1)`, a contradiction.

Apply the lemma with `N_n=R_n`, `p_n=q_R`. We already know `R_n->infinity`; the bad alternative gives `R_n/t_n->0`; and the invasion calculation gives the supercritical lower bound. Contradiction. Therefore

`R/t -> 1`

and equivalently `V_n->0` almost surely.

Since `V=(X+Y+w)/t` with nonnegative summands,

`X/t -> 0`, `Y/t -> 0`, `w/t -> 0`.

Every edge in the first chain has weight `X`, every edge in the second chain has weight `Y`, and the bridge has weight `w`; all are therefore sublinear. Finally `X+d=t` and `Y+e=t`, so

`d/t -> 1`, `e/t -> 1`.

This proves the theorem.

## 7. B30 — first one-chord gluing failure of this proof architecture

The proof works because each substituted chain is a genuine one-dimensional series module: whenever a selected simple path uses the module, it traverses every edge in that module. Hence all module-edge weights stay equal and the whole module is represented by one scalar conductance `X/m` or `Y/k`.

The smallest obvious way to destroy that exact state closure is already visible on the `m=k=2` graph. Let `x` be the internal vertex of the first chain and `y` the internal vertex of the second, and add the single chord `x-y`. Then `s-x-y-t` is a legal simple `s-t` path. Reinforcing it changes the two first-chain edge weights from `(1,1)` to `(2,1)` and the two second-chain edge weights from `(1,1)` to `(1,2)`. Thus a single legal loop-erased path destroys both chain-equality invariants.

So the obstruction is exact and local: after this one chord, neither chain can be series-suppressed to one scalar whose increment is determined only by the outer four path counts. The identities `X+d=t`, `Y+e=t` and the four-path Markov closure that power the Lyapunov polynomial are no longer a closed state description.

This is not evidence that P0072 fails on the chorded graph. It identifies the first concrete gluing step for which the present proof architecture ceases to apply and therefore specifies the next genuinely new ingredient required: a Lyapunov function that controls unequal conductances inside a module, or a higher-dimensional electrical reduction that survives partial module traversal.

## 8. Exact verification

The executed symbolic checker is

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T101700Z__P0072_double_series_exact_checker.py`.

Its archived output is

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T101700Z__P0072_double_series_exact_checker.out`.

The output verifies the UST probability sum, positive-coefficient bilinear drift decomposition, the exact projective boundary factorization, the anisotropy derivative identities, the pure-L compactification identity, and the one-chord chain-equality failure. It ends `ALL_EXACT_CHECKS_PASS`.

## 9. Scope and literature status

Canonical source: Aletti et al., *Open Problems in Stochastic Reinforcement Models* (2025), Section 2 main conjecture, source PDF `https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`; parent: Kious–Mailler–Schapira, *Finding geodesics on graphs using reinforcement learning*, Ann. Appl. Probab. 32(5) (2022), arXiv:2010.04820.

Bounded current check on 2026-09-18: Mailler–Varin, arXiv:2601.22855, studies a modified two-nest process on triangle-series-parallel graphs and does not resolve the original one-nest arbitrary-finite-graph conjecture. No later unrestricted resolution was recovered in the bounded search. Search miss is negative evidence only; worldwide openness and publication novelty remain UNVERIFIED.

Full canonical P0072 remains OPEN/PARTIAL in this track because arbitrary finite graphs and both source rules are required for source closure. The frozen metric `C_P0072` therefore remains zero.
