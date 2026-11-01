# fleet02/B11 — four-bank Walsh overlap compiler for heavy null indefinite rank three

**Run:** `20260922T185213Z-fleet02-B11-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner-control revision at publication refresh:** `2026-09-22.12`  
**Assignment:** Indefinite signatures / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and first unpaid implication

The sole target remains: for independent real coordinates with one-dimensional densities bounded by one and any real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or give a genuine target-level counterexample.

The latest completed assigned-partner result, fleet03/B11 run `20260922T182528Z-fleet03-B11-QFORM-r12`, canonical source

`yspennstate/math-open-problems@e100de67669c37c8243fe9e389efc909f3179839`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T182528Z-fleet03-B11-QFORM-r12/REPORT.md`,

puts an exact-rank-three heavy null pivot into the spectral normal form

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]]`,

with `kappa>=s` and `det M=-kappa^2 c`, and proves a uniform density bound when the leakage form in the heavy spectral coordinate is supported on original coordinates disjoint from the transverse pair. It explicitly leaves `QFORM-OVERLAP-COMPILER-v1`: remove that support separation while preserving the original product law.

This run attacks that first implication directly. It proves a uniform theorem for a maximally overlapping but nontrivial four-bank Walsh class. In this class the leakage, saddle, and third spectral directions use exactly the same residual original-coordinate banks, so the partner's independence hypothesis fails as strongly as possible. The proof aggregates each bank first and then uses a scalar-pivot / indefinite-pair dichotomy. It does not assert that an arbitrary overlap geometry has this four-pattern structure.

## 2. Source-pinned supporting results used

1. **One-dimensional product projection cap.** fleet02/B11 canonical report `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2` proves: if independent `X_j` have densities at most one and `sum a_j^2=1`, then `sum a_j X_j` has density at most `sqrt(e)`.

2. **Orientation-free nonzero scalar-pivot theorem.** Interactive rank-two fusion canonical report `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, proves for an exact-rank-three matrix, after reduction to independent cap-one physical coordinates, that a nonzero physical pivot `a=A_ii` with range leverage `ell_i` gives

`||p_Q||_infinity <=128 [ell_i |a| |det M_3|]^(-1/4)`,

where `M_3` denotes the nonzero three-dimensional spectral matrix. Arbitrary induced affine terms are allowed.

3. **Arbitrary-rank physical indefinite-pair theorem.** Canonical report `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`, proves: if `s_3(A)>=sigma>0` and an original-coordinate principal pair `B` is invertible indefinite, with `D=|det B|` and `eta=sigma_min(B)`, then

`||p_Q||_infinity <=3*400^(1/3) (D^2 eta sigma)^(-1/6)`.

The logarithmic rank-two saddle envelope is retained in that proof and is averaged against a third-singular-value small-ball estimate.

All three statements are used only in their stated scopes. No conditional density after a rotation is asserted.

## 3. Four-bank Walsh overlap model

Fix `h in (1/2,1]` and write `alpha=sqrt(1-h)`. Split a set of residual ORIGINAL coordinates into four disjoint banks `G_1,...,G_4`. In bank `G_g`, choose coefficients of squared sum one and put

`Y_g=sum_{j in G_g} b_{g,j} X_j`, `sum_j b_{g,j}^2=1`.

The four `Y_g` are independent. By the one-dimensional projection theorem,

`||p_{Y_g}||_infinity <= K:=sqrt(e)`.

Let `X_0` be another independent original coordinate and define

`T = sqrt(h) X_0 + (alpha/2)(Y_1+Y_2+Y_3+Y_4)`,

`W = (Y_1+Y_2-Y_3-Y_4)/2`,

`V = (Y_1-Y_2+Y_3-Y_4)/2`.

The five coefficient rows in the spectral `(T,W,V)` coordinates are

`c_0=(sqrt(h),0,0)`,

`c_1=(alpha/2, 1/2, 1/2)`,
`c_2=(alpha/2, 1/2,-1/2)`,
`c_3=(alpha/2,-1/2, 1/2)`,
`c_4=(alpha/2,-1/2,-1/2)`.

If `C` is the `5x3` matrix with these rows, a direct Walsh cancellation gives

`C^T C=I_3`.                                                     (3.1)

Thus `(T,W,V)=C^T(X_0,Y_1,...,Y_4)` is a genuine Parseval three-dimensional projection. Notice that the leakage

`U=(alpha/2)(Y_1+Y_2+Y_3+Y_4)`

in `T=sqrt(h)X_0+U` has exactly the same four-bank support as `W` and `V`; there is no support separation unless `h=1`.

Let `M` be any real symmetric invertible `3x3` matrix of the partner's heavy-null form

`M=[[0,kappa,0],[kappa,d,e],[0,e,c]]`,                             (3.2)

and assume every singular value of `M` is at least `s>0`. Put

`Q=(T,W,V) M (T,W,V)^T`.

Because of (3.1), the corresponding `5x5` physical matrix

`B=C M C^T`                                                        (3.3)

has exactly the same three nonzero eigenvalues as `M`. Hence this is an exact-rank-three target form; the two possible indefinite signatures are interchanged by negation.

## 4. Density-cap normalization without losing the third spectral scale

The aggregated variables have caps `(1,K,K,K,K)`. Define

`D=diag(1,K,K,K,K)`, `Z=D(X_0,Y_1,...,Y_4)^T`.

Then the five coordinates of `Z` are independent and each has density at most one. In these coordinates

`Q=Z^T B' Z`, `B'=D^(-1) B D^(-1)`.                              (4.1)

Since `K>=1`, congruence by `D^(-1)` gives

`s_3(B') >= s/K^2 = s/e`.                                         (4.2)

For every bank index `g=1,...,4`, the heavy-to-bank coefficient is especially rigid. The first row of (3.2) is `(0,kappa,0)`, so

`|B'_{0g}| = sqrt(h) kappa/(2K)
            >= s/(2 sqrt(2e)) =: a_0`.                            (4.3)

Thus aggregation has converted the overlapping spectral geometry into four independent physical bank coordinates, each retaining a quantitative saddle coupling to the heavy coordinate.

We also need a lower bound on the physical range leverage of every bank coordinate after the cap normalization. Before normalization the range projection is `P=C C^T`, so

`P_{gg}=||c_g||^2=(3-h)/4 >=1/2`.                                 (4.4)

Let `ell=P_{gg}` and `u=P e_g`. Then `u` lies in `ran(B)=ran(C)`, `u_g=ell`, and `||u||^2=ell`. Hence `D^(-1)u` lies in `ran(B')`, has `g` coordinate `ell/K`, and norm at most `sqrt(ell)`. By the variational characterization of projection leverage,

`ell'_g >= (ell/K)^2/ell = ell/K^2 >=1/(2e)`.                     (4.5)

No eigenvector rotation of the independent variables has been made.

## 5. Main theorem: maximal four-bank overlap is uniformly controlled

### Theorem 5.1 — QFORM-FOUR-BANK-WALSH-OVERLAP-v1

Under Sections 3–4,

`||p_Q||_infinity < 609/s`.                                        (5.1)

In particular, at the target scale `s>=1`, the density is bounded by the universal constant `609`, uniformly over the number of original coordinates in each bank, all cap-one input laws, all normalized bank coefficient vectors, all `h in (1/2,1]`, and all `d,e,c` compatible with (3.2) and the spectral lower bound.

### Proof

For a bank index `g`, put `a_g=B'_{0g}` and `b_g=B'_{gg}`. By (4.3), `|a_g|>=a_0` for every `g`.

**Case 1: a bank has a nontrivial scalar pivot.** Suppose `|b_g|>=a_0` for some `g`. Apply the exact-rank-three nonzero scalar-pivot theorem to coordinate `g`. Equations (4.2) and (4.5) imply that the product of the three nonzero singular values of `B'` is at least `(s/e)^3`; hence

`||p_Q||_infinity
 <=128 [ell'_g |b_g| |det_nonzero(B')|]^(-1/4)`
` <=128 [(1/(2e)) (s/(2sqrt(2e))) (s/e)^3]^(-1/4)`
` =128 sqrt(2) e (2e)^(1/8) s^(-1)`
` <608.045/s`.                                                     (5.2)

**Case 2: every bank scalar pivot is small.** Suppose instead `|b_g|<a_0` for all four banks. For any `g`, the physical principal pair on coordinates `{0,g}` is

`[[0,a_g],[a_g,b_g]]`.

Its determinant is `-a_g^2`, so it is invertible indefinite. Its smaller singular value is

`eta_g=(sqrt(b_g^2+4a_g^2)-|b_g|)/2 >= |a_g|/2 >=a_0/2`,           (5.3)

where the first inequality uses `|b_g|<a_0<=|a_g|`. Its determinant magnitude is `D_g=a_g^2>=a_0^2`. Apply the arbitrary-rank physical-pair theorem to `B'`, using (4.2):

`||p_Q||_infinity
 <=3*400^(1/3) [D_g^2 eta_g (s/e)]^(-1/6)`
` <=3*400^(1/3) [a_0^5 s/(2e)]^(-1/6)`
` <105.749/s`,                                                     (5.4)

because `a_0=s/(2sqrt(2e))`. Cases 1 and 2 prove (5.1). QED.

The proof is deliberately an aggregate-before-inversion argument. It does not choose one original residual coordinate; it first turns an arbitrarily large bank into one independent scalar coordinate, pays its density cap by scaling, and only then invokes a pivot or pair theorem.

## 6. How the third direction removes the rank-two logarithm here

The opposite-sign rank-two obstruction remains real. If a two-dimensional saddle `(S,W)` has a joint density bounded below on a neighborhood of the origin, the density of `2SW` contains the hyperbolic Jacobian integral

`int g(u,z/(2u)) du/(2|u|)`,

which diverges logarithmically as `z->0`. In particular, product uniform examples give the familiar logarithmic singularity. Nothing in this report promotes rank two to bounded density.

In the four-bank rank-three model, the third spectral direction is encoded in the fact that `B'` has three nonzero singular values at least `s/e`. After bank aggregation it forces one of two quantitative payments:

- either a bank diagonal survives, and its nonzero scalar curvature is coupled to a range leverage at least `1/(2e)` and the full rank-three determinant; the half-Riesz scalar-pivot theorem makes the logarithmic saddle summable;
- or all bank diagonals are smaller than the already-forced heavy-to-bank coupling, making an original-coordinate bank pair uniformly indefinite; the full-matrix pair theorem then averages the same logarithmic pair envelope against the Schur remainder whose norm is protected by the third singular value.

Thus in this genuinely overlapping family the third direction removes the rank-two logarithm through an explicit **pivot-or-pair alternative after product-preserving bank aggregation**, not through fictitious independence of `(T,W,V)`.

## 7. Source-valid falsifier of one-coordinate overlap resolution

The four-bank theorem also gives a family that defeats another tempting local mechanism. Take `h=3/4`, the canonical matrix

`M=[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{1,1,-1}`. In each of the four banks let

`Y_g=m^(-1/2) sum_{k=1}^m X_{g,k}`.

At the aggregated five-coordinate level, `C^T C=I_3`, the four bank leverages are all `9/16`, and the heavy-to-bank coefficients have magnitude `sqrt(3)/4`.

At the original `(4m+1)`-coordinate level, however, every heavy-to-residual coefficient has magnitude

`sqrt(3)/(4 sqrt(m)) ->0`,

and every one-residual-coordinate principal saddle determinant is of order `1/m`. Meanwhile the leakage `U`, saddle form `W`, and third form `V` all use every residual bank. Thus overlap is genuine and every one-coordinate local pair deteriorates, yet Theorem 5.1 remains uniform in `m`.

This is a counterexample to the proof mechanism

`overlap -> choose one residual original coordinate -> pay a fixed local pair/minor`,

not a counterexample to QFORM. The correct object in this family is the grouped bank.

## 8. First unpaid implication after this run

The remaining overlap compiler is now more precise. For a general heavy-null Parseval frame, residual coefficient rows have continuously varying transverse directions; they need not lie in the four exact Walsh patterns used here. Prove a **finite-sector grouped-coordinate reduction** that, without changing the product law, either

1. extracts finitely many disjoint normalized banks whose coefficient directions are quantitatively close enough to a controlled Walsh/grouped model for a pivot-or-pair payment;
2. enters an existing diffuse/ridge branch; or
3. produces a quantitatively conditioned physical indefinite pair directly.

The difficult point is stability under within-sector variation: one may not rotate or condition the grouped variables and then assert independence. Arbitrary additional spectrum beyond exact rank three remains a separate nonseparable debt, although the pair theorem itself already tolerates it once a quantitative pair is found.

## 9. Exact symbolic regression

`VERIFY.py` checks the canonical `h=3/4` model exactly. It verifies `C^T C=I_3`, spectrum `{-1,1,1,0,0}` for the aggregated physical matrix, four bank leverages `9/16`, heavy-to-bank coefficients `+/-sqrt(3)/4`, and bank diagonals `{1/2,1/2,0,0}`. It also evaluates the universal constants in (5.2)–(5.4). The output terminates `QFORM_FOUR_BANK_WALSH_OVERLAP_CHECK_PASS`.

The computation is algebraic regression only; Theorem 5.1 is the symbolic argument above.

## 10. Status

`ESSENTIAL_STEP_APPLIED`. A genuinely overlapping arbitrary-size indefinite rank-three subclass is uniformly solved, and one-coordinate overlap resolution is rigorously falsified as a universal proof mechanism. The unrestricted arbitrary-frame, arbitrary-spectrum conjecture remains `OPEN / NOT PROVED`. No continuity claim is made here.
