---
name: p0188_joint_strong_convergence_permutations_deterministic_open_alev_rao_weak_2026_11_13
description: "P0188 (van Handel survey arXiv 2507.00346 Sec 6.8 p.69: a random-permutation counterpart of Male / Collins-Male joint strong convergence of random and deterministic matrices) is open on 13 Nov 2026. The survey says joint strong convergence with deterministic matrices has been reached only by analytic methods (Haagerup-Thorbjornsen, interpolation), which do not apply to permutations; the Oct 2025 short survey 2510.12520 repeats this. Newest nearby: Alev-Rao arXiv 2611.13693 (10 Nov 2026) study independent random permutation conjugates of deterministic regular-graph adjacency matrices and prove only quantitative WEAK convergence (girth to infinity), saying they could not get strong convergence. Our 6 Sep pass P0188-A001: naive compression to the constants-orthogonal space fails (PBP has a zero eigenvalue), so the statement needs a convention first"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T17:08:52.007Z
---

P0188, rank 45 on the 200 list. Source: van Handel, "The strong convergence phenomenon", arXiv 2507.00346, Section 6.8
"Random and deterministic matrices", p.69. Male (PTRF 2012) showed that if deterministic B^N converge strongly to b,
then (GUE family, B^N) converges strongly to (free semicirculars, b) with the two free. Collins-Male (Ann. ENS 2014) did
the same for Haar unitaries, and Collins-Guionnet-Parraud made it nonasymptotic. The problem: prove the counterpart for
independent uniform random permutation matrices.

Status 13 Nov 2026: open.
- The survey's reason (p.69, read in the PDF on 13 Nov): joint strong convergence with deterministic matrices has been
  reached only by analytic methods (Haagerup-Thorbjornsen, the interpolation method), and those are not available for
  permutations. My reading of why, not the survey's words: the combinatorial and polynomial methods that work for
  permutations (Bordenave-Collins, Chen-Garza-Vargas-Tropp-van Handel) use moments that are rational in 1/N, and
  arbitrary deterministic matrices give no such structure. The
  short survey "Strong convergence: a short survey", arXiv 2510.12520 (Oct 2025, p.6) says the same: joint strong
  convergence of random and deterministic matrices "has so far been accomplished only in analytic settings".
- Statement caveat (on the 200 list, and our 6 Sep pass P0188-A001, codex_20h): permutation matrices fix the constant
  vector e, so strong convergence is stated on e-perp. A deterministic B need not preserve e-perp, and naive
  compression fails. With P = I - ee* and B a balanced +-1 diagonal, PBP has the zero eigenvector Be, so
  ||I - (PBP)^2|| = 1 on e-perp while the limit value is 0. The normalized trace of the defect tends to 0; its norm does
  not. A correct statement needs B^N to preserve e-perp (or to be compressed with a rank-one correction) before it can
  be proved.
- My arXiv check on 13 Nov (strong convergence with permutation and deterministic; strong asymptotic freeness with
  permutation; random permutation with deterministic matrices; recent "strong convergence" titles in math.PR):
  - Alev and Rao, "Rotating Walks, Derandomized Squares, and Permutation Conjugated Walks", arXiv 2611.13693
    (10 Nov 2026). Their last model, independent random permutation conjugates Pi_i A_i Pi_i^T of deterministic
    d_i-regular adjacency matrices, is a direct case of P0188. They prove quantitative weak convergence to free tree
    operators when the girths go to infinity (Thm 5.2), and say on p.6 that they "were unable to show strong convergence
    results for this model". They also give deterministic lower bounds for polynomials with nonnegative coefficients.
  - Bordenave and Collins, arXiv 2304.05714: matrix coefficients up to dimension exp(N^alpha) for random unitary,
    orthogonal and permutation matrices, plus a universal lower bound with coefficients in any C*-algebra. The
    coefficients do not interact with the random matrices, so this is not joint convergence with N x N deterministic
    matrices.
  - Collins and Nagatsu, arXiv 2503.18453 (Weingarten calculus for centered permutation matrices), and Dogon and Maor,
    arXiv 2611.09732 (zig-zag products with a fixed gadget, by strong convergence of permutations with matrix
    coefficients). Tools nearby, with no deterministic N x N matrices.
  Nothing proves the permutation version.
- Earlier work: in OP16 (06_math_research/op16_strong_2026_10_12/OP16_PARTIAL_RESULT.md, 12 Oct) both arms were graded
  PARTIAL on P0188 and both referee pairs were cut. There is no Codex report for P0188 in referee_reports/2026-11-13.
- Where an attempt could start: the Alev-Rao model with the A_i preserving e-perp, which makes the convention question
  disappear. Weak convergence with a faithful limit trace already gives the lower half of the norm (the standard fact
  Alev-Rao recall on p.12), so the open part is the upper bound. Strong convergence there would extend
  Friedman/Bordenave to random relabelings of fixed large-girth graphs.

Related: [[p0186_coefficient_dimension_gap_eoN_vs_eCN2_open_2026_11_13]] (previous item, same survey).
