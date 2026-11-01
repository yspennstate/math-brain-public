# Source, novelty, and scope check

Date: 3 October 2026.  This record concerns the ten-vertex bipartite
Möbius ladder `ML10 = K_{5,5}\setminus C_{10}`.

## Current status

The unrestricted ML10 Sidorenko inequality is **not proved here**.  The
September 2025 primary status source of Fox--Himwich--Mani--Zhou identifies
this graph as a small unresolved case:

- Fox, Himwich, Mani, Zhou, *A note on directed analogues of the Sidorenko
  and forcing conjectures*, EJC 32(3) (2025), P3.38,
  https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/

Rossman's May 2025 primary note is the source of the ladder transfer
identity and its spectral program:

- Benjamin Rossman, *On Sidorenko's Conjecture for Bipartite Möbius
  Ladders*, https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf

The following later primary papers were checked because they prove broad
but structurally different classes.  None, as stated, supplies the
unrestricted ML10 theorem or the colored-coefficient statement studied
here:

- Yuqi Zhao, *Sidorenko-Type Inequalities for Even Subdivisions over
  Finite Abelian Groups*, arXiv:2507.15723.
- Yuqi Zhao, *Conjugacy Class Averages and Sidorenko's Conjecture*,
  arXiv:2606.15368.
- Yuqi Zhao, *Sidorenko Inequalities for Two-Sided Group Correlation
  Kernels*, arXiv:2606.23018.

The search was bounded, and historical priority of the two-state quartic
lemma has not been established.  Internal verification is not external
peer review.

## What is proved

1. For a chosen square of ML10, its four-B/eleven-A colored density is
   nonnegative for every entrywise-nonnegative symmetric `2 x 2` matrix A
   and every real symmetric `2 x 2` matrix B.  An exact 66-term determinant
   certificate and an independent elimination check prove this.
2. A stronger strategy—nonnegativity of every even colored coefficient in
   binary-coordinate averaging—is false even for a strictly positive,
   mean-one, sixteen-state kernel.  Its sixth coefficient is an explicitly
   negative rational number.  Three independent exact evaluations agree.
3. The C4 transfer, reflection, and Walsh-translation identities are exact.
   Individual nontrivial-character C4 contributions can nevertheless be
   negative in the admissible host class, so character-by-character
   positivity is also unavailable.

## What is not proved

The negative sixth coefficient is **not** a Sidorenko counterexample: the
total density is about `70.6086`, hence above one, and the total binary
averaging difference is positive.  Global C4 positivity beyond the
two-state lemma, total averaging monotonicity, unrestricted ML10 Sidorenko,
and general Sidorenko all remain open here.  The q=32 and q=64 optimizations
are finite floating-point evidence only.

