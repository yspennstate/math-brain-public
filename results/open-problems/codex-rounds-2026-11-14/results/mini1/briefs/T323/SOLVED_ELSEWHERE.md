# The identity-matrix part is settled; the full task is not

Yury Polyanskiy, Philippe Rigollet and Andrew Yao,
*Synchronization of mean-field models on the circle*,
[arXiv:2507.22857](https://arxiv.org/abs/2507.22857), submitted 30 July 2025.
The abstract and [full text](https://arxiv.org/html/2507.22857v1) were opened
on 14 November 2026.
This paper predates the prompt's November 2026 status check.

Corollary 2.5 proves almost-everywhere synchronization for the normalized
self-attention system (T2) for beta >= -0.16, in particular every beta > 0.
Writing x_i=(cos(theta_i),sin(theta_i)) converts the prompt's d=2 equation
exactly to (T2). This is a finite-n statement, despite the title's use of
“mean-field”.

For d >= 3, Theorem 6.1 in Borjan Geshkovski, Cyril Letrouit, Yury Polyanskiy
and Philippe Rigollet, *A mathematical perspective on Transformers*,
[arXiv:2312.10794v5](https://arxiv.org/html/2312.10794v5), states the
almost-everywhere clustering result for all beta >= 0. Together these
results settle the prompt's identity-matrix assertion in every d >= 2.

They do not classify arbitrary query, key and value matrices. The bounded
search did not find a complete resolution of that part. Work therefore
continues on an explicit family of general matrices in PROOF.md.
