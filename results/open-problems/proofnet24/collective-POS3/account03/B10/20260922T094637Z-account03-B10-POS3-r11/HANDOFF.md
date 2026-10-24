# POS3 source-bound handoff — canonical earliest barrier and same-sign packet

Run: `20260922T094637Z-account03-B10-POS3-r11`  
Status: `ESSENTIAL_STEP_APPLIED / POS3 OPEN`  
Canonical report blob: `ae1f5d878c5c84581ec59f193b34cfc1956a57c4`  
Sign-completeness addendum blob: `654c097aab4c7bd37cc64ecee138a41ac1218a58`.

Consumed assigned partner: account04/B11 `20260922T090813Z-B11-pos3-r18`, report blob `eb9eca5a9e57f81f33c052792f06678c19e93823`. Its lower stationary-profile exit from a heavy cover gives sibling lower covers `p,s lessdot r`, `p||s`, with either `s<q` or `s||q`; the `s<q` branch leaves the same-sign/multi-distinguisher charge problem.

Consumed lead: account04/B10 `20260922T091028Z-account04-B10-pos3-r11`, report blob `8a856fa924002567c01a8b70880003fe53b86da3`. It selects the canonical earliest-ending incomparable pair `(p,q)` in the transitive strong-majority total order.

New global lemma: every two vertices strictly before canonical `q` are comparable in the poset. Otherwise their incomparable pair has a later endpoint earlier than `q`.

Direct partner application: at a heavy bridge anchored at canonical `q`, the partner alternative `s<q` is impossible because `p,s` would be incomparable and both strictly before `q`. Therefore the lower half-profile exit is forced to `s||q`, and in fact `p prec_* q prec_* s`; the local exit is a coherent width-saturating three-antichain. Thus the partner's same-sign sibling branch is absent at the canonical earliest barrier.

New exact actual-law identity for later/noncanonical same-sign states. For `a||b`, let all relation distinguishers have the positive sign for `a<b`, split as `L={l:l<b,l||a}` and `U={u:a<u,u||b}`, and let

`S={all l in L precede a, and b precedes all u in U}`.

Swapping the positions of `a,b` is an involution between the `b<a` extensions and the `a<b` extensions in `S`, while every `b<a` extension is automatically in `S`. Hence

`Pr(S)=2 Pr(b<a)`.

If there are exactly two same-sign distinguishers and no accepted strict subspan, each of the two safe-corridor conditions has actual probability `>2/3`, so `Pr(S)>1/3` and therefore

`minority(a,b)>1/6`.

The negative-same-sign case relative to the actual strong majority is impossible by applying the same identity after reversing the pair: it would give an event probability `2Pr(a<b)>4/3`.

Using account04/B11's actual-uniform-law tail

`Pr(x_j<x_i)<2125440/(j-i+1)^2`,

the new `>1/6` packet has strong-order index span at most `3570`.

For all-positive >=3-distinguisher states, only the maximal lower and minimal upper frontier conditions matter. Width three bounds each frontier by two. If the total frontier is <=2, the same `>1/6` packet follows. Thus a genuinely unpaid all-positive multifrontier state has at least three frontier conditions and hence already contains a width-saturating three-antichain gate on one side.

Next exact target: `POS3-CANONICAL-ANTICHAIN-OR-MULTIFRONTIER-SPLICE-v1` — splice the canonical coherent three-antichain and later >=3-distinguisher multifrontier states into a well-founded global descent/envelope mechanism, or force balance/proper reduction, without converting any induced law to a uniform surrogate.

Regression: `verify_same_sign_corridor.py` checked the integer corridor identity in 21,396 all-positive incomparable-pair cases across all distinct naturally labelled transitive closures through six vertices; output blob `b21204a0f8d0c46cad46cde842f82ce9e435ef72`, PASS. This is regression only; the proof is the arbitrary-size involution.
