# POS3 account02/B19 — exact asymmetric-chain, product, and ordinal-sum selector adversaries

**Outcome:** `CANDIDATE_REFUTED` for several concrete selector simplifications; parent POS3 remains **OPEN / NOT PROVED**.  
**Target:** every finite nonchain poset of width at most three has an incomparable pair `x,y` with `1/3 <= Pr(x before y) <= 2/3` under the uniform law on all linear extensions.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-bound collective state actually used

The current collective allocation supersedes the old installation/benchmark work, so this report contains only POS3 mathematics.

The campaign lead `account04/B10` had no source-bound `collective-POS3` report in the authorized mathematical archive at the research snapshot; the direct canonical lead path returned no file. The named partner `account03/B10` likewise had no source-bound POS3 artifact at that snapshot. I therefore did not invent either uptake and instead consumed the newest compatible complete peer chain that was actually present:

1. **account01/B10**, commit `e72e4c5649ca5fa7e865d163e2e58d0c99b771d2`, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`: exact three-chain ideal-state path encoding, exact edge-flux formula, the light-slice anti-concentration certificate, and the heavy-slice normal form for a hypothetical counterexample.
2. **account03/B19**, commit `5bef2fe912a3132306e0e131f24f3992337c93a6`, report blob `106c46c118f9863c6fc7867d2ae536dd0786818e`: an exact nine-element refutation of both the extremal-anchor strengthening and the claim that connected incomparability alone forces a light insertion-slice vector. I directly use its surviving conclusion: the next proof must exploit *alignment* of heavy slices with one common transitive strong-majority order, not just heavy-slice magnitudes.
3. **account02/B11**, commit `8a4f5bf21872cbcfbc38433903f60a1f25faacdf`, report blob `b71c5087c4982769946c31f1ec76242bf297fe17`: exact ordinal factorization by incomparability components. I use this result explicitly in the ordinal-padding argument below.
4. The inherited I0122 source state, canonical claim blob `b9dac0d3f56b5119e495fc70f71769100124fc58`, for the exact uniform-law target and finite frontier context.

No biased induced distribution is replaced by a uniform one below. The one place where a projection becomes uniform is proved by a constant-lift multiplicity argument specific to a parallel union of chains.

## 2. Conditional end-to-end proof chain and first missing implication

The current source-valid conditional chain is compact:

1. By account02/B11, a cardinality-minimal POS3 counterexample may be assumed to have connected incomparability graph; ordinal factors can be removed exactly without changing any internal incomparable-pair probability.
2. By account01/B10, under any fixed three-chain cover every incomparable-pair probability is an exact cumulative edge flux. If all slices for one relevant `(x,C_b)` interval have mass at most `E/3`, a balanced pair exists. Hence in a true counterexample every relevant interval has a unique jump `>E/3`, located at the strong-majority gap.
3. By account03/B19, connectedness plus the mere existence of a `>E/3` slice in every relevant insertion distribution is insufficient: such heavy slices coexist with balanced interior pairs.
4. Therefore the first essential missing implication is still: **rule out simultaneous `>E/3` heavy jumps aligned at the gaps of one common transitive strong-majority order in a connected width-three ideal-state system**, using the inherited majority-block structure or another global conservation identity.

This run attacks selector shortcuts that would try to bypass step 4. The exact adversaries below show that raw depth, extremality, product complementarity, and absolute ambient rank are not safe selectors. They do **not** refute the account01/B10 flux theorem itself.

## 3. Exact asymmetric three-chain shuffle adversary

Let

`Q(a,b,c) = C_a || C_b || C_c`

be the parallel union of three chains, with no cross-chain comparabilities. Its width is at most three, and if all three chains are nonempty its three minimal elements form an antichain, so its width is exactly three. Its incomparability graph is complete tripartite and therefore connected.

### Lemma 3.1 — pair probabilities reduce to an exact two-chain hypergeometric law

Fix elements `A_i in C_a` and `B_j in C_b`. Every `A/B` shuffle word has exactly

`binom(a+b+c,c)`

full lifts obtained by inserting the ordered `C`-steps, independent of the `A/B` word. Hence deleting `C` from a uniform linear extension of `Q(a,b,c)` gives the **uniform** law on the `binom(a+b,a)` binary `A/B` shuffles. Therefore

`Pr(A_i < B_j)`

is exactly

`[1/binom(a+b,a)] * sum_{k=i}^{min(a,i+j-1)} binom(i+j-1,k) binom(a+b-i-j+1,a-k)`.

This is a valid uniform projection only because the lift count is constant in this special parallel-chain family; it does not contradict the nonuniform-projection examples in account01/B10 or account01/B19.

### Concrete core `Q = C_1 || C_4 || C_16`

Here

`e(Q) = 21!/(1!4!16!) = 101745`.

There are exactly

`1*4 + 1*16 + 4*16 = 84`

incomparable unordered pairs. The executed checker evaluates **all 84** probabilities by the formula above. Exactly 22 lie in `[1/3,2/3]`.

However the raw same-depth selector fails on every cross-chain same-index choice that exists:

- `Pr(A_1 < B_1) = 1/5`;
- `Pr(A_1 < C_1) = 1/17`;
- `Pr(B_1 < C_1) = 1/5`;
- `Pr(B_2 < C_2) = 5/57`;
- `Pr(B_3 < C_3) = 31/969`;
- `Pr(B_4 < C_4) = 7/969`.

All have balance `<1/3`, even though the same poset has many balanced witnesses, for example

`Pr(A_1 < B_2)=2/5`, `Pr(B_1 < C_3)=29/57`, and `Pr(B_4 < C_14)=28/57`.

The minimal-element selector also fails on all three chain pairs: the three balances are `1/5`, `1/17`, `1/5`. By reversal the corresponding maximal-element choices have the same balances. Thus asymmetry can make local chain depth and extremality point very far from the balanced window while leaving many interior balanced pairs.

**Selector consequence.** A source-valid width-three selector cannot choose a cross-chain pair solely by equal absolute chain depth or by exposed extremality. It must use cumulative extension mass (or an equivalent invariant), not just the chain coordinates.

## 4. Cartesian products: complete three-dimensional admissibility check

The assignment also asks for products where width permits them. Consider a genuine three-dimensional box

`C_a x C_b x C_c`, with all three side lengths at least two.

If any side length is at least three, the product contains `C_2 x C_2 x C_3`, which has the explicit four-element antichain

`(1,1,0), (1,0,1), (0,1,1), (0,0,2)`.

Hence its width is at least four. Therefore the **only** genuinely three-dimensional nontrivial chain box with width at most three is

`C_2 x C_2 x C_2 = B_3`.

(Boxes with a side of length one are lower-dimensional products and do not give a genuinely three-dimensional product mechanism.)

The exact checker independently counts `e(B_3)=48` and all nine incomparable pairs. Six have probability exactly `1/2`, but the three singleton/complementary-doubleton pairs have probabilities `11/12` or `1/12`. In bit-vector notation:

- `Pr(001 < 110)=11/12`;
- `Pr(010 < 101)=11/12`;
- `Pr(011 < 100)=1/12`;

while every same-rank incomparable pair is `1/2`.

Removing the globally least and greatest elements leaves the six-element nontrivial incomparability component; by the account02/B11 factorization, all nine displayed internal probabilities are unchanged. Thus even in a connected width-three core, an apparently symmetric **complement-pair selector** can have balance only `1/12` while same-rank balanced pairs are available.

**Product consequence.** Genuinely asymmetric 3D boxes are excluded by width before probability analysis; the unique admissible 3D box already refutes the complementary-pair selector. Product symmetry by itself is not a balanced-pair selection principle.

## 5. Ordinal-sum padding gives an infinite selector-adversary family

For arbitrary `r,s >= 0`, put

`P_{r,s} = C_r ⊕ Q ⊕ C_s`,

where `Q=C_1 || C_4 || C_16` is the connected asymmetric core above. Every linear extension is the unique chain prefix, followed by a linear extension of `Q`, followed by the unique chain suffix. Therefore

`e(P_{r,s})=e(Q)`

and every incomparable pair lies in `Q` with **exactly the same probability** as in `Q`.

Thus the complete 84-entry probability table is invariant under arbitrary shifts of ambient size and absolute global rank. This turns the finite core into an infinite family of exact adversaries to any selector that uses absolute position in the whole poset without first passing to its nontrivial incomparability component.

This is precisely where the account02/B11 ordinal-factorization result is applied: a valid proof can and should strip the padding before selecting a pair. The adversary shows that this factor-first step is logically necessary for any ambient-rank selector, not merely a convenience.

## 6. Executed exact certificate

The standard-library checker `verify_asymmetric_adversaries.py` was executed before archival.

- script SHA-256: `14280ebd3f06f2ec674e5668d002146a5c19b2e5c6ad0710746ea21c89000bf5`;
- output SHA-256: `4540e54dcafa67274d6da3cb6bd47593ad6909ac7e786fca3f2cbc84d607ef4d`;
- terminal marker: `POS3_ASYMMETRIC_ADVERSARY_CHECK_PASS`.

The output contains the exact probability and balance for every one of the 84 incomparable pairs of `Q`, all nine incomparable pairs of `B_3`, the width-four antichain check for `C_2 x C_2 x C_3`, and the ordinal-sum invariance assertion.

The computation is evidence and regression protection; Lemma 3.1, the product width obstruction, and the ordinal-sum factorization are written proofs.

## 7. Accepted delta and next owner-facing implication

**Before:** the collective chain had exact flux machinery and knew that extremal anchors / connectedness-to-light-slice were false, but it had not source-bound an asymmetric-chain probability table, classified the genuinely 3D chain-product branch under width three, or converted ordinal padding into a selector-invariance adversary.

**After:** three further selector shortcuts are closed:

1. equal-depth / exposed-extremal selection fails in a connected asymmetric three-chain shuffle core;
2. complementary-pair selection fails in the only genuinely 3D chain box allowed by width three;
3. absolute ambient-rank selection fails under arbitrary ordinal padding unless the B11 incomparability-component reduction is applied first.

The parent target remains open. The surviving high-value route is still the source-valid one from account01/B10 + account03/B19: attack **global common-order alignment of the heavy insertion slices**, not their raw sizes or local coordinate positions.

No novelty or priority claim is made. No benchmark gold, held-out labels, credentials, scheduler identifiers, machine paths, unrelated private data, raw transcripts, email, Drive action, paid model/API/Codex call, remote workflow, public posting, or permission change was used.
