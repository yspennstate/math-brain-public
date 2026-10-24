# account02/B14 — block erasure/Poincare envelope collapses to a singleton

**Classification:** `MECHANISM_CHANGE / AUXILIARY_ONLY / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository sources were consumed; no installed mathematical-brain receiver/context was used.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Live universal chain and first missing implication

The newest complete Campaign-A lead consumed is account01/B18

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`
(blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`).  Its current source-bound candidate is

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),\qquad
a^\dagger=0.268204856.
\]

The all-gate equivalence says that proving

\[
D_{\Gamma^\dagger}(G;p)\ge0
\]

for every finite-arity Boolean gate and every interior product bias proves full FEI with constant `C^dagger`; composition reduces the unpaid case to composition-prime gates.  The lead now proves an explicit complementary-data MUX address tube, but unequal-data MUX and then arbitrary prime gates remain open.

For the restriction implementation, the compatible compact induction is: if every nonterminal gate admits one proper physical restriction block `A` for which

\[
D_{\Gamma^\dagger}(G;p)-
\mathbb E_{X_A}D_{\Gamma^\dagger}(G_{A=X_A};p_{A^c})\ge0,
\tag{0.1}
\]

then induction on essential arity closes the all-gate inequality, with constants/literals as terminal states.  The first missing implication is therefore a realizable physical block/coordinate selector proving (0.1) without discarding signed child or output-potential credit.

This run changes mechanism after the preceding B14 routes still left that selector unpaid.  It asks a sharp preliminary question: **can a larger physical block improve the root-only erasure/Poincare-currency part of the selector over every singleton?**  The answer below is no, at every product bias.  Therefore any genuine block advantage in the live stable candidate must come from the signed output-potential/Jensen term or from using the exact restriction entropy below its entropic-uncertainty envelope; block size alone cannot improve the sign-free erasure/currency ratio.

## 1. Named completed peer inputs consumed

### account01/B13 — block entropic uncertainty

I substantively use

`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T0445Z-block-entropic-uncertainty/REPORT.md`.

For a Boolean gate under product bias, a physical block `A`, root spectral sample `S`, `U=S_A`, `T=S_{A^c}`, and physical branch `Z=X_A`, it proves

\[
\Delta_AH=H(U\mid T)+I(Z;T),
\tag{1.1}
\]

and, with

\[
\eta_A:=\sum_{i\in A}
\left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right]\ge0,
\tag{1.2}
\]

the all-dimensional Boolean uncertainty bound

\[
\boxed{\Delta_AH\le 2B_A+\eta_A},\qquad
B_A:=H(S_A\mid S_{A^c}).
\tag{1.3}
\]

At uniform bias `eta_A=0`; for a singleton this includes `JS_i<=B_i` and `Delta_i H<=2B_i`.

### account02/B18 — exact physical restriction currency

I also use

`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T040428Z-random-block-currency/REPORT.md`
(report blob `bd4972b11cb13989282f555deb9354509d1da590`).  For biased Fourier masses

\[
w_S=\widehat G_p(S)^2
\]

and the exact Poincare potential

\[
P(G;p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})
=\frac14\sum_{|S|\ge2}(|S|-1)w_S,
\tag{1.4}
\]

let

\[
Q_A:=P(G;p)-\mathbb E_{X_A}P(G_{A=X_A};p_{A^c})
\tag{1.5}
\]

be the original physical currency spent by revealing block `A`.  The peer report proves the restriction-Parseval identity required to compute this currency exactly.

## 2. New theorem: exact fixed-block currency has an internal-mass rebate

### Theorem 2.1

For every Boolean gate at every interior product bias and every physical block `A`,

\[
\boxed{
4Q_A=
\sum_{|S|\ge2}
\min\{|S\cap A|,\,|S|-1\}\,w_S.
}
\tag{2.1}
\]

Consequently, writing singleton currencies `Q_i:=Q_{\{i\}}`,

\[
\boxed{
Q_A=
\sum_{i\in A}Q_i-rac14
\sum_{\substack{S\subseteq A\\ |S|\ge2}}w_S
\le \sum_{i\in A}Q_i.
}
\tag{2.2}
\]

#### Proof

By the peer restriction-Parseval identity, a root Fourier set `S` of size `k>=2` projects after revealing `A` to `S\setminus A`.  Its root contribution to `4P` is `k-1`; its expected child contribution is exactly

\[
(|S\setminus A|-1)_+.
\]

Put `m=|S cap A|`.  The spent coefficient is

\[
(k-1)-(k-m-1)_+
=
\begin{cases}
m,&m<k,\\k-1,&m=k,
\end{cases}
=
\min\{m,k-1\},
\]

which proves (2.1).  Summing singleton currencies counts the same set with coefficient `m`.  The two coefficients differ by exactly one iff `S subseteq A`, and otherwise agree.  This gives (2.2). `square`

The correction in (2.2) has the right sign for the present problem: revealing a whole Fourier support at once loses one unit of Poincare currency relative to summing its singleton expenditures.

## 3. New theorem: spectral erasure is superadditive over a physical block

### Theorem 3.1

For every probability law of a spectral sample `S` and every physical block `A`,

\[
\boxed{
B_A=H(S_A\mid S_{A^c})
\ge\sum_{i\in A}H(S_i\mid S_{-i})
=\sum_{i\in A}B_i.
}
\tag{3.1}
\]

#### Proof

Order `A={i_1,...,i_m}`.  The chain rule gives

\[
B_A=
\sum_{j=1}^m
H(S_{i_j}\mid S_{A^c},S_{i_1},...,S_{i_{j-1}}).
\]

Each conditioning sigma-field on the right is contained in the full set of other spectral coordinates `S_{-i_j}`.  Since conditioning reduces entropy,

\[
H(S_{i_j}\mid S_{A^c},S_{i_1},...,S_{i_{j-1}})
\ge H(S_{i_j}\mid S_{-i_j})=B_{i_j}.
\]

Summing proves (3.1). `square`

## 4. Block-to-singleton collapse for the exact erasure/currency ratio

Combining (2.2) and (3.1) gives the main statement.

### Theorem 4.1 — no pure block improvement

For every nonempty physical block `A` with `Q_A>0`,

\[
\boxed{
\frac{B_A}{Q_A}
\ge
\frac{\sum_{i\in A}B_i}{\sum_{i\in A}Q_i}
\ge
\min_{\substack{i\in A\\Q_i>0}}
\frac{B_i}{Q_i}.
}
\tag{4.1}
\]

Coordinates with `Q_i=0` cause no difficulty: their nonnegative `B_i` only increase the middle numerator, and `Q_A>0` guarantees at least one positive-currency coordinate.

Thus, for every finite `K`,

\[
\boxed{
B_A\le KQ_A
\quad\Longrightarrow\quad
\exists i\in A:\ B_i\le KQ_i.
}
\tag{4.2}
\]

This is an existential-coordinate statement.  It does **not** assert a paid bound for every prescribed coordinate.

The same collapse survives the account01/B13 bias penalty.  Since `eta_A=sum_{i in A}eta_i`, define

\[
E_A:=2B_A+\eta_A.
\]

Then

\[
\boxed{
\frac{E_A}{Q_A}
\ge
\min_{\substack{i\in A\\Q_i>0}}
\frac{2B_i+\eta_i}{Q_i}.
}
\tag{4.3}
\]

Hence the full block entropic-uncertainty envelope (1.3), normalized by exact Poincare currency, can never beat every singleton at any product bias.

## 5. Application to the stable restriction lower bound: where block advantage can still live

The account01/B13 fixed-block lower bound for the read-once base plus scalar lift has the form

\[
D_{\Gamma_*}(G)-\mathbb E_ZD_{\Gamma_*}(G_{A=Z})
\ge
\mathcal L_A^{\rm RO}
+\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
-(2B_A+\eta_A)+a_*Q_A.
\tag{5.1}
\]

Here `mathcal L_A^RO=sum_{i in A} mathcal L_i^RO` is additive.  Remove only the signed output-potential term and call the remaining root envelope

\[
M_A^0:=\mathcal L_A^{\rm RO}-(2B_A+\eta_A)+a_*Q_A.
\tag{5.2}
\]

Equations (2.2), (3.1), and additivity of `eta` and the input charge give

\[
\boxed{
M_A^0\le\sum_{i\in A}M_{\{i\}}^0.
}
\tag{5.3}
\]

Therefore

\[
M_A^0\ge0
\quad\Longrightarrow\quad
\exists i\in A:\ M_{\{i\}}^0\ge0.
\tag{5.4}
\]

So **larger physical blocks add no certifying power to this sign-free root envelope**.  In the live stable candidate, a genuinely useful block must exploit at least one feature that (5.2) deliberately omits:

1. the signed, nonadditive output-potential/Jensen term `E Gamma_RO(r_Z)-Gamma_RO(r)`;
2. the exact entropy decrement `Delta_A H`, when it is substantially smaller than the uncertainty envelope `2B_A+eta_A`;
3. adaptive descendant slack/credits that are retained rather than reset.

This is the exact remaining interface for B14.  It does **not** refute account02/B18's full random-block stable-potential mechanism, because that mechanism retains the signed output-potential term.

## 6. Uniform-cube corollary: a DTC gateway to the quadratic-eight selector

At uniform bias `eta_A=0`.  Account03/B12's completed quadratic-eight formulation uses

\[
D_8(f)=8(I(f)-\operatorname{Var}(f))-H(f)
\]

and singleton currency

\[
C_i:=\operatorname{Inf}_i(f)-\widehat f(\{i\})^2=4Q_i.
\]

The account01/B13 singleton uncertainty bound gives

\[
L_i:=\Delta_iH\le2B_i.
\]

Thus the root inequality

\[
\boxed{
\sum_i B_i\le4\sum_i C_i=4(I-W_1)
}
\tag{6.1}
\]

would force

\[
\sum_iL_i\le8\sum_iC_i,
\]

and hence some essential coordinate with

\[
L_i\le8C_i.
\tag{6.2}
\]

That is exactly a physical GS8-good split and gives the corresponding induction step.

If `DTC(S):=H(S)-sum_i H(S_i|S_{-i})`, then (6.1) is

\[
\boxed{H(S)-DTC(S)\le4(I-W_1).}
\tag{6.3}
\]

This is only a **sufficient gateway**, not a universal theorem.  Indeed the archived 80-variable erasure witness already has certified `B/I>4.007`, which refutes even the weaker universal claim `sum_i B_i<=4I`; therefore (6.3) cannot be the universal closure mechanism.  The point is diagnostic: it identifies exactly why an unsigned erasure-only quadratic-eight proof cannot close FEI.

Account03/B12 additionally proves that GS8/E8 are preserved under disjoint tensor products, with nonnegative tensor credits.  Therefore a minimal GS8 counterexample can be taken tensor-prime.  Any such all-bad tensor-prime gate must satisfy the strict necessary condition

\[
\boxed{H-DTC>4(I-W_1),}
\tag{6.4}
\]

because otherwise (6.1)-(6.2) produce a good singleton.  The hard region is thus explicitly high-erasure relative to higher-order Poincare currency; tensor replication cannot manufacture it from a safe factor.

## 7. Random fixed-size blocks collapse even more visibly

For completeness, average over uniform `r`-subsets and put

\[
b_r:=\mathbb E_{|A|=r}B_A,
\qquad
h_m:=\mathbb E_{|T|=m}H(S_T).
\]

Then `b_r=H-h_{n-r}`.  Entropy submodularity gives

\[
2h_m\ge h_{m-1}+h_{m+1},
\]

so `h_m-h_{m-1}` decreases in `m`; consequently `b_r` is discrete convex with `b_0=0`, and `b_r/r` is nondecreasing.

The exact account02/B18 formula

\[
Q_r={1\over4}\sum_{k\ge2}W_k
\left({kr\over n}-{(r)_k\over(n)_k}\right)
\]

has decreasing increments, so `Q_r` is discrete concave with `Q_0=0`, and `Q_r/r` is nonincreasing.  Therefore whenever `Q_r>0`,

\[
\boxed{\frac{b_r}{Q_r}\text{ is nondecreasing in }r.}
\tag{7.1}
\]

Thus the fixed-size random-block version of the sign-free erasure/currency selector is already weakest at `r=1`.  This averaged statement is strictly subsumed by the fixed-block theorem (4.1), but it explains directly why merely scanning more block sizes cannot repair the erased selector.

## 8. Exact before/after and failed routes

The last three substantive B14 mechanisms visible in the task history were: the uniform `JS<=16Q` Poincare-currency theorem, an arbitrary-bias coherent bounded-potential lift, and the shared-graft reachability sharpening.  Each moved a different local mechanism but left a physical selector/policy implication unpaid.  This run therefore changes mechanism as required: it does not tune another scalar threshold and instead proves an exact block-versus-singleton dominance theorem.

**Before:** larger physical blocks, especially the random fixed-size bank, remained plausible as a way to improve the erasure/Poincare part of the stable selector.

**After:** for the exact root erasure `B_A` and exact physical Poincare currency `Q_A`, every block ratio is at least one singleton ratio, at every product bias; the account01/B13 uncertainty envelope has the same collapse.  Therefore the unsigned block-size mechanism is decisively exhausted.

**Remaining formula:** for the live stable candidate one must control a block or adaptive history through the terms omitted from (5.2), most concretely

\[
\mathbb E_Z\Gamma_{\rm RO}(r_Z)-\Gamma_{\rm RO}(r)
\]

and/or a strict gain between the exact `Delta_A H` and `2B_A+eta_A`, while retaining descendant slack.  Equivalently, a successful physical selector must be dependency-aware and signed; a pure `B_A/Q_A` block search cannot close the universal gate inequality.

The known prescribed-coordinate counterexamples remain intact, and no every-coordinate claim is made.  The retired sign-free/global phase/rank/l1 and fixed-relative near-subcube routes are not reopened.

## 9. Literature/status

The current primary literature checked in this invocation remains consistent with unrestricted FEI being open.  González--MacManus--Pereyra (29 May 2026) develop the restriction/stopping-tree programme with a remaining universal inequality; Potapov (18 September 2026) proves FEI for plateaued and partially bent classes rather than universally.  No novelty or priority claim is made for Theorems 2.1--4.1 or the collapse formulation.

## 10. Next B14 implication

The next useful B14 step is **not** another block-size scan.  It is to prove, for a minimum stable-candidate prime gate, that the signed output-potential term in (5.1) must compensate the singleton-dominated erasure envelope on some nonuniform/adaptive physical block, or to construct a genuine Boolean prime gate where every such signed selector fails.  Any proposed policy must keep original-coordinate `Q` costs and descendant credits nonreused.

**FULL-PROBLEM CHANGE:** none; full FEI remains open.  
**MECHANISM CHANGE:** yes; the entire unsigned physical-block erasure/Poincare-envelope route is reduced to singleton selection, with the exact signed residual isolated.
