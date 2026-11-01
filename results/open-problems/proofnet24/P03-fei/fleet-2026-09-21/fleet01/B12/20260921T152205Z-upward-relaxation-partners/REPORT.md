# B12 FEI creative attempt: factorial-shadow compression is too weak, and Boolean autocorrelation supplies a missing partner constraint

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.

**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), continuing the upward-mass/cancellation work but not the refuted sharp `B_can` constant. The current TASKS handoff was used: the external balanced 18-variable construction forces any universal cancellation constant to be at least `2.32399499026264678602`, so this run does not try to prove the killed `2.227...` target. I also read the newer fleet03/B12 hierarchical-block handoff, which proves that a standalone scalar payment of singleton branch information is FEI-hard and motivates a structural rather than scalar compression step.

Scientific baseline before this write: `math-open-problems` master was observed at `f080552b0e8328c13f865bc6f830e91ee9d5265d` after the required current `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md` reads.

No novelty or publication-priority claim is made. The Fourier autocorrelation identity used below is standard; the point of this note is the particular obstruction/reduction it gives for the live compression route.

## 1. Attempted compression: reduce positional entropy to the spectral degree law

Let

\[
p_A=\widehat f(A)^2,\qquad K=|S|,\qquad W_k=\Pr(K=k),\qquad
u_A=\sum_{B\supseteq A}p_B.
\]

The previous B12 report proved the Boolean granularity inequality

\[
\sqrt{p_A}\le 2^{|A|-1}\nu_A \qquad(A\ne\varnothing).
\tag{1}
\]

For `k>=1` define the factorial shadow

\[
M_k:=\sum_{|A|=k}\nu_A
    =\sum_{\ell\ge k}\binom{\ell}{k}W_\ell
    =\mathbb E\binom Kk.
\tag{2}
\]

Let `r_k(A)=p_A/W_k` be the conditional law of the spectral atom given `K=k` (when `W_k>0`). Summing (1) over the `k`-th level gives

\[
\sum_{|A|=k}\sqrt{p_A}\le 2^{k-1}M_k.
\tag{3}
\]

Shannon entropy is at most Renyi entropy of order `1/2`, hence

\[
\begin{aligned}
H(r_k)
&\le 2\log_2\sum_{|A|=k}\sqrt{r_k(A)}\\
&\le 2(k-1)+2\log_2 M_k-\log_2 W_k.
\end{aligned}
\tag{4}
\]

Therefore the full spectral entropy obeys the exact-to-(1) one-dimensional reduction

\[
\boxed{
H(S)\le p_0\log_2\frac1{p_0}
      +2(I-V)
      +2R_{\rm fact},
}
\tag{5}
\]

where `V=Pr(K>0)=1-p_0`, `I=E K`, and

\[
R_{\rm fact}:=\sum_{k\ge1}W_k\log_2\frac{M_k}{W_k}.
\tag{6}
\]

For a pure level `K=k`, `M_k=W_k=1`, so (5) reduces to the already proved `H<=2k-2`. Thus (5) looked like a promising sequential-compression reduction: all coordinate-location complexity has been replaced by a scalar factorial-shadow inflation of the degree law.

## 2. Decisive obstruction: all atomwise upward inequalities still permit unbounded entropy/influence

The reduction (5) is not a route to FEI from (1) alone. In fact the complete family of atomwise upward inequalities (1) permits abstract spectral laws with `H/I -> infinity`.

Fix `m=3` and take even `n` tending to infinity. Put

\[
N=\binom n3,
\qquad
\varepsilon=\frac1{4\lfloor\sqrt N\rfloor},
\qquad
p=\frac{1-\varepsilon}{N}.
\tag{7}
\]

Define an **abstract** random subset law by assigning mass `p` to every 3-subset of `[n]`, mass `epsilon` to `[n]`, and zero elsewhere.

For a 3-set `A`,

\[
\nu_A=p+\varepsilon.
\]

Since `p<=1/N` and `epsilon>=1/(4 sqrt(N))`,

\[
p\le 16\varepsilon^2\le 16(p+\varepsilon)^2,
\]

which is exactly (1) squared at `|A|=3`. At the full set, the squared form of (1) is

\[
\varepsilon\le 4^{n-1}\varepsilon^2,
\]

which holds for all sufficiently large `n` (and in particular for the explicit example below). Every other atom has zero mass, so every atomwise upward inequality is satisfied.

But

\[
I=3(1-\varepsilon)+n\varepsilon\longrightarrow3,
\]

while

\[
H=(1-\varepsilon)\log_2\frac{N}{1-\varepsilon}
  +\varepsilon\log_2\frac1\varepsilon
  =3\log_2 n+O(1).
\]

Hence

\[
\boxed{H/I\to\infty.}
\tag{8}
\]

So the granular upward-mass lemma, even imposed at **every nonzero atom**, does not by itself contain enough Boolean structure to prove FEI.

A concrete rational instance is `n=200,m=3`:

- `N=1,313,400`, `floor(sqrt(N))=1146`;
- `epsilon=1/4584`;
- each 3-set has mass `4583/6020625600`;
- both upward inequalities hold exactly as rational comparisons;
- `I=13949/4584 = 3.042975567190227...`;
- `H=20.323408972885055...` bits;
- `H/I=6.678794661388278...`.

This is **not** a Boolean FEI counterexample. It is a counterexample to the relaxation obtained by retaining the full family (1) and forgetting the signed Fourier equations.

The same example explains why `R_fact` can blow up: the tiny top-level spike enters `M_3` multiplied by `binom(n,3)`, so a polynomially tiny high-degree tail can pay the upward inequalities of an exponentially/combintorially broad low level at negligible mean-degree cost.

## 3. The missing Boolean equation: translation autocorrelation

For a genuine Boolean `f`, write `a_A=\widehat f(A)`. The identity `f^2=1` says that every nonconstant Fourier coefficient of `f^2` vanishes. Equivalently, for every nonempty `U`,

\[
\boxed{
\sum_{A\subseteq[n]} a_A a_{A\triangle U}=0.
}
\tag{9}
\]

This is a signed constraint that no inequality involving only one upward mass at a time sees.

Pair the subsets under the fixed-point-free involution `A -> A triangle U`. Choosing one representative from each unordered pair, (9) becomes

\[
\sum_{\{C,D\}:C\triangle D=U}a_Ca_D=0.
\tag{10}
\]

This immediately gives the following quantitative structural lemma.

### Translation-partner lemma

Let `A!=B`, put `U=A triangle B`, and suppose `p_A p_B>0`. Then the other Fourier pairs with the same translation must have enough amplitude to cancel the pair `{A,B}`:

\[
\boxed{
\sum_{\substack{\{C,D\}\ne\{A,B\}\\ C\triangle D=U}}
\sqrt{p_Cp_D}
\ge \sqrt{p_Ap_B}.
}
\tag{11}
\]

Consequently their total endpoint spectral mass satisfies

\[
\boxed{
\sum_{\substack{\{C,D\}\ne\{A,B\}\\ C\triangle D=U}}
(p_C+p_D)
\ge 2\sqrt{p_Ap_B}.
}
\tag{12}
\]

**Proof.** Remove the target term from (10), take absolute values and use the triangle inequality to get (11). Apply `2 sqrt(xy)<=x+y` termwise to obtain (12). QED.

This is exactly the kind of branching alternative that the sequential-prediction route was missing: a large upward contribution from `B superset A` cannot be an isolated remote spike in a Boolean spectrum. It must come with other Fourier pairs separated by the same translation `B\A`.

## 4. Why the shell-plus-spike relaxation is killed immediately

In the abstract law of section 2, all 3-sets have odd degree and `[n]` has even degree because `n` is even. Fix any 3-set `A` and put

\[
U=[n]\setminus A.
\]

Then `|U|=n-3` is odd. The pair `{A,[n]}` has symmetric difference `U`.

Any two 3-sets have symmetric difference of **even** cardinality, so no shell-shell pair can have translation `U`. And the only pair involving `[n]` with translation `U` is `{A,[n]}` itself. Thus the support contains exactly one nonzero unordered pair in (10), making (10) impossible.

So the signed Boolean autocorrelation equation rejects the shell-plus-spike law in one line, even though every granular upward-mass inequality accepts it.

There is a useful general parity corollary.

### Parity anti-dominance corollary

Split the Fourier series into its even- and odd-degree parts. If both parity parts are nonzero, then **neither parity part can consist of a single Fourier atom**.

More quantitatively, if `b_B` is any coefficient in (say) the odd-degree part and the even-degree part is nonzero, then

\[
\boxed{
|b_B|\le \sum_{\substack{D\ne B\\ |D|\text{ odd}}}|b_D|.
}
\tag{13}
\]

One proof sums the cancellation requirement (11) over all even atoms paired with `B`; distinct translations correspond to distinct cross-parity pairs. Equivalently, write the odd part as

\[
o(x)=\frac{f(x)-f(-x)}2.
\]

Since the even part is nonzero, `o` vanishes somewhere; if one odd Fourier coefficient had magnitude larger than the sum of all the others, the triangle inequality would make `o(x)` nonzero at every point, a contradiction.

The shell-plus-spike relaxation violates the extreme case of (13): its even Fourier side contains only the top atom.

## 5. What this changes for APPROACH 1

Two scalar closures are now known to be the wrong endpoint:

1. the old Palm-only coding relaxation is unbounded;
2. the atomwise upward-mass relaxation is also unbounded, by section 2;
3. a standalone singleton branch-information constant is FEI-hard under balanced amplification (newer fleet03/B12 handoff).

The surviving compression route should therefore keep **signed translation partners** while coding. A concrete next target is a partner-aware hierarchical predictor:

- when an atom/prefix `A` has substantial continuation mass in a remote `B`, use `U=A triangle B` as a branch label;
- (11) forces competing spectral mass on other pairs with the same `U`;
- charge the log-loss of choosing the `A -> B` continuation against the entropy/influence created by those partner branches rather than against `nu_A` alone;
- recurse on the resulting translation classes or on a block partition aligned with `U`.

The key unresolved combinatorial question is a **non-overcounting allocation theorem**: can the partner mass required by (11), across the translations actually encountered by a spectral-sample code, be allocated with total charge `O(E|S|)`? A single pair belongs to exactly one translation `U`, which is encouraging, but its endpoints can participate in many translations, so a naive sum of (11) still overcounts. This is now a sharper obstruction than the previous generic 'avoid exponential ancestors' statement.

A second useful direction is to combine the exact hierarchical-block entropy defect from the fleet03 handoff with (9): block partitions aligned with a translation `U` preserve the composition behavior, while (9) supplies a signed certificate that an apparently isolated block continuation must have a competing branch.

## 6. Classification

- **PROVED:** factorial-shadow compression bound (5)-(6) from the granular upward-mass lemma plus Renyi-1/2 entropy.
- **PROVED DEAD ROUTE:** all atomwise granular upward-mass inequalities, by themselves, permit abstract laws with `H/I -> infinity`; explicit rational `n=200` example has `H/I=6.6787946613...`.
- **PROVED:** Boolean translation-partner inequalities (11)-(12), directly from `f^2=1`.
- **PROVED:** parity anti-dominance (13); in particular the shell-plus-spike obstruction cannot be a Boolean Fourier support.
- **NOT A BOOLEAN COUNTEREXAMPLE:** section 2 is deliberately an abstract spectral law used to test a relaxation.
- **OPEN:** a non-overcounting partner allocation / sequential predictor with total cost `O(I)`, hence full FEI.

The attached checker verifies the rational shell inequalities exactly and, on 200 deterministic random Boolean functions of six variables, verifies the autocorrelation identity and polygon/partner inequality exactly with integer Walsh coefficients. Those computations are sanity checks only; the proofs above are algebraic.
