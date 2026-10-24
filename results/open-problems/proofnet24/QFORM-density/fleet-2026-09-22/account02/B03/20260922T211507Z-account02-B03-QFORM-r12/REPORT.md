SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-22T21:15:07Z.
attacking: arbitrary-self cross-bank endpoint — test whether dependence-safe collision/Frobenius control survives nonzero active self curvature, and derive the corrected noncollapse condition.

# account02/B03 r12 — arbitrary-self cross-bank obstruction and corrected noncollapse condition

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Fresh control at start: `yspennstate/math-research-brain@b97cf63a6311eaaf117726452631e026e2d61d9d`; pre-publication refresh: `1d81fec9aa4b8a84883ab068a2b288e6884331c1`; OWNER CONTROL revision `2026-09-22.15`.

## 1. Target and source discipline

The owner target remains the unrestricted theorem: for independent real original-coordinate inputs with one-dimensional densities at most one and any real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a target-valid counterexample.

This report does **not** use post-rotation independence, law-uniform pointwise Fresnel decay, the false conditional cap for a conjugate sum/difference pair, the false arbitrary-joint rank-three coarea bound, the false positive conditional projection-density moment, or a fixed-good-minor selector. The construction below uses two genuinely independent cap-one original coordinates and exact integrals.

The designated partner result actually applied is account03/B03 run `20260922T190034Z-account03-B03-QFORM-r18`, canonical report

`yspennstate/math-open-problems@d18302d55f907552185a42994d48b09f39737cbd`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T190034Z-account03-B03-QFORM-r18/REPORT.md`.

Its dependence-safe physical-cross independent-copy consequence is: a rank-`r` original-coordinate cross block with positive singular-value product `Delta_r` gives

`E|R-R'|^(-1/2) <= [8r/(2r-1)] Delta_r^(-1/(2r))`.             (1.1)

For rank one this is `<=8 sigma^(-1/2)`. The proof retains the dependence of copy sums and differences; no conditional conjugate-density cap is used.

I also use the completed orientation-free rank-two affine half-Riesz theorem, source-pinned in current research at `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, in the exact form

`sup_t E|Z^T P Z+ell^T Z+c-t|^(-1/2) <=128 |det P|^(-1/4)`      (1.2)

for every invertible physical `2 x 2` symmetric coefficient `P` and independent cap-one original coordinates `Z`.

Finally, the immediately preceding B03 report at `yspennstate/math-open-problems@d205dc643b8d2439efdbbe986f93ea8b4f2933f5` proves the full-law physical-pivot collision estimate

`E|Q-Q'|^(-1/2) <= C_* |A_ii|^(-1/2)`,
`C_*=16 sqrt(2)/3^(3/4)=9.9264518304...`.                       (1.3)

## 2. Candidate under test

The latest synthesis has a dimension-free Frobenius half-Riesz theorem when one source bank has **zero** quadratic self block:

`H_(1/2)(R):=sup_t E|R-t|^(-1/2) <=4sqrt(2e)||B||_F^(-1/2)`.

The first unpaid extension is whether the same Frobenius currency survives arbitrary source self curvature. A natural candidate is therefore

> There is a universal `C` such that for every normalized invertible Schur core `S` with `s_2(S)=1`, every physical cross bank `B`, and every cap-one product law,
> `H_(1/2)(Z^T S Z) <= C ||B||_F^(-1/2)`, even when the active banks have arbitrary self blocks.

This candidate is false already in dimension two.

## 3. Exact normalized two-coordinate adversary

Fix `0<eta<1`. Let `X,Y` be independent `Uniform[-1/2,1/2]`, and define

`R_eta = [(X+Y)^2 + eta (X-Y)^2]/(2 eta)`.                      (3.1)

Its physical coefficient matrix is

`S_eta = (1/(2 eta)) [[1+eta, 1-eta], [1-eta, 1+eta]].`         (3.2)

The eigenvectors are `(1,1)` and `(1,-1)`, with eigenvalues respectively

`1/eta` and `1`.                                                  (3.3)

Hence `S_eta` is invertible and its second singular value is **exactly one**:

`s_2(S_eta)=1`.                                                   (3.4)

The physical cross coefficient is

`b_eta=(1-eta)/(2 eta)`,                                         (3.5)

so the scalar cross-bank Frobenius norm is `||B_eta||_F=b_eta`.

This family is therefore inside the exact homogeneous normalized Schur core while its cross bank becomes arbitrarily large.

## 4. Exact one-copy half-Riesz potential

Set

`u=X+Y`, `v=X-Y`.

The change of variables has Jacobian `1/2`, and `(u,v)` has density `1/2` on the diamond

`|u|+|v|<=1`.                                                     (4.1)

Moreover

`R_eta=(u^2+eta v^2)/(2 eta)`.                                   (4.2)

At target zero,

`H_eta(0):=E R_eta^(-1/2)
 =sqrt(2 eta) E (u^2+eta v^2)^(-1/2)`.                           (4.3)

By symmetry and the diamond density,

`E (u^2+eta v^2)^(-1/2)
 =2 int_0^1 asinh((1-v)/(sqrt(eta) v)) dv`.                      (4.4)

Put `t=(1-v)/v`. Integration by parts gives

`2 int_0^1 asinh((1-v)/(sqrt(eta)v))dv
 =2 int_0^infinity dt/[(1+t)sqrt(t^2+eta)]`.                     (4.5)

With `t=sqrt(eta)sinh s` and then `y=e^(-s)`, this becomes

`4 int_0^1 dy/[sqrt(eta)+2y-sqrt(eta)y^2]`.                      (4.6)

Writing `r=sqrt(1+eta)` and evaluating the elementary rational integral yields

`E (u^2+eta v^2)^(-1/2)
 = [2/r] log( (r+1+sqrt(eta))^2/(2sqrt(eta)) ).`                 (4.7)

Therefore

`boxed{
H_eta(0)
 = [2sqrt(2eta)/sqrt(1+eta)]
   log( (sqrt(1+eta)+1+sqrt(eta))^2/(2sqrt(eta)) ).
}`                                                                 (4.8)

Multiply by the cross scale from (3.5):

`boxed{
H_eta(0) sqrt(b_eta)
 =2 sqrt((1-eta)/(1+eta))
   log( (sqrt(1+eta)+1+sqrt(eta))^2/(2sqrt(eta)) ).
}`                                                                 (4.9)

As `eta ->0`, the logarithm is `(1/2)log(4/eta)+o(1)`, so

`H_eta(0) sqrt(b_eta) = log(4/eta)+o(log(1/eta)) -> infinity`.     (4.10)

Thus no universal constant can bound the one-copy half-Riesz potential by `C ||B||_F^(-1/2)` once arbitrary self blocks are admitted, even with `s_2(S)=1`, dimension two, and the simplest cap-one product law.

This refutes the **arbitrary-self Frobenius-scaling extension**, not the normalized-Schur half-Riesz conjecture itself: the matrix also has a huge determinant and is uniformly controlled by the completed rank-two theorem.

## 5. Independent-copy collision stays smaller by a logarithm

Apply the designated account03/B03 partner result (1.1) to the actual cross coefficient (3.5). Since the physical cross block has rank one and singular value `b_eta`, an independent copy `R_eta'` satisfies

`boxed{
E|R_eta-R_eta'|^(-1/2)
 <=8 b_eta^(-1/2)
 =8 sqrt(2eta/(1-eta)).
}`                                                                 (5.1)

The preceding B03 physical-pivot theorem gives a second bound from the diagonal coefficient

`a_eta=(1+eta)/(2eta)`:

`E|R_eta-R_eta'|^(-1/2)
 <=C_* sqrt(2eta/(1+eta)).`                                      (5.2)

Hence the direct one-copy endpoint can exceed the **actual** collision potential by an unbounded factor. Indeed (5.1) and (4.8) imply

`H_eta(0) / E|R_eta-R_eta'|^(-1/2)
 >= (1/4)sqrt((1-eta)/(1+eta))
    log( (sqrt(1+eta)+1+sqrt(eta))^2/(2sqrt(eta)) ) -> infinity.` (5.3)

This is a source-valid obstruction to a universal collision-to-one-copy endpoint promotion in a normalized, cross-rich, self-curved quadratic family.

In the exact independent-copy Fourier language,

`E|R_eta-R_eta'|^(-1/2)
 =(2pi)^(-1/2) int |t|^(-1/2)|phi_eta(t)|^2 dt`,                 (5.4)

whereas the one-copy half-Riesz potential is the regularized signed endpoint involving `Re phi_eta(t)`. The logarithmic gap (5.3) shows that the weighted `L^2` time integral supplied by the independent-copy identity cannot, by itself, recover the signed one-copy endpoint when self curvature nearly square-completes the cross term.

This is stronger for the present proof architecture than the earlier single-square endpoint obstruction: it lies inside the normalized `s_2=1` Schur core and simultaneously has a large physical cross coefficient.

## 6. Corrected source-valid sufficient statement

The same family identifies the missing parameter. Let

`P=[[a,b],[b,c]]`                                                  (6.1)

be a physical principal pair inside an arbitrary residual, and suppose `P` is invertible. Condition on all other original coordinates. The active pair remains independent with density caps one, while all outside couplings become an arbitrary affine term. The completed rank-two affine half-Riesz theorem (1.2) gives

`H_(1/2)(full residual) <=128 |det P|^(-1/4)`.                    (6.2)

Therefore, whenever the physical pair obeys the quantitative noncollapse condition

`|det P|=|ac-b^2| >= delta b^2`,                                  (6.3)

one gets the corrected cross-scale estimate

`boxed{
H_(1/2)(full residual)
 <=128 delta^(-1/4)|b|^(-1/2).
}`                                                                 (6.4)

This is a proved sufficient statement with all outside self curvature and affine shifts retained.

For the adversary (3.2),

`det S_eta=1/eta`,

and

`delta_eta:=|det S_eta|/b_eta^2
 =4eta/(1-eta)^2 ->0`.                                            (6.5)

Thus the exact logarithmic loss occurs precisely in the regime where the rank-two physical pair approaches square completion relative to the cross scale. One cannot replace (6.3) by mere largeness of `|b|` or Frobenius cross mass.

## 7. Consequence for the full proof tree

The correction-safe aggregate route can now separate two endpoints cleanly:

- **zero self block:** use the completed Frobenius half-Riesz theorem, which legitimately aggregates a whole cross bank before inversion;
- **noncollapsed physical pair:** use (6.4), paying determinant only after a quantitative self/cross defect is exposed;
- **remaining case:** the genuinely unpaid geometry is a *collective near-rank-one square-completion regime* across the matching bank, where many self-curved channels can have small determinant defect even though cross Frobenius mass is large.

The last regime cannot be closed by the independent-copy collision energy alone because of (5.3). It requires a product-preserving grouped-square/ridge/aggregate mechanism that spends the large spectral directions before taking the critical endpoint.

This is the first essential missing implication for B03 after the latest zero-self synthesis.

## 8. Arithmetic regression checks

The saved checker evaluates the exact formula, spectrum, cross scale, collision certificates, and noncollapse parameter. Representative rows are:

`eta=1e-2`: `eig=(100,1)`, `b=49.5`, `H=0.871914127671`, `H*sqrt(b)=6.13445964846`, partner collision `<=1.13707048723`, `delta=0.0408121620243`.

`eta=1e-4`: `eig=(10000,1)`, `b=4999.5`, `H=0.150135084063`, `H*sqrt(b)=10.6156227825`, partner collision `<=0.113142742268`, `delta=0.000400080012002`.

`eta=1e-8`: `eig=(1e8,1)`, `b=49999999.5`, `H=0.00280115755329`, `H*sqrt(b)=19.807174912`, partner collision `<=0.00113137085556`, `delta=4.00000008e-8`.

`eta=1e-12`: `eig=(1e12,1)`, `b=5e11`, `H=4.10366839197e-5`, `H*sqrt(b)=29.017317477`, partner collision `<=1.1313708499e-5`, `delta=4.00000000001e-12`.

These computations are regression evidence only; the divergence is proved analytically in (4.10).

## 9. Status

- `QFORM-ARBITRARY-SELF-CROSS-FROBENIUS-SCALE-FALSE-v1`: **PROVED COUNTEREXAMPLE TO INTERMEDIATE MECHANISM**.
- collision-to-one-copy half-Riesz promotion from the dependence-safe rank-one collision certificate: **REFUTED** in a normalized cross-rich quadratic family.
- determinant-defect sufficient statement (6.4): **PROVED** from the completed rank-two affine half-Riesz theorem.
- full QFORM universal density theorem: **OPEN**.
- continuity for the full target: **OPEN**.

No target-level counterexample is claimed.