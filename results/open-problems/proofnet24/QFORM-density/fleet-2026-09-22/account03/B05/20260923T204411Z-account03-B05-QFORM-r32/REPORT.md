SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T20:44:11Z.
attacking: QFORM-HEAVY-ROW-RESIDUAL-DESCENT-v1 — when the r31 Pluecker split fails because one packet row has leverage >=1/2, either spend that row through the exact-slope partner theorem or remove it in original coordinates and prove a strict quantitative contraction of the ratio-variance obstruction.

# account03/B05 r32 — heavy-row residual descent for the ratio packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea bound / product-preserving interval bounds  
Startup control head observed: `yspennstate/math-research-brain@9db813c4f626bc3e85821d23012bcc6fba58178c`; OWNER CONTROL revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING STRUCTURAL/QUANTITATIVE LEMMA; ONE HEAVY-ROW CHAMBER CLOSED; FULL QFORM OPEN**  
Continuity: not proved by the new descent lemma; the r31 exact-cross exits it feeds into do prove continuity in their stated branches.

## 1. Exact sources used

1. Ratio-variance packet normal form:
   `yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946:proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T033640Z-account01-B05-QFORM-r26/REPORT.md`.
2. Designated partner `account04/B05` dominant exact-slope theorem:
   `yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.
   It proves
   \[
   \|p_Q\|_\infty<51.6(\mu m_*)^{-1/3},
   \]
   where `m_*` is the largest exact physical slope-class `u`-mass.
3. Own predecessor r31, Pluecker aggregate / exact-rank-three crossing:
   `yspennstate/math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T193756Z-account03-B05-QFORM-r31/REPORT.md`.
   Its diffuse first-bank hypothesis is `q_X=max_i ||g_i||^2<1/2`; the present run attacks the complementary heavy-row gate.
4. Fresh arbitrary-rank projected-crossing checkpoint was read for compatibility only:
   `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

No independence after rotation is used. Every conditioning step below conditions a literal original coordinate.

## 2. Ratio packet and normalized leverage

Take a nonzero-residual ratio packet `G` from r26. Thus
\[
m=\sum_{i\in G}u_i^2>0,
\qquad
r=\frac{\sum_{i\in G}u_it_i}{m},
\qquad
e_i=t_i-r u_i,
\qquad
\sigma^2=\sum_{i\in G}e_i^2>0,
\]
with
\[
\sum_{i\in G}u_i e_i=0.
\]
Define the orthonormal product projection
\[
S=m^{-1/2}\sum_{i\in G}u_iX_i,
\qquad
R=\sigma^{-1}\sum_{i\in G}e_iX_i.
\]
Its Parseval frame rows are
\[
g_i=\left(\frac{u_i}{\sqrt m},\frac{e_i}{\sigma}\right),
\qquad
\sum_{i\in G}g_i g_i^T=I_2.
\]
Put
\[
a_i=\frac{u_i^2}{m},
\qquad
b_i=\frac{e_i^2}{\sigma^2},
\qquad
q_i=\|g_i\|^2=a_i+b_i,
\qquad q_X=\max_i q_i.
\]
The packet homogeneous Schur remainder over the independent scalar pair `(Y,Z)` is exactly
\[
\lambda\begin{pmatrix}m&0\\0&0\end{pmatrix},
\qquad
\mu=|\det B|\,|\lambda|.
\]
This is an exact identity, not an approximation.

## 3. Heavy-row residual-descent lemma

### Theorem 3.1 (`QFORM-HEAVY-ROW-RESIDUAL-DESCENT-v1`)

Assume `q_X>=1/2`, choose `h` with `q_h=q_X`, and fix any
\[
0<\theta<\frac14.
\]
Then one of the following two alternatives holds.

**A. Schur-mass / exact-slope payment.** If
\[
a_h=\frac{u_h^2}{m}\ge\theta,
\]
then the singleton physical slope class containing `h` has mass at least `theta m`; hence the designated partner theorem gives
\[
\boxed{
\|p_Q\|_\infty<51.6(\mu\theta m)^{-1/3}.
}
\tag{3.1}
\]
This is a full-line interval/density bound for the whole conditional form, with arbitrary affine terms.

**B. Residual-heavy descent.** If `a_h<theta`, condition the literal original coordinate `X_h`, put `G'=G\\{h}`, and let
\[
m'=\sum_{i\in G'}u_i^2,
\qquad
r'=\frac{\sum_{i\in G'}u_it_i}{m'},
\qquad
\sigma'^2=\sum_{i\in G'}(t_i-r'u_i)^2.
\]
Then
\[
\boxed{m'>(1-\theta)m,}
\tag{3.2}
\]
\[
\boxed{\sigma'^2\le(1-q_h+\theta)\sigma^2\le(1/2+\theta)\sigma^2,}
\tag{3.3}
\]
and therefore
\[
\boxed{
\frac{\sigma'}{\sqrt{m'}}
\le
\sqrt{\frac{1-q_h+\theta}{1-\theta}}
\frac{\sigma}{\sqrt m}
\le
\sqrt{\frac{1/2+\theta}{1-\theta}}
\frac{\sigma}{\sqrt m}.
}
\tag{3.4}
\]
The descendant packet has the same scalar pair `B`, the same `lambda`, hence the same `mu`, and after re-orthogonalization its Schur remainder is again exactly
\[
\lambda\begin{pmatrix}m'&0\\0&0\end{pmatrix}.
\tag{3.5}
\]
If `sigma'=0`, the exact-parallel endpoint is already closed by the partner theorem with exact-slope mass at least `m'`.

### Proof

Because `q_h=a_h+b_h>=1/2`, alternative B implies
\[
b_h=q_h-a_h>q_h-\theta.
\tag{3.6}
\]
The mass identity is immediate:
\[
m'=m-u_h^2=(1-a_h)m>(1-\theta)m.
\]
For the residual variance, `r'` is the least-squares minimizer on `G'`; evaluating at the old center `r` gives
\[
\begin{aligned}
\sigma'^2
&=\min_c\sum_{i\ne h}(t_i-cu_i)^2\\
&\le\sum_{i\ne h}(t_i-r u_i)^2\\
&=\sigma^2-e_h^2
=(1-b_h)\sigma^2\\
&<(1-q_h+\theta)\sigma^2.
\end{aligned}
\]
This is (3.3), and division by (3.2) gives (3.4).

Conditioning `X_h` changes only affine terms in the remaining original variables. For the descendant packet, write
\[
S'=m'^{-1/2}\sum_{i\in G'}u_iX_i,
\qquad
R'=\sigma'^{-1}\sum_{i\in G'}(t_i-r'u_i)X_i
\]
when `sigma'>0`. The pullback from `(S',R')` to the two first-bank spectral coordinates is
\[
U_{G'}=\sqrt{m'}S',
\qquad
T_{G'}=r'\sqrt{m'}S'+\sigma'R'.
\]
Since the pre-existing Schur remainder in `(U,T)` is `lambda e_1e_1^T`, pulling it back gives exactly `lambda diag(m',0)`. Thus no small random quadratic error is discarded and `mu` is unchanged. QED.

## 4. Concrete constants: theta=1/8

Set
\[
\theta=\frac18.
\]
Then every heavy packet row gives either the partner payment
\[
\boxed{
\|p_Q\|_\infty<51.6\left(\frac{8}{\mu m}\right)^{1/3},
}
\tag{4.1}
\]
or a product-preserving original-coordinate descent satisfying
\[
\boxed{m'>\frac78m,\qquad \sigma'^2\le\frac58\sigma^2,}
\tag{4.2}
\]
\[
\boxed{
\frac{\sigma'}{\sqrt{m'}}\le\sqrt{\frac57}\frac{\sigma}{\sqrt m}
=0.845154\ldots\frac{\sigma}{\sqrt m}.
}
\tag{4.3}
\]
Equivalently the near-parallel currency improves strictly:
\[
\boxed{
\frac{m'^2}{\sigma'^2}\ge\frac{49}{40}\frac{m^2}{\sigma^2}.
}
\tag{4.4}
\]
For the standard `h=1` r26 packet, `m>=3/20`. Hence alternative A gives the actual partner inequality
\[
\boxed{
\|p_Q\|_\infty
<51.6\left(\frac{160}{3\mu}\right)^{1/3}
<194.23\,\mu^{-1/3}.
}
\tag{4.5}
\]
In particular, when `mu>=1`, this chamber is bounded by `194.23`.

The factor in (4.4) is not heuristic: `(7/8)^2/(5/8)=49/40`.

## 5. Iterated form and relation to r31

Repeat only when the re-orthogonalized descendant frame still has leverage at least `1/2` and the exact-slope payment has not fired. After `k` residual-heavy descents,
\[
\boxed{
m_k\ge(7/8)^k m_0,}
\tag{5.1}
\]
\[
\boxed{
\sigma_k^2\le(5/8)^k\sigma_0^2,
\qquad
\frac{\sigma_k}{\sqrt{m_k}}
\le(5/7)^{k/2}\frac{\sigma_0}{\sqrt{m_0}}.
}
\tag{5.2}
\]
For example, starting from the fixed `h=1` packet (`m_0>=3/20`, `sigma_0/sqrt(m_0)<=1/2`), eight residual-heavy descents still leave
\[
m_8\ge0.0515413,
\qquad
\frac{\sigma_8}{\sqrt{m_8}}\le0.130155.
\tag{5.3}
\]
At the first stage where the re-orthogonalized leverage satisfies `q_X<1/2`, r31's Pluecker aggregate becomes available verbatim after recomputing the descendant residual currencies. For example, when its mixed currency is nonzero,
\[
\|p_Q\|_\infty
\le
6\left(
\frac{4}{\mu m_k|z_{1,k}z_{2,k}|\sqrt{1-2q_{X,k}}}
\right)^{1/3},
\tag{5.4}
\]
and that branch has a continuous density. The axis versions from r31 apply similarly.

Thus the r31 failure `q_X>=1/2` is no longer a static obstruction: every such stage either pays an actual exact-slope mass or moves, using only original-coordinate conditioning, to a strictly more parallel descendant while keeping a quantitative fraction of Schur mass.

## 6. Exact remaining factor

This does **not** finish the unrestricted packet. An arbitrarily long residual-heavy tower can make the lower bound `(7/8)^k m_0` small, and the assumptions give no moment/support control that would permit treating the shrinking residual coefficient as a perturbative random error. Consequently one cannot pass to the exact-slope endpoint by continuity of the random polynomial.

The newly isolated obligation is:

`QFORM-HEAVY-RESIDUAL-TOWER-COMPILER-v1` — exploit the increasing currency `m^2/sigma^2` (or retain the peeled literal coordinates jointly) so that the constant does not lose `(7/8)^(-k/3)` through an arbitrarily long residual-heavy descent.

A valid compiler could combine the peeled literal coordinates with the grouped-hub/projected-crossing theorem, but it must keep the third smoothing resource in original-product coordinates. Conditioning the dependent `R` coordinate, an arbitrary-joint coarea cap, or a small-error argument remains invalid.

## 7. Scope and integrity

- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- The theorem is purely deterministic plus original-coordinate conditioning and therefore permits arbitrary fragmented/unbounded cap-one laws.
- No Gaussian, moment, compact-support, log-concavity, connected-support, or diagonal-basis assumption is used.
- No rotated coordinates are declared independent.
- The partner result is applied at the explicit inequality (4.5), not cited abstractly.
- Essential boundedness is proved only in alternative A and in any later r31 exit. The descent alternative is structural; it does not itself assert a density bound.
- Continuity is not proved by alternative A. r31's exact-cross exits separately yield continuity because their characteristic functions are integrable.
