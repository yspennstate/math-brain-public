SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T10:23:38.428952Z.
attacking: a localized five-mode two-sided relative-resonance theorem that combines partner r54 bipolar control with transverse square energy and survives arbitrary small dense coefficient tails.

# account02/B12 — cross-sign skew-rank shielding of five physical modes

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T102338Z-account02-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted conjecture is not closed here. The new result narrows the local stability debt once an ORIGINAL-coordinate carrier has been identified. Starting only from `s_3(A)>=1`, one still has to force either

- an original-coordinate carrier on which the normalized resonance window and the cross-sign skew rank obey the quantitative inequality below, or
- one of the already-paid physical-core / physical-pair / projected-crossing / grouped-bank / hub / ridge / Schur / common-plane / Pluecker-volume exits.

In particular, I do not infer a universal carrier scale from `s_3(A)>=1`; the live `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction forbids that shortcut.

The point of the present theorem is different: for a fixed quantitative carrier, **arbitrarily large noncommuting signed spectrum is harmless except for skew mixing between the positive and negative sides of the relative cancellation point**. Skew motion within either sign sector costs nothing. Low-rank cross-sign mixing costs only two carrier modes per rank, and only the tail of that cross-sign block costs norm.

## 2. Source-pinned inputs

The newest compatible partner result is account03/B12 r54,
`yspennstate/math-open-problems@fb41bed86e2f0730da84c5559618029bc667db3d`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T094857Z-qform-eigenvalue-r54/REPORT.md`.
It proves the exact whitened carrier identity and two-sided resonance-window bounds. In the notation below it gives, among other statements,

```text
s_j(M+N) >= g s_j(I+B),
```

and, if `q` eigenvalues of the symmetric relative action lie in the `rho`-window around `-1`, an arbitrary-skew estimate retaining only about half the nonresonant modes, while the full-mode estimate charges the global skew norm.

The required pinned source is
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
Its completed `D_5` theorem states that for an ACTUAL disjoint ORIGINAL-coordinate cross block `C=A[I,J]`,

```text
||p_(X^T A X)||_infinity
 <= 5 sqrt(2e) e_5(C^T C)^(-1/10),
```

with no fifth-volume marginal condition. Same-bank quadratic terms, outside couplings and affine terms remain present. In particular, if `s_5(C)>=h>0`, then

```text
e_5(C^T C) >= h^10,
||p_(X^T A X)||_infinity <= 5 sqrt(2e)/h.
```

The proof is Fourier-integrable, so this scoped `D_5` branch also supplies a continuous `C_0` density. Full-target continuity remains separate and open.

## 3. Exact whitened decomposition

Let `M in R^(p x m)` have full column rank. Put

```text
G=M^T M,
g=s_m(M)>0,
U=M G^(-1/2),
Pi=UU^T.
```

For arbitrary `N in R^(p x m)`, define

```text
B=G^(-1/2) M^T N G^(-1/2),
Z=(I-Pi) N G^(-1/2).
```

Then `U^T U=I`, `U^T Z=0`, and

```text
(M+N)G^(-1/2)=U(I+B)+Z.
```

Therefore

```text
[(M+N)G^(-1/2)]^T[(M+N)G^(-1/2)]
 = (I+B)^T(I+B)+Z^T Z,
```

so for every singular index `j`,

```text
s_j(M+N) >= g s_j(I+B).                 (3.1)
```

Write

```text
H=(B+B^T)/2,
K=(B-B^T)/2,
D=I+H.
```

Thus `D` is symmetric and `K` is skew-symmetric. The dangerous scalar resonance is `D=0`, equivalently an eigenvalue `-1` of `H`.

## 4. Cross-sign skew-rank shield

Fix `rho>0` and let

```text
E_+ = 1_[rho,infinity)(D) R^m,
E_0 = 1_(-rho,rho)(D) R^m,
E_- = 1_(-infinity,-rho](D) R^m.
```

Let `P_+,P_0,P_-` be the orthogonal projections and put

```text
q=dim E_0,
K_+- = P_+ K P_- : E_- -> E_+.
```

For an integer `r>=0`, define

```text
kappa_r = s_(r+1)(K_+-)
```

when `r<rank-domain minimum`, and `kappa_r=0` after all singular directions have been spent. Equivalently, by Eckart-Young choose

```text
K_+- = R + E,
rank R <= r,
||E||_op = kappa_r.
```

### Theorem — `QFORM-CROSS-SIGN-SKEW-RANK-SHIELD-v1`

If

```text
d=m-q-2r >= 1,
```

then

```text
boxed:
s_d(M+N) >= g (rho-kappa_r)_+.          (4.1)
```

If a further arbitrary matrix tail `T` satisfies

```text
||T||_op <= delta,
```

then

```text
boxed:
s_d(M+N+T)
 >= [g(rho-kappa_r)_+ - delta]_+.        (4.2)
```

No bound is imposed on the norms of the within-sign skew blocks `P_+ K P_+` and `P_- K P_-`, on the couplings with `E_0`, or on the total norm/rank/signed spectrum of `N`.

### Proof

Restrict the domain to

```text
E=E_+ direct_sum E_-,
dim E=m-q,
```

and project the output back to `E`. For `x in E`, any coupling into `E_0` is orthogonal to the projected output and can only increase the full norm, so it suffices to lower-bound

```text
L=P_E(I+B)|_E.
```

Relative to `E_+ direct_sum E_-`, write

```text
L = A_0 + L_R + L_E,
```

where

```text
A_0 = diag(D_+ + K_++, D_- + K_--),
L_R = [[0,R],[-R^T,0]],
L_E = [[0,E],[-E^T,0]].
```

Here `D_+ >= rho I` and `D_- <= -rho I`, while `K_++` and `K_--` are skew-symmetric. For every `x_+ in E_+`,

```text
|x_+^T(D_+ + K_++)x_+|
 = x_+^T D_+ x_+
 >= rho ||x_+||^2,
```

hence by Cauchy-Schwarz

```text
||(D_+ + K_++)x_+|| >= rho ||x_+||.
```

Likewise, for `x_- in E_-`,

```text
|x_-^T(D_- + K_--)x_-|
 = -x_-^T D_- x_-
 >= rho ||x_-||^2,
```

and therefore

```text
||(D_- + K_--)x_-|| >= rho ||x_-||.
```

Thus

```text
s_(m-q)(A_0) >= rho.                             (4.3)
```

The tail cross-sign block has

```text
||L_E||_op=||E||_op=kappa_r,
```

so singular-value Weyl gives

```text
s_(m-q)(A_0+L_E) >= (rho-kappa_r)_+.            (4.4)
```

The spent part satisfies

```text
rank(L_R) <= 2 rank(R) <= 2r.
```

Rank interlacing therefore gives

```text
s_(m-q-2r)(L)
 >= s_(m-q)(A_0+L_E)
 >= (rho-kappa_r)_+.                             (4.5)
```

By the singular-value max-min principle, the same lower bound holds for `s_d(I+B)`: the projected output already expands a `d`-dimensional subspace by the amount in (4.5), and the omitted `E_0` output is orthogonal and cannot decrease the norm. Finally (3.1) proves (4.1), and ordinary singular-value Weyl proves (4.2). QED.

## 5. What the theorem improves

The partner r54 arbitrary-skew theorem, with `q` resonant modes, guarantees only

```text
s_(ceil((m-q)/2))(M+N) >= g rho.
```

Its full-mode theorem instead charges the global skew norm `||K||`.

The new theorem interpolates between these endpoints. It pays neither the full skew norm nor an automatic factor-two loss. Only the **cross-sign** skew block matters. A rank-`r` coherent transfer between `E_+` and `E_-` spends at most `2r` modes; the remaining cross-sign tail costs `kappa_r`. Huge skew motion inside either sign sector is free.

A useful obstruction form is obtained by fixing `0<=tau<rho` and letting

```text
r_tau = #{ singular values of K_+- strictly larger than tau }.
```

Then `kappa_(r_tau)<=tau`, so if a later tail has norm at most `delta` and

```text
g(rho-tau)>delta,
m-q-2 r_tau >= 5,
```

five modes survive. Therefore any carrier that evades the five-volume receiver must obey

```text
boxed:
q + 2 r_tau >= m-4                              (5.1)
```

for every usable pair `(rho,tau)` with `g(rho-tau)>delta`.

This is a real structural obstruction: a survivor must have either many genuinely resonant modes near the cancellation value, or high-rank skew transport specifically between opposite-sign nonresonant sectors. Merely having a huge signed packet, huge total skew norm, or many added eigenvalues is not enough.

## 6. Original-coordinate QFORM compiler

Let `I,J` be disjoint ORIGINAL-coordinate banks, `|J|=m`, and let

```text
M=A_*[I,J],
N=S[I,J],
```

where `A_*` is a baseline symmetric coefficient matrix and `S=S^T` is an arbitrary signed addition. Form `G,B,H,K,D,E_+,E_0,E_-` from this physical cross block exactly as above.

Now add any globally dense symmetric tail

```text
T_dense=T_dense^T,
||T_dense||_op <= delta.
```

Its physical cross compression satisfies

```text
||T_dense[I,J]||_op <= delta.
```

Hence the ACTUAL final cross block

```text
C=A[I,J]
```

obeys

```text
s_(m-q-2r)(C)
 >= [g(rho-kappa_r)_+ - delta]_+.               (6.1)
```

If `m-q-2r>=5` and

```text
h=g(rho-kappa_r)-delta>0,
```

then `s_5(C)>=h`, and the pinned completed `D_5` theorem gives the actual density inequality

```text
boxed:
||p_(X^TAX)||_infinity <= 5 sqrt(2e)/h.          (6.2)
```

All random conditioning remains in ORIGINAL product coordinates. `G^(-1/2)` and the spectral projections of `D` are deterministic matrix-analysis devices only; no rotated random coordinates are ever asserted independent.

## 7. Strict stress family: huge within-sign skew is harmless

Take two disjoint ORIGINAL-coordinate banks `I,J`, each of size five, and baseline symmetric core

```text
A_0 = [[0,2 I_5],[2 I_5,0]].
```

The baseline cross carrier is

```text
M=2 I_5,
G=4 I_5,
g=2.
```

Let

```text
R_2=[[0,1],[-1,0]],
D=diag(I_3,-I_2),
K_L=diag(L R_2, 0, L R_2),    L>=2,
B_L=D-I_5+K_L.
```

The first `3` coordinates are the positive sector and the last `2` the negative sector. Thus

```text
E_0=0,
q=0,
K_+-=0.
```

Define the cross action

```text
N_L=2 B_L
```

and realize it by the symmetric signed packet

```text
S_L=[[0,N_L],[N_L^T,0]].
```

Because `G^(-1/2)=(1/2)I`, the normalized relative action is exactly `B_L`. The total skew norm is

```text
||K_L||=L -> infinity,
```

but its cross-sign block vanishes identically. Taking `rho=1`, `r=0`, the new theorem gives

```text
boxed:
s_5(M+N_L) >= 2.                                (7.1)
```

This is exact. Indeed

```text
M+N_L = 2(D+K_L),
```

and the singular values of `D+K_L` are

```text
sqrt(1+L^2), sqrt(1+L^2), sqrt(1+L^2), sqrt(1+L^2), 1.
```

Hence

```text
s_5(M+N_L)=2
```

for every `L`.

The improvement over partner r54 is strict on this family. Its arbitrary-skew bipolar theorem yields only

```text
s_3(M+N_L)>=2,
```

which is insufficient for `D_5`, while its full-mode commutator theorem gives the vacuous factor

```text
(1-||K_L||)_+=0
```

for `L>=1`. The new cross-sign theorem retains all five modes because the huge skew action stays inside the two sign sectors.

The packet is genuinely spectrally unbounded: the nonzero singular values of `N_L` include `2L` and `2sqrt(L^2+4)`, so the symmetric off-diagonal packet `S_L` has positive and negative eigenvalues with magnitudes tending to infinity.

## 8. Arbitrary spectator spectrum and arbitrary small dense tail

Append an arbitrary-dimensional direct-sum symmetric spectator block `Theta`, with unrestricted eigenvalue signs, multiplicities, magnitudes and internal mixing. Then add any globally dense symmetric tail satisfying

```text
||T_dense||_op <= 1/64.
```

For the literal final physical cross block `C=A[I,J]`, (7.1) and Weyl give

```text
boxed:
s_5(C) >= 2-1/64 = 127/64.                      (8.1)
```

Therefore

```text
e_5(C^T C) >= (127/64)^10,
```

and the required pinned `D_5` theorem gives the real final-matrix inequality

```text
boxed:
||p_(X^TAX)||_infinity
 <= 5 sqrt(2e)/(127/64)
 = 5.875008457567557... .                        (8.2)
```

This is uniform in `L`, in the full spectator spectrum `Theta`, and in every allowed dense tail. The `D_5` branch also yields a continuous `C_0` density.

The family lies literally in the owner's exact target class. Before the dense tail, the ten-coordinate off-diagonal core has eigenvalues

```text
+/- s_1(M+N_L), ..., +/- s_5(M+N_L),
```

all of modulus at least `2`. An arbitrary direct-sum spectator block does not remove those ten singular directions. After the dense tail,

```text
s_10(A_final) >= 2-1/64 = 127/64 > 1.
```

Since the final matrix is symmetric, at least three final eigenvalues have modulus at least one.

## 9. Dense-tail and independence safeguards

The dense tail is used only through deterministic coefficient inequalities such as

```text
||T_dense[I,J]||_op <= ||T_dense||_op
```

and singular-value Weyl. There is no assertion that `X^T T_dense X` is uniformly small for unbounded cap-one product laws.

Likewise, the whitening and sign-sector decompositions occur only inside deterministic matrix proofs. The probabilistic `D_5` receiver is applied to the literal final ORIGINAL-coordinate cross block. No post-rotation independence is used.

## 10. Remaining implication

The new local obstruction (5.1) isolates the hard added-spectrum geometry. To escape this route on a quantitative physical carrier, the hostile action must create enough actual resonance near `-1`, or enough high-rank skew transport between opposite-sign nonresonant sectors, to satisfy

```text
q+2 r_tau >= m-4.
```

The next unpaid target-level step is to derive an ORIGINAL-coordinate physical certificate from that failure condition—e.g. a physical pair, grouped crossing, hub/common-plane structure, or Schur exit—or else to extract a carrier violating (5.1). Bare `s_3(A)>=1` is not asserted to force such a carrier. Full QFORM remains OPEN.
