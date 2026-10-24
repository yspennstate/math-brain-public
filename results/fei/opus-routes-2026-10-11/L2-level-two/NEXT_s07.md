# NEXT_s07 (recovery agent claude-6bb7036b-s07, stream s07 = FEI mathematics)
Started 12 Oct 14:46 local. Predecessor claude-51330238 (last action 06:57 local). Updated 19:1x local.

DONE (all in this folder unless named):
- NOTES.md sections 0-9: Lemma 1, Lemma 2, Theorem 3 (per-level b_k), Corollary 4, Theorem 5 (localization, Bonami
  threshold 1/2 exact), Proposition 6 + Corollary 7 (slice level law is arcsine; no level inequality for {0,+-1}
  functions passes c = 1/2), gap reduction, obstructions O1-O5, the tribes one-block witness (after O5), section 5b
  (read-once formulas: Lemma R, branch witness exact, bounded cells lose kappa_h eps log(1/eps)), sections 5c, 5d and 5e
  (below), B13 re-derivation, numerics (section 7, with the check_levels full run), the interval certificate (3.6)
  and this stream's own adversarial pass (9.1-9.9).
- Section 5c: Corollary R2 (on read-once AND/OR/parity formulas the height at which S - i first reaches the branch of i
  is an exact witness); bench code/general_witness.py on 43 functions; X009's selector bit rules out witness bounds
  charged coordinate by coordinate. Second path code/audit_general_witness.py.
- Section 5d: pivotal faces P1-P4 (none claimed new). P3 bounds only the trivial witness cost and gives nothing below
  it; the "split" restates B = O(I) and is not a reduction. EVIDENCE: an unpredictable coordinate need not have a
  subcube pivotal set (random-set selector). Code: code/pivotal_faces.py, code/audit_pivotal_faces.py.
- Section 5e (new 18:5x): blocks with signed-character fibers. Lemma B: if F(x, y) = s(x) chi_{tau(x)}(y) over an
  address block X, then sum_{t in Y} B_t <= H(S_Y) = H(tau(X)) <= 2 I_X, constant 2 attained by AND2^N; identity
  B_X = sum_T R_T B(nu_T) for any split. Elementary (erasure entropy <= entropy; Harper on each cell), not claimed new.
  Consequence: on that class the data block, with any number of unpredictable coordinates, is never the obstruction
  (answers old NEXT item 2 for the class); the address part is as hard as FEI (|Y| = 1 is every function). Outside the
  class H(S_Y) <= 2 I_X fails (three witnesses) and only the general form with avg_x H(F_x) holds.
  Code: code/selector_block.py (25 functions, every quantity twice, max difference 3.6e-15; data/selector_block.json,
  .log) and code/audit_selector_block.py (no shared code; 278,440 cases, exhaustive on 4-bit functions and at m = N = 2,
  random to n = 11; no violation; data/audit_selector_block.log).
- Section 5e, Corollary K (19:0x): if every monomial of the GF(2) polynomial of f uses at most one variable from each
  of K blocks (the blocks properly colour the monomial co-occurrence graph), then B <= H <= 2(K - 1) I, so
  H <= 2 (chi - 1) I <= 2 Delta I. K = 2 is the elementary quadratic case (sharp on inner product); for K = 3, 4 the largest
  H/I found is AND_3's 2.9559 and AND_4's 3.4025 against 4 and 6. Not claimed new (no literature search). Code:
  code/block_partite.py (244,934 members, no violation; non-partite control finds 414 violated inequalities among 600;
  data/block_partite.json, .log) and code/audit_block_partite.py (no shared code; 1,360 members admitted by a fiber test,
  no violation; 400 of 400 controls rejected; data/audit_block_partite.log). CLAIMS L2-SB-K (CANDIDATE), L2-SB-K-E.
  Annealing code/block_partite_search.py (shapes to (4,4,4) and (3,3,3,3), 13 s): nothing above AND_K, weak evidence
  that D_3 = c*. Reach: the GF(2) polynomials of tribes, AND/OR trees, read-once formulas, balls and majority have
  complete co-occurrence graphs (top monomial by parity of the weight; e_d with d >= 2 for symmetric), so Corollary K
  never reaches the families behind O2, O5 and 5b; code/partite_reach.py, data/partite_reach.log (controls never complete).
- code/check_levels.py full run (data/check_levels_20261012T181724.json, data/check_levels_full.log): 70,253 functions,
  0 violations of eleven checks.
- CLAIMS.json: 27 claims; CANDIDATE 20, PROVED 2 (checks of other agents' results), EVIDENCE 5. New L2-SB, L2-SB-K
  (CANDIDATE, with novelty fields), L2-SB-E, L2-SB-K-E (EVIDENCE); L2-PF-E remaining_gap and best_next_step point at them.
- ../SYNTHESIS.md: section 3 sentence on paying a block of unpredictable coordinates (L2-SB); target 1 status lines
  18:5x (Lemma B) and 19:0x (Corollary K); item 5 names sections 5d and 5e. ../README.md: NEXT lines 18:5x and 19:0x.

RUNNING: nothing of this stream.

BLOCKED ON HIM: nothing.

NEXT: (1) the open part of B_gap is the witness for coordinates whose trivial cost h2(eps_i) is too large: the missing
inequality of 5c, a lower bound on P(i in S | W) for a scale-and-count witness on the high-level mass of D_i f, on average
over i weighted by eps_i (equivalently, a bound on sum_i eps_i E[log(1/pi_i(W)) | i in S]); test its form on tribes,
AND/OR trees, OR of MAJ3 and X009 before attempting a proof; (2) the address part of 5e, B averaged over normalized
signed subset functions s 1_A (as hard as FEI in general; useful only on subclasses where the cells A_T are structured);
(3) Corollary K: a literature search on K-partite (block-multilinear) GF(2) phases before anyone calls K >= 3 new;
whether D_3 (sup H/I over 3-partite f) equals c* = 2.9559, the K2 constant of A2, which the search suggests; a better
use of the chain rule than subadditivity for K >= 3; (4) a separate adversarial pass on every CANDIDATE in CLAIMS.json,
by an agent other than this stream.
