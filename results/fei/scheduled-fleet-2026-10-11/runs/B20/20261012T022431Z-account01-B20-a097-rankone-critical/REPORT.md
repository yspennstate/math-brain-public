# B20 / A097 — rank-one overlap cannot be a strict critical endpoint

**Run:** `20261012T022431Z-account01-B20-a097-rankone-critical`  
**Primary packet:** A097 (Cross-route transfer)  
**Attempt:** `A097-RANKONE-CRITICAL-TRANSFER-1`  
**Claim:** `B20-A097-RANKONE-CRITICAL-CLASSIFICATION-v1`  
**Gap:** `G-CRITICAL-STEP`  
**Status:** exact cross-route structural theorem proved; independent review pending; full FEI **OPEN**.

## Exact movement

B03/A014 proved that balanced selector branches of exact spectral rank one
must be signed copies of a single Boolean core:

`F(a,x)=sigma(a)g(x)`.

B11/A052 independently proved the physical critical-tensor purity law. This
run performs the missing substitution, with the same physical variables,
uniform measures, entropy units, and normalizers.

For nonconstant factors, put

`w_sigma=I(sigma)/(I(sigma)+I(g))`, `w_g=1-w_sigma`.

Then a descendant-critical rank-one selector satisfies

`R(sigma)=R(g)=R(F)`,

and both factors are descendant-critical. The converse also holds. More
quantitatively, eta-criticality implies

`|R(sigma)-R(g)| <= eta/min(w_sigma,w_g)`,

and factor descendants inherit the A052 `eta/w` criticality bound.

Most importantly, no product with both factors nonconstant can be a strict
critical core: its ratio is the influence-weighted average of the factor
ratios, and a factor with at least the product ratio is an actual proper
physical descendant. Therefore a strict critical member of the exact
rank-one balanced-selector class has no essential address block after dummy
variables are deleted.

This pays a complete structural subcase of the critical endpoint debt. It
does not solve full FEI.

## Explicit unbounded-read consequence

For the A014 family

`F_t=h_t(a) Maj_3(x)`,

the literal selector has worst-case read `2^t`, fractional congestion one,
and spectral rank one. Yet

`I(h_t)=t 2^(1-t)`, `R(Maj_3)=4/3`, `R(h_t)->4`.

For `t>=2`, eta-criticality requires

`eta >= [ (3/2)/(t2^(1-t)+3/2) ] [ R(h_t)-4/3 ] -> 8/3`.

Thus the explicit unbounded-read family stays a positive constant distance
from criticality. Its bounded FEI ledger is not hiding a candidate endpoint.

## Proof boundary

The transfer uses only two author-proved, source-pinned inputs:

1. A014 exact rank-one Boolean factorization and tensor additivity.
2. A052 critical-tensor purity under actual physical restrictions.

Both inputs remain pending their named independent reviews, so this result is
also pending independent review. No assertion is made for spectral rank at
least two, approximate rank one, unbalanced branches, or a prime critical
remainder.

The next exact target is a stable rank-two/near-rank-one decomposition with an
explicit interference potential, followed by a critical-step bound on the
prime remainder.

## Verification

Command:

`python3 verify_rankone_critical.py`

The checker exhaustively tested 3,565 controller/core pairs drawn from all
nonconstant controllers and balanced Boolean cores through three variables.
It checked 36 critical-converse descendant products and 7,130 exact eta-gap
identities. Walsh weights and influences use `Fraction`; entropy is retained
as an exact rational linear form in logarithms of primes, whose signs are
certified by rational outward intervals. All checks passed.

The finite audit is diagnostic; the all-dimensional result is the analytic
proof in `CROSS_ROUTE_SUBSTITUTION.tex`.

## Source pins

- B20 contract blob: `d5872923b24d68dbcb93394134e3309302f5d034`.
- Stream index blob: `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Execution protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A014 report blob: `b3bfea82cb0f54377d92efdd217c3206e9030e64`.
- A014 claims blob: `dd61282583f93fbd991c95ac9d831c5e2bc904a7`.
- A052 critical-source report blob: `b1f1471a031c95af710468ff01ef46b0a032b742`.
- Prior A096 tree-slack report blob: `b1f1d7e4440033f59d1b047ebb10ab0f84d3a332`.

No novelty claim, public release, scheduler change, native Brain ingestion, or
full-FEI conclusion is asserted.

