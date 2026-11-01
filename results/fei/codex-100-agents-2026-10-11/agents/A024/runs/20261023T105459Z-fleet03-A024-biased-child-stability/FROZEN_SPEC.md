# Frozen v1 before search: quadratic affine-flat policy and scalar bound

Helper: A024 stage17 code/check.py definitions before its pilot flag; SHA256
recorded in output. New checker code/check_flat.py v1, Python standard library.
Actual family: f=(-1)^(q+1_A), every quadratic q modulo constant sign, A empty
or every affine flat in F_2^D. Global sign preserves spectra/influence and is
the ONLY symmetry quotient. All flat orientations and offsets are included.
Generate every linear subspace by exact span closure, then all distinct cosets.
Flat counts including empty: D0=2,D1=4,D2=12,D3=52,D4=308.
Quadratic counts modulo sign:1,2,8,64,1024. Pilot D0..3:3434 descriptions;
full D0..4:318826 descriptions. No automatic dimension increase.
For each description: exact selected-pivot B<=4d; every one-bit restriction
checked against actual truth tables and flat membership; dense k<=2 absorption
checked by exact Boolean Mobius coefficients; affine fallback checked against
annihilator/fiber formula; H<=7I checked directly. Finite evidence is not the
all-dimensional proof: DERIVATION supplies that proof explicitly.
Pilot<60 seconds; full<=600 seconds. Truth tables <=16 entries, no root list
materialization; local and stats caches capped4096, tree cache1024. Estimated
memory<200MB. Fraction arithmetic, integer Walsh, exact prime-log vectors and
24/48/96-term rational atanh sign certificates inherited from prior helper.

Scalar tests: L(a,b)<=2|ab| for a,b in {-8,...,8}/8 (289 pairs).
R<=6r|beta| for a=j/8, j=-8..8; beta=b/8, b=0..8-|j|;
r=l/16, l=0..16 (81*17=1377 triples). These feasible marginals can be realized
by finite Boolean children. Exact sign intervals, no floating-point inference.
Positive controls: L(1,1)>19/10 and R_(1/2)(0,1)>0 must be witnessed exactly.

Activation replay, separate sequential job<=180 seconds: 8 explicitly listed
flat/quadratic fixtures, all64 ordered pairs, all one-query physical prefixes
and complete repaired continuations. Max total dimension8. Direct full actual
spectra check B<=10d, full both-terminal H/I telescope, zero additional K10-bad
debit, H<=13I. Pilot uses first4 fixtures (16 pairs). Caches capped as above;
memory estimate<200MB. Existing original credit and prefix debit not renewed.
