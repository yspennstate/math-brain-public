SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T23:23:27Z.
attacking: the aligned two-bank carrier plus diagonal survivor after the simultaneous-cut theorem; convert small diagonal twists into a rank-four ridge-window exit and a quantitative physical localized witness.

# account03/B08 r45 — exact aligned carrier: rank-four ridge-window or physical localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: **NEW SUPPORTING ROUTER / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. The new statement below is a product-safe, original-coordinate estimate for the exact aligned common-plane survivor. It uses no moments, Gaussianity, log-concavity, bounded or connected support, or independence after a rotation. Continuity is proved only on the ridge-window and partner child-window branches explicitly identified below.

## 1. Control and correction boundary

Fresh control at the final prepublication refresh was `yspennstate/math-research-brain@47d9b52fcf49ce23e58bcb7b4eb02480d0f5766b`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM only. The live `CORRECTION_INBOX.json` was reread at that commit. In particular this run does **not** use a uniform pointwise van-der-Corput estimate, an arbitrary-joint coarea estimate, post-rotation independence, naive fiber-sup integration, a universally good scalar Schur pivot, or deletion of a small quadratic term as random noise.

The canonical actual-hour login/start was already present for this run (`20260923T232327Z-account03-B08-qform-diffuse-r45`); no duplicate login or start record was created.

## 2. Source-matching theorem ends the previous duplicate scope

The first unpaid implication from account03/B08 r44 was the arbitrary-high-rank simultaneous physical cut in the exact common-plane state. Before attempting it again, I found that account02/B08 had already completed exactly that step:

`yspennstate/math-open-problems@af30108d1fd48a138ef13c683d397a74f8e0228e`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260923T2307Z-auto11/REPORT.md`.

Its theorem `QFORM-EXACTMATCH-HIGHRANK-COMPOUND-ROUTER-v1` proves, for a two-row physical arm `M` and arbitrary same-bank symmetric residual `S`, the exact compound identity

\[
\Xi(M,S)=S_M^2 D_M(S)^2,
\qquad S_M=\sqrt{\det(MM^T)},
\]

and finds a literal physical cut whose arm-area/projected-crossing product is at least

\[
\sqrt{27/256}\,\Xi(M,S)^{1/2}.
\]

If the projected crossing is diffuse across physical rows, the full ambient form has a continuous density with

\[
\|p_Q\|_\infty
\le 2^{13/6}\sqrt3\,(S_M D_M(S))^{-1/3}.
\tag{2.1}
\]

Otherwise an actual original-coordinate row carries more than half the projected-crossing Frobenius mass. Thus the previous r44 simultaneous-cut debt is closed at its stated scope, and this run changes mechanism to the successor rather than duplicating it.

At the inherited B08 arm scale

\[
S_M>\frac{L^2}{64\sqrt{896}},
\]

define

\[
\eta_{619}=\frac{(2^{13/6}\sqrt3/619)^3}{1/(64\sqrt{896})}
=0.0037987340155334467\ldots .
\]

Then the completed theorem gives the actual inequality

\[
D_M(S)\ge \eta_{619}L
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty<619/L}
\tag{2.2}
\]

on the diffuse-row branch, while the complementary heavy-row branch contains an actual projected physical row of norm

\[
>\frac{3\sqrt6}{32}\eta_{619}L
=8.72340000619756\times 10^{-4}L.
\tag{2.3}
\]

Hence the still-unpaid exact-match state is quantitatively aligned with the two-dimensional arm carrier, modulo physical diagonal twists and a separately recorded small alignment defect.

## 3. Exact aligned normal form

The exact aligned two-bank state can be written, after combining the two light banks into one physical light vector `x in R^m`, as

\[
A=\begin{pmatrix}
B & M\\
M^T & M^T R M+D
\end{pmatrix},
\tag{3.1}
\]

where `B,R` are arbitrary real symmetric `2 x 2` matrices, `M` is an arbitrary `2 x m` physical arm matrix, and

\[
D=\operatorname{diag}(d_1,\ldots,d_m)
\tag{3.2}
\]

is the physical diagonal twist. This is an identity in the original independent coordinates; no random-coordinate rotation is performed.

Let

\[
A_0=\begin{pmatrix}B&M\\M^T&M^TRM\end{pmatrix},
\qquad
\widetilde D=\operatorname{diag}(0,0,d_1,\ldots,d_m).
\]

Define the linear map

\[
T(h,x)=(h,Mx)\in\mathbb R^4,
\qquad
K=\begin{pmatrix}B&I_2\\I_2&R\end{pmatrix}.
\]

Then exactly

\[
\boxed{A_0=T^TKT},
\tag{3.3}
\]

so

\[
\boxed{\operatorname{rank}(A_0)\le4.}
\tag{3.4}
\]

This is the structural fact used below. It retains arbitrary near-singularity of `B` and arbitrary size/sign of `R`.

## 4. Main theorem: small diagonal twist gives ridge-window payment or an actual localized row

### Theorem — `QFORM-EXACTMATCH-SMALLTWIST-RIDGE-LOCALIZED-v1`

Assume (3.1), and suppose the full symmetric matrix `A` has at least three eigenvalues of modulus at least `L>0`. If

\[
\|D\|_{\mathrm{op}}=\max_j|d_j|\le L/128,
\tag{4.1}
\]

let

\[
P=\mathbf 1_{\{|A|\ge L/64\}}
\tag{4.2}
\]

be the physical-coordinate spectral-window projection. Then exactly one of the following useful alternatives holds.

**Diffuse-window alternative.** If

\[
\max_i P_{ii}\le1/32,
\tag{4.3}
\]

then the full quadratic form, for every independent cap-one product input, has a continuous `C_0` density satisfying

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le \frac{288\sqrt{3e}}{13L}
<\frac{64}{L}.}
\tag{4.4}
\]

**Localized-window alternative.** Otherwise there is an actual original coordinate `i` for which

\[
P_{ii}>1/32
\tag{4.5}
\]

and therefore

\[
\boxed{\|Ae_i\|_2>\frac{L}{64\sqrt{32}}=\frac{L}{256\sqrt2}.}
\tag{4.6}
\]

More concretely, for that same physical coordinate either

\[
\boxed{|A_{ii}|\ge \frac{L}{512\sqrt2}}
\tag{4.7}
\]

or its off-diagonal physical star obeys

\[
\boxed{
\left(\sum_{j\ne i}A_{ij}^2\right)^{1/2}
>\frac{\sqrt{3/2}}{512}L
=0.002392079826936697\ldots L.}
\tag{4.8}
\]

The theorem makes no continuity claim on the unconsumed localized alternative.

### Proof

Because `rank(A_0)<=4`, the fifth singular value of `A_0` is zero. Singular-value perturbation and (4.1) give

\[
s_5(A)\le s_5(A_0)+\|\widetilde D\|_{\rm op}
\le L/128<L/64.
\tag{4.9}
\]

Therefore the projection `P` in (4.2) has rank at most four. It has rank at least three because the original target supplies three eigenvalues of modulus at least `L`. Thus this exact aligned survivor really is a three-or-four-dimensional spectral packet even if the physical dimension is arbitrarily large.

If (4.3) holds, scale by `L` and apply the completed spectral-window theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`, Section 7.

That theorem permits arbitrary smaller nonzero eigenvalues of either sign and gives the continuous bound `288 sqrt(3e)/13` at unit scale. Since `X^TAX=L X^T(A/L)X`, density scaling gives (4.4).

If (4.3) fails, choose `i` with (4.5). In an orthonormal eigenbasis of `A`,

\[
\|Ae_i\|_2^2
=\sum_k\lambda_k^2|u_k(i)|^2
\ge (L/64)^2P_{ii}
>\frac{L^2}{64^2\,32},
\]

which is (4.6). Finally

\[
\|Ae_i\|_2^2=A_{ii}^2+\sum_{j\ne i}A_{ij}^2.
\]

If (4.7) fails, subtracting the square of half the lower bound in (4.6) leaves three quarters of that squared norm, yielding (4.8). This proves the theorem. QED.

### Operator-stable variant

The same proof needs only a rank-at-most-four matrix `A_0` and a perturbation `E` satisfying `||E||op<=L/128`. Thus (4.4)-(4.8) remain valid for

\[
A=A_0+E,
\qquad \operatorname{rank}(A_0)\le4,
\qquad \|E\|_{op}\le L/128.
\tag{4.10}
\]

This does **not** assert that the inherited weighted leave-one-out alignment defect `D_M(S)` automatically controls operator norm; that conversion remains unpaid and is not silently assumed.

## 5. Designated partner account04/B08 applied to an actual branch

The completed designated partner theorem is

`yspennstate/math-open-problems@af30108d1fd48a138ef13c683d397a74f8e0228e`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`,
`QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`.

Take the localized coordinate `i` supplied by (4.5) and write

\[
A=\begin{pmatrix}a&b^T\\b&C\end{pmatrix}
\]

after moving this **original** coordinate first. If its physical deletion child `C` has three eigenvalues of modulus at least `L/64`, and if the child spectral projection

\[
P_C=\mathbf1_{\{|C|\ge L/4096\}}
\]

satisfies

\[
\max_j(P_C)_{jj}\le1/32,
\]

then the partner theorem with `m=L/64` gives the actual full-form inequality

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le \frac{288\sqrt{3e}}{13(L/64)}
<\frac{4096}{L},}
\tag{5.1}
\]

and the output density is continuous `C_0`. The cross vector `b`, the scalar `a`, all signs, and every additional child coefficient are retained exactly by conditioning on `X_i`.

Thus the localized alternative in Theorem 4 is further paid whenever its deletion child remains genuinely three-dimensional and diffuse at its own spectral window. The remaining localized state must instead exhibit child spectral loss or another child coordinate with leverage `>1/32`; this is a sharper successor certificate than merely saying “the ridge gate failed.”

## 6. Rigorous computation / regression checks

The exact constants used above are

\[
\frac{288\sqrt{3e}}{13}=63.26405187778285\ldots,
\]

\[
\frac1{64\sqrt{32}}=0.002762135864009951\ldots,
\quad
\frac1{512\sqrt2}=0.0013810679320049755\ldots,
\]

\[
\frac{\sqrt{3/2}}{512}=0.002392079826936697\ldots .
\]

For the inherited compound theorem,

\[
s_*=1/(64\sqrt{896})=0.0005219946131102039\ldots,
\]

\[
C_*=2^{13/6}\sqrt3=7.7766451889586605\ldots,
\quad
\eta_{619}=0.0037987340155334467\ldots,
\]

and `(3 sqrt(6)/32) eta_619 = 0.000872340000619756...`.

A seeded 1000-instance finite-dimensional regression test of the factorization `A_0=T^TKT` and the perturbation inequality `s_5(A)<=||D||op` produced maximum factorization error exactly zero at floating precision and zero violations of the singular-value inequality. These checks support the algebra; the proof above is analytic and does not depend on simulation.

## 7. Exact progress and remaining implication

This run does **not** solve the unrestricted conjecture. It does three concrete things:

1. records that the previous r44 arbitrary-high-rank simultaneous-cut debt is already completed by account02/B08, and applies that theorem to the actual `619/L` inherited gate (2.2);
2. proves that an exact aligned two-bank carrier with physical diagonal twist at most `L/128` is either paid continuously by `<64/L` or produces an explicit original-coordinate diagonal/star witness (4.7)-(4.8);
3. applies the designated account04/B08 deletion-child theorem to pay a genuine child-diffuse subbranch by `<4096/L`.

The next B08 implication is therefore

`QFORM-ALIGNED-LARGETWIST-OR-LOCALIZED-WINDOW-COMPILER-v1`:

> consume either (a) a large physical diagonal twist `max |d_j|>L/128`, allowing cancellation with the aligned `M^T R M` diagonal; or (b) the explicit localized ridge-window witness (4.7)/(4.8) when its deletion child has spectral loss or another high-leverage window, while retaining all aligned same-bank curvature and product provenance. Separately, convert the small nonzero weighted leave-one-out alignment defect into an operator-stable or grouped-coordinate currency without asserting a false operator-norm bound.

Essential boundedness and continuity remain OPEN globally. The new ridge and partner child-window branches are continuous `C_0`; the compound diffuse branch (2.2) is continuous by its source theorem; the unconsumed localized/large-twist states carry no continuity claim.
