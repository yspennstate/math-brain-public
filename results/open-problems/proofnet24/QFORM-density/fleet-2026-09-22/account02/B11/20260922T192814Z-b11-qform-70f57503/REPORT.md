# account02/B11 — exact-ray atom overlap compiler for heavy-null indefinite rank three

**Run:** `20260922T192814Z-b11-qform-70f57503`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner-control revision before publication:** `2026-09-22.15`  
**Assignment:** Indefinite signatures / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and first unpaid implication

The sole target remains the full arbitrary-dimensional statement: for independent real coordinates with one-dimensional probability densities bounded by one and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or produce a genuine target-level counterexample.

The latest completed assigned-partner result actually applied is account03/B11 run `20260922T182528Z-account03-B11-QFORM-r12`, canonical source

`yspennstate/math-open-problems@e100de67669c37c8243fe9e389efc909f3179839`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T182528Z-account03-B11-QFORM-r12/REPORT.md`.

It puts an exact-rank-three heavy null pivot into the spectral normal form

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]]`,

with `kappa>=s` and `det M=-kappa^2 c`, and proves a sharp separated-leakage theorem. It leaves the overlapping residual coefficient geometry as the first local debt. The preceding account02/B11 run handled one exact four-Walsh-bank geometry. The first unpaid implication attacked here is therefore: **how much of the arbitrary overlap branch is already forced by an exact product-preserving ray atom, and what geometry genuinely remains when no such atom exists?**

This report answers that question quantitatively. Any exact projective ray carrying a fraction `alpha^2` of the saddle-coordinate energy gives a uniform bound depending only on `alpha`; the four Walsh directions are not special. An explicit harmonic Parseval family then shows `alpha -> 0` is genuinely possible under the exact target hypotheses, so a universal lower bound on such an atom is false. Finally, a small-coefficient perturbation construction shows why the remaining diffuse-angular branch cannot be closed by simply approximating directions and discarding the error under the present no-moment/no-support assumptions.

## 2. Source-pinned dependencies and correction state

The proof uses only these completed scoped results.

1. **Assigned partner heavy-null normal form.** The account03/B11 report cited above proves the normal form and the determinant identity. It also preserves the rank-two logarithmic control and identifies exactly how an independent third square can make it integrable.

2. **One-dimensional product projection cap.** account02/B11 canonical report

`yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`

proves that for independent density-cap-one variables and coefficients with squared sum one, the normalized linear form has density at most `sqrt(e)`.

3. **Orientation-free exact-rank-three scalar-pivot theorem.** Interactive rank-two-fusion report

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

proves, for an exact-rank-three matrix represented in independent cap-one physical coordinates, that a nonzero physical pivot `a`, physical range leverage `ell`, and nonzero spectral determinant `Delta` give

`||p_Q||_infinity <=128 (ell |a| |Delta|)^(-1/4)`,

with arbitrary induced affine terms allowed.

4. **Arbitrary-rank physical indefinite-pair theorem.** Interactive full-matrix pair report

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`

proves that if `s_3(A)>=sigma>0` and an ORIGINAL independent-coordinate principal pair is invertible indefinite, with `D=|det B|` and `eta=sigma_min(B)`, then

`||p_Q||_infinity <=3*400^(1/3) (D^2 eta sigma)^(-1/6)`.

This theorem retains the logarithmic saddle envelope and pays it using the third singular value; it allows arbitrary remaining spectrum.

The live correction inbox was refreshed through owner-control revision `.15`. In particular `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` forbids replacing an exact-zero mechanism by a merely small diagonal plus cross-row norm, and the earlier conditional-cap corrections forbid pretending rotated/grouped residual forms are conditionally independent. No such step is used below.

## 3. Exact projective-ray aggregation

Work in the partner's exact-rank-three heavy-null setting

`A=R M R^T`, `R^T R=I_3`,

where every singular value of `M` is at least `s>0`. After rotating only the three-dimensional spectral representation, not the independent physical coordinates, let the distinguished heavy physical row be

`r_0=(sqrt(h),0,0)`, `h>1/2`,

and let

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]]`, `kappa>=s`.                 (3.1)

Write every other physical row as `r_j=(u_j,w_j,v_j)`.

Partition the nonzero residual rows into their **exact projective ray classes**. Thus in a class `G` all rows are proportional. There is a unique convenient normalization

`r_j=b_j c_G`, `j in G`, `sum_(j in G) b_j^2=1`,                 (3.2)

where the signs are included in the `b_j`. Define

`Y_G=sum_(j in G) b_j X_j`.                                       (3.3)

The `Y_G` belonging to distinct classes are independent because the classes are disjoint sets of ORIGINAL coordinates. By the one-dimensional projection theorem,

`||p_(Y_G)||_infinity <= K:=sqrt(e)`.                              (3.4)

More importantly, (3.2) is exact: the three spectral linear forms depend on the variables in `G` only through `Y_G`. Therefore after ray aggregation the full quadratic form has exactly the same law as the quadratic form built from the independent variables `X_0,{Y_G}` and physical spectral rows

`c_0=(sqrt(h),0,0), {c_G}`.                                        (3.5)

No approximation, conditioning, or post-rotation independence assertion has occurred.

Let `beta_G` denote the second coordinate of `c_G`, i.e. its coefficient in the saddle variable `W`, and put

`alpha=max_G |beta_G|`.                                            (3.6)

Parseval gives

`sum_G beta_G^2=1`,                                                (3.7)

because the heavy row has zero second component. Thus `alpha>0`; if there are at most `m` exact ray classes then `alpha>=m^(-1/2)`.

## 4. Normalizing the ray variables without losing the third scale

Let `C` be the matrix with rows `c_0,{c_G}`. Then `C^T C=I_3` and the aggregated physical matrix is

`B=C M C^T`.                                                       (4.1)

Scale only the aggregated ray coordinates by `K`: set

`D=diag(1,K,...,K)`, `Z=D(X_0,{Y_G})^T`, `B'=D^(-1) B D^(-1)`.     (4.2)

The coordinates of `Z` are independent and each has density at most one, while `Q=Z^T B' Z` exactly.

### Lemma 4.1 — third singular value survives

`B'` has rank three and

`s_3(B')>=s/K^2=s/e`.                                              (4.3)

**Proof.** Put `F=D^(-1)C`. Since `D^(-2)>=K^(-2)I`,

`F^T F=C^T D^(-2) C >=K^(-2)I_3`.

Write the polar factorization `F=UG`, where `U^T U=I_3` and `G=(F^T F)^(1/2)>=K^(-1)I`. The nonzero eigenvalues of `B'=F M F^T` are those of `G M G`. Hence

`sigma_min(G M G)>=sigma_min(G)^2 sigma_min(M)>=s/K^2`. QED.

### Lemma 4.2 — a strong ray keeps physical leverage

Let `G_*` attain (3.6), and let `ell=||c_(G_*)||^2`. Then

`ell>=alpha^2`                                                     (4.4)

and the physical range leverage `ell'` of the corresponding coordinate for `B'` satisfies

`ell'>=ell/K^2>=alpha^2/e`.                                        (4.5)

**Proof.** Before scaling, `P=CC^T` is the orthogonal projection onto `ran(C)` and `P_(G_*G_*)=ell`. The vector `z=D^(-1)P e_(G_*)` belongs to `ran(D^(-1)C)=ran(B')`, its `G_*` coordinate is `ell/K`, and `||z||^2<=||P e_(G_*)||^2=ell` because `D^(-1)` is a contraction. The variational formula for projection leverage gives (4.5). QED.

Finally, the heavy-to-strong-ray physical coefficient is rigid. The first row of (3.1) is `(0,kappa,0)`, so

`a:=B'_(0,G_*)=sqrt(h) kappa beta_(G_*)/K`,

and therefore

`|a|>=a_0:=s alpha/sqrt(2e)`.                                      (4.6)

The heavy scalar diagonal is exactly zero.

## 5. Main theorem: an exact ray atom pays arbitrary overlap

### Theorem 5.1 — QFORM-HEAVY-NULL-RAY-ATOM-v1

In Sections 3–4,

`||p_Q||_infinity <= s^(-1) max(C_1 alpha^(-3/4), C_2 alpha^(-5/6))`, (5.1)

where

`C_1=128*2^(1/8)*e^(9/8) <429.953`,

`C_2=3*400^(1/3)*2^(7/12)*e^(7/12) <59.350`.                      (5.2)

Consequently, if the residual frame has at most `m` exact projective ray classes,

`||p_Q||_infinity <= s^(-1) max(C_1 m^(3/8), C_2 m^(5/12))`.       (5.3)

For example `alpha>=1/2` gives a bound below `724/s`, and `alpha>=1/4` gives a bound below `1217/s`.

The theorem applies equally to signatures `(+,+,-)` and `(+,-,-)` after negating the form.

### Proof

Let

`b=B'_(G_*G_*)`.

There are two exhaustive cases.

**Case 1: the strong ray has visible scalar curvature, `|b|>=a_0`.**

Apply the exact-rank-three scalar-pivot theorem to coordinate `G_*`. By (4.5) its range leverage is at least `alpha^2/e`. By Lemma 4.1 each of the three nonzero singular values of `B'` is at least `s/e`, so the magnitude of the nonzero spectral determinant is at least `(s/e)^3`. Hence

`||p_Q||_infinity`
` <=128 [(alpha^2/e) a_0 (s/e)^3]^(-1/4)`
` <=128*2^(1/8)*e^(9/8) alpha^(-3/4) s^(-1)`.                    (5.4)

**Case 2: the strong ray scalar curvature is small, `|b|<a_0`.**

The ORIGINAL independent-coordinate principal pair on the heavy coordinate and `G_*` is

`[[0,a],[a,b]]`.                                                    (5.5)

Its determinant is `-a^2`, so it is automatically invertible indefinite. Its smaller singular value is

`eta=(sqrt(b^2+4a^2)-|b|)/2 >= |a|/2 >=a_0/2`,                    (5.6)

using `|b|<a_0<=|a|`. Thus the pair determinant magnitude `D_pair=a^2>=a_0^2`. Apply the arbitrary-rank physical-pair theorem and Lemma 4.1:

`||p_Q||_infinity`
` <=3*400^(1/3) [a_0^4 (a_0/2) (s/e)]^(-1/6)`
` =3*400^(1/3)*2^(7/12)*e^(7/12) alpha^(-5/6) s^(-1)`.            (5.7)

This proves (5.1). Equation (5.3) follows from (3.7). QED.

The proof is genuinely product preserving. Exact ray aggregation is performed before any reciprocal determinant payment, and it is legal only because the quadratic form depends on each class through the single normalized sum (3.3). No conditional density cap is introduced.

## 6. Where the rank-two logarithm goes

The rank-two obstruction is unchanged: a saddle product such as `2UV` can have logarithmically unbounded density near zero for bounded-density independent inputs. Nothing above claims otherwise.

The third direction enters Theorem 5.1 at exactly the two places where rank two cannot pay:

1. in Case 1, the three nonzero singular values force a nonzero rank-three spectral determinant, which the scalar-pivot half-Riesz theorem uses to make the saddle contribution summable;
2. in Case 2, `s_3(B')>=s/e` protects the Schur remainder in the full-matrix pair theorem, whose quarter-power small-ball estimate averages the logarithmic pair envelope.

If the third singular value is removed, both payments lose their uniform scale and the rank-two logarithmic example is recovered. This gives a precise mechanism for both indefinite signatures in the ray-atom branch.

## 7. Source-valid obstruction: a ray atom need not exist at fixed scale

A universal lower bound on `alpha` is false even for exact rank three. Fix `h=3/4`, let `m>=5`, set `theta_j=2 pi j/m`, and take residual rows

`c_j=(1/(2 sqrt(m)), sqrt(2/m) cos(theta_j), sqrt(2/m) sin(theta_j))`, `j=0,...,m-1`,

with heavy row

`c_0^heavy=(sqrt(3)/2,0,0)`.                                      (7.1)

The trigonometric identities `sum cos= sum sin=sum cos sin=0` and `sum cos^2=sum sin^2=m/2` give

`C^T C=I_3`.                                                       (7.2)

Take

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (7.3)

whose spectrum is `{1,1,-1}`. Therefore `A_m=C M_0 C^T` is an exact target matrix with the same three nonzero eigenvalues.

Because every residual row has the same positive first coordinate, two distinct residual rows cannot be proportional. Hence there are exactly `m` distinct projective ray classes and

`alpha_m=max_j sqrt(2/m)|cos(theta_j)|=sqrt(2/m) ->0`.             (7.4)

Moreover every individual heavy-to-residual coefficient is at most `sqrt(3/(2m))`, and every residual scalar diagonal is `O(1/m)` (indeed its magnitude is at most `3/m`). Thus neither a fixed exact ray atom nor a fixed original-coordinate pivot/pair can be forced from the target hypotheses.

This is a counterexample to the stronger structural shortcut

`three large eigenvalues + heavy null row => a ray atom alpha>=alpha_0>0`,

not a counterexample to QFORM. It shows the genuinely unresolved overlap chamber is an **angularly diffuse heavy-null frame** rather than merely a failure to choose the correct Walsh signs.

## 8. Why naive finite-sector approximation is not yet a proof

It is tempting to put the angularly diffuse rows into finitely many narrow sectors, replace each sector by one exact ray, and invoke Theorem 5.1. Under the target assumptions there is no moment or support bound that makes this perturbative replacement legitimate.

A simple exact falsifier of the required output-error estimate is as follows. Let

`A_0=diag(1,1,-1,0)`, `E=epsilon e_4 e_4^T`, `A=A_0+E`,             (8.1)

where `epsilon>0` is arbitrarily small. Both `A_0` and `A` have the required three large eigenvalues. Let the fourth independent coordinate be uniform on `[R,R+1]`, which has density one. Then the perturbation term is

`X^T E X=epsilon X_4^2`,

whose essential support diameter is

`epsilon[(R+1)^2-R^2]=2 epsilon R+epsilon`.                        (8.2)

For any prescribed `L`, choosing `R=L/(2epsilon)` makes (8.2) exceed `L` while `||E||_op=epsilon` tends to zero. Thus **small coefficient/operator error does not imply small random output error uniformly over the admissible laws**. This refutes only a perturbative sector-replacement proof that discards the error by size; it does not refute a density-stability theorem using deeper product structure, and it is not a QFORM counterexample.

Therefore the next compiler must keep the within-sector residual exactly and route it nonperturbatively, for example into a ridge/diffuse certificate or an already-controlled physical pair, rather than treating it as a small additive random variable.

## 9. First unpaid implication after this run

The exact-ray part of `QFORM-OVERLAP-COMPILER-v1` is now paid. The first genuinely unpaid implication is:

**QFORM-ANGULAR-DIFFUSE-OVERLAP-v1.** In the partner's heavy-null exact-rank-three normal form, assume every exact projective ray carries arbitrarily small `W` energy. Prove a dimension-free product-preserving alternative that either

1. converts the angular spread itself into a ridge/regularized-determinant certificate;
2. exposes a quantitative ORIGINAL-coordinate indefinite pair; or
3. groups finitely many sectors while retaining the within-sector residual exactly and paying it through an existing theorem.

The harmonic family (7.1) shows this branch is nonempty. Section 8 shows coefficient closeness alone cannot remove it. Arbitrary additional spectrum remains a separate debt unless a quantitative physical pair is exposed, because the full-matrix pair theorem then already tolerates that spectrum.

## 10. Exact regression

`VERIFY.py` beside this report checks the constants, the exact harmonic Parseval identities and spectrum for `m=8,16,32,64,128`, the `alpha_m=sqrt(2/m)` decay, shrinking local heavy couplings/diagonals, and the perturbation-output oscillation. Its captured output terminates

`QFORM_RAY_ATOM_COMPILER_CHECK_PASS`.

The finite calculation is algebraic regression only; Theorem 5.1 is the symbolic argument above.

## 11. Status

`ESSENTIAL_STEP_APPLIED`. The four-Walsh overlap theorem is upgraded to every heavy-null exact-rank-three frame having a quantitatively non-negligible exact projective ray atom. A target-valid harmonic family proves that no universal atom exists, and the remaining angularly diffuse branch is now explicit. The unrestricted arbitrary-frame, arbitrary-spectrum QFORM conjecture remains `OPEN / NOT PROVED`. Essential boundedness is proved only in the stated branch; continuity is not claimed here.