SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T15:38:42Z.
attacking: the r32 four-bank cancellation survivor — prove that small aggregate cross-rectangle minor mass forces the ENTIRE selected physical four-bank core, not merely its four blocks separately, into a quantitative rank-one low-tail tube.

# account03/B07 r33 — aggregate minors or a single global physical rank-one tube

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T153842Z-account03-B07-qform-r33`  
Initial research-brain main: `364e58649db5f4e86517dbbc904cc041c301af3e`  
Pre-publication research-brain main: `3707705ffa4f4e7cf71827f5ec4527272bedb1d4`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW PHYSICAL LOW-TAIL COMPILER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The full unrestricted conjecture is not proved or disproved here. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or post-rotation independence assumption is used. All banks below are subsets of the original independent coordinates. No single small coordinate minor is inverted.

## 1. Exact incoming packet and sources

The immediate predecessor is account03/B07 r32,

`yspennstate/math-open-problems@b684b8edb29274a17fd5e8ed7fc8049ce12a4595`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T143815Z-account03-B07-qform-r32/REPORT.md`.

It leaves four mutually disjoint original-coordinate banks and the literal physical block

```
K = [ A  B ]
    [ C  D ]
```

with

`alpha=||A||_F`, `beta=||B||_F`, `gamma=||C||_F`, `delta=||D||_F`,

and selected matching product

`P:=alpha delta > 1.076074733e6 a^2`.                            (1.1)

Define the cross-rectangle determinant mass

`Omega := sum_(i,k,j,l) (A_ij D_kl-B_il C_kj)^2`.               (1.2)

Every summand is the square of a literal original-coordinate `2 x 2` minor. The exact r32 expansion is

`Omega=(alpha delta)^2+(beta gamma)^2-2T`,                      (1.3)

where, by index contraction,

`T=<A^T B,C^T D>_F=<A C^T,B D^T>_F`.                            (1.4)

The designated completed partner is account04/B07,

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T091740Z-account04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

In the same strict-N3 chamber it supplies

`h=(2sqrt(2)-1)/1572864`, `tau0=h^2/128`,                       (1.5)

and the physical coefficient cap

`|A_uv|<=h/8` for every relevant off-diagonal physical entry.   (1.6)

Together with the inherited r30/r31 scale floor, r32 already converted (1.1) to the actual partner-scale inequality

`boxed: P>29598.7122613461 h^2`.                                (1.7)

This run uses (1.6)-(1.7) quantitatively in Section 6.

## 2. A near-equality consequence of small aggregate determinant mass

Fix `0<eps<1` and suppose

`Omega < eps^2 alpha^2 delta^2`, `alpha delta>0`.                (2.1)

From the r32 inequality

`sqrt(Omega)>=|alpha delta-beta gamma|`,                         (2.2)

we get

`beta gamma>(1-eps)alpha delta`.                                (2.3)

Put

`eta:=eps^2/[2(1-eps)]`.                                        (2.4)

Using (1.3) and `(x^2+y^2)/2>=xy`,

`T >= alpha beta gamma delta - Omega/2`
`  > [1-eta] alpha beta gamma delta`.                           (2.5)

Now each factor in either representation (1.4) is individually bounded by the corresponding product of Frobenius norms. Therefore the near-maximal product (2.5) forces all four shared-side correlations:

`||A^T B||_F >(1-eta) alpha beta`,                              (2.6)
`||C^T D||_F >(1-eta) gamma delta`,                            (2.7)
`||A C^T||_F >(1-eta) alpha gamma`,                            (2.8)
`||B D^T||_F >(1-eta) beta delta`.                             (2.9)

This is stronger than four unrelated rank-one approximations: the same determinant cancellation forces simultaneous row- and column-side near-equality.

## 3. Shared-side correlation forces small second compound

### Lemma 3.1

Let `U,V` have the same number of rows and assume

`||U^T V||_F >=(1-eta)||U||_F||V||_F`, `0<=eta<1`.              (3.1)

Set

`tau:=1-(1-eta)^2=2eta-eta^2`.                                 (3.2)

Then

`boxed: E2([U V]) <= tau (||U||_F^2+||V||_F^2)^2`.              (3.3)

Here `E2` is the sum of squares of all `2 x 2` minors, equivalently the second elementary symmetric polynomial in the squared singular values.

### Proof

Since

`||U^T V||_F <= ||U||_op ||V||_F`,                              (3.4)

we have

`||U||_op^2 >=(1-eta)^2 ||U||_F^2`.                            (3.5)

Thus the squared singular-value tail of `U` is at most `tau||U||_F^2`. If `S_U=||U||_F^2` and `R_U` is that tail, then

`E2(U)<=S_U R_U<=tau S_U^2`.                                   (3.6)

The same holds for `V`. The total squared minor mass using one column from `U` and one from `V` is the exact wedge identity

`S_U S_V-||U^T V||_F^2 <=tau S_U S_V`.                         (3.7)

Adding (3.6)-(3.7) gives

`E2([U V])<=tau(S_U^2+S_V^2+S_U S_V)`
`          <=tau(S_U+S_V)^2`.                                  (3.8)

QED.

The transposed version applies to vertical concatenations.

## 4. Exact physical minor partition and the global low-tail theorem

The `2 x 2` minors of `K` partition exactly according to whether their two rows are both in the top bank, both in the bottom bank, or split; and likewise for columns. This gives

`E2(K)=E2([A B])+E2([C D])+E2([A;C])+E2([B;D])`
`      -E2(A)-E2(B)-E2(C)-E2(D)+Omega`.                         (4.1)

The last term is exactly the mixed-row/mixed-column mass (1.2); the four internal block masses are the overlap of the horizontal and vertical terms.

Let

`S:=||K||_F^2=alpha^2+beta^2+gamma^2+delta^2`.                  (4.2)

Apply Lemma 3.1 to (2.6)-(2.9). Since the two horizontal squared norms sum to `S`, and the two vertical squared norms also sum to `S`,

`(alpha^2+beta^2)^2+(gamma^2+delta^2)^2`
` +(alpha^2+gamma^2)^2+(beta^2+delta^2)^2 <=2S^2`.              (4.3)

Dropping the nonnegative subtractions in (4.1),

`E2(K)<=2tau S^2+Omega`.                                        (4.4)

By AM-GM and (2.3),

`S >=2alpha delta+2beta gamma`
`  >2(2-eps)alpha delta`.                                       (4.5)

Therefore

`Omega < [eps^2/(4(2-eps)^2)] S^2`.                            (4.6)

Define

`Delta(eps):=2[2eta-eta^2]+eps^2/[4(2-eps)^2]`,                (4.7)

with `eta` from (2.4). Then

`boxed: E2(K)<Delta(eps) S^2`.                                 (4.8)

### Theorem 4.1 — `QFORM-BANKCYCLE-GLOBAL-LOWTAIL-v1`

Assume (2.1) and `Delta(eps)<1/4`. If `s1>=s2>=...` are the singular values of the literal physical block `K`, put

`R=sum_(j>=2) s_j^2`.                                           (4.9)

Then

`boxed: R/S < Theta(eps)`,                                      (4.10)

where

`Theta(eps)=[1-sqrt(1-4Delta(eps))]/2`.                         (4.11)

Equivalently,

`boxed: dist_F(K,rank<=1)<sqrt(Theta(eps)) ||K||_F`,            (4.12)

and

`boxed: sqrt(R)/s1 < sqrt[Theta(eps)/(1-Theta(eps))]`.          (4.13)

### Proof

Write `x_j=s_j^2`. If `R>=S/2`, then `x_1<=S/2`; since every `x_j<=x_1<=S/2`,

`sum_j x_j^2 <=(S/2)sum_jx_j=S^2/2`.                            (4.14)

Hence

`E2(K)=[S^2-sum_jx_j^2]/2>=S^2/4`,                             (4.15)

contradicting (4.8). Thus `R<S/2`.

Also

`E2(K)>=s1^2 R=(S-R)R`.                                        (4.16)

On `[0,1/2]`, `r(1-r)` is increasing. With `r=R/S`, (4.8) and (4.16) imply

`r(1-r)<Delta(eps)`,                                            (4.17)

so `r<Theta(eps)`. This proves (4.10)-(4.13). QED.

The result is genuinely stronger than r32's four separate block tubes: the **entire selected physical four-bank core** is now within one dimension-free Frobenius tube around a single rank-one matrix.

## 5. Concrete `eps=1/64` low-tail alternative

Take

`eps=1/64`.                                                      (5.1)

Then exactly

`eta=1/8064`,
`tau=16127/65028096`,
`Delta=268240895/524419080192`
`     =0.0005115010210951741...`.                              (5.2)

Thus

`Theta=0.0005117629223839182...`,                               (5.3)

and Theorem 4.1 gives

`boxed: dist_F(K,rank<=1)<0.022622178 ||K||_F`,                 (5.4)

`boxed: [sum_(j>=2)s_j(K)^2]^(1/2)/s1(K)<0.022627969`.          (5.5)

The early checkpoint in this run used the looser inequality `Omega<eps^2 S^2/4` and obtained `0.023608194`; it remains valid, but (5.4) is the authoritative sharpened constant.

This is the requested actual physical-core / low-tail alternative. No individual determinant is selected, no reciprocal small minor is paid, and no random-coordinate rotation is introduced.

## 6. Designated account04/B07 result applied to actual inequalities

Insert the partner-scale matching lower bound (1.7). The r32 packet now has the exhaustive alternative

### Aggregate-minor branch

`boxed: sqrt(Omega)>=P/64>462.4798790835328 h^2`.               (6.1)

By the partner physical coefficient cap (1.6), every constituent determinant obeys

`|A_ijD_kl-B_ilC_kj|<=2(h/8)^2=h^2/32`.                        (6.2)

Consequently (6.1) forces at least

`boxed: 219,020,942`                                            (6.3)

nonzero literal cross-rectangle physical minors. Indeed each squared term is at most `h^4/1024`, while `Omega>(462.479879...)^2 h^4`. This is deterministic diffusion evidence, not a Monte-Carlo argument and not by itself an analytic density receiver.

### Global physical low-tail branch

Otherwise (5.4)-(5.5) hold. Moreover

`S>=alpha^2+delta^2>=2alpha delta=2P`.                           (6.4)

Hence

`s1(K)>sqrt[2(1-Theta)P]`
`     >243.24294332152962 h`.                                   (6.5)

Let `u,v` be unit top left/right singular vectors. The partner cap (1.6) gives

`s1=|u^T K v| <=(h/8)||u||_1||v||_1`,                           (6.6)

so the dominant physical rank-one direction also obeys the quantitative delocalization certificate

`boxed: ||u||_1||v||_1>1945.943546572237`.                     (6.7)

This is an actual use of the designated partner's completed coefficient cap. It does **not** by itself imply a maximum-leverage bound; no such claim is made.

## 7. Interface with the newest volume-stability package

The current owner continuation asks B07 for an actual physical-core or low-tail alternative from N3. The theorem above supplies exactly that. I also checked the newest volume-stability receiver rather than silently treating low Frobenius tail as a paid analytic branch.

That receiver requires, for an appropriate two-dimensional range projection, both a leverage gate and an operator-tail-to-collective-tail gate; its quantitative density bound contains `[s1^2 s2^2 T2]^(-1/6)`. The new branch (5.4) permits `s2` and `T2` to tend to zero, so it does **not** automatically meet a universal version of that receiver. Thus the valid source-matching conclusion is an exact incompatibility at this point: the current low-tail alternative must next be joined to a rank-one/hub/grouped-coordinate receiver, not declared paid by volume stability.

This preserves the source warning that a small matrix tail is not a uniformly small random quadratic perturbation on arbitrary unbounded product inputs.

## 8. What changed in the proof map

Before this run, the r32 cancellation survivor was only

`four separate rank-one block tubes`.

That did not identify one coherent low-dimensional physical core and could not be safely substituted into a global low-rank theorem. The determinant identity itself contains more information: near cancellation forces four shared-side Gram contractions to be simultaneously near equality. That is enough to compile the entire four-bank block into one global rank-one tube with an explicit `2.27%` Frobenius tail.

Accordingly the first B07 debt is now

`QFORM-BANKCYCLE-AGGREGATE-E2-OR-GLOBAL-R1-RECEIVER-v1`:

1. consume the aggregate physical `E2`/cross-minor branch (6.1) while retaining arbitrary same-bank curvature and the true ambient remainder; or
2. consume the literal global physical rank-one tube (5.4)-(6.7), retaining its nonzero tail, arbitrary within-bank curvature, outside couplings, and all additional spectrum.

A promising next mechanism is a product-preserving grouped-coordinate or one-hub receiver that treats the rank-one dominant mode exactly while keeping the `2.27%` matrix tail at the matrix/Fourier level. The current account03/B01 diagonal-plus-low-rank theorem is not invoked as though (5.4) implied its exact finite-rank hypothesis.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** This run proves a deterministic structural theorem only; it makes no new continuity claim.

## 9. Deterministic checks and source integrity

`CHECKS.py` and captured `CHECKS.txt` accompany this report. They verify:

- the exact physical-minor partition (4.1) on 400 finite random integer blocks;
- the theorem's `E2/S^2` and singular-tail inequalities on 2,000 near-coherent finite matrices satisfying the aggregate-minor premise;
- all exact rational and partner-scale constants in Sections 5-6.

The captured result ends `STATUS=PASS`. These computations are regression evidence only; the proof is Sections 2-6.


Repository transport is not native learned-memory ingestion. Execution remains `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.
