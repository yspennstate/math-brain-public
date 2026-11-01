# fleet01/B06 — balanced extremal slack ledger and restriction/suspension separation

**Run:** `b06-20260922T103931Z-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / BALANCED_EXTREMAL_SLACK_LEDGER / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Fresh owner-control reconciliation

The fresh owner control is `FEI-ALL-TEAM-20260922T095941Z`, revision `2026-09-22.3`. It assigns all eighty existing workers to the full uniform-cube Fourier entropy–influence conjecture and assigns fleet01/B06 the task **Balanced extremal restriction structure**. It explicitly suspends new BT4 work while preserving the earlier BT4 artifacts. Therefore this run follows the newer owner order rather than the older BT4 prompt cached in the scheduled task.

The current fleet01/B06 target is to derive a structural consequence of extremizing

\[
\rho(f):={H(f)\over I(f)-1}
\]

among balanced genuine Boolean descendants or suspensions, while keeping distinct:

1. a genuinely balanced physical restriction;
2. character suspension of an arbitrary raw restriction;
3. the raw physical restriction itself.

The partner fleet02/B06 current all-team deliverable was not yet present at the latest source check, so this run follows the programme's asynchronous rule and uses completed source-pinned results instead of waiting.

## 1. Source-pinned inputs actually used

### BALANCED

`yspennstate/math-open-problems`, commit
`7d20a4bb4067085af7c5e7c9a82aef31998a7d36`,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T093253Z-balanced-slice-admission/REPORT.md`.

It proves that for a balanced uniform Boolean function and a finite-center gate potential with center `C`,

\[
D_\Gamma(f)=C[I(f)-1]-H(f),
\]

and that bounding `H(f)/(I(f)-1)` over balanced functions is equivalent, at the same constant, to ordinary uniform-cube FEI.

### IPROJ

`yspennstate/math-open-problems`, commit
`4bd6d05f1eb8325d665f2748f4d74dcee2550a04`,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For the actual nonempty spectral law `P`, its coordinate-occurrence vector `r`, and the maximum-entropy conditional-product law `Q_r`, it gives

\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\]

and the exact all-gate decomposition `R_Gamma=B_inf^Gamma+K_occ`.

### EQUALITY

`yspennstate/math-open-problems`, commit
`84c69136ca6b008badb76f15bf1071d029c927aa`,

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`.

On the balanced uniform slice it classifies `K_occ=0` exactly as

\[
f=\chi_F b(x_A),
\]

with `F` nonempty and `b` bent on an even coordinate set `A`.

### HIERARCHY — named OTHER-account theorem applied in the main proof

`yspennstate/math-open-problems`, commit
`2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`.

For a disjoint composition `F=G(f_1,...,f_m)`, with outer nonempty spectral law `P_0`, block occurrence weights `alpha_i`, and child nonempty spectral laws `P_i`, it proves the exact source factorization

\[
P_F(T,(S_i)_{i\in T})=P_0(T)\prod_{i\in T}P_i(S_i),
\]

and therefore

\[
H(P_F)=H(P_0)+\sum_i\alpha_i H(P_i).
\]

It also proves

\[
K_{\rm occ}(F)=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},
\qquad C_{\rm hier}\ge0,
\]

so no hierarchy credit may be silently discarded.

### SELECTOR_DEBIT

`yspennstate/math-open-problems`, commit
`4ccd51ad517f425a529daa52c3352905b86ea69d`,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2–4 only. Its Section 5 quadratic candidate is superseded/refuted and is not used here.

For a genuine physical selector split with selector bias `s`, child disagreement probability `d`, and conditional spectral entropy increment `Delta_i \widetilde H`, it proves

\[
\Delta_i\widetilde H-dh_2(V_s)
\le h_2(d)+{2\over\ln2}\min\{d,1-d\}.
\tag{1.1}
\]

The underlying exact entropy decomposition is also available in fleet01/B12 commit
`92c75e9bcd2fe9c5dc2bedc8a032b31b4afb5484`, report
`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260922T090347Z-folded-js-shannon/REPORT.md`.

## 2. Character suspension: the exact denominator conversion

For an arbitrary Boolean function

\[
g:\{-1,1\}^n\to\{-1,1\},
\]

introduce a fresh uniform coordinate `y` and define its character suspension

\[
\Sigma g(y,x)=y g(x).
\]

Then `Sigma g` is balanced and multiplication by the fresh character simply translates Fourier support:

\[
\widehat{\Sigma g}(S\cup\{y\})=\widehat g(S).
\]

Hence exactly

\[
H(\Sigma g)=H(g),
\qquad
I(\Sigma g)=I(g)+1,
\]

so

\[
\boxed{
{H(\Sigma g)\over I(\Sigma g)-1}={H(g)\over I(g)}.
}
\tag{2.1}
\]

For a fixed candidate ratio `rho`, define

\[
S_\rho(f):=\rho[I(f)-1]-H(f)
\]

for balanced `f`, and

\[
T_\rho(g):=\rho I(g)-H(g)
\]

for an arbitrary Boolean `g`. Equation (2.1) is equivalently

\[
\boxed{S_\rho(\Sigma g)=T_\rho(g).}
\tag{2.2}
\]

This is the exact bookkeeping distinction needed below: an arbitrary raw restriction is compared to a balanced extremizer through `T_rho`, not through `rho(I-1)-H`.

## 3. Main theorem A: exact suspension-slack ledger for a disjoint decomposition

### Theorem A — `BALANCED-EXTREMAL-SUSPENSION-LEDGER-v1`

Let `F` be a balanced Boolean function under uniform physical inputs and suppose it has a disjoint Boolean composition

\[
F=G(f_1,\ldots,f_m),
\]

with every displayed child nonconstant. The children may be biased. For child `i`, write

\[
v_i=1-(\mathbb E f_i)^2\in(0,1],
\]

let `P_i` be its nonempty squared spectral law, and put

\[
\mu_i=\mathbb E_{P_i}|S|,
\qquad
H_i=H(f_i),
\qquad
I_i=I(f_i).
\]

Let `P_0` be the outer nonempty spectral law at the actual child-output biases and

\[
\alpha_i=P_0(i\in T).
\]

Assume `I(F)>1` and put

\[
\rho={H(F)\over I(F)-1}.
\]

Finally define each child's suspension slack

\[
T_i:=\rho I_i-H_i.
\]

Then the following identity is exact:

\[
\boxed{
\sum_{i=1}^m {\alpha_i\over v_i}
\bigl[T_i+h_2(v_i)\bigr]
=H(P_0)+\rho.
}
\tag{3.1}
\]

#### Proof

Since the empty Fourier mass of `f_i` is `(E f_i)^2=1-v_i`, conditioning its squared spectral law on being nonempty gives

\[
H_i=h_2(v_i)+v_iH(P_i),
\qquad
I_i=v_i\mu_i.
\tag{3.2}
\]

The definition of `T_i` therefore gives

\[
H(P_i)
={H_i-h_2(v_i)\over v_i}
=\rho\mu_i-{T_i+h_2(v_i)\over v_i}.
\tag{3.3}
\]

Because `F` is balanced, its empty Fourier mass is zero. Apply the exact HIERARCHY source factorization. It gives

\[
H(F)=H(P_0)+\sum_i\alpha_iH(P_i),
\qquad
I(F)=\sum_i\alpha_i\mu_i.
\tag{3.4}
\]

On the other hand the definition of `rho` gives

\[
H(F)=\rho\left(\sum_i\alpha_i\mu_i-1\right).
\tag{3.5}
\]

Insert (3.3) into the entropy identity in (3.4) and compare with (3.5). The terms `rho sum_i alpha_i mu_i` cancel exactly, leaving (3.1). QED.

### Corollary A1 — a genuine bias-toll exclusion for extremizers

If `F` is extremal relative to the character suspensions of all its children, i.e.

\[
{H(\Sigma f_i)\over I(\Sigma f_i)-1}
={H_i\over I_i}\le\rho
\]

for every essential child, then `T_i>=0` by (2.2). Therefore (3.1) yields

\[
\boxed{
\sum_i {\alpha_i\over v_i}h_2(v_i)
\le H(P_0)+\rho.
}
\tag{3.6}
\]

This excludes every disjoint decomposition whose child-bias toll violates (3.6), without assuming FEI.

There is also an individual variance floor. Since

\[
\phi(v):={h_2(v)\over v}
\]

has derivative

\[
\phi'(v)={\log_2(1-v)\over v^2}<0,
\qquad 0<v<1,
\]

with `phi(v)->infinity` as `v downarrow0`, every essential child obeys

\[
\phi(v_i)\le {H(P_0)+\rho\over\alpha_i}.
\tag{3.7}
\]

Thus a child that is seen by the outer nonempty spectrum with occurrence weight bounded below cannot have arbitrarily small output variance inside such an extremal decomposition.

This is a nontrivial structural restriction on a putative extremizer and is the first main acceptance result of this run.

## 4. Balanced factors: exact co-extremality and a composition-prime reduction

The preceding theorem allows biased children. When the factorization is balanced at every level, the slack ledger becomes even sharper.

### Corollary B — `BALANCED-FACTOR-COEXTREMALITY-v1`

Assume in addition that the outer gate `G` is balanced under uniform inputs and every child `f_i` is balanced. Then

\[
\boxed{
S_\rho(F)
=S_\rho(G)+\sum_i\operatorname{Inf}_i(G)S_\rho(f_i).
}
\tag{4.1}
\]

#### Proof

For balanced children, `v_i=1`, `P_i` is their full squared spectral law, and the outer block occurrence probability is

\[
\alpha_i=\operatorname{Inf}_i(G).
\]

The exact composition formulas are

\[
H(F)=H(G)+\sum_i\alpha_iH(f_i),
\qquad
I(F)=\sum_i\alpha_iI(f_i),
\qquad
I(G)=\sum_i\alpha_i.
\]

Expanding the right side of (4.1) and using the last identity gives exactly `rho[I(F)-1]-H(F)`. QED.

If `F` is a `rho`-extremizer relative to `G` and all balanced children, then every term on the right of (4.1) is nonnegative. Since `S_rho(F)=0`, every term must vanish:

\[
S_\rho(G)=0,
\qquad
S_\rho(f_i)=0
\quad\text{whenever }\operatorname{Inf}_i(G)>0.
\tag{4.2}
\]

Consequently, a minimum-dimensional balanced `rho`-extremizer cannot admit a nontrivial disjoint composition into smaller balanced essential factors: any non-dictator essential factor would itself be a smaller `rho`-extremizer. Dictator/irrelevant insertions are the only trivial exceptions.

This is a genuine balanced composition-prime reduction. It does not claim arbitrary biased prime-gate reduction; Theorem A shows the exact extra bias toll that must be retained there.

## 5. Balanced physical restrictions: disagreement is quantitatively capped

Define

\[
\Phi(d):=h_2(d)+{2\over\ln2}\min\{d,1-d\},
\qquad 0\le d\le1.
\tag{5.1}
\]

### Theorem C — `BALANCED-SPLIT-DISAGREEMENT-CAP-v1`

Let `F` be balanced, `I(F)>1`, and

\[
\rho={H(F)\over I(F)-1}.
\]

Fix a uniform physical coordinate `i` such that both raw restrictions `F_+` and `F_-` are themselves balanced. Put

\[
d=\Pr[F_+\ne F_-]=\operatorname{Inf}_i(F).
\]

Assume `F` is extremal relative to these two balanced restrictions, so

\[
s_\pm:=\rho[I(F_\pm)-1]-H(F_\pm)\ge0.
\tag{5.2}
\]

Then

\[
\boxed{
\Delta_iH
:=H(F)-{H(F_+)+H(F_-)\over2}
=\rho d+{s_++s_-\over2},
}
\tag{5.3}
\]

and therefore

\[
\boxed{
0\le {s_++s_-\over2}
\le \Phi(d)-\rho d.
}
\tag{5.4}
\]

In particular

\[
\boxed{\Phi(d)\ge\rho d.}
\tag{5.5}
\]

#### Proof

The uniform physical restriction identity for influence is

\[
I(F)=d+{I(F_+)+I(F_-)\over2}.
\tag{5.6}
\]

Since `S_rho(F)=0`, direct subtraction gives

\[
{s_++s_-\over2}
=\Delta_iH-\rho d,
\]

which is (5.3).

The exact selector-debit theorem (1.1), at the uniform selector `s=1/2`, has `V_s=1` and `h_2(V_s)=0`; hence

\[
\Delta_iH\le\Phi(d).
\tag{5.7}
\]

The exact packet decomposition also gives `Delta_iH>=0`. Combining (5.2), (5.3), and (5.7) proves (5.4)–(5.5). QED.

### A one-parameter forbidden region

For `d in (0,1]`, the ratio `Phi(d)/d` is strictly decreasing. Indeed,

\[
{d\over dd}{h_2(d)\over d}
={\log_2(1-d)\over d^2}<0.
\tag{5.8}
\]

On `(0,1/2]`, the second term of `Phi(d)/d` is the constant `2/ln2`; on `[1/2,1)` it is

\[
{2\over\ln2}{1-d\over d},
\]

which is also strictly decreasing. Moreover

\[
{\Phi(d)\over d}\to\infty\quad(d\downarrow0),
\qquad
{\Phi(d)\over d}\to0\quad(d\uparrow1).
\]

Therefore, for every `rho>0`, there is a unique

\[
\delta(\rho)\in(0,1)
\quad\text{such that}\quad
\Phi(\delta(\rho))=\rho\delta(\rho),
\tag{5.9}
\]

and Theorem C yields

\[
\boxed{d\le\delta(\rho).}
\tag{5.10}
\]

If equality holds in (5.10), then (5.4) forces

\[
s_+=s_-=0,
\]

so both balanced children are themselves co-extremal and the selector-debit bound is tight.

For orientation only, majority on three bits has

\[
H=2,\qquad I=3/2,\qquad {H\over I-1}=4.
\]

Thus any actual global balanced maximizer, if one exists, has `rho>=4`. The implicit rigorous bound is therefore

\[
d\le\delta(4),
\quad
\Phi(\delta(4))=4\delta(4).
\]

A numerical solve gives `delta(4) approximately 0.5626459040`; this decimal is illustrative, while (5.9)–(5.10) are the analytic statement.

## 6. Raw restrictions are different: exact suspension ledger and a genuine overreach counterexample

The previous theorem requires the raw restrictions themselves to be balanced. That hypothesis cannot be dropped.

### Theorem D — `RAW-RESTRICTION-SUSPENSION-LEDGER-v1`

Keep `F`, `rho`, `i`, and `d` as above, but allow `F_+` and `F_-` to be biased. Compare them to the parent only through their character suspensions and define

\[
t_\pm:=\rho I(F_\pm)-H(F_\pm)
=S_\rho(\Sigma F_\pm).
\tag{6.1}
\]

If the parent is extremal relative to these suspensions, so `t_+,t_- >=0`, then the exact identity is

\[
\boxed{
{t_++t_-\over2}
=\Delta_iH+\rho(1-d).
}
\tag{6.2}
\]

Hence, using the selector theorem,

\[
\boxed{
\rho(1-d)
\le {t_++t_-\over2}
\le \rho(1-d)+\Phi(d).
}
\tag{6.3}
\]

#### Proof

By (5.6), the average child influence is `I(F)-d`. Thus

\[
\begin{aligned}
{t_++t_-\over2}
&=\rho[I(F)-d]-{H(F_+)+H(F_-)\over2}\\
&=\rho[I(F)-d]-H(F)+\Delta_iH\\
&=\rho(1-d)+\Delta_iH,
\end{aligned}
\]

because `H(F)=rho[I(F)-1]`. This is (6.2). The exact packet decomposition gives `Delta_iH>=0`, and (5.7) gives `Delta_iH<=Phi(d)`, proving (6.3). QED.

The extra term `rho(1-d)` is the exact unit of slack lost when a biased raw child is balanced by character suspension. It is not an artifact of the proof.

### Genuine Boolean counterexample to the false unrestricted descent

Let `g=AND_2` on two uniform bits, in either `+/-1` sign convention. Its four squared Fourier masses are all `1/4`, so exactly

\[
H(g)=2,
\qquad
I(g)=1,
\qquad
1-(\mathbb Eg)^2={3\over4}.
\tag{6.4}
\]

Suspend it by a fresh uniform character:

\[
F(y,x)=y g(x).
\]

Then `F` is balanced and

\[
H(F)=2,
\qquad
I(F)=2,
\qquad
\rho(F)=2.
\tag{6.5}
\]

Restricting `y` gives the two **biased** raw children `g` and `-g`. Their disagreement is

\[
d=1,
\]

and their suspension slacks at `rho=2` vanish exactly:

\[
2I(g)-H(g)=0.
\]

Also `Delta_yH=0`, so (6.2) is exact with both sides zero.

But if one incorrectly treated the raw child `g` as if it were balanced and applied the balanced-excess denominator, one would demand

\[
H(g)\le2[I(g)-1]=0,
\]

contradicting the exact value `H(g)=2`.

Thus the implication

> “balanced extremizer + arbitrary physical restriction implies nonnegative balanced child slack `rho(I-1)-H`”

is false even for a three-variable genuine Boolean character suspension. Any critical descent must either retain the raw-child bias term, use character suspension and pay (6.2), or prove that the selected physical restrictions are genuinely balanced.

As a consistency check, Theorem A is exact on this example. Regard `F` as the parity outer gate of the balanced literal `y` and the biased child `g`. The outer biased nonempty spectral law has masses `1/4` and `3/4`, so `H(P_0)=h_2(3/4)`. For the literal, `v_1=1`, `T_1=2`, `alpha_1=1`; for `g`, `v_2=3/4`, `T_2=0`, `alpha_2=3/4`. Hence (3.1) reads

\[
2+h_2(3/4)=\rho+H(P_0),
\]

which is an identity.

## 7. Zero-KL boundary is excluded above ratio two

The EQUALITY source gives every balanced `K_occ=0` function, after discarding irrelevant coordinates, as

\[
f=\chi_F b(x_A),
\]

with `F` nonempty and a bent function on even `m=|A|`. Its exact entropy and influence are

\[
H=m,
\qquad
I=|F|+{m\over2}.
\]

For every non-dictator member of this family,

\[
\boxed{
{H\over I-1}
={m\over |F|-1+m/2}\le2.
}
\tag{7.1}
\]

Therefore any balanced `rho`-extremal object with `rho>2` has

\[
\boxed{K_{\rm occ}>0.}
\tag{7.2}
\]

Since majority-three already realizes ratio `4`, a global balanced maximizer, if one exists, cannot lie on the zero-dependence boundary. This is compatible with, but does not replace, the quantitative KL-payment problem.

## 8. Conditional end-to-end route and the first unpaid implication

The current route can now be stated without conflating three different descendants.

1. BALANCED says that a finite bound on the balanced excess ratio `H/(I-1)` is already full uniform-cube FEI at the same constant.
2. In a hypothetical finite balanced extremal/critical obstruction, pass to a minimal-dimensional object inside whatever genuine descendant/suspension closure is actually justified.
3. Corollary B removes nontrivial **balanced disjoint decompositions**: every essential balanced factor would be a smaller co-extremizer.
4. Theorem C removes high-disagreement **balanced physical splits**: every such split satisfies `d<=delta(rho)`, and a boundary split produces two smaller co-extremizers.
5. Theorem A controls **biased disjoint decompositions** through the exact suspension/bias toll
   \[
   \sum_i {\alpha_i\over v_i}h_2(v_i)\le H(P_0)+\rho.
   \]
   In particular an outer-relevant child cannot have arbitrarily small output variance.
6. Equation (7.2) removes the exact `K_occ=0` boundary whenever `rho>2`.

The first essential missing implication is now the **biased raw-restriction case**. Character suspension changes the balanced denominator from `I-1` to `I`, and Theorem D shows that the exact price of this conversion is the term

\[
\rho(1-d).
\]

The `AND_2` suspension proves that this term cannot be deleted by an abstract extremality argument. A successful continuation must therefore use additional genuine source information — for example child output variance, the hierarchy KL `C_hier`, signed Boolean structure, or an exact balancing conversion — to recover enough of this lost unit, or prove that a relevant extremal split can be replaced by a balanced descendant/decomposition already covered by Theorems A–C.

That is strictly narrower than the pre-run statement “understand balanced extremal restrictions”: the balanced restriction and balanced factor branches now have exact structural closures, while the remaining obstruction is pinned to the quantitatively explicit suspension loss (6.2).

## 9. Honest outcome

**New proved statements in this run:**

- `BALANCED-EXTREMAL-SUSPENSION-LEDGER-v1`, equation (3.1), and its bias-toll exclusion (3.6);
- `BALANCED-FACTOR-COEXTREMALITY-v1`, equation (4.1), giving a balanced composition-prime reduction for a minimum-dimensional extremizer;
- `BALANCED-SPLIT-DISAGREEMENT-CAP-v1`, equations (5.3)–(5.10);
- `RAW-RESTRICTION-SUSPENSION-LEDGER-v1`, equations (6.2)–(6.3);
- a genuine Boolean `AND_2`-suspension counterexample to the false extension of balanced-child slack to arbitrary raw restrictions;
- the direct zero-KL consequence (7.1)–(7.2) from the source equality classification.

**Not proved:** full FEI, existence of a global maximizer, a dimension-independent quantitative neighborhood theorem around `K_occ=0`, or closure of the biased raw-restriction branch.

**Outcome label:** `ESSENTIAL_STEP_APPLIED / BALANCED_EXTREMAL_SLACK_LEDGER / FULL_FEI_OPEN`.
