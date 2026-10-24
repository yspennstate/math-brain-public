SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T01:25:55Z.
attacking: literature-to-proof transfer: optimize the completed account04/B18 Schur-isotropic mixed-volume argument by a source-valid Brascamp--Lieb basis mixture, removing its small-shear loss on a genuine target branch.

# account03/B18 r21 — entropy-matched basis sampling removes the small-shear loss

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING TARGET-LEVEL BRANCH / PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and live boundary

The owner target remains the unrestricted statement: for arbitrary finite `n`, arbitrary independent real original-coordinate variables with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `X^T A X`, or give a valid counterexample. No moment, Gaussian, log-concave, bounded-support, connected-support, smoothness or post-rotation independence hypothesis is added. Continuity is tracked separately.

Fresh control was read from `yspennstate/math-research-brain@5a8cfafa64e4d0a911d4b0b84166234fc3880998`, OWNER CONTROL revision `2026-09-22.15`. The current no-pivot/N3 reduction and correction set were also read. In particular this report does not use arbitrary-joint rank-three coarea, positive moments of conditional projection-density suprema, a law-uniform pointwise quadratic-phase decay estimate, a uniformly good single physical minor/cross cut, or small-operator-error-as-small-random-error.

The newest owner continuation was consumed from the `20260923T002323Z-volume-stability` handoff. Full N3 and hence full QFORM remain open.

## 2. Primary-source transfer actually used

The analytic engine is the completed capped-basis Fresnel theorem in account01/B18 r19. I rechecked its two primary ingredients at their actual scope:

1. William Beckner, *Inequalities in Fourier analysis*, Ann. of Math. **102** (1975), 159--182, DOI `10.2307/1970980`: the sharp Hausdorff--Young inequality used for each original one-dimensional product factor.
2. Bennett--Carbery--Christ--Tao, *The Brascamp--Lieb inequalities: finiteness, structure, and extremals*, arXiv `math/0505065`, Theorem 1.9: Lieb's theorem `BL=BL_g`, i.e. the Brascamp--Lieb constant is exhausted by centered Gaussians. This is exactly what permits the rank-one Gaussian determinant formula used by account01/B18.

The account01/B18 theorem, proved from those sources, says: if `L` is a real `3 x N` rank-three coefficient matrix, `D` is invertible symmetric, and `w` is any probability law on nonsingular three-column bases of `L` with coordinate marginals `alpha_i<=1/2`, then for arbitrary independent cap-one original-coordinate inputs,

`||p_(X^T L^T D L X)||_infinity <=3e (|det D| Z_w)^(-1/3)`,       (2.1)

where

`Z_w=exp(H(w)+E_w log det(L_S)^2)`.                               (2.2)

The proof is uniform under arbitrary affine terms and supplies a continuous density. The present run does not alter any source hypothesis; it supplies a new exact admissible `w` and optimizes it.

A focused literature search did not locate an exact published solution of the owner's unrestricted cap-one three-large-eigenvalue theorem. Classical Gaussian quadratic-form formulas and results requiring moments/convexity do not match the quantifiers here.

## 3. Completed designated-partner input

The latest completed designated partner is account04/B18 r3:

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T001857Z-account04-B18-QFORM-r3/REPORT.md`.

Its exact Schur-isotropic core is

`Q=(Y+u X_0)^T D (Y+u X_0)`,                                      (3.1)

where `X_0` is an ORIGINAL coordinate independent of all residual original coordinates, `Y=V^T X'`, `V^T V=I_3`, `D=D^T` is nonsingular, and

`u^T D u=0`.                                                       (3.2)

With the residual physical rows `v_j^T`, let

`L=[u,v_1,...,v_m]`,                                                (3.3)

so the partner proves the exact identities

`LL^T=I+uu^T`,
`|pdet(L^T D L)|=|det D|(1+||u||^2)`.                              (3.4)

Write

`r=||u||>0`, `n=u/r`,
`p_j=||v_j||^2`,
`q_j=||(I-nn^T)v_j||^2`.                                           (3.5)

The partner also proves two exact Cauchy--Binet probability laws:

`mu_S=det(V_S)^2` on residual triples, with coordinate marginal `p_j`; (3.6)

`nu_jk=det[n,v_j,v_k]^2` on residual pairs, with coordinate marginal `q_j`. (3.7)

Its fixed half-half mixture gives

`||p_Q||_infinity <=3e(2r|det D|)^(-1/3)`,                         (3.8)

and after (3.4), on a target-normalized exact-rank-three matrix,

`||p_Q||_infinity <=3e((1+r^2)/(2r))^(1/3)`.                       (3.9)

Equation (3.9) is the required substantive application of the completed partner theorem. It is uniform for moderate `r` but degenerates as `r->0`. The next section removes that loss without changing the probability laws or product provenance.

## 4. Variable mixed-volume theorem

### Theorem `QFORM-ISOTROPIC-SHEAR-ENTROPY-MATCHED-v1`

Under (3.1)--(3.7), fix `x in (0,1/2]` and suppose

`(1-x)p_j+x q_j <=1/2` for every residual physical coordinate `j`. (4.1)

Define

`Z_r(x)=(1-x)^(-(1-x)) (r^2/x)^x`.                                (4.2)

Then `Q` has a bounded continuous density and

`boxed: ||p_Q||_infinity <=3e [|det D| Z_r(x)]^(-1/3).`             (4.3)

#### Proof

Put a probability law on the three-column bases of `L` by

`w_S=(1-x)mu_S` for residual triples,
`w_{0jk}=x nu_jk` for bases containing the shear coordinate `0`.   (4.4)

The shear-coordinate marginal is `alpha_0=x<=1/2`. By (3.6)-(3.7), every residual marginal is exactly

`alpha_j=(1-x)p_j+x q_j<=1/2`.                                     (4.5)

Hence the capped-basis theorem (2.1) applies.

The determinant-entropy score is exact. For a residual triple,

`det(L_S)^2/w_S = mu_S/[(1-x)mu_S] =1/(1-x)`.                      (4.6)

For a shear pair basis,

`det[u,v_j,v_k]^2 = r^2 nu_jk`,

so

`det(L_{0jk})^2/w_{0jk}=r^2/x`.                                   (4.7)

Since the two banks have total masses `1-x` and `x`, respectively,

`log Z_w=(1-x)log(1/(1-x))+x log(r^2/x)`,                           (4.8)

which is (4.2). Substitution into (2.1) proves (4.3). Continuity is inherited from the integrable characteristic-function majorant in the capped-basis theorem. QED.

## 5. Exact optimization and the new universal branch

Differentiate (4.2):

`d/dx log Z_r(x)=log(r^2(1-x)/x)`.                                 (5.1)

Thus the unconstrained optimum is

`x_*=r^2/(1+r^2)`,                                                  (5.2)

and at this point both basis-bank ratios in (4.6)-(4.7) equal `1+r^2`, so

`boxed: Z_r(x_*)=1+r^2.`                                           (5.3)

If `0<r<=1`, then `x_*<=1/2`. Moreover `q_j<=p_j` because orthogonal projection cannot increase norm. Therefore the simple diffuse-residual condition

`boxed: max_j p_j<=1/2`                                            (5.4)

implies

`alpha_j=(p_j+r^2 q_j)/(1+r^2)<=p_j<=1/2`.                         (5.5)

Equations (4.3), (5.3) and (3.4) yield

`boxed:
 ||p_Q||_infinity
 <=3e [|det D|(1+r^2)]^(-1/3)
 =3e |pdet(L^T D L)|^(-1/3).`                                     (5.6)

Hence, if this is an exact-rank-three target matrix whose three nonzero eigenvalue magnitudes are all at least one,

`boxed: ||p_Q||_infinity <=3e = 8.154845485377... .}`               (5.7)

The density is continuous.

This is genuinely stronger than the partner's fixed-half estimate in the small-shear regime. Under the same diffuse-residual hypothesis, the partner bound (3.9) grows like `r^(-1/3)`, whereas (5.7) is uniform down to arbitrarily small positive `r`.

A slightly more general version replaces (5.4) by the exact condition

`p_j+r^2q_j <=(1+r^2)/2` for every j.                              (5.8)

Thus the new argument also covers some residual rows slightly above leverage `1/2` when their transverse leverage `q_j` is smaller.

## 6. Fully target-valid stress family

For every `0<r<=1`, let

`u=r e_1`.                                                         (6.1)

Let `V` have six physical rows: two copies each of

`e_1/sqrt(2)`, `e_2/sqrt(2)`, `e_3/sqrt(2)`.                        (6.2)

Then `V^T V=I_3` and every residual leverage is `p_j=1/2`. Put

`D_r = [[0,(1+r^2)^(-1/2),0],
        [(1+r^2)^(-1/2),0,0],
        [0,0,1]]`.                                                  (6.3)

Then `u^T D_r u=0` and `det D_r=-1/(1+r^2)`. Since

`LL^T=diag(1+r^2,1,1)`,                                             (6.4)

the nonzero eigenvalues of `A_r=L^T D_r L` are the eigenvalues of

`(LL^T)^(1/2) D_r (LL^T)^(1/2)
 =[[0,1,0],[1,0,0],[0,0,1]]`,                                     (6.5)

namely exactly

`{-1,1,1}`.                                                        (6.6)

So this is a valid target family for every `r>0`, even as the physical shear column tends to zero. The optimized basis law has

`x_*=r^2/(1+r^2)`, `Z=1+r^2`, `|det D_r|Z=1`,                      (6.7)

and (5.7) gives the same `3e` density cap for all `r`.

For comparison, the completed partner theorem applied literally to this same family gives

`3e((1+r^2)/(2r))^(1/3)`.                                          (6.8)

At `r=0.1` this is approximately `13.9909`; at `r=0.01` it is approximately `30.0437`; the entropy-matched theorem remains `8.154845...` in both cases. This comparison is deterministic and not evidence from histograms.

## 7. Ambient conditioning corollary

Because the capped-basis Fresnel theorem is uniform under arbitrary affine terms, the same proof survives conditioning on all original coordinates outside an active physical set. Thus any ambient quadratic form having a physical principal block of the form (3.1)--(3.7), satisfying (5.2)/(5.8) and

`|det D|(1+r^2)>=c^3`,                                             (7.1)

obeys the conditional and hence unconditional bound

`||p_Q||_infinity <=3e/c`.                                        (7.2)

All outside quadratic coefficients and couplings are retained through conditioning as constants and affine terms. This is a supporting localized branch; the bare global condition `s_3(A)>=1` has not been shown to force such a principal block.

## 8. What remains

This run closes the **diffuse residual, small Schur-isotropic shear** endpoint that the partner's fixed half-half volume mixture paid with a deteriorating constant. It does not close:

1. the large-shear regime `r>1`, where the cap on the shear coordinate forces `x<=1/2` and the score optimum lies outside the admissible interval;
2. residual leverage concentration violating (5.8);
3. arbitrary extra spectral directions unless a qualifying physical conditional core is actually present;
4. the full strict-N3 structural implication.

Those cases must be routed to the live high-leverage/hub, low-tail, pair, ridge, or grouped-coordinate mechanisms. The current no-pivot compiler shows that a full proof still requires an exhaustive compatible structural glue theorem. No such implication is asserted here.

**Full QFORM: OPEN / NOT PROVED.**  
**Continuity:** proved for the theorem above and its conditioning corollary; unrestricted continuity remains open.

## 9. Source and correction audit

- Primary sources actually checked: Beckner 1975 sharp Hausdorff--Young; Bennett--Carbery--Christ--Tao Theorem 1.9 / Lieb Gaussian exhaustion.
- Completed partner actually applied: account04/B18 r3, including (3.8)-(3.9) and the exact mixed-volume identities (3.4)-(3.7).
- Capped-basis engine: account01/B18 r19.
- No claim of an exact prior published solution was found.
- No post-rotation independence, arbitrary-joint coarea, worst conditional-density moment, fixed-minor extraction, pointwise law-uniform phase decay, or unbounded-input perturbative deletion is used.
