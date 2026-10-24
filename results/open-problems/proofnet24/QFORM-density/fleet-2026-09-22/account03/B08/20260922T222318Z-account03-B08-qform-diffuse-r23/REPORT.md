SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-22T22:23:18Z.
attacking: physicalize one row of the surviving Schur-minor tube so every localized leading singular vector is paid with the full nonzero tail retained, then force a strong ridge-diffuse certificate in the only remaining branch.

# account03/B08 r23 — one-sided physicalization of the Schur-flag tube and a sharp diffuse-ridge remainder

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control consumed:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREMS / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open: for arbitrary independent real coordinates with one-dimensional probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a target-valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, diagonal-coordinate, or post-rotation-independence assumption is introduced. Continuity is tracked separately.

This run changes mechanism from the preceding grouped-core / near-rank-two determinant-bank arguments. It does **not** perturbatively delete the small higher-rank tail. Instead, it conditions all but one residual **original coordinate on one side**, which forces an exact rank-two physical cross bank while retaining every coefficient of the nonzero tail in the surviving physical row. The complementary branch is then shown to be quantitatively ridge-diffuse at a fixed scale.

## 1. Fresh sources and correction boundary

The source control was refreshed immediately before publication. The later OWNER CONTROL remains revision `2026-09-22.15`; QFORM remains the sole research programme. The live corrections still forbid the false arbitrary-joint rank-three coarea claim, conditional-cap-as-independence, positive conditional projection-density moments, law-uniform pointwise quadratic-phase decay, worst-fiber supremum arguments, and perturbative deletion of a small quadratic coefficient under unrestricted supports.

The designated current-QFORM partner path `account04/B08` still has no completed handoff or report, so no partner theorem is fabricated. The compatible completed account04 theorem actually applied below is:

* account04/B18, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,  
  `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,  
  `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its dependence-safe outer-square kernel is used in Section 3 at an actual inequality.

Two completed same-programme inputs are also used literally:

1. account03/B06, `QFORM-EXACT-RANK2-CROSSBANK-L3-v1`,  
   `yspennstate/math-open-problems@1287456c9a709f8c3f117c23faa46e75f4560d01`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T194649Z-account03-B06-qform-r17/REPORT.md`.  
   If an original-coordinate cross bank has exact rank two and one active bank consists of exactly two physical coordinates, with two-singular-value product `Pi_2`, then its residual density satisfies
   
   `||p_R||_3 <= 3^(2/3) e^(1/3) Pi_2^(-1/3)`,                 (1.1)
   
   with arbitrary same-side quadratic-affine phases and outside conditioning retained. Combining (1.1) with account04/B18 gives
   
   `||p_Q||_infinity <= C_* |a|^(-1/2) Pi_2^(-1/4)`,           (1.2)
   
   where
   
   `C_*=(2^(4/3)+1) sqrt(3) e^(1/4)=7.8281191852... .`         (1.3)

2. account03/B06 r20, `QFORM-WEIGHTED-SCHUR-FLAG-RANK1-ENDPOINT-v1`,  
   `yspennstate/math-open-problems@` [the canonical r20 report path below],  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T215055Z-account03-B06-qform-r20/REPORT.md`.  
   It supplies the weighted Schur-flag representation used in Section 2 and identifies the exact-rank-one endpoint. The present run removes the **rank-one** requirement whenever its leading left singular vector is physically localized.

The B08 source immediately preceding this run is

`yspennstate/math-open-problems@d7add2eca585a9c871e910f4afdda02491944843`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T215031Z-account03-B08-qform-diffuse-r22/REPORT.md`.

It leaves a strict-higher-rank nonzero-pivot bicolop branch with a quantitatively factorized normalized incident-minor tube and explicitly forbids deleting its small spectral tail by moments or characteristic-function continuity.

## 2. Weighted Schur flag, with the full tail retained

Use the notation of the completed B06 r20 Schur flag. Let the left and right banks consist of disjoint ORIGINAL coordinates. Write the left bank as

`U=(U_0,u)`,                                                       (2.1)

so `U_0` and all components of `u` are genuinely independent cap-one variables. On the right put

`W=L V`,                                                           (2.2)

where `V` is the original cap-one product bank and

`s_min(L)>=g>0`.                                                   (2.3)

The residual cross interaction is described by

`Z=[[alpha,b^T],[c,D]]`, `alpha!=0`,                              (2.4)

and its Schur-minor matrix is

`M=alpha D-c b^T`.                                                 (2.5)

The determinant-one triangular changes

`x=U_0+c^T u/alpha`,
`y=W_0+b^T w/alpha`                                                (2.6)

give the exact algebraic identity

`U^T Z W = alpha x y + u^T(M/alpha) w`.                           (2.7)

No tail of `M` has been removed in (2.7).

The full ambient QFORM branch also contains the previously completed genuine ORIGINAL-coordinate outer square with coefficient `a!=0`. Once the residual in (2.7) has an `L^3` density, account04/B18 turns it into an essential `L^infinity` bound via (1.2).

## 3. New theorem: any quantitative physical row pays the entire nonzero tail

### Theorem 3.1 — `QFORM-SCHUR-FLAG-PHYSICAL-ROW-L3-v1`

In the setup (2.1)-(2.7), fix a residual **physical left coordinate** `k` and let

`m_k^T = e_k^T M`                                                 (3.1)

be the corresponding complete row of the Schur-minor matrix. If `m_k!=0`, then after conditioning all other residual left coordinates `u_l`, `l!=k`, the surviving original-coordinate cross bank has exact rank two and its two-singular-value product obeys

`boxed( Pi_2(C_k) >= g^2 ||m_k||_2. )`                           (3.2)

Consequently the residual law has an `L^3` density satisfying

`boxed(
 ||p_R||_3
 <=3^(2/3)e^(1/3) [g^2 ||m_k||_2]^(-1/3),
)`                                                               (3.3)

and, after the genuine outer square,

`boxed(
 ||p_Q||_infinity
 <= C_* |a|^(-1/2)[g^2 ||m_k||_2]^(-1/4),
)`                                                               (3.4)

with `C_*` from (1.3).

All other singular directions of `M`, however small or large, are retained inside the row `m_k`. All same-side quadratic terms, affine terms, outside coordinates and outside couplings allowed by the source scalar-square reduction remain present. The conclusion is absolute continuity plus essential boundedness; continuity is **not** asserted by this `L^3` plus dependent-square route.

### Proof

Condition every left residual original coordinate except `u_k`. The active left bank is then exactly the two ORIGINAL variables `(U_0,u_k)`. Terms containing conditioned coordinates become arbitrary affine or same-side phases, which are allowed by the exact-rank-two theorem.

In the sheared coordinates `(x,u_k)` and `(y,w)`, the active cross coefficient matrix is

`B_k = [[alpha,0],[0,m_k^T/alpha]]`.                              (3.5)

Undo only the deterministic right shear from (2.6). Relative to the original `W=(W_0,w)` coordinates the two active cross rows are

`r_0=(alpha,b^T)`,
`r_1=(0,m_k^T/alpha)`.                                            (3.6)

Their squared exterior area is the `2 x 2` Gram determinant

`det G_k
 =(alpha^2+||b||^2)(||m_k||^2/alpha^2)
   -(b^T m_k)^2/alpha^2`

`=||m_k||^2
  +[||b||^2||m_k||^2-(b^T m_k)^2]/alpha^2`

`>=||m_k||^2`.                                                    (3.7)

The actual right variables are `V`, with `W=LV`. Hence the physical cross matrix is obtained by multiplying these two rows by `L`. Since

`L L^T >= g^2 I`,                                                 (3.8)

we have in Loewner order

`C_k C_k^T >= g^2 G_k`.                                          (3.9)

Both sides are `2 x 2` positive semidefinite matrices. Since `m_k!=0`, `G_k` is positive definite, and determinant monotonicity under (3.9) gives

`det(C_k C_k^T) >= g^4 det G_k >= g^4 ||m_k||^2`.               (3.10)

Taking square roots proves (3.2). The active bank on the left consists of exactly two original physical coordinates, so the improved rank-two estimate (1.1) gives (3.3), uniformly in the conditioning. Average over the conditioned original coordinates to obtain the unconditional `L^3` residual bound.

Finally apply the completed account04/B18 dependence-safe square inequality exactly as compiled in (1.2). This gives (3.4). No independence between the residual and the translated square is asserted. QED.

### Why this is genuinely a nonzero-tail theorem

Theorem 3.1 makes **no rank assumption on `M`**. In particular the tail may have arbitrarily many nonzero singular values. It is not treated as a perturbation and is not dropped from the phase. Conditioning leaves the complete physical row `m_k` in the exact rank-two active cross bank, so every tail coefficient in that row is retained algebraically.

This directly avoids the source-valid small-tail obstruction: a tiny matrix coefficient can have an order-one phase effect on admissible translated or fragmented laws, but Theorem 3.1 never compares the law with the tail deleted.

## 4. Sharpening the surviving near-rank-one tube

In the current B06/B08 factorized survivor the normalized incident-minor matrix `M` obeys

`S:=||M||_F^2 > 1067/2000`,                                      (4.1)

and

`E_2(M):=sum_(mu<nu) s_mu(M)^2 s_nu(M)^2 < 1/4096`.             (4.2)

Let

`m=s_1(M)`,                                                       (4.3)

and write its SVD as

`M=m p q^T+T`,                                                    (4.4)

where `p,q` are unit leading singular vectors and `T` contains every remaining singular component. Then `p^T T=0` and `Tq=0`.

### Lemma 4.1 — `QFORM-BICOLOOP-RANK1-TUBE-SHARPEN-v1`

The source inequalities (4.1)-(4.2) imply the exact lower bound

`boxed(
 m^2 > x_0:=9092287/17072000 >1/2,
)`                                                               (4.5)

and the stronger relative-tail estimate

`boxed(
 ||T||_F/m <1/32.
)`                                                               (4.6)

The previously recorded `4.15%` tube can therefore be sharpened, in this exact source branch, to a `3.125%` Frobenius tube.

### Proof

Let `s_1=m>=s_2>=...` and write `S=sum s_nu^2`. Since

`sum s_nu^4 <= m^2 S`,                                           (4.7)

we have

`E_2(M)
 =[S^2-sum s_nu^4]/2
 >= S(S-m^2)/2`.                                                 (4.8)

Therefore

`m^2 > S-2(1/4096)/S`.                                          (4.9)

The right side is strictly increasing in `S>0`; substituting `S_0=1067/2000` gives

`m^2 > S_0-2(1/4096)/S_0
     =9092287/17072000
     =0.5325847586...>1/2`,                                     (4.10)

which proves (4.5).

Now put `tau^2=||T||_F^2=sum_(nu>=2)s_nu^2`. Since

`E_2(M) >=m^2 tau^2`,                                           (4.11)

(4.2) and (4.5) imply

`tau^2/m^2
 <(1/4096)/m^4
 <(1/4096)/(1/2)^2
 =1/1024`.                                                       (4.12)

Taking square roots proves (4.6). QED.

## 5. Localized-or-diffuse dichotomy for the leading Schur-minor channel

The exact SVD (4.4) gives rowwise

`||e_k^T M||^2
 =m^2 p_k^2 + ||e_k^T T||^2`,                                   (5.1)

because `Tq=0`. Hence

`||e_k^T M|| >=m|p_k|`.                                         (5.2)

### Corollary 5.1 — `QFORM-SCHUR-FLAG-ONEQUARTER-LOCALIZED-CLOSURE-v1`

If

`max_k |p_k| >=1/4`,                                             (5.3)

then the whole nonzero-tail branch is paid. In the live normalization `g=gamma/16`, Theorem 3.1 and (4.5) give

`boxed(
 ||p_Q||_infinity
 <48 / sqrt(|a| gamma).
)`                                                               (5.4)

No rank-one approximation is made in proving (5.4).

### Proof

Choose `k` satisfying (5.3). By (5.2),

`||m_k|| >=m/4`.                                                 (5.5)

Insert (5.5) into (3.4) and use `g=gamma/16`:

`||p_Q||_infinity
 <=4 C_* (m/4)^(-1/4)/sqrt(|a|gamma)`.

Since `m^2>x_0` from (4.5), the dimensionless prefactor is at most

`4 C_* sqrt(2) x_0^(-1/8)
 =47.9108445785...<48`.                                         (5.6)

This proves (5.4). QED.

The contrapositive is the useful diffuse output: if the localized closure (5.4) does not apply, then

`boxed( max_k p_k^2 <1/16. )`                                   (5.7)

Thus every still-unpaid Schur-minor tube has a genuinely delocalized leading **physical-left** singular vector.

## 6. New quantitative ridge certificate in the unpaid diffuse branch

The small tail can now be used only as a **deterministic ridge certificate**, not as a perturbatively deleted random phase.

Define the ridge operator of the complete Schur-minor matrix `M` at scale

`eta=m/sqrt(32)` by

`K_eta(M)=MM^T(eta^2 I+MM^T)^(-1)`.                              (6.1)

### Theorem 6.1 — `QFORM-SCHUR-MINOR-DIFFUSE-RIDGE-CERTIFICATE-v1`

In the unpaid branch (5.7), together with (4.6),

`boxed(
 max_k (K_eta(M))_kk <97/1056 <0.092,
)`                                                               (6.2)

while its effective ridge dimension satisfies

`boxed(
 theta_eta(M):=tr K_eta(M) >32/33 >0.969.
)`                                                               (6.3)

These estimates retain **all** singular directions of `M`.

### Proof

In the SVD basis, the leading ridge eigenvalue is

`lambda_1=m^2/(eta^2+m^2)=32/33`.                               (6.4)

For every tail singular value `s_nu`,

`s_nu^2/(eta^2+s_nu^2)
 <=s_nu^2/eta^2
 =32 s_nu^2/m^2`.                                               (6.5)

Hence the entire tail contribution to the trace is, using (4.6),

`sum_(nu>=2) lambda_nu
 <32 ||T||_F^2/m^2
 <1/32`.                                                         (6.6)

For any physical residual row `k`, (5.7) and (6.6) give

`(K_eta)_kk
 <=(32/33)p_k^2 +sum_(nu>=2)lambda_nu`

`<(32/33)(1/16)+1/32`
`=2/33+1/32`
`=97/1056`,                                                      (6.7)

which is (6.2). The trace is at least the leading eigenvalue (6.4), proving (6.3). QED.

### Interpretation

The formerly vague `near rank one but nonzero tail` state has now split cleanly:

* if the leading Schur-minor left singular vector has one coefficient at least `1/4`, the full tail is retained and the branch is paid by `<48/sqrt(|a|gamma)`;
* otherwise the **complete** Schur-minor channel is extremely ridge-diffuse on the physical left: leverage `<0.092`, effective ridge dimension `>0.969`, and relative Frobenius tail `<1/32`.

This is exactly the kind of source-valid delocalization certificate needed by B08. It does not say the tail is probabilistically negligible.

## 7. What remains: a one-exact-channel plus one-ridge-channel compiler

The weighted Schur flag (2.7) already contains one exact bilinear channel `alpha x y`. The diffuse branch of Theorem 6.1 supplies almost one further ridge dimension in the `u^T(M/alpha)w` channel. The first unpaid analytic implication is therefore substantially narrower than the r22 generic grouped-fiber-tail problem:

> **`QFORM-WEIGHTED-EXACT1-PLUS-RIDGE1-L3-v1` — OPEN.**  
> In the source-valid weighted Schur-flag representation (2.7), combine the exact physical/weighted channel `alpha x y` with the complete Schur-minor ridge certificate (6.2)-(6.3) to prove an `L^3` residual density uniformly in the dimensions and in the right preconditioner `L` under only `s_min(L)>=g`. The proof must spend original-coordinate product structure before any curved/fiber trace. It may not condition on spectral fibers and assert density caps, and it may not delete the `T` phase using its small coefficient.

This compiler is now the natural diffuse counterpart to Theorem 3.1. The numerical geometry is favorable: the second channel already has physical-left ridge leverage below `0.092`, far inside every one-dimensional Hausdorff--Young collar used elsewhere in the fleet, and its effective dimension exceeds `0.969`; the missing issue is the **weighted right-bank dependence** created by `W=LV`, not a shortage of curvature on the left.

## 8. Status and continuity

**Proved in this run:**

1. `QFORM-SCHUR-FLAG-PHYSICAL-ROW-L3-v1`, equations (3.2)-(3.4): one quantitative original physical residual row closes the entire higher-rank tail without perturbing it away.
2. `QFORM-BICOLOOP-RANK1-TUBE-SHARPEN-v1`: the live factorized tube improves to `||T||_F/m<1/32` and `m^2>9092287/17072000`.
3. `QFORM-SCHUR-FLAG-ONEQUARTER-LOCALIZED-CLOSURE-v1`: if the leading left singular vector has any coefficient at least `1/4`, then `||p_Q||_infinity<48/sqrt(|a|gamma)`.
4. `QFORM-SCHUR-MINOR-DIFFUSE-RIDGE-CERTIFICATE-v1`: failure of the localized branch forces `max diag K_eta<97/1056` and `tr K_eta>32/33` at `eta=m/sqrt(32)`.
5. The completed account04/B18 dependence-safe square theorem is applied in the actual inequality (3.4), not merely cited.

**Still open:** the unrestricted universal QFORM conjecture; a universal lower bound on the structural product `|a|gamma`; the weighted exact-one-plus-ridge-one compiler in Section 7; and the full continuous-density conclusion. The new branches proved via `L^3` plus the dependent square establish absolute continuity and essential boundedness only.

No source-matching published theorem was found that ends this exact scope. No counterexample to QFORM is claimed.
