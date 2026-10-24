# account02/B01 r32 — substantive checkpoint

Status: partial proved corollary plus exact N3 stress families; full QFORM remains open.

Source inputs actually used:
- newest-Claude Theorem H (mixed hub/Fresnel–Brascamp–Lieb), `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`;
- assigned partner account03/B01 r21 handoff `yspennstate/math-research-brain@8b3939cff4def148fd1a005b506c99e684176053`, whose canonical report is `yspennstate/math-open-problems@6a63d945b3e2409e5ff5799d2d13c3654bdd27e6:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T002425Z-r21/REPORT.md`.

## Mixed rank-two bank + one hub corollary

Partition the ORIGINAL coordinates as `{0} union B union J`. Suppose

`A_BB = M^T H M + D`,

where `M` is real `2 x |B|` of rank two, `H` is invertible symmetric `2 x 2`, and `D` is diagonal. Put `c=A_{B0}`, `R=range(M^T)`, `c_perp=(I-P_R)c`. Assume `c_perp != 0` and

`max_i [(P_R)_{ii} + u_i^2] <= 1/2`,  where `u=c_perp/||c_perp||_2`.

All other blocks (`A_00,A_0J,A_BJ,A_JJ`) are arbitrary. Then newest-Claude Theorem H with two Fresnel directions and one physical hub gives

`|phi_Q(t)| <= 8 pi^2 |t|^{-2} [|det H| det(MM^T) ||c_perp||_2^2]^{-1/2}`.

Indeed, if `V` is an orthonormal eigenframe for `M^T H M`, its two nonzero eigenvalues satisfy

`|lambda_1 lambda_2| = |det H| det(MM^T)`.

The augmented Gram of rows `(V_i,c_i)` has determinant `||c_perp||_2^2`, and its normalized row leverage is exactly `(P_R)_{ii}+u_i^2`. Using `|phi|<=1`,

`int_R min(1,K|t|^{-2})dt = 4 sqrt(K)`,

hence Fourier inversion yields the continuous-density estimate

`||p_Q||_infinity <= 4 sqrt(2) [|det H| det(MM^T) ||c_perp||_2^2]^{-1/4}`.     (A)

This is an averaged-frequency result. It does not assert any law-uniform pointwise one-dimensional quadratic-phase decay.

## Two strict no-pivot families

Let `m` be divisible by four and let `a,b,w` be the normalized Walsh rows

`a=(1,1,1,1,...)/sqrt(m)`,
`b=(1,-1,1,-1,...)/sqrt(m)`,
`w=(1,1,-1,-1,...)/sqrt(m)`.

They are orthonormal.

### Transverse hub

`Q_perp=(a.X_B)^2+(b.X_B)^2+2 sqrt(2) X_0(w.X_B)`.

Its nonzero spectrum is `{-sqrt(2),1,1,sqrt(2)}`. Physical diagonals on `B` equal `2/m`; every hub-bank 2x2 determinant equals `-2/m`; bank-bank 2x2 determinant magnitudes are at most `4/m^2`. Thus for every fixed no-pivot threshold `tau in (0,1]`, this lies in N3(tau) for all sufficiently large `m`. Every augmented leverage in (A) equals `3/m`, and `|det H|=det(MM^T)=1`, `||c_perp||^2=2`; therefore

`||p_Qperp||_infinity <= 4*2^(1/4) < 4.757`.               (B)

### Aligned hub: cross-volume-blind but partner-controlled

`Q_parallel=(a.X_B)^2+(b.X_B)^2+2 sqrt(2) X_0(a.X_B)`.

Its nonzero spectrum is `{-1,1,2}` and it obeys the same small physical pivot estimates. For every original-coordinate cut, the cross block has rank at most two, so all 3-volume and 5-volume certificates vanish identically.

Nevertheless

`Q_parallel=(a.X_B+sqrt(2)X_0)^2+(b.X_B)^2-2X_0^2`.

This is exactly the assigned partner r21 theorem with common bank `B`, `M=(a;b)`, `H=I_2`, conditioning bank `C={0}`, and no remainder bank. Hence, for all independent cap-one inputs,

`||p_Qparallel||_infinity <= pi e < 8.540`,                (C)

and the partner signed-Fejer interface gives the same bound on its averaged density kernels.

## First explicit remaining interface

For

`Q_eta=(a.X_B)^2+(b.X_B)^2+2 sqrt(2)X_0((a+eta w).X_B)`,

all `eta>=0` remain target-valid: the hub/a/w block has a principal `{hub,a}` submatrix with eigenvalues `-1,2`, while `b` supplies an independent eigenvalue `1`. At `eta=0`, (C) gives `pi e`; for `eta>0`, (A) gives only

`||p_Qeta||_infinity <= 4*2^(1/4) eta^(-1/2)`.

The blow-up as `eta downarrow 0` is a loss of the present certificate, not a QFORM counterexample. The next unpaid implication is a uniform near-parallel interpolation that spends the aligned grouped-pair endpoint and the transverse mixed-hub currency jointly, without treating a small matrix perturbation as a small random quadratic perturbation on unbounded inputs.
