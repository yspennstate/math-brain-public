SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-23T18:30:23Z.
attacking: the finite-core rank-two physical cross packet — extract two literal hub rows, spend any transverse Frobenius crossing by the completed projected-crossing theorem, and force a failed volume-marginal gate into a literal rank-three crossing.

# fleet03/B19 r38 — literal two-row hub compiler for the finite-core rank-two survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Outcome: **NEW TARGET-LEVEL PAYMENT + SHARPENED REMAINING COLLAR / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the new paid branch; full-target continuity remains OPEN.

## 1. Fresh control and correction boundary


This proof does **not** use post-rotation independence, arbitrary-joint coarea, a worst conditional-density supremum, law-uniform pointwise quadratic-phase decay, moment/support assumptions, deletion of a small coefficient as a small random perturbation, or an assertion that one uniformly good physical minor exists. All random independence below is between disjoint ORIGINAL coordinate banks.

The same UTC hour already contained the canonical fleet03/B19 login `20260923T180414Z-fleet03-B19-QFORM-r37`; it was preserved rather than overwritten. This run has its own immutable start/finish records and mathematical directory.

## 2. Current proof frontier consumed

### 2.1 Finite-core compiler from fleet01/B20

The fresh fleet01/B20 compiler is source-pinned at

`yspennstate/math-open-problems@d72f85bd91f01034df4df7f1544aef854771f0a6`

with detailed derivation beginning at commit

`1fe3d344529b743f64cb37b42a7a12b6a86a9414`.

In its unpaid finite-core state there is an ORIGINAL-coordinate heavy set `H`, light complement `L=H^c`, with

`|H|<=124`,                                                       (2.1)

and the literal cross block

`C=A[H,L]`.                                                       (2.2)

The physical-third-volume exit already pays continuously if `s_3(C)>=1/64`. Hence the unpaid state has

`s_3(C)<1/64`.                                                    (2.3)

One surviving branch is a quantitative physical rank-two packet

`s_1(C)s_2(C)>1/480`.                                             (2.4)

The other compiler branches are a strong rank-one tube or a two-light-bank diffuse strong-mode packet. This run attacks (2.4), not those distinct branches.

### 2.2 Projected-crossing receiver

The checked arbitrary-internal-function theorem is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its grouped-hub theorem says: if `k` hub projection coordinates have density cap `M_H`, the hub-to-`J` block has row rank `k` with singular-value product `S`, and the projected `I-J` crossing has `ell`-volume `Z_ell` with all inclusion marginals at most `1/2`, then for `d=k+ell>2`,

`||p_Q||_infinity`
` <= [d/(d-2)] 2^((k+3ell)/(2d)) exp(ell/(2d))`
`    M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,                       (2.5)

with the exponential omitted for `ell=1`. Arbitrary same-bank quadratic terms, diagonals, linear terms and internal hub functions are retained.

Its exact-rank crossing theorem also gives, for crossing rank `r>2`,

`||p_Q||_infinity`
` <= [r/(r-2)] (M_X M_Y/(s_1...s_r))^(1/r)`.                    (2.6)

These are the only analytic receivers used in the new theorem.

## 3. New theorem: rank-two physical crossing either pays or becomes Frobenius-near an actual two-row span

### Theorem 3.1 — `QFORM-R2-PHYSICAL-TWOROW-TRANSVERSE-COMPILER-v1`

Let `H,L` be disjoint ORIGINAL-coordinate banks with `m=|H|>=2`, and let

`C=A[H,L]`.                                                       (3.1)

Assume

`s_1(C)s_2(C)>=sigma>0`.                                         (3.2)

Put `N=binom(m,2)`. Then there exists a literal pair of original coordinates

`T={a,b} subset H`                                               (3.3)

such that, writing

`M=C[T,L]`,
`S=sqrt(det(MM^T))`,                                             (3.4)

one has

`boxed: S>=sigma/sqrt(N).}`                                      (3.5)

Let `Pi` be the orthogonal projection in coefficient space `R^L` onto `row(M)`, put `I=H\T`, and define

`R=C[I,L](I-Pi)`,
`rho=||R||_F`.                                                   (3.6)

If `rho>0`, the full ambient quadratic law has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity <= 3*2^(5/6) (S rho)^(-1/3).}`                 (3.7)

Consequently, for every `tau>0`, either

`boxed: ||C[I,L](I-Pi)||_F<tau,}`                                (3.8)

or

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6) (sigma*tau/sqrt(N))^(-1/3).}`                       (3.9)

Thus failure of the density exit forces the **entire** physical cross block to lie within Frobenius distance `tau` of a rank-at-most-two matrix whose row space is generated by two literal physical rows.

### Proof

Cauchy--Binet gives the exact aggregate two-volume identity

`sum_(T subset H, |T|=2) det(C[T,L]C[T,L]^T)=e_2(CC^T)`.         (3.10)

Since `e_2(CC^T)` contains the top-two squared singular-value product,

`e_2(CC^T)>=s_1(C)^2 s_2(C)^2>=sigma^2`.                         (3.11)

There are `N` row pairs, so one pair satisfies

`det(MM^T)>=sigma^2/N`,                                         (3.12)

which is (3.5). In particular `M` has exact rank two.

Use the two actual coordinates `X_T` as a two-dimensional hub. Their joint density is at most one, so `M_H=1`. In the grouped projected-crossing theorem take

`k=2`, `J=L`, `I=H\T`, `M_J=M`, `ell=1`.                         (3.13)

The projected light crossing is exactly `R` from (3.6), hence

`Z_1=e_1(RR^T)=||R||_F^2=rho^2`.                                (3.14)

If every row-volume marginal obeys

`alpha_i=||R_i||^2/rho^2<=1/2`,                                 (3.15)

then (2.5), with `d=3`, gives directly

`||p_Q||_infinity
 <=3*2^(5/6) S^(-1/3) rho^(-1/3)`,                              (3.16)

which is (3.7).

It remains to show that failure of (3.15) is not an obstruction. Suppose some literal original row `i in I` has

`||R_i||^2>rho^2/2`.                                             (3.17)

Condition on every original coordinate in `H\(T union {i})`. The surviving source coordinates are the three independent cap-one variables indexed by `T union {i}`, while all of `L` remains an independent product bank. Its literal three-row crossing block is

`B=C[T union {i},L]`.                                            (3.18)

Because `R_i` is exactly the component of the third row perpendicular to `row(M)`, the Gram determinant is the base-times-height identity

`det(BB^T)=det(MM^T)||R_i||^2=S^2||R_i||^2`.                    (3.19)

Thus `B` has exact rank three and its singular-value product is `S||R_i||`. Apply (2.6) with `r=3`. The three source variables are literal original coordinates, so `M_X=1`; the orthogonal three-dimensional projection of the product `L`-law has density cap `M_Y<=2^(3/2)`. Therefore, uniformly in the conditioned variables,

`||p_Q||_infinity
 <=3 (2^(3/2)/(S||R_i||))^(1/3)`.                               (3.20)

Using (3.17), `||R_i||>rho/sqrt(2)`, and hence

`||p_Q||_infinity
 <3*2^(2/3)(S rho)^(-1/3)
 <3*2^(5/6)(S rho)^(-1/3)`.                                     (3.21)

Averaging the uniform conditional density bound proves (3.7) also when the row-marginal gate fails. Equation (3.9) follows from (3.5) and `rho>=tau`. QED.

### Why this is product-safe

The argument never replaces the light bank by an arbitrary joint density. It either uses the grouped projected-crossing theorem while the original product coordinates are still present, or conditions down to three literal source coordinates and uses a physical rank-three crossing. Same-bank curvature and all extra spectrum remain inside the arbitrary functions allowed by the receivers.

## 4. Application to the live finite-core rank-two packet

In (2.4), take

`sigma=1/480`, `m<=124`, `N<=binom(124,2)=7626`, `tau=1/64`.       (4.1)

The selected literal pair satisfies

`S>1/(480 sqrt(7626))
 =2.3856699607...*10^(-5)`.                                      (4.2)

If its transverse Frobenius residual satisfies `rho>=1/64`, Theorem 3.1 yields

`||p_Q||_infinity
 <3*2^(5/6)
   [(1/(480 sqrt(7626)))(1/64)]^(-1/3)
 =742.7388172...`.                                                (4.3)

Therefore

`boxed: ||p_Q||_infinity<743}`                                   (4.4)

with a continuous `C_0` density on that branch.

The finite arithmetic is independently encoded in `CHECK.py`; the committed output ends

`QFORM_B19_R38_CHECK_PASS`.

Every still-unpaid finite-core rank-two state now obeys the stronger structural condition

`boxed:
 exists T subset H, |T|=2:
 sqrt(det(C[T,L]C[T,L]^T))>1/(480 sqrt(7626)),
 ||C[H\T,L](I-Pi_row(C[T,L]))||_F<1/64.}`                        (4.5)

This is strictly stronger information than the preceding operator-collar statement `s_3(C)<1/64`: it is an aggregate Frobenius near-rank-two statement anchored by two actual physical rows.

## 5. Designated partner fleet04/B19 applied to an actual inequality

The completed partner theorem used here is fleet04/B19 r2,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

In its **residual-diffuse exact-null-coloop** normal form, with residual determinant parameter `0<D_res<=1` and `|det M|>=1`, it proves

`||p_Q||_infinity<34 sqrt(log(e/D_res))`.                         (5.1)

Therefore, on the concrete source-valid interval

`e^(-8)<=D_res<=1`,                                               (5.2)

one has the actual target-level inequality

`boxed: ||p_Q||_infinity<34*3=102.}`                              (5.3)

The partner theorem also proves continuity in that scope. I do **not** transfer (5.1) to the finite-core collar (4.5); the exact-null-coloop hypotheses are different. Its newer r4 moving-ridge construction is used as a correction boundary: an arbitrary joint density cap on a same-bank triple cannot replace the original-product provenance, even for a fixed matrix with three large eigenvalues.

## 6. Updated compact proof assembly

The current correction-safe end-to-end graph contains the following compatible exits.

1. Diagonal and many localized physical-principal-block branches are already paid at their exact scopes.
2. Marginal-free physical third-volume/fifth-volume and projected-crossing branches pay diffuse or transverse physical crossing packets while retaining arbitrary same-side curvature and extra spectrum.
3. The fleet01/B20 finite-core compiler pays the physical `s_3(A[H,L])>=1/64` branch below `675.211` and leaves rank-one, rank-two and two-source strong-mode packets.
4. **This run pays the rank-two packet whenever its literal two-row span has transverse Frobenius residual at least `1/64`, with continuous bound `<743`.**
5. The exact-null-coloop residual-diffuse branch has the partner's adaptive Hausdorff--Young estimate (5.1), giving `<102` on (5.2).
6. Separate common-plane/triangle compilers from preceding B19/B20 runs pay relative-skew or physical third-volume states and isolate their own approximately symmetric/heavy-anchor endpoint.

These branches are not yet exhaustive. No full theorem is declared.

## 7. First essential remaining implication

The first missing implication in the finite-core rank-two branch is now

`QFORM-FINITECORE-PHYSICAL-R2-FROBENIUS-COLLAR-PAYMENT-v1`:

> Under the fleet01/B20 finite-core carrier hypotheses, pay the state (4.5), or route it quantitatively to an already-paid grouped/rank-one/two-source branch, while retaining the nonzero `1/64` Frobenius cross tail, arbitrary same-bank curvature, the full operator residual `A-S0`, all outside couplings and all extra spectrum.

The small residual in (4.5) cannot be discarded as a small random quadratic perturbation because the input laws have no moments. The special square-plus-hyperbola calculation of fleet03/B03 shows that the projected residual can even vanish exactly while the two-dimensional crossing alone supplies only an `L^2`/half-Riesz endpoint, so the collar is a genuine analytic interface rather than a numerical artifact.

The partner's moving-ridge barrier also excludes an arbitrary-joint coarea shortcut. A valid closure must use the literal two-row product hub together with a third original-product smoothing resource that remains effective as the projected crossing tends to zero, or force a structural degeneration already covered elsewhere.

## 8. Status

- Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- New theorem: `QFORM-R2-PHYSICAL-TWOROW-TRANSVERSE-COMPILER-v1`, proved above.
- New live payment: continuous density `<743` on the transverse finite-core rank-two branch.
- Remaining finite-core rank-two debt: the explicit Frobenius collar (4.5).
- Full-target continuity: **OPEN**; continuity is proved on the new paid branch and on the partner null-coloop scope used in (5.3).
- Two independent end-to-end reviews are not requested because no full candidate proof exists yet.
