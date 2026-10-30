# Anchored packing inequalities for the same complete posterior family

Fix a finite gate table, positive rarities pi_e and positive global weights
lambda_e satisfying each nonnegative physical packing row
sum_e a_ve lambda_e <= b_v. Let

    D = product_e(1+pi_e lambda_e)-1 > 0,
    p(T) = product_(e in T)(pi_e lambda_e)/D, T nonempty.

The complete output coefficients K_AT sum ALL distinct actual finite partition
runs with used-gate set T, divided by pi_T. A used set is not itself a run.
In particular, different abstract descriptions of the same chronological event
must not be added twice. The already established identity is
Q_A = sum_T K_AT p(T). Its posterior entropy is retained: minimizing
E_eta[-ln q_r] - H_nats(eta) over actual runs giving A is -ln Q_A,
with minimizer eta(r)=q_r/Q_A. This follows by subtracting -ln Q_A
to leave KL(eta || q/Q_A), which is nonnegative. Everything below uses this
same family and its complete coefficients; no matching-only lower certificate
is transferred to a larger family.

## 1. A whole packing row becomes a linear cut

For EVERY nonempty anchor U and every row v,

    sum_(e not in U) (a_ve/pi_e) p(U union {e}) <= b_v p(U).       (1)

Indeed p(U union {e})=pi_e lambda_e p(U) for e outside U.
After substitution, (1) is p(U) sum_(e outside U) a_ve lambda_e
<= b_v p(U). The omitted terms are nonnegative. Positivity of D and
p(U) justifies the ratio, although the direct multiplied proof avoids division.
If U is disjoint from the nonzero entries of the row, its exact slack is
p(U)[b_v-sum_e a_ve lambda_e]. Thus on the physical multiplicative manifold
such an anchor detects precisely that complete row's packing failure.

For positive graph edges pi_e=1/4, a_ve=1[e contains v], b_v=1,
this is 4 sum_(e incident v, e outside U) p(U union {e}) <= p(U).
It applies to arbitrary degree and to the full event family. No symmetry,
Boolean spectral inequality or cost estimate is a premise.

The requirement U nonempty matters: replacing p(empty) by probability one
is false already for a single gate, whose conditioned p({e}) equals one.
One may adjoin p(empty)=1/D as an auxiliary unnormalized coordinate, but
it is not an entry of the normalized nonempty root law. Nor does existence
of the cuts make an arbitrary simplex point multiplicative.

## 2. Every pair cone has conditional lifts

For two incident graph gates i,j and every U disjoint from {i,j}, including
U empty, write a=p(U union {i}), b=p(U union {j}), c=p(U union {i,j}).
There is a positive common multiplier z with
a=z lambda_i/4, b=z lambda_j/4, c=z lambda_i lambda_j/16.
Consequently lambda_i+lambda_j<=1 implies ab>=4c(a+b), or

    [[a-4c,4c],[4c,b-4c]] is positive semidefinite.

For every rational t>=0 this gives the linear cut

    4(t+1)^2 c - t^2 a - b <= 0.                            (2)

The same positive-denominator calculation as the unanchored pair cone
proves it; U does not identify any witness or root component of a run.
This extends A010's pair constraints without changing its sufficiency scope:
two gates admit its exact characterization, larger tables do not.

## 3. Rational lower certificates for the all-weight variational infimum

At any physical reference p0 with Q_A>0 on every positive nonempty spectral
mass P(A), put v=sum_A P(A), h_T=sum_A P(A)K_AT/Q_A.
Then sum_T h_T p0(T)=v. In natural units,

    G(p)=-sum_A P(A) ln(sum_T K_AT p(T))
    G(p)>=G(p0)+v-sum_T h_T p(T).                           (3)

Let each retained cut be a_j dot p <= 0 and let positive caps u_T bound
every physical p(T). For ANY nonnegative RATIONAL multipliers y_j, set
s_T=h_T-sum_j y_j a_jT. The exact capped-simplex support function is

    B= min_theta [theta+sum_T u_T max(s_T-theta,0)].         (4)

It is obtained by filling the largest s_T coordinates to capacity until
total mass one. The last score is a valid theta; direct rational equality
between this fill and (4) checks the certificate. For any physical p,
h dot p <= s dot p <= B. Hence

    G(p0)+v-B <= inf_(physical lambda, all actual posteriors) G <= G(p0).

B>=v because p0 is feasible. The bit gap is at most 2(B-v), using ln2>1/2.
No claim is made that the relaxed law is a probability-generating code or
that this gap pays G(p0) itself. Taking the least of several certified Bs
is valid. The linear-program solver proposes y; only their exact rational
values and the exact support calculation are used in the proof.

## 4. Exact separation beyond all pair cones and all subset caps

Take the actual prime table with edges (0,1),(0,2),(0,3),(4,5).
Construct a multiplicative root law using proposed weights
(2/5,2/5,2/5,1/2), pi=1/4. Here D=3979/8000.
These weights violate the hub packing row (sum 6/5), so are inadmissible.
Nevertheless every incident pair has total weight 4/5, hence satisfies ALL
pair-PSD cuts, including every conditional lift and every real t>=0.
All fifteen sharp individual subset caps from A010 hold, as verified by
rational fractional-packing primal/vertex-dual equality and its cap formula.
With U={the disjoint edge}, (1) has left side minus right side
p(U)/5=200/3979>0. Thus the new row inequalities exclude a positive
multiplicative law satisfying the earlier pair cones and subset caps.
This is a relaxation falsifier for an actual prime table, not an admissible
Boolean Fourier law, an optimized-code obstruction or an FEI disproof.

## 5. Explicit complete-cost enclosures

cost.py computes the complete C0=sum_A P(A) log2(1/Q_A) independently of the
LP proposal. For 1<=y<=2 set t=(y-1)/(y+1), so 0<=t<=1/3. The first twenty
terms 2 sum_(j=0)^19 t^(2j+1)/(2j+1) bound ln(y) below, and the omitted tail
is at most 2t^41/[41(1-t^2)]. Normalize each positive rational argument as
2^k y with 1<=y<2 and divide the ln(y) interval by the positive ln(2)
interval. Outward dyadic rounding preserves both signs, also for negative k.
The computed C0 interval has width at most 2^-30 bits. If its endpoints are
Clo,Chi and ell is the certified lower ln(2) endpoint, then

    [Clo-(B-v)/ell, Chi]

contains the infimum over all feasible positive global weights and all
actual-run posteriors in this same family. This follows from (3), positivity
B-v>=0, and existence of the evaluated feasible reference. Final endpoints
are again rounded outward. All 67 exact gap certificates satisfy
2(B-v)<9I/10. This is a finite statement; no dimension-independent cost
payment is inferred from it.

## Scope and the first unpaid line

The finite census certifies stronger lower bounds for exactly its frozen full
families at a fixed evaluation reference, uniformly over every positive feasible
global weight vector and every actual-run posterior. It establishes neither
universal root-law realizability nor influence payment of the complete cost.
The first unsupported line remains C020/PI-J: select a single admissible
reference whose COMPLETE expected cost is <= K I for arbitrary Boolean prime
tables. On leafless shared incidence, cost and inherited scale terms still
need joint payment. An improved optimization gap alone cannot provide that.
