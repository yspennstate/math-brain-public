---
name: public_edition_papers_carry_dead_private_repo_links_rewrite_before_doi_2026_11_12
description: "[VERIFIED] Posting a paper from the math-brain-public edition? Its bib links github.com/<private-repo>/... and private-source-repository/... are dead placeholders (286 in Pseudo-Cognitive Dynamics, guard passed them): rewrite to 'private repository, commit, file' notes before the DOI"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T06:51:17+02:00
  status: verified
  evidence: "Zenodo 24151631 readback (state done, md5, 180 refs); grep counts in yspennstate/pseudo-cognitive-dynamics before/after commit e54cd02"
  lesson: true
---

Papers taken from the math-brain-public edition carry scrubbed bibliography links: the private repo names were replaced by the placeholders `github.com/<private-repo>/blob/<sha>/<path>` (the Brain memory and functionality repository) and `github.com/private-source-repository/blob/<sha>/<path>` (the Math Brain source repository). In the printed PDF they look like URLs and lead nowhere. Pseudo-Cognitive Dynamics (paper 6 of the 12 Nov batch) had 286 of them in 11 .bib files; the guard (`paper_release_guard.py`) passed with them in place, and a scan whose output I filtered with `grep home|secret|trading` hid the `private` line that counted them.

**How to apply:** before any public-edition paper goes to its own repo or Zenodo, run `grep -c -E "github.com/<private-repo>|github.com/private-source-repository" *.bib sections/*.tex`. Rewrite each such `url` field into the entry's note as "Brain memory and functionality repository (private), commit <sha>, file \path{<path>}" (script: scratch area p6_privrefs.py of session agent, copy kept beside LOOP_STATE), rename the placeholders in the appendix revision table, rebuild, and re-check. Never filter a scanner's output down to the categories you expect; read every line.

For the Zenodo References field, pdf_refs.py joins wrapped lines; `\path{}` strings break at any character, so a path token at a line end must be joined without a space, and every extracted path and URL is checked verbatim against the .bib (refs_paths_check.py: 180 refs, 0 misses on paper 6).

Result: github.com/yspennstate/pseudo-cognitive-dynamics (commit e54cd02), DOI 10.5281/zenodo.24151631, state done, md5 a31119a2... matches, 180 references stored as sent (12 Nov 2026 06:49). Related: [[math_brain_public_mirror_sync_scrub_split_hold_2026_11_12]], [[five_math_brain_papers_got_own_repos_and_zenodo_dois_three_held_2026_11_12]], [[pdftotext_drops_overlines_look_at_the_page_2026_11_12]].

