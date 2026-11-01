import pathlib,json,urllib.request
p=pathlib.Path('LITERATURE.md');s=p.read_text(encoding='utf-8-sig').replace('paper 123, DOI','pp.1--32, DOI');p.write_text(s,encoding='utf8')
p=pathlib.Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('# P0177 working proof record',r'''# P0177: quantitative large-time classical and free mode locations

## Proved result

Let X have probability law mu, with alpha=E exp(epsilon X^2)<infinity for some epsilon>0. Write m=E X, mu_k=E[(X-m)^k]. Normalize both Brownian convolutions to noise variance t. The classical density and the free density each have a unique global maximizer at sufficiently large t, and

 M_c(t)=m-mu_3/(2t)+(mu_5-6mu_2mu_3)/(8t^2)+O_mu(t^-3),
 M_f(t)=m-3mu_3/t+(5mu_5-22mu_2mu_3)/t^2+O_mu(t^-3).

Both converge to the initial mean. Explicit O(t^-1) bounds with thresholds and constants in epsilon,alpha alone appear at the end. Free global uniqueness actually holds under finite variance at t>7(7+4sqrt(2))Var(X), without a claim of unimodality. All proofs below are complete real-variable arguments using the published Biane parametrization. No novelty assertion is made.
''');p.write_text(s,encoding='utf8')
p=pathlib.Path('CLAIMS.jsonl');rows=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()]
rows.append({'problem_id':'P0177','claim':'Explicit bounds determined solely by the source epsilon,alpha: classical |M_c-m|<=Q/t at t>=72 log(2alpha^2)/epsilon; free |M_f-m|<=64[((sqrt(2)+2)^3 (log(alpha)/epsilon)^(3/2))+Q]/t at t>7(7+4sqrt(2))log(alpha)/epsilon, Q=8alpha[3/(2e epsilon)]^(3/2).','status':'proved','proof_location':'ATTEMPT.md: Estimates using only the source epsilon and alpha','remaining_gap':'none; constants are sufficient and not optimal','checks':['Jensen bounds on second moment and centered exponential moment','Calculus maximum of a^3 exp(-epsilon a^2)','Earlier explicit classical and free bounds']})
p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
print('Updated theorem summary, source-only constants and claims')
