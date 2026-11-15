disk: small

Read ~/fei_solve_agent/FLOW.md first, all of it; section 12 states this task (sections 7
and 11 are what it rests on). Scripts: the code folder beside it (filt_cs.py, hill_filt.py, local_cs.py,
local_cs2.py, comp_check.py, pm_k33.py, hill_rho.py; truth tables in code/hill_out). Earlier work:
~/codex_fleet/20261108_pro/workers/FEIB16 (FORMULAS.md, WITNESSES.md: exact composition laws and the PM(K33)
towers), FEIB13, FEIB14, FEIB17.

The object. For a Boolean f, a coordinate i and an ordering pi of the other coordinates, label a set T (not
containing i) by the position of its last element in pi; A_k, B_k = the masses of fhat(T)^2, fhat(T + i)^2 on
label k; L^pi_i = sum_k Phi(A_k, B_k) >= E_i = H(1[i in U] | U - i). The conjecture FWC of 12(i): there is an
absolute c with min over (i, pi) of L^pi_i <= c Inf_i for every non-constant Boolean f. FWC implies FEI.
Measured so far: at most 3.5417 (tribes of width 2), on everything in 12(h).

Part 1. Referee 12(b)-(g): the inequality E_i <= L^pi_i, the martingale form, the trivial bound, the shortest
path, the sufficient condition and its pair form (check the identity
A_{>=K} = P[i pivotal at y, not at y'] + 2 Cross_{K-1} and B_{<=K} = E h(y) h(y')), the composition formula.
One verdict line each: PROVED / GAP / FALSE.

Part 2. Try to REFUTE FWC. A counterexample is a family f_n with min over (i, pi) of L^pi_i / Inf_i unbounded.
By 12(c) it needs all influences small in every restriction that matters, and by 12(e) it needs, for every i and
every reveal order, a stage where D_i f is already predictable while E_i f is still undetermined with
probability far above Inf_i. Work beyond n = 10 by structure, not brute force:
  (a) exact formulas for min over pi on compositions F(g_1, ..., g_w) with symmetric or transitive pieces (the
      ordering can be taken block by block? prove or refute that an optimal ordering exists that respects
      blocks), then scan towers: tribes of tribes, AND/OR/MAJ/XOR alternations of depth 3 and 4, the PM(K33)
      tower of FEIB16, recursive majority, iterated address functions, with widths up to 10^3;
  (b) functions with a transitive symmetry group where no coordinate is special: projective-plane and
      Steiner-system DNFs, cyclic DNFs with overlapping terms, Reed-Muller-type quadratic forms plus sparse
      corrections, random k-DNFs at the threshold; compute L exactly where n <= 16 allows, by formula otherwise;
  (c) linear changes of variables of the extremal functions (they keep the spectrum's entropy and change which
      coordinates exist);
  (d) the gap to the exact erasure entropy: maximise min_{i,pi} L^pi_i / Inf_i - min_i E_i / Inf_i (the search
      in hill_filt.py reaches about 1.8 at n = 9); a family where that gap grows is the first step.
Report every family with its exact or numerical value and the growth rate you can prove.

Part 3. Try to PROVE FWC on classes, each closed under restriction, with explicit constants:
  (a) read-once formulas over AND/OR (ordering: by distance in the formula tree, nearest last), using 12(g);
  (b) read-once formulas with majority and threshold gates (section 11 inside each gate);
  (c) monotone DNFs of bounded width; decision trees of bounded expected depth; functions of bounded
      sensitivity or bounded degree;
  (d) a general rule for the pair (i, pi): state it, prove what it gives, test it against the shortest path of
      filt_cs.py on the functions of 12(h) (how far from optimal is the rule?).
Also: is an adaptive version valid (next revealed coordinate depends on the values seen, i.e. a decision tree on
the other coordinates)? Find the correct statement, if there is one, that still bounds E_i or D_i.

Part 4. Literature, one neutral paragraph with exact references: is this witness, or the statement
"E_i <= sum_k Phi(A_k, B_k) along a filtration", in Wan-Wright-Wu (decision trees, protocols and the
Fourier entropy-influence conjecture), Chakraborty-Kulkarni-Lokam-Saurabh (upper bounds on Fourier entropy),
O'Donnell-Tan (composition theorem), O'Donnell-Wright-Zhou (symmetric functions), Keller-Mossel-Schlank,
Shalev (read-k decision trees), Kelman-Kindler-Lifshitz-Minzer-Safra, or a later paper? Work from what you know
and from files on this machine; do not invent a reference; say "not checked" where you could not check.

Deliverables: REFEREE.md (Part 1), FAMILIES.md (Part 2: one line per family, value, growth, script),
PROOFS.md (Part 3; each statement PROVED / CHECKED with scope / OPEN), LITERATURE.md (Part 4), scripts with
their outputs, REPORT.md with one verdict line per part and the single most important finding first,
LEARNINGS.md. Write as you go. Memory: each process under 3 GiB, at most 2 threads, nice 10.
