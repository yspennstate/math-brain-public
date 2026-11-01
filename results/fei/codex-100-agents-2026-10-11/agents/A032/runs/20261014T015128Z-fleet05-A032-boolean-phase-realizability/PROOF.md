# Affine-phase admission in arbitrary dimension

Let h:{-1,1}^m->{0,+/-1,+/-2} be nonzero, integer-valued, with a coordinate-product squared Fourier law. Assume its Fourier signs on the coordinate face are an affine character: sign(hhat(s))=epsilon*(-1)^(t dot(s xor s0)). This is a hypothesis on one common sign assignment, not on separate convolution equations. Deterministic spectral coordinates give an overall physical character. Translate physical coordinates to remove the phase character. The remaining active coefficient magnitudes have the form lambda product_i a_i or b_i, with positive coprime integers a_i,b_i and rational lambda>0. Rationality follows from h's integer Walsh coefficients: primitive ratios and their product give rational lambda.

The inverse is h(x)=lambda*chi_K(x)*product_i(a_i+b_i x_i), up to global sign and translations. For one factor the gcd of a_i+b_i and a_i-b_i is1 when a_i,b_i have opposite parity and2 when both are odd. This includes (1,1), whose possible values are2,0. The gcd of all products of such factor values is the product of these gcds (prime valuations or repeated Bezout). If q pairs are both odd, integrality of every h value implies d=lambda*2^q is a positive integer. Its exact maximum magnitude is

max|h|=d product_i[(a_i+b_i)/gcd(a_i+b_i,a_i-b_i)].

Each fair pair (1,1) contributes1 to this integer product. Each nonfair odd pair contributes at least2, with equality only for (3,1) or (1,3). An opposite-parity pair contributes at least3. Since max|h|<=2, there are only these forms, allowing arbitrary deterministic physical characters and translations:

1. h=+/-chi_K 1_L, where L is a coordinate subcube; N=0 and all nonzero values have magnitude1.
2. h=+/-2 chi_K 1_L; N=0 and all nonzero values have magnitude2.
3. h=+/-chi_K (2 1_E+1_M), where M and E are the two equal halves of a coordinate subcube L, split on one active coordinate; N=1. The primitive nonfair pair is (3,1) in either order. All other active pairs are fair.

This proof is dimension-independent and uses actual integer inverse values. It is not a norm-only argument. Fourier coefficient sign twists may absorb redundant physical characters on fixed cell coordinates; only their magnitudes, which are displayed, enter the following admission classification.

Now let F(y,x) be Boolean with two physical address bits. Set h_J=2 E_y[F(y,x)chi_J(y)]. Direct enumeration of the16 four-sign address truth tables gives, pointwise: either one h_J=+/-2 and all others zero (pure), or all four h_J=+/-1 with sign product-1 (mixed). Every row therefore has the same mixed set M={x:|h_J(x)|=1}; their pure sets E_J={x:|h_J(x)|=2} disjointly partition M^c. Zero rows are possible only when M is empty.

Assume every nonzero row satisfies the product-spectrum and affine-phase hypotheses. If M is empty or the whole cube, each row has N=0, so Q=sum_J w_J N_J=0. Otherwise all rows are nonzero. Each row of type1 has support exactly M and E_J empty. Type2 is impossible. Every row of type3 makes M a coordinate subcube of codimension c>=1; its E_J is obtained by flipping exactly one of M's c fixed coordinates, with all other fixed coordinates retained. Indeed its support L has codimension c-1 and one additional split coordinate. There are only c distinct such neighbor subcubes, each of mass |M|, and disjointness permits at most one row per neighbor.

These E_J must cover M^c, which has (2^c-1)|M| points. Consequently 2^c-1<=c. For positive integer c this forces c=1: the inequality fails at2, and 2^c-1-c strictly increases thereafter. Thus exactly one row is of type3, with E_J=M^c; the other three rows have magnitude1 on M and vanish on M^c. The squared norms give

w=(5,1,1,1)/8 up to address-label permutation; Q=5/8; exactly one N_J=1.

The four labels have physical degrees0,1,1,2. Assigning the largest mass to degree0 minimizes I_A and gives I_A=1/2; any other assignment increases it. This assignment is realizable since every permutation of four slice labels preserves the two pointwise forms. H(w)=3-(5/8)log2(5), so the sharp uniform payment in this admitted all-dimensional class is

Q <= K_aff (H(w)+I_A), K_aff=5/(28-5 log2(5))=0.3050573718... <1/2.

The three-bit point defect, with two of its bits designated addresses, attains the bound. Actual truth signs and Walsh coefficients are independently checked in out/validation.json. This also proves an exact impossibility certificate: a mixed candidate mass law other than (5,1,1,1)/8, or the all-mixed (1,1,1,1)/4, cannot be produced by signs affine on every row's product coordinate face. In particular the previous genuine Boolean extremizer with masses(17,5,5,5)/32 necessarily uses a nonaffine Fourier sign in at least one row. Its existing truth table gives explicit four-cycle phase violations in two rows; this is a diagnostic, not a claim that every realization needs two violations.

The mixed class pays the full entropy as well. Its one nonfair row has marginal1/10 or9/10 on the unique split coordinate, the other three have marginal1/2 there, and every remaining physical data coordinate is deterministic in each conditional law. Thus H(F)=H(w)+(5/8)h2(1/10)+3/8=4-(9/8)log2(3). I_data>= (5/8)(1/10)+(3/8)(1/2)=1/4 and I_A>=1/2. Hence H(F)<= [16/3-(3/2)log2(3)] I(F), sharply in every data dimension. Extra deterministic character factors cost influence without increasing entropy. This argument retains the full conditional entropy and its actual physical-coordinate cost.

For pure affine-phase rows, each nonzero h_J is2 times a character on a coordinate subcube of codimension r_J. The cells partition the cube, w_J=2^-r_J, H(w)=sum w_J r_J, and each conditional row is uniform on a coordinate spectral face of dimension r_J. Therefore H(F)=2 sum w_J r_J <=4 I_data <=4 I(F). This pure character-cell estimate is a known special case of A034's quadratic affine-row result, included only to keep the full admitted class and terminal entropy explicit; no new priority claim is made.

The normalized non-Boolean control psi(x)=product_i(sqrt(15)+x_i)/4, independent of the addresses, has all-plus Fourier signs (affine phase), product spectral marginals1/16 and one address mass1, but Q=m while H(w)+I_A=0. It fails integer five-valued inverse admission, and its all-plus physical value exceeds1. Thus neither the payment nor classification follows from product magnitudes and affine phases alone. A Boolean product-spectrum tensor is itself fair on its active spectral face, but an arbitrary bent phase need not have affine Fourier signs and may leave this admitted class. Arbitrary Boolean tensor seeds are not admitted by this hypothesis; they remain a universal guard.

First unsupported line: extending the weighted payment from affine Fourier row signs to arbitrary common phases using 4h_J^2-h_J^4=3 indicator_M and primitive norm factors. Affine-factor gcd arguments cannot be applied after genuinely nonaffine sign changes: the inverse ceases to factor into independent linear terms. The old six-bit extremizer is an actual Boolean example of this precise limitation. No extension to all data dimensions with arbitrary phases, C018, or full FEI is asserted.
