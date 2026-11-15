# RG10AR - first-reader report, brownian-prefix-filling

Reader: an agent, 14 Nov 2026 02:2x. Read on the queued PDF q4/brownian-prefix-filling/final_9861d62.pdf (6 pp, Zenodo 24149779), single author.

Paper: "A Brownian piece in front of a process absolutely continuous with respect to Brownian motion". Answers Burdzy-Scheutzow, Forward Brownian motion, PTRF 160 (2014) 95-126, Problem 7.5 p.125: if the law Q of X is absolutely continuous w.r.t. Wiener measure, then on an extension X_t = B_{N+t} - B_N with B a Brownian motion and N an a.s. finite nonnegative integer.

## Verdict: ACCEPT (two optional minor points, none blocks posting)

## What was checked, line by line
- Thm 2.1(ii): A in I gives 1_A(theta^n z) = 1_A(z) for all n in Z, so Q(A) = P(A) and E[f|I] = 1. Correct.
- Thm 2.1(i), masses: int a_{n+1} = int a_n - int m_n and int b_{n+1} = int b_n - int m_n from L preserving integrals; a_n = b_n in mass. Correct.
- Closed form a_n = 1 - sum_{k<n} L^{n-k} m_k: checked by unrolling a_1, a_2 (L linear, L1 = 1). Correct.
- Cesaro identity (2.4) and c_{k,M} -> E[m_k|I] in L1 by the mean ergodic theorem for theta^{-1} (same invariant field); the tail bound ||c_{k,M}||_1 <= int m_k makes the k-sum converge; (2.5) h = E[b|I] uses E[f|I] = 1. Correct.
- r > 0 contradiction: D = H cap {b >= delta}, m_n >= min(a_n, delta) >= delta a_n since a_n <= 1; Cesaro lower bound delta eps P(D) > 0 against sum_n int_D m_n <= 1. Correct.
- Random time: N = inf{n : U_n <= g_n(theta^n Z)}, induction "law of theta^n Z on {N >= n} is a_n P" via (2.1) (y = theta z and invariance). P(N >= n) = r_n -> 0, law of theta^N Z = sum m_n P = fP. Correct.
- Section 3: theta w(t) = w(t+1) - w(1), inverse w(t-1) - w(-1) (verified theta theta^{-1} = id), P-invariance, ergodicity via the bijection with C_0[0,1]^Z and Kolmogorov 0-1. f = f+ o rho integrates to 1 and pushes to Q; Y_t = W(N+t) - W(N). Transfer by Kallenberg 2nd ed. Thm 6.10 onto a product extension, measurable graph set carries probability one. Correct; only absolute continuity is used, so the strengthening over "equivalent" is right.
- Remark 1.2 (N cannot be a stopping time unless Q = W): strong Markov. Correct.
- Remark 4.2: for N = n(Z) the law of theta^{n(Z)} Z has density sum_k 1{n(theta^{-k} y) = k}, integer-valued. Correct.
- Remark 4.3: recomputed by hand r_1 = 1/2 (j = 0) and r_2 = 1/4 (j = 1) for f = 2 1{x_0 = 1} on fair bits; matches C(2j,j) 2^{-2j-1}. The first n >= 0 with x_n = 1 has mean one. Correct; "if the pattern continues" is the right hedge.

## Optional minor points
1. Remark 4.1: the forward (one-sided) version claims an a.s. finite randomized stopping time from Rost's theorem. Finiteness rests on the chain being conservative and ergodic (Chacon-Ornstein filling); one clause saying so, or the exact Dellacherie-Meyer number for the finite-time form, would close it. The main theorem does not depend on this remark.
2. Display (2.1): in the text layer the left side reads P(Y in A); it should be P(theta Y in A, F). Check the typeset PDF; if it is only an extraction artefact, nothing to do.

## Literature
- [2] verified on Crossref (10.1007/s00440-013-0524-x, PTRF 160, 95-126, Burdzy, Scheutzow).
- Forward citations of [2] (OpenAlex, 14 Nov): one, Pitman-Tang EJP 20 (2015) no. 61 = [11], already cited. No later paper answers Problem 7.5.
- Rost, Chacon-Ornstein, Aldous-Thorisson, Thorisson 1996/2000, Greven, Holroyd-Peres, Liggett, Last-Morters-Thorisson, Pitman-Tang LNM 2137: bibliographic details match standard records; REFCHECK_auto lists them as having no DOI in the bib (not an error).

Recommendation for ResearchGate: post final_9861d62.pdf as it is.
