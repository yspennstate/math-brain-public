exec(open(__file__.replace('matching_explore.py','explore.py')).read().split('edges=')[0])
f=[len(S)-min(2,len(set(i//2 for i in S))) for S in SS]
for cs in [[0,0,1,2,1,2],[0,1,1,2,2,0],[0,1,2,0,1,2]]:
 K=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(cs[i]==cs[j])-sp.Rational(1,3)))
 T=operator(K,f)
 print('classes',cs,'spec',T.eigenvals())
 for ev,mul,V in T.eigenvects():
  if ev.is_negative:print('negative',ev,V)
