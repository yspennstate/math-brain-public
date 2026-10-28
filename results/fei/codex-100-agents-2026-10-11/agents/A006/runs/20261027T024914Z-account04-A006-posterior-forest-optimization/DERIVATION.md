# A physical-weight dual for the posterior cost

A polynomial certificate can bound the full feasible-weight infimum, even after taking arbitrary public mixtures. It can be sharper than relaxing the induced root law to a simplex. All logarithms below are in bits unless ln is written.

## 1. General certificate, with the actual run space fixed

Fix a finite physical Boolean function f and p(A)=fhat(A)^2 on nonempty sets; write v=sum p(A). Fix ONE generator, a finite collection of its distinct actual runs, and their canonical chronological keys. A chosen collection may be a subreference: no lower bound about that collection is automatically a lower bound about a larger collection. Suppose the exact probability of each chosen run r is c_r(lambda)/Z(lambda), and its output is A(r). Define

    N_A(lambda)=sum_(r:A(r)=A) c_r(lambda),
    Q_lambda(A)=N_A(lambda)/Z(lambda),
    C(Q)=sum_A p(A)log2(1/Q(A)).

For all admissible lambda, Z(lambda)>0 and the masses are nonnegative. The masses and the common denominator may be polynomials with rational coefficients; a positive common denominator can first clear rational functions. Actual chronological child orders are separate runs when the generator draws them separately. Two descriptions of the same sequence of generator draws are ONE run. Numerical coincidence of two distinct probabilities does not merge their events.

Choose any admissible reference Q0 positive on supp p, including a public mixture of admissible Q_lambda. Set C0=C(Q0). Suppose a rational M satisfies the polynomial inequalities

    F_M(lambda) := M Z(lambda)
                    - sum_A [p(A)/Q0(A)]N_A(lambda) >= 0

on the ENTIRE admissible physical parameter set. Then every fixed public mixture Q of these references satisfies

    C0 -(M-v)/ln 2 <= C(Q).

As Q0 itself is eligible, its C0 is an upper bound on the infimum. In particular M=v proves Q0 globally optimal over all weights AND all public mixtures. All normalizing factors remain in F_M.

Proof. The polynomial inequality gives sum_A p(A)Q_lambda(A)/Q0(A)<=M. Averaging over any public probability law on lambda gives the same inequality for Q (finite sums over A allow this interchange). For x>0, -ln x>=1-x, so

    C(Q)-C0 >= [v-sum_A p(A)Q(A)/Q0(A)]/ln2.

If Q vanishes at a positive-p set, C(Q)=infinity and the lower bound holds directly. Parameter limits with Z=0 are included only when the output references have a valid limit; the inequality extends by finite coordinate continuity. The statement does not divide by Z=0. For f constant, v=0 and the nonempty objective is zero; the interesting case has v>0. Subprobability references cause no change to this argument.

The scalar inequality follows also by differentiating x-1-ln x: its derivative is (x-1)/x, negative before 1 and positive after 1. Thus no sign or normalization premise is hidden in the tangent bound.

## 2. Posterior and computable certificates

For any output A with N_A>0 the optimal witness posterior is theta(r|A)=c_r/N_A. Direct substitution gives

    sum_r theta(r|A)log2[Z/c_r] - H(theta(.|A))
       = log2[Z/N_A].

For any other posterior it adds KL(theta || c/N_A), with the usual zero-support conventions. This identity is used to evaluate C, not claimed as new. The new certificate optimizes over the physically realizable parameter set rather than independently varying root probabilities.

The polynomial test is exact and computable. A rational triangulation of a feasible polytope, nonnegative homogeneous barycentric coefficients on each simplex, and exact coefficient identities certify nonnegativity. Sums of nonnegative constraint products and squared polynomials also suffice. A proposed certificate is checked by rational coefficient arithmetic; grid sampling alone never replaces it. A certificate need not exist at a chosen degree. This is a verification interface and a finite-degree search scheme, not an assertion that one fixed degree resolves every instance. Rational outward logarithm intervals turn C0 into a rigorous cost interval. For M>=v one may use ln2>1/2 to obtain the entirely rational additive error 2(M-v) bits; if M<v a valid Q0 in the class would contradict its own score v.

## 3. Exact calibration on a connected overlap, using 15 actual forest runs

Take the edge-union function on K3. It is majority of three physical bits, used here solely to verify a global-weight optimization certificate, not as a new FEI class theorem. Gates are the three width-two edges. The fixed run collection is the maximal-matching star completion already used in A006's previous work: maximal match the selected set, give each unmatched selected vertex one incident gate, and attach it to the matched endpoint when present; otherwise it is a singleton root. Use fixed increasing root order. Retain all chronological child orders as drawn by this generator. The generator probabilities are those of the prior width-two queue construction; the present checker reconstructs them without importing prior code.

There are exactly 15 actual runs: two for each singleton output, one for each pair, and six for the triple. Let lambda_i>0 and lambda_i+lambda_j<=1. Write s1=sum lambda_i, s2=sum_(i<j)lambda_i lambda_j, s3=product lambda_i. The full root normalizer is

    D=product_i(1+lambda_i/4)-1 = s1/4+s2/16+s3/64.

For completeness, the generator underlying these masses can be specified directly. Draw a nonempty root set R with probability product_(i in R)(lambda_i/4)/D and visit roots in increasing order. At a width-two gate choose a particular nonempty local subset B of size s with probability1/[s(s+1)binom(2,s)] (the unused mass is failure). Draw c children with probability1/[(c+1)(c+2)], then a uniform weak composition of c into the s selected-coordinate slots. For each slot draw the ordered child gate labels with probabilities lambda_j over gates incident to that coordinate, with any remaining mass failure. Physical incidence caps make these substochastic choices valid. Queue children in coordinate order and label-draw order. Abort repeated gate visits; restrict accepted runs further to the stated maximal-matching star completions with disjoint ownership of output coordinates. All other draws are outside this subreference. Every accepted run then has EXACT probability

    (product_(root i) lambda_i/4)/D
      times product_(visited i) 1/[s_i(s_i+1)binom(2,s_i)
        (c_i+1)(c_i+2)binom(s_i+c_i-1,c_i)]
      times product_(child j) lambda_j.

The root-set law sums to one, the child-count law telescopes to one, and every remaining choice has mass at most one. Therefore these are probabilities of distinct actual draws of a fixed sampler, not freely assigned witness weights. The finite accepted collection has mass at most one regardless of any infinite unsuccessful trajectories. The test uses this explicit fixed sampler; no equivalence to additional accepted runs of a larger paper generator is assumed.

Each singleton numerator is the sum of its two incident lambdas divided by32. Each pair numerator is its edge lambda divided by48. The triple numerator is s2/1152. These are sums of probabilities of distinct actual runs, without a second counting of descriptions. The resulting subreference need not have mass one; omitted generator outputs are not silently restored.

The actual physical Fourier spectrum has p(singleton)=1/4 each, p(triple)=1/4, and zero at pairs; I=3/2. At lambda0=(1/2,1/2,1/2),

    Q0(singleton)=16/217, Q0(triple)=1/651.

Its score at an arbitrary feasible lambda is

    sum_A p(A)Q_lambda(A)/Q0(A)
       =217(3s1+2s2)/(3072D).

Thus M=v=1 is equivalent to

    F=117s1-242s2+48s3 >=0.

Here is an exact proof on the full physical polytope. If s1<=1, all lambdas are nonnegative and

    F=117s1(1-s1)+(109/3)s1^2
          +(242/3)(sum lambda_i^2-s2)+48s3 >=0,

because sum lambda_i^2-s2 is half the sum of the three squared pair differences. If 1<=s1<=3/2, put t=2(s1-1) and a_i=lambda_i-t/2. Then t>=0, a_i=1-(lambda_j+lambda_k)>=0 and sum a_i+t=1. This identifies the upper tetrahedron as conv(e1,e2,e3,h), h=(1/2,1/2,1/2). Homogenize F in (a,b,c,t). Its EXACT polynomial is

    117(a^3+b^3+c^3)
      +109 sum_sym a^2 b +24abc
      +(335/2)t(a^2+b^2+c^2)
      +117t(ab+ac+bc)
      +(113/2)t^2(a+b+c).

Every coefficient is nonnegative. The missing t^3 coefficient is zero. Here sum_sym contains the six terms a^2b,a^2c,b^2a,b^2c,c^2a,c^2b. The checker multiplies and compares rational polynomials exactly; the printed boundary grid is only an adversarial check of the identity, not its proof. The two regions cover the feasible polytope, since adding the three pair caps gives s1<=3/2.

Consequently the exact global infimum, INCLUDING all fixed parameter mixtures, is

    (3/4)log2(217/16)+(1/4)log2 651.

This certifies optimization for this fixed subreference. It does not prove that the same weights minimize the cost of ALL valid runs of the original queue, other dictionaries, or arbitrary Boolean functions.

At lambda0 the posterior is uniform among two actual runs at each singleton and six at the triple. The earned witness entropy is exactly 3/4+(1/4)log2 6. Repeating every run description twice would falsely add one bit of refund (v=1); the canonical-key check prevents that.

## 4. Quantitative improvement over the old relaxation

The earlier used-root-simplex relaxation has h(single root)=217/256, h(two used gates)=217/96, and h(three used gates)=0. Its gap certificate is therefore Gamma=max h-v=121/96 natural units, despite the physical all-weight optimum having gap ZERO. The physical polynomial certificate removes this spurious relaxation gap. This improvement concerns optimization certification, not a reduction of a claimed FEI constant. It explains why failure of a relaxed root simplex to prove payment is not an obstruction to the actual feasible-weight infimum.

## 5. Boundary and remaining gap

All denominator cancellations use D>0, valid for positive weights and also for nonzero nonnegative weight vectors. At the zero vector F=0 but no Q is defined; only valid output-law limits are allowed. Positive-p output zeros have infinite cost. Pair outputs have zero target mass but are retained in the reference mass and actual-run census. The dual explicitly contains the full D. No target entropy estimate, derivative-energy proxy, free selector, or new physical influence account is assumed.

The first unpaid universal line remains: for every Boolean f there exists an admissible ORIGINAL fixed reference with complete cost O(I(f)), including all physical overlap, posterior labels, selectors and normalizers. This certificate can bound or refute a proposed variational interface. It does not supply that universal reference. The next useful application is a growing-width connected nonfactorable overlap, allowing ALL incidence-feasible weights and public mixtures, with the same exact polynomial score test.
