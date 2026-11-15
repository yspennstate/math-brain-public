# PD08 state (an agent, 12 Nov 2026)

Done: paper 2509.25116v2 fetched and read at statement and outline level, Section 4.5 and the definitions on
PDF pages 30, 35-36, 51 read in full; three dated searches; follow-up abstracts; repository listing;
pd08_check.py run (about 4 minutes on the laptop), output pd08_check.out.

Result: PD08_CHECK.md. Keep REPORTED_SOLVED.

Open, cheapest first:
1. Compare our root list with data/bessel_zeros.mat of the authors' repository (commit 615ee6f3) to settle
   whether N = 1257 / 1260 is "all eigenvalues below about 9.77" or something else. A .mat file is data:
   read it with scipy.io.loadmat under python -I in its own folder.
2. Read arXiv 2611.06117 (113 pages, analytic route). If its proof holds, the row is solved without a computer.
3. Rerun the authors' Julia notebooks on a Mac mini (read the sources first; they are a third party's code).

Not pushed: lit/2509.25116 (the paper's PDF and text); lit/repo_listing/*.json (raw API answers, refused by the secret scan for their signature blocks; LISTING.txt carries the paths, sizes and dates).

## 12 Nov 06:46 - the authors' root file compared (item 1 above, done)
data/bessel_zeros.mat holds 2,516 roots, every root of (6.3), (6.4) below 100; ours are the same 2,516 (largest
difference 7e-13). Class of U 1257, class of v 1259 plus the zero mode = 1260: the paper's N. N means "root
below 100", scaled eigenvalue below 9.7656; lambda_{N+1} is 9.769 and 9.778, K5 0.4604 and 0.4600 <= 0.47. The
"> 10" of Section 6.2 is loose wording. Scripts pd08_mat_dump.py, pd08_zeros_cmp.py; output pd08_zeros_cmp.out;
PD08_CHECK.md part C.
Open, cheapest first: 1. arXiv 2611.06117 (113 pages, analytic route): statement, outline, and the step that
replaces the computer. 2. rerun the authors' Julia notebooks on a Mac mini (read the sources first).

## 12 Nov 06:49 - the second paper, first reading
arXiv 2611.06117 (113 pages) is a different construction, not an analytic version of the first paper: a
cascade through Gaussian swirls at radii 1, 1/Lambda, 1/Lambda^2, ..., fully analytic. Theorem 1.1, Remark 1.2
and Section 1.3 read from the text. Statement consistent with the uniqueness theorems and with scaling; the
centrifugal instability of the Gaussian swirl recomputed by hand (potential (r^2 - 4) exp(-r^2/2), neutral
radius 2, maximum 2 e^-3 at sqrt 6, as the paper states). PD08_CHECK.md has the section.
Open, in order of weight: 1. Lemma 4.9 (sign of the complete quadratic stress) with Lemma 4.7, lines 4051 to
4560 of lit/2611.06117/paper.txt and the pages by eye; 2. Lemma 4.2 and Lemmas 4.4 to 4.6 (lines 2789 to
4050); 3. Proposition 7.7 and Proposition 8.1; 4. the authors' Julia notebooks for the first paper.

## 12 Nov 07:15 - Lemmas 4.7 to 4.9 of the second paper
Read from PDF pages 43, 45 to 51 and redone by hand; identities and the weight inequalities also checked to 40
digits (pd08_weight_check.py, .out). No error found. PD08_CHECK.md has the section.
Open, in order of weight: 1. Lemma 4.2 (growth rates), Lemma 4.4 (band lower bound), Lemma 4.5, Lemma 4.6
(low-frequency deficit), pages 30 to 44, by eye; 2. Proposition 7.7 and Proposition 8.1; 3. the authors' Julia
notebooks for the first paper. Read the PDF pages, not paper.txt (no Greek letters in it).

## 12 Nov 07:18 - Section 4 of the second paper read through
Lemmas 4.1, 4.2, 4.4, 4.6 redone by hand at every computation; 4.3 and 4.5 read at the level of the argument.
No error found. PD08_CHECK.md has the section. Status of the row unchanged: REPORTED_SOLVED, two papers, no
error found in what was read; the second paper's Sections 5 to 9 are unread.
Open, in order of weight: 1. Section 5 (Propositions 5.2, 5.3, 5.5: transfer of the sign to the actual
solution), PDF pages 51 on; 2. Proposition 7.7 and Proposition 8.1; 3. the authors' Julia notebooks for the
first paper. Read the PDF pages, not paper.txt.

## 12 Nov 07:28 - Section 5 of the second paper read through
Propositions 5.2, 5.3, 5.5 and Lemma 5.4 read on PDF pages 51 to 63; every explicit computation redone by hand
and 30 of them again numerically or in exact fractions (pd08_sec5_check.py, .out, all pass). No error found.
PD08_CHECK.md has the section. Status of the row unchanged: REPORTED_SOLVED, two papers, no error found in what
was read; of the second paper Sections 4 and 5 are read, Sections 3 and 6 to 9 are unread beyond the statements.
Open, in order of weight: 1. Proposition 7.7 (the shape estimate at the larger scale) and Proposition 8.1 (the
iteration), with Section 6 (Lemmas 6.1, 6.2: endpoint moment without loss), PDF pages 63 on; 2. Proposition 3.4
(the finite-energy reference solution and the correction bound (5.6), on which Section 5 rests); 3. the authors'
Julia notebooks for the first paper. Read the PDF pages, not paper.txt.

## 12 Nov 07:32 - Section 6 of the second paper read through
Lemmas 6.1, 6.2, 6.3 read on PDF pages 63 to 72; the explicit computations redone by hand and 15 of them by
script (pd08_sec6_check.py, .out, all pass). No error found. PD08_CHECK.md has the section. Status of the row
unchanged: REPORTED_SOLVED, two papers, no error found in what was read; of the second paper Sections 4, 5 and 6
are read, Sections 3, 7, 8, 9 are unread beyond the statements.
Open, in order of weight: 1. Section 7 (Proposition 7.7, the shape estimate at the larger scale), PDF pages 72
on, then Section 8 (Proposition 8.1, the iteration); 2. Section 3 (Lemma 3.1 and Proposition 3.4, on which
Sections 5 and 6 rest); 3. the authors' Julia notebooks for the first paper. Read the PDF pages, not paper.txt.

## 12 Nov 07:44 - Sections 7.1 and 7.2 of the second paper read through
Lemma 7.1 and Lemma 7.2 (entrance through the invariant array) read on PDF pages 72 to 81; the explicit
computations redone by hand and 31 of them by script (pd08_sec7a_check.py, .out, all pass). No error found.
PD08_CHECK.md has the section. Status of the row unchanged: REPORTED_SOLVED, two papers, no error found in what
was read; of the second paper Sections 4, 5, 6 and 7.1, 7.2 are read; Sections 3, 7.3 on, 8, 9 are unread beyond
the statements.
Open, in order of weight: 1. Section 7.3 on (the actual incoming field, Proposition 7.7), PDF pages 81 on, then
Section 8 (Proposition 8.1, the iteration); 2. Section 3 (Lemma 3.1 and Proposition 3.4); 3. the authors' Julia
notebooks for the first paper. Read the PDF pages, not paper.txt.

## 12 Nov 07:48 - Sections 7.3 and 7.4 of the second paper read through
Lemma 7.3 and Lemma 7.4 read on PDF pages 81 to 85; the explicit computations redone by hand and 14 of them by
script (pd08_sec7b_check.py, .out, all pass). No error found. PD08_CHECK.md has the section. Status of the row
unchanged: REPORTED_SOLVED, two papers, no error found in what was read; of the second paper Sections 4, 5, 6 and
7.1 to 7.4 are read; Sections 3, 7.5 on, 8, 9 are unread beyond the statements.
Open, in order of weight: 1. Section 7.5 on (smoothing in parent coordinates, exact time alignment,
Proposition 7.7), PDF pages 85 on, then Section 8 (Proposition 8.1, the iteration); 2. Section 3 (Lemma 3.1 and
Proposition 3.4); 3. the authors' Julia notebooks for the first paper. Read the PDF pages, not paper.txt.

## 12 Nov 08:01 - Sections 7.5 to 8.1 of the second paper read through
Lemmas 7.5, 7.6, 7.8, Proposition 7.7, Section 8.1, the statement of Proposition 8.1 and the series on the
source interval read on PDF pages 85 to 92; the explicit computations redone by hand and 26 of them by script
(pd08_sec7c_check.py, .out, all pass). No error found. PD08_CHECK.md has the section. Status of the row
unchanged: REPORTED_SOLVED, two papers, no error found in what was read; of the second paper Sections 4 to 7 and
8.1 are read (PDF pages 30 to 92); Section 3, the rest of Section 8 and Section 9 are unread beyond the statements.
Open, in order of weight: 1. the proof of Proposition 8.1 from PDF page 93 (transfer interval, leading
amplitude, moment class) and the rest of Section 8 (finite cascades, the shooting argument); 2. Section 3
(Lemma 3.1 and Proposition 3.4); 3. Section 9; 4. the authors' Julia notebooks for the first paper.
Read the PDF pages, not paper.txt.

## 12 Nov 08:09 - proof of Proposition 8.1 and Section 8.3 of the second paper read through
The proof of Proposition 8.1 ((8.13) to (8.26)) and Section 8.3 (Proposition 8.2, the initial preparation,
(8.27) to (8.37)) read on PDF pages 93 to 98; the explicit computations redone by hand and 25 of them by script
(pd08_sec8a_check.py, .out, all pass). No error found. PD08_CHECK.md has the section. Status of the row
unchanged: REPORTED_SOLVED, two papers, no error found in what was read; of the second paper Sections 4 to 7,
8.1, 8.2 and 8.3 are read (PDF pages 30 to 98); Section 3, the rest of Section 8 and Section 9 are unread
beyond the statements.
Open, in order of weight: 1. the rest of Section 8 from PDF page 99 (finite cascades, the shooting argument);
2. Section 3 (Lemma 3.1 and Proposition 3.4); 3. Section 9; 4. the authors' Julia notebooks for the first paper.
Read the PDF pages, not paper.txt.

## 12 Nov 08:18 - Section 8.4, Section 9 and Appendix A of the second paper read through
Lemma 8.3 (finite shooting), Section 9 (finite-depth solutions, compactness, mixed norms and the Lorentz
endpoint, the fixed observations that separate the branches, the proof of Theorem 1.1, Corollary 9.3) and
Appendix A (uniqueness at finite Lorentz index) read on PDF pages 99 to 110; the explicit computations redone by
hand and 55 of them by script (pd08_sec8c_check.py, .out, all pass). No error found. PD08_CHECK.md has the
section. Status of the row unchanged: REPORTED_SOLVED, two papers, no error found in what was read. Of the
second paper Sections 4 to 9 and Appendix A are read (PDF pages 30 to 110, the references start on page 110);
Sections 1 to 3 are read only for their statements.
Open, in order of weight: 1. Section 3 (Lemma 3.1 and Proposition 3.4: the exact reference solution, its
covariance (3.23) and the convergence of the reference solutions, which page 105 uses so that every branch has
the same reference limit); 2. the authors' Julia notebooks for the first paper; 3. a second reader for the
whole chain, since this reading is one reader's.
Read the PDF pages, not paper.txt.

## 12 Nov 08:37 - Section 3 of the second paper read through
Section 3 read on PDF pages 20 to 29; the explicit computations redone by hand and 38 of them by script
(pd08_sec3_check.py, .out, all pass): Lemma 3.1 (weighted shell bounds), the heat array and its coupling bounds
(3.8), Lemma 3.2 ((3.9), (3.10)), Lemma 3.3 (the multiplier Phi, (3.14) to (3.20), also computed for a concrete
array with R = 2), Proposition 3.4 ((3.25), (3.26), the contraction, the covariance (3.23), (3.24), (3.29)).
No error found. PD08_CHECK.md has the section. Read only, not redone: the smoothing step for (3.12), the
derivative estimates (3.22), the energy equalities through zero and the convergence of the linearised
propagators as the inner cutoff is removed.
The second paper is now read from Section 3 to the end (PDF pages 20 to 110) by one reader, with no error
found. Status of the row unchanged: REPORTED_SOLVED, two papers. This is one reader's reading and not a second
independent audit.
Open, in order of weight: 1. the authors' Julia notebooks for the first paper; 2. Sections 1 and 2 of the
second paper against what Sections 3 to 9 prove (statement of Theorem 1.1, the parameter list); 3. a second
reader for the whole chain.
Read the PDF pages, not paper.txt.

## 12 Nov 08:45 - The authors' code of the first paper cannot be rerun here
The README of the authors' repository (commit 615ee6f3, lit/repo_src) lists the requirements: Julia 1.11 or
later and "at least 800 GB RAM". The six notebooks run in order, later ones on the output of earlier ones:
1. get_bessel_zeros (the root file; compared here root by root, part C of PD08_CHECK.md);
2. selfsimilar_profile_verification, (4.44) to (4.46); 3. eigenpair_error_analysis, (4.47) to (4.51);
4. finite_rank_construction, (4.52) to (4.55); 5. selfsimilar_linear_operator_finite_rank, (4.56) to (4.60);
6. eigen_linear_operator_finite_rank, (4.61) to (4.63). The repository has no Manifest.toml at that commit
(the commit list shows it deleted), so the exact package versions are not pinned.
None of our machines has that memory, so the interval-arithmetic verification of (4.44) to (4.63) is not
rerun and will not be. What stands for the first paper is what PD08_CHECK.md records: the closing chain of
Section 4.5 recomputed from the printed constants (parts A, B) and the spectral basis matched against the
authors' root file (part C). The constants (4.44) to (4.63) themselves are taken from the paper.
The item "rerun the authors' Julia notebooks" is closed as not possible here. What could still be done on a
Mac mini without that memory: read src/Matrix_Func.jl (the quadrature error bounds) and src/My_Bessel.jl (the
supremum bounds) as mathematics, about 40 KB of source; whether notebooks 2 and 3 alone fit in a small machine
is not known from the README.
The weight of the row therefore rests on the second paper (arXiv 2611.06117), read here from Section 3 to the
end with no error found. Open: Sections 1 and 2 of the second paper (PDF pages 1 to 19) against what Sections
3 to 9 prove; a second reader.

## 12 Nov 08:56 - Sections 1 and 2 of the second paper compared with Sections 3 to 9
PDF pages 1 to 19 read by eye; 17 scripted checks (pd08_sec12_check.py), all pass. Theorem 1.1 as printed is
what Section 9 proves: (i) from (9.6), (9.8) and the Gaussian sums; (ii) from Propositions 9.1 and 9.2;
(iii) from (9.15) to (9.21); (iv) from (9.24) to (9.27), the compact observation being at the level n = 1,
time T_1 = l_1^2 t_p inside (0, T_0), with T = T_0. The parameters of Section 2 are those of Section 8.
No error found. The second paper is now read whole, PDF pages 1 to 110, by one reader: 251 scripted
checks in all. Read only, not redone (unchanged): the smoothing step for (3.12), the derivative estimates
(3.22), the energy equalities through zero, the convergence of the linearised propagators as the inner cutoff
is removed. Open: a second reader. Row status unchanged: REPORTED_SOLVED.
