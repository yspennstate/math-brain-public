# Uniform singleton guard, independent of core dimension or bias

For the fixed controller A=WUV OR S(U OR V), all four events singleton,
write a=1-Eg in [0,2], d=Inf_S(F)=5a/16. The paired S-row at the
empty remaining mask has squared masses r=(1-7a/16)^2 and s=d^2.
Its total q0=r+s<=1. The total mass of every other paired row is

    q*=1-q0=7a/8-37a^2/128.

Each such row contributes at most its mass to erasure. The constant
row contributes at most d^2 log2(Euler*q0/d^2), using
-(1-t)ln(1-t)<=t. Thus, for a>0,

    B_S/d <= q*/d+d log2(Euler/d^2)
           =14/5+(1/ln2-74/25)d-2d log2 d
           <14/5+2/(Euler*ln2)<14/5+9/8=157/40<4.

Here 1/ln2<3/2<74/25, max_{x>0}(-x ln x)=1/Euler,
Euler>8/3 (its first four Taylor terms, with a positive remainder),
and ln2>2/3 (first atanh term, with a positive remainder). Every
inequality is uniform; no sum/limit interchange occurs. When a=0,
g=+1 and B_S=d=0. The paired constant is positive throughout
0<=a<=2 because 1-7a/16>=1/8; no hidden zero denominator occurs.

This proves actual strict-K4 separator goodness for EVERY independent
Boolean core on every finite cube, with no balance or flatness assumption.
It survives arbitrary adaptive core-only physical restrictions before S,
because each conditional core is still an independent Boolean sign.
There is NO bad-S liability under any such history. This says nothing
about the full-reference CE debit of a core or S query.

# An all-dimensional incoming-product-reference obstruction

Let g_n=1-2*1_{all n data bits are 1}, a_n=2^(1-n), n>=2, and use the
same controller. For Q_n equal to the product of the actual spectral
marginals, CE(P_n,Q_n)=M_n exactly. Physical edge counts give

    I_n=a_n(7n/16+3/4),
    M_n=n h2(7a_n/16)+h2(5a_n/16)+h2(a_n/16)
                         +2h2(3a_n/16).

Since h2(p)>=p log2(1/p) and all fixed coefficients lie in (0,1),

    M_n/I_n >= log2(1/a_n)=n-1.

Using h2(ca)=ca[log2(1/a)+log2(1/c)+log2(Euler)]+O(a^2),
with fixed c and the elementary Taylor remainder bounded for ca<=1/2,

    M_n/I_n=n-1+log2(16/7)+log2(Euler)+O(1/n).

The O(na^2) numerator remainder becomes O(a) after division by
I_n>=7na/16, and is absorbed by O(1/n). Thus no finite source rate
K makes K I_n-CE(P_n,Q_n)>=0 for this incoming product reference.
No nonnegative retirement U-H can improve beyond the zero-held source
K I_n-M_n; eliminating ALL S liability is still insufficient.

For a check that this is not an FEI disproof, put L_A=sum_T phi(Ahat(T)^2).
The exact Fourier entropy is

 H(F_n)=phi((1-7a_n/16)^2)+2a_n L_A
        +4(7/16)a_n log2(1/a_n)-phi((7a_n/16)^2).

Indeed each nonempty data mask has amplitudes -a_n Ahat(T); the single
large constant amplitude replaces the empty/empty entry. Finite grouped
summation gives this display, and H(F_n)/I_n tends to4. Only the full
product cross-entropy rate diverges. No claim H<=4I is made.
