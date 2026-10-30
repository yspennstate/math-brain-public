# QFORM fleet01/B11 r13 — substantive checkpoint

Run: `20260923T014132Z-fleet01-B11-QFORM-r13`

Status at checkpoint: full conjecture OPEN. Scope here is the exact-rank-three zero-physical-diagonal indefinite chamber.

Let `A=R M R^T`, `R^T R=I_3`, with inertia `(2,1)` or `(1,2)`, all physical diagonals zero, and `s=min |lambda(M)|`. After an orthogonal spectral change used only for deterministic matrix algebra and, if necessary, global sign reversal, write

`M=diag(p,q,-r)`, `p,q,r>0`.

Since all physical diagonals vanish, `tr A=tr M=0`, hence `r=p+q`.

For each spectral row `r_i=(x_i,y_i,z_i)`, put

`u_i=(sqrt(p)x_i,sqrt(q)y_i,sqrt(r)z_i)`.

Then `u_i` is Lorentz-null. After an irrelevant row sign, write

`u_i=rho_i (cos theta_i, sin theta_i,1)`.

Parseval gives `sum_i u_i u_i^T=diag(p,q,r)`, so

`sum rho_i^2=r`.

Define `mu_i=rho_i^2/r`; then `sum mu_i=1`.

For `q(theta)=(cos theta,sin theta,1)`, the exact determinant identity is

`det(q(theta_i),q(theta_j),q(theta_k))=4 prod_cyc sin((theta_i-theta_j)/2)`.

Therefore the Pluecker volume weight `w_ijk=det(R_{ijk})^2` is

`w_ijk = 16 (r^2/(pq)) mu_i mu_j mu_k prod_pairs sin^2((theta_a-theta_b)/2)`.

Since `r=p+q`, `r^2/(pq)>=4`, hence

`w_ijk >=64 mu_i mu_j mu_k prod_pairs sin^2((theta_a-theta_b)/2)`.

Consequently, if six pairwise disjoint angular sets `I_1,...,I_6` have pairwise circular separation at least `delta>0`, and `m_a=sum_{theta_i in I_a}mu_i`, then the disjoint-basis mass `D0=sum_{B cap T=empty}w_Bw_T` satisfies

`D0 >=4096 sin(delta/2)^12 prod_{a=1}^6 m_a`.

This is the first substantive new calculation of the run. It converts small positive `D0` into a quantitative statement that the Lorentz-null frame is close in mass to at most five angular clusters, rather than falsely claiming a bounded number of exact rays.

The next step is to derive a finite-bin five-cluster corollary and connect the partner's `D0` half-cut theorem to the newest fractional-volume/diffuse-cross-block exit without paying a local minor.
