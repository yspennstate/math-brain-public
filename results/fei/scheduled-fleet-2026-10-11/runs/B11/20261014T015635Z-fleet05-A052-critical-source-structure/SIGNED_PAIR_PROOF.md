# Signed pair collision with an orientation reserve

Entropy is in bits. Let f be any Boolean sign on a finite uniform cube, let i,j be distinct physical coordinates, and fix a retained Fourier index t avoiding them. Write its four Fourier amplitudes as (alpha,beta,gamma,delta) at (t,t+i,t+j,t+i+j), and q=alpha^2+beta^2+gamma^2+delta^2. Zero q rows are omitted. Define the following homogeneous quantities, each already weighted by the retained row mass:

    c_i=4 alpha^2 beta^2/(alpha^2+beta^2)
          +4 gamma^2 delta^2/(gamma^2+delta^2),
    c_j=4 alpha^2 gamma^2/(alpha^2+gamma^2)
          +4 beta^2 delta^2/(beta^2+delta^2),
    P=4(alpha delta+beta gamma)^2/q,
    Q=4[(alpha beta+gamma delta)^2
         +(alpha gamma+beta delta)^2
         +(alpha delta+beta gamma)^2]/q,
    e=min(alpha^2,beta^2)+min(gamma^2,delta^2)
        +min(alpha^2,gamma^2)+min(beta^2,delta^2),
    o=(beta^2-alpha^2)_+ +(delta^2-gamma^2)_+
        +(gamma^2-alpha^2)_+ +(delta^2-beta^2)_+,
    v=beta^2+gamma^2+2 delta^2=e+o.

Zero numerator/denominator terms are zero, as their continuous extensions. Summing t gives c_i->C_i, c_j->C_j, Q->C_{ij}, e->beta_i+beta_j, o->O_i+O_j and v->Inf_i+Inf_j. In particular C_i uses singleton conditioning on the OTHER queried coordinate as well as t, unlike C_{ij}.

## 1. Exact signed identity and nonnegative merging refunds

Set

    M_i=c_i-4(alpha beta+gamma delta)^2/q,
    M_j=c_j-4(alpha gamma+beta delta)^2/q.

Cauchy--Schwarz with weights alpha^2+beta^2 and gamma^2+delta^2 gives M_i>=0; the analogous two weights give M_j>=0. More explicitly, when both weights are positive,

    M_i=4[alpha beta(gamma^2+delta^2)
           -gamma delta(alpha^2+beta^2)]^2
           /[q(alpha^2+beta^2)(gamma^2+delta^2)].

The zero-weight limit gives zero. Thus, exactly,

    C_{ij}=C_i+C_j+P_{ij}-M_i^total-M_j^total.       (1)

Here P_{ij}=sum_t P. The term alpha delta+beta gamma is retained as a SIGNED sum before squaring. The refunds are not hypothetical child reserves; they are exact differences between singleton row conditioning and merged pair conditioning.

## 2. One influence account and the orientation correction

Cauchy--Schwarz applied two ways gives

    (alpha delta+beta gamma)^2<=q(delta^2+beta^2),
    (alpha delta+beta gamma)^2<=q(delta^2+gamma^2).

Average the right sides: P<=2v. Also, for any x,y>=0,
4xy/(x+y)>=2min(x,y); hence c_i+c_j>=2e. Together with v=e+o, this proves rowwise

    P<=c_i+c_j+2o,
    Q<=2(c_i+c_j)+2o.

Summing yields the all-dimensional unconditional orientation-corrected comparison

    C_{ij}<=2(C_i+C_j)+2(O_i+O_j).                 (2)

This spends the pair queried influence v once, using its exact split into minority and orientation mass. It does NOT assert that C_{ij} is bounded by singleton collisions alone. The three-bit parity guard has C_i=C_j=0 but O_i=O_j=1/2, C_{ij}=1. Its missing pair cost is P_{ij}=1, with both merging refunds zero. Thus the signed degree-two term is explicit and the correction is essential.

The coefficient 2 of orientation cannot be reduced in this general REAL-row inequality while keeping the singleton coefficient fixed: take (alpha,beta,gamma,delta)=(1,0,0,epsilon). Then C_i=C_j=0, o=2epsilon^2, Q=4epsilon^2/(1+epsilon^2), and Q/o tends to2. These arbitrary rows are not asserted to be globally Boolean-realizable. No sharp Boolean constant is claimed.

## 3. Guarded critical-source bound retaining every child

Let f be a least-essential-dimension FEI(K) violation, K>0, D=H(f)-K I(f)>0. Put S_i=-E D_K(f restricted at i), likewise S_j. Minimality gives S_i,S_j>=0. The independently reconstructed A055 singleton bound is

    D+K O_i+S_i<=r_K,
    r_K=log2(1+2^(2/ln2-K)).

Adding the two inequalities and substituting in (2) gives

    C_{ij}<=2(C_i+C_j)
           +(2/K)(2r_K-2D-S_i-S_j).              (3)

The parenthesized expression is nonnegative because it bounds K(O_i+O_j). Its weaker universal residue is 4r_K/K. Both child reserves and the two copies of the same root deficit remain displayed; they are not free independent funding. This closes the specific signed parity-term comparison requested by A051/A055, with an explicit exponentially small additive correction. It does not select a pair.

For K>=4, write T_{ij} for the right side of (3). Insert it in A051's reviewed two-bit critical bank, using monotonicity of log and psi_2:

    D+S_{ij}+(K/2-2)W_g
      <=log2(1+T_{ij})+psi_2(min(1,T_{ij}))+32T_{ij}. (4)

Alternatively retain the actual W0,Wb,Gamma instead of relaxing them. This is only a necessary inequality on every pair. The fixed-threshold child bank controls the additive orientation term; no established argument makes the singleton collisions small enough relative to D or S_{ij} to contradict (4).

## 4. What is and is not resolved

The false unconditional singleton comparison is replaced by (1)--(3), which hold with actual orientation and child reserves. Nonstrict physical ratio criticality alone does not supply the A055 fixed-threshold exponential bound, and an arbitrary hard-core wrapper cannot be given nonnegative S_i. Historical component-pruning failures concern virtual component objects and do not invalidate this proof: its unconditional part is an exact Fourier-row inequality for the original Boolean source, and its guarded part uses only actual smaller-dimensional physical children.

First unsupported line: there is a dimension-independent K and a proper pair or larger block whose singleton collision and remaining phase costs lie below the retained positive root/child reserve. Inequality (3) leaves a positive additive remainder, and D can be arbitrarily small as dimension grows. Neither dyadic granularity nor an exponentially small upper bound contradicts D>0. A proof of selection or a new multirow cancellation estimate remains required for full FEI.
