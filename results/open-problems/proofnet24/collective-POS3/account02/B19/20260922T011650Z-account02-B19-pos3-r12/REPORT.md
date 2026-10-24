# POS3 account02/B19 — asymmetric-chain contraction adversary

**Outcome:** `CANDIDATE_REFUTED`  
**Parent POS3 status:** `OPEN / NOT PROVED`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## Source state consumed

This run implements `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` under OWNER CONTROL revision `2026-09-22.2`. The owner reallocation supersedes the former B19 installation/benchmark duty, so this run performed POS3 mathematics only.

Fresh `math-research-brain` control was read at main `2e5d66287c96d5111d791b3b30df729667502443`; before the actual-hour write it was re-resolved to `db5ae889a1426463c9d55eccb929093756909a03`, and the intervening 16 commits changed only run/login/handoff artifacts, not protected controls. Exact control Git blobs: AGENTS `94387098453b9f4a9b10179183f6f6ec780fd987`; README `3d4a9372c87802ab734141a3374d04c8823372e3`; fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`; roles `ed17ecc94f76720c0345b3e32249b791b20ec611`; PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`; ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`; TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`.

The named campaign lead `account04/B10` had no completed source-bound collective-POS3 report in the bounded fresh search at the start of this run, so no lead theorem is fabricated. I consumed and applied these exact completed OTHER-account results instead:

- named partner **account03/B10**, run `account03-B10-20260922T001407Z-pos3-r11`, scientific report blob `388ac28e375df4e7a49f72ffbf540f362e03696e`: in a hypothetical no-balanced width-three poset, every element has a pinned common-majority-rank atom at least `E/19683`;
- **account01/B10**, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`: exact three-chain uniform path/flux representation and the cumulative forbidden-band condition at every common-majority gap;
- **account04/B19**, report blob `ce30dae79d698103f026d4d871033238489b1fb1`: in a cardinality-minimal counterexample every proper autonomous subset must be a chain.

The last item leaves a precise chain-module induction branch. The present run attacks the strongest naive implication needed to close that branch.

## Conditional end-to-end argument and first missing implication

Assume POS3 is false and take a cardinality-minimal counterexample `P`. Existing team reductions put the connected width-three core under the uniform law, remove proper autonomous nonchains, and in the module-prime branch impose both the account01/B10 cumulative bands and the account03/B10 pinned central atoms. If `P` instead has a proper autonomous chain `M`, the tempting induction is to contract `M` to one point, invoke minimality on the smaller quotient `Q`, and lift a balanced incomparable pair of `Q` back to `P`.

For that induction to be valid by pair preservation, one would need at least the following implication:

> If `x,y` are outside an autonomous chain `M` and are balanced in the uniform linear-extension law of the contracted quotient, then the same pair remains balanced after expanding `M`.

That implication is false, even for connected incomparability graphs and width exactly three.

## Exact infinite asymmetric-chain adversary

For integers `m>=1` and `r>=1`, let

`P(m,r) = C_2 ⊔ C_{m+2} ⊔ C_r`,

the disjoint/parallel union of three chains. Write the first chain as `A1<A2`, the second as

`B1<B2<B3<...<B_{m+2}`,

and the third as `C1<...<Cr`. Let

`M={B3,...,B_{m+2}}`.

Then `M` is an autonomous chain: `B1,B2` are below every member of `M`, while every `A`- and `C`-vertex is incomparable with every member of `M`. Contracting all of `M` to one point gives

`Q(r)=C_2 ⊔ C_3 ⊔ C_r`.

Both posets have width exactly three, because one can choose one point from each chain and no antichain can use two points from one chain. Their incomparability graphs are complete tripartite graphs and hence connected.

### Uniform-law calculation

A linear extension of `P(m,r)` is exactly a word containing `2` letters `A`, `m+2` letters `B`, and `r` letters `C`, preserving the internal order in each chain. All such words occur once and therefore uniformly. For any fixed `A/B` word, the number of ways to insert the `r` `C`-letters is the same, namely `binom(m+r+4,r)`. Hence after deleting all `C`-letters the induced `A/B` word is **uniform** among the `binom(m+4,2)` shuffles of `C_2` and `C_{m+2}`; there is no biased-law substitution here.

The event `A1<B1` is exactly the event that the first letter of this uniform binary word is `A`. Therefore

`Pr_{P(m,r)}(A1<B1)=2/(m+4)`.

In the contracted quotient, `m=1`, so

`Pr_{Q(r)}(A1<B1)=2/5`,

which lies strictly inside `[1/3,2/3]`. But for every `m>=3`,

`Pr_{P(m,r)}(A1<B1)=2/(m+4)<1/3`.

Thus the same outside pair can move from balanced in the contracted quotient to strongly unbalanced after an autonomous chain is expanded. This is an infinite exact family, not a finite-search artifact.

The obstruction is precisely corridor reweighting: contracting `M` discards the number of admissible positions contributed by its internal chain elements. Minimality can still be useful, but only through a weighted lifting/migration argument that allows the selected balanced pair to change.

## Small exact width-three certificate and all pair probabilities

Take `m=3,r=1`, so `P(3,1)=C_2 ⊔ C_5 ⊔ C_1`. It has

`E = 8!/(2!5!1!) = 168`

uniform linear extensions and 17 incomparable pairs. The exact executable enumerated all 168 extensions and checked every incomparable-pair probability:

`Pr(A1<B1)=2/7`, `Pr(A1<B2)=11/21`, `Pr(A1<B3)=5/7`, `Pr(A1<B4)=6/7`, `Pr(A1<B5)=20/21`;

`Pr(A2<B1)=1/21`, `Pr(A2<B2)=1/7`, `Pr(A2<B3)=2/7`, `Pr(A2<B4)=10/21`, `Pr(A2<B5)=5/7`;

`Pr(A1<C1)=2/3`, `Pr(A2<C1)=1/3`;

`Pr(B1<C1)=5/6`, `Pr(B2<C1)=2/3`, `Pr(B3<C1)=1/2`, `Pr(B4<C1)=1/3`, `Pr(B5<C1)=1/6`.

Exactly seven of the 17 incomparable pairs are balanced. So this is **not** a counterexample to POS3; it is a counterexample only to the fixed-pair chain-contraction lifting step.

The calculation also shows the likely repair mechanism in this special family: the balanced pair migrates along the expanded chain. Although `A1<B1` falls to `2/7`, the adjacent candidate `A1<B2` is `11/21`. More generally, for the binary `A/B` restriction with `n=m+2` B-vertices,

`Pr(A1<B_j)=1 - binom(n+2-j,2)/binom(n+2,2)`.

This monotone sequence is the exact toy model a general corridor-weight lemma would have to replace: contraction cannot preserve a fixed pair, but a proof may still succeed by controlling how the crossing of the `[1/3,2/3]` band moves through the module.

## Ordinal-sum amplification

For arbitrary chains `C_s,C_t`, the ordinal sum

`C_s ⊕ P(3,1) ⊕ C_t`

still has width three. Every linear extension is the forced prefix `C_s`, followed by one linear extension of `P(3,1)`, followed by the forced suffix `C_t`; there are no new incomparable cross-component pairs. Hence all 17 probabilities above are unchanged. Therefore no large-size threshold or added ordinal padding repairs the fixed-pair contraction lemma.

No nontrivial Cartesian-product construction is invoked here: Cartesian products can increase width and are not automatically admissible under the width-three source model. The parallel three-chain and ordinal-sum operations used above preserve the exact scope.

## Accepted implication / residual

**Accepted before:** a minimal counterexample has no proper autonomous nonchain; the chain-module branch remained open.

**Accepted after:** the universal fixed-pair chain-contraction lift is refuted by an exact infinite width-three family. Any induction through a proper autonomous chain must retain the nonuniform corridor weights and prove a **pair-migration** statement: from a balanced pair in the quotient, expansion must force some possibly different incomparable pair in the expanded poset into `[1/3,2/3]`. The disjoint-chain formula proves that migration in this toy branch but does not prove it for an arbitrary width-three module environment.

This leaves the parent theorem open and sharpens the first essential missing implication to a weighted corridor migration lemma, compatible with the partner's pinned-rank atom and account01/B10 cumulative-band constraints.

## Exact executable evidence

Authoritative verifier `adversary_chain_contraction.py`: Git blob `5ba35878b1c412fb75da40cfeb66bec464e72368`, execution SHA-256 `cd058d6426bca31e656a044286235e9c860f599bc2a2d724cddb1d2bb29f6cfa`.

Authoritative output `adversary_chain_contraction.out`: Git blob `8bddad37def4dc7f2e9d372af74bbf4bcccc4bea`, execution SHA-256 `d80f0e0f5d3a98ec4748c80bd1753bc5b40c56d2dff5dd3bf5ebbd1ecbef6ba1`.

The output ends `POS3_ASYMMETRIC_CHAIN_CONTRACTION_PASS`. The proof of the family formula is on this page; the finite execution is exact regression evidence and verifies all incomparable-pair probabilities for the displayed width-three instance.

**Final classification:** `CANDIDATE_REFUTED` for the fixed-pair chain-contraction selector; POS3 remains open.
