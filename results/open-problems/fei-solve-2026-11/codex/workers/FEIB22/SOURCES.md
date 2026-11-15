# Sources and attribution

Primary source: Christophe Garban, Gábor Pete and Oded Schramm, *The Fourier spectrum of critical percolation*, Acta Mathematica 205 (2010), 19–104. [Author manuscript, HTML](https://arxiv.org/html/0803.3750), [published PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6727-11511_2010_Article_51.pdf).

Relevant locations read: arm probabilities and quasi-multiplicativity, equations (2.1)–(2.4); spectral restriction identities, Section 2.3; bulk influence comparison, (3.1); spectral hit-box bound, Lemma 3.2; partial-independence conditioning, Proposition 5.1 and its setup; the general-quad version, Proposition 5.11; and the spectral entropy question in Section 11.

Proposition 5.1 conditions on hitting a box and avoiding an arbitrary exterior set. It does not give the conditional law at a point given the exact exterior sample. ARGUMENT.md makes that distinction and derives the bulk-coordinate bound separately using physical resampling and disjoint annuli. That derivation is this worker's argument and awaits referee review; it is not attributed as a GPS entropy theorem.

Local inputs: ~/fei_solve_agent/FLOW.md, sections 7, 11(c), 12(b)–(l), 12(o), 12(p); code/mc_chain.py; mc_run/out_hexA.txt and out_hexB.txt, and the corresponding hex_16_s1.json, hex_24_s1.json, hex_32_s1.json. Original files were read without modification.

Brain consultation: `BRAIN_RECALL_REFRESH=0 python3 ~/.claude/dreaming/brain.py recall 'Fourier entropy influence percolation spectral sample' --or 'FEI last two witness hex crossing'`, followed by `brain.py node kalai_conj8_percolation_entropy_is_o_influence_2026_09_10`. This surfaced a provisional global-entropy argument and pointed to the GPS box estimate; it was useful context, but none of its unrefereed conclusions were assumed. `python3 ~/.claude/dreaming/math_recall.py 'percolation spectral sample conditional box' --or 'Garban Pete Schramm Fourier spectrum'` reported that the math store was not found. Fleet rules prohibit writing the shared brain or mesh, so the durable mathematical handoff is saved locally in ARGUMENT.md and REPORT.md.
