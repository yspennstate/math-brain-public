# POS3 account03/B19 — weighted chain-deletion compression theorem and an exact weighted-width-two obstruction

**Run:** `20260922T020106Z-account03-B19-pos3-r11-a3f7`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This run deliberately changes mechanism from the two preceding B19 finite light-slice counterexamples.  The new mechanism is a global rank-gap conservation law that survives **arbitrary positive weighting of the deleted-poset extensions**, hence in particular survives the exact nonuniform chain-deletion law.  I then apply the current campaign-lead `1/81` result to that weighted law and use exact ideal-state counting to show why a stronger “the weighted width-two remainder itself must contain a balanced pair” induction is false.

## 1. Source-bound state actually consumed

1. **Named partner / campaign lead `account04/B10`.**  
   `proofnet24/collective-POS3/account04/B10/20260922T011127Z-account04-B10-POS3-r11/REPORT.md`, blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`.  In every hypothetical width-three counterexample, for every element `q` the exact three-chain central cell at the strong-majority rank has probability `>1/81`:
   `81 W_q(g_b(q),g_c(q)) > E`.
2. **Other-account exact deletion theorem `account01/B19`.**  
   `proofnet24/collective-POS3/account01/B19/B19-20260921T235148Z-pos3-r01/REPORT.md`, blob `2c2a46da29d5b4114b5a7f71e6b0072d27b9c437`.  If a chain `C` is deleted and `Q=P\C`, then a uniform extension of `P` projects to the genuinely weighted law
   `mu_C(tau)=W_C(tau)/e(P)` on `L(Q)`, where `W_C(tau)` is the exact monotone-corridor insertion multiplicity.  Pair probabilities in `Q` are preserved only under this weighted law; replacing it by the uniform law is invalid.
3. **Other-account multi-boundary endpoint state `account02/B10`.**  
   `proofnet24/collective-POS3/account02/B10/20260922T014627Z-account02-B10-pos3-r12/REPORT.md`, blob `acdb868b3e35a9248d494126311bfff3bfee150b`.  At a first or last strong-majority boundary, both canonical Hasse-blocker channels are active in exact deletion flow, but the next unpaid step is genuinely multi-boundary.
4. **This slot's preceding exact adversary.**  
   `proofnet24/collective-POS3/account03/B19/20260922T010520Z-b19-pos3-r11/REPORT.md`, blob `b32278d17e70387d51be17fd0d0ac912bae48f5e`.  It supplies a connected module-prime nine-element poset with `E=349` that is not a POS3 counterexample but has only two balanced pairs, both interior.

No induced law below is treated as uniform unless it actually is uniform.

## 2. A global conservation law for any weighted extension law

Let `Q` be a finite poset.  Fix a total order

`v_1 prec_* v_2 prec_* ... prec_* v_m`

that extends `Q`.  Partition this reference order into its maximal contiguous blocks

`B_1,...,B_k`

such that each `B_j` is a chain of `Q`.  For `j=1,...,k-1`, let `x_j` be the last element of `B_j` and `y_j` the first element of `B_{j+1}`.  Maximality implies `x_j || y_j`.

For a linear extension `tau` of `Q`, write `r_tau(v)` for the rank of `v` in `tau`.

### Theorem 2.1 — boundary rank-gap compression

For **every** `tau in L(Q)`,

`sum_{j=1}^{k-1} [r_tau(y_j)-r_tau(x_j)] <= k-1`.       `(RG)`

Consequently, for every probability law `nu` on `L(Q)`, however nonuniform,

`sum_j E_nu[r(y_j)-r(x_j)] <= k-1`,

and therefore at least one boundary satisfies

`E_nu[r(y_j)-r(x_j)] <= 1`.                              `(COMP)`

### Proof

Telescope along the full reference order:

`sum_{i=1}^{m-1} [r_tau(v_{i+1})-r_tau(v_i)] = r_tau(v_m)-r_tau(v_1) <= m-1`.

There are exactly `m-k` adjacent reference-order pairs lying inside the chain blocks.  For each such pair, `v_i <_Q v_{i+1}`, hence every linear extension satisfies

`r_tau(v_{i+1})-r_tau(v_i) >= 1`.

Subtracting the contribution of these `m-k` internal adjacencies from the telescoping bound leaves `(RG)`:

`sum_boundary gap <= (m-1)-(m-k)=k-1`.

Taking expectation under an arbitrary law proves the weighted form, and averaging the `k-1` boundary terms gives `(COMP)`.  No probabilistic independence, uniformity, width hypothesis, or finite enumeration is used. `□`

This is the first global conservation identity in the current B19 line that directly survives the biased chain-deletion law.

## 3. Exact chain-deletion corollary: a strong compressed boundary survives the bias

Now let `P` be a hypothetical POS3 counterexample, fix a three-chain cover, delete one chain `C`, and put `Q=P\C`.  Let `L_*` be the inherited transitive strong-majority order of `P` and restrict it to `Q`.  By `account01/B19`, the restriction of a uniform random extension of `P` to `Q` has the exact law

`mu_C(tau)=W_C(tau)/e(P)`.

Suppose `Q` is not a chain.  Apply Theorem 2.1 to `L_*|_Q` and its maximal contiguous `Q`-chain blocks.  Every block boundary `x_j,y_j` is incomparable in `P`, and because `L_*` is the strong-majority order of a counterexample,

`Pr_P(x_j<y_j)>2/3`.

But the same probability under `mu_C` is exactly the original probability, because deleting `C` does not change the relative order of `x_j,y_j` inside a full extension.  Hence:

### Corollary 3.1 — exact weighted compressed-boundary obligation

For **every** deleted chain `C` for which `Q=P\C` is nonchain, a hypothetical POS3 counterexample contains a boundary pair `x||y` in `L_*|_Q` such that simultaneously

`Pr_{mu_C}(x<y)=Pr_P(x<y)>2/3`,                           `(S)`

and

`G_C(x,y):=E_{mu_C}[r_Q(y)-r_Q(x)] <= 1`.                `(C)`

Equivalently, entirely in exact integer corridor weights,

`sum_tau W_C(tau) 1[x<_tau y] > (2/3)e(P)`,

while

`sum_tau W_C(tau)(r_tau(y)-r_tau(x)) <= e(P)`.

This is a strictly smaller weighted-transfer target than proving the full `1/3–2/3` theorem for every corridor-weighted width-two law: any chain-deletion induction need only show that the exact corridor structure cannot sustain a **strong compressed boundary** without producing a balanced pair elsewhere.

## 4. The partner's `1/81` atom also survives the projection

The named partner result gives more than `(S)` and `(C)`.

Let `q in Q` lie on chain `C_a`; let the other retained chain be `C_b` and the deleted chain be `C_c=C`.  In the partner's exact three-chain cell notation, the event

`J_b(q)=g_b(q), J_c(q)=g_c(q)`

has probability `>1/81` in a hypothetical counterexample.  On this event the number of retained-chain elements before `q` is exactly the number before `q` in `L_*|_Q`.  The own-chain prefix is forced.  Therefore this central-cell event is contained in

`{ r_Q(q)=r^*_Q(q) }`

under the weighted projection law `mu_C`.

Thus:

### Corollary 4.1 — projected pinned-rank atom

For every `q in Q`,

`Pr_{mu_C}(r_Q(q)=r^*_Q(q)) > 1/81`.                     `(A81)`

This is an actual application of the current `account04/B10` result.  It does **not** assert that `mu_C` is uniform; it transfers a source-exact event through the genuine projection.

Combining `(S)`, `(C)` and `(A81)`, the first unpaid weighted implication is now concrete:

> **Compressed weighted-width-two implication.**  For a width-two remainder with an exact third-chain corridor weight, rule out a reference-order block boundary that is simultaneously strong (`>2/3`), rank-compressed (`G_C<=1`), and surrounded by the partner-certified pinned-rank atoms (`>1/81`), unless some pair involving the deleted chain is balanced.

The last clause is essential, as the exact certificate below shows.

## 5. Exact obstruction: the weighted width-two remainder can have no balanced pair at all

Use the preceding B19 module-prime poset `P*` on `{0,...,8}` generated by

```text
0<2, 0<3, 0<4,
1<4, 1<5,
2<5,
3<6, 3<7,
4<7, 4<8,
5<8, 6<8.
```

It has `E=349` linear extensions.  Delete the chain

`C=(2<5<8)`.

The remainder is the width-two poset

`Q=(0<3<6) union (1<4<7)`.

Project every one of the 349 **uniform** extensions of `P*` to `Q`; equal projected words are retained with their exact multiplicities `W_C(tau)`.  The support has 14 distinct projected words and total weight 349.

Take the reference order

`0,1,3,4,6,7`.

Every adjacent pair here is incomparable in `Q`, and all five are strong under the exact weighted law:

```text
pair     #x<y / 349     weighted rank-gap numerator /349
0,1      244/349        265/349
1,3      247/349        320/349
3,4      255/349        376/349
4,6      236/349        281/349
6,7      261/349        310/349
```

More strongly, **every incomparable pair wholly inside `Q` is unbalanced outside `[1/3,2/3]` under `mu_C`**.  The six exact balance numerators are

```text
(0,1):105, (1,3):102, (1,6):24,
(3,4):94,  (4,6):113, (6,7):88,
```

all strictly below `349/3`.

So the natural stronger induction claim

> “after deleting one chain, the exact corridor-weighted width-two remainder itself must contain a balanced pair”

is **false**.

The global compression theorem nevertheless fires exactly as predicted.  The sum of the five weighted signed rank gaps is

`1552/349 < 5`,

and four of the five boundaries are individually compressed:

```text
(0,1):265/349,
(1,3):320/349,
(4,6):281/349,
(6,7):310/349.
```

The weighted projected rank atoms at their displayed reference ranks are also large:

```text
0:244/349, 1:142/349, 3:153/349,
4:142/349, 6:148/349, 7:261/349,
```

all far above `1/81`.

Yet `P*` itself is not a POS3 counterexample.  Its balanced pairs are precisely supplied across the deletion interface: `(2,3)` and `(5,6)` each have numerator `156/349` in the displayed orientation.  Both pairs use the deleted chain.

**Consequent correction to the induction strategy.**  A valid chain-deletion proof cannot aim only to find a balanced pair inside the weighted two-chain remainder.  It must use the compressed-boundary / corridor defect to charge mass to **deleted-chain pair events**.  This is exactly the type of cross-interface accounting retained by the `account01/B19` forward/backward insertion recurrence.

## 6. Exact executable check

Companion checker:

`verify_weighted_projection_compression.py`

Executed SHA-256 before upload:

`4ea642dc43e71b5aff3bfc24e4af7cc958cbeb66629efc152f9614d52dc107a5`.

Captured output SHA-256:

`0a435fa0edf3b4e63c8d04f73b547a235d619520ec100e7e5548948eea3e17d3`.

The checker independently constructs the transitive closure, enumerates all 349 extensions, projects them with exact multiplicity, verifies all weighted pair counts, verifies the rank-gap telescope numerically, verifies the projected atoms, and checks that the parent balanced pairs use the deleted chain.  It terminates with

`POS3_B19_WEIGHTED_PROJECTION_COMPRESSION_PASS`.

The finite computation certifies only the stated obstruction/example.  Theorem 2.1 and Corollaries 3.1/4.1 are symbolic arbitrary-size deductions.

## 7. What moved / next exact implication

**Moved this run:**

1. A new arbitrary-law boundary rank-gap conservation theorem gives a compressed boundary after **every exact chain deletion**, with no false uniformization.
2. The named partner's `>1/81` central cell transfers to a `>1/81` projected rank atom under the same nonuniform law.
3. Exact ideal-state counting refutes the stronger weighted-width-two-only balance transfer: a legal width-three chain deletion can leave a weighted width-two law with **no** balanced pair anywhere in the remainder.
4. The exact escape in the adversary is through pairs that meet the deleted chain, isolating where the next charge must land.

**First remaining global implication:** derive a signed identity/injection that takes a strong compressed boundary `(S)+(C)` in the weighted remainder, keeps the partner atom `(A81)`, and charges the nested/context-sensitive part of its corridor swap defect to one or more `C`-involving pair numerators strongly enough to force one into `[1/3,2/3]`.  This directly targets the indispensable nested-defect term identified by `account01/B10`; choosing another chain cover or replacing the projection by a uniform law cannot pay it.

## 8. Status

- Boundary rank-gap compression for arbitrary extension laws: **PROVED**.
- Exact chain-deletion strong-compressed-boundary corollary: **PROVED**, conditional only on the standard hypothetical-counterexample strong-majority state.
- Transfer of the `account04/B10` `>1/81` central cell to a projected rank atom: **PROVED**.
- “Corridor-weighted width-two remainder always contains a balanced pair”: **REFUTED** by the exact 349-extension deletion above.
- Parent POS3: **OPEN / NOT PROVED**.

No novelty or priority claim is made.  No benchmark work, brain installation, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, remote workflow, or permission change was used.
