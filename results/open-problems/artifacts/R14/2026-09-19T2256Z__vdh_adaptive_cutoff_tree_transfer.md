# VDH-8.3-DUALITY — adaptive third-moment cutoff and exact tree-census transfer

**Status:** theorem-sized R14 self-check / PARTIAL source-level strengthening.  This is not an independent audit, not a novelty certificate, and not a repository closure claim.

## 1. Purpose

The current VDH route already has a sharp post-giant `C_2` proof candidate and a quenched fresh-pairing duality statement.  The remaining technical question in the last R14 recovery was whether one can port the bounded-degree extreme-component mechanism to the finite-third-moment triangular array without assuming a quantitative rate of uniform integrability.

The answer below is **yes at the tail-removal/second-moment-transfer level**.  Uniform integrability alone permits an adaptive cutoff `K_n=o(1/epsilon_n)` which removes only `o(n epsilon_n)` second-degree mass, `o(n epsilon_n^2)` half-edge mass, and `o(n)` third-degree mass.  Moreover, tree-component first and joint factorial moments in the full configuration model are related *exactly* to those in the parity-corrected cutoff model.  On the extreme scale, the first-moment distortion is only `N_n^{o(1)}` and the normalized two-component distortion is `1+o(1)`.

Thus the unbounded tail itself is not the remaining lower-bound obstruction.  The residual analytic theorem is a Riordan-type subcritical lower-extreme theorem for a deterministic core satisfying `epsilon_n d_max -> 0`.

This route uses the previous R14 methods selected for the proof-capable follow-up:

- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** isolate and prove the cutoff/transfer theorem rather than another full-profile CLT;
- **B21 — ASK WHO ELSE HAS THIS SHAPE:** use the exact Prüfer/configuration-model tree census appearing in Riordan's bounded-degree proof and, in a recent form, Chen (2026);
- **B30 — ONE SCALE AT A TIME:** remove the high-degree tail, transfer one- and two-component counts, and leave only the `epsilon d_max -> 0` core theorem.

## 2. Assumptions and notation

For each `n`, let

`d^(n)=(d_1,...,d_n)`

be a deterministic degree sequence with even half-edge sum

`ell_n = sum_i d_i`,

and assume

`ell_n/n -> mu in (0,infinity)`.

Let `epsilon_n -> 0` and

`N_n := n epsilon_n^3 -> infinity`.

Assume uniform integrability of the third degree moment in the strong triangular-array form

`G(x) := sup_m m^{-1} sum_{i=1}^m (d_i^(m))^3 1{d_i^(m)>x} -> 0`

as `x->infinity`.

When criticality parameters are invoked, write

`nu_n = ell_n^{-1} sum_i d_i(d_i-1)`

and

`R_n = ell_n^{-1} sum_i d_i(d_i-2)^2`.

## 3. The adaptive cutoff theorem

### Theorem 3.1

There are deterministic cutoffs `K_n` and vertex sets `L_n` such that:

1. `K_n -> infinity` and `epsilon_n K_n -> 0`;
2. every vertex in `L_n` has degree at most `K_n`;
3. `ell_n^L := sum_{i in L_n} d_i` is even;
4. with `H_n := [n]\L_n`,

   `n^{-1} sum_{i in H_n} d_i = o(epsilon_n^2)`,

   `n^{-1} sum_{i in H_n} d_i^2 = o(epsilon_n)`,

   `n^{-1} sum_{i in H_n} d_i^3 = o(1)`.

Consequently, if

`nu_n = 1-epsilon_n+o(epsilon_n)` and `R_n -> R_*>0`,

then the cutoff sequence satisfies

`nu_n^L = 1-epsilon_n+o(epsilon_n)`,

`R_n^L -> R_*`,

where the parameters are computed from the retained degree sequence.

### Proof

Put

`t_n := epsilon_n^{-1/2}`,

`h_n := G(t_n)`,

`a_n := max(epsilon_n^{1/2}, h_n^{1/3})`,

and

`K_n := floor(a_n/epsilon_n)`.

Since `h_n->0`, we have `a_n->0`.  Also `a_n>=epsilon_n^{1/2}`, so `K_n>=epsilon_n^{-1/2}-1 -> infinity`, while

`epsilon_n K_n <= a_n -> 0`.

First retain all vertices with `d_i<=K_n`.  Since `K_n>=t_n` for all large `n`, the discarded third moment satisfies

`n^{-1} sum_{d_i>K_n} d_i^3 <= h_n <= a_n^3 = o(1)`.

For `d_i>K_n`, successively use `d_i^2<=d_i^3/K_n` and `d_i<=d_i^2/K_n`:

`n^{-1} sum_{d_i>K_n} d_i^2 <= (epsilon_n/a_n) h_n <= epsilon_n a_n^2 = o(epsilon_n)`,

and

`n^{-1} sum_{d_i>K_n} d_i <= (epsilon_n/a_n) epsilon_n a_n^2 = epsilon_n^2 a_n = o(epsilon_n^2)`.

If the retained half-edge sum is even, stop.  If it is odd, remove one retained vertex of odd degree; such a vertex exists because an odd sum contains an odd summand.  Its degree is at most `K_n`.  Since `n=N_n/epsilon_n^3`, the extra losses satisfy

`K_n/n <= a_n epsilon_n^2/N_n = o(epsilon_n^2)`,

`K_n^2/n <= a_n^2 epsilon_n/N_n = o(epsilon_n)`,

`K_n^3/n <= a_n^3/N_n = o(1)`.

This proves items 1--4.

For the criticality parameters, the discarded contribution to `sum d_i(d_i-1)` is at most the discarded second moment plus the first moment, hence `o(n epsilon_n)`.  The denominator changes by `o(n epsilon_n^2)`.  Since `ell_n=Theta(n)`,

`nu_n^L = 1-epsilon_n+o(epsilon_n)`.

Similarly `d(d-2)^2 <= C(d^3+d)` for a universal constant `C`, so the discarded numerator in `R_n` is `o(n)` and the denominator changes by `o(n)`.  Therefore `R_n^L->R_*`.  QED.

## 4. Exact tree-census transfer

Let `CM(d)` be the full configuration multigraph and `CM(d^L)` the configuration model on the retained vertices.  Because `ell_n^L` is even, both are defined without an auxiliary parity convention.

For `k>=2`, let

- `T_k^full(L)` be the number of size-`k` tree components of `CM(d)` all of whose vertices lie in `L_n`;
- `T_k^L` be the number of size-`k` tree components of `CM(d^L)`.

Set `ell=ell_n`, `ell_L=ell_n^L`, and

`r_n(k) := product_{j=0}^{k-2} [ell_L-(2j+1)]/[ell-(2j+1)]`.

### Theorem 4.1 (exact first moment)

For every `k` with `2k<=ell_L`,

`E T_k^full(L) = r_n(k) E T_k^L`.

### Proof

Fix `A subseteq L_n`, `|A|=k`.  If `sum_{v in A}d_v != 2k-2`, `A` cannot be a tree component in either model.  Otherwise Prüfer enumeration gives exactly

`(k-2)! product_{v in A} d_v`

internal half-edge pairings which form a tree on `A`.  Hence

`P_full(A tree component) = (k-2)! product_{v in A}d_v * (ell-2k+1)!!/(ell-1)!!`,

while

`P_L(A tree component) = (k-2)! product_{v in A}d_v * (ell_L-2k+1)!!/(ell_L-1)!!`.

Their ratio is exactly `r_n(k)`.  Sum over all `A`.  QED.

For `k,l>=2`, define the ordered joint factorial count

`J_{k,l}=T_k T_l` if `k!=l`, and `J_{k,k}=T_k(T_k-1)`.

### Theorem 4.2 (exact two-component factorial moment)

For every `k,l` with `2(k+l-2)<=ell_L`,

`E J_{k,l}^full(L) = r_n(k+l-1) E J_{k,l}^L`.

### Proof

Sum over ordered disjoint vertex sets `A,B subseteq L_n` of sizes `k,l`.  If their degree sums are not `2k-2` and `2l-2`, the contribution is zero in both models.  Otherwise the internal tree-pairing factors are identical in the two models, while the remaining matching factors are respectively

`(ell-2k-2l+3)!!/(ell-1)!!`

and

`(ell_L-2k-2l+3)!!/(ell_L-1)!!`.

The ratio is `r_n(k+l-1)`.  QED.

These identities are exact finite combinatorics, not asymptotic approximations.

## 5. Extreme-scale asymptotics of the transfer factor

Let

`s_n = C epsilon_n^{-2} log N_n`

for a fixed `C<infinity`, and write

`t_n^H := ell_n-ell_n^L = o(n epsilon_n^2)`

by Theorem 3.1.  Since

`s_n/n = O(epsilon_n log N_n/N_n) -> 0`,

all denominators below are uniformly comparable with `ell_n`.

### Proposition 5.1

Uniformly for `2<=k<=s_n`,

`log r_n(k) = o(log N_n)`.

Hence `r_n(k)=N_n^{o(1)}` uniformly on the entire leading extreme scale.

### Proof

Each factor of `r_n(k)` is

`1 - t_n^H/[ell_n-(2j+1)]`.

For large `n`, the fraction is at most `1/2`, so `-log(1-x)<=2x` gives

`|log r_n(k)| <= C t_n^H k/ell_n`.

Now `t_n^H/ell_n=o(epsilon_n^2)` and `k<=C epsilon_n^{-2}log N_n`, proving the claim.  QED.

### Proposition 5.2 (narrow-window flatness)

If `I_n` is any integer interval contained in `[2,s_n]` with diameter `O(epsilon_n^{-2})`, then

`sup_{k,l in I_n} |log(r_n(k)/r_n(l))| -> 0`.

### Proof

The same one-factor bound gives

`|log r_n(k)-log r_n(l)| <= C(t_n^H/ell_n)|k-l| = o(epsilon_n^2) O(epsilon_n^{-2})=o(1)`.  QED.

### Proposition 5.3 (normalized two-component transfer)

Uniformly for `2<=k,l<=s_n`,

`r_n(k+l-1)/(r_n(k)r_n(l)) -> 1`.

### Proof

Write

`f_j = log(1-t_n^H/[ell_n-(2j+1)])`.

Let `m=k-1` and `q=l-1`.  After cancelling the first `m` terms,

`log r_n(k+l-1)-log r_n(k)-log r_n(l)
 = sum_{j=0}^{q-1}(f_{j+m}-f_j)`.

For `j,m<=s_n`, the map in `j` is Lipschitz with constant at most `C t_n^H/ell_n^2`.  Therefore the absolute value above is at most

`C t_n^H m q/ell_n^2 <= C (t_n^H/ell_n)(s_n^2/ell_n)`.

Using `t_n^H/ell_n=o(epsilon_n^2)` and `ell_n=Theta(n)=Theta(N_n/epsilon_n^3)`,

`s_n^2/ell_n = O(log^2 N_n/(N_n epsilon_n))`.

Thus the product is

`o(epsilon_n log^2 N_n/N_n)=o(1)`.

Exponentiating proves the result.  QED.

## 6. Consequence for a second-moment lower proof

Let `I_n` be a window of width `O(epsilon_n^{-2})` inside the leading extreme scale, and set

`Z_n^L=sum_{k in I_n}T_k^L`,

`Z_n^full=sum_{k in I_n}T_k^full(L)`.

Suppose a lower-extreme theorem for the cutoff core supplies

`E Z_n^L >= N_n^{c+o(1)}` for some fixed `c>0`,

and

`E[Z_n^L(Z_n^L-1)]/(E Z_n^L)^2 -> 1`.

By Propositions 5.1--5.3 and narrow-window flatness,

`E Z_n^full = r_n(k_n)(1+o(1)) E Z_n^L`

for any `k_n in I_n`, the expectation still diverges, and

`E[Z_n^full(Z_n^full-1)]/(E Z_n^full)^2 -> 1`.

Therefore `P(Z_n^full>0)->1` by the second-moment method.

So **any Riordan-type lower-extreme theorem for the adaptive core transfers to the original unbounded finite-third-moment configuration model without loss of the leading constant.**

## 7. What this does and does not settle

This theorem removes a specific obstruction recorded in the previous VDH route: a source-uniform quantitative rate of third-moment uniform integrability is *not* needed to obtain a moment-preserving `o(1/epsilon_n)` core, and the full-model tree-census second moment can be transferred exactly through the deleted tail.

It does **not** by itself prove the missing core lower theorem.  The remaining self-contained analytic target is now:

> For deterministic barely-subcritical configuration models with `Q_n=-epsilon_n(1+o(1))`, `R_n->R_*>0`, `N_n=n epsilon_n^3->infinity`, finite-third-moment control, and `epsilon_n d_max->0`, prove
> `L_1 >= (1-o_p(1)) 2R_* epsilon_n^{-2} log N_n`.

Riordan (2012) proves this with uniformly bounded maximum degree and explicitly remarks that his proof extends when the maximum degree grows reasonably slowly, without quantifying the admissible growth.  Chen (2026) gives a recent exact tree-component first/second-moment implementation in a different random-degree model and explicitly points to supercritical second-largest-component extensions as future work.  Neither source, as checked here, supplies the exact deterministic triangular-array theorem above.

In the VDH repository chain, HARD7-04 already has a separate collared lower-bound proof candidate.  The present result is therefore best viewed as a **clean tail-removal/transfer lemma for audit and future simplification**, not as a duplicate source-closure claim.
