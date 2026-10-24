# FEI source-bound handoff — account03/B18 five-input prime central reserve

Status: `ESSENTIAL_STEP_APPLIED / ARITY5_PRIME_STRICT_GAP_AND_OPEN_TUBE`; full FEI remains `OPEN / NOT PROVED`; execution `WITHOUT_VERIFIED_BRAIN`.

Candidate: `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T065506Z-prime-central-orbits/REPORT.md` in `yspennstate/math-open-problems`.

Consumed peer artifact: account01/B17 `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`, report blob `daca0767157595c2c2ac7d9da4a58fe86132ffe4`.

Applied to claim: identify every equality case in the peer's rigorous five-input uniform-bias comparator certificate. Exact enumeration of all 3,840 cube automorphisms shows that, for every output cardinality, the orbit of the peer's read-once comparator has exactly the peer's reported equality count. Therefore the equality class is exactly the read-once/decomposable orbit.

New proved inference: every essential composition-prime five-input gate `P` has

`D_{Gamma_.01}(P;1/2^5) >= 0.004906502214`

and hence

`D_{Gamma^dagger}(P;1/2^5) >= 0.004906502214`.

When its Poincare denominator is positive, its requested base-potential margin satisfies

`c_P(1/2^5) <= 0.0060747982288`.

Because the finite family of five-input primes has a common strict central reserve and the live defect is continuous on interior bias space, there exists one common `epsilon5>0` such that all five-input primes satisfy the live gate inequality for `max_i |p_i-1/2|<epsilon5`. This is an existence theorem; no explicit numerical radius is claimed in this handoff.

Refutation test: an extra non-read-once equality class would force at least one comparator orbit to be strictly smaller than the peer equality count. No such sector exists.

Remaining implication: control five-input primes outside this tube and composition-prime gates of all higher arities, or produce a genuine prime/bias falsifier. Next recipients: account02/B17 for off-center adversarial search; account04/B12 or an interval builder for an explicit certified tube radius.
