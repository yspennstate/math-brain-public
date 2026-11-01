# Alpha-log controls for the coherent remainder

Status: **PROVED at the stated first-layer scope**. Full FEI and the full A057 hierarchy target remain **OPEN**.

All logarithms below are natural.

## Imported exact interface

For balanced disjoint substitution `F=g(h_1,...,h_m)`, decompose the outer sign at coordinate `j` as `g=a+y_j b`, put `q_j=Inf_j(g)`, and let `alpha_{j,i}=hat h_j({i})`. The complete source identity is

`R_j(alpha)=q_j alpha^2 log(1/alpha^2)+Eraw(a)+alpha^2 Eraw(b)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2`.

The two coherent spectra are not identified. The source proves `R_j(alpha)>=0` by equal-mass noisy-outer normalization.

## New payment

For every genuine Boolean child and every physical coordinate,

`|hat h({i})| <= Inf_i(h)`.

Since `u^2 log(1/u^2) <= (2/e)u` for `0<=u<=1`,

`sum_i alpha_i^2 log(1/alpha_i^2) <= (2/e) I(h)`.

Multiplying by the outer pivotal probability and summing disjoint child blocks yields

`sum_{j,i} q_j alpha_{j,i}^2 log(1/alpha_{j,i}^2) <= (2/e) I(F)`.

This is a nonreusing payment: every physical coordinate occurs once at the one balanced substitution layer. In bits the coefficient is `2/(e ln 2) < 1.062`.

## Exact regimes

- `alpha=0`: the entire coherent remainder is zero.
- `q_j=0` (equivalently `b=0`): the entire coherent remainder is zero.
- Coefficientwise neighboring-support orthogonality, `a_T b_T=0` for every `T`: the entire coherent remainder is zero for every `alpha`.
- Equality in `|alpha_i|<=Inf_i(h)` means all nonzero pivotal edge differences in coordinate `i` have the same sign (unate alignment in that coordinate).
- The analytic scalar envelope `u^2 log(1/u^2)<=(2/e)u` is sharp at `u=e^{-1}`. No claim is made that a balanced Boolean truth table attains the simultaneous global constant.

## Mandatory failure control

The reviewed AND2 outer has

`R(alpha)=(alpha^2/2) log(1/alpha^2)+(3/2)alpha^2+O(alpha^4)`.

Balanced adjacent-pair parity modifications realize arbitrarily small nonzero `alpha` with leaf influence one. Hence `R<=C q alpha^2` is false for every universal finite `C`. The new theorem keeps and sums the logarithm; it does not erase it.

## Controls against named hazards

- **Parity-zero erasure:** coordinates with `alpha=0` contribute exactly zero; nonzero coordinates are charged individually before summation.
- **Restriction synergy:** no iteration through biased restrictions is claimed. This is the remaining A057 hierarchy gap.
- **Rare logarithmic costs:** the exact `alpha^2 log(1/alpha^2)` cost is present and paid by physical pivotality.
- **Whole-set addressing:** no selector increment or existential spectral coordinate is used; the inequality holds simultaneously for every child coordinate.
- **Shared-variable interference:** the theorem assumes the source's disjoint physical child blocks. It makes no overlapping-input claim.
- **Activation equivalence:** the payment is multiplied by the same exact outer pivotal factor `q_j` that appears in `Inf_i(F)=q_j Inf_i(h_j)`.
- **Actual prime gates:** the proof uses only Boolean edge differences and applies to prime children as well as decomposable ones.

## Exact obstruction left unpaid

Define

`C_j(alpha)=Eraw(a)+alpha^2 Eraw(b)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2`.

The run proves no hierarchy-summable upper bound on `sum C_j(alpha_{j,i})`. Moreover, after a physical restriction the child generally becomes biased, so the balanced interface cannot simply be reapplied. The next bounded attempt should derive the corresponding biased-child edge identity and test whether the missing coherent part telescopes against the child-mean entropy released by the restriction.

## Finite audit

`check_level1_payment.py` exhaustively enumerates all balanced Boolean truth tables through four variables (2, 6, 70, and 12,870 tables). It checks `|alpha_i|<=Inf_i` exactly using rational Walsh arithmetic and evaluates the entropy inequality numerically. The largest observed ratio `L/I` is `ln 2`, attained already by a three-bit majority-type spectrum; this is below `2/e`. The audit is a control, not evidence for sharpness or an all-dimension proof.

