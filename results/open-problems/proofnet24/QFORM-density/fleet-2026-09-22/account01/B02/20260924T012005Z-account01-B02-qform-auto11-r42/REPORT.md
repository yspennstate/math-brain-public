SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T01:20:05Z.
attacking: the live disjoint physical-cross packet `E2(M)>4/9` by spending the completed account02/B02 physical-`E3` Fourier receiver first, then proving that every low-`E3` survivor is either already inside the existing giant near-rank-one packet or is quantitatively ultra-near rank two.

# account01/B02 r42 — integrated Fourier / low-E3 structural funnel

Status: **ESSENTIAL_STEP_APPLIED_WITH_CORRECTION / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED / WITHOUT_VERIFIED_BRAIN**.

`CORRECTION.md` is authoritative over one explicitly withdrawn, scope-invalid sentence in `EARLY.md`. The correction does not weaken the result below; it replaces that sentence by a stronger valid argument using only the literal physical cross block.

## 1. Source-valid live packet

From account03/B19 r45, one of the remaining original-coordinate packets is a literal disjoint physical cross block

`M=A[R,C]`

with

`E2(M)>4/9`.

Here `Ek(M)=e_k(M^T M)`, equivalently the sum of squares of all physical `k x k` minors. No singular-vector coordinate is ever declared independent.

Let

`x1>=x2>=x3>=...>=0`

be the squared singular values of `M`; put `e2=E2(M)`, `e3=E3(M)`, and

`T=sum_{k>=3} xk`.

## 2. First essential implication: a low-E3 dichotomy

### Lemma 2.1

For every nonnegative nonincreasing sequence `x1>=x2>=...`,

`x2 (e2-x1*x2) <= 2 e3`.                                      (2.1)

### Proof

Write

`R2=sum_{3<=k<l} xk xl`, `R3=sum_{3<=k<l<m} xk xl xm`.

Then

`e2-x1*x2=(x1+x2)T+R2`,

`e3=x1*x2*T+(x1+x2)R2+R3`.

Therefore

`2e3-x2(e2-x1*x2)
 =x2(x1-x2)T+(2x1+x2)R2+2R3 >=0`.

This proves (2.1).  □

Take the concrete source-valid gate

`eps=2^-18`, `tau=2^-11=1/2048`.

Assume from now on that `e3<eps`; the complementary branch will be paid in Section 3.

### Branch A: `x2>=tau`

By (2.1),

`e2-x1*x2 <= 2e3/x2 <2eps/tau=1/64`.

Since `e2>4/9`,

`x1*x2 > 4/9-1/64 =247/576`.                                  (2.2)

Every term `x1*x2*xk`, `k>=3`, occurs in `e3`, so

`e3>=x1*x2*T`.

Combining with (2.2),

`T < eps/(247/576)=9/1011712
   =8.895812246963562e-6`.                                     (2.3)

Consequently the best rank-two approximation `M2` to this literal physical block obeys

`||M-M2||_F=sqrt(T)
 <sqrt(9/1011712)
 =0.0029825848264489582`.                                      (2.4)

The nonzero tail is retained. Equation (2.4) is a deterministic coefficient reduction, not a probabilistic deletion.

### Branch B: `x2<tau`

Put

`S=sum_{k>=2}xk`,
`F2=sum_{2<=i<j}xi*xj`,
`F3=sum_{2<=i<j<k}xi*xj*xk`.

Then

`e2=x1*S+F2`, `e3=x1*F2+F3`.

Suppose for contradiction that `S>=3tau`. Since every `xk`, `k>=2`, is at most `tau`,

`F2=(S^2-sum_{k>=2}xk^2)/2 >= S(S-tau)/2`.                    (2.5)

There is also the exact identity

`3F3=sum_{2<=i<j}xi*xj*(S-xi-xj)`,

and hence

`3F3 >= (S-2tau)F2`.                                           (2.6)

Because `e3<eps`, (2.5) implies

`x1*S < 2eps/(S-tau)`,                                         (2.7)

and (2.6) implies

`F2 < 3eps/(S-2tau)`.                                          (2.8)

For `S>=3tau`, (2.7)-(2.8) give

`e2=x1*S+F2
 < 2eps/(S-tau)+3eps/(S-2tau)
 <= eps/tau+3eps/tau
 =4eps/tau
 =1/32`,

contrary to `e2>4/9`. Therefore

`S<3/2048`.                                                     (2.9)

Thus the best rank-one approximation `M1` satisfies

`||M-M1||_F=sqrt(S)
 <sqrt(3/2048)=sqrt(6)/64
 =0.038273277230987154`.                                       (2.10)

Moreover `F2<=S^2/2`, so

`4/9<e2<=x1*S+S^2/2`.

The function `4/(9S)-S/2` is decreasing. Using (2.9),

`x1>8192/27-3/4096
    =303.4066749855324`,                                       (2.11)

and hence

`s1(M)=sqrt(x1)>17.418572702306363`.                            (2.12)

In particular `||M||_F>s1(M)>256/15`, and (2.10) is strictly smaller than

`5sqrt(2)/128=0.05524271728019903`.

Therefore Branch B lies **strictly inside the already-live account03/B19 r45 giant near-rank-one packet**, whose gates are

`||M||_F>=256/15`,
`s1(M)>17.0665`,
`dist_F(M,{rank<=1})<=5sqrt(2)/128`.

So no new low-rank-one debt is created.

## 3. Required account02/B02 partner application to an actual inequality

Use the completed account02/B02 marginal-free physical-third-volume theorem, pinned through

`yspennstate/math-open-problems@aeaba9e3351623ead11450857c2d014b43664aef`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`.

For every literal physical cross block `B` with `E3(B)>0`, it gives genuine unweighted Fourier `L1` and

`||p_Q||_infinity <= 10.345084 E3(B)^(-1/6)`,

`int_R |phi_Q(t)| dt <= 2*pi*10.345084 E3(B)^(-1/6)`.

At the actual gate `E3(M)>=2^-18`,

`E3(M)^(-1/6)<=8`,

so

`||p_Q||_infinity <=82.760672`,                                (3.1)

`int_R |phi_Q(t)|dt <=520.000639`.                              (3.2)

This branch has a continuous density vanishing at infinity. The theorem is applied to the actual original-coordinate block `M=A[R,C]`; no post-rotation independence is used.

## 4. Final source-valid funnel

Every live r45 disjoint-cross state `E2(M)>4/9` now satisfies one of exactly these usable exits:

1. **physical E3 Fourier payment:** `E3(M)>=2^-18`, in which case (3.1)-(3.2) pay the full ambient law with a continuous `C0` density;
2. **existing giant near-rank-one packet:** `E3(M)<2^-18` and `x2<1/2048`; the stronger estimates (2.10)-(2.12) place it inside the r45 packet already tracked elsewhere;
3. **ultra-near-rank-two packet:** `E3(M)<2^-18` and `x2>=1/2048`, in which case

   `x1*x2>247/576`,

   `dist_F(M,{rank<=2})<0.002982585`.

Thus the previously broad `E2>4/9` interface is reduced to an already-existing rank-one packet plus a robust two-mode crossing with an extremely small but retained transverse tail.

## 5. Correction ledger

An early draft sentence asserted a same-bank curvature consequence by treating `R union C` as the full ambient coordinate set. The r45 source does not give that exhaustion, so that sentence was invalid and is **withdrawn**. `CORRECTION.md` contains the corrected proof and is authoritative over the incompatible sentence in `EARLY.md`. No theorem or conclusion in this `REPORT.md` uses the withdrawn claim.

## 6. What remains unpaid

The new first B02 interface is

`QFORM-ULTRARANK2-CROSS-THIRD-CURVATURE-L1-v1`:

start from a literal original-coordinate crossing `M=A[R,C]` with

`x1*x2>247/576`,
`sum_{k>=3}xk<9/1011712`,

and couple its two robust crossing directions to the third curvature forced somewhere in the full symmetric matrix by `s3(A)>=1`, while retaining every nonzero transverse tail and every same-bank/outside quadratic coupling. A successful argument may use an averaged physical augmentation, grouped hub, Schur, pair-log, or direct small-ball receiver, but may not rotate the random coordinates and call the singular coordinates independent.

No exact-target counterexample to a universal

`int_R |phi_Q(t)|dt <= C`

was found. The target-wide integrated-Fourier criterion remains `OPEN_NOT_REFUTED`; full bounded density and full-target continuity remain OPEN.

## 7. Scope / execution

Repository transport and actual equation-level use of completed partner mathematics occurred. Native authenticated brain learned-memory receiver ingestion was not verified, so status remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.

No task, schedule, enabled/paused state, notification, email, permission, public-release, installation, paid-call, or cross-account-authentication setting was changed.
