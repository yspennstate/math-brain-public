SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T22:35:40Z.
attacking: second-order rigidity of the asymptotically sharp three-bank cube witness, with an exact dense rotated saturating sequence and a concrete application of fleet02/B17's rough one-sheet barrier.

# QFORM-SECOND-ORDER-SHARP-BANK-RIGIDITY-v1

Status: **PROVED SUPPORTING SHARP-WITNESS THEOREM**. The full unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and correction discipline

The exact second-order three-bank Edgeworth/coarea formula used below is the completed fleet03/B17 report

`yspennstate/math-open-problems@a7639f687efd2a693ba6ad74e87a94a3aed5cfe2`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T221053Z-fleet03-B17-QFORM-auto11/REPORT.md`.

It proves, for independent physical `Unif[-1/2,1/2]` coordinates grouped into three normalized banks of sizes `m_j`, an exact target matrix `A=R B R^T` with `B=O^T diag(1,1,-1) O`, and `u_j=O_{3j}^2`, the uniform expansion

`p_Q(0)/(3 sqrt(2))
 =1-sum_j h4(u_j)/(20m_j)
 +sum_j [h6(u_j)/105+h8(u_j)/800]/m_j^2
 +sum_{i<j} k44(u_i,u_j)/(400m_i m_j)
 +O((sum_j m_j^-1)^3)`.

The exact polynomials `h4,h6,h8,k44` are those proved there. No post-rotation independence is used.

The designated partner result actually applied is fleet02/B17

`yspennstate/math-open-problems@b2deb6e86032549777cc1197407cadf01f8cc6e6`,

main report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260923T214642Z-4c9d/REPORT.md`,

which proves the arbitrary-rough-law majority-sheet bound for the exact six-variable Householder pair-sum matrix.

Binding corrections preserved: no arbitrary-joint coarea cap, no positive conditional-density moment shortcut, no independence after spectral rotation, no law-uniform pointwise quadratic-phase decay, no bounded-fragment localization, and no claim that a cone-tip computation is automatically a global density maximum.

## 2. Exact family and notation

Let `N=m_1+m_2+m_3`.  Put

`J=diag(1,1,-1)`, `B=O^T J O`,

and let `R` repeat `e_j/sqrt(m_j)` in bank `j`.  Then `R^T R=I_3`, so

`A=RBR^T`

has exact nonzero spectrum `{1,1,-1}` in the original independent coordinates.  Write

`u_j=O_{3j}^2`, `u_j>=0`, `u_1+u_2+u_3=1`.

The sharp first-order calculation in the source report says that, after labelling bank 3 as the negative-axis bank, the optimal limiting proportions are

`x_*:=m_3/N -> sqrt(6)/(sqrt(6)+sqrt(57)) = (sqrt(38)-2)/17`,

`y_*:=m_1/N=m_2/N -> (1-x_*)/2`,

and the first-order total-dimension coefficient is

`K_* = 63/160 + 3 sqrt(38)/80 = 0.6249155251113366...`.

The source report established

`p_Q(0)/(3sqrt(2)) = 1-K_*/N+O(N^-2)`

for an exact genuinely rotated dense sequence.  The present run identifies the **sharp second-order coefficient and the complete local rigidity penalty** around that optimizer.

## 3. Second-order coefficient at the aligned optimum

At the aligned negative axis `u=(0,0,1)`, direct substitution into the source polynomials gives

`h4(0)=57/32`, `h4(1)=3/4`,

`a_0:=h6(0)/105+h8(0)/800 = -4833/327680`,

`a_1:=h6(1)/105+h8(1)/800 = -173/17920`,

`b_00:=k44(0,0)/400 = 7803/819200`,

`b_01:=k44(0,1)/400 = 603/51200`.

For symmetric positive banks `m_1=m_2=yN`, `m_3=xN`, `y=(1-x)/2`, the second-order coefficient is therefore

`H(x)=(2a_0+b_00)/y^2+a_1/x^2+2b_01/(xy)`

and simplifies exactly to

`H(x)=-(97955x^2-47608x+6920)/(716800 x^2(1-x)^2)`.

At `x=x_*`,

`H_*:=H(x_*)
 =(-1299963+108550 sqrt(38))/13619200`

` = -185709/1945600 + 2171 sqrt(38)/272384`

` = -0.04631812881650300...`.

Hence the continuously optimized aligned family has

`p_Q(0)/(3sqrt(2))
 =1-K_*/N+H_*/N^2+O(N^-3)`.

The sign is noteworthy: even after the optimal first-order bank allocation, the next correction is again negative.

## 4. Full second-order rigidity under allocation and orientation perturbations

Let the bank proportions satisfy

`p_{j,N}:=m_j/N = p_j^* + d_j/sqrt(N)+o(N^-1/2)`,

where `(p_1^*,p_2^*,p_3^*)=(y_*,y_*,x_*)` and `d_1+d_2+d_3=0`.

Let the squared negative-axis leakage obey

`N(u_1+u_2) -> ell`, `ell>=0`,

so `u_3=1-u_1-u_2`.  The source expansion is uniform in the orientation, and all three limiting proportions stay positive, so its remainder is `O(N^-3)` here.

### 4.1 Allocation penalty

At aligned orientation the first-order coefficient is

`F(p_1,p_2,p_3)=[57/p_1+57/p_2+24/p_3]/640`.

The constrained gradient vanishes at `p^*`.  Taylor expansion gives

`F(p_N)=K_*+Q_alloc(d)/N+o(N^-1)`,

where

`Q_alloc(d)
 = 57(d_1^2+d_2^2)/(640 y_*^3)
   +24 d_3^2/(640 x_*^3)`.

Both coefficients are strictly positive.  Explicitly,

`57/(640y_*^3)=15/16+177 sqrt(38)/1520
 =1.655329788503624...`,

`24/(640x_*^3)=177/160+15 sqrt(38)/64
 =2.551034531945854...`.

Thus any `N^-1/2` bank-proportion displacement pays a nonnegative amount at order `N^-2`, vanishing only for `d=0`.

### 4.2 Orientation penalty

The exact derivative of

`h4(u)=(57+6u-39u^2)/32`

is `h4'(0)=3/16`, `h4'(1)=-9/4`.  Therefore, writing `s=u_1+u_2`,

`sum_j h4(u_j)/(20m_j)
 =F(p_N)/N + c_theta s/N+o(s/N)`,

uniformly for `p_N->p^*`, with

`c_theta=(1/20)[3/(16y_*)+9/(4x_*)]`

` =21/160+87 sqrt(38)/1520`

` =0.4840815909594085... >0`.

If `Ns->ell`, this costs `c_theta ell/N^2` in the density expansion.  Variation of the genuine second-order term caused by `s=O(N^-1)` is only `O(N^-3)`.

### 4.3 Rigidity formula

Combining the preceding expansions gives the sharp local law

`boxed:
 p_Q(0)/(3sqrt(2))
 =1-K_*/N
  +[H_*-Q_alloc(d)-c_theta ell]/N^2
  +o(N^-2).`

Consequences:

1. `H_*` is the **largest possible second-order coefficient** among all sequences approaching the first-order optimal chamber at the natural scales above.
2. Equality at order `N^-2` forces `d_1=d_2=d_3=0` and `ell=0`.
3. A rotation with squared negative-axis leakage of order `1/N` is already detectably suboptimal at second order.
4. Integer rounding of the optimal bank sizes is much smaller: it gives `p_N-p^*=O(1/N)`, hence only an `O(N^-3)` effect.

This is a witness-rigidity statement, not an arbitrary-input upper bound.

## 5. Exact genuinely rotated dense sequence attaining the second-order optimum

For every integer `N>=2`, define the rational unit vector

`w_N=(2N^2,4N^2,N^4-5)/(N^4+5)`

and the Householder involution

`B_N=I-2w_N w_N^T`.

Exactly,

`||w_N||=1`, `B_N^2=I`, `spec(B_N)={1,1,-1}`,

and every entry of `B_N` is nonzero for `N>=2`.  Its squared orientation leakage is

`w_{N,1}^2+w_{N,2}^2
 =20N^4/(N^4+5)^2 = O(N^-4)`.

Choose positive integers `m_1,m_2,m_3` summing to `N` and within `O(1)` of `(y_*N,y_*N,x_*N)`.  Let `R_N` repeat `e_j/sqrt(m_j)` and put

`A_N=R_N B_N R_N^T`.

Then every finite `A_N` is entrywise nonzero and has exact nonzero spectrum `{1,1,-1}`.  With independent physical `Unif[-1/2,1/2]` inputs, the bank-rounding error is `O(N^-3)` in the normalized cone-tip expansion, while the orientation leakage contributes only `O(N^-5)` to the first-order term.  Therefore

`boxed:
 p_{X^T A_N X}(0)
 =3sqrt(2)[1-K_*/N+H_*/N^2+O(N^-3)].`

So the exact dense rotated sequence is not merely first-order optimal: it attains the sharp second-order coefficient `H_*` as well.

In particular, the source-valid universal lower obstruction remains

`C_univ >= lim_N p_{X^T A_N X}(0)=3sqrt(2)`.

This run does not raise the limiting lower bound above `3sqrt(2)`; it makes the finite-size approach to that obstruction rigid through the next order.

## 6. Actual fleet02/B17 partner application

Use the completed fleet02/B17 rough one-sheet theorem for the exact six-variable matrix

`A_H=(1/6)[[1,1,-2,-2,-2,-2],
            [1,1,-2,-2,-2,-2],
            [-2,-2,1,1,-2,-2],
            [-2,-2,1,1,-2,-2],
            [-2,-2,-2,-2,1,1],
            [-2,-2,-2,-2,1,1]]`,

whose nonzero spectrum is `{1,1,-1}`.

For a concrete new rough resonant family, fix `M>=2`, set `eps_j=M^{-j}`, and for `j=1,2,3` let

`E_{2j-1}=[M-1/4,M+1/4] union [-M-1/4,-M+1/4]`,

`E_{2j}=[-M+eps_j-1/4,-M+eps_j+1/4]
          union [M-eps_j-1/4,M-eps_j+1/4]`.

Each set has Lebesgue measure one, so `f_i=1_{E_i}` is an admissible probability density with cap one.  The pair sums contain matched components with centers `eps_j/sqrt(2)->0`, while the physical supports escape to distance `M`; this is a genuine near-kernel/remote-fragment stress law.

The fleet02/B17 theorem applies with no moment, support, connectedness or fragment-count assumption and yields the **actual inequality**

`boxed:
 ess sup_{s>=0} p_{X^T A_H X}(s)
 <=p_*(0)<508/125<3sqrt(2).`

Thus this entire concrete rough resonant family is uniformly subcritical on the majority-sign sheet, even though its physical support becomes remote and its pair-sum centers approach the kernel.

Comparing with Section 5 isolates a real structural distinction: the known sharp lower obstruction is carried by a high-cardinality diffuse three-bank CLT geometry, while arbitrary rough six-variable Householder fragmentation on the majority sheet is separated from `3sqrt(2)` by a fixed positive gap.  Hence a proof that collapses all sharp candidates to that six-variable one-sheet architecture would lose the actual near-extremizers.

## 7. Scope and remaining witness frontier

The theorem above only controls the cone-tip asymptotics of the independent-uniform three-bank Parseval family.  It does not show that the cone tip is the global mode for every rotated finite member, and it gives no arbitrary-law upper bound.  The fleet02 partner result controls only the majority-sign sheet of its six-variable Householder family; the minority-sign/two-sheet side remains outside that theorem.

The strongest source-valid lower obstruction is still

`C_univ>=3sqrt(2)=4.242640687119...`.

A counterexample above this value, if one exists, must leave the second-order-optimal diffuse-bank neighborhood.  The most plausible unpaid witness mechanisms are: several macroscopic shared/intermediate-leverage rows, off-zero/two-sheet concentration, rough laws interacting with a genuinely nonseparable residual, or additional active spectrum.

For the present cube-bank sequence, the weighted local-density expansion used above supplies the needed scoped regularity near the cone tip for sufficiently large bank sizes.  No claim is made about the unrestricted continuity problem.

## 8. Deterministic check

`check_second_order_rigidity.py` verifies the exact radicals, the second-order coefficient, positivity of both rigidity penalties, and the rational Householder unit-vector/leakage identities.  Its recorded output begins

`PASS QFORM_B17_SECOND_ORDER_RIGIDITY`.

No schedule, task, notification, email, visibility, permission, authentication, paid/remote execution, or public-release state is changed by this run.
