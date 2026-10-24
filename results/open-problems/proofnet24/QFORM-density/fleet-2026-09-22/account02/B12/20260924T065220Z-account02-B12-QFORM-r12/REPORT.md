SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T06:52:20.280735Z.
attacking: antipodal relative resonance — prove that a near-`-I` symmetric relative action is harmless when its compressed skew part has five surviving modes, with arbitrary dense tails paid only at coefficient-matrix level.

# account02/B12 — antipodal-skew rescue for arbitrary signed added spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Partner: account03/B12  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target is unchanged: independent ORIGINAL coordinates `X_i` with scalar densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one; prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moments, bounded support, log-concavity, diagonal-basis independence, or post-rotation independence are assumed.

The first unpaid implication after the completed relative-resonance work is structural. Starting only from `s_3(A)>=1`, one must force either a bounded ORIGINAL-coordinate carrier with five quantitatively nonresonant relative directions, or a previously paid physical-core / physical-pair / projected-crossing / grouped-bank / hub / ridge / Schur / common-plane / Pluecker exit. In particular, the live `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction forbids assuming a universal carrier scale for free.

This run narrows the relative-resonance obstruction. A relative map may have its **entire symmetric part exactly antipodal**, `Sym K=-I`, so the previous numerical-range lower bound is zero in every direction, while a skew relative component preserves all carrier singular values. Thus a genuinely destructive packet must be not only near `-I` in symmetric part, but also low-mode in the skew component on that near-antipodal sector.

## 2. Sources actually used

Latest compatible designated partner: account03/B12 r50, canonical report

`yspennstate/math-open-problems@e5c25693bac41b18a8258b6c76f5c7c41eac085b`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T054748Z-qform-eigenvalue-r50/REPORT.md`.

Its exact theorem is the relative-action factorisation. For an ORIGINAL-coordinate embedding `P:R^m->R^n`, baseline carrier `M=A_*P` of full column rank, `g=s_m(M)>0`, and an arbitrary symmetric signed addition `S`, put

`K=M^dagger S P`, `Z=(I-MM^dagger)SP`.

Then

`(A_*+S)P=M(I+K)+Z`, `M^T Z=0`,

and hence, for every `j`,

`boxed: s_j((A_*+S)P) >= g s_j(I+K).`                 (2.1)

No norm bound on `S`, `SP`, `K`, the transverse action `Z`, or the complement spectrum is assumed.

Required pinned source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I reread `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed `D_5` theorem from `FOURIER_ROUTE_REPORT.md` states that for any literal disjoint ORIGINAL-coordinate cross block `B=A[I,J]`, with

`Z_5=e_5(B^T B)`,

one has, with no marginal condition,

`boxed: ||p_(X^T A X)||_infinity <= 5 sqrt(2e) Z_5^(-1/10).`     (2.2)

The pinned source also records that arbitrary-joint 3D coarea is false and that product provenance must be retained. The proof below never uses that false interface.

## 3. Main theorem: compressed scalar-skew shield

Write the partner relative action as

`L=I+K`.

Split it into symmetric and skew parts in the dimensionless carrier metric:

`B=I+Sym(K)`,
`Omega=Skew(K)=(K-K^T)/2`,

so `L=B+Omega`, `B^T=B`, `Omega^T=-Omega`.

Let `U` be any subspace of `R^m` with `dim U>=5`, and let `P_U` denote orthogonal projection onto `U`. Suppose there are numbers `d in R`, `epsilon>=0`, `rho>=0` such that

`|| P_U B P_U - d I_U ||op <= epsilon`,                    (3.1)

and

`s_5(P_U Omega P_U) >= rho`.                               (3.2)

### Theorem 3.1 — `QFORM-ANTIPODAL-SKEW-RESCUE-v1`

Under the setup above,

`boxed:
 s_5(I+K) >= [ sqrt(d^2+rho^2) - epsilon ]_+.`             (3.3)

Consequently the partner factorisation gives

`boxed:
 s_5((A_*+S)P)
 >= g [ sqrt(d^2+rho^2) - epsilon ]_+.`                    (3.4)

If an additional arbitrary globally dense symmetric tail `T` satisfies

`||T||op<=delta`,

then with `A=A_*+S+T`,

`boxed:
 s_5(A P)
 >= [ g( sqrt(d^2+rho^2)-epsilon ) - delta ]_+.`           (3.5)

Because `A` is symmetric,

`(AP)^T(AP)=P^T A^2 P=(A^2)[H,H]`,

so the same quantity is a final five-square-mode reserve:

`boxed:
 sqrt(lambda_5((A^2)[H,H]))
 >= [ g( sqrt(d^2+rho^2)-epsilon ) - delta ]_+.`           (3.6)

### Proof

Compression cannot increase singular values. More precisely, if `J_U:U->R^m` is the inclusion, then both `P_U` and `J_U` are contractions, so for every `j<=dim U`,

`s_j(P_U L J_U) <= s_j(L)`.

Hence

`s_5(L) >= s_5(P_U L P_U|_U).`                            (3.7)

Write

`P_U B P_U = d I_U + E_U`, `||E_U||op<=epsilon`,
`Omega_U=P_U Omega P_U|_U`.

Then

`P_U L P_U|_U = d I_U + Omega_U + E_U`.

Singular-value Weyl gives

`s_5(P_U L P_U|_U)
 >= s_5(d I_U+Omega_U)-epsilon.`                           (3.8)

Since `Omega_U^T=-Omega_U`,

`(dI+Omega_U)^T(dI+Omega_U)
 = d^2 I - Omega_U^2
 = d^2 I + Omega_U^T Omega_U`.

Therefore the singular values of `dI+Omega_U` are exactly

`s_j(dI+Omega_U)=sqrt(d^2+s_j(Omega_U)^2)`.

Using (3.2) in (3.8), then (3.7), proves (3.3). Equation (3.4) is the completed partner inequality (2.1). For the dense tail,

`||(TP)||op<=||T||op<=delta`,

so singular-value Weyl gives (3.5). Symmetry of the final coefficient matrix gives (3.6). QED.

### Important endpoint

At exact antipodal symmetric resonance,

`P_U(I+Sym K)P_U=0`,

we may take `d=0`, `epsilon=0`, and obtain

`boxed: s_5(I+K) >= s_5(P_U Skew(K) P_U).`                 (3.9)

Thus `Sym K=-I` is **not** by itself destructive. Five skew modes inside the antipodal sector rescue five carrier modes at their full relative scale.

## 4. A structural trichotomy for failure

The preceding theorem can be turned into an obstruction normal form requiring no scalar ansatz.

Fix `eta>0`. Let

`B=I+Sym(K)`

and decompose `R^m` into its spectral subspaces

`U_+ = 1_[eta,infinity)(B) R^m`,
`U_- = 1_(-infinity,-eta](B) R^m`,
`U_0 = 1_(-eta,eta)(B) R^m`.

Let `Omega_0=P_0 Omega P_0|_(U_0)`.

### Theorem 4.1 — `QFORM-RELATIVE-RESONANT-NORMAL-FORM-v1`

If any one of the following holds,

1. `dim U_+ >=5`;
2. `dim U_- >=5`;
3. `dim U_0 >=5` and `s_5(Omega_0) >=2 eta`,

then

`boxed: s_5(I+K) >= eta.`                                  (4.1)

Equivalently, if

`s_5(I+K)<eta`,                                             (4.2)

then necessarily

`boxed:
 dim U_+ <=4,
 dim U_- <=4,
 dim U_0 >= m-8,
 s_5(Omega_0)<2 eta.`                                      (4.3)

So a packet that genuinely kills the fifth relative mode must be close to the symmetric cancellation `-I` on all but at most eight relative directions, and its skew action on that large near-antipodal sector must itself have fewer than five modes at scale `2 eta`.

### Proof

On `U_+`, the compressed symmetric part obeys `B_+>=eta I`. Since `Omega_+` is skew,

`x^T(B_++Omega_+)x=x^T B_+ x >= eta ||x||^2`.

By Cauchy-Schwarz,

`||(B_++Omega_+)x|| >= eta ||x||`.

Thus if `dim U_+>=5`, its compressed operator has at least five singular values at least `eta`, and therefore so does `L=B+Omega`. The same argument applies to `U_-` after multiplying the compression by `-1`.

On `U_0`, `||B_0||op<eta`. Hence singular-value Weyl gives

`s_5(B_0+Omega_0)
 >= s_5(Omega_0)-||B_0||op.
`

If `s_5(Omega_0)>=2eta`, this is at least `eta`; compression again transfers the lower bound to `s_5(L)`. This proves (4.1). Its contrapositive gives the first, second and fourth conclusions in (4.3); the dimension count gives `dim U_0>=m-8`. QED.

### Dense-tail compiler

Combining (4.1) with the partner theorem and an arbitrary dense tail `||T||op<=delta` gives

`boxed:
 sqrt(lambda_5((A^2)[H,H])) >= [g eta-delta]_+.`            (4.4)

Whenever

`r:=g eta-delta>0`,

the completed account03/B12 five-square-mode compiler yields

`boxed:
 ||p_(X^T A X)||infinity
 <= sqrt(24*pi*m+K3^2)/r,
 K3=3*2^(4/3)*exp(1/3).`                                   (4.5)

This branch has a continuous `C_0(R)` density. All probabilistic conditioning in that compiler is on literal original-coordinate banks; no spectral rotation is used to assert independence.

## 5. Strict obstruction to the previous two easy criteria

The theorem is not a reformulation of either the previous numerical-range shield or the partner rank-tail corollary.

Take `m=6` and

`J_6=diag(R,R,R)`, `R=[[0,1],[-1,0]]`,

so `J_6^T=-J_6`, `J_6^T J_6=I_6`. For `c>0`, define

`K_c=-I_6+c J_6`.                                           (5.1)

Then

`Sym K_c=-I_6`,
`Skew K_c=cJ_6`,
`I+K_c=cJ_6`,

and therefore

`boxed: s_5(I+K_c)=c.`                                     (5.2)

The previous numerical-range certificate `[1+lambda_5(Sym K_c)]_+` is identically zero.

Also

`K_c^T K_c=(1+c^2)I_6`,

so all six singular values of `K_c` equal `sqrt(1+c^2)`. The partner rank-tail corollary for `m=6` permits a rank at most `m-5=1` exceptional term and requires residual norm `<1`. By Eckart-Young, after subtracting any rank-one matrix the residual norm is at least

`s_2(K_c)=sqrt(1+c^2)>1`.

Thus that corollary gives no certificate. The exact partner theorem is of course still valid, and Theorem 3.1 provides the missing simple geometric certificate: take `U=R^6`, `d=epsilon=0`, `rho=c`.

## 6. Literal symmetric signed-spectrum realisation

The relative example above is realised by a genuine symmetric coefficient matrix without any probabilistic rotation.

Let `H` and `J` be two disjoint six-coordinate ORIGINAL banks. Put

`A_0 = [[0,2I_6],[2I_6,0]]`

on `H union J`, with any further coordinates initially decoupled. Let `P_H` be the coordinate embedding. Then

`M=A_0P_H`, `M^T M=4I_6`, `g=2`.

Define the arbitrary signed addition

`S_c = [[0,2K_c^T],[2K_c,0]]`.                              (6.1)

This is symmetric. Moreover

`M^dagger S_c P_H = K_c`,                                   (6.2)

so Theorem 3.1 and the partner factorisation give

`boxed: s_5((A_0+S_c)P_H) >= 2c.`                          (6.3)

In fact equality holds. The actual physical cross block is

`B_c=(A_0+S_c)[H,J]
    =2(I_6+K_c^T)
    =-2c J_6`,                                              (6.4)

whose six singular values all equal `2c`.

The added matrix itself has eigenvalues

`+2sqrt(1+c^2)` and `-2sqrt(1+c^2)`, each with multiplicity six,

so this is a genuine large signed spectral packet. Its magnitude may be arbitrarily large.

Append an arbitrary-dimensional spectator block `Theta=Theta^T`, with unrestricted signs, multiplicities, internal mixing and eigenvalue magnitudes. Then add any globally dense symmetric tail

`||T_dense||op<=delta`.                                     (6.5)

No assumption is made that `X^T T_dense X` is a small random variable.

## 7. Required pinned D5 theorem applied to the actual final matrix

Take the concrete stress scale

`c=1`, `delta=1/64`.

For the literal final original-coordinate cross block

`B_final=A[H,J]=B_1+T_dense[H,J]`,

physical compression gives

`||T_dense[H,J]||op<=1/64`.

Therefore singular-value Weyl gives the real final inequality

`boxed:
 s_5(B_final) >= 2-1/64 = 127/64.`                          (7.1)

Consequently

`e_5(B_final^T B_final)
 >= product_(j=1)^5 s_j(B_final)^2
 >= (127/64)^10.`                                           (7.2)

Now apply the completed pinned theorem (2.2):

`boxed:
 ||p_(X^T A X)||infinity
 <= 5 sqrt(2e)/(127/64)
 = 5.875008457567557... .`                                  (7.3)

This is an inequality for the **actual final physical cross block**, not a common spectral subspace and not a rotated-law surrogate. It retains arbitrary same-bank quadratic terms, the entire spectator spectrum, and every dense-tail coupling.

For comparison, the partner five-square-mode compiler applied to the same final reserve gives

`||p_Q||infinity <= sqrt(144*pi+K3^2)/(127/64)
                  = 11.964608713325852...`,

so the pinned `D_5` receiver is sharper for this stress family.

## 8. The family is literally in the exact owner target

Before the dense tail, the twelve-coordinate core is

`[[0,-2J_6],[2J_6,0]]`.

A symmetric off-diagonal block matrix `[[0,C],[C^T,0]]` has eigenvalues `+s_j(C)` and `-s_j(C)`. Hence this core has twelve eigenvalues of modulus `2` when `c=1`.

The arbitrary spectator direct sum cannot remove those twelve singular directions. After the globally dense tail of norm at most `1/64`, singular-value Weyl gives

`boxed:
 s_12(A_final) >= 2-1/64 = 127/64 >1.`                      (8.1)

Since the final matrix is symmetric, its singular values are the absolute values of its eigenvalues. In particular, it has at least three eigenvalues of modulus at least one, uniformly over every spectator `Theta` and every allowed dense tail.

Thus the construction is not merely a carrier toy: every member lies in the exact target class.

## 9. Dense-tail and provenance safeguards

The dense tail is used only through deterministic coefficient inequalities such as

`||T_dense P_H||op<=||T_dense||op`,
`||T_dense[H,J]||op<=||T_dense||op`,

and singular-value Weyl.

No assertion of the form `|X^T T_dense X|<=o(1)` is used; such an assertion is false uniformly for arbitrary unbounded cap-one inputs. For example, with `T_dense=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, one has `X^T T_dense X>=delta R^2` almost surely.

Likewise, all random variables remain the original independent coordinates. The matrices `K`, `B`, `Omega` and the spectral projections in Section 4 are deterministic coefficient-space devices only. They are never used as a random change of basis, and no independence is claimed after rotation.

## 10. What remains unpaid

This run eliminates another false obstruction: **near-antipodal symmetric relative action is not enough to destroy a carrier**. The skew action on that sector matters, and five skew modes rescue five square modes even when `Sym K=-I` exactly.

The new failure normal form is (4.3): if a relative packet destroys the fifth mode at scale `eta`, then, apart from at most eight directions, `I+Sym K` lies inside the narrow interval `(-eta,eta)` and the skew compression on that large near-antipodal sector has fifth singular value `<2eta`.

The next useful implication is therefore geometric: turn this nearly symmetric, low-skew, near-`-I` relative normal form into an ORIGINAL-coordinate certificate — ideally a literal physical pair, projected crossing, grouped-bank hub, or Schur/common-plane exit. Starting only from `s_3(A)>=1`, one must still force a bounded carrier to which this normal form applies, or reach one of those already-paid exits. That extraction remains open, so this report does not claim the unrestricted theorem.

## 11. Status

Claim proved here: `QFORM-ANTIPODAL-SKEW-RESCUE-v1` together with the failure normal form `QFORM-RELATIVE-RESONANT-NORMAL-FORM-v1`.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Continuity: obtained only through the cited completed five-mode or pinned `D_5` Fourier receiver where invoked; it is not separately claimed for the unrestricted problem.
