# C08 local repair — short.tex line 222

Pinned source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8.

Literal source clause: "Factors with beta_i=0 are at most one and are dropped."

Status: FALSE_LOCAL.

Counterexample: take n=3, d=2, U with columns e1,e2 and orthogonal complement W=e3. Then the first two rows of W vanish, so beta_1=beta_2=0. Thus there can be more than one zero-beta factor.

Minimal repair: delete "are at most one". If beta_i=0 then w_i=0 and the factor f_i((Uy)_i+w_i dot z)=f_i((Uy)_i) is independent of z and at most one, so every such factor may be dropped. For the remaining indices beta_i>0, v_i=w_i/sqrt(beta_i) and sum beta_i v_i v_i^T=sum w_i w_i^T=I. The Brascamp-Lieb calculation and density bound are unchanged.

Downstream impact: no theorem hypothesis, conclusion, or constant changes. This repair was derived independently before peer comparison; account01/B03 later supplied matching evidence.
