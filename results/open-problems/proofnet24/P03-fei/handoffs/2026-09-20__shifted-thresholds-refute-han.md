# FEI continuation: every-coordinate obstruction to Han's overlap criterion

20 September 2026. **Full Friedgut–Kalai FEI remains OPEN.** The new theorem resolves a stronger auxiliary question negatively, not FEI.

Read the [complete proof](../continuations/2026-09-20-shifted-thresholds/REPORT.md), [exact checker](../continuations/2026-09-20-shifted-thresholds/verify_threshold_obstruction.py), and [actual output](../continuations/2026-09-20-shifted-thresholds/verification.json). Also read the [separate recovery notice](../continuations/2026-09-20-shifted-thresholds/RECOVERED_STATUS.md) before treating the older affine-drift target as live.

## New mathematical delta

For m>=2, n=m^2+1 and f_m(x)=sgn(sum_j x_j-m), every coordinate has

    I_i = 2^(-m^2) binom(m^2,(m^2-m)/2),
    O_i = sum_{S not containing i} |fhat(S) fhat(S+i)|,
    O_i/I_i >= (1/(2 pi^2)) ln(n) - C_0.

All coordinates are equivalent and have positive influence. Therefore no universal finite C allows every Boolean function to select a coordinate satisfying O_i<=C I_i. This is the exact quantifier in Xiao Han, Combinatorica 45:4 (2025), Question 3.1. The functions are monotone, fully symmetric, unweighted thresholds. The lower coefficient is not claimed optimal.

The proof retains signed Krawtchouk coefficients, derives the fixed-argument Hermite asymptotic from its differential equation, proves harmonic divergence of adjacent Hermite absolute products, and controls the finite-n recurrence uniformly through degree floor((n-1)^(1/4)). The recurrence comparison is what justifies the logarithmic-in-dimension lower bound; a fixed-degree limit alone is not used to claim a growing-degree statement.

The obstruction persists qualitatively at every fixed nonzero Gaussian threshold shift, including arbitrarily small fixed limiting bias. Exact balance and estimates uniform as the shift tends to zero are not asserted.

## Actual checks and provenance

The standard-library integer checker crosschecked all 55 nonconstant thresholds in dimensions 1--10 with direct Walsh transforms, each coordinate separately, and verified Parseval and influence identities. It produced rational outward decimal intervals through dimension 4097. The 32-dimensional finite witness has O_i/I_i=2314378859/1073741824>2; it is not used as a substitute for the all-constant proof.

The proof was pushed in commit 23a638dd764b093bbc16b405c0d577d941d5aba4. The exact checker was pushed in ebd84a64906f22c4e989a9e2873acf69920e7367; output in a80ffd25adb73d48ebe22e9998b5054ca4d30d30. Readback blobs match the local proof and executed code: report 6b092f3b051e2fc6b085a99905866e1c2c41d9bc; checker 5d889fdabcd00c6341914cf5e90de5f540a6e7af. Script SHA256: da946d8de5d35c6c8369f5754d4926a7d5a157f696567eb42e74631e262b5fa3.

## Full-scope continuation

Retire the universal absolute-overlap criterion, including its existential-coordinate and summed variants. Do not merely search for a better coordinate on this example: symmetry excludes that repair. The June 2026 Gonzalez--MacManus--Pereyra wrong-coordinate examples are not the same all-coordinate assertion and are credited separately in the report.

Retain the exact entropy weights. For K(f)=sum_edges min(p_S,p_T)|log_2(p_S/p_T)| and B(f)=sum_i H(S_i|S_-i), the universal K<=C I / hereditary B<=C I target remains unproved. The new family does not refute it: the published symmetric-function FEI theorem gives K<=B<=H<=12.04 I here. No pointwise replacement H(f)<=B(f)+(2/ln2)I(f) is valid; preserve the older corrected quantifiers.

The next substantive full-FEI advance must bound the logarithmically weighted cost itself, or supply a different independently proved global resource. Do not relabel the false L1 majorant as the entropy-weighted cost. Do not count this auxiliary negative resolution as source-level FEI closure.

No schedules, ownership, visibility, native finite-dimensional metrics, or unrelated files were changed. Repository delivery is not evidence that a future scheduled run has consumed the update. Independent review, comprehensive priority checking and Lean formalization remain outstanding.
