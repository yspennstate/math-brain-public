# POS3 fleet04/B20 — renewal-channel tail injection and exact first-minimum geometry

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform linear-extension law lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It does not resume superseded brain-installation or benchmark work.

## 1. Exact source-bound state consumed

The newest complete campaign-lead report is

- `fleet04/B10`, `proofnet24/collective-POS3/fleet04/B10/20260922T011127Z-fleet04-B10-POS3-r11/REPORT.md`, blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`.

It proves that in a hypothetical width-at-most-three counterexample every element occupies its position in the transitive strong-majority order with probability `>1/81`; at a one-sided endpoint the same argument gives the stronger initial-block mass `>4/9`.

The required newest complete OTHER-account partner report is

- `fleet01/B19`, `proofnet24/collective-POS3/fleet01/B19/20260922T021702Z-pos3-b19-r11/REPORT.md`, blob `d67e1fb585263c76361b5c227fbb9fc069778b78`.

For a cardinality-minimal counterexample, let `C={c_1<...<c_m}` be the first maximal contiguous strong-majority chain block, let `x=c_m`, and put `Q=P\C`. For `q in Q`, define

`lambda(q)=max({j:c_j<q} union {0})`.

The partner proves the exact first-interruption renewal decomposition. With

`M={q in Min(Q): lambda(q)<m}`,

one has `1<=|M|<=2`, and

`Pr_P(A)=alpha Pr_Q(A)+sum_{q in M} sum_j beta_{q,j} Pr_{q,j}(A)`

for every event depending only on the relative order in `Q`, where

`alpha=e(Q)/e(P)`, `beta_{q,j}=e(R_{q,j})/e(P)`,

`R_{q,j}=P\{c_1,...,c_j,q}`, and all `Pr_{q,j}` are genuine uniform laws on smaller residual posets after the fixed prefix. Put `beta_q=sum_j beta_{q,j}` and `delta=1-alpha=sum_q beta_q`. Every interruption channel has `beta_q<1/3` in a no-balanced counterexample.

At the first majority-block boundary `x prec_* y`, the exact compatible endpoint result

- `fleet03/B11`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`,

supplies exactly two canonical successor blockers `s_1,s_2`, with

`x lessdot s_i`, and `y,s_1,s_2` pairwise incomparable. The same report proves that the blocker pair is nonautonomous and that every distinguisher of `s_1,s_2` lies after the whole second majority block.

The exact endpoint mass-transport result

- `fleet02/B10`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`,

will be used only through its already-proved first-boundary consequences: in the single-interrupter case `alpha=Pr_P(x<y)>2/3`; in the two-interrupter case, writing `M={y,r}` and `q=Pr_Q(y<r)`,

`q > 1/(3 alpha)`

and the second interrupter satisfies `r<s_i` for at least one canonical blocker.

## 2. Compact conditional end-to-end route

Assume a cardinality-minimal POS3 counterexample `P`. The renewal selector problem left by fleet01/B19 asks for a balanced pair in the smaller uniform poset `Q` that survives the exact renewal mixture, or for a pair meeting the deleted block.

The first unpaid universal issue is that the coefficients `beta_q` were only known from above (`<1/3`). The theorem below gives a sharp lower bound on every interruption coefficient in terms of a genuine first-element probability in uniform `Q`. It then identifies **all** minimal elements of `Q` with the first interruption channels and the two endpoint Hasse blockers. This collapses both the one- and two-interrupter branches much further.

## 3. Tail-prefix injection for every interruption channel

For `q in M`, set

`h_q = m-lambda(q) >= 1`,

and let

`rho_q = Pr_Q(q is the first element) = e(Q\{q})/e(Q)`.

### Theorem 3.1 — interruption coefficient lower bound

For every `q in M`,

`beta_q >= h_q alpha rho_q`.                                      (3.1)

### Proof

Fix `j` with `lambda(q)<=j<=m-1`. The partner residual is

`R_{q,j}=P\{c_1,...,c_j,q}`.

Take any `sigma in L(Q\{q})`. Map it to the word

`c_{j+1},c_{j+2},...,c_m, sigma`.

This is a linear extension of `R_{q,j}`. The tail of `C` is in chain order. Because `C` is an order ideal, no element of `Q` lies below any `c_k`; hence placing the entire remaining chain tail before `sigma` violates no relation. Relations from the tail into `Q` are satisfied, and all relations inside `Q\{q}` are respected by `sigma`.

The map is injective, so

`e(R_{q,j}) >= e(Q\{q})`.

There are exactly `h_q=m-lambda(q)` allowed values of `j`. Therefore

`beta_q e(P)=sum_j e(R_{q,j}) >= h_q e(Q\{q})`

`= h_q rho_q e(Q)=h_q alpha rho_q e(P)`.

Divide by `e(P)`. `□`

This is an actual transfer between uniform smaller-poset laws; no projected biased law is relabelled uniform.

## 4. The minimal elements of Q are exactly interruption elements plus surviving endpoint blockers

Let `S={s_1,s_2}` be the two canonical successor blockers at the first boundary.

### Theorem 4.1 — exact minimum-set localization

Every minimal element of `Q` belongs to

`M union S`.                                                     (4.1)

More precisely:

1. If `M={y}`, then
   `Min(Q)={y,s_1,s_2}`.                                        (4.2)
2. If `M={y,r}`, then
   `Min(Q)={y,r} union {s_i : r || s_i}`.                        (4.3)

### Proof

Let `z in Min(Q)`. If `lambda(z)<m`, then by definition `z in M`. If `lambda(z)=m`, then `x<z`. Since `y` and `z` are distinct minimal elements of `Q`, they are incomparable. Thus `z` is a successor of `x` incomparable with `y`. Minimality of `z` in `Q` makes it minimal among all such successors, so `z` is one of the canonical blockers `s_1,s_2`. This proves (4.1).

Suppose first `M={y}`. If some blocker `s_i` were not minimal in `Q`, choose a minimal predecessor `z<s_i`. By (4.1), `z` is either `y` or the other canonical blocker. The first is impossible because `y||s_i`; the second is impossible because the two canonical blockers are both minimal in the successor-blocker set and hence cannot be ordered. Thus both blockers are minimal, proving (4.2).

Now suppose `M={y,r}`. A blocker `s_i` is nonminimal iff it has a minimal predecessor in `Q`. By (4.1), such a predecessor cannot be `y` and cannot be the other canonical blocker, so it must be `r`. Hence `s_i` is nonminimal iff `r<s_i`, equivalently minimal iff `r||s_i` (the reverse order `s_i<r` is impossible because `r` is minimal). This proves (4.3). `□`

Since `Q` still has width at most three, (4.3) says that in the two-channel case at most one endpoint blocker can survive as a minimum.

## 5. Single interruption: the first interrupter touches only x, and alpha has a stricter cap

Assume `M={y}`. Then `delta=beta_y` and, by the partner endpoint theorem,

`alpha=Pr_P(x<y)>2/3`.                                          (5.1)

By (4.2), `Min(Q)={y,s_1,s_2}`. Put

`q_i=Pr_Q(y<s_i)`,

`rho_y=Pr_Q(y is first)=Pr_Q(y<s_1 and y<s_2)`.

Every non-prefix interruption starts with `y`, so for each blocker

`Pr_P(y<s_i) <= delta + alpha q_i`,

and the no-balanced hypothesis gives

`q_i > U(alpha):=1-1/(3 alpha)`.                                (5.2)

The multivariate XYZ/Shepp inequality in the **uniform** law on `Q` gives

`rho_y >= q_1 q_2 > U(alpha)^2`.                                (5.3)

Combining (3.1), (5.3), and `delta=1-alpha`,

`1-alpha > h_y alpha U(alpha)^2`.                               (5.4)

If `h_y>=2`, then (5.4) implies

`27 alpha^2-21 alpha+2 < 0`.

The roots of the left side are `1/9` and `2/3`, so this is impossible under (5.1). Therefore

> **Corollary 5.1.** In the single-interrupter branch,
>
> `h_y=1`, equivalently `lambda(y)=m-1`.                         (5.5)
>
> Thus `c_{m-1}<y` whenever `m>=2`: inside the first chain block, the first interrupter is incomparable only with the top element `x=c_m`.

With `h_y=1`, (3.1) and (5.3) give

`q_1 q_2 <= rho_y <= (1-alpha)/alpha`.                          (5.6)

Together with `q_i>U(alpha)`, this forces

`U(alpha)^2 < (1-alpha)/alpha`,

or equivalently

`18 alpha^2-15 alpha+1<0`.

Hence

> **Corollary 5.2 — improved single-channel endpoint cap.**
>
> `2/3 < alpha < (5+sqrt(17))/12 = 0.760258802...`.              (5.7)

This improves the previous generic endpoint cap `alpha<7/9` in the single-interrupter branch.

There is also a local selector consequence. From (5.6),

`min(q_1,q_2) <= sqrt((1-alpha)/alpha)`.

If `alpha>=9/13`, the right side is at most `2/3`, while (5.2) is greater than `1/2`. Therefore:

> **Corollary 5.3.** If the single-interrupter coefficient satisfies `alpha>=9/13`, then one of the two endpoint-blocker pairs `(y,s_i)` is already balanced under the uniform law on `Q`.

This does not yet prove that the same pair is balanced in `P`; it localizes the smaller-poset selector to the forced endpoint fork.

## 6. Two interruptions: the second interrupter must itself break the Hasse fork, and alpha<2/3

Assume `M={y,r}`, with `y prec_* r` as in the partner report. Let

`q=Pr_Q(y<r)`.

The partner proves

`q>1/(3 alpha)`                                                   (6.1)

and `beta_y<1/3`.

Suppose for contradiction that `r<s_1` and `r<s_2`. Then (4.3) gives

`Min(Q)={y,r}`.

Therefore `rho_y=Pr_Q(y is first)=Pr_Q(y<r)=q`. By (3.1),

`beta_y >= h_y alpha q >= alpha q > 1/3`,

contradicting `beta_y<1/3`.

Thus `r` cannot lie below both blockers. Width three already forbids `r` from being incomparable with both blockers, because then `y,r,s_1,s_2` would be an antichain. After relabelling, exactly one relation has each type:

`r<s_1`, `r||s_2`.                                               (6.2)

By (4.3),

`Min(Q)={y,r,s_2}`.                                              (6.3)

So the second interrupter `r` itself distinguishes the two endpoint blockers. The fleet03/B11 delayed-distinguisher theorem then places `r` strictly after the whole second majority block. This removes the previously open subcase in which the second interruption channel lay below both arms of the endpoint Hasse fork.

We can also separate the two-channel mass range from the single-channel range. Let

`rho_y,rho_r,rho_s`

be the first-element probabilities of the three minima in (6.3), with `s=s_2`. Applying (3.1) to both interruption channels and using `h_y,h_r>=1`,

`delta=beta_y+beta_r >= alpha(rho_y+rho_r)=alpha(1-rho_s)`.       (6.4)

Hence

`rho_s >= 1-delta/alpha`.                                        (6.5)

Put `q_s=Pr_Q(y<s)`. Since `s` being first precludes `y<s`,

`q_s <= 1-rho_s <= delta/alpha`.                                (6.6)

On the other hand, all residual channels together have mass only `delta`, so

`Pr_P(y<s) <= alpha q_s+delta`.

The no-balanced hypothesis has `Pr_P(y<s)>2/3`; therefore

`q_s > 1-1/(3alpha)=U(alpha)`.                                  (6.7)

Combining (6.6) and (6.7),

`1-1/(3alpha) < (1-alpha)/alpha`,

which is exactly

> **Corollary 6.1 — two-channel alpha range.**
>
> `4/9 < alpha < 2/3`.                                          (6.8)

The lower bound is the inherited one-sided strong-majority-rank mass from the campaign lead. Thus the renewal coefficient `alpha` cleanly separates the two possible channel counts:

- one interrupter: `alpha>2/3` and in fact (5.7);
- two interrupters: `alpha<2/3`.

Finally, if `alpha>=3/5` in the two-channel branch, then (6.6) gives `q_s<=2/3`, while (6.7) gives `q_s>4/9`; hence `(y,s)` is a balanced pair in uniform `Q`. Again, this is a selector localization in `Q`, not yet a transfer to `P`.

## 7. What this pays and what remains unpaid

The partner's renewal selector was previously split only by `|M|=1` versus `|M|=2`, with a broad Hasse-fork incidence in the second case. The present run pays three universal structural arrows:

1. Every interruption coefficient has the lower bound `beta_q>=h_q alpha rho_q` from an explicit tail-prefix injection.
2. `Min(Q)` is completely localized to interruption elements and the two endpoint Hasse blockers.
3. The two-channel branch in which the second interrupter lies below both blockers is impossible; therefore the second interrupter is itself the delayed Hasse-fork distinguisher.

It also proves the sharp branch separation `alpha>2/3` for one interruption versus `alpha<2/3` for two interruptions, plus the single-channel constraint `lambda(y)=m-1` and improved cap `(5+sqrt(17))/12`.

The parent POS3 conjecture remains open. The first remaining selector obligation is now narrower:

- **single channel:** `Min(Q)={y,s_1,s_2}`, the deleted-chain contact is only at the top `x`, and `alpha in (2/3,(5+sqrt(17))/12)`; when `alpha>=9/13` a balanced `Q` pair is already one of `(y,s_i)`;
- **two channels:** after relabelling, `Min(Q)={y,r,s}`, with `r` itself the delayed distinguisher, `r` below the other blocker, and `alpha in (4/9,2/3)`; when `alpha>=3/5`, `(y,s)` is balanced in `Q`.

A complete proof must now show that these **named endpoint-minimum balanced selectors**, when present, cannot all be pushed above `2/3` by their exact renewal channels, or else exploit the complementary narrow alpha ranges (`alpha<9/13` in the single branch and `alpha<3/5` in the two branch) to force a pair meeting the deleted block. No arbitrary balanced pair of `Q` may be assumed to transfer; the partner's exact counterexample remains live.

## 8. Verification

The companion standard-library checker `verify_renewal_selector.py` re-enumerates the source-bound seven-element endpoint-fork witness from fleet03/B11. It verifies:

- `e(P)=79`, `e(Q)=54`;
- `alpha=54/79`, `delta=25/79`;
- in uniform `Q`, `Pr(y<s_1)=20/27`, `Pr(y<s_2)=5/9`, and `rho_y=25/54`;
- in `P`, `Pr(y<s_1,y<s_2)=50/79=delta+alpha rho_y=2 delta`;
- `q_1 q_2=100/243 <= rho_y <= delta/alpha=25/54`;
- the exact polynomial threshold used in Corollary 5.1 has upper root `2/3`.

Captured output:

`eP 79 eQ 54`

`alpha 54/79 delta 25/79`

`q_y_s1 20/27 q_y_s2 5/9 rho_y 25/54`

`joint_P 50/79 2delta 50/79`

`q_product 100/243 delta_over_alpha 25/54`

`single_channel_cap_decimal 0.760258802135`

`POS3_RENEWAL_SELECTOR_REGRESSION_PASS`

The finite computation is regression evidence only. Theorems 3.1 and 4.1 and all branch deductions are symbolic arbitrary-size arguments.

## 9. Scope and provenance

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, permission bypass, production-state mutation, or broad mixed-domain memory was used.
