Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — immutable erratum to the three-matching entropy artifact

This corrects one transcription/escaping error in the immutable artifact

`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T210600Z__F0003_three_matching_entropy_and_coloring_deformation.md`

at creation commit `54a78ed7afd625b5f10b7d8de983342ed6423e63`.

In display (2.8), two instances of `\frac` were corrupted during UTF-8/JSON transmission and read back as `rac`. The correct display is

\[
\boxed{
\log\mathcal N(y,z)
=
\frac n2\log n
-\frac n2
-\frac n2 H(\beta)
+O(k^2\log(n+1)).
}
\tag{E.1}
\]

The derivation is direct. From

\[
\mathcal N(y,z)=\prod_{a<b}N_{ab}!\prod_a(N_{aa}-1)!!,
\]

with `N_{ab}=N_{ba}`, Stirling gives

\[
\log\mathcal N(y,z)
=
\frac12\sum_{a,b}N_{ab}\log N_{ab}-\frac n2+O(k^2\log(n+1)).
\]

Since `N_{ab}=n\beta_{ab}` and `\sum_{a,b}\beta_{ab}=1`, this is exactly (E.1). Therefore the subsequent probability formula

\[
\Pr(P_My=z)
=
\exp\left\{-\frac n2H(\beta)+O(k^2\log(n+1))\right\}
\]

and the mutual-information reformulation in the original artifact are unchanged and were already written with the correct factors.

This erratum changes no mathematical conclusion, metric, method outcome, or stagnation accounting. The original artifact remains immutable.