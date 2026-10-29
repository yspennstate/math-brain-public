# Second review: T084-C019 to C024 v1 (random-cluster routes, worker T)

Reviewer: agent B, not the author (worker T) and not the first reviewer
(P, account 3, PASS filed 15 Oct 14:26Z per
w680_rc_local_review_receipt.json). I did not read the first review
(W680_C019_C024_REVIEW.md) or its check scripts before writing this.

Frozen sources, (local file), SHA256 prefixes (full
hashes in RECEIPT_C019_C024.json; they match the receipt's):
C019 6975b52f923c2f83, C020 4a462339a9e10f07, C021 1f7790eac3292f22,
C022 eb7caef9fa45dc4b, C023 dfefea8a1c06ceec, C024 183639e1407309be.

Verdict: PASS on all six, correctness only. No priority judged.

## C019 (route failure, target 2)
On K_{m,n} with the stated A: if e = ab is not a bridge of a superset B, a needs a
second neighbour in R; likewise c. Those edges survive deleting e and f and attach
a and c to the connected M (L nonempty), so B - {e,f} is connected and e, f are
not joint bridges. Correct. The coefficient remark is also right: at rank 2 with
two adjacent marked edges on a simple triangle-free graph the only configuration
is {e,f} (b = 1), while joint bridges need a cycle through both edges, length at
least 4, rank at least 3 (j = 0). Scores nothing by itself (route failure).

## C020 (route failure, target 3)
Identity (1) re-derived: incident edges meeting r of the k components of B leave
k+1-r components; the per-component factor [(1+tz)^s + q - 1] follows. At
q = t = 1/2 on K4, my own enumeration of all 64 subsets gives degree coefficients
(15/32, 45/32, 63/64, 27/128) = (3/128)(20, 60, 42, 9); formula (2) agrees
exactly; the cubic's discriminant is -62640 with one real root (check_c020.py).
The conditional covariance (3) re-derived: t^2(1+t)^(s-2)[D_s - (1+t)^s]/D_s^2
with D_s - (1+t)^s = q - 1. Correct, and the text is right that the mixing term is
not bounded.

## C021 (narrowed: adjacent RC pairs at closing weight >= 1-q)
Re-derived: Cov = -z_e z_f R / Z^2 with R = W10 W01 - W00 W11; the component jump
on deleting both marked edges is 1_e + 1_f + 1_joint (both bridges give 2, one
gives 1, neither gives 0 or the joint 1; joint and bridge cases are disjoint);
expanding q^Delta = (1-s)^Delta gives the four W's and
R = s^2 P_e P_f + s T (J - s B). The injection A -> A + g: a and c lie in
different parts after deleting e, f (a path would put e on a cycle), g is absent,
the image has e, f joint, keeps k, gains z_g. So J >= z_g B >= s B and R > 0.
Correct for any graph containing the triangle, with arbitrary other weights.

## C022 (narrowed: all K_n pairs at lambda >= (1-q) + sqrt(1-q))
Same-component map: add the edge joining the two outer marked endpoints; k kept,
gain lambda; an image has at most two preimages (one candidate edge in each marked
part), so B_same <= (2/lambda) J. Different-component map: add ac and bd; the cycle
a-b-d-c-a carries e and f, k drops by one, gain lambda^2/q, injective, so
B_diff <= (q/lambda^2) J. Then s(2/lambda + q/lambda^2) <= 1 iff
lambda >= s + sqrt(s^2 + sq) = s + sqrt(s). Below-one range iff q > (sqrt5-1)/2.
Correct. With C021 this covers every edge pair of every K_n for these parameters.

## C023 (narrowed: four cross edges, general graph)
The C022 maps with per-edge gains: per marked partition the reciprocal gains of
the two candidates sum to 1/x+1/y (ac|bd) or 1/u+1/v (ad|bc), so B_same <= M J;
the fixed best matching gives B_diff <= (q/P) J. (1-q)(M + q/P) <= 1 gives
J >= (1-q) B. Weights >= 2: (1-q)(1+q/4) < 1. Correct.

## C024 (literature)
PDF papers/tang_zhang_primary.pdf, SHA256 13b86d64...0fef210 (matches). Theorem
1.2 and hypothesis (1.13), |boundary S| >= h(|S| + d_n min(|S|, L_n)) with
L_n = ceil(16(r_n+2)/h), read from the PDF text. For K_{N,N}: boundary
N(a+b) - 2ab >= Ns/2 >= (s + N min(s, L))/4, h = 1/4, r = 2, L = 256, d = N;
connected, regular, r log d = o(d), distinct edges at distance <= 1. The paper's
Section 1.5 already names balanced complete multipartite graphs. Correct as a
locator record; not a new result.

## Row consequence
C021-C023 now carry two distinct-account PASSes (account 3 Codex reviewer and
this Claude session); the lead decides the frontier move.
