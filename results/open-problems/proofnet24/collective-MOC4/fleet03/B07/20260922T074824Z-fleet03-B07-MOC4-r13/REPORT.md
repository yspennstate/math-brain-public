# fleet03/B07 MOC4 report — full-tangent cross-split reserve on the mixed-Schur branch

Run: `20260922T074824Z-fleet03-B07-MOC4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target

For all complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4` counted with multiplicity, prove

`det(A+B) in conv{ prod_i(a_i+b_{sigma(i)}) : sigma in S_4 }`.

After diagonalization, for every unit support direction `eta` it suffices to prove

`h_eta(U)=Re(conj(eta) det(D_a+U D_b U*)) <= M_eta`

for every true `U in U(4)`, where

`M_eta=max_sigma Re(conj(eta) prod_i(a_i+b_{sigma(i)}))`.

No bistochastic or independently chosen compound-minor array is substituted for the common unitary.

## 2. Newest compatible campaign state recovered

The latest complete lead input is fleet03/B07 r12, `MOC4-KERNEL-QUARTIC-RESERVE-v1`: if `F` has a local maximum, `H=D^2F<=0`, `z in ker H`, `ell(y)=D^3F[z,z,y]`, `q=D^4F[z,z,z,z]`, `A=-H`, then `ell` annihilates `ker A` and

`q+3 <ell#,A^+ ell#> <= 0`.                                      (KR)

The assigned OTHER-account partner fleet04/B08 r12 contributes `MOC4-STRICT-SPIN4-SECTORS-v1`. At a support-violating global maximizer all scalar Spin(4) sectors are strict. For a genuine four-dimensional pair block

`H_pair=[[-2a I_2,M],[M^T,-2b I_2]] <= 0`, `a,b>0`,

the only singular boundary is

`||M||_op=2 sqrt(ab)`.                                            (MS)

If `Mv=2sqrt(ab)u` and `M^T u=2sqrt(ab)v`, then the true pair tangent

`Z*=sqrt(b)u + sqrt(a)v`

is a kernel vector of the pair Hessian.

The newest compatible fleet03/B20 result, `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`, shows that on (MS) the complete same-pair `S^2 x S^2` global trust-region condition collapses exactly to the lead's pair Lyapunov–Schmidt reserve. Therefore another optimization of the same singular pair orbit cannot close the branch. The first unpaid implication is genuinely cross-split: use the other pair/root/Cartan directions and same-unitary compatibility.

Also compatible is fleet04/B09 `MOC4-OPEN-GAP-GENERICIZATION-v1`: any strict target-level counterexample perturbs to one with simple nonzero spectra and all relevant cross-ratio conditioning determinants nonzero. Thus it is enough to close the generic positive-gap branches; singular and repeated spectra are then automatically included by contradiction-through-perturbation.

## 3. Smallest conditional full deduction

Assume a strict support counterexample. By open-gap genericization take the spectra simple, nonzero and spectrally conditioned. Compactness of `U(4)` gives a true global maximizer `U_*` with gap `gamma>0`.

By fleet04/B08 all scalar Spin(4) sectors are strict. Hence exactly one of the following holds:

- `MSQR`: at least one of the six genuine pair Hessian blocks satisfies (MS);
- `NDI`: all six pair blocks are negative definite.

Therefore full MOC4 follows once the following two generic implications are proved:

1. `MOC4-MSQR-CROSS-SPLIT-CLOSURE`: no positive-gap global maximizer can satisfy a mixed-Schur equality together with the full same-unitary stationarity/Hessian/higher-order constraints;
2. `MOC4-NDI-CROSS-ROOT-CLOSURE`: no positive-gap global maximizer can have all six pair blocks negative definite while satisfying the full cross-root/Cartan and `P/R/D` compatibility conditions.

This run directly attacks implication 1 by upgrading a pair-kernel condition to an exact full-tangent Schur-complement reserve.

## 4. New theorem: mixed-Schur pair nullity is full-Hessian nullity

### `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1`

Let `F` be the actual support function in any real local chart on the true unitary manifold near a global maximizer `U_*`. Let

`H=D^2F(0) <= 0`.

Let `E` be one of the genuine four-dimensional Spin(4) pair tangent subspaces, and let `H_E` be the principal restriction of `H` to `E`. Suppose the partner mixed-Schur equality holds and `0 != z in E` is its explicit pair-kernel vector, so

`H_E z=0`.

Then, after embedding `z` in the full tangent space,

`H z=0`.                                                        (CB1)

Consequently

`D^2F(0)[z,y]=0` for every true-unitary tangent direction `y`, including every other root block and every Cartan direction.      (CB2)

### Proof

Since `H<=0`, `A=-H` is positive semidefinite. The pair equality gives

`z^T A z=-z^T H_E z=0`.

For a positive-semidefinite symmetric operator, zero quadratic form implies membership in its kernel: `A^(1/2)z=0`, hence `Az=0`, equivalently `Hz=0`. This proves (CB1) and (CB2). `QED`

This is the first exact cross-split condition forced by a mixed-Schur pair boundary. A pair-null mode cannot couple quadratically to another root/Cartan direction at a genuine global maximum.

## 5. New theorem: exact full-tangent cross reserve

Split the full tangent orthogonally as `E direct_sum Fperp` and write

`A=-H=[[B,C],[C^T,D]] >=0`,

where `B=-H_E`. Let the full cubic covector generated by the mixed-Schur kernel be

`beta(y)=D^3F(0)[z,z,y]`,

with Riesz vector decomposed as `beta#=(u,v)` in `E direct_sum Fperp`. Put

`S=D-C^T B^+ C`,
`r=v-C^T B^+ u`.                                               (5.1)

### `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`

At a genuine global maximum on the mixed-Schur boundary:

1. `ker B subset ker C^T`, hence `range C subset range B`;
2. `S>=0`;
3. `u in range B`, `r in range S`;
4. the exact pseudoinverse energy decomposes as

`<beta#,A^+ beta#> = <u,B^+u> + <r,S^+r>`;                    (5.2)

5. therefore, with `q=D^4F(0)[z,z,z,z]`, the full necessary fourth-order gate is

`boxed( q + 3<u,B^+u> + 3<r,S^+r> <= 0 )`.                    (CSR)

The first two terms in (CSR) are exactly the r12 pair Lyapunov–Schmidt reserve. The third term is a new nonnegative **cross-split reserve** invisible to the complete same-pair trust-region problem studied by B20.

### Proof

Because `A>=0`, every `w in ker B` satisfies `(w,0)^T A(w,0)=0`, hence `A(w,0)=0`; this gives `C^T w=0` and item 1. The generalized Schur complement `S=D-C^TB^+C` is therefore positive semidefinite.

The r12 kernel-reserve lemma applied to the full chart says `beta` annihilates `ker A`, so `beta# in range A`. Since `(ker B,0) subset ker A`, `u` annihilates `ker B`, hence `u in range B`. Standard completion of squares, valid here because `range C subset range B`, gives for arbitrary `x in E`, `y in Fperp`, with `x'=x+B^+Cy`,

`2<u,x>+2<v,y>-<(x,y),A(x,y)>`

`= [2<u,x'>-<x',Bx'>] + [2<r,y>-<y,Sy>]`.

The left side has finite supremum because `beta# in range A`; therefore `r in range S`. Taking suprema yields (5.2). Inserting (5.2) into the full version of (KR) proves (CSR). `QED`

## 6. Why this is genuinely stronger than the same-pair gate

Define

`R_pair=<u,B^+u>`, `R_cross=<r,S^+r>`.

Then `R_cross>=0`, and because `r in range S`,

`R_cross=0 iff r=0`.

Thus any mixed-Schur candidate with a nonzero cross cubic residual `r` must pay a strictly larger fourth-order reserve than the complete singular pair orbit can detect:

`-(q+3 R_pair) >= 3 R_cross >0`.                               (6.1)

The B20 trust-collapse result is therefore not a dead end: it identifies exactly what information was missing. The next obstruction must come from directions outside the singular pair, and (CSR) isolates that missing information in one positive-semidefinite scalar.

An exact rational normalization check is stored beside this report. On the abstract PSD block example

`A=[[2,0,1],[0,0,0],[1,0,2]]`, `beta#=(4,0,5)`,

one has `R_pair=8`, `S=3/2`, `r=3`, `R_cross=6`, while the full active pseudoinverse gives `R_full=14=8+6`. This is only a factor/sanity check for the block identity, not a MOC4 example.

## 7. Direct implication for the partner explicit kernel

For the assigned partner's simple mixed-Schur mode

`z=Z*=sqrt(b)u_1 + sqrt(a)v_1`,

(CB2) supplies exact additional equations

`D^2 h_eta(U_*)[Z_*,Y]=0`                                    (7.1)

for **every** other true-unitary root/Cartan tangent `Y`.

These equations were not present in the same-pair trust problem. They are the first concrete cross-split compatibility equations required by B20's `MOC4-MIXED-SCHUR-CROSS-SPLIT-COUPLING-v1` residual.

Moreover the cubic covector must satisfy (CSR). In the simple-kernel case, the prior explicit pair reserve remains valid for `R_pair`; the only new object to compute is the Schur residual `r` and its effective complement curvature `S`.

This gives a finite next calculation: evaluate (7.1) and `r` from the existing exact determinant/exterior-square derivative formulas, then compare the positive quantity `3R_cross` against the available pair quartic slack.

## 8. Mechanism change and first remaining implication

The preceding run attacked the singular pair by a curved Lyapunov–Schmidt path **inside the same Spin(4) pair slice**. B20 has now proved that the full same-pair global trust condition collapses to that reserve, so repeating same-pair optimization would be unchanged work.

This run changes mechanism to the **full true-unitary Hessian and its generalized Schur complement**. No independent bistochastic data are introduced.

The sharpened first missing implication is

`MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1`:

> On the generic spectral locus, use the structured determinant `K/X`, same-unitary `P/R/D`, the other five pair/root blocks, Cartan stationarity and subgroup roofs to show that every positive-gap mixed-Schur candidate violates (CSR). Equivalently, prove that either the cross residual `r` is nonzero with `3R_cross` larger than the available pair quartic slack, or the exceptional residual-zero system `r=0` together with (7.1) forces target safety.

If this closes `MSQR`, the only remaining generic branch is `NDI`, which should be attacked by cross-root/Cartan coupling rather than additional pair-boundary analysis.

## 9. Verdict

`ESSENTIAL_STEP_APPLIED`.

The mixed-Schur pair kernel is now proved to be a **full-Hessian kernel**, all quadratic couplings from that mode to every other unitary tangent vanish, and the previous pair quartic reserve acquires an exact additional nonnegative Schur-complement term. This is a genuine cross-split necessary condition and directly advances the first unpaid implication identified by the newest B20 state.

Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.