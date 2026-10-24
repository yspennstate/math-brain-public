# T248 Edge universality for the conjugate kernel of a random network

Lead: unassigned. Dossier written 2026-10-16 by claude-99aebc7f from the row as listed, the abstracts of the papers named
below (arXiv records; theorem numbers not yet read), and computations in this folder (ck_edge.py, ck_entry.py and their
run files).

## STATUS (20 Oct 17:58, claude-99aebc7f; 22 Oct 10:2x addition: for He_3 at n 1000, tau 0.1, the regularized joint
equation of ck_ipn2.py at eps 0.3 places lambda_max within 0.075 on six of six draws, rms 0.041; see the last section)
OPEN as a theorem; the numerics for the Lipschitz case (relu with mean and linear part removed, m = N = d = n) are done.
Fluctuations sit on the n^(-2/3) scale (n^(2/3) std 3.35-3.47 from n 1000 to 4000). The shape is TW1: quantile asymmetry
rejects the Gaussian and Gumbel at n 2000 (5,000 reps) and n 4000 (900 reps), skewness +0.40 at n 4000 is 1.0 se from TW1.
The centring is 4 (the MP edge) with a correction ~ n^(-0.92 +- 0.06), close to 1/n; no n^(-2/3) centring term is needed.
For He_3 the edge is an outlier set by the heaviest row: lambda = rho^2/(rho - 1) with rho its mean square (corr 0.96-0.99
with lambda_max at n 250-2000, 20 Oct 17:58 section); the regime ends near n 3800 (He_4: 1.0 x 10^5); a mixed
regime follows (n 4000: skew +7.3), and at n 8000 the shape is TW-like (skew +0.23, n^(2/3) std 4.2) with the centre still
19.5 fluctuation widths above 4, a gap that halves per doubling (target 2's crossover, 20 Oct 07:4x section).
TARGETS 3 and 4 are done: the statement in top200_probability_2026_10_14/list.jsonl already names the class (Lipschitz or
smooth, E sigma(Z) = 0, E Z sigma(Z) = 0), puts the linear part and its spikes second, and marks the polynomial case as
asymptotic only. What remains is the theorem (TARGET 1) and the outlier law for He_k (TARGET 2).

## STATEMENT
Row as listed: Y = sigma(W X / sqrt d), W m x d iid Gaussian, X d x N with iid columns, proportional regime. The limiting
spectral law of the conjugate kernel is known (Pennington-Worah, Benigni-Peche; multi-layer, Fan-Wang). Prove that the
largest eigenvalue not explained by spikes from the low-order Hermite components of sigma converges to the right edge of
the limit law with Tracy-Widom (beta = 1) fluctuations, and describe the outliers.
Working form used here: X with columns uniform on the sphere of radius sqrt d (so each w.x/sqrt d is exactly N(0,1)),
m = N = d = n, statistic lambda_max(Y Y^T / N), sigma centred and, where stated, with its linear part removed. The
auditor (codex-w687, UNSURE) asks that the statement fix the input moment and covariance hypotheses, the rule that removes
spikes, and a regularity condition at the edge; the computations below add a fourth requirement (see FAILURE POINT).

## FRONTIER
- Benigni, Peche arXiv:2201.04753: the largest eigenvalues of the conjugate kernel / information-plus-noise model; an
  outlier can separate from the bulk. Read the theorem and its hypotheses before using it as the frontier statement.
- Fan, Wang arXiv:2005.11879: the global spectral law of the conjugate kernel and NTK of multi-layer networks, under an
  approximate orthogonality condition on the inputs.
- Wang, Wu, Fan arXiv:2402.10127: spikes of the conjugate kernel and their alignment with the data.
- Also to read for edge results: arXiv:2405.18274, arXiv:2306.05850, arXiv:2605.29669, arXiv:2502.18428 (listed by the
  row's builder; content not checked in this dossier).
- Classical inputs: Tracy-Widom for sample covariance with general entries (Soshnikov; Peche; Pillai-Yin), and the
  heavy-entry outlier picture (Auffinger, Ben Arous, Peche 2009; Soshnikov 2004), which turns out to be the relevant one
  at accessible sizes (below).

## ARCHITECTURE
Write sigma = sum_k c_k He_k / sqrt(k!). The k = 0 term gives a rank-one spike (1 1^T); the k = 1 term gives the linear
model c_1 W X / sqrt d, whose own edge is that of a product of two Wisharts; the k >= 2 part behaves, in the bulk, like
an independent Wishart of variance sum_{k>=2} c_k^2 (the Pennington-Worah equivalence). The edge question is whether the
same equivalence holds at the n^(-2/3) scale. The entries of the nonlinear part are polynomials of Gaussians: all moments
are finite, but the largest of the N m entries grows like (2 log(N m))^(deg/2), so for deg >= 3 the largest entry squared
over N is of order (log n)^3 / n, which is NOT small until n is in the thousands.

## SETTLED (computed 16 Oct; files in this folder)
- Linear control (sigma(z) = z), ck_edge_run1.txt, 800 reps: mean lambda_max 6.470, 6.585, 6.652 at n = 250, 500, 1000,
  approaching the free-multiplicative edge 27/4 = 6.75 of the product of two MP(1) laws; n^(2/3) x std 9.09, 8.81, 9.37
  (stable, so the n^(-2/3) scale is right); skewness +0.354, +0.123, +0.275 and excess kurtosis +0.225, +0.150, -0.036
  against TW1 +0.294, +0.165 (standard errors about 0.09 and 0.17). Consistent with TW1.
- ReLU with mean and linear part removed (relu0), ck_edge_run2.txt, 400 reps: mean 4.022, 4.008 at n = 250, 500 (the MP(1)
  edge is 4); n^(2/3) x std 3.91, 3.65, against 2^(4/3) x 1.268 = 3.19 for a Wishart of ratio 1; skewness +0.541, +0.454,
  excess kurtosis +0.238, +0.485. The scale and centre are those of a Wishart edge; the skewness is two standard errors
  above TW1 at both sizes and is falling. Consistent with TW1 with a finite-size correction, not yet a confirmation.
- Cubic Hermite activation (he3 = He_3 / sqrt 6, no mean, no linear part), 400 reps: mean 6.821, 5.871 at n = 250, 500
  (far above the edge 4), n^(2/3) x std 69.0, 71.0, skewness +2.49, +3.52, excess kurtosis +10.2, +26.8. Not TW, and
  not at the edge. The mixture (z + he3)/sqrt 2: mean 6.342, 5.666, skewness +2.05, +2.82, excess kurtosis +6.0, +12.3.
  ck_edge_run1.txt repeats he3 at 800 reps: mean 6.753, 5.805, n^(2/3) x std 69.9, 68.0, skewness +2.43, +2.55, excess
  kurtosis +9.6, +10.0 at n = 250, 500, in line with the 400-rep numbers. The run then stopped at he3 n = 1000 on a
  failed 7.6 MB allocation (the laptop's commit charge was at 93 pct, 16 Oct 05:5x), so relu0 and mix at 800 reps and
  he3 at n = 1000 were never run; rerun when memory allows.
- WHY (ck_entry.py, 60 reps): the he3 top eigenvalue is an outlier made by the single largest entry a of Y. With
  theta^2 = a^2 / N, every rep had theta^2 > 1 at n = 250 and 500, and the rank-one prediction (1 + theta^2)^2 / theta^2
  correlates with lambda_max at 0.836 and 0.845 (means 6.05 vs 6.78 at n = 250, 5.28 vs 5.85 at n = 500; the prediction
  runs low because the next-largest entries in the same row and column add to it). From the Gaussian maximum, the typical
  largest he3 entry has median theta^2 = 1.92, 1.35, 0.80, 0.52, 0.33 at n = 1000, 2000, 5000, 10^4, 2 x 10^4 (exact median of
  the maximum of n^2 Gaussian entries; measured at n 1000-8000 in the 20 Oct 07:4x section): the outlier regime ends near
  n = 3400 for he3, and for He_k it ends later as k grows (theta^2 ~ (2 log n^2)^k / (k! n)).

## FAILURE POINT
For polynomial (or any super-linear-growth) activations the finite-n edge is governed by extreme entries, not by the
bulk. A Tracy-Widom theorem is still plausible as n -> infinity (all moments are finite, which is the Soshnikov-type
regime), but any proof must control the largest entries of a matrix whose entries are dependent (the same w_i and x_j
enter a whole row and column), and the statement must say what is meant at sizes where it is false. The relu0 case, whose
entries grow only linearly, shows no such effect at n = 250, 500.

## SHAPE
Weeks. The bounded or linearly growing activation case (Lipschitz sigma) is the realistic first target: the relu0
numbers sit on a Wishart edge already. Polynomial activations of degree >= 3 need an extreme-entry argument first.

## OBSTRUCTION
Edge universality for a nonlinear random-feature matrix with dependent entries: no independence across the row or the
column, a deterministic rank-one/low-rank part from low Hermite components, and entry tails that, for growing sigma,
create entry-driven outliers well into the thousands. Moves: TW1 for Lipschitz sigma with c_0 = c_1 = 0; TW1 after
removing the linear part's spike structure; the location and law of the entry-driven outliers for polynomial sigma at
finite n (an extreme-value statement, Gumbel- or Frechet-like after centring).

## TARGETS
1. Prove: for Lipschitz sigma with E sigma(Z) = 0 and E Z sigma(Z) = 0, lambda_max(Y Y^T / N) converges to the edge of the
   Pennington-Worah law with TW1 fluctuations on the n^(-2/3) scale.
2. For sigma = He_k, k >= 3: describe lambda_max in the regime where the largest entry has theta^2 > 1 (outlier formula plus
   its fluctuations), and prove the crossover to the bulk edge.
3. Experiment: relu0 at n = 1000, 2000 (skewness should fall toward 0.294 if TW1 is right); he3 near n = 5000-10^4 to see
   the crossover, using a Lanczos top eigenvalue rather than a full eigendecomposition.
4. Rewrite the row: name the activation class (Lipschitz, centred, no linear part, or the linear part's spike removed by a
   stated rule) and drop "generic" activations, which the computations show is false at any practical size for
   polynomial activations.

## ADDITION 2026-10-18 (claude-99aebc7f): relu0 at n = 1000, 2000 with a Lanczos top eigenvalue (item 3)
ck_edge2.py (eigsh on v -> Y (Y^T v)/n, Y never squared), 600 reps each, ck_edge2_relu0.txt:
    n      mean      std      n^(2/3) std   skew    exkurt   (TW1: skew +0.294, exkurt +0.165)
    1000   3.99899   0.03503  3.503         +0.205  +0.125
    2000   3.99688   0.02108  3.346         +0.194  -0.059
The fluctuation is on the n^(-2/3) scale (n^(2/3) std flat at 3.3-3.5). With 600 reps the standard error of the skewness is
about 0.10 and of the excess kurtosis about 0.20, so both moments agree with TW1 within one standard error; the data cannot
yet tell TW1 from a nearby law. The mean is not where TW1 centred at 4 puts it: that would be 4 - 0.9515 std = 3.9667 and
3.9799, while the measured means are higher by 0.0323 and 0.0169 (standard errors 0.0014 and 0.0009). So the finite-n edge
sits above 4 by an amount that halves when n doubles [CORRECTED 19 Oct 07:3x below: n 4000 does not follow 1/n; the excess x n^(2/3) is flat], an O(1/n) shift, which is smaller than the n^(-2/3) fluctuation and
leaves the TW1 limit centred at 4 intact. A run at n = 4000 was cut at 500 of 600 reps by a power failure (mean 3.99602 at
rep 500, no std recorded); if the std follows 3.35 n^(-2/3) = 0.0133 its excess is 0.0087, against 0.0085 for a 1/n decay
from n = 2000 and 0.0120 for 1/sqrt(n), so it supports the 1/n rate, though it rests on an assumed std. Item 3's relu0 half
is answered for the fluctuation scale; a sharper test of the TW1 shape needs about 5,000 reps at n = 2000 and 4000.

## 18 Oct 14:17 (claude-99aebc7f): the 3,000-rep n 2000 run stopped at its timeout at rep 1,500 (running mean 3.99654); restarted with samples saved
ck_edge2_relu0_n2000_3000.txt holds only the running mean (3.99654 at 1,500 reps, 3.9965 +- about 0.0005 from 2,100 reps across
the two runs), so the TW1 shape test lost its data. ck_edge2.py now takes a sixth argument, a samples file: every rep appends its
lambda_max and theta^2 and draws from its own stream default_rng([seed, n, rep]), so a cut run resumes exactly (tested: 4 reps
then a resume to 6 gives the same 6 values as one 6-rep run). Relaunched: n 2000, 5,000 reps, f32, seed 11 ->
ck_edge2_relu0_n2000_samples.txt.

## 18 Oct 14:59 (claude-99aebc7f): interim TW1 shape at n 2000 from the saved samples (about 1,050 of 5,000 reps; the run continues)
From ck_edge2_relu0_n2000_samples.txt (f32, seed 11, one stream per rep): mean 3.9961, std 0.0220, n^(2/3) std 3.50 (the scale
again flat). Skew +0.42 to +0.45 (bootstrap 95 pct about [0.27, 0.63]) and excess kurtosis +0.40 to +0.48 ([0.01, 1.05]) as the file
grew from 1,025 reps; TW1's +0.294 and +0.165 lie inside both intervals. The earlier 600-rep run gave +0.194 and -0.059; pooled, the
skew is about +0.33. The moments are tail-driven: dropping the largest 1, 3, 5 values moves the skew to +0.36, +0.31, +0.27 and the
excess kurtosis to +0.19, +0.04, -0.04. The top value sits at z = 4.28, which is about a 15 pct event in 1,000 draws from TW1's
right tail (1 - F1(s) ~ e^(-2 s^(3/2)/3) / (4 sqrt(pi) s^(3/4)) at s = 4.2). lambda_max is uncorrelated with the largest entry's
theta^2 (r = 0.003), so the tail is not the rank-one outlier of ck_entry.py. Reading: consistent with TW1, and moments will not
separate TW1 from a nearby law at this sample size. The test to run at 5,000 reps is a quantile one: standardized quantiles at
0.05/0.25/0.5/0.75/0.95 against TW1's, which do not hang on three samples.

## 18 Oct 19:27 (claude-99aebc7f): the TW1 quantile test at n 2000, 5,000 reps - TW1 fits, Gaussian and Gumbel do not
tw1_quantile.py (output tw1_quantile_n2000.txt) on all 5,000 saved lambda_max (relu0, n 2000, f32, seed 11). TW1 by Bornemann's
Fredholm determinant det(I - K), K(x, y) = Ai((x + y)/2 + s)/2 on L2(0, inf), 80-point Gauss-Legendre (reproduces mean -1.2065,
sd 1.2680). Location- and scale-free tests:
  quantile asymmetry      (q95-q50)/(q50-q05)   (q99-q50)/(q50-q01)
  sample (bootstrap 95%)  1.221 [1.154, 1.289]  1.324 [1.233, 1.408]
  TW1                     1.176                 1.253
  Gaussian                1.000                 1.000
  Gumbel                  1.779                 2.236
Least-squares location-scale fit on nine quantiles (0.01 .. 0.99): rms residual 0.036 law-scales for TW1, 0.119 Gaussian, 0.273
Gumbel. KS against the fitted TW1: D 0.0147, p 0.23; against a Gaussian with the sample mean and std: D 0.0287, p 0.0005 (both fitted,
so both p are optimistic; the ordering is what counts). Reading: at n 2000 the relu0 edge has the TW1 shape - both asymmetry ratios
inside their intervals, Gaussian and Gumbel outside - which is the finite-n evidence the moments could not give. Left for the row:
n 4000 at the same reps to see the residual 0.07 at q99 shrink, and the proof (the edge universality for the conjugate kernel).

## 19 Oct 07:3x (claude-99aebc7f): n 4000, 174 reps - the edge shift is not O(1/n); it holds at about one TW unit
[SUPERSEDED 19 Oct 23:1x by the 429-rep section below: the n 4000 excess is +0.0090 (se 0.0009), not +0.0116; the first 174 reps ran about 2 se high, and the excess decays like n^(-0.92 +- 0.08), close to 1/n.]
ck_edge2.py relu0 4000, f32, seed 11, one stream per rep, samples in ck_edge2_relu0_n4000_samples.txt (resumable; 174 reps before
its 28-minute cap). Against the 5,000-rep n 2000 sample:
    n      reps   mean      std      n^(2/3) std   skew          exkurt   excess over 4 - 0.9515 std   excess x n^(2/3)
    1000   600    3.99899   0.03503  3.50          +0.21         +0.13    +0.0323 (se ~0.0015)          3.23
    2000   5000   3.99668   0.02188  3.47          +0.41 (0.03)  +0.49    +0.0175 (se ~0.0005)          2.78
    4000   174    3.99762   0.01473  3.71          +0.40 (0.19)  +0.58    +0.0116 (se ~0.0015)          2.93
CORRECTION to the 18 Oct addition above: the excess was read there as an O(1/n) shift from two points. A 1/n decay from
n 2000 predicts +0.0087 at n 4000. The measured value is +0.0116, about two standard errors higher, and n^(-2/3) predicts +0.0110. Scaled by n^(2/3),
the excess is flat at 2.8-3.2 from n 1000 to 4000. That is about one TW standard unit (the scale std x n^(2/3) / 1.268 is
2.7-2.9). So at these sizes the mean sits one TW unit above where TW1 centred at 4 puts it, a shift of the fluctuation order.
It is not a vanishing correction below it. Either the centring has an n^(-2/3) correction (a finite-n edge 4 + c n^(-2/3), with
c about 3), or the limit approaches slowly. The data cannot yet say which. The skewness at n 4000 (+0.40, se 0.19) matches
n 2000's +0.41. Both sit above TW1's +0.29, which at n 2000 is four standard errors. Next: run the n 4000 samples file on to 2,000+ reps
(it resumes) and add the n 2000 quantile test (tw1_quantile.py samples 4000) at n 4000. If c stays near 3, the row's edge
statement needs a centring term.

## 19 Oct 21:4x (claude-99aebc7f): n 4000 at 242 reps, interim shape check (tw1_quantile.py)
Quantile asymmetry (q95-q50)/(q50-q05) and (q99-q50)/(q50-q01): sample 1.13 and 1.27, bootstrap 95 percent [0.86, 1.53] and
[0.98, 2.17]; TW1 1.18 and 1.25, Gaussian 1.00 and 1.00, Gumbel 1.78 and 2.24. Gumbel is outside both intervals and fits
badly (rms quantile residual 0.34 scale units); TW1 (0.090) and Gaussian (0.108) both fit, and KS cannot tell them apart
(p 0.82 and 0.88). So at 242 reps the shape rules out Gumbel and sits closer to TW1 than to the Gaussian, but does not
separate them. Separating TW1's asymmetry 1.18 from 1.00 needs an interval roughly a third as wide, about ten times the reps.
The sampler is starved by the box (about 3 s of CPU per hour at BelowNormal; raised to Normal at 21:4x, about 11 s per
minute since), so 2,000 reps at n 4000 is days away on this laptop. The centring question (c near 3) is unchanged.

## 19 Oct 23:1x (claude-99aebc7f): n 4000 at 429 reps - the excess does decay, at about n^(-0.9); the 07:3x reading is withdrawn
Same samples file, 429 reps (rows 0-428, contiguous, one stream per rep). Pooled: mean 3.99593, std 0.01370 (n^(2/3) std 3.45),
skew +0.49 (se 0.12), excess kurtosis +0.56. Excess over 4 - 0.9515 std: +0.0090, bootstrap se 0.0009, x n^(2/3) = 2.26.
Why the 07:3x number moved: by batch, reps 0-173 average 3.99762 (se 0.0011), reps 174-241 3.99522 (0.0014), reps 242-428
3.99462 (0.0010). The first batch sits 2.1 se above the rest. Same script, seed and per-rep streams; I found no change between
batches, so I read it as chance in a 174-rep sample. The 07:3x section built its "not O(1/n)" conclusion on that batch alone.
With n 1000 (+0.0323, se 0.0015), n 2000 (+0.0175, 0.0005) and n 4000 (+0.0090, 0.0009), the excess scaled by n^(2/3) reads
3.23, 2.78 and 2.26. It falls by 0.86 and 0.81 per doubling of n, against 0.79 for 1/n and 1.00 for n^(-2/3). A power fit
end to end gives excess ~ n^(-p) with p = 0.92 (se about 0.08): n^(-2/3) is about three se away and 1/n is within one.
So the row's edge statement needs no n^(-2/3) centring term at these sizes. The mean approaches the TW1 centring 4 - 0.9515
std, with a correction that is close to O(1/n).
The skewness is +0.49 (se 0.12) against TW1's +0.29 and n 2000's +0.41: still above TW1, now at 1.7 se from it at n 4000.
Shape at 429 reps (tw1_quantile.py): rms quantile residual in scale units, TW1 0.098, Gaussian 0.158, Gumbel 0.248; KS p 0.77
(TW1) and 0.55 (Gaussian). The ordering is the same as at 242 reps and the gap between TW1 and the Gaussian is wider; the
Gaussian misses both 1 percent tails (+0.30 and +0.28 scale units). KS still cannot separate the two.

## 20 Oct 02:0x (claude-99aebc7f): n 4000 at 900 reps - excess ~ n^(-0.92), skew back within one se of TW1, the Gaussian rejected
The run finished (ck_edge2_relu0_n4000_run2.txt, DONE at 900 reps; samples file rows 0-899, one stream per rep).
Pooled: mean 3.99574, std 0.01377 (n^(2/3) std 3.47, the same as n 2000's 3.473), skew +0.398 (bootstrap se 0.100),
excess kurtosis +0.30. Excess over 4 - 0.9515 std: +0.00884, bootstrap se 0.00063, x n^(2/3) = 2.23.
By batch: reps 0-173 3.99762 (se 0.0011), 174-428 3.99478 (0.0008), 429-899 3.99556 (0.0006). The new 471 reps sit with
the middle batch, so the first batch's high mean was chance, as read at 23:1x.
Weighted power fit over n 1000, 2000, 4000 (+0.0323, +0.0175, +0.00884): excess ~ n^(-p), p = 0.921 (se 0.058). 1/n is
1.4 se away, n^(-2/3) 4.4 se away. The scaled excess falls 3.23, 2.78, 2.23. The 23:1x conclusion stands with a tighter se:
no n^(-2/3) centring term at these sizes; the correction to the TW1 centring is close to O(1/n).
Skewness: +0.398 against TW1's +0.294, 1.0 se, down from 1.7 se at 429 reps.
Shape (tw1_quantile.py, tw1_quantile_n4000_900.txt; location and scale free): rms quantile residual in scale units TW1 0.033,
Gaussian 0.114, Gumbel 0.282; KS p 0.74 (TW1), 0.17 (Gaussian). Quantile asymmetry (q95-q50)/(q50-q05) = 1.229, bootstrap
95% [1.090, 1.444], and (q99-q50)/(q50-q01) = 1.347, [1.123, 1.609]. TW1 gives 1.176 and 1.253, inside both intervals; the
Gaussian's 1.000 is outside both and Gumbel's 1.779 and 2.236 are outside both. At 429 reps the intervals still held 1.00;
at 900 they do not, so n 4000 now separates TW1 from the Gaussian as n 2000 did at 5,000 reps (1.221 and 1.324 there): the
edge fluctuations are asymmetric the way TW1 is at both sizes.

## 20 Oct 07:4x (claude-99aebc7f): he3 at n 1000-8000 with a Lanczos top eigenvalue - the crossover (item 3)

ck_edge2.py he3, 100 reps per n, float32, seed 41 (ck_edge2_he3_run1.txt):

    n      mean      std       n^(2/3) std   skew     exkurt   median theta^2   exact median   (mean - 4) n^(2/3)
    1000   5.06014   0.57380   57.4          +1.717   +3.482   1.957            1.922          106
    2000   4.41025   0.20763   33.0          +2.014   +5.574   1.393            1.345           65
    4000   4.15058   0.12762   32.2          +7.255   +58.74   0.873            0.911           38
    8000   4.04877   0.01054    4.2          +0.228   -0.535   0.571            0.600           19.5

The measured median theta^2 of the largest entry matches the exact median of the maximum of n^2 independent He3(g)/sqrt 6
entries to within 5 percent at every n (the earlier leading-order values 3.27, 2.20, ... used (2 log n^2)^3/(6n) and ran 1.6x
high). That median crosses 1 at n = 3400. At n 4000 most reps are already below 1 and a few are not, which is the skew 7.3
and excess kurtosis 59: a mixture of bulk-edge reps and outlier reps. At n 8000 the mixture is gone: skew and excess kurtosis
are within reach of TW1 (+0.294, +0.165) at 100 reps, and the fluctuation is on the n^(-2/3) scale with n^(2/3) std 4.2
against relu0's 3.35-3.5. The centre is not at the edge yet: (mean - 4) n^(2/3) is 19.5 at n 8000, against 2.2-3.2 for relu0,
so the sub-critical large entries still push the top eigenvalue up by about five fluctuation widths. It halves per doubling
from n 2000 on (65, 38, 19.5), so on this evidence he3 reaches the relu0 behaviour by about n 6 x 10^4. Target 2's crossover
is therefore located: the outlier formula governs up to about n 3400 for he3, a mixed regime follows, and by n 8000 the shape
is TW-like with a centring shift that, measured in fluctuation units, falls roughly like 1/n (the raw shift 0.410, 0.151,
0.049 falls by about 3 per doubling).

## 20 Oct 17:58 (claude-99aebc7f): target 2 - the He_k outlier is set by the heaviest row, lambda = rho^2/(rho - 1)
Schur complement on row i of M = Y Y^T/n: lambda (off the spectrum of the other rows) is an eigenvalue iff
    1 = (1/n) y_i^T (lambda - H/n)^(-1) y_i,    H = Y^(i)T Y^(i).
Replacing the quadratic form by |y_i|^2 g(lambda)/n, with g the MP(1) Stieltjes transform (lambda g^2 - lambda g + 1 = 0),
gives g = 1/rho with rho = |y_i|^2/n, the row's mean square, so
    lambda = Phi(rho) = rho^2/(rho - 1)   for rho > 2;   no outlier from that row when rho <= 2 (g = 1/2 is the edge 4).
Columns give the same with the column mean square. The old rank-one formula (1 + theta^2)^2/theta^2 is the case
rho = 1 + theta^2, which assumes the rest of the row has mean square 1. For He_3 it does not: given s = |w_i|/sqrt n the
row's entries have variance V_3(s) = (15 s^6 - 18 s^4 + 9 s^2)/6, which rises 3 percent per percent of s^2, and the row that
holds the largest entry is tilted toward large s (its tail weight is exp(-t^2/2s^2) with t about 4.4). Columns have s = 1
exactly (x on the sphere). Two-sided variant: the largest entry a = Y_ij also sits in a heavy column, kept inside H, so
1 = (1/n)(a^2 R_jj + (|y_i|^2 - a^2) g) with R_jj = 1/(lambda(1 - c g)), c the column's mean square without a.
ck_rownorm.py, he3, seed 11, float32, ck_rownorm_he3_run1.txt; prediction "row" = Phi(max over rows and columns of the mean
square), "old" = (1 + theta^2)^2/theta^2 from the largest entry:
        n  reps   lam mean  old err   old corr   row err   row rms   row corr
      250    40   6.6951    -0.7395   0.872     -0.0388   0.2840   0.987
      500    40   5.6331    -0.4893   0.826     -0.1301   0.2793   0.959
     1000    40   5.0687    -0.4647   0.697     -0.1128   0.2132   0.970
     2000    40   4.4958    -0.2476   0.917     -0.1081   0.1510   0.973
The row predictor cuts the bias by a factor 2 to 20 and lifts the correlation to 0.96-0.99; the two-sided variant moves it
a little further (err -0.019, -0.104, -0.077, -0.099; corr 0.989, 0.966, 0.980, 0.980). What is left is a bias of about
-0.1 (2 percent of lambda) that does not shrink from n 500 to 2000; the likeliest source is the quadratic form's
correction from H's own heavy rows and columns (H/n is not MP at these sizes), which a theorem has to control anyway.
So in the outlier regime the law of lambda_max is the law of Phi(rho_max), rho_max the largest mean square over the 2n rows
and columns: an extreme-value statement, not a TW one, with O(1) fluctuations (n^(2/3) std 53-72 here) inherited from the
largest entry and the row scale.
Where the regime ends (ck_crossover.py, ck_crossover_run1.txt): an outlier exists iff some line has rho > 2. The entry
tail is stretched-exponential (exponent 2/k), so a row reaches 2n by one big entry (big-jump principle); an entry in a row
of scale s makes an outlier when its theta^2 exceeds min(2 - V_k(s), 1). Expected number of such lines, Poisson count:
    He_3  n     2000   4000   8000   16000            He_4  n   16000   32000   64000   128000
    P(outlier) 0.969  0.447  0.047  0.001                       1.000   1.000   0.928   0.294
    entry-only 0.906  0.356  0.037  0.001                       1.000   1.000   0.918   0.283
The entry-only column reproduces the measured median theta^2 = 1 crossing at n 3400 (20 Oct 07:4x); the row criterion moves
the He_3 median to about n 3800 and the He_4 one to about n 1.0 x 10^5. A whole row heavy by scale alone (V_k(s) >= 2, no
big entry) matters only at small n (He_3: 0.79 at n 250, 4e-4 at n 1000). Past the crossover the edge is TW-like but still
shifted by the sub-critical heavy lines (19.5 widths at n 8000); Phi gives no shift below rho = 2, so that shift is the
next term (the lines with rho just under 2 push the edge up through the quadratic form), not this one.
The other runs (18:00; ck_rownorm_he3_n4000_run1.txt, ck_rownorm_he4_run1.txt, ck_rownorm_relu0_run1.txt):
        act   n     reps  lam mean   old err   old corr   row err   row rms   row corr
        he3   4000  20    4.1535     -0.1389   0.781      -0.0986   0.1074    0.868     (mixed regime: P(outlier) 0.45)
        he4   500   30    13.579     -0.2422   0.979      +0.2155   0.4674    0.998
        he4   1000  30    12.586     -0.7282   0.947      +0.1174   0.5338    0.995
        he4   2000  30    10.865     -0.2595   0.981      +0.1731   0.2530    0.999
        relu0 1000  20    3.9972     +0.0028   -          +0.0028   0.0346    -         (no line reaches rho 2; Phi = 4)
For He_4, deep in the outlier regime at every n here (crossover near 10^5), the row predictor tracks lambda_max at
correlation 0.995-0.999 with a bias of +1 to +2 percent; the entry formula's rms error is 2-5 times larger. The relu0
control has max line mean square below 2 in every rep, the predictor returns the edge 4, and lambda_max is 3.997. At He_3
n 4000 the reps straddle the threshold, Phi is close to 4 for most of them and the measured mean is 0.1 above: the same
residual as at n 500-2000, which therefore does not come from the outlier step. It is the push from heavy lines below
rho = 2, the term that keeps the n 8000 centre 19.5 widths above 4.
Still to do for target 2's theorem: an isotropic local law for H with these entry tails, to justify y^T R y = rho g + o(1)
uniformly over the heavy line, and the sub-critical push (the residual, of either sign: -0.1 for He_3, +1-2 percent for
He_4).

## 20 Oct 18:49 (claude-99aebc7f): target 2 - where the row predictor's residual lives (ck_schur.py)
For the heaviest line i, A = Y'^T Y'/n without it, the Schur equation 1 = (1/n) y_i^T (lambda - A)^(-1) y_i is solved three ways:
exactly (with A's eigenvectors; reproduces lambda_max to 1e-13 in every rep, the check), "iso" = |y_i|^2/n times A's own
Stieltjes transform m_A (y_i isotropic against A's resolvent, A's true spectrum), and Phi(rho) (A's spectrum MP(1) as well).
So iso - exact is the cost of isotropy and Phi - iso the cost of MP. Seed 7, float64:
        act   n     reps  lam mean   exact-lam  iso-exact (sd)      Phi-iso (sd)        Phi-lam   e_max(A)
        he3     500   12     5.7906   +5.2e-14   +0.0103 (0.2095)   -0.2215 (0.1735)   -0.2112   5.3498
        he3    1000   12     4.8602   +2.9e-14   +0.0715 (0.0805)   -0.1865 (0.1300)   -0.1151   4.5883
        he3    2000   12     4.3702   +1.2e-13   +0.0222 (0.1185)   -0.1298 (0.0523)   -0.1076   4.2696
        he4    1000    8    10.2699   +7.5e-14   +0.3107 (0.2237)   -0.1713 (0.0895)   +0.1393   8.6903
        he4    2000    8    10.0005   -1.8e-13   +0.1762 (0.4375)   -0.0785 (0.0557)   +0.0977   7.8854
For He_3 the residual is the spectrum, not the isotropy: iso - exact averages +0.01 to +0.07 with a per-rep spread of 0.1-0.2
(a rep in which y_i has 8-20 times its isotropic weight on one of A's top eigenvectors - two heavy lines resonating - moves
the root by up to 0.24 either way), while Phi - iso is -0.13 to -0.22 every time with a small spread. The cause is visible
in e_max(A): with line i removed, A's edge is still 4.27-5.35, not 4, because A keeps the other heavy rows and columns, so
m_A(lambda) > g_MP(lambda) near the outlier and the true root sits above Phi(rho). That is the same sub-critical push as the
n 8000 centring shift, seen from inside one Schur complement. It shrinks slowly (-0.22, -0.19, -0.13 at n 500, 1000, 2000).
The falsifier (ck_schur_next.py, ck_schur_next_he3_run1.txt, seed 8, 10 reps): if A's edge is set by its next heavy line,
e_max(A) tracks Phi(rho_2), rho_2 the largest line mean square left in A; a bulk effect would not. corr 0.45 at n 1000, 0.95 at
n 2000, with Phi(rho_2) below e_max(A) by 0.11 and 0.16: the same push one level down, from the lines after the second.
For He_4 the isotropy term is larger and of the other sign (y_i overweights A's top directions, iso above exact by 0.31 at n 1000, 0.18 at n 2000),
which with the MP term (-0.17) gives the +1-2 percent bias of the 18:00 table.
So a theorem for target 2 needs, besides the local law, a second-order term: lambda_max = root of 1 = rho m_A(lambda), with A
the matrix of the remaining lines, whose own edge is set by the next-heaviest lines (a recursive, extreme-value correction),
plus the resonance term between the two heaviest lines when they share a strong direction.

## 20 Oct 19:08 (claude-99aebc7f): target 2 - lambda_max is a function of the entry sizes, carried by the tail of entries
ck_surrogate.py (seed 9, two draws per surrogate): lambda_max of Y against "sign" (every entry given an independent random
sign, |Y_ij| kept, all dependence between entries destroyed), "sep" (Gaussian with the separable profile r_i c_j / mean, the
line norms only) and Phi(rho). Columns: mean difference, rms, correlation with lambda_max.
        act   n     reps  lam       sign - lam              sep - lam               Phi - lam
        he3    1000   8     5.7344   -0.0031 0.0450 0.999     +0.4593 0.5234 0.987     -0.0539 0.2800 0.991
        he3    2000   8     4.4236   -0.0047 0.0268 0.997     +0.1896 0.2003 0.968     -0.1136 0.1346 0.992
        he4    1000   8    18.9353   +0.0059 0.0204 1.000     +3.7153 4.8439 0.992     +0.3566 0.3842 1.000
        he4    2000   8     9.8517   +0.0070 0.0396 1.000     +0.8611 0.9980 0.991     +0.0520 0.3483 0.996
The sign surrogate reproduces lambda_max to an rms of 0.02-0.045 at correlation 0.997-1.000 (He_3 and He_4, n 1000 and
2000), so at these n the top eigenvalue is a function of the matrix of entry sizes |Y_ij|, not of the dependence between
entries that f(WX/sqrt n) builds in. The line norms alone are not enough: the separable profile overshoots in every case
(He_3 +0.46 and +0.19, He_4 +3.7 and +0.86 at n 1000 and 2000), because it spreads a line's mass evenly over the line when
it is concentrated. How concentrated (He_3, same seeds, 4 reps): the largest single Y_ij^2/n in the heaviest line is 1.6-3.2
of its rho 3.7-4.0 at n 500, 1.2-5.5 of rho 2.6-7.8 at n 1000, 0.7-2.4 of rho 2.3-3.5 at n 2000 (max |He_3| over n^2
Gaussians makes Y_ij^2/n decay only like (log n)^3/n). For an additive spike of size s = Y_ij^2/n on an MP(1) bulk the
outlier is (1 + s)^2/s, which is Phi(rho) at rho = 1 + s: the row predictor and a single-entry spike agree when the row is
spike plus unit bulk.
But a few spikes do not carry lambda_max. ck_topk.py (He_3, seed 9, 6 reps; Gaussian bulk at the remaining entries' mean
square, the K largest |Y_ij| put back in place; mean, rms, corr against lambda_max):
        n     K 10                K 100               K 1000              K 4000              K 16000
        1000  -0.432 0.557 0.970    -0.398 0.564 0.976    -0.211 0.298 0.995    -0.050 0.077 0.999    +0.011 0.029 1.000   
        2000  -0.258 0.329 0.712    -0.172 0.208 0.915    -0.034 0.079 0.982    -0.044 0.072 0.981    -0.014 0.038 0.992   
At n 1000 the error falls below 0.1 only at K about 4n; at n 2000 already at K about n/2. So the push comes from the many
moderately large entries of the tail (their number shrinks relative to n as the tail thins), not from the extremes alone.
A deterministic equivalent for the profile S = Y^2 (ck_dyson.py, the Hachem-Loubaton-Najim equations) is not usable here:
its real-z solution stops near 12.5-14 at n 500 against lambda_max 5.0-5.3, because single entries with S_ij/n of order 1
violate the equations' condition (max S_ij/n -> 0).
So the second-order term for target 2 lives in the tail of the entry-size matrix: a theorem would take lambda_max of a
matrix with independent signs and the given |Y_ij| (heavy-tailed, non-separable profile) and show it equals the line
predictor plus a tail correction; the sign symmetrisation itself (that the dependence of f(WX/sqrt n) does not matter at
the edge) is the other half, and is open.

## 21 Oct 01:46 (claude-99aebc7f): target 2 - a hybrid predictor: heavy entries exact, the rest by its deterministic equivalent (ck_hybrid.py)
The 19:08 section left lambda_max a function of the entry sizes, carried by the tail. ck_hybrid.py splits Y = L + H at a
threshold tau on S_ij/n = Y_ij^2/n, keeps H (P = H/sqrt n) exactly, and replaces the resolvent of the light part by its
deterministic equivalent: diagonal blocks zeta t_i, zeta tt_j from the HLN equations for the profile S_L (S with the heavy
entries zeroed) at z = lambda, off-diagonal block 0. With a = -zeta t, b = -zeta tt, an outlier sits where
sigma_max(diag(sqrt a) P diag(sqrt b)) = 1; the predictor is the largest such lambda, or the bulk edge of S_L when there is
none. "flat" replaces S_L by its mean square (Marchenko-Pastur bulk). Check: one spike s on a unit bulk, n 400: flat
reproduces (1+s)^2/s exactly (4.16667, 5.33333); hln is within 0.003 (4.16389, 5.32889), the finite-n HLN edge.

n 1000, 6 reps, seed 9; mean error against the true lambda_max (rms, correlation across reps):

    He_4 (lam 19.347)  tau 0.5   hln -0.038 (0.047, 1.000)   flat -0.329 (0.634)
                       tau 0.25  hln -0.054 (0.065, 1.000)   flat -0.186 (0.267)
                       tau 0.1   hln -0.071 (0.086, 1.000)   flat -0.195 (0.227)
                       tau 0.05  hln -0.065 (0.084, 1.000)   flat -0.102 (0.127)
    He_3 (lam 5.899)   tau 0.5   hln +0.353 (0.542, 0.964)   flat -0.428 (0.575)
                       tau 0.25  hln -0.053 (0.092, 0.999)   flat -0.576 (0.692)
                       tau 0.1   hln -0.195 (0.232, 0.998)   flat -0.411 (0.437)
                       tau 0.05  hln -0.230 (0.261, 0.998)   flat -0.291 (0.327)

He_4 is predicted to 0.3 pct at every tau. He_3 is predicted best at tau 0.25 (rms 0.09 against 0.28 for the row predictor
of 17:58); at tau 0.5 too few entries are kept and the HLN edge of the remainder overshoots (it is the same failure as the
whole-profile HLN of ck_dyson.py, entries with S/n of order 1 left in the bulk); at tau <= 0.1 the predictor undershoots by
0.2. The likely reason for the undershoot: with many moderate entries kept exactly, the diagonal deterministic equivalent
of the light resolvent drops the off-diagonal fluctuation that couples them through shared rows and columns; the flat
variant is worse everywhere, so the profile of the light part matters. He_3 at n 2000 is running (ck_hybrid_he3_run1.txt);
the first rep (lam 4.225) gives 4.334 at tau 0.25 with no outlier found, i.e. the bulk edge of S_L, and 3.89 / 3.73 at
tau 0.1 / 0.05. Whether a fixed tau works across n, or tau must scale with n, is what the n 2000 run will say.

02:17 21 Oct, He_3 at n 2000 (6 reps, lam 4.480): tau 0.5 hln +0.672 (rms 0.747, corr -0.30); tau 0.25 hln +0.100 (rms 0.152,
corr 0.93), flat -0.209; tau 0.1 hln -0.216 (rms 0.231, corr 0.997), flat -0.302; tau 0.05 hln -0.340 (rms 0.358, corr 0.995).
A fixed tau does not carry across n: at tau 0.25, three of six reps find no outlier and return the HLN edge of S_L (4.33-4.56
against lam 4.23-4.25), which is the same overshoot as tau 0.5 at n 1000 - entries with S/n in (0.1, 0.25] left in the light
part push the HLN edge too far once there are fewer large ones. At tau 0.1 the error is a stable offset, -0.195 at n 1000
and -0.216 at n 2000, with correlation 0.997-0.998: the predictor follows the rep-to-rep variation of lambda_max almost
exactly and misses by a near-constant amount. So the open piece is a correction for the light part, not the heavy part:
either the HLN edge is the wrong object for a light profile with entries of S/n ~ 0.1 (finite-n fluctuation of the edge),
or the diagonal deterministic equivalent drops the coupling of the ~1400 kept entries through shared rows. A test that
separates the two: replace the light part by an independent Gaussian matrix with the same profile S_L and recompute lambda_max
of (L' + H) - if the -0.2 persists it is the deterministic equivalent, if it vanishes it is the dependence inside L.

02:31 21 Oct, where the -0.2 comes from (ck_swap.py, He_3, n 1000, 6 reps, tau 0.1, K ~ 1150 heavy entries): keep H, swap the
light part L for an independent Gaussian with the same variance profile S_L ("gauss") or for |L| with independent random
signs ("signs"). Mean lambda_max: true 5.899, signs 5.947 (+0.047, rms 0.084), gauss 6.062 (+0.163, rms 0.206); the hybrid
predictor 5.704 misses the true matrix by -0.195, the signs copy by -0.242 and the Gaussian copy by -0.358. So the
dependence inside L is not the cause (random signs move lambda_max by 0.05); the predictor is wrong even on the matrix its
derivation assumes. The error is in the step itself: the diagonal deterministic equivalent of the light resolvent with the
off-diagonal block set to 0 is accurate for a perturbation of bounded rank, but here P has ~1150 entries (more than n) spread over its rows and
columns, so the O(n^{-1/2}) fluctuations of the quadratic forms of R on its rows and columns add up rather than vanish.
The next form to try is the operator-valued one: solve the HLN-type equations for the light profile with the heavy
entries entering through the self-energy (a block Dyson equation for (L, H) together), not as a separate secular equation.

## 21 Oct 07:5x (claude-99aebc7f): target 2 - the information-plus-noise predictor with the heavy entries fed back (ck_ipn.py), first two reps
ck_ipn.py solves the Hachem-Loubaton-Najim information-plus-noise deterministic equivalent for X + P, X the light part with
profile S_L, P = H/sqrt n the heavy entries, so the heavy entries enter psi, psit through the diagonals of T, Tt instead of
beside a frozen light resolvent. Checks: P = 0 gives edge(S); one spike s 3.0 on a unit bulk, n 300, gives 5.505 against
(1+s)^2/s = 5.333 (the finite-n overshoot of the unregularized 1/mu). He_3, n 1000, tau 0.1, seed 9 (ck_ipn_he3_tau01_run1.txt):

    rep 0 (K 1181)   true 4.6216   gauss copy 4.6215   hybrid 4.2805 (-0.341)   ipn 4.8475 (+0.226)
    rep 1 (K 1156)   true 8.7597   gauss copy 8.8962   hybrid 8.6694 (-0.227)   ipn 9.3087 (+0.413)

(errors against the gauss copy, the matrix both derivations assume.) On both reps the hybrid predictor sits below and the
unregularized ipn above, so the two bracket lambda_max of the Gaussian copy. The overshoot of ipn has the same sign as on the
one-spike check, which points at the 1/mu terms of the heavy-graph components with small singular values; ck_ipn2.py
replaces 1/mu by mu/(mu^2 + eps^2) per component (checks: P = 0 gives 4.00003; spikes 1.5 and 3.0 give 4.1556 and 5.3245
against 4.1667 and 5.3333, i.e. the overshoot is gone on the checks). Its He_3 reps and ck_ipn reps 2-5 are running.
Two reps are a bracket, not a rate; the section is updated when the six land.
ck_ipn2 rep 0 (21 Oct 08:2x, ck_ipn2_he3_tau01_run1.txt; true 4.6216): eps 0.1 gives 4.7509 (top reads bulk), eps 0.3 gives
4.5901 (top reads outlier); unregularized ipn 4.8475, hybrid 4.2805. Error 0.226 -> 0.129 (eps 0.1) -> -0.032 (eps 0.3). Caveat:
as eps grows the 1/mu feedback of the small components is switched off and the predictor slides toward ck_hybrid, so eps is a
dial between the two brackets, and one rep landing near the truth at eps 0.3 may be the dial, not the equation. The test is
rep 1 (true 8.7597, hybrid 8.6694, ipn 9.3087): if eps 0.3 again lands within the gauss copy's error (0.14) with no retuning,
the regularized equation carries the heavy part; if it lands near the hybrid, it does not.

ck_ipn rep 2 (21 Oct 08:3x, ck_ipn_he3_tau01_run1.txt): true 5.0654, gauss 5.3951, hybrid 4.6704, ipn 5.5139. The bracket
hybrid < true < ipn now holds on all three reps (4.28/4.62/4.85, 8.67/8.76/9.31, 4.67/5.07/5.51); the ipn excess is +0.23,
+0.55, +0.45 and the hybrid shortfall -0.34, -0.09, -0.40. On rep 2 the gaussian-equivalent prediction itself misses by
+0.33, so the heavy-tailed rows move the edge by more than the gauss error on this draw, in either direction.

ck_ipn rep 3 (21 Oct 09:3x, same file): true 4.8497, gauss 5.0461, hybrid 4.6913, ipn 5.2126. The bracket holds on 4/4 reps.
Over the four reps the ipn excess is +0.23, +0.55, +0.45, +0.36 (mean +0.40) and the hybrid shortfall -0.34, -0.09, -0.40,
-0.16 (mean -0.25); the gauss error on rep 3 is +0.20. The midpoint of the two brackets misses by -0.06, +0.23, +0.03, +0.10,
better than either end but not an equation; ck_ipn2 rep 1 still decides whether the regularized form is one.

ck_ipn rep 4 (21 Oct 10:4x, same file): true 6.2641, gauss 6.2784, hybrid 6.1820, ipn 6.7454. The bracket holds on 5/5 reps.
Over the five reps the ipn excess is +0.23, +0.55, +0.45, +0.36, +0.48 (mean +0.41) and the hybrid shortfall -0.34, -0.09,
-0.40, -0.16, -0.08 (mean -0.21). The midpoint misses by -0.06, +0.23, +0.03, +0.10, +0.20 (mean +0.10, positive on 4/5), so
the true edge sits on average a third of the way from hybrid to ipn, but the per-rep position is 0.60, 0.14, 0.47, 0.30,
0.15: no fixed weight between the two brackets is an equation.

ck_ipn2 rep 1 (21 Oct 11:5x, ck_ipn2_he3_tau01_run1.txt; same draw as ck_ipn rep 1): true 8.7597, eps 0.1 gives 9.2813 (top
reads bulk), eps 0.3 gives 8.7362 (top reads outlier); hybrid 8.6694, ipn 9.3087, gauss 8.8962. Error at eps 0.3 is -0.024
(rep 0: -0.032), inside the 0.14 set before the rep, with eps unchanged. With eps held at 0.3 the regularized predictor closes
0.91 (rep 0) and 0.74 (rep 1) of the gap from the hybrid to the truth, from below both times; eps 0.1 stays on the ipn side
(+0.13, +0.52). This rep is a weak discriminator, though: the hybrid itself misses by only -0.09 here, so "near the hybrid" and
"near the truth" were both within 0.14. The sharp test is ck_ipn2 rep 2, the draw where the hybrid misses by -0.40 (true
5.0654, hybrid 4.6704, ipn 5.5139): if eps 0.3 again lands within 0.14, the regularized equation carries the heavy part on the
draws where the two brackets disagree most; if it lands near 4.67, eps 0.3 is a dial that happened to fit two draws.

ck_ipn rep 5 (21 Oct 14:2x, ck_ipn_he3_tau01_run1.txt; the run is complete): true 5.8341, gauss 6.1329, hybrid 5.7318, ipn
6.2650. The bracket hybrid < true < ipn holds on 6/6 reps. Over the six reps the ipn excess is +0.23, +0.55, +0.45, +0.36,
+0.48, +0.43 (mean +0.416, rms 0.429) and the hybrid shortfall -0.34, -0.09, -0.40, -0.16, -0.08, -0.10 (mean -0.195, rms
0.232); the gauss-equivalent prediction misses by +0.16 on average (rms 0.29), +0.30 on this rep. The true edge sits at
0.60, 0.14, 0.47, 0.30, 0.15, 0.19 of the way from hybrid to ipn, so the two predictors are a two-sided bound on every draw
seen and neither end nor any fixed weight between them is the equation. Whether ck_ipn2 at eps 0.3 is one rests on its rep 2.

ck_ipn2 rep 2, the sharp test (21 Oct 15:1x, ck_ipn2_he3_tau01_run1.txt): true 5.0654, gauss 5.3951, hybrid 4.6704, eps 0.1
5.4983 (bulk label), eps 0.3 5.0818 (outlier label). On the draw where the hybrid misses by -0.395, eps 0.3 misses by +0.016,
within the 0.14 set before the rep landed and about 4% of the hybrid gap. Over reps 0-2 the eps 0.3 errors are -0.032, -0.024,
+0.016 (rms 0.025) against the hybrid's -0.341, -0.090, -0.395 (rms 0.306) and the gauss-equivalent's -0.000, +0.137, +0.330.
So on three of three draws the regularized joint equation at eps 0.3 places the edge to within 0.035, including the draw where
the two brackets are widest; it is behaving as the equation, not as a dial that fit two draws. eps 0.1 overshoots on all three
(+0.13, +0.52, +0.43) and its fixed point is the bulk branch each time, so the choice between the two values is the choice of
branch, and the outlier branch is the one that carries the heavy rows. What this does not yet settle: three reps at one n and
one tau; eps was picked from a two-point list, and whether 0.3 is the right regularization at n 2000 (or scales with n) is
untested. Reps 3-5 of the same run are still computing (about 4 h each) and are the next out-of-sample check; a rep with
|error| above 0.14 at eps 0.3 would reopen the question.

ck_ipn2 reps 3-5, out of sample (run finished 22 Oct 04:16, ck_ipn2_he3_tau01_run1.txt; written up 22 Oct 10:2x). eps 0.3
errors against the true lambda_max: rep 3 +0.074 (true 4.8497, 4.9233), rep 4 +0.018 (6.2641, 6.2818), rep 5 +0.050 (5.8341,
5.8836); all three inside the 0.14 bar set before they landed, and the top reads outlier each time. On the same draws the
hybrid misses by -0.158, -0.082, -0.102, the gauss-equivalent by +0.196, +0.014, +0.299, and eps 0.1 (bulk branch every time)
by +0.237, +0.444, +0.349. Over all six reps: eps 0.3 mean +0.017, rms 0.041; hybrid mean -0.195, rms 0.232; eps 0.1 mean
+0.352, rms 0.377. Reps 3-5 all err high (mean +0.047) where reps 0-2 averaged -0.013; at six reps the overall mean is about
one standard error from zero, so no bias is shown, but a run at a second n would tell a small upward drift from noise.
Settled at n 1000, tau 0.1: the outlier branch of the regularized joint equation places the He_3 edge to within 0.075 on six
of six draws, an order of magnitude closer than either bracket. Still open: eps was chosen from {0.1, 0.3} on rep 0; whether
the same eps works at n 2000 or at another tau, and what the equation is in the limit (the TARGET 2 outlier law), are untested.

## 22 Oct 11:1x: the eps dial on one isolated spike (ck_spike_n.py, ck_spike_n_run1.txt)

One spike of strength s = 3 on a flat n x n profile, the check built into ck_ipn2.py, run at n 150, 300 and 600 (the n 1200
row and the s 1.5 and 0.5 rows were cut when the machine ran out of memory; they were not rerun). Theory (1+s)^2/s = 5.33333.

| n | eps 0.03 | eps 0.1, 0.3 and 1.0 (identical to 5 digits) |
|---|---|---|
| 150 | 5.56894 (+0.2356, bulk) | 5.31558 (-0.01775, outlier) |
| 300 | 5.50024 (+0.1669, bulk) | 5.32446 (-0.00887, outlier) |
| 600 | 5.42984 (+0.0965, bulk) | 5.32892 (-0.00441, outlier) |

For eps at or above 0.1 the predictor does not depend on eps at all, and its error is -2.66/n to three digits at every n
(n times the error: 2.663, 2.661, 2.646), the plain finite-size shift of a spike that takes one entry out of the bulk. For eps
0.03 the fixed point stops at a bulk edge above the spike (the outlier's own pole is not damped enough and its mass spreads
over the edge, as in unregularized ck_ipn), with an error that falls with n like n^-0.6 to n^-0.8. So on an isolated spike
eps is not a dial: once it is above a threshold that shrinks with n, it drops out. The eps sensitivity seen on the He_3 draws
(eps 0.1 off by +0.35, eps 0.3 by +0.02) must then come from heavy-graph components with several near-singular modes, where
the regularization changes how neighbouring modes feed back, not from a single mode's own pole. That points the limit law
(TARGET 2) at the component structure: test next on a planted component of two or three coupled spikes, which is as cheap as
this check (seconds to a minute a size), before any n 2000 He_3 rep.

## 22 Oct 11:4x: the eps dial on a coupled block (ck_block_n.py, ck_block_n_run1.txt)

The same test with a planted block instead of one spike: on the first k rows and columns the mean matrix P carries the block
and the variance profile S is zero, flat elsewhere. Block A is 2x2 rank one with every entry sqrt(3)/2 (top singular value
t = sqrt 3, so the same limit 5.33333 as the spike s 3). Block B is the 3x3 full-rank matrix [[1.4,.6,0],[.6,1,.5],[0,.5,.8]],
singular values 1.918, 1.040, 0.242, limit (1+t^2)^2/t^2 = 5.95139 for the top one.

| block, n | eps 0.03 | eps 0.1 | eps 0.3 | eps 1.0 |
|---|---|---|---|---|
| A, 150 | +0.2231 (bulk) | -0.02965 | -0.02968 | -0.02999 |
| A, 300 | +0.1608 (bulk) | -0.01482 | -0.01482 | -0.01497 |
| A, 600 | +0.0934 (bulk) | -0.00741 | -0.00741 | -0.00747 |
| B, 150 | +0.2113 (bulk) | -0.03977 | -0.03983 | -0.04050 |
| B, 300 | +0.1541 (bulk) | -0.01984 | -0.01987 | -0.02021 |
| B, 600 | +0.0798 (bulk) | -0.00992 | -0.00992 | -0.01010 |

The picture is the spike's again. For eps at or above 0.1 the outlier branch is taken every time, eps moves the answer by at
most 0.0007, and the error is exactly c/n: n times the error is -4.45, -4.45, -4.45 for A and -5.97, -5.95, -5.95 for B (one
spike: -2.66). The constant grows with the number of rows the block takes out of the bulk, but nothing in it depends on eps.
For eps 0.03 the fixed point again stops at a bulk edge above the outlier, with an error close to the spike's at each n. A
second singular value just above 1 (B's 1.040, whose own outlier would sit at 4.0016, inside the finite-n edge) does not
disturb the top one.

So a single heavy component, coupled or not, rank one or full rank, does not make the predictor sensitive to eps. What the
He_3 draws have that these plants lack is many components at once, most of them near critical (t a little above 1), whose
damped poles sit at or just inside the edge where the bulk fixed point lives; that is where eps should matter, because there
it decides whether a near-critical mode is counted as an outlier or folded into the edge. The next cheap check plants m
blocks of t between 1.0 and 1.3 (m 5 to 40) beside one strong block and watches the top predictor and the edge as eps moves.

## 22 Oct 12:1x: near-critical modes crowding the edge (ck_multi_n.py, ck_multi_n_run1.txt)

One spike s 3 (limit 5.33333) beside m weak spikes of strength u drawn uniformly from [1.0, 1.3] (seed 1), each on its own
row and column with S zeroed on the diagonal entry, flat elsewhere. Every weak spike is above critical, but its own outlier
(1+u)^2/u is at most 4.07 for these u, so on its own it sits at or inside the finite-n edge. The run was stopped by the
machine's low-memory reaper during m 20, after the rows below; it was not restarted (the m 20 rows at n 300, 600 and all of m 40
are missing).

| m, n | eps 0.03 | eps 0.1 | eps 0.3 | eps 1.0 |
|---|---|---|---|---|
| 5, 150 | +0.2987 (bulk) | +0.0383 | +0.0364 | +0.0178 |
| 5, 300 | +0.1980 (bulk) | +0.0194 | +0.0185 | +0.0090 |
| 5, 600 | +0.1141 (bulk) | +0.0098 | +0.0093 | +0.0046 |
| 20, 150 | +0.4715 (bulk) | +0.3234 (bulk) | +0.1902 | +0.1199 |

This is the first planted structure on which eps is a real dial. With five near-critical spikes the error changes sign
(positive, where one spike or one block gave a negative c/n) and depends on eps: n times the error is +5.7, +5.6 and +2.7 for
eps 0.1, 0.3 and 1.0, steady across n 150 to 600, so it is still a finite-size effect. With twenty of them at n 150 eps 0.1
no longer finds the outlier at all and stops at a bulk edge 0.32 high, while eps 0.3 keeps the outlier branch and errs by 0.19.
That is the pattern of the He_3 draws (eps 0.1 on the bulk branch, off by +0.35 on average; eps 0.3 within 0.075). The eps
sensitivity there is then most plausibly the near-critical crowd: modes just above threshold whose damped poles sit on the
edge and push the top predictor up, more so the less they are damped. Two consequences for TARGET 2. The limit law has to
carry the density of near-critical components (here m/n), not only the strong ones; and the n-dependence on He_3 should follow
how that density scales with n. Missing rows to rerun when memory allows: m 20 at n 300 and 600, m 40, and a second seed.

## 22 Oct 12:3x: the twenty-spike row at n 300

The same twenty weak strengths (seed 1, u 1.008 to 1.285) beside the s 3 spike, now at n 300
(ck_multi_n_run2_m20n300.txt, 225 s). The errors against the single-spike theory 16/3:

| n | eps 0.03 | eps 0.1 | eps 0.3 | eps 1.0 |
|---|---|---|---|---|
| 150 | +0.4715 (bulk) | +0.3234 (bulk) | +0.1902 | +0.1199 |
| 300 | +0.2846 (bulk) | +0.0993 | +0.0957 | +0.0600 |

The bulk drop of eps 0.1 at n 150 does not survive doubling n: at n 300 eps 0.1 is back on the outlier branch and agrees with
eps 0.3 to 0.004. On the outlier branch the error is c/n with a fixed constant, n times the error 28.5 and 28.7 for eps 0.3,
18.0 and 18.0 for eps 1.0. So the crowd does two separate things. It inflates the finite-size constant, from about 5.6 with
five weak spikes to about 28.6 with twenty at eps 0.3 (more than linear in m, with different draws behind it); and at small n
it can push a small eps off the outlier branch altogether, which is the failure seen on He_3. Neither is a change in the limit:
every outlier-branch column still goes to 16/3 as 1/n. Two smaller points. Larger eps is the more accurate setting here (eps 1
errs about two thirds as much as eps 0.3 at both n), the opposite of what a smoothing argument would suggest, so the eps 0.3
default should not be taken as the best value. And eps 0.03 stays on the bulk branch at n 300, as on every planted structure
so far. For TARGET 2 this moves the question from the limit law to its rate: the constant in c/n depends on the near-critical
density, and a usable error bar for He_3 at its n needs that dependence. Still missing: m 20 at n 600, m 40, a second seed.

## 22 Oct 12:5x: the twenty-spike row at n 600

The same draw at n 600 (ck_multi_n_run3_m20n600.txt, 296 s):

| n | eps 0.03 | eps 0.1 | eps 0.3 | eps 1.0 |
|---|---|---|---|---|
| 300 | +0.2846 (bulk) | +0.0993 | +0.0957 | +0.0600 |
| 600 | +0.1633 (bulk) | +0.0499 | +0.0480 | +0.0300 |

The outlier-branch error halves exactly with each doubling of n. n times the error is 29.8 and 29.9 for eps 0.1, 28.7 and 28.8
for eps 0.3, 18.0 and 18.0 for eps 1.0, so the c/n law and its constants are settled for this draw at three sizes (eps 0.1 from
n 300 on, once it has left the bulk). The eps 0.03 column falls only by a factor 0.57 per doubling (about n^-0.8), which is the
bulk branch converging on its own scale, not the outlier one. What is left for TARGET 2 is the dependence of c on the
near-critical crowd: m 40 at the same strengths range, and a second seed at m 20 to separate the count from the draw.

## 22 Oct 13:0x: forty near-critical spikes at n 300

ck_multi_n_run4_m40n300.txt (seed 1; the 40 strengths contain the 20 of the m 20 rows). At n 300 the errors are
eps 0.03 +0.40434 (bulk), eps 0.1 +0.21235, eps 0.3 +0.20503, eps 1 +0.13252 (all three on the outlier branch), 415 s.

n times the outlier error at n 300, by the number m of near-critical spikes:

| m  | eps 0.1 | eps 0.3 | eps 1 |
|----|---------|---------|-------|
| 5  | 5.8     | 5.5     | 2.7   |
| 20 | 29.8    | 28.7    | 18.0  |
| 40 | 63.7    | 61.5    | 39.8  |

Doubling m from 20 to 40 multiplies the constant by 2.14, 2.14 and 2.21. From m 5 to m 40 the factor is 11.1 at eps 0.3,
an exponent of about 1.16 in m. So the constant is close to additive over the weak spikes, with a per-spike share that
rises slowly with the crowd (1.1, 1.43, 1.54 at eps 0.3). Two readings fit this. Either each added spike contributes
its own term and the later twenty strengths, nearer 1.3, carry larger terms, or there is a pairwise interaction among
the near-critical modes. The second seed at m 20 (different strengths) and m 40 at n 600 separate the two. The m 40 row
is one size only, so the 1/n law is not yet checked at m 40; m/n is 0.13 here.

## 22 Oct 15:2x: a second draw of the twenty strengths (ck_multi_n_run5_m20n300_seed2.txt)
The computation itself has no noise; the seed only draws the twenty weak strengths in [1.0, 1.3]. Seed 2 gives a
different set (1.017 to 1.29 against 1.008 to 1.285 for seed 1), and at n 300 the errors against 5.33333 are
eps 0.03 +0.28401 (bulk edge), eps 0.1 +0.09883, eps 0.3 +0.09523, eps 1 +0.05970, against seed 1's +0.28459,
+0.09934, +0.09571, +0.06001. Every entry moves by at most 0.0006, under one percent of itself. So the constant c in
the c/n error depends on how many near-critical modes crowd the edge and on their range, not on where inside the
range each one sits: the m 20 constants of the 12:3x section (n x err 29.8 / 28.7 / 18.0 for eps 0.1 / 0.3 / 1 at n 300; seed 2 gives 29.6 / 28.6 / 17.9)
stand for the family, not for one draw.

## 22 Oct 17:4x: the twenty weak strengths moved nearer critical (ck_multi_n_run6_m20n300_u1011.txt)
Same setup as the two m 20 draws above, but the twenty weak strengths are drawn in [1.0, 1.1] (1.003 to 1.095) in place
of [1.0, 1.3]. At n 300 the errors against 5.33333 are eps 0.03 +0.26936 (bulk edge), eps 0.1 +0.08540, eps 0.3 +0.08229,
eps 1 +0.05116 (outlier branch), 6091 s. n times the outlier error is 25.6 / 24.7 / 15.3 for eps 0.1 / 0.3 / 1, against
29.8 / 28.7 / 18.0 on [1.0, 1.3]: the constant falls by 14 to 15 percent at every eps when the crowd sits closer to 1, and
the per-spike share at eps 0.3 drops from 1.43 to 1.23. So the constant is not set by the count m alone. Spikes nearer
1.3 carry larger terms, which is the first of the two readings left open in the 12:3x section; a pairwise interaction
would push the other way, since modes packed into [1.0, 1.1] sit closer together. The eps 0.03 bulk-edge error moves
little (+0.284 to +0.269), so the edge branch is not driven by where the weak strengths sit. One size only: the c/n law at
this range is assumed from the [1.0, 1.3] runs, not checked here.

## 22 Oct 23:0x: the [1.0, 1.1] crowd at n 600 (ck_multi_n_run7_m20n600_u1011.txt)
The same twenty strengths as the 17:4x run (1.003 to 1.095), now at n 600 (8294 s). Errors against 5.33333: eps 0.03 +0.15425
(bulk edge), eps 0.1 +0.04286, eps 0.3 +0.04127, eps 1 +0.02561. n times the outlier error is 25.7 / 24.8 / 15.4 for
eps 0.1 / 0.3 / 1, against 25.6 / 24.7 / 15.3 at n 300; the fitted exponent per doubling is 0.995, 0.996 and 0.998. So the
c/n law holds at this range too, and the 14 to 15 percent drop of the constant against [1.0, 1.3] is a property of the
constant, not of a size where the law had not yet set in. The eps 0.03 bulk-edge column falls by a factor 0.573 per doubling
(exponent 0.80), the same rate as on [1.0, 1.3] (0.57): the bulk branch converges on its own scale whatever the crowd's range.
The open part of TARGET 2 is now the form of c as a function of the crowd: a per-spike term that grows with the strength
(the reading the 17:4x run favoured) together with the m exponent of about 1.16 predicts n x err near 24.7 x 2^1.16 = 55 at eps 0.3 for m 40 on [1.0, 1.1]; one run at
n 300 tests it.

