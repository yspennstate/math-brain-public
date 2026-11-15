# Literature check of the famous-list replacement candidates, 14 Nov 2026 21:1x

13 replacements are owed (TOP200_FAMOUS = 187). The 12 candidates left after the batch 1-4 text screens were
checked against arXiv (queries in famous_litcheck_1114.sh, responses in famous_lit_1114/). Abstracts read where
a title suggested a solution. Items marked "from memory" were not confirmed on arXiv and need a source before
anyone relies on them; they are dropped here because a doubtful candidate is not worth a row.

| key | candidate | finding | status |
|---|---|---|---|
| F10 | random conductances, heavy-tail quenched CLT d=2 | the quenched invariance principle for general nonnegative iid conductances is Andres-Barlow-Deuschel-Hambly (PTRF 2013), from memory; the open heat-kernel questions are d>=4 (Biskup-Boukhadra 1010.5542). The candidate as worded is not open | drop |
| F12 | directed polymer in d=3: free energy, fluctuation exponent | nothing found | free |
| F17 | random interlacements u_* = u_** = bar u | Duminil-Copin, Goswami, Rodriguez, Severo, Teixeira, arXiv:2308.07919 with 2308.07303 and 2308.07920 (2023) | solved, drop |
| G02 | infinite collision property, walks on the percolation cluster | Z^2 cluster: D. Chen and X. Chen, Sci. China Math. 2010, from memory, not on arXiv; 3D UST done in 2301.08547 | drop |
| G07 | internal DLA fluctuations d>=3 | order sqrt(log n) is Jerison-Levine-Sheffield (2013), from memory; only finer laws open (2604.21142 is cylinders) | weak, drop |
| G09 | jamming limit of random sequential adsorption in the plane | no exact value; existence is Penrose (2001); recent arXiv work is numerical | free, weak |
| G11 | favourite sites of planar simple random walk | arXiv:2409.00995 (2024): in d=2 three favourites occur i.o., eventually never four; answers Erdos-Revesz 1987 | solved, drop |
| G22 | random polynomials, real-zero universality | Ibragimov-Maslova; Nguyen-Nguyen-Vu sharp universality (2016), from memory | drop |
| H11 | Swendsen-Wang mixing at criticality on Z^2 | Ullrich 1212.4908: all non-critical temperatures and Ising at every temperature; critical Potts q=3 polynomial (Gheissari-Lubetzky, from memory); q=4 polynomial mixing still open | free only as q=4 |
| J04 | 2-neighbour bootstrap, second-order term | order Theta(p^-1/2) known (Gravner-Holroyd-Morris 1002.3881); 2303.14910 is the modified model. Only the constant is open | weak, drop |
| H12 | exact Boolean-model critical intensity | no exact value known; Lipschitz time constant 2605.31568 is unrelated | free, weak (exact-value problem) |
| H18 | exact site p_c on Z^2 | no exact value known | free, weak (exact-value problem) |

Result: of 12, five survive (F12; H11 as q=4; G09, H12, H18 as weak exact-value problems). That leaves 13 owed
against 1 strong and 4 weak candidates. A fifth candidate batch is needed, drawn from current survey open-problem
lists (Duminil-Copin's 2022 ICM list, the 2024-26 percolation and random-walk surveys) rather than from memory,
because four of the batch-2 and batch-3 picks turned out to be solved since 2023.

## Recheck of the two strong survivors, 14 Nov 2026 21:5x (famous_recheck_1114.sh, responses in famous_lit_1114/rc/)

| key | finding | status |
|---|---|---|
| F12 | the free-energy half is settled: Junk and Lacoin, arXiv:2402.02562 (strong disorder implies very strong disorder, bounded-above environments, all d) and arXiv:2502.04113 (general environments and reference walks), so beta_c = bar beta_c. The first litcheck query missed these because it searched titles for "dimension 3". What is left is the fluctuation exponent in strong disorder, which overlaps T005 | drop |
| H11 | Gheissari and Lubetzky, arXiv:1607.02182: critical q=3 Potts Glauber inverse gap n^{O(1)}, q=4 at most n^{O(log n)}; arXiv:1611.01147: n^{O(log n)} for critical FK dynamics at every q in (1,4]; q=2 polynomial is Lubetzky and Sly, arXiv:1001.1613. No later arXiv paper on critical 2D Potts mixing turned up; Semantic Scholar lists 16 citing papers of 1607.02182, none later than 2018 (thin coverage, not proof of absence) | free: polynomial mixing at critical q=4, and for FK with non-integer q in (1,4) |

After the recheck: one strong candidate (H11, restated) and three weak exact-value ones (G09, H12, H18). Recent open-problem collections in math.PR on arXiv (famous_batch5_1114.sh, famous_lit_1114/b5/) are niche lists the top-200 has already drawn from; the famous end of the field is close to used up at 187 rows.

## Fresh screen, 15 Nov 2026 (an agent), after the earlier pool was spent

Added: T475, critical value of the one-dimensional contact process (Liggett 1995 upper bound 1.942, read from the abstract).

Already on the list under another id (checked by title grep of LIST.md, 15 Nov): random k-SAT threshold (T017, T138),
once-reinforced walk (T047), hard spheres/disks (row near line 726), negative correlation of uniform forests (T084),
Aaronson-Ambainis (T042), Lorentz gas (T053), Lorentz mirror model (T101), DLA dimension (T016), lattice animals (T055),
contact-process exponents (T099), hard-core on Z^2 (T109), independence ratio of random cubic graphs (T119), BHH constant
(T156), Eden limit shape (T170), Steele TSP variance (T222), random matching second term (T427), SAW connective constant
(T459), Hammersley/Ulam constants in d >= 3 (T445), LQG dimension (T037), biased walk speed on GW trees (T048), proper
3-colourings of Z^3 (T110), frog model (T127), excited walk speed (T217).
Solved or moved, so not candidates: Aldous-Lyons soficity (announced negative answer by Bowen-Chapman-Lubotzky-Vidick,
2024; not re-read here), Komlos (T066 retired), union-closed and Sidorenko (moved to the general list), KLS (T018
retired), Courtade-Kumar (T040 retired), Bunkbed (disproved 2024, Gladkov-Pak-Zimin; not re-read here).
Still to screen: oriented (directed) percolation p_c on Z^2 as a constant row; zero-temperature Ising fixation in d >= 3
(grep showed 10 hits for "zero-temperature", check whether one is a row before writing).
Checked 15 Nov 01:5x: zero-temperature fixation is T045 (duplicate). Oriented percolation p_c on Z^2 is not on the list, but it is a third planar-constant row next to T473 and T475; hold it unless no better candidate turns up.
