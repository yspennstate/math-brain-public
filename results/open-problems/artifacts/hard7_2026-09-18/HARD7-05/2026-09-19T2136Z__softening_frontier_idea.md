# HARD7-05 route note — spend the last covariance slack before changing the mesh

New-method route recorded before repository certification.

Incoming rigorous bound: `theta_{2,1/4} > 41/250 = 0.164`, obtained at `r=7/8`, `s=199/200` for the independent-noise softened edge comparator

`Z_j = sqrt(s) Y_j + sqrt(1-s) E_j`,

with off-diagonal covariance `C_k = c r^(k-1)`, `c=s(1+r)/2`.

The previous comparator has avoidable covariance slack. At fixed `r=7/8`, admissibility is the all-lag family

`R(r^k) < s(1+r)r^(k-1)/2`, `k>=1`.

Exploratory evaluation only (not proof) indicates the first lag is the active boundary and puts the admissible softening frontier near `s=0.9944339`. Therefore, rather than increase the Ritz degree again or move `r`, try the rational point

`r=7/8`, `s=24861/25000=0.99444`, `c=74583/80000`.

Three section-B moves for this run:

- **B5 (add a parameter and differentiate/interpolate):** move only the softening parameter `s` down toward the admissibility boundary while holding the AR mesh fixed. This decreases every off-diagonal comparator covariance without giving up self-adjointness.
- **B24 (find the extremal object):** identify the active all-lag covariance constraint. The candidate rational `s=24861/25000` is chosen almost at the apparent lag-one boundary; exact certification must check lags 1--4 and then use the inherited tail envelope for every `k>=5`.
- **B20 (find why the algorithm fails):** exploratory operator calculations suggest that increasing `r` above `7/8` improves the true comparator rate but makes the existing fourth-trace/Temple certificate worse because the spectral-tail separation inflates. So this run does not spend effort on mesh refinement; it spends the already available covariance slack in `s` first.

The finite proof obligation is now precise. Recompute, with outward rational interval arithmetic, the degree-18 Rayleigh quotient and residual for the same frozen trial polynomial at `s=24861/25000`, reuse only the already proved analytic inequality `tr(K_{r,s}^4)<=tr(K_{r,1}^4)` and the hard-edge cap `553151/500000`, and test whether a Temple contradiction certifies the target

`theta_{2,1/4} > 1647/10000 = 0.1647`.

No sampled-path simulation is to be used as proof. If the exact covariance or Temple margins fail, this route is rejected rather than rounded into a theorem.