# Check history

2026-10-12. First exact linear-system check failed: integer coefficient assignments introduced float division. Corrected all coefficients to Fraction; exact checks then passed for L=2,3,5,10,20,40 and all 4096 twelve-step paths.

First Lean run failed because PowerShell piped Unicode mathematical characters to Python as question marks. No formal check was claimed. Recreated the Lean file in ASCII.

Second Lean run failed because Windows PowerShell Set-Content added a UTF8 BOM, which this Lean invocation did not accept at the first import. Removed the BOM with Python utf-8-sig input and utf8 output, and replaced ASCII Boolean inequality by Not of equality. Final run result is recorded in lean_result.json and lean_check.log; only return code zero will count as checked.

The third Lean run checked the induction but failed at the final normalization: h0 was rewritten in a hypothesis but not in the goal. Added rw [h0] to the goal; no mathematical hypothesis was changed. A final sequential rerun follows.

Final Lean run passed with exit code 0. Both theorem declarations are kernel-checked; no axiom placeholders were introduced. The complete stochastic conclusions remain handwritten proofs with the scope stated in ATTEMPT.md.


2026-10-12 second attempt: SecondChecks.lean passed five finite algebraic identities/inequalities; fresh_history_experiments.py passed exact finite cover and likelihood stress tests. FreshHistoryChecks.lean first failed to parse ASCII membership notation, then passed after the Unicode membership and explicit Finset.sum correction. Final exit code: 0; elapsed seconds: 206.7088180000428. Axioms: propext, Classical.choice, Quot.sound. No sorry/native_decide. Full stochastic proof is handwritten, not formally certified by these finite checks. The deterministic plane lemma was independently reproved and its limit order reviewed.
