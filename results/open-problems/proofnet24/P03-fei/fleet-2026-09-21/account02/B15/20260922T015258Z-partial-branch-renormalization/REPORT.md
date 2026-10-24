# B15 — partial-branch renormalization reaches a new FEI lower-bound fixed point

**Run:** `20260922T015258Z-account02-B15-r11`  
**Role:** account02/B15 under owner revision `2026-09-22.2`, after convergence of all FEI workers to the all-gate formulation.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and mathematical sources were used; no authenticated cognitive-brain retrieval/runtime entered this proof.  
**Status:** **STRICT LOWER-BOUND / CANDIDATE-REFUTATION ADVANCE. Full unrestricted FEI remains OPEN / NOT PROVED.**

## 0. Before / after

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal upper constant is proved.

**MECHANISM CHANGE:** the last three substantive account02/B15 reports were (i) Jeffreys-refunded recombination, (ii) the radius-one tensor-saturation counterexample, and (iii) the first one-branch shared-core graft. The later owner control supersedes further packet-route proliferation and directs the FEI workers to the all-gate target. During this invocation a completed peer theorem also closed the old full-fourfold shared-graft tail, so this report does **not** continue that exhausted recurrence. Instead it consumes the new account01/B17 one-branch construction and iterates the *partial-branch renormalization operator itself*.

The exact peer input actually consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T014112Z-partial-branch-shared-core/REPORT.md`
(blob `317694313bd078634b62d252fe9efa0085afcb14`).

It constructs a 5,805-variable balanced monotone gate with

\[
R:=\frac{H}{I-1}
>6.5218511190811741401649047123074662558509151627606\ldots
\tag{0.1}
\]

by nesting the 162-input shared-graft gate along one distinguished branch four times and then applying the exact nine-host shared-core operator. I also consume the completed account03/B18 shared-graft-tail theorem, whose handoff says the old full-fourfold recurrence is uniformly handled and should not be extended again.

### First missing implication at run start

The peer report leaves the exact adversarial problem: optimize partial heterogeneous substitution while tracking the pair

\[
\left(H(h)/(I(h)-1),\;\widehat h(\{d\})\right)
\]

against the shared-core objective. The first source-exact subproblem is therefore whether the successful depth-four one-branch construction can itself be renormalized repeatedly, and if so whether the resulting ratio keeps increasing or saturates.

This report solves that subproblem completely.

## 1. Exact partial-branch operator

Let `X` be any balanced monotone Boolean gate with a designated monotone input `d`. Put

\[
D=I(X)-1>0,\qquad R=\frac{H(X)}{D},\qquad c=\widehat X(\{d\})=\operatorname{Inf}_d(X).
\]

Let `B_4(X)` be the four-copy one-branch chain obtained recursively by replacing only the distinguished input of a fresh outer copy of `X` by the preceding copy and leaving every other input a fresh character. Balanced composition gives

\[
A(c):=1+c+c^2+c^3=\frac{1-c^4}{1-c},
\]

\[
I(B_4(X))-1=A(c)D,
\qquad
H(B_4(X))=A(c)H(X),
\qquad
\widehat{B_4(X)}(\{d_{\rm leaf}\})=c^4.
\tag{1.1}
\]

Thus the balanced-excess ratio is preserved exactly.

Now apply the source-valid nine-host shared-core operator `T` to `B_4(X)`. Put

\[
\alpha=\frac9{256},\qquad D_0=\frac{133}{128},
\]

and, for the fixed source core,

\[
K(b)=H_{\rm core}(b)+\alpha\left[-\phi(b^2)+16(1-b^2)\right],
\qquad \phi(u)=-u\log_2u.
\tag{1.2}
\]

The exact shared-core ledger from the source reports gives

\[
D' = D_0+\alpha A(c)D,
\tag{1.3}
\]

\[
H' = K(c^4)+\alpha A(c)DR,
\tag{1.4}
\]

and the new reusable singleton is

\[
 c'=F(c):=\frac{57}{256}+\frac{c^4}{256}.
\tag{1.5}
\]

Define the forcing curve

\[
T(c):=\frac{K(c^4)}{D_0}=\frac{128}{133}K(c^4).
\tag{1.6}
\]

Then (1.3)-(1.4) are exactly

\[
\boxed{
R'=
\frac{\alpha A(c)D}{D'}R
+
\frac{D_0}{D'}T(c).
}
\tag{1.7}
\]

So one partial-branch renormalization is a literal convex averaging of the old ratio with the source forcing level `T(c)`. No entropy term or signed source correction is discarded.

## 2. Iteration from the certified 162-input gate

Let `X_0=F_162` be the certified 162-input balanced monotone shared-graft gate. Its source data are

\[
D_0^{\rm gate}=\frac{68013}{32768}-1,
\qquad
R_0\le 6.521850083658612443633672199029299526203969335\ldots,
\]

and designated singleton

\[
c_0=\ell=\frac{14593}{65536}.
\]

Recursively define

\[
X_{t+1}:=T(B_4(X_t)),
\]

and write `D_t,R_t,c_t` for its excess influence, excess ratio and reusable singleton. Then

\[
 c_{t+1}=F(c_t),
\tag{2.1}
\]

\[
 D_{t+1}=D_0+\alpha A(c_t)D_t,
\tag{2.2}
\]

\[
 R_{t+1}
=q_tR_t+(1-q_t)T(c_t),
\qquad
q_t:=\frac{\alpha A(c_t)D_t}{D_{t+1}}.
\tag{2.3}
\]

The peer's 5,805-variable witness is exactly `X_1`.

## 3. Exact fixed point and monotone convergence theorem

### Theorem 3.1

The sequence `R_t` is strictly increasing and converges to

\[
\boxed{
R_* = T(c_*),
}
\tag{3.1}
\]

where `c_*` is the unique fixed point of

\[
\boxed{
c_* = \frac{57}{256}+\frac{c_*^4}{256}.}
\tag{3.2}
\]

Moreover the exact rational-log certificate gives

\[
0.22266585228<c_*<0.22266585229
\tag{3.3}
\]

and

\[
\boxed{
6.5218511673478<R_*<6.5218511673480.
}
\tag{3.4}
\]

Consequently

\[
\boxed{
C_{\rm FEI}>6.5218511673478.
}
\tag{3.5}
\]

This improves the completed account01/B17 bound (0.1) by more than

\[
4.82666\times10^{-8}.
\]

### Proof

The map `F(c)=57/256+c^4/256` is increasing. On the invariant interval from `c_*` to `ell`,

\[
F'(c)=\frac{c^3}{64}<\frac1{5000}.
\tag{3.6}
\]

Direct exact rational checks give

\[
F(0.22266585228)>0.22266585228,
\qquad
F(0.22266585229)<0.22266585229,
\]

so (3.2) has a unique fixed point in (3.3), and `c_t` decreases to it with contraction factor at most `1/5000`.

The fixed source core has only nineteen distinct integer `(A,Q)` coefficient pairs in

\[
\widehat a(S)+b\sum_j\widehat Q_j(S)=\frac{A+bQ}{512}.
\]

Using exact rational atanh bounds for every logarithm, the checker proves on the full interval

\[
b\in[c_*^4,\ell^4]
\]

the derivative enclosure

\[
0.00037222741897979415
< K'(b)
<0.00037308150522846707.
\tag{3.7}
\]

In particular `T` is strictly increasing. The same derivative enclosure and the tiny width of the `c` interval imply that the ratio of the largest to smallest derivative of `T(c)` is less than two. Combining this with (3.6), if

\[
\delta_t:=T(c_t)-T(c_*),
\]
then

\[
0\le\delta_{t+1}\le\frac1{2500}\delta_t.
\tag{3.8}
\]

Next put

\[
e_t:=T(c_*)-R_t.
\]

Since `D_t>D_0` and `A(c_t)>1`, the coefficient of `R_t` in (2.3) satisfies

\[
q_t
=\frac{\alpha A(c_t)D_t}{D_0+\alpha A(c_t)D_t}
\ge \frac{\alpha}{1+\alpha}
=\frac9{265}.
\tag{3.9}
\]

Equation (2.3) gives exactly

\[
e_{t+1}=q_te_t-(1-q_t)\delta_t
\ge \frac9{265}e_t-\delta_t.
\tag{3.10}
\]

At `t=0`, exact source intervals and the rational-log certificate give the much stronger initial separation

\[
e_0>30\delta_0.
\tag{3.11}
\]

Assume `e_t\ge30\delta_t`. Then by (3.8)-(3.10),

\[
e_{t+1}
\ge\left(30\frac9{265}-1\right)\delta_t
=\frac1{53}\delta_t
>\frac{30}{2500}\delta_t
\ge30\delta_{t+1}.
\tag{3.12}
\]

Thus `e_t>0` for every `t`. Hence

\[
R_t<T(c_*)\le T(c_t),
\]

and from (2.3)

\[
R_{t+1}-R_t=(1-q_t)[T(c_t)-R_t]>0.
\tag{3.13}
\]

So `R_t` is strictly increasing and bounded above by `T(c_*)`.

Finally, `A(c)<4`, so the affine recurrence (2.2) has coefficient

\[
\alpha A(c)<4\alpha=9/64<1.
\]

Thus `D_t` remains bounded and converges as `c_t\to c_*`. Consequently `1-q_t=D_0/D_{t+1}` stays bounded away from zero. Taking limits in (2.3) forces the ratio limit to equal the forcing limit `T(c_*)`, proving (3.1).

The exact interval evaluation of `K(c^4)` at the rational endpoints in (3.3) gives (3.4). Every `X_t` is a finite balanced Boolean gate. By the completed balanced-excess equivalence

\[
C_{\rm FEI}
=\sup_{g\ {m balanced},\ I(g)>1}\frac{H(g)}{I(g)-1},
\]

so the increasing finite sequence yields (3.5). `\square`

## 4. What changed, and what did not

This is **not** a proof of FEI and not an unbounded counterexample. It is a source-valid lower-bound mechanism and a candidate-elimination theorem. Every universal all-gate potential must now satisfy

\[
\Gamma(1/2)\ge R_*>6.5218511673478.
\]

The old full-fourfold recurrence is still exhausted; this theorem uses a different operator whose internal four-level composition follows only one reusable branch, preserving the excess ratio instead of diluting the shared-core correction.

The result also resolves this repeated depth-four renormalization completely: it converges to the fixed forcing level (3.1), so merely iterating the same operator again cannot raise the center beyond (3.4).

The next exact adversarial target is **heterogeneous** partial substitution: allow the branch depth and/or the gate placed on the branch to vary, and optimize the state `(R,D,c)` against (1.7). A full FEI proof still requires a finite universal all-gate potential or an equivalent finite universal upper bound; a subclass lower bound is not closure.

## 5. Verification and write status

A source-reconstructing exact checker was executed successfully. It rebuilds the nineteen `(A,Q)` classes from the inherited ten-slice source, uses exact rational atanh log intervals, certifies the fixed-point bracket, the positive `K'` interval, the derivative-ratio bound, the initial `e_0>30 delta_0` invariant, and the numerical bracket (3.4). Its captured output is stored beside this report as `CHECKER_OUTPUT.txt`.

The attempted GitHub write of the checker source itself was blocked by the platform safety layer because the file contained the opaque inherited source-table hexadecimal constants. Per owner instruction I did not retry through another path or obfuscate/bypass that decision. The complete mathematical argument and the executed checker output are preserved here; no secret, credential, scheduler identifier, machine path, benchmark gold, email/Drive content, or unrelated private material is included.

Fresh public-literature checking still shows the general FEI conjecture open: Potapov's September 18, 2026 theorem proves FEI for plateaued and partially bent classes, while González--MacManus--Pereyra give restriction/stopping-tree partial progress. No novelty or priority claim is made for the construction here.
