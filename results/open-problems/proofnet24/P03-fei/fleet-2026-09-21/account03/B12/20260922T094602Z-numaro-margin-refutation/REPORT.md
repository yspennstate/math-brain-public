# account03/B12 — source-exact Numaro margin refutes AND extremality

**Run:** `20260922T094602Z-account03-B12-7aecd43a`  
**Classification:** `CANDIDATE_REFUTED / TARGET-LEVEL EXTREMALITY REFUTATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Live target and mechanism change

The current owner control asks every FEI worker to converge on the all-gate formulation.  With the read-once value-iteration base potential `Gamma_0` at `C_0=6.4548`, define

\[
D_{\Gamma}(G;p)=\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u),
\]

and, when the Poincare denominator is positive,

\[
Q_G(p):=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out}),
\qquad
c_G(p):=-\frac{D_{\Gamma_0}(G;p)}{Q_G(p)}.
\tag{0.1}
\]

The owner explicitly proposed two alternatives: prove that the AND/decomposable gate is extremal for this margin, or falsify that statement by finding a genuine gate and bias with `c_G` above the AND margin.  This run executes the second alternative.  It is materially different from the preceding safe-direction constructions.

The phrase “minimum” in the owner message is inconsistent with its explicit falsification criterion “find a gate with `c_G` above the AND's.”  Here “AND extremality” means exactly that no gate asks for a larger positive margin than AND.

## 1. Named other-account result consumed

This run consumes the complete source-bound result

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0912Z-tilted-quartic-strong-prime-refutation/REPORT.md`

(blob `10493748314dbe8071acefcf62c5befcf4aacfab`).

That report uses the exact composition-prime 18-input Numaro truth table and the product bias

\[
p_1=\frac{223}{456},\qquad p_2=\cdots=p_{18}=\frac12,
\qquad p_{\rm out}=\frac{1019}{2048},
\tag{1.1}
\]

with normalized pivotal probabilities

\[
\alpha_1=\frac{57}{256},
\qquad
\sum_{i=2}^{18}\alpha_i=\frac{465}{256},
\qquad
\alpha_i=\frac{\operatorname{It}_i}{V_{p_i}}.
\tag{1.2}
\]

For the shifted potential

\[
\Gamma^\dagger(u)=\Gamma_0(u)+a\,u(1-u),
\qquad a=0.268204856=\frac{33525607}{125000000},
\tag{1.3}
\]

it proves the rigorous defect bound

\[
\boxed{D_{\Gamma^\dagger}(G;p)<-\frac{38023}{10^6}.}
\tag{1.4}
\]

I apply that theorem directly to the owner-normalized margin `c_G`; it is not merely cited.

## 2. Exact quadratic-shift identity

Put `q(u)=u(1-u)=V_u/4`.  Because the all-gate defect is affine in the potential,

\[
D_{\Gamma_0+a q}(G;p)
=D_{\Gamma_0}(G;p)+a\left(\sum_i\alpha_i q(p_i)-q(p_{\rm out})\right).
\]

But

\[
\sum_i\alpha_i q(p_i)
=\sum_i\frac{\operatorname{It}_i}{V_{p_i}}\frac{V_{p_i}}4
=\frac{I(G;p)}4.
\]

Hence the parenthesis is exactly the denominator in (0.1):

\[
\boxed{D_{\Gamma^\dagger}=D_{\Gamma_0}+aQ_G.}
\tag{2.1}
\]

Therefore, whenever `Q_G>0`,

\[
\boxed{c_G=a-\frac{D_{\Gamma^\dagger}}{Q_G}.}
\tag{2.2}
\]

This identity turns any certified defect of a quadratic-shifted potential into the owner’s directly comparable margin.

## 3. Exact Numaro denominator and margin lower bound

Using only the exact data (1.1)-(1.2),

\[
\begin{aligned}
Q_G
&=\frac{57}{256}\frac{223}{456}\left(1-\frac{223}{456}\right)
 +\frac{465}{256}\frac14
 -\frac{1019}{2048}\left(1-\frac{1019}{2048}\right)\\[1mm]
&=\boxed{\frac{62098577}{239075328}}
 =0.25974481565910473\ldots>0.
\end{aligned}
\tag{3.1}
\]

Combining (1.4), (2.2) and (3.1),

\[
\begin{aligned}
c_G
&>\frac{33525607}{125000000}
 +\frac{38023}{10^6}\frac{239075328}{62098577}\\[1mm]
&=\boxed{\frac{3218187637329239}{7762322125000000}}\\[1mm]
&=\boxed{0.4145908383477759\ldots}. 
\end{aligned}
\tag{3.2}
\]

Thus this genuine composition-prime Boolean gate asks for a strictly positive owner-normalized margin larger than `0.41459`.

## 4. Rigorous comparison with every two-input AND bias

The certified read-once theorem in

`proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/REPORT.md`

proves the two-input AND inequality for every interior bias pair with the potential

\[
\Gamma_{\rm cert}(u)=\Gamma_0(u)+0.01\,u(1-u).
\]

Equivalently,

\[
D_{\Gamma_0}(\mathrm{AND};p,q)+0.01\,Q_{\mathrm{AND}}(p,q)\ge0
\]

for all `p,q in (0,1)`.  Whenever `Q_AND>0`, this gives the rigorous global bound

\[
\boxed{c_{\mathrm{AND}}(p,q)\le0.01.}
\tag{4.1}
\]

At a degenerate point with `Q_AND=0`, there is no finite positive ratio exceeding this bound to compare.

Therefore (3.2) and (4.1) imply

\[
\boxed{
c_G(\text{Numaro};223/456,1/2,\ldots,1/2)
>0.4145908383
>0.01
\ge \sup_{p,q}c_{\mathrm{AND}}(p,q).
}
\tag{4.2}
\]

The certified gap is at least

\[
0.4045908383477758\ldots .
\]

This is not a grid comparison: the Numaro lower bound uses the peer's rigorous rational defect certificate, and the AND upper bound uses the existing all-bias interval certificate.

## 5. Exact claim status

**Candidate/version attacked:** `OWNER-CG-EXTREMALITY-v1`, namely the explicit operational claim that the owner-normalized `c_G` is never larger for a genuine gate than for the AND/decomposable extremizer.

**Prior missing implication:** prove the AND/decomposable extremality of `c_G`, or find one genuine Boolean gate and product bias with `c_G` above AND's.

**New result:** the stated extremality criterion is **REFUTED**.  The source-certified composition-prime 18-input Numaro gate at (1.1) has `c_G>0.4145908383`, while the certified read-once theorem gives `c_AND<=0.01` for every two-input AND bias.

**Replacement obligation:** the fleet must not use AND extremality of the read-once base potential as the universal closing step.  The next full-FEI candidate needs either a different symmetric potential shape that pays the Numaro prime gate efficiently, or a new gate theorem whose extremizer is allowed to be genuinely prime.  Any proposed replacement should be tested first against the same `223/456` Numaro witness.

**Consumed peer artifact:** account01/B16 `20260922T0912Z-tilted-quartic-strong-prime-refutation`, applied through the exact quadratic-shift identity (2.1)-(2.2).

**Next recipient:** `account03/B18`, the current B lead/integrator; secondary recipient `account01/B16` because its certified defect becomes a direct owner-margin obstruction.

**Implication to full FEI:** one of the two live owner alternatives is settled in the falsification direction for the stated `Gamma_0` margin.  This does **not** refute FEI and does **not** by itself lower-bound the optimal FEI constant, because another potential may behave differently.  Full unrestricted FEI remains **OPEN / NOT PROVED**.

For orientation only, a pure quadratic repair of this same `Gamma_0` would need center

\[
6.4548+\frac{c_G}{4}>6.558447709586944,
\]

but this is a barrier for that potential ray, not a universal lower bound on FEI.

## 6. Verification and scope

`CHECKER.py` uses only exact `Fraction` arithmetic to recompute `Q_G`, the rational lower bound (3.2), its gap over the rigorous AND certificate bound `0.01`, and the corresponding quadratic-ray center.  It does not re-audit the peer truth table or repeat the read-once interval sweep.

Scoped privacy/secret review: this package contains only FEI formulas, rational constants and repository-relative scientific references.  It contains no credentials, scheduler identifiers, machine paths, private transcripts, email/Drive material, unrelated private data, benchmark gold, paid model/API/Codex calls, remote workflow dispatch or public-posting action.
