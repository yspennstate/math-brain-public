SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T04:13:29Z.
attacking: global exterior-minor overlap decomposition — convert disjoint spectral exterior mass into a literal physical E3 crossing, then isolate the overlap-heavy residue.

# fleet02/B03 — disjoint exterior mass exit

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW STRUCTURAL/ANALYTIC EXIT / LINEAR SMALL-BALL BRANCH / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains open. No moments, bounded support, connected support, Gaussianity, log-concavity, iid hypothesis, diagonal-basis assumption, or independence after rotating the input law is used below. Every cut is in the original physical coordinates. Continuity is stated only on branches whose cited receiver supplies it.

## 1. First unpaid implication

The newest fleet03/B03 r48 result pays every literal physical cross block `B=A[I,J]` with positive third exterior energy

`E3(B)=e_3(B^T B)`

by the marginal-free receiver

`||p_Q||_infinity <= C_E3 E3(B)^(-1/6)`,

`C_E3=8.4530212255281768747...`,

and also supplies a continuous `C_0` density on that branch. Its full report is `math-open-problems@3638467084deb8af24d1b01aa01cc300ee85ea8a`.

The unpaid step was therefore not analytic once a good physical E3 crossing exists; it was structural: how much of the three-large-eigenvalue hypothesis is visible to disjoint physical cross minors at all? The theorem below gives an exact answer in terms of overlap classes.

## 2. Exterior-overlap identity

For every real symmetric `n x n` matrix `A`, define

`mathcal E_r(A) = sum det(A[S,T])^2`,

where the sum is over ordered triples `S,T subset {1,...,n}`, `|S|=|T|=3`, with `|S intersect T|=r`, for `r=0,1,2,3`.

### Theorem 2.1 — `QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`

One has the exact deterministic identity

`boxed: sum_{r=0}^3 mathcal E_r(A) = e_3(A^2)`.

Consequently, if `A` has at least three eigenvalues of modulus at least one,

`boxed: sum_r mathcal E_r(A) >= 1.`

Moreover there exists a literal original-coordinate bipartition `I disjoint_union J={1,...,n}` such that

`boxed: e_3(A[I,J]^T A[I,J]) >= mathcal E_0(A)/64.`

Hence, whenever `mathcal E_0(A)>0`, the newest completed marginal-free physical-E3 receiver gives the full ambient law

`boxed: ||p_Q||_infinity <= 2 C_E3 mathcal E_0(A)^(-1/6)`

and therefore every interval `B` obeys

`boxed: P(Q in B) <= 2 C_E3 mathcal E_0(A)^(-1/6) |B|.`

Numerically `2 C_E3=16.906042451056354...`.

The density on this branch is continuous and vanishes at infinity because the cited E3 receiver has that conclusion.

### Proof

For a fixed `S` of size three, Cauchy–Binet and symmetry give

`det((A^2)[S,S])
 = sum_{|T|=3} det(A[S,T]) det(A[T,S])
 = sum_{|T|=3} det(A[S,T])^2.`

Summing over `S` yields

`sum_{S,T} det(A[S,T])^2
 = sum_{|S|=3} det((A^2)[S,S])
 = e_3(A^2).`

Partitioning the left side by `|S intersect T|=r` proves the first identity. Since the eigenvalues of `A^2` are `lambda_i(A)^2`,

`e_3(A^2)=sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2 >=1`

under the owner hypothesis.

Now assign each physical coordinate independently to `I` or `J` with probability one half. For the literal cross block `M=A[I,J]`, Cauchy–Binet gives

`e_3(M^T M)
 = sum_{S subset I, T subset J, |S|=|T|=3} det(A[S,T])^2.`

Such an ordered pair `(S,T)` must be disjoint. Conversely, every ordered disjoint pair is included with probability exactly `2^-6`, because all six distinct physical coordinates must receive their prescribed sides. Therefore

`E_{I|J} e_3(A[I,J]^T A[I,J]) = mathcal E_0(A)/64.`

At least one cut attains the average. Applying the completed r48 E3 receiver and using `64^(1/6)=2` proves the density and interval bounds. QED.

## 3. Whole-copy decoupled-time estimate

Let

`H = 2 C_E3 mathcal E_0(A)^(-1/6)`.

The branch above proves `||p_Q||_infinity<=H`. For an independent copy `Q'` of the whole scalar output, convolution gives `||p_{Q-Q'}||_infinity<=H`. Layer cake therefore yields

`E |Q-Q'|^(-1/2) <= 2 sqrt(2H)
 = 4 sqrt(C_E3) mathcal E_0(A)^(-1/12).`

Keeping only the whole-output identity

`|phi_Q(t)|^2 = E exp(it(Q-Q'))`

and the positive half-Riesz Fourier identity gives

`boxed:
 integral_R |t|^(-1/2) |phi_Q(t)|^2 dt
 <= 4 sqrt(2 pi C_E3) mathcal E_0(A)^(-1/12)
 =29.1511643034760... mathcal E_0(A)^(-1/12).`

Also

`P(|Q-Q'|<=epsilon) <= 4 C_E3 mathcal E_0(A)^(-1/6) epsilon.`

No coordinatewise `X-X'` is separated from its conjugate `X+X'`, and no such pair is declared independent.

## 4. Explicit universal fork

Taking the threshold `mathcal E_0=1/4` gives the clean deterministic dichotomy

1. if `mathcal E_0(A)>=1/4`, then

`boxed: ||p_Q||_infinity <= 2^(4/3) C_E3 <21.301;`

2. if `mathcal E_0(A)<1/4`, then

`mathcal E_1+mathcal E_2+mathcal E_3>3/4`,

so at least one overlap class satisfies

`boxed: mathcal E_r(A)>1/4 for some r in {1,2,3}.`

Thus the full three-large-eigenvalue problem is reduced, at this structural stage, to three explicitly overlap-heavy exterior configurations whenever the disjoint-crossing exit does not fire. The classes have literal physical meanings: `r=1` is a five-coordinate one-anchor overlap, `r=2` a four-coordinate two-anchor overlap, and `r=3` the principal-triple exterior energy. This does not claim those three overlap-heavy classes are already paid.

That is the new first unpaid implication: route each overlap-heavy class product-preservingly into the existing finite-hub / nested-rank-two / localized-principal / aggregate-frame receivers, without demanding one large individual minor.

## 5. Required pinned e5f71d79 result applied to an actual family

Consider the exact target-valid flat signed-frame family. Let `n=4q`, and form an `n x 3` matrix `R` by repeating each of the four rows

`(+++)`, `(+--)`, `(-+-)`, `(--+)`

exactly `q` times, each row scaled by `1/sqrt(n)`. Then `R^T R=I_3`. Put

`A_q = R diag(1,1,-1) R^T`.

Its nonzero spectrum is exactly `{1,1,-1}`. All frame manipulations here are deterministic coefficient algebra only.

For even `q>=4`, split every one of the four row types evenly between physical banks `I` and `J`. Then

`R_I^T R_I=R_J^T R_J=(1/2)I_3`,

so the literal cross block `M=A_q[I,J]` has exactly three nonzero singular values, all equal to `1/2`. Hence

`boxed: Z_3=e_3(M^T M)=1/64.`

Because the cross block has exact rank three, its volume-sampling row marginals are the left-frame leverages. Every physical row in `I` has

`alpha_i = 2 ||R_i||^2 = 6/n = 3/(2q) <= 1/2.`

Therefore the completed pinned theorem D from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

applies at equation level and gives

`boxed: ||p_{Q_q}||_infinity <= 6 sqrt(e) (1/64)^(-1/6)=12 sqrt(e)=19.7846552484... .}`

Thus

`P(Q_q in B) <=12 sqrt(e)|B|`

for every interval `B`.

The same pinned theorem supplies

`|phi_{Q_q}(t)| <= min{1,
 (2pi)^(3/2)e^(3/4)(1/64)^(-1/4)|t|^(-3/2)}.`

Integrating its square at the exact crossover yields the assigned dependence-safe time estimate

`boxed:
 integral_R |t|^(-1/2)|phi_{Q_q}(t)|^2 dt
 <= (48/5) sqrt(pi) e^(1/4)
 =21.8484076269... .}`

Equivalently,

`boxed: E|Q_q-Q_q'|^(-1/2)
 <= (24 sqrt(2)/5)e^(1/4)
 =8.7162535618... .}`

This is an actual use of a completed result from the required pinned RESULTS/FOURIER_ROUTE_REPORT package, not a citation-only mention.

## 6. Source-valid obstruction to one-minor localization

The same flat family quantifies why the new global exterior currency is useful. For any physical triple `S`,

`det(A_q[S,S])=-det(R_S)^2`.

It is zero unless the three selected rows have three distinct sign types. In the nonzero case the unscaled sign determinant has modulus four, so

`boxed: |det(A_q[S,S])|=16/n^3=1/(4q^3).}`

Thus every single physical principal-triple determinant tends to zero like `q^-3`, even though the total third exterior energy is exactly

`e_3(A_q^2)=1`.

More sharply, if `mathcal E_0(q)` denotes the disjoint exterior mass, the nonzero triple weights are uniform and one obtains exactly

`boxed:
 mathcal E_0(q)
 = (1/4)(1-1/q)^3 +(3/4)(1-1/q)^2.}`

Hence `mathcal E_0(q)->1`; already at `q=4`, `mathcal E_0=135/256>1/2`. The newest partner E3 receiver combined with Theorem 2.1 therefore gives a dimension-free bound while every single principal-triple determinant degenerates. This is an obstruction to an exhaustive proof based on selecting one uniformly good physical triple; it is not a counterexample to QFORM.

## 7. Latest designated partner fleet03/B03 applied

The newest compatible designated partner result read this run is fleet03/B03 r48, `QFORM-BALANCED-CARRIER-E3-PROMOTION-v1`, whose proof imports the completed marginal-free physical-E3 receiver with constant `C_E3` and preserves all same-bank terms and outside couplings.

Theorem 2.1 applies that receiver to the literal cut produced by the random-partition identity, giving the new target-level branch

`||p_Q||_infinity <= 16.9060424511... mathcal E_0(A)^(-1/6)`

and the whole-copy estimate

`integral |t|^(-1/2)|phi_Q(t)|^2
 <=29.1511643035... mathcal E_0(A)^(-1/12).`

On the flat signed-frame family, the balanced explicit cut has `E3=1/64`, so the partner receiver separately gives

`||p_{Q_q}||_infinity <= 2 C_E3=16.9060424511...`,

while the pinned theorem-D envelope gives the sharper time integral recorded above.

## 8. Scope and next debt

This run does not prove the unrestricted theorem. It proves a universal linear-small-ball branch whenever a positive fraction of the mandatory third exterior spectral energy is carried by disjoint physical triples, and it converts failure of that branch into a quantitative overlap-heavy trichotomy.

The next B03 debt is therefore precise: for `r=1,2,3`, turn `mathcal E_r(A)>=c` into either (a) an already-paid finite-hub / grouped-carrier / physical-E3 receiver, or (b) a further exact obstruction showing what aggregate object must replace individual-minor selection. The mechanism must retain every nonzero tail and original-coordinate product provenance.

Full QFORM: OPEN. Unrestricted continuity: OPEN.
