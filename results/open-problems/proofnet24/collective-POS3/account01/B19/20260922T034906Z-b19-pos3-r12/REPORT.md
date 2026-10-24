# POS3 account01/B19 — exact cross-skeleton insertion covariance and the surviving Simpson obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run stays on the exact chain/deletion-transfer assignment but changes mechanism from the preceding ideal-cut moment argument.  I condition on the complete deletion skeleton of a candidate pair and prove a fiberwise insertion-covariance theorem.  It shows that for a pair crossing the first-element cut, the local `kappa+1` reweighting has a fixed favorable sign in every deletion skeleton.  The only possible adverse transfer is a genuine between-skeleton Simpson term.  I then give an exact width-three example proving that this Simpson term can in fact reverse the aggregate sign, so the local theorem cannot simply be averaged.  Finally I apply the assigned partner's one-distinguisher theorem and show by an exact five-point example that its `one` threshold is sharp even in this first-element-cut geometry.

No projected deletion law is treated as uniform anywhere.

## 1. Source-bound collective state consumed

The active owner programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; installation/benchmark work is superseded for B19.

The exact completed mathematical inputs used here are:

1. **Campaign lead account04/B10, latest complete candidate:**  
   `proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`.  It proves the first-boundary nested-predecessor funnel and reduces the surviving exception to a delayed-chain / successor-corridor continuation problem.

2. **Assigned OTHER-account partner account02/B10:**  
   `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`.  Its Theorem 4.1 proves that an incomparable pair with exactly one relation-distinguisher is balanced; hence every incomparable pair in a hypothetical counterexample has at least two distinguishers.

3. **Fresh quantitative teammate input account04/B11:**  
   `proofnet24/collective-POS3/account04/B11/20260922T031025Z-B11-pos3-r14/REPORT.md`, blob `d8584c12674d6210d372c631e7c7da586457f90a`.  It proves a `1/81` deep-cut tail for the first block endpoint and shows that the endpoint reversal mass has a fixed positive shallow component.  This is used only as context for where the surviving between-skeleton term must eventually be controlled; no finite-kernel conclusion is imported.

4. **Immediate B19 predecessor:**  
   `proofnet24/collective-POS3/account01/B19/20260922T024644Z-b19-pos3-r11/REPORT.md`, blob `d1a22bb63b9a5fa57541e1970dac09d7aec14937`.  It deletes the first strong-majority element `c`, writes `Q=P\{c}`, proves that
   `S={z in Q:z||c}` is a width-at-most-two ideal, and gives the exact tilt
   `mu(tau)=(kappa(tau)+1)/(e(P)/e(Q)) * nu(tau)`
   where `nu` is uniform on `L(Q)` and `kappa(tau)` is the initial `S`-run before the first element of `T=Q\S`.

The parent target and source-normalization remain those in the collective POS3 target record.  The inherited finite frontier is unchanged and is not used as an arbitrary-size proof.

## 2. Compact conditional end-to-end route

Assume for contradiction that POS3 fails and choose a cardinality-minimal counterexample `P`.  Let `c` be the first element of the inherited transitive strong-majority order, put `Q=P\{c}`, and define

`S={z in Q:z||c}`, `T=Q\S`.

The predecessor report proves that `S` is an ideal of width at most two and that the restriction of the uniform law of `P` to `L(Q)` is exactly the `kappa+1` tilt of the uniform law `nu` on `L(Q)`:

`mu(A)-nu(A)=Cov_nu(1_A,kappa)/E_nu[kappa+1]`.                 `(2.1)`

By minimality, `Q` has a `nu`-balanced incomparable pair.  The open induction step is to choose one that stays balanced under `mu`, or force a balanced pair involving `c`.

For a candidate crossing the cut, `a in S`, `b in T`, this run proves that **inside every fixed deletion skeleton of `Q\{a,b}` the covariance in (2.1) is nonnegative**.  Therefore every adverse transfer is caused solely by reweighting different skeletons against one another.  This identifies an exact single residual rather than an arbitrary biased-law problem.

## 3. Fixed-skeleton insertion setup

Fix incomparable `a in S`, `b in T`, and let

`R=Q\{a,b}`.

For a skeleton `sigma in L(R)`, let `h=h(sigma)` be the number of initial elements of `sigma` belonging to `S` before the first element of `T`; if `sigma` has no `T` element, put `h=|R|`.

Number the external insertion gaps of `sigma` by `0,1,...,|R|`.  The legal gaps for `a` and `b` are intervals

`A_sigma=[ell_a,u_a]`, `B_sigma=[ell_b,u_b]`.

Because `a||b`, if the two elements choose distinct legal gaps their order is determined by the gap order, while if they choose the same gap there are exactly two legal lifts, one with `a<b` and one with `b<a`.

For a legal lift write `i` for the gap of `a` and `j` for the gap of `b`.  Let `kappa` denote the initial `S`-run in the resulting extension of `Q`.

## 4. Exact local formula

### Lemma 4.1 — first-`T` gap formula

For an `a<b` lift,

`kappa_+(i,j)=min(j,h)+1_{i<=h}`.                              `(4.1)`

For a `b<a` lift,

`kappa_-(i,j)=min(j,h)`.                                      `(4.2)`

### Proof

If `j<=h`, the inserted element `b in T` becomes the first `T` element.  Exactly `j` skeleton elements of `S` precede it.  In the `a<b` orientation, `a` also precedes that first `T` element, adding one; in the `b<a` orientation it does not.

If `j>h`, the first `T` element already present in `sigma` remains first.  It has exactly `h` skeleton `S` elements before it, and `a` contributes one exactly when `i<=h`.  But in the `b<a` orientation with `j>h`, necessarily `i>=j>h` (including the equal-gap `b,a` lift), so no bonus occurs.  This gives (4.1)-(4.2). `square`

## 5. Fiberwise monotonicity theorem

For `j in B_sigma`, define

`F(j)=#{i in A_sigma:i<=j}`,
`G(j)=#{i in A_sigma:i>=j}`.

Thus the number of `a<b` lifts with `b` in gap `j` is `F(j)`, while the number of `b<a` lifts with `b` in gap `j` is `G(j)`.  Equal-gap lifts are correctly counted once on each side.

Let

`f(j)=min(j,h)`.

Then `f` and `F` are nondecreasing in `j`, while `G` is nonincreasing.

### Theorem 5.1 — local insertion tilt has a fixed sign

For every skeleton `sigma` for which both orientations occur,

`E[kappa | a<b, sigma] >= E[kappa | b<a, sigma]`.              `(5.1)`

Equivalently,

`delta_sigma := Cov(1_{a<b},kappa | sigma) >= 0`.              `(5.2)`

This holds for every finite poset in the first-element cut setup; no width-two property beyond the definition of `S,T` is needed in the proof.

### Proof

Under the `a<b` lifts, the `b`-gap has weight `F(j)`.  Under the `b<a` lifts it has weight `G(j)`.  Since `f,F` are both nondecreasing, the finite Chebyshev sum inequality gives

`sum f(j)F(j)/sum F(j) >= (1/|B_sigma|) sum f(j)`.             `(5.3)`

Since `f` is nondecreasing and `G` nonincreasing, the reversed Chebyshev inequality gives

`sum f(j)G(j)/sum G(j) <= (1/|B_sigma|) sum f(j)`.             `(5.4)`

Hence the base contribution `f(j)` has no smaller mean on the `a<b` side than on the `b<a` side.  Formula (4.1) adds the nonnegative bonus `1_{i<=h}` only on the `a<b` side.  This proves (5.1), and (5.2) follows from

`Cov(1_A,kappa | sigma)=p_sigma(1-p_sigma)(E[kappa|A,sigma]-E[kappa|A^c,sigma])`.
` square`

### Quantitative local defect

Let `n_+`, `n_-` be the two orientation counts in the skeleton, `n=n_++n_-`, and let `r_sigma` be the number of `a<b` lifts with `i<=h`.  The same proof gives

`E[kappa|a<b,sigma]-E[kappa|b<a,sigma] >= r_sigma/n_+`,        `(5.5)`

hence

`delta_sigma >= n_- r_sigma / n^2`.                            `(5.6)`

Thus every skeleton with a reverse lift and a positive pre-first-`T` forward lift contributes a strictly positive local correction.

## 6. Exact global Simpson decomposition

Let `H` be the random skeleton obtained from a uniform `nu`-extension of `Q` by deleting `a,b`.  Put

`p_H=Pr_nu(a<b | H)`,
`m_H=E_nu[kappa | H]`.

The law of total covariance gives the exact identity

`Cov_nu(1_{a<b},kappa)`
`= E_nu[delta_H] + Cov_nu(p_H,m_H)`.                           `(6.1)`

Combining (2.1) and (6.1),

`mu(a<b)-nu(a<b)`
`= [ E(delta_H) + Cov(p_H,m_H) ] / E[kappa+1]`.               `(6.2)`

Theorem 5.1 proves the first term is always nonnegative.  Therefore:

> **Every adverse cross-cut transfer is a between-skeleton Simpson effect.**

In particular, if `q=nu(a<b)` is balanced, then `mu(a<b)` is balanced exactly when

`E[kappa+1](1/3-q)`
`<= E(delta_H)+Cov(p_H,m_H)`
`<= E[kappa+1](2/3-q)`.                                       `(6.3)`

For the difficult majority-late orientation `mu(a<b)<1/3`, the between-skeleton term must satisfy the strict quantitative obstruction

`Cov(p_H,m_H) < -E(delta_H) - E[kappa+1](q-1/3)`.             `(6.4)`

This is the first exact unpaid transfer inequality after the local insertion problem is removed.

## 7. Source-valid width-three counterexample to globalizing the local sign

A tempting next claim is false:

> `mu(a<b)>=nu(a<b)` for every incomparable `a in S`, `b in T`.

The following exact width-three cut setup refutes it.

Let `Q` have

`S={0,1,2,3}`, `T={4,5,6}`

and Hasse relations

`0<2<3<5`, `1<6`, `4<6`.

Then `S` is an order ideal of width two.  Add a new minimal element `c=7` with

`c<4`, `c<5`

(and hence `c<6` by `4<6`).  Call the resulting poset `P`.  It has width exactly three.  The exact counts are

`e(Q)=70`, `e(P)=203`.

For the incomparable cross pair `(a,b)=(1,5)`,

`nu(a<b)=32/35`,
`mu(a<b)=185/203`,

so

`mu(a<b)-nu(a<b) = -3/1015 < 0`.                              `(7.1)`

Equivalently,

`Cov_nu(1_{a<b},kappa)=-3/350`.                               `(7.2)`

Yet every fixed-skeleton local covariance is nonnegative.  Summed with the correct skeleton weights,

`E(delta_H)=60/1309 >0`,

while

`Cov(p_H,m_H)=-3561/65450`,

and their sum is exactly `-3/350`.  There are ten deletion skeletons.

Thus the between-skeleton Simpson term can dominate all favorable local insertion terms even when `S` is width two and the restored poset has width three.

This example is **not** a counterexample to POS3 and it does **not** satisfy all hypothetical-minimal-counterexample endpoint constraints.  It refutes only the universal globalization of Theorem 5.1.  Therefore the genuine counterexample constraints `Pr_P(c<z)>2/3` for all `z in S`, the lead's delayed-distinguisher geometry, and the shallow-cut bounds remain potentially decisive information rather than redundant decoration.

## 8. Direct application of account02/B10 r13, and sharpness

For every cross pair `a in S`, `b in T`, the restored element `c` itself distinguishes `a` from `b`:

`c||a`, while `c<b`.

The assigned partner account02/B10 r13 proves that an incomparable pair with exactly one distinguisher is balanced.  Hence in a hypothetical POS3 counterexample **every extreme cross pair must have at least one further distinguisher already inside `Q`**.

That strengthening is exact but cannot be pushed one step further by cardinality alone.

Consider the five-element width-three poset with chain

`c<d<b`

and two further isolated points `a,s`.  Then the incomparable pair `(a,b)` has exactly two distinguishers, namely `{c,d}`, but exact enumeration gives

`e(P)=20`,
`Pr(a<b)=3/4`.                                                 `(8.1)`

Also

`Pr(c<a)=Pr(c<s)=3/4`,

so the first-element orientation is already strongly one-sided.  Nevertheless the poset has an escape pair, for example

`Pr(a<d)=1/2`,

so this is not a POS3 counterexample.

Therefore account02/B10's one-distinguisher theorem is sharp in this cut geometry: **one additional `Q`-distinguisher beyond `c` can already support an extreme cross probability.**  The next argument must use where the distinguishers occur and how they affect the skeleton statistic, not merely their number.  This is exactly where the lead's delayed-chain/corridor structure can enter (6.4).

## 9. First essential missing implication after this run

The prior WICSL transfer problem has now split into a proved local part and one precise global part.

For a `nu`-balanced cross pair `a in S`, `b in T`, all fixed-skeleton insertion effects are controlled by Theorem 5.1.  To exclude the majority-late branch it is enough to prove, for at least one adaptively selected balanced cross pair,

`Cov(p_H,m_H) >= -E(delta_H)-E[kappa+1](q-1/3)`.              `(9.1)`

The majority-early branch has the corresponding upper inequality from (6.3).  Same-side pairs still use the exact ideal-cut recurrence from the predecessor report.

The **first essential missing implication** is therefore an adaptive **majority-constrained cross-skeleton selection lemma**: use the actual minimal-counterexample endpoint constraints (`Pr(c<z)>2/3` for all `z in S`, the large empty-cut atom, the lead's delayed nested-distinguisher corridor, and the shallow-cut concentration) to select a balanced pair in `Q` whose between-skeleton term satisfies (6.3).

The new counterexample proves that Theorem 5.1 alone cannot be summed to obtain this.  The five-point example proves that the partner's distinguisher-count theorem alone cannot obtain it either.  What remains is genuinely a correlation statement between **which deletion skeleton occurs** and **how strongly that skeleton favors the candidate pair**.

This is narrower than the previous generic weighted-law problem: the local insertion kernel has been completely paid, and the residual is the single covariance `Cov(p_H,m_H)`.

## 10. Deterministic regression evidence

A standard-library verifier accompanies this report.  It independently checks:

1. `38,379` finite interval/gap instances of the local inequality in Theorem 5.1;
2. the exact eight-point Simpson example, including `e(Q)=70`, `e(P)=203`, width three, `32/35 -> 185/203`, and the exact local/between covariance split;
3. the five-point two-distinguisher sharpness example, including `20` extensions, distinguisher set `{c,d}`, and probability `3/4`.

Recorded terminal output begins

`POS3_CROSS_SKELETON_TRANSFER_CHECK_PASS`

and records

`simpson_pair_nu 32/35 mu 185/203 cov -3/350`,
`simpson_local 60/1309 between -3561/65450`,
`two_distinguisher_extensions 20 p_0_before_3 3/4`.

Verifier SHA-256: `e2a93ea68c4945d080f01290728875a4e7e6b8bec13276fc96643669dfefe123`.  
Captured-output SHA-256: `6b36365760b4d29c635dcf083dfe5f9f5653e1075a8f0b139c2cdfc49cb1744c`.

The theorem itself is the symbolic argument in Sections 4-6; the computation is regression and exact finite-counterexample verification only.

## 11. Honest status and provenance

- POS3: **OPEN / NOT PROVED**.
- Exact first-element ideal-cut recurrence from the predecessor: retained.
- Fixed-skeleton cross-cut insertion covariance sign: **PROVED**.
- Quantitative local defect (5.6): **PROVED**.
- Exact total-covariance / Simpson decomposition (6.1)-(6.3): **PROVED**.
- Universal globalization `mu(a<b)>=nu(a<b)`: **REFUTED by an exact width-three setup**.
- Strengthening “at most two distinguishers implies balance”: **REFUTED by an exact five-point width-three setup**.
- Majority-constrained adaptive cross-skeleton selection lemma: **OPEN**.

No claim of novelty or priority is made.  No finite check is promoted to the arbitrary-size theorem.  No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API/Codex execution, remote workflow, permission change, or production-brain mutation is included.  No authenticated brain retrieval/context use occurred.
