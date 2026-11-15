# C0130 research log

Task received 2026-11-13, approximately 05:31 Asia/Tbilisi: “Open problem C0130.”

## 2026-11-13 05:34 +04

- Read startup instructions, recalled relevant brain material, read compute state (warn, owner away), and attempted mesh hello/digest/claim/assert. Mesh database is read-only under the sandbox; no live-claim conflict was reported. Global checklist and memory writes are outside the permitted directory. Work is confined to this isolated directory; local log substitutes for unavailable shared bookkeeping.
- No subagents, publication, pushes, or external messages. Numerical processes will use nice 10 and one numerical thread, with small memory requirements.
- Located arXiv:1204.1895v2 and Zerner's 2005 paper. Survey Problem 3.12 refers to the general transient one-dimensional setting; its cited Theorem 18 already solves a two-cookie special case. This does not resolve the general problem.
- Literature search started with exact problem number, return probability, escape probability, and never-return formulations. Sources and search coverage will be recorded below.

## Literature checkpoint

- Downloaded survey v2, Zerner 2005, Basdevant–Singh speed paper, Kosygina–Zerner 2008 and excursions paper, Kosygina–Mountford 2011, Peterson monotonicity, Dolgopyat–Kosygina critical excursions, periodic cookies, Pinsky, and Madden et al. 2019.
- Corrected a source identification error immediately: arXiv:1311.7437 concerns Lorentz mirrors; periodic cookies is arXiv:1311.7439. The unrelated download is retained under an explicit unrelated filename.
- Survey Theorem 3.10 has two settings: stationary ergodic nonnegative stacks (possibly unbounded), with a deterministic-arrow exception excluded, or IID bounded stacks with weak ellipticity. Problem 3.12 follows both. The probability is annealed.
- Zerner 2005 Theorem 18 computes the two-cookie case, already cited by the problem. Basdevant–Singh Lemma 3.4 gives the stationary PGF equation; Remark 3.8 recovers that special case. Madden et al. 2019 still leaves the stationary masses unknown. Peterson proves strict monotonicity, not an escape formula. Excursion papers compute decay exponents and leave distribution-dependent constants.
- Exact-phrase and author searches through 2026 found no general formula resolving Problem 3.12. This is a bounded literature search, not a proof of absence.
- Process priority is inherited as nice 15 (verified by getpriority). Attempting nice 10 prints a permission error because increasing priority from 15 to 10 is disallowed; computations will keep the more considerate inherited priority 15.

## Derivation checkpoint

- For IID stacks transient to the right, backward chain Z'=F_(Z+1) has stationary law pi, and escape = E[p_1] pi(0). Also pi(0) = 1/E_0[tau_0^+]. Forward survival supplies an independent fixed point.
- Investigating a numerical certificate based on the backward chain's exact constant drift 1-delta above M-2: solve the mean hitting-time equation below cutoff K and use an affine function i/(delta-1)+c above K. Tail residuals are 2^(-i) times explicit polynomials, so signs can be certified by expansion in nonnegative binomial polynomials. This is exploratory until implemented and checked.

## Numerical and proof checkpoint

- Implemented the affine-tail Poisson certificate and proved its residual signs for the entire unbounded state space using Vandermonde expansion. Justified optional stopping by an r-moment Lyapunov function for 1<r<min(delta,2), avoiding the false assumption that the stationary mean is finite when delta<=2.
- Exact rational enclosures now saved for two-cookie controls; three identical cookies at p=0.7,0.75,0.8,0.85,0.9,0.93,0.97,0.99,23/30; and four at p=0.75. Some intervals agree to 14–18 decimal places. Additional K=128 three-cookie p=0.8 certificate is running.
- Verified the backward finite-generation expression against a separately constructed finite-interval Markov chain of the actual position and consumed-cookie counts. Five cases agreed far inside their explicit population-cutoff error bounds (roughly 60–80 decimal places). These finite-volume checks verify the identity, not the infinite-volume limit by themselves.
- Independent forward-process Monte Carlo: 100,000 trials each, M=3,p=.8 to generation 16,384; M=3,p=.9 and M=4,p=.75 to generation 4,096. Results agree with the escape certificates at sampling precision. Finite-generation bias is explicitly retained in interpretation.
- Verified 156 kernel entries by independent coefficient extraction, including a signed-cookie stack, plus exact drift and two-cookie controls.
- Ruled out all rational functions A(p)/B(p) with deg(A),deg(B)<=3 as a three-identical-cookie formula: exact rational interval data force the interpolation matrices to be nonsingular. The inverse residual upper norm is <2.55e-7 in the degree-three case.
- Implementation corrections: SymPy DomainMatrix denominator conversion fixed; residual sums changed to integer common-denominator arithmetic for speed; Python's integer-string digit limit raised locally to store the large rational endpoints. One K=128 run was interrupted before optimization; another completed calculation but failed to serialize before the digit-limit fix. No partial output from either is used as evidence.
- Another guessed source ID was caught by title inspection: 1201.0063 is an unrelated Hankel-operator paper; retained under an unrelated filename and replaced by verified 1201.0379. All bibliography source IDs have now been checked against downloaded titles. Source manifest records URL, size, and SHA256.

## 2026-11-13 06:02 +04 — finished

- REPORT.md first line is PARTIAL. General Problem 3.12 is not claimed solved, and the literature conclusion is limited to the documented search. The two-cookie result is correctly attributed to Zerner 2005, Theorem 18.
- Stronger exact M=3,p=4/5,K=128 result: 0.556165463398440124244 <= escape <= 0.556165463398440124318. Underlying rational interval width <7.279e-20; it is contained in the independently recomputed K=64 and K=96 enclosures.
- All final audits passed: 156 independently extracted kernel coefficients, exact drift and two-cookie controls, nested rational bounds, five actual-walk finite-volume checks, three independent forward Monte Carlo runs, and rational-function exclusions of degrees 1/1, 2/2, 3/3. The inverse-residual exclusions were rechecked using only Python Fraction arithmetic from stored certificate matrices.
- Rechecked 25 report file links, all 19 source PDF hashes (17 relevant plus two explicitly unrelated retained downloads), and every decimal table endpoint. Saved code/data/sources occupy about 9.4 MB. Largest recorded exact-process peak RSS: 83,787,776 bytes. All numerical processes finished; no workers remain from this task.
- Report includes explicit near-critical linear bounds, the M=3 critical ratio bounds 3/5 and 9/7, coordinatewise monotonicity, the fixed-p/M-to-infinity limit 2p-1, and exact delta-only counterexamples. Monte Carlo precision and finite-generation bias are distinguished from exact rational certification.
- No publication, push, subagent, or write outside this research directory. Shared checklist/mesh/brain updates remain unavailable under the sandbox; durable findings are preserved in this report and log.

Task: “Open problem C0130” — received 13 November 2026, approximately 05:31 Asia/Tbilisi.
