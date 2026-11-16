---
name: t320_w1_flow_depth_theta_log_r_over_eps_lip_r2_over_eps_2026_11_01
description: [PROVISIONAL] T320 W1 flow depth Theta(log(R/eps)/log L): any map needs Lip >= R^2/(653 eps) (isoperimetry on the mode band); odd-stripe affine couplings reach R^2/eps^2; TV open
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T16:33:00+04:00
  status: provisional
  evidence: "t320/w1check_run1.txt, stripes1d_run1.txt; moves m320a a10900df"
---

Row T320 asks for the depth of L-Lipschitz flow layers that push N(0, I) within eps of the two-Gaussian mixture at separation R.
The W1 version is now settled up to constants: D = Theta(log(R/eps)/log L) for R >= 8, L >= 2 and (R/4) Phibar(R/4) <= eps <= R/400.

The lower bound is sharper than the dossier's earlier eps-free one. Any map T with W1 <= eps has Lip(T) >= R^2/(653 eps). The proof
puts two 1-Lipschitz test functions on <e, T>, which pin each half's mass near 1/2 and make the band |f| < R/8 small, and then applies
Gaussian isoperimetry, which forces band mass >= 0.098 R/(4 Lip). The order R^2/eps is right: a single monotone map has
eps Lip/R^2 -> phi(0)/4.

The construction uses affine couplings in d = 2: x2 <- x2 + (R/2) s(x1) with s an ODD stripe wave of period ~eps. Oddness balances
the modes exactly; the exact 1-D W1 of the stripe conditional is 1/(4K). Scale layers x1 <- L x1 build the slope R^2/eps^2.

The TV version stays open. One coupling leaves x2 | x1 Gaussian (TV ~ 1/2). The candidate route is a scratch register (shrink
x1, copy x2 in, apply g, subtract, rescale), but a non-constant scale is not globally Lipschitz. Angle doubling shows there is no
volume obstruction.

**Why:** W1 and TV need different Lipschitz orders (R^2/eps against R/eps), and stripes work for W1 but not at all for TV.
A W1 construction is not evidence for TV.
**How to apply:** for push-forward depth questions, get the Lipschitz order from isoperimetry on a band between the modes. In a
coupling construction, make the mode selector odd so that the mode masses balance exactly.
Locators: brain-repo 06_math_research/frontier/rows/T320/DOSSIER.md section "1 Nov (an agent)",
moves m320a (a10900df). Related: [[t363_neurons_gain_activations_single_neuron_fate_ode_gives_1_8_basin_2026_11_01]] (same session).

