SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T13:09:36Z.
attacking: the partner r29 tiny-Schur-tail / two-sided high-leverage collar by retaining the actual rank-four cross block and converting an exact-rank-three base star into an incident-volume L1 receiver.

# Early checkpoint — compound stability creates an actual incident 3-volume packet

Full QFORM remains OPEN. This checkpoint records the first substantive implication before the full proof is expanded.

Use fleet03/B02 r29. Its live physical cross block is

`N=N0+E`,

where `rank(N0)=3`, `rank(E)=1`, `s3(N0)>=a`, `||E||op<=a/16`; a physical `2x2` pivot `P` has `D=|det P|` and `D^2>=theta E2(N)`. In the live nested endpoint `theta=7/64` and `a=m*/kappa_theta`, `kappa_theta=(1+sqrt(theta^-1-1))^2`.

Let `C3(M)=wedge^3 M`. Since `E=p q^T` has rank one,

`C3(N)-C3(N0)=(p wedge) (wedge^2 N0) i_q`,

hence

`||C3(N)-C3(N0)||F <= ||E||op sqrt(E2(N0))`.

As `rank(N0)=3`,

`E2(N0)/E3(N0)=s1^-2+s2^-2+s3^-2 <=3/a^2`.

Therefore, with `delta=sqrt(3)/16`,

`||C3(N)-C3(N0)||F <= delta sqrt(E3(N0))`.

Write `N0=U Sigma V^T`, and suppose a physical row `i` and column `j` have exact-base range leverages

`ell_i=||U_i||^2>3/5`, `r_j=||V_j||^2>3/5`.

For exact rank three,

`det N0[S,T]^2=det(Sigma)^2 det(U_S)^2 det(V_T)^2`,

so the squared norm of the third-compound subvector over minors with `i in S, j in T` is exactly

`ell_i r_j E3(N0)`.

Restricting the compound perturbation to that subvector and using the reverse triangle inequality yields for the ACTUAL block N

`J_ij(N):=sum_{S contains i,T contains j,|S|=|T|=3} det N[S,T]^2
 >=(3/5-sqrt(3)/16)^2 E3(N0)
 >=c0 a^6`,

where

`c0=(3/5-sqrt(3)/16)^2=0.2418149394...`.

Also `sqrt(E3(N))<=(1+delta)sqrt(E3(N0))`, so

`J_ij(N)/E3(N) >=((3/5-delta)/(1+delta))^2=0.1968816133...`.

Thus the partner's two-sided high-leverage failure is not merely qualitative: after the actual small rank-one tail is restored, one physical row-column star still carries at least 19.68% of the ACTUAL third exterior volume.

The next step in this run is to combine this incident packet with the partner's dominant physical `2x2` pivot through the already-proved fleet02/B02 incident-(3+2) disjoint-transport theorem. D5 is checked on the live collar as well: because the partner branch has an invertible 2x2 pivot and exact rank-two Schur residual, `rank(N)=4`, hence `E5(N)=0`; the ungated D5 theorem is genuinely unavailable here rather than being silently ignored.
