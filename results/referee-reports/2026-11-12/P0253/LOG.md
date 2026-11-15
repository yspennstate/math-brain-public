# Independent referee log

Task: “You are refereeing a mathematical paper that is already public but has had no outside audit.” Started 2026-11-12 04:44 Asia/Tbilisi.

Scope: PAPER.tex is read only. No browsing, external writes, other agents, or author programs. All audit programs and outputs stay here. The later task-specific restriction against outside writes overrides the earlier global mesh/checklist/memory write instructions; no shared-state tools are being run. Computations will use one worker, a time limit below five minutes per invocation, and a memory limit below 1 GB.

## 1. Introduction and setting

**CORRECT**, lines 46–48: the update rule specifies continuous time, rate one at each vertex, a uniform neighbour, and the opposite opinion. Independent Poisson clocks and a finite *simple undirected* graph should be said explicitly. The usual simple-graph convention is needed later for P(u,u)=0 and for the equality case.

**CORRECT**, eq:Kn, lines 61–64: independently, put k=#plus on K_n. The upward jump rate is (n-k)(n-k-1)/(n-1), and the downward rate is k(k-1)/(n-1). Thus LS=-2S and L(S²)=-4S²+2[n(n-2)+S²]/(n-1). Stationarity gives E S=0 and (4n-6)E S²=2n(n-2), so Var S=n(n-2)/(2n-3). The recurrent class is all nonconstant configurations and its unique stationary law is permutation invariant; n+n(n-1)c=Var S gives c=-1/(2n-3). This calculation does not assume the claimed pair equations.

**CORRECT as mathematics; attribution unverified**, lines 59–66: Var S<n/2 follows from the bound claimed here, and also directly from the weaker inverse-diagonal argument audited below. I recall Aldous–Fill discussing the antivoter model, its variance, and a complete-graph extremal question in the regular setting, but do not confidently remember the proposition numbers, cut-parameter normalization, or exact wording of the question. No book text was provided; these bibliographic assertions cannot be certified from memory alone.

**CORRECT**, lines 69–78, about *every* stationary law: the proof needs stationarity, not irreducibility. Reducibility does not imply several stationary laws. On C_(2r+1), the number of monochromatic edges is odd, cannot increase, and the unique closed class has exactly one such edge (2n configurations). Its uniform stationary law has S=±1 equally, hence Var S=1. For C_3 all six nonconstant states already form this class; for C_5 and longer odd cycles there are transient nonconstant states. A defect can move around the cycle and its circuit reverses the global sign, so the 2n states communicate. Multiple defects can be moved together and annihilated; thus no other closed class. The paper does not actually assert multiple stationary laws on odd cycles.

**CORRECT**, constants do not obstruct the proof: an all-plus or all-minus configuration has exit rate n and has no incoming transition from any other configuration. To reach all plus, the last minus would need to copy the opposite of another minus, but no such neighbour exists. Therefore constants have stationary mass zero and cannot be reached from a nonconstant starting state. They can only be present initially. They are never absorbing here.

**WRONG in the stated regular setting**, lines 78–80: “Bipartite graphs are excluded because ... Var S can be of order n².” In a connected d-regular bipartite graph, d|A|=|E|=d|B|, so |A|=|B| and S=0 in both proper colourings and in every stationary mixture. Consequently Var S=0. The two-point support description and S=±(|A|-|B|) are correct for connected bipartite graphs generally; order n² requires *irregular* examples (a star with an equal mixture has variance (n-2)²). The real proof obstruction is the eigenvalue -1 of P, so Q is singular and vertex means need not vanish. On C_4 or K_(3,3), each of the two point-mass stationary laws has nonzero individual means, although S=0 and the desired upper bound holds. No change to the non-bipartite theorem is required.

**CORRECT**, lines 82–89, spectral hypotheses: for a connected simple undirected regular graph, P is symmetric, 1 is simple, all eigenvalues lie in [-1,1], and -1 occurs exactly in the bipartite case. The corollary and numerical examples will be audited at step 6.

**GAP (editorial scope)**, line 46: “a finite connected d-regular graph” does not explicitly exclude loops, multiple edges, or directed edges. Standard usage often supplies simplicity and undirectedness; the theorem should state it, since its proof uses it. This is not a gap under the conventional simple undirected graph reading.

## 2. Lemma lem:eq, independently derived

**CORRECT**, lines 99–101: C is symmetric with unit diagonal, Q=I+P is symmetric positive definite, and Q1=2·1. Non-bipartiteness supplies strict positivity; regularity supplies symmetry with respect to ordinary counting measure.

**CORRECT**, lines 112–114: Lη_v=-η_v-Σ_u P(v,u)η_u. For a stationary law, Qm=0, hence m=0. This uses only stationarity and invertibility, not uniqueness of that law or spin-flip symmetry.

**CORRECT**, display at lines 116–118: for v≠w,

L(η_vη_w)=-2η_vη_w-Σ_u P(v,u)η_uη_w-Σ_u P(w,u)η_vη_u.

If v∼w, the u=w term of the first sum contributes -P(v,w), since the updated product is (-η_w)η_w=-1; the other endpoint contributes another -P(w,v). The signs in the paper include both contributions correctly. Simultaneous clock rings have probability zero. Taking expectations gives precisely the displayed equation.

**CORRECT**, lines 119–121 and eq:syl: off-diagonal entries of QC+CQ vanish. Its diagonal is 2+2Σ_uP(v,u)c(u,v), because P and C are symmetric. Each c(u,v)∈[-1,1], so δ_v≥0. More explicitly δ_v=4·(mean over neighbours of P{η_u=η_v}), which makes the nonnegativity transparent. The equation QC+CQ=0 at line 119 is explicitly restricted to off-diagonal entries and is not a claim that the full matrix vanishes.

**CORRECT**, lines 122–123 and lemma's final sentence: 1ᵀ(QC+CQ)1=4·1ᵀC1=Σδ_v, and mean zero gives Var S=1ᵀC1=(1/4)Σδ_v. Multiplication “by 1 on both sides” means 1ᵀ on the left and 1 on the right.

**CORRECT**, lines 126–128, mathematical identity: Σ_vδ_v=2n+(4/d)Σ_{unordered edges}c(u,v), hence Var S=n/2+(1/d)Σ_edges c=n(1+cbar)/2. The average is over unordered edges; no factor of two is missing. Exact attributions to AF Lemma 14.20 and Corollary 14.24 remain unverified from memory.

## 3. Lemma lem:rep

**CORRECT**, lines 138–139: orthogonally diagonalizing Q gives the symmetric-matrix eigenvectors q_iq_iᵀ and q_iq_jᵀ+q_jq_iᵀ, with eigenvalues q_i+q_j>0 (where here q_i=1+λ_i). This proves invertibility on symmetric matrices; it also holds on all matrices. The symbol m_u is reused here for an inverse diagonal after m_v denoted a mean in the preceding proof; the scopes differ, so this is only a minor notation issue.

**CORRECT**, lines 139–144: all eigenvalues of Q are positive, so the integral converges exponentially. Differentiating e^(-tQ)De^(-tQ) and integrating gives QC+CQ=D, with the boundary at 0 contributing +D. Invertibility proves the representation. Symmetry and diagonal D give c(v,v)=Σ_uδ_u∫(e^(-tQ))_(vu)²dt.

**CORRECT**, lines 146–148: Σ_v(e^(-tQ))_(vu)²=(e^(-2tQ))_(uu). The integral is (1/2)(Q^(-1))_(uu), *not* (Q^(-1))_(uu). Thus n=(1/2)Σ_uδ_um_u and the lemma's Σ_uδ_um_u=2n has the correct factor. As an independent shorter derivation, multiply QC+CQ=D on the left by Q^(-1) and take traces: tr(C)+tr(Q^(-1)CQ)=2tr C=2n=tr(Q^(-1)D).

**CORRECT**, non-bipartiteness is used exactly to exclude λ=-1 and thereby permit Q^(-1), uniqueness of the Sylvester solution, and exponential convergence of the integral. It already entered the zero-mean argument in step 2. For a connected bipartite regular graph the alternating ±1 vector lies in ker Q.

## 4. Lemma lem:diag

**CORRECT**, lines 163–166: e_u=a+b, a=1/n, b⊥1, ||a||²=1/n, Q^(-1)a=a/2, and Q preserves the orthogonal complement of 1. Thus both cross terms vanish and aᵀQ^(-1)a=1/(2n).

**CORRECT**, lines 168–169: applying Cauchy–Schwarz to Q^(1/2)b and Q^(-1/2)b yields the stated inequality. Both vectors are nonzero (n≥3); equality holds exactly when Qb=αb. Positivity implies α>0, although its value is not needed at this step.

**CORRECT**, lines 170–172: bᵀb=(n-1)/n and bᵀQb=Q_uu-aᵀQa=1-2/n=(n-2)/n>0. Here Q_uu=1 uses absence of loops. Regularity and undirectedness were used earlier in the orthogonal decomposition.

**CORRECT**, lines 174–176: the lower bound is 1/(2n)+(n-1)²/[n(n-2)]=[(n-2)+2(n-1)²]/[2n(n-2)]=(2n-3)/[2(n-2)]. At n=3 it is 3/2, finite and attained on the only admissible graph K_3.

**CORRECT**, lines 178–182, equality: symmetry of P gives Pe_u=(1/d)1_N(u), hence Pb=(1/d)1_N(u)-(1/n)1. If Pb=μb, coordinate u forces μ=-1/(n-1); any nonneighbour other than u forces μ=1, a contradiction for n≥3. If there is no nonneighbour, this contradiction is unnecessary: d=n-1 by simplicity, regularity then forces G=K_n, and every neighbour coordinate does satisfy μ=-1/(n-1). The proof covers N(u)∪{u}=V and n=3 correctly. The stated equality “u adjacent to every other vertex” is equivalent to G=K_n under regularity.

**CORRECT**, lines 185–187: (e_uᵀQe_u)(e_uᵀQ^(-1)e_u)≥1 gives m_u≥1, so 2n≥Σδ_u=4 Var S. In fact m_u>1 because e_u cannot be an eigenvector of Q when d>0 (there is a nonzero neighbour coordinate of Qe_u). Since Σδ_u>0, this weaker argument also gives the strict Var S<n/2 attributed to AF. “Something near 1” is heuristic prose, not a spectral hypothesis.

## 5. Theorem thm:main — proof audit before computation

**CORRECT**, lines 192–196: δ_u≥0 and m_u≥m* imply 2n=Σδ_um_u≥m*Σδ_u=4m*Var S, and division by positive 4m* gives the claimed upper bound. The inequality direction is right: a lower bound on the inverse diagonals becomes an upper bound on variance.

**CORRECT**, lines 196–198: a vertex adjacent to all others has degree n-1, and regularity then forces every vertex to have that degree. Therefore G≠K_n makes all m_u>m*. The identity Σδ_um_u=2n>0, with m_u finite positive and δ_u≥0, implies at least one δ_u>0, so the inequality is strict. No irreducibility or full support is used. On K_n all m_u=m*, so equality follows for any stationary law, independently of the earlier complete-graph calculation.

### Step 5 computation verdict, reached before step 6

**CORRECT on every tested graph**. `audit_exact.py --phase enumerate` generated every labelled regular graph in degrees d≤(n-1)/2 for 3≤n≤8, classified them with an independently written graph-isomorphism backtracker, and used complementation for the remaining degrees. No graph catalogue or authors' program was used. A second, grouped-degree-sequence counting recurrence in `validate_results.py` independently matched all labelled generation counts. Connected non-bipartite isomorphism-class counts for n=3,...,8 are 1,1,2,3,4,14, totalling 25. Rational solutions satisfy the correlation equations, the variance identity, δ≥0, the inverse-diagonal bound and its strict equality characterization, and Σδ_um_u=2n.

For all seven non-bipartite classes on at most six vertices, a separately constructed generator on all 2^n spin states was decomposed into strongly connected components; each closed component's stationary law was solved exactly, normalized, and checked against every original generator column. All pair correlations, all zero vertex means, and every variance agree with the separate correlation solution. The reducible C_5 has a single closed class of size 10. All ten connected regular graphs on at most six vertices were checked, including the bipartite controls C_4, C_6, K_(3,3): their two extremal stationary laws each have S=0 and nonzero vertex means. The JSON contains every state and exact probability of every extremal law, so all stationary mixtures are covered.

Additional rational checks cover C_3,C_5,C_7,C_9, the Petersen graph, the triangular prism, K_n minus a perfect matching for n=6,8,10,12, and all connected non-bipartite K_n minus a 2-factor for 5≤n≤12 (every partition of n into cycle lengths ≥3), plus C_3 Cartesian C_3. The disconnected-looking complements C_3+C_4 and C_3+C_5 are included, so non-transitivity is not being silently assumed away.

The largest ratio on a non-complete graph in the exhaustive 3–8 range is **26/27**, for K_8 minus a perfect matching (Var S=32/9). Across the entire tested set it is **84/85**, for K_12 minus a perfect matching (Var S=96/17). These are maxima of the specified finite tests, not bounds on all graph sizes. Petersen gives 40/13; odd cycles give 1; prism gives 72/37; octahedron gives 12/5.

Tables and exact reproduction commands are in `step5_tables.md`; raw rational matrices, edge lists, full stationary laws, and timings are in `exact_enumerate.json` and `exact_families.json`. Enumeration used 7.595 seconds / 20.8 MiB peak RSS; the additional-family run used 0.690 seconds / 20.8 MiB. The initial attempt to set a macOS address-space limit failed before computation; the revised program requests data/RSS limits, checks measured RSS, and uses a 240-second wall alarm. No computation approached the memory or time limits.

## 6. Corollary cor:vt — proof audit

**CORRECT**, lines 202–205: for two symmetric solutions, E has zero diagonal and QE+EQ=F diagonal. The Sylvester representation gives E=∫H(t)F H(t)dt, H(t)=e^(-tQ), so diag(E)=Mf with M=∫H(t)∘H(t)dt. Each H(t) is positive definite, not merely positive semidefinite; its Hadamard square is positive definite by the strict Schur product theorem. Explicitly, for z≠0, zᵀ(H∘H)z=||H^(1/2)diag(z)H^(1/2)||_F²>0. The integral is finite and positive definite. Alternatively H(0)∘H(0)=I and continuity make its integral over a short interval already positive definite. Thus Mf=0 implies f=0 and then E=0. There is no semidefinite-versus-definite gap.

**CORRECT**, lines 206–209: graph automorphisms preserve the equations and unit diagonal. Uniqueness of their solution makes C invariant even if one did not know whether the underlying stationary law was unique. Consequently δ and the inverse diagonal m are constant on vertex-transitive graphs. This is consistent with step 1: C_5 is reducible but has one stationary law; even hypothetical distinct stationary laws would still have the same first and second moments by the argument here. Bipartite mixtures do not contradict this, since Q is singular there and the uniqueness argument does not apply.

**CORRECT**, lines 209–210 and cor:vt: Σδ_um_u=δ tr Q^(-1)=2n and Var S=nδ/4 give Var S=n²/[2tr Q^(-1)]=n²/[2Σ_i(1+λ_i)^(-1)]. Uniqueness of C is stronger than necessary for the scalar formula: constancy of the inverse diagonal alone suffices in the weighted trace identity.

**CORRECT**, introduction lines 92–95, symbolic examples: K_n has spectrum 1,-1/(n-1)^(n-1); octahedron has 1,0,0,0,-1/2,-1/2, trace inverse 15/2 and variance 12/5=36/15; triangular prism has 1,1/3,0,0,-2/3,-2/3, trace inverse 37/4 and variance 72/37=36/18.5≈1.9459459459. Independent spectral and manuscript-table checks follow.

### Step 6 computation verdict

**CORRECT**, every entry of tab:small, lines 229–235: K_4=8/5→1.6000; K_5=15/7→2.1429; K_6=8/3→2.6667; octahedron=12/5→2.4000; triangular prism=72/37→1.9459; K_7=35/11→3.1818; K_7 minus C_7=203/75→2.7067; K_7 minus (C_3+C_4)=249/101→2.4653. The two unnamed 4-regular graphs are exactly these complements. The enumeration confirms the table is exhaustive through n=7 after cycles are excluded (K_3 is itself a cycle).

**CORRECT**, exact spectral checks: `spectral_check.py` computed each adjacency characteristic polynomial independently using SymPy. For g(x)=det(xI-A), tr Q^(-1)=-d g'(-d)/g(-d), a computation separate from the rational linear-system inverses. All 69 rows checked (including overlaps and two explicitly specified circulants) agree; all 44 vertex-transitive rows give precisely the correlation variance by the corollary. Vertex transitivity was checked by a separately written automorphism backtracker, rather than assumed from names. Three displayed introductory spectra were also recovered exactly from the matrices.

The eight explicitly identified vertex-transitive examples in `step6_tables.md` include K_6, octahedron, prism, Petersen, C_3 Cartesian C_3, C_7, and the circulants with steps ±1,±2 modulo 7 and 8. Their variances are 8/3, 12/5, 72/37, 40/13, 45/13, 1, 203/75, 448/141. The paper does not identify its own two circulants, so the last two are independent examples, not a claimed reproduction of the authors' unnamed specimens.

**GAP (reproducibility evidence only)**, lines 217–221: “297 random ... graphs” and “within 4·10^(-15) on eight ... graphs”. The input graph lists, random seed, and original output are not present in the supplied folder. The linked repository cannot be inspected under the no-browsing rule. The finite exhaustive claim and all named numerical values have been independently checked; the particular 297-graph run, exact membership of its eight-example list, and its stated floating-point discrepancy have not. This is not a gap in either mathematical proof.

## 7. Attributions and novelty — memory only

I do **not** confidently remember a prior proof of this exact complete-graph maximality theorem, of the precise vertex-transitive reciprocal-resolvent formula, or of the weighted inverse-diagonal identity in the named antivoter literature. This is a limit of recall, not evidence that the results are new. No novelty certification is possible here. The identity in lem:rep is a generic Lyapunov/Sylvester trace identity (see the independent two-line trace proof in step 3); it is elementary linear algebra once the correlation equation has been obtained. Prior appearances in an equivalent duality or Stein identity formulation remain possible.

- **AF**, lines 59–66, 127–128, 185–186, 273–274: I recall a regular-graph antivoter discussion, variance bounds, and the complete-graph extremal question, with moderate confidence in this general attribution. I do not recall the exact proposition/lemma/corollary numbers, cut parameter definition or normalization, wording of the final question, or source version well enough to certify them. All mathematical formulas actually used in this paper were independently derived above. **GAP in source verification**, not proof.
- **Matloff**, lines 48–49 and 282–283: the dissonant-voting attribution and title are consistent with my recollection (low-to-moderate confidence). I cannot verify lattice setting, date, pagination, or DOI here. No remembered contradiction; description provisionally fair.
- **DW**, lines 50–52 and 277–278: Donnelly–Welsh is a familiar early antivoter reference; the recurrent-state description is consistent with the independently checked cases and the elementary bipartite gauge transformation to the voter model. The general irreducibility theorem is not re-proved by these finite checks and I cannot certify its precise original hypotheses from memory. Description provisionally fair with moderate confidence.
- **RR**, lines 53–54 and 284–286: I recognize Rinott–Rotar's use of exchangeable-pair/coupling normal approximation for dependent sums, including the antivoter model (moderate-to-high confidence in the subject attribution). I do not recall a result settling this variance maximum or the exact resolvent formula. Description appears fair; precise metadata and novelty unverified.
- **Ross**, lines 53–54 and 289: I recognize the Stein's-method survey and the antivoter model as a standard exchangeable-pairs example (moderate confidence). The variance/edge-correlation identity is natural in that approach. I do not recall the stronger identities here appearing in that survey. Description appears fair; no exact theorem/page certification.
- **Rol**, lines 54–55 and 287–288: I recognize Röllin's translated-Poisson/exchangeable-pair work (moderate confidence in the bibliographic subject), but do not remember the exact antivoter application or rate. **GAP in exposition/source verification**: “obtains the same rate” does not specify which rate, parameters, metric, or comparison theorem. The title is compatible with the prose but does not establish that assertion.
- **CFS**, lines 55 and 275–276: the moderate-deviation/Stein-identities attribution is plausible, but I have low confidence about the specific complete-graph antivoter application without the source. Provisionally compatible; not verified.
- **HR**, lines 55–57 and 279–281: the title is familiar and consistent with exact sampling/stationary-distribution approximation (low-to-moderate confidence). I cannot verify from recall the precise multipartite comparison, its metric, or scope. No remembered contradiction; no claim of verified novelty against it.
- **MathBrainRepo, MathBrainPaper, BrainFramework**, lines 253, 270, 290–295: these are project/provenance references, not mathematical support for the theorem. Their existence, contents, dates, and the claims about how the research was performed were not checked. Funding, affiliations, conflicts, grant numbers, AI-model/version attribution, and repository availability were also not independently verified.

There is no invented prior citation in this audit. Bibliographic metadata, fair comparison of exact rates, and priority require the actual sources; the author's no-browsing restriction was respected.

## Final audit status

All numbered mathematical statements, displayed equations, and load-bearing proof steps are **CORRECT** under the usual finite simple undirected graph convention. The introduction's order-n² justification for excluding *regular* bipartite graphs is **WRONG** and should be replaced. Explicit simplicity and a precise comparison rate would improve the exposition. The source/novelty and original random-run claims remain unverified. `REPORT.md` records the overall verdict and includes both numerical tables and all reproduction commands.
