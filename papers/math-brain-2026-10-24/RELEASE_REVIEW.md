# Release-paper review, 26 October 2026

The public release is accessible to everyone. The paper's statement that the licence has not been chosen was obsolete and has been replaced with explicit MIT terms for original project code and data, CC BY 4.0 for the original paper, and the retained CC BY-SA terms for wiki-derived material. The nested framework package's stale proprietary licence metadata has also been corrected.

## Verified snapshot

The reviewed public repository head was `393821a830f0979d27c38430130900ac57fb1701`. The data checked here are that commit's `export/population/`, not an assertion that the inaccessible live working database has been rebuilt today.

| Check | Result |
|---|---|
| Export tables and SHA-256 file digests | All 16 match the manifest |
| Export rows | 56,733; all per-table counts match |
| Cards/nodes | 13,344 |
| Links | 19,398, including 231 retractions |
| Bundle manifests | 1,052 |
| Card and bundle-manifest digest failures after fresh import | 0 |
| Claim, evidence, edge, mistake and reflex digest failures | 0 |
| SQLite foreign-key violations | 0 |
| SQLite integrity check | `ok` |

Run `python papers/math-brain-2026-10-24/scripts/check_release.py` from the repository root. The checked result is in `release_integrity.json`. The checker fails on a mismatch. The original importer only prints card and bundle-manifest failures, so its exit status alone was never sufficient evidence.

## Reconciliation of the manuscript

The public source previously described the 24 October partial three-arm run. It now incorporates the reported 25 October results: 988 Claude items, 335 Codex items, and 806 items completed in time by both Claude comparison arms. The compaction appendix from the 25 October emailed edition is retained, with its private-data verification limit stated. The 24 October cost ledger keeps its original cutoff and is distinguished from the later accuracy results. Historical 22 October store census tables remain dated historical observations.

The revised text removes unsupported assurances that a private question bank alone prevents future contamination, that the importer rejects all bad digests, that sanitization proves private-store revision repair, or that every released historical file has passed the publication API's sidecar gate. A missing source identifier is no longer treated as proof of original authorship.

## Pattern scan and its limits

A new automated pattern scan opened all 101,252 tracked files in the reviewed head and recursively examined archive members. Including members, it opened 102,379 objects, extracted text from 144 PDFs, opened 88 archives or compressed members, and scanned 101,852 text objects, with no extraction errors. It did not OCR or semantically review 439 binary objects.

The scan flagged 111 objects containing home-path patterns, 46 containing licence/private-label patterns, and one test source containing credential-shaped strings. These are pattern counts, not counts of confirmed private disclosures. The credential matches were visibly synthetic rejection-test fixtures. Some path hits are examples or test fixtures; others occur in historical records and archive members. Licence hits include third-party bibliographic notices and the historical benchmark-data marker. This scan is not a clean-release certificate, and changing its rules to hide these findings would not resolve them.

## Conditions not certified by this revision

1. A fresh export from the live working database was not available here. The existing public export was verified in full; the older remote working-repository export is not evidence of the live database's current contents.
2. Portable release-row digests pass, but this does not establish that the private store's legacy rows were repaired as new superseding revisions. Historical campaign hashes may still refer to pre-sanitization artifacts.
3. A complete comparison of book- and paper-derived expression against source permissions has not been supplied. Long quotations require shortening, removal or permission where necessary. The licence notice grants only project-owned rights.
4. The earlier record of 17 retired test items is not a fresh comparison of all private banks with the enlarged public release. Publicly answerable items are unsuitable for new held-out claims. Their repeated use must be described as regression testing.
5. The paper inventory concerns mathematics, mathematical physics and mathematical-research methods. Supporting files and archives still require the remaining privacy and rights review; this revision does not assert a semantic clearance of every object.

The manuscript is a corrected open-access edition. These outstanding verification requirements prevent describing the entire release as fully cleared.
