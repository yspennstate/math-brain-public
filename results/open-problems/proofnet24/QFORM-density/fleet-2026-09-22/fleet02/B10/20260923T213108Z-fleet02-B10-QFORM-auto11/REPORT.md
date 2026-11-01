SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-23T21:31:08Z.
attacking: the exact-rank-three hybrid/near-null physical direction; consume the ruled-side theorem on its paid side and test endpoint-stable gluing on the genuine two-sheet side without losing original-coordinate product provenance.

# fleet02/B10 — a deep-collar two-sheet obstruction to absolute-discriminant gluing

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: rank-three coupled case, complementary constructions/source-valid counterexamples.
Status: `ESSENTIAL_SOURCE_RESULT_APPLIED / EXPLICIT_INTERMEDIATE-ROUTE_COUNTEREXAMPLE / SPECIAL-FAMILY-UNIFORMLY-PAID / FULL_QFORM_OPEN`.

Fresh owner control during the run remained QFORM-only, revision `2026-09-22.15`. The full unrestricted theorem is not claimed. No independence after spectral rotation is used anywhere below: every independence assertion is between disjoint ORIGINAL-coordinate banks.

## First unpaid implication

`QFORM-NEARCOLOOP-TWOSHEET-JOINT-BANK-GLUING-v2`.

In the exact-rank-three near-coloop collar

`A=RMR^T`, `R^TR=I_3`, `sigma_min(M)>=1`,
`u_0=sqrt(c)e`, `rho=1-c ->0`, `|e^TMe|->0`,
`sum t_j^2=rho`, `sum t_jp_j=0`, `sum p_jp_j^T=I_2`,

with all surviving transverse leaf leverages `<1/61`, prove a uniform density bound on the minority-sign/two-sheet side by keeping the hub jointly with transverse ORIGINAL-coordinate product smoothing. It is not enough to condition the hub and then bound the absolute inverse-square-root discriminant receiver, and it is not enough to pay the positive-leakage projected-crossing estimate `O(rho^(-1/6))`. The construction below shows the first proposed shortcut diverges logarithmically even in a family whose actual density is uniformly bounded by a completed source theorem.

## 1. A target-valid deep near-coloop family

Fix `m=64`. For a parameter

`0<eta<1/(64*257)=1/16448`,

put `c=1-eta`, `rho=eta`, and define a Parseval frame in `R^3` by the ORIGINAL physical rows

`u_0=sqrt(c)e_1`,
`u_1=sqrt(eta)e_1`,
`u_2,...,u_65=e_2/8`,
`u_66,...,u_129=e_3/8`.

Thus

`sum_i u_i u_i^T=I_3`.

Let

`M_eta = [[eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]]`

and `A_eta=R_eta M_eta R_eta^T`. The `2x2` leading block has characteristic polynomial

`lambda^2-eta lambda-(1+eta)=(lambda-(1+eta))(lambda+1)`,

so the three nonzero eigenvalues of `A_eta` are exactly

`{1+eta,-1,1}`.                                                     (1.1)

This is therefore an exact target form for every `eta>0`.

The hub is genuinely in the partner's near-coloop collar:

`c>63/64`, `rho=eta<1/64`,
`e_1^T M_eta e_1=eta<1/16`,
`|(A_eta)_{00}|=c eta<1/64`.                                          (1.2)

Every leaf transverse leverage is either zero or

`||p_j||^2=1/64<1/61`.                                                (1.3)

Hence the family survives the fleet03/B10 r26 `1/61` large-transverse-leaf payment; it is precisely in the diffuse positive-leakage chamber where that report invokes projected crossing.

Choose independent ORIGINAL source coordinates as follows. On the hub/longitudinal bank take `X_0,X_1 ~ Uniform[0,1]`; on the `e_2` bank take 64 iid `Uniform[-1/2,1/2]`; on the `e_3` bank take 64 iid `Uniform[1,2]`. Every one-dimensional density has cap one.

Define the three disjoint-bank aggregates

`Z=sqrt(c)X_0+sqrt(eta)X_1`,
`Y=(1/8) sum_{i=2}^{65} X_i`,
`W=(1/8) sum_{i=66}^{129} X_i`.

Because these are functions of disjoint ORIGINAL coordinate banks, `Z,Y,W` are genuinely independent. The quadratic output is exactly

`Q_eta = eta Z^2 + 2 sqrt(1+eta) ZY + W^2`.                            (1.4)

No post-rotation independence has been asserted.

## 2. Completed source results pay the actual family

### 2.1 Ruled one-sheet theorem: a real inequality

Use the completed ruled-level-set theorem in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For a signature `(2,1)` rank-three form with positive eigenvalues `lambda_1,lambda_2` and negative magnitude `mu`, that theorem gives for every majority-sign level `s>=0`

`p_Q(s) <= (lambda_1 lambda_2 mu)^(-1/2)
            int_0^(2pi) [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta
         <= pi sqrt(2)`.

For (1.1), `lambda_1=1+eta`, `lambda_2=mu=1`; consequently

`boxed: p_{Q_eta}(s) <= pi sqrt(2) < 4.443,  s>=0.`                    (2.1)

This is an actual application of the required source theorem, not a restatement. Its proof uses product-measure marginals along rulings and does not declare the spectral coordinates independent.

### 2.2 The same source gives a global uniform bound on this special family

The one-dimensional projection density of `Y` and of `W` is at most `sqrt(2)` by the Rogozin/Ball projection estimate used in the same source. Conditioning on `X_1` gives

`||p_Z||_infinity <= c^(-1/2) < sqrt(64/63) < sqrt(2)`.                (2.2)

Let `D=diag(K_Z,K_Y,K_W)` with these three caps. Rescale `(Z,Y,W)` to `(K_Z Z,K_Y Y,K_W W)`; the three rescaled variables have independent cap-one densities. Their symmetric coefficient matrix is `D^(-1) M_eta D^(-1)`, and

`sigma_min(D^(-1) M_eta D^(-1))
 >= sigma_min(M_eta)/||D||^2
 >= 1/2`,                                                            (2.3)

because `sigma_min(M_eta)=1` and `||D||<=sqrt(2)`.

The completed three-variable theorem from the same source therefore yields

`boxed: ||p_{Q_eta}||_infinity <= 6 sqrt(pi)/(1/2)
                                =12 sqrt(pi)
                                <21.270.`                              (2.4)

Thus this family is emphatically not a counterexample to QFORM; its whole density, including the two-sheet side, is uniformly controlled while preserving source-product provenance.

### 2.3 Partner fleet03/B10 r26 applied quantitatively

The source-pinned r26 report

`yspennstate/math-open-problems@86d53dbc4715d6d1e8d5c9adb9bea080cf73d482`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T181522Z-fleet03-B10-QFORM-r26/REPORT.md`

proves the `1/61` leaf gate and, in the surviving diffuse positive-leakage state, a projected-crossing estimate `<16.652 rho^(-1/6)`. Since (1.2)-(1.3) put the present family in that state with `rho=eta`, it gives the concrete bound

`boxed: ||p_{Q_eta}||_infinity <16.652 eta^(-1/6).`                    (2.5)

This is finite for each positive leakage but diverges at the exact-coloop endpoint. The special-family bound (2.4) shows that the divergence in (2.5) is not intrinsic to this example; it is exactly the endpoint-stability issue left by r26.

## 3. The hub-first absolute discriminant diverges on a genuine two-sheet level

Write a general spectral vector in the hub decomposition as

`z=sqrt(c)x_0+T`, `V=(y,w)`.

For (1.4), conditioning on every leaf and viewing `Q_eta` as a quadratic polynomial in the ORIGINAL hub variable `x_0`, the discriminant after division by `4c` is

`D_s(y,w)=(1+eta)y^2-eta w^2+eta s`.                                  (3.1)

Indeed all dependence on the longitudinal leaf aggregate `T` cancels exactly. The cap-one hub calculation therefore gives the standard upper receiver

`p_{Q_eta}(s) <= c^(-1/2)
                 E[1_{D_s(Y,W)>0} D_s(Y,W)^(-1/2)]`.                  (3.2)

The point is that the expectation on the right is not uniformly bounded, even after moving strictly to the two-sheet side.

Take the fixed minority-sign level `s=-1`. Since every `e_3`-bank source lies in `[1,2]`,

`8 <= W <=16`, hence `W^2+1<=257`.                                    (3.3)

Let `f_Y` be the density of the normalized sum of the 64 uniforms on `[-1/2,1/2]`. It is the usual compactly supported B-spline density, continuous and strictly positive on the interior of its support. Thus the fixed number

`kappa := min_{|y|<=1/4} f_Y(y)`                                      (3.4)

satisfies `kappa>0`.

For

`2 sqrt(257 eta) <= |y| <=1/4`,                                      (3.5)

our restriction `eta<1/16448` makes the interval nonempty. By (3.3),

`D_{-1}(y,w)=(1+eta)y^2-eta(w^2+1)>0`,                                (3.6)

and also

`D_{-1}(y,w) <= (1+eta)y^2`.                                          (3.7)

Integrating over all `W` and over both signs of `Y` therefore gives the rigorous lower bound

`E[1_{D_{-1}>0}D_{-1}^{-1/2}]
 >= [2 kappa/sqrt(1+eta)]
    int_{2 sqrt(257 eta)}^(1/4) dy/y
 = [2 kappa/sqrt(1+eta)]
    log(1/[8 sqrt(257 eta)]).`                                        (3.8)

Hence

`boxed: E[1_{D_{-1}>0}D_{-1}^{-1/2}] -> infinity
        logarithmically as eta ->0.`                                  (3.9)

This is on the genuine two-sheet level `s=-1`; it is not the cone boundary `s=0` already paid by the ruled theorem.

Consequently the following intermediate claim is false:

`QFORM-TWOSHEET-DIFFUSE-ABS-DISCRIMINANT-UNIFORM-v0`:
"in the near-coloop/diffuse-leaf collar, the hub-first absolute discriminant receiver is uniformly bounded on the minority-sign side."

The counterexample obeys every target source hypothesis, has exact nonzero spectrum `{1+eta,-1,1}`, lies below the partner `1/61` transverse-leverage gate, and has `rho=q=eta->0`. Yet its actual output remains uniformly bounded by (2.4). Thus (3.9) diagnoses a proof-interface singularity, not a QFORM counterexample.

## 4. What the obstruction says about the endpoint gluing

The ruled theorem has now been fully consumed on its correct side: (2.1) removes every `s>=0` level for this `(2,1)` orientation. The obstruction (3.8) shows that the remaining two-sheet problem cannot be finished by the tempting sequence

`condition ORIGINAL hub -> take absolute root Jacobian -> average D_s(V)^(-1/2)`.

Even diffuse transverse leaves do not rescue that receiver. The endpoint proof must retain at least one further ORIGINAL-coordinate bank jointly with the hub before absolute values, so that the `eta=0` mixed-Fresnel mechanism survives as `rho,q ->0`. Equivalently, the next theorem must interpolate between the exact-null mixed-Fresnel endpoint and r26's positive-leakage projected crossing without separately paying either `rho^(-1/6)` or the logarithm in (3.8).

A useful stress requirement for any proposed theorem is therefore: it must control the explicit family (1.4) uniformly at `s=-1` while its proof remains valid after replacing the axis-aligned transverse banks by arbitrary diffuse Parseval leaf rows satisfying `sum t_jp_j=0`. Any proof whose terminal majorant contains (3.2) with an absolute expectation has already failed this test.

## 5. Scope/status

- Full arbitrary exact-rank-three QFORM: OPEN.
- Full arbitrary-matrix QFORM: OPEN.
- Essential boundedness: proved only for the completed source scopes and the special family above.
- Continuity: the source three-variable theorem supplies it for the special family; no new global continuity assertion is made.
- No moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption entered the target statement or the obstruction.

This report is an explicit source-valid counterexample to an intermediate endpoint-gluing mechanism plus a source-pinned actual inequality on the ruled side. It narrows the first unpaid implication to genuinely joint hub-plus-bank smoothing on the minority-sign side.