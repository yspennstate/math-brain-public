SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T13:18:15Z.
attacking: aligned-or-localized multihub leakage receiver: remove the diagonal-light restriction using exact-rank-two grouped Fourier and aggregate E2 smoothing while preserving original-coordinate product provenance.

# Early substantive checkpoint — r38

Full target remains OPEN. This checkpoint records the first useful calculation before the final report.

## Source-pinned bridge

1. fleet03/B08 r37, `58b2a0752f409dd48ae5e39851ac84f13be4470b`, left a two-hub branch with cross matrix `C` and arbitrary non-diagonal same-bank light curvature as an explicit interface.
2. fleet03/B06, `1287456c9a709f8c3f117c23faa46e75f4560d01`, proves for an exact rank-two ORIGINAL-coordinate cross bank, with arbitrary same-bank quadratic-affine terms retained,

`||p_R||_3 <= 3^(2/3) e^(1/3) (sigma_1(C)sigma_2(C))^(-1/3)`

when one active bank consists of exactly two physical coordinates.
3. fleet03/B08 r32, `2cb64b71f8aafa0892547dffebcf6af647ea7c64`, proves for any literal physical cross block `M`

`||p_R||_(9/4) < 7 E_2(M)^(-5/36)`

with arbitrary self blocks/couplings, and after a genuine scalar square of coefficient `a!=0`,

`||p_Q||_inf < 36.45 |a|^(-1/2) E_2(M)^(-1/8)`.
4. designated partner fleet04/B08, `abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`, gives the anisotropic core `H_R=diag(R,R^(-1))`, `R>=3`, with sharp grouped endpoint `<7.251` at unit scale.

## First implication

Let two original hub coordinates `U=(U_1,U_2)` and a disjoint light bank `V` have literal cross block `C` of rank two. Let all hub-hub and light-light quadratic terms, affine terms, outside coordinates and outside couplings be arbitrary. Then the full form has an `L^3` density with

`||p_Q||_3 <= 3^(2/3)e^(1/3) [det(C^T C)]^(-1/6)`.

Thus r37's diagonal-light restriction is unnecessary for `L^3` control in the exact two-hub/rank-two branch; no leverage gate is needed.

If in addition a disjoint genuine scalar square of coefficient `a` is present (or appears after a source-valid scalar completion with the exact cross bank in its residual), the completed square transducer gives

`||p_Q||_inf < 7.829 |a|^(-1/2)[det(C^T C)]^(-1/8)`.

## Leakage-stable anisotropic consequence

For scaled partner core `C=L diag(R,R^(-1))`, `det(C^T C)=L^4`. Therefore arbitrary same-side quadratic-affine leakage on the two arm banks still gives

`||p_Q||_inf < 7.829/L`

under a disjoint outer square of coefficient `L`.

Using the sharper double-incident grouped theorem `c248abc9be918698c6d5a68108c615ba1c4790b3`, the same exact-rank-two core actually retains the partner-scale constant

`||p_Q||_inf <= C_grp/L`, `C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)=7.2500551088...<7.251`,

while allowing arbitrary same-side quadratic-affine terms.

Moreover, if arbitrary additional cross/tail entries enlarge the residual cross block to any `M` that still contains this physical `2x2` core unchanged, then

`E_2(M) >= det(C)^2 = L^4`,

so r32 gives the leakage-stable high-rank bound

`||p_Q||_inf < 36.45/L`.

This pays arbitrary same-side curvature and arbitrary appended cross/tail couplings around the designated partner core. The still-open interface is scalar-Schur cancellation when couplings of the outer square alter the core itself: a rank-one Schur update can make the anchored determinant small, so no pre-Schur E2 survival is claimed.
