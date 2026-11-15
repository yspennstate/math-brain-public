# Substantial omitted advance; the scaling-limit conjecture remains open

Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an appendix by
Laurin Köhler-Schindler, *The phase transition for planar Gaussian percolation
models without FKG*, Annals of Probability **51** (2023), 1785–1829.
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3),
[paper](https://arxiv.org/pdf/2010.11770),
[DOI](https://doi.org/10.1214/23-AOP1633).

The arXiv submission was 22 October 2020; v3 was submitted 17 July 2023.
This predates the supplied November 2026 status check but substantially
advances the results that paragraph actually lists.

For the random plane wave, write E_l = {f >= -l}. Theorem 1.3 and
Example 1.4 (PDF page 4) establish:

- For each fixed l < 0, every component of E_l is bounded almost surely.
- For each fixed l > 0, E_l has exactly one unbounded component almost surely.
- For each fixed nonzero level, its level lines are bounded almost surely.

Theorem 1.7 (PDF page 5) gives, for every fixed l < 0 and a > 0,

    P(Cross_l(R,aR)) <= c1 exp(-c2 sqrt(log R)),   R >= 1,

with positive constants depending on l and a. Here Cross means a
left-to-right crossing inside [0,R] x [0,aR].

These are noncritical results. They establish neither zero-level RSW nor
Cardy's formula nor an SLE(6) limit. The filename follows the task's
substantial-advance stop rule; it does not announce a solution of T064.

An independent later source confirms the remaining gap: Stephen Muirhead
and Igor Wigman, *The giant component of excursion sets of spherical Gaussian
ensembles: existence, uniqueness, and volume concentration*, published online
18 March 2025, Probability Theory and Related Fields **194** (2026),
2099–2172, [article](https://doi.org/10.1007/s00440-025-01367-8).
The discussion after Proposition 1.7 and Section 1.3.1 still leave
percolation at criticality open for monochromatic random waves.
