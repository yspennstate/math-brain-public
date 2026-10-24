P0193: a wider two-atom obstruction
Label: author-checked kernel proof and candidate free-probability refutation. Cached primary criterion checked; blind audit pending w346. No solved-problem claim.

The prior store card uses a = log(10) and four level crossings. Its quoted criterion is Lemma 4.1(3) of Hasebe, Ueda and Wang, Log-unimodality for free positive multiplicative Brownian motion, arXiv:2009.13848. The exact criterion and time normalization are now checked against the cached primary text at sources/free_positive_unimodality_2020_correct/text.txt, character 16998, as preserved in primary_source_excerpts.json. Lemma 4.1(3) states that log-unimodality is equivalent to the equation (sin R/R) integral r xi/[1+r^2 xi^2-2r xi cos R] dnu(xi)=1/t having at most two positive r-roots for every R in (0,pi). Thus its normalization is exactly integral=R/(t sin R). This is a source check by the author of this packet; the independent auditor must check it again.

Let a > 0, C = cosh(a), c = cos(R), and
K_R(s) = 1/[2(cosh(s)-cos(R))],
F_R(u) = [K_R(u-a)+K_R(u+a)]/2.
For 0 < R < pi and y = cosh(u), adding the two fractions gives
F_R(u) = (C y-c)/[2(y^2-2c C y+c^2+C^2-1)].
All denominators are positive, since they are products of positive cosh(u +/- a)-c terms. At the continuous limiting value R = pi this reduces to
F_pi(u) = (C y+1)/[2(y+C)^2].
Differentiation with respect to y gives
dF_pi/dy = [C^2-C y-2]/[2(y+C)^3].

If 1 < C <= 2, this derivative is nonpositive for y >= 1 (strictly negative for y > 1), so the limiting symmetric kernel has a single maximum at u = 0. If C > 2, it increases up to y_* = C-2/C > 1 and decreases afterwards. Consequently its two maxima are at +/- u_* with u_* = arcosh(C-2/C), while u = 0 is a strict local minimum. Their values are
m = F_pi(0) = 1/[2(C+1)],
M = F_pi(u_*) = C^2/[8(C^2-1)],
M-m = (C-2)^2/[8(C^2-1)] > 0.
Thus C > 2 is the exact threshold for bimodality of this limiting kernel. It is not claimed as a necessary threshold for the free-convolution problem.

Here is an explicit uniform four-crossing construction for every C > 2. Set
h = (m+M)/2,
q = C-1/(2h),
c_0 = min(0,(q-1)/2),
R_0 = arccos(c_0),
T = R_0/[h sin(R_0)].
Since h > m, q > -1, hence -1 < c_0 <= 0 and c_0 < q. In particular R_0 < pi and T is finite. The function R/sin(R) is strictly increasing on (0,pi): its derivative has numerator sin(R)-R cos(R), which starts at zero and has derivative R sin(R) > 0. It tends to infinity as R tends to pi. Therefore each t >= T has a unique R in [R_0,pi) satisfying R/[t sin(R)] = h.

For that R, c <= c_0 < q, so F_R(0) = 1/[2(C-c)] < h. For every fixed u the kernel increases with c, so F_R(+/-u_*) >= F_pi(+/-u_*) = M > h. Also F_R(u) tends to zero at both infinities. Continuity therefore gives at least four distinct solutions of F_R(u) = h, one in each of (-infinity,-u_*), (-u_*,0), (0,u_*), and (u_*,infinity).

Candidate consequence using the checked criterion: the cited equivalence requires at most two such r-roots for every R in (0,pi) whenever sigma_t free-multiplicatively convolved with nu is log-unimodal. Therefore nu = (delta_(exp(-a))+delta_(exp(a)))/2 fails that criterion for every t >= T whenever a > arcosh(2). Substituting r = exp(u) converts the atomic integral into the kernel above. The reciprocal symmetry of the two atoms makes the choice r = exp(u) versus exp(-u) immaterial here.

This extends the prior witness a = log(10) to every a > arcosh(2). The previous single recorded witness is a = log(10), approximately 2.302585; the new sufficient family contains every a > arcosh(2), approximately 1.316958. The source criterion has been checked locally; novelty and independent approval of the full free-probability inference remain unverified.

Checks that matter: the factor 1/2 in the mixture; positivity of denominators; the limiting versus finite R distinction; strict separation h between m and M; c_0 > -1; the time normalization in the paper; and the necessity direction of its lemma. The exact-arithmetic tests check the first five, with C = 2 as a boundary control. A blind reviewer must check the last two against the cached paper.
