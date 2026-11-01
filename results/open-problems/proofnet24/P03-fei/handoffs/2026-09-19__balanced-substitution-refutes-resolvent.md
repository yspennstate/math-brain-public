# FEI correction: the full pivotal-resolvent pointwise target is false

19 September 2026. **Full FEI remains OPEN.** This is an owner-requested mathematical continuation, not independent review, an automated-run receipt, or a source-level resolution.

## Read first

- [Complete analytic proofs](../continuations/2026-09-19-balanced-substitution/REPORT.md).
- [Executed rational checker](../continuations/2026-09-19-balanced-substitution/verify_next_step.py).
- [Actual recorded output](../continuations/2026-09-19-balanced-substitution/verification.json).

Run `python verify_next_step.py --part all --output verification.json` in that folder. All acceptance comparisons use integers/Fractions or rational enclosures of prime logarithms. These checks are not Lean or independent audits.

## Urgent correction to the previous next step

The coded-budget report left `D_cross <= K(C+Q_log)` open and recorded its sufficient implication to FEI. **The new report disproves this pointwise estimate for EVERY finite K**, even on balanced monotone functions invariant under a transitive coordinate-permutation group.

The explicit family is F_m=Maj_m(g_d,...,g_d), with disjoint inner blocks, g_d recursive ternary majority, odd m=2r+1, and d=ceil(log_2 m). It has

    C(F_m) -> 4,
    Q_log(F_m) -> 0,
    D_cross(F_m) >= H_r^harm/18 + 1/36 -> infinity,
    H(F_m)/I(F_m) -> 4.

Thus this is NOT an FEI counterexample. Increasing K, assuming monotonicity, or replacing the logarithm by any fixed finite power does not repair the failed bound. The earlier scalar obstruction and the discounted C/Q bounds remain intact; the new result does not contradict their precise statements.

The key identity is C(f)=4[Var(f)-sum_i I_i(f)^2] for monotone f. The local budget stays bounded while outer spectral allocation information survives low-influence substitution.

## Positive results to build on

For independent spectral samples S,T, define A(f)=H(S | S triangle T, S intersection T), called allocation entropy in this report. For balanced disjoint substitution F=h(g_1,...,g_m), the report proves exact conditional-entropy identities with a nonnegative outer-overlap correction. When all inner functions are odd/self-dual, that correction vanishes and

    A(F)=A(h)+sum_i I_i(h)^2 A(g_i).

For a common balanced monotone inner g, another exact identity is

    C(h(g,...,g))+4 sum_leaf I_leaf^2 = C(h)+4 sum_i I_i(h)^2.

A genuine positive infinite-class result: every read-once ternary-majority formula, including unequal depths, satisfies A=(3/4)C and hence

    D_cross <= (3/2)C + (4+2/ln2)Q_log.

This is a pointwise subclass theorem. Its multiplicative derivatives need not remain in that subclass. Known FEI results for bounded-arity formulas are not claimed as new.

For EVERY Boolean function, the report establishes

    A <= D_cross <= 2A+(4+2/ln2)Q_log.

For the multiplicative derivative chain, let T(f)=sum_k 2^(-k) E A(f_k). The existing Q-payment yields

    T/2 <= H(f) <= T+(5+5/(2ln2))J(f).

No uniform bound on T/J is proved. That accumulated allocation target is genuinely global and equivalent to existence of a universal FEI constant. It is not a newly solved inequality merely because it has a name. The correctly quantified hereditary erasure target remains another option.

## Consumed updates, actual checks, and delivery

Read source: `continuations/2026-09-19-coded-budget/REPORT.md`, blob `6bd3cef08192616a27053f01edb94863e7ad3720`, especially definitions and Sections 7.1, 7.4, 8. Read current FEI index blob `82e045faae2753a2bf3cac12ee51c4c3a74abcab`. The earlier majority level formula and Walsh uncertainty argument are reused, with attribution. O'Donnell–Tan composition work and the Maassen–Uffink uncertainty theorem were checked as primary-source background.

Executed checks: 1,850 entropy comparisons across 370 canonical functions; all 278 truth tables through dimension three; all 168 monotone functions on four inputs; 128 exact common-inner substitution examples; ten exact allocation/XOR composition examples; unequal ternary trees; non-odd balanced monotone inner gates; an actual positive overlap-correction example; exact majority spectral weights through eleven inputs; rational lower bounds through 1,025 outer inputs. The finite symbolic large witness is justified analytically; its enormous truth table was NOT enumerated.

Report commit: `08bfe593673d482f30b34b951ee4b463b268c361`, blob `dc9daa94dc791a075ff2f9569d9c7e2fb0547179`.
Checker commit: `0f19d92b297dcf58221d5cefdd4d1757a3e3016a`, blob `e867ba6b12e1a3e7588fd812eba6841319cd97b9`.
Output commit: `85224eddfe6cf89c9332e11b9cc2d428bce8d3ab`.
The report and checker were read back and their Git blob hashes match the local files. Script SHA256: `9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab`.

## Next worker action

First reconstruct Theorem 1 before relying on it. Then stop treating the pointwise full-resolvent estimate as an open proof target. Preserve this counterfamily as an adversarial test for any new local budget. Pursue an accumulated allocation estimate, a full-scope hereditary erasure bound, or another global signed Fourier method. Do not label a reformulation or an unchanged certificate as movement toward full closure.

No schedule, source ownership, native finite-dimension metric, peer report, access control, or repository visibility is changed. The task's current-master retrieval is how this correction is delivered; this file does not assert that a scheduled run has already consumed it.
