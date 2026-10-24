# POS3 handoff — account03/B19 module-prime heavy-slice refutation

Run: `20260922T010520Z-b19-pos3-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `CANDIDATE_REFUTED` for a strengthened induction route; POS3 remains `OPEN_NOT_PROVED`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Exact scientific artifact

Repository: `yspennstate/math-open-problems`  
Report commit: `cee406d73f20ab6d3f97173447d1f7297e25ac01`  
Report path: `proofnet24/collective-POS3/account03/B19/20260922T010520Z-b19-pos3-r11/REPORT.md`  
Report blob: `b32278d17e70387d51be17fd0d0ac912bae48f5e`  
Verifier blob: `4d993ba73c37fa374e6342baba4b8df4bfca1beb`  
Verifier executed SHA-256: `b31ace9f3b54cbb4cff33e9adcb8ce768b176a70583f8e09e3b263ebb1f7c322`  
Output blob: `cd0b55df91a969677e5072b9ea59b4f6d14e7de4`  
Output SHA-256: `79f53971708a031c3abb7f15f8701c4978b7833d129e78d2d15d213ad8f15875`  
Terminal marker: `POS3_B19_MODULE_PRIME_HEAVY_CERTIFICATE_PASS`.

## Claim consumed / attacked

Consumed `account04/B19` blob `ce30dae79d698103f026d4d871033238489b1fb1` (minimal counterexample has no proper autonomous nonchain), `account01/B10` blob `3a0d4e63665646adc853bb48192eba0f81629a15` (exact three-chain flux/heavy-slice normal form), and `account03/B11` blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d` (double-blocker boundary certificate).

The designated partner/team lead `account04/B10` had no archived collective-POS3 root at the final pre-write check, so no partner result was fabricated.

## Exact new finite certificate

A self-dual 9-element width-3 poset with generating relations

`0<2,0<3,0<4,1<4,1<5,2<5,3<6,3<7,4<7,4<8,5<8,6<8`

has exactly `349` linear extensions, connected incomparability graph, and **no proper nontrivial autonomous subset**. Its only balanced pairs are the interior pairs `(2,3)` and `(5,6)`, each with numerator `156/349`. Every incomparable pair touching a minimum or maximum has balance at most `105/349 < 1/3`.

For the exact three-chain cover `A=(0,3,6), B=(1,4,7), C=(2,5,8)`, every relevant cross-chain insertion distribution has a slice `>E/3`; the smallest possible maximum is `142/349 > 1/3`.

Therefore **connectedness + module-primality + absence of an extremal balanced pair does not force a light insertion-slice vector**. The account04/B19 autonomous-module theorem remains valid; it simply does not repair that shortcut.

## Next recipient / exact residual

Primary next recipient: `account04/B10` when its lead artifact appears; also relevant to `account03/B11` and other POS3 integrators.

The surviving essential implication is counterexample-specific: in a connected module-prime width-three core, rule out simultaneous `>E/3` heavy slices aligned at one transitive strong-majority order **together with** the adjacent-boundary double-blocker certificates. The new witness shows that connectedness, no modules, endpoint structure, and heavy-slice magnitudes separately are insufficient. A signed conservation identity coupling heavy-slice *location* to blocker witnesses across consecutive majority boundaries is the next high-value target.

No parent-problem closure, novelty claim, public release, benchmark gold, credentials, scheduler identifiers, machine paths, email/Drive action, paid service, or production-brain mutation is asserted.
