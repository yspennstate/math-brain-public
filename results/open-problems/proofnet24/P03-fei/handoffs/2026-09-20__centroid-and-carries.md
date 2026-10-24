# FEI handoff: proved centroid candidate, uniform-spectrum class, carry obstruction

20 September 2026. Full FEI remains **OPEN / NOT PROVED**.

Read the [complete new proof](../continuations/2026-09-20-centroid-and-carries/REPORT.md), [integer checker](../continuations/2026-09-20-centroid-and-carries/verify_centroid.py), [actual output](../continuations/2026-09-20-centroid-and-carries/verification.json), and [byte-verified manifest](../continuations/2026-09-20-centroid-and-carries/MANIFEST.json).

The previous exact-Booleanity package is now delivered in full scientific scope; see its [delivery recovery](../continuations/2026-09-20-booleanity-order/DELIVERY.md). Its old pending-delivery language is historical. Preserve its distinction between real-valued relaxation counterexamples and genuine Boolean FEI.

## The previously unproved centroid statement is now proved

The current `2026-09-20-affine-symmetric-stopping/WORKLOG.md`, blob `3e98b23319d234477d890e6ffdead574bfc251d2`, labels candidate (C) unproved. The new report supplies an all-dimensional proof, independent of the finite searches.

For nonzero P over F_2, support A of size M, nonnegative coordinate costs c, weighted degree D_c(P), and T_c=sum c_i, sort distances from ANY center as a_1<=...<=a_M. Then

    a_j + a_(M+1-j) >= T_c-D_c(P).

Thus E_{x uniform A}|x+b| >= (n-deg P)/2 for every b in the unweighted case. More generally sum c_i |E_A (-1)^x_i| <= D_c(P).

Proof mechanism: evaluation spaces of cost <=u and <=v are orthogonal over F_2 when u+v<T_c-D_c(P). Their dimensions therefore sum to at most M. Each dimension is at least the number of support points with corresponding distance <=u, by a triangular inclusion-evaluation matrix. A failed reversed pair would force the dimension sum to be at least M+1. This closes the candidate, not full FEI.

## Consequence for uniform nonzero Fourier spectra

For noncharacter Boolean f with every nonzero |fhat|=2^-k, the odd bottom Walsh digit is exactly its full Fourier support. The inherited low-digit observation plus the new centroid proof gives

    H(f)=2k,       Ifrak(f)>=(k+1)/2,
    H(f)<=4k/(k+1) Ifrak(f) <4 Ifrak(f)<=4 I(f).

No affine-support assumption is made. Constant four is optimal over this class in the limit: standard addressing functions have H/I=4k/(k+2). The finite-k coefficient is not asserted optimal. Publication priority of these conclusions is not cleared. There is also a parameterized bound with factor R^2 when all nonzero normalized integer amplitudes are odd and at most R in magnitude; multiple valuation layers are not covered.

The first-layer scalar influence consequence already follows from isoperimetry, as the predecessor noted. It is not announced as a new general FEI bound.

## Failed higher-digit route, now with an exact proof

For odd n>=5 and f_n=1-2*1_{|x|=1}, integer Walsh coefficients are

    W(S)=2^n 1_{S=0}-2(n-2|S|).

The minimum valuation is r=1. For 1<=ell<=n-2 and 2^(ell-1)<=n, binary digit ell of W(S)/2 has algebraic degree EXACTLY 2^(ell-1). The proof uses the identity of that digit with binom(|S|-(n+1)/2,2^(ell-1)) modulo two, then Vandermonde. Thus a bound linear in r and ell is false. This is a genuine Boolean symmetric example, not a FEI counterexample. The squared-digit exploration is retained but not promoted to an additional theorem.

## Verification and continuation scope

The exact checker passed 3,152,586 unweighted center profiles, including exhaustive supports through four variables and all degree-two polynomials on five variables, plus 2,880 weighted profiles. It checked 2,136 plateaued Boolean functions through dimension four and 23 actual digit identities through dimension seventeen. Counts include overlapping families and both orders of pairs; they are not a count of distinct full FEI cases. A separate replay produced byte-identical output. No independent expert audit or proof assistant was used.

Proof blob `87923382aa41f3fd4cf355750679846d8e45e35d`, checker blob `920558b0d065286b7ab24ab554f1700ac397245f`, output blob `c68747e94445103ec36a66397ea7b317bd33e661` were read back and match local bytes. Commits: proof `9c931d664c65a363fa3fad1c1ddca8d72c4d1411`; checker `0b4a7066a6f2a2818db37343059065cf69039951`; output `07c48ed7db932a53ce8af781c658e93ef0ca2387`.

The remaining universal obligation is a mass-weighted entropy/erasure bound for arbitrary Boolean Fourier amplitudes. Uniform-support centroids alone do not supply it, and linearly bounded higher digits cannot be assumed. Preserve all previous retired targets, exact-Booleanity requirements, current positive classes and quantifier warnings. No schedules or worker ownership were changed. When reusing this work, record the actual source blob and the new mathematical step it enabled; availability does not establish future uptake.
