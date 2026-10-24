FILE ~/Downloads/Probability_1000_intake_claude_20260907/sources/bordenave_chafai_circular_2012/text.txt
3326: 6.1. Heavy tailed analogs of quarter circular and circular laws. We now come
3327: back to an array X := (Xij)1≤i,j≤n of i.i.d. random variables on C. We lift the hypothesis
3328: that the entries have a ﬁnite second moment: we will assume that,
3329: • for some 0 < α < 2,
3330: lim
3331: t→∞tαP(|X11| ≥t) = 1,
3332: (6.1)
3333: • as t →∞, the conditional probability
3334: P
3335:  X11
3336: |X11| ∈·
3337: 
3338: 
3339:  |X11| ≥t
3340: 
3341: converges to a probability measure on the unit circle S1 := {z ∈C : |z| = 1}.
3342: 
3343: ===== PDF PAGE 39 =====
3344: AROUND THE CIRCULAR LAW
3345: 39
3346: The law of the entries belongs then to the domain of attraction of an α-stable law. An
3347: example is obtained when |X11| and X11/|X11| are independent with |X11| = |S| where S
3348: is real symmetric α-stable. Another example is given by X11 = εW −1/α with ε and W
3349: independent such that ε is supported in S1 while W is uniform on [0, 1].
3350: The interest on this type of random matrices has started with the work of the physicists
3351: Bouchaud and Cizeau [28]. One might think that the analog of the Ginibre ensemble is a
3352: matrix with i.i.d. α-stable entries. It turns out that this random matrix ensemble is not
3353: unitary invariant and there is no explicit expression for the distribution of its eigenvalues.
3354: This lack of comparison with a canonical ensemble makes the analysis of the limit spectral
3355: measures more delicate. We may ﬁrst wonder what is the analog of the quarter circular
3356: law theorem 2.1. This question has been settled by Belinschi, Dembo and Guionnet [15]
3357: (built upon the earlier work of Ben Arous and Guionnet [16]).
3358: Theorem 6.1 (Singular values of heavy tailed random matrices). There exists a probability
3359: measure να on R+ such that a.s. νn−1/αX ⇝να as n →∞.
3360: This probability measure να depends only on α. It does not have a known explicit closed
3361: form but has been studied in [16, 25, 15]. We know that να has a bounded continuous
3362: density fα on R+, which is analytic on some neighborhood of ∞. The explicit value of
3363: fα(x) is only known for x = 0. But, more importantly, we have
3364: lim
3365: t→∞tα+1fα(t) = α.
3366: In particular, να inherits the tail behavior of the entries:
3367: lim
3368: t→∞tανα([t, ∞)) = 1.
3369: The measure να is a perturbation of the quarter circular law: it can be proved that να
3370: converges weakly to the quarter circular law as α converges to 2. Contrary to the ﬁnite
3371: variance case, the n−1/α normalization cannot be understood from the computation of
3372: Z
3373: s2 dνn−1/αX(s) =
3374: 1
3375: n1+1/α
3376: n
3377: X
3378: i,j=1
3379: |Xij|2
3380: since the later diverges. A proof of the tightness of νn−1/αX requires some extra care that
3381: we will explain later on. However, at a heuristic level, we may remark that if R1, . . . , Rn
3382: denotes the rows of n−1/αX then for each k,
3383: ∥Rk∥2
3384: 2 =
3385: 1
3386: n2/α
3387: n
3388: X
3389: i=1
3390: |Xki|2
3391: converges weakly to a non-negative α
3392: 2 -stable random variable. Hence the n−1/α normal-
3393: ization stabilizes the norm of each row of X.
3394: Following [26], we may also investigate the behavior of the eigenvalues of X. Here is
3395: the analogue of the circular law theorem 2.2 for our heavy tailed entries matrix model.
3396: Theorem 6.2 (Eigenvalues of heavy tailed random matrices). There exists a probability
3397: measure µα on C such that in probability µn−1/αX ⇝µα as n →∞. Moreover, if X11 has
3398: a bounded density, then the convergence is almost sure.
3399: We believe that theorem 6.2 can be upgraded to an a.s. weak convergence, but our
3400: method does not catch this due to slow “in probability” controls on small singular values.
3401: Again, the measure µα depends only on α and is not known explicitly. However, it is
3402: isotropic and has a bounded continuous density with respect to Lebesgue measure dxdy
3403: on C: dµα(z) = gα(|z|)dxdy. The value of gα(r) is explicit for r = 0. As r →∞, the tail
3404: behavior of gα is up to multiplicative constant equivalent to
3405: r2(α−1)e−α
3406: 2 rα.
3407: 
3408: ===== PDF PAGE 40 =====
3409: 40
3410: CHARLES BORDENAVE AND DJALIL CHAFA¨I
3411: This exponential decay is quite surprising and contrasts with the power tail behavior of
3412: fα. It indicates that X is typically far from being a normal matrix. Also, we see that the
3413: eigenvalues limit spectrum is more concentrated than the singular values limit spectrum.
3414: In fact, in the ﬁnite variance case, the phenomenon is already present: the quarter circular
3415: law has support [0, 2] while the circular law has support the unit disc. Again, the measure
3416: is µα is perturbation of the circular law: µα converges weakly to the circular law as α
3417: converges to 2.
3418: The proof of theorem 6.2 will follow the general strategy of Girko’s Hermitization.
3419: Lemma 4.3 gives a characterization of the limit measure in terms of its logarithmic po-
3420: tential. Here, it turns out to be not so convenient in order to analyze the measure µα.
3421: We will rather use the quaternionic version of Girko’s Hermitization, i.e. lemma 4.20. For
3422: statement (i′) in lemma 4.20, we will prove a generalized version of theorem 6.1.
3423: Theorem 6.3 (Singular values of heavy tailed random matrices). For all z ∈C there
3424: exists a probability measure να,z on R+ such that a.s. νn−1/αX−z ⇝να,z as n →∞.
3425: Moreover, with the notations used in lemma 4.20, for all q = q(z, η) ∈H+, there exists
3426: Γ(q) ∈H+, such that a.s. Γn−1/αX(q) converges to Γ(q) and Γ(q)11 = mˇνα,z(η).
3427: Objective method - sparse random graphs and trees. The strategy for proving theorem 6.3,
3428: borrowed from [26], will diﬀer signiﬁcantly from the proof of theorem 2.1. We will prove
3429: that n−1/αX converges in some sense, as n →∞, to a limit random operator A deﬁned
3430: in the Hilbert space ℓ2(N). This will be done by using the “objective method” initially
3431: developed by Aldous and Steele in the context of randomized combinatorial optimization,
3432: see [6]. We build an explicit operator on Aldous’ Poisson Weighted Inﬁnite Tree (PWIT)
3433: and prove that it is the local limit of the matrices n−1/αX in an appropriate sense. While
3434: Poisson statistics arises naturally as in all heavy tailed phenomena, the fact that a tree
3435: structure appears in the limit is roughly explained by the observation that non-vanishing
3436: entries of the rescaled matrix n−1/αX can be viewed as the adjacency matrix of a sparse
3437: random graph which locally looks like a tree. In particular, the convergence to PWIT
3438: is a weighted-graph version of familiar results on the local tree structure of Erd˝os-R´enyi
4355: Z ∞
4356: 0
4357: (e−xsY1 −1)βx−α
4358: 2 −1dx
4359: 
4360: = exp
4361: 
4362: −Γ
4363: 
4364: 1 −α
4365: 2
4366: 
4367: s
4368: α
4369: 2 E[Y
4370: α
4371: 2
4372: 1 ]
4373: 
4374: .
4375: □
4376: Hence, by lemma 6.15, we may rewrite (6.8) as
4377: h d=
4378: t + yS
4379: |z|2 + (t + yS)(t + yS′),
4380: (6.12)
4381: where S and S′ are i.i.d. variables with common Laplace transform (6.10) and the function
4382: y = y(|z|2, t) = E[hα/2]2/α is the unique solution of the equation in y:
4383: 1 = E
4384: 
4385: ty−1 + S

FILE ~/Downloads/Probability_1000_intake_claude_20260907/sources/chatterjee_chaos_2008/text.txt
4065: ing, the zero boundary condition is the more important one. Also,
4066: even in the torus, is log log n the correct order? The author thinks
4067: O(1) is more likely to be the right answer.
4068: (5) Show that chaos implies multiple peaks even when the correlations
4069: are not all nonnegative. This involves getting a bound on the second
4070: moment of R(I0, It), which we do not know how to derive at present.
4071: (6) Find a suitable multiple peaks condition that is actually equivalent