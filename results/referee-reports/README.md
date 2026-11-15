# Referee reports and attempts, 12-15 November 2026

This folder holds the working record of four days of research on open problems in probability and combinatorics:
the brief given to each attempt, the attempt itself (notes, proofs, code, data and run logs), the independent
referee reports written on it, and, where a result survived, the paper drafted from it and the audit of that paper.
Nothing here has been reviewed by a person. It is published so that the method can be inspected end to end, including
the attempts that failed and the corrections the referees forced.

## How a problem moves through the folder

1. **Brief** (`PROMPT.md` in an attempt folder). A coordinating agent states the problem as it appears in the source,
   names the source, and lists what is already known and what would count as progress.
2. **Attempt** (suffix `A`, further attempts `B`, `C`, ...). A worker model reads the literature, works the problem,
   writes code for the computations and records everything in `LOG.md` and `REPORT.md`. Data and scripts sit beside
   the report so each number can be regenerated.
3. **Independent referee** (suffix `AR`). A second model that did not write the attempt reads it against the source
   and rules on each claim: sound, gap or error, with line references and a corrected statement where one exists.
4. **Paper** (suffix `P`) and **paper audit** (suffix `PR`). A result that holds up is written as a paper; a further
   referee audits the manuscript as a referee for a probability journal would, with the cited sources at hand.
5. **Checks after posting** (`*_posted_referee`, `RG*AR`, `*_check`). Posted papers get a fresh referee pass and a
   first reader's report; repeated attempts on one problem (C0033 D-F) each get their own re-check.

Problem identifiers (C0033, D0040, P0347, ...) are the numbers of the problem list the attempts were drawn from; each
brief names the published source of its problem. Folders without an identifier are named by topic.

## Credit

The problems and almost all of the mathematics these attempts build on are the work of the authors cited in each
brief, report and paper; the bibliographies there say what was known before and which ideas are reused. Where an
attempt found that a problem had already been settled in print (for example F0084, D0043), the report says so and
credits the paper that settled it. The attempts were written by Codex worker models (gpt-6.1-sol) under briefs from
coordinating agents; the referee reports and audits were written by separate model instances that did not see the
attempt being written. Copies of third-party papers that were fetched during the work are not redistributed here;
the reports cite them instead.

## What is new in the method

The record shows a loop rather than a single answer: brief, attempt, code and data, an independent referee who did
not write the attempt, then a correction or a retraction. The referee logs are the useful part. They caught literal
misstatements of sources, gaps in infinite constructions, and results that were already in the literature, and they
are why several attempts end in a narrower theorem than the one first claimed. Anyone running a similar programme
can reuse the brief format, the referee rubric (sound / gap / error per claim, with line numbers) and the habit of
keeping the computation next to the claim it supports.

## Index

| Day | Folder | Kind | Title |
|---|---|---|---|
| 2026-11-12 | [AFS](2026-11-12/AFS/) | referee check | Line-numbered findings and corrected text |
| 2026-11-12 | [ANTS](2026-11-12/ANTS/) | referee check |  |
| 2026-11-12 | [ARC](2026-11-12/ARC/) | referee check |  |
| 2026-11-12 | [CHORD](2026-11-12/CHORD/) | referee check |  |
| 2026-11-12 | [COMB](2026-11-12/COMB/) | referee check |  |
| 2026-11-12 | [COVER](2026-11-12/COVER/) | referee check |  |
| 2026-11-12 | [E0081A](2026-11-12/E0081A/) | attempt | First-passage pattern waiting time |
| 2026-11-12 | [E0081AR](2026-11-12/E0081AR/) | independent referee log | Independent referee log |
| 2026-11-12 | [F0127A](2026-11-12/F0127A/) | attempt | Fast mixing does not force mean-field coalescence under uniform stationarity |
| 2026-11-12 | [FORKCOMB](2026-11-12/FORKCOMB/) | referee check | Fork comb, K(2N+4) >= N+2: independent check of section 5 of the K5 run |
| 2026-11-12 | [K5](2026-11-12/K5/) | referee check |  |
| 2026-11-12 | [K5P](2026-11-12/K5P/) | referee check |  |
| 2026-11-12 | [K6P](2026-11-12/K6P/) | referee check | Q2 research log |
| 2026-11-12 | [K7P](2026-11-12/K7P/) | referee check |  |
| 2026-11-12 | [LEA](2026-11-12/LEA/) | referee check | Findings and corrected text |
| 2026-11-12 | [LUMP](2026-11-12/LUMP/) | referee check |  |
| 2026-11-12 | [LUMP2](2026-11-12/LUMP2/) | referee check | Errors requiring correction |
| 2026-11-12 | [LUMP_AUDIT](2026-11-12/LUMP_AUDIT/) | referee check | Second check of the lumping results of 12 November |
| 2026-11-12 | [P0032](2026-11-12/P0032/) | referee check |  |
| 2026-11-12 | [P0033](2026-11-12/P0033/) | referee check | Referee report on PAPER.tex |
| 2026-11-12 | [P0065](2026-11-12/P0065/) | referee check | Independent referee report |
| 2026-11-12 | [P0072](2026-11-12/P0072/) | referee check | Quoted Conjecture (`conj`, lines 56–59) |
| 2026-11-12 | [P0081](2026-11-12/P0081/) | referee check |  |
| 2026-11-12 | [P0089](2026-11-12/P0089/) | referee check |  |
| 2026-11-12 | [P0178](2026-11-12/P0178/) | referee check | Independent referee report |
| 2026-11-12 | [P0209](2026-11-12/P0209/) | referee check |  |
| 2026-11-12 | [P0211](2026-11-12/P0211/) | referee check | Independent referee report |
| 2026-11-12 | [P0220](2026-11-12/P0220/) | referee check |  |
| 2026-11-12 | [P0243](2026-11-12/P0243/) | referee check | Independent referee report |
| 2026-11-12 | [P0253](2026-11-12/P0253/) | referee check | Referee report on PAPER.tex |
| 2026-11-12 | [P0341](2026-11-12/P0341/) | referee check |  |
| 2026-11-12 | [P0347](2026-11-12/P0347/) | referee check | Balance indices of the critical beta-splitting tree |
| 2026-11-12 | [P0347L](2026-11-12/P0347L/) | attempt | The centered Sackin limit for the critical beta-splitting tree |
| 2026-11-12 | [P0347LR](2026-11-12/P0347LR/) | referee log | Independent referee report |
| 2026-11-12 | [P0347R](2026-11-12/P0347R/) | referee log | Independent referee report |
| 2026-11-12 | [P0456](2026-11-12/P0456/) | referee check |  |
| 2026-11-12 | [P0458](2026-11-12/P0458/) | referee check |  |
| 2026-11-12 | [VARTH](2026-11-12/VARTH/) | referee check |  |
| 2026-11-13 | [C0002A](2026-11-13/C0002A/) | attempt | C0002: intermediate level-set volume of the two-dimensional DGFF |
| 2026-11-13 | [C0021A](2026-11-13/C0021A/) | attempt | Source and literature result |
| 2026-11-13 | [C0033A](2026-11-13/C0033A/) | attempt | Open problem C0033: concavity of the entropy of determinantal measures in the kernel |
| 2026-11-13 | [C0033B](2026-11-13/C0033B/) | attempt | Open problem C0033: concavity of the entropy of determinantal measures in the kernel |
| 2026-11-13 | [C0033C](2026-11-13/C0033C/) | attempt | Open problem C0033, third attempt: entropy concavity of determinantal point processes on three points and in rank two |
| 2026-11-13 | [C0034A](2026-11-13/C0034A/) | attempt | C0034: orthogonal union couplings of projection determinantal measures |
| 2026-11-13 | [C0039R](2026-11-13/C0039R/) | referee log |  |
| 2026-11-13 | [C0057A](2026-11-13/C0057A/) | attempt | C0057: exhaustion of critical Boltzmann maps |
| 2026-11-13 | [C0059A](2026-11-13/C0059A/) | attempt | C0059: random walk on the dual of an infinite Boltzmann map |
| 2026-11-13 | [C0083A](2026-11-13/C0083A/) | attempt | C0083: Hamming-graph critical-point expansion |
| 2026-11-13 | [C0092A](2026-11-13/C0092A/) | attempt | C0092: sharpness of the random-cluster transition below one |
| 2026-11-13 | [C0097A](2026-11-13/C0097A/) | attempt | C0097: the inverse-dimension expansion of the SAW connective constant |
| 2026-11-13 | [C0101A](2026-11-13/C0101A/) | attempt | C0101: a counterexample for literal Loewner maximality |
| 2026-11-13 | [C0101AR](2026-11-13/C0101AR/) | independent referee log | C0101 independent referee log |
| 2026-11-13 | [C0109A](2026-11-13/C0109A/) | attempt | C0109: quantitative circular law with a finite (2+epsilon) moment |
| 2026-11-13 | [C0113A](2026-11-13/C0113A/) | attempt | C0113: connectivity of the Poisson Euclidean minimal spanning forest |
| 2026-11-13 | [C0119A](2026-11-13/C0119A/) | attempt | C0119: higher-dimensional directed-polymer chaos |
| 2026-11-13 | [C0122A](2026-11-13/C0122A/) | attempt | C0122 work log |
| 2026-11-13 | [C0130A](2026-11-13/C0130A/) | attempt | C0130: escape probability of a one-dimensional excited random walk |
| 2026-11-13 | [C0132A](2026-11-13/C0132A/) | attempt | Open problem C0132: transience and recurrence of the balanced excited random walks M(d1,d2) |
| 2026-11-13 | [C0133A](2026-11-13/C0133A/) | attempt | C0133: zero speed on the event of non-transience |
| 2026-11-13 | [C0133AR](2026-11-13/C0133AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [C0149A](2026-11-13/C0149A/) | attempt | C0149: Bowen's essential-expansion conjecture |
| 2026-11-13 | [C0151A](2026-11-13/C0151A/) | attempt | C0151: independent-set densities on random regular graphs and FIID on trees |
| 2026-11-13 | [C0153A](2026-11-13/C0153A/) | attempt | C0153 work log |
| 2026-11-13 | [C0159A](2026-11-13/C0159A/) | attempt | C0159 work log |
| 2026-11-13 | [C0159AR](2026-11-13/C0159AR/) | independent referee log | Independent referee log: C0159 |
| 2026-11-13 | [D0004A](2026-11-13/D0004A/) | attempt | Open problem D0004: when do the law-determined-norm inequalities imply complete mixability? |
| 2026-11-13 | [D0004AR](2026-11-13/D0004AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [D0007A](2026-11-13/D0007A/) | attempt | Open problem D0007: is every absolutely continuous law on a bounded interval n-CM for all large n? |
| 2026-11-13 | [D0007AR](2026-11-13/D0007AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [D0017A](2026-11-13/D0017A/) | attempt | D0017 — zero-dimensional double-time fibers of Brownian-sheet slices |
| 2026-11-13 | [D0017AR](2026-11-13/D0017AR/) | independent referee log | Errors, gaps, and qualifications |
| 2026-11-13 | [D0023A](2026-11-13/D0023A/) | attempt | D0023: concentration at slow sites in the disordered zero-range process |
| 2026-11-13 | [D0025A](2026-11-13/D0025A/) | attempt | D0025: a plateau for site-disordered finite-capacity exclusion |
| 2026-11-13 | [D0025AR](2026-11-13/D0025AR/) | independent referee log | Errors or gaps requiring correction |
| 2026-11-13 | [D0025PR](2026-11-13/D0025PR/) | referee audit of a paper | Referee audit log |
| 2026-11-13 | [D0026A](2026-11-13/D0026A/) | attempt | D0026: convergence of one-dimensional FA-1f |
| 2026-11-13 | [D0026AR](2026-11-13/D0026AR/) | independent referee log | Independent referee log: D0026 |
| 2026-11-13 | [D0027A](2026-11-13/D0027A/) | attempt | D0027: exponential relaxation for one-dimensional FA-1f |
| 2026-11-13 | [D0027AR](2026-11-13/D0027AR/) | independent referee log | Errors, gaps, and corrections |
| 2026-11-13 | [D0028A](2026-11-13/D0028A/) | attempt | D0028: stationary measures of kinetically constrained spin models |
| 2026-11-13 | [D0028AR](2026-11-13/D0028AR/) | independent referee log | D0028 independent referee log |
| 2026-11-13 | [D0031A](2026-11-13/D0031A/) | attempt | D0031: finite-state rho-mixing and bilateral determinism |
| 2026-11-13 | [D0034A](2026-11-13/D0034A/) | attempt | D0034: ψ-mixing and Harris-chain representations |
| 2026-11-13 | [D0036A](2026-11-13/D0036A/) | attempt | Definitions and the source |
| 2026-11-13 | [D0036AR](2026-11-13/D0036AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [D0037A](2026-11-13/D0037A/) | attempt | D0037: spectral density and Gaussian interlaced mixing |
| 2026-11-13 | [D0040A](2026-11-13/D0040A/) | attempt | D0040: nested beta ensembles |
| 2026-11-13 | [D0040AR](2026-11-13/D0040AR/) | independent referee log |  |
| 2026-11-13 | [D0040P](2026-11-13/D0040P/) | paper draft |  |
| 2026-11-13 | [D0040PR](2026-11-13/D0040PR/) | referee audit of a paper | Referee log |
| 2026-11-13 | [D0041A](2026-11-13/D0041A/) | attempt |  |
| 2026-11-13 | [D0043A](2026-11-13/D0043A/) | attempt | D0043: the displayed exotic-edge operator is already disproved |
| 2026-11-13 | [D0046A](2026-11-13/D0046A/) | attempt | D0046: dynamics of random operator limits |
| 2026-11-13 | [D0046AR](2026-11-13/D0046AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [D0051A](2026-11-13/D0051A/) | attempt | D0051: thickness on LQG geodesics |
| 2026-11-13 | [D0056A](2026-11-13/D0056A/) | attempt | Open problem D0056: the constant in the survival probability of the critical Derrida-Retaux recursion |
| 2026-11-13 | [D0056AR](2026-11-13/D0056AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [D0058A](2026-11-13/D0058A/) | attempt | D0058 work log |
| 2026-11-13 | [D0058AR](2026-11-13/D0058AR/) | independent referee log | Independent D0058 referee log |
| 2026-11-13 | [D0058P](2026-11-13/D0058P/) | paper draft |  |
| 2026-11-13 | [D0058PR](2026-11-13/D0058PR/) | referee audit of a paper | Referee audit log |
| 2026-11-13 | [D0064A](2026-11-13/D0064A/) | attempt | D0064: solutions of the continuous star-equation |
| 2026-11-13 | [D0065A](2026-11-13/D0065A/) | attempt | D0065 work log |
| 2026-11-13 | [D0065AR](2026-11-13/D0065AR/) | independent referee log | D0065 independent referee log |
| 2026-11-13 | [D0068A](2026-11-13/D0068A/) | attempt | D0068: the ordinary connective-constant limit on a Bernoulli cluster |
| 2026-11-13 | [D0070A](2026-11-13/D0070A/) | attempt | D0070: the minimum connective constant at fixed degree |
| 2026-11-13 | [D0071A](2026-11-13/D0071A/) | attempt | D0071 — the golden-mean lower bound for cubic transitive graphs |
| 2026-11-13 | [D0073A](2026-11-13/D0073A/) | attempt | D0073: strict decrease of connective constants under free quotients |
| 2026-11-13 | [D0093A](2026-11-13/D0093A/) | attempt | D0093: topplings in the fast phase of activated random walk on a cycle |
| 2026-11-13 | [E0018A](2026-11-13/E0018A/) | attempt | E0018: an explicit pair with at least two instability intervals |
| 2026-11-13 | [E0018AR](2026-11-13/E0018AR/) | independent referee log | Source wording and ruling |
| 2026-11-13 | [E0022A](2026-11-13/E0022A/) | attempt | E0022 work log |
| 2026-11-13 | [E0027A](2026-11-13/E0027A/) | attempt | E0027 work log |
| 2026-11-13 | [E0030A](2026-11-13/E0030A/) | attempt | E0030: variance of the optimal Euclidean TSP |
| 2026-11-13 | [E0031A](2026-11-13/E0031A/) | attempt | E0031: variance of one-colour Euclidean minimum matching |
| 2026-11-13 | [E0053A](2026-11-13/E0053A/) | attempt | E0053: maximum and minimum bisections of random regular graphs |
| 2026-11-13 | [E0055A](2026-11-13/E0055A/) | attempt | E0055: projected power iteration for angular synchronization |
| 2026-11-13 | [E0057A](2026-11-13/E0057A/) | attempt | E0057: consistency and sample complexity of multireference alignment |
| 2026-11-13 | [E0065A](2026-11-13/E0065A/) | attempt | E0065: uniform positivity and regularity of quadratic stochastic operators |
| 2026-11-13 | [E0065AR](2026-11-13/E0065AR/) | independent referee log | Independent referee log: E0065 |
| 2026-11-13 | [E0066A](2026-11-13/E0066A/) | attempt | Open problem E0066: trajectories of bistochastic (doubly stochastic) quadratic stochastic operators |
| 2026-11-13 | [E0082A](2026-11-13/E0082A/) | attempt | E0082: bridge constants and the first-passage obstruction |
| 2026-11-13 | [E0082AR](2026-11-13/E0082AR/) | independent referee log | Source, definitions, and exact scope |
| 2026-11-13 | [E0086A](2026-11-13/E0086A/) | attempt | E0086: source audit and annulus local times |
| 2026-11-13 | [E0093A](2026-11-13/E0093A/) | attempt | E0093: random generating sets and mixing on finite groups |
| 2026-11-13 | [E0094A](2026-11-13/E0094A/) | attempt | Open problems E0094 and E0095: which generator or edge to add to speed up a random walk |
| 2026-11-13 | [E0094AR](2026-11-13/E0094AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [E0095A](2026-11-13/E0095A/) | attempt | E0095: adding an edge or a perfect matching |
| 2026-11-13 | [E0098A](2026-11-13/E0098A/) | attempt | E0098 work log |
| 2026-11-13 | [E0098AR](2026-11-13/E0098AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [F0006A](2026-11-13/F0006A/) | attempt | F0006 research log |
| 2026-11-13 | [F0017A](2026-11-13/F0017A/) | attempt | F0017: diagonal sign resilience of a random sign matrix |
| 2026-11-13 | [F0083A](2026-11-13/F0083A/) | attempt | F0083: deterministic nonuniqueness of stable allocations |
| 2026-11-13 | [F0083AR](2026-11-13/F0083AR/) | independent referee log | Independent referee log — F0083 |
| 2026-11-13 | [F0084A](2026-11-13/F0084A/) | attempt | F0084: a power-law upper bound was published in 2009 |
| 2026-11-13 | [F0085A](2026-11-13/F0085A/) | attempt | F0085: stable Poisson allocation and percolation |
| 2026-11-13 | [F0096A](2026-11-13/F0096A/) | attempt | Open problem F0096: Hamiltonicity of G_{n,cn;3} for c >= 3/2 |
| 2026-11-13 | [F0101A](2026-11-13/F0101A/) | attempt | F0101: regularization by biased-coin convolution |
| 2026-11-13 | [F0119A](2026-11-13/F0119A/) | attempt | F0119 work log |
| 2026-11-13 | [F0124A](2026-11-13/F0124A/) | attempt | Setting and source correction |
| 2026-11-13 | [F0124AR](2026-11-13/F0124AR/) | independent referee log | Independent F0124 referee log |
| 2026-11-13 | [F0126A](2026-11-13/F0126A/) | attempt | F0126: reconstruction, support, and the equivalence group |
| 2026-11-13 | [F0126AR](2026-11-13/F0126AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [F0129A](2026-11-13/F0129A/) | attempt | F0129: compactly supported self-repelling Brownian polymers |
| 2026-11-13 | [F0136A](2026-11-13/F0136A/) | attempt | F0136: two-dimensional random walk in Dirichlet environment |
| 2026-11-13 | [F0137A](2026-11-13/F0137A/) | attempt | F0137: nonzero drift and spatial regeneration estimates for RWDE |
| 2026-11-13 | [G0010A](2026-11-13/G0010A/) | attempt | G0010: near-regular graphs can have polynomial subcritical components |
| 2026-11-13 | [G0010AR](2026-11-13/G0010AR/) | independent referee log | Independent referee report on G0010 |
| 2026-11-13 | [G0012A](2026-11-13/G0012A/) | attempt | G0012: the non-backtracking birthday conjecture |
| 2026-11-13 | [G0012AR](2026-11-13/G0012AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [G0015A](2026-11-13/G0015A/) | attempt | G0015: critical continuous-type cascades and the CRT |
| 2026-11-13 | [G0015AR](2026-11-13/G0015AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [I0003A](2026-11-13/I0003A/) | attempt | I0003: recurrence, transience, and what partial-sum growth misses |
| 2026-11-13 | [I0003AR](2026-11-13/I0003AR/) | independent referee log | Independent referee log: I0003 |
| 2026-11-13 | [I0004A](2026-11-13/I0004A/) | attempt | I0004 work log |
| 2026-11-13 | [I0005A](2026-11-13/I0005A/) | attempt | I0005: critical parking in dimension four |
| 2026-11-13 | [I0006A](2026-11-13/I0006A/) | attempt | I0006: lower tails and the finite-time divisible sandpile |
| 2026-11-13 | [I0006B](2026-11-13/I0006B/) | attempt | I0006B: the critical lower tail of the divisible sandpile |
| 2026-11-13 | [I0006BR](2026-11-13/I0006BR/) | referee log | Independent referee report: I0006B |
| 2026-11-13 | [I0006PR](2026-11-13/I0006PR/) | referee audit of a paper | Referee audit log |
| 2026-11-13 | [I0012A](2026-11-13/I0012A/) | attempt | I0012: the critical random comb |
| 2026-11-13 | [I0012AR](2026-11-13/I0012AR/) | independent referee log | Independent referee log |
| 2026-11-13 | [I0014A](2026-11-13/I0014A/) | attempt | Open problems I0013 and I0014 |
| 2026-11-13 | [I0069A](2026-11-13/I0069A/) | attempt | I0069: extrapolation of stochastic maximal regularity |
| 2026-11-13 | [I0070A](2026-11-13/I0070A/) | attempt | I0070 — Time regularization in Hilbert spaces |
| 2026-11-13 | [I0070AR](2026-11-13/I0070AR/) | independent referee log | Independent referee log — I0070 |
| 2026-11-13 | [I0070PR](2026-11-13/I0070PR/) | referee audit of a paper | Independent referee audit |
| 2026-11-13 | [I0071A](2026-11-13/I0071A/) | attempt | I0071: triangular reaction–diffusion systems with transport noise |
| 2026-11-13 | [I0071AR](2026-11-13/I0071AR/) | independent referee log | Independent audit of I0071 |
| 2026-11-13 | [I0071P](2026-11-13/I0071P/) | paper draft |  |
| 2026-11-13 | [I0072A](2026-11-13/I0072A/) | attempt | I0072: quadratic reaction–diffusion systems with mass control |
| 2026-11-13 | [I0078A](2026-11-13/I0078A/) | attempt | I0078: number rigidity, transport, and negative-exponent Riesz gases |
| 2026-11-13 | [I0079A](2026-11-13/I0079A/) | attempt | I0079: nonunique low-intensity Bernoulli–Voronoi limits |
| 2026-11-13 | [I0096A](2026-11-13/I0096A/) | attempt | I0096: deterministic critical-threshold phase retrieval |
| 2026-11-13 | [I0103A](2026-11-13/I0103A/) | attempt | I0103: Paley ETF restricted isometries |
| 2026-11-13 | [I0103AR](2026-11-13/I0103AR/) | independent referee log | Independent referee log — I0103AR |
| 2026-11-13 | [RG11AR](2026-11-13/RG11AR/) | first-reader report |  |
| 2026-11-13 | [RG12AR](2026-11-13/RG12AR/) | first-reader report |  |
| 2026-11-13 | [RG19AR](2026-11-13/RG19AR/) | first-reader report |  |
| 2026-11-13 | [RG20AR](2026-11-13/RG20AR/) | first-reader report |  |
| 2026-11-13 | [RG9AR](2026-11-13/RG9AR/) | first-reader report |  |
| 2026-11-14 | [BPWT_posted_referee](2026-11-14/BPWT_posted_referee/) | referee report on a posted paper | Referee report: the waiting time for a bridge pattern in simple random walk |
| 2026-11-14 | [C0033D](2026-11-14/C0033D/) | attempt | Open problem C0033, fourth attempt: inequality (21) on connected strict three-point kernels |
| 2026-11-14 | [C0033D_check](2026-11-14/C0033D_check/) | re-check of an attempt |  |
| 2026-11-14 | [C0033E](2026-11-14/C0033E/) | attempt | Open problem C0033, fifth attempt: the mixed spectral/graph boundary of inequality (21) on three points |
| 2026-11-14 | [C0033E_check](2026-11-14/C0033E_check/) | re-check of an attempt |  |
| 2026-11-14 | [C0033F](2026-11-14/C0033F/) | attempt | Open problem C0033, sixth attempt: the general mixed collar and the global constant for three-point concavity |
| 2026-11-14 | [C0033F_check](2026-11-14/C0033F_check/) | re-check of an attempt |  |
| 2026-11-14 | [DBAR_posted_referee](2026-11-14/DBAR_posted_referee/) | referee report on a posted paper | Referee report: the d-bar distance between invariant determinantal measures is bounded by the trace norm |
| 2026-11-14 | [DRM_posted_referee](2026-11-14/DRM_posted_referee/) | referee report on a posted paper | Referee report: survival asymptotics and moment predictions for the Derrida-Retaux recursion |
| 2026-11-14 | [DSCT_posted_referee](2026-11-14/DSCT_posted_referee/) | referee report on a posted paper | Referee report: the divisible sandpile odometer at the critical lower tail |
| 2026-11-14 | [E0094_posted_referee](2026-11-14/E0094_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [FA1F_posted_referee](2026-11-14/FA1F_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [FLUX_posted_referee](2026-11-14/FLUX_posted_referee/) | referee report on a posted paper | Referee report: a flux plateau for site-disordered finite-capacity exclusion |
| 2026-11-14 | [GGCR_posted_referee](2026-11-14/GGCR_posted_referee/) | referee report on a posted paper | Referee report: cluster repulsion on the grandparent graph |
| 2026-11-14 | [GU_posted_referee](2026-11-14/GU_posted_referee/) | referee report on a posted paper | Referee report: Conserved charges in linearly reinforced graph urns |
| 2026-11-14 | [I0003_posted_referee](2026-11-14/I0003_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [I0070_posted_referee](2026-11-14/I0070_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [I0071_posted_referee](2026-11-14/I0071_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [KCM_posted_referee](2026-11-14/KCM_posted_referee/) | referee report on a posted paper | Referee report: "Stationary measures of planar kinetically constrained models with bounded conditional odds" (posted version) |
| 2026-11-14 | [NBBR_posted_referee](2026-11-14/NBBR_posted_referee/) | referee report on a posted paper | Referee report |
| 2026-11-14 | [NBL_posted_referee](2026-11-14/NBL_posted_referee/) | referee report on a posted paper | Referee report: nested beta-Laguerre ensembles |
| 2026-11-14 | [NRPC_posted_referee](2026-11-14/NRPC_posted_referee/) | referee report on a posted paper | Referee report: polynomial components in spectrally subcritical percolation on near-regular graphs |
| 2026-11-14 | [OGS_posted_referee](2026-11-14/OGS_posted_referee/) | referee report on a posted paper | Referee report: Adding one permutation to a transposition and a long cycle |
| 2026-11-14 | [P0245_posted_referee](2026-11-14/P0245_posted_referee/) | referee report on a posted paper | Referee report: the stationary cover time of reversible chains on three and four states |
| 2026-11-14 | [P0343_posted_referee](2026-11-14/P0343_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [RG10AR](2026-11-14/RG10AR/) | first-reader report | RG10AR - first-reader report, brownian-prefix-filling |
| 2026-11-14 | [RG4AR](2026-11-14/RG4AR/) | first-reader report | RG4AR - first-reader report, first-passage-pattern-waiting-time |
| 2026-11-14 | [RG7AR](2026-11-14/RG7AR/) | first-reader report | RG7AR - first-reader report, nonergodic-galton-watson-flow-rule |
| 2026-11-14 | [RR_posted_referee](2026-11-14/RR_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [RWRS_posted_referee](2026-11-14/RWRS_posted_referee/) | referee report on a posted paper | Referee report: good configurations of random walk in random scenery under two-sided conditioning |
| 2026-11-14 | [SAU_posted_referee](2026-11-14/SAU_posted_referee/) | referee report on a posted paper | Referee report: uniqueness of stable allocations in dimensions one and two |
| 2026-11-14 | [SHC_posted_referee](2026-11-14/SHC_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [T353_posted_referee](2026-11-14/T353_posted_referee/) | referee report on a posted paper |  |
| 2026-11-14 | [TEF_posted_referee](2026-11-14/TEF_posted_referee/) | referee report on a posted paper | Referee report: frozen edges of stationary tridiagonal dynamics with GUE spectra |
| 2026-11-14 | [URN_posted_referee](2026-11-14/URN_posted_referee/) | referee report on a posted paper |  |
| 2026-11-15 | [BSSDR_posted_referee](2026-11-15/BSSDR_posted_referee/) | referee report on a posted paper | Independent referee report |
