# Spectral-center slab continuation: source and completion record

2 October 2026 UTC. Read the complete final proof, K and root analytic
audits, both full scripts and all check records in this folder. The new
global statement is H(g)<=(C_slab+60)J(g), giving ordinary FEI for every
character modulation of a parallel slab. The full ordinary slab theorem
and its constant are explicit upstream inputs in the prior parallel-slab
continuation, not numerical fits. Its proof and independent audits were
fully read before this extension.

Character spectral shifts, physical-influence flips, Chow identities,
Parseval and edge isoperimetry are standard facts. The author primary
reference Ryan O'Donnell, Analysis of Boolean Functions, May2021 arXiv
edition (originally April2014), was inspected again on2October2026:
https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf.
The new proof reproduces its elementary inputs fully, including the
edge-isoperimetric induction, and does not assert novelty for them.

The earlier O'Donnell–Tan2013 generic composition/deficit framework is
credited in the upstream source records. This centered bound does not
follow from a comparison J>=c(I-Var): that comparison fails even for
two-bit parity represented as a slab. The proof instead centers the
function and glues at most15 coordinates using the universal total-
influence entropy split bound. Its separate genuine-slab local obstruction
proves that a pivot-local centered-influence bound also fails.

The wide-gap union corollary has the explicit previously proved ordinary
input; arbitrary nearby finite-crossing functions do not. The separate
at-most-m-unate-gate closure lemma is conditional on ordinary FEI and
restriction closure. Neither statement proves FEI for arbitrary Boolean
combinations of halfspaces or shared-input circuits.

Root and K independently read the actual final proof and upstream
dependencies, rederived the main steps, and reran the actual scripts.
Exact integer/Fraction assertions and numerical entropy checks are
distinguished in the records. General Boolean FEI and nonuniform-input
entropy remain unresolved here. Historical priority, outside review and
publishability remain unverified; a bounded source search is not a
certificate that an earlier related result does not exist.
