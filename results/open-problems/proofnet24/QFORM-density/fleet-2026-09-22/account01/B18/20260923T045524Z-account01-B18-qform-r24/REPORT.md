SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T04:55:24Z.
attacking: literature-to-proof transfer on the designated partner's explicit diffuse-star/two-sheet stress family, by regrouping Hadamard sign patterns into honest independent original-coordinate banks and reducing to three independent capped scalars.

# account01/B18 r24 — the designated Hadamard diffuse-star stress family is bounded on the full line

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL FAMILY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed for the new full-line estimate; global continuity remains open.

## 1. Fresh control and correction boundary

Fresh owner control remains revision `2026-09-22.15`, with QFORM as the sole research target. The exact target is unchanged: for arbitrary independent original-coordinate inputs with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension- and law-independent density bound.

The live correction ledger was reread immediately before publication. The proof below does **not** use post-rotation independence, arbitrary-joint rank-three coarea, a positive conditional projection-density moment, a worst conditional-fiber cap, pointwise law-uniform quadratic Fresnel decay, a fixed good physical minor, or perturbative deletion of small coefficients. All independence used below comes from disjoint sets of the original independent coordinates.

The newest relevant designated-partner source actually consumed is account02/B18 auto11,

`yspennstate/math-open-problems@826920faef301e7d6880266805e11a0a7350076f`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T040922Z-account02-B18-QFORM-auto11/REPORT.md`.

Its non-separated Schur-isotropic representation is

`Q=(Y+uX_0)^T D(Y+uX_0)`,

with `X_0` an original coordinate independent of the residual original product vector and `Y=V^T X_R`. It proves that the one-sheet half-line is already paid by `pi sqrt(2)`, and isolates an explicit Walsh--Hadamard family showing that the unresolved N3 diffuse-star/two-sheet geometry is genuine.

The second completed theorem used below is account01/B19,

`yspennstate/math-open-problems@c8958cdca7989ce69df1805a5ed0ca18557b5d4c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T041858Z-account01-B19-qform-r11/REPORT.md`.

Its theorem `QFORM-3SCALAR-UNIVERSAL-v1` states: if `W=(W_1,W_2,W_3)` has genuinely independent scalar coordinates with densities at most one and `M=M^T` is `3 x 3` with `sigma_min(M)>=s>0`, then every affine perturbation

`W^T M W+d^T W+c`

has density satisfying

`||p||_infinity <105/s`.                                          (1.1)

The proof is entirely in the original scalar variables: a large physical diagonal is handled by square smoothing plus the completed rank-two affine half-Riesz theorem; otherwise a quantitative indefinite physical pair is handled by the pair-log theorem.

## 2. Primary literature transfer: scalar bank compression

The external source used at exactly its hypotheses is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1. If a probability density is a product of one-dimensional factors each bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`.

For `k=1`, if `Z=sum_j a_j X_j` with `sum_j a_j^2=1` and the `X_j` are independent with densities at most one, then

`||p_Z||_infinity <=sqrt(2)`.                                     (2.1)

No moment, support, smoothness, iid, log-concavity or post-rotation-independence hypothesis is introduced. In the application below each such projection uses a disjoint original-coordinate bank, so the resulting scalar projections are genuinely independent.

## 3. The designated partner's exact target-valid stress family

For `r>=1` and a real Walsh--Hadamard order `m>=4`, the partner takes `V` to be the first three normalized Hadamard columns, so every residual spectral row is

`v_j=(eps_{j1},eps_{j2},eps_{j3})/sqrt(m)`, `eps_{jk} in {+1,-1}`,

and `V^T V=I_3`. Put

`s=sqrt(1+r^2)`,
`u=r e_1`,
`D_r=[[0,1/s,0],[1/s,0,0],[0,0,1]]`.

Then the physical matrix `A=L^T D_r L`, `L=[u,V^T]`, has exactly the three nonzero eigenvalues

`{-1,1,1}`                                                        (3.1)

for every `m,r`. Thus it satisfies the owner target at exact spectral scale one. The output is

`Q_(m,r)=2/s (Y_1+rX_0)Y_2+Y_3^2`.                               (3.2)

The partner proves at the actual target inequality that

`p_(Q_(m,r))(t) <= pi sqrt(2)`                                    (3.3)

for a.e. `t>=0` in the displayed signature. The unresolved part of this explicit family was the minority-sign/two-sheet half-line `t<0`.

The rest of this report closes that family on the **entire** real line.

## 4. Product-preserving four-pattern regrouping

Deterministically sign-flip each residual original variable by the first Hadamard sign:

`Xtilde_j=eps_{j1} X_j`.                                          (4.1)

This preserves independence and every scalar density cap. Define

`a_j=eps_{j1}eps_{j2}`, `b_j=eps_{j1}eps_{j3}`.                   (4.2)

Then

`Y_1=m^(-1/2) sum_j Xtilde_j`,
`Y_2=m^(-1/2) sum_j a_j Xtilde_j`,
`Y_3=m^(-1/2) sum_j b_j Xtilde_j`.                               (4.3)

Because the three Hadamard columns are pairwise orthogonal, the signs satisfy

`sum_j a_j=0`, `sum_j b_j=0`, `sum_j a_j b_j=0`.                 (4.4)

Together with the total count `m`, these four linear equations imply that each of the four patterns `(a_j,b_j) in {+1,-1}^2` occurs exactly `m/4` times.

For every pattern `(a,b)`, define the disjoint-bank aggregate

`Z_ab=m^(-1/2) sum_{j:(a_j,b_j)=(a,b)} Xtilde_j`.                 (4.5)

The four `Z_ab` are genuinely independent because their supports are disjoint sets of original coordinates; they are also independent of the original hub scalar `X_0`.

The coefficient vector in each bank has Euclidean norm

`sqrt[(m/4)(1/m)]=1/2`.                                          (4.6)

Hence

`U_ab:=2 Z_ab`                                                    (4.7)

is a unit one-dimensional projection of that bank's cap-one product source. By the primary LPP theorem (2.1),

`||p_(U_ab)||_infinity<=sqrt(2)`.                                 (4.8)

Consequently the rescaled variables

`W_ab:=sqrt(2) U_ab=2sqrt(2) Z_ab`                               (4.9)

have probability densities bounded by one. The `W_ab` remain mutually independent.

This is the key literature-to-proof transfer: the apparently fully mixed Hadamard projection contains four honest disjoint source banks after grouping by sign pattern, and LPP turns each bank into one cap-one scalar without any false post-rotation independence assertion.

## 5. A uniformly invertible three-scalar active block

Select the two pattern banks

`Z_+=Z_(+,+)`, `Z_-=Z_(-,+)`.                                    (5.1)

Condition on the other two independent pattern aggregates `Z_(+,-),Z_(-,-)`. Since the five variables

`X_0, Z_(+,+), Z_(-,+), Z_(+,-), Z_(-,-)`

come from disjoint original-coordinate banks, this conditioning leaves `X_0,Z_+,Z_-` genuinely independent. The conditioned variables from the other banks enter only through affine and constant terms.

Put

`t=1/s`, `k=r/s=sqrt(1-t^2)`.                                    (5.2)

Since `r>=1`,

`0<t<=1/sqrt(2)`, `k^2>=1/2`.                                   (5.3)

In the active variables `(x,z_+,z_-)=(X_0,Z_+,Z_-)`, the quadratic coefficient matrix is exactly

`H(t)=
 [[0, k, -k],
  [k, 1+2t, 1],
  [-k, 1, 1-2t]].`                                               (5.4)

Indeed the hub cross terms are `2k x(z_+-z_-)`; the `2tY_1Y_2` term contributes `+2t z_+^2-2t z_-^2` and no `z_+z_-` term; and `Y_3^2` contributes `(z_++z_-)^2`.

Now use the cap-one variables

`w_+=2sqrt(2) z_+`, `w_-=2sqrt(2) z_-`.                          (5.5)

Let

`S=diag(1,(2sqrt(2))^(-1),(2sqrt(2))^(-1))`.

The active matrix in `(X_0,w_+,w_-)` is

`H_*(t)=S H(t) S`.                                                (5.6)

Two exact calculations are

`|det H_*(t)|=(1-t^2)/16`,                                       (5.7)

and

`||H_*(t)||_F^2=(9-6t^2)/16`.                                   (5.8)

Let its singular values be `sigma_1>=sigma_2>=sigma_3`. Then

`sigma_1 sigma_2
 <=(sigma_1^2+sigma_2^2)/2
 <=||H_*||_F^2/2`.                                                (5.9)

Therefore

`sigma_min(H_*)=sigma_3
 =|det H_*|/(sigma_1 sigma_2)
 >=2|det H_*|/||H_*||_F^2
 =2(1-t^2)/(9-6t^2).`                                             (5.10)

The last expression decreases with `t^2` on `[0,1/2]`, so by (5.3)

`boxed: sigma_min(H_*(t))>=1/6.`                                 (5.11)

This bound is independent of both the Hadamard order `m` and the shear parameter `r`.

## 6. Full-line density bound for the partner family

Conditioned on the two unused sign-pattern banks, `(X_0,w_+,w_-)` are three independent cap-one scalars, their quadratic matrix has smallest singular value at least `1/6`, and all effects of the conditioned banks are affine/constant. Thus `QFORM-3SCALAR-UNIVERSAL-v1` applies directly to every conditional law:

`||p_(Q_(m,r) | Z_(+,-),Z_(-,-))||_infinity
 <105/(1/6)=630.`                                                 (6.1)

The right side is uniform in the conditioned values. Averaging the conditional densities gives

`boxed:
 ||p_(Q_(m,r))||_infinity <630
}`                                                                  (6.2)

for every `r>=1`, every Walsh--Hadamard order `m>=4`, and **every** admissible independent original-coordinate law with scalar densities at most one.

This is a target-level estimate: the physical matrix has spectrum exactly `{-1,1,1}`. It closes the previously unresolved `t<0` two-sheet half of the partner's explicit mixed-source N3 stress family. Combining with the partner's sharper one-sheet theorem gives the two-sided information

`p_(Q_(m,r))(t) <= pi sqrt(2)` for a.e. `t>=0`,

`p_(Q_(m,r))(t) <630` for a.e. `t<0`,                              (6.3)

while (6.2) is the convenient full-line certificate.

## 7. Scope and remaining implication

This result does **not** solve the general diffuse-star/two-sheet branch. The proof uses the exact Walsh--Hadamard sign-pattern algebra to obtain four disjoint equal-mass source banks; a general N3 diffuse star has only

`sum_j q_j^2=1`, `max_j q_j^2<2tau`

and need not admit the same four-pattern representation. Thus the partner's general first unpaid implication remains:

`QFORM-N3-DIFFUSE-STAR-TWOSHEET-v1`:

> use the coefficient-level product provenance of a general diffuse original-coordinate star, before destructive conditioning, to obtain an endpoint-stable two-sheet bound.

The present theorem proves that the designated partner's canonical Hadamard stress family is **not** a counterexample and that its apparent dependent three-dimensional projection can be paid by a hidden disjoint-bank decomposition. This suggests a structural next step: replace exact four-pattern grouping by a quantitative partition of the residual coefficient rows into a bounded number of source banks whose three active coefficient vectors yield a uniformly invertible scalar compression, or route failure into an already-paid aggregate-volume/ridge branch.

No exact prior theorem settling all owner quantifiers was located. The LPP theorem is used only for linear marginal compression, exactly within its scope; the nonlinear quadratic payment comes from the source-valid three-independent-scalar theorem after disjoint-bank reduction. No novelty claim is based on the absence of a search hit.

## 8. Continuity bookkeeping

The new full-line estimate (6.2) is an essential `L^infinity` density bound. `QFORM-3SCALAR-UNIVERSAL-v1` does not, in the form used here, supply an `L^1` characteristic function or a continuous representative, so continuity is **not claimed** for this full-line family by the present argument. The partner one-sheet theorem also did not require continuity. The global continuity target therefore remains separate and open.

## 9. Arithmetic audit

The critical deterministic identities can be checked symbolically:

`det H(t)=-4(1-t^2)`,

`det H_*(t)=-(1-t^2)/16`,

`||H_*(t)||_F^2=(9-6t^2)/16`,

and hence

`2|det H_*|/||H_*||_F^2=2(1-t^2)/(9-6t^2)>=1/6`

for `0<=t^2<=1/2`. The only probabilistic inequality introduced by the transfer is the primary LPP marginal cap (2.1), used on four disjoint original-coordinate banks.

**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**New closed node:** the account02/B18 explicit Walsh--Hadamard diffuse-star stress family is uniformly bounded on the entire output line by `<630`; its one-sheet side retains the sharper partner bound `pi sqrt(2)`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.
