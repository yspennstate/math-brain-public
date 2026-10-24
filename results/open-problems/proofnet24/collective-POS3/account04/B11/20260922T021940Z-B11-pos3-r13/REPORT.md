# POS3 account04/B11 — arbitrary balanced-pair transfer through an initial ideal block is false

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

The refuted candidate is **not POS3** and is not the existential induction route itself. It is the stronger pairwise transfer statement suggested by the newest exact ideal-block decomposition: that once every incomparable pair meeting the deleted initial block is already strongly oriented, an arbitrary pair that is balanced under the uniform law on the smaller poset must remain balanced under the exact projected law. A five-element width-three poset disproves that strengthening. This matters because the partner's remaining induction step must make a global/adaptive choice among the balanced pairs of the smaller poset; it cannot freeze an arbitrary one before applying the insertion weights.

## 1. Exact state consumed

I used only the current POS3 state relevant to the assigned bounded-variance/high-comparability residue.

1. **Team lead account04/B10**, run `20260922T011127Z-account04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-at-most-three counterexample, the transitive strong-majority order pins every element to its strong-majority rank with probability `>1/81`; in a one-sided endpoint case the same argument gives `>4/9`.
2. **Assigned partner account01/B19**, run `20260922T014910Z-b19-pos3-r11`, report blob `004a04191bf389e3493c3346fd57e67b35500049`, plus late delta blob `dba594662b26fe4b1bd8d8e4f59b17342758a7f7`. For the first initial ideal chain block `C={c_1<...<c_m}` in a fixed three-chain cover and `Q=P\C`, it proves the exact recurrence
   
   `W_C(tau)=#{0<=t_1<=...<=t_n<=m : t_i>=lambda(q_i)}`
   
   for `tau=(q_1,...,q_n) in L(Q)`, where `lambda(q)=max{j:c_j<q}`. It also proves the exact decomposition
   
   `mu = alpha nu + (1-alpha) eta`,  `alpha=e(Q)/e(P)>4/9`,
   
   where `nu` is uniform on `L(Q)` and `mu` is the restriction of the uniform law on `L(P)`. Its adjacent-swap defect is rank one and one-signed for this ideal-block choice. The late delta further shows that at the first strong-majority boundary the non-prefix component reverses the endpoint majority on more than `2/5` of its mass.
3. **account02/B10**, run `20260922T014627Z-account02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`. It proves the endpoint blocker-product cap `2/3 < Pr(x<y) < 7/9` in a hypothetical counterexample and activates both Hasse-blocker channels.
4. **Previous B11 result**, report blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`. Using Peczarski's 6-thin theorem and Aires--Kahn Theorem 1.6, any hypothetical width-three counterexample lies in a bounded incomparability-range band `7<=pi(P)<=K_3`; that report also proves that bounded range, bounded rank variance, bounded one-element insertion multiplicity, connected incomparability and module-primality still do **not** imply a finite kernel.

The external theorem used in the inherited variance route is Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1 (2025). Their Theorem 1.5 / Theorem 2.5 reduces bounded-width large-variance balance to a lower bound on the maximum rank atom, and Theorem 2.6 supplies the two-sided XYZ product estimate. Peczarski, *The Gold Partition Conjecture for 6-Thin Posets*, Order 25 (2008), proves the Gold Partition Conjecture when every element is incomparable with at most six others.

## 2. Conditional end-to-end route and the first transfer question

Assume for contradiction that a width-at-most-three counterexample exists and choose one of minimum cardinality. The completed collective reductions give a transitive strong-majority order and allow the first initial ideal chain block `C` to be deleted. The smaller nonchain `Q=P\C` satisfies POS3 by minimality under its **uniform** law `nu`, so at least one incomparable pair of `Q` is `nu`-balanced.

The projected law `mu` on `L(Q)` coming from the uniform law on `L(P)` is not uniform: it has density proportional to the exact insertion weight `W_C`. The partner's open induction step is therefore a **selection/transfer** statement.

A tempting strengthening is:

> **Pairwise-IBWT candidate.** Suppose every incomparable pair meeting `C` is already strongly oriented in the `C`-before-`Q` direction and `alpha>4/9`. Then **every** pair balanced under `nu` remains balanced under `mu`.

This statement would make the induction immediate after selecting any balanced pair in `Q`. It is false, even for width exactly three and even with `alpha=8/11`.

## 3. Exact five-element counterexample to Pairwise-IBWT

Let `P` have elements

`c,a,b,r,s`

with transitive closure generated by

`c<b<r`, `a<r`, `c<s`.

Put `C={c}` and `Q=P\{c}`. Thus `Q` has only the relations

`a<r`, `b<r`,

and `s` is incomparable with `a,b,r`.

### 3.1 Width, ideal block and cross orientation

The set `{a,b,s}` is an antichain, so `width(P)>=3`. A direct check of the defining relations shows no four-element antichain, hence `width(P)=3`.

`C={c}` is an ideal. The only element of `Q` incomparable with `c` is `a`; all of `b,r,s` lie above `c`. Exact enumeration gives

`e(P)=11`,

`#{L in L(P): c<a}=8`,

so

`Pr_P(c<a)=8/11>2/3`.

Thus **every** incomparable pair meeting `C` (there is exactly one) is already strongly oriented from `C` toward `Q`.

The majority order is the transitive order

`c, a, b, s, r`.

For the three-chain cover `{c<b<r}`, `{a}`, `{s}`, the first same-chain block is exactly `C={c}` and its next element `a` is genuinely incomparable with `c`.

### 3.2 Exact ideal-block weights

For a one-element ideal block, the partner recurrence has a useful closed form. Here `m=1` and `lambda(q)` is `0` when `q||c`, `1` when `c<q`. A nondecreasing binary insertion sequence has one switch from `0` to `1`, so

> `W_C(tau) = 1 + (length of the initial prefix of tau consisting of lambda=0 elements)`.

In this example only `a` has `lambda=0`. Therefore `W_C(tau)=2` exactly when `a` is first in `tau`, and `W_C(tau)=1` otherwise.

The eight uniform extensions of `Q`, with their exact restriction weights, are

| `tau` | `W_C(tau)` |
|---|---:|
| `a b r s` | 2 |
| `a b s r` | 2 |
| `a s b r` | 2 |
| `b a r s` | 1 |
| `b a s r` | 1 |
| `b s a r` | 1 |
| `s a b r` | 1 |
| `s b a r` | 1 |

The weights sum to `11=e(P)`, as they must. The prefix event `c` first has exactly one lift for every extension of `Q`, hence

`alpha=e(Q)/e(P)=8/11>4/9`.

### 3.3 A balanced pair is pushed out of the interval

Under the uniform law `nu` on `L(Q)`, the event `a<s` occurs in five of the eight extensions:

`nu(a<s)=5/8`,

so `(a,s)` is balanced.

Under the projected law `mu`, the same five extensions carry total weight

`2+2+2+1+1=8`,

therefore

`mu(a<s)=8/11>2/3`.

So an honestly uniform-balanced pair of the smaller poset becomes **unbalanced** after the exact ideal-block insertion weights are restored, despite all incomparable pairs meeting `C` already being strongly oriented and despite the uniform component having mass `8/11`.

This refutes Pairwise-IBWT.

It does **not** refute the existential induction target. In the same example

`nu(a<b)=1/2`, while `mu(a<b)=7/11`,

so another balanced pair survives. The parent POS3 statement is therefore untouched; indeed this five-element poset itself has balanced pairs.

## 4. What is now the exact unpaid implication

The counterexample removes an ambiguity in the partner's open transfer step. A successful induction cannot say “take an arbitrary `nu`-balanced pair and transfer it.” The remaining statement must be genuinely existential and adaptive to the insertion density:

> **Existential ideal-block transfer (still open).** In a cardinality-minimal hypothetical POS3 counterexample, with first initial ideal chain block `C`, `Q=P\C`, uniform law `nu` and exact projected law `mu`, prove that **some** `nu`-balanced incomparable pair of `Q` remains `mu`-balanced, or else an incomparable pair meeting `C` is balanced.

Under the counterexample assumption the second alternative is excluded, so the burden is to choose a surviving pair globally. This is strictly weaker than the refuted Pairwise-IBWT and is the correct target for the induction route.

The one-element formula above also identifies the mechanism that any selection theorem must control. Even when all cross comparisons point strongly away from the block, `W_C` performs a **prefix-size bias**: extensions beginning with elements that can interrupt `C` receive extra weight. For longer `C`, account01/B19's rank-one lambda-gradient is the higher-dimensional version of the same effect. Hence the next proof must compare the *set* of balanced pairs against this prefix/lambda geometry; a scalar uniform-component lower bound or pairwise stability claim cannot suffice.

## 5. Verification

The companion deterministic standard-library verifier

`verify_pairwise_ibwt_counterexample.py`

independently enumerates the linear extensions of `P` and `Q`, computes the exact rational probabilities, verifies width three, identifies the unique `C`-touching incomparable pair, checks all restriction weights, and confirms that `(a,s)` moves from `5/8` to `8/11` while `(a,b)` moves from `1/2` to `7/11`.

Its captured output is:

```text
POS3_PAIRWISE_IBWT_COUNTEREXAMPLE_PASS
eQ=8 eP=11 widthP=3
Pr_Q(a<s)=5/8 Pr_P(a<s)=8/11
Pr_P(c<a)=8/11 prefix_mass=8/11
Pr_Q(a<b)=1/2 Pr_P(a<b)=7/11
restriction_weight_multiset=[1, 1, 1, 1, 1, 2, 2, 2]
```

This finite computation verifies the explicit counterexample only. The arbitrary-size POS3 target remains open, and no finite census is promoted to closure.

## 6. Status and source-bound handoff

- Actual bounded-width variance/range residue `7<=pi(P)<=K_3`: **PRESERVED**.
- Finite-kernel shortcut from bounded range/variance/local insertion: **previously refuted**.
- account01/B19 exact ideal-block recurrence, uniform-component decomposition and rank-one swap gradient: **APPLIED**.
- Pairwise-IBWT (“every uniform-balanced pair transfers”): **REFUTED** by the exact width-three example above.
- Existential ideal-block transfer: **OPEN** and now stated without the false pairwise strengthening.
- POS3: **OPEN / NOT PROVED**.

The next high-value step is to exploit the set of `nu`-balanced pairs together with the lambda-prefix ordering, rather than freeze one pair before weighting. A useful attack is to prove a minimax/selection lemma for the exact weights `W_C`: either some balanced pair is stable under the lambda-gradient, or the same gradient forces a cross-block comparison into `[1/3,2/3]`. The present example should be retained as a mandatory regression witness for any such theorem.

No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive data, paid model/API/Codex call, remote workflow, permission change or public release was used. No brain retrieval/context was authenticated in this run, so the result remains `WITHOUT_VERIFIED_BRAIN`.
