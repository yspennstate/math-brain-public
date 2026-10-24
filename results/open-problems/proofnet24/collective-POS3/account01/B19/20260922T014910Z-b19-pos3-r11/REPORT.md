# POS3 account01/B19 — initial-majority-block deletion, uniform-component decomposition, and rank-one insertion gradient

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact collective state consumed

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` and stays off the superseded brain-installation/benchmark work.

The previous account01/B19 report, blob `c2f771152d5be6943cce6872c500ca81c572e962`, proved the exact arbitrary-deleted-chain recurrence

`W_C(tau)=#{t_1<=...<=t_n : t_i in I(q_i)}`

for `tau=(q_1,...,q_n) in L(P\C)`, together with exact adjacent-swap defects. It showed that endpoint-ordered profiles have context-independent sign, only nested profiles can have context-dependent sign, and a universal arbitrary-chain `|Delta W|<=1` or bounded-density shortcut is false.

The newest team-lead result actually consumed is account04/B10, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-at-most-three counterexample it proves that every element occupies its strong-majority rank with probability `>1/81`; in a one-sided boundary case the same proof gives the stronger bound `>4/9`.

The assigned OTHER-account partner result actually consumed is account02/B10, run `20260922T011840Z-b10-pos3-r11`, report blob `54b518413481e7ed162f44c8b6c417b3f94b5d29`. It gives the exact two-element deletion-fiber corridor formula and proves that a one-boundary local cap is false; the remaining proof must couple weighted excess across boundaries.

I also apply account04/B20 report blob `b6b06537e4543c606c96d3f159567192fc0daeac`, which rewrites a general nested-profile swap as a lower-fringe charge minus an upper-fringe charge. The mechanism below changes the deleted object: instead of deleting a whole chain of a fixed three-chain cover, delete the **first maximal same-chain block of the strong-majority order**. That block is an order ideal. This makes every insertion profile one-sided and collapses the two-fringe defect to a rank-one nonnegative term.

## 2. Compact conditional end-to-end induction

Assume for contradiction that a counterexample exists and choose one with minimum cardinality. Use the inherited transitive strong-majority order `L_*`, and fix any three-chain cover. Let

`C={c_1<...<c_m}`

be the first maximal contiguous block of `L_*` belonging to one cover chain, and set `Q=P\C`.

The following observations are immediate but important.

1. `C` is an order ideal of `P`. If `q<c_j` with `q notin C`, then every linear extension of `P`, hence `L_*`, places `q` before `c_j`, contradicting that `C` occupies the first `m` positions of `L_*`.
2. `C` is proper because `P` is not a chain.
3. `Q` cannot be a chain in a minimal counterexample. If it were, then `P` would be the union of the two chains `C` and `Q`, hence have width at most two, and the known width-two `1/3-2/3` theorem would already give a balanced pair.
4. Therefore `Q` is a smaller nonchain of width at most three. By minimality, under the **uniform** law `nu` on `L(Q)`, some incomparable pair `y,z` is balanced.

Thus a cardinality induction would close POS3 if one could transfer that balanced pair through the exact chain-insertion weights, or else force a balanced pair meeting `C`. The rest of this report derives the exact special structure of those weights. The only remaining unpaid step is a sharply stated weighted-transfer lemma in Section 8.

## 3. Ideal-chain specialization of the exact insertion recurrence

For `q in Q` define

`lambda(q)=max({j : c_j<q} union {0})`.

Because `C` is an ideal, no `q in Q` lies below any `c_j`. Hence in the previous B19 notation

`rho(q)=m`

for every `q`, and the feasible chain-prefix interval is the suffix

`I(q)=[lambda(q),m]`.

For `tau=(q_1,...,q_n) in L(Q)`, restriction/lifting therefore gives the exact formula

`W_C(tau)=#{0<=t_1<=...<=t_n<=m : t_i>=lambda(q_i) for all i}`.      (3.1)

Equivalently, with

`D_1(s)=1{s>=lambda(q_1)}`,

`D_i(s)=1{s>=lambda(q_i)} sum_{r<=s} D_{i-1}(r)`,

we have

`W_C(tau)=sum_s D_n(s)`.                                            (3.2)

So for an initial ideal chain block the full induced density depends only on the sequence of the order-preserving integer label `lambda` along `tau`; no upper-profile coordinate survives.

The map `lambda` is order-preserving on `Q`: if `u<v` in `Q`, then every `c_j<u` also satisfies `c_j<v`, hence `lambda(u)<=lambda(v)`.

## 4. The deleted-block law contains more than four ninths of the uniform law

Let `e(R)=|L(R)|`, let `nu` be uniform on `L(Q)`, and let `mu` be the restriction to `Q` of a uniform random linear extension of `P`. By (3.1),

`mu(tau)=W_C(tau)/e(P)`,

and

`e(P)=sum_{tau in L(Q)} W_C(tau)=e(Q) E_nu W_C`.                   (4.1)

Because `C` is an ideal, every `tau in L(Q)` has exactly one lift with the entire chain `C` first, namely

`c_1,...,c_m,tau`.

Hence

`Pr_P(C is the initial m-element block)=e(Q)/e(P)=1/E_nu W_C`.      (4.2)

Now apply the account04/B10 one-sided rank estimate to the last block element `c_m`. All elements preceding `c_m` in `L_*` are `c_1,...,c_{m-1}`, already forced below it. Thus the uncertain predecessor boundary is empty, while width at most three leaves at most two uncertain minimal successors. The same multivariate XYZ argument as in the lead report yields

`Pr_P(rank(c_m)=m)>4/9`.                                            (4.3)

Since `c_1<...<c_m`, the event `rank(c_m)=m` is exactly the event that `C` is the first `m` elements. Combining (4.2) and (4.3),

`E_nu W_C < 9/4`.                                                   (4.4)

More precisely, set

`alpha=e(Q)/e(P)=1/E_nu W_C > 4/9`.

If there are any non-prefix lifts, define

`eta(tau)=(W_C(tau)-1)/(e(P)-e(Q))`.

Then `eta` is a probability law on `L(Q)` and

`mu = alpha nu + (1-alpha) eta`.                                   (4.5)

This is an exact decomposition, not a density comparison: **more than four ninths of the projected law is literally the uniform law on `L(Q)`**. The remaining component `eta` is exactly the law generated by lifts in which some element of `Q` interrupts the chain block before `c_m`.

Consequently, if a `nu`-balanced pair event `A={y<z}` is unbalanced under `mu`, the non-prefix law `eta` must be unbalanced on the same side. For example, if `nu(A)=1/2`, then (using `alpha>4/9`)

`mu(A)>2/3  =>  eta(A)>4/5`,

and

`mu(A)<1/3  =>  eta(A)<1/5`.                                      (4.6)

Thus any failure of cardinality induction is forced into an extremely oriented non-prefix component.

## 5. Rank-one adjacent-swap defect for an initial ideal chain

The ideal-block specialization removes the context-sensitive sign problem from the previous arbitrary-chain recurrence.

Let `S={0,...,m}`, let `U` be the matrix

`U_{st}=1{s<=t}`,

and for an interval `I` let `D_I` be its diagonal indicator matrix. Formula (3.1) can be written

`W_C(q_1...q_n)=1^T D_{I(q_1)} U D_{I(q_2)} U ... U D_{I(q_n)} 1`.

Consider adjacent incomparable `u,v` in a linear extension of `Q`, and write

`a=lambda(u)`, `b=lambda(v)`.

Assume `a<=b`. Put `A=[a,m]`, `B=[b,m]`. The exact local commutator is

`D_A U D_B - D_B U D_A`

`= 1_[a,b-1] 1_[b,m]^T`.                                          (5.1)

Indeed, a matrix entry survives precisely when the first chain-prefix state lies in `[a,b-1]` and the second in `[b,m]`. All entries are nonnegative.

Absorb all earlier factors into a nonnegative prefix row `p^T` and all later factors into a nonnegative suffix column `s`. Then

`W_C(...,u,v,...)-W_C(...,v,u,...)`

`= (sum_{r=a}^{b-1} p_r) (sum_{t=b}^{m} s_t) >= 0`.               (5.2)

This is stronger than a known-sign statement: the entire defect factors as a **rank-one boundary product**. If `a=b`, the two weights are exactly equal. If `a>b`, the reverse inequality follows by symmetry.

Equation (5.1) is exactly the account04/B20 lower-fringe-minus-upper-fringe identity after the present ideal-block choice kills the upper fringe. It also explains why the account02/B10 two-sided endpoint corridor obstruction disappears for this particular deletion: all feasible profiles share the same upper endpoint `m`.

## 6. Global consequence: the weight is driven by lambda-inversions

Because `lambda` is order-preserving on `Q`, any adjacent inversion

`lambda(u)>lambda(v)`

inside a linear extension must consist of incomparable elements. Swapping that adjacent inversion is therefore a legal linear-extension move. By (5.2), it weakly **increases** `W_C`.

Repeatedly bubble-sorting adjacent lambda-inversions transforms every `tau in L(Q)` into a lambda-nondecreasing linear extension without decreasing the weight. Thus:

> **Theorem 6.1 — ideal-block mode theorem.** `W_C` is maximized on the lambda-nondecreasing linear extensions of `Q`. Every adjacent lambda-inversion carries a one-signed, rank-one exact loss given by (5.2).

All lambda-nondecreasing extensions have the same lambda-word, and (3.1) depends only on that word, so they have the same maximum weight.

This gives a global orientation to the exact nonuniform deletion law. The generic full-chain deletion had nested profiles with context-dependent signs; the initial-majority-block deletion has no such sign changes.

## 7. Genuine source-valid warning: the mean bound alone does not transfer balance

The quantitative bound `E_nu W_C<9/4` is not enough by itself.

Take the four-element width-two poset with

`c_1<c_2<v`

and one element `u` incomparable with `c_1,c_2,v`. Delete the ideal chain `C={c_1,c_2}`. Then `Q={u,v}` is a two-element antichain, so under the uniform law `nu`,

`nu(u<v)=1/2`.

Here

`lambda(u)=0`, `lambda(v)=2`,

and the exact recurrence gives

`W_C(uv)=3`, `W_C(vu)=1`.

Therefore

`E_nu W_C=2<9/4`,

but under the projected law

`mu(u<v)=3/4`.

So neither the `9/4` mean bound nor the `>4/9` uniform-component mass alone preserves a balanced pair. This is an actual finite poset, not an abstract weight vector.

Crucially, it does **not** refute the induction route: the same poset has

`Pr(c_2<u)=1/2`,

so a pair meeting the deleted chain is balanced. The example therefore identifies exactly what the missing transfer theorem must use: the hypothesis that **all** incomparable pairs meeting `C` are already strongly oriented, not only a scalar bound on `W_C`.

## 8. First essential missing implication after this run

The full-chain width-two projection route left an aggregate two-fringe charge. The present cardinality-induction route reduces the first unpaid statement further.

> **Ideal-block weighted balance transfer (IBWT).** Let `P` be a cardinality-minimal hypothetical POS3 counterexample, let `L_*` be its strong-majority order, let `C` be the first maximal same-chain block of `L_*` in a fixed three-chain cover, and put `Q=P\C`. Let `nu` be uniform on `L(Q)` and `mu` the exact projected law from `P`. Since `Q` is a smaller nonchain, choose a `nu`-balanced incomparable pair `y,z`. Prove that the exact one-sided insertion system (3.1), together with the counterexample constraints `Pr_P(c_i<q)>2/3` for every incomparable `c_i in C, q in Q`, prevents `mu(y<z)` from leaving `[1/3,2/3]`.

Equivalently, if `mu(y<z)` does leave the interval, prove that some incomparable pair meeting `C` has probability in `[1/3,2/3]`.

The new bookkeeping available for this implication is exact:

1. `mu` has the uniform component (4.5) with `alpha>4/9`;
2. all failure is concentrated in the non-prefix component `eta`;
3. the entire local weight gradient is one-signed and rank one, (5.2);
4. the bias is organized by the order-preserving integer label `lambda`, with no nested/context-sensitive sign reversal;
5. the scalar-only version is genuinely false by Section 7, so the next proof must exploit the chain-touching `>2/3` constraints.

A natural next mechanism is to decompose `eta` by the **first outside interruption of `C`** and charge the resulting rank-one lambda-inversion mass to the exact events `q<c_i`. That is now a strictly one-boundary accounting problem rather than the prior two-fringe arbitrary-chain problem.

## 9. Regression verification

The companion deterministic standard-library verifier `verify_ideal_block_recurrence.py` checks:

- `1,771` suffix-interval matrix cases through chain length `20`, entry-by-entry verifying the rank-one identity (5.1);
- `160,413` adjacent lambda-inversion cases in exact recurrence words through chain length `5` and word length `6`, verifying that sorting an inversion never decreases `W_C`;
- the exact four-element scalar-transfer warning `W(uv)=3`, `W(vu)=1`, uniform probability `1/2`, weighted probability `3/4`.

The archived terminal marker is

`POS3_IDEAL_BLOCK_RECURRENCE_CHECK_PASS`.

Verifier SHA-256: `ce938445a0c04c0cd2089a5b6b8b2cb6c13e4837f96597c7f32f58650137addb`.  
Output SHA-256: `8fe90a65532e948005bf55eff6eb6ad807f7509ce77e621e276bb5478c38edfc`.

These computations are regression checks only. The mathematical results are the explicit recurrence, counting identities and matrix factorization above.

## 10. Status and provenance

- Exact ideal-block specialization (3.1)-(3.2): **PROVED**.
- Exact prefix/uniform-component decomposition (4.2)-(4.5): **PROVED**, using the lead's one-sided `>4/9` theorem under the no-balanced-counterexample hypothesis.
- Exact rank-one adjacent-swap defect (5.1)-(5.2): **PROVED**.
- Lambda-mode theorem: **PROVED**.
- Scalar-only transfer: **REFUTED by a source-valid width-two poset**.
- IBWT: **OPEN / first essential missing implication**.
- Full POS3: **OPEN / NOT PROVED**.
- Run classification: **`ESSENTIAL_STEP_APPLIED`**.

No benchmark gold, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive content, paid model/API/Codex execution, remote workflow, public posting, permission change or production-brain mutation was used. Repository retrieval was source inspection only; no authenticated brain retrieval/context was consumed, so the run remains `WITHOUT_VERIFIED_BRAIN`.
