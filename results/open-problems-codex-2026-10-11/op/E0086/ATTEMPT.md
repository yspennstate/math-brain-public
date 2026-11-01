# E0086 — source correction and partial results

Date: 2026-10-11. All statements below concern discrete-time simple symmetric random walk on Z² started at 0. Result 6 gives a negative answer under the literal unrestricted moving-offset hypotheses: a deterministic admissible nonempty singleton sequence in the emphasized power annulus need not have ANY deterministic almost-sure equivalent. This is a counterexample to the existence of such an asymptotic in that generality, not a formula for regular or fixed-direction sequences.

For a concrete parameter, α=3/8 gives a deterministic sequence H_n⊂{h:n^{3/8}<|h|≤2n^{3/8}}, |H_n|=1, with all-time normalized limsup 1/π and dyadic normalized limsup at most 15/(16π), almost surely. The complete construction and proof are in result 6. This example also has no deterministic equivalent f(n), whether or not f(n)/(log n)² converges.

## Exact objects

Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787v1, PDF pp. 2–4, defines D(x,r)={y∈Z²:|y−x|≤r}, R(n)={S₀,…,Sₙ}, K(n,x)=Σ_{j=0}^n 1{S_j=x}, and τ_n=inf{j≥0:S_j∈∂D(0,n)}. Thus τ_n is the first hit of the INNER boundary, not the first step outside the disc. For fixed M, the class H(M) consists of sets H⊂Z² with 0∉H, |H|≤M, and P(T_x<T_H)>0 for every x∈Hᶜ. The PDF typesets the origin exclusion awkwardly as “{0} /∈ H”; the intended exclusion is 0∉H. Here hitting times in the paper are positive-time hitting times.

The H-boundary is ∂_H G={x∈G:x+H⊂Gᶜ}, and M_H(n)=max_{x∈∂_H R(n)}K(n,x). Set a maximum over an empty boundary to 0. An offset set H is NOT a set of candidate sites over which local time is maximized.

The literal class allows H=∅. In that case ∂_H R(n)=R(n) at every time and M_H(n)/(log n)²→1/π. All moving-offset upper bounds below explicitly assume H_n≠∅. Thus the source hypotheses, literally read, cannot yield a single leading constant depending only on α across all H_n: for α<(√3−1)/4 the empty choice has constant 1/π while every nonempty annular choice has strictly smaller limsup by result 3.

Open problem 2, PDF p. 6, verbatim (mathematical typography normalized):

“Consider D̃_n ∈ H with D̃_n ⊂ D(0,a_n)^c and a_n → ∞ as n → ∞. Then, how is the asymptotic of M_{D̃_n}(n) with probability one?”

It singles out D̃_n⊂D(0,a_n)^c∩D(0,2a_n), a_n=n^β, 0<β<1/2. Its displayed conjecture for a_n≥n^{1/2+ε} is M_{D̃_n}(n)=max_x K(τ_n,x) eventually a.s. This has a time mismatch; we do not silently replace n by τ_n.

## 1. Far-offset regime at deterministic time (proved)

For every ε>0, if every h∈H_n has |h|>a_n≥n^{1/2+ε} eventually, then, almost surely, eventually ∂_{H_n}R(n)=R(n). Consequently M_{H_n}(n)=max_x K(n,x), and M_{H_n}(n)/(log n)²→1/π a.s. The equality is an elementary result; the limit uses the classical planar maximum-local-time theorem of Dembo–Peres–Rosen–Zeitouni (2001), also quoted on PDF p. 2 of Okada.

Proof in full. A coordinate increment X has mean zero and moment generating function E exp(tX)=(1+cosh t)/2≤exp(t²/2). Thus Markov's inequality applied to exp(tS_j^{(i)}) gives P(|S_j^{(i)}|≥u)≤2 exp(−u²/(2j)) for j≥1. If |S_j|≥r, at least one coordinate has absolute value ≥r/√2. Taking a union over j≤n gives P(max_{j≤n}|S_j|≥r)≤4n exp(−r²/(4n)). Put r=n^{1/2+ε}/3. The resulting series Σ_n 4n exp(−n^{2ε}/36) converges. The first Borel–Cantelli lemma implies max_{j≤n}|S_j|<a_n/3 eventually. Hence the diameter of R(n) is less than 2a_n/3. For x∈R(n) and h∈H_n, x+h cannot be in R(n): otherwise the diameter is at least |h|>a_n. Thus every visited x lies in ∂_{H_n}R(n). The reverse inclusion is its definition. The maximal-local-time theorem now supplies the limit. This argument is pathwise and even permits adaptively chosen offset sets meeting the distance condition. Empty offset sets also satisfy the equality without a distance condition.

## 2. The displayed exit-time equality is false as written (proved)

Write L_n=max_x K(n,x) and J_n=max_x K(τ_n,x). The classical theorem, explicitly quoted on Okada PDF p. 2, is L_n/(log n)²→1/π and J_n/(log n)²→4/π, a.s. Always M_{H_n}(n)≤L_n. Therefore limsup M_{H_n}(n)/J_n≤1/4 a.s.; in particular M_{H_n}(n)<J_n eventually, for every sequence of offsets. For the far-offset sets in result 1 the ratio actually tends to 1/4. These assertions follow by division by the positive limiting denominator 4/π. They refute the displayed subsidiary conjecture literally, but do not answer the main question for 0<β<1/2.

A concrete admissible sequence is H_n={(⌈2n^{1/2+ε}⌉,0)}. A singleton away from the origin has cardinality 1 and does not disconnect Z²: any finite nearest-neighbor path from 0 to x≠h can detour around h, and has positive walk probability. For x=0 a finite loop avoiding h gives positive probability of a return before hitting h. Thus H_n∈H(1), and |h|>n^{1/2+ε}.

For completeness, the detour and the positive-time convention can be made fully explicit. Start with a simple finite lattice path from 0 to x≠0,h. If it passes through h, its predecessor and successor are neighbors of h. Replace that portion by a path along the eight-point nearest-neighbor cycle whose successive offsets from h are

(1,0),(1,1),(0,1),(−1,1),(−1,0),(−1,−1),(0,−1),(1,−1),

closing back to h+(1,0). This cycle contains all four neighbors of h and avoids h. The resulting finite walk from 0 to x avoids h and has probability 4^{-length}>0; it witnesses T_x<T_h. For x=0, choose a neighbor u of 0 different from h and use the two-step loop 0,u,0, with probability 1/16. This witnesses the strictly positive-time return T_0<T_h. Therefore every nonzero singleton belongs to the literal class H(1), including every offset in the scan construction.

## 3. A moving-offset upper bound (proved, using the classical potential kernel)

The following classical input is used with its usual simple-square-lattice normalization. The potential kernel a satisfies a(0)=0, a(z)=a(−z), (P−I)a(z)=1{z=0}, and a(z)=(2/π)log|z|+O(1), with a uniform bounded error for |z|≥1. Planar simple random walk is recurrent. These are standard potential-kernel facts; the external reference and exact location are recorded in LITERATURE.md. All deductions from these inputs are proved below.

**Killed-return identity.** For h≠0, let T_h be its positive-time hitting time, and let N_h=Σ_{j=0}^{T_h−1}1{S_j=0}. Then E N_h=2a(h), and P(N_h≥k)=(1−1/(2a(h)))^{k−1}, k≥1.

Proof. Put g(z)=a(z)+a(h)−a(z−h). The asymptotic of a implies g is bounded for each fixed h: the difference of the two logarithms is bounded outside a sufficiently large ball, and only finitely many lattice points remain inside. We have g(0)=0, g(h)=2a(h), and (P−I)g(z)=1{z=0}−1{z=h}. For bounded stopping time T_h∧m, conditioning each increment of g(S_j) on the past and summing gives

E g(S_{T_h∧m})=E Σ_{j<T_h∧m}1{S_j=0}.

The contribution 1{S_j=h} is zero before T_h. Recurrence gives T_h<∞ a.s. Bounded convergence on the left and monotone convergence on the right give E N_h=2a(h). At every visit to 0, the strong Markov property gives the same probability q_h of hitting h before the next return to 0. This probability is positive (follow a simple path to h without returning to 0). The walk hits either of these two sites almost surely. Induction therefore gives P(N_h≥k)=(1−q_h)^{k−1}, so E N_h=1/q_h. Comparing expectations proves q_h=1/(2a(h)) and the displayed tail formula.

**Finite-time tail.** For any fixed nonempty H not containing 0, any h∈H and integer k≥1,

P(M_H(n)≥k)≤(n+1)(1−1/(2a(h)))^{k−1}≤(n+1)exp(−(k−1)/(2a(h))).

Proof. If an eligible site x has at least k visits by time n, let j≤n be its first visit. From time j onward the translated walk starts at 0, has at least k visits to 0 (including time j), and does not hit h before these visits, since x+h is absent from the full range through n. Conditional on the history through deterministic time j, the probability of this future event is at most P(N_h≥k). Take a union over all j=0,…,n, dispensing with the first-visit requirement, which can only enlarge the event. There is no union over lattice sites: the site at time j is S_j.

**Uniform almost-sure upper bound.** Fix 0<α<1/2 and C<∞. Simultaneously for every sequence of nonempty H_n such that H_n contains at least one h with 0<|h|≤C n^α,

limsup_{n→∞} M_{H_n}(n)/(log n)² ≤ 4α(1+2α)/π, a.s.

In particular, this applies to the nonempty annular offset sets in Open problem 2. Combining it with the global maximum bound gives the upper bound min{1,4α(1+2α)}/π. It is strictly smaller than 1/π for α<(√3−1)/4. If a nonempty H_n contains a nonzero offset of length n^{o(1)}, the same argument gives M_{H_n}(n)/(log n)²→0 a.s.

Proof. Work in blocks N≤n<2N, N=2^m. All candidate h have length at most C(2N)^α, and there are at most C₁ N^{2α} such lattice points, for a constant C₁ depending only on C,α. Uniformly over these points,

2a(h) ≤ (4α/π)log N + C₂ =: A_N

for all sufficiently large N. Fix c>4α(1+2α)/π and set k_N=⌈c(log N)²⌉. If M_{H_n}(n)≥k_N for any time in this block, choose a suitable h∈H_n and the first visit time j≤n of an eligible site. That walk segment avoids S_j+h until it makes k_N visits to S_j. This segment need not avoid h all the way to 2N, but the event implies at least k_N visits before the unrestricted future first hit of h. There are at most 2N+1 choices of j and C₁N^{2α} choices of h. Applying the conditional geometric bound to each choice gives probability at most

C₁N^{2α}(2N+1)exp(−(k_N−1)/A_N)
 = N^{1+2α−πc/(4α)+o(1)}.

The limiting exponent is negative by the choice of c, so these probabilities are summable over N=2^m. Borel–Cantelli implies that eventually every n in every block has M_{H_n}(n)<k_N. Since log n≥log N, the limsup is at most c. Intersect the probability-one events for a countable sequence of c decreasing to 4α(1+2α)/π. This proof bounds an event allowing ALL offsets and ALL times in a block, so its conclusion is simultaneous and does not assume H_n varies monotonically or slowly. The global upper bound is the classical maximum-local-time limit. Finally, for the subpolynomial claim apply the uniform bound for each positive rational α<1/2, taking C=1 eventually, and send α down to 0. Nonnegativity supplies the matching zero lower bound.

## 4. The general exterior hypotheses do not force a log-squared limit (counterexample)

Let a_n=log(n+2), and choose singleton offsets H_n={(r_n,0)}, where r_n=n²+10 for even n and r_n=⌈2log(n+2)⌉ for odd n. Every H_n belongs to H(1), by the path-detour argument in result 2; r_n>a_n for every n and a_n→∞. Thus these satisfy the general exterior hypotheses with nonempty sets and a single common distance sequence.

For even n, r_n>n, while the diameter of any n-step nearest-neighbor walk range is at most n. Indeed, for two visited sites S_i,S_j their distance is at most |i−j|≤n. Hence ∂_{H_n}R(n)=R(n) deterministically for even n. The classical maximum-local-time limit gives M_{H_n}(n)/(log n)²→1/π along even n a.s.

For odd n the unique offset has length O(log n), which is subpolynomial. To use result 3 without imposing its hypothesis on even n, introduce the auxiliary singleton sequence H'_n={(⌈2log(n+2)⌉,0)} for all n. Its normalized maximum tends to 0 a.s. Since H_n=H'_n on odd n, the same zero limit holds on that subsequence. Intersecting these two probability-one events proves

liminf M_{H_n}(n)/(log n)²=0 and limsup M_{H_n}(n)/(log n)²=1/π, a.s.

The limsup is no larger than 1/π because M_{H_n}(n)≤L_n for all n, and the liminf is no smaller than 0. Thus the conclusions above are exact. This disproves the existence of a normalized limit under the unrestricted exterior assumptions alone. It does not address the nonempty power-annulus question, because the even offsets are not in the radius-[a_n,2a_n] annulus.

If empty sets are retained literally in the class, even the fixed power annulus admits a simple no-limit example for α<(√3−1)/4: set H_n=∅ on even n and H_n={(⌊n^α⌋+1,0)} on odd n, for all sufficiently large n when that integer is ≤2n^α. The even subsequence has limit 1/π and the odd subsequence has limsup ≤4α(1+2α)/π<1/π. This observation is a degeneracy of the stated class, not a substitute for investigating its intended nonempty case.

## 5. Sharper bound retaining finite-time confinement (prior argument independently checked)

The 2026-09-18 NM13-12 repository reports already contain both result 3 and the sharper argument below. They are internal research records, not a published solution of the open problem. We independently verify the upper argument here and make no novelty claim. The prior packet lower-bound report is retained as a lead only; its lengthy finite-volume estimates have not all been independently checked in this attempt.

For deterministic nonempty offset sets in the source annulus, 0<α<1/2, put g(α)=4α(1−α)/π. Then:

(i) for every c>g(α), P(M_{H_n}(n)≥c(log n)²)→0;

(ii) almost surely limsup M_{H_n}(n)/(log n)²≤min{1,4α(1−α)(1+2α)}/π.

More generally, choose a deterministic witness h_n∈H_n, let W_m={h_n:2^m≤n<2^{m+1}}, and let ρ=limsup_m log|W_m|/log(2^m). Then the almost-sure upper bound in (ii) improves to min{1,4α(1−α)(1+ρ)}/π. Here 0≤ρ≤2α. These remain upper bounds, not equivalents.

**Disk Green identity.** To avoid confusing stopping conventions with the source, write σ_R=inf{j:S_j∉D(0,R)}, and G_R(x,z)=E_x Σ_{j<σ_R}1{S_j=z}. For h≠0 inside the disc, let B_{R,h}=E_0 Σ_{j<σ_R∧T_h}1{S_j=0}. Then

B_{R,h}=G_R(0,0)−G_R(0,h)²/G_R(h,h).

Proof. The finite-state substochastic transition matrix inside the disc is symmetric; hence each of its powers is symmetric, and their entrywise sum G_R is symmetric. Exit has finite expectation: from each of finitely many states choose a path to outside, choose a common finite maximum path length L and the positive minimum probability p of following its chosen path; the strong Markov property bounds P(σ_R>kL)≤(1−p)^k. Strong Markov at T_h gives G_R(0,0)=B_{R,h}+P_0(T_h<σ_R)G_R(h,0), and G_R(0,h)=P_0(T_h<σ_R)G_R(h,h). The denominator is ≥1 since a walk started at h visits h at time 0. Eliminating the hitting probability and using symmetry proves the identity. Exactly as in the killed-return proof, the number of visits counted by B_{R,h} is geometric and has success probability 1/B_{R,h}.

**Green asymptotics.** The potential-kernel increment identity, stopped at σ_R∧m for a walk starting at x, gives

G_R(x,z)=E_x a(S_{σ_R}−z)−a(x−z).

Indeed, (P−I)a(w−z)=1{w=z}; summing conditional increments proves the stopped identity. The stopped positions lie in the radius-R+1 disc, so the kernel values are bounded. Finite exit expectation, bounded convergence, and monotone convergence justify letting m→∞. Now fix s>1/2 and take R=n^s, with n^α<|h|≤2n^α. At exit R<|S_{σ_R}|≤R+1, so uniformly for z=0,h and all starting x in the disc,

E_x a(S_{σ_R}−z)=(2s/π)log n+κ+o(1),

where κ=(2γ+log8)/π. This follows directly by the triangle inequalities R−|z|<|S_{σ_R}−z|≤R+1+|z| and |z|/R→0, followed by the uniform potential-kernel expansion. Therefore

G_R(0,0)=(2s/π)log n+O(1),
G_R(h,h)=(2s/π)log n+O(1),
G_R(0,h)=(2(s−α)/π)log n+O(1).

Inserting these in the exact elimination identity, whose denominator is asymptotic to a positive multiple of log n, gives uniformly in the annulus

B_{R,h}=b_s(α)log n+O(1), where b_s(α)=(2/π)(2α−α²/s).

The O(1) remainder after dividing the squared numerator follows by writing each entry as its displayed leading multiple of log n plus a bounded error, expanding the square, and dividing by a denominator bounded below by (s/π)log n for all large n. Notice b_s(α)↓g(α) as s↓1/2.

**Finite-time tail and (i).** On C_n={max_{j≤n}|S_j|≤R/4}, after a first visit to any candidate y every subsequent displacement from y stays within radius R/2. If y is eligible for H_n and has k visits by n, the translated walk has k visits to 0 before hitting h_n or exiting D(0,R). The geometric formula, conditional on each candidate visit time, and a union over those times give

P(M_{H_n}(n)≥k)≤P(C_n^c)+(n+1)exp(−(k−1)/B_{R,h_n}).

Result 1's coordinate estimate gives P(C_n^c)≤4n exp(−n^{2s−1}/64). For c>g(α), choose s>1/2 close enough to 1/2 that b_s(α)<c. With k=⌈c(log n)²⌉ the second term is n^{1−c/b_s(α)+o(1)}→0, while the confinement term tends to zero. Ceilings do not affect this conclusion; replacing c by any smaller intermediate threshold handles the distinction between integer and real event thresholds. This proves (i).

**Dyadic proof of (ii).** Fix c>g(α)(1+ρ). Choose s>1/2 and η>0 such that c>b_s(α)(1+ρ+η). In block N≤n<2N, use common radius R=(2N)^s and confinement max_{j≤2N}|S_j|≤R/4. Its failure probability is at most 8N exp(−(2N)^{2s−1}/64). All h∈W_m have N^α<|h|≤2(2N)^α, so the same Green expansion holds with log N and coefficient b_s(α), uniformly. There are at most N^{ρ+η} offsets for all large blocks. An eligible witness with k_N=⌈c(log N)²⌉ visits must therefore give a geometric-return event for one of at most (2N+1)N^{ρ+η} pairs (start time,offset), before the common disk exit. The block failure probability is at most

8N exp(−(2N)^{2s−1}/64)+N^{1+ρ+η−c/b_s(α)+o(1)}.

Both terms are summable over N=2^m. Borel–Cantelli, log n≥log N, and a countable sequence of c decreasing to g(α)(1+ρ) give the stated limsup. The global maximum gives the separate 1/π bound. There are O(N^{2α}) lattice points in the offset annulus, giving ρ≤2α and (ii). This argument does not assume monotonicity of H_n. For each fixed deterministic sequence all offsets in W_m are deterministic, which suffices for the conditional Markov bound.

## 6. Deterministic annular scanning: no deterministic almost-sure equivalent (counterexample)

**Theorem.** Fix any α with 1/4<α<1/2. There exists a deterministic sequence of nonempty singleton sets H_n∈H(1), with

H_n⊂D(0,n^α)^c∩D(0,2n^α),

such that, almost surely,

limsup_n M_{H_n}(n)/(log n)²=1/π,

while along dyadic times

limsup_m M_{H_{2^m}}(2^m)/(log 2^m)²≤g(α)=4α(1−α)/π<1/π.

In particular the normalized maximum does not converge. More strongly, there is no deterministic function f(n)>0 eventually for which M_{H_n}(n)/f(n)→1 almost surely. Thus even allowing a deterministic equivalent to depend on the entire deterministic offset sequence does not repair the question without further regularity hypotheses.

The additional external input is Dembo–Peres–Rosen (2007), Theorem 1.1, PDF p. 2: the radius ℛ(t) of the largest completely covered lattice disc at deterministic time t satisfies ℛ(t)=t^{1/4+o(1)} a.s. The paper and statement have been fetched and checked; this is not a moving-offset theorem. Its use below is our own deduction.

The covered-disc paper uses open Euclidean discs, whereas Okada defines closed lattice discs. Only the upper bound is needed here: if a closed lattice disc of radius r is completely covered, its open subdisc of that same radius is completely covered as well. Hence ℛ(t)≥r in the paper's convention. No equivalence of boundary conventions is required for the argument.

**Deterministic construction.** For N=2^m let

A_N={h∈Z²:(2N)^α<|h|≤2N^α}, and b_N=|A_N|.

Order A_N lexicographically, once and for all. A_N is deterministic, excludes 0, and b_N≤(4N^α+1)²=O(N^{2α})=o(N). For every sufficiently large dyadic block N≤n<2N there is room to assign its b_N offsets to the first b_N times: if h^{(i)} is the i-th offset, put H_{N+i−1}={h^{(i)}} for 1≤i≤b_N. At all other times use the fallback H_n={(⌊n^α⌋+1,0)}. For the finitely many blocks in which b_N>N use the fallback throughout. If b_N=0, also use the fallback throughout that block. This defines H_n deterministically for every n≥1.

Every assigned offset is in the required annulus: for N≤n<2N,

|h|>(2N)^α≥n^α and |h|≤2N^α≤2n^α.

The fallback also satisfies n^α<⌊n^α⌋+1≤n^α+1≤2n^α. Each singleton is admissible in H(1), by the detour/return-loop proof already given in result 2. No offset is selected using the walk; only the witness index in the following proof is random.

**Geometric hole lemma.** On the event ℛ(2N)=o(N^α), for every lattice site x and all sufficiently large N, at least one point of x+A_N is unvisited at time 2N.

Proof. Set L=2^α, c=(L+2)/2, d=(2−L)/4>0, and q_N=(⌊cN^α⌋,0). If |z−q_N|≤dN^α, then

|z|≥|q_N|−dN^α≥(c−d)N^α−1>L N^α

for all large N, because c−d−L=d>0. Also

|z|≤|q_N|+dN^α≤(c+d)N^α<2N^α,

because 2−c−d=d>0. Thus the entire lattice disc D(q_N,dN^α) is contained in A_N. If all x+A_N were visited at time 2N, the disc D(x+q_N,dN^α) would be completely covered, forcing ℛ(2N)≥dN^α. This contradicts ℛ(2N)=o(N^α). The same N threshold works for every x because the geometry and ℛ are translation independent. Finally, Theorem 1.1 ensures ℛ(2N)/N^α→0 a.s. when α>1/4. This proves the lemma simultaneously over all x.

**Limsup proof.** Choose any favorite site x_N at time N, so K(N,x_N)=L_N=max_x K(N,x). On the probability-one covered-disc event, the hole lemma supplies h∈A_N with x_N+h∉R(2N). It appears at a deterministic scan time n_N=N+i−1<2N. At that time x_N∈R(n_N), x_N+h∉R(n_N), and K(n_N,x_N)≥K(N,x_N)=L_N. Consequently

M_{H_{n_N}}(n_N)≥L_N.

There is no monotonicity assumption about generalized boundaries in this argument: the hole is chosen from the range at the END of the block, so it remains a hole at its scheduled time. Since N≤n_N<2N, log n_N/log N→1. The classical limit L_N/(log N)²→1/π gives limsup_n M_{H_n}(n)/(log n)²≥1/π a.s. The reverse inequality follows from M_{H_n}(n)≤L_n for every n. This proves the exact limsup.

**Dyadic upper subsequence.** For every c>g(α), the proof of result 5(i) gives, for some δ>0 and s>1/2 and all sufficiently large n,

P(M_{H_n}(n)≥c(log n)²)≤4n exp(−n^{2s−1}/64)+n^{−δ}.

To see a fixed δ explicitly, choose an intermediate c' with g(α)<c'<c and s with b_s(α)<c'. The tail with threshold ⌈c'(log n)²⌉ is n^{1−c'/b_s(α)+o(1)}; take δ=(c'/b_s(α)−1)/2>0 for all large n. The event at the real threshold c(log n)² is contained in that integer-threshold event for all large n. This is a deterministic-sequence bound, and our scan schedule is deterministic. At n=2^m both displayed terms are summable over m. Borel–Cantelli and a countable sequence c↓g(α) therefore give the claimed dyadic limsup. Since g(α)<1/π for α<1/2, the all-time normalized sequence cannot converge.

**No deterministic equivalent, even an oscillating one.** Suppose, to the contrary, that a deterministic eventually positive f satisfies M_{H_n}(n)/f(n)→1 a.s. We first show limsup f(n)/(log n)²≤g(α). If not, choose constants g(α)<c<d<limsup f(n)/(log n)², and a deterministic subsequence n_j with f(n_j)≥d(log n_j)². Almost-sure convergence of the assumed ratio implies M_{H_{n_j}}(n_j)>c(log n_j)² for all large j a.s. The indicators of these events consequently tend to 1 a.s., and bounded convergence implies their probabilities tend to 1. Result 5(i) says those probabilities tend to 0, a contradiction. Thus the asserted deterministic limsup bound holds. Intersect it with the assumed ratio convergence: for every η>0, eventually f(n)≤(g(α)+η)(log n)² and M_{H_n}(n)≤(1+η)f(n). Sending η↓0 gives limsup M_{H_n}(n)/(log n)²≤g(α), contradicting the already proved limsup 1/π. This proves that no deterministic equivalent exists.

This counterexample uses neither empty offset sets nor random/adaptive choices, has fixed cardinality bound M=1, and keeps the exact n^α annular hypotheses. It is an obstruction in the main regime, not only in the loosely constrained exterior regime.

## Referee checks and scope limitations

The two time parameters cannot be identified: τ_n is an exit time from a radius-n disc and is on the n² scale. The source's limit constants themselves contradict the displayed equality. The corrected deterministic-time result requires offset distances exceeding the range diameter, and is not a covered-disc argument. A largest covered disc establishes the existence of an unvisited point in each sufficiently large disc; it does NOT establish that every point of a prescribed finite offset set is unvisited.

The upper-bound proof pays for all candidate offsets in a dyadic block. Applying a fixed-H monotonicity argument directly to changing H_n would be invalid. Also, the geometric probability controls returns before hitting the offset, not returns before a deterministic time; passing to the unrestricted future is an enlargement, so the direction of the inequality is correct. No independence between the candidate events is needed.

Finite verification: finite_checks.py enumerates all 4⁸=65,536 eight-step paths, separately for h=(1,0), (2,0), and (1,1). It verifies each boundary-maximum tail against (n+1)p_h^{k−1}, each truncated killed-local-time tail against p_h^{k−1}, and the deterministic boundary equality for h=(9,0), for all paths. The potential-kernel values used are 1, 4−8/π, and 4/π. All assertions passed; the raw exact path counts and floating-point comparisons are in finite_checks.json. This is a check of finite implications and normalizations, not evidence of a sharp asymptotic constant.

Boundary.lean formalizes the purely algebraic displacement implication used in result 1. On 2026-10-12 local time, `lake env lean ~/brain_workers/TRIO_1011/op/E0086/Boundary.lean`, run from ~/lean_verify, passed with exit code 0 and no compiler diagnostics after a shared-slot wait of 1,815 seconds. It imports only Mathlib.Algebra.Group.Basic and Mathlib.Data.Set.Defs and uses proof terms checked by the kernel, with no sorry or native_decide. The probabilistic proofs, potential-kernel theorem, and scanning asymptotics are not formalized in Lean. The result is recorded in lean_check.json.

The sharper disk calculation was also checked directly on finite killed Markov chains: green_checks.py constructs I−P on the radius-5, radius-10, and radius-20 lattice discs (at most 1,257 states), solves for the unrestricted disc Green columns, and compares the one-trap elimination formula to a direct solve after removing the trap. Nine combinations of radius and offset were tested; the largest absolute discrepancy was 1.999×10^{-15}. Green symmetry and positivity were also asserted. These floating-point checks are recorded in green_checks.json and supplement, rather than replace, the exact Markov proof.

scan_checks.py enumerates the common annuli and the contained discs for α=0.3, 0.375, 0.45 and N=256,4096,65536. All nine geometry checks passed. In every case where the scan fits, each scheduled offset was checked against its own actual time n, not only against the block endpoints. Some finite blocks do not fit (especially at α=0.45); the definition explicitly uses the fallback in those blocks, and 2α<1 proves that only finitely many such blocks occur. These numerical checks use floating-point comparisons and are only supplementary; the inequalities in the geometric hole proof are exact real inequalities.

scan_walk_checks.py verifies the finite path implication on 20 seeded simple random walks through time 8192, using N=4096, α=3/8, and a fixed lexicographic schedule of 3,728 offsets. Every run had a hole relative to a favorite at time N. For the first such offset in the schedule, direct prefix calculations verified eligibility at its scheduled time, the actual-time annulus condition, and local time at least the global maximum at N. All 20 checks passed. The schedule is fixed before generating the walks. These checks test the deterministic implication used by the proof; they are not a measurement of the asymptotic limsup or of the probability tail.

Final counterexample referee checklist:

1. Offset schedule deterministic? Yes: lexicographic enumeration of a deterministic lattice annulus; only the proof's successful scan index depends on the walk.
2. Common cardinality and admissibility? Every H_n is a singleton in H(1); no empty-set degeneracy is used.
3. Correct annulus at each time? Lower radius uses the latest time 2N; upper radius uses the earliest time N. Both inequalities are explicitly verified.
4. Enough scan times? b_N=O(N^{2α})=o(N), with fallback for the finite initial failure blocks.
5. Coverage quantifier? If the WHOLE common annulus around any x were covered, its contained radius-dN^α disc would contradict the global largest-covered-disc upper theorem. No statement about any prescribed individual offset is inferred from that theorem.
6. Hole survives until its scheduled time? The chosen hole is absent at time 2N, hence also absent at the earlier scan time.
7. Favorite site chosen at the correct time? x_N is a favorite at the block START N; its local time cannot decrease before the scan time.
8. Almost-sure subsequence versus convergence in probability? The dyadic conclusion uses explicit polynomial tail rates and summability, not a mistaken direct inference from convergence in probability.
9. Oscillating deterministic equivalents? Excluded separately using the probability upper bound and bounded convergence of event indicators.
10. Scope? This negative example treats 1/4<α<1/2 and arbitrary moving offset sequences. It does not claim a regular-sequence theorem or a characterization for every sequence.

Result 6 is a complete counterexample to a deterministic almost-sure asymptotic under the literal hypotheses, including the nonempty power-annulus restriction for 1/4<β<1/2. It also disproves the conjectural universal almost-sure singleton constant suggested in the prior internal reports when applied without a temporal-regularity restriction. It does not give a full description of liminf/limsup for every possible offset sequence, does not settle regular or frozen-direction singleton sequences, and does not determine a matching constant for 0<β≤1/4. Those strengthened or restricted questions remain unresolved here. The finer liminf of the scanning example is not identified: we prove only liminf≤4β(1−β)/π and the exact limsup 1/π, which suffice to rule out convergence and every deterministic equivalent.
