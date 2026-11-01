# A sharp necessity test for matched-isospectral reference conversion

Uniform normalized Walsh coefficients; finite spaces; entropy, CE and KL in bits.
Every reference is a COMPLETE normalized law. All physical children, reference-only
labels, inherited normalizers, original reaches and old source debits remain.
Full FEI is OPEN. This is a variational transfer/obstruction theorem, not initial
Boolean source admission. No external-reference constraint is asserted to be forced
by FEI unless explicitly supplied.

## 1. Consume the closed frontier

A035-ALL-QUERY-TERMINAL-KL-ENVELOPE v1, run20261023T110610Z, already closes the
saved A031 NEXT. For the actual all-L triangle, its SAME original rate17 source
and C2 reserve>7/8 pay ALL adaptive physical histories with full terminal
KL<=1+delta,0<=delta<1/8, leaving>1/8-delta. Fair_j and one prescribed1/32 mixture
are included. The proof subtracts the original source from

  sum_v reach(v)B_i(p_v)+E_leaf CE(p_leaf,Q_leaf)
     =H(p_root)-sum_v reach(v)J_i(p_v)+E_leaf D(p_leaf||Q_leaf).   (1)

The constant fourth original triangle parent bounds E B_a<=3/4. This is generic
endpoint transfer supplied with a Boolean source. This stage reconstructs (1)
and that subtraction, independently checks complete finite-tree envelopes and
the actual Boolean uniform-five-bit reference obstruction, and consumes A035's
review of our previous strengthened source. No additional marker cycle is new.

## 2. Exact variational transaction criterion

For ANY actual Boolean query i, let p be the full parent spectrum, p_tau the two
actual child spectra, Q a finite-CE supplied complete parent reference, and
Qbar=marg_i Q. For each outcome supply a NONEMPTY admissible reference class A_tau
on the same remaining labels, with finite achievable CE. Define

 d_tau=inf_(R in A_tau) D(p_tau||R).

The sharp infimum of the complete transaction increment, including the queried
erasure and BOTH full child reference costs, is

 inf [B_i(p)+E_tau CE(p_tau,R_tau)-CE(p,Q)]
                  =E_tau d_tau-D(p||Q)-J_i(p).                 (2)

This follows directly from H(p)=B_i+E H(p_tau)+J_i. It is an infimum statement;
an actual minimum is claimed only where a minimizer is constructed below. If
classes impose joint constraints across children, replace E d_tau by the joint
infimum of E D; no independence of admissible choices is silently assumed.

For the supplied incoming marginal the exact occupancy refund is

 rho=CE(p,Q)-B_i-E CE(p_tau,Qbar)>=0.

Thus the infimum fresh conversion price is inf E D(p_tau||R_tau)
-E D(p_tau||Qbar); the infimum net charge also subtracts rho. Any claim of a
NECESSARY positive conversion must name A_tau (including any compatibility
constraint) and lower-bound this infimum. Exhibiting one expensive arbitrary
reference is insufficient.

## 3. Existing actual-block-mass calibration is free, including the nullspace

Let pi be a fixed finite partition of the remaining labels. Starting with any
finite-CE Qbar, restrict each new reference to keep Qbar's conditional law WITHIN
each block and to have the ACTUAL child block mass pi p_tau. The full normalized
calibration is

 Qcal_tau(S)=(pi p_tau)(z) Qbar(S)/(pi Qbar)(z), S in block z.    (3)

If actual block mass is positive, finite CE guarantees a positive denominator.
An actual-zero block is assigned full reference mass0; all such blocks remain
in normalization. Formula (3) gives the exact CE change

 CE(p_tau,Qcal_tau)-CE(p_tau,Qbar)
                    =-D(pi p_tau||pi Qbar)<=0.                 (4)

For an isospectral physical query, both child spectra equal pbar=marg_i p.
Full signed amplitudes u_T,v_T obey p_+-p_-=4u_Tv_T, so isospectrality means
u_Tv_T=0 at EVERY frequency. It gives B_i=J_i=0 and zero sign-bin phase energy.
Equations (3)-(4) still hold: both calibrations are the SAME law, and the whole
transaction releases rho+D(pi pbar||pi Qbar), rather than needing a positive
new bank. If the inherited block masses are already actual, calibration changes
nothing. This identifies the scope of the A096/A097 actual-mass matching step;
it does NOT fund a subsequent prescribed mixture or impose an unproved source.

If admissible classes allow every complete law, choosing R_tau=p_tau gives
d_tau=0 and net increment=-D(p||Q)-J_i<=0. Hence an unconstrained claim of an
intrinsically necessary positive conversion is false. Universal source admission
is exactly the step that this observation does not provide.

## 4. Prescribed compatible branch profiles: exact minimum, not a sample price

Now fix the isospectral retained law pbar and partition pi, write P=pi pbar.
Let Q0=Qbar and r0=pi Q0. Assume the incoming conditionals match the actual ones
INSIDE every occupied block:

 Q0(S)=r0(z) kappa_z(S),   pbar(S)=P(z) kappa_z(S) when P(z)>0.   (5)

For P(z)=0 choose kappa_z from Q0; these reference-only blocks are retained.
Supply prescribed branch profiles r_+,r_- with (r_++r_-)/2=r0 and positive mass
on every occupied block. Require BOTH

 pi R_tau=r_tau,               (R_++R_-)/2=Q0.                 (6)

These are EXTRA explicit reference obligations, not consequences of Booleanity
or of (3). All fine complete laws satisfying (6) are allowed in the minimization.
The KL chain rule gives for every such law

 D(pbar||R_tau)=D(P||r_tau)+sum_z P(z)D(kappa_z||R_tau(.|z))
                                               >=D(P||r_tau).

The complete pair R*_tau(S)=r_tau(z)kappa_z(S) simultaneously attains BOTH bounds
and is compatible with Q0 by (5)-(6). Ghost block conditionals can remain Q0's;
they contribute zero KL but preserve the entire mean reference and normalization.
Therefore the exact MINIMUM conversion price relative to inherited Q0 is

 E_min= (1/2)sum_z P(z)log2[r0(z)^2/(r_+(z)r_-(z))]
      =-(1/2)sum_z P(z)log2(1-eta_z^2)>=0,
 eta_z=(r_+(z)-r_-(z))/(2r0(z)).                              (7)

It is positive exactly when some occupied block has eta_z!=0. With bits as
units, the sharp expression also gives the useful inequalities

 sum_z P(z)eta_z^2/(2 ln2) <= E_min,
 E_min <=sum_z P(z)eta_z^2/[2 ln2(1-k^2)] if |eta_z|<=k<1.       (8)

Use -ln(1-t)>=t and -ln(1-t)<=t/(1-k^2). A zero prescribed occupied mass means
infinite cost, not a removable zero. The source pays E_min-rho at this query;
the occupancy refund is not added a second time or replaced by a fair-bit credit.

Thus actual phase imbalance and reference-profile imbalance are DIFFERENT
objects: isospectral actual children force every u_Tv_T=0, but do not force the
eta_z of an EXTRA required reference profile to vanish. Equation (7) supplies
a sharp lower bound and a complete attainer for a specified obligation.

## 4a. Arbitrary inherited fine laws: sharp reference-only capacity and optimizer

Condition (5) is ESSENTIAL for the simple block formula (7). Here is the general
solution without that condition. Write q_S=Q0(S), and parameterize any compatible
pair by R_+(S)=q_S(1+t_S), R_-(S)=q_S(1-t_S). Values with q_S=0 are0 in both
children. For each block z put

 Delta_z=(r_+(z)-r_-(z))/2,
 g_z=sum_(S in z, pbar(S)=0)q_S.                              (10)

The exact constraints are |t_S|<=1 and sum_(S in z)q_S t_S=Delta_z. On occupied
cells |t_S|<1 is needed for finite CE. Including ALL complete normalizers, the
conversion objective relative to Q0 is simply

       E(t)=-(1/2)sum_(pbar(S)>0) pbar(S)log2(1-t_S^2).        (11)

It is nonnegative, strictly convex on occupied coordinates, and zero exactly
when ALL occupied t_S=0. Ghost/reference-only cells have zero objective and
capacity |sum_ghost q_S t_S|<=g_z. Therefore the SHARP zero-cost criterion is

 E_min=0  iff  |Delta_z|<=g_z for EVERY block z.               (12)

For these cases, keep occupied references literally unchanged and distribute
Delta_z over the ghost cells, e.g. t_S=Delta_z/g_z when g_z>0. Zero ghost mass
permits only Delta_z=0. This changes prescribed block profiles and BOTH full
references while preserving their full average, at EXACTLY zero conversion cost.
It is not deletion of ghosts: they are precisely the constrained moving mass.

If |Delta_z|>g_z and pbar(z)>0, every minimizing ghost tilt with q_S>0 saturates at
sign(Delta_z). Occupied tilts have the same sign and obey the unique multiplier
equation (natural-log scaling; the common positive1/ln2 is absorbed in lambda)

 pbar(S)t_S/(1-t_S^2)=lambda_z q_S,
 t_S=2lambda_z q_S/[pbar(S)+sqrt(pbar(S)^2+4lambda_z^2 q_S^2)],
 sum_occupied q_S t_S=Delta_z-sign(Delta_z)g_z.               (13)

The left side is continuous strictly increasing from minus total occupied q
to plus total occupied q as lambda ranges over the reals. Hence the multiplier
exists uniquely whenever |Delta_z|<sum_(S in z)q_S. The fully one-sided boundary
with an occupied block gives infinite CE. An entirely actual-zero block has
only free ghost capacity and contributes zero cost, including its boundaries.

This is an exact optimizer description, not a floating search. To prove optimality,
convexity gives the occupied supporting-hyperplane bound with slope lambda_z q_S
in natural-log units. At a saturated ghost, 0>=lambda_z q_S(t_S-t*_S). Adding
these inequalities and the exact block constraints gives E(t)>=E(t*). Strict
convexity makes the occupied solution unique; free ghost allocations can be
nonunique in zero-cost cases. The rational certificates check these exact primal
and dual conditions for75 positive-cost configurations and all15 frozen zero-cost
boundary fixtures; no numerical optimizer or extrapolation supplies the theorem.

When (5) holds there are NO reference-only cells INSIDE an occupied block.
Its occupied p and q are proportional, so (13) has a constant tilt in that block.
This recovers (7). Without (5) even a uniform tilt can be suboptimal: for uniform
p on4 cells, q=(3/8,1/8,3/8,1/8), profiles r_+=(3/4,1/4), r_-=(1/4,3/4), moving
1/64 of compatible reference mass toward the first atom in the first plus block
and the opposite direction in the second plus block, with opposite minus moves,
strictly lowers CE relative to the proportional-within-q pair. An exact rational
product below1 certifies this scope guard. No matched-conditional assumption is
silently imported from A096/A097, whose inherited fine profile may be arbitrary.

An actual Boolean FREE nonempty-profile change: use the parity query below but
parent Q(9)=1/2,Q(10)=Q(15)=1/4. Its carried law has q(1)=1/2,q(2)=q(7)=1/4,
true/reference vacuum0 and actual pbar=delta_7. Separate nonempty bins {1} and
{2,7} (all other zero cells assigned harmlessly). Their profiles are(1/2,1/2),
ghost capacities(1/2,1/4). Prescribe r_+=(5/8,3/8),r_-=(3/8,5/8). The complete
pair R_+=(5/8,1/8,1/4), R_-=(3/8,3/8,1/4) on labels1,2,7 is compatible and
has EXACTLY the old CE2 on BOTH children: positive nonempty profile variation,
zero actual phase/JS/occupancy energy, zero conversion charge. This explicitly
closes the reference-only-capacity subcase in the current isospectral nullspace,
conditional on the supplied finite-CE source. It does not price that initial source.

The FREE example extends to EVERY coherent controller a in{-1,0,1}, b=1-a^2
on any independent controller cube, G=a+sigma*b*parity4, sigma=+/-1. Write A_U,B_U
for its controller coefficients. Use the complete reference with vacuum A_U^2
and nonempty cells B_U^2 times the displayed seed reference. It normalizes by
sum A^2+sum B^2=E a^2+E b=1. After the seed query the full actual laws are the
SAME in both children, with vacuum A_U^2 and nonempty occupied label7 of mass
B_U^2. Its queried-seed singleton and all phase products vanish. The old carried reference and BOTH
new complete references agree at EVERY actual occupied cell: at vacuum A_U^2
and at label7 B_U^2/4. The actual query occupancy also matches the reference
deterministically, so rho=0. Consequently B=J=0 and the full CE conversion is
EXACTLY0, including arbitrary zero controller coefficients and all reference-
only cells. Query influence is beta=E b; beta may be arbitrarily small, but no
new source or per-query bank is introduced. Proper profile change requires beta>0; inactive controllers have unchanged references and zero cost. The proof is algebraic for all
controller dimensions;162 small truth-table wrappers independently test it.

## 5. Exact actual Boolean positive-cost nonempty-profile witness

Use the fixed four-variable parity f(x)=product_(j=0)^3 x_j. Query bit3; children
are +/-parity3, with identical spectral law pbar=delta_{7}. All singleton
coefficients, actual u_Tv_T products, B_i and J_i vanish; query influence is1.
The whole Boolean convolution is verified, not merely normalization.

Supply the parent COMPLETE reference Q({3,0})=Q({3,0,1,2})=1/2 (integer labels9,15),
zero elsewhere. It has finite CE1, true vacuum mass0, and no singleton query
reference mass. Its carried marginal is Q0({0})=Q0({0,1,2})=1/2, labels1,7.
Both labels are NONEMPTY; vacuum remains0 in all following references. Reference
occupancy of query bit3 is deterministic1, matching the actual parent, so rho=0.

Take two nonempty bins separating the ghost singleton label1 from occupied
label7 (remaining labels may be assigned to either bin; they have zero mass).
Prescribe r_+(occupied)=1-epsilon and r_-(occupied)=epsilon, epsilon=2^-m,
and complementary ghost masses. The two references average to Q0 and preserve
true vacuum0. Under these stated bin constraints, (7) proves the necessary
minimum

       E_min=(1/2)log2[1/(4 epsilon(1-epsilon))]
             >(m-2)/2.                                      (9)

For m4 it exceeds ONE bit, although actual phase/JS/occupancy funds are ZERO.
Expected full terminal KL is1+E_min>2, outside A035's sufficient1+delta envelope.
All laws have finite support on the SAME fixed cube; no dummy dimensions or
large arrays are used. As m grows, this conditional mandatory cost is unbounded
on a FIXED actual Boolean function, despite fixed influence. This refutes any
unrestricted phase-only or fixed-surplus supplier for these prescribed profiles;
it is NOT an FEI counterexample.

Crucially, actual-block-mass calibration (3) would instead set ghost mass0 and
occupied mass1 in BOTH children, releasing one bit. The prescribed profiles in
(9) are NOT mandated by A096/A097 matching, and no assertion is made that FEI
requires them. Necessity is proved over the explicit class (6), not invented
for universal FEI. Any downstream proposed completion must specify why its own
mathematical constraints impose a profile imbalance of this kind.

## 6. Same-ancestor amortization and the honest next line

On a finite complete tree of exactly isospectral seed queries, identify the
retained seed-label space across nodes and suppose these compatible profiles
are supplied at every node, with the same actual within-block kappa. Then
expected conversion equals the nonnegative sum of reached E_min. It telescopes
EXACTLY to E_leaf D(P||r_leaf)-D(P||r_root). Query erasures and JS are0 in this
identified sector; any actual occupancy refunds are separately subtracted.
Thus original unused surplus A must cover the actual cumulative prescribed
penalty minus those refunds. It cannot be issued again after each calibration.
Untouched independent spectator g keeps complete M(g)+CE(p_g,Q_g) with coefficient
ONE on BOTH sides; partition/cost conditions apply only to the designated source.

The mathematical proofs (2)-(8) are generic reference geometry, explicitly NOT
a new Boolean-admission inequality. Actual signed Booleanity certifies the null
physical witness and all its real reaches; the normalized-singleton control
still excludes normalization-only initial admission. The original entropy-
weighted orthogonality identity is already in A031 LEARNED and is not claimed new.

First unsupported universal line: exhibit an admissible reference class required
by a surviving universal proof, EXCLUDING the free actual/inherited calibration,
whose full-KL infimum has an actual supplied source price, or prove an influence-
priced initial reference for arbitrary signed Boolean cores. Equations (7)-(9)
now provide an exact necessity/attainment test once such constraints are supplied.
Another arbitrary expensive target or bounded marker cycle does not supply them.
