# R19 / I0110 — torsion-scale obstruction to a single persistent-relator scale

Date: 2026-09-17 UTC.

This note continues the route in `runs/R19/2026-09-17_05-50-15_UTC__i0110-persistent-relator-deck.md`. It does not change the frozen `M_9=9/9` metric and does not claim Salez Problem 2.1 solved. Its purpose is to attack the new graph-intrinsic persistent-relator route on a source-valid random-Abelian family.

## 1. Source input used

Hermon--Olesker-Taylor, *Cutoff for Almost All Random Walks on Abelian Groups*, arXiv:2102.02809v2, define for every `gamma in N union {infinity}` the entropic time `t_gamma` by the condition that the entropy of rate-one walk on `Z_gamma^k` equals

`log |G / gamma G|`,

with `Z_infinity=Z`, and set

` t_* = max_gamma t_gamma `.

Their Theorem A gives cutoff at `t_*` with high probability for Abelian `G` when `1 << k <= O(log |G|)` and `k-d(G) >> 1` (under their standing `1 << log k << log |G|` regime).

The previous R19 construction, for a finite graph `G` with `N` vertices and a scale `L`, calls a simple cycle `C` of length at most `L` persistent if

`|Aut(G) . C| >= N/L`,

attaches 2-cells to all persistent cycles, and uses the universal cover of that 2-complex. The earlier report suggested the single predetermined choice `L_N = max(4,floor(log log N))`. The theorem below shows that this single small scale cannot support the entropic lower half of criterion C017 on the full Abelian source class.

## 2. An explicit source-valid adversarial sequence

For integer `n -> infinity`, set

`d_n = n^4`, `s_n=n`, `k_n=d_n+s_n`.

Let `m_n=ceil(e^n)` and choose a prime `p_n` with

`m_n <= p_n <= 2m_n`,

which exists by Bertrand's postulate. Put

`G_n = (Z/p_n Z)^{d_n}`, `N_n=|G_n|=p_n^{d_n}`.

Choose `k_n` independent uniform generators `Z_1,...,Z_k` and use the undirected random Cayley graph.

Then

- `log p_n = n+O(1)`;
- `log N_n = d_n log p_n = n^5+O(n^4)`;
- `log k_n ~ 4 log n`, hence `1 << log k_n << log N_n`;
- `d(G_n)=d_n` and `k_n-d(G_n)=s_n=n -> infinity`.

Thus this is inside the Hermon--Olesker-Taylor source regime.

## 3. Exact identification of the HOT entropic maximum on this family

For `G=(Z/pZ)^d`, multiplication by `gamma` is invertible whenever `p` does not divide `gamma`, hence `G/gamma G` is trivial and `t_gamma=0` in that case. If `p|gamma`, then `gamma G=0` and the target entropy is `log |G|=d log p`.

For every multiple `gamma` of `p`, the coordinatewise projection `Z_gamma -> Z_p` implies, by entropy monotonicity under deterministic maps,

`H(W_gamma(t)) >= H(W_p(t))`.

The same statement holds for `gamma=infinity` via `Z -> Z_p`. Consequently the time needed to reach the common target `d log p` is largest for `gamma=p`:

`boxed(t_* = t_p)`.

This is exactly the torsion-sensitive phenomenon a single small relator scale must survive.

## 4. With `L_n=floor(log log N_n)`, the persistent-relator cover is `Z^{k_n}` with high probability

Let

`L_n=max(4,floor(log log N_n))`.

Then `L_n=O(log n)` and, in particular, `L_n<p_n` for all large `n`.

Consider an undirected word of length at most `L_n` in the generators and inverses. Its exponent vector `a=(a_1,...,a_k) in Z^k` satisfies `||a||_1 <= L_n`. If `a != 0`, then because `L_n<p_n`, at least one coefficient is nonzero modulo `p_n`. Conditioning on all generators except one such coordinate shows

`P(sum_i a_i Z_i = 0 in G_n)=1/N_n`.

There are at most

`sum_{ell<=L_n}(2k_n)^ell <= (2k_n)^{L_n+1}`

such words. Hence

`P(exists a closed word of length <=L_n with nonzero exponent vector)`

`<= (2k_n)^{L_n+1}/N_n`.

Its logarithm is

`O((log n)^2) - (n^5+O(n^4)) -> -infinity`.

Therefore, with probability `1-o(1)`, every closed walk of length at most `L_n` has zero exponent vector.

The same event excludes zero generators and generator collisions, so the standard lattice map

`Phi: Z^{k_n} -> G_n`, `a |-> sum_i a_i Z_i`

is locally the expected Cayley covering. Every commutator square is a simple four-cycle and, because Cayley translations act freely and transitively on vertices, every such square is persistent. Once all commutator squares are filled, every zero-exponent word is null-homotopic in the standard cubical `Z^k` 2-complex. Since the event above says that no attached short cycle has a nonzero exponent vector, the extra persistent cells add no further deck relation. Thus the 1-skeleton of the selected universal cover is, with probability `1-o(1)`, precisely the standard lattice

`boxed(tilde G_{L_n} = Z^{k_n})`.

So the proposed single scale sees only the torsion-free HOT auxiliary process, even though the true source cutoff time is `t_p`.

## 5. The `Z^k` entropic time is parametrically earlier than `t_p`

Write `t_infinity` for the time at which the entropy of the rate-one walk on `Z^k` is `d log p`, and `t_p` for the analogous time on `Z_p^k`.

### 5.1 Elementary upper bound on `t_infinity`

Poisson thinning makes the `k` coordinates independent; at total time `t=ku`, each coordinate is a continuous-time simple random walk on `Z` run for time `u`.

Let `q_u` be its law. Shannon entropy dominates order-two Renyi entropy:

`H(q_u) >= -log sum_x q_u(x)^2`.

The collision probability is a return probability:

`sum_x q_u(x)^2 = P(X_{2u}=0)`.

Fourier inversion gives

`P(X_v=0) = (1/(2pi)) int_{-pi}^{pi} exp(-v(1-cos theta)) dtheta`.

Using `1-cos theta >= 2 theta^2/pi^2` for `|theta|<=pi` yields

`P(X_v=0) <= (1/2)*sqrt(pi/(2v))`.

At `u=p^2` this implies

`H(q_{p^2}) >= log p + c_0`

for an absolute `c_0>0`. Since the target entropy per coordinate is

`(d/k) log p < log p`,

we obtain the fully elementary bound

`boxed(t_infinity <= k p^2)`

for all sufficiently large `p`.

### 5.2 Lower bound on `t_p`

Let `q_u^{(p)}` be one coordinate of the rate-one walk on `Z_p` after coordinate-time `u=t/k`. At `t=t_p`,

`k H(q_u^{(p)}) = d log p = (k-s)log p`,

so

`k D(q_u^{(p)} || U_p) = s log p`.

The first Fourier coefficient is

`rho(u)=exp(-u lambda_p)`, `lambda_p=1-cos(2pi/p)`.

Since `|rho(u)| <= 2 TV(q_u^{(p)},U_p)` and Pinsker gives `D >= 2 TV^2`,

`D(q_u^{(p)}||U_p) >= (1/2) exp(-2u lambda_p)`.

Therefore

`s log p >= (k/2) exp(-2u lambda_p)`,

and hence

`u >= (1/(2lambda_p)) log(k/(2s log p))`.

Using `lambda_p <= 2pi^2/p^2`,

`boxed(t_p >= (k p^2/(4pi^2)) log(k/(2s log p)))`.

For the chosen sequence,

`k/(2s log p) ~ n^2/2`,

so

`t_p/(k p^2) -> infinity`.

Together with `t_infinity <= k p^2`, this proves

`boxed(t_p/t_infinity -> infinity)`.

## 6. Consequence: the single-small-scale version of C017 cannot certify the true cutoff

The selected lift at `L_n=floor(log log N_n)` is `Z^{k_n}` with high probability. Its entropy crosses `log N_n` at `t_infinity`, whereas Hermon--Olesker-Taylor's source cutoff is at `t_*=t_p`, and the ratio `t_p/t_infinity` diverges.

C017 requires a pre-cutoff time `t_n^-` with lift entropy at least a diverging amount *below* `log N_n`, and a post-cutoff time `t_n^+` with `t_n^+/t_n^- ->1`. Any pair capable of straddling the actual cutoff at `t_p` must have `t_n^-=(1-o(1))t_p`; but this is far beyond `t_infinity`, so the `Z^k` lift entropy is already above `log N_n`. Thus the C017 lower hypothesis fails even without asking for a diverging deficit.

This is a genuine obstruction to the **single predetermined small scale** in the previous report. It is not a counterexample to cutoff, to HOT, to ELE, or to Salez Problem 2.1.

## 7. Why this obstruction points to a better structural formulation

Method #17 reveals that the relevant numbers already exist in the source literature: HOT do not use one auxiliary quotient. They use the entire torsion hierarchy

`{Z_gamma^k : gamma in N union {infinity}}`

and take the maximum of the associated entropic times.

The persistent-relator construction has a graph-intrinsic analogue of this hierarchy: use the **whole nested family** of canonical covers

`{tilde G_L : 4 <= L <= floor(sqrt N)}`,

rather than choosing one small `L` in advance.

This remains safe on the random-regular anchor: if `Aut(G)` is trivial, then for every `L<=sqrt N`, a cycle orbit has size one while `N/L>=sqrt N>1`, so no cycle is persistent and every cover in the family is the ordinary universal graph cover.

On the adversarial Abelian sequence above, the family contains `L=p_n` because `p_n << sqrt(N_n)`. At this scale each generator orbit gives a simple `p_n`-cycle whose translation orbit has exactly `N_n/p_n`, meeting the persistence threshold `N_n/L` exactly. Thus the order-`p` relators become visible structurally.

Moreover, with high probability there is no *additional* exponent relation of `l1` length at most `p` except the deterministic `p e_i` relations. Indeed

`# {a in Z^k : ||a||_1 <= p} <= 2^k binom(p+k,k)`.

For `p=e^{n+O(1)}` and `k=n^4+n`, its logarithm is

`k(log p - log k + O(1)) = n^5 - 4 n^4 log n + O(n^4)`,

whereas `log N=n^5+O(n^4)`. After excluding the deterministic vectors `+-p e_i`, every remaining nonzero exponent vector closes with probability `1/N`, and the union bound tends to zero. Consequently the `L=p` persistent-relator cover has 1-skeleton

`boxed(Z_p^k)`

with high probability.

Thus, on this deliberately adversarial family, the same graph-intrinsic multiscale construction contains both relevant HOT auxiliary spaces:

- `L<<p` gives `Z^k` and entropic time `t_infinity`;
- `L=p` gives `Z_p^k` and entropic time `t_p=t_*`.

Taking the largest entropic time over the predeclared family of covers therefore selects the correct torsion scale **without inserting `p` or the group presentation by hand**.

This is a promising repair, not yet a nine-family theorem. The next substantive question is whether one can define the entropy target and post-entropic deck-collision condition uniformly over this canonical family, including nonuniform-stationary and non-Cayley models, without collapsing back to an existential reformulation of cutoff.

## 8. What this run does and does not establish

Established on the page:

1. a source-valid family in the HOT random-Abelian class for which the previous single choice `L=log log N` produces the `Z^k` cover with high probability;
2. on that family, `t_*=t_p` and `t_p/t_infinity -> infinity` by an explicit Fourier/Pinsker lower bound and an elementary Renyi-return upper bound;
3. therefore the single-small-scale C017 route cannot certify the source cutoff;
4. the **predeclared multiscale** persistent-relator family repairs this exact obstruction on the same sequence by containing a `Z_p^k` cover at scale `L=p` while preserving the universal-tree cover on asymmetric random regular graphs.

Not established:

- no new Salez family is added; the fixed `M_9` metric was already saturated at `9/9`;
- no source-level structural property covering all nine families is proved;
- no novelty claim is made for the entropy/Fourier ingredients, which are standard and directly motivated by HOT's `max_gamma t_gamma` construction;
- no closure or audit claim is made.
