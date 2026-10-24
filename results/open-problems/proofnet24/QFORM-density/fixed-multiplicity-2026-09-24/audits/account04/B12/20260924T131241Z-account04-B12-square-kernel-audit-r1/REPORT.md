# B12 audit: scalar square pivots and logarithmic kernel closure

## Verdict

**PASS**, for the B12 lens, on the pinned fixed-multiplicity manuscript. The scalar-pivot domination, square-root singularity, logarithmic convolution, and final half-potential iteration are valid for arbitrary cap-one product laws and arbitrary affine terms. No moment, support, or post-rotation independence assumption is used.

The audit also yields the strict improvement
[
oxed{|p_{X^TAX+ell^TX+c}|_{infty,mathrm{ess}}
le (2010+1200log 16)rac{K^2}{s}
<5338,rac{K^2}{s}}
]
whenever (s_{17}(A)ge s>0), replacing the manuscript's rounded constant (10000). This does **not** prove the original three-eigenvalue conjecture.

## Source pin

- repository: `yspennstate/math-open-problems`
- manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Scalar-square trace check

Condition on all variables except (Y=X_i). Completing the square gives (Q=a(Y-m)^2+R), where (m,R) are measurable in the conditioned variables. The conditional density cap remains (K), hence
[
p_{Qmidmathcal G}(z)le rac{K}{sqrt{|a|,|z-R|}}
]
on the appropriate half-line, and for every interval (I) of length (ho),
[
Pr(Qin Imidmathcal G)le2Ksqrt{rac{2ho}{|a|}}.
]
Tonelli yields the unconditional measure domination
[
p_Q(z)le K|a|^{-1/2}mathbb E|z-R|^{-1/2}.
]
This is obtained after conditioning and does not evaluate an arbitrary density representative or assume independence after completing the square.

## Kernel audit

For
[
J(d)=int_{-1}^{1}|x|^{-1/2}|x-d|^{-1/2},dx,
]
split at (|x|=2|d|). Scaling on the near region gives a bounded integral (<8). On the far region, (|x-d|ge|x|/2), whence
[
J(d)le8+3log_+rac1{|d|}.
]
The logarithm is integrable against the next square kernel:
[
sup_aint_{-1}^{1}|x|^{-1/2}log_+rac1{|x-a|},dxle8.
]
Layer cake reduces this to interval intersections; the centered interval maximizes overlap with the symmetric decreasing weight. At (a=0),
[
2int_0^1x^{-1/2}log(1/x),dx=8.
]
Thus the logarithm created by composing two square-root singularities is exactly paid for by the third half-potential step.

## Exact constant ledger

With (eta=1/100), the residual one-eigenvalue form has truncated half-potential
[
L_0=4+4log16.
]
The scalar-pivot branch therefore costs
[
eta^{-1/2}(8+3L_0)
=10(20+12log16)
=200+120log16.
]
Adding the tail (|z|>1) gives
[
C_9=201+120log16.
]
The outer scalar pivot contributes another factor (10), hence
[
C_{17}=2010+1200log16=5337.106ldots<5338.
]
The competing branches are smaller: (800e<2175), (10pi<32), and the indefinite two-coordinate branch is (<251).

## Scope and remaining gap

The seventeen-eigenvalue essential-density theorem survives this audit with a stronger explicit constant. Continuity remains separate. The target (s_3(A)ge1) remains open: the square/log mechanism controls repeated scalar pivots only while enough residual spectral multiplicity remains; it does not furnish the missing three-eigenvalue structural extraction.

## Reproducibility note

The README advertises `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but these files were absent at the audited paths. This is a packaging defect, not a mathematical failure.
