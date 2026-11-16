# P0251: referee report on the crossover-chain paper (16 November 2026)

The problem is Open Problem 12.5 in D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*:
how fast does the crossover chain on L binary words of length K, which pairs the words at random and swaps
coordinates within each pair, reach its stationary law? The paper under review is
github.com/yspennstate/crossover-chain-mixing (Zenodo doi:10.5281/zenodo.24257131). This folder holds one referee
report, written by a model instance that did not write the paper, and the three scripts it ran.

| file | what it is |
|---|---|
| `01_referee_report_agent_A.md` | Line-by-line check of the paper, four points for the author, and an addendum with a lower bound of order log K. |
| `p0251_l1_check.py` | Simulation of one column (labeled and original chains): mean contraction and total variation, `python p0251_l1_check.py 1024 2000 6`. |
| `p0251_l2_check.py` | Original chain with two identical columns: the overlap statistic W. |
| `p0251_cov_check.py` | The exact covariance of partner indicators under a uniform perfect matching, against brute force at K = 8. |

## What existed before and what is new

The upper bound in the paper rests on A. Czumaj's random switching networks (*Random permutations using switching
networks*, STOC 2015, doi:10.1145/2746539.2746629), used through his Proposition 2.3 and Theorem 3.4. The
comparison with random transpositions goes back to P. Diaconis and M. Shahshahani (Z. Wahrsch. Verw. Gebiete 57
(1981) 159-179), and mixing of genetic-algorithm crossover was studied by Y. Rabani, Y. Rabinovich and A. Sinclair.
The lower bound in the addendum is a second-moment argument of the kind D. B. Wilson introduced for card shuffling
and lozenge tilings (Ann. Appl. Probab. 14 (2004) 274-325): a statistic whose mean contracts by an exact factor
lambda = (K-2)/(2(K-1)) per step while its variance stays of order K.

New in the report: in the original chain a single column is uniform after one step, so a lower bound of order
log K at L = 1 holds only for the labeled variant; for the labeled variant at every L, and for the original chain at
every L >= 2, t_mix(1/4) >= (1/2) log_2 K - 5 for even K >= 8, with an explicit covariance constant
|Cov| <= 3/(K-3). With the paper's upper bound this gives mixing time of order log K + log L for 2 <= L <= K.

## Status

Referee verdict: the paper's argument is correct; the theorem numbers cited from Czumaj's paper other than
Proposition 2.3 and Theorem 3.4 were not confirmed against the full text. The lower bound is a referee's
suggestion with a proof and numerical checks, not yet part of the paper.
