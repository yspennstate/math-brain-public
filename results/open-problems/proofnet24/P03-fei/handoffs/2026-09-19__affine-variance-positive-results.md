# FEI positive continuation: sharp variance accumulation and affine-stable FEI class

19 September 2026. **Full FEI remains OPEN.** These are positive auxiliary/class results with on-page proofs and exact self-checks. No independent review, Lean verification, publication priority, or source closure is claimed.

## Read and reproduce

- [Complete proof report](../continuations/2026-09-19-affine-variance/REPORT.md).
- [Current checker](../continuations/2026-09-19-affine-variance/verify_affine_variance.py), using the attributed unchanged [entropy dependency](../continuations/2026-09-19-affine-variance/prior_exact_entropy.py).
- [Executed results](../continuations/2026-09-19-affine-variance/verification.json).

Run `python verify_affine_variance.py --part all --output verification.json` inside that folder. The recorded tests use exact integer/Fraction comparisons and outward rational logarithm intervals. Rerunning the same program is not an independent audit.

## New mathematical delta

1. For every Boolean f, V(f)=sum_k 2^(-k) E Var(f_k)<=2I(f), where f_k is the existing random multiplicative-derivative chain. The constant two is optimal on a one-point defect family. The proof uses an autocorrelation moment recursion, an explicit scalar supersolution, and cube edge isoperimetry.
2. Define M(f) as the minimum over linear bases of sum_v min(alpha_f(v),1-alpha_f(v)). It is exactly minimum ordinary influence over invertible input changes and output characters. It tensorizes exactly under disjoint products and is invariant under surjective affine lifts. The proof is a minimum-weight binary-basis rank integral.
3. For monotone f, M(f)=I(f)-max_i I_i(f)+min(max_i I_i(f),1-alpha_f(all-ones)). In the self-dual case, M=I-max_i I_i. This is not FEI for every monotone function.
4. Let G be a disjoint product of one-point clauses, quadratic phases, and arbitrary-shape read-once ternary-majority formulas. For any surjective binary linear map L, affine shift b, and output character chi, F(x)=chi(x)G(Lx+b) satisfies H(F)<=4M(F)<=4J(F)<=4I(F). Constant four is optimal over this class. From the elementary prior T<=2H, its full allocation chain satisfies T(F)<=8M(F). No closure of the class under derivatives is assumed.
5. The affine-invariant corrected variance V_*(f)=1-max_s fhat(s)^2+sum_{k>=1}2^(-k)E Var(f_k) satisfies V_*<=2M<=2J universally. The uncorrected V cannot be bounded by J on characters.
6. The exact joint spectrum of two samples from one random derivative includes a nonzero positive-semidefinite shared-shift covariance correction. A blanket independence substitution is false. Allocation entropy is also not concave on arbitrary laws; the report gives an exact rational two-bit example, not a Boolean-spectrum counterexample.

## What these results do not prove

The full accumulated allocation bound T<=C J is still unproved. A nondegenerate quadratic phase has H=n and T=n/2 but V_*=(3/2)(1-2^(-n)); therefore variance alone is insufficient. The affine-mixing theorem requires that all parameter forms are jointly independent (surjectivity). Dependent identifications of clause/gate inputs are not covered.

Do not revive either disproved pointwise resolvent proposal, drop the full-rank condition, or claim that the new constant four applies to all Boolean functions. The standard seed entropy formulas and bounded-arity composition literature are credited. Novelty of the combined affine and variance results remains unverified.

## Actual evidence and reading coverage

The exact current checker verifies 278 truth tables through dimension three plus fixed-seed higher-dimensional examples, 4,803 memoized variance-chain states, all 197 monotone functions through four variables, 400 larger monotone samples, 581 independent basis-enumeration comparisons, 316 tensor pairs, 50 surjective mixed examples, 32 full allocation-chain examples, and 16,658 exact shared-shift pair-law identities. The proofs, rather than these finite tests, supply the all-dimensional assertions.

Consumed source index: `proofnet24/P03-fei/README.md`, blob `8d45ee758aca61c7866e4e40432b324c133d28ad`. The current balanced-substitution report and its unchanged entropy checker were read. Also read in full: the erasure reduction, blob `770f1fc8438b360549ed89480cb260768d839923`, and the signed-balance/fixed-basis barrier, blob `6d886a56ad52de684f635cc124fb56110f67b8b2`. This is not a claim to have re-audited all 1,506 archive pages.

The creator session could not push this continuation: its complete GitHub discovery exposed read actions only, and terminal Git failed to resolve github.com. The delivered conversation package includes an apply-ready patch. If this file is now visible remotely, record the actual commit that applied it; do not invent a historical creation SHA from the local package.

## Continuation priority

Try to extend the explicit affine-stable class to genuinely dependent parameter forms with controlled signed interference, or bound the remaining allocation chain by a resource that includes both structural rank and the paid variance. A proof for a specified new class is substantive; an unproved rearrangement of T<=CJ is not closure. Preserve the exact known counterexamples and the independent hypotheses of every reused result.

No source ownership, native P03 metric, peer report, schedule, access control, or repository visibility is changed by this handoff. Repository visibility alone would not prove that a scheduled worker has consumed the report.
