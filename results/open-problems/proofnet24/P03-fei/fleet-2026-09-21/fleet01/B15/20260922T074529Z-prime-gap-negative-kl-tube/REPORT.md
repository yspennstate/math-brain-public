# fleet01/B15 — composition-prime five-bit gap and negative-KL tube

**Run:** `20260922T074529Z-fleet01-B15-r11b`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PRIME-CENTRAL-GAP / NEGATIVE-KL-TUBE`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact candidate and before/after

This run binds to the current common candidate `LIMIT-PRIME-GATE-LIFT-v1` from the B lead:

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\qquad a^\dagger=0.268204856.
\]

For a Boolean gate \(G\) at product bias \(p\), write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_t=4t(1-t).
\]

The exact composition cocycle reduces this fixed candidate to composition-prime gates. Thus the common universal missing implication is

\[
\boxed{D_{\Gamma^\dagger}(P;p)\ge0}
\tag{0.1}
\]

for every finite composition-prime Boolean gate \(P\) and every interior product bias \(p\).

The completed B-lead theorem
`fleet03/B18/20260922T065506Z-prime-central-orbits/REPORT.md`
proves every essential composition-prime five-input gate has central reserve

\[
D_{\Gamma^\dagger}(P;1/2^5)\ge0.004906502214.
\]

The completed fleet02/B15 theorem
`fleet02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`
then retains the exact negative entropy/KL term and certifies all essential five-input primes in the tube
\(\|p-1/2^5\|_\infty\le4.4\times10^{-6}\).

**New result.** The small central reserve above is caused by decomposable near-equality tables. After applying the exact composition-prime module criterion to the full source-exact five-cube certificate, every essential five-input prime has the much larger central reserve

\[
\boxed{
D_{\Gamma_{.01}}(P;1/2^5)>0.039,
}
\qquad
\Gamma_{.01}(u)=\Gamma_0(u)+0.01u(1-u).
\tag{0.2}
\]

Consequently its read-once-base margin satisfies

\[
\boxed{c_P(1/2^5)<-0.0212.}
\tag{0.3}
\]

Combining (0.2) with the fleet02 negative-KL entropy transport gives the explicit larger common tube

\[
\boxed{
\max_i|p_i-1/2|\le4\times10^{-5}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(P;p)>0.000349632
}
\tag{0.4}
\]

for every essential composition-prime five-input gate. This radius is \(100/11=9.09\ldots\) times the previous \(4.4\times10^{-6}\) prime tube.

This is not full FEI. Higher-arity primes and five-input primes outside (0.4) remain unpaid.

## 1. Exact peer inputs actually used

### 1.1 Complete five-cube source certificate

`fleet01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`
and its exact checker prove, for every five-input Boolean \(G\) of output cardinality \(m\), that

\[
U(G):=6.4573\,I(G)-H(G)
\ge U(F_m),
\tag{1.1}
\]

where \(F_m\) is an explicit binary AND/OR read-once comparator of the same cardinality. The finite checker covers 3,425,314 low-boundary truth tables for \(1\le m\le16\), discharges the remaining higher-boundary tables analytically, and uses outward rational log intervals. Output complementation covers \(m>16\).

The previously quoted global strict objective gap \(0.004906502214\) occurs in the \(m=7,9\) sectors, but that number does not impose composition-primality.

### 1.2 Exact module criterion

`fleet01/B16/20260922T010748Z-prime-arity10-gate/REPORT.md`
proves the following criterion. For a coordinate block \(A\), let \(R_a\) be the row of the truth table on \(A^c\) produced by fixing \(A=a\). An essential \(n\)-input gate is composition-prime for arbitrary disjoint Boolean functional composition iff

\[
\#\{R_a:a\in\{\pm1\}^A\}\ge3
\tag{1.2}
\]

for every \(A\) with \(2\le|A|\le n-1\).

The proof is exact: a block has at most two row types iff its dependence factors through one Boolean summary bit.

### 1.3 Exact negative Shannon term

`fleet02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`
gives the source-exact Gibbs identity

\[
D_\Gamma(G;p)
=
V_{p_{\rm out}}\left[
D_{\rm KL,2}(w^+\Vert\nu_p^+)
-\log_2{Z-1\over x_{p_{\rm out}}}
\right],
\tag{1.3}
\]

and, for transport from a five-bit uniform source \(w^0\), the entropy decomposition below. This run uses its negative sign quantitatively rather than replacing it by a generic continuity bound.

The compatible fleet04/B15 result
`fleet04/B15/20260922T071345Z-gibbs-activity-tensor-transfer/REPORT.md`
proves that under disjoint composition all conditional KL credits transfer exactly, including the block-activity KL term. Thus the new finite calculation is correctly concentrated on composition-prime gates rather than tensor/decomposable descendants.

## 2. New exact finite theorem: the \(0.039\) prime gap

Fix \(m\in\{2,\ldots,16\}\). The checker beside this report independently reconstructs the B17 comparator \(F_m\), the integer Walsh transform, the cube boundary, and the same outward rational log intervals.

For every low-boundary truth table it computes a rigorous lower bound

\[
L(G)\le U(G)-U(F_m).
\tag{2.1}
\]

It then applies the complete row-type criterion (1.2) to **every table for which**

\[
L(G)\le0.039.
\tag{2.2}
\]

There are exactly

\[
\boxed{9490}
\]

such potentially dangerous low-boundary rows among the 3,425,314 enumerated rows. Every one of the 9,490 is decomposable; zero is composition-prime.

The sector counts of rows satisfying (2.2) are

\[
80,320,80,960,480,800,40,1120,960,1920,240,960,560,960,10
\]

for \(m=2,\ldots,16\), respectively.

For all non-enumerated higher-boundary tables, the same analytic entropy upper bound as B17 gives sectorwise certified generic objective gaps. Their minimum is

\[
0.102023592992>0.039
\]

over \(m=2,\ldots,16\). The \(m=1\) and \(m=31\) gates are one-point/co-one-point AND/OR functions of signed literals and hence decomposable; \(m=0,32\) are constants. Output complementation preserves composition-primality and the objective.

Therefore every essential composition-prime five-input Boolean gate satisfies

\[
\boxed{
U(P)-U(F_m)>0.039.
}
\tag{2.3}
\]

Because the read-once certificate gives

\[
D_{\Gamma_{.01}}(F_m;1/2^5)\ge0,
\]

and \(P,F_m\) have the same output measure,

\[
D_{\Gamma_{.01}}(P;1/2^5)
=
[U(P)-U(F_m)]
+D_{\Gamma_{.01}}(F_m;1/2^5)
>0.039.
\]

This proves (0.2).

The checker output is `PASS`. It performs all sign decisions with integer Walsh data and exact rational/outward logarithmic intervals; floating point is not used to decide the \(0.039\) threshold.

## 3. Margin consequence requested by the owner

For the base potential \(\Gamma_0\), adding \(c\,u(1-u)\) changes the gate defect by

\[
cM_P,\qquad
M_P={I(P)\over4}-p_{\rm out}(1-p_{\rm out})\ge0.
\tag{3.1}
\]

For an essential composition-prime Boolean gate, \(M_P>0\): equality would force uniform Fourier degree at most one, hence a constant or signed dictator.

Define the margin demanded by \(P\) at the center by

\[
c_P=-{D_{\Gamma_0}(P;1/2^5)\over M_P}.
\]

Equation (0.2) gives

\[
D_{\Gamma_0}(P;1/2^5)+0.01M_P>0.039.
\]

Since \(I(P)\le5\),

\[
M_P\le {I(P)\over4}\le{5\over4}.
\]

Hence

\[
\begin{aligned}
c_P
&<0.01-{0.039\over M_P}\\
&\le0.01-{0.039\over5/4}\\
&=\boxed{-0.0212}.
\end{aligned}
\tag{3.2}
\]

Thus every genuinely composition-prime five-input gate at the exact uniform center asks for **negative** quadratic margin against \(\Gamma_0\). The previously dangerous \(0.0049065\) rows are decomposable artifacts at this prime-filtered level.

This is a central-slice theorem only; it does not revive the already-refuted global AND/decomposable extremality claim.

## 4. Quantitative use of the negative entropy term

Let

\[
p^0=(1/2,\ldots,1/2),\qquad
\varepsilon_0=4\times10^{-5},
\qquad
\|p-p^0\|_\infty\le\varepsilon_0.
\]

Let \(a^0,a\) be the actual signed biased Fourier coefficient vectors at \(p^0,p\), and \(w^0,w\) their squared laws.

The source-valid transform estimate from fleet03/B15 gives

\[
\eta:=\|a-a^0\|_2
\le {20\over\sqrt3}\varepsilon_0
<12\varepsilon_0.
\tag{4.1}
\]

Let \(J=\{S:w^0(S)>0\}\),

\[
\zeta=\sum_{S\notin J}w(S),
\qquad
r=w(\,\cdot\mid J).
\]

Then

\[
\zeta\le\eta^2<144\varepsilon_0^2.
\tag{4.2}
\]

Every nonzero uniform five-bit Fourier coefficient has magnitude at least \(1/16\), so \(w^0(S)\ge1/256\) on \(J\). With
\(\ell_S=\log_2(1/w^0(S))\in[0,8]\), Shannon's exact change on the surviving support is

\[
\boxed{
H(r)-H(w^0)
=
\sum_{S\in J}(r_S-w^0_S)\ell_S
-
D_{\rm KL,2}(r\Vert w^0).
}
\tag{4.3}
\]

The second term is the requested **negative entropy refund**. Keeping it gives the fleet02 support/leakage estimate

\[
\boxed{
H(w)-H(w^0)
\le
8\eta+h_2(\zeta)+9\zeta
-(1-\zeta)D_{\rm KL,2}(r\Vert w^0).
}
\tag{4.4}
\]

At the fixed radius \(\varepsilon_0\), put

\[
q_0=144\varepsilon_0^2=2.304\times10^{-7}.
\]

Since \(\zeta\le q_0<1/2\), binary entropy is increasing there; moreover
\(h_2(q_0)<31q_0\). Thus

\[
H(w)-H(w^0)
<
96\varepsilon_0+5760\varepsilon_0^2
-(1-\zeta)D_{\rm KL,2}(r\Vert w^0).
\tag{4.5}
\]

Numerically the deterministic entropy debit in (4.5) is

\[
0.003849216.
\]

For comparison, the generic 32-atom Fannes--Audenaert debit at
\(\operatorname{TV}\le12\varepsilon_0\) is about \(0.00836219\). With the input/output transport costs below, that coarse bound exceeds the \(0.039\) prime reserve. The support/KL decomposition is therefore quantitatively what makes the radius \(4\times10^{-5}\) close.

## 5. Remaining deterministic transport and the larger prime tube

For a Boolean gate,

\[
\alpha_i(p):={\operatorname{It}_i(P;p)\over V_{p_i}}
\]

is the pivotal probability under the other four biased inputs, so

\[
0\le\alpha_i\le1,\qquad
|\alpha_i(p)-\alpha_i(p^0)|\le4\varepsilon_0.
\tag{5.1}
\]

For \(t\) in the input tube, write its smaller representative as \(r\). The committed h96 source form is

\[
\Gamma_0(r)=rG(\log_2(1/r)),
\qquad
G(x)<4.9096x+8.629,
\qquad
|G'(x)|<31.
\tag{5.2}
\]

Here \(r\ge0.49996\), hence \(x<1.001\). Using \(1/\ln2<3/2\) and the lift coefficient \(a^\dagger<0.269\), (5.2) gives the conservative bound

\[
|(\Gamma^\dagger)'(t)|<61
\tag{5.3}
\]

through the input tube.

Set \(A(t)=\Gamma^\dagger(t)+h_2(V_t)\). Since
\(h_2(V_{1/2+s})=h_2(4s^2)\), and with
\(z_0=4\varepsilon_0^2=6.4\times10^{-9}\) one has
\(h_2(z_0)<36z_0\), equations (5.1)--(5.3) give

\[
\left|
\sum_i\alpha_i(p)A(p_i)
-
\sum_i\alpha_i(p^0)A(1/2)
\right|
<
445\varepsilon_0+720\varepsilon_0^2.
\tag{5.4}
\]

For a nonconstant five-bit truth table, the uniform output measure is \(m/32\). Product coupling gives

\[
|p_{\rm out}(p)-p_{\rm out}(p^0)|\le5\varepsilon_0.
\]

Hence its smaller representative stays above

\[
{1\over32}-5\varepsilon_0=0.03105>{1\over64}.
\]

The inherited source-valid bound \(|(\Gamma^\dagger)'|<85\) on that output region therefore gives

\[
|\Gamma^\dagger(p_{\rm out}(p))
-
\Gamma^\dagger(p_{\rm out}(p^0))|
<425\varepsilon_0.
\tag{5.5}
\]

Combining the central reserve (0.2), (4.5), (5.4), and (5.5),

\[
\begin{aligned}
D_{\Gamma^\dagger}(P;p)
&>
0.039
-966\varepsilon_0
-6480\varepsilon_0^2\\
&\qquad
+(1-\zeta)D_{\rm KL,2}(r\Vert w^0).
\end{aligned}
\tag{5.6}
\]

At \(\varepsilon_0=4\times10^{-5}\),

\[
966\varepsilon_0+6480\varepsilon_0^2
=0.038650368,
\]

so

\[
\boxed{
D_{\Gamma^\dagger}(P;p)
>
0.000349632
+(1-\zeta)D_{\rm KL,2}(r\Vert w^0)
>0.
}
\tag{5.7}
\]

This proves (0.4). The negative KL term is retained with its source sign and remains available as additional gate-dependent reserve; it is not reused elsewhere.

## 6. Required obstruction checks and scope

The decisive statement was tested against the inherited obstruction classes before introducing a new residual.

* **Addressing/MUX, majority, tribes, and sparse defects:** every five-input uniform-center truth table in these classes is already contained in the exact all-table certificate, and the new module filter applies to it. No class-specific assumption is used.
* **Tensor products/disjoint compositions:** fleet04/B15's exact activity-KL cocycle shows these are decomposable and transfers all negative KL credits with the correct activity weights. They cannot invalidate the prime theorem by a hidden tensor debt.
* **Biased limits:** the present theorem deliberately does not cover boundary-approaching biases. The tube ends at \(4\times10^{-5}\) from the center; biased-limit obstructions remain part of the universal missing quantifier.
* **Higher arity:** untouched by the finite five-cube certificate. The explicit arity-10 prime obstruction remains a genuine reason the all-arity statement is nontrivial.

Thus this is an applied piece of the common all-gate proof candidate, not evidence that the remaining universal prime inequality follows automatically.

## 7. Exact old/new missing implications

**Old first missing implication.**

\[
D_{\Gamma^\dagger}(P;p)\ge0
\quad
\text{for every composition-prime }P
\text{ and every interior }p.
\]

The previously certified five-input neighborhood had radius
\(4.4\times10^{-6}\), based on the global non-equality central reserve
\(0.004906502214\).

**New proved inference.**

1. Every essential composition-prime five-input gate has
   \(D_{\Gamma_{.01}}(P;1/2^5)>0.039\).
2. Equivalently its center margin satisfies \(c_P<-0.0212\).
3. Retaining the negative support-relative entropy term closes every such prime throughout
   \(\|p-1/2^5\|_\infty\le4\times10^{-5}\).

**New first missing implication.** Prove the same fixed-candidate inequality for five-input primes outside this larger central tube, and for higher-arity primes, preferably by a source-exact lower bound on the conditional Gibbs KL in (1.3), or construct a genuine prime gate/bias falsifier.

No auxiliary theorem, finite slice, or equivalence here is claimed to settle FEI.

## 8. Verification and privacy

`check_prime_gap_kl_tube.py` reconstructs the exact low-boundary certificate, applies the complete module criterion to every row whose certified lower bound is at most \(0.039\), verifies all generic sector bounds exceed \(0.039\), and checks the tube arithmetic. Captured output: `PASS`.

Git blob identifiers after readback:

- checker: `b33d8ea9e5c3d541b3ef72e200b4adbf65cb90ba`;
- captured output: `259718af700888da79b18fd70c336d9745f032d0`.

Raw-byte SHA-256 values are not asserted here; the repository connector exposes the Git blob identifiers directly.

The checker is a finite certificate for the five-input prime central gap and deterministic tube arithmetic. The analytic KL identities and Fourier transport are proved in the cited source reports; the checker does not replace those proofs.

Scoped manual review found only FEI mathematics, source-bound repository identifiers, and sanitized verification metadata. No credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email/Drive content, public release action, paid/remote compute, workflow execution, or permission changes are included.
