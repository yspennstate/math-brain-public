# FEIB10 report

Containment does not follow from the hypercontractive size axiom alone. An explicit family satisfies even the sharper Boolean prefactor and has A/I=s/3+1+o(1), hence no universal bound. The construction and proof are in [PROOFS.md](PROOFS.md); [RESULTS.md](RESULTS.md) contains the numerical tables.

The measure has n=2^s coordinates and d=2^(2s/3), with s a multiple of 6 and s>=36. Put mass 1-2^-s-4^(1-d) uniformly on the s-subsets, mass 2^-s uniformly on the d-subsets, and mass 4^(1-d) on [n]. This is a probability measure with explicit rational weights. For example s=36 gives n=68,719,476,736 and d=16,777,216, with A/I approximately 12.9999269065 bits per expected element. At s=384 the ratio is approximately 129.0. These evaluations are from counterexample_output.json; divergence is proved without floating point.

Verdicts on the numbered brief:

1. PROVED and CHECKED. Boolean spectra obey `mu{U>=R, |U-R|<=k} <= 3^k 2^(|R|-1) up(R)^(3/2)` for nonempty R. The uniform axiom is C(3,2,1/2), and b=2 is optimal uniformly in dimension. Checked on all 65,536 four-variable Boolean functions and a seeded sample of 4,232 six-variable functions, for every R and relevant k. No C or Csharp violations. See check_boolean.py and boolean_output.json.
2. PROVED: counterexample. verify_counterexample.py certifies the whole family through exact integer sufficient conditions and symmetry; audit_counterexample.py independently checks exact squared first-layer inequalities using falling factorials. A direct rational enumeration also verifies a smaller instance, n=4096, with A/I approximately 5.01378983506, across every rank and every CDF jump. Direct and structured optimization on n<=6 is saved; the best feasible local value found at n=6 is 4.187125460. Finite search values are lower bounds, not certified global suprema. See exact_finite_output.json, small_repaired.json, families_output.json, and EXTREMAL_MEASURES.md.
3. PROVED: square-Parseval separates the example from Boolean spectra. For any s-set S, the Fourier coefficient of f^2 at [n] minus S would have exactly one unordered contributing pair, {S,[n]}, and cannot vanish for any Fourier signs. The example nevertheless satisfies the Boolean mean-granularity inequality `mu(R)<=4^(|R|-1)up(R)^2`, the natural scalar existential-p analogue, and a valid derivative level-1 inequality. The proposed thinning closure with unchanged constants is itself false for Boolean spectra: a dictator thinned at rho=1/8 violates C. All candidate inequalities and their numerical scopes are stated in PROOFS.md section 3 and checked by the supplied scripts.
4. PROVED: the conditional branch is not triggered, because containment fails. The same family also has B/I unbounded; an explicit lower bound is in PROOFS.md section 4. No additional cancellation axiom is claimed.

Verification and limits:

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 run_checks.py` from this folder at nice >=10. All six verification scripts passed. The recorded run inherited nice 10, requested one numerical backend thread, and peaked at 63,209,472 bytes of child RSS, well below the brief's process limit. See verification_output.json. The initial search had ordinary SLSQP boundary warnings and Apple numerical-backend flags; all saved finite witnesses were repaired and independently rechecked using non-BLAS sums and relative constraint ratios.

The numerical tables do not certify global optima for finite n>1. The general Boolean containment conjecture and FEI remain open. It is also open whether selected square-Parseval consequences, combined with the scalar axioms, suffice for containment.

Brain consultation: the startup memory and a two-wording recall were read. The recalled FEI split/census note confirmed the notation and existing reductions; it did not supply this counterexample. The math recall command reported that the math store was not found. No brain or shared-project result was published: the fleet rules reserve that to the launching session. The referenced check_feib09.py was absent, so every check used here was written in this folder.

Task: “decide whether containment follows from the hypercontractive size statements alone” — first recorded session clock 10 Nov 2026, 02:58 +04 (Asia/Tbilisi).
