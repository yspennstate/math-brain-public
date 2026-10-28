# A024 v5: affine-flat repair and sharper physical mean transport

Author proof; independent reconstruction pending. All entropy is in bits.
Physical inputs are independent uniform bits. No conditioning on hidden outputs.

## 1. Sharper scalar entropy bound, all real a,b

Write e(s)=-s log_2 s, e(0)=0, and
L(a,b)=e(a^2)+e(b^2)-e(a^2+b^2). Then

    0 <= L(a,b) <= 2|ab|.                                      (1)

For ab=0 this is immediate. Otherwise divide the natural-log numerator by
|ab| and put x=|a/b|. The resulting function is

    F(x)=x ln(1+x^-2)+x^-1 ln(1+x^2).

It satisfies F(x)=F(1/x). For x>=1, set t=x^2 and
g(t)=ln(1+t)-t ln(1+1/t). Direct differentiation gives
F'(x)=-g(t)/t and g'(t)=2/(1+t)-ln(1+1/t).
For z in [0,1], h(z)=2z/(1+z)-ln(1+z) has h(0)=0 and
h'(z)=(1-z)/(1+z)^2>=0. Hence g'(t)=h(1/t)>=0, g(1)=0,
and F is nonincreasing on [1,infinity). Its maximum is F(1)=2 ln 2.
Dividing by ln 2 proves (1). Nonnegativity is the binary-entropy identity.
Equality holds when |a|=|b| (and at either zero endpoint).

For arbitrary disjoint Boolean w,h and binary activation
F=1-(1-w)(1-h)/2, a=Ew, r=Pr(h=-1), beta=(Ew_0-Ew_1)/2,
the previously reconstructed exact physical identity is

    d_F=r d_w, B_i(F)=r B_i(w)+R_r(a,beta),
    R_r=L(1-r+ra,r beta)+r(1-r)L(1-a,beta)-r L(a,beta).

Using (1), dropping only the nonpositive final term, |1-r+ra|<=1,
|1-a|<=2 and |beta|<=d_w gives

    R_r <=2r|beta|[|1-r+ra|+(1-r)|1-a|]
         <=6r|beta|<=6r d_w.                                 (2)

This improves v3's constant9 to6 for EVERY disjoint Boolean pair, without
denominators in r, means, or output variances. It is a signed upper bound,
not a claim that R is nonnegative. Deterministic r=0,1 give exact R=0.
Physical restrictions leave untouched inputs uniform even though changed
inner-output means bias the outer inputs. Corrected FEI+ is
sum_{S nonempty} p_mu(S) log_2(product_{i in S}(1-mu_i^2)/p_mu(S));
there is NO output-variance numerator. Contract deterministic children first.

## 2. Quadratic phases edited on arbitrary affine flats

Let A be empty or ANY affine subspace of F_2^D, and let q have degree<=2.
Consider f(x)=(-1)^{q(x)+1_A(x)}. Global signs and arbitrary affine terms
are allowed. Fair coordinate restrictions preserve this family: an affine
linear system restricts to another affine system, or becomes inconsistent;
q restricts to a polynomial of degree<=2. Every actual adaptive path fixes
only revealed physical bits, so this closure applies at every history leaf.

If A is empty, f is a quadratic phase. Each derivative is constant or a
nonconstant affine phase, so each coordinate influence belongs to {0,1/2,1}.
Every coordinate satisfies B_i<=2d_i (B_i=0 at d_i=0).

If A has codimension k<=2, choose k independent equations ell_j(x)=b_j.
Over F_2 its indicator is product_j(1+ell_j(x)+b_j), of degree<=2.
Absorb this indicator into q, using x_i^2=x_i. The result is again a pure
quadratic phase. This includes k=0, where A is the whole cube and only
the global sign changes. These dense-edit cases must NOT use the sparse bound.

Suppose now k>=3. If q has a quadratic edge, select an incident coordinate.
The unedited influence is1/2. Editing A changes pivotal status only across
edges crossing A, a proportion at most2 Pr(A)=2^(1-k)<=1/4. Hence d_i>=1/4
and B_i<=h_2(d_i)<=1<=4d_i. This does not require A to be coordinate-aligned.

If q is affine, let V be the direction space of A, W=V^perp (dimension k),
and u=2^(1-k). For the defect (-1)^{1_A}, Fourier coefficients are1-u at
the empty set, zero outside W, and magnitude u at every nonzero member of W.
This follows by summing characters over a coset: the sum is zero outside
the annihilator, and equals |A| times the coset character inside it.
If the coordinate vector e_i is not in W, no spectral fiber {S,S+e_i}
contains two points of W. Consequently B_i=0. If e_i is in W, there are
2^(k-1)-1 pairs not containing0, giving exactly

    B_i=2u(1-u)+L(1-u,u)<=4u(1-u).                            (3)

In this second case the coordinate influence is u, or 1-u after multiplying
by the affine character. Character translation preserves B_i, while it may
COMPLEMENT influence. Thus (3) is B_i<=4d_i(1-d_i)<=4d_i. The coset offset
changes only coefficient signs. No coordinate-basis change is being queried.

Every residual therefore admits a complete physical continuation whose selected
queries have B_i<=4d_i, independently of D, k, flat orientation and dimension.
Two arbitrary edited vertices form an affine line, so all two-point edits are
included. They need not be adjacent. The result includes arbitrary-width
single-point edits and improves their previous K5 continuation to K4.

## 3. Actual disjoint composition and unchanged original credit

Disjoint products of these factors tensorize their squared Fourier laws:
coordinate B and influence equal those in the corresponding factor. Constants
are harmless. Thus the same K4 policy applies to any finite product, at every
fair physical residual. For an OR of any finite number of disjoint such
products w_j, group all other inputs into h. At a query of w_j, (2) gives

    B_i(F)<=r*4d_i(w_j)+6r*d_i(w_j)=10d_i(F).                 (4)

Only the mean of h enters (2); h needs no structural hypothesis. Here
r=product_{ell!=j} Pr(w_ell=-1) uses actual disjointness. Arbitrary fan-in
adds no factor. Constant absorbing outputs stop the continuation. Sign changes
also yield the analogous AND statement. This is not an arbitrary outer-gate
theorem. It remains valid when inner-output means approach a dictator or a
deterministic limit: no rare log(1/r) is left in the scalar remainder.

After ANY already-executed physical stopping prefix, execute this continuation
at each actual nonconstant leaf. At K=10 the ADDITIONAL bad-node odd-face debit
is identically zero. The old booked debit U and original bank R are unchanged;
no bank is renewed and no earlier debit is claimed paid by this theorem.
The exact prefix equalities retain both FULL actual child functions:

 H(F)=sum_prefix p_v[H(F_v)-(H(F_v0)+H(F_v1))/2]+sum_l p_l H(F_l),
 I(F)=sum_prefix p_v d_v+sum_l p_l I(F_l).

The inherited B05 localization with c_JS=2/ln2 yields H<=7I for a product,
and H<=13I for its stated OR/AND composition. Constants have equality0.
Both leaf entropies are resolved with remaining influence, not erased. No
old prescribed-component-tree Phi identity is asserted for the reordered tree.

## 4. Universal distinguished-fiber credit, with no reference reset

For EVERY Boolean f, coordinate i and Fourier subset T not containing i, write

 a=hat f(T), b=hat f(T union {i}), d=Inf_i(f),
 A=1-d-a^2, D=d-b^2, W=A*D.

Both A,D are nonnegative: they are the squared spectral energies in the two
coordinate halves after removing this distinguished fiber. Pairing Fourier
subsets, applying (1) on all other fibers, and then Cauchy--Schwarz gives

 B_i(f) <= L(a,b)+2 sum_{S!=T, i notin S}|hat f(S)hat f(S union {i})|
        <= L(a,b)+2 sqrt(W) <=2d+2 sqrt(W).                    (5)

For the final inequality, |a|<=1 and |b|<=d: the latter is the Fourier
coefficient of the physical derivative, which has absolute value1 exactly
on the pivotal inputs and0 elsewhere. This holds for ANY T not containing i,
not just the empty Fourier subset. No Fourier mean is divided out.

This is a pointwise certificate for the EXISTING physical query. Selecting T
in (5) changes neither the actual function nor any paid reference distribution.
It is not a physical modulation, change of input measure, or reference reset;
it cancels no old KL charge. In the empty-fiber case a=Ef, b=hat f({i}),
A=Var(f)-d. Near a chosen character the missing energy A supplies the mismatch
rebate explicitly. For K>=2, the sufficient good-query certificate is

    4W <= (K-2)^2 d^2  ==>  B_i<=K d.                        (6)

On any actual physical tree choose one T_v per node; put W_v as above using
that node's ACTUAL residual spectrum. The inherited local entropy increment
bound Delta H_v<=B_v+(2/ln2)d_v and the exact telescopes imply

 H(f) <= (2+2/ln2)I(f)+2 sum_all_nodes p_v sqrt(W_v)

for complete constant-leaf trees. More usefully, for K>=2 the localized bill is

 H(f) <= (K+2/ln2)I(f)
       +sum_{B_v>Kd_v} p_v[2sqrt(W_v)-(K-2)d_v].              (7)

Each bracket in the last sum is positive by (5). For a stopping prefix retain
the extra full terminal term sum_l p_l H(f_l) and replace I(f) on the right
by the SPENT prefix influence sum_prefix p_v d_v. Both complementary terminals
remain actual functions. No independence across nodes or renewed credit is used.

Thus (7) identifies one exact sufficient unpaid credit for C019/C020: choose a
tree and fibers whose total LOCALIZED overlap liability is O(I). It is not a
proof that this price is finite universally. A cruder density-only substitute
can reintroduce the rare logarithmic gap. For affine-flat defects the support
fibers are empty or have the point-defect energies, which is why the repair
above closes without a new bank. General spectra need the actual overlap bill.

## 5. Exact first unsupported universal line

For a general edit set E, the density/boundary estimate still gives a large
quadratic pivot while its density is<=1/8. Once q becomes affine, the edit
spectrum need not be supported on one annihilator with equal nonzero weights.
The fiber formula (3) is then unsupported. A union of affine flats generally
has interference and overlap and cannot be assigned independent new banks.
Taking q constant and arbitrary E includes every Boolean function. A claim
of hereditary uniformly good physical continuations at that step is the first
unproved universal line. The alternative universal route also remains open:
no universal influence price for the
localized liability in (7) has been proved. Old-prefix payment and arbitrary
outer gates remain separate unpaid obligations. Full FEI remains OPEN.
