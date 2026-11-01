# QFORM B17: sharp finite-size optimization and second-order rotated witness expansion

Run: `20260923T221053Z-fleet03-B17-QFORM-auto11`  
Status: `PROVED_SUPPORTING_SHARP_WITNESS_THEOREM`; full QFORM conjecture OPEN; full-target continuity OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope

The owner target is the unrestricted product-input quadratic-form density problem. This report does **not** prove its universal upper bound. It sharpens the best known lower-witness architecture: exact finite-dimensional cap-one product laws whose matrices have precisely three nonzero eigenvalues `+1,+1,-1` and whose three physical coordinate banks converge to the minimum-variance Gaussian obstruction.

No Gaussian input is used in any finite member. No post-rotation independence is asserted. Every physical input variable below is independent `Unif[-1/2,1/2]`, hence has density exactly one on a set of length one.

The designated completed partner result actually used is fleet04/B17,
`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.
It proves an exact rotated three-bank family with

`p_Qm(0)=3 sqrt(2) [1-5295/(21952 m)+O(m^-2)]`,

and therefore every universal target constant satisfies

`C_* >= 3 sqrt(2)`.

The present report (i) computes the complete second-order cone Edgeworth coefficient for every three-bank orientation, (ii) refines the partner's rational rotated family by one full order, and (iii) solves exactly the first-order optimization over **all orientations and unequal bank sizes**, including an exact genuinely rotated finite sequence attaining the optimum asymptotically.

## 2. Exact three-bank family

Let

`J=diag(1,1,-1)`.

Choose `O in O(3)` and put `B=O^T J O`. Let positive integers `m_1,m_2,m_3` be given. For bank `j`, take independent variables

`X_{jk} ~ Unif[-1/2,1/2]`, `1<=k<=m_j`,

and set

`Y_j = m_j^(-1/2) sum_{k=1}^{m_j} X_{jk}`.

Equivalently, let `R` have `m_j` physical rows equal to `e_j/sqrt(m_j)` and define

`A = R B R^T`.

Then `R^T R=I_3`, so the nonzero spectrum of `A` is exactly

`{1,1,-1}`,

and

`Q=X^T A X = Y^T B Y`.

Thus every member satisfies the exact owner spectral hypothesis in the original independent physical coordinates.

Write

`u_j = O_{3j}^2`.

These numbers satisfy `u_j>=0` and `u_1+u_2+u_3=1`; they are the squared coordinates of the negative eigenvector in the three-bank basis.

## 3. Weighted Edgeworth expansion through order two

Put `sigma^2=1/12`, and let `gamma_sigma` be the `N(0,sigma^2)` density. For the normalized sum in a bank of size `m`, direct expansion of

`[sinc(sqrt(3)t/sqrt(m))]^m`

gives

`m log sinc(sqrt(3)t/sqrt(m)) = -t^2/2 - t^4/(20m) - t^6/(105m^2) + O(t^8/m^3)`.

Fourier inversion therefore yields, with the probabilists' Hermite polynomials,

`g_m(y)=gamma_sigma(y) [ 1 - H_4(y/sigma)/(20m)
                         + {H_6(y/sigma)/105 + H_8(y/sigma)/800}/m^2 ]
         + O(m^-3)(1+|y|)^-10`.                                    (3.1)

The weighted form is justified by the same small/intermediate/large-frequency split used in the completed partner proof, now retaining two more Taylor terms. On a fixed small-frequency window use the displayed logarithmic expansion with Gaussian domination; on the intermediate window use `|sinc x|<=exp(-c x^2)` for small `x`; on the outer window use `|sinc x|<=min(1,|x|^-1)`. Applying the same estimates after ten Fourier derivatives gives the stated polynomial weight. The constants can be chosen uniformly for all sufficiently large `m`.

For three banks, multiplying (3.1) shows that every omitted term is bounded in weighted `L^1` by

`O((m_1^-1+m_2^-1+m_3^-1)^3)`.

## 4. Cone measure and exact Hermite expectations

The zero cone of `B` is parametrized by

`y=O^T(r cos(theta), r sin(theta), eps r)`,

where `r>0`, `0<=theta<2pi`, and `eps=+/-1`. Since `B^2=I`,

`dH^2/|2By| = (1/2) dr dtheta`

on each nappe. After normalizing by the leading Gaussian cone integral, `R=r/sigma` has density

`(2/sqrt(pi)) exp(-R^2)`, `R>0`,

so

`E R^(2k)=(2k-1)!!/2^k`.

For one bank let `u=u_j`. The angular/nappe moment is

`E a^(2k) = sum_{s=0}^k C(2k,2s) u^s(1-u)^(k-s)
             C(2(k-s),k-s)/4^(k-s)`,

where `a` is the corresponding bank coordinate of `(cos theta,sin theta,eps)`. Combining this with the radial moments gives the following exact cone expectations:

`h_4(u):=E H_4(Ra) = (57+6u-39u^2)/32`,                       (4.1)

`h_6(u):=E H_6(Ra)
 = -15(19u^3-111u^2+45u+63)/128`,                            (4.2)

`h_8(u):=E H_8(Ra)
 = 105(611u^4-492u^3-1902u^2+1044u+867)/2048`.              (4.3)

For distinct banks `i,j`, orthogonality of the corresponding columns of `O` gives the horizontal inner product `-O_{3i}O_{3j}`. Expanding the mixed angular moments, or equivalently coefficient-extracting from

`cosh(x O_{3i}+y O_{3j})
 I_0(sqrt((1-u)x^2+(1-v)y^2-2 O_{3i}O_{3j}xy))`,

shows that the sign cancels and

`k_44(u,v):=E[H_4(T_i)H_4(T_j)]`

is

`3/2048 * [21385 u^2 v^2 -3690 u^2 v -951 u^2
           -3690 u v^2 -11412 u v +1566 u
           -951 v^2 +1566 v +2601]`.                         (4.4)

Here `T_j` denotes the standardized bank coordinate under the normalized Gaussian cone measure.

## 5. Complete second-order cone-tip formula

Substituting (3.1) into coarea and using (4.1)-(4.4) yields, uniformly in `O in O(3)` as `min_j m_j -> infinity`,

`p_Q(0)/(3 sqrt(2))
 = 1
   - sum_j h_4(u_j)/(20 m_j)
   + sum_j [h_6(u_j)/105+h_8(u_j)/800]/m_j^2
   + sum_{i<j} k_44(u_i,u_j)/(400 m_i m_j)
   + O((sum_j m_j^-1)^3)`.                                   (5.1)

The uniformity in `O` follows because orthogonal changes preserve Euclidean polynomial weights in the cone integral.

This is a quantitative witness constraint, not an upper bound for arbitrary product laws.

## 6. Actual application to the completed fleet04/B17 witness

The partner's exact rational rotation has

`(u_1,u_2,u_3)=(9/49,36/49,4/49)`

and equal bank sizes `m`. Formula (5.1) gives **exactly**

`sum_j h_4(u_j)/20 = 5295/21952`,

recovering the partner's proved first-order term, and additionally

`sum_j [h_6(u_j)/105+h_8(u_j)/800]
 + sum_{i<j} k_44(u_i,u_j)/400
 = -3257268323/337323212800`.

Therefore the completed partner family admits the refined expansion

`p_Qm(0)=3 sqrt(2) [
  1 - 5295/(21952 m)
    - 3257268323/(337323212800 m^2)
    + O(m^-3)]`.                                               (6.1)

Numerically the second coefficient is `-0.009656223465804723...`.

This directly applies the partner result to the exact inequality

`lim_m p_Qm(0)=3 sqrt(2) <= C_*`,

while (6.1) determines how that exact rotated finite sequence approaches the universal lower obstruction.

## 7. Sharp first-order optimization over every orientation

For arbitrary unequal banks define `a_j=1/m_j`. The first-order relative deficit is

`D_1(u)=sum_j a_j h_4(u_j)/20`, `u_j>=0`, `sum u_j=1`.

The polynomial `h_4` is strictly concave because

`h_4''(u)=-39/16<0`.

Hence the minimum of `D_1` over the simplex occurs at a vertex. Since

`h_4(0)=57/32`, `h_4(1)=3/4=24/32`,

one obtains the exact sharp formula

`min_O D_1
 = [57 sum_j m_j^-1 - 33 max_j m_j^-1]/640`.                 (7.1)

The negative spectral axis should therefore be aligned, to first order, with the **smallest** bank.

For equal banks this yields the sharp orientation bracket

`69/320 <= D_1 <= 41/160`.                                    (7.2)

The left endpoint is bank-aligned. The right endpoint follows from Jensen and occurs at `u_1=u_2=u_3=1/3`. The partner's rational dense rotation lies strictly between them:

`69/320 < 5295/21952 < 41/160`.

Thus no fixed genuinely mixed orientation beats the aligned first-order finite-size obstruction inside this three-bank architecture.

## 8. Optimal unequal bank allocation at fixed total dimension

Let

`N=m_1+m_2+m_3`.

At the minimizing orientation in (7.1), label the minority-axis bank `k`. Its first-order numerator is

`24/m_k + 57/m_i + 57/m_j`.

Minimizing over positive real bank sizes with fixed sum `N` gives by Cauchy-Schwarz/Lagrange multipliers

`m_k:m_i:m_j = sqrt(24):sqrt(57):sqrt(57)`.

The sharp total-dimension coefficient is

`K_* = (sqrt(24)+2sqrt(57))^2/640
     = 63/160 + 3sqrt(38)/80
     = 0.6249155251113366...`.                                 (8.1)

Hence choosing integer bank sizes within `O(1)` of the proportions

`0.2449655296 : 0.3775172352 : 0.3775172352`

gives

`p_Q(0)=3 sqrt(2) [1-K_*/N+O(N^-2)]`.                         (8.2)

For comparison, equal banks with the best aligned orientation have coefficient

`207/320=0.646875`

when written in terms of total dimension `N=3m`. The improvement is exact:

`207/320-K_* = 81/320-3sqrt(38)/80 > 0`.                       (8.3)

Thus unequal bank allocation produces a strictly stronger finite-dimensional approach to the same `3sqrt(2)` obstruction.

## 9. Exact genuinely rotated dense sequence attaining (8.2)

The optimizer in (8.1) is spectrally aligned, but one can keep **every finite matrix genuinely rotated and fully bank-coupled** without changing (8.2). For integer `N>=2`, define the rational unit vector

`w_N = (2N^2, 4N^2, N^4-5)/(N^4+5)`

and

`B_N = I - 2 w_N w_N^T`.

Then exactly

`B_N^2=I`, `tr B_N=1`, `spec(B_N)={1,1,-1}`.

Every off-diagonal entry is nonzero, and all diagonal entries are nonzero. Take integer bank sizes summing to `N` and within `O(1)` of the proportions in Section 8, with the third bank the small one. Let `R_N` repeat `e_j/sqrt(m_j)` in bank `j` and put

`A_N=R_N B_N R_N^T`.

Every finite `A_N` is an exact dense block-coupled physical matrix with nonzero spectrum `{1,1,-1}`. Moreover

`w_{N,1}^2=O(N^-4)`, `w_{N,2}^2=O(N^-4)`, `1-w_{N,3}^2=O(N^-4)`.

Consequently the orientation perturbation changes the first-order term by only `O(N^-5)`, while integer rounding costs `O(N^-2)`. Therefore the **genuinely rotated exact sequence** still satisfies (8.2).

This gives a source-valid finite-dimensional rotated stress family that is first-order optimal within the entire independent-uniform three-bank Parseval architecture.

## 10. Additional exact second-order controls

For equal bank sizes `m`:

* bank-aligned `u=(1,0,0)`:

`p_Q(0)/(3sqrt(2)) = 1 - 69/(320m) -17411/(2867200m^2)+O(m^-3)`;

* maximally balanced `u=(1/3,1/3,1/3)`:

`p_Q(0)/(3sqrt(2)) = 1 - 41/(160m) -3511/(460800m^2)+O(m^-3)`;

* partner rational dense orientation:

`p_Q(0)/(3sqrt(2)) = 1 -5295/(21952m) -3257268323/(337323212800m^2)+O(m^-3)`.

All three second-order corrections are negative. This does **not** establish that every orientation has a negative second-order coefficient, nor that the cone tip is globally maximal for every member; those stronger assertions are not used.

## 11. What this constrains and what remains open

The universal lower obstruction remains

`C_* >= 3sqrt(2)`.

This run does not improve the limiting value beyond `3sqrt(2)`, but it sharply identifies the most dangerous finite-size direction inside a large exact rotated family: concentrate the negative spectral axis on the smallest diffuse bank and allocate physical dimensions in the square-root ratio `sqrt(24):sqrt(57):sqrt(57)`. Any proposed proof claiming a finite-dimensional slack stronger than (8.2) for all such Parseval-bank inputs is false.

A witness exceeding `3sqrt(2)` must therefore leave this asymptotic mechanism, for example through a genuinely non-CLT surviving component, several macroscopic shared rows, an off-tip peak, or additional spectrum interacting nontrivially with the three large directions.

For sufficiently large bank sizes the densities in this witness family have continuous representatives by the same weighted local-density/coarea argument. This is only a scoped family statement. The full target's continuous-density conclusion remains OPEN.

No refuted law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, post-rotation independence, naive fiber supremum, conditional positive-density moment, bounded-fragment reduction, or histogram inference is used.
