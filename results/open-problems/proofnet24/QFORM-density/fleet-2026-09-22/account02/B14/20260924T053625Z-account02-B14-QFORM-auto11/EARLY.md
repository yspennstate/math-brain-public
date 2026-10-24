# Early calculation — same-sign Beta endpoint has environment mass homogeneity but no active-mass homogeneity

Run `20260924T053625Z-account02-B14-QFORM-auto11`.

The newest compatible account03/B14 theorem proves the probability-law compiler

`T=a(W+Phi(U,Z))^2+d(U+theta(Z))^2+R(Z)`, `ad>0`,

with `||p_T||inf <= pi K_W K_U/sqrt(|ad|)` for mutually independent `W,U,Z`, arbitrary measurable `Phi,theta,R` and density caps `K_W,K_U`.

The finite-measure extension is asymmetric in exactly the way localization needs. Let the active `W,U` laws be positive subdensities `rho_W,rho_U` with pointwise caps `L_W,L_U`, and let the environment be any finite positive measure `tau` of mass `m_Z`. Then the output pushforward measure has density cap

`||p_eta||inf <= pi L_W L_U m_Z / sqrt(|ad|)`.

Proof: for fixed `(u,z)`, the `W` square pushforward is bounded by `L_W/(sqrt(|a|)sqrt(v))` on the appropriate half-line. For fixed `z`, integrate against `rho_U<=L_U` and use the exact Beta integral

`int_{|x|<sqrt(s/|d|)} dx/sqrt(s-|d|x^2)=pi/sqrt(|d|)`.

Then integrate in `z`, paying only `tau(total)=m_Z`.

Thus arbitrary countable localization of the OUTSIDE/environment law is zero-tax: piece `j` of mass `m_j` costs exactly `m_j` times the common bound, so summation uses `sum m_j=1`. By contrast an ACTIVE-carrier piece of any mass `m>0` but density cap one still costs the full endpoint constant. This cannot be repaired by a positive mass exponent: with `rho_m=1_[-m/2,m/2]`, `W` Lebesgue density one on `[-1/2,1/2]`, and `a=d=1`, the pushforward of the finite product measure by `W^2+U^2` has density exactly `pi` for every `0<s<m^2/4`.

Hence no translation-uniform estimate of the form `C m^gamma` with `gamma>0` can replace the active cap-one endpoint. The square carrier must be reassembled before the Beta payment; only independent environment pieces are mass-homogeneous.
