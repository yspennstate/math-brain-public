# B15 — exact KL form of B-HARMONIC-DELETE-v2 and a Boolean obstruction to per-deletion valuation spending

**Run:** `20260922T000114Z-ac20d633`  
**Directive:** `FEI-PROOF-EXECUTION-20260921T230620Z`, Campaign B  
**Assignment:** fleet02/B15 — apply exact relative-entropy credits to the common residual and prove the influence payment, not a renamed remainder.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome classification:** **ESSENTIAL_REPRESENTATION_APPLIED / CANDIDATE_REFUTED**.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Before / after

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is proved here.

**MECHANISM CHANGE:** the preceding fleet02/B15 run refuted the `mathcal W/T_2` dichotomy and proved that a useful information refund must survive at linear tensor scale. The new Campaign-B lead handoff, fleet03/B18 `20260921T235729Z-harmonic-deletion-residual/HANDOFF_B.md` at commit `d1daf682db18332973c4fd2e5c210bdddd23e94a`, supersedes that retired candidate and fixes one common target, **B-HARMONIC-DELETE-v2**. I bind to that exact target here. The run rewrites its sole residual as `address entropy - factorial credit - exact KL credit`, and then rigorously refutes the natural attempt to spend the signed packet valuation tail separately at every live deletion step.

The named completed other-account result consumed substantively is the fleet03/B18 handoff above. It proves

\[
H(f)=H(J)+T_{\rm stop}+D_{\rm del},
\qquad H(J)\le 4.8588229680899335 I,
\qquad T_{\rm stop}\le I,
\]

with the sole unpaid residual

\[
D_{\rm del}=
\sum_{\substack{A\ne\varnothing\\i\notin A}}
\frac{v_{A+i}}{|A|+1}
\log_2\frac{v_A-p_A}{v_{A+i}}.
\tag{0.1}
\]

I also use the completed fleet01/B12 conditional ordered-code identity `20260921T231256Z-conditional-count-code/REPORT.md`: conditional coordinate-address entropy is a cross-entropy minus an exact KL/mutual-information rebate. The calculation below identifies the precise root-excluded version inside (0.1). Finally, the fleet02/B15 valuation-tail theorem `20260921T170301Z-valuation-tail-majorization/REPORT.md` is used at its proved scope: if `r(S)` is the signed packet valuation, then

\[
R(f):=\mathbb E_p r(S)\le 2J(f)\le2I(f),
\tag{0.2}
\]

with the stronger stop-loss tails retained. No physical projection integrality is assumed.

## 1. The deletion kernel hidden in the harmonic shadows

Let `S` be the Fourier spectral sample, `p_A=P(S=A)`, and `K=|S|`. For `a>=0`, put

\[
v_A=\sum_{S\supseteq A}\frac{p_S}{\binom{|S|}{a}},
\qquad |A|=a,
\qquad t_A=v_A-p_A,
\]

and `Q_{a+1}=P(K>=a+1)`. The elementary harmonic recursion is

\[
\boxed{
(a+1)t_A=\sum_{i\notin A}v_{A+i}.
}
\tag{1.1}
\]

Indeed a fixed source set `S` of size `k>=a+1` contributes on the right

\[
(k-a)\frac{p_S}{\binom{k}{a+1}}
=(a+1)\frac{p_S}{\binom{k}{a}},
\]

which is exactly `(a+1)` times its contribution to `t_A`.

For `t_A>0` define the actual next/deleted-label law

\[
\boxed{
\pi_A(i)=\frac{v_{A+i}}{(a+1)t_A},\qquad i\notin A.
}
\tag{1.2}
\]

Equation (1.1) makes this a probability law. Equivalently: condition on `K>=a+1`, choose a uniformly random `(a+1)`-subset `B` of the true spectral set `S`, then delete one uniformly random element `I` of `B`; `A=B\setminus\{I\}` has law `T_a=t_A/Q_{a+1}` and `I|A` has law (1.2).

Let `V_{a+1}=v_B/Q_{a+1}` be the law of `B`. Since `(B,I)` with `I uniform in B` is in bijection with `(A,I)`,

\[
\boxed{
H(V_{a+1})-H(T_a)
=H(I\mid A)-\log_2(a+1).
}
\tag{1.3}
\]

This keeps the sign of the level increment: the conditional label entropy may be smaller or larger than `log(a+1)`.

## 2. PROVED — exact global negative-KL representation of the common residual

Summing (1.3) with the B-lead weights gives

\[
D_{\rm del}
=\sum_{a\ge1}\sum_{|A|=a}t_A H_2(\pi_A)
-\sum_{a\ge1}Q_{a+1}\log_2(a+1).
\tag{2.1}
\]

The second sum is exactly the factorial credit:

\[
\boxed{
\sum_{a\ge1}Q_{a+1}\log_2(a+1)
=\mathbb E\log_2(K!).
}
\tag{2.2}
\]

For each coordinate define its total non-root deletion mass

\[
\beta_i:=
\sum_{a\ge1}\sum_{\substack{|A|=a\\i\notin A}}
 t_A\pi_A(i).
\tag{2.3}
\]

Conditioning on a fixed source set `S` of size `k`, at every live level `a=1,...,k-1` the next label is uniform on `S`; hence

\[
\boxed{
\beta_i
=\mathbb E\left[
\frac{K-1}{K}\,1_{\{i\in S\}}
\right],
\qquad
\beta:=\sum_i\beta_i=\mathbb E(K-1)_+.
}
\tag{2.4}
\]

Now let `q=(q_i)` be any probability law with `q_i>0` whenever `beta_i>0`. For each live prefix,

\[
H(\pi_A)=
\sum_i\pi_A(i)\log_2\frac1{q_i}
-D_{\rm KL,2}(\pi_A\|q).
\]

Insert this into (2.1). This proves the exact identity

### Theorem B15-HARMONIC-KL-01

\[
\boxed{
D_{\rm del}
=
\sum_i\beta_i\log_2\frac1{q_i}
-
\mathbb E\log_2(K!)
-
\mathcal K_q,
}
\tag{2.5}
\]

where the genuine negative information credit is

\[
\boxed{
\mathcal K_q:=
\sum_{a\ge1}\sum_{|A|=a}
 t_A D_{\rm KL,2}(\pi_A\|q)\ge0.
}
\tag{2.6}
\]

For `beta>0`, the cross-entropy is minimized at

\[
\rho_i=\beta_i/\beta,
\]

giving the canonical form

\[
\boxed{
D_{\rm del}
=
\beta H_2(\rho)
-
\mathbb E\log_2(K!)
-
\mathcal K_\rho.
}
\tag{2.7}
\]

If `beta=0`, then `K<=1` almost surely and `D_del=0`.

This is not a second normalized target. It is an exact relative-entropy decomposition of the B lead's sole residual. It also shows explicitly where negative level contributions live: in the factorial credit and in the KL rebate, neither of which may be positive-parted away.

## 3. How the valuation-tail input enters — and the natural insertion is false

A tempting next move is to refine the live deletion state by the signed source-packet valuation `r(S)` and introduce a nonnegative valuation price `g(r)`, hoping to pay that price with the already-proved valuation tails. This is the direct harmonic-deletion analogue of a Gibbs valuation tilt.

The ordered-source representation makes its true cost exact. A source set `S` of size `K` participates in precisely `K-1` non-root live deletion steps. Therefore **any source-only valuation price charged once at each live deletion has total expected charge**

\[
\boxed{
C_g^{\rm del}(f)
=
\mathbb E_p[(K-1)_+\,g(r(S))].
}
\tag{3.1}
\]

The valuation-tail theorem controls the un-size-biased packet law, e.g. `E r<=2J`; it does **not** control the deletion-size-biased quantity (3.1). The gap is not technical: it is unbounded on a standard genuine Boolean family.

## 4. PROVED Boolean obstruction — standard addressing blows up every unbounded per-deletion valuation price

Let `Adr_k` be the standard addressing Boolean function with `k` address bits and `2^k` data bits. Its Fourier expansion is

\[
Adr_k(x,y)
=2^{-k}\sum_{a\in\{0,1\}^k}
 y_a\sum_{T\subseteq[k]}(-1)^{a\cdot T}\chi_T(x).
\tag{4.1}
\]

Hence it has exactly `4^k` nonzero Fourier coefficients, all of magnitude `2^{-k}`. The spectral sample has the form

\[
S=\{y_a\}\cup T,
\qquad a\text{ uniform},\quad T\subseteq[k]\text{ uniform},
\tag{4.2}
\]

so

\[
K=1+\operatorname{Bin}(k,1/2),
\qquad
I(Adr_k)=J(Adr_k)=1+\frac k2.
\tag{4.3}
\]

There is one magnitude packet. Its physical component is the Boolean function itself, and if `V` is the signed packet mask's unnormalized Walsh transform then

\[
2^{-k}V=Adr_k,
\]

so every nonzero physical value of `V` is `\pm2^k`. Therefore its signed packet valuation is exactly

\[
\boxed{r(S)=k\quad\text{on the whole spectrum}.}
\tag{4.4}
\]

This is fully consistent with the valuation-tail theorem:

\[
R(Adr_k)=\mathbb E r=k\le2J=k+2.
\tag{4.5}
\]

But (3.1) gives

\[
\boxed{
C_g^{\rm del}(Adr_k)
=\frac k2\,g(k),
}
\tag{4.6}
\]

and hence

\[
\boxed{
\frac{C_g^{\rm del}(Adr_k)}{I(Adr_k)}
=
\frac{k}{k+2}\,g(k).
}
\tag{4.7}
\]

Consequently:

### Theorem B15-VALUATION-REPETITION-OBSTRUCTION-02

If a nonnegative valuation price `g` satisfies a universal deletion-step payment

\[
C_g^{\rm del}(f)\le C I(f)
\quad\text{for every Boolean }f,
\]

then necessarily `sup_k g(k)<=C`. In particular the natural choice `g(r)=r`, or any unbounded stop-loss/height price extracted from the valuation-tail theorem, **cannot be paid after repeating it at every live harmonic deletion step**.

For `g(r)=r`,

\[
\frac{C_r^{\rm del}(Adr_k)}{I(Adr_k)}
=\frac{k^2}{k+2}\to\infty,
\]

even though the actual valuation first moment remains `R<=2J`.

This is a Boolean obstruction to a proof mechanism, not a counterexample to FEI.

## 5. Exact calibration: why negative information must stay in the common residual

The same addressing family shows why the failure in Section 4 does not threaten the harmonic residual itself. Its raw valuation depth is large because the **same** source packet survives through `Theta(k)` deletion steps. Recharging depth at each step double-counts a one-time arithmetic feature.

The common residual (2.7), by contrast, charges the coordinate name through the stopped prefix law and subtracts both

- the one-time permutation/factorial credit `E log_2(K!)`, and
- the prefix-dependent KL rebate `mathcal K_rho`.

Thus the correct use of the valuation theorem in Campaign B can only be **one-time or KL-coupled**; it cannot be an independently positive fee repeated along the deletion chain.

This conclusion is consistent with the preceding fleet02/B15 tensor obstruction: a valid refund must survive at the correct linear scale, but a source feature also may not be charged once per occurrence when the common code has already supplied a no-reuse factorial/KL rebate.

## 6. New exact sufficient joint-credit target

The valuation first moment is already universally paid once, `R<=2J<=2I`. Therefore a strictly weaker but still full-FEI-sufficient version of B-HARMONIC-DELETE-v2 is the following **joint credit inequality**:

\[
\boxed{
\mathcal K_\rho
+
\mathbb E\log_2(K!)
+
R(f)
\ge
\beta H_2(\rho)-C_* I(f)
}
\tag{6.1}
\]

for one finite dimension-independent `C_*` and every Boolean `f`.

Indeed (2.7) and (6.1) give

\[
D_{\rm del}\le R+C_*I\le(C_*+2)I,
\]

and the B-lead reduction then gives

\[
\boxed{
H(f)
\le
(7.8588229680899335+C_*)I(f).
}
\tag{6.2}
\]

Equation (6.1) is **OPEN**. Its point is not to rename `D_del`: it identifies three source-exact credits with their correct signs and multiplicities, and Section 4 proves that the valuation credit must occur once as `R`, not as the false repeated quantity `E[(K-1)r]`.

The exact unpaid implication after this run is therefore (6.1), equivalently the B lead's `D_del<=C_del I` with the additional permission to spend the already-paid one-time valuation reserve `R<=2I`. A successful next step must lower-bound the **combined** factorial + prefix-KL + one-time valuation credit against the deletion-label address entropy; estimating any of these three terms independently from below is not justified.

## 7. Last-three comparison and stress tests

The last three substantive fleet02/B15 mechanisms were: (i) adaptive KL-preserving valuation tilt, leaving a global mesh/KL core; (ii) Jeffreys-refunded recombination, exposing a reverse-KL obstruction; and (iii) the reset-aligned radius-one/softmax dichotomy attack, which refuted that candidate and proved tensor saturation. The exact unpaid implication was therefore not unchanged for three runs. The present owner/lead reset supplies a new common residual, and this run attacks that residual rather than reopening a retired bridge.

Addressing is the decisive new test because it simultaneously has unbounded packet valuation, `H/I ->4`, and exact uniform magnitude. It proves the per-deletion valuation route false while remaining harmless for FEI. Constants, characters, and `K<=1` spectra give `beta=D_del=0` exactly. No finite computation is used as an all-dimensional theorem in this report.

## 8. Literature / scope

The current primary-source check still leaves unrestricted FEI open. González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) present restriction/stopping-tree partial progress and explicitly leave the universal step open. Potapov (arXiv:2609.21563, submitted 18 September 2026) proves FEI for plateaued functions with sharp class constant `4` and for partially bent functions with constant `2`; this does not provide the unrestricted harmonic-deletion payment. No priority claim is made for the identities here.

## 9. Outcome

**PROVED in this run:**

1. the exact KL-refunded ordered-deletion representation (2.5)-(2.7) of the current common residual `D_del`;
2. the exact multiplicity of any source-only valuation fee in the harmonic deletion chain, (3.1);
3. the genuine Boolean addressing obstruction (4.7), showing that every unbounded valuation fee is unpayable if repeated at each deletion;
4. the full-FEI-sufficient one-time joint-credit target (6.1).

**NOT PROVED:** (6.1), `D_del=O(I)`, or full FEI.
