# Canonical active resets with an unchanged complementary terminal

All logarithms are base two. This is a supplied-reference theorem for A097's negative-cell edit, not a universal FEI theorem. The initial quota is the SAME 2C0+10 (18 structurally) as the earlier no-reset result. A sharper complementary likelihood estimate pays the specified resets without enlarging that quota. No account is renewed at a descendant.

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

Write v_max=1-mu^2=4s(1-s) and q_max=(mu+e)^2+kappa[(1-e/s)v_max+2et]. For fixed s,t,e the ratio (mu^2+v)/q*(v) increases with v: writing q*(v)=A+Bv, one has A>=mu^2 and 0<=B<=1, so its derivative has numerator A-Bmu^2>=0. Consequently

    log2(V(empty)/q*)<=-log2(q_max).

The bound 1-kappa<=e/s gives, retaining the positive vacuum shift,

    1-q_max<=v_max*2e/s-2mu e<=6e.

For h=e/s in [0,1], the same kappa bound gives

    q_max>=(1-2s+sh)^2+(1-h)^2*4s(1-s)
          =1-sh(6-4h)+s^2 h(4-3h).

This polynomial decreases with s on [0,1/4]: its difference from its value at s=1/4 is

    (1/4-s)h[(6-4h)-(s+1/4)(4-3h)]>=0,

because the bracket is >=4-5h/2>=3/2. Thus

    q_max>=1-5h/4+13h^2/16
          =27/52+(13/16)(h-10/13)^2>=27/52>1/2.

Every denominator is positive. Using ln z<=z-1 and ln2>2/3 now proves the SIGNED bound

    k-c_const<=-log2(q_max)
       <=(1-q_max)/(q_max ln2)<18e.

At v_max the reference remains normalized (possibly zero on other source-support atoms); only this algebraic limit is used, so no infinite-cost reference is supplied to the theorem. In particular q_max<=1. This argument keeps the unchanged complementary child's full entropy plus KL and every reference-only atom. The earlier valid but coarser 48e/initial-rate32 draft is preserved in out/DERIVATION_FIRST_32_BOUND.md.

## 3. One original envelope pays every allowed active history

Define W=c+10e(a+b+r). At a fresh active query a>=2, source transport from section 2 and the erasure comparison from section 1 yield

    B_j(F)+[W_child+k]/2
      <=c+9e+10e(a+b+r-1)
      =W-e,

where W_child=c_child+10(2e)(a-1+b+r). This is the key local inequality on the augmented source envelope, NOT a local influence bound on either child. At a stopping leaf, the actual complete floor costs <=c+10e(a+b+r)=W.

The final active bit uses a different explicit boundary rule. At a=1 its on-cell child is h=-1+2A_(b+r). Supply the explicit point spectrum Q_h(empty)=(1-2u)^2 and Q_h(T)=4u^2 for every nonempty T, u=2^-(b+r). This normalized law equals P_h by direct character sums, so its reset signed cost is -D(P_h||Q_inherited)<=0. The complementary constant child again keeps its full inherited reference. The ordinary no-reset chain rule therefore gives B_j(F)+mean full new terminal CE<=CE(P_F,Q)<=W, without using the false a=1 erasure comparison. This constructs a known point-law reference; it assumes no oracle for arbitrary Boolean spectra.

Induction on the finite physical tree now proves: for any adaptive sequence of active queries, including exposure of ALL active bits or earlier stopping, reset the on-cell child to the specified floor while a>=2 and to the explicit point law on the final active query; retain each off-cell child's full inherited reference. The expected sum of erasures plus EVERY complete terminal CE is <=W_root. Orders and stopping may depend on prior outcomes; physical reaches are 2^-depth. Constant branches may simply stop. Arbitrary further no-reset continuations below any stopping leaf are also paid by the exact reference chain rule. An independent untouched Boolean tensor with prescribed cost c_h keeps that full additive cost throughout and funds nothing.

Now suppose the originally supplied uncalibrated cost is <=C0 I(g), C0>=0. Exact physical charges are C=eb,E=ea,J=er and I(F)=I(g)+C-E+J. For K=2C0+10, since E/I(g)=p2^-b<=1/2,

    K I(F)-[c+10(C+E+J)]
      >=(K-C0)I(g)-(K+10)E+(K-10)(C+J)>=0.

Thus the SAME initial quota K I(F) pays the entire prescribed-reset tree. Structural source R=P_g has C0=4 and gives rate18. At a later frontier, write d for all executed erasure debits, T for all full existing terminal costs, U=K I(F)-d-T, and Rquery for the actual conditional occupancy refund. The exact signed reset identity is remaining=U+Rquery-Z. The tree inequality establishes nonnegative remaining for these specific canonical reset policies; it does not drop d or create another root quota. Extra channel, integer-code or unrelated label bills are outside the theorem.

## 4. Exact remaining gap

The earlier no-reset rate18 now pays these particular canonical active resets as well. The construction does not prove that every canonical reset has nonpositive cost; all sampled resets were negative, which remains a separate stronger question. Arbitrary non-point sources, arbitrary positive incoming profiles, and data/control interleavings remain unproved. A general influence-priced initial reference remains FEI-hard. The theorem is a scoped analytic proof with exact finite validation, pending independent review; any Lean receipt concerns only its explicitly stated algebraic sublemma.
