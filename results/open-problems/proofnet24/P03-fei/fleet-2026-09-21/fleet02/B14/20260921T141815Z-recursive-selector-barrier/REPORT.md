# B14 — recursive Numaro seed gives a finite `rho_0 > 7.096` obstruction

**Status:** PARTIAL / new universal-route obstruction plus rigorous finite recursive certificate. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Live role:** FEI erasure and selector proof.  
**Current sprint subassignment:** fleet02/B14, existential restriction induction / new non-read-once constructions maximizing `min_i Delta_i H / Inf_i`.  
**Publication priority:** UNVERIFIED. The 18-variable seed is external work of Numaro; no novelty claim is made for that seed or for the composition technology.

This run uses FLEET_RULES creative moves **#5 (add a parameter: expose the one-coordinate bias `q` exactly), #19 (make it an algorithm: turn the composition identity into a finite recursive certificate), and #24 (find the extremal object: feed the current best public balanced FEI seed into the selector rather than continue perturbing tribes)**. It adopts the live owner correction that the unrestricted FEI lower bound is already `> 6.521845710923046575`; the earlier Hod-scale target is obsolete for full FEI.

## 1. Before / target / headline

For a nonconstant Boolean function `f`, put

\[
\rho_0(f)=\min_{i:\operatorname{Inf}_i(f)>0}
\frac{\Delta_i H(f)}{\operatorname{Inf}_i(f)},
\qquad
\Delta_iH(f)=H(f)-\frac{H(f_{i,+})+H(f_{i,-})}{2}.
\]

A dimension-independent bound on `rho_0` would prove FEI by restriction induction. The newest project note before this run reports a search witness around `rho_0=6.3148`; the older width-two-tribes benchmark is `6.003746...`. `APPROACHES.md` route 5 explicitly asks for a Boolean family with `rho_0>7` as a decisive test of the potential-free route.

**New result.** Let `G` be Numaro's published balanced monotone 18-variable seed (published truth-table SHA-256
`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`) and define recursively on fresh disjoint blocks

\[
F_1=G,\qquad F_{r+1}=G(F_r^{(1)},\ldots,F_r^{(18)}).
\tag{1}
\]

A general exact one-coordinate composition recursion proved below, followed by a rational-log certificate, gives

\[
\boxed{\rho_0(F_5) > 7.096060618744925556394954995917.}
\tag{2}
\]

`F_5` is a finite Boolean function on `18^5 = 1,889,568` variables. Every relevant coordinate is covered; (2) is not a large value at one selected coordinate. Already

\[
\rho_0(F_4)>7.051852835007350697107979721615
\]

on `104,976` variables, so route 5's requested `>7` obstruction occurs at finite depth four.

This does **not** show `sup_f rho_0(f)=infinity`; the values through depth five remain bounded. It does show that every potential-free restriction induction with a universal step constant below `7.0960606...` is impossible.

## 2. Exact one-coordinate recursion for balanced block composition

This is the mathematical step used by the certificate.

Let `G:{-1,1}^m->{-1,1}` be balanced. Write

\[
a_i=\operatorname{Inf}_i(G),\qquad s_i=|\widehat G(\{i\})|,
\qquad H_G=H(G),\qquad I_G=I(G).
\]

For `K subseteq [m]\\{i}`, abbreviate

\[
a_K=\widehat G(K),\qquad b_K=\widehat G(K\cup\{i\}).
\]

For `q in [0,1]`, define the **one-coordinate biased spectral entropy**

\[
\widetilde H_i(q)
=H\!\left(\left\{(a_K+q b_K)^2,(1-q^2)b_K^2:K\subseteq[m]\setminus\{i\}\right\}\right),
\tag{3}
\]

where zero masses are omitted. Booleanity gives total mass one. Finally set

\[
K_i(q)=H_G-\frac{\widetilde H_i(q)+\widetilde H_i(-q)}2
       +a_i h_2(q^2).
\tag{4}
\]

Consider the recursion (1) for any balanced outer seed `G`. Fix a physical leaf coordinate. Suppose at depth `r` its influence is `p`, the magnitude of the singleton Fourier coefficient is `q`, and its restriction decrement is `Delta`. If, at the next outer level, that copy of `F_r` is inserted in logical coordinate `i` of `G`, then

\[
\boxed{
 p'=a_i p,\qquad q'=s_iq,\qquad
 \Delta'=a_i\Delta+K_i(q).
}
\tag{5}
\]

Hence, when `p>0`,

\[
\frac{\Delta'}{p'}=
\frac{\Delta}{p}+\frac{K_i(q)}{a_i p}.
\tag{6}
\]

### Proof of (5)

Only one inner block is changed by fixing the leaf. Let the two restrictions of that inner function have means `+q` and `-q`; they are opposite because the unconditioned inner function is balanced. For a generic mean `mu`, rewrite the outer uniform Fourier pair

\[
a_K+b_K z_i
=(a_K+\mu b_K)+\sqrt{1-\mu^2}\,b_K\,
\frac{z_i-\mu}{\sqrt{1-\mu^2}}.
\]

Thus the biased outer spectral weights are exactly the two masses in (3). If the special inner restriction is `h`, its nonempty normalized spectral entropy is

\[
H^+(h)=\frac{H(h)-h_2(\mu^2)}{1-\mu^2}.
\]

The biased influence of outer coordinate `i` is `(1-mu^2)a_i`, so its inner entropy contribution is exactly

\[
a_i\,[H(h)-h_2(\mu^2)].
\]

For another logical coordinate `j`, the biased influence is a quadratic expression in `mu`; its term linear in `mu` changes sign when `mu` changes from `+q` to `-q`. Therefore, after averaging the two physical restrictions, the total coefficient multiplying the unchanged entropy `H(F_r)` over all `j != i` is exactly `I_G-a_i`. No symmetry assumption is needed for this cancellation.

Since balanced disjoint composition also gives

\[
H(F_{r+1})=H_G+I_GH(F_r),
\]

subtracting the average child entropy gives

\[
\Delta' = a_i\Delta+H_G-\frac{\widetilde H_i(q)+\widetilde H_i(-q)}2+a_i h_2(q^2),
\]

which is (5). Influence multiplication gives `p'=a_i p`. Balanced Fourier factorization gives `q'=s_iq`. QED.

This proof is an identity; it uses no FEI assumption and no every-coordinate payment claim.

## 3. Specialization to the published 18-variable seed

The verifier independently reconstructs all `2^18` values of Numaro's external seed from the project-preserved ten slices and rejects unless the whole truth-table SHA-256 equals the published digest above. Integer Walsh arithmetic then gives two exact coordinate classes:

* nine core coordinates `C` with
  \[
  a_C=s_C=57/256;
  \]
* nine auxiliary coordinates `A` with
  \[
  a_A=s_A=1/256.
  \]

The seed is balanced and has exact total influence `261/128`. The verifier also checks that all coordinates in each advertised class have identical exact child squared-Walsh multisets, and, for every bias `q` reached through depth five, identical exact biased squared-mass multisets. This reduces all `18^r` physical leaves to the `2^r` class paths in `{C,A}^r` without discarding any coordinate.

Here `s_i=a_i`, so along every class path the singleton magnitude equals the leaf influence: `q=p`. Starting from the exact depth-one child spectra and iterating (6), the certified minima are

| depth `r` | variables | minimizing class path | certified lower bound for `rho_0(F_r)` |
|---:|---:|:---:|---:|
| 1 | 18 | `C` | `4.552314588405312149574520855739` |
| 2 | 324 | `CC` | `6.329015279480452454420605168315` |
| 3 | 5,832 | `CCC` | `6.890112313700557073165093644989` |
| 4 | 104,976 | `CCCC` | `7.051852835007350697107979721615` |
| 5 | 1,889,568 | `CCCCC` | `7.096060618744925556394954995917` |

All 32 class paths at depth five are present in `recursive_selector_verification.json`; the displayed interval for the minimum has width below `1e-30`.

For clarity, the global FEI ratios are computed separately. At depth five,

\[
6.336826070786839252084118443363
< \frac{H(F_5)}{I(F_5)} <
6.336826070786839252084118443364.
\]

So the new `7.096...` number is an **existential restriction-step obstruction**, not a claim that `H/I` itself is `7.096`.

## 4. Direct erasure-selector implication

Use the exact recovered decomposition

\[
\Delta_iH=B_i+JS_i,
\qquad B_i=H(S_i\mid S_{-i}),
\]

and the proved pointwise bound

\[
JS_i\le \frac{2}{\ln2}\min(p_i,1-p_i),
\qquad p_i=\operatorname{Inf}_i.
\tag{7}
\]

Every leaf influence of `F_5` is at most `(57/256)^5<1/2`. Therefore (2) and (7) imply, **for every physical coordinate of the same finite `F_5`**,

\[
\frac{B_i}{p_i}
>
7.096060618744925556\ldots-\frac2{\ln2}
>
\boxed{4.210670536966998\ldots}.
\tag{8}
\]

Consequently, with `B(F)=sum_i B_i`,

\[
\boxed{\frac{B(F_5)}{I(F_5)}>4.210670536966998\ldots.}
\tag{9}
\]

This strictly advances the newest measured erasure frontier on master, whose largest tested-family value was about `3.607` (width-two tribes). It is a proved lower bound from a finite Boolean construction, not a claim of optimality.

Equivalently, if

\[
K_E=\sup_f\min_{i:p_i>0}\frac{B_i}{p_i},
\]

then this certificate gives

\[
K_E>4.210670536966998\ldots.
\tag{10}
\]

Thus the simple route “prove some coordinate has `B_i <= (C-2/ln2)p_i` and then pay JS by `2/ln2`” cannot establish any universal FEI constant `C <= 7.0960606187...`. A sharper proof must exploit cancellation/correlation between the erasure and JS terms, add a genuine potential, or use a nonlocal stopping rule. This preserves the distinction between an existential selector and the known-false every-prescribed-coordinate payment proposal.

## 5. What changed relative to the fresh frontier

**Before.** The live `APPROACHES.md` route 5 recorded `rho_0=6.0037` for width-two tribes and explicitly proposed searching for `rho_0>7`. The newest concurrent step-constant note had pushed a search witness to about `6.3148` and measured `B/I` up to about `3.607`. Separately, the owner correction recovered Numaro's public lower bound `C_FEI>6.521845710923046575`, but that seed had not yet been converted into a restriction-step obstruction in this B14 line.

**After.** The exact recursion (5) turns that external balanced seed into a finite recursive family with certified `rho_0(F_4)>7.05` and `rho_0(F_5)>7.096`, and simultaneously forces `B(F_5)/I(F_5)>4.21067`. Therefore the previous `6.0--6.3` potential-free benchmark was not close to the true obstruction even among explicit monotone recursive functions.

**Remaining universal obligation.** Full FEI remains open. The result does not show `rho_0` unbounded. The next useful B14 question is now different: determine whether `rho_0(F_r)` for this seed converges to a finite value (the all-core path numerically continues upward), and, more importantly, identify a potential or stopping payment that cancels the recursively generated `K_i(q)` term instead of paying it locally. Any proposed erasure selector should first survive `F_4/F_5`.

## 6. Failed/retired routes preserved

* The prior top-flip/symmetric-orbit perturbation around width-two tribes remains a valid finite negative search, but it is no longer the relevant numerical frontier for `rho_0`; recursive balanced composition is stronger.
* The stronger every-coordinate payment proposal remains false in general and is not used here. The statement in (2) happens to hold at every coordinate of one constructed function because all 32 path classes were certified; it is not promoted to a universal quantifier.
* A large `rho_0` does not refute FEI. It refutes only a too-small **potential-free restriction-step constant**.
* The external seed's `6.521845...` lower bound is prior work; this report does not rename it as a new FEI lower bound.

## 7. Literature check and provenance

A fresh public check on 21 September 2026 finds the FEI constant page still listing the conjecture as open and Numaro's certified `>6.521845710923046575` as the best recorded lower bound. González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) explicitly develop the restriction-decrement/stopping-tree mechanism, making a large lower bound on the local step constant directly relevant prior art. Potapov (arXiv:2609.21563, 18 September 2026) proves FEI for plateaued functions with sharp class constant 4, a structured-class result rather than full FEI. I did not locate this exact recursive `rho_0` computation in the bounded search. **That is not evidence of novelty; publication priority remains UNVERIFIED.**

## 8. Reproducibility

Delivered beside this report:

* `verify_recursive_selector.py` — source SHA-256 `bbb649e8e71cfb3443547e4289864f6c1c10efde21cf9eb009069aca72818186`.
* `recursive_selector_verification.json` — actual output SHA-256 `cb8bb701b25bb0f1e133717d5cdd5d5d221d5fea6eb766a81a28eb999ebfd3bc`.

The verifier uses integer Walsh transforms and `fractions.Fraction`. For every logarithm in a strict reported inequality it normalizes the positive integer argument to `[1,2)`, applies the exact atanh series for `ln`, and encloses the tail by a rational geometric bound; `ln 2` is enclosed the same way. Forty terms are used. Floating point is not used to certify the headline inequalities.

The script was executed successfully in this invocation. It independently reconstructs the external seed and verifies the published whole-table hash before using it. No exhaustive `2^(18^5)` truth table is materialized; (5) is the proof that makes the finite recursive certificate possible.
