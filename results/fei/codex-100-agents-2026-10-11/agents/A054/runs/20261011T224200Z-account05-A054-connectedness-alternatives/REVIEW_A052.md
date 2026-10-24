# Independent analytic reconstruction of A052 v1

Source: A052-AFFINE-SYNDROME-CRITICAL-DISORDER v1, run
20261011T220243Z-account05-A052-critical-source-structure, equations (1)--(3)
of CRITICAL_SOURCE_STRUCTURE.tex and the analytic proof in REPORT.md.
Verdict: ACCEPT_AT_STATED_SCOPE, analytic reconstruction only; registry
adoption is pending. No repair or contribution to that source version.

I reconstructed the information identity by expanding the relative
entropy of each partial-Fourier row: sum_t Ent(v_t²)/ln2 equals the
mutual information because Boolean children each have mass one.
Multiplication by a fiber-dependent character preserves v_t² pointwise
and shifts only the row's Fourier labels. Consequently its physical
Dirichlet energy is sum_e |e+e0(t)| fhat(e,t)². The elementary two-point
log Sobolev proof and product tensorization give the factor 2/ln2.
This does not require the demodulated function to be Boolean or a child.

The invertible pivot makes e->V_Ae+V_Ct a bijection for fixed t, so the
conditional entropy equality is exact. With epsilon outside y0, every
mismatch weight is at most r and maximum entropy at fixed epsilon is
h2(epsilon)+epsilon log2(2^r-1). Criticality enters only through the
average deficit of actual physical children; none inherits criticality.
For rank one, Fourier orthogonality gives the flip-mask correlation
sum_s fhat(s)²(-1)^(u dot s). Choosing the majority syndrome yields
epsilon=(1-|correlation|)/2. Zero rows and zero influence cause no division.

I found no unsupported line within the stated theorem. The unsupported
universal block-selection line is correctly excluded. The A054 checker
independently validates the unshifted real-function channel identity and
the raw-mass extension; it does not claim to replay A052's full affine
syndrome census. The review retires one of B11's two existing pending
bundled candidates before the new A054 candidate is handed off.
