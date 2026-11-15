# Coding kernels for Fourier dispersion

All logarithms are base two. Write p_i=I_i, I=sum_i p_i, mu(S)=fhat(S)^2,
up(S)=sum_{U superset S} mu(U), v=1-mu(empty), and
B=sum_S mu(S) log(up(S)/mu(S)). Zero-mass terms are omitted.
A kernel r(U,S) is supported on S subset U and each row sums to one. Its output law is
nu(S)=sum_U mu(U)r(U,S). Write R_r for the right side in the brief.

The new general-class FEI proof requested in the brief is not obtained here. The results below
are proved identities, an explicit influence-log bound, obstructions, direct class calculations,
and a finite kernel search. Small-dimensional optimization is not a proof in arbitrary dimension.

## 1. The coding slack is exactly relative entropy

Since E[r(U,S) | U contains S]=nu(S)/up(S),

    R_r = sum_S mu(S) log(up(S)/nu(S))
        = B + D_2(mu || nu).                                      (1)

This includes the extended-real case when nu(S)=0<mu(S). Gibbs' inequality proves R_r>=B.
For completeness, concavity of log gives
sum_{mu(S)>0} mu(S) log(nu(S)/mu(S)) <=
log(sum_{mu(S)>0} nu(S)) <= 0.

Equality requires nu=mu. Couple U~mu and T~r(U,.). If nu=mu, then
E(|U|-|T|)=0. The integrand is nonnegative, so T=U almost surely. Thus identity is the
unique optimizer on rows with mu(U)>0. Rows of zero input mass can be arbitrary.

A useful, but insufficient, comparison is

    B <= R_r <= B + sum_S mu(S) log(1/r(S,S)),                     (2)

because nu(S)>=mu(S)r(S,S). If r(U,U)>=2^{-c|U|}, then R_r<=B+cI.
If r(U,U)>=a>0 on nonempty U, then R_r<=B+v log(1/a), since r(empty,empty)=1.
These estimates do not prove FEI: they pay for kernel slack after leaving B untouched.

## 2. An explicit product kernel recovers the requested shape

Take lambda_i=1-p_i: delete i with probability 1-p_i, independently among i in U.
Equivalently retain i with probability p_i. Define the Bernoulli law

    q(S)=prod_{i in S} p_i prod_{i outside S}(1-p_i).

For every U containing S,

    r(U,S)=prod_{i in S}p_i prod_{i in U-S}(1-p_i) >= q(S).

Taking the conditional expectation, logarithm, and mu-average proves

    B <= R_influence <= sum_S mu(S) log(1/q(S))
                     = sum_i h_2(p_i)
                     <= sum_i p_i log(1/p_i) + (log_2 e) I.       (3)

The last inequality follows from -(1-p)ln(1-p)<=p. Influences zero or one cause no
problem: when mu(S)>0, S excludes every coordinate of influence zero and includes every
coordinate of influence one. The formula therefore extends to endpoints, or follows by limits.
A constant function has B=R=I=0.

This gives the requested B<=C(I+sum p_i log(1/p_i)) with C=log_2 e. The sharper
statement is (3), with coefficients log_2 e and one separately. Applying the brief's
Theorem 1 gives

    H <= 2 sum_i p_i log(1/p_i) + (2+2 log_2 e) I - 2v.          (4)

There is an immediate stronger entropy bound: entropy subadditivity for the indicator vector
of S~mu gives H<=sum_i h_2(p_i)<=sum_i p_i log(1/p_i)+(log_2 e)I directly. Thus (4)
is a recovery through the requested route, not a new state-of-the-art entropy estimate.

There is also a lower bound specific to this product choice. Since r(U,S)<=prod_{i in S}p_i,

    R_influence >= sum_i p_i log(1/p_i).                         (5)

Consequently this kernel's cost is the influence-log term plus an error between zero and
(log_2 e)I. It cannot yield R<=CI uniformly. For AND_n, p_i=2^{1-n}, so R/I>=n-1.
For odd majority, p_i=binom(n-1,(n-1)/2)/2^{n-1}; Stirling's formula makes
log(1/p_i)=(1/2)log n+O(1), again unbounded. Balanced tribes similarly has
p_i=2^{1-w}(1-2^{-w})^{t-1} tending to zero as the width grows.

Literature comparison: Han's Theorem 1 has the shape in (4). His displayed derivation
in equation (3.4) yields H<=(3/ln 2+2)I+sum_i p_i log_2(1/p_i), after converting
natural logarithms. KKLMS Theorem 1.3 instead bounds truncated spectral entropy using
sum_{|S|<=D}|S|log(|S|+1)mu(S) plus I; Theorem 1.2 gives spectral concentration.
These are different statements. In particular, a concentration theorem cannot silently
be promoted to a full Shannon entropy bound. See the primary-source links in SOURCES.md.

## 3. Fixed product thinning and random restrictions

For a fixed 0<lambda<1, r(U,U)=(1-lambda)^{|U|}. Therefore

    B <= R_lambda <= B+I log(1/(1-lambda)).                      (6)

At lambda=1/2 this is B<=R_half<=B+I. Proving R_half<=CI for all Boolean functions
would prove FEI by the brief's Theorem 1. Conversely FEI implies that bound by B<=H and (6).
This equivalence explains why changing the fixed thinning parameter is not itself progress.

If L is a random live set independent of U, then r(U,S)=Pr[U intersect L=S]. Independent
live coordinates give product kernels; perfectly correlated L=[n] or empty gives the
erasure kernel in the next section. A hard live-set cardinality cap can make R infinite.
Indeed, choose an inclusion-maximal set S in the support of mu. Then nu(S)=mu(S)r(S,S).
A rule with r(S,S)=0 gives infinite cost. For parity on more coordinates than the cap,
this failure is immediate. A deterministic proper-prefix stop has the same problem.

## 4. Keep or erase, delete one, and their limitations

For nonempty U, the keep-or-erase kernel retains U with probability 1/2 and outputs empty
with probability 1/2; the empty row stays empty. Put a=mu(empty). Then

    nu(empty)=(1+a)/2,       nu(S)=mu(S)/2 for S nonempty,
    R_erase=B+(1-a)+a log(2a/(1+a)).                            (7)

The last term is zero by continuity at a=0. Equation (1) implies the added quantity is
nonnegative; its displayed form also shows it is at most v. Thus

    B <= R_erase <= B+v <= B+I.                               (8)

The final inequality v<=I follows because |S|>=1 on nonempty sets. For balanced f,
R_erase=B+1 exactly. This kernel retains each coordinate of U with probability 1/2, so
its small cost does not come from vanishing shrinkage. Its gap bound still leaves B.

The delete-one kernel keeps U with probability 1/2 and otherwise deletes a uniformly
chosen member of U. It has the same diagonal 1/2 on nonempty rows and hence the same
B+v upper bound. For a set of size k it retains k-1/2 coordinates in expectation,
rather than k/2. Its better small-dimensional ratios must be read with that distinction.

For any epsilon in (0,1), replacing 1/2 by keep probability 1-epsilon gives
R<=B+v log(1/(1-epsilon)). The cost approaches B as epsilon approaches zero.
Therefore 'best nonidentity family' has no unique answer without a required amount of
shrinkage. The census reports both unrestricted tested families and half-retention families.

## 5. Prefix stopping, uniform retained size, and mixtures

Fix an order of the coordinates. On input U, choose K uniformly from 0,...,|U| and keep
the first K members of U in that order. The order may be chosen from f, for example by
influences. This is a valid adaptive stopping kernel with diagonal 1/(|U|+1), so

    R_prefix <= B+E_mu log(|S|+1) <= B+I.                      (9)

The last inequality is log_2(k+1)<=k for every nonnegative integer k. Choosing the best
of all coordinate orders from f is still a single valid f-dependent kernel. The census
examines every order in four variables. For larger examples it uses ascending and
descending influence order, breaking ties by index, and takes the better result.

Averaging over a uniform random order gives the order-free kernel

    r(U,S)=1/((|U|+1) binom(|U|,|S|)).                         (10)

It chooses the retained size uniformly and a uniform subset of that size. It obeys (9).
Equivalently, choose a retention probability uniformly in [0,1], then retain independently;
integration of t^{|S|}(1-t)^{|U-S|} gives (10). This also retains half the coordinates
in every row on average.

Any convex mixture of kernels is a kernel. The cost is convex in its output law:
-log is convex. For fixed f, optimizing a mixture is a one-dimensional convex problem
when mixing erasure with independent half-thinning. This optimization computes nu; it
neither assumes nor proves FEI. The census uses a deterministic 44-step derivative
bisection and also evaluates two fixed rational mixtures, so the searched result is
separated from reproducible fixed choices. No identity kernel is in these mixtures.

## 6. A fitted retained-size rule, and what its census means

For k=|U|<=4, choose a retained size j with probabilities q_{k,j} given below, and choose
a uniform j-subset of U. All numerators have denominator 4096.

| k | numerators q_{k,0},...,q_{k,k} |
| --- | --- |
| 0 | 4096 |
| 1 | 2048, 2048 |
| 2 | 1853, 390, 1853 |
| 3 | 1715, 323, 353, 1705 |
| 4 | 1462, 195, 775, 209, 1455 |

For k>4, keep or erase with equal probabilities. This specifies a single kernel in
every dimension, using only the size of U. Each row has mean retained size k/2: summing
j times the listed numerators gives k*4096/2. Each row sums to 4096 and is nonnegative.
The smallest nonempty diagonal probability is 1455/4096, and every diagonal is at least
2^{-k}. Therefore

    B <= R_fitted <= B+min(I, v log(4096/1455)).                 (11)

The weights were discovered by fitting the cost at AND_4, then rounding on a rational grid
while preserving the linear row constraints. Every four-variable function was subsequently
evaluated. Section 12 supplies a rigorous near-optimality certificate under a specified half-retention
constraint. This is a finite discovery experiment, not a held-out test or a new asymptotic theorem.

## 7. Direct bounds for AND and disjoint-term DNF

These are direct calculations, not assumptions of general FEI. The classes are already
known FEI classes; no new-class claim is made.

For AND_n, put q=2^{-n}. Every nonempty Fourier coefficient has square 4q^2 and
mu(empty)=(1-2q)^2. For nonempty S,
up(S)/mu(S)=2^{n-|S|}, so

    B_nonempty = I(1-2q),       I=2nq,
    v/I=2(1-q)/n.

Since -a log_2 a <= (log_2 e)(1-a) for 0<=a<=1,

    B/I <= 1-2q + 2(1-q)(log_2 e)/n.

Equations (6), (9), and (11) now give an explicit constant times I for their respective
kernels. In particular R_half,R_prefix,R_uniform-size,R_fitted <= [2+2(log_2 e)/n]I,
and R_erase,R_delete-one <= [1+2(log_2 e+1)/n]I. The influence kernel fails by (5).

Here is a more general exact calculation. Let f be OR of AND terms on disjoint nonempty
blocks with widths w_1,...,w_t. Input negations and an output negation do not change mu,
so the statement includes unate variants. Put

    q_j=2^{-w_j},  a_j=1-q_j,  P=prod_j a_j,
    L_j=log(1/a_j),  v=4P(1-P),  mu(empty)=(2P-1)^2.

For nonempty S, let J be its touched blocks. Expanding
f=1-2 prod_j(1-AND_j) shows

    mu(S)=4 prod_{j in J} q_j^2 prod_{j outside J} a_j^2,
    log(up(S)/mu(S))=
        sum_{j in J}(w_j-|S intersect block j|)+sum_{j outside J}L_j.

To verify the second identity, on a touched block the up-sum has 2^{w_j-|S_j|}
identical contributions q_j^2. On an untouched block the total unnormalized squared
mass is a_j^2+(2^{w_j}-1)q_j^2=a_j. Divide by the displayed mu(S).

Let M_j=sum_S mu(S)1_{S touches block j}. Summing the first formula gives

    M_j=4q_j P,        I_j(block)=2w_j q_j P/a_j,
    B=B_empty+sum_j [w_j M_j-I_j(block)+L_j(v-M_j)].             (12)

This is the claimed exact formula, including the biased empty coefficient. Write
w_min=min_j w_j and c=log_2 e. The first two terms in each bracket sum to at most I,
because w_j M_j=2a_j I_j(block)<=2 I_j(block). Also
L_j<=c q_j/a_j, hence

    sum_j L_j(v-M_j) <= v sum_j L_j
       <= 4cP(1-P) sum_j q_j/a_j
       <= (2c/w_min) I.

Finally 1-P<=sum_j q_j<=sum_j q_j/a_j implies v/I<=2/w_min. Thus
B_empty<=cv<=(2c/w_min)I, and altogether

    B <= [1+4c/w_min] I,
    R_erase,R_delete-one <= [1+(4c+2)/w_min] I,
    R_half,R_prefix,R_uniform-size,R_fitted <= [2+4c/w_min] I.   (13)

Mixtures inherit the larger of their component bounds by (2), or by convexity. This
proves the requested CI property for tribes at all widths and term counts. The estimate
is deliberately loose. It includes unequal term widths and does not assert a new FEI
class. For overlapping terms, the factorization used in (12) fails: squaring the
inclusion-exclusion expansion creates interacting terms and cancellations. No replacement
bound for those terms is proved here. Bounded DNF width alone does not justify discarding them.

## 8. Address, majority, and the two five-variable examples

For k address bits and 2^k data bits, the address function is balanced. Its spectral
sets contain exactly one data bit and any subset of the address bits, each of mass
4^{-k}. Hence H=2k, I=1+k/2, B=k/2. The up-ratio for a set with s address bits is
2^{k-s}; averaging proves the B formula. Direct summation for half-thinning gives

    R_half = 1+k-(k/2)log(3/2).

Equation (7) gives R_erase=I exactly. The delete-one bound gives R_delete-one<=I.
The prefix, uniform-size, and fitted diagonal bounds give R<=B+I<=2I. The influence
kernel has lower bound k from its data-coordinate contribution alone; here this is O(I),
so it is not an obstruction on address. Indeed sum p_i log(1/p_i)=k/2+k=3k/2:
the k address influences are 1/2 and the data influences are 2^{-k}. Equation (3)
therefore bounds R_influence by (3+log_2 e)I. Its ratios are computed in structured.json.

For majority, a proof can use the established theorem for all symmetric functions, rather
than assume general FEI. O'Donnell--Wright--Zhou, Theorem 1, proves H<=12.04 I. Thus
B<=12.04 I and all the tested kernels with diagonal >=2^{-|U|} have R<=13.04 I.
This is an imported class theorem, not a new proof or best constant. Its noise-stability
argument supplies the missing structural input; the generic coding argument does not.

Independently, symmetric.py evaluates majority's exact coefficient formula. For n=2m+1,
with a=binom(2m,m)/2^{2m}, every coefficient at size 2j+1 has magnitude

    a binom(m,j)/binom(2m,2j),

and even levels vanish. For any symmetric spectrum with per-set mass c_s,
up(s)=sum_{k>=s}binom(n-s,k-s)c_k. For the uniform-size kernel,
nu(s)=sum_{k>=s}W_k/(k+1)/binom(n,s), where W_k=binom(n,k)c_k.
These are finite sums over levels, allowing checks beyond explicit truth tables.

The two five-variable truth tables use exactly the bit convention in the brief. Their
costs are finite sums in structured.json, independently checked with rational Fourier
masses and 70-digit logarithms in rational_certificates.json. A bound for a single
finite function is not an asymptotic theorem. Balanced compositions are addressed next.

## 9. Balanced composition and a rigorous obstruction to extrapolating the census

Let f have disjoint balanced inner functions g_i. Sample T from mu_f and, independently
for each i in T, a nonempty spectral set from mu_{g_i}. Balancedness makes inner spectral
sets nonempty, so the active outer block set T is recovered from the final set. For a
spectral set S with active blocks K,

    mu_F(S)=mu_f(K) prod_{i in K}mu_{g_i}(S_i),
    up_F(S)=up_f(K) prod_{i in K}up_{g_i}(S_i).

The first equality follows by expanding the Fourier series on disjoint blocks. For the
second, every outer T containing K contributes mu_f(T), the constrained blocks contribute
their up-masses, and all other inner blocks sum to one. Divide the two equalities, take
logs and expectations to obtain

    B(F)=B(f)+sum_i I_i(f)B(g_i),
    I(F)=sum_i I_i(f)I(g_i).                                  (14)

The same sampling argument gives the analogous entropy formula. If every balanced gate h
in a collection satisfies B(h)<=beta(I(h)-1), induction using (14) gives
B(F)<=beta(I(F)-1) for every balanced formula over those gates with disjoint inputs.
If beta>=1, (7) then proves R_erase(F)=B(F)+1<=beta I(F). Other diagonal-bounded
kernels obey R<= (beta+1)I. This is a structural theorem with a finite gate check, although
its class is covered by established composition theory.

For iteration of one balanced gate with I_0>1,

    I_d=I_0^d,       B_d=B_0(I_0^d-1)/(I_0-1).

For the brief's balanced 0x008eeeee, the ratio B_0/(I_0-1) is
2.153759374819711 in compositions.json. Therefore B_d/I_d and R_erase/I_d tend to
that number. A four-variable maximum near 1.6 cannot serve as a universal upper bound.

## 10. The proposed small-influence class is equivalent to general FEI

For arbitrary nonconstant f on d variables, take m disjoint copies and multiply their
outputs (XOR in the zero-one convention). The spectral law is a product law. Thus

    H(F)=mH(f),       B(F)=mB(f),       I(F)=mI(f),

because up also factors. Every individual influence is unchanged. Put m=4d and n=4d^2.
Then

    I(F)/sqrt(n)=2 I(f) > max_i I_i(f).

The strict inequality uses I(f)>0 and max_i I_i(f)<=I(f). Consequently a uniform B<=CI,
H<=CI, or R_r<=CI theorem for *all* functions in this small-influence class would imply
general FEI after dividing by m (and using B<=R_r in the third case). The reverse direction
for the tested diagonal-bounded kernels follows from (2). This class is therefore not an
easier route. The construction does not preserve monotonicity or bounded DNF width, and
no such extension is claimed. audit.py checks an explicit instance by a direct truth table.

## 11. What remains missing

The promising numerical families all admit R=B+O(I), or even B+O(v). None of those
comparisons bounds B itself on arbitrary monotone functions or overlapping width-w DNF.
The direct disjoint-DNF proof locates the missing input at the overlapping expansion;
the small-influence alternative has the exact reduction above. No inequality controlling
that missing term by CI has been proved. The requested theorem for a previously unresolved
class is therefore still open in this report. Neither the finite census nor the fitted
kernel is presented as resolving it.

## 12. Certified near-optimality in four variables under half retention

A precise finite problem avoids the ambiguity noted in section 4. Require each kernel row
to satisfy E(|T| | U)=|U|/2. The kernel can otherwise be arbitrary and may depend on f.
Let M be the infimum, over such kernel assignments, of the worst R/I over nonconstant
four-variable Boolean functions. The rational rule in section 6 supplies an upper bound
on M. An AND_4 dual certificate supplies a lower bound within 2*10^{-9} of it.

Here is the lower-bound argument without any optimization assumption. At AND_4,
mu(empty)=49/64 and mu(S)=1/64 for every nonempty S. Its influence is 1/2. Any admissible
output law nu has mean size 1/4. Choose rational a,b with a>0, b>0 and a+b/4=1.
For d_S=a+b|S|, the inequality -ln x>=1-x yields

    D_2(mu||nu)
      = sum_S mu(S) log_2 d_S
        + sum_S mu(S) log_2(mu(S)/(nu(S)d_S))
      >= sum_S mu(S) log_2 d_S
         + (log_2 e)(1-sum_S nu(S)d_S)
      = sum_S mu(S) log_2 d_S.                               (15)

This remains valid if a positive-mass mu atom has zero nu mass, since the left side is
infinite. Thus any such kernel has

    R/I >= 2[B(AND_4)+sum_S mu(S)log_2(a+b|S|)].                (16)

No stationarity equation or floating solver is needed to validate (16). The certificate
uses b=136246219264343/281474976710656 and a=1-b/4. A numerical root search only helped
choose a strong rational value of b.

For the upper bound, certify_size_kernel.py forms every mu, up and nu with exact integer
numerators for the kernel in section 6. Its row denominator after clearing subset-choice
fractions is 49152. It then bounds every logarithm by rational series. After scaling
x=2^e y with 1<=y<2, put z=(y-1)/(y+1), so 0<=z<1/3. Then

    L_m=2 sum_{j=0}^{m-1} z^{2j+1}/(2j+1),
    L_m <= ln y <= L_m+2z^{2m+1}/((2m+1)(1-z^2)).

The last bound follows by bounding every omitted denominator below by 2m+1 and summing
a geometric series. Apply the same bound to ln 2 (z=1/3). Dividing the positive
intervals bounds log_2 y, then add e. The script uses 32 terms, exact Fraction arithmetic
for these bounds, and outward-rounded Decimal arithmetic at precision 45 when accumulating
weighted terms and dividing by I. The weights mu and I are exact dyadic rationals.

The certified maximum interval in certified_size_kernel.json is

    [1.60116289253127354937605371588406570678648642,
     1.60116289253127354937605371588406847027166180].

It is attained at AND_4. Exactly 32 truth tables have that same squared spectral law;
the largest upper bound outside that law is below 1.577481. This certifies the maximum,
including ties, rather than relying on a float ranking. The dual lower bound in (16)
is at least

    1.60116289073089139330247724695121708345789606.

Consequently the displayed rule is within 1.800383*10^{-9} of the best possible worst
four-variable ratio under the conditional mean-size constraint. This numerical tolerance
is a certified bound from the script, not a claim of exact attainment of the infimum.
The certificate does not address larger dimension or kernels with weaker shrinkage.
