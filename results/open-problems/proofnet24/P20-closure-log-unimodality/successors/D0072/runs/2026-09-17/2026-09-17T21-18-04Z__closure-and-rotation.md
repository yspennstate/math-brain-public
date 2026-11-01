Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so I do not claim otherwise. **D0072 CLOSURE MOVEMENT: `E_NNQ=1 -> 1`; independent full-proof audits `1/2 -> 2/2`; source status advances to `PROVED_SOURCE_LITERAL_YES`; narrow closure package created/read back; D0072 is RETIRED from active P20 research. Successor rotation executed and ends on `SUCCESSOR_ADMISSION_REQUIRED / HOLD` because the fresh Khetan six-cell candidate was claimed by R7-02 before P20 could lawfully claim it and the current queue has no other certified READY successor.**

# P20 / D0072 closure, packaging and successor rotation

UTC run date: 2026-09-17.

Source: Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884v2 / Springer Proceedings in Mathematics & Statistics 300 (2020), Section 4.2, Question 4.5.

Canonical P20 claim: `operations/claims/D0072.md` @ creation commit `19ad6d4c267d6504dc7abbf2c2d140b37ed7f8d2`.

Canonical P20 theorem candidate: `P20-D0072-NONNORMAL-QUOTIENT-WITNESS-01`, report `proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T16-18-23Z__run-report.md` @ `92b25a56025b3e0905274c554a4104d4acbc0685`.

Frozen source metric: `E_NNQ=1`, target `1`.

Final P20 disposition after this run: **SOURCE-MATCHING YES / EXACT FINITE CORE PASS / 2/2 DISTINCT OTHER-TRACK FULL-PROOF AUDITS PASS / NARROW INTERNAL CLOSURE PACKAGE COMPLETE / PUBLICATION NOVELTY UNVERIFIED / NO PUBLIC POSTING CLAIM / D0072 RESEARCH RETIRED / SUCCESSOR ADMISSION HOLD.**

## 1. Required continuity and current-state recovery

I continued from the 18:08Z P20 audit-recovery state rather than restarting the witness mathematics. At run start I reread or recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, the D0072 canonical claim, the canonical P20 proof report, the 18:08Z P20 recovery report, the P20 exact finite checker/output, the distinct P19 audit, the newest P26 commits/reports, the newest complete P21 state, and the freshest coordinator/task-health evidence.

No authorized release/reassignment of D0072 occurred before closure. No P20 self-check, main-agent strengthening or repeated auditor receipt is counted as an independent audit.

## 2. Second mandatory independent audit recovered: P26 PASS

A new P26 audit was committed after the preceding P20 run:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_23-58-56__run-report.md`

creation commit:

`20863efed6afdd5f78a8832ca82e7a00f57f01de`

report blob:

`ab2e7293a5dbf58e0238c708d164a334cb542278`.

The verdict is exactly:

`P26-AUDIT-P20-D0072-ENDTOEND-30 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_QUESTION_PASS / CLAIM_SCOPED_K3 / FINITE_CORE_INDEPENDENT_PASS / PRIOR_ART_UNVERIFIED`.

P26 also records:

`P26-RECONCILE-P20-D0072-2OF2-30 = PASS`.

Its distinct second auditor is the already-recovered P19 verdict

`P19-AUDIT-P20-D0072-ENDTOEND-23 = PASS`

from `proofnet24/P19-closure-smr-optimal/runs/2026-09-17/2026-09-17T17-56-34Z__rotation-hold-d0072-audit.md` @ creation commit `8debd604cb2090d04a64564ba6d29a8d70198bde`.

Therefore the required source-level audit gate is now exactly `2/2`, one P26 plus one P19. P26 independently reconstructed the exact source quantifiers, relative generator-preserving GRR dependency, infinite/simple/locally-finite/transitive ambient graph hypotheses, left-coset/right-generator quotient convention, effect of extra GRR generators, nonnormality and freeness of `A`, collapse of the universal transitive `Gamma'` quantifier under the regular full automorphism group, and the normal-index-three/C3 obstruction from `(S_3*A_5)^ab=C_2`. It found no mathematical defect.

P26 also created a third independent finite core, with checker creation commit `a4766dd4197b0c2195e815b24a8a3c7a7444c46c` and PASS output creation commit `d4ff81b6808f86ef3deb5c66830a66df31a4cbea`. The output blob is `70e2650ba193969ac4f43d88aece4f92ae9f48b6`. This is corroborating evidence; the two-auditor count remains P26 + P19, not three.

P26's pinned sidecar is `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_23-58-56__ledger-delta-and-readback.md` @ `a6ed44da81dfadfc8e345a2be2f35b5a5c188870`. It classifies the P20/D0072 claim as `PROVED_SOURCE_LITERAL_YES / CLAIM_SCOPED_K3 / PUBLICATION_NOVELTY_UNVERIFIED` and explicitly records P20-owned closure packaging as the remaining owner action.

## 3. Exact source-level theorem now closure-certified

The audited witness remains exactly the canonical P20 witness; I did not silently replace it with P26's optional simplification or the main-agent all-`K_m` strengthening.

Let

`Lambda=S_3*A_5`,

let `pi:Lambda->S_3` be identity on the `S_3` factor and trivial on `A_5`, let

`H=< (12) >`,

and put

`A=pi^{-1}(H)`.

Start with the finite symmetric generating set

`S_*=(S_3\{1}) union (A_5\{1})`.

Leemann–de la Salle 2022, Theorem 1.1 together with Theorem 3.1, Proposition 3.2 and the proof of Theorem 1.1, yields a finite symmetric final generating set `S` containing `S_*` for which

`G=Cay(Lambda,S)`

has

`Aut(G)=Lambda_L`.

With `Gamma=Lambda_L`, the subgroup `A` is non-normal and acts freely. Its orbit quotient is exactly `K_3`: the orbits are the three left cosets indexed by `H\S_3`, and every pair of distinct quotient vertices is joined because every nonidentity element of the `S_3` factor remains a generator. Since the full automorphism group is regular, every transitively acting subgroup `Gamma'<=Aut(G)` is the whole `Lambda_L`. A normal quotient with three vertices would therefore give a normal index-three subgroup and a `C_3` quotient of `Lambda`, impossible because

`Lambda^ab=(S_3*A_5)^ab ~= C_2`.

Hence Grimmett–Li Question 4.5 has the literal source answer **YES**, and the example even satisfies the subsidiary free-action property.

## 4. P20 exact finite core remains PASS

Original checker:

`proofnet24/P20-closure-log-unimodality/successors/D0072/artifacts/2026-09-17/2026-09-17T16-17-30Z__finite_core.py`

creation commit `144f18a4da6d45581d79bb91d91af14b556cedde`.

Original output:

`proofnet24/P20-closure-log-unimodality/successors/D0072/artifacts/2026-09-17/2026-09-17T16-17-30Z__finite_core.out`

creation commit `14db9090c2e88788c9381cef3246d0d1415d53c8`, ending `ALL_EXACT_CHECKS_PASS`.

It checks exactly the finite claims: `H` is non-normal of index three in `S_3`, the simple left-coset quotient using all nonidentity `S_3` generators is `K_3`, `[S_3,S_3]=A_3`, and `A_5` is perfect. The theorem-sized free-product and GRR statements remain written/cited rather than falsely machine-certified.

## 5. Narrow self-contained closure package created and read back

I created the source-matching package

`proofnet24/P20-closure-log-unimodality/successors/D0072/paper_question4_5_nonnormal_quotient/`.

It contains exactly the audited `K_3` source claim, not the stronger all-`K_m` construction elsewhere in the repository:

1. `README.md` — source scope, witness, canonical proof/checker provenance, two audit IDs, prior-art limitation and scope discipline. Creation commit `bb827ea8f679cf1173e882dedc0b71413a648450`. Read back from that exact commit.
2. `main.tex` — self-contained theorem and full proof, including the relative Leemann–de la Salle dependency and the universal `Gamma'` quantifier. Creation commit `2471e1b007ae39f5468686956f716d7c1f658600`. Read back from that exact commit.
3. `check.py` — exact copy of the canonical P20 finite core. Creation commit `8ed8ea5d0a989d4352c599d1508584ae6d9fe409`. Read back from that exact commit.
4. `check.out` — exact canonical PASS output, ending `ALL_EXACT_CHECKS_PASS`. Creation commit `9cbe61c07f7ef826d34fcae677f399127ab0f373`. Read back from that exact commit.

The package explicitly records **publication novelty UNVERIFIED** and makes no claim of public posting.

## 6. Dated prior-art/current-source limitation

The 2026-09-17 bounded source/literature checks, including the P20 proof run, P19 audit and new P26 audit, rechecked the current Grimmett–Li source, exact Question 4.5 wording and quotient convention, later-author/citing combinations, and the Leemann–de la Salle 2022 GRR theorem. They recovered the original question and the crucial post-source GRR technology but no paper explicitly claiming resolution of the exact Question 4.5 quantifiers. The present run also repeated bounded exact-phrase/current searches. Search misses are only bounded negative evidence. They do not establish worldwide openness before this work or publication novelty.

## 7. Retirement and ledger delta

The source-level mathematical status is now:

- `E_NNQ=1`;
- exact source answer: `YES`;
- P20 finite core: PASS;
- P19 end-to-end audit: PASS;
- P26 end-to-end audit: PASS;
- independent source-level audit count: `2/2`;
- P26 two-audit reconciliation: PASS;
- narrow source-matching package: COMPLETE;
- publication novelty: UNVERIFIED;
- public posting: NOT CLAIMED.

Accordingly **D0072 is RETIRED FROM ACTIVE P20 RESEARCH after successful source closure**. The historical canonical claim file is preserved rather than rewritten.

P20 did not edit root `RESULTS.md`, `QUEUE.md` or `POSTED.md`. Requested P26/coordinator merge input:

```yaml
ledger_delta:
  track: P20
  target: D0072
  source: Grimmett-Li 2020, Question 4.5
  metric: E_NNQ
  value: 1
  target_value: 1
  mathematical_status: PROVED_SOURCE_LITERAL_YES
  canonical_claim: P20-D0072-NONNORMAL-QUOTIENT-WITNESS-01
  p20_finite_core: PASS
  audits: 2/2
  audit_1: P19-AUDIT-P20-D0072-ENDTOEND-23 PASS
  audit_2: P26-AUDIT-P20-D0072-ENDTOEND-30 PASS_FULL_MATHEMATICAL_PROOF
  reconciliation: P26-RECONCILE-P20-D0072-2OF2-30 PASS
  package: proofnet24/P20-closure-log-unimodality/successors/D0072/paper_question4_5_nonnormal_quotient/
  prior_art: BOUNDED_NEGATIVE_SEARCH_ONLY
  publication_novelty: UNVERIFIED
  public_posting: NOT_CLAIMED
  activity: RETIRED_SOURCE_CLOSED
  shared_root_edits_by_P20: NONE
```

## 8. CLOSABLE successor rotation executed in the same run

After D0072 reached 2/2 and was packaged, I immediately executed the successor-admission rule rather than continuing D0072 mathematics.

The freshest coordinator/task-health report recovered is `operations/task_health/runs/2026-09-17T210000Z/status.md` @ creation commit `65cba0e87cfa69a7c555dc51fdb48e592bd6ac3e`. It still records multiple CLOSABLE lanes with admission gaps; root `QUEUE.md` continues to state that its listed PENDING candidates are not automatically dispatchable and that newly certified READY entries are zero.

A same-minute gate elsewhere in the repository produced a fresh source-verified CLOSABLE-shaped candidate, Abhishek Khetan's 2026 cardinality-six exact-cluster tiling question from arXiv:2607.09830. I independently rechecked the current v2 metadata/abstract: the paper proves an eight-cell counterexample, proves a positive prime-square case, combines this with Szegedy's prime-cardinality theorem, and explicitly leaves cardinality six as the possible exception below eight. Bounded current search did not find a later resolution; that is negative evidence only.

However the race-safe ownership recheck now finds the canonical file

`operations/claims/KHETAN-2026-EC6.md`,

with status `ADMITTED_ACTIVE / OPEN`, lane `CLOSABLE OUTSIDE`, and **exclusive owner `R7-02 Finite Certificate Research`**, admission commit `e8017706e9f784cf903bbcfcc95c50878e736b79`. P20 therefore must not claim or duplicate that source.

No other candidate in the fresh queue/task-health state is already certified `READY + CLOSABLE + UNASSIGNED`, and I do not relabel a PENDING/HARD/owned/under-screened candidate merely to fill the slot. Therefore the lawful P20 post-closure state is:

`SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD`.

This is an executed rotation outcome, not a failure to rotate. The next P20 invocation must perform successor admission only, starting from fresh coordinator/queue/claim evidence and continuing beyond already rejected or occupied candidates. D0072 mathematics is retired and must not be resumed absent explicit reassignment.

## 9. Directed P20 -> P21 audit duty

The newest recovered P21-specific commit history still terminates in the I0004 six-run retirement/handoff (`7fb9b8465a1b76a816282fbf501dcf41ffe5fde1`) and no genuinely newer P21 theorem claim was recovered. Therefore no P20->P21 audit receipt is manufactured.

## 10. Durable final state

D0072 is now source-closed internally under the campaign protocol and retired from active P20 research. The next run is successor admission, not another D0072 proof or checker.

**END OF CANONICAL D0072 CLOSURE AND ROTATION REPORT**
