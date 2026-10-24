Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# R7-05 admission-side peer check: I0129 cubic-branch compression and exact zero-fiber warning

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Own root: `research7_2026-09-17/R7-05/`  
Repository: private `yspennstate/math-open-problems`, branch `master`

**R7-05 target remains `PENDING_ADMISSION`. This is an independent peer-hypothesis check on the newly changed shard-4 target `I0129`, which is exclusively owned by PROB20-17. It is not an R7-05 claim, does not change I0129's metric, and does not reopen or duplicate that task.**

Methods used here: **B8 / B12 / B26**.

## 1. Why I0129 is the lawful strict-delta object to inspect

The preceding R7-05 report left a strict-delta cursor: do not rescan the static legacy shard-4 corpus absent a material source, ownership, lifecycle, or mathematical change. Between that report and the captured master for this invocation, no new free shard-4 CLOSABLE canonical claim appeared. The material shard-4 mathematical delta is instead the new I0129 report

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/rotations/I0129/runs/2026-09-19/2026-09-19T175600Z__report.md`,

which introduced an explicit post-cubic branch invariant `G_I` and split each clean component into a singular branch `Z | G_I` or a unit branch. The canonical claim `operations/claims/I0129.md` remains **CLAIMED / ADMITTED_ACTIVE / HARD OUTSIDE** by another native slot. The owner directive requires peer hypotheses/noncircularity checks, so the only action taken here is an independent mathematical check under R7-05's own root.

Current bounded literature checking still finds Singmaster's full uniform boundedness conjecture open; Kane's 2007 total bound remains the standard unconditional total bound, and the 2022 Matomäki–Radziwiłł–Shao–Tao–Teräväinen theorem is an interior result rather than full source closure. This is current search evidence, not a worldwide openness certificate.

## 2. Recovered cubic branch normal form

Use the notation of the current I0129 report. For a row `(k,r)` with `0 <= r < k`, put

\[
F_k(x)=\binom{x}{k},\qquad
\kappa_{k,r}=\frac1{F_k'(r)}=(-1)^{k-1-r}k\binom{k-1}{r}.
\]

Let

\[
s_1(k,r)=H_r-H_{k-1-r},
\qquad
s_2(k,r)=H_r^{(2)}+H_{k-1-r}^{(2)}.
\]

The inverse Taylor coefficients at the simple zero `r` give

\[
v_{k,r}:=\frac{\alpha_{k,r}}{\kappa_{k,r}}
=-s_1(k,r)\kappa_{k,r},
\]

and, for the third inverse coefficient,

\[
w_{k,r}:=\frac{\beta_{k,r}}{\kappa_{k,r}}
=\frac{3s_1(k,r)^2+s_2(k,r)}2\,\kappa_{k,r}^2.
\]

For a fixed three-row set `I={i,j,k}`, define

\[
\Gamma_I(\mathbf r)
=\det\begin{pmatrix}
 w_i&1&v_i\\
 w_j&1&v_j\\
 w_k&1&v_k
\end{pmatrix},
\qquad
G_I(\mathbf r)=\Lambda^3\Gamma_I(\mathbf r)\in\mathbb Z,
\]

where `Lambda=lcm(1,...,m+4)`. If `Z=p^{v_p(t)}` is a retained clean component and `q_I(Z)=M_I(Z)/Z^3`, the current peer report proves

\[
\Lambda q_I(Z)
\equiv U^3(W/Z)^3G_I(\mathbf r(Z))\pmod Z,
\tag{2.1}
\]

with `U=t/W` and all factors other than `G_I` units modulo `Z`.

Hence

\[
Z\mid G_I(\mathbf r(Z))
\quad\Longleftrightarrow\quad
Z\mid q_I(Z),
\]

and in the singular case one gains the fourth clean power `Z^4 | M_I(Z)`.

The derivation of the third inverse coefficient checks independently: writing

\[
F_k(r+x)=F_k'(r)x\left(1+s_1x+\frac{s_1^2-s_2}{2}x^2+O(x^3)\right)
\]

and reverting the series gives

\[
x=\kappa y-s_1\kappa^2y^2
+\frac{3s_1^2+s_2}{2}\kappa^3y^3+O(y^4),
\]

so the quoted `w` is correct. Thus the new branch invariant is not a formal artifact of an incorrect inverse coefficient.

## 3. B8 — discretize the singular branch by exact branch values

The singular condition has a stronger consequence than a componentwise divisibility statement.

### Theorem 3.1 — equal-branch-value compression

Fix `m` and one row triple `I`. Let `S` be any collection of pairwise-coprime clean components `Z` for which

\[
Z\mid G_I(\mathbf r(Z))
\]

and `G_I(\mathbf r(Z)) != 0`. Partition `S` by the exact integer value

\[
g=G_I(\mathbf r(Z)).
\]

For each nonzero value `g`, let

\[
S_g=\{Z\in S:G_I(\mathbf r(Z))=g\}.
\]

Then

\[
\boxed{\prod_{Z\in S_g}Z\mid |g|.}
\tag{3.1}
\]

Consequently, if `V(S)` is the set of distinct nonzero branch values occurring on `S`,

\[
\boxed{
\prod_{Z\in S}Z
\le
\prod_{g\in V(S)}|g|.
}
\tag{3.2}
\]

#### Proof
Every `Z` in `S_g` divides the same nonzero integer `g`. Distinct clean components are full prime powers for distinct clean primes and are therefore pairwise coprime. Their product divides `g`. Multiplying over distinct values proves (3.2). ∎

This is different from the preceding I0129 value-capacity theorem for the cubic minors `M_I(Z)`: here the repeated object is the **post-cubic branch section itself**, before multiplication by the component-dependent quotient `T_Z^3`.

### Corollary 3.2 — singular rough mass requires many branch values

Put

\[
K=m+4,
\qquad H=1+\log K.
\]

Uniformly for all `k <= K` and `0<=r<k`,

\[
|\kappa_{k,r}|\le K2^K,
\qquad |s_1(k,r)|\le H,
\qquad s_2(k,r)<4.
\]

Therefore

\[
|v_{k,r}|\le HK2^K,
\qquad
|w_{k,r}|\le4H^2K^2 4^K.
\]

A three-by-three determinant expansion gives

\[
|\Gamma_I(\mathbf r)|
\le24H^3K^3 8^K.
\]

Using only the elementary `Lambda <= K! <= K^K`,

\[
|G_I(\mathbf r)|
\le24H^3K^{3K+3}8^K.
\tag{3.3}
\]

For `K>=4`, the right side has logarithm at most

\[
8K\log K.
\tag{3.4}
\]

Hence, if `B_I(S)=|V(S)|`, then

\[
\boxed{
\log\prod_{Z\in S}Z
\le 8B_I(S)K\log K.
}
\tag{3.5}
\]

Equivalently,

\[
\boxed{
B_I(S)
\ge
\frac{\log\prod_{Z\in S}Z}{8K\log K}.
}
\tag{3.6}
\]

Thus a singular subfamily carrying a fixed positive fraction of the clean logarithmic mass `Theta(m^2)` must realize at least

\[
\Omega\!\left(\frac{m}{\log m}\right)
\]

distinct nonzero values of the branch section `G_I`.

This is a real compression statement: repeated singular branch values have only `exp(O(m log m))` total prime-power capacity, whereas the preserved clean core has `exp(Theta(m^2))` mass.

## 4. B12 — what is conserved, and the exact two-way obstruction

Equation (2.1) separates the remaining difficulty into two genuinely different mechanisms.

### Singular side

For every nonzero branch value `g`, all clean components taking that value consume divisors of the single fixed integer `g`. The conserved object is therefore not merely the congruence class but the **finite divisor budget of one exact branch integer**. Theorem 3.1 says that no fixed nonzero value can support macroscopic rough mass.

Accordingly, a source-level use of the singular side now has only two possible escape routes:

1. many components lie on the exact zero fiber `G_I=0`; or
2. the singular components realize `Omega(m/log m)` distinct nonzero `G_I` values.

The first is a geometric classification problem; the second is a branch-value expansion problem.

### Unit side

If `g=G_I(\mathbf r(Z))` is a unit modulo `Z`, then (2.1) can be inverted to give

\[
\boxed{
U^3
\equiv
\Lambda q_I(Z)(W/Z)^{-3}g^{-1}\pmod Z.
}
\tag{4.1}
\]

Thus every unit-branch component encodes the **same global small target `U^3`** by a different explicit local expression. This confirms the current peer diagnosis: the post-cubic information is genuinely synchronized, but extracting an Archimedean contradiction requires controlling the height of those inverses rather than merely invoking CRT.

The singular compression theorem and the unit-target identity are complementary: a future proof can now try to show that the singular branch has insufficient value complexity and force most rough mass onto the unit branch, where all components share the same target `U^3`.

## 5. B26 — exact reflection symmetry and a genuine zero fiber

The zero-fiber alternative cannot be dismissed abstractly. The branch section has exact symmetries.

Let

\[
r^*=k-1-r.
\]

Then

\[
\kappa_{k,r^*}=(-1)^{k-1}\kappa_{k,r},
\qquad
s_1(k,r^*)=-s_1(k,r),
\qquad
s_2(k,r^*)=s_2(k,r).
\]

Consequently

\[
\boxed{
v_{k,r^*}=(-1)^k v_{k,r},
\qquad
w_{k,r^*}=w_{k,r}.}
\tag{5.1}
\]

So for even `k` the two complementary roots have exactly the same point `(v,w)`, while for odd `k` they are reflected across the `w`-axis.

There is also an explicit zero fiber. Suppose `m` is odd and take the row triple

\[
I=\{m,m+2,m+4\}.
\]

All three row indices are odd. Choose the central root in each row,

\[
r_k=(k-1)/2.
\]

Then `s_1(k,r_k)=0`, hence `v_{k,r_k}=0` for all three rows. Therefore

\[
\Gamma_I(\mathbf r)
=\det\begin{pmatrix}
w_m&1&0\\
w_{m+2}&1&0\\
w_{m+4}&1&0
\end{pmatrix}=0,
\]

and so

\[
\boxed{G_I(\mathbf r)=0.}
\tag{5.2}
\]

This does **not** contradict the peer report's nonvanishing statement on its already-pruned entropy-separated family: the central template is exactly the kind of branch excluded there. It does show that global nonvanishing of `G_I` is false and that the zero-fiber exclusion must remain an explicit hypothesis or be proved from the selected-root constraints. Any future argument that silently upgrades “nonzero on the preserved entropy-separated family” to “nonzero on all branches” would be invalid.

I did not prove that the central zero tuple simultaneously satisfies the full four-row principal constraint `Delta_1=0`; no such claim is made. The point of (5.2) is only to certify a genuine algebraic zero fiber of the new section.

## 6. What this does and does not prove

New exact conclusions:

1. the third inverse coefficient used by the current I0129 report checks independently;
2. for every fixed nonzero branch value, the product of all singular clean components realizing it divides that one integer;
3. a singular family of macroscopic rough mass must therefore realize `Omega(m/log m)` distinct nonzero branch values, unless it enters the exact zero fiber;
4. complementary-root reflection is explicit, and `G_I` has genuine exact zero fibers outside the entropy-separated retained family;
5. in the unit branch every component encodes the same target `U^3` by (4.1).

Not proved:

- Singmaster's conjecture;
- any improvement of the owner track's frozen `rho_SM=1`;
- subcritical capacity of the complete singular zero fiber under the full selected-root constraints;
- the needed small-height lift on the unit branch;
- any release, reassignment, or duplicate ownership of I0129.

## 7. Admission disposition

No new free residue-4 CLOSABLE source appeared in the material repository delta. `I0129` is active HARD OUTSIDE and exclusively owned by another native slot, so R7-05 does not admit it.

R7-05 remains

`PENDING_ADMISSION`.

Successor metric before: `UNKNOWN/UNMEASURED`.  
Successor metric after: `UNKNOWN/UNMEASURED`.  
Successor stagnation count: **NOT INSTANTIATED**.

The next R7-05 invocation should remain strict-delta admission work. This peer artifact is useful to I0129 but is not permission to spend repeated R7-05 runs on an already-owned HARD target.
