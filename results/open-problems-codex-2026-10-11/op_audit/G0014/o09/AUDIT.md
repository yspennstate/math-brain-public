VERDICT: PASS

Audit date: 2026-10-11. This passes as a complete **literal refutation**, not as a proof of a corrected Bramson theorem. The claimant expressly uses SOLVED in this negative sense in STATUS.md and ATTEMPT.md:21,127–129. No mathematical repair is needed for that verdict.

## What is claimed and what the problem asks

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md directly from the claimant's folder, without changing them. Line references below use the current ATTEMPT.md, whose last line is 129.

The problem asks whether, under the source's Theorem 2.1 hypotheses, the displayed signed derivative martingale is uniformly integrable, equivalently has a positive limit on survival, and the time-depth front has the printed logarithmic correction and limiting-law assertion. The claimant does not prove those assertions. It proves that they cannot hold as printed, using two separate obstructions, and labels its single-type positive theorem as a conditional special case. A refutation answers the literal conjecture; it does not close the intended corrected research programme.

I independently downloaded arXiv:2608.21125. The PDF is nine pages, names Achyut Kumar and Abhinav Duddala, and contains exactly the problematic formulas reported by the claimant. PDF p.3 defines

    B(theta)[i,j] = M[i,j] E exp(-theta A[i,j]),
    I = inf_{theta>0} log rho(B(theta))/theta,
    c_* = 1/I.

PDF p.4 defines the untruncated signed derivative expression with initial value zero, calls it a martingale in Proposition 3.1, and asserts UI and positive survival limit in Conjecture 3.2. Its front coefficient is indeed 3/(2 theta_* c_*). PDF p.3 lists R1, kappa<1, rho(M)>1, irreducibility and the common positive exponential-moment parameter. The finite matrix is explicit. Section 1.2 first writes A_e>=0, then explicitly calls the activation weights positive; the claimant's strict-positivity scope qualification is important. PDF p.2 retains finite variance of the forward-degree law and iterated decoupling limits. The source's reference [1] still has the placeholder 2608.XXXXX.

## Independent proof checks

### Proposition A: ATTEMPT.md:25–41

The argument is correct. For an integrable martingale starting at zero, E D_n=0. UI and almost-sure convergence imply L1 convergence; I checked the claimant's proof rather than simply invoking that theorem. Its Fatou inequality at line 29 follows pointwise because |D|>2K implies eventually |D_n|>K. Its clipped variables are bounded and continuous, so dominated convergence applies. The two clipping-error expectations are each bounded by epsilon, yielding line 35. Hence E D=0. A nonnegative integrable random variable with positive probability of being strictly positive cannot have expectation zero.

The extinction argument is also valid: in a locally finite GW tree, extinction means some generation is empty, and every subsequent derivative sum is zero. Supercritical irreducible finite-type branching has positive survival probability. Consequently the claimed survival positivity, together with extinction value zero, supplies precisely the global nonnegativity needed in Proposition A. No assumption that the finite-generation signed variables are nonnegative is made.

This refutes the simultaneous source assertions **if the displayed object has the martingale property claimed by the source**. The claimant correctly records that qualification at line 41. It does not independently establish that the incorrectly weighted multitype formula is a martingale. This is not being counted as a proof that every printed multitype sequence fails UI; the separate speed obstruction below is sufficient to refute the complete front conjecture.

As an exact sanity check, I considered D_n=1-2^n times the indicator that the first n fair coin tosses are all heads. It is a signed martingale, starts at zero, has mean zero at every generation, and tends almost surely to 1. The rare negative-tail contribution is 1-2^(-n), so it is not UI. This corroborates the distinction between a positive limit and UI; it is not a cascade counterexample.

### Proposition B: ATTEMPT.md:45–64

Every inequality and quantifier checks out for the stated finite-type, strictly positive activation setting. The exponential moment implies finite means. With a_max the largest mean on a nonzero transition, Jensen yields

    B(theta) >= exp(-theta a_max) M
    log rho(B(theta))/theta >= log rho(M)/theta-a_max >= -a_max.

Perron comparison is valid for nonnegative matrices, and B(theta) has M's irreducible support and positive Perron root. Strictly positive activations give entrywise convergence B(theta)->0 by dominated convergence. Finite dimension makes the maximum row sum tend to zero, hence rho(B(theta))->0. At a finite theta the ratio is negative. Thus -infinity<I<0, so the printed c_* is finite and strictly negative.

The front is a nonnegative depth. For a finite theta_*, its remainder after the printed centering has the deterministic lower bound

    -c_* t + [3/(2 theta_* c_*)] log t -> +infinity.

It cannot be tight. If a finite theta_* does not exist, the claimed formula is instead undefined; that does not rescue it. The source's erroneous Theorem 2.1 conclusion is not used as an assumption in this proof. In particular, the claimant is not deriving a contradiction by assuming an already contradictory law of large numbers. It uses the activation representation and hypotheses directly.

Line 57 properly limits this proof: zero-time atoms can prevent B(theta)->0, and infinite types invalidate the finite-matrix argument without further bounds. The source describes the positive finite-type case, and the claimant does not claim this proof for those extensions. Changing the speed sign would change the question being answered.

### Proposition C: ATTEMPT.md:68–82

The inversion is rigorous. For each fixed K, the deterministic integer generations n_+ and n_- tend to infinity, and log n_±=log t-log a+o(1). Substitution gives exactly line 78. Tightness over deterministic generations supplies one L and N controlling all sufficiently large n, including these two selected generations. Monotonicity gives both event identities in line 80; the union bound needs neither independence nor pathwise uniform control of R_n. The stated choice of K absorbs the constant, rounding, and o(1) errors.

Therefore the inverse coefficient is b/a=bc. Conditional on b=3/(2 theta_*), it is 3c/(2 theta_*), not the printed 3/(2 theta_* c). This is a valid conditional identity, not an independently proved cascade minimum-time estimate.

### Conditional single-type theorem: ATTEMPT.md:86–99

I fetched and inspected Chen, arXiv:1402.5864, pp.2–3, and Aidekon, arXiv:1101.1810v6, pp.1–3. Their hypotheses and conclusions match this explicitly narrowed claim. With f(theta)=theta f'(theta) and V=theta A+f(theta), direct differentiation gives the two boundary identities at lines 88–89. Since V>=ell=f(theta), the bounds on Y, Z and the weighted second moment at line 91 hold. In particular sup_{v>=ell} v^2 exp(-v) is finite, and sup_{v>=0} v exp(-v)=1/e. These bounds supply Chen's E[Z log_+ Z+Y(log_+Y)^2] condition and Aidekon's corresponding moments. Nonlattice and positive tilted variance are expressly assumed rather than inferred from positivity.

Chen's theorem concerns nontriviality of the limit, **not UI of the signed martingale**. Aidekon supplies the centered generation-minimum law. On extinction the tail event for the minimum eventually holds because the generation is empty. Subtracting that extinction mass gives a proper conditional survival law, since its derivative limit is finite and positive on survival. This proves tightness on survival.

For nonexplosion, I re-derived P(T_n<=j)<=exp(sj)[m E exp(-sA)]^n by counting particles with time at most j and bounding their indicator by exp(sj-sT_v). Positivity allows an s with m E exp(-sA)<1. The bound is summable; Borel–Cantelli for every integer j proves T_n->infinity. Positive edge times also give monotonicity. Proposition C then applies. No original multitype cascade or decorated time-depth process is proved by this special case, and the claimant does not say otherwise.

### Proposition D: ATTEMPT.md:103–111

Correct for ordinary weak convergence to a probability distribution on the real line as all real times tend to infinity. The center h(t)=ct-d log t is eventually continuous, increasing and unbounded. Sequences with centers k and k+1/2 exist. Integer-valued F gives exp(2 pi i(F-h))=exp(-2 pi i h) deterministically, whose expectations alternate between 1 and -1 along these sequences. Weak convergence would force convergence of the bounded continuous sine and cosine expectations. Tightness, lattice subsequences and properly formulated point-process claims are not excluded; the claimant explicitly preserves these possibilities.

## Other issues and limits, with locations

1. **Source multitype normalization, lines 117 and 41:** the criticism is correct. For a row-parent matrix, one parent's conditional weighted offspring expectation is (Bh)_i; the martingale requires a right eigenvector. An exact independent example is B=[[2,1],[4,2]], rho=4, left vector (2,1), right vector (1,2). B times the left vector is (5,10), whereas rho times it is (8,4). The right vector works. A theta-dependent right eigenvector also contributes derivative terms. Naming those corrections is necessary for any future multitype theorem; the present refutation does not rely on pretending the source's normalization is correct.

2. **Finite optimizer, line 118:** the caveat is valid. For deterministic A=1, f(theta)/theta=log(m)/theta-1 has infimum -1 only at infinity. Finite exponential moments alone do not supply a finite tilt or positive tilted variance. This auxiliary law is not presented as an elliptic OU cascade. No model-specific optimizer result is proved here.

3. **Formal verification scope, line 121:** I read obstruction.lean and lean_check.txt. The file contains the nonnegative-zero-integral implication and two elementary algebraic statements, with no added axiom or sorry visible. The saved log records exit code zero. I did not rerun Lean or verify its installation. These artifacts are not a formalization of the stochastic proof, spectral argument or cascade reduction. The claimant states precisely that limitation; my verdict rests on the independent mathematical checks above.

4. **Numerical evidence, line 122:** independent bisection for binary Exp(1) branching gives theta=3.3110704070010035, a=0.2319609529865344, c=4.311070407001005, printed speed=-4.311070407001005, correct coefficient=1.9530257033581553, and sign-repaired printed coefficient=0.10508427387835254. The boundary equation residual is 3.33e-16; the independently evaluated boundary identities are 1 and 3.59e-16, with tilted variance 0.5898839777373526. I also checked the Jensen bound at six tilt values and inverted the deterministic monotone sequence an+b log n at t=10^3,10^6,10^9. Its correctly centered residual remains between -3.58 and -3.42; the incorrectly centered residual drifts from -16.34 to -41.82. These are diagnostic checks, not proofs or OU model counterexamples. Results are saved in independent_checks.json in this audit folder.

5. **What remains unproved, lines 21,99,123,129:** the corrected full multitype diffusion-cascade Bramson theorem, the proper derivative construction, model-specific tilt and moment estimates, control through the decoupling limits, and the decorated time-depth process are not established. The claimant consistently calls these unresolved. A verdict interpreted as a positive solution to that corrected problem would be unsupported; its explicitly stated literal negative verdict is supported.

## Independent bounded literature search

All web reads used Python urllib, with no built-in web search. I downloaded the source, Chen and Aidekon independently. The arXiv identifier API returns source v1. The query `all:"threshold cascades" AND all:"Bramson"` returns only the source. A threshold-cascades query restricted to 2026-08-21 through 2026-10-11 returns the source and arXiv:2609.27972, *A multiscale front-decoupling criterion for threshold cascades on unimodular random trees*. I downloaded and extracted the latter's 13 pages: its results concern multiscale decoupling, not a derivative-martingale Bramson theorem. The OpenAlex search `threshold cascades Bramson` returned HTTP 429. Thus no exact earlier solution was identified in this bounded search, but database coverage is incomplete and no absence-of-literature theorem is claimed.

The classical Chen paper already explicitly describes the boundary derivative martingale as signed and mean zero (p.2), and states the nontrivial-limit moment criterion (p.3). It independently supports the claimant's identification of the source's UI/nontriviality confusion. It does not settle the original multitype cascade problem.

Fetched PDFs, extracted texts, API results, fetch logs and independent numerical results are retained only in this audit directory. The decisive outcome is that the printed conjecture is false; the corrected intended theorem remains unproved in the submitted work.
