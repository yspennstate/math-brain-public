SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T04:44:34.607657Z.
attacking: destructive-codomain projection stability — arbitrary signed additions may be huge on the physical carrier provided their action is orthogonal to the current carrier image; only the dynamically destructive projection is charged.

# fleet03/B12 — dynamic destructive-projection stability for arbitrary added spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T044434Z-qform-eigenvalue-r49`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The owner target remains open: for independent ORIGINAL coordinates `X_i` with scalar densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free density bound for `X^TAX`, or give a valid counterexample.

No moment, support, Gaussian, log-concavity, iid, diagonal-basis, post-rotation independence, or small-random-error assumption is used below. Every perturbation is handled only as a deterministic coefficient-matrix addition.

The designated partner result actually applied is fleet04/B12 r9:

`yspennstate/math-open-problems@71b7db02d3bd2f5cb6bf07e800caa6bd13a1a3e5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T021341Z-fleet04-B12-resonance-repair-r9/REPORT.md`.

It gives, for the exact resonant six-coordinate carrier described in Section 5 below,

` s_6(M_*) = 2,  M_*=(A_0+E_res)P_H. `

For the density step I use the completed five-square-mode compiler from fleet03/B12 r47:

`yspennstate/math-open-problems@8f9128b3f3ce222f941a3b138460658059957a83`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`.

Its source-valid conclusion is: if an ORIGINAL-coordinate bank `H`, `|H|=m>=5`, satisfies

`lambda_5((A^2)[H,H]) >= g^2>0`,

then the law has a continuous `C_0` density and

`||p_(X^TAX)||_infinity <= sqrt(24*pi*m+K3^2)/g`,  
`K3=3*2^(4/3)*exp(1/3)`.

## 2. One-step theorem: only the destructive codomain projection can lower the carrier

Let `P:R^m -> R^n` be the coordinate embedding for a literal ORIGINAL-coordinate bank `H`. Let `A_*` be any real symmetric baseline and put

`M=A_*P`.

Assume `M` has full column rank and write

`g=s_m(M)>0`.

Let `E` be an arbitrary real symmetric addition. Let `Pi` be the orthogonal projection in `R^n` onto `Ran(M)`, and decompose the local carrier action

`EP = D+T`,
`D=Pi EP`,
`T=(I-Pi)EP`.

Then `Ran(T)` is orthogonal to `Ran(M)` and also to `Ran(D)`.

### Theorem 2.1 — `QFORM-DESTRUCTIVE-CODOMAIN-PROJECTION-STABILITY-v1`

Define

`delta=||D||_op = ||Pi EP||_op`,  
`tau=s_m(T)`.

Then

`boxed:
s_m((A_*+E)P)^2
>= [g-delta]_+^2 + tau^2.`                                      (2.1)

In particular,

`boxed:
s_m((A_*+E)P) >= [g-||Pi EP||_op]_+.`                           (2.2)

Thus the norm, rank, sign, inertia and spectrum of the orthogonal local action `(I-Pi)EP` are completely free: they cannot reduce the protected carrier singular value.

### Proof

For every `x in R^m`,

`(A_*+E)Px = (Mx+Dx)+Tx`.

The first term lies in `Ran(M)` and the second lies in `Ran(M)^perp`. Therefore

`||(A_*+E)Px||^2 = ||Mx+Dx||^2 + ||Tx||^2`.                    (2.3)

For a unit `x`,

`||Mx+Dx|| >= ||Mx||-||Dx|| >= g-delta`,                       (2.4)

whenever `g>=delta`; otherwise use the trivial lower bound zero. Also

`||Tx|| >= tau`.                                                 (2.5)

Substituting (2.4)-(2.5) into (2.3) and taking the infimum over unit `x` proves (2.1). Dropping the nonnegative `tau^2` term gives (2.2). QED.

### Interpretation

This is stronger than charging `||EP||_op`. A perturbation may act with arbitrarily large norm on every physical coordinate in `H` and still cost **zero** if its local image is orthogonal to the current carrier image. This is a deterministic Pythagorean fact, not a probabilistic convolution statement.

For a signed spectral packet

`E=U Theta U^T`, `V=P^T U`,

the charged operator is exactly

`Pi U Theta V^T`.                                                (2.6)

Hence arbitrarily large positive or negative packet eigenvalues whose aggregate carrier action lands in `Ran(M)^perp` are free, even when their physical row footprint has high rank.

## 3. Dynamic theorem for an arbitrary sequence of signed additions

Let

`A_r=A_(r-1)+E_r`, `M_r=A_rP`, `r=1,...,R`,

with every `E_r` real symmetric and `M_0` full column rank. For each step, let `Pi_(r-1)` be the orthogonal projection onto `Ran(M_(r-1))`, and define

`delta_r = ||Pi_(r-1) E_r P||_op`,  
`tau_r   = s_m((I-Pi_(r-1))E_rP)`.

Set

`g_0=s_m(M_0)`,
`g_r = sqrt([g_(r-1)-delta_r]_+^2 + tau_r^2)`.                  (3.1)

### Theorem 3.1 — `QFORM-DYNAMIC-DESTRUCTIVE-BUDGET-v1`

For every `r`,

`boxed: s_m(M_r) >= g_r.`                                       (3.2)

Consequently,

`boxed:
s_m(M_R) >= [s_m(M_0)-sum_(r=1)^R delta_r]_+.`                 (3.3)

No bound at all is required on

`||(I-Pi_(r-1))E_rP||_op`.

The added matrices may have arbitrary signs, ranks, operator norms and mutual noncommutation. At each stage only the part of the new local action that points into the **current** carrier image is destructive.

### Proof

Apply Theorem 2.1 at step `r` with baseline `A_(r-1)`. This gives (3.2) inductively. Since `g_r >= [g_(r-1)-delta_r]_+`, repeated application yields (3.3). QED.

### Density-level corollary

If `m>=5` and the dynamic recurrence leaves `g_R>0`, then

`lambda_5((A_R^2)[H,H]) >= s_m(M_R)^2 >= g_R^2`,                (3.4)

so the completed five-mode compiler gives

`boxed:
||p_(X^T A_R X)||_infinity
<= sqrt(24*pi*m+K3^2)/g_R`,                                     (3.5)

and the density has a representative in `C_0(R)`.

Equation (3.5) is an actual final-matrix statement. No `X^T E_r X` is removed or treated as independent noise.

## 4. A spectral mode can be huge on the physical carrier and still be free

The difference between local-action norm and destructive-action norm is real.

Suppose a packet mode `u` has coefficient `theta`. Its contribution to `EP` is

`theta u (P^T u)^T`.

Its destructive contribution is

`theta (Pi u)(P^T u)^T`.                                       (4.1)

Therefore the mode costs zero whenever `Pi u=0`, even if both `|theta|` and `||P^Tu||` are large.

This differs from a mere "carrier-invisible" condition `EP=0`: here the mode can act strongly on the selected ORIGINAL coordinates, but in a codomain direction orthogonal to the already-protected carrier.

## 5. Required fleet04/B12 application at an actual inequality

Use the exact resonant family from fleet04/B12 r9. Let

`n=12`, `H={1,...,6}`,

and

`A_0=[[0,2I_6],[2I_6,0]]`.

Let

`u=(e_1+e_7)/sqrt(2)`, `E_res=-4uu^T`.

The partner proves exactly that, with `P=P_H`,

`M_*=(A_0+E_res)P`

has columns

`M_* e_1 = -2 e_1`,  
`M_* e_j = 2 e_(6+j)`, `j=2,...,6`,                            (5.1)

hence

`boxed: s_6(M_*)=2.`                                            (5.2)

Its carrier image is

`R_*=span{e_1,e_8,e_9,e_10,e_11,e_12}`.                         (5.3)

Now add the completely arbitrary signed diagonal packet

`S_t=sum_(j=2)^6 t_j e_j e_j^T`,                                (5.4)

where the five real numbers `t_j` are unrestricted in sign and magnitude. These are five literal additional eigenvalues on ORIGINAL coordinates.

Since

`S_t P_H e_j = t_j e_j` for `j=2,...,6`

and `e_2,...,e_6` are orthogonal to `R_*`,

`Pi_* S_tP_H=0`.                                                 (5.5)

Theorem 2.1 therefore gives, with **no bound at all** on the `t_j`,

`boxed:
s_6((A_0+E_res+S_t)P_H) >= 2.`                                  (5.6)

Indeed the columns are still mutually orthogonal and the exact singular values are

`2, sqrt(4+t_2^2),...,sqrt(4+t_6^2)`.                           (5.7)

Now allow a further arbitrary finite sequence of symmetric additions `F_r`, of arbitrary signs, ranks and global norms, subject only to the dynamic destructive budget

`sum_r ||Pi_(r-1) F_r P_H||_op <= 1/4`,                         (5.8)

where `Pi_(r-1)` is updated after all earlier additions. Their orthogonal local actions may be unbounded.

By Theorem 3.1,

`boxed: s_6(AP_H) >= 2-1/4 = 7/4.`                              (5.9)

Thus

`lambda_5((A^2)[H,H]) >= (7/4)^2`.                              (5.10)

The five-mode compiler with `m=6`, `g=7/4` gives

`boxed:
||p_(X^TAX)||_infinity
<= sqrt(144*pi+K3^2)/(7/4)
=13.5670116660... <13.568.`                                      (5.11)

The density is continuous and vanishes at infinity.

This is the requested partner composition at an actual inequality. It strengthens the partner's local-tail condition: the final added spectrum can have arbitrarily large local action on `H`; only the dynamically destructive projection into the current carrier image is charged.

## 6. Deterministic check

A seeded checker generated 10,000 random full-column carriers `M` and arbitrary rectangular local additions `N`. For each instance it formed `Pi=P_Ran(M)` and checked

`s_m(M+N)^2
>= [s_m(M)-||Pi N||]_+^2 + s_m((I-Pi)N)^2`.                    (6.1)

There were zero violations. The minimum numerical margin was

`0.019603268233315818`.

The explicit partner-family test used signed packet eigenvalues

`10^6, -3*10^5, 7*10^4, -2*10^6, 9*10^5`

on `e_2,...,e_6`; it obtained

`||Pi_* S_t P_H||=0`

and

`s_6(M_*+S_tP_H)=2`.

These are only consistency checks; the proof is the exact orthogonal decomposition (2.3).

## 7. Remaining gap

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem says that once a quantitative original-coordinate carrier exists, arbitrary later spectrum is dangerous only through a dynamically defined destructive codomain component. What is still missing from the bare hypothesis `s_3(A)>=1` is a structural theorem forcing either:

1. a bounded physical carrier whose cumulative destructive budget is universally controlled;
2. a large transverse component that itself supplies enough protected square energy; or
3. one of the already-paid projected-crossing, grouped-bank, hub, ridge, physical-core, pair, Schur, common-plane or Pluecker-volume exits.

Continuity is proved for the five-mode corollary (3.5)/(5.11), not for the unrestricted conjecture.

## 8. Source / integrity notes


Repository transport was available. Authenticated native learned-memory retrieval / receiver use was not observed, so this run remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler state, notifications, email, public visibility, permissions, cross-account authentication, paid API/Codex call, remote workflow or installation was changed.
