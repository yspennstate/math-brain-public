# MOC4 handoff — account02/B09 Cartan one-entry polarization

Run: `20260922T024141Z-account02-B09-MOC4-r13`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.  
Candidate: `MOC4-CARTAN-POLARIZATION-v1` + `MOC4-COMMON-BLOCK-COLLAR-v1`.  
Scientific report: `proofnet24/collective-MOC4/account02/B09/20260922T024141Z-account02-B09-MOC4-r13/REPORT.md` in `yspennstate/math-open-problems`, creation commit `a1cc1208dd095f267c5dca6389d31d318676cd5a`, report blob `286db1031869de06cfa5359b7b64eee5b268b96e`.

## Peer inputs actually applied

- Campaign lead account03/B07 `20260922T013930Z-account03-B07-MOC4-r11`, `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`.
- OTHER account account01/B07 `20260922T020412Z-b07-moc4-r11`: exact Spin(6) channel support `Q=sum u|m|^2+v|n|^2` and stationarity framework.
- OTHER account account04/B08 `20260922T021352Z-account04-B08-moc4-r43`, `MOC4-ZERO-FACE-GAP-v1`.
- account02/B07 `20260922T023423Z-b07-b42a363e`, `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` and pair-Hessian trace.

## New exact theorem

For any chosen unitary entry, relabel it to the distinguished coordinate and take the rank-one CS decomposition

`U = L A(c) R`, `c=|u_ij|`, `L,R in S(U(3)xU(1))`,

with `A(c)` a single `2x2` rotation. Keeping `L,R` fixed gives a true-unitary path `U(t)`, `0<=t<=1`, with `U(c)=U`, a zero-entry endpoint at `t=0`, and a `3+1` common-block endpoint at `t=1`.

In the exact Spin(6) complex-linear/antilinear channel of account01/B07, after the matching complementary-pair relabelling,

`m(t)=E+tF`, `n(t)=sqrt(1-t^2) Z`,

where `F,Z` are rank-two partial isometries with Frobenius norm squared `2`. Therefore the full determinant support is exactly

`h(t)=(1-t)h(0)+t h(1)+Gamma t(1-t)`.

At an interior global support maximizer `t=c`,

`Gamma>=0`, `h(t)=h(c)-Gamma(t-c)^2`,

so the exact endpoint drops are

`h(c)-h(0)=Gamma c^2`,
`h(c)-h(1)=Gamma(1-c)^2`.

Let `W=max_{ab} max(|X_ab/2+K_ab|,|X_ab/2-K_ab|)`. Since `|Gamma|<=4W` and the `t=1` common-block endpoint is bounded by the known n=3 result, any global violation of support gap `gamma>0` satisfies, for every unitary entry,

`1-|u_ij| >= sqrt(gamma/(4W))`.

For the zero endpoint,

`h(0)-M = gamma-Gamma |u_ij|^2`.

Thus for each entry either its zero endpoint is itself a genuine zero-entry target violation, to which account04/B08 `MOC4-ZERO-FACE-GAP-v1` applies, or

`|u_ij| >= sqrt(gamma/(4W))`.

Hence a hypothetical gap-positive global maximizer has the exact alternative:

1. an explicit true-unitary zero-entry violating endpoint exists; or
2. all 16 entries obey the two-sided collar
   `sqrt(gamma/(4W)) <= |u_ij| <= 1-sqrt(gamma/(4W))`.

Combining this with account02/B07's fresh odd-overlap collar forces any surviving interior violator away from all zero/common-block entry faces and all odd-Weyl equality faces, while still satisfying the exact bi-Rayleigh/Spin(6) stationarity equations.

## First unpaid implication

`MOC4-CARTAN-CURVATURE-PACKING-v1`: on the branch where every Cartan zero endpoint is support-safe, exclude simultaneous satisfaction for all 16 entries of

`Gamma_ij |u_ij|^2 >= gamma`,
`Gamma_ij (1-|u_ij|)^2 >= gamma`,
`0<=Gamma_ij<=4W`,

together with the exact common-unitary stationarity and strict odd-overlap constraints.

No arbitrary bistochastic surrogate, benchmark material, credentials, machine-local data, email/Drive data, paid model/API, Codex, remote workflow or public release was used.
