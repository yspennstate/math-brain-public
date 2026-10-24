# I0120 / R19 — relation-restricted prime gates for the fifteen-runner case

Date: 2026-09-17 UTC.
Status: **PARTIAL structural reduction; not a proof of LRC(14)**.

## 1. Inputs from the current literature

Write `LRC(k)` for the stationary formulation with `k` nonzero integer speeds and threshold `1/(k+1)`.

Three current ingredients are used.

1. Jaan Allikvere, arXiv:2609.02604v1 (2026-09-02), proves `LRC(13)`, i.e. fourteen total runners.
2. Sungkawichai--Trakulthongchai, arXiv:2604.23906v2 (2026-09-01), define `(k,p,l)`-properness, eventual properness `J(k,p)`, and the prime-gate/product-bound method. Their finite-checking bound says that, assuming `LRC(k-1)`, every primitive counterexample to `LRC(k)` obeys

   `u_1 ... u_k < B_k`, where `B_k = ((binom(k+1,2)^(k-1))/k)^k`.

3. Beck--Everett, arXiv:2609.06259v1 (2026-09-05), prove that every counterexample or tight instance has a **harmful** integer relation `m.u=0` with

   `0 < ||m||_1 <= 2k+3`

   and `sum_i m_i` odd.

For `k=14`, the concrete relation bound is `31`.

The point of this note is to combine (2) and (3) before doing the expensive prime-gate computation.

## 2. Local eventual properness already rules out one residue class

The published gate method proves `J(k,p)=empty` globally. For a counterexample carrying extra information, global emptiness is stronger than necessary.

### Lemma R19-LR1 — localized eventual-properness exclusion

Let `k>=3`, assume `LRC(k-1)`, and let `u=(u_1,...,u_k)` be a primitive integer counterexample to `LRC(k)`. Fix a prime `p` with `p` not dividing `u_1...u_k`, and let `v=u mod p` in `(F_p^*)^k`.

Then `v` is **not** eventually `(k,p)`-proper.

Equivalently, if the actual residue class of a primitive putative counterexample is eventually proper, that counterexample cannot exist.

### Proof

Suppose `v` is eventually proper. By definition there is an integer level `l` such that every lift of `v` to `Z_{p,l}^k` is `(k,p,l)`-proper. Reduce the actual integer tuple `u` modulo `lp`; this is such a lift because no coordinate is divisible by `p`.

If this lift is proper by the witness clause, there is `t in (lp)^(-1) Z` with

`||t u_i|| >= 1/(k+1)` for every `i`,

because `u` and its residue are congruent modulo `lp`. This contradicts that `u` is a counterexample.

It remains to treat the gcd clause. Then for some index `i` there is a divisor

`d = gcd(l, u_1, ..., omit u_i, ..., u_k) > 1`.

(The same divisibility holds for the integer tuple because `d|l` and the proper residue lift is congruent to `u` modulo `lp`.) Since `u` is primitive, `d` does not divide `u_i`. Put

`g=gcd(d,u_i)`, `q=d/g >=2`.

Apply `LRC(k-1)` to the other `k-1` integer speeds `u_j/d`, `j!=i`. There is a real `s` such that

`||s u_j/d|| >= 1/k` for every `j!=i`.

For an integer `r`, let `t=(s+r)/d`. For `j!=i`,

`||t u_j|| = ||s u_j/d|| >= 1/k > 1/(k+1)`.

As `r` runs modulo `d`, the points `(s+r)u_i/d mod 1` run through a translate of the `q` equally spaced points `{0,1/q,...,(q-1)/q}`. If `q=2`, one of the two translated points has distance at least `1/4` from the nearest integer. If `q>=3`, one grid point lies within `1/(2q)` of `1/2`, and hence has distance at least `1/2-1/(2q) >= 1/3`. Thus some `r` gives

`||t u_i|| >= 1/4 >= 1/(k+1)`

for `k>=3`. This same `t` is a lonely witness for every coordinate, again a contradiction.

Therefore the residue class of a primitive counterexample cannot be eventually proper. QED.

This is the local form of the mechanism underlying the global Sungkawichai--Trakulthongchai divisibility lemma, but it is useful here because we will test only thin relation slices of residue space.

## 3. Normalize Beck--Everett relations to finitely many shapes

For `k=14`, Beck--Everett gives a harmful `m` with `||m||_1<=31`.

Because `sum_i m_i` is odd, `||m||_1` is odd as well. Divide `m` by the gcd of its coordinates. That gcd is odd, so the divided relation remains harmful and has no larger `l1` norm.

Now use two exact symmetries of LRC:

- permute speed coordinates;
- change the sign of any individual speed, since `||t(-u_i)||=||tu_i||`.

After applying the same sign change to the relation coefficient, every primitive harmful relation can therefore be represented by a nonincreasing list of **positive absolute coefficients**

`a=(a_1,...,a_s)`, `2<=s<=14`,

such that

- `a_1+...+a_s` is odd and at most `31`;
- `gcd(a_1,...,a_s)=1`.

In other words, relation shapes are primitive integer partitions of odd integers at most `31` into between `2` and `14` parts.

The exact checker accompanying this note gives

`17,575`

primitive shapes if support one is included. The single support-one shape is impossible for a relation among nonzero speeds, leaving

**17,574 nontrivial harmful relation shapes.**

The support distribution is

`2:106, 3:437, 4:994, 5:1623, 6:2067, 7:2276, 8:2212, 9:2016, 10:1715, 11:1424, 12:1129, 13:894, 14:681`.

This is not yet a small proof search, but it is finite and much smaller than treating all signed coefficient vectors separately.

## 4. Relation-restricted prime gates

Pad a relation shape `a` by zeros to length `k=14`. For a prime `p>31`, define the relation slice

`H_a(p) = { v in (F_p^*)^14 : a.v = 0 mod p }`.

Define

`J_a(14,p) = J(14,p) intersect H_a(p)`.

The full published gate asks for `J(14,p)=empty`. The relation-aware gate asks only for `J_a(14,p)=empty`.

Because `p>31`, some nonzero coefficient of `a` is invertible modulo `p`. Given arbitrary nonzero values of the other thirteen coordinates, the relation determines that coordinate uniquely (and it may occasionally determine zero, which is then discarded). Hence

`|H_a(p)| <= (p-1)^13`,

compared with `(p-1)^14` unrestricted signed residues. Thus even before folding signs or applying unit/permutation symmetries, a fixed relation shape saves a factor at least `p-1` in the base residue search.

## 5. Quantifier-swapped product criterion

The main new route is to let **different relation shapes use different easy prime gates**.

### Theorem R19-LR2 — relation-indexed prime-product criterion

Assume `LRC(13)`. Let `A_14` be the set of the 17,574 nontrivial relation shapes above. Suppose that for every `a in A_14` there is a finite set `P_a` of primes `p>31` such that

1. `J_a(14,p)=empty` for every `p in P_a`, and
2. `product_{p in P_a} p >= B_14`, where

   `B_14 = (105^13/14)^14 = 105^182 / 14^14`.

Then `LRC(14)` holds; equivalently, the classical Lonely Runner Conjecture holds for fifteen runners.

### Proof

Suppose instead that a counterexample exists. Divide all speeds by their common gcd, so take a primitive counterexample `u`.

By Beck--Everett there is a harmful relation with `l1` norm at most 31. Normalize it by gcd, coordinate permutation and independent speed-sign changes as in Section 3. Since all these operations preserve the LR property, we obtain one fixed relation shape `a in A_14` and a signed primitive counterexample, still denoted `u`, satisfying

`a.u=0`.

Fix any `p in P_a`. If `p` divided no coordinate of `u`, then the residue `v=u mod p` would lie in `H_a(p)`. Since `J_a(14,p)=empty`, this residue is eventually proper. Lemma R19-LR1 would then rule out `u`. Therefore every `p in P_a` must divide `u_1...u_14`.

Consequently

`u_1...u_14 >= product_{p in P_a} p >= B_14`.

But the Sungkawichai--Trakulthongchai finite-checking bound, using the already proved `LRC(13)`, says every primitive counterexample has

`u_1...u_14 < B_14`.

Contradiction. QED.

### What changed relative to the published gate architecture

The standard criterion has quantifiers of the form

`there exists one prime set P such that for every p in P, all residue classes are eventually proper`.

The relation theorem permits the weaker shape-dependent requirement

`for every relation shape a, there exists a prime set P_a such that only relation-compatible residue classes are eventually proper`.

That is a genuine algorithmic change: a hard global gate may be skipped for one relation shape and replaced by a different prime that is easy on that hyperplane.

The exact checker shows that if one naively used the first primes above 31 uniformly, the first `140` primes, ending at `877`, are enough for their product to cross `B_14`; the first 139 are not. This number is only a scale estimate. The point of the theorem is that `P_a` should be chosen adaptively per relation shape, not uniformly.

## 6. Exact counterexample-first pilot

Before proving the reduction, an exact interval-intersection search tested every strictly increasing fourteen-tuple of positive speeds contained in `{1,...,20}`. There are

`binom(20,14)=38,760`

such tuples. The checker represents the exact good-time set for speed `v` as the union of rational closed intervals

`[(15m+1)/(15v), (15m+14)/(15v)]`, `0<=m<v`,

and intersects these unions using `fractions.Fraction`; no floating-point decision occurs.

Result:

- all 38,760 tuples have a `1/15` witness;
- no counterexample was found;
- the unique tuple whose entire `1/15` witness set consists only of isolated threshold points is `(1,2,...,14)`;
- its exact threshold witness times in `[0,1]` are `1,2,4,7,8,11,13,14` divided by 15.

This bounded search is only PARTIAL evidence and does not move the fixed source metric.

## 7. What this route still has to do

The fixed R19 successor metric is full-source `N_LR=14`, so nothing in this note moves it to 15.

The next obligation is computational but no longer the same computation as Allikvere's `k=13` run. Build a **relation-sliced eventually-properness engine** for `J_a(14,p)` and measure actual survival on a small basis of relation shapes, beginning with:

- support two and three shapes;
- the Dirichlet/tight shape `(2,1)` carried by `(1,2,...,14)`;
- full-support small-coefficient shapes.

The engine should reuse the exact covering/lift machinery from the current record proof, but it should impose the hyperplane relation before level-one generation. If the expected factor-`p` reduction survives orbit canonicalization, this route can turn the new Beck--Everett theorem into a practical fifteen-runner campaign rather than a decorative necessary condition.

A fresh web search on 2026-09-17 for combinations of `Lonely Runner Relations`, `prime gate`, `eventual properness`, and `J(k,p)` did not surface a source already stating this relation-indexed gate criterion. That bounded negative search is not a novelty certificate.
