SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T15:21:38Z.
attacking: the double-diffuse invertible second-anchor collar by coupling its anchored third-volume singleton law to the physical residual second exterior volume under one-sided Weyl differencing.

# account01/B02 — double-anchor E1 x E2 cross-disjoint Fourier receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`  
**Continuity:** proved on the new L1 branch below; full-target continuity remains open.  
**Control at start:** `yspennstate/math-research-brain@5fd590abde30cd76ce2a47304fadb884415b025d`, owner revision `2026-09-22.15`.

The exact target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, iid, Gaussian, log-concavity, diagonal-basis independence, or post-rotation independence assumption is inserted.

## 1. Fresh sources actually used

Newest designated partner available during this run:

`yspennstate/math-open-problems@4029b9b55694ce709e43c62d2729e89108fbdede`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T141147Z-account02-B02-QFORM-auto11/REPORT.md`.

Its live invertible second-anchor packet is an ORIGINAL-coordinate physical cross block

`B=[[P,R],[C,M]]`,

with `P` an invertible physical `2 x 2` block, `D=|det P|`, algebraic cross-Schur residual

`S=M-C P^(-1)R`,

and

`G=D^2 ||S||_F^2 > Z/24`,                                      (1.1)

where `Z=E3(B_parent)` is the third exterior-volume currency of the parent physical block. The same report gives a genuine Fourier-L1 exit if `sr(S)>2`, quantitatively through its `c3(rho)` formula, and in particular a uniform displayed exit for `sr(S)>=5/2`. This run uses (1.1) at an actual inequality below.

Own immediate predecessor:

`yspennstate/math-open-problems@0629c28b13f18241a8bb12147fc7c8442125d31e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T142315Z-account01-B02-qform-auto11-r31/REPORT.md`.

It proves that, after already-paid branches, the invertible second-anchor residue can be reduced to

`rank(S)>=2`, `sr(S)<5/2`,
`h_r:=max_i ||S_i:||_2^2/||S||_F^2 <1/4`,
`h_c:=max_j ||S_:j||_2^2/||S||_F^2 <1/4`.                       (1.2)

It also proves literal physical three-column/three-row slice exits whenever either energy atom is not diffuse.

Analytic template consumed and generalized in this run:

`yspennstate/math-open-problems@5d35b697d95d20e66fd72c96a5ea2dffa1201958`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260923T071011Z-3508bbe2/REPORT.md`.

That completed account02/B02 theorem is the scalar-edge / E2 cross-disjoint one-sided-Weyl-differencing compiler. I repeat its KL-conditioned determinant-expansion argument below with a two-row/two-column physical anchor; the basis determinants and exponent sums are written explicitly, so the new result does not rely on a silent analogy.

## 2. Setup and two exact basis families

Condition on every original coordinate outside the two independent physical banks supporting `B`. Same-bank quadratic terms and affine terms remain arbitrary. Keep notation

`B=[[P,R],[C,M]]`,
`D=|det P|>0`,
`S=M-C P^(-1)R`,
`F=||S||_F^2`,
`G=D^2 F`.                                                        (2.1)

Assume also

`E:=E2(M)=e2(M^T M)>0`.                                          (2.2)

Define the anchored singleton law

`nu_S(i,j)=|S_ij|^2/F`,                                          (2.3)

and the physical residual second-minor law

`nu_M(U,V)=det(M[U,V])^2/E`, `|U|=|V|=2`.                       (2.4)

Draw the two samples independently. Define row and column cross-disjointness probabilities

`delta_r=P(i notin U)`,
`delta_c=P(j notin V)`.                                          (2.5)

These are deterministic coefficient statistics. No random coordinate is rotated.

There are two exact Cauchy-Binet basis families in the target-bank differencing space.

**Family S.** Select the two physical anchor rows of `B`, one residual row `i`, and coordinate vectors for every target coordinate outside the two anchor columns and residual column `j`. Its basis determinant is

`det B[{two anchor rows} union {i}, {two anchor columns} union {j}]
 =det(P) S_ij`.                                                   (2.6)

Hence the total squared determinant mass of this family is exactly

`sum_ij D^2 |S_ij|^2 =G`.                                       (2.7)

**Family M.** Select two residual physical rows indexed by `U`, the two coordinate vectors on the anchor columns, and all residual coordinate vectors outside `V`. Elementary expansion along the coordinate vectors gives basis determinant

`det M[U,V]`,                                                     (2.8)

so the total squared determinant mass is exactly `E`.

The identities (2.6) and (2.8) were also checked numerically on random rectangular blocks; the proof is the displayed block/basis expansion, not the numerical check.

## 3. Main theorem — `QFORM-DOUBLEANCHOR-E1E2-CROSSDISJOINT-L1-v1`

### Theorem 3.1

In the setup above, if `delta_r>0`, then the full ambient quadratic form has

`boxed:
 integral_R |phi_Q(t)| dt
 <=10 pi 2^(1/5) e^(4/5) (delta_r G E)^(-1/10).
}`                                                                  (3.1)

Consequently it has a bounded continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <=5 2^(1/5) e^(4/5) (delta_r G E)^(-1/10)
 <12.783 (delta_r G E)^(-1/10).
}`                                                                  (3.2)

The identical conclusion holds with `delta_c` by transposing the physical cross block.

### Proof

One-sided Weyl differencing in the target bank gives the source-valid inequality used in the completed account02/B02 edge/E2 theorem:

`|phi_Q(t)|^2
 <= integral prod_(r in source bank) h_r((B w)_r)
             prod_(l in target bank) g_l(w_l) dw`,                (3.3)

where

`h_r(s)=|hat f_r(2ts)|`,
`g_l=f_l * tilde(f_l)`,
`0<=g_l<=1`, `integral g_l=1`.                                    (3.4)

All same-bank and affine phases have disappeared from the absolute-value integrand. Thus no cross-only Schur packet is being identified with a TRUE symmetric Schur complement.

Condition the independent pair of determinant samples `(i,j)~nu_S`, `(U,V)~nu_M` on the row-disjoint event `i notin U`. Let the conditioned marginal laws be `mu_S,mu_M`. As in the completed account02/B02 argument,

`D(mu_S||nu_S)+D(mu_M||nu_M) <=log(1/delta_r)`.                  (3.5)

Let `alpha_k^S` be the conditioned singleton-row marginals and `alpha_k^M` the conditioned residual-pair row marginals; define

`alpha_k=(alpha_k^S+alpha_k^M)/2`.                               (3.6)

Because the singleton and pair are disjoint pointwise under the conditioning,

`0<=alpha_k<=1/2`, `sum_k alpha_k=3/2`.                          (3.7)

Let `beta_l^S,beta_l^M` be the corresponding column inclusion marginals and

`beta_l=(beta_l^S+beta_l^M)/2`.                                  (3.8)

No column disjointness was conditioned, but automatically

`0<=beta_l<=1`, `sum_l beta_l=3/2`.                              (3.9)

Apply geometric Brascamp--Lieb to (3.3) with exponents

- each of the two physical anchor row forms: `1/2`;
- residual physical row `k`: `alpha_k`;
- each of the two anchor coordinate maps: `1/2`;
- residual coordinate map `e_l`: `1-beta_l`.

The exponents sum to the target-bank dimension. In Lieb's Gaussian determinant formula, retain only the two exact positive basis families from Section 2. Weighted AM--GM with `mu_S` and `mu_M`, followed by `A_S+A_M>=2 sqrt(A_S A_M)`, gives

`BL <= sqrt(2) delta_r^(-1/4)(G E)^(-1/4)
      prod_k alpha_k^(-alpha_k/2)
      prod_l (1-beta_l)^(-(1-beta_l)/2)`.                         (3.10)

The only difference from the completed scalar-edge/E2 calculation is the factor `sqrt(2)`: each S-basis contains two half-weight anchor rows and each M-basis contains two half-weight anchor coordinate maps. Thus the geometric mean contains an anchor-weight factor `1/4`; the AM--GM factor two leaves `1/2` inside the Gaussian determinant, whose inverse square root is `sqrt(2)`. All Gaussian parameters cancel exactly. Equation (3.5) supplies the displayed `delta_r^(-1/4)`.

For every row exponent `0<c<=1/2`, sharp Hausdorff--Young gives exactly the scalar bound used by account02/B02,

`integral h_r(s)^(1/c) ds
 <=(pi/|t|) sqrt(c) (1-c)^(-(1-c)/(2c)).`                        (3.11)

After raising to the Brascamp--Lieb powers, the `c^(c/2)` factors cancel the inverse powers in (3.10). For the two anchor rows the `c=1/2` factors cancel internally. Since the residual row exponents sum to `3/2`, the remaining row entropy factor is at most

`prod_k (1-alpha_k)^(-(1-alpha_k)/2)
 <=exp((1/2)sum_k alpha_k)=e^(3/4).`                              (3.12)

The total row time factor is

`(pi/|t|)^(1+3/2)=(pi/|t|)^(5/2)`.                              (3.13)

For the coordinate difference densities, sharp Young gives the same endpoint-safe factors as in the source theorem. A convenient conservative bound is obtained from

`2^d(1+d)^(-(1+d)/2)
 <=exp((1-log 2)(1-d)/2)`, `0<=d<=1`.                            (3.14)

The total missing coordinate weight is `5/2` (one from the two half-weight anchor coordinates and `3/2` from the residual selected-column marginals), so this coordinate product is strictly below `e^(5/4)`. Combining with (3.12) gives the clean safe entropy factor `e^2`.

Therefore

`|phi_Q(t)|^2
 <=sqrt(2)e^2 pi^(5/2)
   delta_r^(-1/4)(G E)^(-1/4)|t|^(-5/2)`.                       (3.15)

Taking square roots,

`|phi_Q(t)|
 <=min{1,
       2^(1/4)e pi^(5/4)(delta_r G E)^(-1/8)|t|^(-5/4)}.`       (3.16)

For `A>0`,

`integral_R min(1,A|t|^(-5/4))dt=10 A^(4/5)`.                  (3.17)

Substituting the coefficient in (3.16) proves (3.1). Fourier inversion gives (3.2), continuity, and vanishing at infinity. QED.

Zero exponents are handled by omission/limits exactly as in the source account02/B02 determinant-expansion proof.

## 4. Apply the newest partner packet to the live double-diffuse collar

Now impose the predecessor's double-diffuse conditions (1.2). Under the *unconditioned* product of `nu_S` and `nu_M`, let `q_k` be the residual row inclusion marginals of the physical E2 law `nu_M`; then `sum_k q_k=2`. Therefore

`1-delta_r=sum_k a_k q_k <=h_r sum_k q_k <1/2`,                  (4.1)

where `a_k=||S_k:||^2/F`. Hence

`delta_r>1/2`.                                                    (4.2)

The transpose gives `delta_c>1/2` as well. Thus as soon as `E=E2(M)>0`, Theorem 3.1 yields the unconditional branchwise bound

`boxed:
 integral_R |phi_Q(t)|dt
 <10 pi 2^(3/10)e^(4/5) (G E)^(-1/10)
 <86.079 (G E)^(-1/10),
}`                                                                  (4.3)

and

`boxed:
 ||p_Q||infinity
 <5 2^(3/10)e^(4/5)(G E)^(-1/10)
 <13.700 (G E)^(-1/10).
}`                                                                  (4.4)

This is the actual new integrated-Fourier receiver for the predecessor's rank-one-compatible double-diffuse geometry. It does **not** replace products of Schur entries by `2 x 2` Schur determinants and therefore is not defeated by the exact rank-one cancellation example from the predecessor.

Apply the newest designated account02/B02 packet (1.1): `G>Z/24`. If, at the scale-correct threshold,

`E2(M)>=Z^(2/3)/64`,                                              (4.5)

then

`G E > Z^(5/3)/1536`.                                            (4.6)

Equations (4.3)-(4.4) give the genuine universal-scale exits

`boxed:
 integral_R |phi_Q(t)|dt
 <179.281 Z^(-1/6),
 ||p_Q||infinity <28.534 Z^(-1/6).
}`                                                                  (4.7)

Thus the designated partner result has been applied to the concrete inequality (4.6), not merely cited.

## 5. Exact complement: the physical residual becomes small-E2

If (4.5) fails, then the remaining obstruction has the new physical-coordinate certificate

`boxed: E2(M)<Z^(2/3)/64.`                                       (5.1)

This is about the actual residual physical cross block `M`, not the algebraic Schur residual `S`, so no pre-Schur/post-Schur transfer is being asserted.

There is a useful quantitative refinement. Put

`F_M=||M||_F^2`, `rho_M=sr(M)=F_M/s_1(M)^2`

when `M!=0`. Since, for `x_j=s_j(M)^2`,

`sum_j x_j^2 <=(max_j x_j) sum_j x_j=s_1(M)^2 F_M`,

we have the exact elementary lower bound

`E2(M)=1/2(F_M^2-sum_j x_j^2)
      >=(F_M^2/2)(1-1/rho_M)`.                                  (5.2)

Therefore (5.1) implies the following concrete dichotomy:

- either `F_M<Z^(1/3)`; or
- `F_M>=Z^(1/3)`, in which case `E2(M)/F_M^2<1/64`, and (5.2) forces

`boxed: rho_M<32/31.`                                            (5.3)

At the exact endpoint `E2(M)=0`, `rank(M)<=1`.

So after the new Fourier branch is removed, the physical residual is either Frobenius-small at the natural `Z^(1/3)` scale or within about 3.23 percent (in stable rank) of a physical rank-one block. This is substantially more rigid than the preceding description solely in terms of a diffuse low-stable-rank Schur residual.

## 6. Why the theorem is compatible with the rank-one cancellation boundary

The predecessor exhibited a diffuse exact-rank-one Schur matrix `S=u v^T` for which pairwise extension disjointness is large but `E2(S)=0`. The present theorem never asks for `E2(S)`. Its first determinant family spends the *singleton* anchored mass

`G=D^2 sum_ij |S_ij|^2`,

which remains fully nonzero at rank one. The second determinant family spends `E2(M)` of the actual physical residual block. Hence the new theorem survives exact cancellation inside the Schur `2 x 2` minors and changes mechanism exactly where the previous route stalled.

If `M` itself is rank one, the second family vanishes and the theorem honestly stops; that is the new, source-visible obstruction rather than a hidden division by zero.

## 7. First unpaid implication after this run

The first unpaid interface is now

`QFORM-DOUBLEANCHOR-PHYSICAL-RESIDUAL-NEARRANK1-OR-SMALL-v1`:

> start from the partner packet `G=D^2||S||_F^2>Z/24`, the predecessor double diffusion `h_r,h_c<1/4`, and the new failure certificate `E2(M)<Z^(2/3)/64`; hence either `||M||_F^2<Z^(1/3)` or `sr(M)<32/31`. Use the star term `C P^(-1)R=S-M` through a product-preserving grouped-star / mixed-hub / true-pair receiver, without deleting `M-S` or declaring independence after the Schur shear.

The natural next split is physical: if `M` is small at the `Z^(1/3)` scale, most of the anchored Schur packet must be carried by the two-sided star after an additional scale split on `D`; if `M` is near rank one, use a rank-one-compatible grouped receiver on the **physical** residual and spend the nonzero star only as a second resource. No such final closure is claimed here.

No source-valid counterexample to the target-wide statement

`integral_R |E exp(it X^T A X)| dt <= C`

was found. The stronger universal Fourier criterion remains `OPEN_NOT_REFUTED`; the unrestricted bounded-density conjecture and unrestricted continuity statement remain OPEN.

## 8. Correction audit

This run uses only ORIGINAL-coordinate one-sided differencing and exact coefficient determinants. In particular:

- no law-uniform pointwise van-der-Corput decay is used;
- no independence is asserted after an orthogonal rotation or Schur shear;
- no arbitrary conditional-density cap is invoked;
- no arbitrary-joint coarea estimate is used;
- no single good cross minor is promoted to a theorem;
- no pre-Schur block estimate is transferred to a true symmetric Schur complement;
- no small dense coefficient tail is deleted on unbounded inputs;
- no Monte Carlo evidence is used as proof.

The physical residual `M` in Sections 4-5 is exactly the lower-right ORIGINAL-coordinate block in (2.1).

## 9. Finite algebra / constant audit

For random rectangular numerical blocks with invertible `P`, direct determinant evaluation verified

`det B[{anchor rows}+i,{anchor cols}+j]=det(P) S_ij`

and verified that the Family-M basis determinant equals `+/-det M[U,V]` to relative floating-point error below `10^-14`. These checks are diagnostics only.

Numerical constants used above:

`10*pi*2^(3/10)*e^(4/5)=86.0784537242`,
`5*2^(3/10)*e^(4/5)=13.6998114039`,
`(24*64)^(1/10)=2.08275948798`,
so the scale-threshold constants in (4.7) are `179.280716205` and `28.5334121851`.

## 10. Publication state

The full QFORM target remains OPEN. The theorem above is a branch theorem and needs independent end-to-end review before being treated as a full-candidate ingredient. Target-wide continuity is not proved; continuity is proved only on the explicit Fourier-L1 branches.

MODEL self-report: GPT-5.6 Sol. Configured thinking level / provider reasoning-token telemetry: UNKNOWN / not exposed.
