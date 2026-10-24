Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level — not GPT-6 at maximum.

# R11 idea-before-code — growing-degree power-permutation route

Target: I0054 / Aldous--Janson Open Problem 18. This note is written before any checker for the present run.

Methods selected after the preceding #3/#14/#25 run: **#6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

## New route

The preceding inversive classes use rational functions with distinct poles to prevent Fourier degeneracy on every fixed visible dimension. Try the opposite algebraic category: polynomial permutations.

For an odd prime degree `d` and a prime `p = 2 (mod d)`, the monomial

`phi_{p,d}(x)=x^d`

permutes `F_p` because `gcd(d,p-1)=1`. For distinct offsets `a_1,...,a_m`, a Fourier mode of the translation orbit has phase

`P_h(t)=sum_j h_j (t+a_j)^d`.

If `d >= m`, constancy of `P_h` forces the first `m` moment equations

`sum_j h_j a_j^r=0,  r=0,...,m-1`,

and the Vandermonde matrix is invertible. Hence every nonzero Fourier mode is a nonconstant polynomial of degree at most `d`, so the Weil bound plus Erdos--Turan--Koksma should give

`D_m = O_m(d p^{-1/2} (log p)^m)`.

This is enough for the same threshold/translation split-rate calculation as in C070/C071.

## Why fixed degree is the wrong deformation

The Fourier criterion has a sharp algebraic threshold. For `m=d+1` consecutive offsets `0,...,d`, the `d`th finite-difference coefficients

`h_j=(-1)^{d-j} binom(d,j)`

satisfy

`sum_{j=0}^d h_j (t+j)^d = d!`,

so the translation orbit has an exact nontrivial torus Fourier relation. Thus a fixed-degree polynomial route cannot give full-dimensional equidistribution for all fixed restrictions.

Deform the degree with `N`: let `d_N` be the least odd prime at least `max(3,ceil(log(N+2)))`, and let `p_N` be the least prime at least `max(N,d_N+1)` with `p_N = 2 (mod d_N)`. Dirichlet gives existence; Bertrand gives `d_N=O(log N)=O(log p_N)`. Then `d_N -> infinity`, and for every fixed `m`, eventually `d_N >= m`, while the discrepancy error is still `O_m(p_N^{-1/2}(log p_N)^{m+1})`.

## Candidate C072

For each active clade on labels in `[N]`, independently run proposal clocks indexed by `(u,t)` with

`1 <= u < p_N`, `t in F_{p_N}`,

at rate `1/(2u(p_N-u))`. At a ringing clock, color ambient label `ell` red iff the standard representative of `(t+ell)^{d_N}` is `<u`; split the current clade by red/blue if both colors occur. Forgetting edge times gives a finite rooted binary tree.

Expected proof obligations:

1. Pair separation / finite-tree validity from injectivity of `x^d`.
2. Exact strong lumpability of every finite visible restriction.
3. Fourier/Vandermonde discrepancy estimate for every fixed restriction once `d_N>=m`.
4. Specified split rates converge to `B(i,j)=(i-1)!(j-1)!/(i+j-1)!`.
5. Finite-state generator convergence implies whole-path convergence (indeed path-TV on bounded intervals), then the frozen projective CTCS(infinity) limit.
6. Find a finite labeled-generator invariant showing the class is not a relabeling/time-rescaling of the source and is not merely C071 in disguise.

If any of 2--5 fails, do not count the class.
