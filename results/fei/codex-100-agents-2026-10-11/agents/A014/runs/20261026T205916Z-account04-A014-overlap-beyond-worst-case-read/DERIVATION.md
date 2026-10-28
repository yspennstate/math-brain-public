# Global edge dilution fails; local weights repair the same source

All logarithms have base two. The result concerns a complete fixed occupation
reference, not the entropy of a virtual spectrum. Uniform Boolean functions
use f=1-2C. Write s=EC, v=4s(1-s), p(A)=fhat(A)^2 and I=sum |A|p(A).

## 1. Original mass and disjoint components

For a nonempty vertex set A the original mass F_G(A) is the sum over maximal
matchings in G[A], with a factor lambda_e/24 per root edge, lambda_e/32 for
an unmatched vertex attaching outside A, lambda_e/8 for attachment to a root
endpoint, and J(a,b)=a!b!/[(a+b+1)^2(a+b+2)] per root. Set F_G(empty)=1.
The positive weights are fixed before observing A. On disjoint components
F factors EXACTLY: root maximality, attachment choices and J factors all
separate. Thus the COMPLETE nonempty normalizer is

 Z_G=product_j(1+Z_j)-1,  q_G(A)=F_G(A)/Z_G  (A nonempty).

The actual calibrated full reference is Q(empty)=1-v, Q(A)=v q_G(A), so

 CE(p,Q)=h2(v)+sum_(A nonempty) p(A)log(1/F_G(A))+v log Z_G.       (1)

For one isolated edge its four masses are 1, lambda/32, lambda/32,
lambda/48; hence 1+Z_edge=1+lambda/12. The last value includes J(0,0)=1/2.
For the edge indicator C_e=1-AND(x1,x2), s_e=3/4 and its normalized squared
Fourier law has masses 3/4,1/12,1/12,1/12. These two probability laws differ.

## 2. An actual unbounded-read obstruction to the global scale

For every integer r>=12 let m=r^2 and G_r=K_r disjoint union m edges.
Use the ORIGINAL globally uniform feasible scale lambda=1/Delta=1/(r-1).
Every edge is an indispensable positive minterm of the edge-union function;
maximum read is r-1. All n=r+2m physical coordinates are relevant. There
are no dummy coordinates, cloned coordinates or arbitrary core suppliers.
The clique independent-set indicator has density s_K=(r+1)/2^r and
I(f_K)/s_K=h_r=2r(r-1)/(r+1). Product pivotal counting gives

 s=s_K(3/4)^m,     I=s[(4/3)m+h_r].                            (2)

The wrapper bound needed below can be checked directly here, without a
universal FEI or isoperimetric input. Since r>=12, s_K<=13/4096<1/4,
and hence 4s<1. Binary entropy satisfies h2(v)<=v log(e/v). The function
x log(e/x) is increasing on (0,1], so v<=4s gives
h2(v)<=4s log(e/(4s))<=4s log(1/s). Since log(4/3)<1/2,
log(1/s)<=r+m/2. Finally m=r^2>=6r and I>=4ms/3 imply
4s(r+m/2)<=2I. All logarithms have positive arguments; constants e<4
and log(4/3)<1/2 follow respectively from the exponential series and 16<18.

The ACTUAL p-weighted number of active edge blocks is m s, of singleton
edge blocks (2/3)m s, and of double edge blocks (1/3)m s. These moments
exclude the empty global Fourier set automatically.

Each clique atom satisfies F_K(B)<=1+Z_K. Therefore its total log cost is
at least -v log(1+Z_K), including B=empty. The entire normalizer obeys

 Z_G/(1+Z_K)=(1+lambda/12)^m-1/(1+Z_K)
             >=(1+lambda/12)^m-1>=m lambda/12>=1.

Bernoulli's inequality applies at positive lambda. Thus its signed
normalizer contribution cancels the ONLY potentially negative clique cost;
it is not dropped without payment. All remaining edge constants are positive.
Equations (1)-(2) give

 CE(p,Q)/I >= [m/((4/3)m+h_r)]log(r-1)
            >=(2/3)log(r-1) -> infinity.                       (3)

Here h_r<=2r and r>=12 imply (4/3)m+h_r<=(3/2)m. The full wrapper is
nonnegative, including possible zero endpoint masses with 0log0=0.
Consequently universal influence payment of THIS globally scaled source
is false even with feasible weights and genuine unbounded overlap.
This is not a disproof of FEI. In fact H(f_G)<6I: the normalized indicator
spectrum factors, its clique entropy is <=r, and its edge entropy is
h_e=2-(1/2)log3<5/4. The exact sign/indicator identity implies
H(f_G)<=h2(v)+4s H(P_C). The elementary universal wrapper bound h2(v)<=2I
then gives H/I<=2+3r/m+3h_e<6 for r>=12. The discarded term in that identity
is -4s h2(s)<=0. Thus the divergent quantity in (3) is reference mismatch.

## 3. Exact matching calibration and the normalization refund

On m edges alone, for ANY 0<lambda<=1 the ENTIRE nonempty cost is exactly

 C_nonempty/I=(3/4)log(1/lambda)+(1/2)log32+(1/4)log48
                  +[3(1-(3/4)^m)/m]log[(1+lambda/12)^m-1].     (4)

For m=1 the lambda dependence cancels completely. This is an important
boundary check: ignoring the negative normalizer would manufacture an
obstruction on one edge. For m increasing and lambda=1/(2m-1), the
normalizer stays bounded above and below by positive constants, and (4)
diverges as (3/4)log(2m-1)+O(1). This diagnostic is secondary to (3), which
also treats the globally degree-normalized source with growing read.

## 4. Local weights repair the SAME graph and occupation construction

Keep G_r and the complete formula of section 1, but fix lambda_e=1 on each
isolated edge and lambda_e=1/(r-1) on clique edges. Every vertex has incident
weight sum exactly one. These are intrinsic, component-local, feasible
weights, determined by G_r before sampling. No posterior tuning occurs.
Let R_K(B)=F_K(B)/(1+Z_K) on ALL clique subsets and let each edge law R_e
have its four masses above divided by 13/12. Their product R is normalized
on ALL subsets. The repaired original occupation reference on NONEMPTY
sets is EXACTLY R conditioned nonempty, since disjoint F factorizes.

We use log(1/R_K(B))<=21r/4. Here is a direct proof with conservative
constants, independent of the entropy of the clique. For k=2t,
F_K(B)=(2t)!/[2^t t!] [lambda/48]^t>=t![lambda/48]^t.
For k=2t+1 its additional factor is lambda(3r-2t-3)/96>=1/48, so
F_K(B)>=t![lambda/48]^t/48. The t=0 cases are interpreted separately.
Using t!>=(t/e)^t, ln u<=u-1, log e<3/2, t<=r/2 and log48<6 gives
log(1/F_K(B))<= (9/2)r+6<=5r for r>=12. Empty B has F=1.
The original complete-normalizer counting argument bounds the sum INCLUDING
empty by exp(r/8), hence log(1+Z_K)<=r/4 and the asserted 21r/4 follows.
For clarity that argument counts root matchings by |E|^t/t!, absorbs J<=a!b!
with endpoint ordered lists, sums internal leaves by (1-r lambda/8)^(-2t)<2^t,
and external leaves by (1+r lambda/32)^r<=exp(r/16). This gives
1+Z_K<=exp(r/16+lambda|E|/12)=exp(5r/48)<=exp(r/8).
Its root=0 term includes the empty structure, so the added 1 is accounted for.

For one repaired edge, log(1/R_e(empty))=log(13/12)<1/8 and every
nonempty log(1/R_e(state))<6. The first inequality follows from
13^8<2*12^8; the others from 104/3<64 and 52<64. Its expectation under
the normalized TRUE indicator spectrum is therefore <51/32.

Conditioning R nonempty contributes v log(1-R(empty))<=0, retained before
the upper bound. Summing the nonnegative product log lengths against p on
nonempty sets and then adding the empty indicator atom only INCREASES cost:

 C_nonempty(repaired)<=4s[(21/4)r+(51/32)m].

Together with (2), m=r^2 and r>=12 this gives

 CE(p,Q_repaired)/I <=2+(63/4)(r/m)+153/32<=259/32<9.            (5)

Thus the very same growing-read Boolean family and the SAME full occupation
construction have divergent cost at global weights but bounded cost at
intrinsic local weights. The congestion ratio of the two ORIGINAL full
costs is at least (64/777)log(r-1); no maximum-read multiplier is needed
in (5). This ratio is a diagnostic, not a universal sufficient congestion.
By the earlier general projection/calibration identity, actual full-CE
decrease bookings and BOTH terminal costs on every stopping tree telescope
within this ONE repaired root budget. Those decreases are not identified
with arbitrary query fees and the reference cannot be reset along a history.

## 4a. Explicit spectral congestion in place of maximum read

More generally keep the clique weights fixed as above and give isolated
edge j ANY fixed activity 0<lambda_j<=1. Define, using the ACTUAL spectrum,

 kappa_dil = sum_j Pr_p(S meets edge j) log(1/lambda_j)/I
           = s sum_j log(1/lambda_j)/I.                       (6)

This is an activation-weighted spectral quantity; it is not defined as CE/I.
The nonempty source is still the entire occupation table, with normalizer
(1+Z_K) product_j(1+lambda_j/12)-1. For the normalized FULL law of edge j,
the empty code length is <1/8 and each nonempty code length is
<6+log(1/lambda_j), since 32(1+lambda_j/12)<64 and
48(1+lambda_j/12)<64. Its mean under the true indicator spectral law is
therefore <51/32+(1/4)log(1/lambda_j). Repeating section 4, with the
conditioning refund retained, proves the all-activity theorem

 CE(p,Q_lambda)<=(259/32+kappa_dil)I.                          (7)

Local weights give kappa_dil=0 for EVERY r while maximum read tends to
infinity. Global feasible weights give kappa_dil>=2log(r-1)/3, and section 2
shows that this charge really appears in the complete cost, rather than
being a loose upper-bound artifact. Equation (7) does not claim that
kappa_dil controls arbitrary connected graph references.

## 5. Checks and the unpaid line

Potential failures checked: empty normalization at m=1, exact factorization
over disconnected components, singleton versus double-edge moments, actual
physical influence rather than virtual read, clique attachment factor J,
positivity on every spectral atom, inclusion of empty in 1+Z_K, and feasibility
of every weight. Exact finite validation is recorded separately; the infinite
conclusions use the inequalities above. The new result has an author proof;
independent review remains pending. It is not Lean-checked.

The first unsupported line is existence of fixed, feasible, LOCALLY adaptive
weights and/or a whole-set dictionary on arbitrary physically overlapping
connected representations whose COMPLETE original expected cost is O(I).
Component separation does not solve interactions inside a connected graph.
Arbitrary signed-core source pricing also remains full-FEI strength, as A007
shows. Global feasible scaling is now disproved as a universal replacement;
no inference strips auxiliary influence from the previous padded theorem.
