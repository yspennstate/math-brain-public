# Renewal extension to d18 and d19

Status: exact encoded-operator checks completed, proof (unaudited), C018-v1. The full FPP interpretation remains pending independent review; no independently checked FPP bound is asserted.

The d21 manuscript unique_height_renewal.md supplies the geometric and all-length argument under review. This extension changes the dimension and the rational parameter point. Its hardest open piece remains the proof of the all-length finite-word interpretation, including the prefix/no-cut/suffix decomposition; a matrix certificate alone does not establish that argument.

K21 screens target C011-v3 plus 0.000008: d19 approximately 0.077855718914 (floating ratio 0.999936485709), d18 approximately 0.080099928277 (0.999907619657). New s values are rounded upward to multiples of 10^-6; z retains the original exact parameter fraction. The arbitrary positive floating vector is a witness to be checked, rather than a proved eigenvector.

Both exact parameter points satisfy r=d(z+t^4/z)/((s+1)t)<91/100 for t=7/5. The scalar length>400 remainder is bounded by t*(91/100)^401/(1-91/100)<10^-15. All original d21 sources and certificate hashes have been checked unchanged before making these dated copies. Saved unified diffs show every producer change.

The finite encoded operators, their exact norm checks, scalar recurrence and outward row checks are certified separately by run_renewal_extension.py. Passing those checks will justify an encoded contraction only. Full FPP bounds require the geometric encoding and all-length proof to be accepted.

## Completed finite certificates (2026-10-15T04:40:50.090238+00:00)

d=19: encoded operator contraction factor <= 999936480509838187/1000000000000000000; exact downward floor of sqrt(d) log(z)/s = 0.077855718601. Each dimension has 2564 rational common-norm inequalities and 330 outward-rounded renewal rows.

d=18: encoded operator contraction factor <= 199981523775907539/200000000000000000; exact downward floor of sqrt(d) log(z)/s = 0.080099928228. Each dimension has 2564 rational common-norm inequalities and 330 outward-rounded renewal rows.

These six producers all exited successfully. Reflection counts were checked against killed walks through n=30; scalar renewal coefficients against exhaustive sign profiles through n=15. Every finite-operator truncation is covered by the scalar upper tail with ceiling 91/100. The exact floor uses integer square-root lower bounds and a positive 50-term logarithm series.

The original d21 geometric construction and the prefix/no-cut/suffix argument require independent review before these floors are promoted to FPP time-constant lower bounds. Pending that review, C018 states only the finite encoded-operator result. No new dimension or novelty claim is made.
