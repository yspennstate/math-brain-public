Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# Correction to `2026-09-20T1400+0300__quadratic_neutral_comparator_kurtosis_target.md`

This is a correctness/notation correction only; it does not change the numerical theorem or the next attack.

In Section 1 of the substantive report, replace the displayed definition

\[
R_{2,D}=(I-\Pi_{*,D})H_2(Z_D)
\]

by the exactly centered definition

\[
\boxed{
\widetilde H_{2,D}
:=H_2(Z_D)-\mathbf E_*H_2(Z_D),
\qquad
R_{2,D}:=(I-\Pi_{*,D})\widetilde H_{2,D}.
}
\]

Here `Pi_{*,D}` is the `L^2(u_*)` orthogonal projection onto the centered selected-feature span. With this definition,

\[
\mathbf E_*R_{2,D}=0,
\qquad
\mathbf E_*[R_{2,D}(\Phi_D-\mu_*)]=0
\]

hold **exactly**, so `L_n+bR_{2,D}` has exactly the same normalization and selected target moments as `L_n` for every finite `n`.

The omitted centering scalar is asymptotically negligible. Indeed, with `m=|D|`, root orthogonality gives

\[
\mathbf E_* S_D^2
={m(n-2m)\over2(n-1)},
\]

hence

\[
\mathbf E_* Z_D^2
={8m(n-2m)\over n(n-1)}
=1+O_{\mathbf P}(n^{-1/2}),
\]

while `E_*Z_D=O_P(n^{-1/2})`. Therefore

\[
\mathbf E_*H_2(Z_D)=O_{\mathbf P}(n^{-1/2}).
\]

Subtracting this scalar changes every fixed polynomial-exponential moment in Sections 3--5 by `o_P(1)`. Consequently the formulas

\[
A(a)=e^{a^2}(1+a^2+a^4/4),
\quad
B(a)=-{e^{a^2}\over2}a(a^2-a+2),
\quad
C(a)=e^{a^2}((1-a)^2+1)
\]

and the optimized finite-model bound

\[
\nu_{c_*}^2\le0.450370864992+o_{\mathbf P}(1)
\]

are unchanged.

All later uses of `R_{2,D}` should mean this exactly centered version.