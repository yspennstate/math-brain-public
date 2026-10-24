# P0162: statement-only packet for independent attack

For every n >= 1 and every Boolean-valued f: {0,1}^n -> {-1,+1}, take uniform input, Walsh characters chi_s(x)=(-1)^(s dot x), and Fourier coefficients fhat(s)=E[f(x)chi_s(x)]. Let p_s=fhat(s)^2, so sum_s p_s=1. Define H(f)=sum_s p_s log2(1/p_s) with 0 log(1/0)=0, and I(f)=sum_s |s| p_s=sum_i Pr[f(x) != f(x+e_i)].

The target is existence of a finite absolute C such that H(f) <= C I(f) for ALL n and ALL such f. C cannot depend on n, the bias E[f], a positive lower bound for the variance, or a fixed family. Constant functions have H=I=0 and are included. The empty Fourier coefficient is included in H. This is Shannon entropy, not min-entropy. The {0,1} input convention is equivalent to the usual {-1,+1} cube by x_i -> (-1)^x_i.

Primary statement source: Ryan O'Donnell, John Wright, Yuan Zhou, The Fourier Entropy-Influence Conjecture for certain classes of Boolean functions, author PDF https://www.cs.cmu.edu/~odonnell/papers/fei.pdf, introduction and Section 2.1. Equations and quantifiers are transcribed into the equivalent convention above.

Current openness: UNKNOWN as of 2026-10-10; retrieved literature states the conjecture remains open but a complete current-status check is pending. No novelty claim. A special case or failure of a stronger bridge will not resolve P0162.

Lane reservation for w510: affine-subspace indicators, their sharp entropy/influence ratio, and normalization of the nonempty spectral sample. Please independently attack this boundary lane before reading ATTEMPT.md.
