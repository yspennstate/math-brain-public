SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T01:15:42Z.
attacking: the near-rank-one / genuine-rank-two overlap-one collar by testing whether the newest three-group triangle Plancherel receiver is stable under a second crossing direction, and then identifying the exact anchored determinant currency that survives the obstruction.

# account02/B03 — second-crossing instability and the exact rank-two anchored-volume identity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: decoupled time integral  
Classification: **NEW INTERMEDIATE-MECHANISM COUNTEREXAMPLE / NEW RANK-TWO ANCHORED IDENTITY / TARGET-VALID PINNED-THEOREM APPLICATION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN, and unrestricted continuity remains OPEN. This report does not use post-rotation independence, law-uniform pointwise stationary phase, an arbitrary-joint coarea theorem, a conditional cap for a conjugate sum/difference variable, or deletion of a small nonzero quadratic term.

## 1. Exact source boundary

The newest completed designated partner result at source refresh is account03/B03 r43, final scope supplement

`yspennstate/math-open-problems@f3198cfe9b2f5f88659958c714b1ea0f7dfa29c9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260923T235705Z-account03-B03-QFORM-r43/REPORT.md`.

Its proved `QFORM-THREE-GROUP-TRIANGLE-PLANCHEREL-v1` considers three genuinely independent source groups: a scalar `Z` with density cap `M0`, and two banks with two-dimensional projections `Y=(Y1,Y2)`, `W=(W1,W2)` having joint density caps `MR,MC`. Arbitrary same-bank phases are allowed. For

`T=F0(Z)+FR+FC+2 sigma Y1 W1
   +2Z(gamma Y1+alpha Y2+delta0 W1+beta W2)`

it proves, with

`K=pi^(3/2) M0 (MR MC)^(1/2)|sigma alpha beta|^(-1/2)`,

`|phi_T(t)|<=min(1,K|t|^(-3/2))`,

`||p_T||_infinity<=3 M0^(2/3)(MR MC)^(1/3)|sigma alpha beta|^(-1/3)`,

and

`int |t|^(-1/2)|phi_T(t)|^2 dt <= (24/5)K^(1/3)`.

The r43 scope supplement is important: an older partner's advertised unweighted two-square L2 compiler is false; only its elementary collision inequality survives. None of that false compiler is used here.

The required pinned Claude/Fourier package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

In particular, `COUNTEREXAMPLE_SEARCH.md` proves localized Theorem A: if an actual physical principal `3 x 3` block has all eigenvalues of modulus at least `c`, conditioning on the other original coordinates gives

`||p_Q||_infinity <= 6 sqrt(pi)/c`,

uniformly in the induced affine terms. The pinned Theorem D/D5 crossing receivers require nonzero disjoint third/fifth crossing volume. Both facts are applied below to an actual target-valid family.

The newest operator-overlap structural funnel also identifies the live overlap-one packet: an actual physical hub and disjoint banks can carry anchored third-volume at least `1/2304`; the exact-rank-one light-crossing endpoint is paid by r43. The first remaining analytic collar is genuine rank two / near rank one.

## 2. Main obstruction — `QFORM-TRIANGLE-SECOND-CROSSING-INSTABILITY-v1`

Fix `0<epsilon<=1/4`. Let

`Z,Y1,Y2,W1,W2`

be five independent `Uniform[-1/2,1/2]` random variables. Thus the scalar density cap is one and each planar bank `(Y1,Y2)`, `(W1,W2)` has joint density cap one.

Define the same-bank phases

`F0(Z)=-epsilon^(-1) Z^2`,
`FR(Y)=Y1^2-epsilon Y2^2`,
`FC(W)=W1^2-epsilon W2^2`.

First delete the second light crossing and put

`R_epsilon = F0+FR+FC +2Y1W1-2ZY2-2ZW2`.                         (2.1)

This is exactly the newest account03/B03 triangle theorem with

`M0=MR=MC=1`, `sigma=1`, `alpha=beta=-1`.

Therefore the designated partner gives the actual inequalities

`boxed: ||p_(R_epsilon)||_infinity <=3`,                           (2.2)

`boxed: int_R |t|^(-1/2)|phi_(R_epsilon)(t)|^2 dt
       <=(24/5)sqrt(pi)=8.5077784843...`,                          (2.3)

and, for an independent whole copy,

`boxed: E|R_epsilon-R_epsilon'|^(-1/2)
       <=24/(5sqrt(2))=3.3941125497... .`                          (2.4)

Now add the arbitrarily small second crossing

`-2 epsilon Y2W2`.

The result is

`T_epsilon
 =R_epsilon-2epsilon Y2W2
 =(Y1+W1)^2
  -(sqrt(epsilon)(Y2+W2)+epsilon^(-1/2)Z)^2.`                    (2.5)

Thus a coefficient of size `epsilon` completes the entire negative three-variable block to one square. The original triangle product `|sigma alpha beta|` remains exactly one.

### The output density is unbounded for every epsilon>0

Put

`U=Y1+W1`,
`V=sqrt(epsilon)(Y2+W2)+epsilon^(-1/2)Z`.

The source coordinates used by `U` and `V` are disjoint, so `U,V` are genuinely independent. The triangular density of `U` is

`f_U(u)=1-|u|`, `|u|<=1`,

hence `f_U(u)>=1/2` for `|u|<=1/2`.

The density of `epsilon^(-1/2)Z` equals `sqrt(epsilon)` on

`[-1/(2sqrt(epsilon)),1/(2sqrt(epsilon))]`.

The other summand `sqrt(epsilon)(Y2+W2)` is supported on `[-sqrt(epsilon),sqrt(epsilon)]`. Since `epsilon<=1/4`, convolution therefore gives

`f_V(v)=sqrt(epsilon)`                                             (2.6)

through a nontrivial interval around zero.

Let `g_U,g_V` denote the densities of `U^2,V^2`. For sufficiently small `s>0`, symmetry and the square change of variables give

`g_U(s)=f_U(sqrt(s))/sqrt(s) >= 1/(2sqrt(s))`,
`g_V(s)=f_V(sqrt(s))/sqrt(s) = sqrt(epsilon)/sqrt(s)`.            (2.7)

For `q>0` sufficiently small, the density of `T_epsilon=U^2-V^2` is

`p_(T_epsilon)(q)=int_0^infinity g_U(q+v)g_V(v)dv`.

On `v in [q,s0]`, with fixed small `s0`, one has `q+v<=2v`, so (2.7) yields

`p_(T_epsilon)(q)
 >= [sqrt(epsilon)/(2sqrt(2))] int_q^s0 dv/v
 = [sqrt(epsilon)/(2sqrt(2))] log(s0/q).`                          (2.8)

Consequently

`boxed: ess sup p_(T_epsilon)=infinity for every epsilon>0.`      (2.9)

This refutes the following tempting interpolation principle:

> the r43 triangle theorem remains a bounded-density theorem after adding an arbitrary second crossing `2 tau Y2W2`, perhaps with a constant that deteriorates as `tau->0`.

It is false even when `|tau|=epsilon` is arbitrarily small and the r43 triangle currency `|sigma alpha beta|` stays exactly one. The failure is algebraic rank completion, not a probabilistic approximation issue.

This does **not** refute QFORM: the matrix of `T_epsilon` has only two nonzero eigenvalues,

`2` and `-(epsilon^(-1)+2epsilon)`.

### The assigned weighted whole-copy integral can still be finite

The obstruction also shows why the B03 weighted collision quantity cannot by itself be promoted to a one-copy density bound. Since `f_U<=1`, `f_V<=sqrt(epsilon)` and both have compact support,

`g_U(s)<=s^(-1/2)`, `g_V(s)<=sqrt(epsilon)s^(-1/2)`

on their positive supports. Hence the difference density satisfies a logarithmic upper bound

`p_(T_epsilon)(q) <= C_epsilon(1+|log|q||)`                       (2.10)

near zero and is compactly supported. Therefore `p_(T_epsilon) in L^2` despite (2.9). Plancherel then gives

`int |phi_(T_epsilon)(t)|^2dt=2pi||p_(T_epsilon)||_2^2<infinity`,

and consequently

`int |t|^(-1/2)|phi_(T_epsilon)(t)|^2dt<infinity`.                (2.11)

So finite dependence-safe whole-copy half-Riesz/time energy is strictly weaker than the required one-copy `L^infinity` conclusion, already for a five-coordinate product-law quadratic form.

## 3. Exact rank-two anchored-volume identity

The obstruction explains *why* a second crossing cannot simply be ignored. The live overlap-one packet carries additional anchored determinant information, and at exact rank two that information has a clean invariant formula.

Let the anchored block be

`M=[[b,r^T],[c,N]]`,                                               (3.1)

where the hub is physical and the residual row/column banks are disjoint. Suppose `rank N=2`, with SVD

`N=s1 u1 v1^T+s2 u2 v2^T`, `s1,s2>0`.

Decompose

`c=c1u1+c2u2+c_perp`,
`r=r1v1+r2v2+r_perp`,                                             (3.2)

with the perpendicular pieces orthogonal to the two singular planes. Define the anchored third-volume

`J_sep=sum_(|P|=|Q|=2) det M[{hub} union P,{hub} union Q]^2`.     (3.3)

Because this is the squared Hilbert norm of the anchored compound tensor, orthogonal changes of basis inside the two residual banks do not change it. Compute in the SVD basis. The only nonzero anchored minors are the aligned `2 x 2` singular-plane minor and six families containing one perpendicular row and/or column. Summing their squares gives the exact identity

`boxed:
J_sep = tau^2
 + ||r_perp||^2 (s1^2 c2^2+s2^2 c1^2)
 + ||c_perp||^2 (s1^2 r2^2+s2^2 r1^2)
 + (s1^2+s2^2)||c_perp||^2||r_perp||^2,`                         (3.4)

where

`tau=b s1 s2-s2 r1 c1-s1 r2 c2
    =s1 s2 [b-r^T N^+ c]`.                                       (3.5)

Here `N^+` is the Moore-Penrose inverse on the rank-two singular planes.

For reference, the individual SVD-basis minors are

`tau`,
`-s1 c2 (r_perp)_q`, `s2 c1 (r_perp)_q`,
`-s1 r2 (c_perp)_p`, `s2 r1 (c_perp)_p`,
`-s1(c_perp)_p(r_perp)_q`, `-s2(c_perp)_p(r_perp)_q`.

There are no cross terms because they occupy distinct compound coordinates. This proves (3.4).

For the instability family (2.5), the residual crossing is

`N=diag(1,-epsilon)`,

`c=r=(0,-1)`, `b=-epsilon^(-1)`, so `c_perp=r_perp=0` and

`tau=(-epsilon^(-1))(1)(-epsilon)-1=0`.                            (3.6)

Thus the added small second crossing does not merely perturb the r43 endpoint: it exactly cancels the anchored third-volume. This is why the family is not itself in the live `J_sep>=1/2304` packet.

Equation (3.4) sharpens the genuine remaining obligation. In the rank-two overlap-one collar, a proof may use the live anchored volume; it cannot use the r43 triangle product alone.

## 4. Target-valid augmentation and required pinned-source application

Add a sixth independent cap-one coordinate `S~Uniform[-1/2,1/2]` and define

`Q_epsilon=T_epsilon+S^2`.                                        (4.1)

Its matrix is the orthogonal-support sum

`aa^T-bb^T+e_S e_S^T`,

where `a` represents `Y1+W1` and `b` represents
`sqrt(epsilon)(Y2+W2)+epsilon^(-1/2)Z`. Therefore its nonzero spectrum is exactly

`boxed: {2, 1, -(epsilon^(-1)+2epsilon)}.`                        (4.2)

Hence `Q_epsilon` is in the exact owner target for every `epsilon>0`.

Now apply a completed result from the required pinned `e5f71d79...` package to an actual inequality. The physical principal triple `(Y1,Z,S)` has quadratic block

`diag(1,-epsilon^(-1),1)`.                                        (4.3)

For `0<epsilon<=1/4`, all three eigenvalues of (4.3) have modulus at least one. Pinned `COUNTEREXAMPLE_SEARCH.md`, Theorem A, conditioned on every other original coordinate, therefore gives

`boxed: ||p_(Q_epsilon)||_infinity <=6sqrt(pi)
       =10.6347231054... .`                                       (4.4)

Consequently every interval `I` satisfies the actual linear small-ball inequality

`boxed: P(Q_epsilon in I) <=6sqrt(pi)|I|.`                         (4.5)

This is a source-valid target family: the third curvature cannot be deleted, but once it is kept as an actual physical resource the localized pinned theorem pays the form uniformly.

The same family is an obstruction to relying only on the pinned disjoint-crossing receivers. For disjoint physical index sets `I,J`, the isolated `S^2` term contributes nothing to `A[I,J]`, while the remaining matrix is the difference of two rank-one matrices. Hence

`rank A[I,J] <=2`                                                  (4.6)

for **every** disjoint physical cut. Therefore every pinned third- and fifth-crossing volume satisfies

`Z_3(A[I,J])=Z_5(A[I,J])=0`.                                      (4.7)

So Theorem D, D', and D5 are all silent on this target-valid family, while pinned localized Theorem A gives (4.4). This is an actual obstruction to any proof architecture that insists on a disjoint rank-three crossing before looking for overlap/local curvature.

From (4.4), the whole-copy difference also has density cap at most `6sqrt(pi)`. The elementary layer-cake bound for a density cap `M`,

`sup_s E|X-s|^(-1/2)<=2sqrt(2M)`,

therefore yields the assignment-compatible estimate

`boxed:
 int |t|^(-1/2)|phi_(Q_epsilon)(t)|^2dt
 <=4sqrt(6) pi^(3/4)
 =23.1205425476... .`                                              (4.8)

Again the identity is used only for the whole scalar copy difference.

## 5. What changed in the proof map

The newest r43 exact-rank-one endpoint is genuinely sharp with respect to its *interaction graph*: one cannot add even an arbitrarily small second crossing and hope to retain a theorem controlled only by `|sigma alpha beta|` when same-bank phases are arbitrary. The counterexample (2.5) completes a rank-two opposite-sign form and produces a logarithmic density singularity.

At the same time, the live overlap-one structural packet has `J_sep>=1/2304`, so the exact collapse (3.6) is excluded there. The correct next invariant is therefore the whole anchored volume, not the rank-one triangle product.

For exact rank-two light crossing, (3.4) separates the debt into:

1. the aligned Schur-determinant channel `tau^2`;
2. two one-sided mixed channels involving one perpendicular hub star and one aligned star;
3. the doubly transverse channel.

The doubly transverse exact-rank-one limit is the newest partner theorem. Large disjoint rank-three volumes already pay part of the one-sided geometry. What remains after those exits is an **anchored rank-two noncollapse theorem** that must use `J_sep` itself while retaining the actual third curvature.

A precise next statement is:

`QFORM-ANCHORED-RANK2-JSEP-RECEIVER-v1` (OPEN): in the overlap-one physical packet with independent cap-one original inputs, `rank N<=2` and anchored volume `J_sep>0`, prove a universal bound of the natural scale `C J_sep^(-1/6)` (or another universal scale sufficient at `J_sep>=1/2304`), allowing arbitrary same-bank quadratic curvature and aligned hub-star components, without post-rotation independence.

The present obstruction proves that any proof of this statement must use the noncollapse information `J_sep>0`; a perturbative continuation of the rank-one triangle theorem is impossible. In particular, if all transverse terms in (3.4) are already routed away, the first unpaid scalar is the aligned Schur quantity

`|tau|=|s1s2[b-r^T N^+c]|`,                                      (5.1)

which is invisible to a disjoint crossing theorem but exactly measures distance from the rank-two collapse exhibited in Section 2.

## 6. Status

- full QFORM bounded-density conjecture: **OPEN**;
- unrestricted continuity: **OPEN**;
- r43 triangle theorem: consumed at equations (2.2)-(2.4), not modified;
- `QFORM-TRIANGLE-SECOND-CROSSING-INSTABILITY-v1`: **proved here**;
- exact rank-two anchored-volume identity (3.4): **proved here**;
- target-valid augmented family: **paid uniformly** by pinned e5f localized Theorem A, (4.4)-(4.5);
- pinned D/D'/D5 obstruction on the same family: **exact**, all disjoint cross ranks are at most two;
- next unpaid implication: `QFORM-ANCHORED-RANK2-JSEP-RECEIVER-v1`.

No counterexample to the original conjecture is produced.
