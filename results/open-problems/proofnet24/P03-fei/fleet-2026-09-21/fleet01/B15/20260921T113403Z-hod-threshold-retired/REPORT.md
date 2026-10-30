# B15 — the Hod sharp-constant target is already falsified, and the record seed transfers to the arithmetic remainder

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval was used in this derivation.  
**Route:** APPROACHES 4/8 — spectral magnitude/arithmetic structure and sharp-constant stress testing.  
**Fresh private source frontier before writing:** `master` was re-resolved at `1202d908234bad857121cd4ffd0fbd25f936a1fa`.  
**Public source correction:** the live public `teorth/optimizationproblems` record at commit `9d57db86c8564cb623ec9f9e41429a34efd819fb`, `constants/71a.md` blob `d5fcdad39105d4cb594176b128119ab6f7dda9e4`, records a lower bound `C_71 > 6.521845710923046575`; merged PR #94 already gave a certified comparison strictly above the full Hod value `beta(1/2)`, and merged PR #130 later raised the record to the 18-variable value. The current record source is public and replayable, but its external certificate archive was **not independently replayed in this run**.

This run does not rerun or audit the settled read-once certificate. It instead stress-tests the working conjecture in `APPROACHES.md` that Hod's `beta(1/2)` might be the universal sharp FEI constant. The result is decisive: that working conjecture is stale. More importantly for B15, combining the newer finite-seed lower bound with the project's already-proved arithmetic-remainder isolation theorem gives an explicit family forcing the arithmetic remainder above the old `beta/2` target.

---

## 1. The external sharp-constant premise has changed

The 21 September `APPROACHES.md` says, as a numerical working conjecture, that nothing on record exceeds

\[
\beta(1/2)=6.4547837\ldots.
\]

That statement is no longer current. The public Optimization Problems record for the FEI constant now gives

\[
\boxed{C_{\rm FEI}>L_{18}:=6.521845710923046575}
\tag{1}
\]

from an explicit balanced logic-monotone Boolean function on 18 variables, followed by the O'Donnell--Tan amplification theorem. The record page gives the longer floor-truncated value

\[
6.5218457109230465756581439729485784683666\ldots.
\tag{2}
\]

The merged n=18 PR (#130) records exact influence

\[
I(g_{18})=\frac{261}{128},
\tag{3}
\]

and describes a replayable certificate. It also says that the construction is balanced and logic-monotone, so the same lower bound applies in the monotone class.

For the specific question whether Hod's number can be the universal sharp constant, one does not need to rely on a decimal comparison with the displayed `6.4547837`. The earlier merged PR #94 produced an explicit balanced monotone 14-variable seed with

\[
\frac{H(g_{14})}{I(g_{14})-1}
\ge 6.490112843523394359677229607268\ldots,
\tag{4}
\]

and explicitly compared its certified lower endpoint against a certified **upper** enclosure of the full value `beta(1/2)`, obtaining a positive margin `0.0353291269606358`. Thus, subject to the public certificate chain, the statement

\[
C_{\rm FEI}=\beta(1/2)
\]

is already false. The n=18 seed strengthens the separation further.

**Scope / confidence boundary.** I verified the live public repository state, the merged status and text of PR #94, and the merged n=18 PR metadata/source description. I did not spend this FEI run re-running those external certificates, because the owner explicitly requested creative progress rather than FEI audits. Therefore this report treats (1)--(4) as the current curated public record, not as a fresh independent certification by B15.

Full FEI is unaffected: a larger lower bound on the optimal constant is not a counterexample to the existence of a finite universal constant.

---

## 2. Inherited B15 arithmetic remainder

Retain the project's exact packet notation. For each distinct nonzero Fourier magnitude `a`,

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
p_a=|A_a|a^2,
\]

\[
V_a(x)=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S(x),
\qquad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),
\]

\[
b_a=a2^{r_a},\qquad
\mathcal D(f)=\sum_a p_a\log_2\frac1{b_a}.
\tag{5}
\]

The already-proved isolation theorem defines

\[
C_H:=\sup_{I(f)>0}\frac{H(f)}{I(f)},
\qquad
C_D:=\sup_{I(f)>0}\frac{\mathcal D(f)}{I(f)}
\]

and proves the exact identity, in the extended nonnegative reals,

\[
\boxed{C_H=2C_D.}
\tag{6}
\]

More strongly, for every fixed Boolean `f` it constructs explicit rare Boolean perturbations `F_t` with

\[
I(F_t)\to I(f),\qquad
H(F_t)\to H(f),\qquad
\mathcal D(F_t)\to\frac{H(f)}2.
\tag{7}
\]

This quantitative construction is the bridge from the new finite FEI lower-bound seed to B15's arithmetic route.

---

## 3. PROVED: amplified-seed transfer to arithmetic-remainder witnesses

### Theorem 3.1 — `B15-AMPLIFIED-SEED-TO-REMAINDER`

Let `g` be a balanced Boolean function with `H(g)>0` and `I(g)>1`. Put

\[
L(g):=\frac{H(g)}{I(g)-1}.
\tag{8}
\]

Then there is an explicit two-parameter family of finite Boolean functions `F_{m,t}`, obtained by first taking an O'Donnell--Tan amplification iterate of `g` and then applying the inherited rare-perturbation isolation construction, such that

\[
\boxed{
\lim_{m\to\infty}\lim_{t\to\infty}
\frac{\mathcal D(F_{m,t})}{I(F_{m,t})}
=\frac{L(g)}2.
}
\tag{9}
\]

In particular,

\[
\boxed{C_D\ge \frac{L(g)}2.}
\tag{10}
\]

If a certified seed gives a strict lower bound `L(g)>L_0`, then there are finite Boolean functions with

\[
\frac{\mathcal D}{I}>\frac{L_0}{2}.
\tag{11}
\]

### Proof

The O'Donnell--Tan balanced composition theorem gives a sequence of finite Boolean amplification iterates `f_m` with

\[
\frac{H(f_m)}{I(f_m)}\longrightarrow
\frac{H(g)}{I(g)-1}=L(g).
\tag{12}
\]

For each fixed `m`, apply the project's quantitative isolation theorem to `f_m`. It gives explicit Boolean `F_{m,t}` satisfying

\[
\frac{\mathcal D(F_{m,t})}{I(F_{m,t})}
\longrightarrow
\frac{H(f_m)}{2I(f_m)}
\qquad(t\to\infty).
\tag{13}
\]

Now take `t->infinity` first and then `m->infinity`. Equations (12)--(13) give (9). Equation (10) follows because every member of the family is a finite Boolean function. If `L(g)>L_0`, choose `m` so that `H(f_m)/(2I(f_m))>L_0/2+eta` for some `eta>0`, then choose `t` so large that (13) is within `eta`; this yields (11). `square`

This theorem is not merely the supremum identity (6) restated: it identifies the concrete composition-plus-isolation mechanism that transports any improved finite balanced FEI seed into the specific B15 arithmetic-remainder geometry.

---

## 4. Numerical consequence of the current n=18 record

Apply Theorem 3.1 to the current public n=18 record seed. From (1),

\[
\frac{L_{18}}2
=3.2609228554615232875.
\tag{14}
\]

Using the longer floor-truncated public value (2), the corresponding half is

\[
3.2609228554615232878290719864742892341833\ldots.
\tag{15}
\]

Consequently, conditional only on the current public certificate claim,

\[
\boxed{C_D>3.2609228554615232875.}
\tag{16}
\]

Moreover this is witnessed by an explicit finite two-parameter Boolean family through (9), not just by an abstract supremum argument.

This immediately falsifies the old B15 target

\[
\mathcal D(f)\le\frac{\beta(1/2)}2 I(f)
\quad\text{for every Boolean }f,
\tag{17}
\]

because `beta(1/2)/2` is about `3.22739`, strictly below the already-certified n=14 amplification constant divided by two, and below the current n=18 record half.

The correction is structurally important. The arithmetic remainder is not a small error term sitting below the Hod read-once barrier. Under rare perturbations it can capture essentially one half of the **entire** Fourier entropy while preserving influence, so every improvement in the global FEI lower bound is automatically inherited by the remainder constant.

---

## 5. Consequence for the mesh-band free energy from the previous B15 run

The immediately preceding B15 continuation proved, for the adaptive mesh-band statistic `F_epsilon`,

\[
\mathcal D(f)\le\mathcal F_\epsilon(f)
\le\mathcal D(f)+\epsilon I(f).
\tag{18}
\]

That theorem remains valid. What must be retired is only its old sharp-Hod target. Since (16) gives finite functions with `D/I` above the old `beta/2` threshold, for sufficiently small `epsilon` there are also functions with

\[
\frac{\mathcal F_\epsilon(f)}{I(f)}
>\frac{\beta(1/2)}2+\epsilon
\tag{19}
\]

(after choosing a remainder witness with a fixed positive margin and then taking `epsilon` below that margin). Thus the previous proposed universal inequality at `beta/2+epsilon` cannot hold.

A correct future target cannot be set below the best current lower bound on `C_H/2`. At present the public record forces any universal mesh/remainder coefficient to be at least the number in (16). This does **not** say that `6.521845...` is the sharp FEI constant; it is only the present lower frontier.

---

## 6. Why this preserves the unequal-magnitude / carry obstructions

The transfer does not sneak back to a flat-spectrum or common-grid class. The isolation construction deliberately separates the old nonzero Fourier coefficients into singleton distinguished magnitude components while leaving a tiny residual spectral mass. For the distinguished packets the divisibility order is zero, so almost all of the original entropy is moved into `D`; the small exceptional mass contains the remaining carry structure. Quantitatively the inherited theorem gives `R(F_t)->0` and `D(F_t)->H(f)/2`.

Therefore the construction is compatible with the two obstructions B15 was required to preserve:

1. **Unequal magnitudes:** the amplified high-ratio seed has a highly nonflat spectrum; isolation separates rather than equalises those magnitudes.
2. **Carry / valuation behavior:** no false universal tensor-subadditivity or fixed-grid statement is used. The earlier exact tensor-collision counterexample remains valid. The transfer only exploits the proved fact that the isolation gadget makes the total divisibility contribution asymptotically negligible.

This is exactly why the remainder lower bound is useful: it proves that any successful arithmetic proof must pay a remainder ratio of at least `3.260922855...`, regardless of how one controls carries locally.

---

## 7. What moved, what did not, and the next B15 target

### PROVED / established in this run

1. The internal working premise “Hod's `beta(1/2)` may be the universal sharp constant” is stale relative to the current public FEI record. Merged PR #94 already reports a certified explicit monotone seed whose amplification constant is strictly above the full Hod value, and merged PR #130 raises the current recorded lower bound to `>6.521845710923046575`.
2. The amplified-seed transfer theorem (9) converts **any** balanced finite lower-bound seed into explicit arithmetic-remainder witnesses with limiting ratio one half of its amplification constant.
3. Combining that theorem with the current n=18 record forces the B15 remainder lower frontier to
   `C_D > 3.2609228554615232875` (subject to the public certificate claim).
4. Therefore every attempted universal bound at `beta/2`, including the previous mesh-band sharp-Hod target, is impossible.

### NOT proved

- Full FEI remains OPEN.
- No finite universal upper bound on `D/I` or `H/I` is proved.
- The current record `6.521845...` is **not** claimed sharp.
- The external n=18 certificate was not independently replayed by B15 in this run.
- No tensor-subadditivity, bounded carry depth, common lattice, or packetwise lower-magnitude bound is asserted.

### Next nonoverlapping B15 attack

The best next arithmetic question is no longer “prove `D/I<=beta/2`.” It is:

> **Which packet mesh-depth bands in the explicit record seed and its amplification iterates create the excess above Hod, and can the amplification dynamics of the exact free energy `2D=log N-KL(p||q)` be written as a closed recursion?**

The target is to obtain the exact packet/free-energy profile of the n=18 (or already-merged n=14) seed from its public certificate, then follow the distribution of `X_a=log2(1/b_a)` through disjoint balanced composition while explicitly retaining equal-magnitude collision/valuation terms. A closed recurrence could either (i) expose a still larger family by optimizing the seed's packet free energy, or (ii) identify a genuine universal payment mechanism whose constant is necessarily at least (16).

This is a sharper continuation of APPROACH 4/8 than searching around Hod's now-obsolete threshold.

## Public source identities used

- `teorth/optimizationproblems`, main commit `9d57db86c8564cb623ec9f9e41429a34efd819fb`, `constants/71a.md` blob `d5fcdad39105d4cb594176b128119ab6f7dda9e4`: current recorded lower bound and references.
- Merged PR #94: n=14 balanced monotone seed, exact influence `521/256`, certified entropy interval, O'Donnell--Tan amplification derivation, and certified positive comparison against the full Hod `beta(1/2)`.
- Merged PR #130: n=18 balanced monotone record, exact influence `261/128`, current lower bound, certificate description and DOI.

No publication-priority claim is made for the transfer observation. The private project isolation theorem predates this run; the new contribution here is to combine it with the actually current FEI lower-bound frontier and thereby correct and sharpen B15's arithmetic target.
