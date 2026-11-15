---
name: duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10
description: "About to write a paper or create a public repo for a solved row (T067, Formentin-Kulske 2.13, Potts Galton-Watson)? Check first: 10 Nov I posted a duplicate of posterior-cones-reconstruction (24 Oct) and withdrew it in 14 min; read math-brain-public papers/README.md, list the repos, grep compaction nodes"
metadata:
  type: feedback
  created: 2026-11-10
  created_at: 2026-11-10T11:10:40+02:00
  status: verified
  evidence: "GitHub API: potts-reconstruction-galton-watson private True at 11:07, anonymous ls-remote refused; pub/main papers/public/posterior-cones-reconstruction T067_full_proof.tex Theorem 1 read"
---

On 10 Nov 2026 I wrote and posted a second paper for a theorem we had already published, and withdrew it
fourteen minutes later.

What happened
- The theorem (three-state Potts broadcasting on a Galton-Watson tree with any finite-mean offspring law:
  reconstruction exactly when d lambda^2 > 1, none at equality; four states by the OpenAI cone) is the main theorem
  of our public paper "Posterior cones and sharp reconstruction thresholds on finite-mean Galton-Watson trees",
  repo yspennstate/posterior-cones-reconstruction, dated 24 Oct 2026, 16 pages, HEAD f69959c0 on 8 Nov. It is
  mirrored in math-brain-public under papers/public/posterior-cones-reconstruction and is the T067 paper of the
  31 Oct release papers/three-targets-2026-10-31.
- Working the top-200 review I ranked "Formentin-Kulske Conjecture 2.13" as the closest row, found the 24 Oct proof
  package in the brain, audited it, and wrote a new 10-page paper. Repo yspennstate/potts-reconstruction-galton-watson
  was created 10:24, the paper pushed 10:53 (commit 49c84cf7), the overlap found at 11:03 when I opened the public
  math brain to add the entry, and the repo set private at 11:07 (anonymous ls-remote refused). The local clone
  ~/papers_top10/potts-reconstruction-galton-watson is kept.

Why it happened
- brain.py recall on T067 returned the memories about the proof package and the two regular-tree papers
  (potts-kesten-stigum-small-degree, potts-four-state-binary-tree); the posted Galton-Watson paper lives in the
  brain only inside compaction nodes and checklist entries, which I did not open.
- I did not read the table in math-brain-public papers/README.md, or list the account's repositories, before
  creating a repo. Either would have shown the paper in under a minute.

The rule
Before writing a paper for a solved row, and always before creating a public repo: (1) read
`git show pub/main:papers/README.md` in ~/math-brain-public-edition (the table of every mirrored paper
and the releases), (2) search the account's repositories for the topic words, (3) grep the memory folder, the
compaction nodes included, for the row id AND for the object ("Galton-Watson", "posterior cone"). A proof package
filed weeks ago with two audits has usually been posted by the line that produced it.

What is still worth doing from the morning's work
- The October paper does not cite Formentin and Kulske (Stochastic Process. Appl. 119 (2009) 2992-3005,
  Conjecture 2.13, eq. (45)); one clause there says that the theorem settles their conjecture for q = 3 and 4 and
  at equality. The two-state case is Evans-Kenyon-Peres-Schulman.
- The 10 Nov audit of the analytic chain and the population-dynamics check (brain repo 7656ca6a, folder
  06_math_research/top200_review_2026_11_10/fk213) stand as a third audit of the October paper.
- Checks made that day: in the normalisation m = E x(p) the second-order term on the d-ary tree is
  -(1/2) lambda^4 d(d-1) m^2 (Sly's -(3/4) is for x_n = 2m/3); subadditivity of x fails pointwise at
  p = r = (1/2,1/2,0).

What would change this: if the author prefers the shorter write-up, the private repo holds it; it must replace the
October paper, never stand beside it.

