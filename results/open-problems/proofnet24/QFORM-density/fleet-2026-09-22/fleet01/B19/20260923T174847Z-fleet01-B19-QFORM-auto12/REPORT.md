SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T17:48:47Z.
attacking: the common-plane coherent 2+2+2 cycle with all tails retained; convert arbitrary self-curvature cancellation into an exact third-compound defect or a unique latent rank-two square, after applying fleet02/B19 r36 to the physical transverse leakage.

# fleet01/B19 auto12 — exact latent-rank-two compiler for the common-plane cycle

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / NEW EXACT STRUCTURAL COMPILER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved only on the physical-E3 branch recalled below; not asserted for the new grouped defect or the full target.

## 1. Fresh control and corrections


The exact target remains: independent real ORIGINAL coordinates with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one; prove one universal finite essential density bound for `X^T A X`. Continuity is separate.

The live corrections are preserved. In particular nothing below uses post-rotation independence, arbitrary-joint three-dimensional coarea, conditional projection-density caps produced by a change of variables, law-uniform pointwise quadratic Fourier decay, deletion of a nonzero coefficient tail, or a uniformly good physical minor. The fresh correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` from fleet03/B09 was also consumed: the three-large-eigenvalue hypothesis does not force a singleton/star third-volume aggregate to universal positive scale, so no such premise is used here.

The same UTC-hour B19 login already existed from the earlier same-hour invocation and was not overwritten, as required by the create-only login protocol. This run has its own immutable START and will have its own FINISH.

## 2. Incoming common-plane state and designated partner applied to an actual inequality

The immediate own predecessor is

`yspennstate/math-open-problems@cd266a121698fcefd5d9d00477916cb21b5f7700`,

which leaves disjoint ORIGINAL-coordinate banks `D_1,D_2,K` with physical cross blocks

`C=A[D_1,D_2]`, `N_1=A[D_1,K]`, `N_2=A[D_2,K]`.

The common-plane compiler of fleet03/B19 gives two-dimensional coefficient subspaces `P_1,P_2,Q` and the compressed maps

`C_0=P_1 C P_2`, `N_0=P_1 N_1 Q`, `P_0=P_2 N_2 Q`,

with `N_0,P_0` invertible and, at the live constants,

`|det N_0| >= Delta_*`,
`|det P_0| > (63/64) Delta_*`,

where

`Delta_*=(3/8)*63*(1-2^-20)^2/16384
        =0.0014419528160955833...`.

Moreover each full leg has

`s_2(N_r)^2 >= sigma_*^2
 =0.000356312664981148...`,

so `sigma_*=0.0188762460510862...`.

The designated partner is fleet02/B19 r36,

`yspennstate/math-open-problems@9157730c1b552b81f58b3cb6ef604b687962e548`,

`QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1`. For disjoint physical banks and `N=A[I,K]`, `M=A[I,J]`, it proves

`e_3([M,N]^T[M,N])
 >= (s_1(N)s_2(N))^2 ||(I-P_2)M||_F^2`,                         (2.1)

where `P_2` is a top-two left singular projection of `N`.

Apply (2.1) at the actual physical orientation `I=D_1`, `J=D_2`, `K=K`, `N=N_1`, `M=C`. If

`delta_L^2=||(I-P_1)C||_F^2`,

then

`boxed: Z_phys >= Delta_*^2 delta_L^2.`                          (2.2)

For the live strong-self scale

`F=0.4537176735697731005/8
 =0.05671470919622164...`,

`delta_L^2>=F/64` gives

`Z_phys>=Delta_*^2 F/64
       =1.842543860212322e-9.`                                  (2.3)

The completed marginal-free physical-E3 Fourier theorem from fleet03/B02,

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`,

then gives

`||p_Q||_infinity
 <=3*2^(4/3)*e^(1/3) Z_phys^(-1/6)
 <301.317`,                                                     (2.4)

and `phi_Q in L^1`, hence a continuous `C_0` density. The symmetric orientation at `D_2` is identical. Thus the partner theorem is used here at an actual target-level inequality: fixed transverse self-edge leakage is already paid, and the difficult residue is genuinely in-plane.

## 3. Normalize only the deterministic coefficient spaces

Work now inside the three two-dimensional coefficient spaces `P_1,P_2,Q`. Let the full symmetric compression of `A` to their direct sum be

`H = [[B_1, C_0, N_0],
      [C_0^T, B_2, P_0],
      [N_0^T, P_0^T, B_3]]`,                                    (3.1)

where `B_1,B_2,B_3` are arbitrary real symmetric `2 x 2` self-compressions. No probabilistic independence is asserted inside any plane.

Use the deterministic block congruence

`T=diag(N_0^(-T), P_0^(-T), I_2)`.

Then

`G=T^T H T
  = [[S_1, R, I],
     [R^T, S_2, I],
     [I, I, S_3]],`                                             (3.2)

where

`R=N_0^(-1) C_0 P_0^(-T)`,
`S_1=N_0^(-1)B_1N_0^(-T)`,
`S_2=P_0^(-1)B_2P_0^(-T)`,
`S_3=B_3`.

This is coefficient algebra only. The original random coordinates are not rotated or replaced by independent spectral coordinates.

Put

`V_3(G)=e_3(G^T G)
      =sum_(|Rset|=|Cset|=3) det G[Rset,Cset]^2`.                (3.3)

## 4. Main new inequality: four selected minor families detect every rank-two cancellation

### Theorem 4.1 — `QFORM-COMMONPLANE-LATENT-R2-DEFECT-v1`

For every real `2 x 2` matrix `R` and every real symmetric `2 x 2` matrices `S_1,S_2,S_3`, define

`D(G)= ||S_2-R||_F^2
      +||S_1-R^T||_F^2
      +||I-S_3 S_1||_F^2
      +||I-S_3 S_2||_F^2`.                                     (4.1)

Then

`boxed: V_3(G) >= D(G).`                                        (4.2)

The four terms in (4.1) are not abstract consequences of rank: each is the sum of squares of four explicit `3 x 3` minors of the normalized cycle, and the four minor families are disjoint.

#### Proof

Label the coordinates in the three two-dimensional groups by `x_1,x_2`, `y_1,y_2`, `z_1,z_2`.

**Family A.** Take rows `{x_1,x_2,y_i}` and columns `{y_j,z_1,z_2}`. The corresponding matrix is

`[[R_1j, 1,0],
  [R_2j, 0,1],
  [(S_2)_ij, delta_i1,delta_i2]]`.

Its determinant is exactly

`(S_2)_ij-R_ij`.                                                   (4.3)

Summing its four squares gives `||S_2-R||_F^2`.

**Family B.** Swap the first two groups. Rows `{y_1,y_2,x_i}` and columns `{x_j,z_1,z_2}` give

`(S_1)_ij-(R^T)_ij`,                                             (4.4)

and the four squared minors sum to `||S_1-R^T||_F^2`.

**Family C1.** Inside the `x-z` identity edge, take rows `{x_1,x_2,z_i}` and columns `{x_j,z_1,z_2}`. Reorder the columns as `(z_1,z_2,x_j)`; two transpositions preserve the determinant sign. The block determinant is

`delta_ij-(S_3 S_1)_ij`.                                        (4.5)

Its four squares sum to `||I-S_3S_1||_F^2`.

**Family C2.** The identical construction on the `y-z` identity edge gives

`delta_ij-(S_3 S_2)_ij`,                                        (4.6)

whose squares sum to `||I-S_3S_2||_F^2`.

The row/column group multiplicities of the four families are respectively

`(XXY ; YZZ)`, `(YYX ; XZZ)`, `(XXZ ; XZZ)`, `(YYZ ; YZZ)`,

so no selected minor is counted twice. Since `V_3(G)` is the sum of squares of *all* `3 x 3` minors, (4.2) follows. QED.

This inequality includes all signs, singular or repeated eigenvalues, and every symmetric self block. It has no probabilistic hypothesis at all.

## 5. Exact endpoint: the only complete self-curvature cancellation is one latent two-dimensional square

### Corollary 5.1 — `QFORM-COMMONPLANE-EXACT-LATENT-SQUARE-v1`

For the normalized cycle (3.2), the following are equivalent:

1. `V_3(G)=0`;
2. `rank(G)<=2`;
3. there is an invertible real symmetric `2 x 2` matrix `S` such that

`R=S_1=S_2=S`, `S_3=S^(-1)`.                                    (5.1)

In this case

`boxed:
 G = L^T S L,
 L=[ I_2  I_2  S^(-1) ],
}`                                                               (5.2)

so the corresponding six-variable quadratic coefficient is exactly

`(x+y+S^(-1)z)^T S (x+y+S^(-1)z)`.                              (5.3)

#### Proof

`V_3(G)=0` is equivalent to `rank(G)<=2` by the definition of the third compound. By Theorem 4.1 it also forces `D(G)=0`. Hence

`S_2=R`, `S_1=R^T`.

Since `S_1,S_2` are symmetric, `R=R^T=:S`. The equation `I-S_3S_2=0` makes `S` invertible and gives `S_3=S^(-1)`. This is (5.1). Direct multiplication gives (5.2), so the matrix has rank two. The converse is immediate. QED.

This is the main structural gain of the run. The arbitrary same-bank self curvatures cannot cancel a common-plane `2+2+2` cycle in an uncontrolled fashion. Complete cancellation has one and only one form: the entire normalized six-dimensional compression collapses to a single two-dimensional latent square.

## 6. Quantitative stability of the endpoint

The exact statement has a useful stable version.

Let

`eta=sqrt(V_3(G))`.                                                (6.1)

Theorem 4.1 gives

`||S_2-R||_F<=eta`,
`||S_1-R^T||_F<=eta`,
`||I-S_3S_2||_F<=eta`.                                           (6.2)

Because `S_2` is symmetric,

`||(R-R^T)/2||_F<=eta`,

and therefore

`boxed: ||S_1-S_2||_F<=4 eta.`                                  (6.3)

Fix any `r>eta`. If

`s_2(R)>=r`,                                                      (6.4)

then `s_min(S_2)>=r-eta`; hence `S_2` is invertible and

`S_3-S_2^(-1)
 =(S_3S_2-I)S_2^(-1)`,

so

`boxed:
 ||S_3-S_2^(-1)||_F <= eta/(r-eta).
}`                                                               (6.5)

Define the exact latent rank-two completion

`K_(S_2)=
 [[S_2,S_2,I],
  [S_2,S_2,I],
  [I,I,S_2^(-1)]].`                                             (6.6)

Then, using (6.2)-(6.5) and counting the off-diagonal `R-S_2` block twice,

`boxed:
 ||G-K_(S_2)||_op
 <= ||G-K_(S_2)||_F
 <= eta * sqrt(18+(r-eta)^(-2)).
}`                                                               (6.7)

Thus for every chosen threshold `r_0>eta` there is an exhaustive quantitative alternative:

- `s_2(R)<r_0`, i.e. the normalized third edge lies in a rank-one tube; or
- the whole six-dimensional coefficient compression lies within the explicit distance (6.7) of the unique latent rank-two square family.

No nonzero tail is deleted in this statement.

## 7. Connection back to the full target

The normalized congruence can be undone. If the exact endpoint (5.1) occurs, the original common-plane compression `H` is itself rank two because congruence preserves rank. Lift that rank-two operator by zero on the orthogonal complement of `P_1 direct-sum P_2 direct-sum Q`; call the lifted operator `L_2`.

The full target hypothesis gives `s_3(A)>=1`. Therefore, by the Eckart-Young characterization of the third singular value,

`boxed: ||A-L_2||_op >= s_3(A) >=1.`                             (7.1)

So the latent-square endpoint cannot hide the third target direction: after the exact two-dimensional cancellation is extracted, the retained coefficient remainder has operator norm at least one. This is a deterministic statement about the *retained* matrix; no random perturbation is discarded.

Equation (7.1) does not yet pay that remainder. It identifies the next source-valid analytic problem: combine the exact/near latent rank-two square with the unit third spectral resource without compressing a product-origin bank to an arbitrary joint density.

For completeness, the normalized third compound also has a direct coefficient-scale relation. If `H` is the unnormalized six-dimensional compression and `T` is (3.2), then

`wedge^3 G=(wedge^3 T)^T (wedge^3 H) (wedge^3 T)`.

Since both bicore legs satisfy `s_2>=sigma_*`, the crude bound `||T||op<=sigma_*^(-1)` gives

`V_3(H) >= sigma_*^12 V_3(G)`,                                   (7.2)

with

`sigma_*^12=2.04638600295735e-21`.

The scale is intentionally crude but universal inside the live common-plane state. Equation (7.2) is coefficient currency only; I do **not** claim that a general principal third compound is already an analytic density receiver.

## 8. Compact conditional proof graph after this run

The current source-pinned proof assembly is now sharper.

1. The global compiler enters the strict-N3 / STAR4 geometry after the already-paid physical-pivot, spectral-window, diffuse-D5 and selected-volume exits.
2. Partner fleet02/B19 r36 plus the marginal-free physical-E3 theorem pays any fixed transverse leakage from a rank-two bicore, quantitatively as in (2.2)-(2.4).
3. The right-plane mismatch is likewise paid by a literal physical E3 packet; failure leaves one common `2+2+2` coefficient geometry.
4. In that geometry, arbitrary self-curvature cancellation is now governed by Theorem 4.1. A positive defect is an explicit third-compound packet; zero defect is *exactly* the latent square (5.3); small defect is either a normalized rank-one edge or the quantitative latent tube (6.7).
5. In the exact latent endpoint, the full target immediately forces the retained unit operator-norm remainder (7.1).

Thus the former vague debt

`QFORM-COMMONPLANE-COHERENT-CYCLE-WITH-TAIL-LINFINITY-v1`

has been replaced by the much narrower pair

`QFORM-COMMONPLANE-GROUPED-E3-PRODUCT-RECEIVER-v1`

and

`QFORM-LATENT-R2-SQUARE-PLUS-UNIT-REMAINDER-LINFINITY-v1`,

with the already-existing normalized relative-rank-one tube as the third explicit subcase. Any future receiver must preserve original product provenance; the fleet02/B09 counterexample to cross-cycle plus arbitrary self-curvature and the fleet04/B19 arbitrary-joint barrier remain binding.

The full QFORM theorem is therefore still **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is also open. Continuity is claimed only on the physical-E3 branch (2.4).

## 9. Verification

`check_latent_completion.py` verifies all sixteen selected-minor identities on 2000 random real inputs, sums all `3 x 3` minors to check `V_3>=D`, and checks the exact latent factorization on a random invertible symmetric endpoint. The recorded run ends with

`QFORM_COMMONPLANE_LATENT_COMPLETION_CHECK_PASS`.

The numerical checker is regression evidence only. The proof is the exact determinant calculation in Sections 4-6.
