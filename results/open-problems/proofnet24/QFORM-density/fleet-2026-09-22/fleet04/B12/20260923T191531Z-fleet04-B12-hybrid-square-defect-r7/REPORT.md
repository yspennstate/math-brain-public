SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B12, 2026-09-23T19:15:31Z.
attacking: a two-layer physical square-Gram reserve that simultaneously permits commuting signed eigenvalue replacements and a full-rank noncommuting packet, then compiling the surviving actual carrier through the six-mode theorem.

# fleet04/B12 — hybrid commuting and noncommuting square-defect reserve

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T191531Z-fleet04-B12-hybrid-square-defect-r7
Status: PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN
Continuity: not claimed in the six-mode branch used below.

## 1. Scope and source pins

The unrestricted conjecture remains open. The result below does not derive a bounded physical carrier from the bare condition \(s_3(A)\ge1\); it proves that once a physical square carrier exists, two qualitatively different classes of hostile spectral changes may coexist without destroying it.

Fresh controls were read from math-research-brain main: AGENTS.md blob af9b5936c3eed3bb1cced26eddef5fd3eea941ce, scheduled_tasks/README.md blob 14046b5138615be52bb1c49a998122a7c84e200e, correction inbox blob 6bdbd9987a4eefeba79d53915cfe7e232263f8ec, memory protocol blob 0d902d56688f4b5c575f5b921ddf9f6709e88312, assignment blob eefbe5aa60685c7bfc6cc1a2abc1eb856d7de454, and current request blob 352f1ea2d70f3c0c48379933bb31bdcff1ef5e0. The current Fisher-information continuation is retained only at its additional-regularity scope.

Mathematical inputs:

1. fleet01/B12, commuting square-defect reserve and projected-crossing gauge stability, math-open-problems commit ee689fe26770341f205276b7b167b84f62f8f897.
2. fleet04/B12, localized destructive square-Gram stability, commit c307f81b3196820aa711a5c47f243feeeeb74781.
3. fleet02/B12, six-mode spectral-square carrier compiler, commit e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004.
4. The designated Claude package beginning at commit e5f71d79eff325201dd0274053d20268ce65b837 and all later live corrections.

No random vector is rotated. A small operator-norm matrix is used only as a deterministic singular-value perturbation, never as a small random quadratic error.

## 2. Hybrid two-profile theorem

Let \(A_0=A_0^T\) and let \(C=C^T\) commute with \(A_0\). Put
\[
B=A_0+C.
\]
Choose a simultaneous orthogonal eigenbasis and write the eigenvalues of \(A_0,B\) as \(\lambda_j,\mu_j\). Let
\[
d_j^{\rm raw}=(\lambda_j^2-\mu_j^2)_+,
\qquad d_1\ge d_2\ge\cdots\ge0
\]
be the decreasing rearrangement, with \(d_{n+1}=0\).

Now let \(D=D^T\) be completely arbitrary and define its destructive square defect relative to \(B\) by
\[
N_D=\bigl[B^2-(B+D)^2\bigr]_+.
\]
Write its eigenvalues in decreasing order as
\[
\nu_1\ge\nu_2\ge\cdots\ge0,
\qquad \nu_{n+1}=0.
\]

Finally let \(L=L^T\) have rank at most \(r\), let \(T=T^T\) satisfy \(\|T\|_{\rm op}\le\delta\), and put
\[
A=B+D+L+T.
\]

### Theorem 2.1 — QFORM-HYBRID-TWO-SQUARE-PROFILES-v1

For every original-coordinate set \(H\), and integers \(k,p,q\ge0\) satisfying
\[
k+r+q+p\le |H|,
\]
one has
\[
\boxed{
\sqrt{\lambda_k((A^2)[H,H])}
\ge
\left[
\sqrt{
\left(
\lambda_{k+r+q+p}((A_0^2)[H,H])
-d_{p+1}-\nu_{q+1}
\right)_+
}
-\delta
\right]_+ .
}
\tag{2.1}
\]

Thus:

- all commuting replacements with \(|\mu_j|\ge|\lambda_j|\) are free, regardless of sign or size;
- \(p\) severe commuting losses cost only \(p\) reserve modes;
- an arbitrary, even full-rank, noncommuting packet costs only the tail \(\nu_{q+1}\) of its destructive square defect;
- a further arbitrary-magnitude rank-\(r\) packet costs only \(r\) modes;
- the dense tail costs only \(\delta\) at the final deterministic spectral gate.

### Proof

Because \(A_0\) and \(B\) commute,
\[
B^2\ge A_0^2-N_C,
\qquad
N_C=V\,{\rm diag}\bigl((\lambda_j^2-\mu_j^2)_+\bigr)V^T.
\tag{2.2}
\]
For every compression \(H\), Weyl's inequality and compression monotonicity give
\[
\lambda_j((B^2)[H,H])
\ge
\lambda_{j+p}((A_0^2)[H,H])-d_{p+1}.
\tag{2.3}
\]

By the definition of the positive part,
\[
(B+D)^2\ge B^2-N_D.
\tag{2.4}
\]
The same argument gives
\[
\lambda_j(((B+D)^2)[H,H])
\ge
\lambda_{j+q}((B^2)[H,H])-\nu_{q+1}.
\tag{2.5}
\]
Combining (2.3) and (2.5),
\[
\lambda_j(((B+D)^2)[H,H])
\ge
\lambda_{j+q+p}((A_0^2)[H,H])
-d_{p+1}-\nu_{q+1}.
\tag{2.6}
\]

Let \(P_H\) be the coordinate embedding. Since all matrices are symmetric,
\[
s_j((B+D)P_H)^2
=
\lambda_j(((B+D)^2)[H,H]).
\]
Rank-\(r\) singular-value interlacing gives
\[
s_k((B+D+L)P_H)\ge s_{k+r}((B+D)P_H),
\tag{2.7}
\]
and singular-value Weyl gives
\[
s_k(AP_H)\ge s_k((B+D+L)P_H)-\delta.
\tag{2.8}
\]
Insert (2.6) with \(j=k+r\) into (2.7)-(2.8). This proves (2.1). \(\square\)

This theorem strictly combines the two preceding interfaces: fleet01's ordered commuting losses and fleet04's ordered noncommuting destructive-square loss can now be spent in the same inequality.

## 3. An actual target-class family

Let \(n=16\), let \(V\) be the normalized Walsh-Hadamard matrix, and let
\[
A_0=V\,{\rm diag}(2,\ldots,2,-2,\ldots,-2)\,V^T
\]
with eight signs of each type. Hence
\[
A_0^2=4I_{16}.
\tag{3.1}
\]

Perform arbitrary simultaneous eigenvalue replacements
\[
B=V\,{\rm diag}(\mu_1,\ldots,\mu_{16})\,V^T
\]
subject only to at most two inequalities \(|\mu_j|<2\). All other replacements may reverse sign and have unbounded magnitude. Therefore
\[
d_3=0.
\tag{3.2}
\]

Next add an arbitrary symmetric matrix \(D\), of any rank and norm, subject only to
\[
{\rm rank}\,[B^2-(B+D)^2]_+\le2.
\tag{3.3}
\]
Equivalently, \(\nu_3=0\). Add an arbitrary rank-one symmetric \(L\), and a full dense symmetric \(T\) with
\[
\|T\|_{\rm op}\le\frac14.
\tag{3.4}
\]
Put \(A=B+D+L+T\).

Choose any eleven original coordinates \(H\). In (2.1) take
\[
k=6,\qquad r=1,\qquad q=2,\qquad p=2.
\]
Using (3.1)-(3.4),
\[
\boxed{
\sqrt{\lambda_6((A^2)[H,H])}
\ge
\sqrt{\lambda_{11}(4I_{11})}-\frac14
=
\frac74.
}
\tag{3.5}
\]
This is an actual principal-compression spectral gate.

The final matrix also satisfies the global target hypothesis. Indeed \(B\) has at least fourteen singular values at least \(2\). From (2.5) on the full space with \(j=4,q=2\),
\[
s_4(B+D)^2
=
\lambda_4((B+D)^2)
\ge\lambda_6(B^2)-\nu_3
\ge4.
\tag{3.6}
\]
Rank-one interlacing and the dense tail then give
\[
\boxed{s_3(A)\ge s_4(B+D)-\frac14\ge\frac74>1.}
\tag{3.7}
\]

Thus the family is genuinely in the original target class. The noncommuting packet \(D\) may be full rank and arbitrarily large; it is not treated as a separable or small random remainder.

## 4. Applying the completed fleet02/B12 compiler

The six-mode theorem applies to the actual final matrix with
\[
m=11,\qquad s=g=\frac74,\qquad N=\binom{11}{2}=55.
\]
Choose
\[
b=\frac{87}{50},\qquad
a=\frac{1653}{68750},\qquad
\kappa=\frac{b}{55}-a=\frac{261}{34375}.
\]
Then \(0<a<b/N\) and \(0<b<g\). Its four terms are
\[
\frac{2\sqrt{6\pi m}}a=1197.779149\ldots,
\]
\[
\frac{\pi}{\kappa}=413.763400\ldots,
\]
\[
3\,400^{1/3}\kappa^{-5/6}s^{-1/6}
=1175.718657\ldots,
\]
and
\[
\frac{5\sqrt{2e}}{\sqrt{g^2-b^2}}
=62.405021\ldots.
\]
Therefore every admissible independent cap-one product law satisfies
\[
\boxed{\|p_{X^TAX}\|_{\infty,{\rm ess}}<1198.}
\tag{4.1}
\]

This is uniform over:

- fourteen arbitrary-sign, arbitrary-magnitude commuting eigenvalue replacements;
- two arbitrarily severe commuting destructive replacements;
- one arbitrary full-rank noncommuting packet satisfying only the rank-two destructive-square condition (3.3);
- an arbitrary-magnitude rank-one packet;
- every dense symmetric tail of operator norm at most \(1/4\).

The conclusion is essential boundedness. Continuity is not claimed because the six-mode compiler uses branches for which continuity has not been proved.

## 5. Remaining obstruction

The full conjecture is still open. The bare condition \(s_3(A)\ge1\) does not yet extract a bounded original-coordinate carrier \(H\) with enough square-Gram reserve. The new theorem enlarges the stable class after such a carrier is present, but it does not manufacture the carrier.

The exact next structural problem is:

> From \(s_3(A)\ge1\), either extract a bounded physical set \(H\) for which \(\lambda_6((A^2)[H,H])\) is quantitatively positive, or route the failure into a projected-crossing, physical-pair, ridge, Plücker-volume, or grouped-bank exit.

No independence after rotation, arbitrary-joint coarea estimate, single universally good minor, or small-random-error argument is available for that step.
