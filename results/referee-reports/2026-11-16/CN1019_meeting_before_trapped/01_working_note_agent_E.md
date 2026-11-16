# CN1019: meeting before hitting a frozen target (Addario-Berry, Oliveira, Peres, Sousi, Conjecture 1.5)

Source: L. Addario-Berry, R. I. Oliveira, Y. Peres, P. Sousi, Random walks colliding before getting trapped, arXiv:1506.07845,
Electron. J. Probab. 21 (2016), doi 10.1214/16-EJP4414 (Conjecture 1.6 in the journal numbering). X, Y at rate 1, Z frozen,
all independent from pi on a finite irreducible reversible chain: is P(M_good <= M_bad) >= 1/3? They prove 1/4 (strict
inequality) for transitive chains (Thm 1.2); Holroyd's example (their Section 6) shows 1/3 cannot be raised; "any uniform
lower bound c > 0 ... would be a new result". Restated as OP 2.1 in Addario-Berry's 2022 note "How to create an open
problem". Searches on 16 Nov 2026 (arXiv, Semantic Scholar citations: two citing papers, neither on this question; web)
found no later proof, counterexample or refined form.

## Computation (meet.py; m8.txt)
F(pi, c) = sum pi_x pi_y pi_z h_z(x,y), h_z harmonic for the pair generator (ties count as good), exact linear solve;
minimised over all reversible chains on n states (pi and every conductance free), 30 Powell starts.
  n:        3          4         5         6          7          8
  min F:    0.407407   0.375000  0.360000  0.351852   0.346952   0.343786
  formula:  0.407407   0.375000  0.360000  0.351852   0.346939   0.343750      (1/3 + 2/(3n^2))
n = 3..6 match the formula to six digits; n = 7, 8 stop 1.3e-5 and 3.6e-5 above it (Powell local optima). No run went
below it. The minimisers have uniform pi and degenerate conductances (separated time scales); the infimum is a limit.
Coverage caveat: F returns 1.0 when the solve is ill-conditioned or h leaves [0,1], which walls off part of the region
where the extremal (multi-scale) chains live; conductances are clipped to [e^-14, e^14].

## Multi-scale chains (scale-separation limit; argument sketched, checked numerically)
Build a chain by merging blocks on separated time scales: each merge of blocks A, B (weights a, b) is much slower than
everything inside A and B and much faster than everything above. In the limit, with all three walkers in the merged
block the problem is the 2-state problem on weights (a, b), scaled; X, Y in a block without Z meet before leaving;
X and Z in a block trap X. So the merge lowers F by (a+b)^3 (1 - (a^2+b^2)/(a+b)^2) = 2ab(a+b) = (2/3)((a+b)^3 - a^3 - b^3),
and the sum telescopes from F = 1 for one state:
    F -> 1/3 + (2/3) sum_x pi_x^3 = P(X0=Y0=Z0) + (1/3) P(not all equal)      for every binary tree and every pi.
This explains the table (uniform pi: 1/3 + 2/(3n^2)). Holroyd's example ({0,1}^n, coordinate j flips at rate ~ eps^(j-1))
is the balanced tree with uniform pi on 2^n states, so its limit is 1/3 + (2/3) 4^(-n). Checked on four nonuniform trees
with eps = 1e-2, 1e-3, 1e-4: the gap to the formula falls like eps (dtest.py, d6.txt).

Composition identity. Write D = F - 1/3 - (2/3) sum pi^3. For a two-level chain (blocks B of weight w_B, fast inside,
slow between) the same limit argument gives F = F_top - sum_B w_B^3 (1 - F_B), and since sum pi^3 = sum_B w_B^3 s3(B),
    D = D_top + sum_B w_B^3 D_B.
D = 0 for every 2-state chain, so the tree formula is a corollary, and D >= 0 is preserved by scale-separated
composition: a counterexample to the refined bound would have to contain a piece with no scale separation.

## Refined form of the conjecture
For every finite irreducible reversible chain, F >= 1/3 + (2/3) sum pi^3; equivalently, conditioned on the three not
starting at one state, X and Y meet first with probability at least 1/3. Equality for every 2-state chain; approached
by multi-scale chains for every pi, so it would be sharp at every pi, not only as pi spreads out. It is the tie-corrected
form of the symmetry heuristic in the paper's introduction.
Evidence: minimising D over all conductances at 36 fixed interior pi (n = 3, 4, 5; 12 pi each, 8 Powell starts;
dfixed.py, df.txt) gives min D in [1e-16, 3e-7], never negative. The free-pi search (d6.txt) slides to point masses where
D = 0 and says nothing. One optimiser, n <= 5: this is not strong evidence for larger n.

n = 3 is proved (n3proof.py). With w_z the conductance of the edge opposite z, h_z = a_z/(a_z+b_z), a_z = w_z(1-pi_z),
b_z = sum_{x != z} w_x pi_x, and F = 1 - 2 e2 + 2 e3 sum_z h_z (e2, e3 elementary symmetric in pi), so the refined bound
is sum_z h_z >= 1. Clearing denominators and homogenising with pi1+pi2+pi3 = 1, the numerator of sum h_z - 1 is a
polynomial with 25 terms, all coefficients positive; each term carries two distinct w's, so the inequality is strict for
irreducible chains. Closed form checked against the linear solve on 200 random chains (max error 1.6e-12).

Optimiser-free scan (dscan.py, ds.txt): 400 chains per n and family, n = 4..10, families random / star / path / barbell /
lollipop / cycle with a chord, lognormal conductances (sigma up to 5), pi uniform, Dirichlet or one state carrying
0.5..0.95 (pi_max up to 0.999 seen). Smallest D per cell between 2.8e-9 and 6e-4; no negative value anywhere.

Status: open. Next: n = 4 symbolically (the pair system is 6 unknowns per z), or D >= 0 for stars.
