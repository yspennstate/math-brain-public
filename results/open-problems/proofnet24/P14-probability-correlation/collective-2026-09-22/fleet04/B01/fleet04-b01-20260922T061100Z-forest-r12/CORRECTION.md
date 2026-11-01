# Correction to `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1`

The immutable `report.md` contains one harmless strictness typo in Section 2: after proving `0<p_h<=1/2`, it says `0<V_h<1/4`. The correct statement is

`0 < V_h = p_h(1-p_h) <= 1/4`.

Equality `V_h=1/4` can occur when `p_h=1/2`. No subsequent argument requires strict inequality at `1/4`; only `V_h>0` and `p_h<=1/2` are used. In particular, the total-covariance identity, the all-conditioner inequality `rho_eg rho_fg >= rho_ef`, the positive-covariance matching theorem, and the all-edge budget `T_e+T_f+a^2+(m-2)a<=1` are unchanged.

The original report is preserved rather than overwritten.
