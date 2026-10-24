# B12 / A057 — one source reserve for two nonorthogonal affine defects

Run ID: `20261013T062350Z-account01-B12-two-coset-reserve`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-12`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v12`  
Status: **STRICT CLASS EXTENSION; PENDING INDEPENDENT REVIEW; FULL FEI OPEN**

## Outcome

The preceding run paid a single affine-coset character flip sharply by
`8 ln 2` times source influence.  This run removes spectral flatness of the
complete source.  The source may now be the union of two affine cosets with
arbitrarily overlapping annihilator spectra, provided the two physical pieces
are at Hamming distance at least two.

Let `x` be a physical selector, let `E1,E2` be disjoint affine cosets in the
remaining variables, put `s=1_E1+1_E2` and

`d(x,z)=1_{x=-1}s(z)`.

For the genuine Boolean branches `g-=x`, `g+=x+2d`, with `a=x+d`, `b=d`,
`h=-x`, the signed associator satisfies

`Omega=E_nat(a+h b)-E_nat(a)-E_nat(d) <=16 ln(2) I(d)`.

No Fourier orthogonality or common annihilator is assumed.  This is a proper
two-piece theorem outside the one-flat-spectrum class.  The constant is
dimension-, codimension-, direction-, overlap-, bias-, and depth-independent;
it is not claimed sharp.

## Actual hierarchy statement

For any adaptive nonreusing physical hierarchy in which every reached local
source has this separated two-coset form and the local sources are restrictions
of one physical source `b`, the actual reach weights obey

`sum_v w_v Omega_v <=16 ln(2) sum_v w_v I_{B_v}(b_v) <=16 ln(2) I(b)`.

Thus both affine pieces and all changing activation weights are paid by one
source budget, without a per-piece or per-depth recharge.

## Proof mechanism

The new ingredient is an entropy-of-superposition inequality.  For two real
Fourier coefficients `r,t` with `r^2+t^2<=1`,

`Phi((r+t)^2)<=2Phi(r^2)+2Phi(t^2)+(r^2+t^2)/e`.

Summation gives

`E_nat(s)<=2E_nat(1_E1)+2E_nat(1_E2)+p/e`,

where `p=Pr[s=1]`.  Each affine indicator has

`E_nat(1_Ej)<=4 ln(2) I(1_Ej)`.

Physical distance at least two makes the derivative cross term exactly zero,
so the two influences add even though their Fourier supports overlap.

Pairing Fourier coefficients in the selector direction also gives the exact
identity

`Omega=E_nat(s)+C(p)`,

where

`C(p)=Phi((1-p)^2)-3Phi(p^2/4)-Phi((1-p/2)^2)-p(1-p)ln4<=0`.

Finally `I(d)=I(s)/2+p/4`.  These identities yield the displayed `16 ln2`
constant.

## Verification and controls

`python3 check_two_coset.py` uses exact `Fraction` Walsh arithmetic.  It
exhausts every separated pair decomposition through four slice variables:

- `3516` affine-coset pair decompositions;
- `2420` distinct unions counted by dimension;
- `3128` genuinely non-affine pair cases;
- `3452` positive-associator cases;
- zero violations of the theorem or its exact influence identities.

The largest non-affine ratio in that finite scope is `2.49682381449...`, for
a point plus a disjoint affine line.  The finite search is reconstruction
evidence only; the all-dimension theorem is analytic.

Mandatory guards:

- **Shared-variable interference:** the selector is a physical coordinate of
  the same composition; no false raw-convolution tensor rule is used.
- **Spectral overlap:** annihilator spectra may overlap arbitrarily; the proof
  uses signed superposition, not orthogonality.
- **Rare defects:** both codimensions are unrestricted and the logarithmic
  entropy is retained.
- **B01/A003 two-defect control:** two separated points are included; its
  signed alignment obstruction does not violate the theorem.
- **Activation weights/depth:** actual weights sum through the nonreuse
  derivative ledger.
- **Adjacency:** deliberately not discarded.  If the pieces are adjacent,
  `I(s1+s2)<I(s1)+I(s2)` because of a negative derivative cross term; this is
  the explicit next unpaid collision.

## Movement and next gap

Prior status: a sharp source payment was known only when the complete source
was one affine coset and hence spectrally flat.

New status: two nonparallel affine pieces with overlapping spectra have a
single dimension-free source payment.  This is a strict class extension;
`16 ln2` replaces the sharp one-piece `8 ln2`.

Next action: remove the distance-two condition.  For adjacent pieces, retain
the exact negative derivative cross term

`I(s1+s2)=I(s1)+I(s2)+2<grad s1,grad s2>`

and prove that the entropy associator supplies a matching collision refund,
or construct a scalable adjacent-coset falsifier requiring an additional
terminal boundary reserve.  Arbitrary many-piece and arbitrary-source
coherent remainders remain open.  A057 is not complete, independent A090/A091
review is pending, and full FEI remains **OPEN**.

