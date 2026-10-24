# B03 r29 crossblock strengthening

Parent handoff: `20260923T165124Z-account01-B03-QFORM-r29.md`.

New post-report theorem: for ANY original-coordinate split `I,J`, write `Q=F(X_I)+2X_I^T B X_J+G(X_J)` with arbitrary internal quadratic-plus-affine `F,G`, and set

`Z3=e_3(BB^T)=sum_{i<j<k}|b_i wedge b_j wedge b_k|^2`.

If `Z3>0`, then no row-marginal or exact-rank hypothesis is needed:

`||p_Q||inf <= 3*2^(3/2)*exp(1/2) Z3^(-1/6)
             =13.989863889582747... Z3^(-1/6)`,

and the density is continuous `C_0`.

Whole-copy dependence-safe estimate:

`int |t|^(-1/2)|phi_Q(t)|^2dt
 <=18.372247652462104... Z3^(-1/12)`.

Proof: if every 3-volume row marginal is <=1/2, apply the weighted-subset Fourier lemma directly at `k=0,ell=3`. If some row has marginal >1/2, promote that genuine physical row to a hub. Exact exterior algebra gives `V3'=alpha_i Z3>Z3/2`, so the parent row-marginal-free one-hub theorem pays the heavy branch. Its heavy branch already applies the designated account02/B03 `k=3` selector theorem to an actual inequality.

Singular-value corollary: if the physical cross block has `s3(B)>0`,

`||p_Q||inf <=13.9898638896/s3(B)`.

This removes the analytic volume-leverage gate from arbitrary-rank rank-three crossing cuts. The remaining full-target debt is structural: from `s3(A)>=1`, either extract a cross cut with `Z3`/`s3(B)` at universal scale or route to already-paid diagonal/pivot/grouped-hub/low-cross-rank packets.

Full proof: `yspennstate/math-open-problems@2062e0f60e39c2cb88fb72c4908d95f19676d00`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T165124Z-account01-B03-QFORM-r29/ADDENDUM_CROSSBLOCK.md`.
Checks: `yspennstate/math-open-problems@4049ddc9c879e14727900b99c158d884aebfa982`, same run path `CHECKS_CROSSBLOCK.json`, result `QFORM_B03_ROW_MARGINAL_FREE_3VOLUME_CROSSBLOCK_PASS`.

Full QFORM remains OPEN; unrestricted continuity remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.
