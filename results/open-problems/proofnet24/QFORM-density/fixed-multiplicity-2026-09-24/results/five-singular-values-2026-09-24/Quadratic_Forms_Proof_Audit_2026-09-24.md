# Quadratic forms five-singular-value result — audit package

This directory records the independently re-audited fixed-multiplicity quadratic-form result developed on 24 September 2026.

## Main verified theorem

Let (X=(X_1,dots,X_n)) have independent real coordinates with densities bounded by (K). Let (A=A^T), (binmathbb R^n), (cinmathbb R). If

[
s_5(A)ge s>0,
]

then (Q=X^TAX+b^TX+c) has an essentially bounded density satisfying

[
|p_Q|_infty<2400,K^2/s.
]

A companion result proves a uniform full negative-half-moment bound under three large singular values. This does **not** prove the bounded-density theorem at multiplicity three or four.

## Audit status

A new full audit was performed after assembling the five-singular-value proof. The audit rechecked:

- every proof block in the original 17-singular-value manuscript;
- the grouped product-Fourier receiver and heavy-row promotion argument;
- the five-direction structural extraction;
- the scalar, definite-pair, and indefinite-pair pivot branches;
- the three-direction negative-half-moment appendix;
- normalization and density scaling;
- the obstruction showing that the current third-volume route does not automatically extend to four singular values.

No fatal mathematical gap was found in the five-singular-value theorem. The four- and three-singular-value **density** problems remain open in this route.

## Important scope

This is a mathematical proof audit, not Lean kernel verification or journal peer review. Finite exact/numerical checks supplement the written proofs but do not replace them.

## Companion sources

The original 17-singular-value manuscript remains pinned at commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

The complete five-singular-value manuscript source is stored beside this audit as `main.tex`.