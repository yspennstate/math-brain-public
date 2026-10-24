SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T02:22:14Z.
attacking: two-sided mass-homogeneous overlap localization — preserve full unnormalised mass simultaneously through arbitrary translated slice fragments and arbitrary translated slope fragments, then apply account02/B14's completed overlap-slope theorem to a strict target family.

# Early calculation

Programme `QFORM-DENSITY-3EIG-20260922`, owner programme revision `2026-09-22.5`; full QFORM status remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source pin for the completed designated-partner result used here: `yspennstate/math-open-problems@0adab5e8aa852db2831d712bc820c9ea347b79ae:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T020607Z-account02-B14-QFORM-auto11/REPORT.md`, theorem `QFORM-OVERLAP-SLOPE-SUBPROBABILITY-HOMOGENEITY-v1`.

The partner theorem is one-sided in the following useful sense: with a probability slice law satisfying `ess sup_l |F_t(l)| <= A |t|^{-1/2}` and a slope-bank positive measure of mass `m` whose slope pushforward has density cap `M`, its output measure has density at most

`5 pi^{-1/5} A^{2/5} m^{3/5} M^{2/5}`.

The missing symmetric localization calculation is immediate once the slice law is also left unnormalised. Let the slice positive measure have mass `n`, disintegrate as `nu_l(dy) dl`, and satisfy the same unnormalised cap `ess sup_l |F_t(l)| <= A |t|^{-1/2}`. Then

`int |F_t(l)|^2 dl <= A n |t|^{-1/2}`,

so its first Plancherel multiplier obeys

`||G_t||_2 <= sqrt(pi A n) |t|^{-3/4}`.

For a slope positive measure of mass `m` with pushforward cap `M`, the partner's total-variation argument gives

`||K_t||_2 <= sqrt(pi m M) |t|^{-1/2}`.

Hence the unnormalised output measure `eta` of

`Q=H(X)+2XL+Y+2XS(Z)+R(Z)`

has

`|eta_hat(t)| <= pi sqrt(A M n m) |t|^{-5/4}`

and total mass `nm`. Since

`int_R min(B,C|t|^{-5/4}) dt = 10 C^{4/5} B^{1/5}`,

Fourier inversion yields

`||p_eta||_infinity <= 5 pi^{-1/5} A^{2/5} M^{2/5} (nm)^{3/5}`.

Therefore if the slice law is decomposed into pieces of masses `n_j` with `A_j <= A0 n_j`, and independently the slope law into pieces of masses `m_k` with `M_k <= M0 m_k`, then the `(j,k)` cell costs at most

`5 pi^{-1/5}(A0 M0)^{2/5} n_j m_k`.

Summing arbitrary countably many cells gives exactly the unsplit constant

`5 pi^{-1/5}(A0 M0)^{2/5}`.

This is the candidate theorem `QFORM-OVERLAP-TWO-SIDED-SUBPROBABILITY-HOMOGENEITY-v1`. The final report will prove the translation-mixture hypotheses `A_j<=A0 n_j` and `M_k<=M0 m_k` directly and apply them to an actual full-target quadratic family.
