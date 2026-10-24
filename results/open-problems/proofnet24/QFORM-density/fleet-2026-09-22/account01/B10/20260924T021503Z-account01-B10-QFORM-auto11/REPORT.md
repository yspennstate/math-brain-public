SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T02:15:03Z.
attacking: the punctured near-null one-sided mixed-bank chamber; retain the clean transverse square bank and pay the nonzero hub Rayleigh coefficient by an exact discriminant cancellation rather than by perturbation.

# account01/B10 — punctured one-sided mixed-bank closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control revision:** `2026-09-22.15`  
**Run:** `20260924T021503Z-account01-B10-QFORM-auto11`  
**Status:** `NEW_ANALYTIC_BRANCH / EXACT_DISCRIMINANT_CANCELLATION / PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope

Let `U` be an `n x 3` matrix with orthonormal columns and let `M` be a real symmetric invertible `3 x 3` matrix with

`min_j |lambda_j(M)| >= 1`.

Put `A=UMU^T`, so this is an exact-rank-three target. Assume one ORIGINAL physical coordinate is a hub row

`u_0 = sqrt(h) e_1`, `0<h<=1`,

and that the remaining ORIGINAL coordinates split into two disjoint banks `B,C` with

`u_i=t_i e_1+y_i e_2`, `i in B`,

`u_j=w_j e_3`, `j in C`.

Thus the longitudinal leakage may be arbitrarily entangled, through the same original variables, with the first transverse scalar; the second transverse scalar is carried by a disjoint clean original-coordinate bank. No independence between the two linear observables of bank `B` is assumed.

Choose `e_2` in the direction of the transverse component of `Me_1`; then

`M = [[a,s,0],[s,b,c],[0,c,d]]`,

where `a=e_1^TMe_1`. This report treats every `|a|<1`, including the punctured near-null collar. Let

`D=|det M|`.

The theorem proved below is

`||p_Q||_infinity <= 51.2 [h D |d|]^(-1/4) <= 51.2 [h(1-|a|)]^(-1/4)`.      (1.1)

In particular, in the live ultra-collar

`h>4095/4096`, `|a|D<2^(-12)`, `D>=1`,

one has

`||p_Q||_infinity < 51.207`.                                             (1.2)

This is an essential-density statement. Continuity is not claimed here.

## 2. Product provenance and Parseval identities

Let the physical inputs be independent with densities at most one. Write

`H=X_0`,

`T=sum_{i in B} t_i X_i`,

`Y=sum_{i in B} y_i X_i`,

`W=sum_{j in C} w_j X_j`.

Because `B` and `C` are disjoint ORIGINAL-coordinate banks, `W` is genuinely independent of `(H,T,Y)`. The pair `(T,Y)` is not declared independent.

Parseval, `U^TU=I_3`, gives

`sum_B t_i^2 = 1-h`,

`sum_B y_i^2 = 1`,

`sum_B t_i y_i = 0`,

`sum_C w_j^2 = 1`.                                                       (2.1)

The active spectral coordinates are

`Z=sqrt(h)H+T`, `Y`, `W`,

and hence

`Q = a Z^2 + 2s ZY + bY^2 + 2cYW + dW^2`.                              (2.2)

No rotation of the random variables has been used to create independence.

## 3. The source theorem used, with its exact gate

The proved source theorem used here is Theorem 5.1(b) of

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_with_diagonal/REPORT.md`.

Its relevant statement is this. If the leaves split into disjoint sets `S,T`,

`V=<v,X_S>`, `L=<w,X_T>`,

and

`R = alpha X_h^2 + 2X_h(L+beta) + lambda (V-F)^2 + C`,

where `F` is any function of `X_T` and `C` is any quadratic polynomial in `X_T`, then

`||p_R||_infinity <= 25.6 |lambda|^(-1/2)|v|^(-1) alpha_1(Delta_C)^(1/2)`,  (3.1)

with

`Delta_C=(L+beta)^2-alpha C`,

and

`alpha_1(S)=sup_{r,u>0} P(|S-r|<=u)/sqrt(u)`.

The proof conditions only on original-coordinate banks. It does not use post-rotation independence. This source report is explicitly partial globally; only the stated Theorem 5.1(b) is used here.

## 4. Exact completion and the cancellation

Expand (2.2) in the genuine hub variable `H`:

`Q = ah H^2 + 2 sqrt(h) H(aT+sY)`

`    + aT^2+2sTY+bY^2+2cYW+dW^2`.                                      (4.1)

We will first show `d != 0`; this follows from the spectral estimate in Section 6 below. Complete the `W` square:

`dW^2+2cYW = d(W+(c/d)Y)^2 - (c^2/d)Y^2`.                              (4.2)

Therefore (4.1) is exactly in the source form with

`X_h=H`,

`alpha=ha`,

`L=sqrt(h)(aT+sY)`,

`lambda=d`,

`V=W`, `|v|=1`,

`F=-(c/d)Y`,

`C_B=aT^2+2sTY+(b-c^2/d)Y^2`.                                         (4.3)

The discriminant quantity in (3.1) now collapses exactly:

`Delta_C = L^2 - ha C_B`

`= h[(aT+sY)^2-a(aT^2+2sTY+(b-c^2/d)Y^2)]`

`= h[s^2-ab+ac^2/d]Y^2`

`= - h (det M/d) Y^2`.                                                  (4.4)

Every term containing the same-source leakage `T` cancels. This is the main identity of the run. It is exact and does not use smallness of `a`, moments, support control, or any independence between `T` and `Y`.

## 5. A sharp enough alpha_1 payment

By (2.1), the coefficient vector of `Y` has Euclidean norm one. The scalar Ball--Rogozin projection bound gives

`||p_Y||_infinity <= sqrt(2)`.                                          (5.1)

For any scalar variable with density cap `K`, and any `kappa>0`, the set

`{y: |kappa y^2-r|<=u}`

has Lebesgue measure at most

`2 sqrt(2u/kappa)`                                                       (5.2)

for every `r` and `u>0`: if `r>=u` it is the union of two symmetric intervals and its length is maximized at `r=u`; if `0<=r<u`, it is contained in `[-sqrt((r+u)/kappa),sqrt((r+u)/kappa)]`; negative `r` is easier. Consequently

`alpha_1(kappa Y^2) <= 2 sqrt(2) K / sqrt(kappa)`.                       (5.3)

Using `K=sqrt(2)` and (4.4),

`alpha_1(Delta_C) <= 4 sqrt(|d|/(hD))`.                                 (5.4)

Substitute (5.4) into (3.1):

`||p_Q||_infinity`

` <= 25.6 |d|^(-1/2) [4 sqrt(|d|/(hD))]^(1/2)`

` = 51.2 [hD|d|]^(-1/4)`.                                               (5.5)

This proves the first inequality in (1.1).

## 6. Spectral cancellation: the small transverse square cannot occur here

Because every singular value of `M` is at least one,

`||M^{-1}|| <= 1`.                                                       (6.1)

Also, in dimension three,

`||M|| <= D`,                                                            (6.2)

because `D` is the product of the three singular values and the other two singular values are at least one.

Let

`C_11=bd-c^2`.

The inverse cofactor identity gives

`(M^{-1})_11=C_11/det M`,

hence by (6.1)

`|C_11| <= D`.                                                           (6.3)

Expanding the determinant,

`det M = aC_11-s^2 d`.                                                   (6.4)

Therefore, for `|a|<1`,

`s^2 |d| >= D-|a||C_11| >= D(1-|a|) >0`.                               (6.5)

In particular `d!=0`, retrospectively justifying (4.2). Moreover `s<=||Me_1||<=||M||<=D`, so

`D|d| >= D^2(1-|a|)/s^2 >= 1-|a|`.                                     (6.6)

Combining (5.5) and (6.6) gives the second inequality in (1.1):

`||p_Q||_infinity <= 51.2 [h(1-|a|)]^(-1/4)`.                           (6.7)

For the live ultra-collar, `|a|D<2^(-12)` and `D>=1` imply `|a|<1/4096`, while `h>4095/4096`. Hence

`h(1-|a|) > (4095/4096)^2`,

so

`||p_Q||_infinity < 51.2 sqrt(4096/4095) < 51.207`.                      (6.8)

No reciprocal small physical minor appears.

## 7. Completed account02/B10 partner result applied to an actual inequality

The newest completed designated partner result available at publication time is

`yspennstate/math-open-problems@d11a83e445576f8563997083670387aa18a331e5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260924T001342Z-account02-B10-nearcoloop-r11/REPORT.md`.

Its Theorem 4.1 closes the exact-null (`a=0`) version of exactly the one-mixed-bank geometry above. It proves, for `h>63/64`,

`||p_Q||_infinity <= 8*2^(1/4) h^(-1/4) < 9.552`.                       (7.1)

This is applied here as the endpoint inequality for the same chamber. The present argument supplies the punctured extension `0<|a|<1`, and in particular the whole nonzero ultra-collar under the same one-clean-square-bank geometry, at the coarser universal constant (6.8).

The partner theorem requires genuine independence only for the clean square bank, which is exactly the original-coordinate separation in (2.1). No conditional-cap-as-independence shortcut is used.

## 8. What this does and does not close

This result eliminates a genuine punctured-hub instability in the one-sided mixed-bank chamber: a nonzero hub Rayleigh coefficient is not paid by continuity, a moment estimate, or a small-coefficient perturbation. It is paid algebraically by the exact discriminant cancellation (4.4), followed by a source-valid hub-with-diagonal composition theorem.

The generic exact-rank-three problem remains open. Two debts survive:

1. **bidirectional mixed-bank overlap:** both transverse banks may carry longitudinal leakage, so there need not be a clean square bank on disjoint original coordinates;
2. **fully generic punctured near-null geometry:** after selecting a heavy row, physical rows need not split into the two-plane bank plus clean transverse bank assumed here.

Those are source-provenance problems, not smallness problems. The correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` prevents replacing them by abstract conditional density caps.

The next target is therefore

`QFORM-PUNCTURED-BIDIRECTIONAL-MIXED-BANK-DISCRIMINANT-v1`:

retain the exact cancellation in the hub discriminant while deriving the required square-root profile when the transverse square itself shares original coordinates with the second leakage observable. This is precisely the overlap case left open by both the completed partner theorem and the hub-with-diagonal source theorem.

## 9. Status and integrity

- full arbitrary exact rank three: **OPEN**;
- full owner QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**;
- continuity for this new punctured branch: **NOT CLAIMED**;
- no Gaussian, moment, compact-support, connected-support, log-concavity, or diagonal-basis assumption was introduced;
- no spectral projected coordinates were declared independent;
- all independence used is traced to disjoint ORIGINAL-coordinate banks;
- no Monte Carlo or numerical extremality claim is used in the proof.

Changed-file review for this report: one private mathematical Markdown file under the authorized account01/B10 run root; manual fallback privacy review found no credentials, scheduler IDs, signed URLs, machine paths, personal data, or unrelated material. No public release or permission change was made.
