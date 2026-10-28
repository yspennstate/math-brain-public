# Checks of nine open-problem candidates (September 2026)

Nine questions posed in surveys, monographs and recent papers in probability and operator algebras, each with a
candidate answer, a written analysis of that answer, and an exact finite check of the identities the argument rests
on. Every candidate answers the question as literally stated; several of them depend on the statement carrying no
restriction (on degree, on independence, on the number of ends) that the surrounding text might suggest. Each
analysis says which narrower versions it does not address.

None of this establishes novelty. The literature searches recorded in each analysis were bounded, and in two cases
(P0208 and P0288) the analysis points to published work that already contains the main construction.

## The questions

| id | source | question | outcome of the analysis |
|---|---|---|---|
| P0174 | Hasebe and Ueda, ALEA 15 (2018), Problem 3.3 | the best constant C such that free Brownian motion started from a law of support diameter D is unimodal for t >= C D^2 | C = 1: unimodal for t >= D^2 by a moment argument; the symmetric two-point law shows every smaller constant fails |
| P0189 | van Handel, arXiv:2507.00346, Section 6.9 | does strong convergence of random matrices imply convergence of their Brown measures | no, in the unrestricted form: twisted cyclic shifts are nilpotent, converge strongly to an element of the irrational rotation algebra, and keep their Brown measures at zero while the limit's is spread over a disk |
| P0193 | Hasebe, Ueda and Wang, arXiv:2009.13848, Problem 4.7 | is free positive multiplicative Brownian motion eventually log-unimodal for every compactly supported initial law | no: the law with equal masses at 1/10 and 10 gives a log-density with four points on one level at all large times |
| P0208 | Aldous and Fill, *Reversible Markov chains and random walks on graphs*, p. 259 | asymptotics of hitting and commute times on arc-transitive graphs other than cycles | the 4-regular graph on Z_m x {0,1} gives tau_0 = (m^2-1)/6 + m and maximal commute time 2 floor(m^2/4) + 2m; the graph itself is known (Conder's 2013 lecture notes) |
| P0209 | Aldous and Fill, p. 137 | a chain-independent normal approximation controlled by the sup norm of the observable and time over relaxation time | no: a four-state reversible chain with a rare slow coordinate and a fast sign flip has relaxation time one and a bounded observable whose fluctuations are not close to normal on that scale |
| P0266, P0267 | the critical variational SPDE survey, Problems 4 and 5 | moment bounds and continuous dependence in the critical-noise setting | both fail for the scalar equation du = (u - u^3) dt + sqrt(2) u^2 dW: through the reciprocal of a four-dimensional Bessel process the expected squared supremum is infinite even from a positive constant start |
| P0276 | Salez, arXiv:2508.21055, Problem 2.4 | does the product condition imply cutoff for random walk on Abelian Cayley graphs | no, for unweighted graphs of unbounded degree: a hypercube with uniform resets and an auxiliary cyclic factor has the product condition and a mixing profile exp(-s) below the critical time |
| P0288 | Pollett, arXiv:2202.05428, Section 2(ii) | rank-one factorization of the limiting conditional kernel of a killed chain | no: the walk on Z killed at the origin has a rank-two limit kernel; the same two-end mechanism appears in Foley and McDonald, arXiv:1709.07578 |

## Layout

- `solutions/` holds the eight candidate texts (P0266 and P0267 share one), each opening with a line on what it does
  and does not address.
- `analyses/` holds one note per question (P0208 and P0209 share a note, as do P0266 and P0267). Each note rederives
  the load-bearing steps by a second route, lists the source pages read, and ends with the strongest remaining
  objection and the limits of the literature search.
- `checks/` holds five scripts. Each prints a JSON record of the finite cases it verified and of the deliberately
  wrong variants it rejected (an omitted correction term, a dropped mass, a wrong rate).

## Running the checks

Python 3.10 or later. Four of the scripts use only the standard library; `check_p0266_p0267.py` needs sympy.
P0174 and P0189 have no script here; their notes are analytic.

    python checks/check_p0193.py
    python checks/check_p0208_p0209.py
    python checks/check_p0266_p0267.py
    python checks/check_p0276.py
    python checks/check_p0288.py

The finite cases confirm the identities; they do not prove the infinite families. Those arguments are in the notes.
