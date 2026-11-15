You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/, sources/ of another run):
open problem I0003, Section 7, Problem 3 of A. Bou-Rabee and Y. Peres (the paper on random walks on Manhattan-type lattices /
orientation fields; find it, record exact title, authors, arXiv id and version): for which orientation fields (e_y on horizontal
lines, f_x on vertical lines, each +1 or -1) is the walk on Z^2 that follows the orientations recurrent?

The claim is PARTIAL. With two-sided primitives S, T of e, f (S(0)=T(0)=0) and M(r)^2 = max_{|k|<=r}|S(k)|^2 + max_{|k|<=r}|T(k)|^2:
A. fields whose primitives differ by a bounded amount have the same type (diagonal Green functions finite at the same sites);
B. sum_m 1/(1+M(2^m)^2) = infinity implies recurrence (e.g. |S(k)|+|T(k)| = O(sqrt(log |k|)));
C. for fields eventually constant on all four tails, recurrent iff e_- = -e_+, f_- = -f_+, e_+ f_+ = -1 (the two circulating
   arrangements), all others transient; so (g(y), -g(x)) is recurrent and (g(y), g(x)) transient although |S|, |T| agree;
D. iid symmetric horizontal signs plus any vertical field with bounded primitive: transient a.s., simultaneously for all such fields;
E. for upper-bound classes S = O(|k|^a), T = O(|k|^b), every member recurrent iff a = b = 0.
The proof uses a continuous-time generator L = S + A with A antisymmetric, the identity for the symmetric part of the resolvent,
(H - A H^{-1} A)^{-1}, and a variational formula for the diagonal resolvent; predecessors cited are Gaudilliere-Landim (Lemma 5.5)
and Bosi (Theorem 9(i)).

Break it if it is wrong.
1. Get the source paper and the works REPORT relies on (Gaudilliere-Landim on random walks in divergence-free / random stream
   environments, Bosi on Manhattan / random orientation walks, Campanino-Petritis, Guillotin-Plantard - Le Ny, Pene, Brémont, and
   any 2024-2026 follow-ups) into sources/ as plain text from arXiv, independently of claim_files/sources. State Problem 3 exactly
   and check REPORT restates it correctly, including what "recurrent" means for a possibly reducible walk.
2. Check the proof line by line. In particular: (a) is A really antisymmetric on l^2(Z^2) for every field (each orientation constant
   along its own line), and is counting measure invariant? (b) the resolvent identity (1) and the variational formula for the
   diagonal of the inverse: signs, domains, and the step from diagonal resolvent as lambda -> 0 to recurrence for a nonreversible,
   possibly reducible chain. (c) Statement A: is the comparison under bounded primitive change uniform and two-sided? (d) Statement
   B: the test functions and the dyadic sum; build a field with sum finite that is recurrent, to confirm REPORT's claim that
   convergence is not sufficient. (e) Statement C: check both directions by hand on the circulating pair and on one transient
   arrangement; try to break the "finite arbitrary configurations do not matter" clause. (f) Statement D: the probability-one event
   uniform over all bounded-primitive vertical fields; measurability and the use of A. (g) Statement E: the transient examples from
   Bosi's sparse perturbations and the maximal inequality.
3. Small simulations of return times for the C1 pair (recurrent vs transient) are allowed as evidence only.
4. Ask the hard question: is any of A-E already in the literature (Bosi, Gaudilliere-Landim, Brémont, the source paper itself)?
   Check every citation in REPORT against sources.
5. Verdict: correct or not, novel or not, exactly what is proved, and how much of Problem 3 it answers.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Small numerical
checks in code/ are allowed (evidence only). Source texts may go in sources/ as plain text only; no PDFs kept, no page images.
Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
