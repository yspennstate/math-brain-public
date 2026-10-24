SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T11:54:50Z.
attacking: localized signed-inertia shielding: arbitrarily large added spectrum may spend only opposite-sign inertia on a bounded ORIGINAL-coordinate core, with an arbitrary dense operator-norm tail paid deterministically.

# account02/B12 — localized signed-inertia shield

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T115450Z-qform-b12-r11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING LOCALIZED-CORE STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and source state

The exact owner target remains open: the ORIGINAL coordinates are independent with arbitrary scalar densities `0<=f_i<=1`; `A=A^T` is arbitrary and has at least three eigenvalues of modulus at least one. No moment, support, iid, log-concavity, Gaussian, diagonal-basis, or post-rotation independence assumption is used.

The newest completed compatible partner is account03/B12 r56,
`yspennstate/math-open-problems@7ef8482d158e56e2e7300a4bc3d132654927ee5b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T115229Z-qform-eigenvalue-r56/REPORT.md`.
It proves that the target is already closed whenever

`r_1:=#{j:|lambda_j(A)|>=1} >=141`,

with arbitrary remaining signed spectrum. Thus any genuine counterexample must lie in the finite spectral-count sector

`boxed: 3<=r_1<=140.`

The next unpaid implication is therefore sharper than a generic additional-spectrum question: in this finite-large-spectrum sector, force either a bounded ORIGINAL-coordinate core that retains three signed modes after local hostile-inertia spending, or one of the already-paid projected-crossing / grouped-hub / ridge / physical-pair / Schur / common-plane / Pluecker exits. The theorem below closes the first alternative without any norm bound on the added signed packet.

Two completed receivers are used at their exact scopes.

1. The finite physical-core theorem, recalled and source-pinned in account03/B12 r47 (`math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`): if a literal ORIGINAL-coordinate principal block `C=A[H,H]`, `m=|H|`, has `s_3(C)>=a>0`, then, after conditioning only on ORIGINAL coordinates outside `H`,

`||p_(X^TAX)||_(infinity,ess) <= 2 sqrt(6 pi m)/a.`

Outside quadratic terms and cross couplings become arbitrary affine terms in the conditioned block and are retained.

2. The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, proves the unrestricted physical fifth-volume theorem `D_5`: for a literal disjoint ORIGINAL-coordinate cross block `B=A[I,J]`,

`||p_(X^TAX)||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10),`

with **no fifth-volume row-marginal condition**. Same-bank curvature and outside couplings remain present. I apply this theorem to an actual final block in Section 6.

## 2. Main deterministic theorem

For a real symmetric matrix `M`, let

`n_+(M)=#{lambda_j(M)>0}`, `n_-(M)=#{lambda_j(M)<0}`.

For `g>0`, also set

`p_g(M)=#{lambda_j(M)>=g}`, `n_g(M)=#{lambda_j(M)<=-g}`.

### Theorem 2.1 — `QFORM-LOCAL-SIGNED-INERTIA-SHIELD-v1`

Let `H` be a literal set of `m` ORIGINAL coordinates and write

`A=A_0+S+T`,

where `A_0,S,T` are real symmetric. Put

`C_0=A_0[H,H]`, `R=S[H,H]`, `C=A[H,H]`,

and assume only

`||T||_op<=delta`.

No bound is imposed on `||S||`, its global rank, inertia, eigenvalue magnitudes, or orientation. Define

`r_+=n_+(R)`, `r_-=n_-(R)`,
`p=p_g(C_0)`, `n=n_g(C_0)`.

Then for every `g>delta`, the final physical block `C` has at least

`p_*=(p-r_-)_+`

eigenvalues `>=g-delta`, and at least

`n_*=(n-r_+)_+`

eigenvalues `<=-(g-delta)`.

Consequently

`boxed: s_{p_*+n_*}(C) >= g-delta`

whenever `p_*+n_*>0`. In particular, if

`boxed: (p-r_-)_+ + (n-r_+)_+ >=3,`                         (2.1)

then the full quadratic form satisfies

`boxed:
 ||p_(X^TAX)||_(infinity,ess)
 <= 2 sqrt(6 pi m)/(g-delta).`                               (2.2)

The packet `S` may contain arbitrarily many arbitrarily large eigenvalues of either sign. Only the **opposite-sign inertia of its physical compression** spends protected modes. A positive-semidefinite addition on `H` is completely free for the positive protected modes, regardless of its norm and rank; a negative-semidefinite addition is analogously free for negative protected modes.

### Proof

Take the spectral positive/negative parts of the physical compression

`R=R_+-R_-`, `R_+,R_->=0`,

with

`rank(R_+)=r_+`, `rank(R_-)=r_-`.

First protect the positive threshold. Since `R_+>=0`, Loewner monotonicity gives

`lambda_j(C_0+R_+) >= lambda_j(C_0)`

for every decreasing eigenvalue index `j`. Subtracting the PSD matrix `R_-` of rank `r_-` can shift the decreasing eigenvalue list by at most `r_-` places: for every `k` with `k+r_-<=m`, rank interlacing gives

`lambda_k(C_0+R_+-R_-) >= lambda_{k+r_-}(C_0+R_+) >= lambda_{k+r_-}(C_0)`.   (2.3)

If `p>r_-`, take `k=p-r_-`; then the right side of (2.3) is at least `g`. Hence `C_0+R` has at least `p-r_-` eigenvalues at least `g`.

Apply the same argument to the negated matrices. Namely

`-(C_0+R)=(-C_0)+R_- - R_+`.

The positive addition `R_-` is free and only the rank-`r_+` subtraction `R_+` can spend negative protected modes. Since `p_g(-C_0)=n_g(C_0)=n`, the matrix `C_0+R` has at least `(n-r_+)_+` eigenvalues at most `-g`.

Finally `C=(C_0+R)+T[H,H]` and

`||T[H,H]||_op<=||T||_op<=delta`.

Weyl therefore moves every eigenvalue by at most `delta`, giving the two asserted final threshold counts at `g-delta`. Positive and negative threshold eigenspaces are disjoint, so their counts add and yield the singular-value statement. If their sum is at least three, `s_3(C)>=g-delta`, and the completed ORIGINAL-coordinate physical-core receiver gives (2.2). No random variable involving `T` or `S` is separated off. QED.

## 3. Spectral-window corollary

The theorem has a useful form tailored to additional eigenvalues. Fix a deterministic spectral cutoff `tau>0` and split a symmetric matrix spectrally as

`A=A_+-A_-+E`,

where `A_+,A_->=0` contain any chosen positive and negative spectral packets and

`||E||_op<tau`.

For a literal bounded coordinate set `H`, put

`P_H=A_+[H,H]`, `N_H=A_-[H,H]`.

For any `g>tau`, either of the conditions

`p_g(P_H)-rank(N_H)>=3`,                                      (3.1)

or

`p_g(N_H)-rank(P_H)>=3`                                      (3.2)

implies

`boxed: s_3(A[H,H]) >= g-tau`

and therefore

`boxed:
 ||p_(X^TAX)||_(infinity,ess)
 <= 2 sqrt(6 pi |H|)/(g-tau).`                                (3.3)

The magnitudes of the opposite-sign packet are absent from (3.1)-(3.3). Thus a huge negative spectral packet cannot destroy a localized positive core unless its physical compression has enough negative **inertia/rank directions** to spend that core, and vice versa.

This gives a concrete survivor obstruction complementary to partner r56. In the remaining `3<=r_1<=140` sector, a hard bounded carrier must satisfy, at every usable scale `g`,

`p_g(P_H) <= rank(N_H)+2`

and

`p_g(N_H) <= rank(P_H)+2`,                                    (3.4)

unless another already-paid receiver exits first. The obstruction is local sign-rank saturation, not large packet norm.

## 4. Strictness over norm and total-rank perturbation accounting

Take `m=7`,

`C_0=2 I_7`,

and for arbitrary `L>0` and arbitrary orthogonal `O in O(7)` let

`R_L=O diag(L,L,L,-L,-L,-L,-L) O^T`.

Then

`rank(R_L)=7`, `||R_L||=L`, `r_+=3`, `r_-=4`.

A norm-only perturbation estimate gives at best `[2-L]_+`, which is zero for `L>=2`. A total-rank budget sees rank seven and can spend all seven baseline modes.

The signed-inertia theorem instead uses only the four hostile negative directions. Since

`p_2(C_0)=7`,

it gives

`p_2(C_0+R_L)>=7-4=3`

for **every** `L`, with no commutativity hypothesis needed. Add any globally dense symmetric `T` with

`||T||_op<=1/4`.

Then the actual final ORIGINAL-coordinate principal block obeys

`boxed: lambda_3(A[H,H])>=7/4.`                                (4.1)

All entries outside this principal block, including arbitrary outside spectrum and arbitrary cross couplings, may be chosen freely before the final dense tail; conditioning outside `H` turns those couplings only into affine terms.

The physical-core receiver therefore gives the uniform family bound

`boxed:
 ||p_Q||_(infinity,ess)
 <= 2 sqrt(42 pi)/(7/4)
 =13.127787208700704... .`                                     (4.2)

By Cauchy interlacing, (4.1) also forces the full final symmetric matrix to have at least three eigenvalues `>=7/4>1`. Hence this is literally an exact-target family, uniformly in `L`, arbitrary outside signed spectrum and every allowed dense tail.

The gain is qualitative: an arbitrarily large **full-rank** local packet is harmless to three protected positive modes when only four of its local inertia directions point destructively.

## 5. Hybrid form and failure certificate

For later use define the localized signed reserve

`R_H(g;C_0,R)= (p_g(C_0)-n_-(R))_+ + (n_g(C_0)-n_+(R))_+.`

Then Theorem 2.1 is the compact implication

`R_H(g;C_0,R)>=3` and `g>delta`

`=> ||p_Q||_(infinity,ess) <= 2 sqrt(6 pi |H|)/(g-delta).`

Thus failure on every bounded candidate carrier forces

`boxed: R_H(g;C_0,R)<=2`                                      (5.1)

at every attempted quantitative scale. This is the usable obstruction passed forward: any future extraction argument may ignore packet magnitude and instead try to show that persistent local sign-rank saturation (5.1) creates a physical pair, projected crossing, grouped hub, ridge, Schur/common-plane, or Pluecker-volume certificate.

## 6. Required pinned-source application to a real final inequality

Use a companion twelve-coordinate subclass with `H={1,...,7}` and a disjoint five-coordinate bank `J`. Keep the seven-coordinate signed-inertia family of Section 4, allow an arbitrary symmetric same-bank block on `J`, and before the dense tail take the literal physical cross block

`B_0=A[H,J]=[2 I_5; 0_{2x5}]`.

The arbitrary unbounded signed addition is allowed in the `H-H` and `J-J` blocks and elsewhere, but this companion subclass leaves the displayed `H-J` crossing fixed until the final dense tail. Let

`||T||_op<=1/4`.

For the **actual final ORIGINAL-coordinate cross block**

`B=A[H,J]=B_0+T[H,J]`,

rectangular Weyl gives

`boxed: s_5(B)>=2-1/4=7/4.`                                    (6.1)

Therefore

`e_5(B^T B)>=s_5(B)^10 >=(7/4)^10`.                             (6.2)

Apply the completed pinned `D_5` theorem from `e5f71d79...` to this actual final block. Equations (6.1)-(6.2) give

`boxed:
 ||p_Q||_infinity
 <= 5 sqrt(2e)/(7/4)
 = 6.661839947420355... .`                                      (6.3)

This use is source-valid: there is no row-marginal hypothesis, same-bank quadratic terms stay in the form, and the fifth volume is computed from a literal final ORIGINAL-coordinate cross block. No common spectral modes are converted into fictitious cross volume.

The same family remains in the owner's exact target by either (4.1) or the cross block itself. Continuity holds on this D5 branch from the pinned Fourier proof; continuity for the unrestricted target remains a separate issue.

## 7. Dense-tail and independence safeguards

The small dense tail is used only through deterministic coefficient inequalities such as

`||T[H,H]||_op<=||T||_op`, `||T[H,J]||_op<=||T||_op`,

followed by Weyl. There is no assertion that `X^T T X` is uniformly small. Indeed for `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, one has `X^T T X>=delta R^2` almost surely.

Every probabilistic receiver conditions only on ORIGINAL independent coordinates. Orthogonal diagonalizations used to define inertia are deterministic matrix arguments; the rotated random variables are never declared independent.

## 8. Status and next step

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Partner r56 has reduced any counterexample to `3<=r_1<=140`. The new theorem removes another false obstruction: arbitrary norm, arbitrary favorable rank, and arbitrarily many huge same-sign local eigenvalues do not matter once a bounded core is found; only opposite-sign local inertia spends its protected modes.

The next B12 implication is to combine the r56 heavy/light finite-count geometry with (5.1): prove that persistent local sign-rank saturation on every bounded candidate core forces one of the already-paid cross/pair/hub/ridge/Schur/common-plane exits, or lowers the five-direction light endpoint. No `g_*`-scale carrier is assumed merely from `s_3(A)>=1`.
