# Independent A015 review of the common-anchor theorem

Source A008/runs/20261023T121653Z-fleet03-A008-gate-label-compression,
COMMON_ANCHOR.md and its CLAIMS.json. Claim
A008-COMMON-ANCHOR-OVERLAP-OBSTRUCTION-AND-CORE-DICTIONARY-PAYMENT@1,
statement hash f6e2559e906465e54cfeeaeda85415530d987e63c28b73ea05a9774b802081a0.
Verdict HOLDS at the FULL stated scope, without repair. The stronger
common-anchor bound in CORE_FUSION.md uses a different NEW law and does
not repair or revise this accepted source claim.

For f=2[z OR prod_j OR(X_j)]-1, the pivotal event at z is that the private
product fails, giving1-a. At a private bit of block j the event requires
z=0, the other w_j-1 bits false and every other block true, giving
a epsilon_j/(1-epsilon_j). Summing verifies I=1-a+J on the actual physical
cube. There is only one z, regardless of clause read.

Reconstruct the sampler from scratch. A local mask has empty probability
1-t_j and each nonempty probability c_j=t_j^2/(1-t_j). Its total nonempty
probability is t_j. An actual anchor with prior t_j/rho is forced uniformly
nonempty. For every tuple and each possible active anchor, the joint
probability is mu(tuple)/rho. Thus the full union law sums K mu/rho, with
K the number of nonempty masks. It normalizes because E_mu K=rho. Distinct
allocations of z are genuine tuple choices; permuting a single tuple is not.
An independent two-array union/occupation DP in this run implements exactly
this law, rather than importing any A006/A008 helper.

For an output B!=empty on private coordinates and WITHOUT z, every local
mask is forced to B_j, so the tuple is unique; its K is L(B). This gives
Q(B)=L/rho times the active c_j and inactive(1-t_j) products. Adding z to
any nonempty selection among the L active local masks gives2^L-1 DISTINCT
additional tuples, preserving every private coordinate and every anchor
option. Therefore Q(B+z)>=(2^L-1)Q(B). Other inactive-block z allocations
only increase it. This explains why the ambiguity refund is legitimate.

For equal private widths2, a local mask constrained to empty or{z} has
total weight25/28 and singleton weight1/56. Summing K mu yields
Q({z})=(1/7)(25/28)^(r-1). Actual singleton mass is(1-a)^2. At r>=4,
a=(3/4)^r<1/2 and I<2: r(3/4)^(r-1) is maximal at3,4 with value27/16.
Since log2(28/25)>3/28, this single atom gives cost/I>3(r-1)/224.
This is a bound on the FULL output law, with all other contributions
nonnegative, not the cost of one selected description.

For R=(delta_{z}+Q)/2, the core atom costs at most1. Each private pair B,B+z
has length at most1+log_+rho+sum_active(2w_j+2)+3rho. Every local empty mask
and the anchor prior remain in the exact expression before inequalities.
Physical expansion f=(1+g)/2+zeta(1-g)/2 gives identical Fourier mass
Uhat(B)^2 at B and B+z. Thus pair mass is2a(1-a) and block-j occupation
is2a epsilon_j. Neither is computed with independent copies of z.

Writing S=sum epsilon_j=2rho, the four debits are: the private constant
term<=2J, positive anchor log<=3J/2, inactive-mask cost<=3J, and active
subset cost<=8J. The core singleton term is at most1-a. The facts used are
1-a<=S, J>=aS, log_+rho<=3rho/2 and w+1<=2w. Hence complete nonempty cost
<=(1-a)+(29/2)J<=(29/2)I. The elementary full-wrapper bound h2(Var f)<=2I
is independently proved in CORE_FUSION.md, so full cost<=33I/2.

Finally, the independent PRIVATE indicator square law nu has entropy<2r
when widths are2. Expanding the empty, core and private-pair sectors gives
H(f)=2a H(nu)+2(1-a)h2(a)<4ra+2(1-a)<6I, since J=(2/3)ra.
No FEI premise, uncharged selector, or revised root is used.

Exact validation in out/checks.json includes14 width lists of lengths1..3
with widths1,2, the full independent union DP and rigorous atanh/dyadic
cost upper bounds<=29I/2, plus61 scalar obstruction parameters r4..64.
These check the independently reconstructed all-parameter proof above;
they do not establish its infinite scope by extrapolation. No substantive
source repair was supplied, and the review does not accept unrelated
claims in that source's CLAIMS.json.
