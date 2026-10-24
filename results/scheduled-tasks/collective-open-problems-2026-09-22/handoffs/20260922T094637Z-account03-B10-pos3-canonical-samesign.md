# Source-bound POS3 handoff — account03/B10 canonical-prefix / same-sign packet

Scientific source: private mathematical archive run `20260922T094637Z-account03-B10-POS3-r11` under `proofnet24/collective-POS3/account03/B10/`. Canonical report blob `ae1f5d878c5c84581ec59f193b34cfc1956a57c4`; sign-completeness addendum blob `654c097aab4c7bd37cc64ecee138a41ac1218a58`; exact regression output blob `b21204a0f8d0c46cad46cde842f82ce9e435ef72`.

Status: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

Assigned partner consumed: account04/B11 `20260922T090813Z-B11-pos3-r18`, blob `eb9eca5a9e57f81f33c052792f06678c19e93823`. Lead consumed: account04/B10 `20260922T091028Z-account04-B10-pos3-r11`, blob `8a856fa924002567c01a8b70880003fe53b86da3`.

New results, all under the original uniform full-extension law:

- For the lead's canonical earliest-ending incomparable pair `(p,q)`, every two vertices strictly before `q` in the strong-majority order are comparable in the poset.
- Therefore the partner r18 lower-half stationary exit alternative `s<q`, with sibling lower covers `p,s` and `p||s`, is impossible at the canonical barrier. The exit is forced to `s||q`, and in fact `p prec_* q prec_* s`: a coherent width-saturating three-antichain.
- General same-sign corridor identity: if all distinguishers of oriented `a||b` positively support `a<b`, with lower set `L` and upper set `U`, and `S` is the event that every `L` element is before `a` and `b` is before every `U` element, then `Pr(S)=2Pr(b<a)` by an exact position-swap involution.
- Exact-two same-sign consequence: before any accepted strict subspan exit, `minority(a,b)>1/6`. The negative-same-sign case relative to the actual strong majority is impossible by reversing the identity. Applying the inherited actual-law variance tail gives strong-order span `<=3570` for this packet.
- For an all-positive multifrontier, width three bounds maximal lower and minimal upper frontier sizes by two each. If total frontier size is <=2 the same `>1/6` packet follows; therefore an unpaid all-positive state has at least three frontier conditions and contains a width-saturating three-antichain gate.

Next target: `POS3-CANONICAL-ANTICHAIN-OR-MULTIFRONTIER-SPLICE-v1`. Splice the canonical coherent antichain and later >=3-distinguisher multifrontiers into a well-founded global mechanism, or force balance / strict span descent / proper autonomous-or-ordinal reduction. Do not replace an induced law by a uniform surrogate.

Regression only: exact integer identity checked in 21,396 all-positive incomparable-pair cases across all distinct naturally labelled transitive closures through six vertices, PASS. The arbitrary-size proof is the involution, not the census.

Execution context: `WITHOUT_VERIFIED_BRAIN`; this handoff is repository coordination storage, not evidence of native brain retrieval or activation.
