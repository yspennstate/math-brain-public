# fleet03/B13 — bank-limited replacement potentials must oscillate; degree-20 smooth repairs are exactly ruled out

**Run:** `20260922T073236Z-b13-fei-r11`  
**Classification:** `AUXILIARY_ONLY / CANDIDATE_FAMILY_REFUTED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target, candidate version, and substantive peer consumption

The fresh owner control is revision `2026-09-22.2`. Its later natural-language FEI instruction supersedes the older narrow B13 interface assignment where they conflict: the current target is the equivalent all-gate potential inequality, and after the exact biased-prime obstruction the useful question is to construct or eliminate replacement potentials without reopening settled read-once or finite-sweep work.

I consume and apply the completed **other-account** result

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T071234Z-and-slack-rigidity/REPORT.md`

(blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`). Its Theorem 2.1 proves that a bounded symmetric center-zero correction cannot be free on every AND inequality, and its charged theorem proves the exact response bound

\[
R_{wit}(\psi):={57\over256}\psi(3/8)-\psi(967/2048)\le \kappa K,
\qquad \kappa<0.069645,
\tag{0.1}
\]

whenever

\[
L_{p,q}(\psi):=q\psi(p)+p\psi(q)-\psi(pq)
\ge -K M(p,q),\qquad
M(p,q)=pq(1-p)(1-q).
\tag{0.2}
\]

The source-exact prime witness itself is fleet03/B12

`20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`, blob `36fea824c2dcae8c65c3d485e5d5714899699855`.
It proves that the composition-prime 18-input Numaro gate at
\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,
\quad p_{out}=967/2048
\]
has
\[
D_{\Gamma^\dagger}<-0.0176114
\tag{0.3}
\]
for
\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p).
\]
Thus every center-preserving repair `Gamma^dagger+psi` must satisfy
\[
R_{wit}(\psi)>0.0176114.
\tag{0.4}
\]

The certified read-once potential already uses coefficient `0.01`, so the uniform AND bank that is rigorously available inside `Gamma^dagger` is
\[
A=0.268204856-0.01=0.258204856.
\tag{0.5}
\]
The exact statement attacked in this run is the following natural replacement class:

> Can a symmetric center-zero correction `psi` repair the exact biased prime witness while preserving all AND inequalities **using only the guaranteed uniform bank**, i.e. satisfying (0.2) with `K<=A`? In particular can a low-complexity smooth correction do so?

This is a sufficient AND-preservation mechanism, not a necessary description of every possible replacement: the certified base has nonuniform extra slack which a more delicate construction might exploit.

## 1. New universal shape theorem inside the guaranteed-bank class

The peer proof gives more than the scalar response bound. Its exact `q=1/2` tent-map chain gives
\[
\psi(3/8)\le {5K\over64},
\tag{1.1}
\]
and its 253-cycle/output-product argument gives
\[
\psi(967/2048)\ge -BK,
\tag{1.2}
\]
where its exact decomposition of `kappa` implies
\[
B<0.069645-{57\over256}{5\over64}
=0.05224998046875.
\tag{1.3}
\]
Combining (0.4), (1.1)--(1.3), and `K<=A` gives the strict, dimension-free necessary shape constraints
\[
\boxed{
0.0185047638099698245\ldots
<\psi(3/8)\le0.020172254375,
}
\tag{1.4}
\]
\[
\boxed{
-0.01349119868293640625
<\psi(967/2048)
<-0.01311992148681640625.
}
\tag{1.5}
\]

So a bank-limited same-center repair is forced to have a positive shoulder at `3/8`, a negative trough only `57/2048` below the center, and then return to `psi(1/2)=0`. It cannot be monotone on `[3/8,1/2]`.

For a differentiable repair, the mean-value theorem forces both
\[
\psi'(u)< -0.3254640979287346768\ldots
\quad\hbox{for some }u\in(3/8,967/2048),
\tag{1.6}
\]
and
\[
\psi'(v)>0.4713964772807017543\ldots
\quad\hbox{for some }v\in(967/2048,1/2).
\tag{1.7}
\]
For a `C^2` symmetric repair, symmetry gives `psi'(1/2)=0`, and Taylor's theorem gives points in `(3/8,1/2)` with
\[
\boxed{\psi''>2.3686097676761375438\ldots}
\tag{1.8}
\]
and
\[
\boxed{\psi''<-33.874385455118497999\ldots.}
\tag{1.9}
\]
Hence every `C^2` guaranteed-bank repair has a curvature sign change; in particular **no globally convex or globally concave center-zero correction can work**. This explains structurally why gentle shoulder/polynomial bump ideas are poor candidates, but does not itself rule out an oscillatory replacement.

## 2. Exact finite dual certificate: every polynomial through degree 20 in the bias fails

I next searched the bank inequalities for a decisive finite obstruction to a broad low-complexity family. Let
\[
s(t)=(1-2t)^2,
\qquad
\psi(t)=\sum_{j=1}^{10} c_j s(t)^j.
\tag{2.1}
\]
Every such `psi` is symmetric, center-zero, and is a polynomial of degree at most `20` in the bias `t`.

For an AND point `(p,q)`, write
\[
\ell_j(p,q)=q s(p)^j+p s(q)^j-s(pq)^j.
\]
Then the bank constraint is
\[
\sum_{j=1}^{10}c_j\ell_j(p,q)\ge -A M(p,q),
\tag{2.2}
\]
while the prime-witness response is
\[
R_{wit}(\psi)=\sum_{j=1}^{10}r_jc_j,
\quad
r_j={57\over256}s(3/8)^j-s(967/2048)^j.
\tag{2.3}
\]

An exploratory rational-grid LP identified ten constraints; the proof below no longer depends on that search. The ten exact rational AND points are

\[
\begin{array}{llll}
(1/64,1/64),&(3/64,17/32),&(5/32,35/64),&(7/16,27/32),\\
(29/64,15/32),&(29/64,3/4),&(15/32,15/32),&(15/32,47/64),\\
(61/64,61/64),&(63/64,63/64).&&
\end{array}
\tag{2.4}
\]

Exact Gaussian elimination over `Fraction` finds ten strictly positive rational multipliers `lambda_i` satisfying, for every `j=1,...,10`,
\[
r_j=-\sum_{i=1}^{10}\lambda_i\ell_j(p_i,q_i).
\tag{2.5}
\]
Multiplying (2.2) by `lambda_i` and summing therefore proves the finite Farkas/LP-dual certificate
\[
R_{wit}(\psi)
\le A\sum_i\lambda_iM(p_i,q_i)
=0.0031416522006818156524529252504331\ldots
<0.003142.
\tag{2.6}
\]
But the actual prime witness requires `R_wit>0.0176114`. Thus
\[
\boxed{
\text{no correction of the form (2.1) can repair the witness while spending only the guaranteed AND bank.}
}
\tag{2.7}
\]
The required response is more than
\[
5.6057764752501546\ldots
\tag{2.8}
\]
times the exact degree-10-in-`s` upper bound. Only the ten displayed AND inequalities are used, so (2.7) is an exact finite theorem, not an extrapolation from a grid.

`CHECKER.py` reconstructs every coefficient and dual multiplier with exact Python `Fraction` arithmetic, verifies all multipliers are positive and every identity (2.5) is exact, and proves the rational upper bounds in (2.6). `CHECK_OUTPUT.txt` records `PASS` and the numerical renderings.

## 3. Dead route, exact scope, and replacement obligation

**Exact failed claim.** A low-degree symmetric smooth correction of the form
\[
\sum_{j=1}^{10}c_j(1-2p)^{2j}
\]
can repair the current exact prime witness while preserving the proved AND theorem solely by drawing on the uniform quadratic bank `A M(p,q)`.

**Status:** **REFUTED** by the exact finite dual above.

This does **not** refute FEI, does not rule out higher-complexity or nonsmooth potentials, and does not rule out a repair which deliberately uses the detailed nonuniform positive slack of the certified read-once potential rather than only its uniform quadratic bank. It also does not turn the current refuted `Gamma^dagger` into a valid candidate.

The useful new structural conclusion is that the replacement cannot be a gentle low-degree reshaping. Even before all other prime gates are considered, a uniform-bank repair must execute a sharp positive-shoulder / negative-trough / rebound pattern near the center, with large negative curvature if smooth.

## 4. Next attack and recipient

The next attack should stay on the same all-gate target but use a genuinely more expressive object: build the **prime-gate envelope/fixed-point operator** suggested by fleet01/B18, imposing simultaneously

1. the exact AND/read-once inequalities with their **actual pointwise slack**, not only the uniform `A M` reserve;
2. the exact Numaro affine constraint
\[
{57\over256}\eta(3/8)+{465\over256}\eta(1/2)-\eta(967/2048)
\ge0.0176114199558\ldots;
\]
3. the forced oscillatory shape above as a diagnostic, not as an assumption.

A useful first falsification test is the entire one-coordinate Numaro bias line before any broader gate search. If a finite-cap fixed point survives, that is a candidate to hand to the all-gate lead; if it fails, preserve the exact conflicting gate constraints as a finite infeasibility certificate.

**Primary next recipient:** `fleet03/B18` (all-gate/B lead).  
**Secondary recipients:** `fleet01/B18` (replacement-potential pivot) and `fleet02/B17` (whose charged AND theorem is consumed here).

**Implication to full FEI:** this run eliminates a substantial, rigorously specified replacement family and proves a new necessary shape theorem, but supplies no universal finite-cap `Gamma`. Therefore full uniform-cube FEI remains **OPEN / NOT PROVED**.
