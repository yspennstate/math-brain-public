# P0162 referee report, 2026-10-10

I verified the universal Boolean, uniform-cube FEI statement from the author-hosted primary paper. The dated intake status is historical; current global openness remains UNKNOWN. I found no full proof in the two 2026 primary papers checked. Owner memory records FEI as open in September and assigns the plateaued constant-four result to Potapov.

I independently checked w505's explicit counterexample to an **all-coordinate** entropy-defect bound and w504's exact restriction identity, conditional induction, good-base-coordinate family, direct family FEI bound, and small-influence localization. Verdicts and exact scope are in `CLAIMS.jsonl` and `REVIEW_PACKET.md`. The unproved load-bearing step is a uniform **exists-coordinate** bound when every influence is below 1/16; no parent solution is claimed.

Reproduction: `python -X utf8 test_selector.py` passed three complete Walsh truth tables; `python -X utf8 test_w504.py` passed four. The selector defect/influence ratio was 4.867668747, 8.030013847, 10.255970235 at m=1,2,3, while the whole-family H/I ratio stayed 1.266809821, 1.800892435, 1.952643846. The base-coordinate ratio in w504's family was 1.622556249, 3.093729729, 3.722358844, 3.921212616 at even m=2,4,6,8, always below 4.

Brain output: I prepared a two-entry, one-relation draft under `~/math-brain-inbox/w506/`. It duplicated w504's later reviewed bundle and used the same inaccurate signed-coefficient phrase in its proof text, so I preserved it as ignored `bundle_001.withdrawn.part`. The exact correction is `-2t(-1)^beta` for the auxiliary control blocks; their squared masses and the kept entropy inequality are unchanged. w504 published corrected `~/math-brain-inbox/w504/bundle_003.json`; I checked the corrected phrase. My draft is **not currently submitted**. w509 independently kept the mathematical C003 result and returned a packaging FIX on my duplicate draft; integration and retrievability are unobserved. No live store or code file was changed, so no live-file diff applies.

Risk: the checked special family and finite runs cannot certify the universal FEI conjecture. w505's FEI target and bad-selector concept may duplicate existing cards. w504's earlier draft versions have the signed-coefficient error; use the corrected `bundle_003.json` only. No served-model evidence is available from this worker packet, so model-specific promotion gates remain for the validating coordinator.

The recalled proof-completion scar prompted one narrow hook proposal in `HOOK_PROPOSAL.jsonl`. It is saved locally for review and has not been submitted to the hooks directory because this worker's folder-only write rule grants no hook-output exception.

NEXT: Referee a general suitable-coordinate lemma or counterexample in the small-influence regime; check Boolean convolution constraints, not just arbitrary spectral laws.
