VERDICT: PASS (correct and complete)

# Independent audit of G0014

Audit date: 2026-10-11. This verdict accepts the claimant's explicitly stated **refutation of the literal conjecture**, not a proof of a corrected Bramson theorem. The latter remains unresolved in this submission. No mathematical failure requiring a repair was found in the refutation or its explicitly conditional auxiliary results.

## What is claimed, and whether it answers the question

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's directory without changing them. ATTEMPT.md lines 11–21 and 127–129 claim that the source's simultaneous uniform-integrability/positive-limit assertions are incompatible for its asserted mean-zero signed martingale, and independently that its printed speed makes the claimed front expansion impossible. STATUS.md expressly defines SOLVED as “refuted AS POSED.” It does not claim the intended corrected theorem or its multitype extremal-process limit.

The source's actual Conjecture 3.2 asserts, under Theorem 2.1's hypotheses, that the untruncated signed derivative martingale is uniformly integrable, equivalently has a limit positive almost surely on survival, and that

    F(t) = c_* t - [3/(2 theta_* c_*)] log t + O_P(1),

with the stated randomly shifted Gumbel/decorated-process conclusion. Theorem 2.1 assumes R1, kappa<1, rho(M)>1, irreducibility, and a common positive exponential-moment parameter for all activation type pairs. Part I uses a finite matrix. Definition 1.2 defines c_* as the reciprocal of inf_{theta>0} log rho(B(theta))/theta, without a minus sign. Section 3.1 defines the displayed signed derivative sequence with initial value zero. These are exactly the assertions the submission challenges. Refuting the literal conjunction answers the problem as supplied; it need not prove or disprove a different conjecture with corrected definitions.

I independently downloaded https://arxiv.org/pdf/2608.21125. It returned HTTP 200; SHA256 was 64484fb650e510843769fb34ef14d51c0ec0b694a753880be8a4f2bd70ce3b47, matching the claimant's record. The PDF has nine pages and names Achyut Kumar and Abhinav Duddala, rather than the intake's Dudeja. Relevant statements are on PDF pages 2–5. This is a source transcription check, not an endorsement of its purported first-order theorem.

## Proof checks and issues of interpretation

### 1. Proposition A: correct incompatibility, with an essential stated qualification

Location: ATTEMPT.md lines 25–41; also lines 115–116 and CLAIMS.jsonl's first entry.

I re-derived the full argument. For an integrable martingale with D_0=0, E D_n=0. Uniform integrability plus almost-sure convergence implies convergence in L1. The submission proves this implication rather than merely citing it: its Fatou inequality at line 29 is valid because |D|>2K implies eventually |D_n|>K; clipped variables converge by bounded convergence; the two tail errors each contribute at most epsilon. Thus E D=0. A globally nonnegative integrable D with P(D>0)>0 cannot have expectation zero: some event {D>=1/k} must have positive probability. Every inequality in this argument is valid. It does not require D_n itself to be nonnegative.

The application is correct for the source's asserted martingale: the root has T_root=0, hence the displayed D_0=0; on extinction the locally finite genealogy eventually has empty generations, hence terminal limit zero; supercritical irreducible finite-type GW survival has positive probability. Positivity on survival consequently makes the terminal limit globally nonnegative and nontrivial.

Qualification, already acknowledged at lines 39–41: this is not an independent proof that the source's multitype formula actually is a martingale. If that formula is incorrectly normalized, zero initial value alone does not force zero later means. I therefore accept Proposition A as an incompatibility of the source's asserted martingale/UI/positivity package, not as a stand-alone proof about an arbitrary nonmartingale sequence. The independent speed obstruction below prevents this qualification from becoming a gap in the literal refutation. A truncated nonnegative martingale is a different object; replacing the displayed sequence by it changes the question.

### 2. Proposition B: correct general obstruction to the printed front formula

Location: ATTEMPT.md lines 45–64; CLAIMS.jsonl's second entry.

I independently obtained the same bounds. For a_max=max E A_{ij}, Jensen gives B(theta)>=exp(-theta a_max)M entrywise. Perron monotonicity then gives

    log rho(B(theta))/theta >= log rho(M)/theta - a_max >= -a_max.

Strictly positive activation times imply E exp(-theta A_{ij})->0 by dominated convergence. There are finitely many entries, so the row-sum norm and then rho(B(theta)) tend to zero. B retains M's irreducible support at each finite theta, so its Perron root is positive. Some finite theta has rho(B(theta))<1. Therefore the infimum I is finite and strictly negative, and c_*=1/I<0. Finite positive exponential moments imply the finite means used here.

A nonnegative front depth cannot equal c_*t+O(log t)+O_P(1) with c_*<0: its residual after the stated centering is bounded below by -c_*t+O(log t), which tends to infinity. This refutes the requested expansion throughout the stated finite-type positive-activation representation, without requiring a finite optimizer or a multitype martingale proof.

Source qualification: Section 1.2 first writes A_e>=0 and then describes the weights as positive. The strictly positive reading used by the submission is also the continuous passage-time reading for a child starting below threshold. Lines 57 and 119 explicitly exclude zero-time atoms. This exclusion must remain visible: if zero-time atoms are admitted as an enlarged abstract model, the dominated-convergence conclusion becomes B(theta)->M_{ij}P(A_{ij}=0), and the strict-negative conclusion need not follow. This is a stated scope limit, not a hidden extension of the proof. Likewise, no infinite-type statement is proved.

### 3. Proposition C: correct conditional inversion and coefficient

Location: ATTEMPT.md lines 68–82; CLAIMS.jsonl's third entry.

For n_±=h(t)±K+e_± and h(t)=t/a-(b/a)log t, I obtained

    a n_± + b log n_± - t = ±aK + a e_± - b log a + o(1).

The rounded indices are deterministic. Marginal tightness uniformly for all sufficiently large deterministic generations is therefore enough; no independence, random-index substitution, or joint uniform coupling is needed. Monotonicity and divergence of T_n justify both event identities in line 80. The two exceptional events have total probability at most 2epsilon, proving tightness of the inverse residual.

With b=3/(2theta_*) and c=1/a, the inverse coefficient is 3c/(2theta_*), as claimed. This is explicitly conditional on the generation-time estimate; it is not evidence that the estimate holds for the original cascade.

### 4. Bounded-offspring single-type result: valid invocation, not the original theorem

Location: ATTEMPT.md lines 86–99; CLAIMS.jsonl's fourth entry.

I fetched and read Chen, arXiv:1402.5864, PDF pages 1–3, and Aidekon, arXiv:1101.1810v6, PDF pages 1–3. Chen explicitly calls D_n a signed mean-zero martingale and states a necessary and sufficient condition for a nontrivial limit, not uniform integrability of that untruncated sequence. Its condition is E[Z log_+Z+Y(log_+Y)^2]<infinity. Aidekon requires boundary normalization, nonlattice displacements, tilted second moments and the same logarithmic moments, and gives the generation-indexed minimum's mixed-Gumbel limit.

For V=theta A+f(theta), direct differentiation gives E sum e^{-V}=1 and E sum V e^{-V}=f(theta)-theta f'(theta)=0. The submission assumes a finite boundary tilt, positive tilted variance and nonlattice law. V>=ell=f(theta), N<=K, and the bounds Y<=K exp(-ell), Z<=K/e and sum V^2e^{-V}<=K sup_{v>=ell}v^2e^{-v} establish every remaining moment requirement. The last supremum is finite since ell is finite and v^2e^{-v}->0 at +infinity.

Subtracting the extinction contribution from Aidekon's limiting tail and conditioning on survival gives a proper conditional limit because D_infinity is positive there. The nonexplosion estimate is also valid: 1_{T_v<=j}<=exp(sj)exp(-sT_v), and the branching expectation gives the stated summable geometric bound once m E exp(-sA)<1. Borel–Cantelli and nonnegative path increments establish the conditions needed by Proposition C. The resulting tight front expansion is proved for this single-type special case only. No multitype or time-indexed decorated-process conclusion is established or claimed.

### 5. Proposition D: correct lattice obstruction, with the stated scope

Location: ATTEMPT.md lines 103–111; CLAIMS.jsonl's fifth entry.

For integer F(t), exp(2pi i[F(t)-h(t)])=exp(-2pi i h(t)) identically. A continuous eventually increasing unbounded h(t)=ct-d log t, c>0, hits integer and half-integer phases along sequences tending to infinity. The bounded continuous test function cos(2pi x) then has expectations 1 and -1. Thus no ordinary all-real-time weak limit on R exists. This does not rule out tightness, lattice subsequences, or differently formulated point-process statements. The submission correctly keeps that distinction.

### 6. Ancillary source defects and formal-check limits

Location: ATTEMPT.md lines 117–123.

For a row-parent matrix, conditional offspring weighting is B h, hence a right Perron eigenvector is required. I checked this exactly using M=[[2,1],[2,1]], rho=3 and left vector phi=(2,1): phi^T M=(6,3)=3phi^T but Mphi=(5,5), not (6,3). A theta-dependent eigenfunction also requires derivative terms. This confirms the source defect mentioned at line 117; this matrix is an algebraic diagnostic, not a constructed OU cascade counterexample.

The finite-optimizer warning at line 118 is correct: deterministic A=1 gives f(theta)/theta=(log m)/theta-1, with infimum -1 attained only at infinity. As the submission says, this does not establish deterministic activation for an elliptic OU cascade.

I inspected obstruction.lean and lean_check.txt read-only. They contain the terminal nonnegative-zero-integral lemma and elementary coefficient/sign identities, with a recorded successful invocation. There is no added axiom, sorry or native_decide in that file. I did not rerun Lean or independently certify its environment. These small formal checks do not formalize the stochastic convergence, spectral-radius argument, or cascade reduction, and neither my verdict nor the submission's proof requires them.

## Independent exact and numerical checks

I wrote and ran independent_checks.py in this audit directory; its assertions passed, with results in independent_checks.json. For binary Exp(1) activation, f(theta)=log(2/(1+theta)) and f'(theta)=-1/(1+theta). Independently solving f=theta f' gave theta=3.3110704070010044, a=0.23196095298653446, c=4.311070407001004, printed c=-4.311070407001004, corrected logarithmic coefficient 1.9530257033581542 and sign-only-repaired printed coefficient 0.10508427387835252. These agree with ATTEMPT.md line 122 and CLAIMS.jsonl's numerical entry.

An exact rational Exp(1) first-generation calculation at theta=3 gave E D_1=0. The left/right matrix check above used rational arithmetic. Direct binary-search inversion of deterministic T_n=a n+b log n for t=10^3,10^4,10^5,10^6 gave residuals about -3.58,-3.72,-3.56,-3.42 with the correct coefficient, while the wrong-coefficient residuals moved from -16.34 to -28.96. I also checked the positive-part moment bound numerically; its proof follows by differentiating ve^{-v}, whose maximum on v>=0 is 1/e. Numerical tests supplement the exact arguments and do not establish model matching.

## Fresh bounded literature search

Using Python urllib only, I queried the arXiv API for “threshold cascades” AND “Bramson”, and for threshold-cascade submissions dated 2026-08-21 through 2026-10-11. The first returned only the source; the second also returned arXiv:2609.27972v1, *A multiscale front-decoupling criterion for threshold cascades on unimodular random trees*. I downloaded that PDF and inspected its theorem statements and keyword occurrences. Its Theorem 3.1 concerns finite-scale contraction/front decoupling and Theorem 4.6 an initial-scale estimate. It supplies no derivative-martingale or Bramson/extremal-limit theorem settling Conjecture 3.2. “Derivative” occurrences concern the coupling derivative; the Bramson occurrence is in the cited source's title.

The OpenAlex query “threshold cascades Bramson” returned HTTP 429. Search URLs, response statuses and PDF hashes are recorded in source_checks.json; API responses and extracted PDFs are retained here. This search identified no exact affirmative solution, but incomplete database coverage cannot establish that none exists. The known Chen/Aidekon results support the incompatibility and the conditional single-type result; they do not prove the requested corrected multitype cascade theorem.

## Accepted conclusion

The literal conjecture is refuted: a genuine mean-zero signed martingale cannot have both the asserted UI and positive nonnegative survival limit, and independently the source's printed speed contradicts its nonnegative front in the positive finite-type activation setting. The auxiliary results are correct within their stated hypotheses. No special case has been passed off as the full theorem.

The corrected multitype derivative-martingale, Bramson-delay and properly qualified extremal-process problem is not proved here. PASS applies only to the submission's clearly delimited negative answer to the exact statement supplied.
