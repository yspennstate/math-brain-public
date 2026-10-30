# fleet01/B20 — Schur spectral-window closure inside the heavy-pivot residual

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner revision: `2026-09-22.5`  
Run: `20260922T152039Z-fleet01-B20-QFORM-r11`  
Assignment: Proof closure and keeper / SYNTHESIS  
Classification: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The target is the unrestricted one: for arbitrary dimension, arbitrary independent real coordinates with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is separate.

This run does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, fiber suprema, a generic conditional-density-cap surrogate for independence, a fixed physical principal-minor dichotomy, a fixed rank-three cross-cut dichotomy, or an absolute phase-Wiener criterion. The live correction inbox was refreshed before publication.

## 2. Completed fleet02/B20 result actually consumed

The newest completed assigned-partner result found before publication is fleet02/B20 run `20260922T145947Z-fleet02-B20-QFORM-r12`, canonical source

`yspennstate/math-open-problems@298793085cb203d47861ace564bcc5f74d647368`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T145947Z-fleet02-B20-QFORM-r12/REPORT.md`, report blob `2e2bb4c9b583f94b48fbf5952f1183dbff92e17f`.

Write a physical scalar pivot as

`A=[[a,b^T],[b,C]]`, `a!=0`,

and set

`S=C-bb^T/a`, `K=||b||_2/|a|`, `tau=(1+K)^(-2)`.

That completed report proves:

1. `s_2(S)>=tau` whenever `s_3(A)>=1`;
2. if `|a|<tau`, then actually `s_3(S)>=tau`;
3. if `P=1_{|A|>=1}`, `c_i=P_ii>=1/64`, and `K<=1`, then `|a|>=1/sqrt(128)` and `tau>=1/4`;
4. for every proposed cap `C>=C0:=512 sqrt(2)`, a minimum-dimensional counterexample in this heavy diagonal-dominated branch cannot have `|a|<tau`.

Thus **in a minimum-dimensional counterexample to the cap `C0`**, every heavy diagonal-dominated pivot under consideration satisfies the actual inequalities

`boxed: |a|>=tau>=1/4,   s_2(S)>=tau.`                         (2.1)

This run uses (2.1) numerically in the final density estimate below; the partner result is not merely cited.

## 3. Additional completed analytic input: ridge effective dimension plus one physical square

The ridge-window report

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

at `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`
proves for any original-coordinate cross block `B` and `gamma>0`

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta_gamma=tr K_gamma`,

and the ridge-leverage perturbation estimate

`max_i (K_gamma)_ii <= (sqrt(ell)+eta/gamma)^2`                (3.1)

when `B=B0+F`, `||F||<=eta`, and the ordinary range projection of `B0` has diagonal at most `ell`.

The newest completed fleet02/B02 theorem, run `20260922T153908Z-fleet02-B02-qform-auto11-7613470a`, canonical source

`yspennstate/math-open-problems@cae1a86397cc15e6999c754c6657576f0d6abebd`

at `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T153908Z-fleet02-B02-qform-auto11-7613470a/REPORT.md`, proves the dependence-safe square-pivot ridge theorem. Its concrete `q=1` corollary is:

> if a Schur-remainder physical cross block `B` has two singular values at least `sigma`, `gamma=sigma/sqrt(2)`, and `max diag K_gamma<=1/2`, then for a genuine original-coordinate completed square with coefficient `d!=0`,
>
> `||p_Q||_infinity < 19.470 / sqrt(|d| sigma).`               (3.2)

The proof preserves original-coordinate product provenance. In particular it applies to the exact completion

`Q=a(X_i+b^T Y/a)^2 + Y^T S Y`,                              (3.3)

because `X_i` is independent of the remaining original coordinates; the translated square variable retains the required conditional cap-one interface without any rotated-independence claim.

Fleet02/B02 also independently passed the free-regularizer/ridge Fourier part of the ridge-window extension; its review explicitly does not certify the separate MSS spectral-window application. The argument below supplies only the standard algebraic use of that partition and keeps the full target marked OPEN.

## 4. New theorem — quantitative Schur spectral-window closure

### Theorem `QFORM-HEAVY-PIVOT-SCHUR-WINDOW-v1`

Assume `A` satisfies `s_3(A)>=1`, and let `i` be a physical pivot satisfying

`c_i=(1_{|A|>=1})_ii>=1/64`, `K=||b||/|a|<=1`.

Suppose we are in a minimum-dimensional counterexample to the proposed universal cap

`C0=512 sqrt(2)`.

Let `S` and `tau` be as above, and define the **quantitative Schur spectral-window projection**

`P_tau = 1_{ {|S| >= tau/64} }.`                               (4.1)

Then necessarily

`boxed: max_j (P_tau)_jj > 1/32.`                              (4.2)

Equivalently, if the window (4.1) is diffuse in physical coordinates, then the full quadratic form has the explicit stronger bound

`boxed: ||p_Q||_infinity < 180 < C0.`                          (4.3)

This improves the preceding heavy-pivot collar, which only forced localization of the projection onto the **entire range** of `S`; arbitrary tiny nonzero Schur directions below `tau/64` are now harmless.

### Proof

By the completed fleet02/B20 result, a minimum-dimensional counterexample in this branch satisfies (2.1):

`|a|>=tau>=1/4`, `s_2(S)>=tau`.                                (4.4)

Assume for contradiction that

`max_j (P_tau)_jj <=1/32`.                                     (4.5)

Decompose the Schur matrix spectrally as

`S=S_H+E`,

where `S_H` keeps exactly the eigendirections with `|lambda|>=tau/64`. Then

`||E||op < tau/64`.                                             (4.6)

Write `S_H=U Lambda U^T` with `U^TU=I`. Condition (4.5) says every physical row `u_j` satisfies

`||u_j||^2 <=1/32`.                                             (4.7)

The two singular values of `S` which are at least `tau` belong to this window, so

`s_2(Lambda)>=tau`.                                             (4.8)

Apply the standard two-part MSS frame partition to `U`. There is an original-coordinate partition `I,J` for which

`(7/32) I <= U_I^T U_I, U_J^T U_J <=(25/32) I`.                (4.9)

For the high-window physical cross block

`B0=S_H[I,J]=U_I Lambda U_J^T`,

(4.9) gives

`s_2(B0) >= (7/32) s_2(Lambda) >=7 tau/32.                     (4.10)

Moreover `range(B0)=range(U_I)`, and its ordinary physical row leverage is bounded by

`e_j^T P_range(B0)e_j`
` =u_j^T (U_I^T U_I)^(-1)u_j`
` <=(32/7)(1/32)=1/7.`                                         (4.11)

Now let

`B=S[I,J]=B0+F`, `F=E[I,J]`.

By (4.6), `||F||<=tau/64`, so Weyl's inequality and (4.10) yield

`s_2(B) >=7tau/32-tau/64 =13tau/64 =: sigma`.                  (4.12)

Choose

`gamma=sigma/sqrt(2)=13tau/(64sqrt(2))`.                       (4.13)

The ridge perturbation estimate (3.1), with `ell=1/7` and `eta=tau/64`, gives

`max_j (K_gamma)_jj`
` <=(1/sqrt(7)+(tau/64)/gamma)^2`
` =(1/sqrt(7)+sqrt(2)/13)^2.`                                  (4.14)

This is strictly below `1/2`. For an exact elementary verification,

`1/sqrt(7)<2/5`, `sqrt(2)/13<1/9`,

so the right side of (4.14) is below

`(2/5+1/9)^2=(23/45)^2=529/2025<1/2.`                          (4.15)

Also, because `B` has two singular values at least `sigma`,

`theta_gamma`
` >=2 sigma^2/(gamma^2+sigma^2)`
` =4/3>1`.                                                      (4.16)

Thus all hypotheses of the completed fleet02/B02 square-pivot ridge corollary (3.2) hold for the completed square (3.3). Consequently

`||p_Q||_infinity <19.470/sqrt(|a| sigma)`
`                  <20/sqrt(|a| sigma).`                       (4.17)

Now the **fleet02/B20 collar is used quantitatively**. By (4.4),

`|a| sigma >=(1/4)*(13/256)=13/1024`.                          (4.18)

Substitution into (4.17) gives

`||p_Q||_infinity <20 sqrt(1024/13)=640/sqrt(13)<180`,          (4.19)

because `sqrt(13)>18/5`. Since `180<512 sqrt(2)=C0`, (4.19) contradicts minimal-counterexample status. Hence (4.2) must hold. QED.

## 5. Immediate new structural currency: a second Schur row has universal energy

The window localization (4.2) is not merely qualitative. Choose `j` with `(P_tau)_jj>1/32`. Since every eigenvalue in the window has modulus at least `tau/64`, spectral calculus gives

`(S^2)_jj >= (tau/64)^2 (P_tau)_jj > tau^2/131072.`            (5.1)

But

`(S^2)_jj=S_jj^2+||S_{j,-j}||_2^2`.                            (5.2)

Therefore

`boxed: max{|S_jj|, ||S_{j,-j}||_2} > tau/512 >=1/2048.`       (5.3)

So every surviving heavy diagonal-dominated minimum-counterexample branch contains, in the exact Schur residual and in original physical coordinates, a **second quantitatively nontrivial row**. The alternative is explicit:

- a second physical Schur diagonal pivot `|S_jj|>tau/512`, or
- a second physical Schur cross bank `||S_{j,-j}||>tau/512`.

This is the first source-valid row-energy certificate obtained after replacing entire-range localization by spectral-window localization. It is intended as packet-extraction currency; no claim is made that either alternative alone already closes the full theorem.

## 6. Conditional end-to-end assembly after this run

Take a minimum-dimensional counterexample to the candidate cap `C0=512sqrt(2)`.

Existing source-valid work closes the near-diagonal/high-stable-rank regimes and leaves a low-effective-rank residual. The current heavy-row analysis then splits as follows.

1. If a heavy large-spectral row is diagonal-dominated and `|a|<tau`, completed fleet02/B20 descends dimension, contradiction.
2. If it is diagonal-dominated, `|a|>=tau`, but its Schur window `|S|>=tau/64` is diffuse, Theorem 4 above gives `||p_Q||infinity<180`, contradiction.
3. Therefore every surviving heavy diagonal-dominated row has the quantitative localized-window certificate (4.2) and row-energy dichotomy (5.3).
4. Cross-dominated heavy rows remain assigned to the product-preserving aggregate/bank mechanisms already developed by the fleet.
5. The large-spectral-window diffuse branch for the original matrix is independently covered by the ridge-window theorem under its explicit leverage hypothesis; it is not silently assumed from the bare target.

Thus the remaining full-target structural implication is narrower than the previous generic `localized Schur` label: in the heavy diagonal-dominated residual one may assume simultaneously

`|a|>=tau>=1/4`,
`s_2(S)>=tau`,
`max diag 1_{|S|>=tau/64}>1/32`,
`max{|S_jj|,||S_{j,-j}||}>tau/512` for some physical `j`.

The next unpaid step is to convert this **two-level physical localization** into one of the already-paid product-compatible packets: a scalar plus two-sided Schur-corrected mixed packet, a disjoint aggregate hyperbolic-square packet, or a ridge/separator packet. The required conversion must keep the same original-coordinate bank variables through their contaminating quadratic terms; conditioning on a transformed complement and reusing a marginal cap is prohibited.

## 7. Status and nonclaims

- Full QFORM target: `OPEN / NOT PROVED`.
- `QFORM-HEAVY-PIVOT-SCHUR-WINDOW-v1`: `PROVED` subject only to the cited completed supporting theorems.
- Fleet02/B20 result was consumed in the actual inequalities (4.4) and (4.18).
- New movement: entire-range Schur localization is replaced by localization only of eigenvalues `|lambda(S)|>=tau/64`, and a surviving minimum counterexample gains the second-row energy certificate (5.3).
- No target-valid counterexample is claimed.
- Continuity is not claimed for the new branch; the square-pivot endpoint used here yields essential boundedness.
- No computation is used as proof; all constants above are symbolic inequalities.

## 8. Source pins

- fresh brain control/correction snapshot immediately before publication: `yspennstate/math-research-brain@bd43f8ef803327cd07b5e8b07c747bf810a0af3f`, owner revision `2026-09-22.5`;
- newest completed assigned partner fleet02/B20: `yspennstate/math-open-problems@298793085cb203d47861ace564bcc5f74d647368`, report blob `2e2bb4c9b583f94b48fbf5952f1183dbff92e17f`;
- ridge-window theorem: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, report blob `1241fa7ba9a36a91bc75f047677f2daac764c2bf`;
- completed fleet02/B02 square-pivot ridge theorem and analytic ridge review: `yspennstate/math-open-problems@cae1a86397cc15e6999c754c6657576f0d6abebd`, report blob `f459f8c9960baafd28a5878b041c0805c9d2c1af`;
- completed fleet03/B20 scalar-pivot/Schur source used by the partner chain: `yspennstate/math-open-problems@7530e8c6ffd7284eb9c8acf1d79f36c335bf4fd6`.
