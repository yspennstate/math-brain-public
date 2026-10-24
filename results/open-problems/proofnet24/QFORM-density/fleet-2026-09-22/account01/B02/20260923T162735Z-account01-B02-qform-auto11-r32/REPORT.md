SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T16:27:35Z.
attacking: the double-anchor small-E2 collar by replacing the physical residual E2 packet with either physical star-leg E2 packet, using the same cross-disjoint one-sided-Weyl compiler.

# account01/B02 — star-leg E2 Fourier receiver and triple near-rank-one collapse

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`  
**Continuity:** proved on the new explicit Fourier-L1 branches below; unrestricted continuity remains open.  
**Brain state:** `WITHOUT_VERIFIED_BRAIN`.

The target remains the exact arbitrary-law statement: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, compact support, iid assumption, Gaussianity, log-concavity, connected support, or post-rotation independence is used.

## 1. Fresh sources actually used

Current owner control remained QFORM-only, owner revision `2026-09-22.15` at startup. The live correction ledger was read before the argument and is respected below.

The newest designated partner used at an actual inequality is account02/B02:

`yspennstate/math-open-problems@4029b9b55694ce709e43c62d2729e89108fbdede`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T141147Z-account02-B02-QFORM-auto11/REPORT.md`.

Its live invertible second-anchor packet is a physical ORIGINAL-coordinate cross block

`B = [[P,R],[C,M]]`,

where `P` is a physical `2 x 2` invertible block, `D=|det P|`,

`S = M-C P^{-1}R`, `F=||S||_F^2`, `G=D^2 F`,

and, on the branch under consideration,

`G > Z/24`,                                                     (1.1)

where `Z` is the parent third exterior-volume currency. The partner also proves a Fourier-L1 exit when the Schur residual stable rank is sufficiently away from the low-rank endpoint.

My immediately preceding B02 result is

`yspennstate/math-open-problems@1a1e6cb54f557b5b60aa1cef4928634aaccd1ff4`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T152138Z-account01-B02-qform-auto11-r31/REPORT.md`.

It proved the cross-disjoint compiler `QFORM-DOUBLEANCHOR-E1E2-CROSSDISJOINT-L1-v1` and reduced its surviving invertible-anchor collar to

`h_r:=max_i ||S_{i:}||_2^2/F <1/4`,
`h_c:=max_j ||S_{:j}||_2^2/F <1/4`,                              (1.2)

and, after the physical-residual E2 branch fails,

`E2(M) < Z^(2/3)/64`.                                            (1.3)

This run changes the second determinant family: instead of spending `E2(M)`, it spends `E2(C)` or, after transpose, `E2(R)`. Thus it is not a repetition of the preceding mechanism on the same coefficient packet.

## 2. Setup and exact determinant families

Fix the physical block

`B = [[P,R],[C,M]]`,                                              (2.1)

with `P` of size `2 x 2`, `C` of size `m x 2`, `R` of size `2 x n`, and `M` of size `m x n`. Let

`D=|det P|>0`,
`S=M-C P^{-1}R`,
`F=||S||_F^2`,
`G=D^2F`.                                                         (2.2)

Assume `F>0`. For the left star leg define

`E_C=E2(C)=sum_{|U|=2} det(C[U,:])^2`.                           (2.3)

If `E_C>0`, define two deterministic determinant laws:

`nu_S(i,j)=|S_ij|^2/F`,                                          (2.4)

and

`nu_C(U)=det(C[U,:])^2/E_C`, `|U|=2`.                            (2.5)

Draw `(i,j)~nu_S` and `U~nu_C` independently and set

`delta_C=P(i notin U)`.                                          (2.6)

Everything here is coefficient geometry in the original coordinate basis.

There are two positive basis families in the target-bank one-sided-Weyl Brascamp--Lieb determinant expansion.

### Family S: anchored singleton

Choose the two physical source rows of `P`, one residual source row `i`, and every residual target coordinate vector except the vector indexed by `j`. This is a basis of the `n+2`-dimensional target bank. Block elimination gives exactly

`det basis = +/- det(P) S_ij`.                                   (2.7)

Therefore the total squared determinant mass of this family is

`sum_ij D^2 |S_ij|^2 = G`.                                      (2.8)

### Family C: two left-star rows

Choose two residual source rows `U={u,v}` and all `n` residual target coordinate vectors. Expanding along those coordinate vectors leaves the two anchor columns and gives

`det basis = +/- det C[U,:]`.                                    (2.9)

Hence the total squared determinant mass is exactly

`sum_|U|=2 det(C[U,:])^2=E_C`.                                  (2.10)

These are literal physical coefficient determinants. No random variable is rotated or Schur-sheared.

## 3. Main theorem — `QFORM-DOUBLEANCHOR-STARLEG-E2-L1-v1`

### Theorem 3.1

In the setup above, if `E_C>0` and `delta_C>0`, then the full ambient quadratic form satisfies

`boxed:
 integral_R |phi_Q(t)| dt
 <= 10*pi*2^(1/5)*e^(4/5)*(delta_C G E_C)^(-1/10).
`                                                                    (3.1)

Consequently the law has a bounded continuous density vanishing at infinity, with

`boxed:
 ||p_Q||_infinity
 <=5*2^(1/5)*e^(4/5)*(delta_C G E_C)^(-1/10)
 <12.783*(delta_C G E_C)^(-1/10).
`                                                                    (3.2)

The transposed statement holds with

`E_R=E2(R)=sum_{|V|=2}det(R[:,V])^2`                              (3.3)

and the corresponding column-disjoint probability.

### Proof

One-sided Weyl differencing in the target original-coordinate bank gives the same source-valid inequality as in the preceding B02 compiler:

`|phi_Q(t)|^2
 <= integral prod_(r in source bank) h_r((B w)_r)
             prod_(l in target bank) g_l(w_l) dw`,                (3.4)

where

`h_r(s)=|hat f_r(2ts)|`,
`g_l=f_l*tilde(f_l)`,
`0<=g_l<=1`, `integral g_l=1`.                                   (3.5)

All arbitrary same-bank phases and affine terms disappear only through this legitimate differencing step. No pointwise scalar quadratic stationary-phase estimate is used.

Condition the independent determinant samples `(i,j)~nu_S` and `U~nu_C` on the event `i notin U`. Denote the conditioned laws by `mu_S,mu_C`. The standard relative-entropy identity for conditioning a product law gives

`D(mu_S||nu_S)+D(mu_C||nu_C) <= log(1/delta_C)`.                 (3.6)

Let `a_k^S` be the conditioned singleton-row marginals and `a_k^C` the conditioned pair-row marginals. Put

`alpha_k=(a_k^S+a_k^C)/2`.                                       (3.7)

Because the singleton and the pair are pointwise disjoint under the conditioning,

`0<=alpha_k<=1/2`, `sum_k alpha_k=3/2`.                          (3.8)

Let `beta_l` be the conditioned column marginal of the singleton law; `sum_l beta_l=1`. Assign Brascamp--Lieb exponents in (3.4) as follows:

- each of the two anchor source-row forms: `1/2`;
- residual source-row form `k`: `alpha_k`;
- each anchor target-coordinate map: exponent `0`;
- residual target-coordinate map `l`: `d_l=1-beta_l/2`.

The total exponent is correct:

`1 + 3/2 + sum_l(1-beta_l/2)
 = 5/2 + n-1/2
 = n+2`.                                                          (3.9)

The basis family S has the fixed anchor-row weight `(1/2)^2=1/4`; family C has no corresponding loss. The latter is therefore at least as favorable as the second family in the already-proved r31 E1(S) x E2(M) compiler, where both positive basis families carried a fixed factor `1/4`. Retaining only (2.7) and (2.9), applying weighted AM--GM under `mu_S,mu_C`, and using (3.6), we may conservatively reuse the r31 determinant bound

`BL <= sqrt(2) delta_C^(-1/4)(G E_C)^(-1/4)
      prod_k alpha_k^(-alpha_k/2)
      prod_l d_l^(-d_l/2)`.                                      (3.10)

This inequality is deliberately not sharpened by the improved fixed-factor geometry.

For every source exponent `0<c<=1/2`, sharp Hausdorff--Young gives the same scalar integral used in the preceding compiler,

`integral h_r(s)^(1/c) ds
 <= (pi/|t|) sqrt(c)
    (1-c)^(-(1-c)/(2c)).`                                        (3.11)

After raising to BL powers, the `c^(c/2)` factors cancel those in (3.10). The two anchor source rows contribute total source weight one, and the residual source weights sum to `3/2`, so the total time power in `|phi|^2` is

`(pi/|t|)^(5/2)`.                                                 (3.12)

The row entropy is bounded exactly as before by `e^(3/4)`. For the target difference densities, the two zero anchor-coordinate exponents are omitted, and the residual coordinate exponents `d_l=1-beta_l/2` lie in `[1/2,1]`. The total missing coordinate weight equals

`2 + sum_l beta_l/2 = 5/2`,                                      (3.13)

the same safe total used in r31. The same endpoint-safe Young estimate therefore contributes at most `e^(5/4)`. Thus the total entropy factor can again be bounded by `e^2`, yielding

`|phi_Q(t)|^2
 <= sqrt(2)e^2 pi^(5/2)
    delta_C^(-1/4)(G E_C)^(-1/4)|t|^(-5/2)`.                    (3.14)

Taking square roots,

`|phi_Q(t)|
 <= min{1,
  2^(1/4)e pi^(5/4)(delta_C G E_C)^(-1/8)|t|^(-5/4)}.`          (3.15)

Finally

`integral_R min(1,A|t|^(-5/4)) dt=10 A^(4/5)`.                 (3.16)

Substitution proves (3.1). Fourier inversion proves (3.2), and `phi_Q in L1` gives a continuous representative tending to zero at infinity. QED.

Zero BL exponents are handled by omission or the same limiting argument as in the preceding source theorem.

## 4. Automatic disjointness in the live double-diffuse collar

Assume the inherited row diffusion in (1.2). Under the unconditioned determinant laws let

`a_k=||S_{k:}||_2^2/F`,                                          (4.1)

and let `q_k=P_(nu_C)(k in U)`. Since `nu_C` is a two-row minor law,

`sum_k q_k=2`.                                                    (4.2)

Therefore

`1-delta_C=sum_k a_k q_k
 <= h_r sum_k q_k
 <1/2`,                                                          (4.3)

so

`boxed: delta_C>1/2.`                                             (4.4)

By transposition, if `E_R>0`, the inherited column diffusion gives the analogous

`boxed: delta_R>1/2.`                                             (4.5)

Hence Theorem 3.1 gives, whenever `E_C>0`,

`integral |phi_Q|
 < 10*pi*2^(3/10)e^(4/5)(G E_C)^(-1/10)`,                       (4.6)

and the same formula with `E_R`. Numerically the coefficient in (4.6) is `86.078454`.

## 5. Actual application of the designated account02/B02 packet

Now use the partner inequality (1.1) at a concrete scale. If

`E_C >= Z^(2/3)/64`,                                              (5.1)

then, by `delta_C>1/2` and `G>Z/24`,

`delta_C G E_C > Z^(5/3)/3072`.                                 (5.2)

Theorem 3.1 therefore yields

`boxed:
 integral_R |phi_Q(t)|dt <179.280717 Z^(-1/6),
 ||p_Q||_infinity <28.533413 Z^(-1/6).
`                                                                    (5.3)

Exactly the same implication holds when

`E_R >= Z^(2/3)/64`.                                              (5.4)

This is the required use of the designated partner at an actual inequality: its packet `G>Z/24` is multiplied by the star-leg exterior volume and the automatically positive disjointness probability to produce a scale-homogeneous Fourier-L1 certificate.

## 6. Failure collapses all three physical blocks toward rank one or small size

The preceding r31 theorem already pays the analogous branch if

`E2(M)>=Z^(2/3)/64`.                                              (6.1)

After removing (5.1), (5.4), and (6.1), the surviving physical coefficient geometry obeys

`boxed:
 E2(C), E2(R), E2(M) < Z^(2/3)/64.
}`                                                                    (6.2)

This has an elementary but useful stable-rank consequence. For any nonzero matrix `H`, let

`F_H=||H||_F^2`, `rho_H=sr(H)=F_H/s_1(H)^2`.

Writing `x_j=s_j(H)^2`,

`E2(H)=1/2[(sum x_j)^2-sum x_j^2]
      >= F_H^2/2*(1-1/rho_H)`,                                  (6.3)

because `sum x_j^2 <= (max x_j)sum x_j=F_H^2/rho_H`.

Consequently every `H in {C,R,M}` satisfies the explicit alternative

`boxed:
 F_H < Z^(1/3)
 or
 rho_H <32/31.
}`                                                                    (6.4)

Indeed, if `F_H>=Z^(1/3)`, then (6.2) gives `E2(H)/F_H^2<1/64`; combining with (6.3) gives `1-1/rho_H<1/32` and hence `rho_H<32/31`.

At the exact endpoint `E2(H)=0`, `rank(H)<=1`.

Thus the unresolved invertible-anchor geometry is no longer merely “small E2 in M”: **each of the physical residual and both physical star legs is either Frobenius-small at the natural `Z^(1/3)` scale or within 3.23 percent in stable rank of rank one.**

## 7. Exact compound identity for the two-sided star

Put

`T=C P^{-1}R`.                                                    (7.1)

Because `C` has two columns and `R` two rows, the second exterior power factorizes into a column vector, one scalar, and a row vector:

`wedge^2 T=(wedge^2 C)(det P^{-1})(wedge^2 R)`.                  (7.2)

Taking Frobenius norms and using Cauchy--Binet gives the exact identity

`boxed:
 D^2 E2(T)=E2(C)E2(R).
}`                                                                    (7.3)

Therefore the double star-leg failure (6.2) also implies

`boxed:
 D^2 E2(CP^{-1}R) < Z^(4/3)/4096.
}`                                                                    (7.4)

This is coefficient currency only. I do not treat the algebraic Schur shear as preserving product independence and do not delete `T` as a small random quadratic perturbation.

## 8. Exact zero-E2 endpoint: a finite rank-one-star normal form

Suppose, more rigidly,

`E2(C)=E2(R)=E2(M)=0`.                                            (8.1)

Then

`rank C<=1`, `rank R<=1`, `rank M<=1`,                           (8.2)

and therefore `rank T<=1`. Since

`S=M-T`,                                                          (8.3)

we have

`rank S<=2`.                                                      (8.4)

Block Gaussian elimination is an algebraic rank identity, so

`rank B = rank P + rank S =2+rank S <=4`.                        (8.5)

The live packet `G=D^2||S||_F^2>0` excludes `S=0`. Hence the exact all-zero-E2 survivor has `rank S` equal to one or two. In the genuinely rank-two case it admits the explicit coefficient normal form

`C=u c^T`, `R=r v^T`, `M=a b^T`,                                (8.6)

so that, with

`tau=c^T P^{-1} r`,                                               (8.7)

`T=tau u v^T`,
`S=a b^T-tau u v^T`.                                             (8.8)

Thus the exact endpoint is a physical rank-one residual plus a rank-one two-sided star, over an invertible two-coordinate anchor. No diagonalization of random coordinates is involved.

I do **not** claim this rank-four endpoint is automatically controlled by an existing rank-one-bilinear-plus-square theorem: the currently available grouped rank-one theorem does not permit arbitrary quadratic self-curvature in the active partner bank, which is still present here. That is the next genuine gap rather than a hidden assumption.

## 9. First unpaid implication after this run

The first unpaid interface is now

`QFORM-DOUBLEANCHOR-TRIPLE-NEARRANK1-STAR-CLOSURE-v1`:

> Starting from the partner packet `G=D^2||S||_F^2>Z/24`, double diffusion `h_r,h_c<1/4`, and the failure certificates `E2(C),E2(R),E2(M)<Z^(2/3)/64`, exploit the fact that every physical block `C,R,M` is either Frobenius-small at scale `Z^(1/3)` or has stable rank `<32/31`. Close the resulting rank-one-star/rank-one-residual geometry by a product-preserving grouped-hub, physical-pair, or mixed rank-one receiver that retains arbitrary within-bank quadratic curvature.

The exact endpoint is (8.6)-(8.8). The approximate endpoint must retain all transverse terms; a small matrix coefficient is not a uniformly small random quadratic perturbation under arbitrary unbounded cap-one input laws.

No source-valid counterexample to the target-wide stronger criterion

`integral_R |E exp(it X^T A X)|dt <= C`                           (9.1)

was found. It remains `OPEN_NOT_REFUTED`. The unrestricted bounded-density conjecture and unrestricted continuity statement remain OPEN.

## 10. Correction audit

This run uses only original-coordinate product structure, one-sided differencing, exact physical determinant families, and coefficient exterior-power identities. In particular:

- no law-uniform pointwise quadratic-phase decay is used;
- no independence is asserted after spectral rotation or Schur shear;
- no arbitrary conditional-density cap is used;
- no arbitrary-joint coarea theorem is used;
- no fixed good `2 x 2` cross minor is promoted to a theorem;
- no pre-Schur estimate is transferred to a true symmetric Schur complement;
- no small dense matrix tail is deleted on unbounded laws;
- no numerical histogram or interval-extremality assumption is used.

The stronger Fourier-L1 branch proves continuity only where (3.1) applies.

## 11. Constant and scale audit

The conservative theorem coefficient is

`10*pi*2^(1/5)*e^(4/5)=80.3140371852`,                            (11.1)

and the density coefficient is

`5*2^(1/5)*e^(4/5)=12.7823760177`.                               (11.2)

With `delta>1/2`, `G>Z/24`, and `E_leg>=Z^(2/3)/64`, the product loss is

`(2*24*64)^(1/10)=3072^(1/10)=2.23224634807`,                    (11.3)

which gives exactly the displayed numerical constants

`179.280716205` and `28.5334121851`.                              (11.4)

All exponents are scale-homogeneous: `G` has coefficient degree six, `E_C` and `E_R` degree four, so `(G E_leg)^(-1/10)` has degree minus one, as required for a density/Fourier-time scale.

## 12. Publication status

This is a new supporting branch theorem and structural reduction, not the full conjecture. It has not received two independent end-to-end reviews. A full candidate still requires every target quantifier and two actual independent reviews.

MODEL self-report: `GPT-5.6 Sol`. Thinking level and provider reasoning-token/time counters: `UNKNOWN/null; not exposed`.
