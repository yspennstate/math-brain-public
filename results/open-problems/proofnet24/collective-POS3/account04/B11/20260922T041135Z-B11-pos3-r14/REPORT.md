# POS3 account04/B11 — bounded variance localizes the 1/6 selector and the first-element tilt

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run stays on the assigned exceptional bounded-variance/high-comparability regime. It does not assume a finite kernel. The new point is that the two presently unbounded-looking objects in the live proof route are quantitatively local under the actual counterexample variance constraints:

1. the newest lead's canonical pair with minority probability `>1/6` must have strong-majority index distance at most `3570`; and
2. in the assigned partner's exact first-element deletion tilt, the contribution to the transfer of any uniform-balanced pair from extensions with initial incomparable run `kappa>=38` is `<1/81`. The complementary `kappa<=37` part is indexed by at most `741` width-two initial ideals.

Neither conclusion bounds the total number of elements. The local window may move through an arbitrarily long poset, and every shallow ideal can have an arbitrarily large residual continuation.

## 1. Exact source-bound state consumed

The latest complete team-lead version read in this invocation is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

Its unified strict-chain terminal selector proves that after internal strong-majority span descent is exhausted in the inherited delayed-predecessor corridor, there is a canonical incomparable pair whose minority ordering probability lies strictly in `(1/6,1/3)`. In the two-blocker subbranches it also produces a canonical successor fork/bridge. The stated remaining obligation is a global amplification/charge theorem rather than another local distinguisher census.

The assigned OTHER-account partner result applied directly is

- account01/B19, `proofnet24/collective-POS3/account01/B19/20260922T034906Z-b19-pos3-r12/REPORT.md`, blob `dd68f31ee0dcf9a8fa08024062a5bc67b73fb77a`.

For the first strong-majority element `c`, with `Q=P\{c}`, `S={z in Q:z||c}`, `T=Q\S`, uniform law `nu` on `L(Q)`, and `kappa(tau)` the length of the initial `S`-run of `tau`, it proves the exact projected-law tilt

`mu(tau) = (kappa(tau)+1)/M * nu(tau)`,

where `M=E_nu[kappa+1]`, and therefore for every event `A` on `L(Q)`,

`mu(A)-nu(A) = Cov_nu(1_A,kappa)/M`.                           (1.1)

For a cross pair it further decomposes this covariance into a nonnegative fixed-skeleton insertion term plus a between-skeleton Simpson covariance. Its exact width-three example shows that the Simpson term can reverse the aggregate sign, so a blanket monotonicity claim is false.

The bounded-variance input is

- account03/B10, `proofnet24/collective-POS3/account03/B10/20260922T0214Z-a03-b10-r11/REPORT.md`, blob `3e50b4d0adaa18c79a96079139d660b832418a2d`.

In a hypothetical counterexample it records the inherited exact strong-majority-rank atom

`Pr(rank(x)=rank_*(x)) > 1/81` for every element `x`,             (1.2)

and proves

`Var(rank(x)) < 6560` for every `x`.                             (1.3)

For every element in the first or last maximal strong-majority chain block it has the sharper

`Pr(rank(x)=rank_*(x)) > 4/9`,
`Var(rank(x)) < 65/16`.                                         (1.4)

The previous B11 report `20260922T031025Z-B11-pos3-r14`, blob `d8584c12674d6210d372c631e7c7da586457f90a`, localized the **actual insertion depth of the first block endpoint** to `406` shallow cut ideals with a `<1/81` deep mass. That does not localize B19's `kappa`: `c` can be inserted very early even when `kappa` is large. Section 4 below pays this distinct missing implication by controlling the tilt variable itself.

## 2. Compact conditional end-to-end route

Assume POS3 is false and take the inherited cardinality-minimal width-three counterexample `P` with transitive strong-majority total order

`x_1 prec_* x_2 prec_* ... prec_* x_n`.

The lead now has a canonical no-descent pair with minority probability `>1/6`. The first question is whether that pair can be arbitrarily far apart in the strong-majority order, allowing the corridor to export mass to an uncontrolled remote location. Section 3 proves it cannot: the all-element rank-variance theorem gives an explicit radius `3570`.

Independently, delete `c=x_1`. Minimality supplies balanced pairs in the smaller nonchain `Q` when that branch is used, but the partner's exact projected law is the nonuniform `kappa+1` tilt (1.1). The first question there is whether a transfer failure can be carried by arbitrarily deep values of `kappa`. Section 4 proves that for any `nu`-balanced pair, the entire contribution of `kappa>=38` to the probability shift has absolute value `<1/81`; the relevant shallow score is a finite sum over at most `741` initial width-two ideals.

Thus both live unbounded mechanisms are localized without claiming that the whole poset is finite or that the remaining global charge is automatic.

## 3. Variance-to-radius theorem for strong minority pairs

Let `r_*(x)` denote the position of `x` in the strong-majority order and let `R_x` be its random rank in a uniform linear extension of `P`.

### Lemma 3.1 — second moment about the strong-majority rank

For every `x in P`,

`E[(R_x-r_*(x))^2] < 531360`.                                  (3.1)

#### Proof

Put `X=R_x-r_*(x)`, `q=Pr(X=0)`. By (1.2), `q>1/81`. Since

`E X = E[X 1_{X!=0}]`,

Cauchy--Schwarz gives

`(E X)^2 <= (1-q) E[X^2]`.

Therefore

`Var(X)=E[X^2]-(E X)^2 >= q E[X^2]`.

Using (1.3),

`E[X^2] <= Var(X)/q < 6560*81 = 531360`. `square`

This is a second moment about the **fixed strong-majority position**, not merely a variance about the mean.

### Theorem 3.2 — explicit strong-majority radius from minority mass

Let `x=x_i`, `y=x_j` with `i<j`, put `d=j-i`, and suppose `x||y`. Then

`Pr(y precedes x) < 2125440/(d+1)^2`.                          (3.2)

Consequently, if

`Pr(y precedes x) > 1/6`,                                      (3.3)

then

`d <= 3570`,                                                    (3.4)

so the strong-majority span of the pair is at most `3569` elements.

#### Proof

Write

`X=R_x-i`, `Y=R_y-j`.

On the event `y` precedes `x`, integer ranks satisfy

`j+Y <= i+X-1`,

hence

`X-Y >= d+1`.                                                   (3.5)

By Markov applied to `(X-Y)^2`, followed by `(X-Y)^2<=2X^2+2Y^2` and Lemma 3.1,

`Pr(y<x)`
`<= E[(X-Y)^2]/(d+1)^2`
`< 4*531360/(d+1)^2`
`= 2125440/(d+1)^2`.

If the left side is `>1/6`, then

`(d+1)^2 < 6*2125440 = 12752640`.                              (3.6)

The adjacent squares are

`3571^2 = 12752041`,
`3572^2 = 12759184`.

Thus the integer `d+1` is at most `3571`, proving `d<=3570`. `square`

### Corollary 3.3 — direct application to the newest lead selector

Every canonical `(1/6,1/3)` minority pair produced by account04/B10 r13 in a hypothetical counterexample has strong-majority index distance at most `3570`.

In particular, in a no-descent two-successor-blocker residue, whichever canonical flanking pair carries the lead's `>1/6` minority mass has its blocker within `3570` strong-majority positions of the opposite endpoint.

This does **not** make the entire poset bounded and does not contradict the previously recorded linear-depth adversaries: those examples refute a radius statement from local fork geometry alone. The radius here uses the additional global hypothetical-counterexample rank atom and variance theorem.

### Endpoint sharpening

The same calculation with the endpoint-block bounds (1.4) gives, for any endpoint-block element `z`,

`E[(R_z-r_*(z))^2] < (65/16)/(4/9) = 585/64`.                 (3.7)

If both endpoints of a `>1/6` minority pair lie in the first/last endpoint blocks, the same proof gives index distance at most `13`. If exactly one endpoint has the sharper bound while the other uses (3.1), the corresponding bound is at most `2524`. These sharpenings are recorded only as consequences; no later argument assumes both endpoints lie in those blocks.

## 4. The assigned partner's tilt is shallow to `1/81` accuracy

Now let `c=x_1`, `Q=P\{c}`, and use the partner notation `S,T,nu,mu,kappa`. Because `c` is the first strong-majority element, it belongs to the first majority block and has no poset predecessor.

For a full extension of `P`, let

`J=R_c-1`,

the number of elements of `Q` appearing before `c`.

By (1.4) and the same argument as Lemma 3.1,

`E[J^2] < 585/64`.                                              (4.1)

Fix `tau in L(Q)` with `kappa(tau)=k`. The only legal insertion gaps for `c` are exactly the first `k+1` gaps, numbered `0,1,...,k`. Conditional on the restriction being `tau`, the uniform full-extension law is uniform over those `k+1` lifts. Hence

`J | (tau,kappa=k)` is uniform on `{0,1,...,k}`,                 (4.2)

and therefore

`E[J^2 | tau] = k(2k+1)/6 >= k^2/3`.                           (4.3)

Averaging (4.3) under the actual projected law `mu` and using (4.1) yields

### Theorem 4.1 — projected second moment of the exact tilt coordinate

`E_mu[kappa^2] < 1755/64`.                                     (4.4)

This is the missing bridge between endpoint rank variance and the partner's reweighting coordinate. It is not a statement about a surrogate uniform projection.

### Theorem 4.2 — deep tilt contributes less than `1/81` to any balanced-pair transfer

Let `A` be any pair-order event on `L(Q)` with

`q:=nu(A) in [1/3,2/3]`.

Put

`G={kappa<=37}`, `D={kappa>=38}`,

and define the shallow transfer score

`T_G(A) := (1/M) E_nu[(1_A-q) kappa 1_G]`.                     (4.5)

Then

`|(mu(A)-q)-T_G(A)| < 15/1216 < 1/81`.                         (4.6)

#### Proof

From the partner identity (1.1),

`mu(A)-q = (1/M) E_nu[(1_A-q)kappa]`.

The omitted deep term is

`R_D=(1/M)E_nu[(1_A-q)kappa 1_D]`.

Since `q in [1/3,2/3]`, pointwise `|1_A-q|<=2/3`. Also

`(1/M) E_nu[kappa 1_D]`
`= E_mu[ kappa/(kappa+1) 1_D ]`.                               (4.7)

For every integer `k>=38`,

`k/(k+1) <= k^2/(38*39)`,                                      (4.8)

because `38*39 <= k(k+1)`. Therefore Theorem 4.1 gives

`|R_D|`
`<= (2/3) E_mu[kappa/(kappa+1) 1_D]`
`< (2/3) * (1755/64)/(38*39)`
`= 15/1216`
`< 1/81`,                                                       (4.9)

where the last inequality is the exact arithmetic `15*81=1215<1216`. `square`

### Corollary 4.3 — at most 741 shallow initial-ideal states

For each `tau`, its initial `S`-run set is a prefix of a linear extension of `Q`, hence an order ideal contained in the width-at-most-two ideal `S`.

Fix a two-chain cover of `S`. An ideal of size at most `37` is determined injectively by its two chain-prefix lengths `(r,s)` with `r+s<=37`. Therefore the number of possible sets is at most

`sum_{j=0}^{37}(j+1) = 38*39/2 = 741`.                         (4.10)

If `I` ranges over these shallow initial-run ideals and

`q_I=nu(A | initial-run ideal = I)`,

then (4.5) is the exact finite-front-state sum

`T_G(A)=(1/M) sum_{|I|<=37} |I| nu(I) (q_I-q)`.                (4.11)

The conditional laws behind the `q_I` may still contain arbitrarily many elements; (4.11) is **not** a finite-kernel reduction.

### Transfer criterion

Equation (4.6) gives an immediate exact sufficient condition. If some `nu`-balanced pair satisfies

`q+T_G(A) in [1/3+1/81, 2/3-1/81]`,                           (4.12)

then the same pair is balanced under the full projected law `mu`.

Conversely, if a hypothetical counterexample pushes a `nu`-balanced pair below `1/3`, then necessarily

`T_G(A) < 1/3-q+1/81`;                                         (4.13)

if it pushes it above `2/3`, necessarily

`T_G(A) > 2/3-q-1/81`.                                         (4.14)

For the partner's cross pairs, its fixed-skeleton theorem says the local insertion covariance is nonnegative. Thus a negative transfer still requires the genuine between-skeleton Simpson mechanism identified in account01/B19 r12, but (4.6) now shows that an unbounded `kappa` tail cannot account for more than `1/81` of the pair-probability shift.

## 5. Relation to the previous 406-state endpoint-cut theorem

The previous B11 result bounded the **realized insertion depth** `J`: with probability more than `80/81`, at most `27` elements of the rest of the poset precede the first-block endpoint. That produced at most `406` realized cut ideals.

The new theorem addresses a different variable. In the partner's deletion formula, `kappa` is the number of incomparable elements available before the first forced successor in the restriction `tau`, whether or not `c` is actually inserted after them. A large `kappa` extension can still have `J=0` if `c` is inserted in the first gap. Hence the old `J` tail does not control the reweighting factor `kappa+1`.

The conditional uniform-gap identity (4.2) is what transfers the endpoint rank second moment to `kappa`, and (4.6) controls the **probability-shift functional itself**, not merely the mass of deep realized insertions.

## 6. First essential missing implication after this run

The live global obstruction is now narrower in two complementary senses.

1. **Lead corridor.** The account04/B10 r13 canonical pair with minority mass `>1/6` cannot be exported arbitrarily far: it lies within `3570` positions in the strong-majority order. The next global charge theorem may therefore work with overlapping bounded windows, while still allowing an unbounded number of windows along the poset.

2. **Partner transfer.** For the first-element deletion, every balanced-pair transfer is determined to additive error `<1/81` by the at-most-`741` shallow initial-ideal score (4.11). The exact remaining induction step is to select a `nu`-balanced pair for which this shallow score obeys (4.12), or else force a balanced pair meeting the deleted element. For cross pairs, the partner's Simpson decomposition says the only adverse mechanism after fixed-skeleton insertion is the between-skeleton term; the new result removes the unbounded `kappa` tail as a possible large source of that adverse transfer.

A valid next synthesis would couple the lead's bounded-radius `>1/6` fork charge to these shallow exact insertion states or to the three-chain cumulative-band flux, proving that repeated bounded windows must overlap in a way that yields a `1/3` charge. What is **not** justified is enumerating 741 states, treating their residual posets as finite, or claiming that radius `3570` bounds the whole counterexample.

## 7. Status, failures, and provenance

- POS3: **OPEN / NOT PROVED**.
- Latest lead `>1/6` canonical selector: **CONSUMED/APPLIED**.
- Assigned partner account01/B19 exact `kappa+1` tilt and Simpson decomposition: **CONSUMED/APPLIED**.
- All-element second moment about strong-majority rank `<531360`: **PROVED** from the inherited atom/variance bounds.
- Any `>1/6` minority pair has strong-majority index distance `<=3570`: **PROVED**.
- First-element projected tilt coordinate `E_mu[kappa^2]<1755/64`: **PROVED**.
- Deep `kappa>=38` contribution to transfer of any `nu`-balanced pair `<15/1216<1/81`: **PROVED**.
- At most `741` shallow initial-ideal states in that transfer score: **PROVED**.
- Finite-kernel reduction: **NOT CLAIMED / still unavailable**.
- Global amplification from `1/6` to `1/3`: **OPEN**.
- Adaptive shallow-score selection theorem: **OPEN**.

No finite computation or code is used as proof in this report. The displayed integer and rational constants are direct arithmetic consequences of the cited inequalities. No finite census is promoted to an arbitrary-size proof.

Scoped privacy/provenance review: this report contains only mathematical statements, source-bound repository references and nonsecret run labels. It contains no credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark material, email/Drive content, paid model/API/Codex calls, remote workflows, public posting, permission changes, or production-brain mutation.