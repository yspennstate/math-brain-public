SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T20:31:05Z.
attacking: convert the fresh two-bank curved-tube estimate into a full rough-input interval/density theorem with one genuinely independent scalar hub; localize the remaining debt to uniform coupling b->0 and compare it with the partner Pluecker crossing currencies.

# account02/B05 — two-bank curved tube to a full hub density theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea bound; complementary constructions/source-valid counterexamples.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `PROVED SUPPORTING INTERVAL/DENSITY THEOREM; FULL QFORM OPEN`.  
**Regularity:** essential boundedness only; continuity is not claimed.

The same-hour canonical B05 login already existed and was preserved rather than overwritten. This run uses a fresh immutable run path.

## 1. Fresh correction and first unpaid implication

The newest control-side correction read before this proof is `math-research-brain@9b2a00d3afd0f89b61178accaabbf20b5b480a23`: the proposed genuine-product twisted Wiener quantity `J(1)` is unbounded even for smooth independent cap-one inputs in a fixed orthonormal frame. That is an interface counterexample, not a QFORM counterexample. In particular the punctured small-coupling problem must not be closed by taking an absolute Fourier/Wiener norm before using the curved geometry.

The fresh replacement input is the proved two-bank curved-tube theorem

`math-open-problems@5e23223ed8626d8df8343d2d26879c08cf139093:`
`proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`.

It retains the original two-bank product provenance and proves the required dyadic gain without a moment or support hypothesis.

The first unpaid implication is now

`QFORM-TWOBANK-HUB-PUNCTURED-COUPLING-v1`:

> make the theorem below uniform as the overlapping light coupling `b -> 0` through nonzero values. The exact `b=0` endpoint is already bounded by the Borel null-hub square theorem from the preceding B05 run, while every fixed `b!=0` is bounded below. Small `b` cannot be treated as a small random perturbation because the input laws have no moments or support bounds.

## 2. Source theorem used

Let independent random vectors

`A=(L_A,V_A,P_A)`, `B=(L_B,V_B,P_B)`

have joint density caps `M_{3,A},M_{3,B}` and `(L,V)`-marginal caps `M_{2,A},M_{2,B}`. Put

`(L,V,P)=A+B`,

`K_2=(M_{2,A}M_{2,B})^(1/2)`, `K_3=(M_{3,A}M_{3,B})^(1/2)`, and `K=K_2+K_3`.

The fresh theorem supplies an absolute constant `C_T` such that, for `0<r<=1`, `a>0`, `b!=0`, and arbitrary real `c,d,gamma`,

P(r<=|L|<=2r,
  |bP+c+dL+(gamma+V^2)/(2L)|<=a)
 <= C_T a r^(3/2)|b|^(-1/2) K.                    (2.1)

It also proves an `r^2 log` improvement when `|gamma|>=1`; the first part alone is enough for the global density theorem below.

## 3. Main theorem — `QFORM-TWOBANK-HUB-DENSITY-v1`

Let `H` be independent of both banks and have probability density `f_H` with

`||f_H||_infinity <= m`.

For arbitrary real `alpha,beta,gamma_0` and `b!=0`, define

Q = 2HL + 2bLP + V^2 + alpha L^2 + beta L + gamma_0.       (3.1)

Set

A_b := [C_T(1+sqrt(2))/4] K |b|^(-1/2).                    (3.2)

Then for every interval `I`,

boxed{
P(Q in I)
 <= |I| inf_{0<R<=1} [ A_b sqrt(R) + m/(2R) ].
}                                                            (3.3)

Consequently Q is absolutely continuous and

boxed{
||p_Q||_(infinity,ess)
 <= (3/2) m^(1/3) max{m,A_b}^(2/3).
}                                                            (3.4)

In the quantitatively active branch `A_b>=m`, this is the sharper homogeneous estimate

boxed{
||p_Q||_(infinity,ess)
 <= (3/2) [C_T(1+sqrt(2))/4]^(2/3)
    m^(1/3) K^(2/3) |b|^(-1/3).
}                                                            (3.5)

No moment, bounded support, connected support, log-concavity, continuity of the input densities, or independence after any spectral rotation is used.

### Proof

Let `I` have length `h` and center `t`. On a shell

r <= |L| <= 2r,

`Q in I` implies

| H+bP+(alpha/2)L+beta/2+(gamma_0-t+V^2)/(2L) |
 <= h/(4|L|)
 <= h/(4r).                                                  (3.6)

Condition **only** on the genuinely independent scalar `H`. The value of H merely translates the parameter `c` in (2.1), whose constant is uniform in `c`. Therefore

P(Q in I, r<=|L|<=2r)
 <= (C_T/4) h sqrt(r)|b|^(-1/2)K.                           (3.7)

Fix `0<R<=1` and cover `0<|L|<=R` by the disjoint dyadic shells with

r_k=R 2^(-k-1),  k>=0.

Since

sum_{k>=0} sqrt(r_k)=(1+sqrt(2))sqrt(R),

summing (3.7) gives

P(Q in I, 0<|L|<=R)
 <= A_b h sqrt(R).                                          (3.8)

On `|L|>R`, condition on `(L,V,P)`. As a function of H, Q is affine with slope `2L`; hence

P(Q in I | L,V,P) <= m h/(2|L|),

and therefore

P(Q in I, |L|>R) <= m h/(2R).                               (3.9)

The law of L is absolutely continuous, so `P(L=0)=0`. Equations (3.8)-(3.9) prove (3.3).

If `A_b>=m`, the unconstrained minimizer

R_*=(m/A_b)^(2/3)

lies in `(0,1]`; substitution gives exactly

A_b sqrt(R_*)+m/(2R_*)=(3/2)A_b^(2/3)m^(1/3).               (3.10)

If `A_b<m`, choose `R=1` to obtain `A_b+m/2<3m/2`. This proves (3.4)-(3.5). A finite measure satisfying `mu(I)<=D|I|` for every interval is dominated by `D` times Lebesgue measure (cover open sets by disjoint intervals and use outer regularity), so Q has an a.e. density with the same essential bound. QED.

## 4. Stable affine-square form

The conclusion is unchanged, with the same `K`, if `V^2` in (3.1) is replaced by

lambda (V+sL+v_0)^2,  |lambda|>=1.                          (4.1)

For `lambda<0`, reflect Q and H. For `lambda>0`, apply the deterministic map

(l,v,p) -> (l, sqrt(lambda)(v+s l)+v_0, p)

to each bank, placing the constant translation in either bank. Its three-dimensional and `(l,v)` Jacobians have absolute determinant `sqrt(lambda)>=1`, so both relevant density caps weakly decrease after pushforward. The shear itself has determinant one. This is only a deterministic change of compressed coordinates; it does **not** assert that the transformed spectral coordinates are independent.

Thus arbitrary `LV`, linear-V, L-square, L-linear and constant terms arising from conditioning are harmless in this one-square normal form.

## 5. Original-coordinate product corollary

Suppose `(L,V,P)=U^T X` comes from a three-column original-coordinate projection and the source coordinates can be partitioned into two independent banks whose Gram matrices satisfy

U_A^T U_A >= kappa I_3,
U_B^T U_B >= kappa I_3,                                    (5.1)

with `0<kappa<=1`. The source theorem's product-projection corollary gives absolute `C_P` such that

M_{2,i} <= C_P kappa^(-1),
M_{3,i} <= C_P kappa^(-3/2).                               (5.2)

Therefore

K <= C_P(kappa^(-1)+kappa^(-3/2))
 <= 2C_P kappa^(-3/2).                                     (5.3)

If the independent hub H is either an original cap-one coordinate (`m<=1`) or a normalized scalar product projection (`m<=sqrt(2)`), (3.4) implies the clean quantitative branch

boxed{
||p_Q||_(infinity,ess)
 <= C max{1, kappa^(-1)|b|^(-1/3)}
}                                                            (5.4)

for an absolute C. Hence every chamber with `kappa>=kappa_0>0` and `|b|>=b_0>0` is paid by a universal constant depending only on those fixed thresholds.

This corollary preserves overlap: every original-coordinate row may have nonzero L,V,P coefficients. The split is between original independent coordinate banks, not between rotated statistics.

## 6. Exact endpoint and the punctured debt

At `b=0`, the total pair `(L,V)` has density cap

||p_(L,V)||_infinity
 <= min(M_{2,A},M_{2,B})                                   (6.1)

because it is the convolution of the two bank marginals. The preceding B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` therefore applies directly and gives, after the same affine shear,

||p_Q||_(infinity,ess)
 <= 7.762 [m min(M_{2,A},M_{2,B})]^(2/3)|lambda|^(-1/3).    (6.2)

Thus the endpoint `b=0` is uniformly paid, while (3.5) pays every fixed `b!=0`. The only missing part of this canonical overlap family is **uniform stability through `b->0`**. This is a genuine punctured problem: the fresh correction shows that an absolute twisted-Wiener norm can blow up for original independent cap-one laws, and the no-moment hypothesis forbids declaring `bP` to be a small random error.

## 7. Noncritical-level refinement from the same curved geometry

If the center `t` of I obeys

|gamma_0-t|>=1,                                             (7.1)

the stronger part of the source tube theorem yields, for `0<R<=1`,

P(Q in I)
 <= |I| { (C_T/4) R [
      K_2(1+2log 2+log_+(1/(|b|R)))+K_3]
      + m/(2R) }.                                           (7.2)

Indeed the dyadic identity

sum_k r_k log_+(1/(|b|r_k))
 <= R[log_+(1/(|b|R))+2log 2]                              (7.3)

is immediate from `r_k=R2^(-k-1)`. Thus away from the quadratic critical value the punctured loss is only logarithmic at the tube level. The hard uniform transition is concentrated at the critical/two-sheet geometry, rather than on the already ruled one-sheet side.

## 8. Required pinned `e5f71d79...` result applied

The required source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem F gives, for an exact-rank-three spectral frame with every original-coordinate leverage at most `1/2`,

boxed{ ||p_Q||_infinity <=12 }                              (8.1)

at target normalization. Therefore any unpaid **exact-rank-three** instance that reaches the present overlap analysis must be on the high-leverage side; there is no need to spend the new tube theorem on the already diffuse class.

The same source's ruled Theorem C gives, for signature `(2,1)` and the one-sheet half-line,

boxed{ p_Q(s)<=pi sqrt(2),  s>=0. }                         (8.2)

Hence (3.3)-(7.2) are genuinely complementary to the ruled calculation: they are full-line/critical-overlap tools aimed at the convex/two-sheet side rather than a replacement of the curved ruling.

## 9. Fresh designated partner `account03/B05` applied at a real obstruction

The newest compatible partner theorem is

`math-open-problems@561a0d56e540a5fa5a689bcb36862d40d6ae0604:`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T193756Z-account03-B05-QFORM-r31/REPORT.md`.

In its live ratio packet, when

q_X<=1/4,  q_Z<=1/2,  mu m z_1^2>=1/8,

the exact original-bank rank-three crossing currency satisfies `Omega_Z>=1/128`, so

boxed{ ||p_Q||_infinity <=6*128^(1/3)=30.2381051974... }.    (9.1)

The symmetric statement holds for `z_2` under `q_Y<=1/2`. Consequently, in the moderate-leverage chamber

q_X<=1/4, q_Y<=1/2, q_Z<=1/2,                               (9.2)

any ratio-packet survivor not already paid by the partner bound (9.1) must satisfy simultaneously

mu m z_1^2 <1/8,
mu m z_2^2 <1/8,

and therefore

boxed{ mu m (z_1^2+z_2^2) <1/4,
        mu m |z_1 z_2| <1/8. }                              (9.3)

This is an actual narrowing of the obstruction: a diffuse partner plane with quantitative residual `z`-currency is already paid by an exact original-coordinate crossing. The surviving partner packet must instead be heavy in one of the leverage parameters or have collapsed normalized residual currency. That is complementary to the punctured `b->0` debt in Section 6.

## 10. What is and is not proved

Proved here:

1. the full rough-input interval inequality (3.3) and essential density bound (3.4) for the two-bank curved core with one genuinely independent hub and every `b!=0`;
2. stability under the determinant-one affine shear needed to retain `LV` and linear-V terms;
3. the original-product bank corollary (5.4);
4. the noncritical-level logarithmic refinement (7.2);
5. the explicit partner obstruction (9.3).

Not proved:

- a bound uniform as `b->0` through nonzero values when P overlaps the same product banks as `(L,V)`;
- the general high-leverage/heavy-scalar ratio-packet splice outside the partner crossing currencies;
- the unrestricted full QFORM conjecture;
- full-target continuity.

The new theorem never takes an unrestricted curved-fiber supremum, never conditions on a dependent rotated coordinate and then calls it independent, and never treats a small coefficient as a small random perturbation. Independent review is **PENDING**.
