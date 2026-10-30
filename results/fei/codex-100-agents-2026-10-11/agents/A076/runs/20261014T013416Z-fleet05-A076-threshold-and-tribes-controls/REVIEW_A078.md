# Independent review of the signed rare-private-query obstruction

Reviewer A076; no substantive repair. Scope: A078-PAIRED-QUARTER-PROFILE-AND-PADDING
@2, appended actual Boolean family, full influences, signed erasure formula
and D_x/Inf_x>=k-4 in PROOF.md sections 1-2 only. Earlier quarter-profile
theorem, L asymptotics, and other bundle clauses are not reviewed here.

Reconstruction: build the two actual Boolean branch tables independently,
FWHT their fresh-selector mux, and pair coefficients at the physical x query.
The common-frequency terms are S(-a,a;b), except the empty row S(1-a,a;b).
The sign of each bent coefficient cancels by symmetry. For nonempty rows,
the product of the two shifted squared amplitudes is (b^2-a^2)^2; since
b^2=a, the logarithmic lower bound becomes exactly
a^2 log2(N-1)/2-a^2. The negative empty-row bound follows from
Phi(p,q)<=q log2(e(p+q)/q), p+q<=1, and log2(e)<3/2.
Divide the summed bound by a/2 to obtain
(1-1/N)log2(N-1)-2(1-1/N)-(2k+3/2)/N.
For k>=4, log2(N-1)>=k-1 and 3k/2^k<=1 give the asserted k-4 lower
bound (the displayed intermediate error bound in A078 is conservative).
All these steps are analytic, not extrapolations from the finite checks.

The edge calculations give x influence a/2, each shared influence
(a+1/2)/2, and selector influence (1-b+a)/2 because E(GH)=b-a. Thus the
obstruction uses an actual rare private query and includes all physical
influences. It does not imply failure at every coordinate or FEI failure.

code/check_review.py independently checks actual spectra, physical x influence,
compressed row equality and signed lower bounds at k=2,4,6, including the
strict k=4 violation of factor two, using exact logarithmic products and
proved rational intervals. out/REVIEW_VALIDATION.json records execution.
Verdict: HOLDS_AT_SCOPED_STAGE3_SIGNED_OBSTRUCTION. The new owned-pivot
policy in OWNED_PIVOT_PROOF.md consumes this adverse fixture; it does not
repair or alter the reviewed statement.
