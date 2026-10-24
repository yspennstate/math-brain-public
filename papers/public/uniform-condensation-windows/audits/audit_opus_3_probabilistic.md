# Adversarial audit — Opus 3 (probabilistic assembly, consequences, literature)

Paper: `main.tex` (855 lines)
Scope owned: §7 (uniform windows, Lemma 7.1, proof of Thm 2.1), §8 (Cor 2.2, (8.1)/(8.2),
cyclic lemma, Cor 8.1), §9 (Thm 9.1), and the literature/novelty claim.
Scratch, scripts and downloaded sources: `agent3_scratch/`.

---

## VERDICT

**HOLDS UNDER ATTACK** — every load-bearing step in §§7–9 survives exact re-derivation
(the Markov calibration, the pigeonhole, the window arithmetic, the `A_J^n` cancellation,
the final two-line display, the diagonal, the cycle lemma, the root identity, and both
directions of Thm 9.1); the only defects I can substantiate are one over-attributed
citation, one unstated (but true, and one-line-repairable) hypothesis in the cycle-lemma
paragraph, and compression in the span-`d` and diagonal paragraphs.

**This verdict is conditional and narrow.** §§7–9 are an assembly: Lemma 7.1 consumes
Lemma 3.1 (insertion), Lemma 6.1 (greedy residual) and — decisively — Lemma 5.1
(`limsup G_J = +∞`), which is the actual engine and is another auditor's scope. I
re-derived Lemmas 3.1 and 6.1 line by line while checking that §7 uses them within their
stated hypotheses, and both hold; I did **not** audit Lemmas 4.1/4.2/5.1/5.2 beyond a
spot check on a sparse factorial law. If the margin lemma fails, §7 assembles correctly
around a false input and the paper still collapses. Take "holds" here to mean "the
probabilistic assembly is sound given its inputs", nothing more.

---

## NOVELTY VERDICT

**The problem appears genuinely open, and the paper's citation of it is accurate down to
the page number. I found no prior work that settles it. Confidence: reasonably high on the
"no one has claimed it" half; moderate on the "no one has it as an unremarked corollary"
half, because I could not run a true full-text search of the post-2012 literature.**

Verified, against the actual PDFs rather than search snippets:

* `arXiv:1112.0510` has **exactly one version, v1** (submission history: "[v1] Fri, 2 Dec
  2011"; v2/v3 both 404). So `\cite{JansonPreprint}`'s "v1" is the only preprint numbering
  there is.
* **Problem 18.40 (preprint v1, p. 122) and Problem 19.41 (published, p. 228) are the same
  problem, word for word:** *"Is Y_(1)/n →_p 0 possible when λ > ν = 0? (Example 18.38 /
  19.39 shows that this is possible for a subsequence.)"* Read from
  `arxiv.org/pdf/1112.0510v1` and from the Project Euclid PDF of `10.1214/11-PS188`
  (150 pp., front page footer `103`, Problem 19.41 on the page whose printed folio is
  **228**). **The paper's `\cite[p.~228]{Janson}` is correct.**
* The paper's rendering of the problem — "whether `Y_(1)/n → 0` in probability can hold
  along the full sequence" — is right. The parenthetical rules out the subsequence reading,
  and the immediately preceding Problem 19.40 spells the pattern out ("…possible for a
  subsequence, but we conjecture that it is not possible for the full sequence").
* **Example 19.39 says what the paper attributes to it**: `w_k = k!` on
  `supp(w) = {0} ∪ {i! : i ≥ 0}`, `ρ = ν = 0`, `Y_(1)/n → 0` along `n = i!`. The paper's
  "sparse factorial support gives examples with a sublinear largest box on certain
  subsequences" is exact.
* Janson's own state-of-the-art sentence, on the same page as the problem: *"We expect that
  bad behaviour as in the examples above only can occur for quite irregular weight
  sequences, but we have no general result beyond Theorem 19.34."* Theorem 19.34 is the
  **power-law** case `w_k ∼ ck^{-τ}`, `τ > 2` — which has `ρ = 1`, not `ρ = 0`. So the
  survey itself contains nothing for the zero-radius regime beyond the examples.
* **JJS (arXiv:1104.2810) is correctly hedged.** Read in full: Theorem 2.3 assumes
  `w_{n+1}/w_n → ∞` (their eq. (2.5)) and concludes weak convergence to the infinite star;
  Theorems 2.4/2.5 are the explicit families `w_n = ((n−1)!)^γ`. The paper's "an
  infinite-star local limit under a successive-weight-ratio hypothesis, and stronger size
  estimates for explicit factorial families" is accurate, and JJS **cannot** imply Thm 2.1
  or Cor 2.2: the ratio hypothesis fails for every sequence with long runs of zero weight,
  which is precisely the hard case the paper targets (it is also Janson's *separate*
  Problem 19.43).

Searches run, with their bounds stated:

| route | bound | result |
|---|---|---|
| OpenAlex `cites:W2120547819` (the survey) | **230 citing works**, all fetched, 196 with abstracts, screened on 16 phrases incl. "zero radius", "superexponential", "19.41", "18.40", "largest box", "irregular weight" | 2 weak hits ("open problem" in a height/width paper; "maximal out-degree" in Conditioning GW trees on large maximal out-degree). Neither is this problem. Full title list read by eye. |
| Stufler, *Limits of random tree-like discrete structures*, Prob. Surveys 17 (2020) — full text | §6.5.2 "The superexponential case", Lemma 6.17, Thm 6.18, Cor 6.19; plus every "type III" occurrence and every "open problem" hit | Gibbs partitions/EGF species, **and** Thm 6.18 assumes eventual full support on a lattice ("there is an integer `I` with `a_i > 0` for all `i ≥ I` with `i ≡ 1 mod d`"). Excludes arbitrary support gaps. For the *tree* type-III case the survey explicitly defers — "we establish the same asymptotic behaviour as simply generated trees with vertices as atoms and superexponential weights on the out-degrees [73, 71]", where [71] is Janson's survey. It adds nothing for zero radius with arbitrary support. |
| Stufler, *Gibbs partitions: a comprehensive phase diagram* (arXiv:2204.06982) — full text | grep for the problem numbers / zero radius | only a passing reference to superexponential recursive structures |
| *Random allocation models in the thermodynamic limit* (PRE 108, 064107, 2023) — full text | grep on "radius" | works with a positive radius of convergence and a fugacity; the standard condensation regime, not `ρ=0` |
| Jonsson–Stefánsson, *Condensation in nongeneric trees* | abstract/summary | `w_n ∼ n^{-β}`, i.e. `ρ = 1`; not zero radius |
| Google/Bing web search, 6 distinct query formulations incl. exact `"Problem 19.41"` and `"Problem 18.40"` | ~9 results each | no paper claiming to answer it |
| arXiv API `all:"superexponential branching weights"` | totalResults = **1** | only JJS itself |
| Kortchemski, *Limit theorems for conditioned non-generic Galton–Watson trees* (arXiv:1205.3145) — full text | end of paper | **positive evidence the regime is untouched.** Verbatim, checked in the PDF myself: *"It would thus be interesting to find out if the theorems obtained in the present work for [simply generated trees whose associated] radius of convergence is 0. In the latter case, Janson [17] proved that `T_n` converges locally … toward a deterministic tree consisting of a root vertex with an infinite number of leaves attached to it. We thus expect that the asymptotic properties derived in the present work will take a different form in this case. We hope to investigate this in future work."* |
| Abraham–Delmas (arXiv:1311.6683), Jonsson–Stefánsson (arXiv:1009.1826), *Condensation in subcritical Cauchy Bienaymé trees* (2025) | full texts / abstracts | all in the **positive**-radius regime (an actual offspring distribution exists, `ρ_G = 1`). Structurally cannot cover `ρ = 0`. |

A second literature pass run in parallel (19 further web queries plus full-text extraction of
five primary sources, list in that agent's report) reached the same conclusion independently
and found nothing I had missed except the Kortchemski remark and the Theorem 7.1 point below,
both of which I then verified myself in the source PDFs rather than relaying.

**Named limits of this search — do not read it as proof of absence.** (i) OpenAlex's citation
graph is incomplete; MathSciNet and Google Scholar would list more than 230. (ii) I screened
**titles and abstracts**, not full texts, for those 230; a paper could settle this in a
remark without saying so up front. (iii) arXiv's `all:` field is title/abstract/comments
only, so no true full-text search of arXiv was possible, and the API started returning
406/400 after ~12 calls. (iv) I did not search the physics literature (zero-range processes,
Godrèche–Luck, Grosskinsky–Schütz–Spohn, Armendáriz–Loulakis) systematically — but that
whole literature is the *sub*exponential/heavy-tail regime with a positive radius, the
opposite extreme from superexponentially growing weights, so the a-priori risk there is low.
The honest statement for the paper to make is the one it already makes in `SUMMARY.md`
("publication novelty remains unverified"), and that hedge should survive into any public
release.

One scope note the paper could add, in its own favour: Janson's §19.6 works under
`ν < λ < ∞` (Lemma 19.32), so Cor 2.2's `λ ∈ (0,∞)` matches the problem exactly. The case
`m_n/n → ∞` is outside both.

---

## FINDINGS

No FATAL. No GAP. Four MINOR, four EDITORIAL.

| # | sev | line | one line |
|---|---|---|---|
| 1 | MINOR | 679 | `\cite[Lemma 14.7]{JansonPreprint}` states the *unconditional* size-biased identity, not (8.3); published number 15.7 not given |
| 2 | MINOR | 658–660 | "orbit of `n` rotations" assumes a trivial rotational stabiliser without proof (true, one line) |
| 3 | MINOR | 536 | `q_0=1` comes from the `w_0=1` normalisation, not from the record definition |
| 4 | MINOR | 91–98, 700–702 | the general prior result is Janson's own Theorem 7.1 (no ratio hypothesis), and it is never cited |
| 5 | EDITORIAL | 630–633 | the diagonal reuses `r` and does not flag `δ = δ(ε)` |
| 6 | EDITORIAL | 613–616 | the span-`d` paragraph compresses three steps |
| 7 | EDITORIAL | 640–648 | (8.1) does not say which `ε` its `δ, k_r` come from |
| 8 | EDITORIAL | 563–566 | the Markov step is exactly tight and should be displayed |

### MINOR-1 — `main.tex:679`: `\cite[Lemma~14.7]{JansonPreprint}` does not state (8.3)

The text reads *"Conditional on `(A_j)`, the known root-degree identity
`\cite[Lemma~14.7]{JansonPreprint}` reads"* followed by (8.3),
`P(d^+(o)=j | (A_i)) = jA_j/(n-1)`.

What Janson's Lemma 14.7 (preprint p. 64; **Lemma 15.7** in the published version, p. 170)
actually says, verbatim:

> **Lemma 14.7.** For any `d ≥ 0` and `n ≥ 2`, `P(d⁺_{T_n}(o) = d) = (n/(n−1)) d P(Y₁ = d)`.
> Thus, the distribution of the root degree `d⁺_{T_n}(o)` of `T_n` is the size-biased
> distribution of `Y₁`.

That is an **unconditional** identity relating the root degree to the marginal law of a
*single box* `Y₁`, with an extra factor `n/(n−1)`. (8.3) is its conditional refinement. The
two are consistent — given the counts, `P(Y₁ = j | (A_i)) = A_j/n`, and
`(n/(n−1))·j·(A_j/n) = jA_j/(n−1)` — but Janson never states the conditional form, and
getting it from his lemma needs the extra observation that his cyclic-shift proof is
count-preserving. Nothing breaks (the paper proves (8.3) directly, and I verified that
direct proof exactly), but as written the sentence over-attributes.

Second, smaller point on the same line: the paper gives dual numbering for the Problems
(19.41/18.40) and for Example 19.39, but cites the lemma by preprint numbering only. The
published number is **15.7** (the published version inserts a new §9 "The maximum degree",
which pushes every later section by +1).

**Fix** (replace lines 678–680):

```latex
Fix $n\ge2$. Let $A_j$ be the number of vertices of outdegree $j$, and let
$D=\max\{j:A_j>0\}$. Janson's root-degree identity
\cite[Lemma~14.7]{JansonPreprint}, Lemma~15.7 of \cite{Janson}, states that
$d^+(o)$ has the size-biased law of a single occupancy. Its conditional form is
\begin{equation}\label{eq:rootidentity}
 \Pp(d^+(o)=j\mid(A_i))=\frac{jA_j}{n-1},
\end{equation}
which the following count establishes directly.
```

### MINOR-2 — `main.tex:658–660`: "an orbit of $n$ rotations" is asserted, not proved

> The cyclic lemma groups every allocation sequence of total $n-1$ into an orbit of
> $n$ rotations containing exactly one valid tree sequence

The `n`-to-1 weighted correspondence needs the orbit to have `n` **distinct** elements, i.e.
a trivial rotational stabiliser. That is true here, and for a reason specific to the total
being `n−1`: if the sequence had period `p | n` with `p < n` and per-period sum `σ`, then
`n−1 = (n/p)σ`, so `g := n/p ≥ 2` divides both `n` and `n−1`, hence `g | 1` — contradiction.
Without that sentence, "orbit of `n` rotations" and "exactly one valid tree sequence" do not
by themselves give `Z(n-1,n) = n·Σ_{trees} weight`, and the whole of Cor 8.1 rests on it.
Exhaustively checked for `2 ≤ n ≤ 10` (66,196 sequences): 0 periodic orbits, 0 sequences with
a number of valid shifts other than 1.

**Fix** (insert after "…exactly one valid tree sequence"):

```latex
The orbit has exactly $n$ elements: a period $p\mid n$ with $p<n$ would force
$g=n/p\ge2$ to divide both $n$ and the total $n-1$, hence $g=1$.
```

### MINOR-3 — `main.tex:536`: "The record definition implies $q_0=1$"

`q_0 = w_0 e^{0} = w_0 = 1` follows from the §2 normalisation, not from (4.1). The record
definition delivers the *other* half of the sentence, `q_j ≤ j^{-b}` for `1 ≤ j ≤ u`.
Cosmetic, but it is the sentence that licenses `A_J ≥ 1 > 0`, so a referee will stop on it.

**Fix**: `The normalisation $w_0=1$ gives $q_0=1$, and the record definition implies
$q_j\le j^{-b}$ for $1\le j\le u$.`

### MINOR-4 — `main.tex:91–98, 700–702`: the strongest general known result is Janson's own Theorem 7.1, and the paper never cites it

§1 positions the work against JJS ("an infinite-star local limit under a
successive-weight-ratio hypothesis"), and §8 says Cor 8.1 "is stronger than merely
identifying an infinite-star local limit". Both are true. But the paper never mentions that
the infinite-star local limit holds for **every** zero-radius weight sequence with `w_0>0`
with **no** ratio hypothesis, and that this is a theorem of the very survey being cited.
Verbatim, Janson Theorem 7.1 (published p. 121; preprint §7):

> **Theorem 7.1.** Let `w = (w_k)_{k≥0}` be **any** weight sequence with `w_0 > 0` and
> `w_k > 0` for some `k ≥ 2`. … Then `T_n →_d T̂` as `n → ∞` … in case (ii) `μ = ν < 1`
> (the subcritical case) and `T̂` has a finite spine ending with an explosion.

With `ν = 0` this gives `π_0 = 1`, spine length zero, and `T̂` = the infinite star. So the
first question any referee will ask is "doesn't Theorem 7.1 already give this?" The answer
is a good one and the paper should make it: local convergence controls only balls of fixed
radius, hence only that `d^+(o) → ∞`; it says nothing about `d^+(o)/n`, and Janson's own
Examples 19.37–19.39 satisfy Theorem 7.1's hypotheses while `Y_(1)/n` oscillates, splits
between two giant boxes, or tends to zero along a subsequence. That is also the cleanest
internal evidence that Problem 19.41 is genuinely open: Janson proved the fully general
local limit in the same survey and still posed the problem twelve pages later.

**Fix** — replace the last sentence of the §8 discussion (lines 700–702):

```latex
The root identity is not a new result. Nor is the infinite-star local limit: it holds for
every zero-radius weight sequence with $w_0>0$ by \cite[Theorem~7.1]{Janson}, and under a
successive-weight-ratio hypothesis in \cite{JJS}. Local convergence controls balls of
fixed radius and therefore gives only $d^+(o)\to\infty$; Examples~19.37--19.39 of
\cite{Janson} satisfy its hypotheses while $Y_{(1)}/n$ oscillates, splits, or vanishes
along subsequences. The corollary above is a statement about the fraction of the mass,
and is obtained from the unrestricted subsequence theorem.
```

and correspondingly widen the §1 sentence so that Theorem 7.1, not JJS, is named as the
general prior result.

### EDITORIAL-5 — `main.tex:630–633`: the diagonal reuses $r$ and hides $\delta=\delta(\varepsilon)$

> Apply this assertion separately with $\varepsilon=1/r$, selecting a size greater than the
> preceding one and a failure probability below $1/r$. This diagonal choice proves (2.3).

The construction is **correct** — I wrote it out in full and it closes — but `r` is already
the index of `k_r`, `n_r` *inside* the fixed-$\varepsilon$ argument, and `\delta`, the
windows, the `k`'s and the `n`'s all move with `\varepsilon` (by (7.1)). As written it reads
as though one sequence `n_r` serves every accuracy. This is exactly the quantifier slip the
brief warned about; it is a notational slip here, not a mathematical one, but it should be
written out.

**Fix** (replace the two sentences):

```latex
The parameters $\delta$, $k_r$ and $n_r$ produced above depend on $\varepsilon$.
Apply the assertion separately for each $i\ge1$ with $\varepsilon=1/i$, obtaining
sizes $n^{(i)}_1<n^{(i)}_2<\cdots$ in $\mathcal N$ along which
$\Pp_w(Y_{(1)}\le(1-1/i)m_{n})\to0$. Choose indices $\rho(i)$ recursively so that
$\tilde n_i:=n^{(i)}_{\rho(i)}>\tilde n_{i-1}$ and
$\Pp_w(Y_{(1)}(m_{\tilde n_i},\tilde n_i)\le(1-1/i)m_{\tilde n_i})<1/i$; both are
possible because $n^{(i)}_\rho\to\infty$ in $\rho$ and the displayed limit is zero.
For fixed $\varepsilon>0$ and every $i\ge1/\varepsilon$ the event
$\{Y_{(1)}\le(1-\varepsilon)m\}$ is contained in $\{Y_{(1)}\le(1-1/i)m\}$, so
$\Pp_w(Y_{(1)}/m_{\tilde n_i}\le1-\varepsilon)<1/i\to0$. With $Y_{(1)}\le m$ this
proves \eqref{eq:conclusion} along $(\tilde n_i)$.
```

### EDITORIAL-6 — `main.tex:613–616`: the span-$d$ paragraph compresses three steps

All three are true; none is written down.

1. The window translates with **the same $\delta$**: `(1+3δ)k'_r ≤ m/d ≤ (1+5δ)k'_r` is
   `(1+3δ)k_r ≤ m ≤ (1+5δ)k_r` with `k_r = d k'_r`. That is what makes the theorem's
   statement identical in both cases, and `k_r = d k'_r` is supported for `w` because
   `w'_{k'_r} = w_{d k'_r} > 0`.
2. "The original windows contain multiples of `d` for all large `r`" — because the window
   length is `2δk_r → ∞`. Stated, not justified.
3. Integers `m` in the window that are *not* multiples of `d` have `Z(m,n) = 0` and are
   therefore excluded from (2.2)'s supremum by its own `Z(m,n)>0` constraint. This is why
   the translated statement is exactly (2.2) and not something weaker. Not mentioned.

**Fix** (replace lines 613–616):

```latex
For span $d$, apply the argument to $w'_j=w_{dj}$, which has $w'_0=1$, span one and
zero radius, with masses $m/d$ and the density interval $[\alpha/d,\beta/d]$; the map
$y\mapsto y/d$ is a weight-preserving bijection of allocations and leaves $Y_{(1)}/m$
unchanged. Writing $k_r=dk'_r$, which is supported for $w$, the window
$(1+3\delta)k'_r\le m/d\le(1+5\delta)k'_r$ is exactly
$(1+3\delta)k_r\le m\le(1+5\delta)k_r$. Integers $m$ in that window that are not
multiples of $d$ have $Z(m,n)=0$ and are excluded by the constraint in
\eqref{eq:uniform}; multiples of $d$ do occur there because the window has length
$2\delta k_r\to\infty$, and for each of them the span-one certificate supplies an
admissible $n$.
```

### EDITORIAL-7 — `main.tex:640–648`: (8.1) does not say which $\varepsilon$ its $\delta,k_r$ come from

`I_r` is built from `δ` and `k_r`, which exist only relative to a fixed accuracy `ε` and the
density interval `[λ/2, 2λ]` of the Cor 2.2 proof. One clause ("with `δ` and `k_r` as
produced by Theorem 2.1 at accuracy `ε` and density interval `[λ/2,2λ]`") fixes it.

The uniformity claim itself is fine and I checked it: for `n ∈ I_r`,
`λn ∈ [(1+3.5δ)k_r, (1+4.5δ)k_r]` **exactly** (the ceiling and floor both cut the right
way, costing nothing), and choosing `η = λδ/(2(1+4.5δ))` in `|m_n − λn| ≤ ηn` gives
`|m_n − λn| ≤ δk_r/2` uniformly on `I_r`, landing `m_n` in `[(1+3δ)k_r, (1+5δ)k_r]`, with
`m_n/n ∈ [λ−η, λ+η] ⊂ [λ/2, 2λ]`.

### EDITORIAL-8 — `main.tex:563–566`: the Markov step is exactly tight and deserves its display

The first condition of (7.4) is calibrated so that the bound is **exactly** `1/2`:

```
n μ_J/(δk) ≤ [(1+5δ)k/α]·μ_J/(δk) = (1+5δ)μ_J/(αδ) ≤ (1+5δ)/(αδ) · αδ/(2(1+5δ)) = 1/2
```

(checked as exact rationals over 60 parameter combinations — the value is `1/2` on the
nose in every one). Because there is zero slack, a referee will want the two lines. Also,
Markov bounds the *upper* tail; the paper writes the conclusion for the lower one without
the complement step. Suggested insert after "…because $n\le(1+5\delta)k/\alpha$":

```latex
Explicitly, $\Pp(S_n>\delta k)\le\E S_n/(\delta k)=n\mu_J/(\delta k)
\le(1+5\delta)\mu_J/(\alpha\delta)\le1/2$ by \eqref{eq:finiteconditions}.
```

---

## WHAT I TRIED THAT DID NOT BREAK IT

Everything below was re-derived independently (scripts `agent3_scratch/a3_checks.py`,
`a3_endtoend.py`, `a3_endtoend2.py`), in exact rationals, before being compared with the
paper. I also reproduced both of the paper's own scripts: `checks_uniform.json` and
`checks_stress.json` are byte-identical to the shipped files after CRLF normalisation
(the README's `cmp` step fails on Windows for that reason alone, not a defect).

**1. The Markov step (attack 1).** Passes, exactly and with zero slack. 60 exact cases.

**2. The pigeonhole (7.5) (attack 2).** `{S_n ≤ δk} = {0,…,⌊δk⌋}` has `⌊δk⌋+1` elements, so
the largest atom is `≥ (1/2)/(⌊δk⌋+1)`. Correct as written. `q_0 = 1 > 0` is *not* needed
for the pigeonhole (the atoms already sum to `≥ 1/2`); it is needed for `A_J ≥ 1 > 0` and
hence for `p_J` to exist, and for `Z_u(t,n) > 0` to give admissibility. Both are used and
both hold.

**3. `2δk ≤ r ≤ 5δk` (attack 3).** `r ≤ (1+5δ)k − k − 0 = 5δk`;
`r ≥ (1+3δ)k − k − ⌊δk⌋ ≥ 3δk − δk = 2δk`. Floors work in the right direction. No
off-by-one.

**4. `I(r) ≤ J − D` (attack 4).** `r/2 ≤ 5δa^J/2 < a^{J−D}/40`, so
`log_a(r/2) < J − D − log_a 40`. A factor 40 of slack; the floor and the two-sided
`a^{J−1} < s_J ≤ a^J` bound are not close to binding. Checked as exact rationals over 703
parameter instances (`a ∈ {2, 3/2, 11/10, 101/100, 1001/1000}`, `D ∈ {2,3,5,11,30}`,
`β ∈ {1/2,1,5,100}`, three `δ`'s, three `J`'s, three `k`'s at both window ends and the
middle, three `t`'s) — **zero violations**, simultaneously for `r`'s bounds, `I(r) ≤ J−D`,
`5δk+1 ≤ n/2`, `nK ≥ 2m`, `r < k` and `u < k`.

**5. The insertion hypotheses (attack 5).** (a) `R + C' ≤ r`: every part is a *positive*
supported size (the large ones are `s_i ≥ K ≥ 2`, the terminal ones are the "positive parts"
of §5's fixed representations), so the number of parts is at most their total. True.
(b) `5δk+1 ≤ n/2`: from `n ≥ m/β ≥ (1+3δ)k/β` and the second condition of (7.4). That
condition is itself achievable because `δ < 1/(100(1+β))` implies `δ(10β−3) < 1`. True.

**6. `nK ≥ 2m` (attack 6).** `nK ≥ (m/β)·4(1+β) = 4m(1+β)/β ≥ 2m` since `4+2β ≥ 0`. Very
loose; `K ≥ 2β` would do.

**7. THE CANCELLATION (attack 7) — the one I most expected to break, and it does not.**
`P(S_n = t) = A_J^{-n} e^{-ht} Z_u(t,n)` is an identity, term by term, because
`Π p_J(x_v) = A_J^{-n} e^{-hΣx_v} Π w_{x_v}`; likewise at `m`. The numerator **is** exactly
`Z_u(m,n)`: `{Y_(1) ≤ u}` is the event that every coordinate is `≤ u`, and I confirmed this
by brute-force enumeration of all compositions (three laws; `brute_num == Z_u(m,n)` and
`brute_den == Z(m,n)` in every case). Chaining:

```
Z_u(m,n)/Z(m,n) ≤ e^{hm}A_J^n · 2^{C*+2}(⌊δk⌋+1) / (n w_k W_r e^{ht} A_J^n)
                = [2^{C*+2}(⌊δk⌋+1)/n] · e^{h(k+r)}/(w_k W_r)
```

`A_J^n` appears once in the numerator and once in the denominator and cancels **exactly**,
not asymptotically — verified symbolically by computing the ratio with and without the
factor and checking equality as rationals. Nothing of the form `A_J^n` survives with either
sign. The `2^{C*+2}` is `2^{C*+1}` (insertion, using `C' ≤ C_*` in the safe direction) times
`2` (the atom). Accounted for.

**8. The final two-line display (attack 8).** `⌊δk⌋+1 ≤ δk+1 ≤ 2δk` (needs `δk ≥ 1`, which
is a stated finite condition) and `1/n ≤ β/((1+3δ)k)` give the constant
`2^{C*+3}βδ/(1+3δ)` **exactly**; checked over 54 parameter cases, no violations. The
exponent: `hk − log w_k = −[k(B_J − B_{J−1}) − b log k]` using (4.2) at an active `J`, plus
`hr − log W_r ≤ E_J` from Lemma 6.1, totals `−G_J`. Every sign is right, and the constant
`C` in (7.4) matches with the `max{1,·}` guarding the trivial regime.

I also ran the *whole* Lemma 7.1 chain end to end on two sparse-support laws that are not
the paper's example (`supp = {0,1,3,11}` and `{0,2,5,13}`, rational tilts), doing exactly
what the proof does: check Markov, **select** `t` by the pigeonhole, check the atom bound,
build a greedy supported representation of `r`, check the insertion bound against the exact
`Z(m,n)`, then check the display. 8 cases, all five checks pass in all 8. As a positive
control, I first ran the same test with `t` chosen arbitrarily and a deliberately weak tilt:
the display **failed** there, exactly where the atom bound fails — so the test has teeth and
is not vacuously green.

**9. Proof of Thm 2.1 (attack 9).** The direction is right: `u ≥ (1−ε)m` gives
`{Y_(1) ≤ (1−ε)m} ⊆ {Y_(1) ≤ u}`. The bound `u/m ≥ (a^{J_r−1}−1)/((1+5δ)a^{J_r})` uses only
`u ≥ a^{J−1}−1` and `m ≤ (1+5δ)a^J`, so it is **uniform over the whole window**, not only at
an endpoint. `1/(a(1+5δ)) > 1−ε` is a stated requirement of (7.1) and is satisfiable because
`a` is chosen first with `a < 1/(1−ε)`, then `D = D(a)`, then `δ` as small as needed. The
order of choices in §7 is consistent with this.

**10. Span-`d` (attack 10).** `w' = (w_{dj})` has `w'_0 = 1`, span 1 and zero radius
(`(w_{dj_i})^{1/j_i} = ((w_{s_i})^{1/s_i})^d → ∞`). Density scales as `[α/d, β/d]`, the
window pulls back with the same `δ`, `d k_r` is supported, and non-multiples of `d` are
filtered out by `Z(m,n)>0`. All correct; see EDITORIAL-6 for the three unwritten steps.

**11. Cor 2.2 and the diagonal (attack 11).** `n_r/k_r → (1+4δ)/λ`: with
`x_r = (1+4δ)k_r/λ`, `x_r ≤ n_r ≤ (N_j/N_{j−1})x_r` and `N_j/N_{j−1} → 1`. Then
`m_{n_r}/k_r → 1+4δ`, strictly interior to `[1+3δ,1+5δ]`, and `m_{n_r}/n_r → λ`, strictly
interior to `[λ/2,2λ]`. The diagonal closes (written out in EDITORIAL-5); the `δ`-depends-
on-`ε` worry does **not** bite, because only one index is extracted per accuracy. The
`limsup E[Y_(1)/n] = λ`, `L^1` and `Y_(2)` claims all follow from `0 ≤ Y_(1)/m ≤ 1`,
bounded convergence, and `Y_(1)+Y_(2) ≤ m`.

**12. (8.1)/(8.2) (attack 12).** Uniformity verified, quantifiers written out above. The
ceilings and floors in (8.1) cost nothing. `|I_r| ~ δk_r/λ` is right, and the relative width
`δ/(1+3.5δ)` is a fixed positive constant as the text claims.

**13. Cycle lemma (attack 13).** The conclusion survives; the stabiliser is genuinely
trivial and the gcd argument is short (see MINOR-2). Exhaustive check `n ≤ 10`.

**14. Cor 8.1 (attack 14).** `(n−1)!/∏A_i!` and `j(n−2)!/((A_j−1)!∏_{i≠j}A_i!)` are both
correct, and their ratio is `jA_j/(n−1)` identically. Brute-forced over all plane trees
`2 ≤ n ≤ 10`: 96 degree-count classes, 283 conditional identities, **0 violations** — and
those 96 classes match the paper's own `checks_stress.json` (`1+2+3+5+7+11+15+22+30 = 96`
for `n ≤ 10`, 138 including `n = 11`; 23,713 trees `= ΣC_1..C_10`), so their check and mine
agree on the same population. On `D > (n−1)/2` one gets `A_D = 1` (uniqueness), and
`1 − P(root is the unique max) ≤ P(D ≤ (n−1)/2) + E[1 − D/(n−1)]`. The convergence needs
only `0 ≤ D/(n−1) ≤ 1` plus convergence in probability — **bounded convergence, no uniform
integrability required**. The paper's claim is right.

**15. Thm 9.1's construction (attack 15).** Zero radius ✓ (`limsup e^{k} = ∞` on the
support). `m_n = n−1` admissible at every `n` ✓ (`n−1` ones and one zero: `n` boxes,
sum `n−1`). The key step is valid: if `k = N_{r_j} ≤ n−1` and `n ∈ N`, then `n > N_{r_j}`
forces `n ≥ N_{r_j+1} ≥ θk`, so `k ≤ n/θ`; boxes of size `0` or `1` are `≤ 1`, so
`Y_(1) ≤ max{1, n/θ}` covers the "the largest box is a 1" case explicitly. The final
assertion's `L`-argument is also right. Checked on an explicit `N` with `θ = 4`.

**16. The equivalence (attack 16).** `(i)⇒(ii)` is exactly Cor 2.2, hypothesis for
hypothesis. `¬(i)⇒¬(ii)` is legitimate: since `N_{j+1}/N_j > 1` always, `liminf ≥ 1`, so
failure to converge to `1` **is** `limsup > 1`, which is what the construction consumes. Not
secretly one-way.

**17. No illegitimate product-of-conditionals anywhere in §§7–9.** I looked for the classic
failure (per-coordinate bounds multiplied into a joint bound without independence). There
is none: `S_n` is by construction the sum of `n` genuinely independent copies of `p_J`, and
`Z_u(t,n) = e^{ht}A_J^n P(S_n=t)` is an *identity* (the allocation measure restricted to
boxes `≤ u` **is** the i.i.d. product measure conditioned on its sum), not an estimate.
Markov uses only linearity of `E S_n = nμ_J`. The insertion is an injection between weighted
sets, summed. The greedy is an exact decomposition of one product's logarithm. Cor 8.1 is
exact conditional combinatorics.

**18. §10's Table 1 reproduces from the shipped script output.** `1.50986220045e-58`,
`9.05917320269e-58 ≤ 2^{-189}`, `7.58157669219e-56 ≤ 2^{-183}` and "97 such pairs" all match
`checks_uniform.json` (`maximum_actual_probability_rounded = 1.5098622004476568e-58`,
`uniform_sharp_bound_at_most_2_to_minus = 189`, `uniform_insertion_bound_at_most_2_to_minus
= 183`, `integer_pairs_checked = 97`). The exact rationals are in the JSON as claimed.

**Other things I tried that did not break it.** Lemma 3.1's proof re-derived line by line
(injectivity, `a_0 ≥ n−t`, `b_j = a_j+r_j ≤ min{n,⌊m/j⌋}`, `(n−t)_Q ≥ (n/2)^Q` from
`t+Q ≤ n/2`, the shared-size case, the sum over count vectors) — clean, and `a_k = 0`
because `u < k`, so `b_k = 1` is forced. Lemma 6.1's greedy re-derived (`i ≥ i_0`, `q ≥ 1`,
`h_* ≤ x' < h_*+s_i ≤ 2a^i`, strict decrease of the index, `qs_i ≤ x < 2a^{i+1}`,
`log w_{s_i} = s_iB_i − b\log s_i` valid at *every* `i` not just active ones, terminal
deficit `≤ MB_{J−1}+C_0`) — all correct, and all stage indices land in `[i_0, J−D]` so the
sum in `E_J` covers them. `μ_J → 0` and `A_J → 1` need pointwise `q_j → 0` plus the
dominating `j^{1−b} = j^{−3}` (`b = 4 > 2`) — the crude bound `Σ_{j≤u} j^{1−b} ≤ ζ(3)` alone
would *not* give `μ_J → 0`, but the paper says "dominated convergence" and that is the right
tool. I checked the theorem for consistency against Janson's own Examples 19.38
(powers of two: at `n = 2^i+1`, `m = 2^i` is supported, `Y_(1) = m`) and 19.39 (factorials:
at `n = i!+1`, `m = i!` is supported with astronomically large weight) — no contradiction,
and the mechanism does the right thing on both. I hand-computed the margin `G_J` for a
sparse factorial law (`G_J ≈ N_j^2`, `E_J ≲ 2a^{2−D}N_jN_{j−1}`) and the certificate behaves
as advertised.

---

*(This was the 2026-09-17 ask: be one of three independent Opus 5 auditors of
`paper_audit_20260917/pkg/main.tex`, own the probabilistic assembly (§7), the consequences
(§8), the sharpness theorem (§9) and the literature/novelty claim, attack the 19 listed
points, and write the result to `audit_opus_3_probabilistic.md`.)*
