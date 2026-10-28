# Canonical active resets with an unchanged complementary terminal

All logarithms are base two. This is a supplied-reference theorem for A097's negative-cell edit, not a universal FEI theorem. The initial quota below is 2C0+24 (32 structurally), rather than the earlier no-reset quota 2C0+10 (18 structurally). The additional initial allowance pays genuinely specified resets. No account is renewed at a descendant.

Let a>=2,b>=0,r>=1, n=a+b, s=2^-a,t=2^-n,p=2^-r, e=2pt. Write g=1-2A_a and F=g+2A_r D_n=1-2A_a+2A_(n+r). Supply a normalized finite-cost reference R for g, calibrated at the empty atom to mu^2, mu=1-2s. Calibration only decreases source CE. Set c=CE(P_g,R). The A097 complete floor has data marginal reference

    Rprime=(1-e/s)R+(e/s)mu delta_empty+2e U_n,

and actual conditional control kernel. Its complete cost is <=c+10e(a+b+r). All references below retain every normalizer and reference-only atom.

## 1. Active erasure decreases under the edit

For an active physical coordinate j put phi(u,v)=(u+v)log2(u+v)-u log2 u-v log2 v. The exact Fourier pair enumeration gives

    B_j(F)=phi((mu+e)^2,(2s-e)^2)
      +(2^a-2)(2s-e)^2+2^a(2^(b+r)-1)e^2,
    B_j(g)=phi(mu^2,4s^2)+(2^a-2)4s^2.

The difference of the nonvacuum terms is exactly -2e(1-4s+e)<=0. No off-support source coefficient is omitted from the edit's second term.

For x>=y>0, phi(x^2,y^2) decreases as (x,y) is replaced by (x+h,y-h), 0<=h<y. Indeed its derivative has the sign of

    x ln(1+(y/x)^2)-y ln(1+(x/y)^2).

For z=x/y>=1, L(z)=ln(1+z^2)-z ln(1+z^-2) has L(1)=0 and

    L'(z)=2(z+1)/(1+z^2)-ln(1+z^-2)
          >=2(z+1)/(1+z^2)-z^-2>0.

The last numerator is 2z^3+z^2-1>=2. Thus L>=0. Here mu>=2s>0, 0<e<=s, so the entire segment satisfies x>=y>0. Consequently B_j(F)<=B_j(g). This uses a>=2 essentially: for a=1, g is a dictator and has zero erasure, while the edited function can have positive erasure.

## 2. The complementary full terminal is kept, not reset

Query j. The off-cell child F_1 is constant +1; retain its FULL inherited reference Q_-j, without resetting it to a point mass. Its CE is k=-log2 q*, where q*=Q(empty)+Q({j}) on the joint data/control Fourier cube. The on-cell child is the same family with a'=a-1, n'=n-1, e'=2e.

For the source, give the on-cell child the spectral marginal V=R_-j, then calibrate its empty mass to (1-4s)^2. Call this source reference R_child and its complete cost c_child. Source chain rule and nonnegative conditional occupancy KL give

    B_j(g)+(c_child+c_const)/2<=c,
    c_const=-log2 V(empty).

All costs are finite; V(empty)>=mu^2>=1/4. The new on-cell complete reference is EXACTLY the A097 floor constructed from R_child with parameters (a-1,b,r), including its actual conditional control kernel. This is a prescribed reset, not the declaration of a new free reference.

To bound the additional complementary liability, write v=R({j}), q_j=4s^2-4se+2et, and

    kappa=(2s-e)^2/q_j,
    q*=(mu+e)^2+kappa[(1-e/s)v+2et],
    V(empty)=mu^2+v.

The first summand is exact because empty calibration makes Rprime(empty) equal the true data-vacuum mass. The conditional control kernel then restores the actual joint vacuum mass. Since e<=t<=s,

    q_j>=2s^2+2(s-e)^2>=2s^2,
    1-kappa=(2^r-1)e^2/q_j<=e/s,
    0<=v<=1-mu^2<=4s.

Therefore V(empty)-q*<=v[(1-kappa)+kappa e/s]<=8e. Both q* and V(empty) are positive, and q*>=(mu+e)^2>=1/4. Using ln z<=z-1 and ln2>2/3 gives the signed bound

    k-c_const=log2(V(empty)/q*)<=48e.

This remains valid when the signed difference is negative. It retains the complementary child's complete entropy plus KL, including reference-only support, rather than silently setting its cost to zero.

## 3. One original envelope pays every allowed active history

Define W=c+24e(a+b+r). At a fresh active query a>=2, source transport from section 2 and the erasure comparison from section 1 yield

    B_j(F)+[W_child+k]/2
      <=c+[48e]/2+24e(a+b+r-1)
      =W,

where W_child=c_child+24(2e)(a-1+b+r). This is the key local inequality on the augmented source envelope, NOT a local influence bound on either child. At a stopping leaf, the actual complete floor costs <=c+10e(a+b+r)<=W.

Induction on the finite physical tree proves: for any adaptive sequence of active queries, stopping before querying the final remaining active bit, resetting the on-cell child at each query to the specified floor and retaining each off-cell child's full inherited reference, the expected sum of erasures plus EVERY complete terminal CE is <=W_root. Orders and stopping may depend on prior outcomes; physical reaches are 2^-depth. Constant branches may simply stop. Arbitrary further no-reset continuations below any stopping leaf are also paid by the exact reference chain rule. An independent untouched Boolean tensor with prescribed cost c_h keeps that full additive cost throughout and funds nothing.

Now suppose the originally supplied uncalibrated cost is <=C0 I(g), C0>=0. Exact physical charges are C=eb,E=ea,J=er and I(F)=I(g)+C-E+J. For K=2C0+24, since E/I(g)=p2^-b<=1/2,

    K I(F)-[c+24(C+E+J)]
      >=(K-C0)I(g)-(K+24)E+(K-24)(C+J)>=0.

Thus the SAME initial quota K I(F) pays the entire prescribed-reset tree. Structural source R=P_g has C0=4 and gives rate32. At a later frontier, write d for all executed erasure debits, T for all full existing terminal costs, U=K I(F)-d-T, and Rquery for the actual conditional occupancy refund. The exact signed reset identity is remaining=U+Rquery-Z. The tree inequality establishes nonnegative remaining for these specific canonical reset policies; it does not drop d or create another root quota. Extra channel, integer-code or unrelated label bills are outside the theorem.

## 4. Exact remaining gap

The earlier no-reset rate18 does not automatically pay these resets; this proof uses rate32 because it bounds the complementary signed likelihood by 48e. Arbitrary non-point sources, arbitrary positive incoming profiles, data/control interleavings, and reset of the final active bit remain unproved. A general influence-priced initial reference remains FEI-hard. The theorem is a scoped analytic proof with exact finite validation, pending independent review; any Lean receipt concerns only its explicitly stated algebraic sublemma.
