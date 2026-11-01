# B16 FEI campaign C — source-exact net candidate, complete conditional deduction, and the two-defect cancellation test

**Run:** `20260921T234240Z-fleet01-B16-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** **ESSENTIAL_STEP_APPLIED**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

This report follows `FEI-PROOF-EXECUTION-20260921T230620Z`.  It does not treat a positive-current surrogate as the theorem.  It recovers the original signed compiler statement, gives a complete conditional deduction from that statement to FEI, and applies the statement to the required genuine Boolean half-band obstruction.  The new calculation proves that the obstruction has a bounded signed NET compiler debt even though its already-formed positive live current divided by `J` diverges.  It also refutes a tempting pointwise self-phase payment.  No auxiliary theorem is claimed to settle FEI.

## 1. Exact source candidate and immutable versions

The canonical source is

`proofnet24/P03-fei/runs/2026-09-15/2026-09-15_11-42-26__run-report.md`

(source blob recorded by the succeeding canonical report as `b85418013f2f1586a0196ac97a7fb24ac03340f4`).  For a Boolean phase after the one minimizing-character gauge, write

\[
J(f)=\sum_i\min\{I_i(f),1-I_i(f)\}.
\]

At every paid complete-degree prefix `d`, in **natural logarithm units**, the exact compiler identity is

\[
\boxed{
H_{\rm nat}(f)
=\kappa_2J(f)-\mathcal B_d(f)+\mathcal Q_{d,<2}(f)+R_d(f),
}
\tag{1.1}
\]
where

\[
\kappa_2=\frac23+\operatorname{artanh}(1/2)
=\frac23+\frac12\log3,
\tag{1.2}
\]
`mathcal B_d` is the retained signed high-resolvent/R16 bank after its internal odd-order refunds, `mathcal Q_{d,<2}` is the genuine small-resolvent cumulative source, and `R_d` is the terminal endpoint.  The R16 reservoir behind the high bank is

\[
C_{k,r}\ge0,\qquad
D_{k,r}=C_{0,r}-C_{k,r},
\qquad
\Delta_{k,>2}
=\sum_{r\ge2}\frac{(-1)^rD_{k,r}}
{(r-1)2^{r-1}},
\tag{1.3}
\]
so odd collision orders are refunds and are not absolute-valued.

The same NET source has the exact R32 truth-table form

\[
\boxed{
H_{\rm nat}(f)-R_d(f)
=\frac8N
\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}I_{|A|,N},
}
\tag{1.4}
\]
with

\[
C_0=RM(1,n)^\perp,
\qquad
D_d=RM(n-d-1,n),
\]
\[
I_{w,N}=\int_0^\infty
\frac{\sin^w t\cos^{N-w}t}{t^3}\,dt\ge0.
\tag{1.5}
\]
Thus `|A|=0 mod 4` terms are positive debits and `|A|=2 mod 4` terms are genuine negative credits.

Equivalently, with

\[
\mathfrak G_d(s)
=2N\!\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N),
\tag{1.6}
\]
we have

\[
\boxed{
H_{\rm nat}(f)-R_d(f)
=4\int_0^\infty\frac{\mathfrak G_d(s)}{s^3}\,ds.
}
\tag{1.7}
\]
Fleet04/B16's exact finite-resolvent identity further gives

\[
\mathcal Q_{d,<2}
=\int_0^\infty w_{<2}(s)\mathfrak G_d(s)\,ds,
\qquad
w_{<2}(s)+w_{>2}(s)=\frac4{s^3},
\tag{1.8}
\]
so the low and high terms are co-located on the same signed packet before any square.

### Candidate `C-NET-ARCHIVE-v1`

Use the completely source-recovered terminal cutoff

\[
\boxed{d_*=n-\lfloor n/5\rfloor-1,}
\tag{1.9}
\]
for which the historical terminal theorem gives

\[
\boxed{|R_{d_*}(f)|<\frac32J(f).}
\tag{1.10}
\]
Define the source-exact net debt

\[
\boxed{
\mathcal N_*(f)
:=\mathcal Q_{d_*,<2}(f)-\mathcal B_{d_*}(f).
}
\tag{1.11}
\]
The single missing candidate statement is

\[
\boxed{
\exists C_*<\infty\ \forall n\ \forall f:\quad
\mathcal N_*(f)\le C_*J(f).
}
\tag{C-NET}
\]
This is not a positive-current estimate, not a relationwise absolute-value estimate, and not a critical-core assumption.  It is the original low-minus-high signed compiler obligation with its actual source cutoff and terminal normalization.

## 2. Complete conditional deduction `C-NET => FEI`

This is written out because campaign C requires the end-to-end implication rather than an appeal to equivalence.

Let `f` be any Boolean function.  Choose the minimizing character `chi_T` and put `F=f chi_T`.  Then Fourier squared masses are permuted, hence

\[
H_{\rm nat}(F)=H_{\rm nat}(f),
\tag{2.1}
\]
and the physical edge influences become

\[
I(F)=J(f)\le I(f).
\tag{2.2}
\]
If `F` is a character then `H=0` and there is nothing to prove.  Otherwise apply (1.1) at `d_*`, (C-NET), and (1.10):

\[
\begin{aligned}
H_{\rm nat}(f)
&=H_{\rm nat}(F)\\
&=\kappa_2J(f)+\mathcal N_*(F)+R_{d_*}(F)\\
&\le\left(\kappa_2+C_*+\frac32\right)J(f)\\
&\le\left(\kappa_2+C_*+\frac32\right)I(f).
\end{aligned}
\tag{2.3}
\]
Dividing by `ln 2` gives the bit-entropy FEI constant

\[
\boxed{
C_{\rm FEI}
=\frac{C_*+\frac32+\frac23+\frac12\log3}{\log2}.
}
\tag{2.4}
\]
All dimensions and all Boolean functions are included.  No asymptotic endpoint or finite-dimensional exception is used in this deduction.

For comparison only, the stronger carried half-band cutoff `d_h=ceil(n/2)` has `R_{d_h}=o(J)` uniformly over noncharacters.  It is useful for asymptotic obstruction calculations below, but (2.3) deliberately uses the fully recovered archive cutoff so that the conditional proof has an explicit all-dimensional terminal constant.

## 3. Exact named other-account result consumed

The current lead-C input used here is fleet02/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260921T230348Z-oriented-relation-square-root/REPORT.md`

(report blob `74a8144e588366e95d5c8b5ca8f0e384d8f1d6fd`).  It proves the relation-oriented square root

\[
\zeta_A(y)=\frac{h_{A_V}(y)-h_{A_U}(y)}2,
\qquad
\zeta_A(y)^2=\nu_A(y),
\tag{3.1}
\]
and the original-coordinate Dirichlet estimate

\[
\frac14\sum_i\mathbb E_y(\Delta_i\zeta_A)^2
\le\frac{|A|}{2}J(f).
\tag{3.2}
\]
After relation normalization by `|A|^{-1/2}` this is dimension-free.  Its exact open interface is that active-syndrome square-root allocation uses `1/|R|`, while the physical relation root uses `1/|A|`; the same-syndrome cross terms are exact even-correlation combinations and are not known to be paid by R16/terminal credits.

I also apply fleet02/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T225920Z-live-low-amplitude-parent-aggregation/REPORT.md`

(blob `4eb584133626148cdc89213fdaca906ae7b70ef8`).  It proves, before the final positive current is formed, that every measurable live low-resolvent window has a coherently integrated terminal-aware source with exact active-parent coefficients satisfying

\[
\boxed{
\sum_j\lambda_{j,W}\le64J(f).
}
\tag{3.3}
\]
It explicitly leaves the Borel-scale variance / high-resolvent / outside-live signed companion unresolved.  The calculation below shows why that unresolved companion cannot be replaced by an `O(J)` post-square bank on the known half-band obstruction.

## 4. Required two-point-defect test — exact Fourier law

Use the actual obstruction family from the fleet02 half-band correction.  Let the original cube have dimension `n>=2` and size

\[
M=2^n.
\]
Let `u,v` be two vertices at Hamming distance two, and set

\[
f(u)=f(v)=-1,
\qquad
f(x)=+1\quad(x\notin\{u,v\}).
\tag{4.1}
\]
Appending the source dummy coordinate does not change Fourier entropy or original-coordinate influence.  The fine truth-table length is `N=2M`, matching the half-band construction.

For the original `n`-cube Fourier law, put

\[
x=\frac4M.
\]
The constant Fourier coefficient is

\[
\widehat f(\varnothing)=1-x,
\qquad
p_0=(1-x)^2.
\tag{4.2}
\]
For `S\ne\varnothing`,

\[
\widehat f(S)
=-\frac2M\bigl(\chi_S(u)+\chi_S(v)\bigr).
\tag{4.3}
\]
Since `u+v` has weight two, exactly

\[
K=\frac M2-1
\]
nonconstant subsets have even parity on `u+v`; on those

\[
|\widehat f(S)|=\frac4M=x,
\qquad p_S=x^2,
\tag{4.4}
\]
and all remaining nonconstant coefficients vanish.  Hence

\[
\boxed{
p_0=(1-x)^2,\qquad
K=M/2-1\text{ atoms of mass }x^2.}
\tag{4.5}
\]
The normalization is exact because

\[
(1-x)^2+Kx^2=1.
\]
Every original coordinate has influence `4/M`, so

\[
\boxed{J(f)=I(f)=\frac{4n}{M}.}
\tag{4.6}
\]
The exact natural entropy is

\[
\boxed{
H_{\rm nat}(f)
=-2(1-x)^2\log(1-x)
-2x(2-x)\log x.
}
\tag{4.7}
\]
Since `n=log_2 M=2-log_2 x`, this gives

\[
\frac{H_{\rm nat}(f)}{J(f)}
=4\log2+\frac{2-8\log2}{n}+O(2^{-n}).
\tag{4.8}
\]
In particular

\[
\boxed{H_2(f)<4J(f)}
\tag{4.9}
\]
for every `n>=2`.  One direct proof of (4.9) is to compare `4(log2)J-H_nat`: after division by two it equals

\[
2x\log4+(1-x)^2\log(1-x)-x^2\log x.
\]
Using `log(1-x)>=-x/(1-x)` makes this at least

\[
x(2\log4-(1-x))-x^2\log x>0.
\]
Thus the family is explicitly FEI-benign; it is only a compiler-route obstruction.

## 5. The source-exact NET candidate passes the obstruction

At the fully recovered archive cutoff, (1.1), (1.10), and (4.9) give immediately

\[
\begin{aligned}
\mathcal N_*(f)
&=H_{\rm nat}(f)-\kappa_2J(f)-R_{d_*}(f)\\
&<\left(4\log2+\frac32-\kappa_2\right)J(f).
\end{aligned}
\]
Therefore

\[
\boxed{
\mathcal N_*(f)<3.05661591123906\,J(f)
}
\tag{5.1}
\]
for every member of the family.  This is a direct evaluation of the **positive and negative compiler contributions together**.  It does not bound the positive part separately.

At the stronger carried half-band endpoint, `R_{d_h}/J ->0` uniformly over noncharacters, so (4.8) gives the sharper asymptotic

\[
\boxed{
\frac{\mathcal Q_{d_h,<2}-\mathcal B_{d_h}}{J}
\longrightarrow
4\log2-\kappa_2
=1.55661591123906\ldots .
}
\tag{5.2}
\]
This should be contrasted with the exact positive-current correction from fleet02:

\[
L_D
\sim\frac4{27n^3},
\qquad
J=\frac{8n}{2^{n+1}},
\qquad
\frac{L_D}{J}\to\infty.
\tag{5.3}
\]
Thus the positive-current blow-up is absent from the original NET source.  Any exact representation which first exposes `L_D` with positive coefficient must contain another co-located signed contribution of the same leading polynomial scale.  The aggregate high bank by itself cannot be that later compensation because the preceding B16 source proves

\[
\mathcal B_{d_h}=O(J).
\tag{5.4}
\]
Consequently the missing cancellation must occur **before the positive current / local square is finalized**, precisely where the fleet02/B18 even-correlation cross ledger and fleet02/B16 Borel-scale variance remain unresolved.

This is the concrete application of the named peer candidate: branch (b) of its open interface cannot mean “form the positive current, then pay the off-diagonal cross bank by a fixed `O(J)` R16/terminal amount.”  On this authentic family that interpretation is impossible.  The even-correlation/high/terminal pieces must remain inside the same signed pre-square object.

## 6. First missing inference attacked: pointwise self-phase payment is false

The preceding fleet01/B16 self-phase transform gives, on the original `n`-cube,

\[
M\Xi(s)
=\cos s-\cos((1-x)s)
+K\,[1-\cos(xs)],
\qquad
x=4/M,\quad K=M/2-1.
\tag{6.1}
\]
The full signed integral is exactly entropy:

\[
4M\int_0^\infty\frac{\Xi(s)}{s^3}\,ds
=H_{\rm nat}(f).
\tag{6.2}
\]
A tempting next inference would be to pay the source pointwise by its physical boundary, for example

\[
M\Xi(s)\le C J(f)
\quad\text{uniformly in }s.
\tag{6.3}
\]
The same required obstruction kills (6.3) rigorously.  Fix `c>0` and take

\[
s=c\sqrt M.
\]
Then `xs=4c/\sqrt M ->0`, and

\[
|\cos s-\cos((1-x)s)|\le xs\to0,
\]
while

\[
K[1-\cos(xs)]
\longrightarrow4c^2.
\]
Hence

\[
\boxed{M\Xi(c\sqrt M)\to4c^2,}
\tag{6.4}
\]
but `J(f)=4n/M ->0`.  Thus no finite dimension-independent `C` can make (6.3) true.

This is a source-level obstruction, not a post-square artifact.  It says the required proof must be **integrated/multiscale** even after the self-phase reorganization.  On this family each logarithmic scale can carry order `1/M` source mass while the total physical budget is order `n/M`; the number of active scales is itself order `n`.  A valid universal proof has to charge those scales coherently to original-coordinate structure rather than demand pointwise `O(J)`.

## 7. Old and new missing implications

**Old missing implication (now known false in its strong form):**

> Form the complete positive finite-window current (or a pointwise positive self-phase source) and then control it by a fixed multiple of `J` plus a fixed aggregate R16 bank.

The half-band current obstruction and (6.4) rule out both post-square and pointwise versions.

**New exact missing implication:**

> Prove `C-NET-ARCHIVE-v1`, i.e. the original signed whole-expression bound
> \[
> \mathcal Q_{d_*,<2}-\mathcal B_{d_*}\le C_*J,
> \]
> with the low/high/terminal and same-syndrome/even-correlation pieces kept co-located until after cancellation; equivalently, obtain a pre-square multiscale inequality for the signed source whose integration gives this net bound.

Fleet02/B16 already pays the coherently integrated live-low component by `64J`.  The first genuinely unpaid object is therefore the source-exact Borel-scale variance/high/outside-live signed residual, with fleet02/B18's even-correlation cross ledger retained.  The two-defect calculation proves that this residual cannot be estimated by taking the absolute value of each companion separately: on the known obstruction the required cancellation is parametrically larger than `J` before the net is formed.

## 8. Status

**Classification: `ESSENTIAL_STEP_APPLIED`.**  The source-exact candidate is now fixed with an immutable cutoff and a complete all-dimensional conditional deduction to FEI.  The required two-point-defect obstruction has been evaluated on that candidate and does **not** refute it; instead it proves where the necessary large signed cancellation must occur.  A natural first inference—pointwise source payment by `J`—is rigorously refuted, forcing the next C attempt to be genuinely integrated and pre-square.

This is **not** `FULL_PROOF_CANDIDATE`: the universal estimate `C-NET` remains unproved.  Full FEI remains OPEN.
