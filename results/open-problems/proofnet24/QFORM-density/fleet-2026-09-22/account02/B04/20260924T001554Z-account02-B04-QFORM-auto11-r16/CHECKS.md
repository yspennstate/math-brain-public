# Deterministic checks — Walsh residual paving stress matrix

All calculations here are exact except the final displayed decimals.

Take the 64 physical Z-coordinates indexed by x in F_2^6. For k=1,...,5 set

U_{xk}=2^{-3}(-1)^{x_k},

so U^T U=I_5. Let

Lambda=diag(2,2,-2,-1,-1),  E=U Lambda U^T.

Because tr Lambda=0 and U_{xk}^2=1/64,

E_xx=(1/64) tr Lambda=0

for every physical x. The nonzero spectrum of E is exactly {2,2,-2,-1,-1}; hence rank(E)=5 and s_3(E)=2. Every row leverage is

ell_x=sum_{k=1}^5 U_{xk}^2=5/64.

Thus r beta=25/64 and the account03/B04 r44 residual-paving constant with H empty is

g=(1-sqrt(25/64))/2=3/16.

The generic r44 cross-E3 consequence therefore gives

||p||_infinity <= C_*/[(3/16)*2]=(8/3)C_*=22.5413899347418...

with C_*=8.4530212255281768747....

## Explicit physical partition

Let tau_x=(-1)^{x_6}, I={tau=+1}, J={tau=-1}. Each side has 32 rows. Since the sixth Walsh character is distinct from every product of two of the first five coordinate characters,

U_I^T U_I=U_J^T U_J=(1/2)I_5.

Writing L=sqrt(2)U_I and R=sqrt(2)U_J gives L^T L=R^T R=I_5 and

M:=E[I,J]=(1/2)L Lambda R^T.

Hence the five nonzero singular values of M are exactly

1,1,1,1/2,1/2.

Therefore, for a_j=s_j(M)^2=(1,1,1,1/4,1/4),

Z_3=e_3(a)=1+6/4+3/16=43/16,
Z_5=e_5(a)=1/16.

## Natural third-volume row marginals

For the natural squared-minor law the singular-direction weights are

p_m=a_m e_2(a without m)/Z_3.

For each of the three unit singular values,

e_2(1,1,1/4,1/4)=33/16,
so p_m=33/43.

For each of the two half singular values,

e_2(1,1,1,1/4)=15/4,
so p_m=(1/4)(15/4)/(43/16)=15/43.

The sum is 3. Every left singular vector is a column of L and has squared physical coordinate 1/32. Hence each constrained-side row marginal equals

alpha_i=(1/32) sum_m p_m=3/32<1/2.

Thus the pinned e5 Theorem D is admissible with its natural volume law.

For any supported probability weight w on physical 3x3 minors, if nu is the natural squared-minor law,

log G(w)=log Z_3-D_KL(w||nu)<=log Z_3.

Since nu itself is admissible and q=1 is the smallest allowed exponent in this family, the natural law is the global optimum over all supported weights and all D/D' exponents. The exact optimized pinned bound is

B_D=6 sqrt(e) (43/16)^(-1/6)
   =8.3895837251512747618....

The marginal-free account03/B04 cross-E3 theorem gives on the same literal block

B_E3=C_* (43/16)^(-1/6)
    =7.1689224211050229847....

The pinned D5 theorem gives

B_D5=5 sqrt(2e) (1/16)^(-1/10)
    =15.383113394117070339....

## Direct ridge optimization on exactly the same M

Put g=gamma^2. The five nonzero ridge eigenvalues are

1/(1+g), 1/(1+g), 1/(1+g), 1/(1+4g), 1/(1+4g).

Thus

theta(g)=3/(1+g)+2/(1+4g).

Every physical left-row leverage is theta(g)/32, hence is <1/2 for every g>0; q=1 is admissible whenever theta>2. The trace gate is

g < g_max=(1+sqrt(7))/4.

The completed simplified q=1 ridge certificate is

R(g)=sqrt(e)/(sqrt(2g)) * theta(g)/(theta(g)-2).

After differentiating log R(g)^2,

d/dg log R(g)^2
=-3(112g^3+48g^2-6g-5)/[g(14g+5)(8g^2-4g-3)].

On the admissible interval the boundary values diverge. The cubic has exactly one positive root by Descartes' rule of signs, so that root is the unique global minimizer:

g_*=0.2894328117919802489163144854...,

112g_*^3+48g_*^2-6g_*-5=0.

The optimized ridge bound is

R(g_*)=5.6245011981443490524....

Therefore on this one physical crossing:

5.6245011982  ridge
<7.1689224212  marginal-free E3
<8.3895837252  globally optimized pinned D/D'
<15.3831133942 pinned D5
<22.5413899348 generic r44 paving bound.

## Full target matrix

Add two original physical coordinates h,n with the star block [[0,1],[1,0]] and take direct sum with E. The full symmetric matrix A_* has nonzero spectrum

{2,2,1,-1,-1,-1,-2}.

Hence it has seven eigenvalues of modulus at least one. Relative to the zero anchor h, N={n}, the 64 Walsh coordinates form Z, every principal triangle through h is singular, and the residual Z-Z curvature is exactly E. Thus A_* is an actual target-valid member of the zero-anchor C1 structural branch, not merely an isolated cross-block example.
