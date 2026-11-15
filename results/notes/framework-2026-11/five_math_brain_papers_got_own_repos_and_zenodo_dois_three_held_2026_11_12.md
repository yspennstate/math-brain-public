---
name: five_math_brain_papers_got_own_repos_and_zenodo_dois_three_held_2026_11_12
description: "[VERIFIED] His 01:34 'independent repos + Zenodo' ask: 5 math-brain-public papers now own repos + DOIs 24150838/40/46/48/52 (md5+refs checked); pseudo-cognitive, crossing cores, section profiles held; rerun pitfalls"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T05:44:46+02:00
  status: verified
  evidence: "Zenodo API readback of 24150838/40/46/48/52 (state done, md5, references) and git ls-remote heads, 12 Nov 05:38"
---

His 12 Nov 01:34 email answer ("Make independent repos for these other ones and publish in zendono"), about the eight math-brain-public manuscripts that had no Zenodo record. Done 12 Nov 05:3x by an agent for five of them. Each one was staged from math-brain-public origin/main 6520487c into its own public repo (one "Initial commit"), then given a new Zenodo record by API:

| repo (github.com/yspennstate/...) | head | Zenodo |
|---|---|---|
| math-brain-shared-auditable-memory | e15df0d8 | 10.5281/zenodo.24150838 |
| nonlinear-sgd-power-tails | e8ed0a93 | 10.5281/zenodo.24150840 |
| calibration-along-gradient-descent | 5c3dd70e | 10.5281/zenodo.24150846 |
| phase-retrieval-sampling-barriers | 2d7b9e83 (PDF rebuilt; the old PDF had an older abstract) | 10.5281/zenodo.24150848 |
| three-problems-kernel-methods | 9eb54ac3 | 10.5281/zenodo.24150852 |

Each record was checked after publish: state done; one file whose md5 equals the repo PDF's; references stored exactly as sent. The one difference was the kernel record's ref 35, where Zenodo turned curly quotes into straight ones. Related identifiers on each: isSupplementedBy the repo at its commit, isPartOf math-brain-public, references brain-framework-public.

Three were held, and the reasons were sent to him (email 1a1cdda3131bbb5e, thread 1a1cce273ed0206d):
- pseudo-cognitive-dynamics: no author line, no declarations, and the title term is Elisha's. Authorship is his call; my recommendation is Elisha as co-author.
- crossing-cores-toeplitz-hankel: no master source for sections 1-13, and its declarations are likely inaccurate.
- toeplitz-hankel-section-profiles: depends on crossing cores, has no competing-interest section, its AI declaration is likely inaccurate, and some lines are overfull.
The Roe-algebra manuscript (it overlaps 23329820) and the dissertation were not posted.

What a rerun of this recipe needs to know:
1. Check that the PDF in the repo is built from the current .tex. T321's PDF carried an older abstract; I caught it by searching the PDF text for the TeX abstract's last sentence.
2. Get references from the PDF with the peer's pdf_refs_ay.py, then clean them. It ran past [13] into the back matter on one paper (46 entries). It also glued the address block and an "Israel" line onto the last entry, and it leaves words split at a line-break hyphen (Ad-vances, Psy-chometrika). Keep only the [n] lines and assert the count against \bibitem.
3. The Zenodo deposit list caps at size=100 (size=200 gives HTTP 400). Page through it for the duplicate-title check; 139 titles were on the account.
4. A naive TeX-to-text pass flattens nested exponents (2^{2^{2l}}) and subscripted Lip constants. Read every abstract in a dry run before publishing, because a DOI is permanent.
Scripts are in the session scratchpad: zen8_publish.py, zen8_refs_fix.py, zen8_zenodo.py, zen8_email.py. Related: [[zenodo_bulk_upload_by_own_file_input_and_draft_files_api_2026_11_08]], [[zenodo_refs_from_the_pdf_accents_labels_and_tails_2026_11_11]], [[github_papers_vs_zenodo_24_files_lag_two_old_repos_2026_11_12]].

