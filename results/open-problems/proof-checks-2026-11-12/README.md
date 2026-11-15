# Checks of reported solutions, 11-13 November 2026

Since late 2024, and above all between July and October 2026, a number of well-known open problems were reported
solved, many of them in preprints
written with or by AI systems (the OpenAI mathematics release at github.com/openai/math, and preprints by human
authors that present or extend such proofs). Before we take a row off our list of problems to attack, we read the
reported solution and test what can be tested. This folder holds those checks, one folder per row, with the
working left in: the reading notes, the scripts that recompute finite cases or constants, their output, and in some
folders a referee report by a second model.

Each check says what was read in full, what was read in part, and what was taken on trust. A check is not a
referee's report on the paper and does not replace one; where it says a proof "holds", it means that the parts read
contain no error we could find. Copies of the papers themselves are not included; each check names the paper by
author, title and arXiv number or repository commit. The few files copied from OpenAI's release are listed in
`THIRD_PARTY.md` with their license.

## The checks

Each folder name ends with the date of its check (for example `an07_sendov_2026_11_12`).

| folder | problem | reported by | what the check found |
|---|---|---|---|
| `ag05_jacobian` | Jacobian conjecture | A. van den Essen (arXiv 2609.17795); M. de Bondt (arXiv 2610.24889) | the three-dimensional counterexample recomputed |
| `ag10_cubic_fourfold` | irrationality of the very general cubic fourfold | L. Katzarkov, M. Kontsevich, T. Pantev, T. Yu (2025) | solved; a stronger 2026 claim on special cubic fourfolds is unverified |
| `al04_kaplansky` | Kaplansky's zero-divisor conjecture in positive characteristic | S. V. Ivanov (arXiv 2610.17662) and a second preprint (arXiv 2611.04599) | what the preprints prove, with the finite parts recomputed |
| `an07_sendov` | Sendov's conjecture | L. Mazur (computer-assisted proof, verified in Lean); exposition by T. Tao | reported proved for every degree; the reduction was checked and tested numerically; the Lean proof and the certificate were not run here |
| `an09_fuglede` | Fuglede's conjecture in dimension two | Tao Zhang (arXiv 2607.15632) | the finite sets of the preprint checked |
| `co06_cdc` | cycle double cover conjecture | proof credited to OpenAI; written up by J. Geelen (arXiv 2607.15399), exposition by S. Oum (arXiv 2607.16356) | the linear-algebra proof read and checked |
| `co08_erdos_sos` | Erdős–Sós conjecture | proof credited to an OpenAI model; written up by D. R. Wood (arXiv 2609.17877); second proof by B. Frederickson (arXiv 2609.21159) | the counting proof read and checked |
| `dg06_caratheodory` | Carathéodory and Loewner conjectures | announced by L. Alpöge; construction of N. Ando and M. Umehara (arXiv 2610.34036) | the smooth counterexample checked |
| `dg08_cartan_hadamard` | Cartan–Hadamard conjecture | two 2026 preprints, by routes that share only Kleiner's confined-profile argument | the key inequality checked numerically; regularity and rigidity not read; all sources unrefereed |
| `dg09_stable_bernstein` | stable Bernstein problem in R^7 | Hong, Li, Wang (arXiv 2609.15720) | claimed solved, not confirmed; the exact checks of Section 13 pass, most of the 85 pages and the authors' Lean files were not checked |
| `ge07_sofa` | moving sofa problem | J. Baek (arXiv 2411.19826) | read in part; no error found in the parts read; computable statements tested |
| `it01_mds` | MDS conjecture in even characteristic | Bocong Chen, Jing Huang (arXiv 2610.28208) | the last section checked; 90 cases computed |
| `lo01_vaught` | Vaught's conjecture | N. L. Ackerman, C. E. Freer, R. W. Knight (arXiv 2610.15217) | what the counterexample refutes, and what its Lean theorem states |
| `lo05_h10_over_q` | Hilbert's tenth problem over Q | OpenAI preprint (openai/math) | claimed solved negatively; not confirmed independently |
| `nt01_quasi_rh` | zero-free regions (the Riemann hypothesis row) | OpenAI preprints of October 2026 (openai/math) | provisional; the preprints do not claim the Riemann hypothesis and the row stays |
| `nt02_landau_siegel` | non-existence of Landau–Siegel zeros | OpenAI preprint (openai/math) and a second proof | two proofs read in full; no error found; the Lean files were not compiled here |
| `pd08_leray_hopf` | non-uniqueness of Leray–Hopf solutions of 3D Navier–Stokes | T. Y. Hou, Y. Wang, C. Yang (arXiv 2509.25116) and a second paper from the same group | claimed solved twice, computer-assisted; not confirmed by others |
| `t042_aaronson_ambainis` | Aaronson–Ambainis conjecture | a 2026 short proof, named in the check | checked by hand and by computer, given two quoted results |
| `t115_gotsman_linial` | Gotsman–Linial bound for polynomial threshold functions | OpenAI preprint (openai/math, 25 Sep 2026) | solved in its asymptotic form; read in full |
| `t188_odlyzko_poonen` | Odlyzko–Poonen conjecture | proof using results of Breuillard–Varjú and Dobrowolski | the elementary core checked by hand and computer |
| `t189_fpras_matchings` | FPRAS for perfect matchings in general graphs | two written proofs, the second by independent authors | checked except one Poincaré inequality, which was tested on K_6 and K_8 |
| `t197_free_group_factors` | free group factor isomorphism problem | a 23-page proof, and a later self-contained proof by a specialist | read in full; no error found |
| `t249_crossover` | the NTK between the ordered phase and the critical line (our own derivation) | our agents | derived two ways and checked numerically; an independent referee report then judged the uniform proof wrong |
| `t283_lowdeg` | low-degree conjecture | S. Mao (arXiv 2607.20318) | what the preprint proves and what remains |
| `t104_alon` | a row of our list (T104) attacked by our agents | our agents | a short note with search code; independent referee passes judged the main inequality sound for every n >= 14 after small repairs, and found the note's claim from n = 10 false and some side statements false |
| `top200_vet` | the vetting of our list of 200 open problems | our coordinating agent | the scripts and tables used to check each row's status in the literature |

## Credit

The solutions recorded here belong to their authors, named above and in each check with the paper they wrote. Where
a proof is credited to an AI system, the credit is as the paper or the repository gives it, and the human authors
who wrote up, checked or extended it are named. Our part is only the reading and the tests in these folders. The
checks were written by a coordinating language-model agent, with referee passes by OpenAI Codex workers; none has
been reviewed by a person.
