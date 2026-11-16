# Referee log

Task: referee HOOKS_AND_TWO_ROWS.md and GAP_STATE_FORM.md, requested 11 Nov 2026 (request clock time not exposed in this session).

## Orientation and constraints

Read both working notes and N4_PROOF.md; Proposition 1 is accepted as allowed. Work stays in this directory; no web, other agents, pushes, or visible windows. No mesh/checklist/brain commands that write outside this directory are run, under the author's specific restriction for this run. Startup memory and compute state are inspected read-only. The compute snapshot is stale and says warn, not distress; all numerical work will run at nice 10, one thread, well below 1 GB, in jobs under five minutes.

Package check command:

`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -c "import importlib.util; print({x: bool(importlib.util.find_spec(x)) for x in ['numpy','scipy','mpmath','sympy']})"`

Result: numpy, scipy, mpmath, sympy are all available. No existing numerical code was read or reused. Initial reads: the two target notes and N4_PROOF.md, plus directory listing and read-only startup/compute state. The local directory initially contained only the four source documents and PROMPT.md.

## Step 1 — hooks

**Lemma H: CORRECT.** The standard hook isomorphism sends a hook polytabloid to the wedge of its column differences; it is nonzero and equivariant and both dimensions are binomial(n-1,k). For a transposition, P projects onto (e_i-e_j), has rank one, and every exterior expansion term containing two P factors vanishes. Thus I-exterior^k(s)=D(I-s). Diagonalising L on V proves the sum-of-distinct-eigenvalues formula, including disconnected graphs with zero eigenvalues.

**Consequence for pairs of hooks: CORRECT**, with the ratio written only when its denominator is positive (as in the initial connected-graph notation). Each eigenvalue after the first j is at least the average of the first j, giving S_k >= (k/j) S_j. The undivided inequality holds also if S_j=0. The reported example ratios agree with k/j; they are numerical observations, **NOT A PROOF** of sharpness over all graphs.

## Step 2 — conjugation

**Conjugation identity: CORRECT.** Tensoring with sign sends every transposition matrix R to -R, so L_nu'=2WI-L_nu, with the entire spectrum reflected.

**Reformulation for tau=[2,1^(n-2)]: CORRECT.** Substitution into 2W-lambda_max(L) >= c(2W-lambda_max(mu)) gives the displayed inequality. Conjugation reverses dominance; the allowed mu are exactly the partitions other than [n] and [1^n] (including the tautological equality pair). **Hook case c=1: CORRECT**, since the largest k-term eigenvalue sum is at least the largest single eigenvalue.

## Step 3 — matrix model and disjoint unions

**Section 3 model, Rayleigh quotient, projection and norm: CORRECT** for n>=4. Sym^2 V decomposes as [n]+[n-1,1]+[n-2,2]; zero diagonal removes the first two components. The off-diagonal row-sum map has rank n, giving dimension n(n-3)/2. If A(d)=Pi diag(d) Pi for sum d=0, diag A(d)=(n-2)d/n; this gives the stated orthogonal projection and norm subtraction. Swapping i,j changes only the ik,jk entries; Frobenius numerator and denominator both have the required factors of two.

**Lemma U: CORRECT.** Restriction to S_k x S_(n-k) and addition of the tensor-factor spectra prove it.

**Connected heavy-component limit and horizontal-strip formula: CORRECT** with min(empty)=+infinity. A connected interchange Laplacian has kernel only in the trivial representation (zero energy forces invariance under every positive-weight transposition, and those generate the symmetric group). Pieri gives the strip condition. This does not justify describing a disjoint heavy component as an ordinary vertex contraction of G_1.

**n=6 (2211,222), n=7 (3211,322), and n=8 (4211,422) explanations: CORRECT.** With a star on four vertices and a connected heavy component on the remaining vertices, the admissible minimum for sigma comes from 22 and is 3t; that for tau comes from 211 and is 2t. Other allowed four-box shapes cannot lower those minima.

**Remaining three n=8 examples under 'The same holds ... (22211,2222), (2111111,2222) and (221111,2222)': WRONG as an application of the stated construction.** A horizontal strip of size four cannot be removed from any of these diagrams, all of width two. Thus the connected-heavy-component limits have no finite blocks, not bottoms 2t and 3t. For example G=K_{1,3}+h K_4 and (tau,sigma)=(2111111,2222): the hook-conjugation formula gives lambda_min(tau)=12h+6-max(4h,4)=8h+6 for h>1. The heavy S_4 types inside sigma have width <=2; their K_4 energies are 6h,8h,12h for 22,211,1111 respectively. The 22 x 22 restriction occurs, so lambda_min(sigma)=6h+3 for sufficiently large h, and the ratio tends to 4/3, not 2/3. Also the ordinary unit star on eight vertices already has minima 6 and 9 for (2111111,2222), a ratio 2/3, contradicting any claim that this particular pair has star ratio 1. This does not refute the reported numerical minima; their actual extremisers are not supplied. The K_4 scalar was checked as 6 minus the sum of box contents (not twice that value).

**Section 7 search minima: NOT A PROOF.** The external output files are absent here; the claimed universal lower bounds are not established by searches. Exact n=4 examples support 2/3, and the valid heavy-component embeddings explain three of the listed pairs.

## Step 4 — what sections 4–6 actually claim

**Conjecture F: NOT A PROOF.** It is explicitly a conjecture; its algebraically equivalent forms and its star and single-edge equality examples are **CORRECT**. At the unit star the two conjugate minima are n-2 and n-1. A single edge has zero bottom in both these representations. The reported searches are numerical, not proofs, and their output files are not present.

**Dual form and the two explicit matching measures: CORRECT.** This is Proposition 1 after sign twist. For the star construction the row constraints fix T_kl=-(a_k+a_l)/(n-3); rotational symmetry among the leaves gives the matching state and tight star edges. For the edge construction, 2 sum a_k^2=1, so the edge 12 has energy 2 and each 1k or 2k has expected energy 1/2, exceeding the required (n-5)/(2(n-2)). Pairs on the zero coordinates have nonnegative energy and require a negative lower bound.

**Section 5 assertion that P(xy) spans V_22 for every x: WRONG.** Quote: 'as it must: the vectors P(x.y) span V_22, so this is Theorem 3 again'. For n=4, x=(1,-1,0,0)/sqrt(2), y=(1,1,-1,-1)/2 lies in {1,x}^perp and maps to zero. The domain is two-dimensional, so the image has dimension at most one, and a nonzero second direction shows it is exactly one. Theorem 3 guarantees an unrestricted matching density matrix, not feasibility in every prescribed image. This error invalidates that parenthetical explanation, not Theorem 3.

**Covariance reduction R: GAP in state normalization as written.** Quote: 'then Conjecture F holds ... (Proposition 1 with the state rho(x,C))'. The projected matrices are not unit vectors. The correct state is E[|P(xy)><P(xy)|]/E||P(xy)||_F^2, provided the denominator is positive; equivalently a probability measure on normalized matrices with probabilities weighted by their squared norms. Uniform normalized images are in general a different measure. A covariance supported in the kernel gives denominator zero and cannot define rho. This degenerate case must be excluded or treated separately. The matrix calculations and (*) can be valid for the unnormalized covariance construction, subject to this condition. The independent algebra check below will audit their coefficients.

**Section 5(a),(b),(c),(d) searches and choices of covariance: NOT A PROOF.** They are explicitly trials or numerical observations, and the note says 'None is a proof.' The conditional statements involving M and the gap state require a nonzero projected state; tau=0 also requires a separate argument. The all-equal complete graph has tau=0. The universal Gval claim for n>=5 is expressly left open.

**Section 6 remaining pairs: CORRECT.** Enumerating partitions and removing hook pairs, trivial/sign cases and standard-module cases leaves precisely the five ordered (tau,sigma) pairs listed. The decimal minima are **NOT A PROOF** and are not certificates of global optimality.

## Step 5 — GAP_STATE_FORM.md, theoretical audit

The numerical and exact algebra audits requested in step 6 will independently test these calculations. Source line numbers below refer to the unchanged target files.

**Setting, N positivity and converse (lines 8–15): CORRECT.** In the converse, the entrywise bound makes L=lam Pi-N have nonpositive off-diagonal entries and zero row sums, so L is a nonnegative graph Laplacian; N>=0 bounds its spectrum above by lam and Nx=0 attains lam.

**Affine identity Gval/(n-2)=a lam+b and auxiliary pair identity (21–26): CORRECT by expansion.** Expand L=lam Pi-N in tr(MN), use N1=Nx=0, and collect powers of lam. The apparent quadratic term cancels. Expanding the unordered-pair sum gives nt+tau. These are identities, not proofs of nonnegativity.

**Consequence 1, a>=0 (30–31): CORRECT.** For orthogonal unit x,y, ||(xy^t+yx^t)/sqrt(2)||_F^2=1 and the projection subtracts (2n/(n-2)) sum x_i^2 y_i^2. Summing with gap weights gives tau-(2n/(n-2))t>=0.

**Consequence 2, adding c K_n and boundary reduction (33–36): CORRECT** for c>=0 and fixed x,N. All eigenvalues on V increase by cn, preserving the top eigenspace. This reduces the *sufficient Gval inequality*, not directly all instances of the original conjecture to sparse graphs.

**Leading-terms inequality (42–44): CORRECT. Equality description (45): WRONG.** Quote: 'Equality needs every g_k = lam, a single edge.' There is a second equality case: all g_k=0, e.g. any positive equally weighted complete graph, with N=0 and tau=0. For lam>0 the full equality classification is all gaps zero OR all n-2 gaps equal lam. The latter makes L=lam xx^t; nonnegative weights force x to have only one positive and one negative nonzero coordinate, hence a single edge. The star leading value 2(n-1)(n-2) is correct.

**Unit-star formulas (50–51): CORRECT.** Direct substitution gives t=(n-2)/n and a lam=2(n-1)((n-1)(n-2)-2), b=-a lam.

**Two-eigenvalue Laplacian and weight constraint (55–59): CORRECT** with g>=0 and the usual degenerate cases noted: g=0 has no simple top eigenvalue, and lam=g gives zero lower eigenvalue. The phrase 'one other nonzero eigenvalue' does not include the stated single-edge example. Saying the two *listed* equality examples lie in this family is correct; claiming they exhaust equality would be wrong because complete graphs have N=0 and Gval=0.

**Gval=2g^2 Psi and its derivation (61–66): CORRECT by substitution**, to be tested independently in step 6. The Q-square and pair identities reduce respectively to 1+p3^2-2q and -3D. **Special values (68–70): CORRECT.** The padded-star formula is a statement about the vector, not a claim that every padded star is a member of the two-eigenvalue graph family. The n=4 simplification is correct. **Numerical minima (72): NOT A PROOF**; the edge is also an equality vector for every n, so the star is not the only minimiser.

**Conditional graph consequence of Psi>=0 (73): CORRECT for the stated family**, not a proof for arbitrary graphs. Precisely: for every unit sum-zero x and every g>0, Psi(x)>=0 certifies F for the boundary graph with weights g(m-x_i x_j), and, by a>=0, for every graph obtained by adding c K_n, c>=0. Equivalently it certifies all nonnegative graphs L=lam xx^t+(lam-g)Q with lam>=g(1+nm). For n>=5 the projected state's trace is gK/(n-2)>0. The remaining g=0 case is an equally weighted complete graph, handled directly. The note says 'on this family', correctly. It does not establish the full conjecture at n>=5.

**One-positive lower bound and explanation of its loss (76–79,108–115): CORRECT for n>=5.** Here 1/2<=u<=(n-1)/n. The indicated moment bounds and coefficient signs justify substituting their lower bounds. For the dependence on beta_3, the derivative is -2(n-3)(u^(3/2)-beta_3)<=0; the expression printed as a 'coefficient' in line 111 is the coefficient after factoring beta_3, not this derivative. Simultaneous tightness of all three bounds requires all n-1 negatives equal. The resulting expression is indeed negative for 2/3<u<(n-1)/n. It is an unsuccessful lower bound, explicitly not a proof.

**Open statements (83–87): NOT A PROOF**, correctly labelled open. The n=4 failure of Gval is a numerical assertion to be independently checked.

**Split of Psi, K>0, D>=0 and the two-valued classification (91–106): CORRECT.** D is the squared norm of x^2-1/n-p3*x. A two-valued vector with both multiplicities at least two has m>=1/n. Sign/permutation variants of the star are implicit.

**Subset-mean remedy (117–125): NOT A PROOF**, correctly labelled numerical/candidate. Moreover max over all |A|>=2 of mu_A equals m exactly: a mean is at most its largest pair product, and two-element sets attain m. The candidate is precisely Psi>=0 again, expressed as a disjunction, not a stronger bound or elimination of the substantive pair maximum. The restricted-complement numerical experiments do not prove anything universal.

**Bound m>=M and equality condition (129–140): CORRECT.** Multiply each pairwise bound by c_i c_j>=0 and sum ordered distinct pairs. The denominator n(n-1)S^2-1 is at least n-2>0 under the chosen largest-modulus orientation. Equality holds exactly on pairs for which both c's are positive, as stated. The edge and star equalities check directly.

**Phi' inequality (142–144): CORRECT for n>=5.** In fact n*den*Psi-Phi'=n(n-1)K*den*(m-M), making the role of K>0 explicit. **Local minima claim (146–148): NOT A PROOF**, correctly numerical. The implication Phi'>=0 => Psi>=0 is exact; the premise is unproved.

**Concavity and finite-value reduction (150–157): CORRECT with a routine missing degeneracy explanation.** The printed Hessian and determinant give negative definiteness for n>=5, S^2>=1/n. An extreme minimizing moment pair admits a supporting nonzero linear form. At a maximizer of its separable quartic, interior coordinates satisfy 4b y^3+3a y^2-2v y-u=0 if the two constraints are regular. If constraint gradients are dependent, all interior coordinates coincide, already within the claimed bound. Endpoints can have arbitrary integer multiplicity. This is a reduction to at most five distinct coordinate values, not to finitely many numerical vectors; continuous parameters remain. Non-exposed extreme points cause no problem: any supporting face supplies the same cubic for every maximizer. It leaves the inequality explicitly unproved.

**Scan 1, relaxed measures (163–169): NOT A PROOF of a graph inequality.** The stated boundary support types follow from nonnegative supporting quartics on [-S,S]: at most two double interior roots, or both endpoints and one double interior root (including zero-weight degeneracies). A negative relaxed example, if reproduced, refutes that relaxation only. Integer multiplicities or another property of genuine vectors must then be used.

**Scan 2, integer three-valued vectors (171–173): NOT A PROOF**, explicitly a finite grid, not coverage of all continuous parameter values. Both scans will be reproduced with independent parameterisations. Calling floating point evaluations 'exact' (161) is unsupported: exact/rational/interval certificates are not provided. The two reported scan output files are absent.

**Final status (175–177): CORRECT.** The comparison Psi>=Phi'/(n*den) is proved for n>=5; Phi'>=0 remains numerical evidence; the few-value reduction does not finish it.

## Step 6 — independent implementation

Created referee.py from scratch in this directory. It contains Young orthogonal matrices built from recursively enumerated tableaux, direct matrix projections and covariance states, scalar formula tests, constrained minimisation, symbolic expansions and independent moment-grid parameterisations. It sets all numerical library thread counts to one before import, installs a 240-second alarm, logs each completed block immediately, and reports peak resident memory. No original numerical source was available or read. Runs and outputs follow.

### Independent run observations

The shell already inherits nice=10. Attempting an additional `nice -n 10` prints 'setpriority: Operation not permitted' under the sandbox, but the program runs at the existing nice=10. Later commands use the Python executable directly and print their inherited priority.

The first Specht run returned finite spectra and Coxeter residuals <=1.2e-16 despite numerical-library floating-point-status warnings on tiny matrix multiplications. A separate no-BLAS multiplication check is planned before relying on that run. The first, nonsmooth SLSQP minimisation completed 160 starts per n but some iterations left the sphere and overflowed; those trials are not treated as successful minimisations. The implementation was changed to a bounded, smooth epigraph formulation with one auxiliary variable bounding every x_i*x_j. Its fresh run is authoritative for the optimisation figures; the original output is retained as optimize.out.

The algebra run independently reproduced N, A_ij, (*), M's expanded Gval and the affine N form. It also reproduced exactly the claimed total-weight-one two-edge-path slacks -1/18, -1/12, -1/10 after accounting for the note's n-2 multiplier. The phrase 'two unit edges ... total weight 1' means the path has been rescaled; literally two unit edges have total weight 2.

### Further audit of the three-valued covariance claim

**HOOKS section 5(b), edge-vector theta interval: WRONG.** Quote: 'and is [0, 0.18] at the edge vector for n = 5'. At x=(1,-1,0,0,0)/sqrt(2), the rotated vector is v=(3,3,-2,-2,-2)/sqrt(30) and P(xv)=0. Thus C(theta)=theta vv^t+(1-theta)Pi_B/2 gives the same normalized image state for every 0<=theta<1. Direct substitution into (*) gives slack 0 for pair 12, (3/2)(1-theta) for 1k and 2k, and 5(1-theta) for pairs among the last three coordinates. All are nonnegative throughout [0,1]; theta=1 has zero projected trace. The independent symbolic run will record these exact expressions. The correct admissible interval for nonzero states is [0,1), not [0,0.18].

### Clarification of the n=8 disjoint-union verdict

Two of the unexplained width-two examples admit other heavy-component constructions. For (22211,2222), use a four-vertex star and two separate heavy edges, applying Pieri twice: (22211,2222)->(2211,222)->(211,22). For (221111,2222), use a six-vertex star and one heavy edge: (221111,2222)->(21111,222), whose star minima are 4 and 6. For (2111111,2222), the ordinary eight-vertex star gives 6/9; this is also Theorem 4.5 of the supplied Alon text. Thus the ratios can be explained, but the note must specify these different constructions; a *connected* heavy graph on the other four vertices does not explain them. The earlier WRONG verdict applies to reusing that specific connected construction; as a broadly intended disjoint-union assertion the first two width-two examples have a GAP in the missing graph description, which is repaired here. The claim that all the listed pairs have ratio one on stars is wrong.

### Scan verdicts reached

The independent integer scan covers 2001 values of S^2 for each n=5..12 and every two-block multiplicity and sign. It finds no value below rounding error (roughly 2e-12); the only zero locations are S^2=1/2 and (n-1)/n. **Scan 2: NOT A PROOF; independent check agrees.** The grid does include these special values, and it is evaluated in floating point, not exact arithmetic.

The independent probability-measure scans find negative Phi' in both boundary families. At n=5 the two-interior-atom minimum is about -2.7913 at S^2=.4405, atom weight .688; at n=16 it is about -2267.68 at S^2=.4075. The second family is negative too. **Scan 1: NOT A PROOF of Phi'>=0; independent check agrees with the stated failure of the relaxation.** Grid minima differ slightly because the original grid is unspecified. Full numbers and commands are recorded by referee.py and scans.out.

An indentation error introduced while replacing Specht multiplications stopped the first exact-mode launch before any calculation. Fixed the indentation and relaunched; no output from the failed launch is used.

The first indentation fix left a second misindented line in the same loop. Replaced the full loop indentation and relaunched successfully; both failed launches exited before numerical work.

The exact run proves the split and Phi' comparison identity symbolically, reproduces the Hessian and determinant, proves P(xy)=0 for the rank counterexample and confirms the full edge theta interval. Its initial small random search did **not** reproduce a negative n=4 Gval; this is recorded as a failed search, not evidence against the cited counterexample. A targeted constrained graph search is needed for that assertion.

The direct-contraction Specht rerun completed without the tiny-BLAS warnings. The first smooth epigraph optimisation still had some solver failures at higher n, so the objective is scaled by n^3 (which preserves minimisers), with bounded coordinates and exact constraint Jacobians; a fresh 200-start run is being used to improve solver reliability. All unit-vector objective values are computed from actual max products, independently of the epigraph variable.

The scaled epigraph run completed all 200 starts successfully at every n=5,6,7,8. Minima are zero within 3e-15, at star or edge vectors; both are exact analytic zeros at every n. This agrees with the note's numerical evidence but supplies no global certificate. Original and intermediate solver outputs are retained, and optimize_scaled.out is the authoritative optimisation output.

The first targeted n=4 graph search (18,564 differential-evolution evaluations plus 60 SLSQP starts) found only -2.2e-15 at a single edge, not the claimed -0.0149 W^2. A second search uses the independently parameterised N=yy^t+r zz^t with an arbitrary orthonormal frame (x,y,z) in V and the exact boundary lam=4 max(-N_ij). This avoids choosing unstable top eigenvectors near spectral degeneracy. The known failure of the uniform state is independently confirmed: the rounded vector supplied in the note, centred and normalised, has minimum slack -0.14025117089308015 on pair 14.

The N-parameter search **does** reproduce negative n=4 Gval: -0.014715702538821294 W^2, with direct tr(MN) agreeing with 2(a lam+b). This supports the note's n=4 counterexample claim. It lies near a repeated top eigenvalue, explaining why naive optimisation over weights with an eigensolver can miss the relevant eigenvector choice. An exact rational graph witness with a *simple* top eigenvalue is being certified separately, using y=(3,-2,3,-4)/sqrt(38), z=(1,0,-1,0)/sqrt(2), N=yy^t+zz^t/100, lam=24/19 and x=(1,-7,1,5)/sqrt(76).

### Normalization gap: a repair of Reduction R

The stated derivation omits the positive-trace condition; it can be completed without strengthening R's global hypothesis. Let A_x map y to P((xy^t+yx^t)/sqrt(2)). At the star A_x is injective (its leaf entries recover y), so the determinant of its Gram matrix is not identically zero. Thus A_x is injective for a dense set of unit x. For these x every PSD covariance of trace one has tr(A_x C A_x^*)>0, and the normalized state gives the desired inequalities. Approximate an exceptional x by generic x and extract a convergent subsequence of density matrices; compactness and continuity give a matching state at the limit. Therefore R is a valid global sufficient condition, but the printed 'state rho(x,C)' argument needs this normalization/limit paragraph. The pointwise criterion in (c) still needs nonzero projected y; a zero image cannot certify that individual graph through this state.

The first rational approximation to the negative n=4 example was too coarse: it gives positive Gval=848853/34295000, so it is **not** a counterexample. This failed candidate is retained in certificate.out. Replaced it by y=(9,-7,9,-11)/sqrt(332), x=(1,-10,1,8)/sqrt(166), lam=99/83, epsilon=1/10000, much closer to the numerical witness. Only the result in certificate_checked.out will be used as a certified counterexample if its exact sign is negative.

**n=4 Gval failure: independently certified.** certificate_checked.out gives weights (12,13,14,23,24,34)=(9/83,899917/1660000,0,9/83,44/83,0), eigenvalues 0,16/83,989917/830000,99/83, and top eigenvector (1,-10,1,8)/sqrt(166). Its exact Gval is -1390241124027/57178700000000, or -0.024313968733584358; Gval/W^2=-0.014631140210437482. This verifies the reported negative phenomenon without relying on an unstable repeated eigenvalue. It refutes only the proposed sufficient state inequality at n=4, not Conjecture F. The same command symbolically verifies the one-positive lower-bound expression (residual exactly zero).

A supplementary independent Phi' minimisation checks the note's local-minimum claim: 80 constrained starts at each n=5..8, with x_1 the largest absolute coordinate, analytic derivatives, sum/norm constraints and -x_1<=x_i<=x_1. Results are in phiopt.out. An independent edge-permutation model for [n-2,2] is compared against the Young orthogonal modules on 80 graphs each at n=5,6; projection and norm identities are checked too. The tiny-BLAS status warnings appeared again in the first model action multiplication, so that multiplication now uses the already verified direct contractions; model_checked.out is authoritative. The branching output explicitly enumerates all four-box horizontal-strip survivors and star minima for every pair discussed in section 7.

## Report assembled

Wrote REPORT.md with a statement-by-statement verdict table, exact errors and repairs, all requested numerical results with commands, corrected n=8 constructions, the conditional two-eigenvalue graph conclusion, limits of the numerical checks, and the list of labels needing correction. Overall verdict on the asserted proved parts: **WRONG** (false ancillary assertions; the main representation and scalar identities survive). Final audit of cross-references and output values remains before reporting completion.

The final output audit corrected the n=6 matrix-model residual to the value in model_checked.out (1.4432899320127035e-15). It also identified that the Phi' random comparison had been limited to the note's n>=5 range. Extended this comparison to n=4 as well, so step 6(d) covers all n=4..9 consistently; the identical seeded algebra run is being saved as algebra_checked.out. This change affects only the previously omitted n=4 comparison statistic.

## Final audit and completion

The n=4 Phi' comparison minimum is 0.007425987197142554 on the same 300 random vectors; all n=5..9 figures are unchanged. REPORT.md now cites algebra_checked.out and includes that statistic. Programmatically matched every algebra table entry and all Psi minimization minima to authoritative JSON output lines, checked 200/200 successful Psi solves at each n, parsed referee.py successfully, and verified every authoritative run has a completed resource record below 300 seconds and 1 GB. All tool-launched computation sessions have completed. No input document was modified. All requested steps and REPORT.md are complete.

Final verdict on the PROVED parts: **WRONG**. The false spanning assertion, false edge theta interval, omitted complete-graph equality case, and normalization gaps are documented separately from the correct representation and scalar identities. No counterexample to Conjecture F or Conjecture 1.5 is claimed.

Task: 'You are refereeing a mathematical working note' — 11 Nov 2026; exact user-message clock time unavailable, first local check 08:00:36 +04.

`COMMAND {"command": "nice -n 10 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py specht", "seed": 20261111, "threads": 1, "timeout_seconds": 240}`

`SPECHT {"n": 5, "graphs": 160, "dimensions": {"(5,)": 1, "(4, 1)": 4, "(3, 2)": 5, "(3, 1, 1)": 6, "(2, 2, 1)": 5, "(2, 1, 1, 1)": 4, "(1, 1, 1, 1, 1)": 1}, "coxeter_max_abs": 1.1102230246251565e-16, "hook_full_spectrum_max_abs": 2.220446049250313e-15, "conjugate_full_spectrum_max_abs": 2.1094237467877974e-15, "hook_ratio_minus_k_over_j_min": 0.0504744848153269}`

`SPECHT {"n": 6, "graphs": 160, "dimensions": {"(6,)": 1, "(5, 1)": 5, "(4, 2)": 9, "(4, 1, 1)": 10, "(3, 3)": 5, "(3, 2, 1)": 16, "(3, 1, 1, 1)": 10, "(2, 2, 2)": 5, "(2, 2, 1, 1)": 9, "(2, 1, 1, 1, 1)": 5, "(1, 1, 1, 1, 1, 1)": 1}, "coxeter_max_abs": 1.1102230246251565e-16, "hook_full_spectrum_max_abs": 2.4424906541753444e-15, "conjugate_full_spectrum_max_abs": 2.4424906541753444e-15, "hook_ratio_minus_k_over_j_min": 0.0017534470869424723}`

`RESOURCES {"seconds": 0.10588008299237117, "maxrss_bytes": 75071488}`

`COMMAND {"command": "nice -n 10 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py algebra", "seed": 20261111, "threads": 1, "timeout_seconds": 240}`

`ALGEBRA {"n": 4, "vectors": 300, "max_abs": {"gval_psi": 9.769962616701378e-15, "split": 2.220446049250313e-16, "gap_affine": 3.3306690738754696e-15, "pair_identity": 5.329070518200751e-15, "q_square_identity": 5.828670879282072e-16, "q_pair_identity": 7.355227538141662e-16, "covariance_star": 7.993605777301127e-15, "uniform_N": 2.3314683517128287e-15, "uniform_A": 4.440892098500626e-15, "expanded_Gval": 7.771561172376096e-15}, "min_m_minus_M": 0.011408343995856773, "min_n_den_Psi_minus_Phi": null, "min_a": 0.011873588499084875, "min_random_Phi": 0.04750582185704824}`

`ALGEBRA {"n": 5, "vectors": 300, "max_abs": {"gval_psi": 2.4868995751603507e-14, "split": 1.3322676295501878e-15, "gap_affine": 6.661338147750939e-15, "pair_identity": 4.440892098500626e-15, "q_square_identity": 4.996003610813204e-16, "q_pair_identity": 7.771561172376096e-16, "covariance_star": 8.881784197001252e-15, "uniform_N": 3.9968028886505635e-15, "uniform_A": 7.105427357601002e-15, "expanded_Gval": 1.0658141036401503e-14}, "min_m_minus_M": 0.01360651560029856, "min_n_den_Psi_minus_Phi": 20.839849623544257, "min_a": 0.3642706592580021, "min_random_Phi": 0.7239550956105621}`

`ALGEBRA {"n": 6, "vectors": 300, "max_abs": {"gval_psi": 5.684341886080802e-14, "split": 3.552713678800501e-15, "gap_affine": 8.881784197001252e-15, "pair_identity": 7.105427357601002e-15, "q_square_identity": 7.494005416219807e-16, "q_pair_identity": 7.771561172376096e-16, "covariance_star": 1.1546319456101628e-14, "uniform_N": 3.552713678800501e-15, "uniform_A": 7.105427357601002e-15, "expanded_Gval": 1.3322676295501878e-14}, "min_m_minus_M": 0.028893558841178134, "min_n_den_Psi_minus_Phi": 98.06059873376786, "min_a": 0.6844141472554601, "min_random_Phi": 15.735246346354373}`

`ALGEBRA {"n": 7, "vectors": 300, "max_abs": {"gval_psi": 1.1368683772161603e-13, "split": 7.105427357601002e-15, "gap_affine": 9.769962616701378e-15, "pair_identity": 4.440892098500626e-15, "q_square_identity": 5.551115123125783e-16, "q_pair_identity": 7.216449660063518e-16, "covariance_star": 1.509903313490213e-14, "uniform_N": 4.884981308350689e-15, "uniform_A": 8.881784197001252e-15, "expanded_Gval": 1.4654943925052066e-14}, "min_m_minus_M": 0.03564875683315622, "min_n_den_Psi_minus_Phi": 542.8398143023923, "min_a": 0.8746758000548924, "min_random_Phi": 26.719935391643673}`

`ALGEBRA {"n": 8, "vectors": 300, "max_abs": {"gval_psi": 2.2737367544323206e-13, "split": 1.4210854715202004e-14, "gap_affine": 7.105427357601002e-15, "pair_identity": 5.773159728050814e-15, "q_square_identity": 6.661338147750939e-16, "q_pair_identity": 8.326672684688674e-16, "covariance_star": 1.687538997430238e-14, "uniform_N": 6.217248937900877e-15, "uniform_A": 1.2434497875801753e-14, "expanded_Gval": 1.5987211554602254e-14}, "min_m_minus_M": 0.05989971804725272, "min_n_den_Psi_minus_Phi": 2057.4957820170994, "min_a": 0.9199558239390218, "min_random_Phi": 80.73697729614435}`

`ALGEBRA {"n": 9, "vectors": 300, "max_abs": {"gval_psi": 3.410605131648481e-13, "split": 1.4210854715202004e-14, "gap_affine": 7.993605777301127e-15, "pair_identity": 4.884981308350689e-15, "q_square_identity": 4.440892098500626e-16, "q_pair_identity": 7.216449660063518e-16, "covariance_star": 1.7763568394002505e-14, "uniform_N": 7.105427357601002e-15, "uniform_A": 1.5987211554602254e-14, "expanded_Gval": 1.7763568394002505e-14}, "min_m_minus_M": 0.050893947184497496, "min_n_den_Psi_minus_Phi": 4034.3753242922776, "min_a": 1.0455999963059204, "min_random_Phi": 264.9472712870991}`

`SPECIAL {"n": 4, "star": {"Psi": -2.220446049250313e-16, "Phi": -8.289665250534501e-15, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.6666666666666667}, "edge": {"Psi": 0.0, "Phi": 8.881784197001252e-15, "min_uniform_slack": 1.480297366166875e-16, "projected_norm": 0.4999999999999999}, "path_slack": -0.027777777777777707, "path_slack_times_n_minus_2": -0.055555555555555414}`

`SPECIAL {"n": 5, "star": {"Psi": 2.220446049250313e-16, "Phi": -6.66133814775092e-15, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.833333333333333}, "edge": {"Psi": -3.3306690738754696e-16, "Phi": 2.842170943040401e-14, "min_uniform_slack": 2.96059473233375e-16, "projected_norm": 0.6666666666666665}, "path_slack": -0.02777777777777768, "path_slack_times_n_minus_2": -0.08333333333333304}`

`SPECIAL {"n": 6, "star": {"Psi": -3.1086244689504383e-15, "Phi": -1.406874616804999e-13, "min_uniform_slack": 2.220446049250313e-16, "projected_norm": 0.8999999999999998}, "edge": {"Psi": -6.661338147750939e-16, "Phi": 5.684341886080802e-14, "min_uniform_slack": 1.554312234475219e-16, "projected_norm": 0.75}, "path_slack": -0.024999999999999772, "path_slack_times_n_minus_2": -0.09999999999999909}`

`SPECIAL {"n": 7, "star": {"Psi": 8.881784197001252e-16, "Phi": -1.3470706032118563e-13, "min_uniform_slack": 2.220446049250313e-16, "projected_norm": 0.9333333333333331}, "edge": {"Psi": -9.992007221626409e-16, "Phi": 1.1368683772161603e-13, "min_uniform_slack": 1.7023419710919053e-16, "projected_norm": 0.7999999999999997}, "path_slack": -0.0222222222222222, "path_slack_times_n_minus_2": -0.111111111111111}`

`SPECIAL {"n": 8, "star": {"Psi": 1.7763568394002505e-15, "Phi": 1.2180732613030286e-13, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.9523809523809522}, "edge": {"Psi": -1.3322676295501878e-15, "Phi": 2.2737367544323206e-13, "min_uniform_slack": 3.7007434154171876e-16, "projected_norm": 0.8333333333333331}, "path_slack": -0.019841269841269604, "path_slack_times_n_minus_2": -0.11904761904761763}`

`RESOURCES {"seconds": 7.1542205000296235, "maxrss_bytes": 75399168}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py optimize --starts 160", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`OPTIMIZE {"n": 5, "starts": 160, "optimizer_success": 159, "min_Psi": 2.37476704967321e-12, "x": [0.894427190999916, -0.2236067977498247, -0.2236067977500342, -0.22360679775027786, -0.22360679774977912], "q": 0.6500000000000002, "p3": 0.6708203932499373, "m": 0.05000000000007918, "exact_star_Psi": 2.220446049250313e-16, "exact_edge_Psi": -3.3306690738754696e-16, "worst_final_value": 3.5367205733628966, "seconds": 1.3591988330008462}`

`OPTIMIZE {"n": 6, "starts": 160, "optimizer_success": 113, "min_Psi": 5.968189355848903e-12, "x": [0.7071067811865016, -0.7071067811865934, -7.923412395044954e-14, -2.8115684343733106e-14, 5.848341889834149e-14, 1.4067157216421622e-13], "q": 0.5, "p3": -1.3772316620475067e-13, "m": 9.946982259748361e-14, "exact_star_Psi": -3.1086244689504383e-15, "exact_edge_Psi": -6.661338147750939e-16, "worst_final_value": NaN, "seconds": 11.580022290989291}`

`OPTIMIZE {"n": 7, "starts": 160, "optimizer_success": 122, "min_Psi": 1.071276400921306e-11, "x": [0.9258200997725515, -0.1543033499622643, -0.1543033499618452, -0.1543033499616544, -0.15430334996221412, -0.1543033499621582, -0.15430334996241543], "q": 0.7380952380952384, "p3": 0.7715167498104597, "m": 0.02380952380960033, "exact_star_Psi": 8.881784197001252e-16, "exact_edge_Psi": -9.992007221626409e-16, "worst_final_value": 24.99476539922938, "seconds": 18.8894820829737}`

`OPTIMIZE {"n": 8, "starts": 160, "optimizer_success": 95, "min_Psi": 2.5280222359924664e-11, "x": [0.9354143466934853, -0.133630620955896, -0.13363062095576683, -0.13363062095665906, -0.13363062095626288, -0.1336306209565536, -0.1336306209564317, -0.13363062095591516], "q": 0.7678571428571428, "p3": 0.8017837257372732, "m": 0.017857142857248195, "exact_star_Psi": 1.7763568394002505e-15, "exact_edge_Psi": -1.3322676295501878e-15, "worst_final_value": 46.7091768872838, "seconds": 30.227960040967446}`

`RESOURCES {"seconds": 30.22862675000215, "maxrss_bytes": 75464704}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py optimize --starts 200", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`OPTIMIZE {"n": 5, "starts": 200, "optimizer_success": 199, "min_Psi": 2.220446049250313e-16, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0], "q": 0.5000000000000001, "p3": 0.0, "m": 0.0, "exact_star_Psi": 2.220446049250313e-16, "exact_edge_Psi": -3.3306690738754696e-16, "worst_final_value": 3.333333333333336, "seconds": 0.14443558303173631}`

`OPTIMIZE {"n": 6, "starts": 200, "optimizer_success": 164, "min_Psi": 4.440892098500626e-16, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0, 0.0], "q": 0.5000000000000001, "p3": 0.0, "m": 0.0, "exact_star_Psi": -3.1086244689504383e-15, "exact_edge_Psi": -6.661338147750939e-16, "worst_final_value": 5.333333351262587, "seconds": 0.30338425002992153}`

`OPTIMIZE {"n": 7, "starts": 200, "optimizer_success": 101, "min_Psi": 6.661338147750939e-16, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0, 0.0, 0.0], "q": 0.5000000000000001, "p3": 0.0, "m": 0.0, "exact_star_Psi": 8.881784197001252e-16, "exact_edge_Psi": -9.992007221626409e-16, "worst_final_value": 13.333729023847315, "seconds": 0.6856315000331961}`

`OPTIMIZE {"n": 8, "starts": 200, "optimizer_success": 77, "min_Psi": 8.881784197001252e-16, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "q": 0.5000000000000001, "p3": 0.0, "m": 0.0, "exact_star_Psi": 1.7763568394002505e-15, "exact_edge_Psi": -1.3322676295501878e-15, "worst_final_value": 18.00000609224003, "seconds": 1.2177981660352089}`

`RESOURCES {"seconds": 1.2179126249975525, "maxrss_bytes": 75137024}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py scans", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`INTEGER_GRID {"n": 5, "grid": 2001, "evaluations": 8766, "min_Phi": -2.3314683517128287e-14, "arg": [0.8, 1, -0.22360679774997896, -0.22360679774997896], "zero_u_sorted": [0.5, 0.8]}`

`INTEGER_GRID {"n": 6, "grid": 2001, "evaluations": 12208, "min_Phi": -4.476419235288631e-14, "arg": [0.8333333333333334, 1, -0.18257418583505539, -0.18257418583505539], "zero_u_sorted": [0.5, 0.833333333333]}`

`INTEGER_GRID {"n": 7, "grid": 2001, "evaluations": 15368, "min_Phi": -5.684341886080802e-14, "arg": [0.49999999999999994, 1, -0.7071067811865476, 1.3877787807814457e-17], "zero_u_sorted": [0.5, 0.857142857143]}`

`INTEGER_GRID {"n": 8, "grid": 2001, "evaluations": 18832, "min_Phi": 1.2180732613030286e-13, "arg": [0.875, 1, -0.1336306209562122, -0.1336306209562122], "zero_u_sorted": [0.5, 0.875]}`

`INTEGER_GRID {"n": 9, "grid": 2001, "evaluations": 22176, "min_Phi": 1.6786572132332377e-13, "arg": [0.8888888888888888, 1, -0.11785112322837794, -0.11785113119338363], "zero_u_sorted": [0.5, 0.888888888889]}`

`INTEGER_GRID {"n": 10, "grid": 2001, "evaluations": 25698, "min_Phi": 4.547473508864641e-13, "arg": [0.5, 1, -0.7071067811865475, -1.3877787807814457e-17], "zero_u_sorted": [0.5, 0.9]}`

`INTEGER_GRID {"n": 11, "grid": 2001, "evaluations": 29154, "min_Phi": -1.4772183476452481e-12, "arg": [0.9090909090909091, 1, -0.09534626287582629, -0.09534625848552956], "zero_u_sorted": [0.5, 0.909090909091]}`

`INTEGER_GRID {"n": 12, "grid": 2001, "evaluations": 32730, "min_Phi": -9.094947017729282e-13, "arg": [0.49999999999999994, 1, -0.7071067811865476, 1.3877787807814457e-17], "zero_u_sorted": [0.5, 0.916666666667]}`

`RELAXED_GRID {"n": 5, "minima": {"two_atoms": [-2.7913027859764767, [0.4405, 0.6880000000000001, 0.05978806542705967, -0.6636526412636804]], "endpoints_middle": [-2.778817507002067, [0.4385, 0.06180471035626833, 0.31408175042411773, 0.6858490799467991, 6.91696290831545e-05]]}}`

`RELAXED_GRID {"n": 16, "minima": {"two_atoms": [-2267.680214238837, [0.4075, 0.904, 0.020707055841839413, -0.6382950999691165]], "endpoints_middle": [-2230.57106684927, [0.40499999999999997, 0.021213203435596406, 0.09685384309040224, 0.9030610142957195, 8.514261387827099e-05]]}}`

`RESOURCES {"seconds": 1.0493197499890812, "maxrss_bytes": 75399168}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py exact", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`EXACT {"split": "0", "phi_remainder": "0", "hessian": "Matrix([[-4*n**2*(n - 1), 4*S*n**2*(n - 1)], [4*S*n**2*(n - 1), -4*n*(n - 3)*(S**2*n*(n - 1) - 1)]])", "determinant": "16*n**3*(n - 1)*(S**2*n**3 - 5*S**2*n**2 + 4*S**2*n - n + 3)"}`

`N4_NEGATIVE_GVAL {"Gval": 0.0, "weights": null}`

`EXACT_KERNEL {"x": "Matrix([[sqrt(2)/2, -sqrt(2)/2, 0, 0]])", "y": "Matrix([[1/2, 1/2, -1/2, -1/2]])", "projected_matrix": "Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])"}`

`EXACT_EDGE_THETA_N5 {"starred_slacks": {"12": "0", "1k": "-3*(theta - 1)/2", "kl": "-5*(theta - 1)"}, "admissible_theta": "[0,1] in homogeneous slacks; [0,1) for nonzero normalized state"}`

`RESOURCES {"seconds": 0.453339166007936, "maxrss_bytes": 114475008}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py specht", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`SPECHT {"n": 5, "graphs": 160, "dimensions": {"(5,)": 1, "(4, 1)": 4, "(3, 2)": 5, "(3, 1, 1)": 6, "(2, 2, 1)": 5, "(2, 1, 1, 1)": 4, "(1, 1, 1, 1, 1)": 1}, "coxeter_max_abs": 1.1102230246251565e-16, "hook_full_spectrum_max_abs": 2.220446049250313e-15, "conjugate_full_spectrum_max_abs": 2.1094237467877974e-15, "hook_ratio_minus_k_over_j_min": 0.0504744848153269}`

`SPECHT {"n": 6, "graphs": 160, "dimensions": {"(6,)": 1, "(5, 1)": 5, "(4, 2)": 9, "(4, 1, 1)": 10, "(3, 3)": 5, "(3, 2, 1)": 16, "(3, 1, 1, 1)": 10, "(2, 2, 2)": 5, "(2, 2, 1, 1)": 9, "(2, 1, 1, 1, 1)": 5, "(1, 1, 1, 1, 1, 1)": 1}, "coxeter_max_abs": 1.1102230246251565e-16, "hook_full_spectrum_max_abs": 2.4424906541753444e-15, "conjugate_full_spectrum_max_abs": 2.4424906541753444e-15, "hook_ratio_minus_k_over_j_min": 0.0017534470869429164}`

`RESOURCES {"seconds": 0.09702254203148186, "maxrss_bytes": 74973184}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py optimize --starts 200", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`OPTIMIZE {"n": 5, "starts": 200, "optimizer_success": 200, "min_Psi": -1.1102230246251565e-15, "x": [0.8944271909999159, -0.22360679774997894, -0.22360679774997896, -0.22360679774997894, -0.22360679774997902], "q": 0.6499999999999997, "p3": 0.6708203932499369, "m": 0.05000000000000001, "exact_star_Psi": 2.220446049250313e-16, "exact_edge_Psi": -3.3306690738754696e-16, "worst_final_value": 3.333333333333337, "seconds": 0.20891891699284315}`

`OPTIMIZE {"n": 6, "starts": 200, "optimizer_success": 200, "min_Psi": -2.220446049250313e-15, "x": [0.9128709291752769, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539], "q": 0.6999999999999998, "p3": 0.7302967433402217, "m": 0.03333333333333334, "exact_star_Psi": -3.1086244689504383e-15, "exact_edge_Psi": -6.661338147750939e-16, "worst_final_value": 5.333333333333382, "seconds": 0.39194108394440264}`

`OPTIMIZE {"n": 7, "starts": 200, "optimizer_success": 200, "min_Psi": -4.440892098500626e-16, "x": [0.9258200997725514, -0.15430334996209188, -0.15430334996209188, -0.15430334996209188, -0.15430334996209188, -0.15430334996209188, -0.15430334996209188], "q": 0.7380952380952378, "p3": 0.7715167498104594, "m": 0.0238095238095238, "exact_star_Psi": 8.881784197001252e-16, "exact_edge_Psi": -9.992007221626409e-16, "worst_final_value": 13.333333333333488, "seconds": 0.6631227919715457}`

`OPTIMIZE {"n": 8, "starts": 200, "optimizer_success": 200, "min_Psi": 8.881784197001252e-16, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "q": 0.5000000000000001, "p3": 0.0, "m": 0.0, "exact_star_Psi": 1.7763568394002505e-15, "exact_edge_Psi": -1.3322676295501878e-15, "worst_final_value": 18.000000000000117, "seconds": 0.9447611249634065}`

`RESOURCES {"seconds": 0.9448842089623213, "maxrss_bytes": 75759616}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py targeted", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`TARGETED_N4 {"Gval": -2.220446049250313e-15, "W": 1.0, "weights": [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], "eigenvalues": [0.0, 0.0, 0.0, 2.0], "x": [0.0, 0.0, -0.7071067811865475, 0.7071067811865475], "differential_evolution_evaluations": 18564, "slsqp_starts": 60}`

`UNIFORM_FAILURE {"n": 4, "x": [-0.8456820832937901, 0.19392709711465161, 0.19392709711465161, 0.45782788906448685], "min_slack": [-0.14025117089308015, [1, 4]]}`

`STAR_EXPANDED {"n": 4, "lhs": 24.0, "rhs": 24.00000000000001, "claimed": 24}`

`STAR_EXPANDED {"n": 5, "lhs": 120.00000000000007, "rhs": 119.99999999999997, "claimed": 120}`

`STAR_EXPANDED {"n": 6, "lhs": 359.9999999999999, "rhs": 360.0, "claimed": 360}`

`STAR_EXPANDED {"n": 7, "lhs": 839.9999999999998, "rhs": 839.9999999999999, "claimed": 840}`

`STAR_EXPANDED {"n": 8, "lhs": 1680.0000000000002, "rhs": 1680.0, "claimed": 1680}`

`STAR_EXPANDED {"n": 9, "lhs": 3024.0, "rhs": 3024.0000000000005, "claimed": 3024}`

`RESOURCES {"seconds": 1.6379829999641515, "maxrss_bytes": 76136448}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py n4search", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`N4_N_PARAMETER_SEARCH {"Gval": -0.024691358021919685, "Gval_over_W2": -0.014715702538821294, "W": 1.2953346653241038, "weights": [[0.0, 0.1111115549710065, 0.5428891109556647, 1.1900480600957053e-12], [0.1111115549710065, 0.0, 0.11111155497025835, 0.5302224444259842], [0.5428891109556647, 0.11111155497025835, 0.0, 0.0], [1.1900480600957053e-12, 0.5302224444259842, 0.0, 0.0]], "x": [-0.07958308136532417, 0.7776748817496152, -0.07958140292559308, -0.618510397458698], "lam": 1.1968897768828253, "direct_Gval": -0.024691358021920518, "parameters": [4.7123877693902445, 5.48771297983355, 2.6179955735988045, 2.6850743850396317e-13]}`

`RESOURCES {"seconds": 3.683229125046637, "maxrss_bytes": 77348864}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py certificate", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`RATIONAL_N4_COUNTEREXAMPLE {"edge_order": "12,13,14,23,24,34", "weights": ["3/19", "2081/3800", "0", "3/19", "10/19", "0"], "lambda_top": "24/19", "other_eigenvalues": ["0", "5/19", "2381/1900"], "x": "Matrix([[sqrt(19)/38, -7*sqrt(19)/38, sqrt(19)/38, 5*sqrt(19)/38]])", "eigenvector_residual": "Matrix([[0], [0], [0], [0]])", "Gval": "848853/34295000", "Gval_decimal": 0.024751508966321622, "Gval_over_W2": "6790824/529890259", "Gval_over_W2_decimal": 0.01281552903579607}`

`EXACT_ONE_POSITIVE_BOUND {"residual": "0"}`

`RESOURCES {"seconds": 0.34010854200460017, "maxrss_bytes": 115687424}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py certificate", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`RATIONAL_N4_COUNTEREXAMPLE {"edge_order": "12,13,14,23,24,34", "weights": ["9/83", "899917/1660000", "0", "9/83", "44/83", "0"], "lambda_top": "99/83", "other_eigenvalues": ["0", "16/83", "989917/830000"], "x": "Matrix([[sqrt(166)/166, -5*sqrt(166)/83, sqrt(166)/166, 4*sqrt(166)/83]])", "eigenvector_residual": "Matrix([[0], [0], [0], [0]])", "Gval": "-1390241124027/57178700000000", "Gval_decimal": -0.024313968733584358, "Gval_over_W2": "-5560964496108/380077315651787", "Gval_over_W2_decimal": -0.014631140210437482}`

`EXACT_ONE_POSITIVE_BOUND {"residual": "0"}`

`RESOURCES {"seconds": 0.37714041699655354, "maxrss_bytes": 116015104}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py phiopt", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`PHI_OPTIMIZE {"n": 5, "starts": 80, "success": 75, "min_Phi": -2.1316282072803006e-14, "x": [0.7071067811865476, -0.7071067811865476, 0.0, 0.0, 0.0]}`

`PHI_OPTIMIZE {"n": 6, "starts": 80, "success": 79, "min_Phi": -1.406874616804999e-13, "x": [0.9128709291752769, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539, -0.18257418583505539]}`

`PHI_OPTIMIZE {"n": 7, "starts": 80, "success": 73, "min_Phi": -1.7053025658242404e-13, "x": [0.7071067811865477, 4.185443782346218e-10, -7.90593584374412e-11, -4.0403808884213983e-10, -0.7071067811865477, -8.312361766125382e-11, 1.4767680542610833e-10]}`

`PHI_OPTIMIZE {"n": 8, "starts": 80, "success": 72, "min_Phi": -4.547473508864641e-13, "x": [0.7071067811865477, 1.0841158551021653e-11, -7.073219498845487e-10, 1.7009501913645754e-10, -0.7071067811865477, 8.926040340937373e-10, -3.125375632672605e-10, -5.3680708781811744e-11]}`

`RESOURCES {"seconds": 2.7332629170268774, "maxrss_bytes": 76578816}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py model", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`MODEL {"n": 5, "graphs": 80, "dimension": 5, "spectrum_max_abs": 1.7763568394002505e-15, "projection_constraint_max_abs": 7.771561172376096e-16, "norm_identity_max_abs": 3.552713678800501e-15}`

`MODEL {"n": 6, "graphs": 80, "dimension": 9, "spectrum_max_abs": 1.1102230246251565e-15, "projection_constraint_max_abs": 1.3322676295501878e-15, "norm_identity_max_abs": 7.105427357601002e-15}`

`BRANCHING {"tau": [2, 2, 1, 1], "sigma": [2, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [5, 6]}`

`BRANCHING {"tau": [3, 2, 1, 1], "sigma": [3, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [4, 4]}`

`BRANCHING {"tau": [4, 2, 1, 1], "sigma": [4, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [4, 4]}`

`BRANCHING {"tau": [2, 2, 2, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [8, 9]}`

`BRANCHING {"tau": [2, 1, 1, 1, 1, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [6, 9]}`

`BRANCHING {"tau": [2, 2, 1, 1, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [7, 9]}`

`RESOURCES {"seconds": 0.03563133394345641, "maxrss_bytes": 77053952}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py model", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`MODEL {"n": 5, "graphs": 80, "dimension": 5, "spectrum_max_abs": 1.7763568394002505e-15, "projection_constraint_max_abs": 7.771561172376096e-16, "norm_identity_max_abs": 3.552713678800501e-15}`

`MODEL {"n": 6, "graphs": 80, "dimension": 9, "spectrum_max_abs": 1.4432899320127035e-15, "projection_constraint_max_abs": 1.3322676295501878e-15, "norm_identity_max_abs": 7.105427357601002e-15}`

`BRANCHING {"tau": [2, 2, 1, 1], "sigma": [2, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [5, 6]}`

`BRANCHING {"tau": [3, 2, 1, 1], "sigma": [3, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [4, 4]}`

`BRANCHING {"tau": [4, 2, 1, 1], "sigma": [4, 2, 2], "tau_four_box_survivors": [[2, 1, 1]], "sigma_four_box_survivors": [[2, 2]], "ordinary_star_minima": [4, 4]}`

`BRANCHING {"tau": [2, 2, 2, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [8, 9]}`

`BRANCHING {"tau": [2, 1, 1, 1, 1, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [6, 9]}`

`BRANCHING {"tau": [2, 2, 1, 1, 1, 1], "sigma": [2, 2, 2, 2], "tau_four_box_survivors": [], "sigma_four_box_survivors": [], "ordinary_star_minima": [7, 9]}`

`RESOURCES {"seconds": 0.016179708007257432, "maxrss_bytes": 76873728}`

`COMMAND {"command": "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py algebra", "seed": 20261111, "threads": 1, "timeout_seconds": 240, "nice": 10}`

`ALGEBRA {"n": 4, "vectors": 300, "max_abs": {"gval_psi": 9.769962616701378e-15, "split": 2.220446049250313e-16, "gap_affine": 3.3306690738754696e-15, "pair_identity": 5.329070518200751e-15, "q_square_identity": 5.828670879282072e-16, "q_pair_identity": 7.355227538141662e-16, "covariance_star": 7.993605777301127e-15, "uniform_N": 2.3314683517128287e-15, "uniform_A": 4.440892098500626e-15, "expanded_Gval": 7.771561172376096e-15}, "min_m_minus_M": 0.011408343995856773, "min_n_den_Psi_minus_Phi": 0.007425987197142554, "min_a": 0.011873588499084875, "min_random_Phi": 0.04750582185704824}`

`ALGEBRA {"n": 5, "vectors": 300, "max_abs": {"gval_psi": 2.4868995751603507e-14, "split": 1.3322676295501878e-15, "gap_affine": 6.661338147750939e-15, "pair_identity": 4.440892098500626e-15, "q_square_identity": 4.996003610813204e-16, "q_pair_identity": 7.771561172376096e-16, "covariance_star": 8.881784197001252e-15, "uniform_N": 3.9968028886505635e-15, "uniform_A": 7.105427357601002e-15, "expanded_Gval": 1.0658141036401503e-14}, "min_m_minus_M": 0.01360651560029856, "min_n_den_Psi_minus_Phi": 20.839849623544257, "min_a": 0.3642706592580021, "min_random_Phi": 0.7239550956105621}`

`ALGEBRA {"n": 6, "vectors": 300, "max_abs": {"gval_psi": 5.684341886080802e-14, "split": 3.552713678800501e-15, "gap_affine": 8.881784197001252e-15, "pair_identity": 7.105427357601002e-15, "q_square_identity": 7.494005416219807e-16, "q_pair_identity": 7.771561172376096e-16, "covariance_star": 1.1546319456101628e-14, "uniform_N": 3.552713678800501e-15, "uniform_A": 7.105427357601002e-15, "expanded_Gval": 1.3322676295501878e-14}, "min_m_minus_M": 0.028893558841178134, "min_n_den_Psi_minus_Phi": 98.06059873376786, "min_a": 0.6844141472554601, "min_random_Phi": 15.735246346354373}`

`ALGEBRA {"n": 7, "vectors": 300, "max_abs": {"gval_psi": 1.1368683772161603e-13, "split": 7.105427357601002e-15, "gap_affine": 9.769962616701378e-15, "pair_identity": 4.440892098500626e-15, "q_square_identity": 5.551115123125783e-16, "q_pair_identity": 7.216449660063518e-16, "covariance_star": 1.509903313490213e-14, "uniform_N": 4.884981308350689e-15, "uniform_A": 8.881784197001252e-15, "expanded_Gval": 1.4654943925052066e-14}, "min_m_minus_M": 0.03564875683315622, "min_n_den_Psi_minus_Phi": 542.8398143023923, "min_a": 0.8746758000548924, "min_random_Phi": 26.719935391643673}`

`ALGEBRA {"n": 8, "vectors": 300, "max_abs": {"gval_psi": 2.2737367544323206e-13, "split": 1.4210854715202004e-14, "gap_affine": 7.105427357601002e-15, "pair_identity": 5.773159728050814e-15, "q_square_identity": 6.661338147750939e-16, "q_pair_identity": 8.326672684688674e-16, "covariance_star": 1.687538997430238e-14, "uniform_N": 6.217248937900877e-15, "uniform_A": 1.2434497875801753e-14, "expanded_Gval": 1.5987211554602254e-14}, "min_m_minus_M": 0.05989971804725272, "min_n_den_Psi_minus_Phi": 2057.4957820170994, "min_a": 0.9199558239390218, "min_random_Phi": 80.73697729614435}`

`ALGEBRA {"n": 9, "vectors": 300, "max_abs": {"gval_psi": 3.410605131648481e-13, "split": 1.4210854715202004e-14, "gap_affine": 7.993605777301127e-15, "pair_identity": 4.884981308350689e-15, "q_square_identity": 4.440892098500626e-16, "q_pair_identity": 7.216449660063518e-16, "covariance_star": 1.7763568394002505e-14, "uniform_N": 7.105427357601002e-15, "uniform_A": 1.5987211554602254e-14, "expanded_Gval": 1.7763568394002505e-14}, "min_m_minus_M": 0.050893947184497496, "min_n_den_Psi_minus_Phi": 4034.3753242922776, "min_a": 1.0455999963059204, "min_random_Phi": 264.9472712870991}`

`SPECIAL {"n": 4, "star": {"Psi": -2.220446049250313e-16, "Phi": -8.289665250534501e-15, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.6666666666666667}, "edge": {"Psi": 0.0, "Phi": 8.881784197001252e-15, "min_uniform_slack": 1.480297366166875e-16, "projected_norm": 0.4999999999999999}, "path_slack": -0.027777777777777707, "path_slack_times_n_minus_2": -0.055555555555555414}`

`SPECIAL {"n": 5, "star": {"Psi": 2.220446049250313e-16, "Phi": -6.66133814775092e-15, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.833333333333333}, "edge": {"Psi": -3.3306690738754696e-16, "Phi": 2.842170943040401e-14, "min_uniform_slack": 2.96059473233375e-16, "projected_norm": 0.6666666666666665}, "path_slack": -0.02777777777777768, "path_slack_times_n_minus_2": -0.08333333333333304}`

`SPECIAL {"n": 6, "star": {"Psi": -3.1086244689504383e-15, "Phi": -1.406874616804999e-13, "min_uniform_slack": 2.220446049250313e-16, "projected_norm": 0.8999999999999998}, "edge": {"Psi": -6.661338147750939e-16, "Phi": 5.684341886080802e-14, "min_uniform_slack": 1.554312234475219e-16, "projected_norm": 0.75}, "path_slack": -0.024999999999999772, "path_slack_times_n_minus_2": -0.09999999999999909}`

`SPECIAL {"n": 7, "star": {"Psi": 8.881784197001252e-16, "Phi": -1.3470706032118563e-13, "min_uniform_slack": 2.220446049250313e-16, "projected_norm": 0.9333333333333331}, "edge": {"Psi": -9.992007221626409e-16, "Phi": 1.1368683772161603e-13, "min_uniform_slack": 1.7023419710919053e-16, "projected_norm": 0.7999999999999997}, "path_slack": -0.0222222222222222, "path_slack_times_n_minus_2": -0.111111111111111}`

`SPECIAL {"n": 8, "star": {"Psi": 1.7763568394002505e-15, "Phi": 1.2180732613030286e-13, "min_uniform_slack": -2.220446049250313e-16, "projected_norm": 0.9523809523809522}, "edge": {"Psi": -1.3322676295501878e-15, "Phi": 2.2737367544323206e-13, "min_uniform_slack": 3.7007434154171876e-16, "projected_norm": 0.8333333333333331}, "path_slack": -0.019841269841269604, "path_slack_times_n_minus_2": -0.11904761904761763}`

`RESOURCES {"seconds": 5.765801917004865, "maxrss_bytes": 77496320}`
