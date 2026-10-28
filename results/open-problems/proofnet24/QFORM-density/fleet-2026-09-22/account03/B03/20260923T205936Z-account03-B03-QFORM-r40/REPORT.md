SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T20:59:36Z.
attacking: the critical two-sided decoupled-time endpoint; consume account04/B03's actual dependent sum/difference theorem, then replace the stalled formal quarter-plus-quarter transduction by an exact original-copy bilinear factorization in the matched-opposite-curvature case.

# account03/B03 r40 — matched-opposite conjugate-pair half-Riesz compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER RESULT APPLIED / MATCHED-OPPOSITE TWO-SIDED ENDPOINT CLOSED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


The completed designated partner source is

`yspennstate/math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260923T183012Z-account04-B03-dependent-riesz-r2/REPORT.md`.

The whole-copy Riesz identity and the earlier effective-dimension compiler used below were already proved in account03/B03 r36:

`yspennstate/math-open-problems@884927dd365932b0b1ec9b796826b886eb7a3466`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260923T181128Z-account03-B03-QFORM-r36/REPORT.md`.

## 1. Apply the partner theorem to an actual conjugate pair

Let `X=(X_1,X_2)` have independent real coordinates with densities at most one, let `X'` be an independent copy, and put

`U=X-X'`, `V=X+X'`.                                                (1.1)

The coordinates of `U` are mutually independent and each has density at most one; the same is true marginally for `V`. The vectors `U,V` are generally dependent, and no contrary assertion is made.

Let `P` be an invertible real symmetric `2 x 2` matrix and define, with arbitrary affine data,

`A(U)=U^T P U + ell_-^T U + d_-`,
`B(V)=-V^T P V + ell_+^T V + d_+`.                                 (1.2)

The partner theorem `QFORM-DEPENDENT-SUMDIFF-FRACTIONAL-BUDGET-v1`, applied with `P_-=P`, `P_+=-P`, and `theta=1/2`, gives for every `s,t`:

`boxed:
 E |A(U)-s|^(-1/4) |B(V)-t|^(-1/4)
 <= calB(P),
}`                                                                  (1.3)

where in particular

`calB(P) <= 128 |det P|^(-1/4)`.                                   (1.4)

This is an actual use of the designated partner result on the dependent `(U,V)` law. For example, Markov on the singular kernel yields the concrete joint-window inequality

`boxed:
 P(|A(U)-s|<=r, |B(V)-t|<=r)
 <= calB(P) r^(1/2),
}`                                                                  (1.5)

and hence, at `r=eps^2`, a linear bound `<=calB(P) eps` for the simultaneous two-window event.

The important limitation is equally explicit: (1.3) distributes a **total** singularity budget `1/2`; it does not formally imply a half-Riesz bound for the sum `A(U)+B(V)`. A third square cannot be attached by a mere extra Holder step. This is exactly the endpoint identified by account04/B03. The next section changes mechanism and uses the exact original-copy geometry of the matched-opposite case.

## 2. A two-dimensional bilinear half-Riesz theorem with arbitrary one-side potential

### Lemma 2.1 — scalar cap-to-half-Riesz

If a real random variable `Y` has a probability density bounded by `M`, then for every `s`,

`E|Y-s|^(-1/2) <= 2 sqrt(2M)`.                                     (2.1)

Indeed, by layer cake,

`E|Y-s|^(-1/2)
 = int_0^infty P(|Y-s|<t^(-2)) dt
 <= int_0^infty min(1,2M t^(-2)) dt
 =2 sqrt(2M).`                                                      (2.2)

No support, moment or regularity assumption is used.

### Lemma 2.2 — radial inverse-half moment in two dimensions

If `Z` is an `R^2`-valued probability vector with joint density bounded by `M`, then

`E ||Z||^(-1/2) <= (4/3) pi^(1/4) M^(1/4)`.                        (2.3)

Again layer cake gives

`P(||Z||<t^(-2)) <= min(1,M pi t^(-4))`,                            (2.4)

and splitting at `t=(M pi)^(1/4)` gives (2.3).

### Theorem 2.3 — `QFORM-2D-BILINEAR-ONESIDE-HALFRIESZ-v1`

Let `X=(X_1,X_2)` and `Y=(Y_1,Y_2)` be independent vectors, all four scalar coordinates mutually independent with probability densities at most one. Let `C` be any invertible real `2 x 2` matrix, let `a,b in R^2`, and let `F:R^2->R` be arbitrary measurable. Define

`R = F(X) + (X-a)^T C (Y-b)`.                                      (2.5)

Then

`boxed:
 sup_s E|R-s|^(-1/2)
 <= C_2 |det C|^(-1/4),
 C_2=(4/3) 2^(7/4) pi^(1/4)
    =5.97074738624132... .
}`                                                                  (2.6)

**Proof.** Fix `X=x`. Put `w=C^T(x-a)`. Since `Y_1,Y_2` are genuine independent original coordinates, choose `j` with

`|w_j| >= ||w||/sqrt(2)`.                                          (2.7)

Conditioning on the other `Y` coordinate, the scalar projection `w^T(Y-b)` has density cap at most `1/|w_j|`; averaging that conditioning therefore gives the unconditional conditional-on-`x` cap

`||p_{w^T(Y-b)}||_infinity <= sqrt(2)/||w||`.                       (2.8)

This is **not** a conditional cap for a conjugate sum/difference variable. It is ordinary conditioning inside an independent original product bank.

Lemma 2.1 now gives, uniformly in the shift `s-F(x)`,

`E_Y |R-s|^(-1/2)
 <= 2^(7/4) ||C^T(x-a)||^(-1/2).`                                  (2.9)

It remains to average over `X`. The joint density of `X` is at most one. Hence the transformed vector

`Z=C^T(X-a)`                                                        (2.10)

has a joint density bounded by `|det C|^(-1)`. Its coordinates need not be independent after this deterministic transform, and no such independence is used. Lemma 2.2 yields

`E_X ||C^T(X-a)||^(-1/2)
 <= (4/3) pi^(1/4)|det C|^(-1/4).`                                 (2.11)

Combining (2.9)-(2.11) proves (2.6). The exceptional point `C^T(x-a)=0` has `X`-probability zero and the displayed radial majorant is locally integrable. `square`

The theorem also covers an arbitrary affine term in `Y`: because `C` is invertible, `q^T Y` is absorbed by replacing `a` with `a-C^{-T}q` (up to an `X`-only term, which is absorbed into `F`). Thus the theorem is stable under all conditioning-generated affine data of that form.

## 3. Exact matched-opposite conjugate-pair upgrade

Return to (1.1)-(1.2) and put

`S=A(U)+B(V)`.                                                      (3.1)

Expand in the independent originals `X,X'`:

`S=-4 X^T P X'
  +(ell_-+ell_+)^T X
  +(-ell_-+ell_+)^T X'
  +d_-+d_+.`                                                        (3.2)

Because `P` is invertible, define

`a=(1/4)P^(-1)(-ell_-+ell_+)`,
`b=(1/4)P^(-1)( ell_-+ell_+)`.                                     (3.3)

Then there is a constant `c` such that

`boxed:
 S-c = -4 (X-a)^T P (X'-b).
}`                                                                  (3.4)

Specifically `c=d_-+d_+ + 4 a^T P b`. Thus the problematic dependence between `U` and `V` disappears **only because we return to the genuine independent original copy pair `(X,X')` and use the exact matched-opposite algebra**. No conditional law of `U` given `V` is introduced.

Apply Theorem 2.3 with `C=-4P`. Since `|det(-4P)|=16|det P|`,

`boxed:
 sup_z E|S-z|^(-1/2)
 <= C_pair |det P|^(-1/4),
 C_pair=(4/3)2^(3/4)pi^(1/4)
       =2.9853736931206605... .
}`                                                                  (3.5)

Call this `QFORM-MATCHED-OPPOSITE-CONJUGATE-HALFRIESZ-v1`.

This is the missing **half** singularity in this precise two-sided endpoint. It is stronger than the quarter-plus-quarter estimate (1.3), but it does not follow from (1.3) alone: the upgrade uses the exact relation `P_+=-P_-` and the original-copy factorization (3.4).

## 4. Assigned dependence-safe integrated time estimate

Let `S~` be an independent copy of the **whole** random variable `S`. The independent-copy identity gives

`|phi_S(t)|^2 = E exp(it(S-S~))`.                                   (4.1)

The standard one-dimensional Riesz identity, justified by positive regularization and already recorded in r36, is

`int_R |t|^(-1/2)|phi_S(t)|^2 dt
 =sqrt(2pi) E|S-S~|^(-1/2).`                                       (4.2)

Condition on `S~` and use the translation-uniform bound (3.5). Therefore

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2 dt
 <= C_time |det P|^(-1/4),
 C_time=sqrt(2pi) C_pair
       =(4/3)2^(5/4)pi^(3/4)
       =7.483222109515818... .
}`                                                                  (4.3)

This is exactly of the assigned form: the independent-copy identity is used for the **whole** `S-S~`; no coordinate difference is separated from its conjugate sum, and no false conditional cap is used.

## 5. One genuine square recovers linear one-copy small-ball scaling

Let `Z` be a genuine independent original scalar coordinate with density at most one, independent of all variables in `S`, and let `d!=0`. Set

`T=d(Z+h)^2+S+c_0`.                                                 (5.1)

For fixed `S`, the square term has the standard density envelope

`g(w) <= |d|^(-1/2)|w|^(-1/2)`                                     (5.2)

on its allowed side. Hence, for almost every `t`,

`p_T(t)
 <= |d|^(-1/2) E|t-c_0-S|^(-1/2).`                                 (5.3)

Using (3.5),

`boxed:
 ||p_T||_(infinity,ess)
 <= C_pair |d|^(-1/2)|det P|^(-1/4).
}`                                                                  (5.4)

Consequently every interval `I` obeys the genuine linear one-copy small-ball bound

`boxed:
 P(T in I)
 <= C_pair |d|^(-1/2)|det P|^(-1/4) |I|.
}`                                                                  (5.5)

This establishes an essentially bounded density in this branch. **Continuity is not proved by this argument.**

## 6. Concrete target-valid control family

Ignoring affine terms, the quadratic matrix of (5.1) in the independent physical coordinates `(X,X',Z)` is

`M_T = [[0,-2P,0],[-2P,0,0],[0,0,d]].`                              (6.1)

If `lambda_1,lambda_2` are the eigenvalues of the symmetric matrix `P`, then the eigenvalues of `M_T` are

`{ 2lambda_1,-2lambda_1,2lambda_2,-2lambda_2,d }`.                  (6.2)

Thus if `|lambda_1|,|lambda_2|>=1/2` and `|d|>=1`, this is an actual target instance with five eigenvalues of modulus at least one, for arbitrary cap-one input laws and arbitrary affine terms. In that normalized subfamily `|det P|>=1/4`, so (5.4) gives

`||p_T||_infinity
 <= sqrt(2) C_pair
 =4.221955965563093... .`                                           (6.3)

This is a useful control, not the unrestricted theorem. If only one eigenvalue of `P` is at least `1/2` while the other tends to zero, (6.2) plus `|d|>=1` still gives three large eigenvalues, but the determinant factor in (5.4) deteriorates. Therefore the bare three-eigenvalue hypothesis has **not** been reduced to this matched pair.

## 7. What changed and the remaining implication

The previous r39/r40 attack tried to turn the partner's abstract `1/4+1/4` singularity budget directly into the half-Riesz receiver needed by a square. That formal route has no spare exponent. This run changes mechanism on the same target: in the exact matched-opposite two-sided case, it returns to the genuine independent originals and rewrites the conjugate quadratic pair as one nondegenerate two-bank bilinear form. The determinant-scale half-Riesz estimate (3.5), whole-copy integrated estimate (4.3), and square transduction (5.4) are now complete.

The **first remaining B03 implication** is structural, not analytic: show that an actual still-unpaid QFORM decoupling branch contains, after product-preserving conditioning/completion, either

1. a matched-opposite two-sided physical pair with `|det P|` quantitatively paid at target scale, or
2. another proved receiver (for example a source-validated projected crossing / square-bilinear Schur branch) whose third smoothing resource is a genuinely independent original coordinate.

The present theorem must not be applied by merely declaring approximately opposite curvatures: with arbitrary unbounded input supports, a small matrix perturbation is not a small random quadratic perturbation. Exact algebra or a new stability theorem is required.

The unrestricted QFORM conjecture remains **OPEN**. The full-target continuous-density conclusion remains **OPEN**. No scheduler state, task identity, notification/email setting, permission, public-release state, paid model/API/Codex action, installation, or cross-account authentication was changed.