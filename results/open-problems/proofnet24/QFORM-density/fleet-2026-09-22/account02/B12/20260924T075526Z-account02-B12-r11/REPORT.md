SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T07:55:26Z.
attacking: adaptive multi-packet canonical-angle rank spending on an original-coordinate carrier, then an actual physical-cross D5 receiver under an arbitrary dense operator-norm tail.

# account02/B12 — adaptive multi-packet canonical-angle stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T075526Z-account02-B12-r11`  
Status: **NEW SUPPORTING STABILITY THEOREM + STRICTNESS CONSTRUCTION / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and first unpaid implication

The full target remains: independent real coordinates with arbitrary densities bounded by one, and an arbitrary real symmetric coefficient matrix with at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, iid hypothesis, diagonal-basis assumption, or independence after a spectral rotation is used.

The newest compatible designated partner is account03/B12 r52:

- canonical mathematics: `yspennstate/math-open-problems@3fa0b38081ce4d0c44c074febf188dede6f6f6ae`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T074439Z-qform-eigenvalue-r52/REPORT.md`;
- theorem: `QFORM-PRINCIPAL-ANGLE-SPECTRUM-SHIELD-v1`.

If `M,N in R^(p x d)`, `M` has full column rank, `g=s_d(M)`, and `c_1>=...>=c_d` are the canonical correlations between `Ran(M)` and `Ran(N)`, then for `q=0,...,d-1`,

` s_(d-q)(M+N) >= g sqrt(1-c_(q+1)^2). `                 (1.1)

This run closes the **composition** step for many arbitrary packets. The remaining target-level implication is still structural: from only `s_3(A)>=1`, force either a bounded ORIGINAL-coordinate carrier for which the cumulative adaptive resonance budget below leaves at least five modes, or one of the already-paid physical-pair / projected-crossing / grouped-bank / ridge / hub / Schur / common-plane / Pluecker-volume exits. Nothing below asserts that such a carrier follows automatically from `s_3(A)>=1`.

## 2. Adaptive multi-packet theorem

Let

`M_0 in R^(p x m)`

have full column rank, and let `N_1,...,N_R in R^(p x m)` be completely arbitrary packets. Their ranks and operator norms are unrestricted.

Choose integers `q_r>=0`. Put

`d_0=m`, `V_0=I_m`, `M_r=M_0+sum_(ell=1)^r N_ell`.

Inductively suppose `V_(r-1):R^(d_(r-1))->R^m` is an isometry and

`g_(r-1)=s_(d_(r-1))(M_(r-1)V_(r-1))>0`.

Let

`c_1^(r)>=...>=c_(d_(r-1))^(r)>=0`

be the canonical correlations between

`Ran(M_(r-1)V_(r-1))`

and

`Ran(N_r V_(r-1))`.

Assume `q_r<=d_(r-1)-1`, define

`eta_r=sqrt(1-(c_(q_r+1)^(r))^2)`,
`d_r=d_(r-1)-q_r`,

and assume `eta_r>0` whenever another stage remains.

### Theorem 2.1 — `QFORM-ADAPTIVE-MULTIPACKET-ANGLE-BUDGET-v1`

If `Q=sum_r q_r<m`, then

`boxed:
 s_(m-Q)(M_R)
 >= s_m(M_0) prod_(r=1)^R eta_r.`                           (2.1)

Consequently, for any further matrix `E` with `||E||op<=delta`,

`boxed:
 s_(m-Q)(M_R+E)
 >= [s_m(M_0) prod_r eta_r-delta]_+.`                       (2.2)

No size, rank or sign condition occurs on any `N_r`.

### Proof

At stage `r`, apply the partner theorem (1.1) to the compressed pair

`M=M_(r-1)V_(r-1)`, `N=N_rV_(r-1)`.

It gives

` s_(d_r)(M_rV_(r-1)) >= g_(r-1) eta_r. `                  (2.3)

Let `W_r:R^(d_r)->R^(d_(r-1))` be an isometry onto the top `d_r` right-singular subspace of `M_rV_(r-1)`, and set

`V_r=V_(r-1)W_r`.

Then

` s_(d_r)(M_rV_r)=s_(d_r)(M_rV_(r-1))
                  >=g_(r-1)eta_r. `                        (2.4)

Induction yields

` s_(d_R)(M_RV_R)>=s_m(M_0)prod_r eta_r. `                 (2.5)

The singular-value max-min principle says

` s_(d_R)(M_R)
  =max_(dim L=d_R) min_(x in L, ||x||=1)||M_Rx||, `

so using the particular subspace `Ran(V_R)` proves (2.1). Equation (2.2) is ordinary singular-value Weyl.

The subspaces `V_r` are deterministic matrix-proof subspaces only. They are never used as transformed random coordinates, so no independence-after-rotation assertion is made.

## 3. Scalar cumulative overlap budget

At each stage put

`Omega_r=tr(Pi_(Ran(M_(r-1)V_(r-1))) Pi_(Ran(N_rV_(r-1))))
        =sum_i (c_i^(r))^2.`

Monotonicity of the canonical correlations gives

`(q_r+1)(c_(q_r+1)^(r))^2<=Omega_r`.                        (3.1)

Hence, with

`B=sum_r Omega_r/(q_r+1)`,

whenever `B<1`,

`prod_r eta_r
 =sqrt(prod_r(1-(c_(q_r+1)^(r))^2))
 >=sqrt(1-sum_r(c_(q_r+1)^(r))^2)
 >=sqrt(1-B).`                                               (3.2)

Thus

`boxed:
 s_(m-Q)(M_R+E)
 >=[s_m(M_0)sqrt(1-B)-delta]_+.`                            (3.3)

This is an additive **resonance-energy budget** for arbitrarily many packets. Large packet norm by itself costs nothing. Exact orthogonality at a stage (`c_1^(r)=0`) costs neither scale nor dimension; `q_r` is needed only for resonant directions one chooses to spend.

Because the final sum is independent of the packet ordering, every ordering gives a valid certificate. One may therefore choose a decomposition/order that maximizes the surviving product without changing the final coefficient matrix.

## 4. QFORM carrier-column specialization

Let `H` be `m` ORIGINAL coordinates with coordinate embedding `P_H`. Let

`A=A_0+S_1+...+S_R+T`

be symmetric, where every `S_r` is an arbitrary symmetric signed packet and `T` is an arbitrary symmetric dense tail with

`||T||op<=delta`.

Apply Theorem 2.1 with

`M_0=A_0P_H`, `N_r=S_rP_H`, `E=TP_H`.

If `Q=sum q_r` and

`h=s_m(A_0P_H)prod_r eta_r-delta>0`,                       (4.1)

then, since `A` is symmetric,

`boxed:
 sqrt(lambda_(m-Q)((A^2)[H,H]))
 =s_(m-Q)(AP_H)
 >=h.`                                                       (4.2)

If `m-Q>=5`, then in particular

`lambda_5((A^2)[H,H])>=h^2`.                                (4.3)

Therefore the completed five-square-mode compiler quoted in account03/B12 r52 gives the dependence-safe full-law bound

`||p_(X^TAX)||_infinity
 <=sqrt(24*pi*m+K_3^2)/h`,
`K_3=3*2^(4/3)*exp(1/3)`.                                   (4.4)

This branch uses only ORIGINAL-coordinate conditioning in its probabilistic receiver. The adaptive right-singular subspaces occur solely inside the deterministic proof of (4.2).

## 5. Physical-cross specialization and the pinned D5 theorem

The required pinned source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,
including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in their latest compatible state.

Its completed unrestricted fifth-volume theorem D5 states for a literal ORIGINAL-coordinate cross block `B=A[I,J]`, with arbitrary same-side blocks, outside coordinates/couplings and affine terms retained,

`boxed:
 ||p_(X^TAX)||_infinity
 <=5 sqrt(2e) E_5(B)^(-1/10),
 E_5(B)=e_5(B^T B),`                                        (5.1)

with no fifth-volume row-marginal condition.

Now take `M_0=A_0[I,J]`, `N_r=S_r[I,J]`, with `|J|=m`. If `m-Q>=5` and the reserve `h` in (4.1) is positive, Theorem 2.1 gives

`s_5(A[I,J])>=h`.                                            (5.2)

Therefore

`E_5(A[I,J])
 >=prod_(j=1)^5 s_j(A[I,J])^2
 >=h^10`,                                                    (5.3)

and the pinned theorem yields the concrete hybrid compiler

`boxed:
 ||p_(X^TAX)||_infinity
 <=5 sqrt(2e)/h.`                                            (5.4)

This is the requested real use of a completed result from the pinned source.

## 6. Strictness: two transverse packets whose sum is perfectly aligned

The adaptive theorem is not merely the one-packet theorem applied to the total perturbation.

Take two disjoint ORIGINAL-coordinate banks `I,J`, with `|I|=10`, `|J|=5`, and split `I=I_0 union I_1` into two five-coordinate banks. In row-block notation define the baseline cross map

`M_0=[2 I_5; 0]`                                              (6.1)

and, for any `L>0`, the two packets

`N_1=[0; L I_5]`,                                             (6.2)

`N_2=[(L^2/2) I_5; -L I_5]`.                                (6.3)

Then

`M_0^T N_1=0`,                                                (6.4)

and with `M_1=M_0+N_1=[2I_5;LI_5]`,

`M_1^T N_2
 =2(L^2/2)I_5-L^2I_5
 =0`.                                                         (6.5)

Hence at both stages **all** canonical correlations are zero. Taking `q_1=q_2=0`, Theorem 2.1 gives

`s_5(M_0+N_1+N_2)>=2`.                                       (6.6)

In fact

`N_1+N_2=[(L^2/2)I_5;0]`,                                   (6.7)

so

`M_0+N_1+N_2=[(2+L^2/2)I_5;0]`                              (6.8)

and all five singular values equal `2+L^2/2`.

But (6.7) has exactly the **same range** as `M_0`. Thus the one-shot canonical correlations between `Ran(M_0)` and `Ran(N_1+N_2)` are

`c_1=...=c_5=1`.                                              (6.9)

For a five-mode receiver one cannot spend even one direction, so the one-shot r52 estimate at `q=0` gives only zero. The sequential adaptive certificate gives the full baseline floor. Therefore collapsing several signed packets into their total range can destroy all angle information even when every packet is individually transverse to the carrier state it actually encounters.

This is a source-valid obstruction to a **one-shot angle-only composition rule**, not a counterexample to QFORM.

## 7. Symmetric exact-target realization with unbounded signed packet spectra

Realise (6.1)-(6.3) by symmetric matrices on the physical coordinates `I union J`:

`A_0=[[0,M_0],[M_0^T,0]]`,
`S_r=[[0,N_r],[N_r^T,0]]`.                                  (7.1)

Each `S_r` is a genuine signed spectral addition. `S_1` has nonzero eigenvalues `+L` and `-L`, each with multiplicity five. `S_2` has nonzero eigenvalues

`+L sqrt(1+L^2/4)` and `-L sqrt(1+L^2/4)`,

each with multiplicity five. Their magnitudes are unbounded as `L->infinity`.

Before any dense tail,

`A_*=A_0+S_1+S_2
    =[[0,M_*],[M_*^T,0]],
 M_*=[(2+L^2/2)I_5;0]`.                                     (7.2)

Thus `A_*` has ten nonzero eigenvalues

`+(2+L^2/2)` and `-(2+L^2/2)`,

five of each.

Append an arbitrary-dimensional direct-sum symmetric spectator spectrum `Theta`, with arbitrary signs, multiplicities and magnitudes, and then add **any globally dense symmetric** tail `T` satisfying

`||T||op<=1/4`.                                               (7.3)

For the actual final physical cross block `B=A[I,J]`,

`s_5(B)
 >=2+L^2/2-1/4.`                                             (7.4)

For every `L>=1`,

`boxed: s_5(B)>=9/4.`                                        (7.5)

The pinned D5 theorem therefore gives the real final-matrix inequality

`boxed:
 ||p_(X^TAX)||_infinity
 <=5 sqrt(2e)/(9/4)
 =20 sqrt(2e)/9
 =5.181431070215832... .`                                    (7.6)

The bound is uniform as the signed packet eigenvalues tend to infinity.

The same family lies literally in the owner's exact target class. Before the dense tail the off-diagonal core contributes ten singular values `2+L^2/2`; an arbitrary direct-sum spectator cannot remove them. Weyl therefore gives

`boxed:
 s_10(A)>=2+L^2/2-1/4>=9/4>1`                               (7.7)

for every `L>=1`. Since `A` is symmetric, its singular values are the absolute values of its eigenvalues, so there are certainly at least three final eigenvalues of modulus at least one.

## 8. Dense-tail and provenance safeguards

The dense tail enters only through deterministic inequalities such as

`||T[I,J]||op<=||T||op`

and singular-value Weyl. No assertion is made that `X^T T X` is a uniformly small random perturbation for arbitrary unbounded cap-one inputs.

Likewise, canonical-angle and right-singular subspaces are used only to prove coefficient-matrix inequalities. The final density receivers are applied to the actual ORIGINAL-coordinate carrier/cross block. No post-rotation independence is assumed.

## 9. What remains

This run removes a composition obstruction in the additional-eigenvalue problem. Several arbitrary-rank, arbitrary-magnitude signed packets can be processed sequentially; only the cumulative number of resonant directions and the adaptive canonical-angle budget matter. Even a total packet whose range is perfectly aligned with the baseline may decompose into completely transverse stages.

The full conjecture is still OPEN. The next target-level implication is:

> starting from only `s_3(A)>=1`, prove that some bounded ORIGINAL-coordinate carrier admits an adaptive packet decomposition/order with total spent resonance dimension at most `m-5` and positive cumulative reserve, or convert systematic failure into one of the already-paid physical-pair, projected-crossing, grouped-bank, ridge, hub/common-plane, Schur, or Pluecker-volume exits.

The live corrections excluding universal pointwise decay, arbitrary-joint coarea, worst fiber suprema, conditional-cap/moment arguments and post-rotation independence remain in force.
