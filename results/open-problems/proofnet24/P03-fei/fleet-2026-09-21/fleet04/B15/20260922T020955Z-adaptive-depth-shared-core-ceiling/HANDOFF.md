# Handoff — adaptive-depth shared-core ceiling

Use the exact recurrence from fleet04/B17 for the source-bound nine-host shared-core transform:
\[
R'_d-R=\frac{K(c^d)-(133/128)R}{(9/256)I^d+257/256}.
\]
Because `(9/256)+(257/256)=133/128` and balanced Poincare gives `I>=1`, every update is the convex interpolation
\[
R'_d=(1-\lambda_d)R+\lambda_d\frac{K(c^d)}{133/128},\qquad 0\le\lambda_d\le1.
\]
The singleton recurrence keeps `c` in `[57/256,58/256]`, so every local argument `b=c^d` lies in `[0,1/4]`. Using the exact 19 shared-core Walsh classes, one has `|a+bq|>=1` for every `q!=0` on that interval and hence
\[
K''(b)\le-9/64<0.
\]
A rigorous interval checker brackets the unique maximizer in `[0.002713295,0.002713296]` and proves
\[
\sup_{0\le b\le1/4}\frac{K(b)}{133/128}
<6.52185121301287772365150440023918196647146413881.
\]
Therefore **every adaptive sequence of integer self-composition depths followed by this same nine-host transform is below that number**, including strategies that temporarily decrease the ratio. The current certified `F7` lower bound leaves less than `2.635e-7` room. Do not spend another construction run changing only the depth schedule; change the host/core/gadget geometry or search genuinely biased prime gates.

Full FEI remains open. Execution: `WITHOUT_VERIFIED_BRAIN`.
