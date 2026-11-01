SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T12:13:57Z.
attacking: replace local six-row Hellinger extraction by a global compatibility-Hellinger coupling of physical third-volume bases, and identify the exact overlap endpoint where the newest fleet02/B04 theorem takes over.

# fleet01/B04 — global compatibility-Hellinger compiler; local six-row extraction is false

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control refreshed before publication:** `yspennstate/math-research-brain@ed4752c378fd8daea62429a34678122eb0e87c65`; revision still `2026-09-22.15`, QFORM only.  
**Outcome:** `ESSENTIAL_MISSING_IMPLICATION_REFUTED_AND_REPLACED / SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / FULL_TARGET_OPEN`.  
**Continuity:** proved in the new Fourier theorem below; full-target continuity remains open.  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`.

## 1. What changed

The preceding B04 result `QFORM-SIXROW-COMPLEMENT-HELLINGER-VOLUME-v1` attached to one six-row packet the currency

`C_R(M)=sum_{S subset R, |S|=3} sqrt(a_S a_{R\S})`,

where

`a_S=sum_{|T|=3} det(M[S,T])^2`.

Its first advertised missing implication asked whether the bare three-large-eigenvalue hypothesis could force **one** original-coordinate cut and six-row set with `C_R>=c0` universally, or otherwise route a support defect.

That direct local-extraction route is false. Section 4 below gives a target-valid family for which **every original-coordinate cut and every six-row set** has `C_R<=8/k^3 ->0`, even though the natural cross block has `E3=1` and the form is uniformly controlled. This is an intermediate-route counterexample, not a counterexample to QFORM.

The replacement proved here is global rather than local: aggregate many compatible pairs of physical row bases before Fourier inversion. The resulting exact determinant/entropy currency automatically pays the diffuse repeated-frame family with no loss.

## 2. Sources actually used

1. **Sharp arbitrary-weight third-volume Fourier theorem.**  
   `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`, source
   `yspennstate/math-open-problems@b967ff246e7e5b480b098c17f01cd0fc93072991`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T014717Z-fleet02-B04-QFORM-auto11-cont/REPORT.md`.
   For a probability weight `w` on nonzero physical `3x3` minors, row marginals `alpha_i<=q/2`, `1<=q<3/2`, and

   `G(w)=exp(H(w)+sum_w log det(M_ST)^2)`,

   it proves

   `||p_Q||_inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`

   with arbitrary same-bank quadratic curvature, outside couplings and affine terms in original coordinates. Its characteristic-function envelope is integrable, hence `p_Q in C_0(R)`.

2. **Predecessor six-row compiler.**  
   `QFORM-SIXROW-COMPLEMENT-HELLINGER-VOLUME-v1`, source
   `yspennstate/math-open-problems@d57e4401409946cb300e16500f1c85906b943a49`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T104329Z-fleet01-B04-QFORM-auto11/REPORT.md`.

3. **Newest designated partner fleet02/B04.**  
   `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`, source
   `yspennstate/math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`.
   If `Z=E3(M)>0` and no supported minor law has every constrained-side row marginal strictly below `3/4`, it proves

   `||p_Q||_inf <= 6*4^(1/6) Z^(-1/6)`,

   with the sharper `6 Z^(-1/6)` in its coloop/rank-one-flat cases. Its proof retains arbitrary self blocks and outside conditioning.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea bound, positive conditional projection-density moment, or single-minor lower bound is used.

## 3. New theorem — compatibility-Hellinger coupling compiler

Let `I,J` be disjoint ORIGINAL coordinate banks and let `M=A[I,J]`. For every physical row triple `S subset I`, put

`a_S := sum_{T subset J, |T|=3} det(M[S,T])^2`
`     = det(M[S,J] M[S,J]^T)`

by Cauchy--Binet, and let `B` denote the finite family of triples with `a_S>0`.

Choose **any symmetric compatibility relation** `E subset B x B`: `(S,T) in E` iff `(T,S) in E`. Assume

`B_E := sum_{(S,T) in E} sqrt(a_S a_T) >0`.                    (3.1)

Define the symmetric pair law

`Pi(S,T) = 1_E(S,T) sqrt(a_S a_T)/B_E`,                         (3.2)

and let `mu` be either marginal. For each physical row `i`, set

`alpha_i = P_mu(i in S)`,
`beta_i  = P_Pi(i in S intersect T)`,
`beta_*  = max_i beta_i`.                                      (3.3)

Finally let `H_Pi(T|S)` be the ordinary Shannon conditional entropy of the second base given the first under `Pi`.

### Theorem `QFORM-COMPATIBILITY-HELLINGER-COUPLING-v1`

If `beta_*<1/2`, then for every admissible independent cap-one product input law, in the full arbitrary-self-block/outside-coupling scope of the weighted Fourier theorem,

`boxed:
 ||p_Q||_inf
 <= [3e/((1-2 beta_*) sqrt(1+beta_*))]
    [B_E exp(-H_Pi(T|S))]^(-1/6).
`                                                                    (3.4)

The density has a representative in `C_0(R)`.

If every first-coordinate base has at most `D` compatible partners, then

`H_Pi(T|S)<=log D`,

so the simpler explicit consequence is

`boxed:
 ||p_Q||_inf
 <= [3e/((1-2 beta_*) sqrt(1+beta_*))]
    (B_E/D)^(-1/6).
`                                                                    (3.5)

### Proof

Because `Pi` is symmetric, both of its marginals equal `mu`. For a fixed physical row `i`, let

`A={i in S}`, `B={i in T}`.

Then `P(A)=P(B)=alpha_i` and `P(A intersect B)=beta_i`. Inclusion-exclusion gives the exact identity

`2 alpha_i = P(A union B)+beta_i <=1+beta_i`.                   (3.6)

Hence

`alpha_i <= (1+beta_*)/2`.                                     (3.7)

Set

`q=1+beta_*`.

The assumption `beta_*<1/2` is exactly `1<=q<3/2`, and (3.7) is the required row-marginal gate `alpha_i<=q/2`.

Next compute the determinant/entropy currency. From (3.2), on the support of `Pi`,

`log Pi(S,T)=(1/2)log a_S+(1/2)log a_T-log B_E`.

By symmetry,

`H(Pi)=log B_E - sum_S mu(S) log a_S`.                          (3.8)

The chain rule gives

`H(Pi)=H(mu)+H_Pi(T|S)`.                                       (3.9)

Combining (3.8)--(3.9),

`boxed:
 exp(H(mu)+sum_S mu(S)log a_S)
 = B_E exp(-H_Pi(T|S)).
`                                                                    (3.10)

Now lift each row triple `S` to column triples by the canonical conditional law

`q_S(C)=det(M[S,C])^2/a_S`.                                    (3.11)

For the full minor law `w(S,C)=mu(S)q_S(C)`, the Gibbs identity inside each fixed row triple gives

`H(w)+sum_(S,C) w(S,C)log det(M[S,C])^2`
` =H(mu)+sum_S mu(S)log a_S`.                                  (3.12)

Therefore the full weighted-Fourier currency is exactly

`G(w)=B_E exp(-H_Pi(T|S))`.                                    (3.13)

Apply the sharp arbitrary-weight theorem at `q=1+beta_*`. Since

`3-2q=1-2beta_*`,

(3.4) follows. The imported theorem supplies an integrable characteristic-function envelope, hence a continuous density vanishing at infinity. Finally, if every conditional support has size at most `D`, then `H(T|S)<=log D`, which yields (3.5). QED.

### Structural interpretation

This theorem contains the preceding six-row construction as the special case where `E` is a complement matching inside one six-row set: then `beta_*=0`, `H(T|S)=0`, and (3.10) becomes exactly the former complement-Hellinger currency.

More importantly, it permits many compatible partners per base. The entropy term `exp(-H(T|S))` cancels the raw growth in the number of compatible pairs. This is precisely what is needed in diffuse frames where every single six-row packet is tiny.

## 4. Exact correction — no universal single-six-row currency, even after optimizing the cut

Fix `k>=2`. Let

`V_3 = I_3-(2/3) 1 1^T
     = (1/3)[[1,-2,-2],[-2,1,-2],[-2,-2,1]]`,

so `V_3` is orthogonal and every entry is nonzero. Let `U_k` be the `3k x3` matrix whose rows consist of

- `k` copies of `e_1/sqrt(k)`,
- `k` copies of `e_2/sqrt(k)`,
- `k` copies of `e_3/sqrt(k)`.

Then `U_k^T U_k=I_3`. Put

`M_k=U_k V_3^T`,
`A_k=[[0,M_k],[M_k^T,0]].`                                     (4.1)

Every physical cross coefficient of `M_k` is nonzero. The singular values of `M_k` are exactly `(1,1,1)`, hence

`spec(A_k)={+1,+1,+1,-1,-1,-1,0,...,0}`.                       (4.2)

Thus `A_k` satisfies the owner's exact target hypothesis.

For the natural left-to-right cross block, a physical row triple has positive third volume iff it chooses one row from each of the three groups, and then

`a_S=1/k^3`.                                                    (4.3)

There are `k^3` such bases, so

`E3(M_k)=1`.                                                    (4.4)

A six-row set `R` contains two complementary row bases iff it contains exactly two rows from each group. In that case there are exactly `2^3=8` oriented basis triples inside `R`, every summand in the complement-Hellinger currency equals `1/k^3`, and therefore

`C_R(M_k)=8/k^3`.                                               (4.5)

All other six-row sets have `C_R=0`.

The same conclusion survives optimization over **every original-coordinate cut** of the full matrix `A_k`. To see this, split the three right-bank coordinates between the two sides of a cut and let `r` be the number on the row side. After permuting rows and columns, the cross block is a rectangular direct sum

`M_k[L_I,R_J] direct_sum M_k[L_J,R_I]^T`.                       (4.6)

If `0<r<3` and the cross block has rank three, the two summands must have ranks `3-r` and `r`. The second summand has exactly `r` right-bank physical rows, so **every** rank-three row basis contains all of those `r` rows. Hence two disjoint row bases cannot exist and every six-row complement currency is zero. If the cut has rank below three, it is zero trivially. If `r=3`, only three right-bank rows can be active in a rank-three basis, so again there are no two disjoint row bases. The only orientation admitting positive complement currency is `r=0`, already covered by (4.5).

Consequently

`boxed:
 sup_(all original-coordinate cuts, |R|=6) C_R <= 8/k^3 ->0.
`                                                                    (4.7)

This disproves the proposed structural implication “the three-large-eigenvalue hypothesis forces one six-row complement-Hellinger packet of universal size.” It does **not** disprove QFORM or the six-row theorem itself.

### Global compatibility aggregation repairs the same family

Use the natural cross block and let `E` consist of all ordered **disjoint** row-base pairs. Every base has exactly `(k-1)^3` compatible partners. Hence

`B_E = k^3 (k-1)^3 (1/k^3) = (k-1)^3`,                         (4.8)

`H_Pi(T|S)=log((k-1)^3)`,                                      (4.9)

and `beta_*=0`. Therefore the exact currency (3.13) is

`G=1`.                                                          (4.10)

The new theorem gives, for every admissible product law,

`boxed: ||p_(X^T A_k X)||_inf <= 3e = 8.154845485377136...`     (4.11)

uniformly in `k`, and the density lies in `C_0(R)`. From the same q=1 Fourier envelope,

`||phi_Q||_1 <= 6 pi e = 51.238405336041396...`.                (4.12)

Thus a local packet currency can vanish like `k^-3` while the correct global product-Fourier currency remains exactly one.

## 5. A genuinely dense rank-five indefinite form: overlap-one coupling

The compatibility theorem is not restricted to disjoint-base support or exact rank three.

Let

`H_5=I_5-(2/5)11^T`                                            (5.1)

(the 5-dimensional Householder reflection), and put

`M=2H_5`,
`C=J_5/10`,
`A_5=[[C,M],[M,C]].`                                           (5.2)

Every entry of `A_5` is nonzero. Since `H_5=-1` on `span{1}` and `+1` on its orthogonal complement, while `C=1/2` on `span{1}` and zero on the orthogonal complement, the exact spectrum is

`spec(A_5)={2.5,-1.5,+2,+2,+2,+2,-2,-2,-2,-2}`.                (5.3)

Thus this is a dense, genuinely non-diagonal indefinite target matrix with ten eigenvalues of modulus at least `1.5`.

The five rows of `M` are mutually orthogonal with norm two. Therefore for every three-row set `S`,

`a_S=det(4I_3)=64`.                                             (5.4)

There are ten row triples. Let `E` pair two triples exactly when

`|S intersect T|=1`.                                           (5.5)

Every triple has exactly three compatible partners, so `Pi` is uniform on the `10*3=30` ordered compatible pairs and `mu` is uniform on the ten triples. Hence

`B_E=30*64=1920`,                                               (5.6)

`H_Pi(T|S)=log 3`,                                              (5.7)

`G=1920/3=640`.                                                 (5.8)

Every compatible pair has intersection size one. By symmetry across the five physical rows,

`sum_i beta_i=1`, so beta_i=1/5 for every i.                    (5.9)

Thus

`beta_*=1/5`, `q=6/5`.                                         (5.10)

The new theorem yields the explicit all-product-law estimate

`boxed:
 ||p_(X^T A_5 X)||_inf
 <= [3e/((3/5)sqrt(6/5))] 640^(-1/6)
 =4.226464260548676... .
`                                                                    (5.11)

The density is continuous and vanishes at infinity. The same integrable Fourier envelope gives

`||phi_Q||_1 <= 2 pi * 4.226464260548676...
             =26.555658143199075...`.                           (5.12)

This example has only five physical rows on the constrained side, so **no disjoint pair of three-row bases exists at all**. The overlap-one compatibility relation crosses that support barrier while remaining strictly inside the Fourier endpoint `q<3/2`.

## 6. Exact application of the newest fleet02/B04 partner theorem

The overlap compiler has a sharp combinatorial endpoint. Let

`H_4=I_4-(1/2)11^T`,
`M_4=2H_4`,
`C_4=J_4/10`,
`A_4=[[C_4,M_4],[M_4,C_4]].`                                   (6.1)

Again every entry is nonzero. The exact spectrum is

`spec(A_4)={2.4,-1.6,+2,+2,+2,-2,-2,-2}`.                      (6.2)

For each of the four physical row triples,

`a_S=64`, so `Z=E3(M_4)=4*64=256`.                              (6.3)

Any probability law on these four triples can be parametrized by `p_i`, the probability of omitting row `i`. Then

`alpha_i=1-p_i`, `sum_i p_i=1`.                                (6.4)

If every `alpha_i<3/4`, every `p_i>1/4`, impossible. Hence this block lies exactly in the hypothesis of fleet02/B04's completed support-defect exit. Applying that theorem to this actual dense target matrix gives

`||p_(X^T A_4 X)||_inf
 <=6*4^(1/6)*256^(-1/6)
 =3.`                                                           (6.5)

This is a direct application of the designated partner's newest completed result, with arbitrary same-bank curvature `C_4` retained.

It is also exactly the endpoint of the new compatibility theorem: any two **distinct** three-subsets of a four-element row set intersect in two rows, and identical triples intersect in three. Therefore every symmetric pair coupling satisfies

`sum_i beta_i = E|S intersect T| >=2`,

so

`beta_* >=1/2`.                                                 (6.6)

Thus `q=1+beta_*>=3/2`, outside the weighted-Fourier gate. The partner theorem pays precisely this support endpoint with the explicit bound (6.5).

## 7. What is paid and what remains

This run changes the B04 mechanism rather than repeating the preceding local six-row search.

**Paid:**

- the exact compatibility-Hellinger coupling identity (3.10), converting a symmetric physical-base pair law into determinant/entropy currency;
- the overlap criterion `beta_*<1/2`, which converts pairwise anti-overlap directly into the sharp weighted Fourier gate;
- a global aggregate certificate that stays constant on a family where **every** local six-row complement currency tends to zero;
- a rank-five, fully dense, genuinely rotated indefinite form with explicit universal estimate `4.226465` and continuous density;
- the `beta_*=1/2` four-row endpoint is matched to the newest fleet02/B04 support-defect theorem and explicitly bounded by `3`.

**Not paid:** the bare three-large-eigenvalue hypothesis has not yet been shown to force, for some original-coordinate cut, a compatibility relation whose effective currency

`G_E = B_E exp(-H_Pi(T|S))`                                    (7.1)

is universally bounded below while `beta_*<=1/2-c`, nor has every failure of that condition been routed into the completed exact support-defect, compound-hub, ridge, pair-log, aggregate-square or grouped-bank branches.

The next precise obligation is therefore

`QFORM-COMPATIBILITY-CURRENCY-OR-COMPOUND-HUB-v1`:

> From the bare spectral hypothesis, either produce a physical cross cut and symmetric row-base compatibility relation with `beta_*<1/2` and target-scale `G_E`, or prove that quantitative failure forces the bounded compound row/column hub geometry already isolated by the other workers, with no reciprocal payment in an arbitrarily small extra singular direction.

This is a global coupling/currency problem. A return to single six-row packet extraction would contradict Section 4.

## 8. Status and review

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**. The new theorem proves continuity only in its stated compatibility-currency branch through the imported integrable Fourier estimate. No independent end-to-end review of this new compiler/correction has yet been recorded.

All calculations above are exact algebra except the displayed decimal evaluations. Separate finite checks are saved in `CHECKS.json`. No Monte Carlo evidence is used.
