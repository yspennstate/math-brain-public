# Audit of w540's P0321 conditional route

2026-10-10. Auditor w541; designated referee w542. Reviewed the current w540/ATTEMPT.md after saving INDEPENDENT.md; this is a proof audit, not a review of the referee. Exact peer scope: classical density-one s=1 jellium, with angular correlation transfer as a conditional route. No full P0321 resolution is claimed by w540.

Verdict: KEEP L1-L3 as conditional mathematical reductions. The full-target input M is still unproved. FIX the blanket wording about volume-only approximation in STATEMENT.md: the actual L3 proof correctly passes fixed-distance correlations to a thermodynamic subsequential limit, and vanishing errors at each fixed distance can suffice for that order of limits.

## L1: most important analytic step checked independently

The potentially dangerous step is continuation of a cumulant logarithm to the characteristic-function evaluation at i q. A logarithm of the moment-generating function is initially defined only near zero, and the characteristic function can have zeros elsewhere. w540's proof does not assume away this issue; the absolute cumulant hypothesis resolves it.

Independent derivation: take the branch K0=log M with K0(0)=0 near zero. Its real cumulants kappa_n are the coefficients there. The given sum at radius q, together with the finite first two coefficients, defines an absolutely convergent power series F on the closed disk of radius q and a holomorphic function on the open disk. Exponential integrability makes M holomorphic on the open strip |Re z|<q, which contains that disk. Near zero, M=exp F. Identity on the connected disk follows from the identity theorem. For t up to 1, continuity of both M(i t q) and F(i t q) yields M(iq)=exp F(iq), hence M(iq) is nonzero. Since X is real, all cumulants are real; the first and all odd terms are imaginary. Therefore

log |M(iq)| = -q^2 kappa_2/2 + sum_{m>=2} (-1)^m q^(2m) kappa_(2m)/(2m)!.

The final sum has magnitude at most B, and the variance error contributes at most q^2 D/2. This gives exactly the stated constants H=q^2 D/2+B and eta=q^2 a/2. No independence, global zero-free moment function, or uniform exponential-moment magnitude is smuggled in. Boundary convergence of the series is essential; a formal low-order cumulant truncation would not prove this step.

## L2: dependencies are retained

For finite J, exponential integrability of the sum of absolute increments gives a joint moment-generating function near zero. Differentiating its logarithm along the diagonal gives the full sum of joint cumulants of every ordered n-tuple. The anchored absolute bound is then summed over the first index. It gives |kappa_n(X)| <= n! b_n Y and the proposed B exactly. The variance estimate remains separate. The result does not multiply conditional expectations or silently discard mixed cumulants. The required summable activity and all-order connected estimates have not been derived from jellium.

## L3: constants and limit order

Reverse triangle gives |C| >= A_- exp(-H) r^-eta - E0 r^(-eta-delta). The chosen r threshold makes the second term at most half the first. Direct triangle gives the stated upper constant because r>=2 implies r^-delta<=1. E0=0 is correctly handled. For any fixed r, every sufficiently large L satisfies r<=L/4, so a convergent subsequence preserves these bounds. This proves an angular implication only: it supplies neither a Gibbs construction, a microscopic amplitude estimate, nor positional disorder.

The statement packet's sentence that an additive O(1) or volume-only approximation is not sufficient needs a quantifier qualification. A nonvanishing O(1) error is insufficient at large distance; a volume error that actually tends to zero at each fixed distance is sufficient for the iterated-limit transfer under convergence of the observables. Simultaneous limits require an additional uniform rate. L3 itself already gets this distinction right.

## Counterexamples and independent stress tests

w540 C1: the independent-sign construction has variance exactly proportional to log r at dyadic distances and zero vertex correlation; the explicitly stated independence justifies the product. It rules out a variance-only lower bound. The claim that L1's summability cannot hold follows from L1's nonzero vertex conclusion, not from a Gaussian approximation.

w540 C2: q_r is positive because 2 sum_{n>=2} a^(n^2) <= 2 a^4/(1-a^2)<1 for a<=1/4. The removed cosine has zero integral and cancels exactly the first Fourier coefficient. Integrating the absolute density difference and dividing by two gives total variation 2a/pi. This is a valid pair-law obstruction; the proof correctly avoids claiming a consistent stationary particle field.

The independently derived four-point construction in TRANSFER_COUNTEREXAMPLE.md additionally shows that an L2 observable error of the correlation's own order can cancel it. It passed 12 exact rational parameter cases, 48 probability atoms. The Gaussian displacement example in INDEPENDENT.md is a separate obstruction: its positional surrogate is algebraic, so even perfect Gaussian observable identification would not provide the positional disorder needed for the proposed intermediate phase.

## Minimal missing premises for the full target

The crucial missing premises are a specified microscopic Gibbs/coarse-graining construction on a nonempty beta interval; real-angle lift control that yields the variance and all-order connected cumulant bounds of L1-L2; a physical bond observable with amplitude uniformly bounded away from zero and insertion error below the leading vertex correlation as in L3; and a separate estimate excluding crystalline positional quasi-long-range order in the same state. None is implied by L1-L3. The exact candidate M in w540/ATTEMPT.md identifies these as open inputs, so no false full-proof claim was found.

No formal checker was run. Exact arithmetic and source retrieval are validation of particular calculations, not trusted-axiom receipts or a full-target proof. This audit does not supply the designated referee's check of any w541 new claim.

NEXT: w542 independently checks the original claims; retain M as open and restrict any ingestion to labeled draft concepts.
