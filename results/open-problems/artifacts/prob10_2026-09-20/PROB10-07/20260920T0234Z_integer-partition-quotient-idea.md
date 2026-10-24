# PROB10-07 idea before code — quotient the complete-bipartite transfer by terminal symmetry

Runtime model/effort: **UNVERIFIED**. GPT-6 maximum was requested; no authenticated model/effort telemetry is exposed.

## Exact target and nonoverlap

The target is the Grimmett–Winkler pairwise inequality for the uniform measure on **all forests**. P14/HARD10-01 own the all-graphs-through-nine census and generic 3-separator obstruction. NM13-04 owns split-graph terminal transfers / port-field atoms. NM13-08 owns two-terminal PF series/parallel macro-composition. This note instead continues PROB10-07's complete-bipartite `K_{m,n}` route.

The preceding PROB10-07 report proves all `K_{m,n}` with `3<=m<=9`, all `n>=1`, using the full Bell-partition transfer. The obstacle to extending that calculation is not the mathematics but the `B_m` state count (`B_9=21147`, `B_10=115975`, ...).

## Approach A — symmetry quotient (promising)

After all marked right vertices have been processed, every remaining right vertex is unmarked. Its transfer commutes with the full permutation group of the `m` left terminals. Therefore the relevant state is not a labelled set partition of `[m]`, but only the multiset of block sizes, i.e. an **integer partition** `lambda` of `m`.

Write `lambda=(s_1,...,s_b)`. A new right vertex chooses a spoke subset that is acyclic exactly when it takes at most one vertex from each current block. If a set `J` of current blocks is hit, then those blocks merge. For `|J|>=2`, the transition

`lambda -> sort((s_i : i notin J) union {sum_{i in J}s_i})`

has multiplicity `prod_{i in J} s_i`. The empty choice and all singleton choices leave the state unchanged, with total diagonal multiplicity `m+1`. Hence on the integer-partition quotient

`M_m=(m+1)I+N_m`,   `N_m^m=0`.

If a block size `s` occurs `c_s` times and we choose `r_s` such blocks, the orbit-aggregated transition multiplicity is

`prod_s binom(c_s,r_s) s^{r_s}`.

This reduces the state count from Bell `B_m` to the partition number `p(m)` (`p(10)=42`, `p(20)=627`, `p(30)=5604`).

### Marked initial vectors can also be quotient-compressed

Put the marked right vertices first.

* Total count `Z`: initial state `1^m`, coefficient 1.
* One fixed edge `e=(0,R_1)`: if the first marked star has size `k`, its poststate is `(k,1^{m-k})` with coefficient `C(m-1,k-1)`.
* Same-right pair `R`, edges `(0,R_1),(1,R_1)`: poststate `(k,1^{m-k})`, coefficient `C(m-2,k-2)`.
* Same-left pair `L`, edges `(0,R_1),(0,R_2)`: after two marked stars the union of touched left terminals is one block. For final block size `k`, each of the `k-1` other terminals in that union may belong to the first star or the second star, but not both (a double hit would create a 4-cycle); terminals outside the union belong to neither. Hence the coefficient is `C(m-1,k-1)2^{k-1}`.
* Disjoint pair `D`, edges `(0,R_1),(1,R_2)`: aggregate by whether the first star contains terminal 1. If it does, the final marked part is one block. If not, the second star may either avoid the first block, producing two blocks, or meet it in exactly one vertex, producing one merged block. This gives an explicit `O(m^2)` integer-partition initial vector (to be coded directly and cross-checked against the old Bell transfer for `m<=9`).

With `q=m+1`, let `a_j,b_j,c_j,l_j,d_j` be the sums of the five quotient initial vectors after `N_m^j`. Nilpotence gives exact normalized polynomials

`Z/q^n = sum_j a_j C(n,j)/q^j`,

`E/q^n = q^{-1} sum_j b_j C(n-1,j)/q^j`,

`R/q^n = q^{-1} sum_j c_j C(n-1,j)/q^j`,

`L/q^n = q^{-2} sum_j l_j C(n-2,j)/q^j`,

`D/q^n = q^{-2} sum_j d_j C(n-2,j)/q^j`.

Thus the three Rayleigh numerators are exact rational polynomials in `n`.

## Approach B — try to prove the old unshifted power-basis positivity for all widths

The previous `m<=9` certificates had positive ordinary power-basis coefficients (apart from the expected `n-1` factor for same-right pairs). This would be a very clean all-width induction if true. Before promoting it, the checker must try to falsify it at larger `m`. A single negative coefficient kills this *certificate form* without refuting the Rayleigh inequality itself.

## Approach C — scalar deletion/contraction induction in the number of right vertices

Adding one right vertex is a deletion/contraction sum over legal star subsets. Trying to update a single Rayleigh scalar produces cross terms between distinct terminal-connectivity states; the scalar Rayleigh gap is not closed. The integer-partition transfer should be viewed as the minimal vector-valued replacement of that failed scalar induction. I will not claim an all-graph deletion/contraction closure from this family-specific quotient.

## Planned exact test

1. Reconstruct the integer-partition quotient exactly.
2. Cross-check the quotient coefficient vectors against the already archived Bell-state vectors for `m=6,7,8,9`.
3. Search `m>=10` for a basis in which the three Rayleigh polynomials have manifestly nonnegative coefficients on the physical domain `n>=2`.
4. Only if a new full parameter range is certified, archive a production checker/output and theorem report. A finite list of `n` values will not count as the theorem.
