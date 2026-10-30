# Scalar bookkeeping check

Command executed:

    python -X utf8 ~/.claude/dreaming/lean_check.py --stmt "example (S R U d : ℚ) (hS : 0 ≤ S) (hd : 0 ≤ d) (hd1 : d ≤ 1/16) (hR : R ≤ d/4*S) (hU : U ≤ d/6*S) : R+U ≤ (5/192)*S := by nlinarith"

Observed exit1: RUNTIME_UNVERIFIED in126.5s.
source_sha256:169b190217a4efa650e7d4acfeb3fed2f7dd8434a25f986feaca7ed77cc47cfb.
Translation fidelity: UNVERIFIED.

No Lean certification is claimed. The statement, if checked, would only
certify the rational reserve bookkeeping: two bounded debits total at
most5/192 of a nonnegative surplus. It would not certify the analytic
Fourier statements or their translation. The same algebra is checked
with Fraction in147 declared finite scalar cases and proved for all
parameters in PROOF.md. No successful compiler/axiom receipt exists.
