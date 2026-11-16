# Checks of the 2025-2026 claimed solutions of well-known open problems, 12 November 2026

Between mid-2025 and November 2026 preprints appeared claiming solutions of a number of long-standing problems that sat
on our list of problems to attack. Before spending effort on any of them we read the claimed proofs and tested what
could be put on a computer. This folder holds those checks, one sub-folder per row of the list: the reading notes
(`*_CHECK.md`), the scripts that test the statements, and the outputs of those scripts.

Every result recorded here belongs to the authors named below. The checks are ours, and each says plainly which parts
were read line by line, which were tested numerically, and which were not read at all. A check that passes is a
reason to stop treating the row as open, not a referee's verdict on the paper. Several sources are unrefereed
preprints, and several are credited by their authors to language models; that is stated where it applies.

Copies of the papers themselves, the search results used to look for follow-up work, and the coordinator's working
notes are not included. Line numbers such as `paper_c.txt, lines 225-719` refer to a plain-text extraction of the
paper named at the top of the same file.

## The rows

| folder | problem | source checked | what was found |
|---|---|---|---|
| `ag05-jacobian` | Jacobian conjecture, dimension 3 | L. Alpöge's counterexample (July 2026), in the form of A. van den Essen, arXiv 2609.17795; M. de Bondt, arXiv 2610.24889 | the map recomputed exactly: constant Jacobian determinant and two distinct points with the same image |
| `ag10-cubic-fourfold` | irrationality of the very general cubic fourfold | Katzarkov, Kontsevich, Pantev, Yu, arXiv 2508.05105 | solved (Theorem 6.8 there); a 2026 claim about special cubic fourfolds is recorded as unverified |
| `al04-kaplansky` | Kaplansky's zero-divisor conjecture, positive characteristic | S. V. Ivanov, arXiv 2610.17662; N. Mghirbi and S. Douglas, arXiv 2611.04599; an OpenAI preprint for p = 2 (not read) | the finite parts recomputed; what each preprint proves is separated from what it takes from the unread source |
| `an07-sendov` | Sendov's conjecture | L. Mazur (computer-assisted, Lean); T. Tao's digest and Lean formalisation; S. An, arXiv 2609.04246; earlier Brown-Xiang, Tao (Acta Math. 2022), Zhang | the reduction read; the last scalar inequality tested on a fine grid and on random polynomials; the Lean code and An's certificate were not run |
| `an09-fuglede` | Fuglede's conjecture in dimension two | Tao Zhang, arXiv 2607.15632 | the two explicit 60-point sets in Z60 x Z12 checked: one tiles without a spectrum, the other has a spectrum and does not tile |
| `co06-cdc` | cycle double cover conjecture | J. Geelen's exposition, arXiv 2607.15399, of the proof credited to OpenAI; S. Oum, arXiv 2607.16356 | the linear-algebra proof checked by hand |
| `co08-erdos-sos` | Erdős-Sós conjecture | D. R. Wood, arXiv 2609.17877, of the counting proof credited to GPT-6 Astra; B. Frederickson, arXiv 2609.21159 | the counting proof checked by hand; the cited Lean formalisation (T. Adamczewski) not examined |
| `dg06-caratheodory` | Carathéodory and Loewner umbilic conjectures | announced by L. Alpöge; N. Ando and M. Umehara, arXiv 2610.34036 | the smooth counterexample checked |
| `dg08-cartan-hadamard` | Cartan-Hadamard isoperimetric conjecture | Chen, Ghomi, Wang (arXiv 2609.11005, 2609.20517); Agnoletto, Da Silva, Nardulli, Resende (arXiv 2609.17093, 2610.37817); Case-Mengesha; Wheeler | the key inequality and the profile step checked; minimiser regularity and the rigidity arguments not read |
| `dg09-stable-bernstein` | stable Bernstein problem in R^7 | Hong, Li, Wang, arXiv 2609.15720 | the exact arithmetic of Section 13 checked (8 checks); the analytic proof, about 70 pages, and the certificates not read, so the row is marked reported solved |
| `ge07-sofa` | moving sofa problem | J. Baek, arXiv 2411.19826 | about half of the 119 pages read with no error found; every statement about Gerver's sofa and the bound Q that could be computed came out as stated |
| `it01-mds` | MDS conjecture, even characteristic | Bocong Chen and Jing Huang, arXiv 2610.28208 | Section 5 checked in full |
| `lo01-vaught` | Vaught's conjecture | N. L. Ackerman, C. E. Freer, R. W. Knight, arXiv 2610.15217, with its public Lean repository | what the counterexample refutes, and what the Lean main theorem states, compared |
| `lo05-h10-over-q` | Hilbert's tenth problem over Q | OpenAI preprint in github.com/openai/math | Sections 2 to 6 read line by line, with the cited inputs listed; claimed, not yet confirmed independently |
| `nt01-quasi-rh` | the Riemann hypothesis row | the OpenAI zero-free-region preprint of 5 Oct 2026 (Hecke L-functions over Q(sqrt -3)) | Lemma 4.1 tested numerically; the row itself stays open, since no source claims the Riemann hypothesis |
| `nt02-landau-siegel` | Landau-Siegel zeros | OpenAI preprint of 1 Oct 2026; B. Kerr, arXiv 2610.21099; W. Banks, arXiv 2610.15483; Guo, arXiv 2610.30476 | two proofs read in full; the report holds up |
| `pd08-leray-hopf` | non-uniqueness of Leray-Hopf solutions of Navier-Stokes | T. Y. Hou, Y. Wang, C. Yang, arXiv 2509.25116; T. Y. Hou, Qin, Song, Zhang, arXiv 2611.06117 | claimed twice, not confirmed by an independent group; the closing chain of Section 4.5 of the first paper recomputed (19 of 20 steps reproduce; one slip in the third digit, and two bounds that should carry a square root of a Gram-matrix norm), and further sections checked by the `pd08_sec*_check.py` scripts |
| `t042-aaronson-ambainis` | Aaronson-Ambainis conjecture | Huffstutler, Miloschewsky, Podder, arXiv 2611.12795; D. Turturean, arXiv 2611.09773 (not read) | the short proof read in full |
| `t115-gotsman-linial` | Gotsman-Linial bound for polynomial threshold functions | OpenAI preprint of 25 Sep 2026; Chapman (2018) for the failure of the exact form | the asymptotic bound I(f) <= 8 d sqrt(n) read in full |
| `t188-odlyzko-poonen` | irreducibility of random 0-1 polynomials | C. Kogler, arXiv 2609.26771 (proofs credited to GPT-6 Astra, with Lean); Konyagin; Breuillard and Varjú | the elementary core checked; the Lean code not inspected |
| `t189-fpras-matchings` | FPRAS for perfect matchings in general graphs | OpenAI preprint of 23 Sep 2026 and an independent second proof | all but one Poincaré inequality verified by hand; that one tested on K_6 and K_8 |
| `t197-free-group-factors` | free group factor isomorphism problem | OpenAI preprint of 23 Sep 2026 and a later self-contained proof by a specialist | read in full, every step checked, the combinatorial core tested |
| `t283-lowdeg` | the low-degree conjecture | S. Mao, arXiv 2607.20318 | refutes the polynomial-time, graph-valued form at small noise only; the other forms stay open |

## Why this is useful

A list of open problems goes stale quickly once machine-assisted proofs start to appear. Each check here took a few
hours and ended in one of three ways: the row leaves the list, the row stays with a narrower statement, or the claim
is recorded as unconfirmed with the exact part that was not checked. The scripts are short and can be rerun by anyone
who wants to test the same statements.

## Credit

The problems are due to the people whose names they carry. The solutions are due to the authors in the table and to
the earlier work they build on, which each check cites. Several of the sources state that a language model produced
the first proof (OpenAI's models, GPT-6 Astra); the human authors who wrote, checked or formalised those proofs are
named in the table. The checks themselves were done by a language-model agent and have not been refereed.
