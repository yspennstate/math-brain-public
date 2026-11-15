# P7 outline: linear monotone DNFs on at most eight variables, and where the local certificates stop

Source: FEIB23 (codex/workers/FEIB23: PROOFS.md A-G, REPORT.md, RESULTS.md, census*.json, certify.cpp, labeled_check.cpp,
structured.cpp, TD_*.json), refereed by FEIB28 (A-G confirmed); census rerun independently 11 Nov (CENSUS_CHECK.md).

Working title: "The Fourier entropy of linear monotone DNFs on few variables"

1. Introduction. FEI; erasure ratio E_i/Inf_i (P1-P5 notation); linear = any two terms share at most one variable
   (P6 = uniform width, bounded degree, ratio 2+o(1)). Here: no width/degree assumption.
   Theorem 1 (census): over all linear monotone DNFs with at most 8 relevant variables,
     max H/I in [3.88910541981418, 3.88910541981709], unique attainer: OR of four variables with the 4-cycle DNF on four
       others (terms x1, x2, x3, x4, y1y2, y2y3, y3y4, y4y1);
     max min_i E_i/Inf_i in [3.30470132244542, 3.30470132245649], unique attainer: two disjoint 4-cycle DNFs.
     table of maxima by n = 1..8 (both ratios; counts 1 2 5 16 72 592 10808 552251; labeled 18,785,639,553 at n=8).
   Theorem 2 (LOCAL): a term t of width L+1, L >= 3, whose every variable has load lambda_j <= (1+1/(64L^2))2^-L gives
     E_i < 6 Inf_i at every i in t. Loads elsewhere irrelevant.
   Theorem 3 (BIAS): H/I <= 2[n/r + 1 + log2(e)/r], r = log2(1/min(P[f=1],P[f=-1])), any Boolean f.
   Proposition 4 (MIX): mixed-width version of P6's certificate (state, prove the differences only; cite P6).
   Theorem 5 (obstruction): transversal designs TD(w,Q), Q = 2^k, w = k + 2 ceil(log2 k) + 1: P2's width bound, the
     relative-influence bound, MIX for every threshold choice, LOCAL and BIAS all fail, while P[F=0] -> 0
     subexponentially. Numerics TD(3,3),(3,5),(3,7),(4,5),(5,5): actual ratios stay small (H/I 3.88 at (5,5)).
2. Notation and the relative-influence bound (REL): E_i/delta <= 2|E f| + log2(e v/delta) (sharper than P2 Lemma var).
3. Census: enumeration by widths downward with exact canonical forms (FEIB23 E); completeness by two labeled counts
   (pair-clique recursion vs orbit-stabilizer); certified logs (integer series, 2^-52, outward rounding); independent
   recheck (our indep_census_check.c). Remark: tree erasure averages for the two attainers (1.952, 2.092).
4. LOCAL proof (PROOFS C).
5. BIAS proof (PROOFS D) incl. elementary edge-isoperimetry.
6. MIX (PROOFS B) as a generalization of P6's Lemmas A, h, N.
7. Obstruction (PROOFS F) + numerics table from TD_*.json.
8. Open scope (PROOFS G, short).
Code repo: fei-linear-dnf-census: census.cpp, labeled_check.cpp, certify.cpp, log_intervals.py, structured.cpp,
  indep_census_check.c, outputs (census{1..8}.json, certified, labeled_check, out_n*.json, TD_*.json);
  census8.families is 21 MB -> include gzipped (about 4-5 MB) or as release asset.
Check before writing: literature on exhaustive FEI computations for small n (O'Donnell's FEI constant search? "FEI n<=..."
  computational verification), and whether BIAS is known (H <= ... for small-bias / sparse functions).
Referee: an agent again (independent code). Funding block word for word from P4/P5.

NOTE 11 Nov 02:0x: TD(3,7) (n=21, 49 terms of width 3, degree 7) has H/I = 4.1346 > the 8-variable maximum 3.8891, and
TD(4,5) 3.9024, TD(5,5) 3.8800, TD(3,5) 3.8798. So the census maxima are NOT the class suprema; say so in the intro and
put the TD table next to the census table. min E/Inf on TD stays 2.10-2.72; whole-term tree averages 1.69-2.32.
Literature already checked by FEIB23 (LITERATURE.md, 10 Nov): no FEI theorem for linear monotone DNFs; Paraashar-Saurabh
arXiv 2611.06451 (4 Nov 2026), Lecomte-Tan 2109.04525, ACKSW, WWW, Shalev, OT13, Han, GMP 2606.00246. Still to check:
exhaustive small-n FEI computations; whether BIAS is folklore.
Lit 11 Nov 02:0x: exhaustive search over all Boolean functions on n <= 5 variables exists for the MIN-entropy variant
(Biswas-Sarkar arXiv 2212.07713: max FMEI ratio 16/7 at n <= 5; 128/45 by a 30-variable construction). Cite it as the
nearest computation. BIAS: elementary (edge isoperimetry + entropy of a sparse spectrum); present as a lemma, no novelty
claim.
