# exact target, quantifiers, hypotheses and units

Run: 20261011T210330Z-account05-A001-quantifier-audit. Agent A001, stream B01. Artifact: source-bound quantifier audit. Full FEI remains OPEN. Independent acceptance of this audit is pending.

The target is

\[
\exists C\in[0,\infty)\ \forall n\in\mathbb N_0\ \forall f:\{-1,1\}^n\to\{-1,1\},\qquad H_2(f)\le C I(f).
\]

Here \(\widehat f(S)=2^{-n}\sum_x f(x)\prod_{i\in S}x_i\), \(P_f(S)=\widehat f(S)^2\), \(H_2(f)=\sum_SP_f(S)\log_2(1/P_f(S))\), and \(I(f)=\sum_S|S|P_f(S)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})]\). Set \(0\log(1/0)=0\). Constants, including the zero-dimensional cube, have H=I=0. Ratios are taken only for nonconstant functions, equivalently I>0. The assertion \(\forall n\exists C_n\) is weaker and elementary; it is not FEI.

Equivalently, \(C_{\rm FEI}=\sup_{n,f:I(f)>0}H_2(f)/I(f)<\infty\). A disproof requires actual Boolean signs \(f_j\) with \(H_2(f_j)/I(f_j)\to\infty\). Refuting a proposed constant, a local payment, or a non-Boolean relaxation does not satisfy this target. Natural-log entropy is \(H_{\rm nat}=(\ln2)H_2\).

Use \(D_{\rm char}=\sum_i\min(I_i,1-I_i)\), \(v=\operatorname{Var}(f)\), and \(\delta=I-v\). These are distinct from dual total correlation, physical pivotal influence under biased measures, and the influence drop of a restriction. Uniform H+ is the nonempty-atom contribution; under biases it includes the product-basis correction and can be negative.

# sources actually read, revisions and theorem locators

The complete provenance list, with SHA-256, byte count, encoding and line count, is [out/SOURCE_MANIFEST.json](out/SOURCE_MANIFEST.json). The helper reads every listed file and saves line-numbered versions of manuscript texts. Mathematical inspection focused on definitions, theorem interfaces, reduction proofs and scope statements; this run does not independently certify every analytic proof in the manuscripts.

Sources include all protocol-required campaign root files, the campaign TeX plan, all three earlier run REPORT.md files (B05, B09, B19), the five supplement entry files and twelve curated sources, the board, and these primary manuscript interfaces:

- **T38:** context/threshold_paper_38pp.txt, dated 11 October 2026; supplemented by baseline/current-threshold-paper.tex where PDF text drops mathematical symbols. Theorem A-D; Lemmas 2.1-2.2; Theorem 4.2; Corollary 4.3; Theorem 5.1; Proposition 5.5; Sections 5.7-5.8; Theorem 6.6; Proposition 7.1 and Corollaries 7.2-7.8; Propositions 8.1, 8.6, 8.9 and Corollaries 8.2-8.5, 8.7-8.10; Section 9.2.
- **T29:** earlier 29-page text; theorem index and corresponding composition/scope passages. Theorems A-D and 4.2, 5.1, 6.6 retain their roles. The later joint-witness/selector/activation sections are absent. Its Section 8 is the current Section 9's consequences, so citations cannot be transferred by section number.
- **R:** source_material/reductions/paper/{main,forests,restrictions,multiplexers,biased,conclusion}.tex. This is the campaign plan's *second recovered manuscript*, Restrictions and witness coding for the Fourier entropy-influence problem, separate from the percolation manuscript. Precise file/label locators appear below; a publication revision is not inferred from the downloaded tree.
- **P30:** context/percolation_spectral_pivotal_entropy_30pp.txt. Theorems 1.1-1.2, Lemma 2.1, Theorems 3.1-3.2, 4.4, Proposition 4.3, Corollary 3.3 and Section 12, plus Proposition 10.1's singularity scope.
- **P31:** the other 31-page version. Corresponding theorem interfaces and scope statements; its proof/source-verification wording differs, and its page count is not evidence of chronological priority.
- Supplement sources ERASURE_REDUCTION, BLOCK_RESTRICTION_IDENTITY, ERASURE_SYNERGY_AND_DUALITY, ROUTE_MAP_CURATED, GAMMA_ENDPOINT_LEDGER and the remaining source notes were read as navigation and scoped mathematical inputs. Claims whose complete originals are not bundled are not promoted to independently accepted theorems here.

EXECUTION_PROTOCOL revision is 2026-10-11-execution-v2. The protocol distinguishes public-paper metadata from the archived mathematical snapshot. This run pins the actual local bytes rather than asserting they equal a particular remote commit. The board is the supervisor's 2026-10-11 21:04 UTC snapshot: A001 had no prior stage. claude/B01/STREAM_NOTES.md was absent at the prescribed location; no contrary stream direction was available.

# complete derivation or exact first unsupported line

The following is the inventory of FEI sufficient conditions and reductions in T and R, together with the requested geometric manuscript. An identity or entropy lower bound is included where it is liable to be mistaken for an FEI upper-bound route. “Proved class theorem” means source-established at the stated scope, not newly independently accepted in this run.

| ID | Classification and exact scope | Source | First unsupported implication toward full FEI |
|---|---|---|---|
| T01 | Proved class: every regular (unate, one total desirability order) function has H <= Creg Dchar, Creg=log2(4+e)+2log2(e*pi)<8.937. Includes every deterministic weighted LTF and all character multiples. | T38 Theorem A; Lemma 2.2 | Every Boolean function is not shown to have such an order. “Regular” does not mean small weights. |
| T02 | Proved class: f=F(h1,...,hm), arbitrary outer F, regular hi, H <= [11.238+(17/5)log2 m]I and H <= [11.460+(22/5)log2 m]Dchar. | Theorem B | Arbitrary representation with bounded m, or removal of its log m cost. Taking hi=xi has m=n and does not give an absolute constant. |
| T03 | Proved class: unate gates with at most w desirability chains; add log2 w to T01 and to the T02 coefficients. | Theorem 4.2 | Bounded width for all functions, or paying the width term independently of w. Singleton chains only yield w=n. |
| T04 | Proved class: a Boolean labeling of one linear score with at most m transitions has ordinary coefficient 11.238+(12/5)log2 m and T02's centered consequences. | Corollary 4.3 | Uniformly bounded transitions for an arbitrary seed, or new payment for growing m. |
| T05 | Proved class: fixing k specified bits leaves regular restrictions; represent using those k literals and 2^k regular restrictions, so T02 gives O(k+1) coefficient. | Section 4.5, T38 lines 756-759 | Bounded k for arbitrary functions. Restrictions of a class remain in that class; the converse universal representation is unpaid. |
| T06 | Proved class: union/intersection of arbitrarily many outer gates, each a combination of <=M regular functions, each physical variable relevant to <=k outer gates. H <= [41+7log2 k+(29/5)log2 M]I; H+ <= [132+(118/5)log2 k+(106/5)log2 M](I-v). Chains add log2 w to ordinary coefficient, 2log2 w to FEI+ coefficient. | Theorem C / 5.1 | Uniformly controlled k,M,w or payment replacing their logarithms. General coherent outer composition is not this theorem. |
| T07 | One-way sufficient: a valid fixed queue reference and complete finite witness yield H <= h2(v)+v Lambda+sum_(A!=empty) P_f(A) min C(A). | Proposition 5.5, Section 5.8 | A representation/reference/witness choice with the complete residual <=K I uniformly, retaining roots, subset normalizers, ranks, attachments, child counts and labels. |
| T08 | Proved class: ordinary addressing has H=2a, I=1+a/2; the queue code gives H<10I, exact spectrum H=4(I-1). | Section 5.7; Corollary 8.2 | Extension of the whole-set payment to every Boolean spectrum. Addressing alone does not do this. |
| T09 | Proved biased gate class: every symmetric threshold under every product law has corrected H_mu+ <= CT (I_mu-Var_mu), CT=80+460/ln2<744. Deterministic inputs are frozen/deleted. | Theorem D / 6.6 | Weighted thresholds under arbitrary biases are not covered; see T15. |
| T10 | One-way composition theorem: disjoint input blocks, gate at the actual induced independent output biases, every constituent corrected FEI+ coefficient <=C implies composed coefficient <=C. a_i=I_i(g)/v_i, entropy and deficit both split with these weights. | Proposition 7.1; Corollary 7.2; R biased.tex biasfull:composition | A uniform gate inequality at all reached biases. Overlapping blocks have coefficient collisions; independent clones do not justify identifying occurrences. |
| T11 | Proved formula classes: read-once symmetric-threshold/parity formulas under arbitrary product laws, arbitrary depth/fan-in/negations, coefficient CT. Uniform full H<=744I and H<=747(I-v). AND/OR/parity have their separate smaller elementary gate constants. | Corollary 7.3; Lemma 7.5; Corollary 7.7 | Every Boolean function does not have a read-once realization by this basis with the same physical inputs. |
| T12 | Proved hybrid classes: disjoint uniform LTF terminal blocks; internal symmetric thresholds/parity at arbitrary means; arbitrary weighted LTF internal gates only with balanced nonconstant children; fixed-arity other gates with their established induced-bias constants. Coefficient is the maximum gate constant. | Corollary 7.4 | Remove the balance condition only after proving weighted biased FEI+, and separately pay physical variable reuse. |
| T13 | Proved balanced/mixed classes: read-once regular or character-regular gates, all nonconstant outputs below root balanced, H<=4Creg(I-v). More generally use 4Cm for T02 gates, T06's FEI+ coefficient, corresponding chain corrections, and unrestricted-bias symmetric thresholds/parity elsewhere. | Corollary 7.8 and following mixed-gate paragraph | Unbalanced internal regular gates need a new induced-bias theorem; growing gate parameters must stay in the maximum. |
| T14 | One-way conversion: uniform H+<=C(I-v) gives H<=max(C,log2 e)I and H<=(C+eta)(I-v), eta<2.553. | Lemma 7.6; Corollary 7.7 | The universal corrected FEI+ premise is unpaid; discarding the empty atom without this conversion is invalid. |
| T15 | Open class-extension target: absolute biased corrected FEI+ for every weighted LTF, uniformly in arity/weights/biases. | Section 9.2; R biased.tex | Precisely the displayed weighted-bias inequality. If proved it expands disjoint formula classes; no arbitrary-variable-reuse reduction to full FEI is established. |
| T16 | Proved selector identities/closure: cells partition independent controls; leaves balanced with pairwise disjoint nonempty Fourier supports. H=H(p)+sum pj[H(qj)+H(gj)], I=Dsel+sum pj I(gj). Affine cells codimension cj, dual-coordinate support rj give H=2sum pj cj+sum pj H(gj), I=(1/2)sum pj rj+sum pj I(gj). | Proposition 8.1; Corollary 8.2; R multiplexers.tex prop:subcubemux | Arbitrary cells' internal normalized spectrum or colliding leaf supports remain unpaid. Physical data blocks may overlap only under the stated Fourier separation. |
| T17 | One-way/class closures under T16 hypotheses: H(hj)<=Cs I(hj), H(gj)<=Cg(I(gj)-1) give H(F)<=max(Cs+4,Cg)(I(F)-1). Corrected cell FEI+ improves coefficient to max(Cs,Cg,4). Affine cells use max(4,Cg). | Corollaries 8.2-8.5 | The cell and leaf bounds with a common finite constant, plus separation, must be established. Removing these hypotheses silently inserts an arbitrary seed. |
| T18 | Proved shared-data class: fresh a-bit uniform selector, arbitrary common-data branches. Exact H=average H(gb)+a+sum RT[H(nuT)-H(rT)]; H<=average H(gb)+2a. If I_sel>=c a and branches H<=C I, conclude H<=max(2/c,C)I. Neighbor orthogonality gives c=1/2. | Proposition 8.6; Corollary 8.7; R prop:muxcollision, cor:muxorthogonal | A dimension-free positive c in a new class, or paying full collision cost when I_sel/a tends to zero. The 2a bound is not itself an influence payment. |
| T19 | Proved recursive class: fresh selector coordinates absent from both branches; neighboring branches orthogonal at each node; regular leaves; arbitrary depth/data reuse; H<=Creg I. R's earlier cor:thresholdmux gives the same type of threshold closure. | Corollary 8.8 | Arbitrary functions are not shown to admit this orthogonal fresh-selector hierarchy. Reused controls require a new proof. |
| T20 | Equivalence with the same optimal constant: all two-cell selectors Mg for balanced arbitrary g versus full FEI. | Section 8.3 | A uniform bound for the arbitrary-core selector class itself. Cheap label entropy alone does not pay cell entropy. |
| T21 | Equivalence with the same optimal constant: for every fixed eps,delta>0, point activations of arbitrary balanced cores with 0<I<=eps and Pr(F=-1)<=delta have supremum C_FEI. | Proposition 8.9; Corollary 8.10 | The arbitrary balanced-core bound; rarity does not decrease the optimal constant. |
| R01 | Equivalence with the same optimal constant: for each fixed eps>0,k>=0, simultaneously I<=eps, EF>=1-eps, max_i I_i/Var<=eps, and spectral-support distance>k retain supremum C_FEI. A stronger construction has distance>2k and all <=k-bit restrictions preserve H and mean and remain in the class. | R main.tex thm:simultaneous; lem:balanced,diffuse,activation,coding,codeexist,plateau | A uniform FEI estimate on that actual Boolean class; finite-depth plateaus and diffuse influences do not remove arbitrary seed difficulty. |
| R02 | Equivalence, including R01 conditions, with additional I<=2^(-s(N)) for any fixed nonnegative s(N)=o(N), N final dimension. | main.tex cor:subexponential | Uniform estimate at that subexponential scale. The known fixed linear exponent cN class is different and does not supply it. |
| R03 | One-way sufficient endpoint J: for each f choose an admissible gate union/ordered covers, one global feasible positive lambda vector and conditional laws on distinct actual partition-forest runs; residual R_f<=K I with one finite universal K implies C=2+Kref+K. | forests.tex thm:posteriorforest, eq:foresttarget | The residual inequality itself. Existence of finite covers/runs is insufficient. No reverse implication for this restricted reference family or equality of optimal constants is proved. |
| R04 | Proved fractional structured estimate: H<=C0 I+(48/5)sum alpha_j log2 S_j(lambda)+v log2 Z, C0<41; S_j=sum_(l,t) sqrt(q_jlt) M_l^(5/48)lambda_l^(-11/48). q is from disjoint physical signed pivotal pieces, gates combine regular inner gates. Outer-only estimate retains its sum of sqrt(q_jl)lambda_l^(-11/48). | forests.tex thm:fractionalforest, eq:outerfractional | Uniformly bound the complete influence-weighted logarithmic sum under a constructive cover and global feasible weights. The local Renyi half order here is not a bound on full spectral Renyi entropy. |
| R05 | One-way hereditary induction: restriction-closed class, every nonconstant member has relevant i with Delta_i H<=C I_i, then H<=C I. Threshold cutoff I_i>=tau gives coefficient kappa(tau)/tau by the scalar profile. | restrictions.tex prop:restrictioninduction, lem:kappaconcavity | Existence of such a uniformly paid split at every reached nonconstant member. FEI alone is not claimed here to imply a same-constant Delta selection. |
| R06 | Equivalence in finiteness: exists K finite, for every nonconstant Boolean f exists relevant i with B_i(f)<=K I_i(f). FEI(C) implies selection with K=C; selection(K) implies FEI(K+2/ln2). | restrictions.tex prop:restrictioninduction | Proving any finite universal K. The quantifier is exists i, not every i or maximum-influence i. Optimal constants are not identified. |
| R07 | One-way tree/block criterion: actual adaptive physical restrictions; expected full path decrements plus terminal H paid by root influence. Block decrement = conditional spectral erasure + channel term, channel <=(2/ln2) I_W; influence telescope exact. A bound on cumulative erasure by K times queried influence plus leaves with constant L gives max(K+2/ln2,L). | restrictions.tex eq:treetelescopeH/I, prop:blockincrement | A measurable proper-block/stopping rule with uniform cumulative payment and certified leaves. W=all inputs returns H as the purported erasure payment. |
| R08 | One-way centered induction: at each nonterminal noncharacter node choose i with Delta_i H<=C d_i^D, where d_i^D=Dchar-parent average Dchar(children)>=min(I_i,1-I_i); telescopes to H<=C Dchar. | restrictions.tex prop:centerbudget and following paragraph | The selection bound. If max I_i<=1/4, d_i^D=I_i at every split; centering has no gain there. |
| R09 | Exact FEI equivalence at fixed constant C: a symmetric nonnegative finite Gamma on dyadic probabilities, Gamma(1/2)<=C, satisfies Gamma(pout)+H_nu(G)<=sum_i I_i^nu(G)[Gamma(pi)+h2(4pi(1-pi))]/[4pi(1-pi)] for every finite Boolean gate and every interior dyadic bias vector. | biased.tex biasfull:gatepotential and biasfull:gammaslack | Construct and prove Gamma independently of FEI. Defining Gamma_C by an infimum of C I-H assumes its nonnegativity from the desired FEI statement. No extension to all real biases is established. |
| R10 | One-way encoder inference: unbiased encoders of prescribed dyadic output biases allow raw composition with coefficients R_C(g)=[C I(g)-H+(g)]/Var(g). Conjunction encoders have R_C=2+[C/(2(1-p))-2]log2(1/p). | biased.tex biasfull:encoding, biasfull:encoderslack | Uniform control of encoder slack is absent; if C exceeds a valid C0, every encoder incurs a logarithm at rare p. Uniform FEI does not automatically prove biased FEI+ by this substitution. |
| R11 | Failed transfers, not sufficient conditions: all-coordinate local charge, maximum-I or maximum-dD split, separable influence potentials with O(t) near zero, and variable cloning followed by diagonal identification. | restrictions.tex prop:bentsplice, cor:badmaximum, prop:separablepotential; conclusion.tex prop:cloning | These edges are refuted at their precise scopes. The independent-clone majority example has clone H,I->0 while identified majority has H>=2. No universal diagonal entropy transfer is available. |
| P01 | One-way abstract encoding: rooted refinement forest, branching <=b, terminal capacity <=M, entropy bounded by root entropy plus expected occupied masks and leaf contents. | P30 Lemma 2.1 | For arbitrary Boolean spectra, a hierarchy whose entire expected occupancy cost is O(I); the mask chain rule alone has no such bound. |
| P02 | Proved conditional geometric criterion: four-arm quasi-multiplicativity/fixed-factor regularity, pi4(u,t)>=c(u/t)^(2-eps), location-uniform bulk four-arm upper comparison and half-plane three-arm bound C(r/t)^beta with beta>1 yield H(S),H(P)<=C m(R). Additional I>=c m(R) gives influence upper bounds; biases bounded away from endpoints give H(S)<=C J. | P30 Proposition 4.3; Theorem 4.4 | The geometric assumptions and lower influence comparison do not hold by definition for arbitrary Boolean functions. Removing them is a new theorem. |
| P03 | Proved class: bounded-aspect critical square-bond rectangles and triangular-site rectangles with px in [p,1-p], p in [p0,1/2], R<=L_eta(p). H(S) comparable to J, H(P) comparable to physical I, uniform in location/profile with constants depending on fixed p0,eta,aspect/lattice conventions. Nonroot retained-scale entropy comparable to m(R)/m(s). Fair inputs give FEI. | Theorems 1.1-1.2; Section 5-6 | An embedding of arbitrary Boolean signs into these crossings with a paid ratio-preserving ledger is not supplied. Small R outside the cutoff can be separately handled by bounded finite dimension for fixed conventions. |
| P04 | Proved LOWER bounds: monotone pivotal H(P)+H(f conditional on P)>=sum h2(pi)I_i; uniform H(P)>=I-1. Local guards of bounded size and overlap force exponential spectral-atom upper bounds, hence entropy LOWER bound. | Theorems 3.1-3.2; Corollary 3.3 | Neither is an entropy upper bound. Equal one/two-coordinate marginals of spectral and pivotal sets do not transfer their full Shannon entropies. |
| P05 | Proved conditional singularity criterion: uniform local Fourier coercivity under every exterior operator, bounded disjoint-block coloring, spectral tested size escaping, and comparison laws forbidding the local pattern yield discrete asymptotic singularity. | Proposition 10.1, Theorem 10.3, Section 12 | This is not an FEI route. General Jordan-quad singularity does not assert general-quad entropy; microscopic separation does not establish continuum singularity. |

The percolation paper is an additional requested source, not a substitute for R. Its lower bounds, singularity, transport and thinning statements have no implicit edge to universal FEI. T's read-k DNF concentration corollary is downstream of T06 and introduces no additional sufficient condition for full FEI.

R's monotone dual-rail embedding (biased.tex biasfull:dualrail) is another failed transfer shortcut, not a universal reduction with paid cost. Conditioning independent rail pairs to decode fair bits has valid-event probability at most 2^(-n) and KL cost at least n ln2. That explicit dimension cost must be paid before importing a monotone class theorem. The statement concerns this embedding, not all monotone encodings. The weighted-threshold normalization no-gos in biasfull:tribes, biasfull:mixture, the failure theorem and local-TC proposition similarly refute precise proposed physical-TC/pivotal-credit payments, rather than the weighted corrected FEI+ target T15 itself.

The supplement introduces further targets beyond these manuscripts: mismatch/KL tree payment (G-R-MISMATCH), actual-source history transfer, weighted reveal lifetime, full signed Booleanity and fixed-cyclic conditional completion. Their quantifier audit follows below; none is accepted as a new universal premise.

**Endpoint J explicitly.** With one fixed representation and global lambda, set pi_l=min(Pr(h_l=1),1/2), Lambda=sum log2(1+lambda_l pi_l), Z=1-2^(-Lambda), and Kref=3+2log2 3+log2(6e). For actual partition runs with subsets A_l partitioning A,

\[
B_\lambda=\sum_{l\in\mathcal F}[\log_2(1/\lambda_l)+s_l\log_2 M_l+(6/5)s_l\log_2(\kappa_l/s_l)]
 +\sum_{l\in\mathcal R}\log_2(1/\pi_l)+(6/(5\ln2))\sum_{j\in A}F_{\tau(j)}^j(A).
\]

The source proves \(H\le h_2(v)+K_{\rm ref}I+R_f\), with

\[
R_f=v(\Lambda+\log_2 Z)+\sum_{A\ne\varnothing}P_f(A)
 [\mathbb E_{\mathcal P_A}B_\lambda(A;r)-H_2(\mathcal P_A)].
\]

Thus the unpaid line is \(\exists K<\infty\ \forall f\ \exists\text{admissible global representation, weights, conditional actual-run laws}:R_f\le KI(f)\). The packing constraint is sum_(l:j in R_l) lambda_l<=1 for every j. Laws may depend on A, but the reference generator and weights remain fixed for f. Actual runs must be distinct; counting abstract descriptions twice fabricates posterior credit. Conditioning contributes v log Z, which is nonpositive and cannot be dropped in a claim of exact equality. Since h2(v)<=2I, the forward constant is 2+Kref+K. No equivalence of optimal constants for this witness family is asserted.

**Good-coordinate equivalence reconstructed.** The exact Fourier split gives Delta_i H=B_i+M_i, 0<=M_i<=(2/ln2)I_i, and I=I_i+average child I. If every nonconstant reached function admits relevant i with B_i<=K I_i, induction starting at constant leaves proves H<=(K+2/ln2)I. Conversely conditioning reduces entropy in each term of a chain rule, so sum_i B_i<=H. If H<=C sum_i I_i and every positive-I coordinate had B_i>C I_i, summing would contradict this inequality; zero-I coordinates have B_i=0. This proves existence, with K=C, for each function. The reverse implication uses FEI as an explicit assumption; it cannot justify the selection premise in a purported FEI proof. There is no proved equality of the two optimal constants.

**Scalar and centered routes.** Concavity bounds Delta_i H<=kappa(I_i), but kappa(u)/u=log2(1/u)+3/ln2+O(u) diverges near zero. A restriction-closed class with a uniformly available I_i>=tau can use kappa(tau)/tau; availability is a structural assumption. Centering gives a nonnegative extra budget and a telescope, but low-influence nodes have none of that gain. The bent splice refutes all-coordinate bounded pricing and the source's diluted splice refutes maximum-I and maximum-dD selection; neither refutes existential R06.

**Tree and supplement mismatch.** For a finite uniform physical restriction tree with visitation probability pi_v, H(root)=sum pi_v Delta_v H+sum pi_leaf H(leaf), and the same formula holds for I with queried coordinate influences. Proving sum pi_v B_v<=K sum pi_v I_query plus leaf H<=L I_leaf suffices with coefficient max(K+2/ln2,L). A stronger source bound uses mismatch mass mu=sum(|ahat|-|bhat|)^2/4 and the charge mu[log2(1/mu)-D2(nu||q)+3/ln2]. The linear part is already paid by influence; the entire remaining logarithmic tree sum **and terminal entropy** still need payment. This mu is different from B05's influence-variation refund M. The B05 reviewed family refutes fixed-price L<=Kd+AV+BM at every split, while child budgets can remain ample. Its no-go is consumed as a route correction, not an FEI disproof.

**Elementary optimum-preserving reductions reconstructed.** On disjoint blocks, tensor spectra are products, so H(f^tensor t)=tH(f), I(f^tensor t)=tI(f). Balancing by a fresh sign gives g_t=z f^tensor t, H(g_t)=tH(f), I(g_t)=tI(f)+1. Hence balanced functions have the same optimal FEI constant as all functions, as an extended-real supremum. Character multiplication permutes atoms by symmetric difference and replaces I_i by either I_i or 1-I_i; consequently universal H<=C I is equivalent, at that same C, to universal H<=C Dchar. Lemma 2.2 then gives H<=4C(I-v). Conversely universal H+<=K(I-v) implies FEI(max(K,log2 e)); these strong/nonempty formulations are equivalent in finiteness, without an assertion of equal optimum.

For balanced g, M_g=((1+g)/2)y1+((1-g)/2)y2 has H=2+H(g)/2 and I=1+I(g)/2. Applying a selector bound C to g_t gives

\[
tH(f)+4\le C(tI(f)+3).
\]

Divide by t and let t tend to infinity. This gives H(f)<=C I(f); the reverse direction is subset inclusion. No additive loss remains. For rarity, F=1+A_r(g-1), p=2^(-r),

\[
H(F)=pH(g)+2rp(2-p)+(1-p)^2\log_2\frac1{(1-p)^2},\qquad I(F)=p[I(g)+r].
\]

Take g=g_t and r=ceil(2log2(t+1)). Then I(F)->0, Pr(F=-1)=p/2->0, r/t->0, and the final entropy term divided by p tends to 2log2 e. Therefore H(F)/I(F)->H(f)/I(f) for every nonconstant seed. Inclusion and approximation establish equality of suprema, also if the supremum is infinite. These are completed implications, not proofs that the common supremum is finite. R01-R02 add coding and smoothing; their source derivations are recorded as recovered baseline, with independent reconstruction requested from A002/A094 rather than silently claimed here.

**Dyadic gate-potential equivalence reconstructed at its actual domain.** Assume FEI(C); define Gamma_C(p)=inf over finite uniform Boolean g of probability p of [C I(g)-H(g)]. For dyadic p the admissible set is nonempty, Gamma is finite/nonnegative, symmetric, endpoints zero, and a dictator gives Gamma(1/2)<=C. With finitely many disjoint child encoders approaching their infima, raw composition yields

\[
C I(F)-H(F)=\sum_i\frac{I_i^\nu(G)}{V_{p_i}}
 [C I(g_i)-H(g_i)+h_2(V_{p_i})]-H_\nu(G).
\]

The left side is at least Gamma(pout). Taking the finite collection of approximation limits proves R09. Conversely apply R09 to any Boolean G with all inputs fair: V=1, h2(V)=0, and Gamma(pout)>=0 immediately imply H(G)<=C I(G). Nondyadic output probabilities have no finite uniform encoder; neither continuity nor an all-real potential follows merely from this infimum. A proposal defining Gamma through C I-H while assuming it nonnegative has not paid the conjecture.

**Fixed conditional marginal admission.** Fix any actual Boolean base F0(X,Y0) realizing a specified marginal on spectral X, with X degree <=d if needed. For an arbitrary Boolean seed f on fresh Z blocks put F_t=F0 f^tensor t. Its X marginal is unchanged, its X degree is unchanged, and

\[
H(\mathcal S_{Y0,Z}\mid\mathcal S_X)
=H_{F0}(\mathcal S_{Y0}\mid\mathcal S_X)+tH(f),\quad
I(F_t)=I(F0)+tI(f).
\]

Therefore a universal bound on this conditional entropy by C I(F_t), even restricted to that one fixed realized marginal and admitting arbitrary data tensors, implies full FEI(C) after division by t. Full FEI(C) implies the conditional bound since conditional entropy<=full entropy. The tensor-stable endpoint thus has the same optimum, once a finite actual Boolean base exists. This proof establishes the admission test without depending on a missing cyclic-source proof. The campaign's particular cyclic realization is navigation-only here: no unbundled source is certified as read. Bounds using only I_Y or an additive d term still need their own exact constant ledger. The marginal bound H(p_X)<=(2/ln2)I_Y+2(d-1) does not pay the conditional term.

**History/reveal distinction.** The supplemental map records H_nat-3I<=C_path<=H_nat+I. A universal C_path<=K I would imply FEI with bit coefficient (K+3)/ln2; FEI(C) would bound C_path by (C ln2+1)I. This is equivalent in finiteness if those source identities are available, not a new independently audited theorem in this run. Separately the weighted reveal target integral exp(t) E TC(P_t) dt<=A_eps[DTC(P0)+J0] retains the negative forced-information refund and concerns natural units under its precise policy. Even a proof of that lifetime bound leaves actual-source entropy/history transfer unpaid. Finite integral in each fixed dimension is not a uniform bound.

**Geometric payment.** Refinement is a genuine upper-bound mechanism: with fixed b,M, H(A) is at most root entropy plus log2(2^b-1) times total internal expected occupancy and log2(2^M-1) times leaf expected occupancy. For crossing sets, arm bounds give E N_s<=C m(R)/m(s); lower power growth makes the reciprocal-scale sum finite uniformly, and I>=c m(R) converts to FEI. Its first universal gap is a dimension-independent occupancy hierarchy and root/terminal payment for arbitrary Boolean spectra, not the chain rule. Pivotal entropy lower bounds and equal one/two-coordinate marginals do not supply this missing upper bound.

# executed validation with domain, arithmetic, commands and outputs

Frozen specification: [out/FROZEN_SPEC.json](out/FROZEN_SPEC.json), saved before the identity runs. No GPU, heavy job, optimization solver, randomness or automatic dimension increase was used.

Commands executed from A001:

```text
python -X utf8 runs/20261011T210330Z-account05-A001-quantifier-audit/code/source_audit.py
python -X utf8 runs/20261011T210330Z-account05-A001-quantifier-audit/code/exact_identities.py --nmax 2
python -X utf8 runs/20261011T210330Z-account05-A001-quantifier-audit/code/exact_identities.py --nmax 3
python -X utf8 runs/20261011T210330Z-account05-A001-quantifier-audit/code/finalize.py
```

The pilot exhausts 22 labelled truth tables for n=0,1,2 and passed 424 exact assertions in about 0.14 seconds. The full predeclared domain is all 278 labelled truth tables for n=0,1,2,3. [out/EXACT_CHECK_n3.json](out/EXACT_CHECK_n3.json) records the full result. Checks include Parseval, all character permutations and minimum character influence, the exact physical restriction marginal and H/I identities, tensor entropy, balancing, two-cell selectors, and activations with r=1,2. Entropies are compared as exact rational linear combinations of log2 primes; no floating entropy comparison certifies an inequality. The finalizer checks JSON fields against the protocol, statement hashes, byte-identical progress compatibility, and artifact sizes.

Finite checks validate implementations and displayed identities at their declared domain; the algebra above proves universal elementary implications. This run does not rerun the B05/B09 certificate suites or certify all manuscript constants by finite sampling.

# proof dependencies and changed downstream conclusions

The audit depends on the byte-pinned theorem interfaces above. Elementary implication proofs use only product spectra, Fourier character permutation, exact restriction identities, entropy chain rule and the source composition identities. No desired universal FEI conclusion is an unconditional dependency. R09's converse proof assumes FEI openly, exclusively to establish an equivalence.

Downstream corrections for B01/B20: keep endpoint J one-way sufficient; retain existential rather than all-coordinate quantifiers for endpoint R; distinguish Delta-selection from B-selection; preserve dyadic gate-potential domain; label arbitrary-core selectors, rare activations, simultaneous hardening and tensor-stable fixed-marginal conditional completion as full-FEI-strength; keep percolation and formula closures as proper class theorems. A003 can use this graph without declaring any unpaid leaf solved. A005 can apply the tensor admission test. A006 must pay all J terms. A026/A064 must pay reached-node/path and terminal costs. A041's weighted-bias target is a class extension with a separate variable-reuse gap.

The registered B05 no-go is independently reviewed at its local scope. B09's biased uncertainty lemma remains author-proved pending review; the repaired AND certificate refutes tax-free biased J<=M, and its asymptotic upper tax is not automatically a lower bound proving necessity. Those registry distinctions are retained.

# one next mathematical action and independent reviewer

Next action: A003 should freeze one explicit admissible posterior-forest representation on a new low-selector-energy or rare-core family, compute every term of R_f, and identify whether its only remaining payment is the seed entropy itself. This consumes the complete graph and avoids duplicating A002's hardening derivation. Independent reviewers: A086 for the witness/selection direction and A094 for the full quantifier and gate-potential/tensor admission chain. A002 is the appropriate independent reconstruction consumer for R01-R02.

# actual persistence receipts or precise save blocker

All requested run files are under this agent's assigned run directory, with code/ and out/. The execution matrix's additional TARGET_QUANTIFIERS.md and GAP_MAP.json deliverables are also saved. Rolling STATUS.md, WORKLOG.md and LEARNED.md are in A001 only. out/SOURCE_MANIFEST.json records inputs; out/ARTIFACT_RECEIPTS.json records output hashes and sizes after construction. The finalizer's output records schema verification and successful saves. No shared index, another agent folder, read-only source tree, brain database, scheduler, git repository or external service was modified. Supervisor ingestion, independent acceptance, mirror verification and downstream mathematical use are NOT claimed. Missing B01 lead notes are recorded as an access limitation, not a mathematical blocker.
