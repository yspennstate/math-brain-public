# B18 — the recursive shared-graft obstruction has a finite limiting cap

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were used directly, but no authenticated installed brain retrieval/context was used.

## 1. Exact candidate chain and the first missing implication

The live all-gate formulation is the following. For a symmetric nonnegative potential \(\Gamma\), define the gate slack

\[
D_\Gamma(G;p)
=\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
 -\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

If \(D_\Gamma(G;p)\ge0\) for every Boolean gate of every arity and every product bias, and \(\Gamma(1/2)\le C\), then the gate reformulation gives full FEI with constant \(C\).

The exact other-account result consumed in this run is fleet03/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`,
report blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`.

It applies the source-valid recurrence from the preceding fleet01/B18 report twice further and certifies genuine balanced monotone Boolean gates \(F_3,F_4\). In particular

\[
R_4:=\frac{H(F_4)}{I(F_4)-1}
\in[L_4,U_4],
\]
with

\[
L_4=
6.5218509485644448965490881329959858569477358114202361,
\]
\[
U_4=
6.5218509485644448965496895824490791318643557898359042.
\tag{1.1}
\]

The same peer report explicitly leaves one missing inference: prove a tail theorem for the recursive shared-core transformation before freezing another scalar center at a finite-stage lower bound. This run closes that inference.

The second exact peer input is fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`.

It proves that for disjoint gate composition, both \(D_\Gamma\) and the Poincare currency

\[
M(G;p)=\frac14\left(\sum_i\operatorname{It}_i(G;p)-V_{p_{\rm out}}\right)
\]
compose with the same nonnegative weights. Hence for any scalar quadratic lift, corrected slack also composes, and it is enough to prove the gate inequality on composition-prime gates.

Thus the compact conditional end-to-end argument after this run is:

1. choose one explicit center \(C_*\) above every member of the recursive shared-graft obstruction family;
2. form the corresponding scalar lift \(\Gamma_*\) of the read-once potential;
3. prove \(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime Boolean gate \(P\), every arity, and every interior product bias;
4. the cocycle gives the inequality for every gate;
5. the all-gate reformulation then gives \(H(f)\le C_*I(f)\) for every Boolean \(f\).

Only step 3 remains unproved after the tail analysis below. No auxiliary result below is presented as a proof of FEI.

## 2. Exact recursive obstruction

Let \(F_t\) denote the recursively grafted balanced monotone gates in the inherited source-valid construction. Put

\[
R_t=\frac{H(F_t)}{I(F_t)-1},\qquad
c_t=\text{the designated singleton Fourier coefficient of }F_t.
\]

The inherited exact recurrence is

\[
c_{t+1}=\frac{57}{256}+\frac{c_t^4}{256},
\tag{2.1}
\]

\[
I_{t+1}=\frac{513}{256}+\frac9{256}I_t^4,
\tag{2.2}
\]

and

\[
R_{t+1}-R_t=
\frac{K(c_t^4)-\frac{133}{128}R_t}
     {\frac9{256}I_t^4+\frac{257}{256}},
\tag{2.3}
\]
where

\[
K(b)=H_{\rm core}(b)+\frac9{256}
\left[-\phi(b^2)+16(1-b^2)\right],
\qquad \phi(x)=-x\log_2x.
\]

Define

\[
Q(c)=\frac{128}{133}K(c^4),
\qquad
\lambda_t=\frac{133/128}{I_{t+1}-1}.
\]

Then (2.3) becomes the exact affine recursion

\[
\boxed{R_{t+1}=(1-\lambda_t)R_t+\lambda_t Q(c_t).}
\tag{2.4}
\]

This form separates the moving target \(Q(c_t)\) from the rapidly vanishing update weight.

## 3. The singleton recurrence contracts to one fixed point

Set

\[
a=\frac{57}{256},\qquad T(c)=a+\frac{c^4}{256}.
\]

The initial source coefficient is

\[
c_1=\frac{14593}{65536}=0.2226715087890625\ldots
\]

and the peer-certified iteration gives

\[
c_4=0.2226658522832368234585407797301598223\ldots .
\]

Since \(T\) is increasing and \(T(c_1)<c_1\), the sequence decreases. On the whole interval \([a,c_1]\),

\[
0<T'(c)=\frac{c^3}{64}<1.8\times10^{-4}<1.
\]

Therefore \(T\) is a contraction there, so \(c_t\downarrow c_\infty\), the unique fixed point of (2.1) in this interval.

## 4. The target function Q is increasing on the entire tail interval

Write the exact nine-bit source core in the inherited notation as integers \(A_s,Q_s\), so

\[
H_{\rm core}(b)
=\sum_s \phi\!\left(\frac{(A_s+bQ_s)^2}{512^2}\right).
\]

Differentiating gives

\[
K'(b)=
\sum_s
\frac{2Q_s(A_s+bQ_s)}{512^2}
\phi'\!\left(\frac{(A_s+bQ_s)^2}{512^2}\right)
+\frac9{256}\left[-2b\phi'(b^2)-32b\right].
\tag{4.1}
\]

The committed verifier reconstructs the exact pair-count table \((A_s,Q_s)\) inherited from the source core and evaluates (4.1) by outward interval arithmetic on the full tail range \(b=c^4\), \(a\le c\le c_4\). It obtains

\[
\boxed{
3.724253976679159166\times10^{-4}
\le K'(b)\le
3.738751260500945911\times10^{-4}.}
\tag{4.2}
\]

In particular \(K'(b)>0\), hence \(Q(c)=(128/133)K(c^4)\) is strictly increasing for every \(c\in[a,c_4]\).

Endpoint logarithms were independently enclosed in this run using the same rational atanh-series method as the inherited source checker. The resulting certified endpoint bounds are

\[
\boxed{
Q(c)\ge q_-:=
6.52185116719555246536276288334294304707982413002878
}
\tag{4.3}
\]
for every tail value \(c\ge a\), and

\[
\boxed{
Q(c)\le q_+:=
6.52185116734786336372295569270409538753347541689836
}
\tag{4.4}
\]
for every \(c\le c_4\).

## 5. The entire future movement after F4 is too small to reach the barrier

The inherited recurrence gives \(I_4>8\). For every \(I\ge8\),

\[
\frac{513}{256}+\frac9{256}I^4>I^2,
\]
so from stage 4 onward

\[
I_{t+1}>I_t^2.
\tag{5.1}
\]

Also

\[
\lambda_t
=\frac{133/128}{I_{t+1}-1}
<\frac{266}{9}I_t^{-4}.
\]

Consequently

\[
\sum_{t\ge4}\lambda_t
<\frac{266}{9}
\sum_{j\ge0}8^{-4\cdot 2^j}
<\frac{266}{9}\frac{8^{-4}}{1-8^{-4}}
=\boxed{\frac{38}{5265}}
\approx0.00721747388414055.
\tag{5.2}
\]

Now compare the maximal possible total future upward motion with the distance from the current ratio to the lower target barrier. Using (1.1), (4.3), (4.4), and (5.2),

\[
(q_+-L_4)\frac{38}{5265}
<1.579063609069821\times10^{-9},
\tag{5.3}
\]
whereas

\[
q_--U_4
>2.186311075688130\times10^{-7}.
\tag{5.4}
\]

The gap in (5.4) is more than two orders of magnitude larger than the total possible motion in (5.3). Therefore every later \(R_t\) remains strictly below \(q_-\). Since \(q_-\le Q(c_t)\), equation (2.4) gives

\[
\boxed{R_{t+1}>R_t\quad\text{for every }t\ge4.}
\tag{5.5}
\]

Thus the recursive shared-graft obstruction increases monotonically forever, but by a summable amount, and converges to a finite limit \(R_\infty\).

This closes the exact first missing inference left by the fleet03/B18 extension report.

## 6. One further stage and a narrow certified limit bracket

The next influence satisfies

\[
I_5>200,
\]
and the exact affine update (2.4), together with the endpoint enclosures at \(c_4\), gives

\[
\boxed{
R_5\in[
6.521850949550445938234348676473909586910822493449,
6.521850949550446130442192482396930621029721447248
].}
\tag{6.1}
\]

In particular

\[
R_{5,\rm lo}-U_4
>9.86001041684659094\times10^{-10},
\]
so the fifth stage is rigorously a strict improvement.

Because \(I_5>200\), the same squaring argument yields

\[
\sum_{t\ge5}\lambda_t
<\frac{266}{9}\frac{200^{-4}}{1-200^{-4}}.
\]

Using \(q_+\) as a uniform target ceiling then gives the explicit limit enclosure

\[
\boxed{
6.521850949550445938234348676473909586910822493449
< R_\infty
<6.521850949550450153644489106618467838753558803161.
}
\tag{6.2}
\]

Every \(F_t\) is a genuine finite balanced Boolean gate; balanced self-composition of each finite stage makes ordinary \(H/I\) approach \(R_t\). Therefore the family proves the improved rigorous lower floor

\[
\boxed{
C_{\rm FEI}>
6.521850949550445938234348676473909586910822493449.
}
\tag{6.3}
\]

This is a lower bound only. It does not prove that \(C_{\rm FEI}\) is finite.

## 7. The new stable candidate and the exact remaining universal implication

The tail theorem means there is no reason to keep moving the scalar center after every finite recursive graft. Choose the explicit safe center

\[
\boxed{C_*=6.5218512,}
\tag{7.1}
\]
which is strictly above the upper endpoint in (6.2).

Let \(\Gamma_{\rm RO}\) be the inherited read-once potential normalized by
\(\Gamma_{\rm RO}(1/2)=6.4548\), and set

\[
a_*=4(C_*-6.4548)=0.2682048,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\tag{7.2}
\]

Call the following statement `LIMIT-PRIME-GATE-LIFT-v1`:

> For every composition-prime Boolean gate \(P\) of every finite arity and every interior product bias vector \(p\),
> \[
> D_{\Gamma_*}(P;p)\ge0.
> \tag{7.3}
> \]
> Constants, unary identities/negations, and boundary biases are handled by the direct base cases and continuity.

If (7.3) is proved, the fleet02/B17 cocycle proves the same corrected inequality for every Boolean gate. The all-gate reformulation then gives

\[
H(f)\le6.5218512\,I(f)
\]
for every uniform-cube Boolean function \(f\). Hence (7.3) is now one explicit, dimension-independent, noncircular missing implication whose proof would close FEI.

The recursive shared-coordinate family cannot refute (7.3) merely by continuing the same recurrence: its entire limiting balanced ratio is below \(C_*\) by (6.2). This does not exclude a different composition-prime gate or biased configuration.

## 8. Status change

**Old missing implication:** control the infinite tail of the recursive shared-core obstruction and determine whether repeatedly freezing the scalar center at \(R_2,R_3,R_4,\ldots\) would fail forever without a finite cap.

**New proved inference:** the exact recurrence is a contraction in its singleton parameter, \(Q\) is increasing on the tail interval, the update weights are summable super-exponentially, every stage after \(F_4\) strictly improves the ratio, and the complete recursive family converges inside the explicit interval (6.2).

**New first essential missing implication:** prove `LIMIT-PRIME-GATE-LIFT-v1`, equation (7.3), for every composition-prime Boolean gate and every product bias, or construct a genuine Boolean prime/bias counterexample to that same fixed statement.

**Classification:** `ESSENTIAL_STEP_APPLIED` because the exact missing tail inference named by the consumed peer result is now proved and applied to replace an unstable sequence of scalar-cap candidates by one stable fixed candidate. This is not `FULL_PROOF_CANDIDATE`: (7.3) is still open.

## 9. Verification scope

The adjacent fast verifier checks the exact recurrence algebra, reconstructs the source core pair-count table used for the derivative interval, verifies the positive derivative interval, the influence-growth/tail-weight bounds, the barrier comparison, the strict fifth-stage gain, and the final limit enclosure. For speed, its displayed endpoint \(Q\)-enclosures are the rational enclosures independently recomputed in this run by the inherited atanh-series method rather than recomputed inside the fast script. The mathematical report therefore distinguishes those two checks instead of claiming one executable did both.

Scoped privacy review: only FEI mathematics, source-bound repository paths, hashes and sanitized proof metadata are included. No credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive action, public-posting action, paid compute, or permission changes are included.
