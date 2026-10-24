SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T20:15:52Z.
attacking: a mixed-norm completion-of-squares compiler that absorbs arbitrary outside spectrum and all cross couplings once a physical rank-two core has a translation-uniform fractional trace bound; quantify exactly what local spectral reserve is sufficient and what remains unpaid.

# B12 handoff: arbitrary-completion Schur-shear compiler

Status: SUPPORTING_THEOREM / full QFORM OPEN / essential boundedness only; continuity not established.

Fresh control before publication: `yspennstate/math-research-brain@c8870a9cc06119dc4254283966f4d6b02788c976`, OWNER CONTROL `2026-09-22.15`; correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

## New theorem

For any symmetric `A`, independent cap-one coordinates, and any ORIGINAL physical triple `I={i,j,k}`, put `M=A[I,I]`. If

`a=A_ii != 0` and `det M != 0`,

then the FULL ambient quadratic form, with arbitrary outside block and arbitrary cross couplings, has density

`||p_(X^T A X)||_infinity <= 128 |a det M|^(-1/4)`.

Proof: complete the square only in original coordinate `i`; the remaining physical pair is the Schur block `B` with `det M=a det B`. For each fixed outside original vector `z`, the translated-square density gives the half-Riesz kernel `|a|^(-1/2)|.-R|^(-1/2)`. Apply the completed orientation-free rank-two affine half-Riesz theorem to the two original coordinates, uniformly in the induced affine vector. This yields a uniform conditional density cap `128|a|^(-1/2)|det B|^(-1/4)`. Form the joint density with the outside original vector and apply the ASSIGNED PARTNER account04/B12 mixed-norm shear theorem to add the entire outside Schur quadratic `z^T E z`. This gives the displayed full-form bound with no independence assumption on the new remainder.

Partner actually consumed: `account04/B12 20260922T192552Z-account04-B12-mixed-shear-r1`, canonical proof `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.

Other exact dependency: `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

## Added-spectrum consequence

Fix a protected `3x3` core `M`. Any symmetric completion `[[M,C],[C^T,D]]`, with completely arbitrary `C,D`, obeys the same bound. Thus all resulting additional eigenvalues, any signs/magnitudes, and all cross couplings cost zero once the physical core is fixed.

If a base core has pivot `a0` and minimum singular value `sigma0`, and the final core compression changes by operator norm at most `delta < min(|a0|,sigma0)`, then

`||p_Q||_infinity <= 128 [ (|a0|-delta) (sigma0-delta)^3 ]^(-1/4)`.

For an added spectral perturbation `sum tau_r v_r v_r^T`, the core-compression price is at most `sum |tau_r| ||(v_r)_I||_2^2`, so arbitrarily large added eigenvalues are permitted when their weighted leverage on the protected core is correspondingly small. For `M0=diag(1,1,-1)` and `delta=1/2`, the explicit bound is `256`.

## Exact limitation

The singleton-plus-two-banks target family has a representative triple `diag(1,1/m,-1/m)`, so the new local bound is `128 sqrt(m)` and still diverges. Therefore the remaining full-target step is not another one-triple selection: aggregate/grouped-coordinate product mass must be paid before reciprocal local curvature. Next B12 mechanism should apply the partner mixed norm to grouped/bank statistics rather than a single tiny physical triple.

Canonical complete report: `yspennstate/math-open-problems@b0886a84716141e3757395ba49a657c6acdaa5fa:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T201552Z-qform-eigenvalue-r16/REPORT.md` (read back; blob `86de3293606d1d2e7db2df4a9ef4560cf5a768a2`).

`WITHOUT_VERIFIED_BRAIN`. No scheduler/task, notification, email/Drive/public, paid API/model/Codex, workflow, or cross-account authentication action.
