# account01/B06 — discriminant-averaged curved half-Riesz smoothing

**Run:** `20260922T193442Z-qform-r15-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** curved fiber integration  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conditional end-to-end route

The full target remains: for independent real coordinates with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid target counterexample. Continuity is a separate desired conclusion and is not proved here.

This run attacks the following physical-pivot route. If `a=A_kk!=0`, complete the square only in the original coordinate `X_k`:

`Q = a (X_k + a^{-1} b^T Z)^2 + R(Z)`.

Conditionally on `Z`, the shifted `X_k` still has a density cap one. Therefore

`p_Q(t) <= |a|^{-1/2} E |R-t|^{-1/2}`.                                      (1.1)

Thus a translation-uniform half-Riesz bound for the Schur remainder `R` is enough. The exact-zero inner pivot was handled in the preceding B06 run. The new point is to control a genuinely nonzero inner scalar pivot by retaining the full quadratic discriminant, rather than replacing it by the false near-zero continuity argument.


## 2. Dependencies actually used

### Named assigned partner: account02/B06

I use account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

Its `k=1` case gives, for every nonzero coefficient vector `c`,

`||p_(sum_j c_j X_j)||_infinity <= sqrt(e)/||c||_2`.                    (2.1)

This is applied below to the exact-zero branch of the unified scalar-pivot dichotomy; it is a weighted affine-fiber estimate preserving the original product law.

### Arbitrary-rank quarter-small-ball input

I also use the completed source-pinned estimate in

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`:

for every nonzero symmetric `T`, independent cap-one `Y`, arbitrary affine terms, every center `u`, and every `rho>0`,

`P(|Y^T T Y+v^T Y+c-u|<rho) <= min(1,5 (rho/||T||)^(1/4))`.             (2.2)

No post-rotation independence or moment assumption is used.

## 3. One-dimensional discriminant lemma

### Lemma 3.1 — `QFORM-QUADRATIC-DISCRIMINANT-HALF-RIESZ-v1`

Let `X` have a probability density `f<=1`. Let

`P(x)=d x^2+w x+c`, `d!=0`, and `Delta=w^2-4dc`.

Then, with the right side interpreted as `+infinity` when `Delta=0`,

`E |P(X)|^(-1/2) <= 16 |d|^(-1/4) |Delta|^(-1/8)`.                     (3.1)

#### Proof

Complete the square and put

`a = sqrt(|Delta|)/(2|d|)`.

After translation,

`|P(x)|^(-1/2)=|d|^(-1/2) |x^2 +/- a^2|^(-1/2)`.

It suffices to prove

`sup_{0<=f<=1, int f=1} int f(x)|x^2 +/- a^2|^(-1/2) dx <=16 a^(-1/4)`. (3.2)

For the plus sign, the kernel is symmetric decreasing, hence the bathtub principle gives

`<= int_{-1/2}^{1/2} (x^2+a^2)^(-1/2) dx =2 asinh(1/(2a))`.

For `a>=1` this is at most `a^{-1}<=a^{-1/4}`. For `0<a<=1`, it is at most `2 log(2/a)`, and `log(1/a)<=4/(e a^{1/4})`; thus (3.2) holds with room to spare.

For the minus sign, let

`m_a(eps)=Leb{x: |x^2-a^2|<eps}`.

If `eps<=a^2/2`, then

`m_a(eps)=2(sqrt(a^2+eps)-sqrt(a^2-eps))<=6 eps/a`.

If `eps>a^2/2`, then `m_a(eps)<=4 sqrt(eps)`. By layer cake and the density cap,

`int f(x)|x^2-a^2|^(-1/2)dx
 <= int_0^infinity min(1,m_a(s^{-2})) ds`.

For `a<=1`, splitting at `s=1` and `s=sqrt(2)/a` gives

`<= 6+4 log(sqrt(2)/a) <=16 a^{-1/4}`.

For `a>=1`, splitting at `sqrt(2)/a` and using `m_a(s^{-2})<=6/(a s^2)` in the tail gives

`<= (sqrt(2)+2sqrt(6)) a^{-1/2} <7 a^{-1/2} <=7a^{-1/4}`.

This proves (3.2). Substituting `a=sqrt(|Delta|)/(2|d|)` gives (3.1), since the factors `2^{1/4}` are accounted for explicitly in the next application. `QED`

## 4. New arbitrary-rank scalar-pivot theorem

Write independent variables as `(X,Y)` and consider

`R=d X^2 + 2(b^T Y+u)X + Y^T C Y + v^T Y + c`,                      (4.1)

with `d!=0`. Define the Schur remainder

`T=C-bb^T/d`,

and the corresponding affine quadratic

`G(Y)=Y^T T Y +(v-2u b/d)^T Y + c-u^2/d`.                              (4.2)

Then

`R = d (X+(b^T Y+u)/d)^2 + G(Y)`.                                    (4.3)

The discriminant of the polynomial `R-t` in `X` is exactly

`Delta(Y) = -4d (G(Y)-t)`.                                            (4.4)

### Theorem 4.1 — `QFORM-SCALAR-PIVOT-DISCRIMINANT-HALF-RIESZ-v1`

Assume `T!=0` and set `s=||T||`. Then

`sup_t E |R-t|^(-1/2) <= 96 |d|^(-3/8) s^(-1/8)`.                    (4.5)

#### Proof

Condition on `Y` and apply Lemma 3.1. Using (4.4), the factor `2^{1/4}` from `a^{-1/4}` cancels the factor `4^{-1/8}` in the discriminant, giving

`E_X |R-t|^(-1/2) <=16 |d|^(-3/8) |G(Y)-t|^(-1/8)`.                  (4.6)

It remains to average the eighth-root singularity. From (2.2), for `Z=|G-t|`,

`P(Z<rho)<=min(1,5(rho/s)^(1/4))`.

Therefore

`E Z^(-1/8)
 =(1/8) int_0^infinity rho^(-9/8) P(Z<rho) d rho
 <=5 s^(-1/8)+s^(-1/8)
 =6 s^(-1/8)`.                                                         (4.7)

Combining (4.6) and (4.7) proves (4.5). `QED`

This is exactly the curved discriminant mechanism missing from the previous exact-zero run. The quarter-power small-ball estimate is sufficient because the discriminant lemma asks only for an `1/8` negative moment rather than the critical `1/4` moment.

## 5. Exact-zero endpoint and use of the named partner

When `d=0`, (4.1) is linear in `X`. Put `beta=||b||_2`. If `beta>0`, the assigned partner theorem (2.1) gives

`||p_(2b^T Y+2u)||_infinity <= sqrt(e)/(2 beta)`.                       (5.1)

Conditioning on `Y`, the one-dimensional bathtub estimate for the half-Riesz kernel and then applying the same estimate to the linear coefficient yields the previously proved endpoint

`sup_t E|R-t|^(-1/2) <=4 sqrt(2) e^(1/4) beta^(-1/2)`.                 (5.2)

Thus the unified scalar-pivot picture is now:

- `d=0`: product-linear smoothing, paid by account02/B06 weighted affine fibers;
- `d!=0` and `T!=0`: discriminant smoothing, paid by (4.5);
- `d!=0` and `T=0`: the rank-one square obstruction can have infinite half-Riesz potential, exactly as in the prior source-valid counterexample.

The last obstruction is structural, not an artifact of the proof.

## 6. Consequence for the full quadratic form after an outer physical pivot

Let a symmetric target matrix be blocked around an original coordinate `k` with `a=A_kk!=0`:

`A=[[a,r^T],[r,C]]`, `S=C-rr^T/a`.

Then (1.1) holds with `R(Z)=Z^T S Z` plus the induced affine term if present.

Choose an original coordinate `i` in the Schur variables with `d=S_ii!=0`, and let `T` be the further scalar Schur complement. If `rank(S)>=2`, then `T!=0`. Hence

`||p_Q||_infinity <=96 |a|^(-1/2)|d|^(-3/8)||T||^(-1/8)`.             (6.1)

Equivalently, let `B=A_{ {k,i},{k,i} }` be the physical `2x2` principal pair. Since

`det B = a d`,                                                            (6.2)

and `A-diag(0,T)` differs by a rank-two matrix after pair completion, Eckart--Young gives

`||T|| >= s_3(A)`.                                                        (6.3)

Therefore every such pair satisfies the arbitrary-rank branch

`||p_Q||_infinity
 <=96 |a|^(-1/8) |det B|^(-3/8) s_3(A)^(-1/8)`.                   (6.4)

Under the target normalization `s_3(A)>=1`,

`||p_Q||_infinity <=96 |a|^(-1/8)|det B|^(-3/8)`.                      (6.5)

This works for either sign of the invertible pair and with all remaining eigenvalues/couplings arbitrary. It is not a full-target estimate because the bare three-large-eigenvalue hypothesis does not force one physical pair with the reciprocal factors in (6.5) uniformly bounded.

If instead `d=0` and the corresponding Schur row has off-diagonal norm `beta>0`, (5.2) yields

`||p_Q||_infinity <=4 sqrt(2)e^(1/4)|a|^(-1/2) beta^(-1/2)`.            (6.6)

This is the exact-zero endpoint and no continuity from (6.5) to (6.6) is asserted.

## 7. Mathematical change and remaining implication

The previous B06 run showed that merely taking a small nonzero Schur diagonal and pretending it is zero is false: a rank-one square can make the half-Riesz potential infinite. The new theorem identifies the correct replacement. Keep the **quadratic discriminant** until after the inner-coordinate integration; it converts the singularity from inverse square root into an eighth-root negative moment of the genuine Schur remainder. The already-proved arbitrary-rank quarter-small-ball theorem then pays that moment.

The first unpaid full-target implication is now sharper:

`QFORM-WEIGHTED-SCALAR-PAIR-AGGREGATION-v1`:
combine (6.5), the exact-zero endpoint (6.6), the diffuse/ridge-window branch, and original-coordinate product aggregation to avoid selecting a single physical pair with an unbounded reciprocal determinant cost.

The singleton-plus-two-banks and Hadamard families remain mandatory stress tests. In particular, this run does not claim that one uniformly conditioned physical pair exists.

## 8. Correction compatibility

This proof does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, unrestricted fiber suprema, the refuted arbitrary-joint rank-three coarea lemma, the refuted conditional positive-moment gate, or a fixed-good-minor theorem. It retains the original product structure at the only endpoint where it is needed, via the named partner affine-fiber estimate.

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`. Essential boundedness is proved only in the quantified branches above. The universal conjecture and the separate continuous-density conclusion remain open.
