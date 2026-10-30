# fleet04/B12 — unequal-data MUX cross-deficit obstruction

**Outcome:** `ESSENTIAL_REDUCTION_APPLIED / PRIME_MUX_CORRIDOR_NARROWED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and exact dependencies

The later owner control supersedes the old row-coding route and fixes the all-gate potential problem. For a Boolean gate `G` at product biases `p`, write

\[
V_u=4u(1-u),\qquad A_\Gamma(u)=\Gamma(u)+h_2(V_u),
\]
\[
D_\Gamma(G;p)=\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}A_\Gamma(p_i)
-\Gamma(p_{\rm out})-\widetilde H_G(p).
\]
A symmetric nonnegative finite-cap `Gamma` with `D_Gamma>=0` for every gate is equivalent to full FEI.

This run consumes two exact completed peer results.

1. **fleet02/B13, `20260922T032411Z-gate-block-critical-core`.** For every physical input block `A`,
   \[
   D_\Gamma(G)=\mathbb E_zD_\Gamma(G_z)+R_{\Gamma,A}(G),
   \]
   with the actual product branch law and no discarded child slack. Therefore any minimum-essential-arity counterexample is composition-prime and has `R_{Gamma,A}<0` for every nonempty proper physical block. This is the exact implication used below.

2. **fleet01/B18, `20260922T0325Z-addressing-star-cdagger`.** It fixes
   \[
   C^\dagger=6.521851214,\qquad
   a^\dagger=0.268204856,
   \qquad
   \Gamma^\dagger=\Gamma_0+a^\dagger u(1-u),
   \]
   and proves the equal-data MUX/common-data addressing family for this same candidate. Thus the nearest unclosed MUX case is `q_0 != q_1`.

The inherited read-once certificate proves every AND/OR gate after adding the smaller quadratic margin
\[
c_{\rm RO}=0.01
\]
to the same base candidate `Gamma_0`. Equivalently,
\[
D_{\Gamma_0}(\mathrm{AND};x,y)\ge -c_{\rm RO}P_{\rm AND}(x,y),
\qquad
P_{\rm AND}(x,y)=x(1-x)y(1-y).
\tag{0.1}
\]

The older fleet04/B18 mixed-curvature integrability identity remains preserved. Nothing here assumes or implies `sum_k d_k=O(J)`.

## 1. Exact biased spectrum of the unequal-data MUX

Let `M=MUX(A;D_0,D_1)` select `D_0` when `A=0` and `D_1` when `A=1`, with independent true-biases
\[
p=\Pr(A=1),\qquad q_0=\Pr(D_0=1),\qquad q_1=\Pr(D_1=1).
\]
Put
\[
r=(1-p)q_0+pq_1,
\qquad
d=q_0+q_1-2q_0q_1.
\]
The six nonzero squared biased-Fourier coefficients are
\[
\begin{array}{c|c}
S&w_S\\ \hline
\varnothing&(1-2r)^2\\
\{D_0\}&(1-p)^2V_{q_0}\\
\{D_1\}&p^2V_{q_1}\\
\{A\}&V_p(q_1-q_0)^2\\
\{A,D_0\}&p(1-p)V_{q_0}\\
\{A,D_1\}&p(1-p)V_{q_1}.
\end{array}
\tag{1.1}
\]
They sum to one. Hence the biased influences are exactly
\[
\operatorname{It}_A=V_p d,
\qquad
\operatorname{It}_{D_0}=(1-p)V_{q_0},
\qquad
\operatorname{It}_{D_1}=pV_{q_1}.
\tag{1.2}
\]

The Poincare currency controlling a quadratic lift is
\[
P_M:=\frac{I(M;p,q_0,q_1)}4-r(1-r).
\]
A cancellation that is not visible in `d` gives the exact identity
\[
\boxed{
P_M=p(1-p)\bigl[q_0(1-q_0)+q_1(1-q_1)\bigr]
=Q_0+Q_1,
}
\tag{1.3}
\]
where
\[
\boxed{
Q_0=\frac{V_pV_{q_0}}{16},\qquad
Q_1=\frac{V_pV_{q_1}}{16}.
}
\tag{1.4}
\]
Thus **data asymmetry creates no extra quadratic currency**: the complete currency is exactly the sum of the two data-variance currencies.

## 2. Exact physical-block split

Reveal `D_0`. If `D_0=0`, the child is `AND(A,D_1)`. If `D_0=1`, after genuine NPN input/output complementation the child is `AND(A,not D_1)`. Therefore
\[
D_\Gamma(M)
=(1-q_0)D_\Gamma(\mathrm{AND};p,q_1)
+q_0D_\Gamma(\mathrm{AND};p,1-q_1)
+R_0^\Gamma.
\tag{2.1}
\]
Both child branches have the same Poincare currency
\[
P_{\rm child,0}=\frac{V_pV_{q_1}}{16}=Q_1,
\]
so the exact block currency is
\[
\boxed{P_M-\mathbb E P_{\rm child,0}=Q_0.}
\tag{2.2}
\]
Similarly, revealing `D_1` gives
\[
D_\Gamma(M)
=(1-q_1)D_\Gamma(\mathrm{AND};1-p,q_0)
+q_1D_\Gamma(\mathrm{AND};1-p,1-q_0)
+R_1^\Gamma,
\tag{2.3}
\]
with
\[
\boxed{P_M-\mathbb E P_{\rm child,1}=Q_1.}
\tag{2.4}
\]
Revealing the selector `A` leaves the two unary data dictators, whose gate slack and Poincare currency are both zero. Hence the selector residual is simply the parent slack itself.

For reference, if `H_M` denotes the entropy of the six weights in (1.1) and
\[
H_\wedge(x,y)=H\!\left((1-2xy)^2,V_x y^2,V_yx^2,V_xV_y/4\right),
\]
then the two data residuals are the explicit scalar functions
\[
\begin{aligned}
R_0^\Gamma={}&(1-p)A_\Gamma(q_0)-\Gamma(r)
 +(1-q_0)\Gamma(pq_1)+q_0\Gamma(p(1-q_1))\\
&-H_M+(1-q_0)H_\wedge(p,q_1)+q_0H_\wedge(p,1-q_1),
\end{aligned}
\tag{2.5}
\]
\[
\begin{aligned}
R_1^\Gamma={}&pA_\Gamma(q_1)-\Gamma(r)
 +(1-q_1)\Gamma((1-p)q_0)+q_1\Gamma((1-p)(1-q_0))\\
&-H_M+(1-q_1)H_\wedge(1-p,q_0)+q_1H_\wedge(1-p,1-q_0).
\end{aligned}
\tag{2.6}
\]
There is no ambient coordinate label or dimension term anywhere in (2.5)-(2.6).

## 3. New quantitative obstruction for any MUX counterexample

Let
\[
\Gamma^\dagger=\Gamma_0+a^\dagger u(1-u),
\qquad a^\dagger=0.268204856.
\]
For every gate,
\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger P.
\tag{3.1}
\]
By (2.2)-(2.4), the corresponding residual lift is exactly
\[
R_0^\dagger=R_0^0+a^\dagger Q_0,
\qquad
R_1^\dagger=R_1^0+a^\dagger Q_1.
\tag{3.2}
\]

### Theorem 3.1 — cross-deficit forcing

If an interior unequal-data MUX violates the fixed candidate,
\[
D_{\Gamma^\dagger}(M;p,q_0,q_1)<0,
\tag{3.3}
\]
then
\[
\boxed{
R_0^\dagger<-(a^\dagger-c_{\rm RO})Q_1,
\qquad
R_1^\dagger<-(a^\dagger-c_{\rm RO})Q_0,
}
\tag{3.4}
\]
and therefore
\[
\boxed{
R_0^\dagger+R_1^\dagger
<-0.258204856\,P_M.
}
\tag{3.5}
\]

#### Proof

From (3.3) and (3.1),
\[
D_{\Gamma_0}(M)<-a^\dagger(Q_0+Q_1).
\tag{3.6}
\]
The two `D_0`-restricted children are AND/OR gates with common Poincare currency `Q_1`. The certified read-once margin (0.1) therefore gives
\[
(1-q_0)D_{\Gamma_0}(\mathrm{AND};p,q_1)
+q_0D_{\Gamma_0}(\mathrm{AND};p,1-q_1)
\ge -c_{\rm RO}Q_1.
\tag{3.7}
\]
Subtract (3.7) from (3.6) using (2.1):
\[
R_0^0<-a^\dagger Q_0-(a^\dagger-c_{\rm RO})Q_1.
\]
Add the exact lift `a^dagger Q_0` from (3.2) to obtain the first inequality in (3.4). The second is symmetric, using the `D_1` split. Adding them and using `P_M=Q_0+Q_1` proves (3.5). QED.

Numerically,
\[
\boxed{a^\dagger-c_{\rm RO}=0.258204856.}
\]
So a putative prime-MUX counterexample cannot merely make both physical data splits slightly bad. Each split must overspend by at least **25.8204856% of the other data coordinate's entire quadratic currency**.

Boundary cases are already paid: if `p` is deterministic, MUX is a unary data gate; if `q_0` or `q_1` is deterministic, the gate reduces by NPN to an AND/OR gate. The diagonal `q_0=q_1` is already paid by the fleet01/B18 star theorem. Thus a new MUX counterexample would have to be genuinely interior and genuinely unequal-data.

## 4. A three-scalar closure target

The theorem turns the entire unequal-data MUX class into one explicit candidate-specific scalar inequality. It is sufficient to prove
\[
\boxed{
R_0^{\Gamma^\dagger}(p,q_0,q_1)
+R_1^{\Gamma^\dagger}(p,q_0,q_1)
\ge -0.258204856\,P_M(p,q_0,q_1)
}
\tag{4.1}
\]
for all interior `p,q_0,q_1`. Equations (1.1), (1.3), (2.5), and (2.6) make (4.1) a direct three-real-variable inequality involving only the committed one-variable potential and four-/six-atom Shannon entropies. If (4.1) holds, (3.5) rules out every unequal-data MUX counterexample. Together with the already-proved equal-data MUX result, this closes the full one-selector MUX gate class for the fixed `Gamma^dagger` candidate.

This is strictly narrower than re-sweeping all arity-three NPN gates and retains the exact child slack that the owner message says the naive Shannon induction lost. It also gives a quantitative falsification criterion: any counterexample to (4.1) below the threshold is not yet a counterexample to the gate candidate; a true MUX counterexample must cross the strict threshold in (3.5).

## 5. Exact checker

`CHECKER.py` uses exact rational arithmetic on 343 interior bias triples to verify, independently of any FEI claim:

- the six spectral weights sum to one;
- all three biased-influence formulas in (1.2);
- the exact Poincare identity `P_M=Q_0+Q_1`;
- the child/block currency identities (2.2) and (2.4);
- both displayed residual formulas against the exact block decomposition for an arbitrary nonlinear symmetric test potential;
- the quadratic-lift covariance `D -> D+aP`, `R_i -> R_i+aQ_i`.

The maximum floating discrepancy in the residual-formula cross-check was `4.996e-16`; all rational identities were exact. This finite grid is only an implementation check of the algebra. The theorem itself is the symbolic argument above.

Checker SHA-256: `97df45fa5d1003d293bd7fe0909e5ca551ac3df8c48bb69d059adab9131211b2`.  
Output SHA-256: `b0f0ad8d90945832ece94b592fdd3d6655d4744a03a9987fb130cded53c05ed5`.

## 6. Honest status and next implication

**Full FEI remains OPEN / NOT PROVED.** The universal all-prime-gate implication remains open. This run makes target-level progress only on the nearest explicit prime family named by the current candidate work: unequal-data MUX.

The next decisive step on this exact route is now not another gate enumeration. It is to prove or falsify (4.1) for the committed `Gamma^dagger`. Because the residuals and currency are explicit, this is suitable either for a rigorous interval certificate or for an analytic convexity/KL argument. A violation of (4.1) must then be checked against the stronger parent condition (3.3) before it can count as a candidate counterexample.

No benchmark material, email/Drive, paid or remote compute, workflow dispatch, unrelated private data, scheduler mutation, notification enabling, or production-key material was used.
