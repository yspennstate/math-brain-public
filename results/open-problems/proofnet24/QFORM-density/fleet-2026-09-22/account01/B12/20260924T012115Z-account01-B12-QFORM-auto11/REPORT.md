SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T01:21:15Z.
attacking: low-rank spectral-resonance stability — reduce arbitrary signed large eigenvalue packets to a finite-dimensional Woodbury resonance matrix, and route a surviving six-mode physical carrier through the completed account02/B12 theorem.

# account01/B12 — low-rank spectral-resonance stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T012115Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**.  
Continuity: **not proved by this branch**; the partner six-mode theorem used below only guarantees essential boundedness in all of its exits.

Fresh prepublication control was read from `yspennstate/math-research-brain` main at `d492006b984d185c88d8f75d79feb8e63602f6bd`; OWNER CONTROL remains `2026-09-22.15`, programme revision `2026-09-22.5`. The live correction inbox was reread. In particular this proof does not use post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, fiber-sup integration, or any assertion that a small matrix tail gives a uniformly small random quadratic remainder.

## 1. Compact end-to-end implication

Let `H` be a set of `m` ORIGINAL coordinates and let `P:R^m -> R^n` be its coordinate embedding. Suppose a baseline symmetric matrix `A0` has a full-column physical carrier

`M0 := A0 P`,  `G0 := M0^T M0 = (A0^2)[H,H] > 0`.

Add an arbitrary signed spectral packet

`E = U Theta U^T`,

where the columns of `U` are orthonormal and `Theta=diag(theta_1,...,theta_r)` has arbitrary nonzero real entries. No commutation with `A0` is assumed. Put

`V := P^T U`,
`R := M0^dagger U`,
`Pi := M0 M0^dagger`,
`U_perp := (I-Pi)U`,
`L := I_m + R Theta V^T`.

Then the exact carrier identity is

`(A0+E)P = M0 L + U_perp Theta V^T`,                         (1.1)

and the two summands have orthogonal column-space contributions because

`M0^T U_perp = 0`.                                             (1.2)

Consequently

`((A0+E)^2)[H,H]`
` = L^T G0 L + V Theta U_perp^T U_perp Theta V^T`
` >= L^T G0 L`.                                                (1.3)

This already gives a dependence-safe stability theorem: every contraction of the old physical carrier must occur through the finite-dimensional relative gain `L`; the component of the added eigenvectors orthogonal to `Ran(M0)` contributes only a positive Gram term.

## 2. Main theorem: QFORM-LOW-RANK-SPECTRAL-RESONANCE-STABILITY-v1

Let singular values be decreasing. Under the hypotheses above, for every `1<=j<=m`,

`boxed: s_j((A0+E)P) >= s_j(M0) s_m(L).`                     (2.1)

Equivalently,

`boxed: sqrt(lambda_j(((A0+E)^2)[H,H]))`
`       >= s_j(M0) s_m(L).`                                   (2.2)

### Proof

By (1.3), eigenvalue monotonicity for positive semidefinite matrices gives

`lambda_j(((A0+E)^2)[H,H]) >= lambda_j(L^T G0 L)`.

The right side is `s_j(M0 L)^2`. The standard product singular-value inequality for square `L` gives

`s_j(M0 L) >= s_j(M0) s_m(L)`.

This proves (2.1)-(2.2). No probability argument occurs here. QED.

There is also an exact collapse criterion. Since the two terms in (1.1) lie in orthogonal subspaces and `M0` is injective,

`boxed: ker((A0+E)P) = ker(L) intersect ker(U_perp Theta V^T).` (2.3)

Thus a zero of the relative gain is only a candidate destructive resonance; transverse added action can repair it.

## 3. Woodbury reduction: the dangerous large packet is only r-dimensional

Assume `Theta` is invertible and define the `r x r` matrix

`K_Theta := Theta^{-1} + V^T R`.                               (3.1)

Whenever `K_Theta` is invertible, Woodbury gives the exact inverse

`L^{-1} = I_m - R K_Theta^{-1} V^T`.                          (3.2)

Hence

`boxed: s_m(L) >= [1 + ||R||op ||K_Theta^{-1}||op ||V||op]^{-1}.` (3.3)

Also, by Sylvester's determinant identity,

`det L = det(I_r + Theta V^T R) = det(Theta) det(K_Theta).`    (3.4)

Therefore the potentially destructive part of an arbitrarily large rank-`r` signed spectral packet is compressed to the small matrix `K_Theta`. The signs and magnitudes of the added eigenvalues enter through `Theta^{-1}` rather than through `||Theta||`.

### High-eigenvalue nonresonance corollary

Assume

`eta := s_r(V^T R) > 0`.                                      (3.5)

If every added eigenvalue satisfies

`min_a |theta_a| >= 2/eta`,                                   (3.6)

then `||Theta^{-1}||op<=eta/2`, so

`s_r(K_Theta) >= eta/2`, `||K_Theta^{-1}||op <= 2/eta`.

Consequently

`boxed: s_m(L) >= alpha := [1 + 2||R||op||V||op/eta]^{-1}.`    (3.7)

Combining with (2.1),

`boxed: s_j((A0+E)P) >= alpha s_j(M0), 1<=j<=m.`              (3.8)

Thus once a fixed geometric nonresonance gate `eta>0` holds, all sufficiently large added eigenvalues of either sign and independently unbounded magnitude are uniformly harmless to the physical carrier. This is not a same-sign or commuting statement.

## 4. Finitely many common-scale resonances

For a fixed signed packet `U Lambda U^T`, let

`A(t)=A0+t U Lambda U^T`,

where `Lambda` is invertible. Then

`L(t)=I_m+t R Lambda V^T`

and

`det L(t)=det(I_r+t Lambda V^T R)`.                            (4.1)

The right side is a real polynomial of degree at most `r` and equals one at `t=0`. Hence there are at most `r` real candidate scales at which the baseline-range part can lose rank. By (2.3), actual carrier collapse can occur only at those candidate scales and additionally requires vanishing of the transverse term. If `U_perp=0`, this candidate condition is also sufficient. This gives a precise sense in which arbitrary large common-scale spectral additions are stable except near finitely many low-dimensional resonances.

## 5. Arbitrary smaller eigenvalues and carrier-invisible spectrum

Now let the actual final matrix be

`A = A0 + U Theta U^T + E_low + S + T`,                       (5.1)

where:

* the large packet satisfies (3.5)-(3.6);
* `E_low=E_low^T` is arbitrary with `||E_low||op<=h` — this may contain arbitrarily many eigenvalues of either sign and arbitrary orientation;
* `S=S^T` is completely arbitrary subject only to `SP=0`; its complementary spectrum, rank, signs and magnitudes are unrestricted;
* `T=T^T` is arbitrary subject only to the local action bound `||TP||op<=delta`; in particular `||T||op` may be arbitrarily large because its outside-outside block is not charged.

Since `SP=0`, rectangular Weyl gives

`boxed: s_j(AP) >= [alpha s_j(M0)-h-delta]_+, 1<=j<=m.`       (5.2)

Therefore

`boxed: sqrt(lambda_j((A^2)[H,H]))`
`       >= [alpha s_j(M0)-h-delta]_+.`                        (5.3)

This is the requested large/small eigenvalue compiler. It never treats `X^T(E_low+S+T)X` as an independent convolution or as a small random variable. All estimates are on the actual coefficient matrix in original coordinates.

## 6. Exact noncommuting signed stress family

Take `n=12`, split the original coordinates into

`H={1,...,6}`, `J={7,...,12}`,

and set

`A0 = [[0, 2 I_6],[2 I_6,0]].`                                (6.1)

Then

`M0=A0P_H=[0;2I_6]`, `G0=4I_6`, `s_j(M0)=2` for all `j<=6`.

For `j=1,2,3`, define

`u_j=(e_j+2e_{6+j})/sqrt(5)`                                  (6.2)

and add

`E_hi=sum_{j=1}^3 theta_j u_j u_j^T`,                         (6.3)

where the three `theta_j` may have arbitrary independent signs and satisfy only

`|theta_j|>=10`.                                               (6.4)

These are the eigenvalues of the added packet `E_hi`; because the packet does not commute with `A0`, they are not asserted to be eigenvalues of the final matrix. Indeed

`A0 u_j=(4e_j+2e_{6+j})/sqrt(5)`

is not proportional to `u_j`, so this is genuinely noncommuting.

Here

`V=R=(1/sqrt(5))[e_1,e_2,e_3]`, `V^T R=(1/5)I_3`,             (6.5)

so the general theorem already gives a magnitude-independent high-scale bound. But the family allows an exact stronger computation. For `j<=3`,

`(A0+E_hi)e_j = (theta_j/5)e_j + (2+2theta_j/5)e_{6+j}`,      (6.6)

while for `j=4,5,6`,

`(A0+E_hi)e_j=2e_{6+j}`.                                      (6.7)

These six vectors are mutually orthogonal, and for `j<=3`,

`||(A0+E_hi)e_j||^2`
` = theta_j^2/25 + (2+2theta_j/5)^2`
` = ((theta_j+4)^2+4)/5 >= 8`                                 (6.8)

under (6.4). Therefore

`boxed: s_6((A0+E_hi)P_H)=2`,
`boxed: lambda_6(((A0+E_hi)^2)[H,H])=4`,                      (6.9)

uniformly over all sign choices and all arbitrarily large magnitudes.

Now add simultaneously:

* any symmetric `E_low` with `||E_low||op<=1/32` (arbitrarily many small signed eigenvalues);
* any symmetric `S` with `SP_H=0` (arbitrary complementary spectrum, with no norm/rank/sign restriction);
* any symmetric `T` with only `||TP_H||op<=1/64` (its outside-outside spectrum is unrestricted).

For the actual final matrix,

`s_6(AP_H) >= 2-1/32-1/64 = 125/64`.                         (6.10)

Hence

`boxed: lambda_6((A^2)[H,H]) >= (125/64)^2`.                 (6.11)

Since column restriction cannot increase singular values,

`s_3(A)>=s_6(A)>=s_6(AP_H)>=125/64>1`,                        (6.12)

so every matrix in this family is literally inside the owner's exact three-large-eigenvalue target class.

## 7. Actual application of completed partner account02/B12

Use the completed theorem `QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1` from

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

That theorem applies to the actual final matrix when an original-coordinate carrier `H`, `|H|=m>=6`, has

`lambda_6((A^2)[H,H])>=g^2`

and `s_3(A)>=s`. With its canonical specialization

`N=binom(m,2), b=g/2, a=g/(4N), kappa=g/(4N)`,                (7.1)

the four exhaustive bounds are

`8N sqrt(6 pi m)/g`,
`4 pi N/g`,
`3*400^(1/3)*(4N/g)^(5/6)*s^(-1/6)`,
`10sqrt(2e)/(sqrt(3)g)`.                                      (7.2)

For the final matrices above take

`m=6`, `N=15`, `g=s=125/64`.

The four numbers are respectively

`653.3973875978095`,
`96.50972631827844`,
`343.19207834882434`,
`6.892417435798889`.

Therefore the partner theorem gives the actual full-law inequality

`boxed: ||p_{X^T A X}||_{infinity,ess} < 654`.                (7.3)

This is uniform over every independent cap-one product law, every choice of the three unbounded signed high-packet eigenvalues satisfying `|theta_j|>=10`, every arbitrary-rank small signed packet of norm at most `1/32`, every carrier-invisible arbitrary complementary spectrum, and every tail with local carrier action at most `1/64`.

No rotated eigen-coordinate independence and no dependent convolution is used.

## 8. What this does and does not solve

The theorem gives a genuine additional-eigenvalue stability mechanism that is different from hard low-rank footprint counting, Schur-pivot stability, or commuting spectral replacement. A large noncommuting packet is reduced to an `r x r` resonance matrix `Theta^{-1}+V^T M0^dagger U`; away from its low-dimensional resonances, the added eigenvalue magnitudes disappear from the carrier bound. Arbitrarily many small eigenvalues are paid by one operator threshold, and arbitrary spectrum invisible to the chosen carrier is free.

The full QFORM conjecture is still OPEN. The missing structural implication is not perturbative: from the bare hypothesis `s_3(A)>=1`, one still must force either (i) a bounded original-coordinate carrier admitting a useful baseline/high-packet split with a quantitative resonance gap, or (ii) one of the already-paid diffuse-volume, grouped-bank/hub, ridge, physical-pair, half-Riesz, Schur, or related receivers. This report does not prove that dichotomy.

Continuity of the output density is also not established by the partner theorem in all exits, so only essential boundedness is claimed in (7.3).

## 9. Sanity checks

A finite random checker was run on 5000 random symmetric baselines, random orthonormal signed rank-three packets, and the fixed first-six-coordinate carrier. It checked:

1. the Gram identity (1.3), with maximum operator discrepancy about `2.82e-12`;
2. every inequality `s_j((A0+E)P)>=s_j(M0)s_m(L)`, with zero violations;
3. the Woodbury lower bound (3.3) whenever the small resonance matrix was numerically invertible, with zero violations.

These computations are sanity checks only; the proof is the exact algebra above.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Repository transport was used, but no authenticated native brain retrieval/receiver-use event was observed. No schedules, task states, email/push notifications, permissions, public releases, paid model/API calls, remote workflows, or cross-account authentication were changed.
