# Whole review of A010-DENOMINATOR-CAPS-AND-JOINT-PAIR-PACKING@1

Source-declared statement hash: ddc55eebe48a4483fd797bca1b36d75a01dcf7fcbf30db9bd94f2238f97feb95.
Actual SHA256 of the consumed exact_statement text:
4277ffe54b05e9848ef6fb1e0497beaf97f110863ea8bbffc0872aeb6194aa14.
The final readback caught this mismatch. Source files remain untouched; the
local reviewed copy corrects only its hash metadata and binds every new
dependency to the actual consumed text. No cause of the source mismatch is
inferred, and the declared digest is not treated as verified identity.
Verdict: HOLDS at its stated scope, without repair. This is a reconstruction by
A006, the author of two upstream premises; that authorship is disclosed. It is
independent reconstruction of the new extension, not independent origination
of the upstream full-family identity. No acceptance by another agent of this
stage's extension is claimed.

The denominator proof expands D_T/prod(lambda/4) as
sum_(j=0)^(k-1)4^j e_j(1/lambda). Each j-fold product has mean bounded below
by (k/L)^j by two applications of AM-GM; j=0 is one. The resulting denominator
is (1+4k/L)^k-(4k/L)^k, positive. For k>=2 its retained last term is exactly
the old product/sum bound's denominator, and the other positive terms establish
strict improvement, including when the old bound is capped at one. Equality
requires equal weights in T. When equal weights are packing-feasible, scaling
them by 1-epsilon leaves room for sufficiently small positive outside weights;
this proves the sharp supremum assertion and does not claim an attained
maximum in the larger positive table. Irregular equal-weight-infeasible
subsets are correctly excluded from that sharpness statement.

For an incident pair, p_i,p_j,r are strictly positive. Cancellation recovers
lambda_i=4r/p_j, lambda_j=4r/p_i. The common row gives
p_i p_j>=4r(p_i+p_j). It implies both diagonal signs, so the determinant
test really is equivalent to the displayed PSD cone. For exactly two gates,
normalization and the reconstructed weights regenerate all three probabilities;
this sufficiency is not extended to larger tables. The rational falsifier has
determinant -2/81, reconstructed row sum 17/15 and t=1/2 cut -1/18.

check.py rebuilds the 67 complete graph coefficient tables using A006's
pre-existing chronological enumerator, rather than importing A010's parent-map
implementation. It independently computes integer Walsh spectra and flip
influences and matches every h coordinate and all 5,878 distinct runs. replay.py
rechecks every subset's rational packing primal/vertex-price dual, sharp cap,
old support optimum and new dual bound. The original 61/67 strict cap gains
are verified from the resulting exact objectives. The same replay reconstructs
the complete-star h formula and all 31 cardinality primal-dual certificates,
including strict improvement and the I/6 natural-gap bound. Pair reconstruction
and determinant equality are checked on 120 rational positive weight pairs,
including saturated packing boundaries. These tests supplement the analytic
all-table/all-positive-weight proof; they are not substitutes for it.

The attempted Lean statement of this stage concerns the new anchored row
identity only and returned RUNTIME_UNVERIFIED. It supplies no formal acceptance
of this review or of A010's theorem. Universal complete-cost payment remains
open, exactly as A010 states.
