# Statement-only adversary handoff: C0048

2026-10-10. This file contains no proposed proof.

Verified primary target: prove that the phase transition of the nearest-neighbor q-state Potts model on Z^d, d>=3, is discontinuous for every integer q>=3. Source: Duminil-Copin's 2017 Ising/Potts lectures, Conjecture 2, printed p.93 (PDF page index 92), https://www.ihes.fr/~duminil/publi/2017PIMS.pdf. The definition on printed p.5 is spontaneous magnetization at beta_c, not an unspecified jump at some beta.

Our normalization: spins {1,...,q}, zero field, unit ferromagnetic nearest-neighbor bonds, Gibbs weight exp(beta sum_{<x,y>} 1{sigma_x=sigma_y}), beta>=0. Let mu_beta^1 be the infinite-volume fixed-color-1 boundary state; m(beta)=(q mu_beta^1(sigma_0=1)-1)/(q-1), and beta_c=inf{beta:m(beta)>0}. Magnetization discontinuity at the order/disorder critical point means m(beta_c)>0 (with the appropriate standard one-sided continuity of the state). FK normalization p=1-exp(-beta).

For clarity, energy discontinuity is a separate stronger thermodynamic certificate: if P(beta)=lim |Lambda_n|^(-1) log Z_n^free(beta), then P'_+(beta_c)>P'_-(beta_c). Merely proving a jump at some beta>=beta_c does not identify it as beta_c. Merely producing different color-permuted ordered states does not imply an energy gap.

Source normalization: simplex spins satisfy a dot b=1 for the same color and -1/(q-1) otherwise. Thus our beta_delta equals q/(q-1) times the source's beta_simplex, and our m(beta_delta) equals its mu^b[ sigma_0 dot b ]. Reparameterizing beta preserves the critical-discontinuity statement. For finite entropy comparisons in this route, only exterior sites are pinned and the same variable region is compared in both laws.

Please attack the exact critical magnetization target independently. Current openness UNKNOWN as of this handoff; the dated ranking is not current-status evidence. PDF text was read directly; the screenshot tool returned an internal error.
