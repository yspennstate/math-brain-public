SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T05:58:11Z.
attacking: the r51 aligned-star/top-two survivor: pay the exact aligned rank-two-child endpoint, expose its product-safe aggregate determinant-star, and route target-scale child leakage through the designated account04/B08 deletion-child theorem.

# account03/B08 r52 — exact aligned endpoint and punctured-collar router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW TARGET-SCALE ENDPOINT THEOREM + PRODUCT-SAFE STRUCTURAL IDENTITY + DESIGNATED PARTNER APPLICATION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. This report proves essential boundedness at the exact aligned endpoint and a continuous bound on the target-scale child-third-spectrum partner branch. No moment, support, iid, Gaussian, log-concavity, post-rotation independence, arbitrary-joint 3D coarea, conditional-density cap, fiber supremum, pointwise quadratic-phase decay, or deletion of a small random quadratic term is used.

## 1. Fresh state and source pins

Initial fresh control was read from `yspennstate/math-research-brain@f3b5298d1bffeedae854bfaae50444a1322f9393`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. The live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account03/B08.json` were read before the mathematics. The same UTC-hour account03/B08 login already existed for r51; protocol says not to overwrite a same-hour login, so r52 created a unique START record and preserved that login.

Immediate predecessor:

- account03/B08 r51, `yspennstate/math-open-problems@b28041e2486d6523b22946efc2c4a9b5bc5eea04`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T052228Z-account03-B08-qform-diffuse-r51/REPORT.md`.

Analytic inputs used exactly at their proved scopes:

1. General three-variable small-hub coarea core, `yspennstate/math-open-problems@391db3ae3b9f9fd5104eb19c8394cc13c9f6a045`, `proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md`. If a cap-one physical hub is independent of a light pair of joint density cap `M`, and a symmetric `3 x 3` core `T` has `s_3(T)>=1` and physical hub diagonal `<1/64` in modulus, then the quadratic output density is at most `1+32M`. The theorem allows deterministic affine terms. In particular an orthonormal two-dimensional projection of an original product source has `M<=2`.

2. Orientation-free rank-two affine half-Riesz / exact-rank-three Schur consequence, `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. For an exact-rank-three representation `A=VMV^T`, `V^TV=I_3`, a physical row with leverage `c_i`, and nonzero `a=A_ii`, the full form obeys

`||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.

3. Exact-null physical-hub mixed-Fresnel closure, `yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`. It is used only for the optional continuity sharpening at zero hub diagonal.

4. Designated partner account04/B08, `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`, `yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`. If an ORIGINAL-coordinate deletion child has three eigenvalues of modulus at least `s` and its spectral projection onto `|lambda|>=s/64` has physical leverage at most `1/32`, then the full parent has

`||p_Q||_infinity <64/s`, `p_Q in C_0(R)`.

## 2. The exact aligned endpoint is uniformly paid

Consider one ORIGINAL physical hub coordinate `H=X_0` and the remaining independent product vector `X=(X_1,...,X_N)`. Let `V in R^(N x 2)` have orthonormal columns and let `Lambda=Lambda^T` be invertible. Put

`C=V Lambda V^T`, `b=V c`,

and

`A = [[a,b^T],[b,C]].`                                             (2.1)

Thus the deletion child has exact rank two and the physical star is exactly aligned with its two-dimensional range. Assume

`s_3(A)>=L>0`.                                                       (2.2)

### Theorem 2.1 — `QFORM-EXACT-ALIGNED-RANK2-CHILD-ENDPOINT-v1`

For every admissible product law,

`boxed: ||p_(X^T A X)||_infinity <= 128*64^(1/4)/L <362.039/L.`     (2.3)

This is an essential-boundedness conclusion. If in addition `a=0` and

`max_j ||V_{j,*}||_2^2 <=1/2`,                                    (2.4)

then the stronger exact-null theorem gives

`boxed: ||p_Q||_infinity <=3*2^(4/3)/L <7.560/L,  p_Q in C_0(R).` (2.5)

In the live r51 diffuse-two-frame chamber, (2.4) is automatic because the gate is `max_j ||V_j||^2<=1/16`.

### Proof

Define the `(N+1) x 3` orthonormal-column matrix

`U = [[1,0,0],[0,V]]`

and the symmetric `3 x 3` core

`K = [[a,c^T],[c,Lambda]].`                                       (2.6)

Then exactly

`A=U K U^T`.                                                       (2.7)

Since (2.2) holds, `A` has rank at least three; (2.7) has rank at most three. Hence `rank(A)=3`, `K` is invertible, its three nonzero eigenvalues are exactly those of `A`, and

`s_3(K)>=L`, `|det K|>=L^3`.                                      (2.8)

The physical hub row of `U` is `(1,0,0)`, so its spectral-range leverage equals one. Also `Y=V^T X` is independent of `H`, and the valid two-dimensional product-projection theorem gives a joint density cap

`||p_Y||_infinity<=2`.                                            (2.9)

There are two cases.

**Small physical hub diagonal.** If `|a|<L/64`, scale the core by `L`: `T=K/L` has `s_3(T)>=1` and `|T_HH|<1/64`. Apply the source-pinned general three-variable coarea theorem with `M=2` to `Q/L`. It gives

`||p_(Q/L)||_infinity<=1+32*2=65`,

hence

`||p_Q||_infinity<=65/L`.                                        (2.10)

No independence of the two components of `Y` is asserted or needed.

**Non-small physical hub diagonal.** If `|a|>=L/64`, apply the exact-rank-three consequence of the orientation-free rank-two affine half-Riesz theorem to (2.7). The hub leverage is `c_0=1`, so

`||p_Q||_infinity <=128 [|a| |det K|]^(-1/4)
 <=128 [L^4/64]^(-1/4)
 =128*64^(1/4)/L.`                                                (2.11)

Together (2.10)-(2.11) prove (2.3).

For `a=0`, the hub row is an exact null row in the rank-three spectral core, with leverage `h=1`. Every complementary physical row has transverse leverage exactly `||V_j||^2`; under (2.4), the source-pinned null-hub mixed-Fresnel theorem applies. Since `|det K|>=L^3`, scaling gives (2.5), including continuity. QED.

The point of Theorem 2.1 is not that exact rank three was unknown in every orientation. It closes precisely the limiting endpoint left by the r51 aligned-star router using a physical hub plus a two-dimensional product projection, without selecting a tiny physical minor.

## 3. Exact distributed determinant-star identity

The same endpoint carries a useful product-safe physical aggregate which survives even when every single physical triple is tiny.

Let `v_j^T` be row `j` of `V`. For every two distinct child coordinates `j,k`, let `A_{0jk}` be the ORIGINAL-coordinate principal `3 x 3` block on the hub and those two child coordinates.

### Lemma 3.1 — `QFORM-ALIGNED-ENDPOINT-DETERMINANT-STAR-v1`

Under (2.1),

`det A_{0jk} = det(K) det(v_j,v_k)^2`.                            (3.1)

Consequently

`boxed: sum_(j<k) |det A_{0jk}| = |det K| >=L^3.`                (3.2)

Moreover there is an ORIGINAL-coordinate partition of the child coordinates `J disjoint Kset` such that

`boxed: sum_(j in J,k in Kset) |det A_{0jk}| >= |det K|/2 >=L^3/2.` (3.3)

If `max_j ||v_j||^2<=1/16`, then each individual normalized Pluecker weight satisfies

`det(v_j,v_k)^2<=1/256`,                                         (3.4)

so (3.2)-(3.3) are genuinely aggregate curvature rather than a disguised uniformly large fixed minor.

### Proof

For `I={0,j,k}`, the `3 x 3` row restriction of `U` is

`U_I=[[1,0,0],[0,v_j^T],[0,v_k^T]]`.

Thus

`det A_I = det(U_I K U_I^T)=det K * det(U_I)^2
          =det K * det(v_j,v_k)^2`,

which is (3.1). Cauchy-Binet and `V^TV=I_2` give

`sum_(j<k) det(v_j,v_k)^2 = det(V^T V)=1`,

proving (3.2). Put each child coordinate independently into either side of a random half-partition. Each unordered pair is separated with probability `1/2`, so the expected cross mass in (3.3) equals `|det K|/2`; at least one actual physical partition attains the expectation. Finally Hadamard gives `det(v_j,v_k)^2<=||v_j||^2||v_k||^2`, proving (3.4). QED.

This identity gives a concrete source-disjoint aggregate currency for the aligned endpoint. It does **not** by itself license reciprocal-minor averaging, and this report does not claim that (3.3) pays a nonzero overlapping leakage term.

## 4. Designated partner applied at a target-scale child-third-spectrum inequality

Return to the literal r51 deletion geometry

`A=[[a,b^T],[b,C]]`,                                              (4.1)

let `m=s_2(C)` and `r=s_3(C)`, and recall that on the inherited diffuse-source survivor

`m>=m_0 L`, `m_0=sqrt(47/48)=0.9895285072531598...`.             (4.2)

The aligned chamber is

`beta:=dist(b,range(V)) < ||b||/4`,                              (4.3)

where `V` is the top-two absolute-eigenvalue frame of `C`.

If

`r>=L/64`,                                                       (4.4)

then the actual ORIGINAL-coordinate deletion child has three eigenvalues of modulus at least `r`. Apply the designated account04/B08 theorem at **the actual scale `s=r`**. Let

`P_r=1_{|C|>=r/64}`.                                             (4.5)

If

`max_j (P_r)_jj <=1/32`,                                        (4.6)

then

`boxed: ||p_Q||_infinity <64/r <=4096/L,  p_Q in C_0(R).`       (4.7)

If (4.6) fails, choose a physical child coordinate `j` with `(P_r)_jj>1/32`. Spectral energy gives

`||C e_j||_2 > (r/64)/sqrt(32)`.

Splitting this Euclidean norm into diagonal and off-diagonal parts yields

`boxed: max{|C_jj|, ||C[j,-j]||_2} > r/512 >=L/32768.`          (4.8)

This is the required completed account04/B08 partner result applied to an actual inequality in the present aligned chamber.

A separate pre-router failure is already quantitative: if the child top-two frame itself has a physical leverage `>1/16`, then

`||C e_j||_2 >m/4`,

so

`max{|C_jj|,||C[j,-j]||_2}>m/(4sqrt(2))
 >=0.1749255794... L`.                                           (4.9)

## 5. Sharpened remaining aligned survivor

Combine r51 with Theorem 2.1 and Section 4. The full target is **not** closed, but the exact location of the next B08 debt becomes narrower.

In the r51 distributed-star state, after the already-paid transverse chamber and the physical top-two-leverage alternative, an unpaid aligned state may be assumed to satisfy

`max_j ||V_j||^2<=1/16`,                                        (5.1)

`beta<||b||/4`,                                                  (5.2)

`0<=r<L/64`,                                                     (5.3)

and it cannot have simultaneously

`beta=0` and `r=0`,                                              (5.4)

because (5.4) is exactly Theorem 2.1 and is paid by `<362.039/L`.

Thus the remaining object is a **punctured overlapping-leakage collar around a now-paid endpoint**, not the endpoint itself.

For completeness, when `beta>0`, r51 can be used with the actual ratio

`zeta=beta/||b||`.

With `tau_0=sqrt(3/8)`, `q_0=zeta tau_0/2`, and

`theta(zeta)=q_0/[4(1+q_0)]`,                                   (5.5)

if

`r<=theta(zeta)m`,                                               (5.6)

then the literal third-compound crossing yields

`||p_Q||_infinity
 <=6^(4/3) [beta m^2 tau_0/(32(1+q_0)^2)]^(-1/3),
 p_Q in C_0(R).`                                                 (5.7)

This is an actual estimate for every nonzero transverse puncture satisfying (5.6), but it is not target-uniform as `beta/L ->0`; no uniform-in-puncture claim is made. If (5.6) fails, the account04/B08 theorem is still available at the smaller actual scale `theta(zeta)m`, but its constant similarly deteriorates when `zeta->0`. That deterioration is precisely why the nonzero collar remains a real proof obligation rather than something that can be removed by continuity in matrix coefficients.

## 6. Why the next step is not a perturbation argument

Write the aligned skeleton

`A_0 = [[a,(Vc)^T],[Vc,V Lambda V^T]]`

and the exact residual

`R=A-A_0=[[0,w^T],[w,E]]`,

where `w` is orthogonal to `range(V)` and `E` is the child spectral tail. Even when `||R||op` is numerically small compared with `L`, the source laws have no moment or bounded-support assumption. Therefore this report does **not** delete `R`, couple `X^T R X` to a small random error, or claim density stability in operator norm. The live correction set explicitly forbids that shortcut.

The exact determinant-star (3.3) suggests the correct next mechanism: spend aggregate source-disjoint curvature while retaining the puncture `w,E` inside the analytic receiver. This is consistent with the newer cross-star/Witt work elsewhere in the fleet, which also shows that joint-density caps alone are insufficient once an overlapping cancellation variable is present.

## 7. New first unpaid implication

`QFORM-ALIGNED-ENDPOINT-PUNCTURED-CROSSSTAR-RECEIVER-v1`:

> In the state (5.1)-(5.3), with `(beta,r)!=(0,0)`, retain the full original product source and the nonzero overlapping terms `2H w^T X + X^T E X`. Use the exact endpoint cross-star mass `>=L^3/2` (or a stable replacement derived before reciprocal minor inversion) to prove a uniform `C/L` density bound, or route the puncture to an additional physical localized witness. No arbitrary-joint replacement and no small-random-quadratic deletion is allowed.

The exact endpoint itself is finished; target-scale child-third-spectrum leakage is finished modulo a concrete physical row witness; the remaining B08 obstruction is the nonzero punctured collar.

## 8. Continuity status

- Full target: **OPEN**.
- Full-target continuous representative: **OPEN**.
- Exact aligned endpoint Theorem 2.1: essential boundedness proved. Continuity is additionally proved in its exact-null `a=0`, child-leverage `<=1/2` subbranch by (2.5); continuity is not claimed for every nonzero `a` branch of (2.3).
- Designated partner diffuse-window branch (4.7): `C_0` continuity proved by the source theorem.
- r51 transverse puncture branch (5.7): `C_0` continuity proved by the source theorem.

The finite computations in `CHECK.py`/`CHECKS.txt` verify the determinant-star identities and constants as regression evidence only; the proof above is analytic.
