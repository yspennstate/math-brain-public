# Referee report on PAPER.tex

Overall verdict: **SOUND**.

This verdict concerns thm:main and cor:vt under the conventional assumption that graphs are finite, simple, and undirected. I found no gap in either proof. I did find a false explanation in the introduction: regular bipartite graphs cannot have stationary variance of order n². That sentence needs correction. Priority, precise literature attributions, and the authors' particular random-graph run remain unverified.

The audit was carried out in the requested order; contemporaneous verdicts and derivations are in LOG.md. PAPER.tex was not changed. There was no browsing, no use of the linked author code, no other agent, no git push, and no visible window. All audit files are local. Earlier global instructions requiring writes to the shared brain/mesh/checklist were superseded by the explicit folder-only restriction for this run.

## Verdicts by statement and proof step

Line numbers refer to the original PAPER.tex. GAP below distinguishes an explanatory omission or unavailable evidence from a mathematical proof gap.

| Statement or step | Verdict | Reason |
| --- | --- | --- |
| Abstract, lines 31–39 | CORRECT | Both mathematical conclusions follow from the audited proofs; attribution is separately qualified below. |
| Model, lines 46–48 | CORRECT | Continuous time, rate one at each vertex, uniform neighbour, and opposite opinion are specified. |
| Graph conventions, line 46 | GAP | Say “simple undirected”; the proof uses P(u,u)=0 and symmetry. Conventional usage supplies this assumption. |
| General non-cycle irreducibility attribution, lines 50–52 | GAP | Compatible with all exact tests, but the general DW theorem and its original hypotheses were not independently established here; neither main proof uses it. |
| Complete-graph correlation and eq:Kn, lines 61–64 | CORRECT | Independent one-dimensional generator calculation gives n(n−2)/(2n−3) and c=−1/(2n−3). |
| AF variance bounds and question, lines 59–66 | GAP | The formulas used here were independently verified; exact book wording, numbering, and normalization cannot be certified from memory. |
| thm:main, lines 68–75 | CORRECT | The weighted trace identity and sharp diagonal bound give the inequality and strictness. |
| Every stationary law / odd cycles, lines 77–78 | CORRECT | All proof steps require stationarity only; odd cycles have one closed class despite transient states. |
| Bipartite stationary mixtures and S values, lines 78–79 | CORRECT | Connected bipartite graphs have only the two proper colourings as recurrent classes. |
| Bipartite order-n² rationale, lines 79–80 | WRONG | In a regular bipartite graph the colour classes have equal size; all stationary laws have S=0 and variance 0. |
| Spectrum of P, lines 82–83 and 100–101 | CORRECT | Connected regular undirected P is symmetric; non-bipartiteness excludes eigenvalue −1. |
| cor:vt, lines 85–90 | CORRECT | The trace formula follows exactly when the inverse diagonal is constant. |
| Three introductory examples, lines 92–95 | CORRECT | All spectra, fractions, and displayed decimal values match independent exact calculations. |
| C and Q definitions, lines 99–101 | CORRECT | C is symmetric with unit diagonal; Q is positive definite and Q1=2·1. |
| lem:eq: generator on η_v, lines 112–114 | CORRECT | Lη_v=−η_v−(Pη)_v; stationarity gives Qm=0 and m=0. |
| lem:eq: product-generator display, lines 114–119 | CORRECT | Each endpoint contributes once; copying its neighbour contributes −1, including adjacent endpoints. |
| eq:syl: off-diagonal zeros, lines 119–120 | CORRECT | The displayed product equation is precisely the off-diagonal Sylvester equation. |
| eq:syl: diagonal δ, lines 120–121 | CORRECT | δ_v=2(1+(PC)_vv); symmetry accounts for the factor two. |
| δ_v≥0, line 121 | CORRECT | δ_v=4 times the neighbour-averaged probability of equal endpoint opinions. |
| Var S=(1/4)Σδ, lines 122–123 | CORRECT | Multiplication by 1ᵀ and 1 gives 4·1ᵀC1=Σδ; E S=0. |
| Var S=n(1+cbar)/2, lines 126–128 | CORRECT | Each unordered edge contributes twice to the oriented neighbour sum. |
| lem:rep statement, lines 130–135 | CORRECT | Σδ_u(Q⁻¹)_uu=2n also follows immediately by taking tr(Q⁻¹(QC+CQ)). |
| Sylvester invertibility, lines 138–139 | CORRECT | Every eigenvalue q_i+q_j is strictly positive. |
| Integral solves Sylvester equation, lines 139–143 | CORRECT | The derivative has the right negative sign and the boundary contribution is +D. |
| Integral unit-diagonal equation, lines 143–144 | CORRECT | Diagonal D and symmetry give the entrywise-square kernel. |
| Sum and factor 1/2, lines 146–148 | CORRECT | ∫e^(−2tQ)dt=(1/2)Q⁻¹, yielding 2n rather than n. |
| lem:diag statement, lines 154–160 | CORRECT | The bound is sharp exactly at universal vertices, hence exactly on K_n under regularity. |
| e_u=a+b and inverse splitting, lines 163–166 | CORRECT | The constant eigenspace is orthogonal to b; its contribution is 1/(2n). |
| Cauchy–Schwarz and equality, lines 168–169 | CORRECT | Equality holds exactly when Qb is a multiple of b. |
| bᵀb and bᵀQb display, lines 170–172 | CORRECT | These are (n−1)/n and (n−2)/n; the latter uses P(u,u)=0. |
| Diagonal-bound arithmetic, lines 174–176 | CORRECT | 1/(2n)+(n−1)²/[n(n−2)]=(2n−3)/[2(n−2)]. |
| Pb and nonneighbour contradiction, lines 178–180 | CORRECT | The u coordinate forces μ=−1/(n−1); a nonneighbour would force μ=1. |
| Universal-vertex converse, lines 181–182 | CORRECT | If there is no nonneighbour, regularity gives d=n−1 and the claimed eigenvector identity holds. |
| n=3 boundary case | CORRECT | The only admissible graph is K_3; the inverse diagonal bound is 3/2 and variance is 1. |
| n/2 remark, lines 185–187 | CORRECT | m_u≥1 gives the non-strict bound; actually m_u>1 since e_u is not a Q eigenvector. |
| Main inequality chain, lines 192–196 | CORRECT | δ≥0 permits replacing each inverse diagonal by its lower bound; the direction is correct. |
| Positive δ sum, line 197 | CORRECT | Σδ_um_u=2n>0 with all m_u>0 and δ_u≥0 forces Σδ_u>0. |
| Non-complete strictness, lines 196–198 | CORRECT | A regular non-complete simple graph has no universal vertex, so every inverse-diagonal inequality is strict. |
| Complete-graph equality, line 198 | CORRECT | All inverse diagonals equal m*, so equality follows for any stationary law. |
| Difference E and diagonal F, lines 202–204 | CORRECT | The Sylvester representation gives diag(E)=Mf. |
| Strict Schur-product step, line 205 | CORRECT | e^(−tQ) is positive definite; its Hadamard square and their integral are positive definite. |
| Uniqueness of C, lines 205–206 | CORRECT | Mf=0 gives f=0, hence E=0 by Sylvester invertibility. |
| Automorphism invariance, lines 206–208 | CORRECT | Relabelling preserves the system; uniqueness makes C invariant for every stationary law. |
| Constant δ and m, lines 208–209 | CORRECT | Vertex transitivity makes both quantities constant across vertices. |
| Final corollary formula, lines 209–210 | CORRECT | δ tr Q⁻¹=2n and Var S=nδ/4 give n²/(2 tr Q⁻¹). |
| Exhaustive n≤7 claim, lines 215–219 | CORRECT | Independent enumeration gives precisely the listed non-cycle classes and their exact values. |
| Petersen 40/13 and C_7=1, lines 220–221 | CORRECT | Both match rational correlation and characteristic-polynomial computations. |
| Particular 297-graph and floating-point runs, lines 217–221 | GAP | Their inputs and output are absent here; the repository was not accessed. This is an evidence limitation. |
| Every entry of tab:small | CORRECT | All eight displayed numerical values round correctly; see the table below. |

## Independent derivations and reducibility checks

For K_n, let k be the number of plus opinions and S=2k−n. The upward and downward jump rates of k are

    b_k=(n−k)(n−k−1)/(n−1),    a_k=k(k−1)/(n−1).

They imply LS=−2S and

    L(S²)=−4S²+2[n(n−2)+S²]/(n−1).

Stationarity therefore gives E S=0 and Var S=n(n−2)/(2n−3). The nonconstant complete-graph states communicate, so their unique stationary law is permutation invariant. Then n+n(n−1)c=Var S gives c=−1/(2n−3). This checks the complete-graph benchmark independently of the paper's matrix proof.

For general distinct v,w, the independently computed generator is

    L(η_vη_w)=−2η_vη_w−Σ_u P(v,u)η_uη_w−Σ_u P(w,u)η_vη_u.

When v∼w the endpoint-copying terms are −P(v,w) and −P(w,v). The paper handles them correctly using c(w,w)=c(v,v)=1. Thus there is no omitted adjacent-vertex correction.

The weighted trace identity has an especially short independent check:

    tr[Q⁻¹(QC+CQ)]=tr C+tr(Q⁻¹CQ)=2tr C=2n=Σ_u δ_u(Q⁻¹)_uu.

This confirms both the factor and the sign without any integral. For the corollary's strict positive definiteness, set H=e^(−tQ). For z≠0,

    zᵀ(H∘H)z = ||H^(1/2) diag(z) H^(1/2)||_F² > 0.

Invertibility of H^(1/2) makes the strict inequality immediate. Equivalently, H(0)∘H(0)=I and continuity make a short initial portion of the integral already positive definite. The Schur step is valid.

The constants all plus and all minus are transient: each has exit rate n and no incoming transition from another state. To reach all plus, the last minus would need a minus neighbour, which does not exist. They have stationary mass zero and cannot be reached from a nonconstant state; they may of course be chosen initially.

On an odd cycle the number of monochromatic edges is odd and never increases. Defects can move and annihilate in pairs. Every state reaches the single-defect class, whose 2n states form one communicating class with uniform stationary law. A circuit of the defect reverses the global sign. In this class S=±1 equally, hence Var S=1. Reducibility on all nonconstant states, as for C_5, does not mean several stationary laws. The full-chain calculation below recovers the sole 10-state closed class on C_5. No example with multiple stationary laws inside the stated hypotheses was found; in any event the proof is valid separately for each law because only generator stationarity is used.

On a connected bipartite graph, multiply opinions by a fixed proper ±1 colouring. This turns the antivoter dynamics into ordinary voter dynamics. Finite connected voter dynamics eventually reaches consensus, so the original chain has exactly the two proper colourings as its closed classes. In a d-regular bipartite graph, d|A|=d|B| forces |A|=|B|. Every stationary mixture therefore has S=0, even though individual vertex means may be nonzero. The theorem's bound would hold trivially there. Non-bipartiteness is needed for Q⁻¹ and the zero-mean argument, not because the regular bipartite variance can be large. A star with the equal mixture of its two colourings has variance (n−2)², illustrating why the paper's explanation applies to irregular graphs only.

The lower-bound prose involving κ is also easy to normalize if κ means |E|−MaxCut(G): let M(η) count monochromatic edges. The audited edge identity gives Var S=(2/d)E M≥2κ/d. The source leaves κ undefined, so the match to AF's notation still needs checking.

## Numerical method and independent checks

The audit programs are original. The main numerical calculations use standard-library integers and fractions, with Bareiss elimination and an exact residual check of every solved system. SymPy is used only for the separate spectral checks. No author software or graph catalogue was used.

For enumeration, every labelled regular graph in degrees 0≤d≤floor((n−1)/2) was generated by filling the upper triangle of its adjacency matrix. A residual degree-sequence test pruned impossible branches. Our own isomorphism backtracker identified representatives; complementation covered the higher degrees. A second program independently counted labelled realizations using grouped neighbour choices and matched every generation count. This gives 25 connected non-bipartite isomorphism classes for 3≤n≤8.

For the full chain, every directed update was built on all 2^n bit states. The integer generator is d times the true continuous-time generator, which leaves stationary laws unchanged. A strongly connected component decomposition found every closed class. Each class's stationary probability vector was solved exactly, checked to be positive and normalized, and verified against all columns of the original generator, including transient-state columns. Every first moment and every pair correlation was compared with the separately solved correlation equations. All seven non-bipartite classes on at most six vertices agree. The three bipartite controls give all their extremal laws as well. Every stationary law is a mixture of the enumerated extremal laws; the regular bipartite mixtures all retain S=0.

All exact edge lists, matrices, inverse diagonals, and every state/probability of every full-chain extremal law are saved in exact_enumerate.json and exact_families.json. For graphs labelled n8_d3_* or n8_d4_*, those edge lists specify the graph without reliance on a standard name.

The additional test set includes all odd cycles requested, Petersen, prism, octahedron, matching complements through n=12, and every connected non-bipartite complement of a 2-factor through n=12. The maximum ratio below is stated separately for the exhaustive range and the full finite test set.

The spectral check uses g(x)=det(xI−A) to compute tr Q⁻¹=−d g′(−d)/g(−d), separately from the inverse linear systems. A separate automorphism search identifies vertex-transitive specimens. All 69 rows, including overlaps, have matching traces; all 44 vertex-transitive rows satisfy the corollary exactly. These rows are not 69 distinct graphs.

# Step 5 exact computations

| n | connected regular classes | non-bipartite | bipartite controls |
| --- | --- | --- | --- |
| 3 | 1 | 1 | 0 |
| 4 | 2 | 1 | 1 |
| 5 | 2 | 2 | 0 |
| 6 | 5 | 3 | 2 |
| 7 | 4 | 4 | 0 |
| 8 | 17 | 14 | 3 |

| n | d | graph | exact Var S | Var / complete-graph bound |
| --- | --- | --- | --- | --- |
| 3 | 2 | K3 | 1 | 1 |
| 4 | 3 | K4 | 8/5 | 1 |
| 5 | 2 | C5 | 1 | 7/15 |
| 5 | 4 | K5 | 15/7 | 1 |
| 6 | 3 | K6 minus (C6) | 72/37 | 27/37 |
| 6 | 4 | K6 minus matching | 12/5 | 9/10 |
| 6 | 5 | K6 | 8/3 | 1 |
| 7 | 2 | C7 | 1 | 11/35 |
| 7 | 4 | K7 minus (C3+C4) | 249/101 | 2739/3535 |
| 7 | 4 | K7 minus (C7) | 203/75 | 319/375 |
| 7 | 6 | K7 | 35/11 | 1 |
| 8 | 3 | n8_d3_rep5 | 64/31 | 52/93 |
| 8 | 3 | n8_d3_rep3 | 271/122 | 3523/5856 |
| 8 | 3 | n8_d3_rep2 | 792512/323579 | 643916/970737 |
| 8 | 3 | n8_d3_rep1 | 2368/865 | 1924/2595 |
| 8 | 4 | n8_d4_comp_rep1 | 1856/719 | 1508/2157 |
| 8 | 4 | n8_d4_comp_rep2 | 4928960/1658269 | 4004780/4974807 |
| 8 | 4 | n8_d4_comp_rep3 | 63594/20693 | 137787/165544 |
| 8 | 4 | n8_d4_comp_rep4 | 192/61 | 52/61 |
| 8 | 4 | n8_d4_comp_rep5 | 448/141 | 364/423 |
| 8 | 5 | K8 minus (C3+C5) | 194/59 | 1261/1416 |
| 8 | 5 | K8 minus (C4+C4) | 96/29 | 26/29 |
| 8 | 5 | K8 minus (C8) | 1344/401 | 364/401 |
| 8 | 6 | K8 minus matching | 32/9 | 26/27 |
| 8 | 7 | K8 | 48/13 | 1 |

## All extremal full-chain stationary laws for n≤6

| n | d | graph | states | extremal laws | class sizes | variances | check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2 | K3 | 8 | 1 | 6 | 1 | all pair entries agree |
| 4 | 2 | C4 | 16 | 2 | 1, 1 | 0, 0 | absorbing colourings; S=0 |
| 4 | 3 | K4 | 16 | 1 | 14 | 8/5 | all pair entries agree |
| 5 | 2 | C5 | 32 | 1 | 10 | 1 | all pair entries agree |
| 5 | 4 | K5 | 32 | 1 | 30 | 15/7 | all pair entries agree |
| 6 | 2 | C6 | 64 | 2 | 1, 1 | 0, 0 | absorbing colourings; S=0 |
| 6 | 3 | K6 minus (C3+C3) | 64 | 2 | 1, 1 | 0, 0 | absorbing colourings; S=0 |
| 6 | 3 | K6 minus (C6) | 64 | 1 | 62 | 72/37 | all pair entries agree |
| 6 | 4 | K6 minus matching | 64 | 1 | 62 | 12/5 | all pair entries agree |
| 6 | 5 | K6 | 64 | 1 | 62 | 8/3 | all pair entries agree |

## Additional families (including overlaps with the exhaustive list)

| graph | n | d | exact Var S | ratio |
| --- | --- | --- | --- | --- |
| C3 | 3 | 2 | 1 | 1 |
| C5 | 5 | 2 | 1 | 7/15 |
| C7 | 7 | 2 | 1 | 11/35 |
| C9 | 9 | 2 | 1 | 5/21 |
| Petersen | 10 | 3 | 40/13 | 17/26 |
| triangular_prism | 6 | 3 | 72/37 | 27/37 |
| K6_minus_matching | 6 | 4 | 12/5 | 9/10 |
| K8_minus_matching | 8 | 6 | 32/9 | 26/27 |
| K10_minus_matching | 10 | 8 | 60/13 | 51/52 |
| K12_minus_matching | 12 | 10 | 96/17 | 84/85 |
| K5_minus_C5 | 5 | 2 | 1 | 7/15 |
| K6_minus_C6 | 6 | 3 | 72/37 | 27/37 |
| K7_minus_C3_C4 | 7 | 4 | 249/101 | 2739/3535 |
| K7_minus_C7 | 7 | 4 | 203/75 | 319/375 |
| K8_minus_C3_C5 | 8 | 5 | 194/59 | 1261/1416 |
| K8_minus_C4_C4 | 8 | 5 | 96/29 | 26/29 |
| K8_minus_C8 | 8 | 5 | 1344/401 | 364/401 |
| K9_minus_C3_C3_C3 | 9 | 6 | 27/7 | 45/49 |
| K9_minus_C3_C6 | 9 | 6 | 6003/1535 | 2001/2149 |
| K9_minus_C4_C5 | 9 | 6 | 71655/18239 | 119425/127673 |
| K9_minus_C9 | 9 | 6 | 2997/761 | 4995/5327 |
| K10_minus_C3_C3_C4 | 10 | 7 | 36264/8129 | 77061/81290 |
| K10_minus_C3_C7 | 10 | 7 | 6464/1443 | 6868/7215 |
| K10_minus_C4_C6 | 10 | 7 | 360912/80363 | 383469/401815 |
| K10_minus_C5_C5 | 10 | 7 | 328/73 | 697/730 |
| K10_minus_C10 | 10 | 7 | 95120/21163 | 20213/21163 |
| K11_minus_C3_C3_C5 | 11 | 8 | 165745/33049 | 3149155/3271851 |
| K11_minus_C3_C4_C4 | 11 | 8 | 47565/9473 | 100415/104203 |
| K11_minus_C3_C8 | 11 | 8 | 40635/8087 | 85785/88957 |
| K11_minus_C4_C7 | 11 | 8 | 3569223/709279 | 22605079/23406207 |
| K11_minus_C5_C6 | 11 | 8 | 594757/118157 | 11300383/11697543 |
| K11_minus_C11 | 11 | 8 | 194821/38701 | 336509/348309 |
| K12_minus_C3_C3_C3_C3 | 12 | 9 | 72/13 | 63/65 |
| K12_minus_C3_C3_C6 | 12 | 9 | 15714/2831 | 54999/56620 |
| K12_minus_C3_C4_C5 | 12 | 9 | 21187296/3813659 | 18538884/19068295 |
| K12_minus_C3_C9 | 12 | 9 | 439596/79109 | 769293/791090 |
| K12_minus_C4_C4_C4 | 12 | 9 | 1440/259 | 36/37 |
| K12_minus_C4_C8 | 12 | 9 | 2469600/444019 | 432180/444019 |
| K12_minus_C5_C7 | 12 | 9 | 438988/78915 | 768229/789150 |
| K12_minus_C6_C6 | 12 | 9 | 840/151 | 147/151 |
| K12_minus_C12 | 12 | 9 | 614880/110531 | 107604/110531 |
| C3_cartesian_C3 | 9 | 4 | 45/13 | 75/91 |

Largest non-complete ratio for n≤8: K8 minus matching: 26/27 = 0.9629629630.

Largest non-complete ratio in the entire tested set: K12_minus_matching: 84/85 = 0.9882352941.

Labels n8_d3_* and n8_d4_* refer to complete edge lists in exact_enumerate.json. Graphs are simple and undirected.

Commands:
```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit_exact.py --phase enumerate
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit_exact.py --phase families
PYTHONDONTWRITEBYTECODE=1 python3 validate_results.py --phase 5
```

# Step 6 exact checks

## Every entry of tab:small

| graph | n | d | exact variance | paper display | verdict |
| --- | --- | --- | --- | --- | --- |
| K4 | 4 | 3 | 8/5 | 1.6000 | CORRECT |
| K5 | 5 | 4 | 15/7 | 2.1429 | CORRECT |
| K6 | 6 | 5 | 8/3 | 2.6667 | CORRECT |
| octahedron | 6 | 4 | 12/5 | 2.4000 | CORRECT |
| triangular prism | 6 | 3 | 72/37 | 1.9459 | CORRECT |
| K7 | 7 | 6 | 35/11 | 3.1818 | CORRECT |
| K7 minus (C7) | 7 | 4 | 203/75 | 2.7067 | CORRECT |
| K7 minus (C3+C4) | 7 | 4 | 249/101 | 2.4653 | CORRECT |

## Eight explicit vertex-transitive examples

| graph | n | d | trace Q^-1 | n²/(2 trace) | pair variance |
| --- | --- | --- | --- | --- | --- |
| n6_d5_comp_rep0 | 6 | 5 | 27/4 | 8/3 | 8/3 |
| n6_d4_comp_rep0 | 6 | 4 | 15/2 | 12/5 | 12/5 |
| n6_d3_comp_rep1 | 6 | 3 | 37/4 | 72/37 | 72/37 |
| Petersen | 10 | 3 | 65/4 | 40/13 | 40/13 |
| C3_cartesian_C3 | 9 | 4 | 117/10 | 45/13 | 45/13 |
| C7 | 7 | 2 | 49/2 | 1 | 1 |
| circulant_C7_steps_1_2 | 7 | 4 | 525/58 | 203/75 | 203/75 |
| circulant_C8_steps_1_2 | 8 | 4 | 141/14 | 448/141 | 448/141 |

The two circulants here are explicitly defined as edges ±1,±2 modulo n. The paper does not identify its two circulants, so these cannot be asserted to be the same specimens.

Characteristic-polynomial trace checks: 69 rows including overlaps, 44 vertex-transitive. Every trace agrees with the separately computed inverse; every vertex-transitive variance agrees exactly with the corollary.

## Exact spectral checks for the three introduction examples

- K6: P spectrum (eigenvalue: multiplicity) {'1': 1, '-1/5': 5}; trace=27/4; variance=8/3.
- K6 minus matching: P spectrum (eigenvalue: multiplicity) {'1': 1, '-1/2': 2, '0': 3}; trace=15/2; variance=12/5.
- K6 minus (C6): P spectrum (eigenvalue: multiplicity) {'1': 1, '1/3': 1, '-2/3': 2, '0': 2}; trace=37/4; variance=72/37.

Command:
```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 spectral_check.py
```

## Attributions and novelty, from memory only

I do not confidently remember a paper proving this exact maximality statement or the precise vertex-transitive formula. I also do not remember the weighted inverse-diagonal identity explicitly in the named antivoter references. This does not establish novelty. The trace identity itself is a standard elementary consequence of a Sylvester equation; an equivalent formulation in the older Stein or random-walk duality literature remains possible. I cannot certify priority without those sources.

| Citation | Memory-based assessment |
| --- | --- |
| Aldous–Fill | Moderate confidence in the regular-graph antivoter setting, variance discussion, and complete-graph extremal question. Exact proposition numbers, κ convention, and wording not certified. |
| Donnelly–Welsh | Familiar early antivoter attribution; recurrent-state description is consistent with the checks. Precise general irreducibility hypotheses not verified from the source. |
| Matloff | Dissonant-voting attribution is consistent with low-to-moderate-confidence recall; precise setting and metadata unverified. |
| Rinott–Rotar | Moderate-to-high confidence that this work treats coupling/normal approximation for the antivoter model. No recalled result settling this paper's exact maximum or formula. |
| Ross | Moderate confidence that the survey uses antivoter dynamics as an exchangeable-pairs example. No confident recollection of these sharper identities there. |
| Röllin | Translated-Poisson/exchangeable-pair subject is familiar; the exact antivoter rate is not. “The same rate” is too unspecified to certify. |
| Chen–Fang–Shao | Stein/moderate-deviation attribution is plausible; low confidence about the precise complete-graph antivoter application without the source. |
| Huber–Reinert | Title and general sampling/approximation subject are familiar; the specific multipartite comparison and its metric are not confidently recalled. |
| Math Brain / Brain Framework | Project/provenance references were not inspected and are not needed for the mathematical proofs. |

I have no concrete remembered contradiction to these work descriptions, and no basis for asserting that they establish novelty. I have not invented any additional reference. Precise dates, page ranges, DOI targets, rate comparisons, and original hypotheses remain source-verification work.

## Errors, typos, and unclear sentences

1. **Lines 78–80, false regular-bipartite rationale.** Replace the sentence with: “For connected regular bipartite graphs all stationary laws are supported on the two proper colourings and S=0. We assume non-bipartiteness so that I+P is invertible.” If retaining the n² observation, explicitly restrict it to possibly irregular bipartite graphs.
2. **Line 46, graph convention.** Add “simple undirected.” With loops, P(u,u)=0 fails; with unrestricted multigraphs, identifying equality with the graph K_n needs qualification. This is an implicit conventional hypothesis, not a detected failure for ordinary simple graphs.
3. **Lines 47–48, clock convention.** “Independent rate-one Poisson clocks” would make the standard continuous-time construction fully explicit; the present generator interpretation is already clear.
4. **Lines 54–55, “the same rate.”** Specify the rate, its parameters, which theorem it matches, and the metric in each approximation problem.
5. **Line 60, κ.** Define the cut parameter and its normalization rather than only calling it “a cut parameter.” If κ=|E|−MaxCut(G), the stated bound follows as derived above.
6. **Lines 94 and 221, graph products.** State that × denotes Cartesian product, or use the usual □ notation. The name “prism” disambiguates the first example, but the notation can otherwise mean a different graph product.
7. **Line 131 after line 114, m notation.** The inverse diagonal m_u reuses m_v from the earlier mean-vector proof. The scopes differ, so this is harmless, but another symbol would ease reading.
8. **Lines 235 and 238–239, graph identification and “exact.”** Name the two 4-regular graphs as complements of C_7 and C_3+C_4, and either give fractions or say the table shows rounded exact solutions. The displayed decimals themselves are correct.
9. **Lines 217–221, numerical reproducibility.** Identify the eight graphs, the random seed and generation method, or an immutable data/code snapshot. Two unnamed circulants and an external link do not identify the supplied run.
10. **Line 267, “No data were used.”** This is ambiguous beside a computational table and saved outputs. “No external or empirical data were used” would distinguish that assertion from the generated numerical data.
11. **Line 272, bibliography width.** There are eleven bibitems but thebibliography uses {9}. Use {99} so the label width accommodates the two-digit entries; the exact typesetting effect was not compiled.

I found no misspelled mathematical symbol, wrong table rounding, or further algebraic typo. These are the errors and unclear phrases I noticed, not a guarantee about typography after compilation.

## Limits of this audit

- The actual Aldous–Fill text and the other cited works were unavailable in the folder. Their wording, precise numbering, literature coverage, and novelty were assessed only to the limited extent described above; no browsing was used.
- The authors' original 297 random graphs, original floating-point tolerances, and unnamed two circulants were not reproduced. The independently checked exhaustive table and all named numerical assertions do agree.
- The LaTeX was not compiled. Funding, affiliations, grant numbers, conflicts, AI-version/provenance claims, and repository availability were not verified.
- Exhaustive graph enumeration stops at eight vertices. Additional named/family tests extend to twelve vertices. Numerical testing supports, but does not replace, the fully checked proof.

The original source hash and program/output hashes are recorded in audit_manifest.json. The two principal exact runs took about 7.6 seconds and 0.7 seconds respectively, each with about 21 MiB peak RSS. The spectral run took under one second; its measured RSS is in spectral_checks.json. All completed computations stayed below five minutes and 1 GB. The attempted hard address-space limit failed before any enumeration; the successful runs used the documented soft-limit requests, a 240-second alarm, and measured memory. Work was sequential except for one brief overlap between the two small numerical invocations; no more than two computation processes ran.

Task: “You are refereeing a mathematical paper that is already public but has had no outside audit.” Owner request received 2026-11-12, approximately 04:44 Asia/Tbilisi (launcher/start record; no exact message timestamp was supplied).

Final verdict: **SOUND**.
