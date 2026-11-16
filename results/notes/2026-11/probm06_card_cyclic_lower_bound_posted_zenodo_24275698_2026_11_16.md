---
name: probm06_card_cyclic_lower_bound_posted_zenodo_24275698_2026_11_16
description: "[VERIFIED] Card-cyclic-to-random shuffle (Morris-Ning-Peres; Levin-Peres Chapter 26 asks for cutoff): paper posted 16 Nov 2026, repo card-cyclic-lower-bound, Zenodo 10.5281/zenodo.24275698. Lower bound c n log n for every c < 1/(2a), about 0.239, up from 1/(2+2a), about 0.162."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

In the card-cyclic-to-random shuffle the cards labelled 1, ..., n are removed in turn, cyclically, and each is
reinserted at a uniform position. Paper: https://github.com/yspennstate/card-cyclic-lower-bound, archived at
doi:10.5281/zenodo.24275698.

Result. Let -a+ib be the root of e^{-z} = 1-z used by Morris, Ning and Peres (a about 2.089). The mixing time is at
least c n log n for every c < 1/(2a), about 0.239; the earlier constant was 1/(2+2a), about 0.162.

How the proof goes.
- Work with the pair-order functions f_ij (is card i above card j). They are linearly independent: swapping two
  adjacent cards i, j changes f_ij and nothing else.
- In a frame that rotates with the card being reinserted, the chain acts on these functions as the exterior square of
  an explicit n by n companion-type matrix M (Proposition 2.2).
- The wedge of the eigenvectors of M for s = 0 and s = z is an exact eigenfunction of the chain, with eigenvalue of
  modulus 1 - a/n + O(n^{-2}).
- Wilson's second-moment lemma for a complex eigenvalue of a lifted chain finishes the bound.

What existed before. Morris, Ning and Peres (Ann. Appl. Probab. 24, 2014; arXiv:1207.3406) proved order n log n with
the constant 1/(2+2a) and asked about cutoff. Pinsky (Random Structures Algorithms 46, 2015) introduced the shuffle.
Bernstein and Nestoridi (Ann. Probab. 47, 2019) gave the upper bound (3/2) n log n. Jonasson (ALEA 12, 2015,
arXiv:1501.05485) treated the variant relabelled by position after each pass, with a single-card eigenvector test
function. The lower-bound method is Wilson's: Ann. Appl. Probab. 14 (2004) for a real eigenvalue, and Electron.
Commun. Probab. 8 (2003), Lemma 2, for a complex eigenvalue of a lifted chain. New are the exterior-square description,
the exact pair eigenfunction and the constant 1/(2a). Cutoff remains open.

Checks. checks/check_shuffle.py verifies Proposition 2.2 on every deck for n = 3 to 6 in exact arithmetic and the
eigenfunction on every deck for n = 5, 6, 7; a clean clone on a second machine reproduced checks/output.txt exactly.
A first-reader audit (minor edit, five must-fix items) was applied before posting. Two of those items were citations
(Jonasson and Wilson 2003) found by reading as a referee, not by keyword search; each was checked against arXiv and the
journal's own index before it went in.
