# B16 — two-selector dual barrier for universally gate-safe even sextic repairs

**Classification:** `AUXILIARY_ONLY / EXACT_REPLACEMENT_CLASS_BARRIER`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Version and source-current assignment

The active owner control is revision `2026-09-22.2`. Its live natural-language FEI message supersedes the older Campaign-C-only prompt and converges FEI workers on the all-gate formulation: find one finite-cap symmetric potential satisfying the gate inequality for every Boolean gate and every product bias, or falsify the current replacement mechanism. I therefore do **not** revive the retired all-Boolean positive half-band current bound.

This run attacks replacement version

`SAFE-EVEN-SEXTIC-REPAIR-BARRIER-v1`.

The old missing implication is: after the exact source candidate `TILTED-QUARTIC-GATE-REPAIR-v1` failed, can a better *universally gate-safe additive polynomial direction* repair the same strong composition-prime Numaro witness substantially more efficiently at the potential centre, while preserving every already-paid gate inequality?

## 1. Named cross-account result consumed

This run consumes fleet01/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260922T0912Z-tilted-quartic-strong-prime-refutation/REPORT.md`

(blob `10493748314dbe8071acefcf62c5befcf4aacfab`). That report gives the exact strong composition-prime 18-input Numaro witness at

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}={1\over2},
\qquad p_{\rm out}={1019\over2048},
\]

with pivotal data

\[
\alpha_1={57\over256},\qquad
\sum_{i=2}^{18}\alpha_i={465\over256},
\]

and the rigorous source defect

\[
D_{\Gamma^\dagger}< -{38023\over10^6},
\qquad \Gamma^\dagger(1/2)=6.521851214.
\tag{1.1}
\]

It also refutes the previously proposed scale of the fleet03/B12 universally-safe tilted quartic. The present run applies this exact witness to the entire endpoint-zero symmetric even polynomial repair cone through degree six.

## 2. Exact class and the witness-payment functional

Let a repair direction be written in mean coordinates as

\[
\eta(u)=F(1-2u).
\]

Consider every symmetric endpoint-zero even polynomial direction of degree at most six with positive centre value. After positive rescaling, every such direction is uniquely

\[
F_{A,B}(m)=(1-m^2)(1+A m^2+B m^4),
\qquad F_{A,B}(0)=1.
\tag{2.1}
\]

Call it **universally gate-safe** when for every Boolean gate and every product bias,

\[
\sum_i \alpha_i F(m_i)-F(\mu)\ge0,
\qquad
\alpha_i={\operatorname{It}_i\over V_{p_i}},
\quad m_i=1-2p_i,
\quad \mu=\mathbb E G.
\tag{2.2}
\]

This is exactly the condition that adding a nonnegative multiple of `eta` can never decrease any gate defect.

For the strong Numaro witness, set

\[
m_1={5\over228},\qquad m_{\rm out}={5\over1024}.
\]

Writing the basis

\[
b_0=(1-m^2),\quad b_1=(1-m^2)m^2,\quad b_2=(1-m^2)m^4,
\]

the amount paid by `F_{A,B}` per unit centre is the affine functional

\[
R(A,B)=O_0+O_1A+O_2B,
\tag{2.3}
\]

where exact arithmetic gives

\[
O_0={62098577\over59768832},
\]

\[
O_1={16938576520025\over203621856882720768},
\]

\[
O_2={35311637412221110625\over693703711666428733273669632}.
\tag{2.4}
\]

## 3. Two genuine Boolean selector constraints

The universal quantifier in (2.2) already imposes strong linear restrictions on `(A,B)` from two actual two-input selector gates.

For a Shannon split with selector bias `t`, child means `a,b`, `q=1-t`, parent mean `c=qa+tb`, and disagreement `delta`, gate safety requires

\[
qF(a)+tF(b)-F(c)+\delta F(q-t)\ge0.
\tag{3.1}
\]

When one child is constant and the other is a one-variable Boolean gate, the lower Booleanity value

\[
\delta={|a-b|\over2}
\]

is attained exactly. Hence the following are source-valid Boolean gates, not relaxed moment configurations.

### Selector 1

Take

\[
(a,b,t)=\left(-1,{31\over32},{31\over32}\right).
\]

Equation (3.1) becomes

\[
C_{10}+C_{11}A+C_{12}B\ge0,
\tag{3.2}
\]

with

\[
C_{10}={1953\over1048576},
\quad
C_{11}={16568379009\over1099511627776},
\quad
C_{12}={28487677659001281\over1152921504606846976}.
\tag{3.3}
\]

### Selector 2

Take

\[
(a,b,t)=\left({3\over32},1,{17\over32}\right).
\]

Then

\[
C_{20}+C_{21}A+C_{22}B\ge0,
\tag{3.4}
\]

where

\[
C_{20}={258825\over1048576},
\quad
C_{21}=-{236990264175\over1099511627776},
\quad
C_{22}=-{84397791851807175\over1152921504606846976}.
\tag{3.5}
\]

Every universally gate-safe even sextic must satisfy both (3.2) and (3.4).

## 4. Exact dual certificate: the whole degree-six cone has almost no extra efficiency

Define

\[
\lambda_1=
{106624992234261574365420550\over74071884319574458230463049577}>0,
\]

\[
\lambda_2=
{2054409844073332992321877\over4222157355711667002846373389}>0.
\tag{4.1}
\]

Direct exact arithmetic verifies

\[
O_1=-\lambda_1 C_{11}-\lambda_2 C_{21},
\qquad
O_2=-\lambda_1 C_{12}-\lambda_2 C_{22}.
\tag{4.2}
\]

Therefore (3.2)-(3.4) imply

\[
\begin{aligned}
R(A,B)
&=O_0+O_1A+O_2B\\
&\le O_0+\lambda_1C_{10}+\lambda_2C_{20}\\
&=\boxed{
{117399595402058107229743783687\over
112981776538836095856994516992}
}\\
&=\boxed{1.03910204812280882\ldots}.
\end{aligned}
\tag{4.3}
\]

This is a rigorous linear-programming dual certificate, not a numerical optimization. Equality in the two necessary selector constraints occurs at

\[
A={212299128242176\over143773227712611}
=1.4766249017\ldots,
\]

\[
B=-{39145912483708928\over40112730531818469}
=-0.9758974761\ldots,
\tag{4.4}
\]

but no claim is made that this equality polynomial is itself universally gate-safe; (4.3) is only a necessary-cone upper bound, which is all that is needed for the barrier.

### Consequence for the strong Numaro witness

Since the inherited source defect has magnitude greater than `38023/10^6`, every universally gate-safe endpoint-zero symmetric even polynomial repair of degree at most six must add centre value strictly larger than

\[
{38023/10^6\over R_{\max}}
=
{67123532645877576137039101868544\over
1834368678157157925464746620109375}
=0.0365921711622939211\ldots .
\tag{4.5}
\]

Thus every repair of the fixed source `Gamma^dagger` within this entire class has

\[
\boxed{
\Gamma(1/2)>6.55844338516229364\ldots .
}
\tag{4.6}
\]

This is **not** a lower bound on the true FEI constant. It is a barrier only for additive universally gate-safe even polynomial repairs through degree six above this fixed source potential.

## 5. The proved tilted quartic is already essentially optimal inside degree six

Fleet03/B12 proved universal safety of

\[
F_*(m)=1-m^4-{1\over36}(1-m^2)^2.
\]

At the strong witness its centre-normalized efficiency is exactly

\[
R_*=
{1481037552510921721\over1425352998179045376}
=1.03906720258281005\ldots .
\tag{5.1}
\]

Compared with the absolute necessary-cone ceiling (4.3), the relative gap is only

\[
{R_{\max}-R_*\over R_{\max}}
=3.3534280932\times10^{-5}.
\tag{5.2}
\]

So optimizing the degree-four coefficient, or even passing to an arbitrary even sextic while insisting on universal gate safety, can improve this witness-payment/centre ratio by **at most about 0.00336 percent**. The strong witness is not waiting for a small low-degree coefficient optimization.

There is also a sharper exact obstruction inside the tilted-quartic one-parameter family. Applying the already-used genuine selector `(a,b,t)=(1/5,1,3/5)` gives

\[
S_2={144\over625}
\quad\hbox{for }1-m^2,
\qquad
S_4={4896\over390625}
\quad\hbox{for }1-m^4.
\]

For

\[
F_\theta=(1+\theta)(1-m^4)-2\theta(1-m^2),
\]

universal safety therefore necessarily gives

\[
\boxed{\theta\le {17\over608}=0.02796052631578947\ldots .}
\tag{5.3}
\]

Together with the fleet03/B12 proof at `theta=1/36`, this improves its previous bracket to

\[
\boxed{
{1\over36}\le\theta_*\le{17\over608}<{1\over35}.
}
\tag{5.4}
\]

## 6. Attempted refutation and dead route

A natural response to the refuted tilted-quartic scale was to optimize the safe polynomial shape. The exact dual certificate above shows that this is a **dead route for meaningful centre-efficiency improvement through degree six**: even the whole necessary cone buys only `3.35e-5` relative efficiency over the already-proved `theta=1/36` direction on the decisive strong witness.

This does **not** refute the possibility that a larger scale of the existing safe direction, or another finite-cap potential, proves FEI. Full FEI only needs a finite constant, not the smallest one. It instead removes a misleading optimization subproblem and identifies what a genuinely different replacement must change.

## 7. Old/new implication and replacement obligation

**Old missing implication.** Repair the strong composition-prime Numaro gate while preserving every gate already paid by `Gamma^dagger`, then prove the universal all-prime-gate inequality.

**New proved result.** Every additive universally gate-safe endpoint-zero symmetric even polynomial direction of degree at most six has strong-witness payment/centre efficiency at most `1.03910204812280882...`; the existing proved tilted quartic already reaches `1.03906720258281005...`. Therefore no degree-6-or-lower safe-polynomial shape can materially lower the approximately `6.55844` centre forced by this fixed-source repair strategy.

**Replacement obligation.** Do not spend another run optimizing degree-four or degree-six safe coefficients. A materially different continuation must use at least one of: a higher/non-polynomial Bellman-shaped universally safe direction with demonstrably better strong-witness efficiency; a different source potential whose prime defect is smaller; or a direct proof that a finite larger scale repairs **all** composition-prime gates. Any replacement must test the `223/456` Numaro bias immediately.

**Consumed peer artifact.** fleet01/B16 `20260922T0912Z-tilted-quartic-strong-prime-refutation`, blob `10493748314dbe8071acefcf62c5befcf4aacfab`.

**Applied to claim.** The peer's exact Numaro defect and pivotal probabilities were inserted into the complete degree-6 repair functional and dualized against two exact Boolean selector constraints.

**Next recipient.** fleet03/B18, with fleet01/B16 as the prime-witness adversary and fleet04/B17/fleet03-B12 as safe-direction sources.

**Full-FEI implication.** None yet at target level: the universal prime-gate inequality remains OPEN. This result removes a low-degree replacement subroute and sharpens the shape requirement for the next candidate; it does not prove or refute FEI.

## 8. Verification and operational status

`CHECKER.py` is standard-library exact `Fraction` arithmetic. It reconstructs both selector inequalities, the strong-witness objective, the positive dual multipliers, the exact optimum upper bound, the centre barrier, the tilted-quartic comparison and the sharpened `17/608` bracket. `CHECKER_OUTPUT.txt` reports `PASS`.

The canonical shared-brain current-hour login write was attempted once before substantive mathematics and was blocked by platform safety. It was not retried or bypassed. Accordingly no canonical brain start/finish/receipt or shared-brain handoff is claimed for this invocation. The scientific package is private mathematical repository storage only. No authenticated brain retrieval or receiver-context use occurred, so the run remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler repair, schedule mutation, notification mutation, cross-account action, email, Drive action, public posting, workflow dispatch, paid model/API, Codex, credential access or unrelated private-data access was performed.
