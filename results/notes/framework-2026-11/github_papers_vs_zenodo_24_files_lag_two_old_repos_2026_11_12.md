---
name: github_papers_vs_zenodo_24_files_lag_two_old_repos_2026_11_12
description: "Are all GitHub papers on Zenodo (12 Nov)? 138 records, 114 public paper repos each have one; 24 Zenodo files older than the PDF on GitHub; 2 old-version repos and 8 empty References fields"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:14:05+02:00
  status: verified
  evidence: "work_agent/zen_gh/audit.json and match.txt (Zenodo deposition list and GitHub repo list read 12 Nov 00:5x-01:10 workstation; md5 of each PDF)"
---

Are all the GitHub papers on Zenodo? Checked 12 Nov 2026 about 01:10 workstation for a request to check that every GitHub paper is also on Zenodo.

**What was measured**
- Zenodo account (authenticated deposition list): 138 records, all published. 114 each link to one paper repo under yspennstate; the other 24 are his earlier arXiv / ResearchGate papers and link only to the site.
- GitHub account: 197 repos, 128 public. 114 public paper repos have a record. Of the other 14 public repos, 11 are not papers, one is a supplement (law-of-robustness-two-layer; the paper is record 23329778), and two are papers with no record: free-strong-unimodality (the 10 Oct combined paper; its results are records 24063842 and 24063846, matched by README and title only) and fourier-entropy-influence-symmetric (constant 6.1347; the 4.650431 version is record 24142256 from symmetric-fei-constant).
- PDF on GitHub main against the file Zenodo serves, by md5: 90 identical, 24 differ. In all 24 the PDF's last commit on GitHub (9 or 11 Nov) is later than the Zenodo file (13 Oct for 23 of them; fei-hidden-coordinates was uploaded 11 Nov 17:08 UTC and changed on GitHub at 22:07 UTC). Contents were not compared.
- 8 records have an empty References field: stable-unimodality-opposite-gaps, free-strong-unimodality-point-masses, toeplitz-hankel-exact-moments, ising-perceptron-margin, relu-global-stability-numerics, outer-vertex-isoperimetry, ross-s-second-queueing-conjecture, maximal-kemeny-constant.
- 16 private repos hold a paper or draft and have no record (top-level listings only).

**How to redo it**
Match by the GitHub link in each record's related identifiers, and leave out the shared credit links (brain-framework-public, math-brain-public, the site): 84 of the records carry those two as well, and counting them makes every record look multi-linked. Then md5 each candidate PDF from raw.githubusercontent against the record's file checksum, and for a mismatch read the PDF's last commit date against the record's created date. Scripts and data: ~/.claude/brain_graph/studies/math_hunt_2026_11_11/work_agent/zen_gh/ (fetch.py, match.py, current2.py, audit.py, audit.json).

**What would change it**
Any new Zenodo version or a new push to a paper repo; the 24 are a snapshot. Nothing was uploaded: a new version for each of the 24 waits for his word and has to pass the citation hooks first. The list of the 24 is in audit.json and in the email body beside it.

Related: [[zenodo_lagged_github_reference_commits_check_latest_md5_2026_11_11]], [[zenodo_refs_from_the_pdf_accents_labels_and_tails_2026_11_11]].


**13 Nov 2026 02:0x outcome (an agent).** Re-checked by md5 from fresh clones: emit-oco2-kernel-emulators and the Chern Doubling-and-Jamming repo were already current. New versions published: maximal-kemeny-constant 24181327 (8863963, b675e2c1) and fei-hidden-coordinates 24181376 (6db9f8e, dfe75baf). ising-perceptron-margin left for after its first-reader audit (an agent). The other 19 carry a ResearchGate DOI (10.13140), so Zenodo refuses a new version (zen_api.py exits on it); `git diff` of the .tex since 13 Oct shows only the Math Brain acknowledgement and added references in every one, no mathematical change, and their References fields were filled by metadata edit on 12 Nov. Decision: no duplicate records for those 19. Reopen only if one of them gets a mathematical correction; then the route is a new Zenodo record with isNewVersionOf the RG DOI.
