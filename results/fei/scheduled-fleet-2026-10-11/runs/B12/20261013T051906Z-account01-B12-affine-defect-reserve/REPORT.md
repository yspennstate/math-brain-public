# B12 / A057 — sharp source reserve for affine-coset character flips

Run ID: `20261013T051906Z-account01-B12-affine-defect-reserve`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-11`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v11`  
Status: **PROPER-CLASS THEOREM; PENDING INDEPENDENT REVIEW; FULL FEI OPEN**

## Outcome

The previous run proved that overlap plus the paid selector alpha-log envelope
cannot control the signed block associator, and that any payment by the exact
source influence needs coefficient at least `8 ln 2`.  This run proves that
the forced coefficient is also sufficient on a genuinely broader all-parameter
class: arbitrary affine-coset flips of a character, including correlated
affine constraints and their adaptive nonreusing hierarchies.

Let `D` be an affine subspace of codimension `k>=1`, let `chi` be a nonconstant
character, and set

`g-=chi`, `g+=chi(1-2 1_D)`, `a=chi(1-1_D)`, `b=-chi 1_D`, `h=-chi`.

For the signed full-block associator

`Omega=E_nat(a+h b)-E_nat(a)-E_nat(h b)`,

the exact classification is:

- if `chi` varies on `D`, then `Omega=0`;
- if `chi=+1` on `D`, then `Omega<=0`;
- if `chi=-1` on `D`, then `Omega<=4 p k ln2<=8 ln2 I(b)`, where
  `p=2^-k`.

Consequently `Omega<=8 ln2 I(b)` for every member of the class.  For coordinate
subcubes with `chi=-1` on `D`, `Omega/I(b)->8 ln2`; the constant is sharp.

## Actual hierarchy payment

At an adaptive nonreusing physical hierarchy whose reached local branch pairs
all have this affine-coset form, keep the actual reach weights `w_v` and assume
the local sources `b_v` are restrictions of one physical source `b`.  The
local theorem and the exact derivative-energy ledger give

`sum_v w_v Omega_v <= 8 ln2 sum_v w_v I_{B_v}(b_v) <= 8 ln2 I(b)`.

Thus this class has one source-influence payment with no factor depending on
depth, block dimension, codimension, address count, overlap, or changing
activation weights.  This is the first positive source-reserve theorem after
the overlap-only falsifier.

## Proof mechanism

The Fourier transform of an affine-coset indicator is flat on its annihilator
`W`.  Multiplication by `chi_r` translates that flat support to `r+W`.

If `r` is not in `W`, the character varies on the coset.  The spectra of
`a`, `h b`, and `a+h b` have respectively `2^k-1`, `2^k`, and `2^(k+1)-1`
small coefficients of the same magnitude, plus the same large coefficient;
their entropy contributions cancel exactly.

If `r` is in `W`, the character is constant.  Only the negative level can
give a positive associator.  With `p=2^-k`, `L=k ln2`, and
`Phi(t)=t ln(1/t)`, its exact value is

`Phi((1-2p)^2)-Phi((1-p)^2)+(p^-1-1)Phi(4p^2)-(2p^-1-1)Phi(p^2)`.

Writing the first difference as `A(p)`, the identity becomes

`Omega=A(p)+(4p-6p^2)L-8p(1-p)ln2`.

For `f(t)=Phi((1-t)^2)`, `f'(t)<=2`, so `A(p)<=2p`.  Since `p<=1/2`,
`2p<=8p(1-p)ln2`, proving `Omega<=4pL`.  If `m` physical coordinates occur
in `W`, then `I(b)=pm/2>=pk/2`, which gives the claimed constant.

## Mandatory controls

- **B01/A003 parity/two-defect tensor seed:** its defect set `{000,111}` is
  an affine coset on which parity varies, so the B12 associator is exactly
  zero.  The signed cap-alignment obstruction remains real for its own KL/JS
  claim, but it does not falsify this affine associator theorem.
- **Rare logarithmic cost:** the negative-level codimension-`k` family has
  the same `p k` rare-event scale as the point defect and makes `8 ln2` sharp.
- **Shared-variable interference:** the selector is the same character used
  in the branches; no disjoint-product law is invoked.
- **Parity-zero/activation equivalence:** the varying-character case cancels
  exactly, rather than being bounded by absolute values.
- **Near tensors/addressing:** no universal claim is made outside the stated
  affine-coset class; the remaining arbitrary-source step is explicit.

## Verification

Command: `python3 check_affine_defect.py`

The checker uses exact `Fraction` Walsh arithmetic and exhausts all `4998`
affine-coset/nonconstant-character instances through four variables.  It
checks `3294` varying, `852` positive-level, and `852` negative-level cases,
the `8 ln2` bound, Boolean realizability, and the B01 two-defect zero.  The
all-dimension theorem and sharp limit are analytic in
`AFFINE_DEFECT_RESERVE.tex`; enumeration is a reconstruction check only.

## Movement and remaining gap

Prior status: the source influence had the correct scale only on the
point-defect falsifier; sufficiency was unproved on any correlated
all-parameter overlap class.

New status: coefficient `8 ln2` is proved sufficient and sharp for every
affine-coset character flip and for adaptive nonreusing hierarchies built from
those local pieces, with one physical source budget.

Still open: replace spectral flatness of each affine-coset source by a
quantitative defect—e.g. a mixture of affine cosets whose translated Fourier
supports overlap—and prove a reserve of the form

`sum w_v Omega_v <= 8 ln2 I(b) + C * (single-use nonflat terminal reserve)`

without charging the same source at multiple ancestors.  This is the next
strictly larger class.  A057 is not complete, independent A091/A090 review is
pending, and full FEI remains **OPEN**.

