# fleet02/B06 — angle-free double-null square receiver

Run `b06-20260923T140913Z-d5217c7f4886`. Programme `QFORM-DENSITY-3EIG-20260922`. Full conjecture remains OPEN.

## Sources actually consumed



Required pinned Claude source read at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: updated `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

## 1. Scalar negative-moment lemma

If a real random variable W has a density bounded by L and 0<s<1, then

`E |W|^{-s} <= (2L)^s/(1-s)`.

Proof. By the bathtub principle, among densities bounded by L and of mass one the integral against the symmetric decreasing weight |x|^{-s} is maximized by density L on `[-1/(2L),1/(2L)]`. Hence

`E|W|^{-s} <= 2L int_0^{1/(2L)} x^{-s} dx = (2L)^s/(1-s)`.

No support or moment hypothesis is used.

## 2. Finite-Lp shared-double-null theorem

### Theorem `QFORM-DOUBLE-NULL-LP-v1`

Let X,Y be independent real random variables with densities at most one. Let Omega be independent of (X,Y). Let U=U(Omega), V=V(Omega), R=R(Omega), with U and V each possessing scalar densities bounded by L_U and L_V, respectively; U and V may be arbitrarily dependent. Put

`T = 2 X U + 2 Y V + R`.

Then for every p>1,

`||p_T||_p <= p (L_U L_V)^((p-1)/(2p))`.

In particular

`||p_T||_3 <= 3 (L_U L_V)^(1/3)`.

### Proof

Condition on Omega and write u=U, v=V. For u,v nonzero, the density h_{u,v} of `2uX+2vY` satisfies `||h||_1=1` and, by Young `L^2*L^2 -> L^infty`,

`||h||_infty <= ||p_{2uX}||_2 ||p_{2vY}||_2 <= 1/(2 sqrt(|uv|))`,

because `int f_X^2 <= int f_X =1` and similarly for Y. Interpolating L1 and Linfinity, with theta=1-1/p,

`||h||_p <= 2^{-theta}|uv|^{-theta/2}`.

Minkowski for the mixture over Omega gives

`||p_T||_p <= 2^{-theta} E |UV|^{-theta/2}`.

No independence between U and V is used. Cauchy-Schwarz and the scalar lemma at exponent theta give

`E|UV|^{-theta/2}`
` <= (E|U|^{-theta} E|V|^{-theta})^{1/2}`
` <= 2^theta p (L_U L_V)^{theta/2}`.

The powers of 2 cancel, proving the theorem.

This is the weighted product-structure replacement for the forbidden worst-fiber supremum: each conditional fiber can blow up as `|uv|^{-theta/2}`, but the actual product-derived coefficient laws pay the singularity after averaging.

## 3. Translation-uniform square norm

If Z has density at most one, a is nonzero, and c is arbitrary, the density g of `a(Z+c)^2` obeys

`||g||_{3/2} <= 2 |a|^{-1/3}`.

Indeed, `g(w) <= (|a||w|)^(-1/2)` on the appropriate half-line. Therefore

`int g^{3/2} <= |a|^{-1/4} int g(w)|w|^{-1/4}dw`
` = |a|^{-1/2} E|Z+c|^{-1/2}`
` <= 2 sqrt(2) |a|^{-1/2}`,

again by bathtub, and raising to the `2/3` power yields the claim.

The shift c may be any value fixed by an independent background; no support assumption is made.

## 4. Main result: angle-free square bridge

### Theorem `QFORM-DOUBLE-NULL-SQUARE-L3-BRIDGE-v1`

Let X,Y,Z be mutually independent cap-one variables and independent of a background Omega. Let U,V,B,R be arbitrary measurable functions of Omega. Assume only that U and V have marginal density caps L_U,L_V. For a nonzero real a, define

`Q = 2 X U + 2 Y V + a Z^2 + 2 B Z + R`.

Then Q has an essentially bounded density and

`||p_Q||_infty <= 6 (L_U L_V/|a|)^(1/3)`.

U and V may be perfectly collinear, may share every background coordinate, and need not have a joint density.

### Proof

Condition on Omega. Complete the Z-square:

`aZ^2+2BZ = a(Z+B/a)^2 - B^2/a`.

The anchor sum `2uX+2vY` has, by the preceding conditional estimate at p=3,

`||p_{2uX+2vY}||_3 <= 2^{-2/3}|uv|^{-1/3}`.

The translated square has `L^{3/2}` norm at most `2|a|^{-1/3}`. Young `L^3*L^{3/2}->L^infty` therefore gives the conditional bound

`||p_{Q|Omega}||_infty <= 2^{1/3}|a|^{-1/3}|UV|^{-1/3}`.

Average this genuine singular fiber. Cauchy-Schwarz plus the scalar negative-moment lemma at exponent 2/3 gives

`E|UV|^{-1/3}`
` <= (E|U|^{-2/3}E|V|^{-2/3})^{1/2}`
` <= 3*2^{2/3}(L_U L_V)^{1/3}`.

Multiplication by `2^{1/3}|a|^{-1/3}` gives exactly 6.

The proof never takes a conditional density supremum over the background and never rotates the input law.

## 5. Physical-coordinate corollary

Let A be symmetric. Suppose original physical coordinates i,j,k satisfy

`A_ii=A_jj=A_ij=A_ik=A_jk=0`, `A_kk=a !=0`.

Let W be all other original coordinates and define the two complete anchor row norms into W

`alpha = (sum_{l notin {i,j,k}} A_il^2)^(1/2)`,
`beta  = (sum_{l notin {i,j,k}} A_jl^2)^(1/2)`.

All other entries of A are arbitrary. Then the full form can be written exactly in the theorem's shape with

`U=sum A_il W_l`, `V=sum A_jl W_l`, `B=sum A_kl W_l`.

Using the existing product-affine projection bound `||p_{c dot W}||_infty <= sqrt(e)/||c||_2`,

`L_U <= sqrt(e)/alpha`, `L_V <= sqrt(e)/beta`.

Hence

`||p_{X^T A X}||_infty <= 6 (e/(|a| alpha beta))^(1/3)`.

This is angle-free: no determinant or area of the two anchor coefficient rows appears.

## 6. Application to partner fleet03/B06 r38

Partner r38, using its preceding r37 aggregate-anchor result on the fresh absolute cut, records

`||C||_F > L0 = 0.04453127861416...`,

for `C=bD-cr^T`, and at the exact zero cross-anchor endpoint b=0 one has exactly

`C=-cr^T`, so `||C||_F=||c|| ||r||`.

Therefore, in the r38 zero-anchor endpoint, on the physical subbranch where a third original coordinate supplies an uncoupled square `|a|>=1`, the complete anchor row norms satisfy

`alpha beta >= ||c|| ||r|| = ||C||_F > L0`.

The theorem gives the real target-level inequality

`||p_Q||_infty < 6 (e/L0)^(1/3) = 23.6244128006...`.

Thus the exact-collinear/shared-coefficient obstruction is fully paid in this decoupled-third-square subbranch, even though the two anchor coefficient rows may have zero angle. The partner's aggregate cofactor currency is consumed before any local reciprocal minor is selected.

## 7. Application of the required pinned Claude result

The pinned `RESULTS.md` at `e5f71d79...` proves that every invertible physical 2x2 principal block B with `|det B|>=D` and `sigma_min(B)>=kappa` yields a bounded density depending only on (D,kappa), with arbitrary remaining coefficients, under the three-large-eigenvalue hypothesis.

Apply this to a coupled third direction and one null anchor. The physical pair block is

`B=[[0,c],[c,a]]`.

Its determinant magnitude is `c^2`, and

`sigma_min(B) = (sqrt(a^2+4c^2)-|a|)/2`
`             = 2c^2/(sqrt(a^2+4c^2)+|a|)`.

Hence for any fixed delta,M>0, the branch `|c|>=delta`, `|a|<=M` is already paid by the pinned physical-pair theorem with

`D=delta^2`,
`kappa >= 2 delta^2/(sqrt(M^2+4delta^2)+M)`.

This is a genuine reduction of the remaining coupled-third-direction debt: after the new angle-free decoupled-square theorem and this pinned physical-pair exit, a hard coupled branch may be restricted to small anchor-third couplings relative to the third diagonal scale, rather than all coupled configurations.

The pinned `COUNTEREXAMPLE_SEARCH.md` ruled one-sheet theorem and the Fourier report's square/hyperbola peels remain compatible but are not needed to prove the new theorem above.

## 8. Route counterexample: why the third square cannot be completed through the anchors

The theorem's independence structure is essential. It cannot be extended by letting the square translation depend arbitrarily on the same physical anchors. For independent cap-one `X,Z ~ Unif[-1/2,1/2]`,

`(Z+X)^2`

has an unbounded density at zero: `Z+X` has triangular density positive at zero, and squaring creates a `s^{-1/2}` singularity. Thus a statement asserting a translation-uniform `L^{3/2}` square norm after replacing the background shift by an anchor-dependent shift is false. This is a route counterexample only, not a QFORM counterexample: the displayed quadratic form has rank one.

## 9. First unpaid implication

`QFORM-NEAR-COLLINEAR-COUPLED-THIRD-DIRECTION-v2`:

After removing (i) transverse shared-coefficient rows by the previous joint-reciprocal theorem, (ii) exact/near-collinear rows with an uncoupled physical third square by the theorem above, and (iii) quantitatively nondegenerate null-anchor/third-coordinate physical pairs by the pinned physical-block theorem, prove that the residual small-coupling/high-third-diagonal branch either admits a product-preserving perturbative version of the L3 square bridge or routes into an already-paid volume, ridge, physical-pair, mixed-hub, or grouped-bank receiver.

The obstruction is precise: completing the third square when `A_ik` or `A_jk` is nonzero produces a shift depending on X or Y, so the independent `L^3 * L^{3/2}` convolution is lost. Small matrix norm alone cannot be treated as a small random perturbation for unbounded input laws. The next proof must preserve the physical product variables while using the small coupling structurally.

## Status

Supporting theorem proved; one partner result and one required pinned-Claude result applied at actual inequalities. No counterexample to the full conjecture was found. Essential boundedness only; continuity not claimed. Execution remains `WITHOUT_VERIFIED_BRAIN` because repository retrieval/publication is not verified native learned-memory receiver use.
