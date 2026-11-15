# Independent referee log

2026-11-11T10:19:16.286882+04:00 — Started review of ALLN_PROOF.md. Owner task: referee ALLN_PROOF.md, steps 1–7. All writes and scripts stay in this folder. No web, no agents, no push. Global brain/checklist/mesh commands that write outside the folder are not run under this task’s narrower instruction. Computations use nice -n 15 and one process at a time, each below five minutes and 1 GB.

Read the note in full; no verdict yet.

Resource check: startup governor status ok (read only). nice -n 15 prints a setpriority warning because priority is already capped; os.getpriority reports 10. Every computation will still be prefixed nice -n 15. numpy/scipy/mpmath import successfully.

Audit driver startup correction: Darwin rejected the virtual-address limit before any check ran. Removed that nonportable limit; exact checks use a few MB, and the numerical driver will check resident memory and use bounded batches. The sandbox rejects nice priority adjustment; the wrapper is present on every computation, and inherited niceness is 10.
## 1. Step 1 — CORRECT
Formal expansion in Q[n,q,p²,m] gives zero difference after clearing n(n−1). The RHS has q coefficient 2(n−3)−2=2(n−4), p² coefficient −2(n−3), and constant −[2(n−3)+(n²−6n+6)]/n=−(n−4). An independent six-term determinant expansion gives nTQ−nP²−T³. A Gram matrix is positive semidefinite, and T>0, so division by nT³ gives q−p²≥1/n. A=n²−6n+6=(n−3)²−3≥1 for n≥5. Hence C=(n−1)(A+2nq)>0 for all permitted nonzero x. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 1

## 2. Normalisation — GAP, easily filled
Quote: “Sort x decreasingly, replace x by −x if x_1+x_n<0, and scale so that x_1=1. Then x_1=1≥b”. Changing sign reverses the ordering. For n=14 and x=(1 repeated 13 times,−13), the literal operations return the same vector, b=13>1. Re-sort after the sign change (equivalently replace (x_1,…,x_n) by (−x_n,…,−x_1)); then the stated normalization is valid. Psi is invariant under every permutation, sign change, and nonzero scaling. A nonzero sum-zero sorted vector has x_1>0 and x_n<0, so x_1=0 and b=0 cannot occur.

With that repair: (I) eps=x_2≥0 and x_(n−1)≥−eps, so all middle entries lie in [−eps,eps]; M=eps≤mT. (II) eps=−x_(n−1)≥0 and x_2≤eps, giving the same interval and M=b eps≤mT. Thus Y2≤(n−2)eps² and delta=1−b=−sum middle lies in [0,(n−2)eps]. On x_2+x_(n−1)=0, both eps agree, but the two valid lower bounds M=eps and M=b eps may differ; this is consistent because b≤1. Command: ... python3 audit.py 2

## 3. Step 2 (I) — CORRECT; Step 2 (II) — CORRECT
(I) F(e1)=−1/10+441(n−2)/(100 n²(n−1)²)<0 for n≥5; F(1)=−n(n−2)<0. Since eps=x_2≤1, the entire range [e1,1] is covered. The first bound follows, for example, because (n−2)/(n²(n−1)²) decreases for n≥3 and at n=5 the correction is 1323/40000<1/10.

(II) Sorting gives b≥eps; the sum gives b≥1−(n−2)eps. For f(b)=b eps/[1+b²+(n−2)eps²], f'(b)=eps[1+(n−2)eps²−b²]/[1+b²+(n−2)eps²]²≥0 for 0≤b≤1, eps≥0. This covers every occurring eps (0≤eps≤b≤1). For eps≥1/(n−1), substituting b=eps works exactly when eps²≥1/(n−1)². For eps≤1/(n−1), the lower b=1−(n−2)eps is positive. Clearing its positive denominator gives the stated quadratic, which factors as −(n−2)(n²−1)(eps−2/((n−2)(n+1)))(eps−1/(n−1)). Therefore every eps in [e2,1/(n−1)] and [1/(n−1),1] is covered. e2≤e1 iff (n−7)(n+6)≥0. In particular [e2,e1] is included in Step 2 (II), and eps>1/(n−1) is in its first subcase. The Step 2 / Step 3 ranges overlap at their endpoints; the II subcases overlap at 1/(n−1). Thus coverage is complete, though not disjoint if “exactly” means disjoint. All polynomial evaluations and roots checked with Fractions for n=5,…,5000. Command: ... python3 audit.py 3

## 4. Step 3 — GAP in written justifications, filled here
All displayed lower bounds have the correct sign, once normalization is repaired. M≥kappa eps holds in I because M=eps, and in II because b≥1−(n−2)e2=kappa. The quotient M/eps only makes sense when eps>0; eps=0 is handled separately. Y2≤(n−2)e1²≤0.002 for n≥14, because this bound decreases with n; T≥1 and T≤2+Y2≤2.002. Expanding 2(1+b⁴+Y4)−(1+b²+Y2)² gives (1−b²)²+2Y4−2(1+b²)Y2−Y2²≥−4Y2−Y2². For 0<b≤1, 1−b³=(1−b)(1+b+b²)∈[0,3delta]; |Y3|≤eps Y2 and Q=1+b⁴+Y4≥1. Since n−4>0, its term uses a lower bound on 2Q−T². Since −2(n−3)<0, the P² term uses the upper bound P²≤(3(n−2)eps+eps Y2)². The M coefficient is positive, M≥0 and Q≥1: first replacing Q by 1, then M by kappa eps, lowers it. This proves the displayed G_M bound.

Exact comparisons at n=14 (all decimal constants treated as rational):
- Ymax: 27/16900 = 0.00159763313609467
- first_left: 18009/3250 = 5.54123076923077
- first_right: 9971/750 = 13.2946666666667
- second_left: 10693188033/32500000 = 329.021170246154
- second_right: 2274/5 = 454.8
- third_left: 329043/250 = 1316.172
- third_right: 2274/5 = 454.8

All three inequalities and Y2 bound verified exactly for every integer n=14,…,5000 (full Fractions in exact_comparisons.json). The final “1316 against 455” is rounded: the exact numbers are 329043/250=1316.172 and 2274/5=454.8.

Proof for every larger n: (a) (n−2)/(n²(n−1)²) has negative derivative for n≥3 (numerator −3n²+9n−4), so its n=14 value suffices. (b) 4.002(n−4)(n−2)e1 < 4.002*2.1=42021/5000 < D(14)/100, and D=(n−1)²(n²−6n+6)/(n+1) increases for n≥5, since both (n−1)²/(n+1) and n²−6n+6 are positive increasing factors. (c) the second coefficient divided by n−2 is (189/5)*(n−3)(n−2)/(n(n−1))*(1+1/(1500(n−2)))² < (189/5)*(18001/18000)² < 379/10. (d) D/(n−2)=n²−7n+14+(−18n+34)/(n²−n−2). Its derivative is 2n−7+(18n²−68n+70)/(n²−n−2)²>0 for n≥4 (the quadratic numerator has discriminant −416 and positive leading coefficient). This supplies the missing proof of “the ratio grows”. For eps>0 the unused +2n(n−1)kappa eps term even makes G_M>0; for eps=0, b=1 and all middle entries vanish, so Psi=0. The strict first comparison must be read as non-strict at eps=0, or separated as done here. Command: ... python3 audit.py 4

## 5. Boundary tests — CORRECT after normalization repair
Exact rational tests at n=14, including eps=0, eps=e1, eps=e2, b=1, b=eps, many repeated values, one positive entry, and the two-case overlap. Every value equals the value for −x and for a scaled permutation.
- eps0: Psi=0 (0)
- I_e1_b1: Psi=3058171533064440/309039175947529 (9.89574064093311)
- I_e2_b1: Psi=5066210201220/531637854301 (9.52943843301203)
- II_e1_all_middle_negative: Psi=2866787329923/302919972238 (9.46384389494994)
- II_e2_all_middle_negative: Psi=260876/28561 (9.13399390777634)
- b_equals_eps_equality: Psi=0 (0)
- b_equals_eps_other: Psi=4235/6 (705.833333333333)
- many_equal_balanced: Psi=720/7 (102.857142857143)
- one_positive_unequal: Psi=32741269/1361886 (24.0411231189688)
- overlap_eps_positive_b_lt_1: Psi=1075511085/16777216 (64.10545617342)
Details and full rational vectors: boundaries.json. b=eps occurs throughout the one-positive/all-negatives-equal family, with some zero middle entries allowed; the samples above include both zero and strictly positive Psi. For eps=0 the unique normalized vector is (1,0,…,0,−1). Command: ... python3 audit.py 5

6 search random start: priority=10, single BLAS thread, 265s watchdog; continuous search is not an exact global certificate.

6 random/local n=5: min Psi=-2.22044604925031e-16; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.2 MB.

6 random/local n=6: min Psi=-2.22044604925031e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.3 MB.

6 random/local n=7: min Psi=-4.44089209850063e-16; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.4 MB.

6 random/local n=8: min Psi=8.88178419700125e-16; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.5 MB.

6 random/local n=9: min Psi=0; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.5 MB.

6 random/local n=10: min Psi=1.33226762955019e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.6 MB.

6 random/local n=11: min Psi=-3.5527136788005e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.7 MB.

6 random/local n=12: min Psi=0; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.7 MB.

6 random/local n=13: min Psi=1.99840144432528e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.8 MB.

6 random/local n=14: min Psi=2.22044604925031e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.8 MB.

6 random/local n=15: min Psi=-1.24344978758018e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=78.9 MB.

6 random/local n=16: min Psi=2.66453525910038e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.0 MB.

6 random/local n=17: min Psi=-1.24344978758018e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.1 MB.

6 random/local n=18: min Psi=3.10862446895044e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.2 MB.

6 random/local n=19: min Psi=-3.5527136788005e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.3 MB.

6 random/local n=20: min Psi=3.5527136788005e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.3 MB.

6 random/local n=21: min Psi=3.77475828372553e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.5 MB.

6 random/local n=22: min Psi=3.99680288865056e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.5 MB.

6 random/local n=23: min Psi=0; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.7 MB.

6 random/local n=24: min Psi=4.44089209850063e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=79.8 MB.

6 random/local n=25: min Psi=3.5527136788005e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.0 MB.

6 random/local n=26: min Psi=-2.1316282072803e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.0 MB.

6 random/local n=27: min Psi=-1.06581410364015e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.3 MB.

6 random/local n=28: min Psi=-1.77635683940025e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.3 MB.

6 random/local n=29: min Psi=0; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.6 MB.

6 random/local n=30: min Psi=-3.90798504668055e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.6 MB.

6 random/local n=31: min Psi=-1.77635683940025e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.9 MB.

6 random/local n=32: min Psi=6.21724893790088e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=80.9 MB.

6 random/local n=33: min Psi=-3.5527136788005e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.1 MB.

6 random/local n=34: min Psi=6.66133814775094e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.2 MB.

6 random/local n=35: min Psi=6.88338275267597e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.2 MB.

6 random/local n=36: min Psi=7.105427357601e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.3 MB.

6 random/local n=37: min Psi=7.32747196252603e-15; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.3 MB.

6 random/local n=38: min Psi=-1.4210854715202e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.4 MB.

6 random/local n=39: min Psi=-5.6843418860808e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.5 MB.

6 random/local n=40: min Psi=0; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.6 MB.

6 random/local n=64: min Psi=-1.4210854715202e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=81.9 MB.

6 random/local n=100: min Psi=2.1316282072803e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=82.3 MB.

6 random/local n=257: min Psi=5.61772850460329e-14; 770 samples, 18 local starts; vector saved in random_progress.json; peak RSS=84.0 MB.

6 random invocation checkpoint: 39/39 n completed, elapsed=6.09s. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py random --budget 180.0


Boundary-test correction before numerical block search: the previous label b_equals_eps_other had a two-positive vector belonging to case I, where its eps was 1. Relabeled it many_equal_two_positive and added the actual case II example (1, zero repeated 11 times, −1/2, −1/2). This changes no proof conclusion. Re-running stage 5 below.
## 5. Boundary tests — CORRECT after normalization repair
Exact rational tests at n=14, including eps=0, eps=e1, eps=e2, b=1, b=eps, many repeated values, one positive entry, and the two-case overlap. Every value equals the value for −x and for a scaled permutation.
- eps0: Psi=0 (0)
- I_e1_b1: Psi=3058171533064440/309039175947529 (9.89574064093311)
- I_e2_b1: Psi=5066210201220/531637854301 (9.52943843301203)
- II_e1_all_middle_negative: Psi=2866787329923/302919972238 (9.46384389494994)
- II_e2_all_middle_negative: Psi=260876/28561 (9.13399390777634)
- b_equals_eps_equality: Psi=0 (0)
- b_equals_eps_other: Psi=847/3 (282.333333333333)
- many_equal_two_positive: Psi=4235/6 (705.833333333333)
- many_equal_balanced: Psi=720/7 (102.857142857143)
- one_positive_unequal: Psi=32741269/1361886 (24.0411231189688)
- overlap_eps_positive_b_lt_1: Psi=1075511085/16777216 (64.10545617342)
Details and full rational vectors: boundaries.json. b=eps occurs throughout the one-positive/all-negatives-equal family, with some zero middle entries allowed; the samples above include both zero and strictly positive Psi. For eps=0 the unique normalized vector is (1,0,…,0,−1). Command: ... python3 audit.py 5

6 search blocks start: priority=10, single BLAS thread, 265s watchdog; continuous search is not an exact global certificate.

6 block batch 1: n=5, k=2, partitions 1–2/2, min Psi=-2.44249065417534e-15; full values saved in block_batches/batch_00000_n5_k2.npz; peak RSS=77.7 MB.

6 block batch 2: n=5, k=3, partitions 1–2/2, min Psi=-8.88178419700125e-16; full values saved in block_batches/batch_00001_n5_k3.npz; peak RSS=77.7 MB.

6 block batch 3: n=5, k=4, partitions 1–1/1, min Psi=1.33226762955019e-15; full values saved in block_batches/batch_00002_n5_k4.npz; peak RSS=77.8 MB.

6 block batch 4: n=6, k=2, partitions 1–3/3, min Psi=-2.22044604925031e-15; full values saved in block_batches/batch_00003_n6_k2.npz; peak RSS=77.8 MB.

6 block batch 5: n=6, k=3, partitions 1–3/3, min Psi=2.22044604925031e-15; full values saved in block_batches/batch_00004_n6_k3.npz; peak RSS=77.9 MB.

6 block batch 6: n=6, k=4, partitions 1–2/2, min Psi=9.32587340685131e-15; full values saved in block_batches/batch_00005_n6_k4.npz; peak RSS=78.0 MB.

6 block batch 7: n=7, k=2, partitions 1–3/3, min Psi=-2.22044604925031e-15; full values saved in block_batches/batch_00006_n7_k2.npz; peak RSS=78.2 MB.

6 block batch 8: n=7, k=3, partitions 1–4/4, min Psi=-4.44089209850063e-16; full values saved in block_batches/batch_00007_n7_k3.npz; peak RSS=78.4 MB.

6 block batch 9: n=7, k=4, partitions 1–3/3, min Psi=1.19904086659517e-14; full values saved in block_batches/batch_00008_n7_k4.npz; peak RSS=78.4 MB.

6 block batch 10: n=8, k=2, partitions 1–4/4, min Psi=-8.88178419700125e-16; full values saved in block_batches/batch_00009_n8_k2.npz; peak RSS=78.4 MB.

6 block batch 11: n=8, k=3, partitions 1–5/5, min Psi=6.21724893790088e-15; full values saved in block_batches/batch_00010_n8_k3.npz; peak RSS=78.5 MB.

6 block batch 12: n=8, k=4, partitions 1–5/5, min Psi=3.99680288865056e-14; full values saved in block_batches/batch_00011_n8_k4.npz; peak RSS=78.5 MB.

6 block batch 13: n=9, k=2, partitions 1–4/4, min Psi=-9.76996261670138e-15; full values saved in block_batches/batch_00012_n9_k2.npz; peak RSS=78.5 MB.

6 block batch 14: n=9, k=3, partitions 1–7/7, min Psi=-7.105427357601e-15; full values saved in block_batches/batch_00013_n9_k3.npz; peak RSS=78.7 MB.

6 block batch 15: n=9, k=4, partitions 1–6/6, min Psi=2.93098878501041e-14; full values saved in block_batches/batch_00014_n9_k4.npz; peak RSS=78.9 MB.

6 block batch 16: n=10, k=2, partitions 1–5/5, min Psi=0; full values saved in block_batches/batch_00015_n10_k2.npz; peak RSS=78.9 MB.

6 block batch 17: n=10, k=3, partitions 1–8/8, min Psi=8.61533067109121e-14; full values saved in block_batches/batch_00016_n10_k3.npz; peak RSS=78.9 MB.

6 block batch 18: n=10, k=4, partitions 1–9/9, min Psi=4.88498130835069e-14; full values saved in block_batches/batch_00017_n10_k4.npz; peak RSS=79.4 MB.

6 block batch 19: n=11, k=2, partitions 1–5/5, min Psi=-6.21724893790088e-15; full values saved in block_batches/batch_00018_n11_k2.npz; peak RSS=79.5 MB.

6 block batch 20: n=11, k=3, partitions 1–10/10, min Psi=2.66453525910038e-15; full values saved in block_batches/batch_00019_n11_k3.npz; peak RSS=79.6 MB.

6 block batch 21: n=11, k=4, partitions 1–11/11, min Psi=3.09974268475344e-13; full values saved in block_batches/batch_00020_n11_k4.npz; peak RSS=80.2 MB.

6 block batch 22: n=12, k=2, partitions 1–6/6, min Psi=0; full values saved in block_batches/batch_00021_n12_k2.npz; peak RSS=80.2 MB.

6 block batch 23: n=12, k=3, partitions 1–12/12, min Psi=2.39808173319034e-13; full values saved in block_batches/batch_00022_n12_k3.npz; peak RSS=80.2 MB.

6 block batch 24: n=12, k=4, partitions 1–15/15, min Psi=3.38040706537868e-12; full values saved in block_batches/batch_00023_n12_k4.npz; peak RSS=80.2 MB.

6 block batch 25: n=13, k=2, partitions 1–6/6, min Psi=-5.32907051820075e-15; full values saved in block_batches/batch_00024_n13_k2.npz; peak RSS=80.2 MB.

6 block batch 26: n=13, k=3, partitions 1–14/14, min Psi=-1.77635683940025e-15; full values saved in block_batches/batch_00025_n13_k3.npz; peak RSS=80.2 MB.

6 block batch 27: n=13, k=4, partitions 1–18/18, min Psi=2.35900188272353e-12; full values saved in block_batches/batch_00026_n13_k4.npz; peak RSS=80.3 MB.

6 block batch 28: n=14, k=2, partitions 1–7/7, min Psi=5.32907051820075e-15; full values saved in block_batches/batch_00027_n14_k2.npz; peak RSS=80.3 MB.

6 block batch 29: n=14, k=3, partitions 1–16/16, min Psi=2.36255459640233e-13; full values saved in block_batches/batch_00028_n14_k3.npz; peak RSS=80.3 MB.

6 block batch 30: n=14, k=4, partitions 1–23/23, min Psi=9.46798195400333e-13; full values saved in block_batches/batch_00029_n14_k4.npz; peak RSS=80.6 MB.

6 block batch 31: n=15, k=2, partitions 1–7/7, min Psi=-1.24344978758018e-14; full values saved in block_batches/batch_00030_n15_k2.npz; peak RSS=80.6 MB.

6 block batch 32: n=15, k=3, partitions 1–19/19, min Psi=-3.5527136788005e-15; full values saved in block_batches/batch_00031_n15_k3.npz; peak RSS=80.7 MB.

6 block batch 33: n=15, k=4, partitions 1–27/27, min Psi=3.33244543071487e-12; full values saved in block_batches/batch_00032_n15_k4.npz; peak RSS=81.4 MB.

6 block batch 34: n=16, k=2, partitions 1–8/8, min Psi=3.5527136788005e-15; full values saved in block_batches/batch_00033_n16_k2.npz; peak RSS=81.5 MB.

6 block batch 35: n=16, k=3, partitions 1–21/21, min Psi=1.05515596260375e-12; full values saved in block_batches/batch_00034_n16_k3.npz; peak RSS=81.5 MB.

6 block batch 36: n=16, k=4, partitions 1–34/34, min Psi=3.03757019537443e-13; full values saved in block_batches/batch_00035_n16_k4.npz; peak RSS=82.3 MB.

6 block batch 37: n=17, k=2, partitions 1–8/8, min Psi=-1.06581410364015e-14; full values saved in block_batches/batch_00036_n17_k2.npz; peak RSS=82.3 MB.

6 block batch 38: n=17, k=3, partitions 1–24/24, min Psi=-3.5527136788005e-15; full values saved in block_batches/batch_00037_n17_k3.npz; peak RSS=82.3 MB.

6 block batch 39: n=17, k=4, partitions 1–39/39, min Psi=2.1476154188349e-12; full values saved in block_batches/batch_00038_n17_k4.npz; peak RSS=82.7 MB.

6 block batch 40: n=18, k=2, partitions 1–9/9, min Psi=5.32907051820075e-15; full values saved in block_batches/batch_00039_n18_k2.npz; peak RSS=82.7 MB.

6 block batch 41: n=18, k=3, partitions 1–27/27, min Psi=5.50670620214078e-14; full values saved in block_batches/batch_00040_n18_k3.npz; peak RSS=82.8 MB.

6 block batch 42: n=18, k=4, partitions 1–47/47, min Psi=1.77635683940025e-15; full values saved in block_batches/batch_00041_n18_k4.npz; peak RSS=83.1 MB.

6 block batch 43: n=19, k=2, partitions 1–9/9, min Psi=-1.59872115546023e-14; full values saved in block_batches/batch_00042_n19_k2.npz; peak RSS=83.1 MB.

6 block batch 44: n=19, k=3, partitions 1–30/30, min Psi=7.105427357601e-15; full values saved in block_batches/batch_00043_n19_k3.npz; peak RSS=83.1 MB.

6 block batch 45: n=19, k=4, partitions 1–54/54, min Psi=-2.8421709430404e-14; full values saved in block_batches/batch_00044_n19_k4.npz; peak RSS=83.5 MB.

6 block batch 46: n=20, k=2, partitions 1–10/10, min Psi=-2.48689957516035e-14; full values saved in block_batches/batch_00045_n20_k2.npz; peak RSS=83.6 MB.

6 block batch 47: n=20, k=3, partitions 1–33/33, min Psi=4.68958205601666e-13; full values saved in block_batches/batch_00046_n20_k3.npz; peak RSS=83.6 MB.

6 block batch 48: n=20, k=4, partitions 1–64/64, min Psi=-2.1316282072803e-14; full values saved in block_batches/batch_00047_n20_k4.npz; peak RSS=84.3 MB.

6 block batch 49: n=21, k=2, partitions 1–10/10, min Psi=-1.4210854715202e-14; full values saved in block_batches/batch_00048_n21_k2.npz; peak RSS=84.3 MB.

6 block batch 50: n=21, k=3, partitions 1–37/37, min Psi=3.5527136788005e-15; full values saved in block_batches/batch_00049_n21_k3.npz; peak RSS=84.3 MB.

6 block batch 51: n=21, k=4, partitions 1–72/72, min Psi=-2.8421709430404e-14; full values saved in block_batches/batch_00050_n21_k4.npz; peak RSS=84.6 MB.

6 block batch 52: n=22, k=2, partitions 1–11/11, min Psi=7.105427357601e-15; full values saved in block_batches/batch_00051_n22_k2.npz; peak RSS=84.6 MB.

6 block batch 53: n=22, k=3, partitions 1–40/40, min Psi=1.22923893286497e-12; full values saved in block_batches/batch_00052_n22_k3.npz; peak RSS=84.6 MB.

6 block batch 54: n=22, k=4, partitions 1–84/84, min Psi=-2.1316282072803e-14; full values saved in block_batches/batch_00053_n22_k4.npz; peak RSS=85.3 MB.

6 block batch 55: n=23, k=2, partitions 1–11/11, min Psi=-6.03961325396085e-14; full values saved in block_batches/batch_00054_n23_k2.npz; peak RSS=85.3 MB.

6 block batch 56: n=23, k=3, partitions 1–44/44, min Psi=0; full values saved in block_batches/batch_00055_n23_k3.npz; peak RSS=85.3 MB.

6 block batch 57: n=23, k=4, partitions 1–94/94, min Psi=-3.90798504668055e-14; full values saved in block_batches/batch_00056_n23_k4.npz; peak RSS=86.3 MB.

6 block batch 58: n=24, k=2, partitions 1–12/12, min Psi=-7.105427357601e-15; full values saved in block_batches/batch_00057_n24_k2.npz; peak RSS=86.3 MB.

6 block batch 59: n=24, k=3, partitions 1–48/48, min Psi=2.22399876292911e-11; full values saved in block_batches/batch_00058_n24_k3.npz; peak RSS=86.3 MB.

6 block batch 60: n=24, k=4, partitions 1–108/108, min Psi=-3.19744231092045e-14; full values saved in block_batches/batch_00059_n24_k4.npz; peak RSS=86.7 MB.

6 block batch 61: n=25, k=2, partitions 1–12/12, min Psi=0; full values saved in block_batches/batch_00060_n25_k2.npz; peak RSS=86.7 MB.

6 block batch 62: n=25, k=3, partitions 1–52/52, min Psi=7.105427357601e-15; full values saved in block_batches/batch_00061_n25_k3.npz; peak RSS=86.7 MB.

6 block batch 63: n=25, k=4, partitions 1–120/120, min Psi=-4.61852778244065e-14; full values saved in block_batches/batch_00062_n25_k4.npz; peak RSS=87.8 MB.

6 block batch 64: n=26, k=2, partitions 1–13/13, min Psi=-1.77635683940025e-14; full values saved in block_batches/batch_00063_n26_k2.npz; peak RSS=87.8 MB.

6 block batch 65: n=26, k=3, partitions 1–56/56, min Psi=1.13416831482027e-10; full values saved in block_batches/batch_00064_n26_k3.npz; peak RSS=87.8 MB.

6 block batch 66: n=26, k=4, partitions 1–136/136, min Psi=-2.8421709430404e-14; full values saved in block_batches/batch_00065_n26_k4.npz; peak RSS=89.3 MB.

6 block batch 67: n=27, k=2, partitions 1–13/13, min Psi=-1.06581410364015e-14; full values saved in block_batches/batch_00066_n27_k2.npz; peak RSS=89.3 MB.

6 block batch 68: n=27, k=3, partitions 1–61/61, min Psi=-2.48689957516035e-14; full values saved in block_batches/batch_00067_n27_k3.npz; peak RSS=89.4 MB.

6 block batch 69: n=27, k=4, partitions 1–150/150, min Psi=-3.5527136788005e-14; full values saved in block_batches/batch_00068_n27_k4.npz; peak RSS=90.2 MB.

6 block batch 70: n=28, k=2, partitions 1–14/14, min Psi=-2.1316282072803e-14; full values saved in block_batches/batch_00069_n28_k2.npz; peak RSS=90.2 MB.

6 block batch 71: n=28, k=3, partitions 1–65/65, min Psi=5.16600096034381e-11; full values saved in block_batches/batch_00070_n28_k3.npz; peak RSS=90.2 MB.

6 block batch 72: n=28, k=4, partitions 1–169/169, min Psi=-2.48689957516035e-14; full values saved in block_batches/batch_00071_n28_k4.npz; peak RSS=90.5 MB.

6 block batch 73: n=29, k=2, partitions 1–14/14, min Psi=0; full values saved in block_batches/batch_00072_n29_k2.npz; peak RSS=90.5 MB.

6 block batch 74: n=29, k=3, partitions 1–70/70, min Psi=4.2632564145606e-14; full values saved in block_batches/batch_00073_n29_k3.npz; peak RSS=90.5 MB.

6 block batch 75: n=29, k=4, partitions 1–185/185, min Psi=-3.90798504668055e-14; full values saved in block_batches/batch_00074_n29_k4.npz; peak RSS=92.9 MB.

6 block batch 76: n=30, k=2, partitions 1–15/15, min Psi=-6.3948846218409e-14; full values saved in block_batches/batch_00075_n30_k2.npz; peak RSS=92.9 MB.

6 block batch 77: n=30, k=3, partitions 1–75/75, min Psi=2.82405210327852e-11; full values saved in block_batches/batch_00076_n30_k3.npz; peak RSS=92.9 MB.

6 block batch 78: n=30, k=4, partitions 1–206/206, min Psi=-7.46069872548105e-14; full values saved in block_batches/batch_00077_n30_k4.npz; peak RSS=93.7 MB.

6 block batch 79: n=31, k=2, partitions 1–15/15, min Psi=-2.1316282072803e-14; full values saved in block_batches/batch_00078_n31_k2.npz; peak RSS=93.7 MB.

6 block batch 80: n=31, k=3, partitions 1–80/80, min Psi=1.06581410364015e-14; full values saved in block_batches/batch_00079_n31_k3.npz; peak RSS=93.7 MB.

6 block batch 81: n=31, k=4, partitions 1–225/225, min Psi=-1.77635683940025e-14; full values saved in block_batches/batch_00080_n31_k4.npz; peak RSS=95.8 MB.

6 block batch 82: n=32, k=2, partitions 1–16/16, min Psi=-4.9737991503207e-14; full values saved in block_batches/batch_00081_n32_k2.npz; peak RSS=95.8 MB.

6 block batch 83: n=32, k=3, partitions 1–85/85, min Psi=3.06968672703078e-10; full values saved in block_batches/batch_00082_n32_k3.npz; peak RSS=95.8 MB.

6 block batch 84: n=32, k=4, partitions 1–249/249, min Psi=-7.46069872548105e-14; full values saved in block_batches/batch_00083_n32_k4.npz; peak RSS=97.4 MB.

6 block batch 85: n=33, k=2, partitions 1–16/16, min Psi=-2.1316282072803e-14; full values saved in block_batches/batch_00084_n33_k2.npz; peak RSS=97.4 MB.

6 block batch 86: n=33, k=3, partitions 1–91/91, min Psi=7.105427357601e-15; full values saved in block_batches/batch_00085_n33_k3.npz; peak RSS=97.4 MB.

6 block batch 87: n=33, k=4, partitions 1–256/270, min Psi=-4.9737991503207e-14; full values saved in block_batches/batch_00086_n33_k4.npz; peak RSS=99.1 MB.

6 block batch 88: n=33, k=4, partitions 257–270/270, min Psi=895.849724602106; full values saved in block_batches/batch_00087_n33_k4.npz; peak RSS=99.1 MB.

6 block batch 89: n=34, k=2, partitions 1–17/17, min Psi=-1.06581410364015e-14; full values saved in block_batches/batch_00088_n34_k2.npz; peak RSS=99.1 MB.

6 block batch 90: n=34, k=3, partitions 1–96/96, min Psi=7.17292891749821e-12; full values saved in block_batches/batch_00089_n34_k3.npz; peak RSS=99.1 MB.

6 block batch 91: n=34, k=4, partitions 1–256/297, min Psi=-7.105427357601e-14; full values saved in block_batches/batch_00090_n34_k4.npz; peak RSS=100.4 MB.

6 block batch 92: n=34, k=4, partitions 257–297/297, min Psi=903.529411764765; full values saved in block_batches/batch_00091_n34_k4.npz; peak RSS=100.5 MB.

6 block batch 93: n=35, k=2, partitions 1–17/17, min Psi=-3.19744231092045e-14; full values saved in block_batches/batch_00092_n35_k2.npz; peak RSS=100.5 MB.

6 block batch 94: n=35, k=3, partitions 1–102/102, min Psi=2.8421709430404e-14; full values saved in block_batches/batch_00093_n35_k3.npz; peak RSS=100.5 MB.

6 block batch 95: n=35, k=4, partitions 1–256/321, min Psi=-1.27897692436818e-13; full values saved in block_batches/batch_00094_n35_k4.npz; peak RSS=100.5 MB.

6 block batch 96: n=35, k=4, partitions 257–321/321, min Psi=1016.92555141398; full values saved in block_batches/batch_00095_n35_k4.npz; peak RSS=100.5 MB.

6 block batch 97: n=36, k=2, partitions 1–18/18, min Psi=-7.105427357601e-14; full values saved in block_batches/batch_00096_n36_k2.npz; peak RSS=100.5 MB.

6 block batch 98: n=36, k=3, partitions 1–108/108, min Psi=3.23979065797175e-10; full values saved in block_batches/batch_00097_n36_k3.npz; peak RSS=100.5 MB.

6 block batch 99: n=36, k=4, partitions 1–256/351, min Psi=-7.8159700933611e-14; full values saved in block_batches/batch_00098_n36_k4.npz; peak RSS=100.9 MB.

6 block batch 100: n=36, k=4, partitions 257–351/351, min Psi=1027.55555555556; full values saved in block_batches/batch_00099_n36_k4.npz; peak RSS=100.9 MB.

6 block batch 101: n=37, k=2, partitions 1–18/18, min Psi=0; full values saved in block_batches/batch_00100_n37_k2.npz; peak RSS=100.9 MB.

6 block batch 102: n=37, k=3, partitions 1–114/114, min Psi=7.105427357601e-14; full values saved in block_batches/batch_00101_n37_k3.npz; peak RSS=100.9 MB.

6 block batch 103: n=37, k=4, partitions 1–256/378, min Psi=-3.5527136788005e-14; full values saved in block_batches/batch_00102_n37_k4.npz; peak RSS=100.9 MB.

6 block batch 104: n=37, k=4, partitions 257–378/378, min Psi=1148.4333802084; full values saved in block_batches/batch_00103_n37_k4.npz; peak RSS=100.9 MB.

6 block batch 105: n=38, k=2, partitions 1–19/19, min Psi=0; full values saved in block_batches/batch_00104_n38_k2.npz; peak RSS=100.9 MB.

6 block batch 106: n=38, k=3, partitions 1–120/120, min Psi=5.11604980601987e-10; full values saved in block_batches/batch_00105_n38_k3.npz; peak RSS=100.9 MB.

6 block batch 107: n=38, k=4, partitions 1–256/411, min Psi=-9.2370555648813e-14; full values saved in block_batches/batch_00106_n38_k4.npz; peak RSS=100.9 MB.

6 block batch 108: n=38, k=4, partitions 257–411/411, min Psi=1159.57894736842; full values saved in block_batches/batch_00107_n38_k4.npz; peak RSS=101.0 MB.

6 block batch 109: n=39, k=2, partitions 1–19/19, min Psi=-5.6843418860808e-14; full values saved in block_batches/batch_00108_n39_k2.npz; peak RSS=101.0 MB.

6 block batch 110: n=39, k=3, partitions 1–127/127, min Psi=-4.2632564145606e-14; full values saved in block_batches/batch_00109_n39_k3.npz; peak RSS=101.0 MB.

6 block batch 111: n=39, k=4, partitions 1–256/441, min Psi=-5.6843418860808e-14; full values saved in block_batches/batch_00110_n39_k4.npz; peak RSS=101.8 MB.

6 block batch 112: n=39, k=4, partitions 257–441/441, min Psi=1285.0097751154; full values saved in block_batches/batch_00111_n39_k4.npz; peak RSS=101.8 MB.

6 block batch 113: n=40, k=2, partitions 1–20/20, min Psi=1.4210854715202e-14; full values saved in block_batches/batch_00112_n40_k2.npz; peak RSS=101.8 MB.

6 block batch 114: n=40, k=3, partitions 1–133/133, min Psi=2.05709227429907e-10; full values saved in block_batches/batch_00113_n40_k3.npz; peak RSS=101.8 MB.

6 block batch 115: n=40, k=4, partitions 1–256/478, min Psi=-5.6843418860808e-14; full values saved in block_batches/batch_00114_n40_k4.npz; peak RSS=101.8 MB.

6 block batch 116: n=40, k=4, partitions 257–478/478, min Psi=1299.6; full values saved in block_batches/batch_00115_n40_k4.npz; peak RSS=101.8 MB.

6 block batch 117: n=64, k=2, partitions 1–32/32, min Psi=2.1316282072803e-14; full values saved in block_batches/batch_00116_n64_k2.npz; peak RSS=101.8 MB.

6 block batch 118: n=64, k=3, partitions 1–256/341, min Psi=7.6468609222502e-11; full values saved in block_batches/batch_00117_n64_k3.npz; peak RSS=101.8 MB.

6 block batch 119: n=64, k=3, partitions 257–341/341, min Psi=3603.75; full values saved in block_batches/batch_00118_n64_k3.npz; peak RSS=101.9 MB.

6 block batch 120: n=64, k=4, partitions 1–256/1906, min Psi=-2.62900812231237e-13; full values saved in block_batches/batch_00119_n64_k4.npz; peak RSS=101.9 MB.

6 block batch 121: n=64, k=4, partitions 257–512/1906, min Psi=-2.27373675443232e-13; full values saved in block_batches/batch_00120_n64_k4.npz; peak RSS=102.1 MB.

6 block batch 122: n=64, k=4, partitions 513–768/1906, min Psi=3603.75; full values saved in block_batches/batch_00121_n64_k4.npz; peak RSS=102.9 MB.

6 block batch 123: n=64, k=4, partitions 769–1024/1906, min Psi=3603.75; full values saved in block_batches/batch_00122_n64_k4.npz; peak RSS=102.9 MB.

6 block batch 124: n=64, k=4, partitions 1025–1280/1906, min Psi=3603.75; full values saved in block_batches/batch_00123_n64_k4.npz; peak RSS=102.9 MB.

6 block batch 125: n=64, k=4, partitions 1281–1536/1906, min Psi=3603.75; full values saved in block_batches/batch_00124_n64_k4.npz; peak RSS=102.9 MB.

6 block batch 126: n=64, k=4, partitions 1537–1792/1906, min Psi=3603.75; full values saved in block_batches/batch_00125_n64_k4.npz; peak RSS=103.2 MB.

6 block batch 127: n=64, k=4, partitions 1793–1906/1906, min Psi=3603.75; full values saved in block_batches/batch_00126_n64_k4.npz; peak RSS=103.2 MB.

6 block batch 128: n=100, k=2, partitions 1–50/50, min Psi=-1.98951966012828e-13; full values saved in block_batches/batch_00127_n100_k2.npz; peak RSS=103.2 MB.

6 block batch 129: n=100, k=3, partitions 1–256/833, min Psi=4.681481868829e-10; full values saved in block_batches/batch_00128_n100_k3.npz; peak RSS=103.2 MB.

6 block batch 130: n=100, k=3, partitions 257–512/833, min Psi=9219.84000003689; full values saved in block_batches/batch_00129_n100_k3.npz; peak RSS=103.2 MB.

6 block batch 131: n=100, k=3, partitions 513–768/833, min Psi=9219.84000001281; full values saved in block_batches/batch_00130_n100_k3.npz; peak RSS=103.2 MB.

6 block batch 132: n=100, k=3, partitions 769–833/833, min Psi=9219.84; full values saved in block_batches/batch_00131_n100_k3.npz; peak RSS=103.2 MB.

6 block batch 133: n=100, k=4, partitions 1–256/7153, min Psi=-3.83693077310454e-13; full values saved in block_batches/batch_00132_n100_k4.npz; peak RSS=103.5 MB.

6 block batch 134: n=100, k=4, partitions 257–512/7153, min Psi=1.43671741170692e-11; full values saved in block_batches/batch_00133_n100_k4.npz; peak RSS=104.1 MB.

6 block batch 135: n=100, k=4, partitions 513–768/7153, min Psi=-5.40012479177676e-13; full values saved in block_batches/batch_00134_n100_k4.npz; peak RSS=104.1 MB.

6 block batch 136: n=100, k=4, partitions 769–1024/7153, min Psi=-5.40012479177676e-13; full values saved in block_batches/batch_00135_n100_k4.npz; peak RSS=104.1 MB.

6 block batch 137: n=100, k=4, partitions 1025–1280/7153, min Psi=9219.84; full values saved in block_batches/batch_00136_n100_k4.npz; peak RSS=104.1 MB.

6 block batch 138: n=100, k=4, partitions 1281–1536/7153, min Psi=9219.84000000001; full values saved in block_batches/batch_00137_n100_k4.npz; peak RSS=104.1 MB.

6 block batch 139: n=100, k=4, partitions 1537–1792/7153, min Psi=9219.84; full values saved in block_batches/batch_00138_n100_k4.npz; peak RSS=105.0 MB.

6 block batch 140: n=100, k=4, partitions 1793–2048/7153, min Psi=9219.84; full values saved in block_batches/batch_00139_n100_k4.npz; peak RSS=106.6 MB.

6 block batch 141: n=100, k=4, partitions 2049–2304/7153, min Psi=9219.84; full values saved in block_batches/batch_00140_n100_k4.npz; peak RSS=106.6 MB.

6 block batch 142: n=100, k=4, partitions 2305–2560/7153, min Psi=9219.84; full values saved in block_batches/batch_00141_n100_k4.npz; peak RSS=106.8 MB.

6 block batch 143: n=100, k=4, partitions 2561–2816/7153, min Psi=9219.84; full values saved in block_batches/batch_00142_n100_k4.npz; peak RSS=107.7 MB.

6 block batch 144: n=100, k=4, partitions 2817–3072/7153, min Psi=9219.84; full values saved in block_batches/batch_00143_n100_k4.npz; peak RSS=107.7 MB.

6 block batch 145: n=100, k=4, partitions 3073–3328/7153, min Psi=9219.83999999999; full values saved in block_batches/batch_00144_n100_k4.npz; peak RSS=107.7 MB.

6 block batch 146: n=100, k=4, partitions 3329–3584/7153, min Psi=9219.84; full values saved in block_batches/batch_00145_n100_k4.npz; peak RSS=107.7 MB.

6 block batch 147: n=100, k=4, partitions 3585–3840/7153, min Psi=9219.84; full values saved in block_batches/batch_00146_n100_k4.npz; peak RSS=108.6 MB.

6 block batch 148: n=100, k=4, partitions 3841–4096/7153, min Psi=9219.84; full values saved in block_batches/batch_00147_n100_k4.npz; peak RSS=108.8 MB.

6 block batch 149: n=100, k=4, partitions 4097–4352/7153, min Psi=9219.84; full values saved in block_batches/batch_00148_n100_k4.npz; peak RSS=108.8 MB.

6 block batch 150: n=100, k=4, partitions 4353–4608/7153, min Psi=9219.84; full values saved in block_batches/batch_00149_n100_k4.npz; peak RSS=109.0 MB.

6 block batch 151: n=100, k=4, partitions 4609–4864/7153, min Psi=9219.84; full values saved in block_batches/batch_00150_n100_k4.npz; peak RSS=109.0 MB.

6 block batch 152: n=100, k=4, partitions 4865–5120/7153, min Psi=9219.84; full values saved in block_batches/batch_00151_n100_k4.npz; peak RSS=109.0 MB.

6 block batch 153: n=100, k=4, partitions 5121–5376/7153, min Psi=9219.84; full values saved in block_batches/batch_00152_n100_k4.npz; peak RSS=109.0 MB.

6 block batch 154: n=100, k=4, partitions 5377–5632/7153, min Psi=9219.84; full values saved in block_batches/batch_00153_n100_k4.npz; peak RSS=109.9 MB.

6 block batch 155: n=100, k=4, partitions 5633–5888/7153, min Psi=9219.84; full values saved in block_batches/batch_00154_n100_k4.npz; peak RSS=109.9 MB.

6 block batch 156: n=100, k=4, partitions 5889–6144/7153, min Psi=9219.84; full values saved in block_batches/batch_00155_n100_k4.npz; peak RSS=109.9 MB.

6 block batch 157: n=100, k=4, partitions 6145–6400/7153, min Psi=9219.84; full values saved in block_batches/batch_00156_n100_k4.npz; peak RSS=109.9 MB.

6 block batch 158: n=100, k=4, partitions 6401–6656/7153, min Psi=9219.84; full values saved in block_batches/batch_00157_n100_k4.npz; peak RSS=109.9 MB.

6 block batch 159: n=100, k=4, partitions 6657–6912/7153, min Psi=9219.84; full values saved in block_batches/batch_00158_n100_k4.npz; peak RSS=110.8 MB.

6 block batch 160: n=100, k=4, partitions 6913–7153/7153, min Psi=9219.84; full values saved in block_batches/batch_00159_n100_k4.npz; peak RSS=110.8 MB.

6 block batch 161: n=257, k=2, partitions 1–128/128, min Psi=-3.97903932025656e-13; full values saved in block_batches/batch_00160_n257_k2.npz; peak RSS=110.8 MB.

6 block batch 162: n=257, k=3, partitions 1–256/5504, min Psi=-3.97903932025656e-13; full values saved in block_batches/batch_00161_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 163: n=257, k=3, partitions 257–512/5504, min Psi=64432.4296453018; full values saved in block_batches/batch_00162_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 164: n=257, k=3, partitions 513–768/5504, min Psi=64466.2201545809; full values saved in block_batches/batch_00163_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 165: n=257, k=3, partitions 769–1024/5504, min Psi=64480.7120391488; full values saved in block_batches/batch_00164_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 166: n=257, k=3, partitions 1025–1280/5504, min Psi=64488.7657322636; full values saved in block_batches/batch_00165_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 167: n=257, k=3, partitions 1281–1536/5504, min Psi=64493.8917925164; full values saved in block_batches/batch_00166_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 168: n=257, k=3, partitions 1537–1792/5504, min Psi=64497.4410508256; full values saved in block_batches/batch_00167_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 169: n=257, k=3, partitions 1793–2048/5504, min Psi=64501.1016065215; full values saved in block_batches/batch_00168_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 170: n=257, k=3, partitions 2049–2304/5504, min Psi=64502.8642350902; full values saved in block_batches/batch_00169_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 171: n=257, k=3, partitions 2305–2560/5504, min Psi=64504.8787778731; full values saved in block_batches/batch_00170_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 172: n=257, k=3, partitions 2561–2816/5504, min Psi=64506.3897624128; full values saved in block_batches/batch_00171_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 173: n=257, k=3, partitions 2817–3072/5504, min Psi=64507.2033966065; full values saved in block_batches/batch_00172_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 174: n=257, k=3, partitions 3073–3328/5504, min Psi=64508.2134521774; full values saved in block_batches/batch_00173_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 175: n=257, k=3, partitions 3329–3584/5504, min Psi=64509.0341440817; full values saved in block_batches/batch_00174_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 176: n=257, k=3, partitions 3585–3840/5504, min Psi=64509.9156496975; full values saved in block_batches/batch_00175_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 177: n=257, k=3, partitions 3841–4096/5504, min Psi=64510.458125873; full values saved in block_batches/batch_00176_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 178: n=257, k=3, partitions 4097–4352/5504, min Psi=64511.0636908386; full values saved in block_batches/batch_00177_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 179: n=257, k=3, partitions 4353–4608/5504, min Psi=64511.5661888245; full values saved in block_batches/batch_00178_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 180: n=257, k=3, partitions 4609–4864/5504, min Psi=64512.0856060942; full values saved in block_batches/batch_00179_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 181: n=257, k=3, partitions 4865–5120/5504, min Psi=64512.59070104; full values saved in block_batches/batch_00180_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 182: n=257, k=3, partitions 5121–5376/5504, min Psi=64513.0010966494; full values saved in block_batches/batch_00181_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 183: n=257, k=3, partitions 5377–5504/5504, min Psi=82513.591752083; full values saved in block_batches/batch_00182_n257_k3.npz; peak RSS=110.8 MB.

6 block batch 184: n=257, k=4, partitions 1–256/119239, min Psi=-1.73372427525464e-12; full values saved in block_batches/batch_00183_n257_k4.npz; peak RSS=111.7 MB.

6 block batch 185: n=257, k=4, partitions 257–512/119239, min Psi=-1.4210854715202e-12; full values saved in block_batches/batch_00184_n257_k4.npz; peak RSS=118.5 MB.

6 block batch 186: n=257, k=4, partitions 513–768/119239, min Psi=-2.1316282072803e-12; full values saved in block_batches/batch_00185_n257_k4.npz; peak RSS=118.5 MB.

6 block batch 187: n=257, k=4, partitions 769–1024/119239, min Psi=3.95061761082616e-11; full values saved in block_batches/batch_00186_n257_k4.npz; peak RSS=118.9 MB.

6 block batch 188: n=257, k=4, partitions 1025–1280/119239, min Psi=-1.79056769411545e-12; full values saved in block_batches/batch_00187_n257_k4.npz; peak RSS=119.0 MB.

6 block batch 189: n=257, k=4, partitions 1281–1536/119239, min Psi=1.14823706098832e-11; full values saved in block_batches/batch_00188_n257_k4.npz; peak RSS=119.0 MB.

6 block batch 190: n=257, k=4, partitions 1537–1792/119239, min Psi=2.8421709430404e-14; full values saved in block_batches/batch_00189_n257_k4.npz; peak RSS=119.0 MB.

6 block batch 191: n=257, k=4, partitions 1793–2048/119239, min Psi=5.47117906535277e-11; full values saved in block_batches/batch_00190_n257_k4.npz; peak RSS=119.0 MB.

6 block batch 192: n=257, k=4, partitions 2049–2304/119239, min Psi=-1.90425453183707e-12; full values saved in block_batches/batch_00191_n257_k4.npz; peak RSS=119.7 MB.

6 block batch 193: n=257, k=4, partitions 2305–2560/119239, min Psi=-1.50635059981141e-12; full values saved in block_batches/batch_00192_n257_k4.npz; peak RSS=120.0 MB.

6 block batch 194: n=257, k=4, partitions 2561–2816/119239, min Psi=2.8421709430404e-14; full values saved in block_batches/batch_00193_n257_k4.npz; peak RSS=120.8 MB.

6 block batch 195: n=257, k=4, partitions 2817–3072/119239, min Psi=3.86535248253495e-11; full values saved in block_batches/batch_00194_n257_k4.npz; peak RSS=120.8 MB.

6 block batch 196: n=257, k=4, partitions 3073–3328/119239, min Psi=-2.18847162614111e-12; full values saved in block_batches/batch_00195_n257_k4.npz; peak RSS=120.8 MB.

6 block batch 197: n=257, k=4, partitions 3329–3584/119239, min Psi=-1.84741111297626e-12; full values saved in block_batches/batch_00196_n257_k4.npz; peak RSS=121.6 MB.

6 block batch 198: n=257, k=4, partitions 3585–3840/119239, min Psi=-1.47792889038101e-12; full values saved in block_batches/batch_00197_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 199: n=257, k=4, partitions 3841–4096/119239, min Psi=-1.4210854715202e-12; full values saved in block_batches/batch_00198_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 200: n=257, k=4, partitions 4097–4352/119239, min Psi=-2.18847162614111e-12; full values saved in block_batches/batch_00199_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 201: n=257, k=4, partitions 4353–4608/119239, min Psi=-1.4210854715202e-12; full values saved in block_batches/batch_00200_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 202: n=257, k=4, partitions 4609–4864/119239, min Psi=-2.07478478841949e-12; full values saved in block_batches/batch_00201_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 203: n=257, k=4, partitions 4865–5120/119239, min Psi=-1.96109795069788e-12; full values saved in block_batches/batch_00202_n257_k4.npz; peak RSS=121.8 MB.

6 block batch 204: n=257, k=4, partitions 5121–5376/119239, min Psi=-1.36424205265939e-12; full values saved in block_batches/batch_00203_n257_k4.npz; peak RSS=122.6 MB.

6 block batch 205: n=257, k=4, partitions 5377–5632/119239, min Psi=-1.36424205265939e-12; full values saved in block_batches/batch_00204_n257_k4.npz; peak RSS=122.6 MB.

6 block batch 206: n=257, k=4, partitions 5633–5888/119239, min Psi=64390.2387591102; full values saved in block_batches/batch_00205_n257_k4.npz; peak RSS=123.4 MB.

6 block batch 207: n=257, k=4, partitions 5889–6144/119239, min Psi=64390.2387591103; full values saved in block_batches/batch_00206_n257_k4.npz; peak RSS=123.4 MB.

6 block batch 208: n=257, k=4, partitions 6145–6400/119239, min Psi=64390.2387591102; full values saved in block_batches/batch_00207_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 209: n=257, k=4, partitions 6401–6656/119239, min Psi=64390.2387591103; full values saved in block_batches/batch_00208_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 210: n=257, k=4, partitions 6657–6912/119239, min Psi=64390.238759111; full values saved in block_batches/batch_00209_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 211: n=257, k=4, partitions 6913–7168/119239, min Psi=64390.2387591715; full values saved in block_batches/batch_00210_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 212: n=257, k=4, partitions 7169–7424/119239, min Psi=64390.2387616989; full values saved in block_batches/batch_00211_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 213: n=257, k=4, partitions 7425–7680/119239, min Psi=64390.2387591113; full values saved in block_batches/batch_00212_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 214: n=257, k=4, partitions 7681–7936/119239, min Psi=64390.2387591102; full values saved in block_batches/batch_00213_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 215: n=257, k=4, partitions 7937–8192/119239, min Psi=64390.2387591202; full values saved in block_batches/batch_00214_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 216: n=257, k=4, partitions 8193–8448/119239, min Psi=64390.2387591108; full values saved in block_batches/batch_00215_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 217: n=257, k=4, partitions 8449–8704/119239, min Psi=64390.2387591113; full values saved in block_batches/batch_00216_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 218: n=257, k=4, partitions 8705–8960/119239, min Psi=64390.2387591246; full values saved in block_batches/batch_00217_n257_k4.npz; peak RSS=123.6 MB.

6 block batch 219: n=257, k=4, partitions 8961–9216/119239, min Psi=64390.2387591125; full values saved in block_batches/batch_00218_n257_k4.npz; peak RSS=124.0 MB.

6 block batch 220: n=257, k=4, partitions 9217–9472/119239, min Psi=64390.2387592067; full values saved in block_batches/batch_00219_n257_k4.npz; peak RSS=124.1 MB.

6 block batch 221: n=257, k=4, partitions 9473–9728/119239, min Psi=64390.2387591427; full values saved in block_batches/batch_00220_n257_k4.npz; peak RSS=124.2 MB.

6 block batch 222: n=257, k=4, partitions 9729–9984/119239, min Psi=64390.2387592191; full values saved in block_batches/batch_00221_n257_k4.npz; peak RSS=125.0 MB.

6 block batch 223: n=257, k=4, partitions 9985–10240/119239, min Psi=64390.2387591249; full values saved in block_batches/batch_00222_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 224: n=257, k=4, partitions 10241–10496/119239, min Psi=64390.2387592604; full values saved in block_batches/batch_00223_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 225: n=257, k=4, partitions 10497–10752/119239, min Psi=71460.8192600187; full values saved in block_batches/batch_00224_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 226: n=257, k=4, partitions 10753–11008/119239, min Psi=64432.4296452817; full values saved in block_batches/batch_00225_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 227: n=257, k=4, partitions 11009–11264/119239, min Psi=64432.4296452817; full values saved in block_batches/batch_00226_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 228: n=257, k=4, partitions 11265–11520/119239, min Psi=64432.4296452818; full values saved in block_batches/batch_00227_n257_k4.npz; peak RSS=126.3 MB.

6 block batch 229: n=257, k=4, partitions 11521–11776/119239, min Psi=64432.4296452818; full values saved in block_batches/batch_00228_n257_k4.npz; peak RSS=126.9 MB.

6 block batch 230: n=257, k=4, partitions 11777–12032/119239, min Psi=64432.4296452818; full values saved in block_batches/batch_00229_n257_k4.npz; peak RSS=127.0 MB.

6 block batch 231: n=257, k=4, partitions 12033–12288/119239, min Psi=64432.4296452929; full values saved in block_batches/batch_00230_n257_k4.npz; peak RSS=127.4 MB.

6 block batch 232: n=257, k=4, partitions 12289–12544/119239, min Psi=64432.4296453408; full values saved in block_batches/batch_00231_n257_k4.npz; peak RSS=127.4 MB.

6 block batch 233: n=257, k=4, partitions 12545–12800/119239, min Psi=64432.4296452846; full values saved in block_batches/batch_00232_n257_k4.npz; peak RSS=127.4 MB.

6 block batch 234: n=257, k=4, partitions 12801–13056/119239, min Psi=64432.429645283; full values saved in block_batches/batch_00233_n257_k4.npz; peak RSS=128.8 MB.

6 block batch 235: n=257, k=4, partitions 13057–13312/119239, min Psi=64432.4296452821; full values saved in block_batches/batch_00234_n257_k4.npz; peak RSS=129.0 MB.

6 block batch 236: n=257, k=4, partitions 13313–13568/119239, min Psi=64432.4296453404; full values saved in block_batches/batch_00235_n257_k4.npz; peak RSS=129.0 MB.

6 block batch 237: n=257, k=4, partitions 13569–13824/119239, min Psi=64432.429645282; full values saved in block_batches/batch_00236_n257_k4.npz; peak RSS=129.0 MB.

6 block batch 238: n=257, k=4, partitions 13825–14080/119239, min Psi=64432.4296452818; full values saved in block_batches/batch_00237_n257_k4.npz; peak RSS=129.0 MB.

6 block batch 239: n=257, k=4, partitions 14081–14336/119239, min Psi=64432.4296452819; full values saved in block_batches/batch_00238_n257_k4.npz; peak RSS=129.2 MB.

6 block batch 240: n=257, k=4, partitions 14337–14592/119239, min Psi=64432.429645448; full values saved in block_batches/batch_00239_n257_k4.npz; peak RSS=129.3 MB.

6 block batch 241: n=257, k=4, partitions 14593–14848/119239, min Psi=64432.4296453413; full values saved in block_batches/batch_00240_n257_k4.npz; peak RSS=129.3 MB.

6 block batch 242: n=257, k=4, partitions 14849–15104/119239, min Psi=64432.4296453318; full values saved in block_batches/batch_00241_n257_k4.npz; peak RSS=129.3 MB.

6 block batch 243: n=257, k=4, partitions 15105–15360/119239, min Psi=64432.4296452819; full values saved in block_batches/batch_00242_n257_k4.npz; peak RSS=129.3 MB.

6 block batch 244: n=257, k=4, partitions 15361–15616/119239, min Psi=64432.4296453073; full values saved in block_batches/batch_00243_n257_k4.npz; peak RSS=129.3 MB.

6 block batch 245: n=257, k=4, partitions 15617–15872/119239, min Psi=69493.2307349779; full values saved in block_batches/batch_00244_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 246: n=257, k=4, partitions 15873–16128/119239, min Psi=64453.5447889693; full values saved in block_batches/batch_00245_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 247: n=257, k=4, partitions 16129–16384/119239, min Psi=64453.5447889694; full values saved in block_batches/batch_00246_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 248: n=257, k=4, partitions 16385–16640/119239, min Psi=64453.5447889694; full values saved in block_batches/batch_00247_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 249: n=257, k=4, partitions 16641–16896/119239, min Psi=64453.5447889693; full values saved in block_batches/batch_00248_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 250: n=257, k=4, partitions 16897–17152/119239, min Psi=64453.5447889695; full values saved in block_batches/batch_00249_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 251: n=257, k=4, partitions 17153–17408/119239, min Psi=64453.5447889779; full values saved in block_batches/batch_00250_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 252: n=257, k=4, partitions 17409–17664/119239, min Psi=64453.5447889704; full values saved in block_batches/batch_00251_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 253: n=257, k=4, partitions 17665–17920/119239, min Psi=64453.544788975; full values saved in block_batches/batch_00252_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 254: n=257, k=4, partitions 17921–18176/119239, min Psi=64453.5447889697; full values saved in block_batches/batch_00253_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 255: n=257, k=4, partitions 18177–18432/119239, min Psi=64453.5447889694; full values saved in block_batches/batch_00254_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 256: n=257, k=4, partitions 18433–18688/119239, min Psi=64453.5447889711; full values saved in block_batches/batch_00255_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 257: n=257, k=4, partitions 18689–18944/119239, min Psi=64453.5447889721; full values saved in block_batches/batch_00256_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 258: n=257, k=4, partitions 18945–19200/119239, min Psi=64453.54478898; full values saved in block_batches/batch_00257_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 259: n=257, k=4, partitions 19201–19456/119239, min Psi=64453.5447889871; full values saved in block_batches/batch_00258_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 260: n=257, k=4, partitions 19457–19712/119239, min Psi=64453.5447889731; full values saved in block_batches/batch_00259_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 261: n=257, k=4, partitions 19713–19968/119239, min Psi=64453.5447890007; full values saved in block_batches/batch_00260_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 262: n=257, k=4, partitions 19969–20224/119239, min Psi=64453.5447889742; full values saved in block_batches/batch_00261_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 263: n=257, k=4, partitions 20225–20480/119239, min Psi=64453.5447889729; full values saved in block_batches/batch_00262_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 264: n=257, k=4, partitions 20481–20736/119239, min Psi=64453.5447892326; full values saved in block_batches/batch_00263_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 265: n=257, k=4, partitions 20737–20992/119239, min Psi=64466.2201545795; full values saved in block_batches/batch_00264_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 266: n=257, k=4, partitions 20993–21248/119239, min Psi=64466.2201545794; full values saved in block_batches/batch_00265_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 267: n=257, k=4, partitions 21249–21504/119239, min Psi=64466.2201545794; full values saved in block_batches/batch_00266_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 268: n=257, k=4, partitions 21505–21760/119239, min Psi=64466.2201545794; full values saved in block_batches/batch_00267_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 269: n=257, k=4, partitions 21761–22016/119239, min Psi=64466.2201545807; full values saved in block_batches/batch_00268_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 270: n=257, k=4, partitions 22017–22272/119239, min Psi=64466.2201545795; full values saved in block_batches/batch_00269_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 271: n=257, k=4, partitions 22273–22528/119239, min Psi=64466.2201545798; full values saved in block_batches/batch_00270_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 272: n=257, k=4, partitions 22529–22784/119239, min Psi=64466.2201545795; full values saved in block_batches/batch_00271_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 273: n=257, k=4, partitions 22785–23040/119239, min Psi=64466.2201545798; full values saved in block_batches/batch_00272_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 274: n=257, k=4, partitions 23041–23296/119239, min Psi=64466.2201545798; full values saved in block_batches/batch_00273_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 275: n=257, k=4, partitions 23297–23552/119239, min Psi=64466.2201545796; full values saved in block_batches/batch_00274_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 276: n=257, k=4, partitions 23553–23808/119239, min Psi=64466.2201545814; full values saved in block_batches/batch_00275_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 277: n=257, k=4, partitions 23809–24064/119239, min Psi=64466.2201545845; full values saved in block_batches/batch_00276_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 278: n=257, k=4, partitions 24065–24320/119239, min Psi=64466.2201545821; full values saved in block_batches/batch_00277_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 279: n=257, k=4, partitions 24321–24576/119239, min Psi=64466.2201545824; full values saved in block_batches/batch_00278_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 280: n=257, k=4, partitions 24577–24832/119239, min Psi=64466.2201545803; full values saved in block_batches/batch_00279_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 281: n=257, k=4, partitions 24833–25088/119239, min Psi=64466.2201545824; full values saved in block_batches/batch_00280_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 282: n=257, k=4, partitions 25089–25344/119239, min Psi=64466.2201545807; full values saved in block_batches/batch_00281_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 283: n=257, k=4, partitions 25345–25600/119239, min Psi=67508.3970571662; full values saved in block_batches/batch_00282_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 284: n=257, k=4, partitions 25601–25856/119239, min Psi=64474.6730089686; full values saved in block_batches/batch_00283_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 285: n=257, k=4, partitions 25857–26112/119239, min Psi=64474.6730089686; full values saved in block_batches/batch_00284_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 286: n=257, k=4, partitions 26113–26368/119239, min Psi=64474.6730089687; full values saved in block_batches/batch_00285_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 287: n=257, k=4, partitions 26369–26624/119239, min Psi=64474.6730089688; full values saved in block_batches/batch_00286_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 288: n=257, k=4, partitions 26625–26880/119239, min Psi=64474.6730089686; full values saved in block_batches/batch_00287_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 289: n=257, k=4, partitions 26881–27136/119239, min Psi=64474.6730089687; full values saved in block_batches/batch_00288_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 290: n=257, k=4, partitions 27137–27392/119239, min Psi=64474.67300897; full values saved in block_batches/batch_00289_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 291: n=257, k=4, partitions 27393–27648/119239, min Psi=64474.6730089687; full values saved in block_batches/batch_00290_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 292: n=257, k=4, partitions 27649–27904/119239, min Psi=64474.6730089686; full values saved in block_batches/batch_00291_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 293: n=257, k=4, partitions 27905–28160/119239, min Psi=64474.6730089688; full values saved in block_batches/batch_00292_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 294: n=257, k=4, partitions 28161–28416/119239, min Psi=64474.673008969; full values saved in block_batches/batch_00293_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 295: n=257, k=4, partitions 28417–28672/119239, min Psi=64474.6730089751; full values saved in block_batches/batch_00294_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 296: n=257, k=4, partitions 28673–28928/119239, min Psi=64474.6730089695; full values saved in block_batches/batch_00295_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 297: n=257, k=4, partitions 28929–29184/119239, min Psi=64474.6730089722; full values saved in block_batches/batch_00296_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 298: n=257, k=4, partitions 29185–29440/119239, min Psi=64474.6730089704; full values saved in block_batches/batch_00297_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 299: n=257, k=4, partitions 29441–29696/119239, min Psi=64474.6730089699; full values saved in block_batches/batch_00298_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 300: n=257, k=4, partitions 29697–29952/119239, min Psi=64474.6730089688; full values saved in block_batches/batch_00299_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 301: n=257, k=4, partitions 29953–30208/119239, min Psi=64474.6730089689; full values saved in block_batches/batch_00300_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 302: n=257, k=4, partitions 30209–30464/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00301_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 303: n=257, k=4, partitions 30465–30720/119239, min Psi=64480.7120389685; full values saved in block_batches/batch_00302_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 304: n=257, k=4, partitions 30721–30976/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00303_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 305: n=257, k=4, partitions 30977–31232/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00304_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 306: n=257, k=4, partitions 31233–31488/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00305_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 307: n=257, k=4, partitions 31489–31744/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00306_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 308: n=257, k=4, partitions 31745–32000/119239, min Psi=64480.7120392318; full values saved in block_batches/batch_00307_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 309: n=257, k=4, partitions 32001–32256/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00308_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 310: n=257, k=4, partitions 32257–32512/119239, min Psi=64480.7120389686; full values saved in block_batches/batch_00309_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 311: n=257, k=4, partitions 32513–32768/119239, min Psi=64480.7120389685; full values saved in block_batches/batch_00310_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 312: n=257, k=4, partitions 32769–33024/119239, min Psi=64480.7120389685; full values saved in block_batches/batch_00311_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 313: n=257, k=4, partitions 33025–33280/119239, min Psi=64480.7120389881; full values saved in block_batches/batch_00312_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 314: n=257, k=4, partitions 33281–33536/119239, min Psi=64480.7120389736; full values saved in block_batches/batch_00313_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 315: n=257, k=4, partitions 33537–33792/119239, min Psi=64480.7120389691; full values saved in block_batches/batch_00314_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 316: n=257, k=4, partitions 33793–34048/119239, min Psi=64480.7120389691; full values saved in block_batches/batch_00315_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 317: n=257, k=4, partitions 34049–34304/119239, min Psi=64480.7120389687; full values saved in block_batches/batch_00316_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 318: n=257, k=4, partitions 34305–34560/119239, min Psi=64480.7120389689; full values saved in block_batches/batch_00317_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 319: n=257, k=4, partitions 34561–34816/119239, min Psi=71460.8192600187; full values saved in block_batches/batch_00318_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 320: n=257, k=4, partitions 34817–35072/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00319_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 321: n=257, k=4, partitions 35073–35328/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00320_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 322: n=257, k=4, partitions 35329–35584/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00321_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 323: n=257, k=4, partitions 35585–35840/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00322_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 324: n=257, k=4, partitions 35841–36096/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00323_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 325: n=257, k=4, partitions 36097–36352/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00324_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 326: n=257, k=4, partitions 36353–36608/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00325_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 327: n=257, k=4, partitions 36609–36864/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00326_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 328: n=257, k=4, partitions 36865–37120/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00327_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 329: n=257, k=4, partitions 37121–37376/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00328_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 330: n=257, k=4, partitions 37377–37632/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00329_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 331: n=257, k=4, partitions 37633–37888/119239, min Psi=64485.2420090558; full values saved in block_batches/batch_00330_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 332: n=257, k=4, partitions 37889–38144/119239, min Psi=64485.2420090558; full values saved in block_batches/batch_00331_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 333: n=257, k=4, partitions 38145–38400/119239, min Psi=64485.2420090558; full values saved in block_batches/batch_00332_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 334: n=257, k=4, partitions 38401–38656/119239, min Psi=64485.2420090557; full values saved in block_batches/batch_00333_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 335: n=257, k=4, partitions 38657–38912/119239, min Psi=64485.2420090562; full values saved in block_batches/batch_00334_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 336: n=257, k=4, partitions 38913–39168/119239, min Psi=73404.3718577641; full values saved in block_batches/batch_00335_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 337: n=257, k=4, partitions 39169–39424/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00336_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 338: n=257, k=4, partitions 39425–39680/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00337_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 339: n=257, k=4, partitions 39681–39936/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00338_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 340: n=257, k=4, partitions 39937–40192/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00339_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 341: n=257, k=4, partitions 40193–40448/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00340_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 342: n=257, k=4, partitions 40449–40704/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00341_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 343: n=257, k=4, partitions 40705–40960/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00342_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 344: n=257, k=4, partitions 40961–41216/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00343_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 345: n=257, k=4, partitions 41217–41472/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00344_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 346: n=257, k=4, partitions 41473–41728/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00345_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 347: n=257, k=4, partitions 41729–41984/119239, min Psi=64488.7657322018; full values saved in block_batches/batch_00346_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 348: n=257, k=4, partitions 41985–42240/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00347_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 349: n=257, k=4, partitions 42241–42496/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00348_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 350: n=257, k=4, partitions 42497–42752/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00349_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 351: n=257, k=4, partitions 42753–43008/119239, min Psi=64488.7657322017; full values saved in block_batches/batch_00350_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 352: n=257, k=4, partitions 43009–43264/119239, min Psi=65512.8559955656; full values saved in block_batches/batch_00351_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 353: n=257, k=4, partitions 43265–43520/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00352_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 354: n=257, k=4, partitions 43521–43776/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00353_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 355: n=257, k=4, partitions 43777–44032/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00354_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 356: n=257, k=4, partitions 44033–44288/119239, min Psi=64491.5849708086; full values saved in block_batches/batch_00355_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 357: n=257, k=4, partitions 44289–44544/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00356_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 358: n=257, k=4, partitions 44545–44800/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00357_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 359: n=257, k=4, partitions 44801–45056/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00358_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 360: n=257, k=4, partitions 45057–45312/119239, min Psi=64491.5849708086; full values saved in block_batches/batch_00359_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 361: n=257, k=4, partitions 45313–45568/119239, min Psi=64491.5849708085; full values saved in block_batches/batch_00360_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 362: n=257, k=4, partitions 45569–45824/119239, min Psi=64491.5849708087; full values saved in block_batches/batch_00361_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 363: n=257, k=4, partitions 45825–46080/119239, min Psi=64491.5849708087; full values saved in block_batches/batch_00362_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 364: n=257, k=4, partitions 46081–46336/119239, min Psi=64491.5849708086; full values saved in block_batches/batch_00363_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 365: n=257, k=4, partitions 46337–46592/119239, min Psi=64491.5849708086; full values saved in block_batches/batch_00364_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 366: n=257, k=4, partitions 46593–46848/119239, min Psi=64491.5849708087; full values saved in block_batches/batch_00365_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 367: n=257, k=4, partitions 46849–47104/119239, min Psi=64491.5849708087; full values saved in block_batches/batch_00366_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 368: n=257, k=4, partitions 47105–47360/119239, min Psi=69493.2307349778; full values saved in block_batches/batch_00367_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 369: n=257, k=4, partitions 47361–47616/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00368_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 370: n=257, k=4, partitions 47617–47872/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00369_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 371: n=257, k=4, partitions 47873–48128/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00370_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 372: n=257, k=4, partitions 48129–48384/119239, min Psi=64493.8917925288; full values saved in block_batches/batch_00371_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 373: n=257, k=4, partitions 48385–48640/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00372_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 374: n=257, k=4, partitions 48641–48896/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00373_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 375: n=257, k=4, partitions 48897–49152/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00374_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 376: n=257, k=4, partitions 49153–49408/119239, min Psi=64493.8917924595; full values saved in block_batches/batch_00375_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 377: n=257, k=4, partitions 49409–49664/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00376_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 378: n=257, k=4, partitions 49665–49920/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00377_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 379: n=257, k=4, partitions 49921–50176/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00378_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 380: n=257, k=4, partitions 50177–50432/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00379_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 381: n=257, k=4, partitions 50433–50688/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00380_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 382: n=257, k=4, partitions 50689–50944/119239, min Psi=64493.8917924596; full values saved in block_batches/batch_00381_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 383: n=257, k=4, partitions 50945–51200/119239, min Psi=65513.5715661208; full values saved in block_batches/batch_00382_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 384: n=257, k=4, partitions 51201–51456/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00383_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 385: n=257, k=4, partitions 51457–51712/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00384_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 386: n=257, k=4, partitions 51713–51968/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00385_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 387: n=257, k=4, partitions 51969–52224/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00386_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 388: n=257, k=4, partitions 52225–52480/119239, min Psi=64495.8142619601; full values saved in block_batches/batch_00387_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 389: n=257, k=4, partitions 52481–52736/119239, min Psi=64495.8142619601; full values saved in block_batches/batch_00388_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 390: n=257, k=4, partitions 52737–52992/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00389_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 391: n=257, k=4, partitions 52993–53248/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00390_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 392: n=257, k=4, partitions 53249–53504/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00391_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 393: n=257, k=4, partitions 53505–53760/119239, min Psi=64495.8142619601; full values saved in block_batches/batch_00392_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 394: n=257, k=4, partitions 53761–54016/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00393_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 395: n=257, k=4, partitions 54017–54272/119239, min Psi=64495.8142619601; full values saved in block_batches/batch_00394_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 396: n=257, k=4, partitions 54273–54528/119239, min Psi=64495.81426196; full values saved in block_batches/batch_00395_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 397: n=257, k=4, partitions 54529–54784/119239, min Psi=64495.8142619602; full values saved in block_batches/batch_00396_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 398: n=257, k=4, partitions 54785–55040/119239, min Psi=64497.4410507715; full values saved in block_batches/batch_00397_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 399: n=257, k=4, partitions 55041–55296/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00398_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 400: n=257, k=4, partitions 55297–55552/119239, min Psi=64497.4410507715; full values saved in block_batches/batch_00399_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 401: n=257, k=4, partitions 55553–55808/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00400_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 402: n=257, k=4, partitions 55809–56064/119239, min Psi=64497.4410507715; full values saved in block_batches/batch_00401_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 403: n=257, k=4, partitions 56065–56320/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00402_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 404: n=257, k=4, partitions 56321–56576/119239, min Psi=64497.4410507715; full values saved in block_batches/batch_00403_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 405: n=257, k=4, partitions 56577–56832/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00404_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 406: n=257, k=4, partitions 56833–57088/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00405_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 407: n=257, k=4, partitions 57089–57344/119239, min Psi=64497.4410508163; full values saved in block_batches/batch_00406_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 408: n=257, k=4, partitions 57345–57600/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00407_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 409: n=257, k=4, partitions 57601–57856/119239, min Psi=64497.4410507715; full values saved in block_batches/batch_00408_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 410: n=257, k=4, partitions 57857–58112/119239, min Psi=64497.4410507716; full values saved in block_batches/batch_00409_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 411: n=257, k=4, partitions 58113–58368/119239, min Psi=64497.4410507718; full values saved in block_batches/batch_00410_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 412: n=257, k=4, partitions 58369–58624/119239, min Psi=69493.2307349779; full values saved in block_batches/batch_00411_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 413: n=257, k=4, partitions 58625–58880/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00412_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 414: n=257, k=4, partitions 58881–59136/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00413_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 415: n=257, k=4, partitions 59137–59392/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00414_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 416: n=257, k=4, partitions 59393–59648/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00415_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 417: n=257, k=4, partitions 59649–59904/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00416_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 418: n=257, k=4, partitions 59905–60160/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00417_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 419: n=257, k=4, partitions 60161–60416/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00418_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 420: n=257, k=4, partitions 60417–60672/119239, min Psi=64498.8355023414; full values saved in block_batches/batch_00419_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 421: n=257, k=4, partitions 60673–60928/119239, min Psi=64498.8355023415; full values saved in block_batches/batch_00420_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 422: n=257, k=4, partitions 60929–61184/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00421_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 423: n=257, k=4, partitions 61185–61440/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00422_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 424: n=257, k=4, partitions 61441–61696/119239, min Psi=64498.8355023413; full values saved in block_batches/batch_00423_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 425: n=257, k=4, partitions 61697–61952/119239, min Psi=64498.8355023423; full values saved in block_batches/batch_00424_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 426: n=257, k=4, partitions 61953–62208/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00425_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 427: n=257, k=4, partitions 62209–62464/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00426_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 428: n=257, k=4, partitions 62465–62720/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00427_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 429: n=257, k=4, partitions 62721–62976/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00428_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 430: n=257, k=4, partitions 62977–63232/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00429_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 431: n=257, k=4, partitions 63233–63488/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00430_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 432: n=257, k=4, partitions 63489–63744/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00431_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 433: n=257, k=4, partitions 63745–64000/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00432_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 434: n=257, k=4, partitions 64001–64256/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00433_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 435: n=257, k=4, partitions 64257–64512/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00434_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 436: n=257, k=4, partitions 64513–64768/119239, min Psi=64500.044072691; full values saved in block_batches/batch_00435_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 437: n=257, k=4, partitions 64769–65024/119239, min Psi=64500.0440726922; full values saved in block_batches/batch_00436_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 438: n=257, k=4, partitions 65025–65280/119239, min Psi=64500.0440750369; full values saved in block_batches/batch_00437_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 439: n=257, k=4, partitions 65281–65536/119239, min Psi=64501.1016065171; full values saved in block_batches/batch_00438_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 440: n=257, k=4, partitions 65537–65792/119239, min Psi=64501.1016065171; full values saved in block_batches/batch_00439_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 441: n=257, k=4, partitions 65793–66048/119239, min Psi=64501.1016065175; full values saved in block_batches/batch_00440_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 442: n=257, k=4, partitions 66049–66304/119239, min Psi=64501.1016065171; full values saved in block_batches/batch_00441_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 443: n=257, k=4, partitions 66305–66560/119239, min Psi=64501.1016065172; full values saved in block_batches/batch_00442_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 444: n=257, k=4, partitions 66561–66816/119239, min Psi=64501.1016065172; full values saved in block_batches/batch_00443_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 445: n=257, k=4, partitions 66817–67072/119239, min Psi=64501.1016065172; full values saved in block_batches/batch_00444_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 446: n=257, k=4, partitions 67073–67328/119239, min Psi=64501.1016065316; full values saved in block_batches/batch_00445_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 447: n=257, k=4, partitions 67329–67584/119239, min Psi=64501.1016065172; full values saved in block_batches/batch_00446_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 448: n=257, k=4, partitions 67585–67840/119239, min Psi=64501.1016065171; full values saved in block_batches/batch_00447_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 449: n=257, k=4, partitions 67841–68096/119239, min Psi=64501.1016065171; full values saved in block_batches/batch_00448_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 450: n=257, k=4, partitions 68097–68352/119239, min Psi=64501.1016065172; full values saved in block_batches/batch_00449_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 451: n=257, k=4, partitions 68353–68608/119239, min Psi=66512.3476704665; full values saved in block_batches/batch_00450_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 452: n=257, k=4, partitions 68609–68864/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00451_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 453: n=257, k=4, partitions 68865–69120/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00452_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 454: n=257, k=4, partitions 69121–69376/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00453_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 455: n=257, k=4, partitions 69377–69632/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00454_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 456: n=257, k=4, partitions 69633–69888/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00455_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 457: n=257, k=4, partitions 69889–70144/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00456_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 458: n=257, k=4, partitions 70145–70400/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00457_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 459: n=257, k=4, partitions 70401–70656/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00458_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 460: n=257, k=4, partitions 70657–70912/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00459_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 461: n=257, k=4, partitions 70913–71168/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00460_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 462: n=257, k=4, partitions 71169–71424/119239, min Psi=64502.0347515443; full values saved in block_batches/batch_00461_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 463: n=257, k=4, partitions 71425–71680/119239, min Psi=65512.8568178991; full values saved in block_batches/batch_00462_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 464: n=257, k=4, partitions 71681–71936/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00463_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 465: n=257, k=4, partitions 71937–72192/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00464_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 466: n=257, k=4, partitions 72193–72448/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00465_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 467: n=257, k=4, partitions 72449–72704/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00466_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 468: n=257, k=4, partitions 72705–72960/119239, min Psi=64502.8642349944; full values saved in block_batches/batch_00467_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 469: n=257, k=4, partitions 72961–73216/119239, min Psi=64502.8642349944; full values saved in block_batches/batch_00468_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 470: n=257, k=4, partitions 73217–73472/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00469_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 471: n=257, k=4, partitions 73473–73728/119239, min Psi=64502.8642349944; full values saved in block_batches/batch_00470_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 472: n=257, k=4, partitions 73729–73984/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00471_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 473: n=257, k=4, partitions 73985–74240/119239, min Psi=64502.8642349945; full values saved in block_batches/batch_00472_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 474: n=257, k=4, partitions 74241–74496/119239, min Psi=64502.864234995; full values saved in block_batches/batch_00473_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 475: n=257, k=4, partitions 74497–74752/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00474_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 476: n=257, k=4, partitions 74753–75008/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00475_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 477: n=257, k=4, partitions 75009–75264/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00476_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 478: n=257, k=4, partitions 75265–75520/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00477_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 479: n=257, k=4, partitions 75521–75776/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00478_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 480: n=257, k=4, partitions 75777–76032/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00479_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 481: n=257, k=4, partitions 76033–76288/119239, min Psi=64503.6064213119; full values saved in block_batches/batch_00480_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 482: n=257, k=4, partitions 76289–76544/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00481_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 483: n=257, k=4, partitions 76545–76800/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00482_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 484: n=257, k=4, partitions 76801–77056/119239, min Psi=64503.6064213111; full values saved in block_batches/batch_00483_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 485: n=257, k=4, partitions 77057–77312/119239, min Psi=64503.6064215723; full values saved in block_batches/batch_00484_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 486: n=257, k=4, partitions 77313–77568/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00485_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 487: n=257, k=4, partitions 77569–77824/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00486_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 488: n=257, k=4, partitions 77825–78080/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00487_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 489: n=257, k=4, partitions 78081–78336/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00488_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 490: n=257, k=4, partitions 78337–78592/119239, min Psi=64504.2744026523; full values saved in block_batches/batch_00489_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 491: n=257, k=4, partitions 78593–78848/119239, min Psi=64504.274402684; full values saved in block_batches/batch_00490_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 492: n=257, k=4, partitions 78849–79104/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00491_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 493: n=257, k=4, partitions 79105–79360/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00492_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 494: n=257, k=4, partitions 79361–79616/119239, min Psi=64504.2744026522; full values saved in block_batches/batch_00493_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 495: n=257, k=4, partitions 79617–79872/119239, min Psi=64504.2744047227; full values saved in block_batches/batch_00494_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 496: n=257, k=4, partitions 79873–80128/119239, min Psi=64504.2744026523; full values saved in block_batches/batch_00495_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 497: n=257, k=4, partitions 80129–80384/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00496_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 498: n=257, k=4, partitions 80385–80640/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00497_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 499: n=257, k=4, partitions 80641–80896/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00498_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 500: n=257, k=4, partitions 80897–81152/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00499_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 501: n=257, k=4, partitions 81153–81408/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00500_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 502: n=257, k=4, partitions 81409–81664/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00501_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 503: n=257, k=4, partitions 81665–81920/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00502_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 504: n=257, k=4, partitions 81921–82176/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00503_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 505: n=257, k=4, partitions 82177–82432/119239, min Psi=64504.8787778696; full values saved in block_batches/batch_00504_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 506: n=257, k=4, partitions 82433–82688/119239, min Psi=64504.8787778706; full values saved in block_batches/batch_00505_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 507: n=257, k=4, partitions 82689–82944/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00506_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 508: n=257, k=4, partitions 82945–83200/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00507_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 509: n=257, k=4, partitions 83201–83456/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00508_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 510: n=257, k=4, partitions 83457–83712/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00509_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 511: n=257, k=4, partitions 83713–83968/119239, min Psi=64505.4282190739; full values saved in block_batches/batch_00510_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 512: n=257, k=4, partitions 83969–84224/119239, min Psi=64505.4282190738; full values saved in block_batches/batch_00511_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 513: n=257, k=4, partitions 84225–84480/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00512_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 514: n=257, k=4, partitions 84481–84736/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00513_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 515: n=257, k=4, partitions 84737–84992/119239, min Psi=64505.4282190737; full values saved in block_batches/batch_00514_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 516: n=257, k=4, partitions 84993–85248/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00515_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 517: n=257, k=4, partitions 85249–85504/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00516_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 518: n=257, k=4, partitions 85505–85760/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00517_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 519: n=257, k=4, partitions 85761–86016/119239, min Psi=64505.9298904235; full values saved in block_batches/batch_00518_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 520: n=257, k=4, partitions 86017–86272/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00519_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 521: n=257, k=4, partitions 86273–86528/119239, min Psi=64505.9298904237; full values saved in block_batches/batch_00520_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 522: n=257, k=4, partitions 86529–86784/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00521_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 523: n=257, k=4, partitions 86785–87040/119239, min Psi=64505.9298904236; full values saved in block_batches/batch_00522_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 524: n=257, k=4, partitions 87041–87296/119239, min Psi=64505.9298906049; full values saved in block_batches/batch_00523_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 525: n=257, k=4, partitions 87297–87552/119239, min Psi=64505.9298904261; full values saved in block_batches/batch_00524_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 526: n=257, k=4, partitions 87553–87808/119239, min Psi=64506.389762235; full values saved in block_batches/batch_00525_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 527: n=257, k=4, partitions 87809–88064/119239, min Psi=64506.389762235; full values saved in block_batches/batch_00526_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 528: n=257, k=4, partitions 88065–88320/119239, min Psi=64506.3897622351; full values saved in block_batches/batch_00527_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 529: n=257, k=4, partitions 88321–88576/119239, min Psi=64506.3897622351; full values saved in block_batches/batch_00528_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 530: n=257, k=4, partitions 88577–88832/119239, min Psi=64506.3897622351; full values saved in block_batches/batch_00529_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 531: n=257, k=4, partitions 88833–89088/119239, min Psi=64506.389762235; full values saved in block_batches/batch_00530_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 532: n=257, k=4, partitions 89089–89344/119239, min Psi=64506.3897622351; full values saved in block_batches/batch_00531_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 533: n=257, k=4, partitions 89345–89600/119239, min Psi=64506.3897622382; full values saved in block_batches/batch_00532_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 534: n=257, k=4, partitions 89601–89856/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00533_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 535: n=257, k=4, partitions 89857–90112/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00534_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 536: n=257, k=4, partitions 90113–90368/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00535_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 537: n=257, k=4, partitions 90369–90624/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00536_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 538: n=257, k=4, partitions 90625–90880/119239, min Psi=64506.8128497141; full values saved in block_batches/batch_00537_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 539: n=257, k=4, partitions 90881–91136/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00538_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 540: n=257, k=4, partitions 91137–91392/119239, min Psi=64506.8128497142; full values saved in block_batches/batch_00539_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 541: n=257, k=4, partitions 91393–91648/119239, min Psi=64506.8128584392; full values saved in block_batches/batch_00540_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 542: n=257, k=4, partitions 91649–91904/119239, min Psi=64506.8128497143; full values saved in block_batches/batch_00541_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 543: n=257, k=4, partitions 91905–92160/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00542_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 544: n=257, k=4, partitions 92161–92416/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00543_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 545: n=257, k=4, partitions 92417–92672/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00544_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 546: n=257, k=4, partitions 92673–92928/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00545_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 547: n=257, k=4, partitions 92929–93184/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00546_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 548: n=257, k=4, partitions 93185–93440/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00547_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 549: n=257, k=4, partitions 93441–93696/119239, min Psi=64507.2033977741; full values saved in block_batches/batch_00548_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 550: n=257, k=4, partitions 93697–93952/119239, min Psi=64507.2033966062; full values saved in block_batches/batch_00549_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 551: n=257, k=4, partitions 93953–94208/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00550_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 552: n=257, k=4, partitions 94209–94464/119239, min Psi=64507.5650180393; full values saved in block_batches/batch_00551_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 553: n=257, k=4, partitions 94465–94720/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00552_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 554: n=257, k=4, partitions 94721–94976/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00553_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 555: n=257, k=4, partitions 94977–95232/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00554_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 556: n=257, k=4, partitions 95233–95488/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00555_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 557: n=257, k=4, partitions 95489–95744/119239, min Psi=64507.5650180391; full values saved in block_batches/batch_00556_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 558: n=257, k=4, partitions 95745–96000/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00557_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 559: n=257, k=4, partitions 96001–96256/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00558_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 560: n=257, k=4, partitions 96257–96512/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00559_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 561: n=257, k=4, partitions 96513–96768/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00560_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 562: n=257, k=4, partitions 96769–97024/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00561_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 563: n=257, k=4, partitions 97025–97280/119239, min Psi=64507.9008127619; full values saved in block_batches/batch_00562_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 564: n=257, k=4, partitions 97281–97536/119239, min Psi=64507.9008127621; full values saved in block_batches/batch_00563_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 565: n=257, k=4, partitions 97537–97792/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00564_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 566: n=257, k=4, partitions 97793–98048/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00565_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 567: n=257, k=4, partitions 98049–98304/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00566_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 568: n=257, k=4, partitions 98305–98560/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00567_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 569: n=257, k=4, partitions 98561–98816/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00568_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 570: n=257, k=4, partitions 98817–99072/119239, min Psi=64508.2134521643; full values saved in block_batches/batch_00569_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 571: n=257, k=4, partitions 99073–99328/119239, min Psi=64508.2134521645; full values saved in block_batches/batch_00570_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 572: n=257, k=4, partitions 99329–99584/119239, min Psi=64508.5052514997; full values saved in block_batches/batch_00571_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 573: n=257, k=4, partitions 99585–99840/119239, min Psi=64508.5052514943; full values saved in block_batches/batch_00572_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 574: n=257, k=4, partitions 99841–100096/119239, min Psi=64508.5052514943; full values saved in block_batches/batch_00573_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 575: n=257, k=4, partitions 100097–100352/119239, min Psi=64508.5052514943; full values saved in block_batches/batch_00574_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 576: n=257, k=4, partitions 100353–100608/119239, min Psi=64508.5052514943; full values saved in block_batches/batch_00575_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 577: n=257, k=4, partitions 100609–100864/119239, min Psi=64508.5052547306; full values saved in block_batches/batch_00576_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 578: n=257, k=4, partitions 100865–101120/119239, min Psi=64508.5052514943; full values saved in block_batches/batch_00577_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 579: n=257, k=4, partitions 101121–101376/119239, min Psi=64508.7782272938; full values saved in block_batches/batch_00578_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 580: n=257, k=4, partitions 101377–101632/119239, min Psi=64508.7782272938; full values saved in block_batches/batch_00579_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 581: n=257, k=4, partitions 101633–101888/119239, min Psi=64508.7782272938; full values saved in block_batches/batch_00580_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 582: n=257, k=4, partitions 101889–102144/119239, min Psi=64508.7782272938; full values saved in block_batches/batch_00581_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 583: n=257, k=4, partitions 102145–102400/119239, min Psi=64508.7782332528; full values saved in block_batches/batch_00582_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 584: n=257, k=4, partitions 102401–102656/119239, min Psi=64508.778227294; full values saved in block_batches/batch_00583_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 585: n=257, k=4, partitions 102657–102912/119239, min Psi=64509.034144066; full values saved in block_batches/batch_00584_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 586: n=257, k=4, partitions 102913–103168/119239, min Psi=64509.034144066; full values saved in block_batches/batch_00585_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 587: n=257, k=4, partitions 103169–103424/119239, min Psi=64509.034144066; full values saved in block_batches/batch_00586_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 588: n=257, k=4, partitions 103425–103680/119239, min Psi=64509.034144347; full values saved in block_batches/batch_00587_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 589: n=257, k=4, partitions 103681–103936/119239, min Psi=64509.034144066; full values saved in block_batches/batch_00588_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 590: n=257, k=4, partitions 103937–104192/119239, min Psi=64509.2745524585; full values saved in block_batches/batch_00589_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 591: n=257, k=4, partitions 104193–104448/119239, min Psi=64509.2745524585; full values saved in block_batches/batch_00590_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 592: n=257, k=4, partitions 104449–104704/119239, min Psi=64509.2745524585; full values saved in block_batches/batch_00591_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 593: n=257, k=4, partitions 104705–104960/119239, min Psi=64509.2745524585; full values saved in block_batches/batch_00592_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 594: n=257, k=4, partitions 104961–105216/119239, min Psi=64509.274554804; full values saved in block_batches/batch_00593_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 595: n=257, k=4, partitions 105217–105472/119239, min Psi=64509.2745524586; full values saved in block_batches/batch_00594_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 596: n=257, k=4, partitions 105473–105728/119239, min Psi=64509.5008207099; full values saved in block_batches/batch_00595_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 597: n=257, k=4, partitions 105729–105984/119239, min Psi=64509.5008207099; full values saved in block_batches/batch_00596_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 598: n=257, k=4, partitions 105985–106240/119239, min Psi=64509.5008207099; full values saved in block_batches/batch_00597_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 599: n=257, k=4, partitions 106241–106496/119239, min Psi=64509.500822088; full values saved in block_batches/batch_00598_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 600: n=257, k=4, partitions 106497–106752/119239, min Psi=64509.5008207101; full values saved in block_batches/batch_00599_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 601: n=257, k=4, partitions 106753–107008/119239, min Psi=64509.7141607048; full values saved in block_batches/batch_00600_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 602: n=257, k=4, partitions 107009–107264/119239, min Psi=64509.7141607049; full values saved in block_batches/batch_00601_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 603: n=257, k=4, partitions 107265–107520/119239, min Psi=64509.7141612958; full values saved in block_batches/batch_00602_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 604: n=257, k=4, partitions 107521–107776/119239, min Psi=64509.7141607067; full values saved in block_batches/batch_00603_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 605: n=257, k=4, partitions 107777–108032/119239, min Psi=64509.9156496881; full values saved in block_batches/batch_00604_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 606: n=257, k=4, partitions 108033–108288/119239, min Psi=64509.9156496881; full values saved in block_batches/batch_00605_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 607: n=257, k=4, partitions 108289–108544/119239, min Psi=64509.9156496881; full values saved in block_batches/batch_00606_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 608: n=257, k=4, partitions 108545–108800/119239, min Psi=64509.9156529385; full values saved in block_batches/batch_00607_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 609: n=257, k=4, partitions 108801–109056/119239, min Psi=64509.9156496882; full values saved in block_batches/batch_00608_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 610: n=257, k=4, partitions 109057–109312/119239, min Psi=64510.1062484568; full values saved in block_batches/batch_00609_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 611: n=257, k=4, partitions 109313–109568/119239, min Psi=64510.1062484568; full values saved in block_batches/batch_00610_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 612: n=257, k=4, partitions 109569–109824/119239, min Psi=64510.1062506369; full values saved in block_batches/batch_00611_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 613: n=257, k=4, partitions 109825–110080/119239, min Psi=64510.1062484583; full values saved in block_batches/batch_00612_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 614: n=257, k=4, partitions 110081–110336/119239, min Psi=64510.2868166817; full values saved in block_batches/batch_00613_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 615: n=257, k=4, partitions 110337–110592/119239, min Psi=64510.2868166817; full values saved in block_batches/batch_00614_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 616: n=257, k=4, partitions 110593–110848/119239, min Psi=64510.2868201243; full values saved in block_batches/batch_00615_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 617: n=257, k=4, partitions 110849–111104/119239, min Psi=64510.2868166817; full values saved in block_batches/batch_00616_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 618: n=257, k=4, partitions 111105–111360/119239, min Psi=64510.4581258702; full values saved in block_batches/batch_00617_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 619: n=257, k=4, partitions 111361–111616/119239, min Psi=64510.4581337187; full values saved in block_batches/batch_00618_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 620: n=257, k=4, partitions 111617–111872/119239, min Psi=64510.4581258704; full values saved in block_batches/batch_00619_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 621: n=257, k=4, partitions 111873–112128/119239, min Psi=64510.6208703863; full values saved in block_batches/batch_00620_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 622: n=257, k=4, partitions 112129–112384/119239, min Psi=64510.6208750042; full values saved in block_batches/batch_00621_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 623: n=257, k=4, partitions 112385–112640/119239, min Psi=64510.6208709874; full values saved in block_batches/batch_00622_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 624: n=257, k=4, partitions 112641–112896/119239, min Psi=64510.6208703864; full values saved in block_batches/batch_00623_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 625: n=257, k=4, partitions 112897–113152/119239, min Psi=64510.7756835601; full values saved in block_batches/batch_00624_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 626: n=257, k=4, partitions 113153–113408/119239, min Psi=64510.7756787667; full values saved in block_batches/batch_00625_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 627: n=257, k=4, partitions 113409–113664/119239, min Psi=64510.7756768573; full values saved in block_batches/batch_00626_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 628: n=257, k=4, partitions 113665–113920/119239, min Psi=64510.9231137546; full values saved in block_batches/batch_00627_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 629: n=257, k=4, partitions 113921–114176/119239, min Psi=64510.92311224; full values saved in block_batches/batch_00628_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 630: n=257, k=4, partitions 114177–114432/119239, min Psi=64511.0636907421; full values saved in block_batches/batch_00629_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 631: n=257, k=4, partitions 114433–114688/119239, min Psi=64511.0636964538; full values saved in block_batches/batch_00630_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 632: n=257, k=4, partitions 114689–114944/119239, min Psi=64511.0636907455; full values saved in block_batches/batch_00631_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 633: n=257, k=4, partitions 114945–115200/119239, min Psi=64511.1981444754; full values saved in block_batches/batch_00632_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 634: n=257, k=4, partitions 115201–115456/119239, min Psi=64511.19787985; full values saved in block_batches/batch_00633_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 635: n=257, k=4, partitions 115457–115712/119239, min Psi=64511.3261110446; full values saved in block_batches/batch_00634_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 636: n=257, k=4, partitions 115713–115968/119239, min Psi=64511.3261054887; full values saved in block_batches/batch_00635_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 637: n=257, k=4, partitions 115969–116224/119239, min Psi=64511.4487593883; full values saved in block_batches/batch_00636_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 638: n=257, k=4, partitions 116225–116480/119239, min Psi=64511.4487565737; full values saved in block_batches/batch_00637_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 639: n=257, k=4, partitions 116481–116736/119239, min Psi=64511.5661895614; full values saved in block_batches/batch_00638_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 640: n=257, k=4, partitions 116737–116992/119239, min Psi=64511.5661941797; full values saved in block_batches/batch_00639_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 641: n=257, k=4, partitions 116993–117248/119239, min Psi=64511.678729134; full values saved in block_batches/batch_00640_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 642: n=257, k=4, partitions 117249–117504/119239, min Psi=64511.7866765495; full values saved in block_batches/batch_00641_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 643: n=257, k=4, partitions 117505–117760/119239, min Psi=64511.7866785099; full values saved in block_batches/batch_00642_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 644: n=257, k=4, partitions 117761–118016/119239, min Psi=64511.890331352; full values saved in block_batches/batch_00643_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 645: n=257, k=4, partitions 118017–118272/119239, min Psi=64511.9898724376; full values saved in block_batches/batch_00644_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 646: n=257, k=4, partitions 118273–118528/119239, min Psi=64512.0883928452; full values saved in block_batches/batch_00645_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 647: n=257, k=4, partitions 118529–118784/119239, min Psi=64512.2664590423; full values saved in block_batches/batch_00646_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 648: n=257, k=4, partitions 118785–119040/119239, min Psi=64512.451171025; full values saved in block_batches/batch_00647_n257_k4.npz; peak RSS=130.0 MB.

6 block batch 649: n=257, k=4, partitions 119041–119239/119239, min Psi=64512.6649012162; full values saved in block_batches/batch_00648_n257_k4.npz; peak RSS=130.0 MB.

6 block invocation checkpoint: job=117/117, offset=0, elapsed=127.62s; complete=True. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py blocks --budget 160.0

6 search summary start: priority=10, single BLAS thread, 265s watchdog; continuous search is not an exact global certificate.

## 6. Numerical search completed
| n | smallest floating Psi | 80-digit recheck | block partitions (2/3/4) |
|---:|---:|---:|---|
| 5 | -2.44249065418e-15 | 0.0 | 2/2/1 |
| 6 | -2.22044604925e-15 | -1.2650638e-80 | 3/3/2 |
| 7 | -2.22044604925e-15 | 4.2168792e-81 | 3/4/3 |
| 8 | -8.881784197e-16 | -8.4337584e-81 | 4/5/5 |
| 9 | -9.7699626167e-15 | 3.3735033e-80 | 4/7/6 |
| 10 | 0 | -8.4337584e-80 | 5/8/9 |
| 11 | -6.2172489379e-15 | 2.5301275e-80 | 5/10/11 |
| 12 | 0 | 2.6988027e-79 | 6/12/15 |
| 13 | -5.3290705182e-15 | 3.3735033e-80 | 6/14/18 |
| 14 | 2.22044604925e-15 | 0.0 | 7/16/23 |
| 15 | -1.24344978758e-14 | 4.048204e-79 | 7/19/27 |
| 16 | 2.6645352591e-15 | 0.0 | 8/21/34 |
| 17 | -1.24344978758e-14 | 0.0 | 8/24/39 |
| 18 | 1.7763568394e-15 | 8.6688764e-15 | 9/27/47 |
| 19 | -2.84217094304e-14 | 1.7236424e-15 | 9/30/54 |
| 20 | -2.48689957516e-14 | 3.7108537e-79 | 10/33/64 |
| 21 | -2.84217094304e-14 | 8.7541403e-15 | 10/37/72 |
| 22 | -2.13162820728e-14 | 1.0281257e-15 | 11/40/84 |
| 23 | -6.03961325396e-14 | 6.7470067e-80 | 11/44/94 |
| 24 | -3.19744231092e-14 | 5.695162e-15 | 12/48/108 |
| 25 | -4.61852778244e-14 | 7.1669627e-15 | 12/52/120 |
| 26 | -2.84217094304e-14 | 3.124899e-15 | 13/56/136 |
| 27 | -3.5527136788e-14 | 8.4852902e-15 | 13/61/150 |
| 28 | -2.48689957516e-14 | 8.8458652e-15 | 14/65/169 |
| 29 | -3.90798504668e-14 | -6.7470067e-79 | 14/70/185 |
| 30 | -7.46069872548e-14 | 2.3549714e-14 | 15/75/206 |
| 31 | -2.13162820728e-14 | -6.7470067e-80 | 15/80/225 |
| 32 | -7.46069872548e-14 | 2.3742322e-15 | 16/85/249 |
| 33 | -4.97379915032e-14 | 6.7580148e-15 | 16/91/270 |
| 34 | -7.1054273576e-14 | 1.9478625e-14 | 17/96/297 |
| 35 | -1.27897692437e-13 | -4.3855543e-79 | 17/102/321 |
| 36 | -7.81597009336e-14 | 1.8950103e-14 | 18/108/351 |
| 37 | -3.5527136788e-14 | 2.5578614e-15 | 18/114/378 |
| 38 | -9.23705556488e-14 | 7.1840816e-15 | 19/120/411 |
| 39 | -5.68434188608e-14 | -3.9807339e-78 | 19/127/441 |
| 40 | -5.68434188608e-14 | 7.6002855e-15 | 20/133/478 |
| 64 | -2.62900812231e-13 | 3.5267138e-14 | 32/341/1906 |
| 100 | -5.40012479178e-13 | 8.096408e-78 | 50/833/7153 |
| 257 | -2.18847162614e-12 | 7.9155896e-14 | 128/5504/119239 |
Every integer partition into 2, 3 and 4 nonempty blocks was enumerated, up to permutation. 2-valued shapes have no continuous freedom after mean/scale normalization. For 3/4 blocks: 64-point circle / 102-point sphere grids, three best starts per partition, 90 iterations of continuous tangent pattern refinement; SLSQP epigraph refinement of six worst points per batch with every eligible block pair constraint. This is exhaustive over integer multiplicities, but continuous minimization is numerical, not certified global. Also 770 samples and 18 analytic-gradient local starts per n, including neighborhoods of both zero families. Full smallest-float vectors and 80-digit checks: search_summary.json; per-partition optimized values: block_batches/*.npz. Exact zero vectors (1,0,…,0,−1) occur at every n. Tiny negative floating values at exact-zero vectors are rounding, not counterexamples. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py summary

## 7. Remarks
Remark 1 — GAP (exhaustiveness not proved in the note), filled. For eps>0 in Step 3 the bound is strictly positive. Otherwise equality must be in Step 1, whose two nonnegative terms must both vanish: q−p²=1/n and m=1/[n(n−1)]. Equality in the Gram determinant means x_i²=alpha+beta*x_i for every i (1 and x are independent), so there are exactly two values, one positive and one negative. If both multiplicities are at least two, both squares are eligible pair products, so m≥1/n>1/[n(n−1)]. Therefore one multiplicity is one, yielding (1,−1/(n−1),…,−1/(n−1)) up to scaling, sign and permutation. Together with eps=0, these are the only two zero families for n≥14.

Remark 2 — WRONG as a claim that the printed computation works unchanged, repairable by changing constants. Exact table follows. The 0.002 bound fails for n=10,11,12; the 1% first-term comparison also fails at n=10. With the printed constants all conditions close only at n=13 among 10,…,13. Counterexample to its printed Y2 bound: at n=10 take (1, four copies of 7/300, four copies of −7/300, −1). This is case I with eps=e1, but Y2=49/11250>1/500.
- n=10: Ymax=49/11250, first_left=14007/3125, first_right=1863/550, second_left=7057176049/37500000, second_right=1516/5, third_left=16767/50, third_right=1516/5, y_bound=False, first=False, second=True, third=True
- n=11: Ymax=3969/1210000, first_left=2647323/550000, first_right=61/12, second_left=3827817021/17187500, second_right=3411/10, third_left=2013/4, third_right=3411/10, y_bound=False, first=True, second=True, third=True
- n=12: Ymax=49/19360, first_left=14007/2750, first_right=363/50, second_left=14176890063/55000000, second_right=379, third_left=35937/50, third_right=379, y_bound=False, first=True, second=True, third=True
- n=13: Ymax=539/270400, first_left=1386693/260000, first_right=1746/175, second_left=1905981007/6500000, second_right=4169/10, third_left=172854/175, third_right=4169/10, y_bound=True, first=True, second=True, third=True

A uniform repair from n=10: use Y2≤0.005, T≤2.005, 4.005 in the first term, 2% instead of 1%, and 0.005 instead of 0.002 in the second term. The second term is still ≤37.9(n−2)eps, and 0.98D≥37.9(n−2). At n=10, Ymax=49/11250<0.005, first coefficient with repair=4.4856 <D/50=6.774545…, second coefficient=188.2384081666…<303.2, and 0.98D=331.952727…>303.2. For all n≥11, the repaired first coefficient is <4.005*2.1=8.4105 <D(11)/50=10.1666…, while n=10 is checked directly. The second comparison follows from (189/5)*(1+1/4800)²<37.9 and (n−3)(n−2)/(n(n−1))<1. The same increasing D/(n−2) proves the last comparison from its n=10 value. Thus the theorem itself also follows for every n≥10 after these explicit edits.

Remark 3 — CORRECT. In sorted order, among positive pairs the largest is x_1*x_2, and among negative pairs it is x_(n−1)*x_n. Mixed signs give nonpositive products. At least one extreme pair has nonnegative product (for n≥3); this also handles zeros and the vector with only two nonzero coordinates. Thus the maximum is exactly the displayed maximum. Command: ... python3 audit.py 7

6 independent search validation: {"partitions": 142524, "batches": 649, "max_weighted_sum_error": 7.105427357601002e-15, "max_T_error": 5.851322960159777e-06, "max_saved_objective_absolute_difference": 1.862645149230957e-09, "gradient_relative_errors": [[5, 2.877202557359764e-10], [14, 1.7076863448543015e-09], [40, 7.304335802490412e-11], [257, 2.2888037820059845e-10]], "worst_raw_float": -2.1884716261411086e-12, "all_worst_float_vectors_nonnegative_in_exact_arithmetic": true, "peak_RSS_bytes": 99696640, "elapsed_seconds": 0.5545398750109598}
Every reported smallest-float vector was re-centered and evaluated with exact binary-rational arithmetic and all eligible coordinate pairs; all are nonnegative. The most negative floating reading is rounding error. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 verify_search.py


Report preparation: all requested analytic stages and numerical searches are complete. Remaining work is to present the repaired proof and audit the report against generated exact data. No counterexample found, including n=5,…,13; numerical absence alone is not a proof for n=5,…,9. The repaired argument also proves n≥10.

REPORT.md written with verdict table, filled proof gaps, exact comparisons, boundary vectors, all 39 per-n search results, equality classification, and repaired constants from n=10. Overall theorem verdict: SOUND after the explicit proof repairs. Remark 2 is WRONG if read as claiming the printed constants work unchanged. The exact global numerical certificate for continuous block values at n=5,…,9 was not obtained. Command: nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 write_report.py
