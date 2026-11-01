# Deterministic checks for fleet01/B09 20260923T104749Z

## 1. Fixed cutoff arithmetic

For `rho_*=10^-6`,

- `tau_*=(rho_*/2)^(1/3)=0.007937005259841...`.
- `delta_*=rho_*+tau_*/(1-tau_*)=0.008001505312588...`.
- `1-rho_*-tau_*=0.992061994740159...`.
- `1-2delta_*=0.983996989374823...`.
- Hence `h_*=0.983996989374823...`.
- `K0=3 exp(1/3) 2^(1/6)=4.69956594392443...`.
- `2sqrt(e) rho_*^(-1/4)=104.274288843589...`.
- `K0 delta_*^(-1/4)=15.713206699890...`.
- Thus `C_*<105`.

## 2. Triangle algebra

If `t=w12+w13+w23>=1-delta` and each `ell_i<1-2delta`, then

`w12=t-(w13+w23)>=t-ell3>delta`,

and cyclically all three internal weights exceed `delta`.

Writing `dij=|det(ci,cj)|` and `wij=dij^2/detG`, this implies

`dij>=sqrt(delta detG)`.

For the pivot at vertex 1,

`Delta_1^2=det(G-c1c1^T)=sum_{j<k, j,k!=1} det(cj,ck)^2`,

so `Delta_1>=d23`; cyclically likewise. If `Ri=||ci||Delta_i`, then

`R1R2R3 >= ||c1||||c2||||c3|| d12d13d23`.

Since `d12d13d23 <= (||c1||||c2||||c3||)^2`,

`R1R2R3 >= (d12d13d23)^(3/2)`.

Therefore some `Ri >= (d12d13d23)^(1/2) >= (delta detG)^(3/4)`.

The fleet03/B09 chirped-pivot bound `K0 Ri^(-1/3)` then gives

`K0(delta detG)^(-1/4)`.

## 3. Scaling

Under `A -> sA`, every cross row `ci -> s ci`, so `G -> s^2 G` and `det G -> s^4 det G`. Therefore `(det G)^(-1/4) -> |s|^-1(det G)^(-1/4)`, matching density scaling.

## 4. Latest fleet02/B09 partner application

For `m=25`, `rho=(24/25)^2=0.9216`. The grouped one-hub dense-hub-curvature theorem gives

`3e rho^(-1/3)=3e(24/25)^(-2/3)=8.379824333473508...`.

The compressed matrix is `[[0,1],[1,0]] direct_sum [1] direct_sum [1]`, so its nonzero spectrum is `{1,-1,1,1}`.

No stochastic simulation is used in these checks.
