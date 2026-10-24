# B07 — actual bounded-dimensional core and diffuse-star bank extraction

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B07, 2026-09-23T09:17:40Z.

## Status

Supporting theorem and quantitative reduction only. The unrestricted conjecture remains open; continuity is separate.

## 1. Actual bounded-dimensional spectral subproblem

**Physical principal-block gate.** Let (I\subset[n]), (m=|I|), and (H=A[I,I]). If (s_3(H)\ge\gamma>0), then
[
\boxed{\|p_{X^TAX}\|_\infty\le {2\sqrt{6\pi m}\over\gamma}.}
]

Proof: condition on all original coordinates outside (I). The conditional polynomial is
[
x_I^THx_I+\ell(Z)^Tx_I+r(Z).
]
The physical-fiber theorem, including arbitrary affine translations created by conditioning, gives the displayed conditional bound. Averaging its interval form over (Z) proves the claim. The hypothesis is on the final actual principal block, so no low-rank component can be cancelled by a remaining diagonal or another matrix component. No independence after rotation is used.

Consequently, if (n\le M) and (s_3(A)\ge1), taking (I=[n]) yields
[
\boxed{\|p_{X^TAX}\|_\infty\le2\sqrt{6\pi M}.}
]
For (n\le64), this is (16\sqrt{6\pi}). Thus the actual bounded-dimensional spectral subproblem is closed in every signature and for arbitrary remaining spectrum.

## 2. Applying account01/B07 at an actual inequality

Applied source:
[
\texttt{math-open-problems@85fab09c44665e39173f34aa32529199cff0fe27}
]
at `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T083305Z-r21/CHECKPOINT.md` (blob `beeada853656d141eab2e87b6abd08e13a164f65`).

In N3 with threshold (\tau\le1), the partner proves the original-coordinate cap
[
|A_{ij}|\le\delta_\tau:=\sqrt{\tau+\tau^2}.
]
Its unpaid rank-four survivor has an actual physical row star and column star with norms exceeding
[
h=(2\sqrt2-1)\varepsilon a_0
 ={2\sqrt2-1\over1572864}
 >1.16248\times10^{-6},
]
where (\varepsilon=1/64) and (a_0=1/24576).

Choose
[
\boxed{\tau_0={h^2\over128}.}
]
Then
[
\delta_{\tau_0}\le\sqrt{2\tau_0}={h\over8}.
]
Thus every partner-supplied unpaid heavy star has norm (>h), while every individual physical coefficient in it is at most (h/8). This applies the completed partner result to the final physical entries, not to a cancellable component.

## 3. Four disjoint banks

**Lemma.** If (\|v\|_2>h) and (\|v\|_\infty\le h/8), then there are four pairwise disjoint coordinate banks (S_1,\dots,S_4) such that
[
\boxed{\|v_{S_r}\|_2\ge h/4\quad(r=1,2,3,4).}
]

Put (w_j=v_j^2\le h^2/64), with (\sum_jw_j>h^2). Greedily fill each bank until its mass first reaches (h^2/16). A completed bank has mass (<h^2/16+h^2/64=5h^2/64). After three banks, more than (49h^2/64) remains, so the fourth can be completed. Taking square roots proves the lemma. Such a star has at least 65 nonzero physical coordinates.

## 4. Quantitative coordinate-core dichotomy

At the fixed N3 threshold (\tau_0):

1. an actual bounded-size principal block (H) with (s_3(H)\ge\gamma) pays the complete law by
   [
   \|p_Q\|_\infty\le {2\sqrt{6\pi|I|}\over\gamma};
   ]
2. the partner's fifth-volume or diffuse-range alternatives pay at their stated scopes;
3. the remaining rank-four survivor contains both an actual row star and an actual column star, and each star contains four disjoint original-coordinate banks of norm at least (h/4), while every coefficient is at most (h/8).

This turns failure of bounded physical-coordinate minors into a concrete diffuse-bank certificate. It does not assume one universally good minor.

## 5. Exact residual

The full theorem is not yet closed. One must align or cross the heavy row and column bank partitions to produce an actual original-coordinate bilinear/volume certificate surviving arbitrary dense self-couplings. The partitions may overlap or be misaligned; treating that overlap as an independent product twist would be invalid. A completion must extract disjoint innovations from the overlap pattern or prove that a large overlap forces an actual bounded principal core.

## Pins

- Request blob: `165c570ecb4dcc6299c38fc3298771e4a8339dac`.
- Memory protocol blob: `0d902d56688f4b5c575f5b921ddf9f6709e88312`.
- Latest observed programme-main commit before publication: `df992ae3d72dcc485afabef7d0f1559f6e1be75a`.
- Status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.
