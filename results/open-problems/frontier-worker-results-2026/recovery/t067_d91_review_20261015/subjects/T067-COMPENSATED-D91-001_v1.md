# Explicit three-state ferromagnetic cutoff d>=91

T067-COMPENSATED-D91-001 v1. Status: proof (unaudited).
No priority assertion, no Galton--Watson assertion, and no resolution of T067
at all regular degrees. All new dependencies remain subject to external audit.

For every integer d>=91 and 0<lambda<=1/sqrt(d), the uniform-root symmetric
ferromagnetic three-state Potts broadcast process on the regular d-ary tree
is nonreconstructible, including equality.

## Parameters and finite Gaussian certificate

Set D=91, L=209657/2000000, beta=49/4. Exact integer arithmetic verifies
D L^2>=1 and L<39/250. Let fU,fM be C_U,C_M from (2) of
COMPENSATED-REPLACEMENT-EXT-001 v1 with derivative constants
(1/8,1/5,2/5,1/2,3/5); let qU,qM be those same explicit rational functions
with constants (8,20,38,38,99), all evaluated at this fixed L. Define

 alpha_D=(D-qU)/fU,
 B_D=81[(1-qU/D)fM/fU+qM/D],
 E_D(s)=alpha_D(s-g3(s))-B_D s^2-U_G(s).

checks/verify_compensated91.py independently reconstructs these constants
by the five separate error categories, and proves by exact rational comparisons

 D-qU-9beta fU>0,  qM-qU fM/fU>0,
 E_D(s)>3/200 for every s in [1/10,2/3].              (1)

For completeness, the continuous Gaussian comparison uses86 rational signal
endpoints s_i=10/(100-i), i=0,...,85, and85 intervening intervals. It reads
the refined raw quadrature sums for F_1 and Q, not the producer's degree100
gate. Each coordinate of a standard two-dimensional normal is truncated at
6 and split into192 signed bins of width1/16. Conditional-mean quadrature
errors are bounded by (9s/10)P0 D0 and90s P0 D0; whole-square tails by
1-P0^2 and36(1-P0^2). The analytic justification is written in
GAUSSIAN-FOURTH-GATE-001 v1; changing bin width only changes the exact bin
moments and their resulting D0, not the proof. No observed error rate is used.

The same derivative and heat-generator argument gives
|g3''|<32, |U_G''|<3600, so |E_D''|<=32alpha_D+2B_D+3600=:C_D.
From raw directed dyadic endpoints, the separate exact verifier recomputes
conservative endpoint lower bounds e_i and checks all85 inequalities

 min(e_i,e_(i+1))-C_D(s_(i+1)-s_i)^2/8>3/200.

The minimum exact rational, all margins, source hashes and86 endpoint hashes
are in checks/compensated91_gate.json. Both a missing endpoint and a unit
inflation of the U_G upper bound make the live gate fail. A separate192bit
direct three-logit quadrature on all192^2 signed product bins agrees with
both raw sums at indices0,42,85. Arb outward rounding remains a software
trust premise. These are same-worker checks, not independent external audits.

## Fixed-point exclusion and local entry

At critical lambda=d^(-1/2), the canonical posterior law decreases in
Blackwell order and converges by the reverse-martingale construction.
For fixed finite d, positive likelihood denominators bounded below by1-L
make its BP map continuous, hence the limit is a symmetric calibrated fixed
point. Put x=M/9, U=E||3p-1||^4, T=E sum_i(3p_i-1)^3.
The initial pure-state law has T=6; positive edges multiply T by lambda^3,
and the reviewed CUBIC-FUSION-001 v1 preserves nonnegative T. Thus T>=0
also in the limit, and0<=x<=2/3.

For x>0 put K=U/(81x^2), gamma=(x-g3(x))/x^2. Since lambda<=L, the
general-L F_1 comparison and compensated comparison respectively yield

 K>=(d gamma/81-fM)/fU,
 (d-qU-9beta fU)K
     <=d U_G(x)/(81x^2)-beta d gamma/9+qM+9beta fM.

The coefficient on the latter left is positive by (1) and d>=D.
Substituting the first bound into the second cancels beta exactly and gives

 E_d(x)=((d-qU)/fU)(x-g3(x))
         -81[(1-qU/d)fM/fU+qM/d]x^2-U_G(x)<=0.       (2)

For x>=1/10, the reviewed GAUSSIAN-GAP-001 v1 gives x-g3(x)>0.
The first coefficient in (2) increases with d, while the subtracted
coefficient equals81[fM/fU+(qM-qU fM/fU)/d] and decreases, by (1).
Therefore E_d(x)>=E_D(x)>3/200, contradicting (2).

The canonical limiting x is consequently below1/10. The new, separately
reconstructed UNIFORM-LOCAL-EXT-001 v1 excludes every nonzero critical fixed
point with x<=1/10 for every d>=42, covering d>=91. Hence the canonical
limit is zero and its iterates eventually enter the radius. Convergence to
the canonical fixed point was established first; absence of arbitrary fixed
points alone was not substituted for finite-time entry. Second-moment decay
implies total-variation decay and nonreconstruction.

For 0<lambda<eta=1/sqrt(d), replace each observation with an independent
unconditional observation with probability1-lambda/eta and hide the flag.
Its posterior map is S_c(p)=u+c(p-u), c=lambda/eta, and
1-eta+3eta S_c(p)_i=1-lambda+3lambda p_i.
Discarding observations and applying this root-independent degradation
preserve Blackwell order under conditional-root-independent fusion. Induction
from the pure-state experiment gives x_n^lambda<=x_n^eta, whose limit is zero.
This rederives the subcritical step without a blanket audit-metadata premise.

New supporting claims: FOURTH-DERIVATIVES-001 v1, COMPENSATED-CUBIC-001 v1,
COMPENSATED-REPLACEMENT-EXT-001 v1 and UNIFORM-LOCAL-EXT-001 v1. The checked
cutoff remains256 until the authorized external exact-version reviews admit
these new pieces and this composition. Degrees5..90 remain outside this claim.
