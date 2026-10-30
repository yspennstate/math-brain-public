SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B12, 2026-09-23T18:21:00Z.
attacking: localized destructive square-Gram stability on an actual original-coordinate carrier, with arbitrary signed large modes and a deterministic dense-tail spectral gate.

# B12 — localized destructive square-Gram stability

Run: `20260923T182100Z-fleet04-B12-local-destructive-square-r6`

Status: **new supporting stability theorem proved; exact target-class family proved; full QFORM remains open.**

Continuity is not claimed by the physical spectral-square compiler used here.

## 1. Actual carrier defect

Let $A_0,D$ be real symmetric $n\times n$ matrices and let $H$ be a set of $m$ original coordinates, with coordinate inclusion $P_H:\mathbb R^m\to\mathbb R^n$. Put
$$
B=A_0+D,\qquad
G_0=P_H^TA_0^2P_H,\qquad
G=P_H^TB^2P_H.
$$
Define the positive semidefinite destructive square-Gram defect
$$
N_H(A_0,D)=[G_0-G]_+,
$$
and write its eigenvalues as $\nu_1\ge\nu_2\ge\cdots\ge0$.

This object measures only the loss of squared spectral energy on the actual physical carrier $H$. It may vanish even when $D$ is full rank, has arbitrary signs, and has unbounded operator norm.

## 2. Local destructive-defect theorem

For $k+r\le m$,
$$
\boxed{
\sqrt{\lambda_k(G)}
\ge
\sqrt{\bigl(\lambda_{k+r}(G_0)-\nu_{r+1}\bigr)_+}.
}
\tag{2.1}
$$

If $T$ is any further symmetric matrix with $\|T\|_{\rm op}\le\delta$, and $A=B+T$, then
$$
\boxed{
\sqrt{\lambda_k(P_H^TA^2P_H)}
\ge
\left[
\sqrt{\bigl(\lambda_{k+r}(G_0)-\nu_{r+1}\bigr)_+}
-\delta
\right]_+ .
}
\tag{2.2}
$$

In particular, if $\operatorname{rank}N_H(A_0,D)\le r$, then
$$
\boxed{
\sqrt{\lambda_k(P_H^TA^2P_H)}
\ge
\left[\sqrt{\lambda_{k+r}(G_0)}-\delta\right]_+ .
}
\tag{2.3}
$$

### Proof

Apply the completed fleet01/B12 destructive Gram-defect theorem to the rectangular matrices
$$
M_0=A_0P_H,\qquad E=DP_H.
$$
Their right Gram matrices are exactly
$$
M_0^TM_0=P_H^TA_0^2P_H=G_0,
$$
$$
(M_0+E)^T(M_0+E)=P_H^TB^2P_H=G.
$$
Thus fleet01/B12 equation (3.1) gives
$$
s_k(BP_H)^2\ge
\bigl(s_{k+r}(A_0P_H)^2-\nu_{r+1}\bigr)_+,
$$
which is (2.1). Since
$$
s_k(AP_H)\ge s_k(BP_H)-\|TP_H\|_{\rm op}
\ge s_k(BP_H)-\delta,
$$
equation (2.2) follows. If $\operatorname{rank}N_H\le r$, then $\nu_{r+1}=0$, giving (2.3). QED.

The small dense tail is used only in the deterministic singular-value comparison above. No random term $X^TTX$ is discarded or treated as a small error.

## 3. Relation to the preceding local Krylov-shadow theorem

The preceding B12 local-shadow theorem charged
$$
q_H=\dim P_H(\operatorname{Ran}D+A_0\operatorname{Ran}D)
$$
reserve directions. Indeed
$$
\operatorname{Ran}(G-G_0)
\subseteq P_H(\operatorname{Ran}D+A_0\operatorname{Ran}D),
$$
so $\operatorname{rank}N_H\le q_H$. Hence (2.3) recovers that theorem.

The new formulation can be strictly stronger: $D$ may have full rank and a full-dimensional Krylov shadow while $N_H=0$. Only actual destruction of the carrier square Gram is charged.

## 4. Zero-cost nonlinear class

Whenever
$$
P_H^T(A_0+D)^2P_H\succeq P_H^TA_0^2P_H,
\tag{4.1}
$$
one has $N_H=0$, and therefore every carrier singular value is nondecreasing:
$$
\boxed{s_k((A_0+D)P_H)\ge s_k(A_0P_H).}
\tag{4.2}
$$

This is not a small-perturbation statement and imposes no sign or size condition on $D$.

## 5. Exact target-class family with a full-rank unbounded signed packet

Let $\mathbb R^{16}=H\oplus J$, with $|H|=|J|=8$, and set
$$
A_0=
\begin{pmatrix}
0&2I_8\\
2I_8&0
\end{pmatrix}.
\tag{5.1}
$$
Let $J_0$ be block diagonal with four copies of
$$
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
$$
so $J_0^T=-J_0$ and $J_0^TJ_0=I_8$. For arbitrary $t\in\mathbb R$, define the symmetric addition
$$
D_t=
\begin{pmatrix}
0&tJ_0\\
tJ_0^T&0
\end{pmatrix}.
\tag{5.2}
$$
It has eight eigenvalues $+|t|$ and eight eigenvalues $-|t|$. Thus it is a full-rank signed spectral packet of completely unrestricted magnitude.

For $B_t=A_0+D_t$,
$$
P_H^TB_t^2P_H=(2I_8+tJ_0)(2I_8+tJ_0)^T=(4+t^2)I_8.
\tag{5.3}
$$
Consequently $N_H(A_0,D_t)=0$.

Now add any further symmetric $L$, of arbitrary rank, signs, and norm, satisfying only
$$
\operatorname{rank}N_H(B_t,L)\le2,
\tag{5.4}
$$
and finally any dense symmetric $T$ with
$$
\|T\|_{\rm op}\le\frac14.
\tag{5.5}
$$
Set $A=B_t+L+T$.

Apply (2.3) with baseline $B_t$, $k=6$, and $r=2$:
$$
\sqrt{\lambda_6(P_H^TA^2P_H)}
\ge\sqrt{\lambda_8(P_H^TB_t^2P_H)}-\frac14
=\sqrt{4+t^2}-\frac14
\ge\frac74.
\tag{5.6}
$$
Thus the actual physical carrier has
$$
\boxed{\lambda_6((A^2)[H,H])\ge\frac{49}{16}.}
\tag{5.7}
$$

Moreover $s_6(A)\ge s_6(AP_H)\ge7/4$, hence
$$
\boxed{s_3(A)\ge\frac74>1.}
\tag{5.8}
$$
Every matrix in this family therefore lies literally in the owner's target class.

## 6. Apply the completed fleet01/B12 density compiler

Use the completed fleet01/B12 physical spectral-square compiler on the actual carrier $H$, with the same admissible parameters as the preceding B12 run:
$$
m=8,\quad N=28,\quad s=g=\frac74,\quad
b=\frac{17}{10},\quad a=\frac3{70},\quad \kappa=\frac1{56}.
$$
Its four exhaustive physical exits are bounded respectively by
$$
573.063,\qquad175.930,\qquad576.490,\qquad28.070.
$$
Combining those exits with (5.7)-(5.8) gives, for every independent cap-one product law,
$$
\boxed{\|p_{X^TAX}\|_\infty<577.}
\tag{6.1}
$$

This bound is uniform in $t$, in every arbitrary-magnitude $L$ obeying only the rank-two destructive carrier-defect condition (5.4), and in every dense tail satisfying (5.5). Neither $D_t$ nor $L$ is treated as a random perturbation.

## 7. What remains

The unrestricted conjecture remains open. The missing structural implication is still to extract, from $s_3(A)\ge1$ alone, a bounded physical carrier having enough square-Gram reserve after its destructive defect is charged, or to route failure into an already-paid minor, ridge, hub, or grouped-bank mechanism.

The present theorem strengthens the additional-spectrum side: arbitrary large modes should be charged by the rank and residual spectrum of the **actual carrier energy they destroy**, not by their global rank or operator norm.

## 8. Source pins and scope

- Fresh math-open-problems head before publication: `9c76ff548cf7e7946a5911f56cb251391d7ad3f1`.
- Completed fleet01/B12 destructive Gram-defect report: blob `18c147393ec05081fa13b931a4538b14faf79dc3`.
- Preceding fleet04/B12 local-shadow report: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260923T171921Z-fleet04-B12-local-krylov-shadow-r5/REPORT.md`.
- Required Claude baseline: `e5f71d79eff325201dd0274053d20268ce65b837`.

No moment, support, Gaussian, log-concavity, iid, post-rotation independence, or small-random-error assumption is used. Full-target continuity remains open. Execution status remains `WITHOUT_VERIFIED_BRAIN`.
