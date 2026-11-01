# Same256 repair for every balanced shared controller

This is an analytic extension of PROOF.md Section4, with the SAME fixed
t2 tensor seed and two adjacent DATA points. The two edits use the SAME
arbitrary balanced Boolean controller a on any finite uniform cube.
No symmetry, monotonicity, or bound on the control dimension is assumed.
All quantities V, GV and I_DATA are exactly those defined in PROOF.md.

Write d_j=ahat({j}) and phi(u)=-u log2(u). PROOF.md Sections2--3 give

 GV(F)-2delta GV(a)=Dstar+sum_j[T(0)-(T(d_j)+T(-d_j))/2].       (A)

The DATA cancellation and Dstar bounds use only balance and do not use
majority. The function T is nonnegative on[-1,1]: each displayed summand
p log2(Z/p) is nonnegative because Z>=p, and5delta(1-s^2)>=0.
Terms with p=0 are defined by continuity. Also T(0)<=7: substitute a
single dictator into V(F)=2delta V(a)+T(0), use V(dictator)=0, and
0<=V(F)<=H(F)<=7 for the actual seven-bit Boolean output.

For |d_j|<=1/2 the curvature bound -13<T''<1 gives

 T(0)-(T(d_j)+T(-d_j))/2 <= (13/2)d_j^2.

By Parseval, sum_j d_j^2<=1, so the total from these small singleton
coefficients is at most13/2. At most THREE coefficients have |d_j|>1/2;
four would have squared mass greater than1. Each contributes at most
T(0)<=7 by nonnegativity of T at the two child means. Therefore (A) gives

 GV(F)-2delta GV(a) <=42+13/2+3*7=139/2<70.                 (B)

Balance also gives Pr(F!=b)=delta, independent of a. The same physical
influence comparison as in PROOF.md yields I_DATA(F)>=21/16. Since
70<256*(21/16), EVERY balanced shared Boolean controller satisfies

             GV(F)<=2delta GV(a)+256 I_DATA(F).           (C)

Equivalently retain the marked-sector owner W_y(h)=V(h)-J_y(h) for
h=y*a, descending to V(a) when the marked bit is queried. This is a
genuine arbitrary-control-dimension statement for the SAME-controller
adjacent-edit grammar. It does not prove a transfer for two DIFFERENT
dependent controllers, arbitrary seeds/tensor depths, or arbitrary
original-owner eligibility. PROOF.md's majority subfamily still refutes
the unmarked h owner at every fixed DATA rate.

The finite nonsymmetric check is corroboration only; (A)--(C), Parseval,
and the uniform curvature estimate provide the full arbitrary-a proof.
