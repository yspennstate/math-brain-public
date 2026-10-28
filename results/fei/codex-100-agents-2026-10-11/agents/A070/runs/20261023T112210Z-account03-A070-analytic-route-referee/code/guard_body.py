for eps in [-1,1]:
 a=[F(7,5),F(-1,5)];b=[F(1),F(1)]
 v,ref,cr,qc=joint(a,b,1,0,F(1,3),eps)
 ck(sum(spectrum(v))==1)
 av=children(a,0);bv=children(b,0);rr=marginal(cr,0)
 costs=[ce([(x+y)/2 for x,y in zip(spectrum(aa),spectrum(bb))],rr) for aa,bb in zip(av,bv)]
 pc=[(x+y)/2 for x,y in zip(spectrum(a),spectrum(b))]
 db=plus(ce(pc,cr),times(plus(*costs),-F(1,2)))
 ck(decrement(v,ref,0)==db)
 ch=children(v,0)
 ck([sum(spectrum(w)) for w in ch]==[F(37,25),F(13,25)])
 energy=sum(p for s,p in enumerate(spectrum(v)) if s&1)
 ck(energy==F(8,25));ck(inf(v,0)==F(1,2));ck(energy!=inf(v,0))
result=dict(status='PASS',assertions=checks,cases=2,core_CE_identity='HOLDS for unnormalized real children',root_norm=1,child_squared_norms=['37/25','13/25'],core_spectral_energy='8/25',core_physical_pivotal_probability='1/2',elapsed_seconds=time.perf_counter()-start)
(R/'out/REAL_GUARD.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps(result))
