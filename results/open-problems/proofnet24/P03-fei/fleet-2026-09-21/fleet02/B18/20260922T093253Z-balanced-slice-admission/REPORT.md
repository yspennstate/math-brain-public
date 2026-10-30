# fleet02/B18 — balanced-slice admission theorem and Campaign-C redirect

**Run:** `B18-20260922T093253Z-r11b`  
**Classification:** `ESSENTIAL_STEP_APPLIED / ADMISSION_GATE_FAIL_REDIRECT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Version and control reconciliation

Fresh owner control revision `2026-09-22.2` keeps B12--B18 on FEI and supersedes conflicting earlier Campaign-C mathematical duties by the all-gate convergence target. The older C programme's positive-current/R16-only closure was already source-exactly refuted on the half-band Boolean family, and the execution reset itself requires C to redirect after repeated failure of its admission gate. I therefore preserve that failed signed-NET history rather than silently resurrecting it.

The last completed own B18 report was

`fleet02/B18/20260922T090632Z-safe-ray-zero-set/REPORT.md`,

which proved the strict interior zero set of a universally safe repair direction and introduced `SAFE-RAY-COERCIVITY-v1`. The newest compatible completed **OTHER-account** result consumed and applied here is fleet03/B18

`fleet03/B18/20260922T092424Z-quartic-safe-cone-frontier/REPORT.md`, report blob `0db03e32e6bb040ddb17ef096a50ffa3bcfe597a`.

It replaces the refuted fixed candidate by

\[
\Gamma_Q(u)=\Gamma^\dagger(u)+\lambda_Q\eta_4(u),
\qquad
\lambda_Q={58551\over200000},
\]
\[
\eta_4(u)=u(1-u)(1-2u(1-u)),
\qquad
C_Q:=\Gamma_Q(1/2)=6.558445589,
\tag{0.1}
\]

and gives the exact common Shannon residual `B-GIBBS-Q4-v1`

\[
D_{\Gamma_Q}(G;p)=V_q R_Q(G;p),
\tag{0.2}
\]

with all original-coordinate Gibbs prices and the full conditional KL credit retained. It rigorously repairs the strongest currently source-certified biased Numaro obstruction while worsening no gate, but leaves universal `R_Q\ge0` unpaid.

A second completed **OTHER-account** result used below is fleet03/B18

`fleet03/B18/20260922T0857Z-balanced-iprojection-parity/REPORT.md`.

Its Theorem 2.1 proves the same-constant equivalence

\[
\boxed{
H(g)\le C I(g)\ \forall g
\iff
H(f)\le C[I(f)-1]\ \forall\text{ balanced }f.
}
\tag{0.3}
\]

It also gives the exact balanced I-projection identity

\[
H(f)=H_{\max}(r)-K_{\rm occ}(f),
\tag{0.4}
\]

with a genuine signed-Boolean complement-parity lower bound on `K_occ`, but no dimension-independent closing payment.

## 1. Compact conditional deduction to full FEI

The current smallest honest chain is:

1. **PROVED:** for every nonconstant Boolean gate and interior product bias, `B-GIBBS-Q4-v1` satisfies the exact identity (0.2). No KL/JS credit or coordinate label is discarded.
2. **PROVED:** the quartic direction in (0.1) is universally gate-safe, and the chosen rational scale repairs the strongest currently certified Numaro biased prime witness.
3. **UNPAID:** prove `R_Q(P;p)\ge0` for every finite composition-prime Boolean gate `P`, every interior product bias, and the required boundary limits.
4. **CONDITIONAL:** the existing composition/base-case theorem then gives the all-gate inequality for `Gamma_Q`, hence full FEI with finite constant `C_Q`.

The purpose of this run is to enforce the admission gate on step 3: determine whether the new safe-potential machinery actually reduced the universal difficulty, or merely reparameterized it.

## 2. Main theorem: every finite-center gate potential collapses to balanced excess FEI at the cube center

### Theorem 2.1 — `CENTER-SLICE-ADMISSION-v1`

Let `Gamma` be any symmetric finite potential used in the all-gate defect

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p).
\tag{2.1}
\]

Put

\[
C=\Gamma(1/2).
\]

For every balanced Boolean function `f` under uniform inputs,

\[
\boxed{
D_\Gamma(f;1/2,\ldots,1/2)
=C[I(f)-1]-H(f).
}
\tag{2.2}
\]

Consequently, universal nonnegativity of the all-gate defect on the balanced-uniform slice is equivalent, with the **same constant `C`**, to unrestricted FEI.

### Proof

At uniform input bias,

\[
V_{1/2}=1,
\qquad h_2(V_{1/2})=h_2(1)=0,
\qquad
{\operatorname{It}_i(f)\over V_{1/2}}=\operatorname{Inf}_i(f).
\]

Because `f` is balanced, its output bias is also `1/2`, and the biased Fourier entropy in (2.1) is the ordinary spectral entropy `H(f)`. Therefore

\[
\begin{aligned}
D_\Gamma(f;1/2^n)
&=\sum_i \operatorname{Inf}_i(f)\,\Gamma(1/2)
-\Gamma(1/2)-H(f)\\
&=C[I(f)-1]-H(f),
\end{aligned}
\]

which is (2.2).

If this quantity is nonnegative for every balanced Boolean `f`, fleet03/B18's same-constant theorem (0.3) gives `H(g)\le C I(g)` for every Boolean `g`. Conversely unrestricted FEI at constant `C` implies the balanced-excess inequality by the other direction of (0.3). `QED`

### Interpretation

Equation (2.2) is independent of the shape of `Gamma` away from `1/2`. A universally safe perturbation can repair biased gate constraints by changing the shape, but on balanced uniform gates it can only act through its **center increment**. Thus no safe-ray, spline, quartic, or other off-center potential shaping is by itself a smaller balanced-uniform proof problem.

This is an admission theorem, not a refutation of the all-gate method. It says exactly where the full difficulty remains.

## 3. Exact collapse of the preceding `SAFE-RAY-COERCIVITY-v1`

The preceding B18 report used

\[
\eta_*(u)={1\over8}\left[1-(1-2u)^4-{1\over36}(1-(1-2u)^2)^2\right],
\]

so

\[
\eta_*(1/2)={35\over288}.
\tag{3.1}
\]

For balanced uniform `f` with `I(f)>1`, its safe energy is therefore exactly

\[
E_*(f;1/2^n)={35\over288}[I(f)-1].
\tag{3.2}
\]

Since

\[
D_{\Gamma^\dagger}(f;1/2^n)
=C^\dagger[I(f)-1]-H(f),
\qquad C^\dagger=6.521851214,
\]

the quotient from `SAFE-RAY-COERCIVITY-v1` satisfies the exact identity

\[
\boxed{
\tau(f;1/2^n)
={288\over35}
\left[{H(f)\over I(f)-1}-C^\dagger\right]_+.
}
\tag{3.3}
\]

Let

\[
C_{\rm bal}:=\sup_{f\ \mathrm{balanced},\ I(f)>1}{H(f)\over I(f)-1}.
\]

Then

\[
\boxed{
\sup_{f\ \mathrm{balanced}}\tau(f;1/2^n)
={288\over35}[C_{\rm bal}-C^\dagger]_+.
}
\tag{3.4}
\]

By (0.3), `C_bal<infinity` is exactly unrestricted FEI. Hence the balanced-uniform subproblem of `SAFE-RAY-COERCIVITY-v1` was already equivalent to the full conjecture; the strict zero-set theorem removed a denominator pathology but did **not** create a smaller universal coercivity lemma.

This is the precise admission-gate correction to the preceding B18 mechanism.

## 4. Application to the newest quartic candidate and common Gibbs residual

For the completed fleet03/B18 direction

\[
\eta_4(u)=u(1-u)(1-2u(1-u)),
\]

we have

\[
\eta_4(1/2)={1\over8}.
\tag{4.1}
\]

Therefore its balanced-uniform defect currency is

\[
\sum_i\operatorname{Inf}_i(f)\eta_4(1/2)-\eta_4(1/2)
={I(f)-1\over8}.
\tag{4.2}
\]

For the actual candidate (0.1), Theorem 2.1 gives

\[
\boxed{
D_{\Gamma_Q}(f;1/2^n)
=C_Q[I(f)-1]-H(f),
\qquad C_Q=6.558445589.
}
\tag{4.3}
\]

Because the exact Gibbs normalization (0.2) has `V_q=1` on this slice,

\[
\boxed{
R_Q(f;1/2^n)=C_Q[I(f)-1]-H(f).
}
\tag{4.4}
\]

Thus the new `B-GIBBS-Q4-v1` residual is source-exact and useful, but its balanced-uniform universal inequality is **not a weaker target than FEI**. It is FEI at `C_Q` written in an exact Shannon/I-projection coordinate system.

Substituting fleet03/B18's balanced I-projection identity (0.4), (4.4) becomes

\[
\boxed{
R_Q(f;1/2^n)
=K_{\rm occ}(f)+C_Q(\mu-1)-H_{\max}(r),
\qquad \mu=I(f).
}
\tag{4.5}
\]

Therefore the first genuinely informative signed implication on the balanced slice is not another potential-shape adjustment. It is the exact Boolean dependence payment

\[
\boxed{
K_{\rm occ}(f)
\ge H_{\max}(r)-C_Q(\mu-1)
}
\tag{4.6}
\]

whenever the right-hand side is positive, with original coordinate labels and signed Boolean realizability retained. Fleet03/B18's complement-parity theorem supplies a strictly positive but generally dimension-dependent part of this payment; it does not yet prove (4.6).

This identifies the correct Campaign-B handoff target without renaming a residual as progress.

## 5. Strong biased witness: what the safe directions did accomplish

The newest peer package also confirms that potential shaping is not useless: it repairs a genuine **biased** obstruction.

For the strong 18-input Numaro gate at

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}=1/2,
\]

the old seed has certified defect below `-0.038023734`. The previous tilted direction has exact currency

\[
D_{\eta_*}
={7405187762554608605\over58643094782223581184},
\]

so even to repair this one witness its scale must satisfy

\[
T>{0.038023\over D_{\eta_*}}
=0.30111139168944795\ldots,
\]

forcing center above

\[
6.558444612295593\ldots .
\tag{5.1}
\]

The newer quartic safe-cone optimization is slightly more efficient: the completed fleet03/B18 theorem proves that pure quartic is optimal inside `cone{eta_2,eta_4}` for this witness, forcing center above

\[
6.558445486109393\ldots
\tag{5.2}
\]

under its stronger certified deficit interval, and chooses the rational candidate

\[
C_Q=6.558445589
\]

with rigorous positive witness slack exceeding `1.05909e-7`.

So the safe-shape work has genuinely removed the known biased prime obstruction. The new theorem here says that this success does not pay the balanced-uniform universal quantifier.

## 6. Campaign-C admission gate and redirect

The older Campaign-C signed compiler route had already failed its prescribed admission gate: the all-Boolean positive-current budget was refuted on the half-band Boolean source, no complete source-exact NET inequality with all R16/entropy/terminal credits was proved, and subsequent C work moved through several incompatible repair mechanisms. Later owner control then converged the fleet on the all-gate formulation.

The immediately preceding B18 safe-ray mechanism also fails **as a reduction** by (3.4): its balanced coercivity statement is exactly FEI in disguise.

Therefore this lead now records the required redirect rather than spending another run tuning a C/ray coefficient:

**Redirect target:** fleet03/B18 `B-GIBBS-Q4-v1`, with balanced core statement (4.6), equivalently the source-current `B-BALANCED-IPROJECTION-v1` dependence-credit payment. The next substantive attack must use signed Boolean structure to pay coordinate-labelled KL/degree-price leakage, or produce an actual Boolean counterexample to `Gamma_Q`. It must not discard KL/JS credits, replace the spectral law by an arbitrary unsigned law, or count a finite check as universal closure.

This handoff is mathematical only. No other account's scheduler, prompt, task, or artifact is modified.

## 7. Last-three substantive B18 comparison

The last three completed substantive B18 reports were:

1. `20260922T051105Z-random-depth-barycenter`: exact signed random-depth cocycle/front-loading; terminal-scale criterion corrected as circular.
2. `20260922T080607Z-center-bank-dual-tradeoff`: exact center-versus-AND-bank positive dual for shaped repairs; later genuine nonuniform slack showed that bank-spending obstruction was not decisive.
3. `20260922T090632Z-safe-ray-zero-set`: universally safe direction, strict constant/literal zero set, and coercivity quotient.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is proved.

**MECHANISM CHANGE:** `safe-ray coercivity as a putative reduced universal lemma -> exact balanced-slice admission theorem plus redirect to signed Boolean I-projection/KL payment`. The before/after is exact: before, finiteness of the safe-ray quotient was treated as a potentially smaller remaining arrow; after (3.3)-(3.4), its balanced slice is proved equivalent to unrestricted FEI, so it cannot be advertised as a reduction.

## 8. Verification and scope

The adjacent exact-Fraction checker verifies:

- `eta_*(1/2)=35/288`;
- `eta_4(1/2)=1/8`;
- the inherited strong-witness lower scale for the old tilted ray;
- the inherited quartic safe-cone center lower bound;
- `C_Q=6.558445589` exactly; and
- the positive strong-witness slack for the rational quartic scale.

The mathematical identities (2.2), (3.3), and (4.4) are analytic and do not depend on the checker.

No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, email/Drive material, public posting, paid API/model/Codex call, remote workflow, or permission change was used or written. Repository authentication supplied source access only; no native mathematical-brain receiver/query was used, so execution remains `WITHOUT_VERIFIED_BRAIN`.
