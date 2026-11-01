# Integer profile admission forbids exclusive inherited ownership

All inputs are physical independent Bernoulli bits. Let p_i be strictly between zero and one, v_i=4p_i(1-p_i), and let P be the squared orthonormal product Fourier spectrum. Logarithms below are natural; no entropy sign relies on floating arithmetic.

## 1. The minimum variance is an admission condition

For every integer z, z(z-1)>=0. Consequently any integer-valued random variable W of finite second moment and mean m in (0,1) satisfies

    Var(W) >= m(1-m).

Equality holds precisely when W is supported on {0,1}. This follows by taking the expectation of W(W-1), then subtracting m^2. The probability space may be arbitrary: changing the space, signs, or higher moments cannot lower this minimum while preserving the mean and integer values. A constant real variable W=m shows why the integer hypothesis matters. At m=0 or 1 the strictly positive lower bound disappears.

## 2. All-dimensional actual Boolean obstruction

Fix any d>=3 and any independent interior biases. The Boolean sign

    f_d(x)=2 product_{j=1}^d x_j -1

is an actual AND gate, with no repeated input variables. For S_i=[d]\{i}, define the genuine integer cofactor profile

    Z_i(x_i)=(1/2) sum_{b in {0,1}^{S_i}} (-1)^(d-1-|b|) f_d(b,x_i).

The constant part sums to zero. Only b=all ones contributes to the product term, so Z_i(x_i)=x_i exactly. Thus its mean is p_i and its variance is p_i(1-p_i). The full packet is positive and is the ONLY strict superset of S_i. Direct product expansion gives

    P([d])=4 product_j p_j(1-p_j),
    P(S_i)=4 p_i^2 product_{j!=i}p_j(1-p_j),
    [4^(d-2)/v_{S_i}] P([d])=p_i(1-p_i).

Now suppose an ownership proposal retains every inherited mean p_i and retains integer-profile admission, but allocates a nonnegative fraction lambda_i of that unique strict-superset packet to the i-th profile. In exact terms it asserts the existence of integer-valued W_i with

    E W_i=p_i,
    Var(W_i)=[4^(d-2)/v_{S_i}] lambda_i P([d]).

The minimum-variance condition forces lambda_i>=1 for EVERY i. Therefore sum_i lambda_i>=d. No exclusive allocation (sum_i lambda_i<=1), nor an allocation with any fixed dimension-independent total cap, can preserve all those inherited integer profiles. This is an admission obstruction, before applying a logarithmic payment inequality. It does not show that the actual entropy needs this excessive budget.

The d-fold owner count is NOT an unbounded ratio to the packet's degree-deficit weight d-1: d/(d-1)<=3/2 for d>=3. In particular, the corresponding raw local variance charges 2d P([d]) are at most 3(d-1)P([d]). Thus this example leaves degree-weighted shared funding viable. A single complete reference need not consist of exclusive integer-profile fragments. Those distinctions are essential: this theorem does not refute the campaign's general O(Delta) ownership target.

The first nontrivial pair instance is AND3: all three pair profiles require the whole triple variance. At fair biases each pair has m=1/2, Var=1/4, P(pair)=P(triple)=1/16. Deleting the triple from one pair profile gives the constant real profile 1/2. Its integer admission fails, and h(1/2)=(ln4)/4>0 while its retained variance is zero. Equivalently the pair residual E_pair-ln4 P(pair)=(ln4)/16 is strictly positive. At lambda=1/3 the retained variance is 1/12, also below the necessary 1/4. Even an arbitrary new probability space cannot restore the claimed integer profile at that mean and variance.

## 3. Normalizing the spectral deletion does not restore a Boolean gate

For fair AND3 the empty Fourier mass is 9/16 and every nonempty mass is 1/16. Delete the triple and normalize by the remaining mass 15/16. The empty mass becomes 3/5. A Boolean sign on the same fair three-bit cube has mean (j-4)/4 for an integer j from 0 through 8. None of those means has square 3/5. The normalized deleted law is therefore NOT the Fourier law of any Boolean gate on the inherited cube, regardless of Fourier phases. This statement is stronger than rejection of the inherited inverse transform alone.

This spectral conditioning is not a physical restriction. Fixing one AND input to zero produces a constant; fixing it to one produces AND on the remaining inputs with their original biases. Those physical operations change the complete coefficient list coherently. Conditioning the Fourier set not to equal [3] does neither.

## 4. Boundary and repeated-wire scope

The positive lower bound and division by v_{S_i} use interior biases exactly where stated. Deterministic coordinates contract first. At p_i=0 or 1 the corresponding integer profile is constant and its variance vanishes; no positive-fraction conclusion is made for that profile. Fixed face and corner certificates check Parseval after contraction.

Repeated wires must be identified physically. AND(X,X,Y)=AND(X,Y), whose mean at p_X=1/3,p_Y=2/5 is -11/15. Treating the two X occurrences as independent gives mean -41/45. Their squared empty masses are 121/225 and 1681/2025 respectively. No independent three-wire product transform describes the repeated-wire physical gate. These are exact rational checks, independent of the ownership theorem.

## 5. What survives and the exact unpaid step

A044's original physical integer-profile inequality remains valid and keeps its whole strict-superset mass for each profile. Its previously accepted proof is not repaired or re-reviewed here. A041's normalized pointwise max of complete quadratic references is also not refuted: it never promises that each selected part is an independently realizable Boolean gate or an integer cofactor profile. A non-Boolean conditional law can still be a legitimate reference.

The obstruction excludes simultaneous preservation of all inherited profile means, integer admission, strict-superset-only Parseval funding, and bounded nonnegative packet ownership. A method may change or omit profiles, merge complete references, exploit signed residuals, or use other actual energy, but it must then rederive its payment and include the omitted coefficient and terminal costs. It cannot simply inherit A044's integer lemma after splitting packets.

The next unpaid line is a complete-reference cross-entropy bound, with the full normalizer, off-support mass, ordinary KL law and terminal entropy retained. This stage proves no all-dimensional entropy bound and supplies no FEI counterfamily. The all-dimension statement above concerns the failed ownership mechanism, not the conjecture.
