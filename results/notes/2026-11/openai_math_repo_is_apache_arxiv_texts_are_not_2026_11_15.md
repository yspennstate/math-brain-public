---
name: openai_math_repo_is_apache_arxiv_texts_are_not_2026_11_15
description: "[VERIFIED] Copy openai/math manuscripts or Lean into a public repo? Yes, Apache-2.0 with license file + THIRD_PARTY note; arXiv paper texts no (cite only); mbp_port leaves agent ids in folder names"
metadata:
  type: reference
  created: 2026-11-15
  created_at: 2026-11-15T10:44:05+02:00
  status: verified
  evidence: "api.github.com/repos/openai/math/license -> Apache-2.0, 15 Nov 2026; proof-checks folder names carried an agent id after mbp_port"
---

Can we republish files from openai/math (the OpenAI mathematics release) in math-brain-public? Yes: the repository is under the Apache License 2.0 (checked 15 Nov 2026 via api.github.com/repos/openai/math/license). Manuscripts and Lean files may be copied if the license text travels with them and the copies are marked. In math-brain-public, results/open-problems/codex-rounds-2026-11-14/ carries LICENSE-openai-math.txt and THIRD_PARTY.md for the AV_ folders that hold such copies.

arXiv paper texts are a different matter: the default arXiv license allows no redistribution. For the proof-checks-2026-11-12 batch, every lit/*.txt|tex|pdf (other authors' papers, one with an author's email) was dropped, and each check cites its paper by author, title and arXiv id. Check a paper's own license before copying it; CC-BY papers may go in, with credit.

mbp_port.py scrubs file contents (agent ids, home paths) but not folder names. The proof-check folders were named like ag05_jacobian_<agent-id>_2026_11_12, so they were renamed by hand. After porting, grep the path list as well as the contents.

