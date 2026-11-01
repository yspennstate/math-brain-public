# PROB10-06 idea before code — differentiate the branch-addition gap, not the two scores separately

Runtime model exposed to this worker: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is **UNVERIFIED**. GPT-6/maximum is prompt-only and is not claimed.

Source convention remains fixed: `P(nu=0)=0`, `m=E nu>1`; child bias `beta` weights each child relative to the parent and larger `beta` pushes outward; parent bias is `lambda=1/beta`, so the LPP conjecture is decreasing speed in `lambda` on `0<lambda<m`. This run stays on the unresolved no-leaf family `P(nu=2)=1-p, P(nu=3)=p` and does not claim full-source closure.

## New route

The predecessor bounded

`Delta = h_2/c_2 - h_3/c_3 = (log(c_3/c_2))'`

by bounding `h_2/c_2` and `h_3/c_3` separately. That loses the critical cancellation because both normalized scores can be large while their difference is modest. Instead use the exact branch-addition identity

`J := c_2-c_3 = E[B_0 B_3/(D_2 D_3)]`,

where `D_2=lambda-1+B_0+B_1+B_2` and `D_3=D_2+B_3`. Writing `d=J/c_2`, one has `c_3/c_2=1-d`, hence

`Delta = -d'/(1-d) = (-J' - d h_2)/c_3 <= (-J')/c_3`

for `lambda>1`, because `h_2>=0`.

Differentiate the integrand. With `U_i=-B_i'>=0`,

`D_2'=1-(U_0+U_1+U_2) <= 1`,
`D_3'=1-(U_0+U_1+U_2+U_3) <= 1`.

Therefore

`-J' <= 2 E[U] E[B]/a^2 + 2(E[B])^2/a^3`, `a=lambda-1`,

using independence after dropping denominators to `a`. If `u=ess sup B`, then for support at most 3,

`u <= (3-lambda)/3`,

and `D_3 <= a+4u=(9-lambda)/3`, hence

`c_3 >= E[B]/Dmax`, `Dmax=(9-lambda)/3`.

Thus the new cancellation-preserving bound is

`Delta <= Dmax * [ 2 eta/a^2 + 2 u/a^3 ]`, `eta=E[U]`.

The predecessor's type-vector reciprocal-Jensen contraction supplies a rigorous upper bound `eta<=A/(1-rho)` with exact finite-depth error. The proposed finite target is the genuinely new strip

`p in [3/4,1]`, `lambda in [107/50,12/5]`.

If exact rational interval arithmetic proves both

`rho < 49/50`,
`lambda*g(theta)*Delta < 999/1000`,

then Aidekon's exact score identity gives strict speed decrease with explicit margin at least

`4*(1/1000)/(3+12/5)^2 = 1/7290`,

while the same coefficient gives `E[B_N-B] <= (49/50)^N`.

This would move the upper-tail endpoint from `2.14` to `2.4`, while the all-mixture endpoint remains `1.85527` and the parent conjecture remains OPEN/PARTIAL.

## Three materially different attacks for this run

- **Move #3 — prove something stronger:** differentiate the exact branch-addition gap `J=c_2-c_3`; this is the primary route above and preserves cancellation that separate score bounds lose.
- **Move #2 — attack the negation first:** test the tempting stronger claim `Delta<=0`. It already fails on the deterministic 3-ary endpoint `p=1`: there `B=(3-lambda)/3`, `c_3/c_2=6/(9-lambda)`, so `Delta=1/(9-lambda)>0`. Any valid proof must control a positive but finite `Delta`, not force its sign negative.
- **Move #12 — find what is conserved / exact recursive observable:** use the logarithmic escape elasticity `q=U/B`, which obeys the exact pathwise discounted recursion `q=(1-B)(lambda^{-1}+sum_i (B_i/S) q_i)`. This gives a ray representation, but on the deterministic 3-ary tree the discount is `1-B=lambda/3 ->1` as `lambda->3`; therefore no uniform full-transient contraction can follow from a bias-independent bound on this discount alone. The obstruction is exact and points back to the branch-gap cancellation.

No code has been written for this run before this note.