SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T14:47:37Z.
attacking: spectral-square row-energy spill: convert arbitrary extra spectrum into either a bounded physical core or cross smoothing directions without treating tails as random perturbations.

# account03/B12 r35 — spectral-square spill and carrier dichotomy for arbitrary added spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN**  
Continuity: **continuous C0 on the ridge and fractional-volume exits; only essential boundedness is asserted for the physical-core exit and hence for the unconditional carrier dichotomies**  
Execution-memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact contribution

This run changes mechanism from the preceding singular-tail erosion compilers. Instead of writing the final quadratic form as a baseline plus a random quadratic remainder, it uses the exact positive identity

\[
(A^2)_{HH}=A_{HH}^2+A_{H,H^c}A_{H^c,H}
\tag{1.1}
\]

on ORIGINAL coordinates. This gives a sign-free way to route spectral energy: if a spectral window has substantial compression to a physical coordinate set, then either the physical self block already has three substantial eigenvalues or the missing energy must appear in many singular directions of the actual final cross block.

The central deterministic theorem is the following.

### Theorem 1.1 — `QFORM-SPECTRAL-SQUARE-SPILL-STABILITY-v1`

Let \(A=A^T\) and let \(H\) be a set of original coordinates. Write

\[
C=A[H,H],\qquad B=A[H,H^c].
\]

Let \(G\) be any positive-semidefinite matrix satisfying

\[
0\le G\le A^2.
\]

Suppose for some integer \(k\ge1\) and \(g>0\),

\[
\lambda_k(G[H,H])\ge g^2.
\tag{1.2}
\]

For any integer \(0\le r<k\), put \(c=s_{r+1}(C)\). If \(c<g\), then

\[
\boxed{
 s_{k-r}(B)\ge \sqrt{g^2-c^2}.
}
\tag{1.3}
\]

All singular values are in decreasing order. No sign hypothesis is imposed anywhere.

A canonical choice is the final-matrix spectral window

\[
P_\Lambda={\bf1}_{\{|A|\ge\Lambda\}},\qquad G=\Lambda^2P_\Lambda.
\]

Since \(A^2\ge\Lambda^2P_\Lambda\), if

\[
\lambda_k(P_\Lambda[H,H])\ge a,
\]

then

\[
\boxed{
 s_{k-r}(A[H,H^c])
 \ge \sqrt{\Lambda^2 a-s_{r+1}(A[H,H])^2}
}
\tag{1.4}
\]

whenever the radicand is positive.

This is the assigned additional-eigenvalue control at matrix level. Every eigenvalue below the window, however numerous and of either sign, remains in the final matrix and is never called a small random perturbation. Every eigenvalue above the window, including additional arbitrarily large ones of either sign, contributes positively to the spectral square. The random input is never rotated.

## 2. Proof of the spectral-square spill theorem

The exact block multiplication identity is

\[
(A^2)[H,H]=C^2+BB^T.
\tag{2.1}
\]

Spectrally truncate the symmetric matrix \(C\) at rank \(r\): write

\[
C=C_r+E,
\]

where \(C_r\) contains the \(r\) eigenmodes of largest absolute eigenvalue. Then

\[
\operatorname{rank}C_r\le r,\qquad C_rE=EC_r=0,
\qquad E^2\le c^2I_H,
\tag{2.2}
\]

because \(c=s_{r+1}(C)\). Therefore

\[
BB^T+C_r^2
=(A^2)[H,H]-E^2
\ge G[H,H]-c^2I_H.
\tag{2.3}
\]

By (1.2),

\[
\lambda_k(BB^T+C_r^2)\ge g^2-c^2.
\tag{2.4}
\]

The matrix \(C_r^2\) is positive semidefinite of rank at most \(r\). Weyl's eigenvalue inequality gives, for \(k>r\),

\[
\lambda_k(BB^T+C_r^2)
\le \lambda_{k-r}(BB^T)+\lambda_{r+1}(C_r^2)
=\lambda_{k-r}(BB^T).
\tag{2.5}
\]

Combining (2.4) and (2.5) proves

\[
s_{k-r}(B)^2=\lambda_{k-r}(BB^T)\ge g^2-c^2,
\]

which is (1.3). Equation (1.4) follows from \(G=\Lambda^2P_\Lambda\). QED.

Two features are important. First, the theorem charges only the actual physical self block; no moment of \(X\) appears. Second, the argument is monotone in the full spectral square: additional large directions cannot invalidate the certificate merely because their signs differ.

## 3. Leverage-free analytic exit: seven spectral-square modes

Let \(|H|=m\), assume (1.2) for some \(k\ge7\), and put

\[
A_m=2\sqrt{6\pi m},
\qquad
D_j={3j\sqrt{3e}\over2(j-4)^{3/2}},\quad j\ge5.
\tag{3.1}
\]

The completed finite-dimensional physical receiver says that if \(s_3(C)\ge h\), then after conditioning only on the outside ORIGINAL coordinates,

\[
\|p_Q\|_\infty\le {A_m\over h}.
\tag{3.2}
\]

The completed \(q=2\) ridge theorem says that if an actual original-coordinate cross block has \(j\ge5\) singular values at least \(b\), then the full ambient quadratic form has a continuous \(C_0\) density and

\[
\|p_Q\|_\infty\le {D_j\over b}.
\tag{3.3}
\]

Its leverage condition is automatic at \(q=2\).

Fix \(0<\tau<1\). If \(s_3(C)\ge\tau g\), use (3.2). Otherwise Theorem 1.1 with \(r=2\) gives

\[
s_{k-2}(B)\ge g\sqrt{1-\tau^2},
\]

and \(k-2\ge5\), so (3.3) applies. Hence

\[
\|p_Q\|_\infty
\le {1\over g}
\max\left\{ {A_m\over\tau},
{D_{k-2}\over\sqrt{1-\tau^2}}\right\}.
\tag{3.4}
\]

Choosing

\[
\tau={A_m\over\sqrt{A_m^2+D_{k-2}^2}}
\]

equalizes the two branches and proves the following.

### Theorem 3.1 — `QFORM-SPECTRAL-SQUARE-CARRIER-DICHOTOMY-v1`

If an original-coordinate set \(H\) of size \(m\) and a certificate \(0\le G\le A^2\) satisfy

\[
\lambda_k(G[H,H])\ge g^2
\]

for some \(k\ge7\), then

\[
\boxed{
\|p_Q\|_\infty
\le {\sqrt{A_m^2+D_{k-2}^2}\over g}.
}
\tag{3.5}
\]

All outside spectrum, all outside couplings, all signs and all input supports are unrestricted. No cross-block leverage hypothesis is needed.

For the smallest carrier \(m=k=7\),

\[
A_7=2\sqrt{42\pi},\qquad D_5={15\sqrt{3e}\over2},
\]

and therefore

\[
\boxed{
\|p_Q\|_\infty
\le {31.4085597307\ldots\over g}.
}
\tag{3.6}
\]

For a final spectral window, if

\[
\lambda_7(P_\Lambda[H,H])\ge a,
\]

then \(g=\Lambda\sqrt a\), so

\[
\boxed{
\|p_Q\|_\infty
\le {31.40856\over \Lambda\sqrt a}.
}
\tag{3.7}
\]

This is a dimension-free, sign-free theorem for arbitrary additional spectrum once seven units of spectral-square mass have an actual bounded physical carrier. The overall theorem only asserts an essentially bounded density because its physical-core branch does not supply continuity. The ridge branch itself is continuous \(C_0\).

## 4. Five-mode carrier with a diffuse final cross range

The newest fractional three-volume theorem gives a stronger cross receiver when only three cross singular directions survive. For an actual cross block \(B\), its third-volume marginal operator \(W\) satisfies

\[
0\le W\le P_{\operatorname{Ran}B}.
\tag{4.1}
\]

Thus if

\[
\max_i(P_{\operatorname{Ran}B})_{ii}\le {1\over2},
\tag{4.2}
\]

all row volume marginals obey \(\alpha_i\le1/2\). The \(q=1\) fractional-volume theorem then gives

\[
\|p_Q\|_\infty\le 3e\,e_3(B^TB)^{-1/6}
\le {3e\over s_3(B)},
\tag{4.3}
\]

with a continuous \(C_0\) density.

Suppose now \(k\ge5\) in (1.2) and (4.2) holds. If \(s_3(C)\ge\tau g\), use the physical receiver; otherwise Theorem 1.1 with \(r=2\) yields \(s_3(B)\ge g\sqrt{1-\tau^2}\). Consequently

\[
\|p_Q\|_\infty
\le {1\over g}
\max\left\{{A_m\over\tau},{3e\over\sqrt{1-\tau^2}}\right\}.
\]

Optimizing gives

\[
\boxed{
\|p_Q\|_\infty
\le {\sqrt{A_m^2+9e^2}\over g}.
}
\tag{4.4}
\]

For \(m=k=5\),

\[
\boxed{
\|p_Q\|_\infty
\le {21.0592645484\ldots\over g}.
}
\tag{4.5}
\]

This equation is an actual application of the newest volume-stability package at its exact marginal gate, not merely a citation. It is continuous on the volume exit and only essentially bounded on the physical exit.

## 5. Required account04/B12 partner application

The designated completed partner result is

`yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its complementary-Schur theorem permits an arbitrary real symmetric \(2\times2\) hostile spectral packet \(\Theta\), with unbounded eigenvalue magnitude and either sign. In its explicit five-coordinate core,

\[
D=\operatorname{diag}(2,-2,2),\qquad \rho={1\over2}.
\]

For an additional arbitrary dense symmetric local tail of norm at most \(1/5\), the partner theorem gives the actual matrix inequality

\[
\begin{aligned}
g_{\rm partner}
&=2\left({9-\sqrt{17}\over8}\right)-{1\over5}\\
&={41-5\sqrt{17}\over20}
=1.019223593595\ldots>0.
\end{aligned}
\tag{5.1}
\]

Applying its physical receiver at \(m=5\) yields

\[
\boxed{
\|p_Q\|_\infty
\le {2\sqrt{30\pi}\over g_{\rm partner}}
={40\sqrt{30\pi}\over41-5\sqrt{17}}
=19.0500487308\ldots.
}
\tag{5.2}
\]

Thus a structured arbitrary-magnitude signed packet is already completely free on this branch; only the dense residual tail is charged. This partner use is at an explicit inequality and does not assume independence of the spectral remainder.

## 6. Why the spectral-square route is useful for arbitrary extra eigenvalues

Suppose the final matrix has spectral decomposition

\[
A=\sum_j\lambda_j v_jv_j^T.
\]

At threshold \(\Lambda\),

\[
A^2\ge\Lambda^2\sum_{|\lambda_j|\ge\Lambda}v_jv_j^T.
\tag{6.1}
\]

Equation (6.1) treats positive and negative eigenvalues identically and never separates their random quadratic contributions. In particular:

1. arbitrarily many smaller eigenvalues of either sign are retained exactly and cannot reduce the PSD lower certificate;
2. arbitrary larger eigenvalues of either sign add PSD spectral-square mass rather than becoming hostile random noise;
3. if that energy does not appear in the physical self block beyond two directions, (1.3) forces it into the final cross block;
4. the only remaining payment is geometric: whether enough spectral-square energy can be carried by a bounded original-coordinate set, or whether the spread-out remainder enters one of the existing diffuse/grouped/hub exits.

This is qualitatively different from the preceding r32-r34 mechanism, which fixed a baseline cross block and eroded its singular profile by \(s_{r+1}\) of an added perturbation.

## 7. Finite deterministic checks

The accompanying `CHECK.py` tests the spectral-window specialization (1.4) on 10,000 seeded random mixed-sign symmetric matrices, with random coordinate carriers, thresholds and rank budgets. There were 3,466 positive-radicand certificates and zero violations. The minimum observed value of

\[
s_{k-r}(B)^2-(\Lambda^2a-s_{r+1}(C)^2)
\]

among the tested positive certificates was \(0.9543495160\ldots\). The checker also evaluates the simple split constants and the partner constant. These computations are sanity checks only; the proof is the deterministic argument in Section 2.

## 8. Exact scope and remaining gap

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new result removes a real additional-spectrum difficulty: once a spectral-square carrier is present, arbitrary other eigenvalues of either sign cannot be treated as an independent convolution and need not be. They are retained in the final matrix, while (1.1) forces a self-versus-cross alternative.

The missing target-level implication is structural. The bare assumption that \(A\) has only three eigenvalues of modulus at least one does **not** itself provide the five- or seven-mode carrier used above. The next useful B12 step is therefore:

> from only the three-large-eigenvalue premise, prove either a bounded original-coordinate spectral-square carrier of the type above, or force the complementary low-carrier geometry into an already-paid diffuse-volume, grouped-bank, hub/star, ridge-window, pair, or rank-two-half-Riesz exit.

That implication is not proved here. No general continuity conclusion is claimed. There is no use of Gaussianity, moments, compact support, log-concavity, connected support, spectral-coordinate independence, pointwise van der Corput decay, arbitrary-joint coarea, or dimension-growing fiber suprema.

## 9. Sources and control state

Fresh control was resolved before publication at

`yspennstate/math-research-brain@357e76eed6b53af5ec39f085b88d25d2a8554b29`.

The programme remained `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`, OWNER CONTROL `2026-09-22.15`, with no account03/B12 pause. The live correction inbox blob remained

`c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Primary mathematical dependencies actually used:

- Ridge receiver: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
- Fractional three-volume receiver: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
- Designated partner: `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured thinking level and provider reasoning-token/thinking-time counters were not exposed and remain `UNKNOWN`/null.
