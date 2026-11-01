# Lean proof guide and exact scope

The file `EndpointCore.lean` is a partial formal companion to `paper.tex`. It is **not** a complete Lean proof of the selected probability theorem. The full requested stochastic formalization remains unfinished. No placeholder theorem for the original source question is supplied.

## The substantial measure-theory theorem

`no_integrable_dominator_of_expectation_defect` takes an actual measurable space, a measure, functions Fₙ, f, M, almost-everywhere convergence Fₙ→f, domination ‖Fₙ‖≤M, the identities ∫Fₙ=c, and the strict inequality ∫f<c. It proves ¬Integrable M. This is not a numerical surrogate. The proof invokes Mathlib's dominated-convergence theorem, obtains convergence of integrals to ∫f, obtains convergence to c from the constant integral identities, and uses uniqueness of limits to contradict the strict inequality.

The mathematical substitution in the paper is:

| Formal symbol | Paper object |
|---|---|
| F n | R_{S∧τ_{r/(n+2)}}^{-2} |
| f | R_S^{-2} |
| M | sup_{s≤S} R_s^{-2} |
| c | r^{-2} |
| hF | Measurability of the stopped continuous process |
| hbound | A stopped value is bounded by the path maximum |
| hlim | A positive continuous radial path has positive compact minimum |
| hint | Bounded optional stopping |
| hdefect | Explicit Gaussian integral and positivity of exp(−r²/(2S)) |

**The substitution and these stochastic facts have not been checked in Lean.** Displaying them in this table is a proof plan, not a certificate.

`nonintegrable_of_nonnegative_lower_bound` uses actual a.e. order and Mathlib integrability to transfer nonintegrability from a nonnegative measurable M to a larger Z. It corresponds to the pathwise maximum comparison after scaling. The scaling and process-specific identification remain prose mathematics.

## Algebraic declarations

- `gaussian_expectation_defect`: the displayed candidate Gaussian expectation is strictly below r^{-2}. It does not derive the Gaussian integral.
- `gaussian_defect_identity`: exact subtraction identity for the missing expectation.
- `critical_coercivity_identity`: the quartic drift and diffusion energy terms cancel to −v².
- `critical_coercivity_bound`: the scalar lower bound with θ'=1, M'=2.
- `critical_interpolation_indices`: β=2/3, ρ=2 lie in the required ranges and meet the critical equality.
- `reciprocal_ito_coefficients`: algebra of the drift after reciprocation, assuming u≠0. It is not Itô's theorem.
- `finite_time_hitting_bounds`: algebraic consequence of a supplied stopping identity and supplied expectation bound. The probability law is not modeled by this declaration.

## Unfinished obligations for a full source theorem

1. Construct the four-dimensional Brownian process and its filtration, then the radial process and scalar driver.
2. Prove the needed Itô, deterministic time-change, bounded continuous-time stopping and localization results in the chosen formal probability model.
3. Establish nonattainment, Gaussian reciprocal-square expectation, path measurability and all stopping-event identities.
4. Instantiate the measure-theoretic core with those actual random variables.
5. Formalize the SDE strong-solution/uniqueness statement and the same-driver countable family.
6. Formalize the variational spaces, embeddings and exact Agresti–Veraar hypothesis correspondence, or explicitly scope a first full theorem to the scalar model.
7. Formalize the tail/moment corollaries, including extended expectations and all endpoint exclusions.

The checked-out Mathlib contains Brownian-motion and martingale modules. A file-name search under its probability directory did not find the required Itô/Bessel SDE development; that bounded search is not a proof that no external Lean library supplies it.

Compiler and Mathlib provenance, immutable input snapshots, output and transitive axiom lists are recorded in the audit directory. Allowed foundational axioms are propext, Classical.choice and Quot.sound. A timeout, error, or unprinted target is not a pass. The checked source must match the supplied file byte-for-byte. A mutation control must reject a false theorem while still producing the valid target checks.

## Successful build

The final file compiled with Lean 4.33.1 on 2026-09-10. All nine declarations printed only propext, Classical.choice and Quot.sound as transitive axioms. Exact source SHA-256: `d2186cbf92b935a11d7d9a8dec30fedc16173c1389f1c41a28e5c0fdc147b6fb`. The audit directory holds the successful immutable input and receipt at `lean_runs/20260910T080047Z/`. Earlier timeout and failed-source records remain separate. This is a component-level pass, not a full source-theorem certificate.
