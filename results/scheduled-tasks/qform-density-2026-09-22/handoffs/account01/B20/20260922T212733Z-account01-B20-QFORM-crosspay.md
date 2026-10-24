SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-22T21:27:33.980639Z.
attacking: account02/B20 r19's opposite-sign two-pivot strong residual Schur cross-bank payment.

# B20 handoff — two physical squares + rank-one cross bank

Status: `ESSENTIAL_STEP_APPLIED / OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAID / FULL_TARGET_OPEN`.

Canonical mathematics: `yspennstate/math-open-problems@5d47a9db625a630d748d8f2106869777ba5f732f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T212733Z-account01-B20-QFORM-crosspay/REPORT.md`.

Completed partner consumed: account02/B20 r19, `yspennstate/math-open-problems@e004778aef69cbf704ab9ccfb216a6f9bbba327b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T210111Z-account02-B20-QFORM-r19/REPORT.md`.

Source-valid scalar projection input: account03/B18 snapshot `yspennstate/math-open-problems@313aaf988145f63be448447eaf661aa399772088`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/B18-20260922T155856Z-r13/REPORT.md`, recording the Livshyts--Paouris--Pivovarov cap-one product-marginal bound `||p_{c^T X}||_inf <= sqrt(2)/||c||_2`.

## New theorem

After two physical scalar Schur pivots, write exactly

`Q=a U^2+d V^2+Z^T T Z`,

with untouched original-coordinate product source `Z`, and suppose `s_1(T[L,K])>=beta>0` for disjoint physical banks. Then

`||p_Q||_inf <= |a|^(-1/2) [16|d|^(-1/2)+2^(5/2) beta^(-1/2)]`.

The proof first decouples only physical bank `L`, obtaining

`L_{Z^T T Z}(h) <= 2^(5/4)(h/beta)^(1/4)`;

the second physical square raises this to a `h^(3/4)` small-ball bound; layer cake gives a uniform half-Riesz bound; the first physical square pays the density. No shifted-pivot independence or post-rotation independence is used.

Applying account02/B20 r19's actual inequalities

`|a|>=3501/8000`, `|d|>1/8`, `beta>1/4`

gives

`||p_Q||_inf <40 sqrt(16000/3501)=85.51138237264878...<85.512`.

Thus the exact r19 unpaid implication `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1` is now paid.

## Remaining debt

Full QFORM remains OPEN. Continuity remains separate. Next closure work should route the remaining high-leverage/strong-star/grouped-coordinate or zero/near-isotropic pivot states into this paid two-square-plus-cross packet or another reviewed product-preserving packet. Do not revive uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea, or rotated-independence shortcuts.

Execution label: `WITHOUT_VERIFIED_BRAIN`.
