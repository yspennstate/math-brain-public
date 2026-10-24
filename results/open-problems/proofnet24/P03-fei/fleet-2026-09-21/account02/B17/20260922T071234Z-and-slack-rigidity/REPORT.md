# account02/B17 — off-centre prime refutation forces AND-slack transport

**Run:** `B17-20260922T071234Z-r11`  
**Classification:** `CURRENT_FIXED_CANDIDATE_REFUTED / ESSENTIAL_STRUCTURAL_REPLACEMENT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Candidate, completed peer results, and exact change

The latest complete Campaign-B lead report I could read is account03/B18

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T062639Z-rare-gating-nonamplification/REPORT.md`

(blob `fd5041b1ff948f566ce001ad3e226876f0279800`). It still names
`LIMIT-PRIME-GATE-LIFT-v1`

\[
 C^\dagger=6.521851214,\qquad
 \Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p)
\tag{0.1}
\]

as the live all-gate candidate, and proves that the exact rare-gating transform cannot amplify a balanced core already safe at any center `C>=4`. I apply that theorem here: the growing rare-cylinder mechanism from my preceding run is removed from the adversary list.

A second completed **other-account** result is decisive and source-compatible: account03/B12

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`

(blob `36fea824c2dcae8c65c3d485e5d5714899699855`). Using the already-certified composition-prime 18-input Numaro gate, it gives the exact interior bias

\[
 p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,
\qquad p_{out}=967/2048,
\tag{0.2}
\]

and certifies

\[
 D_{\Gamma^\dagger}(P;p)
 =-0.0176114199558017537894958865691\ldots<0.
\tag{0.3}
\]

Thus the B-lead report's sentence that (0.1) remains universally viable is stale relative to this exact completed peer obstruction. The obstruction refutes the fixed potential, **not FEI**.

The last three B17 substantive mechanisms were: radius-one changed-support rigidity (`20260922T041256Z-onecell-support-rigidity`), radius-two support rigidity plus sparse Fourier-dust slope four (`20260922T044637Z-radius2-dust-compensation`), and growing rare-gated defects plus exponential-codimension safety (`20260922T061440Z-mesoscopic-defect-codimension`).

**FULL-PROBLEM CHANGE: NONE.** FEI remains open.  
**MECHANISM CHANGE: YES.** Before this run B17 was varying actual Boolean sources against a fixed potential. The exact biased prime witness kills that fixed potential, and account03/B18 closes rare-cylinder amplification. This run therefore moves to a different object: **charged potential reshaping**, where pre-existing AND slack is treated as a finite resource rather than demanding a free pointwise correction.

## 1. Gate-defect notation and the exact witness correction

For a symmetric potential `Gamma`, let

\[
 D_\Gamma(G;p)=
 \sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
 -\Gamma(p_{out})-\widetilde H_G(p),
\qquad V_t=4t(1-t).
\tag{1.1}
\]

For the two-input AND gate,

\[
 {\operatorname{It}_1\over V_p}=q,\qquad
 {\operatorname{It}_2\over V_q}=p,\qquad p_{out}=pq.
\]

Hence a potential perturbation `Gamma -> Gamma+psi` changes the AND defect by exactly

\[
 L_{p,q}(\psi):=q\psi(p)+p\psi(q)-\psi(pq).
\tag{1.2}
\]

Also

\[
 L_{p,q}\bigl(t(1-t)\bigr)=p q(1-p)(1-q)=:M(p,q).
\tag{1.3}
\]

For the peer's 18-input witness, all coordinates except the first remain at `1/2`, so any center-preserving symmetric perturbation `psi(1/2)=0` changes (0.3) by exactly

\[
 R_{wit}(\psi)
 ={57\over256}\psi(3/8)-\psi(967/2048).
\tag{1.4}
\]

A same-center repair of this exact witness therefore needs

\[
 R_{wit}(\psi)>0.0176114.
\tag{1.5}
\]

## 2. Rigidity theorem: there is no nonzero free center-preserving AND repair

### Theorem 2.1 (AND-slack rigidity)

Let `psi:(0,1)->R` be bounded and symmetric,

\[
 \psi(t)=\psi(1-t),\qquad \psi(1/2)=0.
\]

If

\[
 L_{p,q}(\psi)\ge0
\qquad\hbox{for every }p,q\in(0,1),
\tag{2.1}
\]

then

\[
 \boxed{\psi\equiv0.}
\tag{2.2}
\]

### Proof

Set `q=1/2` in (2.1). For `x in (0,1/2)`, take `p=2x` and use symmetry when `2x>1/2`. With

\[
 T(x)=\min\{2x,1-2x\}\in[0,1/2],
\]

we obtain

\[
 \psi(x)\le {1\over2}\psi(Tx).
\tag{2.3}
\]

Iterating gives

\[
 \psi(x)\le2^{-m}\psi(T^m x).
\]

Boundedness therefore implies `psi(x)<=0` for every `x in (0,1/2)`, and symmetry gives the same on all of `(0,1)`.

Now fix arbitrary `p in (1/2,1)` and choose `q=1/(2p) in (1/2,1)`, so `pq=1/2`. Then (2.1) gives

\[
 q\psi(p)+p\psi(q)\ge0.
\]

Both summands are nonpositive, hence both vanish. Thus `psi(p)=0` for every `p>1/2`; symmetry and `psi(1/2)=0` finish the proof. `QED`

### Consequence

A localized shoulder, cusp, polynomial bump, or any other bounded symmetric **center-zero** correction cannot repair (0.3) while independently preserving every AND defect. Any nontrivial same-center reshaping must deliberately make some AND inequalities worse and pay for that loss from existing slack. This is a structural obstruction to a stronger bridge, not an FEI obstruction.

## 3. Quantitative theorem: the exact witness consumes at least 97.9% of the guaranteed AND bank

The free-rigidity theorem says some AND slack must be spent. The next result prices how much using only exact AND inequalities.

Assume the weaker charged condition

\[
 L_{p,q}(\psi)\ge-K M(p,q)
\qquad(p,q\in(0,1)),
\tag{3.1}
\]

for some `K>=0`, together with symmetry and `psi(1/2)=0`. No boundedness or continuity is needed for the finite calculation below.

For `x in (0,1/2)`, the `q=1/2` instance of (3.1) yields

\[
 \psi(x)\le {1\over2}\psi(Tx)+Kc(x),
\qquad c(x)={x(1-2x)\over2}.
\tag{3.2}
\]

At `x=3/8`, the orbit `3/8 -> 1/4 -> 1/2` gives exactly

\[
 \psi(3/8)\le {5K\over64}.
\tag{3.3}
\]

For the second witness point, set

\[
 y_0={57\over1081},\qquad y_{j+1}=T(y_j).
\]

Exact integer arithmetic gives `y_253=y_0` with no earlier repetition. Iterating (3.2) around this 253-cycle gives

\[
 \psi(y_0)\le K U,
\qquad
 U={\sum_{j=0}^{252}2^{-j}c(y_j)\over1-2^{-253}}
 =0.07018449003990096\ldots .
\tag{3.4}
\]

Now put

\[
 x={1081\over2048},\qquad q={1024\over1081},
\]

so `xq=1/2`, `psi(x)=psi(967/2048)`, and `psi(q)=psi(57/1081)`. Equation (3.1) at this pair gives

\[
 \psi(967/2048)
 \ge-{K\over q}\bigl(M(x,q)+xU\bigr).
\tag{3.5}
\]

Combining (3.3)--(3.5),

\[
 \boxed{
 R_{wit}(\psi)\le \kappa K,
 }
\tag{3.6}
\]

where the coefficient is the explicit finite rational number

\[
 \kappa
 ={57\over256}{5\over64}
 +{M(1081/2048,1024/1081)+(1081/2048)U\over1024/1081}
 =0.06964414494777522\ldots
 <0.069645.
\tag{3.7}
\]

Since the peer certificate gives the strict witness deficit `>0.0176114`, every center-preserving correction that repairs that witness and obeys (3.1) must satisfy

\[
 \boxed{K>0.2528769.}
\tag{3.8}
\]

This is a quantitative negative-credit statement: the off-centre prime witness cannot be repaired cheaply in the AND currency.

## 4. Comparison with the rigorously certified AND bank

The completed read-once certificate proves the AND inequality for

\[
 \Gamma_{cert}(p)=\Gamma_0(p)+0.01\,p(1-p),
\]

with center `6.4573`. The refuted candidate (0.1) therefore contains a rigorously guaranteed extra quadratic AND bank

\[
 A=0.268204856-0.01=0.258204856,
\tag{4.1}
\]

because (1.3) adds exactly `A M(p,q)` to every AND defect.

Thus any same-center perturbation `psi` that preserves the already-certified AND theorem merely by spending this guaranteed bank has `K<=A`. By (3.8), repairing the one exact biased prime witness consumes more than

\[
 {0.2528769\over0.258204856}>97.93\%
\tag{4.2}
\]

of that entire bank. The guaranteed coefficient reserve after paying this one witness is less than `0.00533`.

This does **not** prove that a same-center all-gate repair is impossible: the estimate is one-sided and a correction may exploit more detailed positive slack than the uniform bank (4.1), or a different finite-cap potential may abandon this base shape entirely. What it proves is that the natural stronger repair principle "fix the new prime obstruction without spending AND slack" is impossible, and even the weakest uniform-slack accounting is almost saturated by one actual prime/bias witness.

## 5. New replacement mechanism and remaining universal implication

The previous universal implication

\[
 D_{\Gamma^\dagger}(P;p)\ge0
 \quad\hbox{for every composition-prime Boolean gate and every interior bias}
\]

is **REFUTED** by account03/B12, so it is no longer an open lemma to certify.

The materially different replacement is **SLACK-BUDGETED POTENTIAL TRANSPORT**. Write

\[
 \Gamma_{new}=\Gamma^\dagger+\psi,
 \qquad \psi(1/2)=0,
\]

if retaining the current center is desired. Instead of requiring the false/free condition `L_AND psi>=0`, explicitly retain the existing signed AND credit:

\[
 D_{\Gamma^\dagger}(AND;p,q)+L_{p,q}(\psi)\ge0
\qquad\forall p,q,
\tag{5.1}
\]

while forcing the exact prime repair

\[
 {57\over256}\psi(3/8)-\psi(967/2048)
 \ge0.0176114199558\ldots .
\tag{5.2}
\]

Then test the same `Gamma_new` on all remaining composition-prime gates and all product biases. Equations (2.2) and (3.8) show that this mechanism must genuinely **transport negative/positive slack between gate constraints**; it cannot be reduced to a free local bump or another scalar quadratic lift. If the center is allowed to rise instead, account03/B12 already proves that the one-parameter quadratic family requires coefficient `>0.3367154`, hence center `>6.53897885`.

The final universal target remains the owner-equivalent all-gate theorem: construct one symmetric nonnegative finite-cap `Gamma` satisfying (1.1)'s gate inequality for every Boolean gate and every interior product bias. Any such finite cap proves FEI. No such potential is proved here.

## 6. Sanity checker and scope

`CHECKER.py` uses exact `Fraction` arithmetic to verify the 253-cycle, the finite rational sum (3.4), the exact `M` term, the bound `kappa<0.069645`, the resulting `K>0.2528769` from the peer-certified deficit `>0.0176114`, and the 97.9% bank-consumption comparison. It does not re-certify the peer's 18-bit Walsh interval; that source-exact certificate is consumed from account03/B12. The theorem proofs above are analytic; the checker guards arithmetic only.

Scoped privacy review: this package contains only FEI mathematics, logical account/slot labels, public-to-the-private-repository source-bound paths/hashes, and nonsecret constants. It contains no credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private data, email/Drive operations, paid/remote model calls, workflow dispatch, or permission changes.
