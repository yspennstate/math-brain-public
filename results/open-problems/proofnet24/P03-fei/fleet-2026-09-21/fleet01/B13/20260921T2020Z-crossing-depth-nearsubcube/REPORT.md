# B13 FEI joint route — logarithmic crossing depth and near-subcube block forcing

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated mathematical/cognitive brain retrieval or receiver-context use occurred.  
**Route:** current joint fleet01/B13 interface: marginal/Han constraints that force the adaptive-crossing mechanism, continuing APPROACHES 2/13.  
**Novelty/publication priority:** unverified; no novelty claim is made.

This run changes method from the earlier singleton/product-profile calculations. The current joint FEI state says that fleet01/B18 has a curvature-refunded block restriction inequality whose missing arrow is to **force useful posterior crossings**, while fleet04/B18 supplies near-subcube derivative geometry and mixed-derivative conservation. I consume those results, plus fleet02/B12's Ellis-based support stability and fleet03/B12's newest curvature/Palm handoff, and derive an exact block-size obstruction and a positive near-subcube crossing theorem.

The key conclusion is two-sided:

* a marginal of size `p` **cannot** cross posterior majority after fewer than about `log_2(1/p)` revealed bits, no matter what Boolean function produced it;
* a pivotality support that is close to a coordinate subcube **does** create almost the maximum possible crossing when one reveals its defining block, at essentially that same logarithmic depth.

This also kills one tempting interpretation of the current singleton-crossing bank: at every corrected critical core relevant above ratio `6.13050258...`, all one-bit-induced majority crossings vanish identically. Therefore the useful A-interface must use row-adapted multi-bit blocks rather than singleton restrictions.

## 1. Setup: posterior crossing of a pivotality event

Let `Y in {0,1}` be any event on a uniform Boolean cube, with

\[
p=\Pr(Y=1)\le \frac12.
\]

For a coordinate block `A` of size `t`, let

\[
U_A=\Pr(Y=1\mid X_A),
\qquad
c(A):=\mathbb E(2U_A-1)_+.
\tag{1.1}
\]

For the FEI application `Y=eta_j` is the `j`-pivotality indicator, so `p=Inf_j(f)` and `c(A)=c_j(A)` in the fleet04/B14 and fleet01/B18 notation, provided `j notin A`.

The function `u -> (2u-1)_+` is convex. Hence if `A subseteq B`,

\[
\boxed{c(B)\ge c(A).}
\tag{1.2}
\]

Indeed `U_A=E[U_B|X_A]`, so (1.2) is conditional Jensen. Thus posterior crossing is monotone under additional information as long as the pivotal coordinate itself is not removed.

## 2. PROVED: sharp block-size cap for every posterior crossing

### Theorem B13-CROSSING-DEPTH-01

For every event `Y`, every block `A` of size `t`, and `p=Pr(Y=1)<=1/2`,

\[
\boxed{
 c(A)\le \Phi_t(p):=
 \begin{cases}
 0,&p\le2^{-(t+1)},\\
 2p-2^{-t},&2^{-(t+1)}<p<2^{-t},\\
 p,&p\ge2^{-t}.
 \end{cases}}
\tag{2.1}
\]

Consequently,

\[
\boxed{c(A)>0\quad\Longrightarrow\quad |A|\ge\left\lfloor\log_2\frac1p\right\rfloor.}
\tag{2.2}
\]

### Proof

Each atom `{X_A=z}` has probability `2^{-t}`. Therefore

\[
U_A(z)=\frac{\Pr(Y=1,X_A=z)}{2^{-t}}
\le \min\{1,2^t p\}=:M.
\tag{2.3}
\]

For `0<=u<=M`, convexity of `phi(u)=(2u-1)_+` and `phi(0)=0` give

\[
\phi(u)\le {u\over M}\phi(M).
\]

Taking expectations and using `EU_A=p`,

\[
c(A)\le {p\over M}(2M-1)_+.
\]

If `M<=1/2` this is zero; if `1/2<M<1`, substitute `M=2^t p` to obtain `2p-2^{-t}`; if `M=1`, obtain `p`. This proves (2.1). Equation (2.2) is the first regime rewritten. `QED`

The bound is sharp on dyadic block-supported events. It is a pure information/atom-size obstruction: no Boolean-specific theorem is needed.

### Immediate consequence: singleton crossings disappear below influence `1/4`

Taking `t=1`,

\[
\boxed{p\le1/4\quad\Longrightarrow\quad c(\{i\})=0\ \text{for every revealed bit }i.}
\tag{2.4}
\]

This is stronger than saying the total singleton-crossing bank is small: it says every summand is exactly zero.

## 3. PROVED: a coordinate subcube forces crossing at the earliest possible depth

Let `E={Y=1}` have density `p`, and let `Q` be a coordinate subcube with defining-coordinate set `F`, density `s=2^{-|F|}`. Put

\[
\delta=\mu(E\triangle Q).
\]

### Theorem B13-NEAR-SUBCUBE-CROSSING-02

Revealing the defining block `F` gives

\[
\boxed{c(F)\ge (p-\delta)_+.}
\tag{3.1}
\]

In particular, if

\[
\mu(E\triangle Q)\le \varepsilon p,
\qquad 0\le\varepsilon<1,
\]

then

\[
\boxed{c(F)\ge(1-\varepsilon)p.}
\tag{3.2}
\]

### Proof

Let `z_Q` be the unique `F`-atom defining `Q`. Its posterior is

\[
U_F(z_Q)=\frac{\mu(E\cap Q)}s.
\]

The contribution of this one atom to `c(F)` is

\[
s\left(2{\mu(E\cap Q)\over s}-1\right)_+
=(2\mu(E\cap Q)-s)_+.
\]

But the symmetric-difference identity

\[
\delta=p+s-2\mu(E\cap Q)
\]

makes this contribution exactly `(p-delta)_+`. All other atoms contribute nonnegatively. `QED`

For exact support `E=Q`, `p=2^{-k}` and `F` has size `k`. Theorem 2 says every block of size `<k` has zero crossing, while Theorem 3 gives `c(F)=p`. Thus coordinate-subcube pivotality supports are extremal for **earliest possible majority crossing**: the crossing switches on exactly at depth

\[
k=\log_2(1/p).
\tag{3.3}
\]

This is the structural reason singleton crossings are the wrong scale for the low-influence critical regime.

## 4. Consuming the other-account stability result: low depth defect creates an almost-maximal block crossing

The newest compatible fleet02/B12 physical-erasure report proves the exact derivative-row defect decomposition and imports Ellis's dimension-free cube-isoperimetric stability theorem. For a derivative row `g_j`, let

\[
p_j=\Pr(g_j\ne0),
\qquad
\Delta_j={d_j\over p_j}-{1\over2}\log_2{1\over p_j},
\]

and let `S_iso,j` be its support-isoperimetric slack. That report gives

\[
S_{\rm iso,j}\le4p_j\Delta_j,
\qquad
\epsilon_{\rm iso,j}:={S_{\rm iso,j}\over2p_j}\le2\Delta_j.
\tag{4.1}
\]

In the Ellis-stability regime it supplies a coordinate subcube `Q_j`, with defining set `F_j`, satisfying

\[
\delta_j:={\mu(E_j\triangle Q_j)\over p_j}
\le {2\epsilon_{\rm iso,j}\over\log_2(1/\epsilon_{\rm iso,j})}.
\tag{4.2}
\]

Applying Theorem 3 to this actual pivotality support yields the new consequence

\[
\boxed{
c_j(F_j)\ge(1-\delta_j)p_j.}
\tag{4.3}
\]

So the low-defect branch of the derivative-stability programme has a concrete A-interface output: it does not merely resemble a subcube in total variation; it carries a **real physical restriction block** which produces almost the full possible posterior-majority refund.

Also `|mu(Q_j)/p_j-1|<=delta_j`, so the block depth obeys

\[
|F_j|=\log_2(1/p_j)+O(\delta_j)
\tag{4.4}
\]

in the small-error regime (with the exact integer value determined by the dyadic subcube measure). Together with (2.2), this shows that the stability block is asymptotically at the minimum information depth at which any crossing could occur.

This consumes, rather than merely cites, fleet02/B12 `20260921T175134Z-physical-erasure-budget/REPORT.md` and the near-subcube geometry used by fleet04/B18 `20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`. The newest fleet03/B12 curvature/Palm report is compatible: its low-congestion/high-depth dichotomy acts on the same transverse sets `F_j`, while (4.3) supplies their missing block-crossing interpretation.

## 5. PROVED: transfer into the current curvature-refunded critical-core inequality

Now use fleet01/B18's corrected potential

\[
\mathcal P=\sum_i\mathfrak j(p_i),
\qquad
\mathcal F=H-\mathcal P,
\]

and an `F/J`-critical centered core of ratio

\[
\rho={\mathcal F\over J}.
\]

Its all-block theorem is

\[
\sum_{j\notin A}
(\rho+\mathfrak j'(p_j))c_j(A)
\le
\sum_{i\in A}[h_2(p_i)-\rho p_i].
\tag{5.1}
\]

For a near-subcube derivative row `j`, take `A=F_j`. Since `j notin F_j`, (4.3) and (5.1) give the new local payment

\[
\boxed{
(\rho+\mathfrak j'(p_j))(1-\delta_j)p_j
\le
\sum_{i\in F_j}[h_2(p_i)-\rho p_i].}
\tag{5.2}
\]

For `rho>2`, fleet01/B18 defines `sigma(rho)` by

\[
{h_2(\sigma)\over\sigma}=\rho,
\]

and `kappa(rho)=\mathfrak j'(\sigma(rho))`; criticality implies `p_i<=sigma(rho)`, so

\[
\boxed{
(\rho+\kappa(\rho))(1-\delta_j)p_j
\le
\sum_{i\in F_j}[h_2(p_i)-\rho p_i].}
\tag{5.3}
\]

At the currently inherited unrestricted lower-bound scale

\[
C_0=6.521845710923046575,
\qquad
\rho_0=C_0-{2\over\ln2}=3.63645562914512\ldots,
\]

the inherited calibration gives

\[
\kappa(\rho_0)=2.38851518768246\ldots.
\]

Thus for the robust relative-support threshold `delta_j<=1/16`, (5.3) has coefficient

\[
(\rho_0+\kappa(\rho_0)){15\over16}
=5.648410140775856\ldots,
\tag{5.4}
\]

so every such row forces at least `5.6484 p_j` of scalar slack into its actual transverse defining block.

### Union/Hall form

The monotonicity (1.2) gives a useful nonreuse strengthening. Let `R` be any collection of near-subcube rows such that, with

\[
A=\bigcup_{j\in R}F_j,
\]

no pivot in `R` belongs to `A`. Then every `j in R` survives and `c_j(A)>=c_j(F_j)`. Therefore (5.1) yields

\[
\boxed{
\sum_{j\in R}
(\rho+\mathfrak j'(p_j))(1-\delta_j)p_j
\le
\sum_{i\in\cup_{j\in R}F_j}[h_2(p_i)-\rho p_i].}
\tag{5.5}
\]

This is a weighted Hall-type condition for a realizable family of derivative subcubes. It is stronger than summing (5.2), because the right side counts each revealed coordinate only once. The remaining combinatorial issue is precisely to find a sufficiently large survivor family `R`, or show that failure to find one forces the dense/cyclic mixed-derivative structure toward the rigidity branch of fleet04/B18.

## 6. Decisive method kill: singleton crossing-rich arguments are vacuous at the current FEI scale

On an `F/J`-critical core, taking a singleton in the B18 inequality gives

\[
h_2(p_i)\ge\rho p_i.
\tag{6.1}
\]

The function `h_2(p)/p` is decreasing on `(0,1/2]`. At `p=1/4`,

\[
{h_2(1/4)\over1/4}=4h_2(1/4)
=3.245112497836531\ldots.
\tag{6.2}
\]

Therefore

\[
\rho>3.245112497836531\ldots
\quad\Longrightarrow\quad
p_i<1/4\ \text{for every active }i.
\]

By (2.4), this implies

\[
\boxed{c_j(\{i\})=0\quad\text{for every pair }i\ne j.}
\tag{6.3}
\]

Since `P/J<=2/ln2`, any Boolean function with

\[
{H\over J}>3.245112497836531+{2\over\ln2}
=6.130502579614458\ldots
\tag{6.4}
\]

has a corrected critical descendant in this singleton-zero regime. The current inherited lower-bound scale `6.5218457...` is already well above (6.4).

Hence fleet01/B18's global singleton-crossing budget (its equations (5.6)--(5.7)) is mathematically valid but **cannot be the crossing-rich mechanism at the high-ratio scale relevant to FEI**: every one of those singleton crossing terms is then zero. A successful crossing proof must reveal logarithmic-size, row-adapted blocks such as `F_j`.

This is a method change, not an audit: it removes a whole class of one-bit adaptive-crossing strategies and replaces it with the block theorem (4.3)--(5.5).

## 7. Exact finite calculation

`check_crossing_depth.py` was executed with exact rational arithmetic.

For every event of density at most `1/2` on cubes through dimension four and every coordinate block, it checked (2.1):

* **628,602** event/block cases;
* **0** violations;
* **91,478** equality cases.

For every event and every coordinate subcube through dimension three, it checked (3.1):

* **7,068** event/subcube cases;
* **0** violations;
* **2,704** equality cases.

The script SHA-256 is `15c3ff2ef5aa54c2be57551cf46ce042555db4c46cc84a3e763e7ea686200835`; captured stdout SHA-256 is `b09af8ea3c65997f365af7b63e0ff3ca72a7df04dc2ce5c5cc05ca88048a1acd`. The analytic proofs above do not depend on the finite check.

## 8. Remaining universal implication

This run does **not** prove FEI. The new proof chain is:

\[
\text{small derivative depth defect}
\Longrightarrow
\text{near coordinate-subcube support}
\Longrightarrow
\text{near-maximal crossing at logarithmic block depth}
\Longrightarrow
\text{transverse scalar-slack payment.}
\]

The unpaid arrow is now a concrete nonreuse/selection statement for the family of defining blocks `F_j`.

A precise next target is the following dichotomy on a high-`rho` corrected critical core:

1. find a low-defect row family `R` with substantial influence mass and `R cap (union_{j in R}F_j)=empty`, so the one-shot union inequality (5.5) pays all of them without reusing scalar slack; or
2. prove that failure of such a survivor family forces a dense/cyclic transverse dependency graph which, using the exact mixed-derivative conservation of fleet04/B18 and the fleet03/B12 high-depth-cluster dichotomy, quantitatively approaches the already solved one-point-defect rigidity endpoint.

The second alternative is where genuine Boolean integrability must enter; an arbitrary family of abstract subcubes need not satisfy mixed-derivative commutation.

**Full FEI remains OPEN / NOT PROVED.**
