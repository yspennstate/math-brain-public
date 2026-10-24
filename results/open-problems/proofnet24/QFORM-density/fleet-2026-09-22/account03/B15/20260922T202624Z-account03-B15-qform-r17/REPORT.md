# QFORM B15 r17 — exact spectral-boundary normal form for the extremal density problem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account03/B15`  
**Run:** `20260922T202624Z-account03-B15-qform-r17`  
**Control at pre-publication refresh:** `yspennstate/math-research-brain@0bd971f334ea5788aadaf70c72b86fa77081944d`, OWNER CONTROL revision `2026-09-22.15`  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_TARGET_LEVEL_NORMAL_FORM / FULL-CONJECTURE-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result in one sentence

The optimal QFORM density-height constant is unchanged if one restricts simultaneously to matrices on the exact spectral boundary `s_3(A)=1`, compactly supported smooth cap-one product inputs, continuous `C_0` output densities, and any prescribed finite family of scaling-invariant algebraic genericity conditions. Consequently any counterexample sequence, if the universal constant is infinite, can be chosen entirely in this normalized regular class; it can even be chosen with strict marginal cap `<=1/2` after a harmless input dilation.

Here `s_3(A)` is the third largest singular value of the real symmetric matrix `A`, equivalently the third largest absolute eigenvalue. The owner target is exactly `s_3(A)>=1`.

This is a no-loss reduction of the full target, not a proof that the resulting supremum is finite. Full QFORM remains **OPEN / NOT PROVED**.

## 2. Source-corrected premises

The live state and correction ledger were refreshed before publication. In particular this proof does **not** use:

- the refuted arbitrary-joint rank-three coarea estimate;
- the refuted positive conditional-projection-density moment;
- the refuted uniform scalar conditional supremum;
- law-uniform pointwise van-der-Corput decay;
- independence after spectral rotation;
- a single uniformly conditioned physical minor.

The latest correction consumed explicitly is `QFORM-R26-ARBITRARY-JOINT-COAREA-PREMISE-RETRACTED-v1`; it is irrelevant to the proof below because the argument uses only exact scaling of the original product-law quadratic form and two already completed target-level reductions.

Two completed B15 results are applied:

1. **Assigned partner account04/B15**: `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`. It proves exactly

   `C_all = C_C0 = C_sm`,

   including `+infinity`, and quantitatively: for every target density `p` and every `eta>0` there is a compactly supported smooth cap-one target instance with output `p_eta in C_0(R)` and

   `||p_eta||_infinity >= ||p||_infinity-eta`.

2. **account03/B15 r14 genericization theorem**: `yspennstate/math-open-problems@065b515da52986860a862ed50261bfc35b9caa0b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T173720Z-account03-B15-r14/REPORT.md`. For every finite family of nonzero polynomial conditions on each `Sym_n`, the optimal constant over compactly supported smooth inputs and matrices avoiding those algebraic zero sets is still `C_sm=C_all`, provided the final bound is uniform in the genericity gap.

The partner theorem is applied below to an actual extremal inequality, not merely cited as background.

## 3. Work at the interval functional level

For any target law `mu=law(X^TAX)`, define

`M(A,f) = sup_I mu(I)/|I|`,

where the supremum is over bounded nondegenerate intervals. This definition makes sense without assuming a priori that `mu` has a density. If `mu=p(t)dt`, then `M(A,f)=||p||_infinity`.

Let

`C_all = sup M(A,f)`

over the exact owner target class: independent real coordinates with densities bounded by one and symmetric `A` with `s_3(A)>=1`.

## 4. Exact spectral-boundary lemma

### Lemma 4.1 — scaling to `s_3=1` can only increase density height

Fix any target instance and put

`s=s_3(A)>=1`, `B=A/s`.

Then `s_3(B)=1` and

`boxed( M(B,f)=s M(A,f). )`                                        (4.1)

### Proof

Write `Q_A=X^TAX` and `Q_B=X^TBX=Q_A/s`. For every bounded interval `J`,

`P(Q_B in J)=P(Q_A in sJ)`

and `|sJ|=s|J|`. Hence

`P(Q_B in J)/|J| = s P(Q_A in sJ)/|sJ|`.

As `J` ranges over all bounded nondegenerate intervals, `sJ` does also. Taking suprema gives (4.1). No density, Fourier inversion, moment, support, or regularity hypothesis is used. QED.

### Corollary 4.2 — exact boundary reduction

Let

`C_bd = sup{ M(A,f): target instance with s_3(A)=1 }`.

Then

`boxed( C_bd=C_all )`                                               (4.2)

including `+infinity`.

Indeed `C_bd<=C_all` by inclusion, while Lemma 4.1 maps every target instance to the boundary with no loss, in fact with multiplicative gain `s_3(A)`.

Thus the universal problem is exactly a boundary problem. Matrices with three singular values strictly larger than one are never harder in this scale-invariant height functional than their normalization to third singular value one.

## 5. Smooth, continuous-output, algebraically generic boundary class

For each dimension `n`, fix any finite family

`P_n={P_{n,1},...,P_{n,m_n}}`

of nonzero **homogeneous** real polynomials on `Sym_n`. Let

`G_n={A: P_{n,j}(A)!=0 for all j}`.

Homogeneity is imposed only so that `G_n` is invariant under multiplication of `A` by a nonzero scalar. It includes the usual exact nondegeneracies used in QFORM proofs: nonzero physical entries, nonzero prescribed minors, nonzero discriminant/simple spectrum, and any finite list of homogeneous determinant/transversality conditions.

Define `C_norm` as the supremum of `M(A,f)` over instances satisfying all of:

1. every marginal belongs to `C_c^infinity(R)`, is nonnegative, has mass one, and is bounded by one;
2. `A in G_n`;
3. `s_3(A)=1`.

### Theorem 5.1 — exact normalized regular extremal envelope

`boxed( C_norm=C_all=C_sm=C_C0 )`                                  (5.1)

including the value `+infinity`.

### Proof

The class defining `C_norm` is a subclass of the full target, so

`C_norm<=C_all`.

By the completed r14 theorem, the supremum over smooth compact inputs and generic matrices `A in G_n` with `s_3(A)>=1` equals `C_all`. Take any such generic smooth instance. Set `s=s_3(A)` and `B=A/s`. Because every `P_{n,j}` is homogeneous,

`P_{n,j}(B)=s^{-deg P_{n,j}} P_{n,j}(A)!=0`,

so `B` remains in `G_n`; also `s_3(B)=1`. Lemma 4.1 gives

`M(B,f)=s M(A,f)>=M(A,f)`.

Taking the supremum over the generic smooth class yields

`C_norm>=C_all`.

Therefore `C_norm=C_all`. The assigned partner theorem supplies the remaining exact equalities `C_all=C_sm=C_C0`. QED.

## 6. Quantitative partner application to a rough target

The preceding equality can be stated as an explicit approximation inequality useful for proof assembly.

Fix any rough target instance with density `p` and let `eta>0`. The assigned account04/B15 theorem gives a compactly supported smooth cap-one target instance with `C_0` density `p_sm` satisfying

`||p_sm||_infinity >= ||p||_infinity-eta`.                         (6.1)

The r14 genericization equality implies that, allowing another error `eta`, one can choose a smooth algebraically generic target instance with output `p_gen` such that

`||p_gen||_infinity >= ||p||_infinity-2eta`.                       (6.2)

Now put `s=s_3(A_gen)>=1` and `A_norm=A_gen/s`. By Lemma 4.1,

`||p_norm||_infinity = s ||p_gen||_infinity`
`                    >= ||p||_infinity-2eta`,                     (6.3)

with `s_3(A_norm)=1`, and homogeneity preserves every chosen genericity condition.

Equation (6.3) is the actual use of the completed partner mathematics: every rough target height can be approximated from below, with arbitrarily small loss, by a smooth `C_0` output on the exact spectral boundary and in an algebraically generic matrix class.

## 7. Consequences for extremizing or counterexample sequences

### 7.1 Actual maxima, not only essential suprema

Every member of the normalized smooth class has an output density in `C_0(R)` by the partner theorem. Therefore its `L^infinity` norm is attained at some finite point: if `m=||p||_infinity>0`, then `p(t)->0` as `|t|->infinity`, so outside a compact set `p<m/2`, while continuity gives a maximum on that compact set.

Consequently, if `C_all<infinity`, the exact constant is the supremum of **actual pointwise maxima** of continuous densities in the class `s_3(A)=1`, smooth compact product marginals, and any fixed finite homogeneous genericity package.

If `C_all=+infinity`, there exists a sequence in the same class and points `t_k` with

`p_k(t_k)->infinity`.                                                (7.1)

Thus any genuine counterexample to a finite universal constant may be sought on this normalized regular class; rough inputs, exact algebraic degeneracies, and spectral scale `s_3>1` are not necessary to witness failure.

### 7.2 Strict cap slack for an unbounded witness sequence

There is a further useful falsification normal form. Suppose (7.1) holds. For each instance let `Y_i=2X_i`. Then

`g_i(y)=(1/2) f_i(y/2)`,

so `g_i` is smooth, compactly supported, has mass one, and

`||g_i||_infinity<=1/2`.

The matrix is unchanged and still satisfies `s_3(A)=1`, while

`Y^TAY=4 X^TAX`.

Therefore the output density height is divided by four:

`||p_{Y^TAY}||_infinity=(1/4)||p_{X^TAX}||_infinity`.              (7.2)

Divergence is preserved. Hence if the conjectured finite constant is false, it is already false along a sequence with **strict density-cap slack** `||f_i||_infinity<=1/2`, in addition to smooth compact marginals, `C_0` outputs, homogeneous algebraic genericity, and exact `s_3(A)=1`.

This strict-slack statement is only a preservation-of-divergence result; it does not say the optimal finite constant is unchanged by replacing cap one by cap one-half.

## 8. What this does and does not remove

This result removes three inessential sources of extremal complexity:

- spectral scale above the threshold: normalize exactly to `s_3=1`;
- rough/discontinuous input densities when studying the optimal universal height: the partner reduction replaces them by smooth compact inputs with arbitrarily small height loss;
- exact algebraic coincidences: r14 removes any finite homogeneous package of them without changing the supremum.

It does **not** remove the decisive difficulty: the normalized generic matrices may approach the excluded algebraic sets arbitrarily closely. Physical diagonals, determinants, cross-block singular values, leverage gaps, and similar quantities may still tend to zero. Thus an estimate containing an uncancelled reciprocal local-minor price remains insufficient.

The first unpaid implication is now particularly clean:

> Prove one dimension-independent bound on `M(A,f)` for smooth compact cap-one product inputs, homogeneous-algebraically-generic symmetric matrices with `s_3(A)=1`, **uniformly all the way to every algebraic near-degeneracy**.

By Theorem 5.1 that implication is exactly equivalent, at the level of the optimal constant, to the original full QFORM conjecture.

## 9. Regularity ledger

- Absolute continuity: already established for every nonzero quadratic form of an absolutely continuous vector; not redone here.
- Per-instance bounded density and `C_0` representative at rank at least three: account03/B15 r16 supplies a candidate proof pending independent end-to-end review; this report does not rely on that candidate.
- Extremal continuous-output reduction: proved by the completed assigned partner account04/B15 and used in (6.1)-(6.3).
- Exact spectral-boundary reduction `s_3=1`: proved here at the interval functional level, independent of any density-existence theorem.
- Universal matrix- and dimension-independent height: **OPEN / NOT PROVED**.
- Full solution: **OPEN / NOT PROVED**.

No Gaussian, log-concavity, moment, connected-support, diagonal-basis, spectral-coordinate independence, or input-density continuity hypothesis has been added to the original target. The smooth/compact/generic/boundary restrictions in Theorem 5.1 are a proved no-loss extremal reduction, not an assumption on the final theorem.
