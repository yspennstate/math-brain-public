# POS3 fleet01/B19 — first-interruption renewal recurrence and two-channel reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run changes mechanism from the preceding adjacent-swap / weight-gradient analysis.  Instead of trying to compare the biased projected law directly with the uniform law on the deletion skeleton, it partitions **full linear extensions of the original poset by the first interruption of the deleted initial chain block**.  The result is an exact renewal recurrence in terms of uniform linear-extension laws of strictly smaller residual posets.  No induced biased law is treated as uniform.

## 1. Exact collective state consumed

The active collective directive is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; old brain-installation and benchmark duties are superseded for this slot.

The essential inherited mathematics used here is:

1. **Prior fleet01/B19**, report blob `004a04191bf389e3493c3346fd57e67b35500049`.  For an initial ideal chain `C={c_1<...<c_m}` and `Q=P\C`, with
   `lambda(q)=max({j:c_j<q} union {0})`, it proved the exact one-sided insertion weight
   `W_C(tau)=#{0<=t_1<=...<=t_n<=m : t_i>=lambda(q_i)}`
   for `tau=(q_1,...,q_n) in L(Q)`, the exact uniform-prefix component, and the rank-one adjacent-swap defect.  It left an ideal-block weighted transfer statement unpaid.

2. **Campaign lead fleet04/B10**, run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`.  In a hypothetical width-three counterexample, every element occupies its strong-majority rank with probability `>1/81`; at a one-sided endpoint the same argument gives `>4/9`.

3. **Assigned OTHER-account partner fleet02/B10**, run `20260922T014627Z-fleet02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`.  At the first strong-majority block boundary `x prec_* y`, its exact blocker mass transport gives
   `2/3 < p_xy < 7/9`,
   and forces both canonical successor-blocker channels to carry positive deletion-fiber defect.

4. **Additional OTHER-account structural input fleet03/B11**, run `20260922T011439Z-fleet03-B11-pos3-r12`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`.  At that first boundary there are exactly two canonical successor blockers `s_1,s_2`; they are Hasse covers of `x`, and `y,s_1,s_2` are pairwise incomparable.  Their first distinguisher is delayed beyond the second majority block.

The named partner result in item 3 is applied quantitatively below; it is not merely cited.

## 2. Conditional end-to-end induction and the obstruction left by the previous run

Assume for contradiction that POS3 fails, and choose a cardinality-minimal counterexample `P`.  Use the inherited transitive strong-majority order `L_*`.  Let

`C={c_1<...<c_m}`

be the **first maximal contiguous block of `L_*` which is a chain in `P`**, let `x=c_m`, and put `Q=P\C`.  Then:

- `C` is an order ideal: any predecessor outside `C` of an element of `C` would occur earlier in the linear extension `L_*`.
- If `Q` were a chain then `P` would be the union of two chains and the known width-two theorem would already give a balanced pair.  Hence `Q` is a smaller nonchain of width at most three.
- By minimality, the **uniform** law on `L(Q)` has at least one balanced incomparable pair.
- If that balanced pair survived the exact projected law induced from `P`, the induction would close.

The preceding B19 report encoded that projected law by the insertion weight `W_C`.  The first missing implication was to exploit more than the scalar uniform-component bound.  The theorem below replaces the arbitrary residual weight by an exact mixture of smaller uniform-poset laws.

## 3. First-interruption renewal recurrence

For `q in Q` define

`lambda(q)=max({j in {1,...,m}: c_j<q} union {0}).`

Because `C` is an ideal, no element of `Q` lies below any `c_j`.  Hence the exact lift weight of `tau=(q_1,...,q_n) in L(Q)` is

`W_C(tau)=#{0<=t_1<=...<=t_n<=m : t_i>=lambda(q_i)}`.      (3.1)

Define the set of **first interrupters**

`M={q in Min(Q): lambda(q)<m}`.                               (3.2)

Every first element of a linear extension of `Q` is minimal.  The all-`m` insertion vector is the unique lift with all of `C` first.

### Theorem 3.1 — support and exact first-interruption decomposition

Let `tau=(q,q_2,...,q_n) in L(Q)`.

1. `W_C(tau)>1` iff `q in M`.
2. If `q in M`, then

   `W_C(tau)-1 = sum_{j=lambda(q)}^{m-1} W_{q,j}(q_2,...,q_n)`,    (3.3)

   where

   `W_{q,j}(q_2,...,q_n)`
   `=#{j<=t_2<=...<=t_n<=m : t_i>=lambda(q_i)}`.                 (3.4)

3. Put

   `R_{q,j}=P\{c_1,...,c_j,q}`                                  (3.5)

   with the induced order.  Then

   `e(P)=e(Q)+sum_{q in M} sum_{j=lambda(q)}^{m-1} e(R_{q,j}).`   (3.6)

4. More generally, for any event `A` depending only on the relative order of elements of `Q`,

   `Pr_P(A)=alpha Pr_Q(A)+sum_{q in M} sum_j beta_{q,j} Pr_{q,j}(A)`,   (3.7)

   where

   `alpha=e(Q)/e(P)`, `beta_{q,j}=e(R_{q,j})/e(P)`,               (3.8)

   and `Pr_{q,j}` is obtained by fixing the prefix
   `c_1,...,c_j,q`
   and then taking a **uniform** linear extension of the smaller residual poset `R_{q,j}`.  Thus

   `alpha + sum_{q,j} beta_{q,j}=1`.                              (3.9)

### Proof

If `lambda(q)=m`, then every feasible vector in (3.1) has `t_1=m`; monotonicity forces every `t_i=m`, so `W_C(tau)=1`.  If `lambda(q)<m`, the all-`m` vector is feasible and so is the vector with `t_1=lambda(q)` and `t_2=...=t_n=m`, hence `W_C(tau)>1`.  Since `q` is the first element of `tau`, it is minimal in `Q`; this proves part 1.

For `q in M`, every non-prefix lift has a unique value `j=t_1<m`, the number of elements of `C` before the first `Q` element `q`.  Fixing that `j` leaves exactly the sequences counted by (3.4).  Summing over `j=lambda(q),...,m-1` proves (3.3).

For such `(q,j)`, the set `{c_1,...,c_j,q}` is an ideal of `P`: the chain prefix is an ideal because `C` is, `q` has no predecessors in `Q` because it is minimal, and all its predecessors in `C` lie among `c_1,...,c_j` by `j>=lambda(q)`.  Consequently, after the fixed prefix, **every** linear extension of `R_{q,j}` and only such an extension gives a full extension in this interruption channel.  The disjoint alternatives are: all of `C` first (giving exactly `e(Q)` extensions), or a unique first interrupter `q` after a unique `j<m` chain elements (giving `e(R_{q,j})`).  This proves (3.6), and partitioning the same extensions according to `A` proves (3.7).  `□`

The important point is that (3.7) is an induction-ready identity among actual uniform residual-poset laws.  It does **not** assert that the projection to `Q` itself is uniform.

## 4. Width three collapses the recurrence to at most two interruption channels

Let `x=c_m`.  Every `q in M` is incomparable with `x`: `q<x` is impossible because `C` is an ideal, while `x<q` would give `lambda(q)=m`.  Also `M` is an antichain because it consists of minimal elements of `Q`.  Therefore

`{x} union M`

is an antichain, and width at most three gives

`|M|<=2`.                                                        (4.1)

Let `y` be the first element of `Q` in `L_*`.  Maximality of the first chain block gives `x||y`; since no element of `Q` precedes `y` in `L_*`, `y` is minimal in `Q`, so

`y in M`.                                                        (4.2)

Hence, in a minimal counterexample,

`1<=|M|<=2`.                                                     (4.3)

The formerly arbitrary biased deletion law is therefore a renewal mixture with **one or two first-interrupter channels only**.

For `q in M`, write

`beta_q=sum_j beta_{q,j}`.                                       (4.4)

Every extension in the `q`-channel has `q<x`, so the no-balanced-pair hypothesis and the strong-majority order `x prec_* q` give

`beta_q <= Pr_P(q<x) < 1/3`.                                    (4.5)

The lead's one-sided rank theorem gives

`alpha=Pr_P(C is the initial block)=Pr_P(rank(x)=m)>4/9`.        (4.6)

These are exact constraints on the renewal coefficients, not bounds on a fictitious uniform projection.

## 5. Applying the named partner: the single-channel case has a protected central interval

Suppose `M={y}`.  Then an extension fails to begin with all of `C` iff `y<x`; hence

`alpha=Pr_P(x<y)`.                                               (5.1)

The assigned partner fleet02/B10 theorem applies to this first strong-majority boundary and gives

`2/3 < alpha < 7/9`.                                             (5.2)

Thus the single non-prefix channel has mass

`2/9 < 1-alpha < 1/3`.                                          (5.3)

For any incomparable pair `a,b in Q`, write `q=Pr_Q(a<b)`.  From the renewal mixture alone,

`alpha q <= Pr_P(a<b) <= alpha q + (1-alpha)`.                   (5.4)

Therefore every pair satisfying

`1/(3 alpha) <= q <= 1-1/(3 alpha)`                              (5.5)

is automatically balanced in `P`.  Because `alpha>2/3`, the interval in (5.5) is nonempty and contains `1/2`.  In particular:

> **Corollary 5.1.** A cardinality-minimal POS3 counterexample in the single-interrupter case cannot have an incomparable pair in `Q` whose uniform ordering probability is exactly `1/2`.

This is a strict new structural restriction on the smaller induction object `Q`.

## 6. Two interrupters: their uniform majority direction cannot reverse

Now suppose

`M={y,r}`

with `y prec_* r`.  Since both are minimal in `Q`, they are incomparable.  Let

`q=Pr_Q(y<r)`.

In every non-prefix `y`-channel extension, `y<r`; in every non-prefix `r`-channel extension, `r<y`.  Therefore (3.7) specializes **exactly** to

`Pr_P(y<r)=alpha q + beta_y`,                                    (6.1)

`Pr_P(r<y)=alpha(1-q)+beta_r`.                                  (6.2)

The no-balanced-pair hypothesis gives `Pr_P(y<r)>2/3`; (4.5) gives `beta_y<1/3`.  Hence

`q > 1/(3 alpha)`.                                               (6.3)

Likewise (6.2) is `<1/3`, so

`q > 1-1/(3 alpha)`.                                             (6.4)

Consequently

`q > max{1/(3 alpha), 1-1/(3 alpha)} >= 1/2`.                   (6.5)

Thus deleting the first chain block may weaken the strong `>2/3` relation between the two possible interrupters, but it **cannot reverse even its strict majority direction under the uniform law on `Q`**.

Also, `C`-first implies `x<y`; applying the partner's strict endpoint cap gives

`4/9 < alpha < 7/9`.                                             (6.6)

Equation (6.5), together with (6.6), is a quantitative two-channel constraint on the uniform induction object.

## 7. The second interruption channel must meet the partner's Hasse fork

The fleet03/B11 endpoint theorem supplies two successor blockers `s_1,s_2` with

`x lessdot s_1`, `x lessdot s_2`,

and `y,s_1,s_2` pairwise incomparable.

If a second interrupter `r` exists, then `r||y`.  If `r` were also incomparable with both `s_1,s_2`, the four elements

`y,r,s_1,s_2`

would be an antichain, contradicting width three.  Hence `r` is comparable with at least one `s_i`.  Since `r` is minimal in `Q`, one cannot have `s_i<r`.  Therefore

> **Corollary 7.1.** In the two-interrupter case, the second first-interruption element satisfies `r<s_i` for at least one of the two canonical endpoint Hasse blockers.

So the renewal channels are not independent of the partner's endpoint transport geometry: the second channel is forced into the Hasse-fork structure.

## 8. Genuine counterexample to the naive local transfer statement

The preceding renewal theorem is necessary because even the **single-interrupter** case does not preserve every balanced pair of `Q` under only the chain-touching strong inequalities.

Take an ideal chain

`C={c_1<c_2<c_3<c_4}`

and six elements `q_0,...,q_5` whose induced poset `Q` has Hasse covers

`q_0<q_2`, `q_0<q_3`, `q_1<q_2`, `q_2<q_4`, `q_2<q_5`.

Set

`lambda=(4,3,4,4,4,4)`.

Thus every element of `C` is below every `q_i` except that `c_4||q_1`; this defines a width-three poset `P`.  Exact enumeration gives

`e(Q)=18`, `e(P)=26`, `M={q_1}`.

The only chain-to-`Q` incomparable pair satisfies

`Pr_P(c_4<q_1)=18/26=9/13>2/3`.                                 (8.1)

Nevertheless `q_2||q_3` is balanced under the uniform law on `Q` at the endpoint value

`Pr_Q(q_2<q_3)=12/18=2/3`,                                      (8.2)

while under the exact projected law from `P`,

`Pr_P(q_2<q_3)=18/26=9/13>2/3`.                                 (8.3)

So the statement

> “the one-sided insertion recurrence plus all chain-touching `>2/3` constraints preserves every balanced pair of `Q`”

is **false**, even with one first interrupter and width three.

This is not a counterexample to POS3: the same `P` has, for example,

`Pr_P(q_4<q_5)=1/2`.                                             (8.4)

The example is also consistent with the protected interval (5.5): here `alpha=18/26=9/13`, for which the protected interval is `[13/27,14/27]`; the pair in (8.2) lies outside it, while the exact-half pair in (8.4) is protected.

## 9. First essential missing implication after this run

The previous broad IBWT statement has now been separated into a false local version and a narrower source-valid global residual.

A minimal counterexample must satisfy the exact renewal recurrence (3.7) with only one or two first-interrupter channels, channel masses `<1/3`, `alpha>4/9`, the single-channel protected interval (5.5), the two-channel majority preservation (6.5), and the endpoint Hasse-fork incidence in Corollary 7.1.

The first unpaid implication is therefore the following **renewal selector lemma**:

> For the first strong-majority chain block of a cardinality-minimal width-three counterexample, prove that the uniform smaller poset `Q` has an incomparable pair whose probability falls in the protected interval of the actual renewal mixture, or else use the at-most-two interruption channels together with the forced Hasse-fork incidence to produce a balanced pair meeting the deleted block.

The finite example in Section 8 shows that one cannot demand that an arbitrary `[1/3,2/3]` pair of `Q` transfer.  The selection must use the global strong-majority/Hasse-block structure.  In the one-channel case an exact-half pair already closes the induction; in the two-channel case the two possible first interrupters retain their strict majority orientation in `Q` and the second interrupter is forced below an endpoint blocker.  These are the first constraints that a global selector can exploit without replacing the true biased law by a uniform one.

## 10. Verification and provenance

A deterministic standard-library verifier for this run checks:

- `5,694` exact insertion-word cases for the first-interruption identity `W-1=sum_j W_{q,j}` through chain length four and word length five;
- the exact width-three construction of Section 8;
- `e(Q)=18`, `e(P)=26`, `M={q_1}`;
- the exact probabilities `2/3`, `9/13`, `9/13`, and `1/2` in (8.1)-(8.4).

The proof of Theorem 3.1 and the width-three/channel corollaries is symbolic; the computation is regression evidence for the recurrence and the finite falsification only.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive data, public posting, paid model/API/Codex execution, remote workflow, permission change, or production-brain mutation was used.  No novelty or priority claim is made.
