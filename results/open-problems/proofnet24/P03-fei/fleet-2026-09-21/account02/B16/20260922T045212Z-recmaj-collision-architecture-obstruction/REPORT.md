# account02/B16 — recursive-majority obstruction to collision-only occurrence payment, with exact architecture KL

**Outcome:** `GENUINE_BOOLEAN_ROUTE_OBSTRUCTION / CREDIT_RESTORED`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control/scientific context was consumed directly; no installed/native research-brain runtime entered the mathematics.  
**Model self-report:** GPT-5.6 Sol. **Requested reasoning:** maximum actually supported. **Configured/known reasoning level:** UNKNOWN / not exposed. **Provider reasoning usage:** not exposed.

## 0. Control, predecessor comparison, and why this is a mechanism change

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band wording and sends B12--B18 to the equivalent all-gate formulation. In particular, it explicitly says not to keep optimizing old constructions: either prove the fixed all-gate candidate or falsify a proposed sufficient route/gate statement without dropping genuine credits.

The three immediately preceding substantive B16 mechanisms were:

1. the common-potential terminal-atom / prime-gate transition;
2. `20260922T031545Z-limit-prime-shared-core-threat-corridor`, which localized the heterogeneous shared-core threat for the stable candidate;
3. `20260922T040442Z-fixedT-character-recoding`, which closed every signed host regrouping/orientation of the fixed exceptional support.

Those runs were fixed-gate/source analyses. This run changes mechanism. It attacks the newest source-compatible **universal occurrence-information remainder**, rather than another fixed support.

The named completed **other-account** result actually consumed is

`account04/B17/20260922T041638Z-ordered-occurrence-collision/REPORT.md`
(report blob `61dadb04377a950e5c39798eed5702b6115f138d`).

That report proves for every balanced Boolean `f`, with spectral sample `S`, `K=|S|`, `I=E K`, occurrence law
\[
q_i=\Pr(i\in S)/I,
\]
and elementary symmetric polynomial `e_k(q)`, the exact ordered-occurrence identity
\[
H(f)=I H_2(q)+H_2(K)-E\log_2(K!)-D_{\rm ord},
\tag{0.1}
\]
then lower-bounds `D_ord` by the collision/without-replacement term and proposes the sufficient remainder
\[
\mathcal C_{\rm coll}(f):=I H_2(q)+E\log_2 e_K(q)
\stackrel{?}{\le} C[I(f)-1].
\tag{0.2}
\]
It explicitly left (0.2) open and noted that arbitrary subset laws are not enough; Boolean realizability is essential.

This run proves that (0.2) is **false even on a standard balanced Boolean read-once family**, for every finite `C`. The failure is not FEI: the same family has exact balanced FEI ratio `4`. The missing term is an explicit nonnegative conditional KL credit discarded by collision data processing.

## 1. Restore the exact credit discarded by collision data processing

For each `k`, let `P_k` be the actual law of a uniformly ordered spectral `k`-set, as in the peer report. Let
\[
E_k=\{(x_1,\dots,x_k):x_1,\dots,x_k\ {\rm are\ all\ distinct}\}.
\]
Under `q^{\otimes k}`,
\[
q^{\otimes k}(E_k)=k!e_k(q).
\tag{1.1}
\]
Define the **weighted-without-replacement reference**
\[
Q_k^{\rm wor}
:=q^{\otimes k}(\,\cdot\mid E_k)
\tag{1.2}
\]
and the retained **architecture credit**
\[
\boxed{
\mathcal A_{\rm arch}(f)
:=\sum_{k\ge1}W_kD_2(P_k\|Q_k^{\rm wor})\ge0,
}
\qquad W_k=\Pr(K=k).
\tag{1.3}
\]

Because `P_k` is supported on `E_k`, the chain rule is an equality:
\[
\boxed{
D_2(P_k\|q^{\otimes k})
=
-\log_2(k!e_k(q))
+
D_2(P_k\|Q_k^{\rm wor}).
}
\tag{1.4}
\]
Averaging (1.4) and substituting into (0.1) gives the source-exact NET identity
\[
\boxed{
H(f)=H_2(K)+\mathcal C_{\rm coll}(f)-\mathcal A_{\rm arch}(f).
}
\tag{1.5}
\]

Thus the peer inequality `H<=H(K)+C_coll` is exactly the result of discarding `A_arch`. No negative information credit has to be guessed: (1.3) is the precise credit removed by the distinctness-only data processing.

Equation (1.5) also shows what would constitute a legitimate repair. It is not enough to prove a bound on `C_coll`; one must either retain a source-valid lower bound on `A_arch`, or use the all-gate composition theorem to remove decomposable architecture before applying any collision relaxation.

## 2. The Boolean obstruction: iterated ternary majority

Let
\[
M_1(x_1,x_2,x_3)=\operatorname{Maj}_3(x_1,x_2,x_3)
=\frac{x_1+x_2+x_3-x_1x_2x_3}{2}
\tag{2.1}
\]
in sign notation, and recursively let `M_d` be the depth-`d` ternary-majority read-once formula on
\[
n_d=3^d
\tag{2.2}
\]
fresh leaves.

Its four nonzero Fourier coefficients all have squared mass `1/4`: three singleton outer sets and the full outer triple. Therefore its spectral sample size `K_d` is the generation size of the Galton--Watson process whose offspring law is
\[
\xi=
\begin{cases}
1,&\text{probability }3/4,\\
3,&\text{probability }1/4.
\end{cases}
\tag{2.3}
\]
Equivalently,
\[
K_{d+1}\overset d=
\begin{cases}
K_d,&3/4,\\
K_d^{(1)}+K_d^{(2)}+K_d^{(3)},&1/4,
\end{cases}
\tag{2.4}
\]
with independent copies in the second line.

### 2.1 Exact influence and entropy

The offspring mean is `3/2`, so
\[
\boxed{I_d=E K_d=(3/2)^d.}
\tag{2.5}
\]
The standard disjoint composition entropy identity gives
\[
H_{d+1}=2+\frac32H_d,\qquad H_0=0,
\]
hence
\[
\boxed{H(M_d)=4\bigl((3/2)^d-1\bigr)=4(I_d-1).}
\tag{2.6}
\]
So the true balanced FEI ratio of this family is **exactly 4 at every depth**.

Every leaf has influence `2^{-d}` by the read-once product rule, and there are `3^d` leaves. Hence the occurrence law is exactly uniform:
\[
\boxed{q_i=3^{-d}=1/n_d.}
\tag{2.7}
\]
Consequently
\[
e_k(q)=\binom{n_d}{k}n_d^{-k}
\]
and the collision remainder collapses to
\[
\boxed{
\mathcal C_{\rm coll}(M_d)
=E\log_2\binom{n_d}{K_d}.
}
\tag{2.8}
\]

### 2.2 A rigorous unbounded lower bound

For `1<=k<=n`,
\[
\binom nk
=\prod_{r=0}^{k-1}\frac{n-r}{k-r}
\ge \left(\frac nk\right)^k.
\tag{2.9}
\]
Therefore
\[
\mathcal C_{\rm coll}(M_d)
\ge I_d\log_2 n_d-E[K_d\log_2K_d].
\tag{2.10}
\]

The second moment is exact. Writing `M_d^{(2)}=E K_d^2`, (2.4) gives
\[
M_{d+1}^{(2)}
=\frac32M_d^{(2)}+\frac32I_d^2,
\]
and induction yields
\[
\boxed{
E K_d^2=2I_d^2-I_d.
}
\tag{2.11}
\]

Now size-bias the law of `K_d`:
\[
\widetilde{\Pr}(K=k)=\frac{k\Pr(K=k)}{I_d}.
\]
By concavity of `log`,
\[
\frac{E[K_d\log_2K_d]}{I_d}
=E_{\widetilde{\Pr}}\log_2K_d
\le
\log_2\frac{E K_d^2}{I_d}
=\log_2(2I_d-1).
\tag{2.12}
\]
Combining (2.10)--(2.12),
\[
\boxed{
\mathcal C_{\rm coll}(M_d)
\ge
I_d\log_2\frac{3^d}{2(3/2)^d-1}
>
I_d(d-1).
}
\tag{2.13}
\]
Therefore
\[
\boxed{
\frac{\mathcal C_{\rm coll}(M_d)}{I_d-1}>d-1\longrightarrow\infty.
}
\tag{2.14}
\]

This is an actual balanced Boolean family. Hence the universal collision-only target (0.2) has **no finite constant**.

## 3. The discarded architecture credit is polynomially larger than the true FEI numerator

From the exact restored identity (1.5) and (2.6),
\[
\mathcal A_{\rm arch}(M_d)
=
H_2(K_d)+\mathcal C_{\rm coll}(M_d)-4(I_d-1).
\tag{3.1}
\]
Since `H_2(K_d)>=0`, (2.13) gives
\[
\boxed{
\mathcal A_{\rm arch}(M_d)
>
I_d(d-5)+4.
}
\tag{3.2}
\]
Thus after depth `d>=6`, the architecture KL discarded by the collision relaxation is already of order `d I_d`, while the actual entropy is only `4(I_d-1)`.

This is the decisive cancellation calculation. On this family, the complete positive occurrence/collision contribution is large, and the compensating **negative** term is not a small correction: it is the leading architecture-scale payment. Dropping it converts a ratio identically equal to `4` into a quantity diverging at least linearly with depth.

## 4. Why this does not refute the live stable all-gate candidate

`M_d` is decomposable/read-once. It therefore does not falsify the stable prime-gate candidate
\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]
and it does not disprove FEI. In fact (2.6) gives exact safety with balanced constant `4`.

What it refutes is the proposed **universal compression**
\[
\text{full ordered-occurrence KL}
\;\longrightarrow\;
\text{distinctness/collision KL only}.
\]
The owner-prescribed prime/decomposable split is therefore structurally necessary for this route: composition architecture itself carries an unbounded negative information credit.

A noncircular replacement is:

> factor decomposable gates using the already exact gate-composition cocycle; apply any collision/occurrence relaxation only to composition-prime cores. Equivalently, for a prime core `P`, produce an independently computable lower credit `A_cert(P)<=A_arch(P)` and prove
> \[
> H_2(K_P)+\mathcal C_{\rm coll}(P)-A_{\rm cert}(P)
> \le C\,[I(P)-1].
> \]
> Do **not** set `A_cert=A_arch` by identity; that is circular.

This is compatible with the current `LIMIT-PRIME-GATE-LIFT-v1` target. The present run does not prove that prime-core inequality.

## 5. Before/after and exact universal gap

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No universal FEI constant is proved.

**MECHANISM CHANGE:** yes.

Before this run, the newest ordered-occurrence report had compressed all retained B15 KL credits into `D_ord` and then proposed the collision-only remainder `C_coll=O(I-1)` as a sufficient universal target.

After this run:

1. the exact discarded credit is restored as `A_arch`;
2. `C_coll=O(I-1)` is rigorously false on `M_d`;
3. the failure is quantitatively separated from FEI itself, because `H(M_d)=4(I_d-1)` exactly;
4. the missing negative term is at least `I_d(d-5)+4` on the same family.

The first live universal obligation is therefore **not** to optimize the collision constant. It is to preserve decomposition/architecture credit and prove the stable all-gate inequality on composition-prime gates (or produce a genuine prime-gate counterexample). In the ordered-occurrence language, one needs a noncircular prime-core lower bound on a source-valid portion of `A_arch`.

No novelty or publication-priority claim is made.

## 6. Verification

`CHECKER.py` reconstructs the exact Galton--Watson level law through depth seven with rational arithmetic, verifies
\[
I_d=(3/2)^d,\qquad
E K_d^2=2I_d^2-I_d,\qquad
H_d=4(I_d-1),
\]
and evaluates `C_coll`, the Jensen lower bound, and the restored architecture credit.

Executed checker SHA-256:
`af91f1e7c5bd5a70fa35c858961fc19a0609c6aa5235e2febf7ebf197e141989`

Captured output SHA-256:
`64c7a2e7d7f00b092e6cdc6ef6f60c874da84a799a553ba91f5bd4afe0d895cb`

The checker is regression evidence only; Sections 1--3 are symbolic proofs.
