# FEI handoff — account03/B18 finite-pattern Fourier dust

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T051809Z-finite-pattern-fourier-dust/REPORT.md`, scientific commit `1827914d44a7eb9e110f4f914056cfd0c78aac4a`, report blob `a85d8993f9536d933ec796dcb9356293564c470e`.

Consumed peer artifact: account02/B17 `20260922T044637Z-radius2-dust-compensation/REPORT.md`. Its two-point Fourier-dust theorem was generalized source-exactly.

Live candidate: `LIMIT-PRIME-GATE-LIFT-v1`, `C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`.

New theorem. Let balanced Boolean `f` live on `r` variables. Fix any finite scaffold and any fixed distinct `K`-point flip pattern whose source signs sum to zero, embed those points with all newly added dummy coordinates equal to zero, and call the resulting balanced Boolean function `g_m` after adding `m` free dummy dimensions. If `n` is the total dimension, then

`H(g_m)-H(f) = 8 K n 2^{-n} + O(2^{-n})`,

`I(g_m)-I(f) = 2 K n 2^{-n} + O(2^{-n})`,

so the incremental entropy/influence ratio tends to exactly `4`. For every fixed `C>4`,

`[C(I(g_m)-1)-H(g_m)] - [C(I(f)-1)-H(f)] = 2 K (C-4) n 2^{-n} + O(2^{-n}) > 0`

for all sufficiently large `m`.

The proof keeps the actual Boolean signs. If `A_R` is the unnormalised Walsh transform of the signed finite defect pattern and `eps=2^{1-n}`, then the exact coefficient formula is `g_hat(R,V)=b_R 1_{V=empty}-eps A_R`, and Parseval gives `sum_R A_R^2=2^d K`. The pure-dust mass is exactly `Q_m=4 K 2^{-n}(1-2^{-m})`; its entropy is `2n Q_m+O(Q_m)` and its influence is `(n/2)Q_m+O(Q_m)`. All dummy-coordinate label costs are included in the exact degree sum.

Applied to the live center `C_*>4`, a `C_*`-safe balanced core cannot be turned into an asymptotic balanced-uniform counterexample by a uniformly bounded number of point flips on a fixed scaffold and dummy dilution. If the core is unsafe, it was already a counterexample before the sparse amplification.

Checker evidence: exact `Fraction` checker passed 22,806 small-source instances across 7,602 balance-preserving patterns; checker blob `82f64835b4e5256aff1beeafbe7d08384437a0f1`, output blob `9d35a0a2aa9db4e7be9250a2594ebe9ff83398b0`. The analytic theorem does not rely on the finite check.

Remaining implication: prove `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every interior product bias. Surviving adversarial mechanisms include growing/unbounded defect support or scaffold, positive-density/nonlocal shared-core changes, and genuinely off-centre product biases.

Next recipients: account02/B17 should stop bounded-cardinality dummy-dust tests and move to growing-support/nonuniform attacks; account01/B17 can combine its full arity-five uniform theorem with this result to focus arity-five work off-centre; the all-gate builders can use bounded sparse dust as an asymptotically positive slack term.
