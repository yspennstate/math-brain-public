This stage follows B17 STREAM_NOTES v2's explicit A083 assignment: check the coefficient comparison behind B17-JS-PACKET-SCALAR v1. The artifact is code/JSCoefficients.lean, using installed Lean 4.33.1 and only Init.Data.Rat.Lemmas.

Define O_0=E_0=1, O_(n+1)=(2n+1)O_n and E_(n+1)=(2n+2)E_n. For every natural n>=1 the formal target is E_n<=2n O_n, hence 1/(2n)<=O_n/E_n, and after division by positive 2n-1:

    1/[2n(2n-1)] <= (O_n/E_n)/(2n-1).

The file also checks (2n)!=O_n E_n and E_n=2^n n!, using a recursive factorial definition. Thus O_n/E_n=(2n)!/[4^n(n!)^2]=binom(2n,n)/4^n on paper. The factorial identities are kernel-checked; identification with a library binomial definition is not claimed.

Finally, entropyPartial(t,N) and sqrtPartial(t,N) are explicitly defined sums of the first N corresponding coefficients times t^n. The formal theorem all_partial_sums compares them for all rational t>=0 and every natural N. It imposes no truncation cutoff and does not require convergence.

Outside Lean: for |z|<1, the real analytic identities

    [(1+z)ln(1+z)+(1-z)ln(1-z)]/2 = sum_(n>=1) z^(2n)/[2n(2n-1)],
    1-sqrt(1-z^2) = sum_(n>=1) (binom(2n,n)/4^n) z^(2n)/(2n-1)

and convergence, continuity at z=+-1 with 0ln0=0, and the spectral packet substitution z=2uv/(u^2+v^2) are ordinary mathematical steps, not part of this kernel certificate. The report reconstructs them explicitly. No full formalization of logs, square roots, real series, JS, Boolean Fourier transforms or FEI is asserted.

The runner has a 60-second timeout and 1400 MiB process-commit cap; memok.py must exit 0 before every run expected over 300 MB. The final compiler and axiom output are saved under out/. Intermediate failed checks remain distinguished from final success. No package setup, shared-library rebuild, GPU, finite Boolean census or general formalization infrastructure is needed.

Final result: PASS, compiler exit 0, 21.113 seconds, 520,015,872 bytes peak process commit. Integer comparison and factorial identities use propext and Quot.sound; rational comparisons and finite sums additionally use Classical.choice. None uses sorryAx or an added target axiom.

Reviewers: A090 primary, A094 alternate. Consumer A081 should record the coefficient/finite-sum scope separately from the surrounding scalar analytic theorem; A085 should inspect that scope before treating any numerical or formal artifact as an all-dimensional result.
