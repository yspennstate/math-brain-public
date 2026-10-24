Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Date: 2026-09-20 UTC.

Status: retained Talagrand F0111 k=2 screen only; **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. Native Burdzy--Scheutzow Problem 7.2 / I0076 remains **OPEN / PARTIAL / RETIRED-HANDOFF** with no surviving frozen candidate and is not reopened.

Immediate predecessor: `runs/R15/20260920_0953Z_successor_screen_f0111_kenergy_excess_t105b.md`. This note continues the already-committed boundary-minimum idea `artifacts/R15/f0111_boundary_minimum_idea_u106c.md` rather than restarting.

Methods for this run remain **#7 TAKE THE LIMIT, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY**. The preceding completed report used #3/#25/#27. All thirty method numbers already occur in older R15 history, so this is nonconsecutive reuse on the reduced scalar object.

# Pivot before code: replace the fragile c=7/100 boundary evaluation by a robust entropy inequality

The preceding report proves that any remaining n=30, full-support, two-level Hessian-null exact quadratic contact in the N=|K|=12 or 13 cell must satisfy the sharpened necessary gate

\[
\widehat\Gamma_N(d,s)=\log S-\left(1+\frac\eta2\right)K_{\rm sec}-H_J^*(d,s)\le0.
\]

On the lower scalar closure `U_K=N` one has `eta=0`, hence every K-coordinate collapses to zero and all K slack disappears. Moreover

\[
S y=N,\qquad Sx=S+29-N,
\]

so, with `p=C_N s`, `C_12=15`, `C_13=17`, the adaptive two-heavy J profile is exactly

\[
u_1=S(1-p),\qquad u_2=1+pS.
\]

The previous adaptive-ray monotonicity proof works for every `0<c<=7/100` because its only c-dependent requirement was `e^c U_max < (121/100)s`, already certified at the larger endpoint c=7/100. For the boundary proof choose the smaller

\[
c=\frac3{100},\qquad \varepsilon=\frac c{\log S},\qquad t=1+\varepsilon.
\]

Set

\[
A=1-p,\qquad D=S^{-1},\qquad B=p+D.
\]

Then `A+B-D=1`, `u_1=SA`, `u_2=SB`, and on `U_K=N`

\[
\widehat\Gamma_N^\partial
=-\frac1t\log F-\varepsilon U_{\max}\log(SA)\log(SB),
\]

where

\[
F=A^t+B^t-D^t.
\]

Because `D^t=D e^{-c}` exactly and, for `0<x<=1`,

\[
x^{1+\varepsilon}=x e^{\varepsilon\log x}
\le x\left(1+\varepsilon\log x+\frac{\varepsilon^2\log^2x}{2}\right),
\]

we obtain

\[
1-F\ge \varepsilon\mathcal E-\frac{\varepsilon^2}{2}\mathcal V
+D\bigl(c-1+e^{-c}\bigr),
\]

with

\[
\mathcal E=-A\log A-B\log B+D\log D,
\qquad
\mathcal V=A\log^2A+B\log^2B.
\]

The last D-term is nonnegative. Therefore the purely logarithmic inequality

\[
\boxed{
\mathcal J_N:=
\mathcal E-tU_{\max}\log(SA)\log(SB)-\frac\varepsilon2\mathcal V>0
}
\]

implies `F<1` and, using `-log F >= 1-F`, forces

\[
\widehat\Gamma_N^\partial>0.
\]

This is the key simplification: the exact boundary sign can now be certified with rational interval arithmetic and rigorous logarithm enclosures only; no transcendental power evaluation is needed.

For `0<s<=10^{-4}`, use the carried exact bounds

\[
\frac{29}{20}<\frac{-k}{s}<\frac{13}{8},\qquad U_{\max}<\frac98s.
\]

They imply

\[
S>\frac{232}{13s},\quad \log S>12,\quad
\log(1+pS)<6,\quad
B<\left(C_N+\frac{13}{232}\right)s.
\]

Writing `L=log S`, one has the exact stable identity

\[
\mathcal E=-(1-p)\log(1-p)+pL-B\log(1+pS).
\]

Also `|log B|<L`, so the variance penalty is bounded by a multiple of `B L`. These inequalities should leave a rational positive margin already at N=12, the tighter case.

For `10^{-4}<=s` up to the known rational scalar roofs (`3601/250000` for N=12 and `12637/10^6` for N=13), certify `J_N>0` only on the exact curve `U_K=N`. Since `U_K` is strictly increasing in d and s, each s-slab gives a rigorous d-bracket for that curve by rational bisection at the two slab endpoints. Recursive exact interval arithmetic with atanh-series logarithm bounds can then cover the one-dimensional curve. Numerical scratch is route-finding only and is not evidence.

If this succeeds, the new theorem will be: the entire lower scalar boundary `U_K=N` is incompatible with the sharpened arbitrary-heterogeneity contact inequality for both remaining branches N=12 and N=13. This does **not** yet eliminate their interiors; the remaining task will be to prove a one-sided d-monotonicity or boundary-to-interior comparison.

No checker has been committed at the time of this note.