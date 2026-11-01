Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0220 — Plancherel hitting-time representation and all-coordinate Bessel marginals

Status: **OPEN / PARTIAL**. This artifact proves a source-relevant structural representation and an exact all-coordinate marginal formula. It does **not** yet claim source-level closure, novelty, or independent audit.

## 1. Source target and historical input

David Aldous's living problem page, *A one-dimensional drift-jump particle process* (posted February 2018), asks for a fairly explicit description of the unique stationary law of the consistent process

`0 < X_1 < X_2 < ...`

with linear drift `dX_i/dt=X_i` and the nearest-particle-to-the-right Poisson fallback rule:

`https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html`.

The key historical input is equation (42) in Aldous--Diaconis's unfinished 1993 notes, Section 4.1:

`(X_1(∞),...,X_k(∞)) =_d (Gamma(B(1)),...,Gamma(B(k)))`,

where `B(i)` are stabilized patience-sorting pile-top labels and `Gamma(j)` is the j-th point of a rate-one Poisson process independent of the `B(i)`. Section 4.2 obtains a scalar-series formula for `k=2` and records

`P(B(2)=b)=1/[b(b-2)!]`, `b>=2`.

The purpose here is to translate this representation into Plancherel growth and then exploit classical determinantal LIS machinery.

---

## 2. Method B2 — obstruction search first

A natural but too-simple possibility is that the discrete first-row hitting sequence behind the stationary particles is Markov in the particle index. The historical notes themselves say the analogous statement for `(X_i)` appears false. Before using Plancherel growth as a solution mechanism, we checked whether its first-row hitting sequence loses essential hidden shape information.

Let `(Lambda_n)_{n>=0}` be Plancherel growth, and put

`T_j = inf{n : (Lambda_n)_1 >= j}`.

The standard transition from `lambda |- n` to `mu |- n+1`, with `mu/lambda` one box, is

`p(lambda,mu)=f^mu / ((n+1) f^lambda)`,

where `f^lambda` is the number of standard Young tableaux of shape `lambda`.

An exact rational dynamic program through size 6 gives

`P(T_4=6 | T_3=5, T_2=2) = 19/66`,

whereas

`P(T_4=6 | T_3=5, T_2=4) = 5/18`.

Since `19/66 != 5/18`, the sequence `(T_j)` is not Markov in `j`. Thus any attempted source solution that compresses the stationary law to a one-dimensional transition depending only on the latest first-row hitting time discards genuine information. The exact certificate is implemented in

`research7_2026-09-17/R7-04/code/2026-09-19T005000Z__P0220_exact_checks.py`.

This negative result is useful because it identifies the correct state category: the **whole Young-diagram growth state**, not the last hitting time alone.

---

## 3. Method B18 — translate patience pile tops into Plancherel first-row hitting times

### Proposition 3.1 — pile tops are the first row of the RSK insertion tableau

Let `sigma=(sigma_1,...,sigma_n)` be a permutation, and run patience sorting with the usual rule: place each incoming card `x` on the leftmost pile whose current top exceeds `x`, or start a new pile if no such pile exists. Let

`B(n,1)<B(n,2)<...`

be the pile-top labels after all cards are processed, with `B(n,j)=infinity` if pile `j` does not exist.

Let `P(sigma)` be the Robinson--Schensted insertion tableau under ordinary row insertion. Then, for every existing pile,

`B(n,j)=P(sigma)(1,j)`.

#### Proof

Induct over processed cards. Initially both first row and pile-top list are empty. Suppose they agree before inserting a card `x`.

In row insertion, `x` replaces the leftmost first-row entry strictly larger than `x`; that displaced entry is bumped into the second row. If no first-row entry is larger, `x` is appended at the right edge.

Patience sorting performs exactly the same update to the vector of pile tops: `x` becomes the top of the leftmost pile whose previous top is larger than `x`, or creates a new rightmost pile. Lower cards in each pile do not affect the pile-top vector, just as bumped entries do not affect the new first row.

Thus equality of the two vectors is preserved after each insertion. QED.

### Proposition 3.2 — stabilized pile-top labels have the Plancherel first-row hitting-time law

Let `B(j)` be Aldous--Diaconis's stabilized limit of `B(n,j)` for a uniform random permutation. Let `(Lambda_n)` be the standard Plancherel growth chain, and define

`T_j=inf{n : (Lambda_n)_1 >= j}`.

Then, jointly for every fixed `k`,

`(B(1),...,B(k)) =_d (T_1,...,T_k)`.

#### Proof

For a uniform permutation `sigma in S_n`, RSK is a bijection

`sigma <-> (P,Q)`

between permutations and pairs of standard Young tableaux of the same shape. For a fixed standard tableau `T` of size `n` and shape `lambda`, the number of permutations with `P=T` is `f^lambda`, namely one choice for each possible recording tableau `Q` of shape `lambda`. Therefore

`P(P=T)=f^lambda/n!`.

By the same argument,

`P(Q=T)=f^lambda/n!`.

Hence `P` and `Q` have the same marginal law as random standard tableaux.

By Proposition 3.1, `B(n,j)=P(1,j)`. On the other hand, when the recording tableau `Q` is revealed in increasing label order, its shape evolves by Plancherel growth, and `Q(1,j)` is exactly the first discrete time at which the first row acquires its `j`-th box. Thus

`(P(1,1),...,P(1,k)) =_d (Q(1,1),...,Q(1,k)) =_d (T_1,...,T_k)`

whenever the relevant entries occur by size `n`. Passing to the stabilized finite-dimensional distribution in Aldous--Diaconis equation (41) yields the stated joint identity. QED.

### Proposition 3.3 — stationary drift-jump particles are Plancherel first-row hitting times in continuous time

Let `N_x` be a rate-one Poisson process, independent of the discrete Plancherel growth chain, and define the poissonized growth process

`Lambda(x)=Lambda_{N_x}`.

Put

`tau_j=inf{x>=0 : Lambda_1(x)>=j}`.

Then for every fixed `k`, under the stationary drift-jump law,

`(X_1,...,X_k) =_d (tau_1,...,tau_k)`.

#### Proof

Aldous--Diaconis equation (42) gives

`(X_1,...,X_k)=_d(Gamma(B(1)),...,Gamma(B(k)))`

with `Gamma(m)` the m-th event time of an independent rate-one Poisson process. Proposition 3.2 replaces the vector `B` in law by the Plancherel hitting vector `T`. Since

`Gamma(T_j)=inf{x:N_x>=T_j}=inf{x:Lambda_1(x)>=j}=tau_j`,

the result follows jointly. QED.

This is the main category change: the stationary particle vector is the **top-row hitting-time vector of rate-one poissonized Plancherel growth**.

---

## 4. Method B25 — exact determinant formula for every stationary one-particle marginal

Let `L_n` be the length of the longest increasing subsequence of a uniform permutation of `n` letters. For `m>=0`, let `u_m(n)` be the number of permutations in `S_n` with `L_n<=m`.

### Lemma 4.1 — exact tail of the discrete pile label

For every `k>=1` and integer `n>=0`,

`P(B(k)>n)=P(L_n<k)=u_{k-1}(n)/n!`.

#### Proof

For a uniform permutation of `n` letters, `B(n,k)=infinity` exactly when patience sorting creates fewer than `k` piles. The number of piles equals the LIS length. Therefore

`P(B(n,k)=infinity)=P(L_n<k)`.

The stabilized variable `B(k)` has `B(k)<=n` exactly on the union of its stable atoms with values at most `n`; those are precisely the cases in which the `k`-th pile exists in the `n`-letter restriction. Hence

`P(B(k)>n)=P(B(n,k)=infinity)=P(L_n<k)`.

QED.

An immediate difference formula is

`P(B(k)=b)=P(L_{b-1}<k)-P(L_b<k)`.

For `k=2`, only the decreasing permutation has LIS `<2`, so `P(L_n<2)=1/n!`. Hence

`P(B(2)=b)=1/(b-1)!-1/b!=1/[b(b-2)!]`,

which exactly reproduces Aldous--Diaconis equation (45).

### Theorem 4.2 — all-coordinate Bessel/Toeplitz survival formula

For every `k>=1` and `x>=0`, the stationary coordinate `X_k` satisfies

`P(X_k>x) = exp(-x) det[ I_{i-j}(2 sqrt(x)) ]_{i,j=1}^{k-1}`,

where `I_r` is the modified Bessel function of the first kind, `I_{-r}=I_r`, and the determinant for `k=1` is the empty determinant `1`.

Equivalently, if

`D_m(y)=det[I_{i-j}(2y)]_{i,j=1}^m`,

then

`P(X_k>x)=e^{-x} D_{k-1}(sqrt(x))`.

#### Proof

Let `N_x` be the rate-one Poisson count by time `x`, independent of `B(k)`. Since `X_k=Gamma(B(k))` in law,

`{X_k>x}={N_x<B(k)}`.

Conditioning on `N_x=n` and using Lemma 4.1,

`P(X_k>x)`
`= sum_{n>=0} e^{-x} x^n/n! * P(B(k)>n)`
`= e^{-x} sum_{n>=0} u_{k-1}(n) x^n/(n!)^2`.

Gessel's Bessel-determinant identity states, for each `m>=1`,

`sum_{n>=0} u_m(n) y^(2n)/(n!)^2 = det[I_{i-j}(2y)]_{i,j=1}^m`.

Set `m=k-1` and `y=sqrt(x)`. For `k=1`, `B(1)=1` and `X_1=Gamma(1)` is exponential(1), matching the empty determinant convention. QED.

### Checks at low k

For `k=1`:

`P(X_1>x)=e^{-x}`.

For `k=2`:

`P(X_2>x)=e^{-x} I_0(2 sqrt(x))`.

This also follows directly from the source's `k=2` formula because

`P(B(2)>n)=1/n!`

and hence

`P(X_2>x)=e^{-x} sum_{n>=0} x^n/(n!)^2`.

For `k=3`:

`P(X_3>x)=e^{-x}[ I_0(2 sqrt(x))^2-I_1(2 sqrt(x))^2 ]`.

The accompanying exact checker expands the determinant generating functions and compares their rational coefficients against exhaustive LIS counts for determinant sizes `m=1,2,3` and `n=0,...,7`; all identities pass exactly.

---

## 5. Full joint law as a Schur-process gap law

The marginal theorem moves the frozen metric all the way to infinity, but Aldous's source asks for the **joint stationary distribution**. The Plancherel translation gives a clean exact form for that stronger object as well.

### Proposition 5.1 — explicit finite-dimensional distribution of poissonized Plancherel growth

Let

`0=t_0<t_1<...<t_r`,

and let

`empty=lambda^(0) subset lambda^(1) subset ... subset lambda^(r)`

be Young diagrams. Write

`n_j=|lambda^(j)|`, `d_j=n_j-n_(j-1)`, and let `f^(mu/lambda)` denote the number of standard Young tableaux of skew shape `mu/lambda`.

Then the rate-one poissonized Plancherel growth process satisfies

`P(Lambda(t_j)=lambda^(j), j=1,...,r)`

`= exp(-t_r) * [ f^(lambda^(r))/n_r! ]`

`  * product_{j=1}^r [ f^(lambda^(j)/lambda^(j-1)) (t_j-t_(j-1))^(d_j) / d_j! ].`

#### Proof

The discrete Plancherel transition is

`p(lambda,mu)=f^mu/((n+1)f^lambda)`

for one-box extensions `mu/lambda`. For a fixed skew-growth path from `lambda` of size `n` to `mu` of size `m`, multiplying one-box transition probabilities telescopes to

`[f^mu/f^lambda] [n!/m!]`.

There are `f^(mu/lambda)` such paths. Thus the `m-n` step transition probability is

`f^(mu/lambda) [f^mu/f^lambda] [n!/m!]`.

Apply this successively to the nested diagrams and multiply by the independent Poisson increment probabilities

`exp(-(t_j-t_(j-1))) (t_j-t_(j-1))^(d_j)/d_j!`.

All intermediate `f^lambda` and size-factorials telescope, leaving exactly the displayed formula. QED.

Using the Plancherel specialization `rho_t`, for which

`s_(mu/lambda)(rho_t)=f^(mu/lambda) t^(|mu|-|lambda|)/( |mu|-|lambda| )!`,

the same formula is

`exp(-t_r) s_(lambda^1)(rho_(t_1))`
`* product_{j=2}^r s_(lambda^j/lambda^(j-1))(rho_(t_j-t_(j-1)))`
`* s_(lambda^r)(rho_1)`.

Therefore the multi-time process is a Schur process.

### Corollary 5.2 — exact joint survival law

For arbitrary positive integers `k_1,...,k_r` and ordered times `0<t_1<...<t_r`,

`P(X_(k_j)>t_j for all j)`

`= P(Lambda_1(t_j)<k_j for all j)`

`= exp(-t_r) sum_{nested lambda^0,...,lambda^r; lambda^j_1<k_j}`

`    [ f^(lambda^r)/|lambda^r|! ]`

`    * product_{j=1}^r [ f^(lambda^j/lambda^(j-1)) (Delta t_j)^(d_j)/d_j! ].`

This follows immediately from Proposition 3.3 and Proposition 5.1. These joint survival probabilities determine every finite-dimensional stationary distribution.

### Corollary 5.3 — determinantal/Fredholm upgrade available from established Schur-process theory

Encode a partition by particles

`z_i=lambda_i-i`.

Then `lambda_1(t)<k` is equivalent to the absence of particles at time `t` in the integer half-line

`{k-1,k,k+1,...}`.

Nica (2017) identifies the relevant poissonized Robinson--Schensted trajectory as a Schur process; Okounkov--Reshetikhin (JAMS 2003) prove that Schur-process correlation functions are determinantal with an explicit contour-integral kernel. Therefore the multi-time event above is a Fredholm gap determinant of the corresponding specialized extended Plancherel/Schur kernel on the union of those time-slice half-lines.

This is the most promising route to a genuinely compact full stationary law. **However, this run does not yet specialize and write the extended kernel itself in source notation.** For that reason, and because the literature reconciliation could mean the source is already implicitly known once this identification is made, this artifact does not promote P0220 to PROVED or KNOWN.

---

## 6. Exact finite checks executed after the derivation

The checker

`research7_2026-09-17/R7-04/code/2026-09-19T005000Z__P0220_exact_checks.py`

uses exact rational arithmetic and performs three independent finite checks:

1. the source formula `P(B_2=b)=1/[b(b-2)!]` telescopes to `P(B_2>n)=1/n!` for `n=1,...,9`;
2. for `m=1,2,3`, the formal Bessel-Toeplitz determinant coefficients through `n=7` exactly equal exhaustive permutation counts `u_m(n)/(n!)^2`;
3. the Plancherel-growth hitting-time non-Markov obstruction is verified exactly, yielding `19/66` versus `5/18`.

Executed output:

`K2_SOURCE_TAIL_CHECK_PASS n=1..9`

`GESSEL_COEFFICIENT_CHECK_PASS m=1,2,3 n=0..7`

`PLANCHEREL_HITTING_NONMARKOV_PASS P(T4=6|T3=5,T2=2)=19/66 P(T4=6|T3=5,T2=4)=5/18`

`ALL_EXACT_CHECKS_PASS`

These checks validate finite consequences only; they are not substitutes for the written proofs above.

---

## 7. Metric movement and remaining gap

Frozen metric:

`K_Bessel := sup { k>=1 : a finite Toeplitz/Bessel determinant formula for P(X_k>x), all x>=0, has been rigorously derived and source-matched }`.

Before this run: `K_Bessel=1`.

After Theorem 4.2: **`K_Bessel=infinity`**.

This is genuine movement of the frozen mathematical metric. It does **not** itself close the source, because one-coordinate marginals do not determine the stationary dependence structure.

The full source-level gap is now sharply reduced to one literature-specialization task:

> Write the specialized multi-time Schur/extended-Bessel correlation kernel for the pure Plancherel growth process in the present time normalization, prove that its Fredholm half-line gap probabilities equal the joint survival probabilities of `(X_1,...,X_k)`, and determine whether that exact representation is already present in the pre-2018 literature under another name.

The positive nested-partition formula in Corollary 5.2 already describes the complete law exactly, but whether it meets Aldous's intended threshold of “fairly explicit” is a source-interpretation question. The Fredholm form is the stronger endpoint to pursue.

## 8. Dated source/prior-art status, 2026-09-19

- Aldous's current problem page still displays P0220's source question as open.
- Aldous--Diaconis 1993 notes contain equation (42), the balance equation, and the `k=2` scalar series; these are treated as prior art.
- Baik--Deift--Johansson 1999 explicitly cite Gessel's determinantal formula for the Poissonized LIS distribution; Theorem 4.2 is therefore primarily a **source-connection/application theorem**, not a claim that the Bessel determinant itself is new.
- Okounkov--Reshetikhin 2003 prove determinantal correlation functions for Schur processes.
- Borodin--Olshanski's Plancherel dynamics work computes dynamical correlation functions for closely related partition processes.
- Nica 2017 identifies the poissonized RS trajectory as a Schur process with poissonized Plancherel fixed-time marginals.
- A bounded exact-title/current-source search did not locate a paper explicitly declaring Aldous's 2018 drift-jump stationary-law problem solved. That absence is not used as proof of novelty or openness.

## 9. Next attack

Because the metric moved, target-specific unchanged stagnation remains `0`. The next ordinary research run should use a nonrepeating triple centered on the remaining joint-law problem, for example:

- **B1:** change category fully from drift-jump particles to a determinantal space-time gap process and specialize the Schur kernel;
- **B7:** derive the multi-time kernel by a semigroup/Doob-transform route from Plancherel growth, independently of the Schur-process citation;
- **B21:** import the extended-kernel/gap-probability technology from integrable probability and compare exact normalizations against `k=1,2`.

No source-level PROVED/KNOWN claim is made in this artifact.