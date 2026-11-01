# PROB20-20 — immutable correction to the 2026-09-17T20-40-46Z adaptive-baseline report

This note corrects one hypothesis in Theorem 7.1 of

`runs/2026-09-17/2026-09-17T20-40-46Z__report.md`

created at commit `b65fcf4d6c80c79260de7c5457318ce041bb196e`.

The mathematical transfer argument is valid, but equation (7.3) in the immutable report was stated slightly too weakly. Merely assuming

\[
\mathbb P(P_l\le C_{n_l}<2P_l)\to1
\]

does not by itself guarantee that subtracting an `o(n)` deterministic baseline leaves the excess mass above `P_l`; the source mass could in principle sit only `o(n)` above `P_l`.

## Correct phase hypothesis

Replace (7.3) by the following margin-compatible version. There must exist deterministic `a_l>0` with `a_l->0` such that

\[
\mathbb P\left(
 P_l+a_ln_l\le C_{n_l}<2P_l-a_ln_l
\right)\to1
\tag{C.1}
\]

and

\[
\sqrt{H_l}=o(a_l).
\tag{C.2}
\]

Then the proved baseline bound

\[
B_{n_l}/n_l\le4\sqrt{H_l}
\]

implies

\[
\mathbb P(P_l\le E_{n_l}<2P_l)\to1,
\]

which is exactly what Step 5 needs. Every subsequent estimate, in particular

\[
F_{n_l,j_l}/\lambda_{n_l,j_l}
\le (\delta+o(1))H_l\to0,
\]

is unchanged.

## Why the explicit fixed law in Section 9 still satisfies the corrected theorem

Lemma 8.1 should be read with a chosen deterministic margin. For the `l`-th selected root, first fix (for example)

\[
a_l:=\frac{\delta}{8l}.
\]

Convergence `C_n/n ->_p delta` provides `N_l` so that for every `n>=N_l`, the deviation from `delta` is smaller than `a_l` with probability at least `1-1/l`. Because the explicit law has infinitely many roots `j_k` and the Section 9 estimate gives

\[
H_{R_n,j_k}\to0
\]

uniformly for every source-valid `R_n->infinity` with `R_n<=j_k/2+O(1)`, choose the next root far enough that simultaneously

1. its phase index `n_l` is at least `N_l`, and
2. `4\sqrt{H_l}<a_l`.

Place `P_l/n_l` below `delta` by a margin of, say, `3a_l`; then on the source good event `C_{n_l}` lies at least `2a_ln_l` above `P_l` and remains far below `2P_l`. Subtracting the baseline still leaves `E_{n_l}>=P_l`.

Thus the explicit root/defender law, the exact inverse-fiber estimate, the subsequential one-box conclusion, and its ceiling value

\[
b(w,\lambda)=\lambda-\nu
\]

all remain valid. What changes is only the general theorem's phase-pair hypothesis.

## Status impact

- unrestricted Janson Problem 18.39: still **PARTIAL / OPEN**;
- frozen unrestricted metric: still **UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED, no movement**;
- unchanged count: still `1 -> 2`;
- no closure claim;
- no source, literature, or scheduler statement changes.
