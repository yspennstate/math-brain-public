# F0022 source check and initial result (2026-10-12)

Source: V. Beffara and H. Duminil-Copin, *Planar percolation with a glimpse of Schramm-Loewner evolution*, arXiv:1107.0158, downloaded from https://arxiv.org/pdf/1107.0158. PDF page 44, Section 5, Question 1 reads:

> Question 1. Prove that the mean number of clusters per site κ(p) = E_p(|C|^{-1}) behaves like |1/2−p|^{2+α+o(1)}, where C is the cluster at the origin and α = −2/3.

The preceding heading specifies site percolation on the triangular lattice. No Taylor subtraction is stated. The printed power is 4/3.

## Counterexample to the literal formula

Take independent Bernoulli(p) occupation variables on the triangular lattice. Write C(0) for the open cluster of the origin. Define X=1/|C(0)| on finite nonempty clusters, X=0 on an infinite cluster, and X=0 when the origin is closed. This is the usual convention for the mean number of open clusters per site. Without a convention for an empty cluster the displayed expectation is undefined.

There are exactly six distinct neighbors of the origin. Let A be the event that the origin is open and its six neighbors are closed. Independence gives P_p(A)=p(1-p)^6. On A, C(0)={0} and X=1. Elsewhere X≥0. Consequently

κ(p)=E_p X≥p(1-p)^6.

For every p in [1/4,3/4], this is at least (1/4)^7=1/16384. In particular liminf_{p→1/2} κ(p)≥1/128 by the sharper continuous lower bound. Any function |1/2-p|^{4/3+ε(p)} with ε(p)→0 tends to zero: eventually its exponent is ≥2/3 and, for 0<|1/2-p|<1, it is ≤|1/2-p|^{2/3}. The same holds if multiplied by a bounded constant. Thus κ(p) cannot have the printed asymptotic on either side of 1/2.

If the expectation is conditioned on the origin being open instead, the same proof gives E_p[X | 0 open]≥(1-p)^6, also bounded away from zero. If C means the cluster of the origin's color, the isolated-open event still proves the lower bound. The counterexample is not dependent on these reasonable alternative conventions.

## Continuity, with a full elementary proof

For a positive integer M, let X_M=X 1{1≤|C(0)|≤M}. The event C(0)=S, where S is a finite connected vertex set containing 0, says exactly that every vertex of S is open and every vertex of its external vertex boundary ∂S is closed. It therefore has probability p^{|S|}(1-p)^{|∂S|}.

Every connected set S of size ≤M containing 0 lies in graph-distance ball B(0,M-1): a path within S from 0 to any vertex can be taken simple and has at most M-1 edges. This ball is finite, so there are finitely many such S. The expectation

κ_M(p)=Σ_{S connected, 0∈S, |S|≤M} |S|^{-1}p^{|S|}(1-p)^{|∂S|}

is a polynomial in p, hence continuous on [0,1]. Pointwise 0≤X-X_M≤1/(M+1), because finite clusters omitted have at least M+1 vertices, while empty and infinite clusters contribute zero. Taking expectations yields sup_{p∈[0,1]}|κ(p)-κ_M(p)|≤1/(M+1). To show continuity directly, fix p0 and ε>0, choose M with 2/(M+1)<ε/2, then choose δ so |κ_M(p)-κ_M(p0)|<ε/2 when |p-p0|<δ. The triangle inequality gives |κ(p)-κ(p0)|<ε. Therefore κ is continuous and κ(1/2)≥1/128; in fact κ(p)→κ(1/2)>0.

## Scope

This disproves the question exactly as printed. It does not resolve a repaired question about a nonanalytic remainder after subtracting a Taylor polynomial. The usual specific-heat convention suggests 2−α=8/3, whereas the source prints 2+α=4/3. That suggested repair is not assumed or claimed proved here. Literature search and independent checks are complete; see LITERATURE.md and the checks below.


## Conditional reduction for a corrected formulation (not a solution of it)

Here is the exact scope of what a third-derivative upper bound would yield. Let f∈C²([0,a])∩C³((0,a]) and suppose that, for every η∈(0,2/3), |f'''(t)|≤C_η t^{−1/3−η} for sufficiently small t>0. Then

|f(h)−f(0)−h f'(0)−h² f''(0)/2|≤C_η h^{8/3−η}/[(2/3−η)(5/3−η)(8/3−η)].

Proof. Fix η and sufficiently small h. The bound is integrable on (0,h) since −1/3−η>−1. For δ>0, the fundamental theorem of calculus gives f''(u)−f''(δ)=∫_δ^u f'''(t)dt. Let δ↓0; continuity of f'' at zero and absolute convergence give f''(u)−f''(0)=∫_0^u f'''(t)dt. Integrate this identity twice, using f' and f continuous at zero. Fubini is justified by the absolute bound C_η h²∫_0^h t^{−1/3−η}dt<∞. The remainder equals (1/2)∫_0^h(h−t)² f'''(t)dt. For b=−1/3−η, direct integration gives

(1/2)∫_0^h(h−t)²t^b dt = h^{b+3}/[(b+1)(b+2)(b+3)].

Indeed expand (h−t)² and integrate each of h²t^b, −2h t^{b+1}, t^{b+2}; the coefficient is (1/2)[1/(b+1)−2/(b+2)+1/(b+3)]=1/[(b+1)(b+2)(b+3)]. This proves the inequality. The same argument applies on the other side by setting f(t)=κ(1/2−t).

This lemma is independently proved. Applying it to κ would additionally rely on the cited regularity and derivative estimates, which we have not independently proved here. It provides an upper estimate only. The remaining corrected target is the full two-sided logarithmic law

|R(h)|=|h|^{8/3+o(1)}, R(h)=κ(1/2+h)−κ(1/2)−κ'(1/2)h−κ''(1/2)h²/2.

Neither the singleton lower bound nor an existential subsequence lower bound for |κ'''| proves a lower bound for |R(h)| for every small h. One would need a quantitative estimate that controls integration and cancellation. This corrected target is not substituted for the original question in our verdict.

## Exact computations and Lean verification

- exact_checks.py enumerates all 128 configurations of the origin and six neighbors, using exact fractions at p=0, 1/4, 49/100, 1/2, 51/100, 3/4, 1. Total probability is 1, and exactly one configuration is the isolated-open event, with probability p(1−p)^6. All assertions passed; outputs are in exact_checks.json.
- The same script constructs all rooted connected sets of sizes 1 through 5 on the coordinate triangular lattice with steps ±(1,0), ±(0,1), ±(1,1). Each next level is obtained by adjoining a boundary site and deduplicating. Every rooted connected set is generated, because a spanning tree permits removal of a non-root leaf, leaving a connected predecessor; repeated removal reaches {0}. Conversely every generated set is connected. The numbers are 1, 6, 33, 176, 930. Exact finite-cluster contributions at p=1/2 are 1/128, 3/1024, 13/8192, 65/65536, 357/524288. Their sum is 7341/524288≈0.0140, a further computational lower bound. This enumeration is an independent check; the solved verdict uses only the first elementary term.
- Singleton.lean imports only Mathlib.Data.Rat.Defs and Mathlib.Tactic.NormNum. It verifies (1/2)(1−1/2)^6=1/128, 2+(−2/3)=4/3, and 1/128>0. Command: lake env lean ~/brain_workers/TRIO_1011/op/F0022/Singleton.lean, run from ~/lean_verify, one Lean invocation at a time with a 3600-second process timeout. The first invocation failed because PowerShell introduced a UTF-8 BOM; after removing the BOM the invocation exited 0. lean_check.txt records the successful output and axioms. No sorry or native_decide is used. Norm_num produces ordinary kernel-checked proof terms. Only these algebraic statements are formally checked, not the infinite-volume probability or continuity proof.

## Hostile referee audit

1. **Empty/infinite cluster convention:** stated explicitly. Infinite clusters contribute zero. The singleton argument also survives conditioning on occupation or using clusters of either color. Without an empty-cluster convention the expectation is undefined, not evidence for the proposed asymptotic.
2. **Independence and degree:** the triangular lattice has six distinct neighbors; the event fixes seven independent Bernoulli variables. Exact local enumeration agrees. Exterior variables are unrestricted; no path can leave an isolated origin.
3. **Nonnegativity:** reciprocal finite sizes are nonnegative; omitting other events cannot increase the lower bound. No infinite-cluster probability or arm estimate is needed.
4. **Critical point versus approach:** the lower bound holds for every p, not only p=1/2. Its continuity yields a positive liminf on either side. Thus setting a special value at p=1/2 cannot avoid the contradiction.
5. **The o(1) exponent:** an exponent approaching 4/3 stays positive; the stated power must tend to zero. The exact arithmetic is Lean checked.
6. **Uniform polynomial approximation:** connected rooted sets of bounded size lie in a finite ball; their exterior boundaries are finite; the omitted reciprocal is ≤1/(M+1) uniformly in p, including p=0 and p=1. The epsilon proof of continuity is given above.
7. **Interpretation of “singularity”:** a nonsmooth part can vanish while κ itself tends to a positive background. Our counterexample does not disprove the conventional singular-part prediction. No authorial erratum has been located or asserted.
8. **Literature quantifiers:** Zhang's lower bound is along a sequence, not for all small deviations. Mertens–Jensen–Ziff's expansion is not an independently checked rigorous proof. API rate limits prevent an exhaustive current-status conclusion.
9. **Prior work:** the repository already records this literal counterexample. It was rederived and independently checked; it is not presented as novel research.

## Final scope and gap

The literal source formula has a complete counterexample; no gap remains in that conclusion. The regular-background-subtracted 8/3 law is a different problem and is not proved or refuted in this folder. The conditional upper-bound reduction above makes one implication precise but supplies no uniform lower bound for that remainder.
