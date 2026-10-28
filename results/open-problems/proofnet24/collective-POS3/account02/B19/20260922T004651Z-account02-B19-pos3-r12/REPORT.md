# POS3 account02/B19 — exact module-prime adversary to the local-selector package

**Run:** `20260922T004651Z-account02-B19-pos3-r12`  
**Outcome:** `CANDIDATE_REFUTED`  
**Parent status:** **OPEN / NOT PROVED**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## Control and source state


Fresh control at invocation start was `yspennstate/math-research-brain` main `d3a1a4b135baea144f335c2ff8e76e83eb3f9c59`. The exact control blobs read were README `3d4a9372c87802ab734141a3374d04c8823372e3`, fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`, roles `ed17ecc94f76720c0345b3e32249b791b20ec611`, PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`, ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`, and TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`.

Science dependencies were read from `yspennstate/math-open-problems` at observed master `12373649c7da8599f4c563b9152b7a7d89bfa395`.

The named campaign lead `account04/B10` had no archived `collective-POS3/account04/B10` artifact at that science revision, so no lead result is fabricated. I instead consumed the latest exact relevant team dependencies that were present:

1. **Named partner account03/B10**, run `account03-B10-20260922T001407Z-pos3-r11`, report blob `388ac28e375df4e7a49f72ffbf540f362e03696e`. It proves the pinned majority-rank atom: in a no-balanced width-three poset, every element has at least `E/19683` extensions at its common strong-majority rank, hence every central 3-chain flux cell at the two majority gaps has mass at least `E/19683`.
2. **account01/B10**, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`. It gives the exact uniform 3-chain path encoding and the stronger cumulative band condition in any counterexample: for every relevant `(x,C_b)` with majority gap `g`,
   `sum_{t<g} W_{x,b}(t) < E/3` and `sum_{t<=g} W_{x,b}(t) > 2E/3`.
3. **account04/B19**, run `B19-20260922T001218Z-r44`, report blob `ce30dae79d698103f026d4d871033238489b1fb1`. Its autonomous-substitution theorem implies a cardinality-minimal POS3 counterexample has no proper autonomous nonchain subset.
4. **account04/B20**, run `20260922T001111Z-b20-auto11`, report blob `514b9fca62e570479d8cc8d0e5c3469468286d2`. Its adjacent-swap theorem gives an exact local `|Delta W|<=1` insertion-weight control; this is auxiliary here and was not assumed to close the target.
5. My previous B19 exact adversary/addendum had `E=4477` and satisfied the partner's heavy-gap and pinned-cell checks, but it still contained the proper autonomous chain module `(0,5)`. The present run attacks that structural weakness directly.

## Conditional end-to-end target

Assume POS3 is false and choose a cardinality-minimal counterexample `P`. Existing exact reductions give a transitive strong-majority linear extension `L_*`, width exactly three, connected incomparability graph, and a 3-chain path representation under the **uniform** law on all linear extensions. Account04/B19 removes every proper autonomous nonchain. Account01/B10 then forces the full cumulative forbidden-band jump at every relevant majority gap, and account03/B10 forces the central joint atom at the two common gaps to be at least `E/19683`.

Therefore an end-to-end proof may focus on this exact remaining implication:

> No finite connected width-three module-reduced 3-chain path system coming from a poset can simultaneously realize all account01/B10 cumulative band inequalities at one common strong-majority order and all account03/B10 pinned central-cell lower bounds.

The current selector package was weaker: it treated module-primality plus a unique local `>E/3` majority-gap peak plus the pinned central cell as if those local facts were already close to contradiction. The calculation below refutes that replacement. The cumulative inequalities cannot be discarded.

## New exact module-prime witness

Take three chains

`A: 0<1<2<3<4`, `B: 5<6<7<8<9`, `C: 10<11<12<13<14`

and add cross-relations so that the transitive reduction has exactly the following 22 covers:

`0<1, 0<5, 1<2, 2<3, 2<12, 3<4, 3<9, 5<6, 5<11, 6<2, 6<7, 7<4, 7<8, 8<9, 9<14, 10<1, 10<11, 11<12, 12<8, 12<13, 13<4, 13<14`.

Equivalently this is obtained from the preceding B19 15-element witness by deleting the two cross generators `(1,7)` and `(5,1)` and recomputing transitive closure.

The exact verifier **enumerates every linear extension**, rather than sampling or projecting a biased law. Every valid extension has weight one. It obtains:

- `E = 6294` linear extensions.
- Width exactly `3`: `(1,6,11)` is a 3-antichain and there is no 4-antichain.
- The incomparability graph is connected.
- There are `24` incomparable pairs.
- There is **no nontrivial proper autonomous subset at all** (exhaustive test over every proper subset of size at least two), stronger than the account04/B19 minimal-counterexample requirement.
- The reference order
  `L_*=(0,10,5,6,1,11,2,7,12,3,13,8,9,4,14)`
  is a linear extension. Every unbalanced incomparable pair's `>2/3` orientation agrees with this order.
- All `28` relevant element/other-chain insertion marginals have a **unique** maximum at the `L_*` gap and that peak is `>E/3`. The smallest peak is `2366/6294 = 1183/3147 > 1/3`.
- Every one of the 15 `L_*` joint central cells satisfies the partner bound `>=E/19683`; the smallest is `1089/6294 = 363/2098`, far above the lower bound.
- Nevertheless `16/28` relevant rows fail the full account01/B10 cumulative band condition. Only `12/28` pass it.

Thus adding full autonomous-primality does **not** rescue the local heavy-peak+pinned-cell selector.

## All balanced pairs and exact probabilities

The verifier checks all 24 incomparable pairs. Exactly eight are balanced:

- `Pr(1<6)=3023/6294`.
- `Pr(2<7)=676/1049`.
- `Pr(2<11)=362/1049`.
- `Pr(3<12)=361/1049`.
- `Pr(4<9)=1096/3147`.
- `Pr(5<10)=1132/3147`.
- `Pr(7<12)=694/1049`.
- `Pr(8<13)=1541/3147`.

The authoritative output `verify_output_exact.txt` records the exact probability for **every** incomparable pair, including all 16 unbalanced pairs. This is a POS3-positive poset, not a counterexample to the conjecture.

## First essential implication after this refutation

The source-valid conclusion is negative but decisive:

> `connected + width 3 + many majority blocks + module-prime + unique local majority-gap mass > E/3 + pinned central atom >= E/19683` does **not** imply a contradiction and is not a sound selector for a hypothetical counterexample.

The first essential surviving global datum is the **cumulative band placement**, not merely the size or uniqueness of the local peak. Any next selector/adversary search must enforce, for every relevant row at its common majority gap `g`,
`3*sum_{t<g}W(t)<E` and `3*sum_{t<=g}W(t)>2E`.
This witness shows exactly where the weaker local conditions leak: 16 relevant rows violate one of those strict inequalities while keeping all local peaks and central atoms large.

A useful next mathematical attack is therefore to search directly inside the much narrower set satisfying **all** cumulative bands and pinned cells simultaneously, or to sum signed flux-conservation identities over consecutive majority-order boundaries to contradict those bands. Module decomposition alone has been exhausted by this witness.

## Reproducibility and artifact integrity

Authoritative verifier: `verify_module_prime_adversary.py`, Git blob `1e823123c7847b66a5173a964ec6a9b454cc42a6`; local SHA-256 at execution was `3e6bcf25581b161b51af744b3f961d4089dfa21dccb6df8c73a81cd88a7a51f9`.

Authoritative exact output: `verify_output_exact.txt`, Git blob `92fb81785ef72f1d2e3da363a0c27b659f20759d`; the native execution output SHA-256 was `befd503e803dbf3e24c676776f5ef3690d698bcd12d46a6705cecdbbae6331dd`.

A pre-receipt file named `verify_output.txt` is **non-authoritative**: while manually relaying native output it acquired one duplicated terminal field on the failed-band row for `x=9`. It is preserved as history and is not used for any mathematical claim. The executable plus `verify_output_exact.txt` are the source of record.

No broad memory, benchmark gold, credentials, scheduler identifiers, unrelated private data, email, Drive, paid API/model/Codex call, public posting, remote workflow, or permission change was used.

**Final research classification:** `CANDIDATE_REFUTED`. The parent POS3 theorem remains open.
