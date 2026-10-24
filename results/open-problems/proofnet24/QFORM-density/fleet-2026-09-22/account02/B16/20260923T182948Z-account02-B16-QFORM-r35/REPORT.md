# account02/B16 QFORM r35 — rank-two cross plus rank-one same-side Fresnel

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T18:29:48Z.
attacking: the superdiffuse true-near-coloop two-bank residual by first paying one bank's non-diagonal rank-one same-side curvature together with the rank-two cross interaction, while retaining the projected two-dimensional dependence and original-source factorisation.

Full target status: **OPEN / NOT PROVED / NOT DISPROVED**. This note proves a supporting source-valid compiler and a target-valid stress family; it is not a proof of the unrestricted conjecture and not a counterexample. Continuity is asserted only for the compiler below, where an integrable Fourier majorant is obtained.

## First unpaid implication

`QFORM-TWO-BANK-COUPLED-INNOVATION-FRESNEL-v1`: in account03/B16 r30's surviving true-near-coloop state, each balanced source bank has a longitudinal row very close to its transverse two-row span. The theorem below identifies the exact one-bank determinant loss: the Fresnel/BL determinant is the rank-two cross singular product squared times the squared norm of the *true source innovation* transverse to that cross two-plane. Hence a one-bank rank-one Fresnel closure degenerates precisely when r30's innovation is small. The next step is to use both banks jointly so that the determinant is paid by inter-bank slope separation / cross-third-volume rather than by either small innovation separately, or else produce a source-valid obstruction.

## Theorem: QFORM-RANK2-CROSS-PLUS-RANK1-SAME-SIDE-FRESNEL-v1

Let the original independent coordinates be partitioned as `I ⊔ J ⊔ K`, and condition on `X_K`. Assume the conditioned quadratic form has arbitrary `I`-side quadratic part and arbitrary affine terms, while

- `M=A_{IJ}` has rank two, with SVD `M=U Σ V^T`, `Σ=diag(s1,s2)`, `s1,s2>0`, and `U,V` have orthonormal columns;
- in the **original J coordinates**, `A_{JJ}=D+eps*w*w^T`, where `D` is diagonal and `eps∈{+1,-1}` (the magnitude is absorbed into `w`);
- for each original source coordinate `j∈J`, define
  `a_j=(s1 V_{j1}, s2 V_{j2}, w_j)∈R^3`, and put `G=Σ_j a_j a_j^T`;
- `G` is positive definite and every normalized row leverage satisfies `c_j=a_j^T G^{-1}a_j ≤ 1/2`.

Then for arbitrary independent source densities bounded by one,

`|phi_Q(t)| ≤ 16*pi^(5/2)*det(G)^(-1/2)*|t|^(-5/2)` for `t≠0`,

and therefore `Q` has a continuous density satisfying

`||p_Q||_∞ ≤ (5/3)*2^(8/5)*det(G)^(-1/5)`.

Numerically, the universal prefactor is `5.0523885550346606`.

### Proof, with product provenance retained

After conditioning on `X_K`, write

`Q = R(X_I) + X_J^T D X_J + eps*(w·X_J)^2 + 2 X_I^T M X_J + b^T X_J + const`,

where `R` absorbs the arbitrary `I`-side quadratic/affine terms. Set `Z=U^T X_I∈R^2`. The two coordinates of `Z` are **not** declared independent. The completed two-dimensional product-projection theorem from the pinned `e5f71d79...` package gives only the legitimate joint statement

`||p_Z||_∞ ≤ 2`.

Disintegrate the complex source measure over this projection:

`H_t(z) dz = E[ exp(i t R(X_I)); Z∈dz ]`.

Because the conditional phase has modulus one, `|H_t(z)|≤p_Z(z)≤2`. Hence

`|phi_Q(t)| ≤ 2 ∫_{R^2} |Phi_J(t,z)| dz`,

where `Phi_J` is the original-product `J`-bank expectation. No projected independence and no conditional-density cap is introduced.

Fresnel-linearize only the rank-one square `eps*(w·X_J)^2` (with the standard damping/limit justification). If `rho_j=(s1 V_{j1},s2 V_{j2})` and

`g_{j,t}(x)=exp(i t D_{jj}x^2) f_j(x)`,

then `|g_{j,t}|≤f_j` and

`|Phi_J(t,z)| ≤ (4*pi*|t|)^(-1/2) ∫_R ∏_{j∈J} |hat g_{j,t}( 2t<rho_j,z> + u w_j + t b_j )| du`.

Change variables `y=2tz`. The two-dimensional Jacobian is `(4|t|^2)^(-1)`, so

`|phi_Q(t)| ≤ (1/2)(4*pi)^(-1/2)|t|^(-5/2) I_t`,

with

`I_t = ∫_{R^3} ∏_j |hat g_{j,t}( <a_j,(y,u)> + t b_j )| dy du`.

Now normalize the original-source row system. Let `b_j=G^{-1/2}a_j`, `c_j=||b_j||^2`, and `u_j=b_j/sqrt(c_j)` for nonzero rows. Then `Σ_j c_j u_j u_j^T=I_3`, `Σ_j c_j=3`, and `p_j=1/c_j≥2`. After the change of variables by `G^{1/2}`, geometric Brascamp--Lieb gives

`I_t ≤ det(G)^(-1/2) ∏_j [ c_j^(-1/2) ∫ |hat g_{j,t}(s)|^(1/c_j) ds ]^(c_j)`.

Apply the pinned completed twisted characteristic-function estimate

`∫ |hat g|^p ≤ 4*pi/sqrt(p)` for `p≥2` whenever `|g|≤f` and `f` is a density bounded by one.

At `p=1/c_j`, the bracket is at most

`c_j^(-1/2) * 4*pi*sqrt(c_j) = 4*pi`.

Therefore

`I_t ≤ (4*pi)^3 det(G)^(-1/2)`,

and

`|phi_Q(t)| ≤ (1/2)(4*pi)^(5/2) det(G)^(-1/2)|t|^(-5/2)
             = 16*pi^(5/2) det(G)^(-1/2)|t|^(-5/2)`.

Together with `|phi_Q|≤1`, put `B=16*pi^(5/2)det(G)^(-1/2)` and integrate `min(1,B|t|^(-5/2))`. The cutoff is `T=B^(2/5)` and

`∫_R min(1,B|t|^(-5/2)) dt = (10/3) B^(2/5)`.

Fourier inversion yields

`||p_Q||_∞ ≤ (1/(2*pi))*(10/3)*B^(2/5)
           = (5/3)*2^(8/5)*det(G)^(-1/5)`.

The same integrable Fourier majorant gives continuity on this branch.

## Exact innovation determinant identity

Because `V^T V=I_2`,

`G = [[Σ^2, Σ V^T w], [w^T V Σ, ||w||^2]]`.

Taking the Schur complement of `Σ^2` gives the exact identity

`det G = (s1*s2)^2 * ( ||w||^2 - ||V^T w||^2 )
       = (s1*s2)^2 * ||(I-VV^T)w||^2`.

If `delta=||(I-VV^T)w||`, the density certificate is therefore

`||p_Q||_∞ ≤ (5/3)*2^(8/5) * (s1*s2*delta)^(-2/5)`.

This isolates the precise source-level obstruction. The component of `w` lying *inside* the right cross two-plane does not create a new Fresnel direction; only the genuine source innovation transverse to that plane contributes to the three-dimensional BL determinant. If `w∈Range(V)`, the augmented determinant is singular and this one-bank compiler cannot close the case.

## Target-valid aggregate stress family

Take `m=2^q≥8`. On one original source bank choose two diffuse Walsh columns `C=(c1,c2)∈R^{m×2}`. On a disjoint source bank choose three diffuse Walsh columns `(v1,v2,w)∈R^{m×3}`, and put `V=(v1,v2)`. All columns are orthonormal and all entries are `±m^{-1/2}`. Define

`A_m = [[0, C V^T], [V C^T, w w^T]]`.

In the carrier basis `(c1,c2,v1,v2,w)`, the nonzero matrix is

`[[0_2,I_2,0],[I_2,0_2,0],[0,0,1]]`.

Hence the nonzero spectrum is exactly

`{1,1,1,-1,-1}`,

so this family lies inside the full QFORM target. Here `s1=s2=1`, `G=I_3`, and every augmented original-source row has leverage `3/m≤1/2`. The theorem therefore gives, for **every** choice of independent cap-one input densities,

`||p_{X^T A_m X}||_∞ ≤ (5/3)*2^(8/5) = 5.0523885550346606...`,

and the density is continuous.

This is an actual use of two completed pinned results at the nonlinear interface: the two-dimensional product-projection density cap `≤2` is used for the dependent projected pair `C^T X`, while the twisted Fourier `L^p` estimate is used only on the still-factorized original `J` source bank after rank-one Fresnel linearization. At no point are projected coordinates treated as independent.

The example also gives a certificate obstruction. The cross block has rank two, so the pinned rank-three cross-volume quantities satisfy `e_3(M^T M)=0` (and `e_5=0`), making those routes unavailable. Yet all physical coefficients vanish with `m`: cross entries have modulus at most `2/m`, the rank-one same-side entries have modulus `1/m`, every physical diagonal has modulus at most `1/m`, every physical `2x2` principal determinant is `O(m^-2)`, and every fixed physical `3x3` principal determinant is at most `48/m^3` in modulus by the determinant expansion. Thus atom-by-atom reciprocal-minor certificates deteriorate while the aggregate source-plane/source-innovation receiver remains uniformly bounded. This is an aggregation-before-curvature obstruction, not a counterexample.

## Interface with account03/B16 r30

The designated partner's r30 survivor has two genuine original-coordinate balanced banks and, in each, a longitudinal source row lying very close to its transverse two-row span. The identity

`det G=(s1*s2)^2*delta^2`

shows that the partner's small innovation is not a harmless perturbation in any one-bank rank-one Fresnel reduction: it is exactly the determinant bottleneck. Since the source variables are unbounded, that remainder cannot simply be deleted. The useful next compiler must couple both banks (or an equivalent source-preserving decomposition) so that the determinant is supported by two-slope separation / cross-bank third-volume while same-side curvature is retained through the oscillatory integral.

No hidden moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is used.