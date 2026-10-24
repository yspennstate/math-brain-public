SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T14:23:15Z.
attacking: the newest second-anchor critical-stable-rank collar by converting one-sided anchored Schur energy concentration into an exact-rank-three physical slice, and forcing the failure branch to be genuinely double-diffuse.

# account01/B02 r31 — second-anchor slice-or-double-diffuse Fourier receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** `VERIFIED_BRAIN` in the narrow protocol sense: authenticated repository retrieval occurred and the newest designated-partner result was actually used below. `full_brain_connected=false`; no native learned-memory population is claimed.  
**Continuity:** proved on the new Fourier-L1 branches below; full-target continuity remains open.  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`.

The owner target remains unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, iid, Gaussian, log-concavity, diagonal-basis-independence, or post-rotation-independence assumption is inserted.

## 1. Fresh sources actually used

Fresh control remained QFORM-only, owner revision `2026-09-22.15`.

The newest designated partner available during this run is account02/B02 at

`yspennstate/math-open-problems@4029b9b55694ce709e43c62d2729e89108fbdede`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T141147Z-account02-B02-QFORM-auto11/REPORT.md`.

It combines physical-anchor Plancherel with degree-five sharp Hausdorff--Young volume control. On the invertible second-anchor branch produced by its predecessor, one has an ORIGINAL-coordinate physical `2 x 2` cross anchor `P`,

`D=|det P|`,
`S=M-C P^(-1) R`,
`G=D^2 ||S||_F^2 > Z/24`,                                      (1.1)

where `Z=E3(B)` is the third exterior volume of the parent physical cross block. The newest partner theorem proves a genuine Fourier-L1 exit whenever

`rho:=sr(S)=||S||_F^2/||S||op^2 >=5/2`,                         (1.2)

with

`||p_Q||inf <15.665527 G^(-1/6) <26.606039 Z^(-1/6)`.          (1.3)

Tracking its displayed `|t|^(-9/8)` envelope gives the corresponding explicit integrated-Fourier estimate

`int_R |phi_Q(t)|dt <98.429408 G^(-1/6)
                    <167.170668 Z^(-1/6)`.                      (1.4)

The same partner report records the singular-second-anchor analogue: choosing a genuine scalar physical pivot `p` gives a scalar cross-Schur residual `S1` and

`H=p^2 E2(S1)>Z/24`;                                             (1.5)

when `sr(S1)>=5`, its degree-six interpolation gives a genuine L1 exit.

I also use the completed exact-rank-three physical-cross-block theorem from

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T230126Z-account03-B02-QFORM-r17/REPORT.md`:

if an ORIGINAL-coordinate physical cross block `C` has rank exactly three, then

`int_R |phi_Q(t)|dt <=12 pi E3(C)^(-1/6)`,
`||p_Q||inf <=6 E3(C)^(-1/6)`,                                  (1.6)

with arbitrary same-bank curvature, outside couplings and affine terms retained. This is the receiver used below.

No small Schur tail is deleted. The Schur shear is used only for coefficient identities; probabilistic conditioning remains in ORIGINAL coordinates.

## 2. Exact one-column / one-row anchored slice identity

Write the invertible physical second-anchor block as

`B=[[P,R],[C,M]]`,                                                (2.1)

and let

`S=M-C P^(-1)R`, `D=|detP|`, `F=||S||_F^2`, `G=D^2F`.            (2.2)

Assume `F>0`. Define normalized Schur row and column energies

`a_i=||S_i:||_2^2/F`, `b_j=||S_:j||_2^2/F`,                     (2.3)

and

`h_r=max_i a_i`, `h_c=max_j b_j`, `h=max(h_r,h_c)`.             (2.4)

For a residual physical column `j`, let `C_j` be the literal ORIGINAL-coordinate cross block obtained by keeping **all** source-bank rows but only the two physical pivot columns together with column `j`. Thus `C_j` has exactly three columns.

For every residual physical row `i`, the `3 x 3` minor using the two pivot rows and residual row `i` satisfies

`det C_j[{pivot rows} union {i},:]
   =det(P) S_ij`.                                                 (2.5)

This is the ordinary block determinant identity. Summing the squares of all `3 x 3` minors of `C_j` and retaining only these anchored minors gives, by Cauchy--Binet,

`boxed:
 E3(C_j)=det(C_j^T C_j)
       >=D^2 sum_i |S_ij|^2
       =b_j G.
}`                                                                 (2.6)

If `b_j>0`, (2.6) shows `rank(C_j)=3` because `C_j` has exactly three columns. Hence the exact-rank-three Fourier theorem (1.6) applies to an actual physical cross block:

`int |phi_Q| <=12pi (b_jG)^(-1/6)`,
`||p_Q||inf <=6 (b_jG)^(-1/6)`.                                  (2.7)

Transposing the whole physical cross block gives the row counterpart

`int |phi_Q| <=12pi (a_iG)^(-1/6)`,
`||p_Q||inf <=6 (a_iG)^(-1/6)`                                  (2.8)

for every row with `a_i>0`.

No single `3 x 3` minor is selected or inverted. The three-dimensional receiver is the whole physical three-column (or three-row) block, whose third volume already aggregates every compatible anchored extension.

## 3. Main theorem — `QFORM-SECONDANCHOR-SLICE-OR-DOUBLE-DIFFUSE-v1`

For every `0<eta<1/2`, the invertible second-anchor packet (2.1)-(2.4) satisfies the following dichotomy.

### Branch A: a one-sided Schur-energy atom is at least eta

If

`h=max(h_r,h_c)>=eta`,                                           (3.1)

then

`boxed:
 int_R |phi_Q(t)|dt <=12pi (eta G)^(-1/6),
 ||p_Q||inf <=6 (eta G)^(-1/6).
}`                                                                 (3.2)

If in addition the designated partner packet (1.1) holds, then

`boxed:
 int_R |phi_Q(t)|dt
 <12pi (24/eta)^(1/6) Z^(-1/6),
 ||p_Q||inf
 <6(24/eta)^(1/6) Z^(-1/6).
}`                                                                 (3.3)

At the clean threshold `eta=1/4`,

`boxed:
 int_R |phi_Q(t)|dt <80.669555 Z^(-1/6),
 ||p_Q||inf <12.838959 Z^(-1/6).
}`                                                                 (3.4)

The density is continuous and vanishes at infinity.

### Branch B: failure forces double diffusion and a two-sample disjointness resource

If (3.1) fails, normalize Schur-entry energy to a probability distribution

`w_ij=|S_ij|^2/F`.                                                (3.5)

Its row and column marginals are exactly `a_i,b_j`. Draw two iid entries `(I1,J1),(I2,J2)` from `w`. Inclusion-exclusion gives the exact identity

`delta_2
 :=P(I1!=I2 and J1!=J2)
 =1-sum_i a_i^2-sum_j b_j^2+sum_ij w_ij^2`.                     (3.6)

Since

`sum_i a_i^2<=h_r`, `sum_j b_j^2<=h_c`,                          (3.7)

failure of (3.1) gives

`boxed: delta_2 >=1-h_r-h_c >1-2eta.`                            (3.8)

At `eta=1/4`, the surviving branch therefore has

`boxed:
 h_r<1/4,
 h_c<1/4,
 delta_2>1/2.
}`                                                                 (3.9)

This is a quantitative, dimension-free, product-coordinate structural statement about the same Schur packet. It does not rotate random coordinates.

### Proof

Branch A is (2.7) or (2.8) at a maximizing column/row. Branch B is the elementary iid collision identity (3.6) plus (3.7). QED.

## 4. Apply the newest account02/B02 result to an actual inequality

The newest designated partner theorem (1.2)-(1.4) and Theorem 3.1 now route the invertible second-anchor packet as follows.

1. If `sr(S)>=5/2`, the newest account02/B02 anchor-D5 geometric-mean theorem gives the genuine unweighted-L1 estimate (1.4).
2. If `sr(S)<5/2` but `max(h_r,h_c)>=1/4`, the new physical-slice theorem gives the sharper branchwise estimate (3.4).
3. Therefore an invertible second-anchor packet still unpaid by these two Fourier mechanisms must satisfy simultaneously

`boxed:
 rank(S)>=2,
 sr(S)<5/2,
 h_r<1/4,
 h_c<1/4,
 delta_2>1/2.
}`                                                                 (4.1)

The `rank(S)=1` endpoint is already paid by the earlier completed account02/B02 grouped cross-Schur theorem, so it is excluded from the genuine remainder.

There is an additional singular-vector consequence. Let `u,v` be top left/right singular vectors of `S`, and

`L=max_i |u_i|^2`, `R=max_j |v_j|^2`.                             (4.2)

Because

`||S_i:||_2^2 >=s_1(S)^2 |u_i|^2`,
`||S_:j||_2^2 >=s_1(S)^2 |v_j|^2`,                               (4.3)

we have

`h_r>=L/rho`, `h_c>=R/rho`.                                      (4.4)

Thus (4.1) implies

`boxed: L<rho/4<5/8, R<rho/4<5/8.`                               (4.5)

So the formerly broad “critical stable rank” invertible collar is now a **two-sided diffuse leading-singular-vector** collar with more than one-half disjointness for independent anchored extensions. This is the concrete receiver target left by this run.

## 5. Cancellation boundary: disjoint extension pairs do not force fourth volume

The disjointness resource (3.9) cannot be promoted to a fourth-volume bound without additional phase/algebraic information.

Take `m>=5` and

`S=u v^T`,
`u=v=m^(-1/2)(1,...,1)`.                                        (5.1)

Then

`h_r=h_c=1/m<1/4`,                                               (5.2)

and because `w_ij=1/m^2`,

`delta_2=(1-1/m)^2>1/2`.                                        (5.3)

Nevertheless

`E2(S)=0`                                                        (5.4)

exactly, since `rank(S)=1`; every residual `2 x 2` determinant cancels. This is a source-valid deterministic counterexample to the stronger intermediate implication

> “more than one-half pairwise row-and-column-disjoint anchored extension energy forces positive fourth exterior volume at comparable scale.”

It is **not** a counterexample to QFORM or to the target-wide Fourier-L1 criterion: this exact-rank-one endpoint is already uniformly paid by the grouped cross-Schur theorem.

The lesson for the next mechanism is precise: it must be **rank-one-compatible** and then gain stability when a nonzero transverse tail is present. Merely counting disjoint extension entries is insufficient because the two cross products in a `2 x 2` determinant can cancel.

## 6. Scalar-pivot analogue for the singular second-anchor branch

The same physical-slice idea has a clean analogue for the rank-one second-anchor branch of the newest partner proof.

Let `p!=0` be its genuine scalar ORIGINAL-coordinate pivot, `S1` the scalar cross-Schur residual, and

`H=p^2 E2(S1)>0`.                                                 (6.1)

Normalize the residual squared `2 x 2` minors by

`omega_(R,T)=det S1[R,T]^2/E2(S1)`, `|R|=|T|=2`.                (6.2)

Let

`c_T=sum_R omega_(R,T)`, `r_R=sum_T omega_(R,T)`,
`h_2=max(max_T c_T,max_R r_R)`.                                  (6.3)

For a fixed residual physical column pair `T`, keep all source rows but only the scalar pivot column together with the two columns in `T`; call this literal physical block `C_T`. It has exactly three columns. Every minor using the scalar pivot row and a residual row pair `R` obeys

`det C_T[{pivot row} union R,:]=p det S1[R,T]`.                 (6.4)

Cauchy--Binet therefore gives

`E3(C_T)>=p^2 sum_R det S1[R,T]^2=c_T H`.                       (6.5)

If `c_T>0`, `C_T` has exact rank three, so (1.6) yields

`int|phi_Q|<=12pi(c_T H)^(-1/6)`,
`||p_Q||inf<=6(c_T H)^(-1/6)`.                                  (6.6)

The transpose gives the row-pair analogue. Consequently

`boxed:
 int|phi_Q|<=12pi(h_2 H)^(-1/6),
 ||p_Q||inf<=6(h_2 H)^(-1/6).
}`                                                                 (6.7)

On the partner packet `H>Z/24`, any `h_2>=1/4` again gives exactly the constants (3.4). Thus the newest partner's singular critical-stable-rank branch can be narrowed further to `sr(S1)<5` **and** pair-atom diffusion `h_2<1/4`, apart from already-paid exact-rank-two endpoints.

No claim is made that small pair atoms imply disjoint pair sets; a star of many two-subsets shows that would need a separate inclusion-marginal argument.

## 7. First unpaid implication after this run

For the invertible second anchor the first unpaid interface is now

`QFORM-SECONDANCHOR-DOUBLEDIFFUSE-NONZERO-TRANSVERSE-v1`:

> starting from `G=D^2||S||_F^2>Z/24`, `rank(S)>=2`, `sr(S)<5/2`, `h_r,h_c<1/4`, hence top singular-vector physical leverages `<5/8` on both sides and two-sample extension disjointness `delta_2>1/2`, obtain a genuine product-preserving L1 Fourier or direct-density estimate while retaining every transverse Schur direction.

A natural next mechanism is a rank-one-compatible grouped/Hausdorff--Young interpolation which uses the `delta_2>1/2` extension transport but does **not** replace products of entries by `2 x 2` determinants before controlling cancellation.

For the scalar-pivot singular branch the corresponding residue is `sr(S1)<5` with diffuse exterior pair atoms, again after the exact-rank-two endpoint has been removed.

No target-valid exact-target counterexample to

`int_R |E exp(it X^T A X)|dt <= C`

was found. The stronger universal Fourier criterion therefore remains `OPEN_NOT_REFUTED`; the unrestricted bounded-density conjecture and unrestricted continuity statement remain OPEN.

## 8. Correction audit

This run respects every relevant live correction:

- no law-uniform scalar pointwise van-der-Corput decay;
- no independence after a spectral rotation or Schur shear;
- no arbitrary conditional projection-density cap;
- no arbitrary-joint coarea theorem;
- no promotion of a generic `2 x 2` cross minor to the full theorem;
- no deletion of a small coefficient/operator-norm tail on unbounded product inputs;
- no inference that disjoint extension **entries** imply a nonzero `2 x 2` determinant.

All Fourier receivers are applied to literal ORIGINAL-coordinate physical cross blocks. The Schur residual appears only inside exact determinant identities such as (2.5) and (6.4).

## 9. Deterministic diagnostics

With seed `20260923`, 200 random invertible `2 x 2` anchors with random residual blocks were checked numerically. For every tested residual column, `E3(C_j)>=D^2||S_:j||_2^2`; the smallest observed ratio was `1.445678...`. A separate scalar-pivot check over 100 random systems verified (6.5) on all tested residual column pairs; the smallest observed ratio was `1.041155...`. These are diagnostics only; the proof is the exact Cauchy--Binet/block-determinant argument above.

For the rank-one stress family (5.1), direct evaluation gives `delta_2=(1-1/m)^2` and `E2(S)=0` (up to machine roundoff), confirming the cancellation boundary.

MODEL: GPT-5.6 Sol. THINKING LEVEL / provider reasoning telemetry: UNKNOWN / not exposed.
