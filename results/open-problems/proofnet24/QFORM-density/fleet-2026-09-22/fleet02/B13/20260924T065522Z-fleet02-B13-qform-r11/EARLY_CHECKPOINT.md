SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-24T06:55:22.857152Z.
attacking: the rank-one plus four-diagonal rough survivor; replace absolute support radius by a translation-invariant product-diameter obstruction while retaining the separable and entangled tails.

# Early substantive checkpoint

Status: supporting theorem only; unrestricted QFORM remains OPEN and continuity remains separate.

## First unpaid implication

`QFORM-DIAMETER-BANK-TO-ROUGH-RECEIVER-v1`: in the partner fleet03/B13 r45 normal form, convert the forced translation-invariant spread of the original product sets into a density payment while keeping the O(rho^-1) separable diagonal tail and the genuinely entangled secondary carrier inside the phase; otherwise construct a finite-union product-indicator counterexample sequence satisfying the spread lower bounds below.

## Translation-invariant support-width lemma

Let X_i be uniform on bounded measurable sets E_i of measure one. Suppose A=M+F and every affine perturbation of the M-form has density at most C_M under the translated product laws. Put

h_i = (ess sup E_i - ess inf E_i)/2,
H^2 = sum_i h_i^2.

For a slab J with ratio rho=P(X^TAX in J)/|J|, choose m_i=(ess sup E_i+ess inf E_i)/2 and write X=m+Y. Then |Y_i|<=h_i and

X^TAX = [Y^TMY+2(Am)^TY+const] + Y^TFY.

Thus all remote translations are absorbed into the affine term of the paid M receiver. If delta=sup_{|y_i|<=h_i}|y^TFy|, then

rho <= C_M(1+2 delta/|J|).

In particular delta<=||F||op H^2, and if rho>=2C_M,

H^2 >= rho |J|/(4 C_M ||F||op).

Hence if ||F||op<=C_F/rho,

H^2 >= rho^2 |J|/(4 C_M C_F).

Equivalently, with diam_i=ess sup E_i-ess inf E_i,

sum_i diam_i^2 >= rho^2 |J|/(C_M C_F).

This is strictly stronger than an absolute-radius escape statement: translating a unit-measure component arbitrarily far does not help activate F after recentering, because the translation is paid by the affine-uniform M receiver.

## Partner-r45 specialization

The latest completed designated partner fleet03/B13 r45 supplies, in the hard diffuse exact-rank-two survivor, a physical normal form

A = D_C + lambda_1 vv^T + E_sep + E_ent,   |C|<=4,
||E_sep||op <= C_D/rho,   C_D=2 sqrt(30 pi),
||E_ent||op = O(rho^-7/6),

with E_sep diagonal and E_ent a retained secondary carrier. Put M=D_C+lambda_1 vv^T. The already-proved finite-direction grouping theorem pays every affine M-form once s_3(M)>=1/2, with

C_M = 500 e * 5 * (8+log 5) = 65302.90114768759... .

For sufficiently high rho, Weyl gives s_3(M)>=1/2. Define

H_tail^2=sum_{i notin C} h_i^2,
W_w=sum_i |w_i| h_i

when E_ent=lambda_2 ww^T. Then

delta <= (C_D/rho) H_tail^2 + |lambda_2| W_w^2.

Therefore every rho>=2C_M witness satisfies

C_D H_tail^2 + rho |lambda_2| W_w^2 >= rho^2 |J|/(4 C_M).

So either

H_tail^2 >= rho^2 |J|/(8 C_M C_D)

or

W_w^2 >= rho |J|/(8 C_M |lambda_2|).

Using only partner r45's |lambda_2|<=K_ent rho^-7/6 gives W_w^2 >= rho^(13/6)|J|/(8 C_M K_ent) in the second branch. The tail-spread denominator is explicit:

8 C_M C_D = 10143504.402673082... .

No moment, bounded-diameter, centered-support, fixed-fragment-count, attained optimizer, or post-rotation independence assumption is used. The finite-union approximation is used only to make the support widths finite for each strict witness; the lower bound says those widths must diverge along an unbounded-density sequence.

## Pinned Fourier obstruction

From the required completed D5 theorem at math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, every physical cross block B=A[I,J] of the same slab witness obeys

e_5(B^TB) <= (5 sqrt(2e)/rho)^10,

hence

s_5(B) <= 5 sqrt(2e)/rho.

Thus any counterexample sequence satisfying the diameter escape above must simultaneously lose fifth physical cross-volume on every original-coordinate cut. This is an actual inequality-level use of the pinned source; its numerical counterexample search is not used as proof.
