VERDICT: PARTIAL retrieved and audited the formal model of the claimed outside solution

Round 4's retrieval claim holds: the paper and statement map remain
accessible. The new step obtains the formal model and target files that
round 4 could not access, pins them to a commit, and checks applicability
to T127. PROOF.md derives the uniform walk law, activation rule and visit
event from the definitions, and handles an additional sleeping root frog.

The claimed outside answer remains recurrence for d=3 and transience for
d=4. Exact attribution and references are in SOLVED_ELSEWHERE.md. This
session does not independently certify the complete solution. Under step 1,
the literature branch ends further original-model research; no new packet
refinement or Bernoulli computation was undertaken.

The GitHub connector succeeded where raw web retrieval failed. Fourteen
source files are saved under outside/, including the formal definitions,
both target and challenge files, paper, citation metadata, input manifest,
license and historical verification records. outside_manifest.json records
their URLs, Git blob identities and fixed commit
d6b298c0100af57a8f46f8314eca8bf8f7eb4693.

Reproduce the local source checks:
```
OMP_NUM_THREADS=1 nice -n 15 python3 audit_sources.py > audit_sources_output.txt 2>&1
```
Exit 0; all 14 blob hashes match. Thirteen shared definitions match the
d=4 challenge, twelve match the d=3 challenge, and the recurrence predicate
matches separately. The four inspected development files have no executable
sorry, axiom or native_decide tokens. These are finite source checks, not
verification of the imported proof graph. Peak RSS was 18497536 bytes and
runtime below one second. The sandbox denied the requested nice adjustment;
the denial is retained in the output. No heavy computation was run.

What failed: raw web retrieval of the formal files and the Zenodo record.
The first source-audit run expected a Transient definition in the recurrence
challenge, which intentionally omits it; the audit was corrected. Saving
the archive initially added a terminal LF to each source; the script removed
it only after checking that removal recovered the exact advertised blob.

Uncertainty: no Lean build, comparator run, certificate replay or audit of all
imported modules was performed. The saved historical records are not a fresh
verification of the pinned tree. The complete outside argument therefore
remains unverified here. The earlier Bernoulli results were read but not
rerun under the step-1 stopping branch; nothing here contradicts them.

Next worker: use the now-local formal sources, not another retrieval-only
session. Inspect the imported assembly/checker arguments and obtain the
three inputs named in outside/ASSETS.md. A complete formal replay needs a
separately authorized environment: the recorded comparator used more than
1 GB and more than 20 minutes. Smaller checker or source audits may fit the
current limits. Keep source-reported PASS distinct from a reproduced PASS.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 08:25 Asia/Tbilisi.
