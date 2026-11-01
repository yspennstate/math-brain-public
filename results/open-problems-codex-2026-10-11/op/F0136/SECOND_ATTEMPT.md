# Second serious attempt at F0136 — 2026-10-11

## Gap reread and two approaches not pursued in the first attempt

The first attempt established local integrability and quoted the conditional regeneration theorem, but did not establish a spatial ballisticity condition or finite mean regeneration duration from nonzero drift alone. The conjecture remains: every positive planar Dirichlet parameter vector with d_alpha != 0 and kappa > 1 has nonzero limiting velocity.

**Approach A: compute the actual Kalikow auxiliary kernel, rather than apply the coarse sufficient drift inequality.** Kalikow's condition implies the spatial condition used by the conditional regeneration theorem. Its kernel is weighted by occupation, so it may retain information lost in the inequality sum of absolute drift parameters > 1. Compute this kernel exactly on minimal domains, then try to prove its projected drift positive on arbitrary domains whenever kappa > 1 and d_alpha != 0. A negative auxiliary drift on a legitimate domain would disprove this proposed route, though not the ballisticity conjecture itself.

**Approach B: a range-versus-clock reduction using a polynomial tail for the first regeneration range.** Instead of seeking (T)_gamma (a stretched exponential spatial estimate), decompose the first regeneration time according to its range and combine finite-domain exit-time moments with Holder's inequality. This could show that a sufficiently high polynomial spatial moment is enough. The hard points are uniform growth of finite-box clock moments and dependence between the random range and the clock. Neither can be discarded. This is a different global reduction from the first attempt and a possible weaker replacement for (T)_gamma, but it currently has two unresolved inputs.

Approach A is pursued first because it directly targets a known sufficient spatial criterion, yields exact quantities on finite domains, and can be falsified without relying on long-time simulation.

## Read-only brain query

Requested `math_recall.py` on “Kalikow auxiliary random walk Dirichlet regeneration integrability T gamma”, explicitly targeting the missing global estimate and the named criterion. Results are hints, not proof. The returned cards and any useful follow-up will be recorded below.

Completed that query and a second on “Kalikow condition occupation Green function Dirichlet integration by parts Tournier”. Complete results are saved in `brain_gap_recall.txt` and `brain_kalikow_recall.txt`. The first returned generic random-walk/Kesten cards and unrelated material; the second returned symmetric Hunt-process Green kernels, Dirichlet forms, and Gaussian integration by parts. None supplies the missing nonreversible planar Dirichlet regeneration estimate. In particular, a symmetric Dirichlet-form theorem cannot be applied just because “Dirichlet” appears in the model name. No brain card was used as a proof input.

## A1. Exact auxiliary kernel on a two-site domain

For a finite connected domain U containing the starting point 0, write

G_U(0,x)=E_0^omega[sum_(n<tau_U) 1_{X_n=x}].

The (annealed) Kalikow auxiliary kernel at x is

hat_omega_U(x,e_i) = E[G_U(0,x) omega(x,x+e_i)] / E[G_U(0,x)].

Outgoing transitions to vertices outside U are included; they lead to the cemetery state of the killed auxiliary chain. Kalikow's condition in direction ell requires a uniformly strictly positive projected drift for this kernel over finite connected U and x in U. The standard condition is sufficient for (T), but is not known to be necessary for ballisticity.

The kernel definition is checked directly against Tournier, arXiv:0801.2875, PDF p.14, Section 4; its formula includes all nearest-neighbour outgoing edges and exactly the Green occupation weighting used here. The connected-domain convention is also checked against Enriquez–Sabot, arXiv:math/0503713, Section 4, PDF pp.4–5.

Take U_-={0,-e_1}, alpha=(a,c,b,c), a>b>0 and c>0, A=a+b+2c. Put p=omega(0,-e_1), q=omega(-e_1,0). Then p~Beta(b,A-b) and q~Beta(a,A-a) independently, and

G_U_-(0,0)=1/(1-pq).

Suppose kappa_1=2A-a-b>1; this ensures M=E[1/(1-pq)]<infinity by the pair-integrability proof in ATTEMPT.md Section 2. Write (z)_0=1 and (z)_n=z(z+1)...(z+n-1) for n>=1. Define c_n=E[p^n]E[q^n]=(b)_n(a)_n/(A)_n^2. Tonelli gives M=sum_(n>=0)c_n.

The origin's eastward auxiliary drift has numerator

K_- = E[(omega(0,e_1)-p)/(1-pq)].

Dirichlet moments give, for every nonnegative integer n,

E[omega(0,e_1)p^n] = a E[p^n]/(A+n),
E[p^(n+1)] = (b+n) E[p^n]/(A+n).

These identities follow directly by multiplying the Dirichlet density by the monomial, adding one to the parameter of the east coordinate or n to that of the west coordinate, and taking the ratio of normalizing constants. In particular they do NOT assert independence of coordinates in one row.

Independence of the rows at 0 and -e_1 now yields

K_- = sum_(n>=0) c_n (a-b-n)/(A+n).

Subtraction is legitimate: each of the two nonnegative series being subtracted is bounded by M, hence finite. More directly, each summand in absolute value is at most c_n, since |a-b-n|<=A+n. The series is absolutely convergent.

The transverse auxiliary drift is exactly zero. Indeed, interchanging the north and south outgoing coordinates at 0 preserves the Dirichlet law, leaves p and the denominator unchanged, and negates their difference. Integrability is bounded by M.

## A2. A rigorous counterexample to the proposed Kalikow reduction

Let Delta=a-b lie in (0,1). The n=0 and n=1 terms sum to

S_1 = Delta/A + (ab/A^2)(Delta-1)/(A+1).

All terms with n>=1 are strictly negative. Consequently, whenever

Delta A(A+1) < ab(1-Delta),

we have K_- <= S_1 < 0. This requires no numerical approximation and no tail bound. The positivity of M then gives hat_d_U_-(0) dot e_1 = K_-/M < 0.

For the explicit planar parameter vector

alpha=(10,4,9,4)/32,

we have A=27/32, Delta=1/32, s_1=19/32, s_2=8/32, and kappa=35/32>1. Thus the original walk has strictly positive eastward mean drift and satisfies the exact hypotheses of F0136. Nonetheless,

S_1 = 1/27 - 310/4779 = -133/4779 < 0.

Therefore Kalikow's condition fails in every direction ell with d_alpha dot ell>0. In fact it fails in every nonzero direction. To see this without depending on whether singleton domains are allowed, take U_+={0,e_1}. Now p is the east probability with parameter a, and q the west probability in the neighbouring row with parameter b. The same computation gives

K_+ = sum_(n>=0) c_n (a-b+n)/(A+n) > 0,

with finite strictly positive normalizer M and zero transverse component. Directions with ell_1>0 fail on U_-, directions with ell_1<0 fail on U_+, and directions with ell_1=0 give zero projected auxiliary drift on either pair and cannot have a strictly positive lower bound. These two domains are finite, connected, contain 0, and their origin is an admissible test site.

This is a counterexample to **Kalikow's condition following from the hypotheses of F0136**, not a counterexample to ballisticity. A negative auxiliary drift on one domain does not imply zero velocity. It rules out the attempted route of sharpening the known drift inequality until Kalikow covers the entire conjectured regime.

## A3. The obstruction persists for arbitrarily small positive drift

Keep b=9/32, c=4/32, and take a=b+epsilon, with 0<epsilon<=1/32. Then A=13/16+epsilon, kappa=17/16+epsilon>1, and d_alpha=(epsilon,0). For the sign inequality above,

epsilon A(A+1) <= (1/32)(27/32)(59/32) = 1593/32768,

whereas

ab(1-epsilon) >= (9/32)^2(31/32) = 2511/32768.

Every factor used in these inequalities is positive, so multiplying their bounds preserves the indicated inequalities. Since 1593<2511, the sufficient sign inequality holds strictly for this whole family. Each of these parameter vectors therefore fails Kalikow's condition in all directions, despite kappa>1 and arbitrarily small nonzero drift.

More generally, for any fixed b,c>0 with 2(a+b+2c)-max(a+b,2c)>1 at a=b, the displayed sign inequality holds for all sufficiently small positive Delta=a-b, by continuity: its left side tends to zero and its right side tends to b^2>0. This last continuity statement adds no ballisticity assertion.

## Further exact calculation for Approach A

Before closing this route, one boundary case admits a complete closed form, rather than only a signed-series bound.

## A4. Exact closed form at total concentration A=1

Let alpha=(a,c,b,c), with a>b>0, s=a+b<1 and c=(1-s)/2, so A=1. On U_-={0,-e1}, p~Beta(b,1-b) and q~Beta(a,1-a) independently. For every 0<=p<1,

E_q[1/(1-pq)] = sum_(n>=0) p^n E[q^n]
                     = sum_(n>=0) (a)_n p^n/n!
                     = (1-p)^(-a).

The first equality is Tonelli. The second is the beta-moment identity. For completeness, the third is the binomial power-series identity: the ratio of successive coefficients is (a+n)/(n+1), so the series S has radius of convergence one. Termwise differentiation on compact subintervals of [0,1) gives (1-p)S'(p)=aS(p), S(0)=1. The unique solution of this scalar differential equation is (1-p)^(-a). Thus the identity applies at every p in the support of the beta law.

Consequently,

M = E_p[(1-p)^(-a)]
  = B(b,1-a-b)/B(b,1-b)
  = Gamma(1-a-b)/(Gamma(1-a)Gamma(1-b)),

which is finite and positive because a,b>0 and 1-a-b>0. Similarly,

V = E[p/(1-pq)]
  = E_p[p(1-p)^(-a)]
  = B(b+1,1-a-b)/B(b,1-b)
  = b M/(1-a).

These beta-integral evaluations follow by inserting the beta density and using Gamma(z+1)=z Gamma(z). No numerical continuation or unproved hypergeometric identity is required.

The east coordinate at the origin, conditional on p, has mean a(1-p)/(1-b), by the conditional Dirichlet law of the other three coordinates. This also follows from the joint-moment identities above, summed absolutely. Hence its weighted mean is W=a(M-V)/(1-b). Subtracting the west weighted mean V and dividing by M gives the **exact normalized auxiliary drift**

hat_d_U_-(0) dot e1 = [(a-b)(1-a-b)-ab]/[(1-a)(1-b)].

Repeating the calculation on U_+ gives

hat_d_U_+(0) dot e1 = [(a-b)(1-a-b)+ab]/[(1-a)(1-b)].

Both transverse components vanish, as before. Therefore every such parameter vector with (a-b)(1-a-b)<ab fails Kalikow's condition in all directions.

For the particularly simple example

alpha=(12,5,10,5)/32=(3/8,5/32,5/16,5/32),

we have A=1, d_alpha=(1/16,0), kappa=21/16>1, and the two auxiliary drift vectors at the origin are exactly

hat_d_U_-(0)=(-5/22,0),    hat_d_U_+(0)=(7/22,0).

The whole auxiliary probability vectors are explicit as well. The table uses direction order (+e1,+e2,-e1,-e2); all rows sum to one.

| Law at the origin | +e1 | +e2 | -e1 | -e2 | Eastward drift |
| --- | --- | --- | --- | --- | --- |
| Static mean row | 3/8 | 5/32 | 5/16 | 5/32 | 1/16 |
| Auxiliary row for U_- | 3/11 | 5/44 | 1/2 | 5/44 | -5/22 |
| Auxiliary row for U_+ | 6/11 | 5/44 | 5/22 | 5/44 | 7/22 |

For example, on U_- the weighted west probability is V/M=b/(1-a)=1/2. Each other coordinate j has weighted mean alpha_j(M-V)/((1-b)M), by the same conditional Dirichlet calculation; this gives the displayed east, north and south probabilities. The U_+ row follows with east and west interchanged in that computation. Thus the negative auxiliary drift is a valid stochastic row, not a sign computation detached from a Markov kernel.

This is an explicit boundary case where the classical integration-by-parts drift bounds involving division by A-1 cannot be used, but the actual auxiliary kernel is well defined. It strengthens the route obstruction to exact normalized values. The original positive-speed question remains unproved.

The left-pair sign can be classified explicitly at fixed horizontal mass s. Writing Delta=a-b>0 and ab=(s^2-Delta^2)/4, its numerator is negative exactly when

Delta < sqrt(4(1-s)^2+s^2)-2(1-s).

This follows by solving the quadratic Delta^2+4(1-s)Delta-s^2<0; the other root is negative, and the denominator of the auxiliary drift is positive. At equality the left-pair drift is zero and the strict Kalikow condition still fails. The positive root lies below s, because the quadratic at Delta=s is 4s(1-s)>0, so all these boundary examples have positive a,b. This is a necessary two-site test for Kalikow's condition, not a sufficient criterion when the test is passed. All these A=1 vectors have kappa=1+min(s,1-s)>1.

There is also a rigorous control showing why this obstruction must not be called non-ballisticity. In dimension three, take parameters in direction order (+e1,+e2,+e3,-e1,-e2,-e3)

alpha^(3)=(24,5,5,20,5,5)/64.

They have A=1, d_alpha=(1/16,0,0), and kappa=21/16. The two-site computations above depend only on a=3/8, b=5/16 and total A, so the two auxiliary drift vectors are (-5/22,0,0) and (7/22,0,0); the transverse components vanish by paired-parameter symmetry. Thus this vector also fails Kalikow's condition in all directions. Nevertheless it is ballistic by the overview's Theorem 5(i), since d=3, d_alpha!=0 and kappa>1. This is an application of a known theorem in a different dimension, not a solution of F0136.

## Referee checklist for the auxiliary-kernel computations

1. Normalization exists: kappa_1>1 is checked exactly, so M is finite, and M>=1.
2. Correct weighting: the numerator uses occupation from 0, not an unweighted mean environment. At x=0 in either pair, it is exactly 1/(1-pq).
3. Parameter orientation: for U_-, p has parameter b (west), q has parameter a (east). U_+ reverses these roles.
4. Dependence within one row is handled by Dirichlet joint moments. Only the two distinct rows are independent.
5. Infinite sums: both positive-coordinate series are finite; the signed series is absolutely convergent. Its negative tail strengthens, rather than weakens, the negative prefix.
6. North/south cancellation is an exact symmetry with equal parameters, not an approximation.
7. Domains and test sites satisfy the standard finite-domain Kalikow definition. This establishes failure of that sufficient condition, not failure of (T) or of positive speed.
8. The original positive drift and kappa threshold are recomputed independently of the auxiliary kernel.

Exact rational prefix checks are saved in `kalikow_probe.json`. A Lean certificate for the finite arithmetic and sign steps will be recorded separately; the probabilistic identities are proved above, not delegated to Lean.

## B1. A weaker global sufficient criterion, with the dependence handled explicitly

Although Approach A has been ruled out as a universal route, the range-versus-clock approach can be reduced to a precise summability condition. This is a conditional reduction, not a proof of its needed hypotheses.

Let tau be the first directional regeneration time, known to be finite almost surely under directional transience. Set M_range=max_(0<=n<=tau)||X_n||_infinity, and let T_R be first exit from the deterministic box B_R={x:||x||_infinity<=R}. For p>1 define C_p(R)=(E[T_R^p])^(1/p). On {M_range<=R}, every path point through time tau is in B_R, hence tau<T_R. This implication is pathwise and does not assume tau is a stopping time.

Partition into A_0={M_range<=1} and A_k={2^(k-1)<M_range<=2^k}, k>=1. Since tau and M_range are finite almost surely, these events cover the path space up to a null set. Monotone summation and Holder's inequality give

E[tau] <= C_p(1) + sum_(k>=1) C_p(2^k) P(M_range>2^(k-1))^(1-1/p).

The event depends on the same environment and trajectory as T_R. Holder is precisely what accounts for that dependence; multiplying their separate expectations would not be justified.

Therefore the displayed series being finite is sufficient for finite mean regeneration duration and, by the renewal argument in ATTEMPT.md Section 4, nonzero speed. In particular, if for some 1<p<kappa, some q>=0 and some beta>0,

C_p(R)<=C R^q,   P(M_range>R)<=C' R^(-beta),

and beta(1-1/p)>q, then the series converges geometrically. This requires only a sufficiently high polynomial spatial tail, rather than a stretched exponential one, **provided the polynomial clock-moment bound is established**.

## B2. Each finite-box clock moment exists; uniform growth remains unproved

For every deterministic finite connected U and every 1<p<kappa, E[T_U^p]<infinity follows from the published killed-Green-function theorem, as follows. This is stronger than the first attempt's finite-mean statement but still not a uniform estimate in U.

For fixed omega set m_omega=max_(x in U) E_x^omega[T_U]. Here is a direct proof that this is finite. From each x choose a simple path through U exiting the domain in at most N=|U| steps. Each such path has positive quenched probability, and the minimum eta of those finitely many probabilities is positive. The Markov property gives P_x^omega(T_U>jN)<=(1-eta)^j, so E_x^omega[T_U]<=N/eta. Thus m_omega is finite and m_omega>=1. Let L=ceil(2m_omega). Markov's inequality gives P_x^omega(T_U>L)<=1/2 for every x in U. The Markov property at deterministic times jL then gives P_x^omega(T_U>jL)<=2^(-j). Consequently

E_x^omega[T_U^p] <= L^p sum_(j>=0)(j+1)^p 2^(-j)
                      <= H_p m_omega^p,

where H_p=3^p sum_(j>=0)(j+1)^p2^(-j)<infinity, since L<=2m_omega+1<=3m_omega.

The Green comparison from ATTEMPT.md Section 3 gives m_omega<=sum_(y in U) G_U^omega(y,y). For p>=1, convexity gives

m_omega^p <= |U|^(p-1) sum_(y in U) G_U^omega(y,y)^p.

The overview's Proposition 1 (PDF p.11), translated to y, ensures every annealed term on the right is finite for p<kappa. Taking environment expectations proves the claimed finite p-th clock moment. Singleton U is again trivial. No quantitative size dependence of those Green moments has been established here.

## B3. Why this second reduction still does not close F0136

There are two independent missing inputs: polynomial growth of C_p(R), and a polynomial range tail of sufficiently high order. The first attempt had neither, and the present argument proves neither. Almost-sure finiteness of M_range and finiteness of C_p(R) for each individual R cannot imply convergence of the dyadic sum.

For a bare scalar illustration, take integer M>=1 with P(M>=n)=1/n and set tau=M^2 and T_R=R^2+1. Then tau<T_R on {M<=R}, all deterministic T_R have every moment finite, and M is finite almost surely, but E[tau]=infinity. This is not a random-walk or Dirichlet counterexample; it verifies the logical insufficiency of the two finiteness assertions alone.

## Outcome of the additional attempt

Rereading Tournier's 2008 preprint, PDF p.16, also exposed a historical finite-time counterexample-search candidate: alpha=(0.5,0.1,0.2,0.1) in the direction order used here. It has kappa=1.1 and positive drift, and the preprint reports apparent sublinear displacement while explicitly saying no such regime was proved. A bounded probe of this exact vector is implemented in `probe_walk.py`: twenty independent lazy quenched environments, twenty thousand steps each, with three checkpoints. Rows are sampled as normalized independent gamma variables once per visited site and retained on revisits. This uses well below 1 GB of memory, and can only supply finite-time observations; it cannot determine the limiting velocity. The numerical result is recorded separately after the job returns.

The completed two-dimensional probe had average x-displacements 134.55, 483.25 and 825.2 at times 2000, 10000 and 20000; the corresponding ratios to time were 0.067275, 0.048325 and 0.04126. The effective exponent between the first and last mean was 0.78768. Runtime was about 0.61 seconds.

To check that declining finite-time ratios are not a reliable zero-speed certificate, a separate control used d=3 and alpha=(0.5,0.05,0.05,0.2,0.05,0.05), with the same A=0.9, d_alpha=0.3e1 and kappa=1.1. The overview's Theorem 5(i) proves this model ballistic. Yet twenty independent paths of twenty thousand steps gave mean x-displacements 167.1, 687.55 and 1210.85 at the same checkpoints, ratios 0.08355, 0.068755 and 0.0605425, and an effective exponent 0.86011. Runtime was about 1.08 seconds. Code, seeds, all checkpoints and observations are in `probe_ballistic_control.py` and `ballistic_control_probe.json`.

Both experiments are bounded finite-time observations. There is no proved ordering or coupling between the two dimensions. The three-dimensional control invalidates the proposed diagnostic of zero speed from the tested declining ratios; it does not prove positive speed in dimension two. No extrapolation or counterexample to F0136 is claimed.

New completed results: an explicit, fully analytic Dirichlet parameter family satisfying the F0136 hypotheses but failing Kalikow's condition in every direction; exact finite-pair auxiliary drift formulas; and the dyadic range/clock summability reduction with finite deterministic-domain p-th clock moments for 1<p<kappa. No novelty is claimed without a dedicated priority search.

The general positive-speed conjecture is still unproved here. The two-site obstruction eliminates one stronger sufficient route; the range/clock reduction identifies weaker quantitative estimates that could replace it, but leaves their derivation open. The honest verdict remains PARTIAL.

## Completed verification

KalikowObstruction.lean passed `lake env lean` from ~/lean_verify with exit code 0. It contains eight finite arithmetic/sign theorems, including the exact -133/4779 prefix and the normalized -5/22 and 7/22 values. No placeholders, added axioms or native_decide are present. The kernel checks algebra only; the Dirichlet and beta-integral identities are the full prose proofs above. The first run timed out; the next exposed the reserved identifier prefix, which was renamed. All receipts are retained.

The exact 100-point rational family probe and both finite-walk data sets passed their consistency checks. All new claims, including the distinction between a Kalikow counterexample and a counterexample to the target, are recorded in CLAIMS.jsonl. The final verdict is PARTIAL.
