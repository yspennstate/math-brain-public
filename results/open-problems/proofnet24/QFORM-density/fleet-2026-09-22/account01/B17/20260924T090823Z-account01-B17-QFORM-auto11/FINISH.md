# Finish — account01/B17

Run: `20260924T090823Z-account01-B17-QFORM-auto11`  
Finish UTC: `2026-09-24T09:26:30.153396Z`  
Status: `SUPPORTING_THEOREM_PROVED / EXACT_DENSE_STRESS_FAMILIES / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`.

Main result: for the compensated one-macroscopic-row hybrid
\[
Y_q=G_q+\sqrt q\,vU,\qquad
G_q\sim N\left(0,(I-qvv^T)/12\right),
\qquad B\sim(1,1,-1),
\]
the exact cone-tip formula reduces to the scalar factor
\[
H(x)=\sqrt{1+x}\int_{-1/2}^{1/2}e^{-6xu^2}du,
\]
and `H(x)<=1` for all `x>=0`, strictly for `x>0`. Therefore `p_{Y_q^TBY_q}(0)<=3sqrt(2)` for every macro orientation. To second order the least penalized orientation is uniquely the minority eigenaxis.

An exact entrywise-dense physical sequence with active spectrum `{1,1,-1}` and one leverage-`1/2` row converges uniformly in output density to the aligned `q=1/2` hybrid and has cone-tip limit
\[
2\sqrt{3\pi}\,\mathrm{erf}(1/\sqrt2)
=4.1916863432298254954\ldots .
\]

Completed account02/B17 result `QFORM-RANDOM-LOCATION-GAUSSIAN-INDEFINITE-BARRIER-v1` was applied to a separate exact entrywise-dense target family with spectrum `{1,1,-3/2}`. The global limiting density norm is bounded by
\[
3.9715052655710787928\ldots<3.98,
\]
and the source-pinned Fresnel--Brascamp--Lieb theorem upgrades convergence so all sufficiently large finite members satisfy `||p||_infinity<3.98`.

Checks: `CHECK.py`; evaluated output: `CHECK_OUTPUT.txt`; result `PASS_QFORM_B17_ONE_MACRO_ORIENTATION_BARRIER`.

The unrestricted universal theorem and unrestricted continuity conclusion remain open. Execution context remains `WITHOUT_VERIFIED_BRAIN`. No schedule, enabled/quiet state, notification/email/push state, task identity, authentication, permission, visibility, paid/remote execution, or public-release state was changed.
