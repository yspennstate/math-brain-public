from pathlib import Path
import json

root = Path(__file__).resolve().parent
def append(name, value):
    with (root/name).open('a', encoding='utf-8') as f:
        f.write(value)

p = root/'SECOND_ATTEMPT.md'
s = p.read_text(encoding='utf-8')
s = s.replace('For each fixed z, the probability that S_n(z) differs from V_n(z)', 'For Lebesgue-almost every fixed z, the probability that S_n(z) differs from V_n(z)')
s = s.replace('dense in C_c(C) on each compact set', 'dense in the unit ball of C_c(C) on each compact set')
p.write_text(s, encoding='utf-8')

append('SECOND_ATTEMPT.md', r'''

## Route B: exact atomic-mixture reduction, and where the transfer fails

Suppose the fixed entry law P has two distinct atoms a,b with probabilities p_a,p_b>0. Put q=2 min(p_a,p_b) and c=(b-a)/2. In the heavy-tailed setting q<1: q=1 would force the entire law to be the equal two-point distribution. Define the residual probability law

P_res = [P-(q/2) delta_a-(q/2) delta_b]/(1-q).

Its masses are nonnegative and its total mass is one. Draw a Bernoulli(q) mask delta, a fair sign epsilon, and a residual sample Y independently. Set D=(a+b)/2 when delta=1 and D=Y otherwise. Then X=D+c delta epsilon has precisely law P: conditioning on delta gives atoms a,b with masses q/2 and the remaining law with weight 1-q. This proves the decomposition for complex as well as real atoms. If E|X|^kappa is finite, so is E|D|^kappa, since the residual law is dominated by P/(1-q) plus a finite deterministic contribution.

Take independent copies entrywise. Conditional on all delta_ij and D_ij, the signs remain independent fair signs, so

c^{-1}(X_n-n^{1/alpha}zI)=delta_n circ epsilon_n+B_n,
B_n=c^{-1}(D_n-n^{1/alpha}zI).

Here circ denotes entrywise multiplication. The core and mask are dependent on each other, but are both independent of the signs. Unconditionally each entry of the bounded noise delta epsilon is independent and identically distributed; it is NOT independent of the core D. After conditioning the mask, the noise has zero entries on its complement, so it is no longer iid. Thus an iid additive-noise theorem cannot be applied by either conditioning choice. This is the precise obstruction to treating a general mixture as an independent convolution.

### The mask itself is not the obstruction: complete super-regularity proof

Fix a sufficiently small constant epsilon_0>0 and delta_0=q/2. With probability at least 1-exp(-c_q n), the zero-one mask is (delta_0,epsilon_0)-super-regular in Cook's Definition 1.23: every row and column has at least delta_0 n ones, and every cut I by J with |I|,|J|>=epsilon_0 n contains at least delta_0 |I||J| ones.

For completeness, if S is the sum of m independent Bernoulli(q) variables, then

P(S<=qm/2)<=exp(-qm/8).

Indeed, exponential Markov at lambda=log 2 gives
P(S<=qm/2)<= exp(lambda qm/2)(1-q+q exp(-lambda))^m
<=exp[-qm(1-log 2)/2]<=exp(-qm/8).
The last inequality uses log 2<3/4; for example integrate 1/t on [1,2], whose strict convexity places its integral below the trapezoidal value 3/4. Apply this to each row and column and union bound to obtain 2n exp(-qn/8). For any fixed large cut use m=|I||J|>=epsilon_0^2 n^2. There are at most 4^n cuts, giving at most exp(2n log 2-q epsilon_0^2 n^2/8). The sum of these two errors is at most exp(-c_q n) for large n (constants may also depend on epsilon_0). This proves the assertion without assuming independence between different cuts.

Choose sigma_0=1/2. Cook's thresholded profile delta_n(sigma_0) is the same zero-one mask. Choosing epsilon_0 small enough to satisfy epsilon_0<c_1 delta_0 sigma_0^2 meets Theorem 1.24's super-regularity hypotheses. The Rademacher sign law is centered, variance one, bounded, and has a fixed controlled second moment as required in Definition 1.3. Also ||epsilon_n||<=n deterministically, hence ||delta_n circ epsilon_n||<=n, by the Frobenius bound. The residual moment bound and the same maximum-entry argument as Step 1 give a summable probability that ||B_n|| exceeds some fixed polynomial, uniformly for z in a fixed disk.

Cook's Theorem 1.24 (current fetched PDF, printed page 15) therefore applies uniformly after conditioning on good masks and polynomial-size cores. It supplies

P(s_min(delta_n circ epsilon_n+B_n)<=n^{-beta}, ||delta_n circ epsilon_n+B_n||<=n^gamma)
<=C sqrt(log n/n),

with beta depending on gamma and constants depending on fixed q and the sign law. Adding the summable core-norm and mask failures gives the same nonsummable rate, not the needed summable one. The reduction is valid; it does not improve the hard-edge error.

### Audit of the neighboring high-confidence theorems

Tao--Vu, arXiv:0805.3167v3, Definition 5.1, printed page 10, explicitly includes an upper bound on E|x|^2. Thus its controlled-second-moment terminology does not cover the unconditioned infinite-variance X. Remark 5.3 says a non-identically distributed extension is 'quite likely' and then states that the paper focuses on iid entries: that is not a theorem with the required quantifiers. Its fixed-vector Theorem 6.4 does allow independent controlled laws, but a global minimum over all directions is an additional step. Moreover the conditioned mask has deterministic zero entries outside the mask, which fail individual controlled nondegeneracy. Theorem 3.2 has an o(1) error as well as the norm-tail term; it is not a summable bound merely by choosing its polynomial parameter large.

Vishesh Jain, arXiv:1908.11255v3, Theorem 1.1, printed pages 4--5, supplies high-confidence bounds for arbitrary large deterministic cores with iid centered variance-one noise. It does not state the same bound for a nonseparable zero-one amplitude mask. Applying it before conditioning would wrongly assume independence of the core and noise; applying it after conditioning would wrongly assume iid noise. No such transfer has been proved here.

Thus Route B reduces a broad atomic benchmark to a concrete structured-noise invertibility question, but the papers inspected do not close it. An improvement of Cook's conditional profile theorem to, for example, n^{-2} error at some polynomial threshold for each fixed polynomial-size core would finish this two-atom subclass by the already-proved concentration argument. This improvement is a remaining question, not an asserted theorem. Entry laws with fewer than two atoms would also require a more general decomposition to obtain a full solution by this route.

## Hostile-referee checks for this renewed attempt

1. Lemma A.1 was reread in the actual survey: it assumes independent nonconstant complex entries and positive fixed truncated variance, not finite variance. Its exact error is c sqrt(log(cs))(t s^2+n^{-1/2}). The norm and scaling substitutions above include the additional n^{-1/alpha} factor.
2. The source's in-probability logarithmic potential input is needed only for Lebesgue-almost every fixed z. Fubini is applied to this full-area set, not to an uncountable intersection of probability-one events.
3. Concentration identifies the deterministic mean without an expectation-uniform-integrability assumption: if |E S_n-ell|>2t along a subsequence, the events |S_n-E S_n|<=t and |S_n-ell|<=t cannot both occur, although their probabilities tend to one. This contradiction proves E S_n->ell.
4. All upper clips are eventually inactive uniformly on each disk by a summable polynomial norm bound. Consequently the lower clipping defect is nonnegative and supported on the hard-edge exceptional set. Without this eventual inactivity the support argument would be invalid.
5. Uniform local L2 bounds concern the TRUE eigenvalue potentials, obtained from fractional eigenvalue moments; they do not claim uniform negative-log integrability of all singular values. Finite eigenvalue singularities have area zero and locally integrable logarithms.
6. The dyadic argument uses nonnegativity of exceptional areas. It establishes vanishing average area, not eventual absence of bad dimensions. The Jordan example checks this exact limitation.
7. The chosen metric is sufficient, and the result holds for any other bounded metric d' inducing weak convergence: continuity at mu gives, for each epsilon>0, a delta>0 such that d(rho,mu)<delta implies d'(rho,mu)<epsilon. If d'<=L, its average is at most epsilon+(L/delta) times the average of d. Let N tend to infinity and then epsilon decrease to zero.
8. The Jordan/cyclic example fails the iid-entry hypothesis and also is not given as principal minors of an iid infinite array. It only disproves a proposed implication from the general potential/concentration inputs. It is not a counterexample to the question.
9. The numerical script second_checks.py checks 15 small Jordan/cyclic cases, the null-vector residual, cyclic singular-value lower bound, and clipped rank-one inequality, plus an exact rational atomic-mixture identity. All checks passed; SECOND_CHECKS.json retains the values. The largest dense matrix is 64 by 64. These finite tests supplement, not replace, the proofs above.
10. CesaroCore.lean is a deliberately limited formalization of the algebraic inequality used to interpolate between dyadic partial averages. The probability, random-matrix and potential arguments are not formally verified. The Lean result will be recorded separately when the single running check finishes.

## Final mathematical gap

The unrestricted source law now has an almost-sure averaged/statistical convergence theorem, in addition to the earlier smoothness and independent-convolution subclasses. To get full-sequence almost-sure convergence, it remains to eliminate sparse exceptional dimensions: for example prove ||S_n-V_n||_{L1(K)}->0 almost surely for every bounded disk K, or obtain a summable fixed-z lower-singular-value tail sufficient for that conclusion. No argument here shows area(B_n)->0 almost surely; only its Cesaro average tends to zero. No counterexample respecting iid entries and the exact source tail/angular hypotheses has been constructed. Verdict remains PARTIAL.
''')

append('ATTEMPT.md', '''\n\n## Renewed serious attempt, 2026-10-11\n\nThe full proofs and theorem audits are saved in SECOND_ATTEMPT.md. Two previously unpursued routes here were considered: spatially integrated clipping defects, and a conditional atomic-mixture mask transfer to high-confidence invertibility. The latter was pursued first, giving a complete mixture decomposition and super-regularity proof, but Cook's applicable theorem retains the nonsummable error. The former yields a proved unrestricted theorem: almost surely (1/N) sum_{n<=N} mu_n converges weakly to mu_alpha, and (1/N) sum_{n<=N} d(mu_n,mu_alpha) tends to zero for every bounded compatible weak metric. Thus exceptional dimensions have density zero almost surely. This does not settle full-sequence convergence. A complete non-iid Jordan/cyclic counterexample in that file shows why the general potential inputs cannot eliminate sparse exceptions. No novelty is claimed. The remaining gap is precisely almost-sure decay of the spatial clipping defect, rather than its Cesaro average, or a summable invertibility estimate exploiting the iid-entry structure. Numerical checks are SECOND_CHECKS.json; the limited Lean check is tracked in CESARO_LEAN_CHECK.txt.\n''')

lit = (root/'LITERATURE.md').read_text(encoding='utf-8').replace('The relevant hit is Ashwin Jain,', 'The relevant hit is Vishesh Jain,')
(root/'LITERATURE.md').write_text(lit, encoding='utf-8')
append('LITERATURE.md', '''\n\n## Second-attempt searches and exact theorem audit, 2026-10-11\n\nRead-only math-store query: `Cook Jain bounded amplitude Bernoulli profile arbitrary deterministic perturbation summable smallest singular value`. Returned generic subgaussian and Borel--Cantelli cards; none supplies the missing conditional profile theorem. No brain write was performed.\n\nDirect arXiv PDF fetches: https://arxiv.org/pdf/1608.07347 ; https://arxiv.org/pdf/1908.11255 ; https://arxiv.org/pdf/0805.3167 . All succeeded. Files second_cook.pdf/.txt, second_jain.pdf/.txt, second_taovu.pdf/.txt preserve the versions inspected. The precise URLs and date are in second_search_log.json.\n\nArXiv API query: `(ti:"invertibility" OR ti:"singular value") AND (all:"perturbation" OR all:"inhomogeneous") AND cat:math.PR`, newest first, max_results=60. Successful response in second_inhomogeneous_search.xml; exact escaped URL in second_search_log.json. Relevant neighboring hits include arXiv:1909.04219v4, *The smallest singular value of inhomogeneous square random matrices*, whose abstract assumes expected squared Hilbert--Schmidt norm <=Kn^2; and arXiv:2412.18906v2, *The Rank and Singular Values of the Inhomogeneous Subgaussian Random Matrices*, a subgaussian model. These are abstract-level leads, not verified solutions or direct implications for the unrestricted infinite-variance model.\n\nTheorem-level references:\n\n- Nicholas Cook, *Lower bounds for the smallest singular value of structured random matrices*, Annals of Probability 46 (2018), 3442--3500, arXiv:1608.07347. In the currently fetched PDF, the relevant super-regular-profile result is **Theorem 1.24, printed page 15**, and its definition is Definition 1.23, page 14. This corrects reliance on the prior handoff's different numbering (1.26). Its error is O(sqrt(log n/n)) under a polynomial norm cap. SECOND_ATTEMPT.md proves why the conditioned two-atom mask meets its hypotheses, and why the error still does not settle the question.\n- Terence Tao and Van Vu, *Smooth analysis of the condition number and the least singular value*, Mathematics of Computation 79 (2010), 2333--2352, arXiv:0805.3167v3. Theorem 3.2, printed page 6, includes an o(1) term; Definition 5.1, page 10, includes bounded second moment; Remark 5.3, page 10, describes rather than proves a likely non-identically distributed extension. The fixed-vector Theorem 6.4, page 12, is insufficient on its own to control the least singular value over all directions.\n- **Vishesh Jain**, *Quantitative Invertibility of Random Matrices: a Combinatorial Perspective*, Discrete Analysis 2021:10, 40 pp., DOI 10.19086/da.27994, arXiv:1908.11255v3. Theorem 1.1, printed pages 4--5, requires iid mean-zero variance-one noise. The previously recorded first name 'Ashwin' was an error, corrected here and in the earlier paragraph. The conditional masked noise does not meet the iid hypothesis.\n\nNo inspected paper states and proves the source-matching unrestricted almost-sure theorem. The new averaged theorem is our deduction from source estimates, not a theorem in print asserted to solve C0031. The literature verdict therefore remains unverified as to present openness, with no SOLVED_IN_LITERATURE claim.\n''')

claims = [
 dict(problem_id='C0031', claim='Under the exact normalized tail/angular source hypotheses, the Cesaro averages of the empirical spectral measures converge weakly almost surely to mu_alpha.', status='proved', proof_location='SECOND_ATTEMPT.md, Route A Steps 1--5', remaining_gap='Full-sequence almost-sure convergence remains unresolved.', checks='Source Lemma A.1 reread; scaling, local L2, support and dyadic averaging audited; Lean interpolation check tracked separately.'),
 dict(problem_id='C0031', claim='Under the unrestricted source hypotheses, the Cesaro mean of any bounded compatible weak metric distance to mu_alpha tends to zero almost surely; exceptional dimensions have density zero.', status='proved', proof_location='SECOND_ATTEMPT.md, Route A Step 5 and referee check 7', remaining_gap='Density-zero exceptional dimensions can still be infinite.', checks='Countable determining family, geometric metric tail, and continuity at the fixed limit checked.'),
 dict(problem_id='C0031', claim='A two-atom entry law admits the stated independent-sign random-mask decomposition; the iid positive-density mask is super-regular except with exponentially small probability.', status='proved', proof_location='SECOND_ATTEMPT.md, Route B decomposition and super-regularity proof', remaining_gap='The applicable shifted-profile invertibility bound has nonsummable error; law class also excludes entries with fewer than two atoms.', checks='Exact residual probability identity, explicit Chernoff bound and cut union bound; rational finite example in SECOND_CHECKS.json.'),
 dict(problem_id='C0031', claim='Independent rows, in-probability spectral convergence, uniform moment/local L2 bounds and convergent clipped potentials do not imply full almost-sure spectral convergence in general.', status='counterexample', proof_location='SECOND_ATTEMPT.md, Jordan/cyclic reduction counterexample', remaining_gap='This is not an iid-entry counterexample to C0031.', checks='Complete spectrum and approximate-null-vector computations; second Borel--Cantelli; 15 finite numerical consistency checks.'),
 dict(problem_id='C0031', claim='Fifteen Jordan/cyclic numerical cases satisfy the stated residual, cyclic minimum and clipped rank-one inequalities.', status='numerical_evidence', proof_location='second_checks.py and SECOND_CHECKS.json', remaining_gap='Finite checks alone establish no asymptotic theorem.', checks='All assertions passed; maximum dense size 64.')
]
for c in claims:
    append('CLAIMS.jsonl', json.dumps(c, ensure_ascii=False)+'\n')
append('STATUS.md', '\n2026-10-11 renewed attempt: Proved unrestricted almost-sure Cesaro and statistical weak convergence; completed the two-atom mask decomposition and super-regularity proof. Cook/Tao--Vu/Jain audits do not close the summable-tail gap. A complete Jordan/cyclic non-iid stress test shows why sparse exceptional dimensions cannot be ruled out by the general potential inputs. Fifteen numerical cases and one exact rational mixture check passed. Lean dyadic interpolation check is running singly.\n')
print('Saved renewed proofs, theorem audits, claims and progress log.')
