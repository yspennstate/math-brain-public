Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Date: 2026-09-20 UTC.

Status: retained Talagrand F0111 k=2 screen only; **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. Native Burdzy--Scheutzow Problem 7.2 / I0076 remains **OPEN / PARTIAL / RETIRED-HANDOFF** with no surviving frozen candidate and is not reopened.

Immediate predecessor: `runs/R15/20260920_0953Z_successor_screen_f0111_kenergy_excess_t105b.md`.

Methods for this run: **#7 TAKE THE LIMIT, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY**. The immediately preceding triple was #3/#25/#27. All thirty method numbers have occurred somewhere in older R15 history; this is a nonconsecutive reuse on the newly reduced two-scalar object.

# Idea before code: force the sharpened gate to its scalar boundary

The predecessor proves that any remaining n=30, full-support, two-level Hessian-null exact quadratic contact in the N=|K|=12 or 13 cell must satisfy

\[
\widehat\Gamma_N(d,s)
:=\log S-\left(1+\frac{\eta}{2}\right)K_{\rm sec}-H_J^*\le0,
\]

where `s=z-1>0`, `d=delta`, `eta=U_K-N`,

\[
K_{\rm sec}=\frac{\eta}{S}\frac{c_K\log c_K}{c_K-1},\qquad c_K=\frac{U_K}{L_K},
\]

and `H_J^*` is the exact adaptive-ray two-heavy J extremizer from r103z. Numerical scratch is not evidence, but it suggests the minimum of `widehat Gamma_N` at fixed s occurs on the lower scalar boundary `U_K=N`.

The route is to prove that rather than interval-check the full two-dimensional cell.

## #12 conserved quantity at the boundary

On `U_K=N`, the exact K-excess identity from o100w gives

\[
\sum_{j\in K}(e^{q_j}-1)=U_K-N=0.
\]

Because every `q_j>0` in the full-support screen, the closure boundary has

\[
e^{q_j}=1,\quad q_j=0\quad(j\in K).
\]

Consequently

\[
\eta=K_{\rm sec}=E_{1,K}=E_{KK}=0.
\]

Also `Sy=U_K=N` and `\sum_i e^{q_i}=S+29`, hence

\[
Sx=S+29-N=S+M-1,
\]

where `M=30-N`. Therefore the carried two-heavy J closure has the exact simplification

\[
u_1^*=S(1-C_Ns),\qquad
u_2^*=1+C_NSs,
\]

with `C_12=15`, `C_13=17`, and `u_1^*+u_2^*=S+1`.

Thus on `U_K=N`,

\[
\widehat\Gamma_N=\log S-H_J^*
\]

and the first logarithmic part of `H_J^*` becomes a two-number expression with no K variables at all.

## #7 / #29: boundary-first proof plan

Let

\[
L=\log S,\qquad \varepsilon=\frac{7}{100L},\qquad t=1+\varepsilon,
\]

and set

\[
A=1-C_Ns,\qquad B=C_Ns+S^{-1}.
\]

Then on `U_K=N`,

\[
H_J^*
=\log S+\frac1t\log\!\left(A^t+B^t-S^{-t}\right)
+\varepsilon U_{\max}\log(SA)\log(SB).
\]

So the exact boundary gap is

\[
G_N^{\partial}(s)
=-\frac1t\log\!\left(A^t+B^t-S^{-t}\right)
-\varepsilon U_{\max}\log(SA)\log(SB).
\]

The target is two steps:

1. prove `partial_d widehat Gamma_N > 0` on each scalar-feasible cell. Then the minimum at each fixed s is exactly the boundary `U_K=N`, because both scalar functions increase in d and scalar feasibility begins at the unique `d_U(s)` with `U_K=N`;
2. prove `G_N^partial(s)>0` for the entire feasible s interval up to the known scalar collision `s_N`. This would eliminate N=12 and N=13 completely for this full-support two-level first-bifurcation mechanism.

There is a second possible proof if direct d-monotonicity is algebraically ugly: compare every interior point to the boundary point on the same s-slice. The K term is order eta, while the change in the J extremizer is also differentiable in d. A one-sided derivative comparison may suffice without proving global monotonicity term-by-term.

The most important structural observation is that the difficult endpoint is not `s->0`; the existing boundary coefficient already gives a uniform positive first-order margin there. The numerically tight region lies near the other scalar endpoint where the interval `d_U(s)<d<d_L(s)` collapses. On that endpoint both `U_K=N` and `L_K=N`, so `c_K=1` in the limit and all K slack disappears. Hence both ends of the scalar strip are rigid. The remaining job should be an exact one-variable sign proof, not another matrix estimate.

No checker or finite certificate has been written for this route yet. Any subsequent finite sign claim must be separately certified before being called proved.