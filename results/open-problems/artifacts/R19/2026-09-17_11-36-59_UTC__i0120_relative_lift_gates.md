# R19 / I0120 — relation-preserving prime gates and a support-two pilot

Date: 2026-09-17 UTC.  
Status: **PARTIAL / source OPEN / no `N_LR` movement**.

## 1. Continuity and current source boundary

The active R19 claim is now `I0120`, the fifteen-total-runner case `LRC(14)`, under the create-only claim `operations/claims/I0120.md`. The predecessor targets remain preserved and are not reopened.

- `I0084` remains the frozen Hasebe--Ueda arXiv-v2 Conjecture 5.5 package, where `mu*S_t` is **ordinary classical convolution** even when `S_t` is the law of a free stable process. A new independent P26 audit this run cycle gives `P26-AUDIT-R19-I0084-C010-SPARSE-BUMP-20 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED / PARENT_SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`, and reconciles it with the already-existing distinct R18 C010 audit. This closes that abstract C010 claim at the two-audit level, but it does not close or reopen the parent frozen I0084 source package.
- `I0110` remains rotated after its six-run saturated `M_9=9/9` campaign; the ELE source-scope failure found by P26 remains preserved.

Fresh primary-source checks on 2026-09-17 still put the full Lonely Runner record at `LRC(13)` (fourteen total runners): J. Allikvere, arXiv:2609.02604 (2026-09-02). Beck--Everett, arXiv:2609.06259 (2026-09-05), prove that every counterexample or tight instance has a harmful short integer relation. A bounded fresh search found no primary-source proof or refutation of general `LRC(14)`. This is dated negative search evidence, not a novelty certificate.

The previous R19 run proved a relation-indexed product criterion using

`J_a(14,p) = J(14,p) intersect H_a(p)`.

The main new observation here is that this still throws away the most valuable information: **the exact harmful relation persists through every lift**. The lift engine should never leave that hyperplane.

## 2. Relative eventual properness

Write `LRC(k)` for the stationary formulation with `k` nonzero integer speeds and threshold `1/(k+1)`. Let `m=(m_1,...,m_k)` be a primitive nonzero integer relation vector, let `p` be prime, and let

`H_m(p) = {v in (F_p^*)^k : m.v = 0 mod p}`.

For `v in H_m(p)` and a positive integer `l`, call a lift `w in Z_{p,l}^k` **m-compatible** when

1. `w = v mod p`, and
2. `m.w = 0 mod lp`.

Call `v` **m-relatively eventually proper** if some level `l` has the property that every m-compatible lift of `v` is `(k,p,l)`-proper in the Sungkawichai--Trakulthongchai sense. Let

`J_m^rel(k,p)`

be the subset of `H_m(p)` that is not m-relatively eventually proper.

This is deliberately weaker than global eventual properness. Indeed, if all lifts are proper then certainly all relation-compatible lifts are proper, hence

`J_m^rel(k,p) subseteq J(k,p) intersect H_m(p)`.

Thus asking for `J_m^rel(k,p)=empty` is never stronger than the relation-sliced gate used in the preceding R19 run.

## 3. The actual counterexample cannot escape the relation hyperplane

### Lemma R19-LR3 — relative-lift exclusion

Assume `k>=3` and `LRC(k-1)`. Let `u=(u_1,...,u_k)` be a primitive integer counterexample to `LRC(k)` satisfying the exact integer relation

`m.u=0`.

Let `p` be prime and suppose `p` divides none of the coordinates of `u`. Then

`u mod p in J_m^rel(k,p)`.

### Proof

Suppose not. Then for some level `l`, every m-compatible lift of `u mod p` is proper. Reduce the actual integer vector `u` modulo `lp`. It is an m-compatible lift because `m.u=0` as an integer equality.

If this lift is proper by the witness clause, a time `t in (lp)^(-1) Z` is a lonely witness for the actual integer tuple, contradiction.

If it is proper by the gcd clause, then for some `i`

`d = gcd(l,u_1,...,omit u_i,...,u_k)>1`.

Primitivity gives `d` not dividing `u_i`. Put `g=gcd(d,u_i)` and `q=d/g>=2`. By `LRC(k-1)` applied to the other speeds `u_j/d`, choose `s` so that

`||s u_j/d|| >= 1/k`, `j!=i`.

For `t=(s+r)/d`, integer `r`, those `k-1` distances are unchanged. As `r` varies mod `d`, the exceptional coordinate runs through a translate of the `q`-point uniform grid. One grid point has distance at least `1/4` from the nearest integer (`q=2`) or at least `1/3` (`q>=3`). Since `1/4 >= 1/(k+1)` for `k>=3`, one choice of `r` is a lonely witness for every coordinate, contradiction.

Therefore the actual counterexample residue cannot be m-relatively eventually proper. QED.

## 4. Stronger relation-indexed product criterion

Let `A_14` be the 17,574 primitive harmful absolute-coefficient shapes from the preceding run. For a shape `a`, sign-change the corresponding speed coordinates so that the exact relation becomes

`a.u=0`

with positive nonzero coefficients on the support; this does not alter any lonely-runner distance or the absolute speed product.

### Theorem R19-LR4 — relative relation gates suffice

Assume `LRC(13)`. Suppose that for every `a in A_14` there is a finite set `P_a` of primes `p>31` such that

1. `J_a^rel(14,p)=empty` for every `p in P_a`, and
2. `product_{p in P_a} p >= B_14`, where

   `B_14=(105^13/14)^14=105^182/14^14`.

Then `LRC(14)` holds.

### Proof

If a primitive counterexample existed, Beck--Everett would supply one of the shapes `a`. Fix `p in P_a`. If `p` divided none of the speeds, Lemma R19-LR3 would put the residue in `J_a^rel(14,p)`, contradicting its emptiness. Hence every `p in P_a` divides the absolute speed product, so

`|u_1...u_14| >= product_{p in P_a} p >= B_14`.

This contradicts the finite-checking product bound for primitive counterexamples, using the already-proved `LRC(13)`. QED.

This strictly improves the previous sufficient condition: it is enough to kill only relation-preserving lift branches, not every improper lift that happens to start on the same level-one hyperplane.

## 5. Exact all-level branching reduction

The relation constraint does more than thin level one.

### Proposition R19-LR5 — a primitive relation removes one full lift dimension at every level

Let `m in Z^k` be primitive, `v in H_m(p)`, and let `l>=1`. The number of m-compatible lifts of `v` from modulus `p` to modulus `lp` is exactly

`l^(k-1)`.

The unrestricted lift fiber has size `l^k`; therefore relation preservation gives an **exact factor-l reduction** in the raw lift fiber.

### Proof

Choose integer representatives of `v`. Every lift has a unique form

`w=v+p q`, `q in (Z/lZ)^k`.

Since `m.v=0 mod p`, write `m.v=p c`. The relation condition modulo `lp` is

`m.q = -c mod l`.

The homomorphism

`phi_m : (Z/lZ)^k -> Z/lZ`, `q -> m.q`

is surjective because `gcd(m_1,...,m_k)=1`; Bezout gives an integer linear combination of the coefficients equal to one, hence also a preimage of one modulo `l`. Its kernel therefore has size `l^(k-1)`, and every fiber has that same size. QED.

For `k=14`, the relation-compatible fiber is exactly `l^13`, not `l^14`. Equivalently, at every prime-factor lift stage `c`, the branch count is `c^13` rather than `c^14`. In particular the repeated binary stages used in the current record proof save a factor two **at every stage**, and a terminal `c=7` stage saves a further factor seven. This is the principal algorithmic gain of the present run.

## 6. Support-two shapes after the unit/sign/permutation quotient

The preceding run's raw hyperplane count saved a factor at least `p-1` before symmetries. The natural question was whether that reduction survives the actual level-one orbit quotient.

Take a primitive support-two shape `(a,b)` with `a+b` odd and at most 31, and write the exact signed relation as

`a u_i = b u_j`.

For a prime `p>31`, fold signs and use the global unit action to normalize the marked coordinate `u_i` to folded class `1`. The marked partner is then forced to

`r=[a b^{-1}] in F_p^*/{+/-1}`.

Put `n=(p-1)/2`. A relation-marked normalized tuple then has only twelve unmarked folded coordinates, so before applying the level-one witness filter there are at most

`C(n+11,12)`

multisets. An unrestricted tuple with one marked normalized coordinate has thirteen remaining folded coordinates, hence at most

`C(n+12,13)`

multisets. The exact pre-cover compression ratio is therefore

`C(n+12,13)/C(n+11,12) = (n+12)/13 = (p+23)/26`.

Thus the raw factor `p-1` is substantially consumed by orbit normalization at the first small primes, although the gain remains linear in `p` asymptotically.

There is also an exact set-cover representation. For folded speed `v`, let

`D_p(v)={t : 15 d_p(tv)<p}`

be its bad-time set on the folded nonzero time classes. Let `C_{p,r}(s)` be the number of size-`s` supports containing `{1,r}` whose bad-time sets cover every folded time class. For a covering support of size `s`, the twelve unmarked coordinates must use each of the `s-2` non-marked support classes at least once, while the two marked classes may receive any extra multiplicity. Stars-and-bars gives exactly

`C(13,s-1)`

relation-marked normalized tuples over that support. Hence

`N_p(r)=sum_{s=2}^{14} C_{p,r}(s) C(13,s-1)`.

This formula is what the exact checker evaluates.

## 7. Methods #8, #20, #24 — exact first-three-prime pilot

For `p=37,41,43`,

`floor((p-1)/15)=2`.

Therefore every folded bad-time set is exactly a multiplicative translate of `{1,2}`. Level-one improper supports are precisely edge covers of the graph on `F_p^*/{+/-1}` whose edges are `{x,2x}`. This is the promised discretization (#8): the first three prime gates reduce to finite cycle-edge-cover problems.

The executed exact checker gives:

| p | n | normalized unrestricted marked cover candidates | `r=2` candidates | `r=4` candidates | minimum ratio classes | maximum ratio classes |
|---:|---:|---:|---:|---:|---|---|
| 37 | 18 | 217646 | 87802 | 163736 | `{2,18}` | `{4,9}` |
| 41 | 20 | 81081 | 27742 | 62635 | `{2,20}` | `{4,10}` |
| 43 | 21 | 35280 | 11907 | 26068 | `{2,21}` | `{4,11}` |

The paired classes are inverses in the folded multiplicative group. Among all 106 primitive support-two harmful shapes, the class containing the tight Dirichlet shape `(2,1)` is the **smallest** relation-marked level-one family at each of these three primes, while the class containing `(4,1)` is the **largest** (up to inversion).

This answers #20 and #24 in a useful way.

- **Why the naive algorithmic hope fails:** the raw `p-1` hyperplane saving does not appear as anything close to a factor `p` after the unit quotient at the first gates. For the hardest `r=4` slice, the normalized cover-family reduction is only `217646/163736`, `81081/62635`, and `35280/26068`, i.e. roughly 1.3-fold. The level-one relation filter alone is not enough.
- **Extremal pilot:** `(2,1)` is not the right stress test. The first three exact gates identify `(4,1)` (and the inverse ratio class) as a harder support-two benchmark. The next implementation should start there.
- **New leverage:** unlike the modest small-prime level-one reduction, Proposition R19-LR5 gives an exact factor `l` through the entire relation-preserving lift fiber. The relation must therefore be enforced **at every lift stage**, not only before level-one generation.

The checker also records the full covering-support histograms for `r=2`, `r=4`, and the normalized unrestricted family at all three primes.

## 8. What remains

This run does **not** prove `LRC(14)` and therefore does not move the frozen metric `N_LR=14`.

The next concrete obligation is now sharper than in the previous report:

1. implement the relative lift tree `J_a^rel`, rather than `J intersect H_a`;
2. start with the hardest support-two shape `(4,1)` at `p=37,41,43`;
3. carry the exact relation congruence through every binary/terminal lift and compare surviving improper fibers to the unrestricted pipeline;
4. only then scale to the remaining support-two shapes and higher-support sign patterns.

Suggested next new-method moves: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

Prior-art note: bounded searches on 2026-09-17 for combinations of `Lonely Runner`, `relation-preserving`, `prime gate`, `eventual properness`, and `hyperplane lift` found the current Allikvere and Beck--Everett papers but no primary source stating this relative-lift prime-product criterion. That is negative search evidence only; publication novelty is **UNVERIFIED**.