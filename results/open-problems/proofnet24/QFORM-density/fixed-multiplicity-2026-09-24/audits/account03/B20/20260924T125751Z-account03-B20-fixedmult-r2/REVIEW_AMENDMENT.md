# account03/B20 release-gate amendment — fixed multiplicity

Run: `20260924T125751Z-account03-B20-fixedmult-r2`

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, declared SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Corrected release verdict

My earlier B20 review called the pinned 17-eigenvalue manuscript a mathematical PASS. That verdict was too strong for the literal pinned text. A genuinely separate account01/B18 review identified a real but repairable gap in the singular-ambient limiting paragraph of `lem:schur`: the baseline regularizes by `A+epsilon I`, applies the invertible estimate at the moving threshold `t-|epsilon|`, and then invokes continuity. Continuity alone does not justify that moving-threshold passage.

I independently checked the issue and the proposed fixed-threshold repair. The correct status is therefore:

- **literal pinned manuscript:** `GAP (repairable)`, not `PASS` and not `FALSE`;
- **mathematical 17-eigenvalue theorem after the fixed-threshold Schur repair:** `PASS in this account03/B20 reconstruction`; no other fatal defect found in the prior complete B20 end-to-end audit;
- **release status:** not yet release-ready as an exact-source independently validated manuscript, because the canonical `manuscript.tex` blob remains the unpatched baseline and the advertised reproducibility bundle is still absent at the stated root;
- **unrestricted three-eigenvalue conjecture:** open / not proved / not disproved by this manuscript.

This amendment supersedes the earlier account03/B20 claim of PASS for the literal baseline source.

## Independent verification of the Schur repair

Write

\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix},\qquad B\text{ invertible},\qquad S=D-C^TB^{-1}C.
\]

The desired statement is

\[
N_S(t)\ge N_A(t)-k\qquad(t>0),
\]

where `k=dim B` and `N_T(t)` counts eigenvalues of a symmetric matrix whose absolute value is at least `t`.

The invertible-ambient proof in the manuscript is valid: `S^{-1}` is the complementary principal compression of `A^{-1}`; applying principal-compression interlacing separately to `A^{-1}` and `-A^{-1}` gives the absolute-value count.

For singular `A`, fix an arbitrary `delta in (0,t)`. Choose `epsilon_m -> 0` avoiding the finitely many forbidden values for which `A+epsilon_m I` is singular, and with `|epsilon_m|<delta/2`. For all large `m`, `B+epsilon_m I` is also invertible. Set

\[
A_m=A+\epsilon_m I,
\qquad
S_m=D+\epsilon_m I-C^T(B+\epsilon_m I)^{-1}C.
\]

Then `S_m -> S` in operator norm. Every eigenvalue `lambda` of `A` with `|lambda|>=t` gives an eigenvalue `lambda+epsilon_m` of `A_m` satisfying

\[
|\lambda+\epsilon_m|\ge t-|\epsilon_m|>t-\delta,
\]

so

\[
N_{A_m}(t-\delta)\ge N_A(t).
\]

Apply the invertible-ambient result at the **fixed** threshold `t-delta`:

\[
N_{S_m}(t-\delta)
\ge N_{A_m}(t-\delta)-k
\ge N_A(t)-k.
\]

Because the set `{x: |x|>=t-delta}` is closed and ordered eigenvalues vary continuously under operator-norm convergence, passing `m->infinity` gives

\[
N_S(t-\delta)\ge N_A(t)-k.
\]

Finally, in finite dimension `N_S(t-delta)` decreases to `N_S(t)` as `delta downarrow0`. Hence

\[
\boxed{N_S(t)\ge N_A(t)-k.}
\]

No constant or downstream hypothesis changes. This repairs every invocation of `lem:schur` in the pivot half-potential and main theorem.

## Independent-review accounting

The account01/B18 report is a genuinely separate end-to-end review and correctly classified the baseline as `GAP (repairable)` while supplying the fixed-threshold repair. This account03/B20 run independently verifies that repair and amends its own earlier full-manuscript review accordingly. Thus the *mathematical chain with the repair inserted* has two separate review chains supporting it, but the exact canonical source should **not** be labelled independently validated until a patched source is committed and the release reviews identify that exact new blob.

Several other workers independently reported PASS on the unpatched baseline, but they did not catch the moving-threshold issue. They are useful corroboration for the remaining lines, not a reason to erase the source-level gap.

## Package status

At the fresh root inspection used in this run, the manuscript directory exposes `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`; the README-advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are not present at that root. This is a release/reproducibility gap, not a mathematical dependency gap.

## Continuity

The repaired theorem establishes an essentially bounded density globally. The no-pivot branch, where the characteristic function is integrable, gives a continuous density. The pivot branches are measure-domination arguments and do not establish global continuity for arbitrary rough input densities.
