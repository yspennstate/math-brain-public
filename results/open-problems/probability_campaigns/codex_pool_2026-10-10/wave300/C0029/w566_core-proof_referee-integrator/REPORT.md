# C0029 referee and brain draft report

**Finding.** The exact coefficient-one Spielman–Teng target was recovered from the 2002 primary conjecture and compared with the 2025 (1+o(1)) result. Current openness is UNKNOWN after bounded primary-literature and local checks. No proof of the parent problem is claimed. The hardest missing input in w564's route is the signed averaged mixed-row estimate H, which is algebraically equivalent to the parent inequality.

**Peer verdicts.** KEEP w564 L1 (exact row-extension threshold), L2 (exact row telescope), L3 (Hadamard obstruction) and w565 C01 (two-coordinate sign atom) within their stated scope. KEEP w565's independent n=4 dependence calculation and generic quantifier counterexample as obstructions only. H is explicitly UNPROVED. The review proof and reproduction are in `REVIEW_PACKET.md`; w564's reviewed `ATTEMPT.md` SHA-256 is `7861BF36F60FB966A8B9CEEB736801BA0BBAA2D9AFF9BDB96811B01597D2293B`. w565's claims SHA-256 as read is `D12566EC1FC58368212449EA319B0943F44FA071E3CD8426D70F08ABED354C83`.

**Archive FIX.** The 2026-09-07 C0029-A001 record incorrectly calls 1−exp(−t²/2−t) an exact finite-n real Gaussian least-singular-value CDF. At n=1,t=1, `python -X utf8 -c "import math; print(math.erf(1/math.sqrt(2)),1-math.exp(-1.5))"` gives 0.6826894921370857 versus 0.7768698398515702: absolute error 0.09418034771448447. Replacing the false formula by the exact n=1 CDF makes that control error zero. For arbitrary finite n use F_n and the published bound F_n(t)≤t. This is a proposed correction to the archive record; the live file was not edited.

**Brain draft.** Submitted `bundle_001.json` with 5 entries and 4 locally supported relations to `~/math-brain-inbox/w566/bundle_001.json`. SHA-256 of both local and submitted copies: `59EC98A55888917A7853EBF2D03556F706155E3769048F15657086C8B9A0EC18`. Validation command: `python -X utf8 -c "import json,pathlib; b=json.loads(pathlib.Path('bundle_001.json').read_text(encoding='utf-8')); assert len(b['entries'])==5 and len(b['relations'])==4"` passed. Source tags use the accepted `owner-own-work` prefix. The bundle excludes my L4 until w569 checks it.

| State | C0029 bundle |
| --- | --- |
| Submitted | Yes, inbox path and hash above |
| Reviewed | Mathematical peer claims locally checked by w566; required final model identity unverified |
| Ingested | No evidence; integrator not run here |
| Retrievable | No evidence; recall not claimed |

**Risk and next step.** Exact orthogonality is exponentially rare under iid sign rows by my L4, but near-orthogonal and other arithmetic skeletons are uncontrolled. L4 is a proved special case awaiting w569's independent audit. The w565 exact-check script was not run because its fresh compute gate said BLOCKED; my 7/8 versus 13/16 reproduction is analytic. The recorded model request does not establish the served final-review model.

**How to apply.** After the independent review gates, the coordinator ingests `~/math-brain-inbox/w566/bundle_001.json` with the draft integrator and corrects C0029-A001's finite-n Gaussian formula using `SOURCE_STATUS.json` and `REVIEW_PACKET.md` as evidence; then verify ingestion and recall separately.

NEXT: w569 audits L4; coordinator applies the archive FIX and integrates the reviewed draft; continue H only with a genuine signed averaged estimate.
