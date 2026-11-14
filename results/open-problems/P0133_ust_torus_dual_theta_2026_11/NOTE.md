# P0133: the dual theta of a uniform spanning tree on a torus (Schramm 2006, Problem 6.2) - numerics, 14 Nov 2026

## Setting

Let T be a uniform spanning tree of a fine discretization of the torus C / <1, tau>. Every edge e outside T closes a
fundamental cycle with homology class h(e) in Z^2 (the class (a, b) is the period a + b tau). The nonzero classes
that occur are +-p, +-q, +-(p + q) for a basis (p, q) of Z^2 (a superbase {v1, v2, v3}, v1 + v2 + v3 = 0, taken up
to sign), unless only two classes occur, in which case the complement of T in the dual graph has a figure-eight core
rather than a theta core. The question is the scaling limit of this topological data.

## Code (this folder)

- ust_torus_theta.py: Wilson's algorithm on the n1 x n2 rectangular torus, lift of the tree to the plane, classes of
  all fundamental cycles (numba).
- ust_torus_shear.py: the same on the sheared torus Z^2 / <(n1, 0), (s, n2)>, modulus tau = (s + i n2) / n1. A class
  is read from the lifted displacement (DX, DY) as b = DY / n2, a = (DX - b s) / n1.
- ust_metal.swift: the sampler of ust_torus_shear.py on an Apple GPU (Metal source compiled at run time, one tree per
  thread, Wilson's walk and both retrace passes as one loop). 10^6 trees of the 160x160 torus in 206 s on a Mac mini.
  Same output format; on 40x40 s20 its law matches the numba sampler (48,000 against 24,000 samples, every superbase
  within 2 se). mesh_table.py prints the law by mesh for one modulus; shape_fit.py fits log w over moduli;
  cand_fit.py fits short closed forms; holdout.py fixes a fitted w and tests it on moduli it was not fitted on.
- classify.py: tally of superbases, ordered by |a + b tau|. compare.py: the law of one discretization against another,
  with an optional matrix carrying the classes of a PSL2(Z)-equivalent modulus to those of the first.

## Findings

1. The figure-eight core disappears in the limit. Its frequency on the square torus: 0.0255 (n = 8), 0.0059 (16),
   0.0016 (32), 0.0005 (64); on every sheared torus tested it falls by a factor of 2-4 when the mesh is halved. So in
   the limit the dual core is a theta graph almost surely and the data is a random superbase S of the lattice.

2. The law of S converges and depends on tau only. Two meshes of the same modulus agree to within sampling error
   (24,000 samples each):

   | tau | meshes | P(top superbase) | next superbases |
   |---|---|---|---|
   | i | 32, 64 | 0.475 / 0.474 for each of {1, i, 1 +- i} | four of norms (1, 2, 5), 0.0125 each |
   | 0.5 + 0.866i | 30x26 s15, 60x52 s30 | 0.728 / 0.726 for {1, tau, 1 - tau} | three, 0.090 each |
   | 0.5 + i | 40x40 s20, 80x80 s40 | 0.717 / 0.712 for {1, tau, 1 - tau} | two at 0.117-0.121, one at 0.048 |
   | 2i (and 0.5i, axes swapped) | 32x64, 48x24 | 0.42 for each of {1, 2i, 1 +- 2i} | {1, 1 +- 2i, 2 +- 2i} 0.075 |
   | 0.25 + 1.5i | 40x60 s10 | 0.561 {1, tau, 1 - tau}, 0.314 {1, tau, 1 + tau} | 0.101, 0.017, 0.003 |

   The symmetries of each lattice are respected: the three level-two superbases of the hexagonal torus are equally
   likely, and at tau = 0.5 + i the reflection pairing {1, tau, 1 + tau} with {1, tau - 1, tau - 2} holds.

3. Shape of the law. To first order, P(S) is close to C(tau) exp(-c Q(S)), Q(S) = (|v1|^2 + |v2|^2 + |v3|^2) / Im tau,
   with c between 0.88 and 0.91 for the first excited level on the square, hexagonal and 0.5 + i tori. It is not exact:
   at tau = 2i the same ratio gives c = 0.86, and deeper levels drift (0.76-1.06, partly noise). So the limit law looks
   like a theta-type sum over superbases with a nontrivial prefactor, as one would expect from the compactified-boson
   description of the c = -2 (spanning tree) theory, but we have not identified it.

4. The law does not see how the torus sits on the lattice. The modulus 0.6 + 0.8i = (tau - 1) / tau for tau = 0.5 + i
   is realised as 50x40 s30 and 100x80 s60, and 0.8 + 0.4i = 2i / (1 + 2i) as 100x40 s80 and 150x60 s120; mapping
   their classes back by the matching element of PSL2(Z) (compare.py with matrices 0 -1 1 1 and 1 0 1 1) and comparing
   with 40x40 s20 and 32x64 (24,000 samples each side):

   | modulus pair | P(top two or three superbases), axis-aligned / placed at an angle | largest diff/se |
   |---|---|---|
   | 0.5 + i vs 50x40 s30 | 0.717 / 0.716, 0.117 / 0.117, 0.116 / 0.120, 0.047 / 0.046 | 1.1 |
   | 0.5 + i vs 100x80 s60 | 0.717 / 0.708, 0.117 / 0.119, 0.116 / 0.125, 0.047 / 0.047 | 2.8 |
   | 2i vs 100x40 s80 | 0.423 / 0.424, 0.418 / 0.416, 0.077 / 0.079, 0.075 / 0.075 | 1.0 |
   | 2i vs 150x60 s120 | 0.423 / 0.417, 0.418 / 0.425, 0.077 / 0.076, 0.075 / 0.077 | 1.7 |

   The one gap above 2 se is between the finer 100x80 mesh and the coarser 40x40 one, and it goes the way the
   axis-aligned 80x80 s40 mesh already went (0.712 and 0.121 there), so it is a mesh effect of about one percent,
   not a dependence on the placement. Together with finding 2 this is the numerical form of conformal invariance of
   the superbase law: P depends on tau through its PSL2(Z) class only.

5. Million-sample runs (ust_metal.swift). Standard errors are about 0.0005 for the top superbases.

   Mesh ladders (P per superbase on each mesh):

   | tau | superbase | 32x32 / 40x40 s20 | 64x64 / 80x80 s40 | 128x128 / 160x160 s80 |
   |---|---|---|---|---|
   | i | {1, i, 1 + i}, and its mirror {1, i, 1 - i} | 0.4741, 0.4746 | 0.4749, 0.4748 | 0.4753, 0.4745 |
   | i | the four at Q = 8 | 0.0124-0.0126 | 0.0124-0.0126 | 0.0125-0.0126 |
   | 0.5 + i | {1, tau, 1 - tau} | 0.7142 | 0.7142 | 0.7137 |
   | 0.5 + i | the two at Q = 5.5 | 0.1185, 0.1183 | 0.1188, 0.1189 | 0.1194, 0.1192 |
   | 0.5 + i | {tau, 1 - tau, 1 - 2 tau} at Q = 6.5 | 0.0465 | 0.0464 | 0.0462 |

   The figure-eight frequency keeps falling by a factor of about 3.5 per halving of the mesh (0.0016, 0.00044, 0.00013
   on the square torus). The law itself moves by at most 0.0009 from the coarsest to the finest mesh, so the values
   in the last column are the scaling limit to about three digits. Two digits of it: on the square torus each top
   superbase has probability 0.475 and each of the four next 0.0125, so these six superbases carry all but about 10^-4 of the
   mass; at 0.5 + i the top superbase has 0.714.

   256x256 (10^6 trees) leaves the square torus where it was: 0.4750 and 0.4749 for the top pair, 0.0124-0.0126 for
   the four at Q = 8, figure eights 0.00004. The hexagonal torus (30x26 s15, 60x52 s30, 120x104 s60, tau = 0.5 + 0.8667i, so
   within 0.001 of e^{i pi/3}): the equilateral superbase {1, tau, 1 - tau} has 0.7273, 0.7277, 0.7276, the three at
   Q = 5.77 (angles 30, 30, 120) 0.0895-0.0908 each, the six at Q = 12.7 0.00017 each.

   Read as P proportional to exp(-c Q), the ratio of the top superbase to the next level gives c = 0.909 (square, Q 4
   to 8), 0.904 (hexagonal, Q 3.46 to 5.77, and again 0.904 out to Q = 12.7), 0.896 and 0.911 (0.5 + i, Q 3.5 to 5.5
   and to 6.5), but 0.85 at tau = 2i (Q 5 to 7). So the exponential form holds to a few percent near the hexagonal
   and square points and not at the long thin torus; the exponent is not a constant of the model.

   A superbase's triangle determines its lattice up to similarity, so "P_tau(S) = w(shape(S)) / Z(tau)" holds for any
   law and says nothing beyond conformal invariance; the content is in the form of w. Every triangle has
   cot A cot B + cot B cot C + cot C cot A = 1, so e1 = sum cot (= Q / 2) and e3 = prod cot fix the shape, and
   shape_fit.py fits log w as a polynomial in (e1, e3) with log Z free per modulus. On the six finest meshes above
   (34 cells, 11 shapes): degree 1 gives chi2/dof 112 (log w = -1.737 e1 + 0.021 e3), degree 2 gives 2.97. Eleven
   shapes cannot tell more; the grid of finding 6 is for this.

   Placement, at a million samples a side and the finer meshes: 160x160 s80 (tau = 0.5 + i) against 200x160 s120
   (tau = 0.6 + 0.8i, classes mapped by 0 -1 1 1) agree to 0.34 se on the four main superbases, with nothing above
   1.9 se on any cell. 64x128 (tau = 2i) against 300x120 s240 (tau = 0.8 + 0.4i, mapped by 1 0 1 1): the top
   superbases 0.4207 and 0.4196 against 0.4199 and 0.4211, a mirror pair whose sum agrees to 1.25 se; the two at
   Q = 7, 0.0770 and 0.0768 against 0.0769 and 0.0765.

6. The weight as a function of shape. A grid of tori 100 x n2 with shift s (n2 = 100, 110, 125, 150, 175, 200, 250,
   300 and s = 0, 10, ..., 50, plus 100 x 90 s50), 10^6 trees each, gives 49 moduli, 333 superbase cells with at least
   200 counts and 284 distinct shapes. On it log w is fitted as a polynomial in e1 = cot A + cot B + cot C (= Q/2) and
   e3 = cot A cot B cot C, with log Z free per modulus:

   | degree | coefficients | chi2/dof |
   |---|---|---|
   | 1 | 2 | 94.03 |
   | 2 | 5 | 11.67 |
   | 3 | 9 | 2.54 |
   | 4 | 14 | 1.25 |

   On the first 38 moduli, before the n2 = 250 and 300 rows were complete, the cubic fitted at chi2/dof 1.5 to 1.7;
   the elongated tori push the needed degree to four. The degree a polynomial needs grows with the range of shapes, so the
   polynomial is a local description of w and not its form.
   Fitted on the grid alone and held fixed, with only log Z refitted, the quartic predicts the six finest
   earlier meshes (256x256, 160x160 s80, 200x160 s120, 300x120 s240, 64x128, 120x104 s60) at chi2/dof 1.02 over 28
   degrees of freedom, no cell beyond 1.92 se; the cubic, which predicted them at 1.28 when fitted on the first 38
   moduli, gives 2.48 (worst 3.25 se, hexagonal) when fitted on all 49.

   Short closed forms do worse. The best four-term form Q, log Q, sum log L_i, sum L_i^2 (L_i = |v_i|^2 / Im tau)
   reaches chi2/dof 2.58; the best three-term form Q, log Q, sum log sin reaches 3.94; Q with side sums
   sum log L_i and sum 1/L_i reaches 11.57. The side features do not help on their own, so the weight is not a
   product of one factor per side. A formula for w is not in hand.

## What would solve it

An exact formula for P_tau(S). Candidates: Kenyon's line-bundle Laplacian (arXiv 1001.4028), which gives the
homology law of incompressible cycle-rooted spanning forests on the torus in closed form, applied to the theta by a
two-loop (non-abelian or second-order) version of the same expansion; Kassel-Kenyon (arXiv 1211.6974) for
topological laws of curves induced by the Laplacian determinant. The numbers above are the check any candidate must
pass. Status: open; numerics only, not audited.
