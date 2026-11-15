# GE07 moving sofa: state of the check

Source: J. Baek, "Optimality of Gerver's Sofa", arXiv 2411.19826v1, 29 Nov 2024, 119 pages, 8 chapters.
Local copies lit/2411.19826/paper.txt (6030 lines) and lit/1606.08111/paper.txt (Romik, 1561 lines); not pushed.

## Done (12 Nov 2026)

Note: GE07_CHECK.md. Scripts and outputs: ge07_check.py -> ge07_check.out; ge07_q.py -> ge07_q_800.out,
ge07_q_1600.out. Search record: lit/search/s1.xml.

Section line numbers in paper.txt: 1.2 at 322, 1.3 at 511, 1.4 at 641, 1.5 at 777, 1.6 at 878, 1.7 at 960
(differential inequality 1013, its solution 1120), 1.8 at 1193; 6.5 at 4105; 8.1 at 4841; 8.2 at 5045 (Theorem 8.2.4
at 5160); 8.3 at 5176; 8.4 at 5351; 8.5 at 5606 (Theorem 8.5.7 at 5773, Corollary 8.5.8 at 5821).

## Not done

- Chapters 2–5, Chapter 6 apart from 6.5, Chapter 7, the proof of Theorem 8.2.4 and the proofs of Section 8.5 are
  unread.
- Publication and formalization status of the paper: not established (the arXiv record has one version and no
  journal reference).
- Trela, arXiv 2610.13955: abstract only. Its verifier is said to use only the Python standard library and exact
  rationals; running it would give an exact check of the Gerver-specific hypotheses.
- A test of Theorem 8.2.4 on caps far from Gerver's (the family here is 20 caps, all with smooth rotation paths).
