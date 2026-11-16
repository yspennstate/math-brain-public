# CN1019: two random walks meeting before either is trapped (working record, 16 November 2026)

The problem is Conjecture 1.5 (1.6 in the journal numbering) of L. Addario-Berry, R. I. Oliveira, Y. Peres and
P. Sousi, *Random walks colliding before getting trapped*, Electron. J. Probab. 21 (2016), arXiv:1506.07845: on a finite
irreducible reversible chain, start X, Y (rate 1) and a frozen Z independently from the stationary law pi. Is the
probability that X and Y meet before either hits Z at least 1/3? The problem remains open. This folder is one agent's
working record (snapshot of 16 Nov 2026, 07:21) and the scripts it ran.

| file | what it is |
|---|---|
| `01_working_note_agent_E.md` | The computation, the scale-separation limit, the composition identity, the refined conjecture and its proof for three states. |
| `meet.py` | Exact F(pi, c) by a linear solve for the pair walk; minimisation over all reversible chains on n states (`m8.txt`, `minimisers.txt`). |
| `dtest.py` | Multi-scale chains against the limit formula (`d6.txt`). |
| `dfixed.py` | Minimum of D at fixed interior pi, n = 3, 4, 5 (`df.txt`). |
| `dscan.py` | Optimiser-free scan of D over six graph families, n = 4..10 (`ds.txt`). |
| `n3proof.py` | The three-state closed form and the positivity of the 25-term numerator. |

## What existed before and what is new

Addario-Berry, Oliveira, Peres and Sousi posed the question, proved a uniform bound of 1/4 for transitive chains
(their Theorem 1.2), and gave, after A. E. Holroyd, the example on the hypercube with geometrically separated rates
showing that 1/3 cannot be raised. L. Addario-Berry restated it as Open Problem 2.1 in his 2022 note *How to create an
open problem*.

New in the record: under scale separation every binary merge of blocks of weights a and b lowers the probability by
2ab(a+b), so multi-scale chains tend to 1/3 + (2/3) sum pi^3, and Holroyd's example is the balanced case; the defect
D = F - 1/3 - (2/3) sum pi^3 is additive under scale-separated composition; the refined conjecture F >= 1/3 + (2/3)
sum pi^3 is proved for three states and is unbroken in the numerical searches up to ten states.

## Status

Open. The refined bound for n >= 4 is a conjecture supported by optimisation and scans, not a proof; the scale-separation
limit is argued and checked numerically, not written as a theorem.
