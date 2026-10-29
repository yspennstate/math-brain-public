# The joint single-edge constant survives the spectral engine weights

Date: 2026-08-16  
Status: weighted edge inequality and engine specialization proved; independent audit required

Companions:

* `SINGLE_EDGE_JOINT_SHARP_20260816.md`, SHA-256
  `19fb35ca94b5a8559e3cfaafc58a6d78562ff8b517ca75f299516694dca1cbca`
  (independent audit pending);
* `DISTINGUISHED_BLOCK_SPECTRAL_SPLIT_20260816.md`, SHA-256
  `f18916f69b7fbd24c96325ae3da9c046ba31152a893ca736fb11de737e083f0f`.

The joint threshold lemma improves the outside-uncertainty coefficient from
`3/32` to `64/729` when target mass and outside variance have equal weights.
The distinguished-coordinate spectral engine gives them different weights.
Its target coefficient is always at least its outside coefficient, and this is
exactly the order for which the same improvement tensorizes algebraically.

The resulting ledger is still edge-coordinate only.  It does not control the
sum of route uncertainties or construct the conditional decision algorithms
needed by the block engine.

## 1. Weighted joint threshold inequality

Let `q:[0,1]->[0,1]` be decreasing.  Write

`Q(q)=integral_0^1 integral_0^1
       q(u)q(v)[min(u,v)-uv]du dv,`                           (1)

`J(q)=2 integral_(0<u<v<1)
       u(1-v)q(v)[1-q(u)]du dv,`                             (2)

`p=integral_0^1q(u)du,       r=integral_0^1q(u)[1-q(u)]du.` (3)

The sharp target-mass companion proves

`Q(q)<=p^2/9.`                                               (4)

The joint companion proves

`Q(q)+J(q)<=p^2/9+(64/729)r.`                               (5)

**Lemma.** For every `lambda>=mu>=0`,

`lambda Q(q)+mu J(q)
 <=(lambda/9)p^2+(64mu/729)r.`                              (6)

### Proof

Simply write

`lambda Q+mu J=mu(Q+J)+(lambda-mu)Q`                        (7)

and apply (5) to the first term and (4) to the second.  Both coefficients are
nonnegative precisely because `lambda>=mu`.  QED

The constants in (6) are simultaneously sharp under uniform edge weights.
in (4), so `lambda/9` cannot be decreased.  For

`P(Tau=8/9)=epsilon,       P(Tau=0)=1-epsilon,`              (8)

the target mass is quadratic in `epsilon` while the outside term is linear;
as `epsilon->0`, the required uncertainty coefficient tends to `64mu/729`.
Thus increasing the target coefficient cannot buy a smaller uniform
uncertainty coefficient.

## 2. Edge resampling form

Let the edge-weight density on `[a,b]` satisfy

`rho(t)>=alpha>0` almost everywhere.                               (9)

For one edge `e`, put

`z_e=(X^e-X)^+,       Y_e=(w_e,w_e'),`                      (10)

`M_e=E[(E[z_e|Y_e])^2],`

`V_e=E[Var(z_e|Y_e)].`                                      (11)

Let

`p_e=P(e in gamma),`

`r_e=E[Var(1_(e in gamma)|w_e)].`                           (12)

The exact target/outside kernels, followed only by the two reciprocal density
bounds, give

`M_e<=alpha^(-2)Q(q_e),       V_e<=alpha^(-2)J(q_e),`       (13)

with `p=p_e` and `r=r_e` in (3).  Therefore (6) yields, for every
`lambda>=mu>=0`,

`lambda M_e+mu V_e
 <=alpha^(-2)[lambda p_e^2/9+(64mu/729)r_e].`               (14)

At `lambda=mu=1`, this is the joint second-moment estimate in the companion.
At `mu=0`, it is the sharp target-only estimate.

## 3. Distinguished-coordinate engine specialization

Specialize the distinguished-block spectral split to single-edge labels.  In
that notation,

`C_z+P_z=sum_e M_e,       V_z=sum_e V_e.`                    (15)

For a noise parameter `kappa in (0,1)` and integer `r>=2`, set

`lambda=1+kappa,`

`mu=kappa+(1-kappa)^r,`

`c_r=r(r-1)/2.`                                              (16)

Since `(1-kappa)^r<=1`,

`0<=mu<=lambda.`                                             (17)

The exact spectral-engine inequality is

`Var(X_(Mn))
 <=(1+kappa)C_z+P_z+mu V_z+c_r D_z,`                        (18)

where `D_z` is the variance-weighted outside revealment term.  Positivity and
(15)--(17) imply

`(1+kappa)C_z+P_z+mu V_z
 <=lambda(C_z+P_z)+mu V_z`

` <=alpha^(-2)[(lambda/9)sum_e p_e^2
                +(64mu/729)sum_e r_e].`                     (19)

Consequently

`Var(X_(Mn))
 <=alpha^(-2)[((1+kappa)/9)sum_e p_e^2
      +(64/729)(kappa+(1-kappa)^r)sum_e r_e]
   +c_r D_z.`                                                (20)

Equation (20) is the sharp weighted single-edge ledger supplied by these
one-dimensional inputs.  Adding the separately sharp target and outside
bounds would put `3/32` in place of `64/729` in its second coefficient.

## 4. What remains open

The first sum in (20) is the squared-influence target.  The second is

`sum_e r_e=sum_e E[Var(1_(e in gamma)|w_e)],`                (21)

which can still be comparable to expected geodesic length under the available
bounds.  The last term `D_z` asks for algorithms that, after the target edge is
revealed, determine the positive increment with small variance-weighted
outside revealment.

Thus the improved coefficient is a real constant gain but not a variance
halving theorem.  A closing argument must control (21), preserve cancellations
at block scale, or replace exact outside revealment by a quantitatively audited
approximate certificate.

## 5. Break checks

1. The order `lambda>=mu` is essential in (7).  The proof gives no assertion
   for a negative coefficient `lambda-mu`.
2. The engine order follows from `(1-kappa)^r<=1`; no asymptotic choice of `r`
   is needed for (17).
3. In (18), `P_z` has coefficient one rather than `1+kappa`.  Replacing it by
   the larger coefficient in (19) is an explicit upper relaxation.
4. The density lower bound is used twice in each kernel.  No density upper
   bound or uniform-law substitution is hidden in (13).
5. The sharpness construction (8) is limiting: its diagonal high-threshold
   pairs contribute at order `epsilon^2`, so it need not attain equality for a
   fixed positive `epsilon`.

An independent referee should verify the weighted decomposition (7), the
coefficient order (17), and the passage from the exact spectral ledger (18) to
(20) before this note is used in the FPP campaign.
