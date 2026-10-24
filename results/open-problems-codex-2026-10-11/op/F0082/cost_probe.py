import math,json,pathlib
out=[]
for name,f in [('linear',lambda t:t),('sqrt',math.sqrt),('log1p',math.log1p),('power_0.9',lambda t:t**.9),('squared',lambda t:t*t)]:
 # Both orientations are needed: one detects convexity, the other concavity.
 for a,b,c,d,label in [(.5,.5,4.5,4.5,'old_lengths_1_9'),(.5,4.5,4.5,.5,'old_lengths_5_5')]:
  theta=.001
  new1=math.sqrt(a*a+d*d+2*a*d*math.cos(theta));new2=math.sqrt(c*c+b*b+2*c*b*math.cos(theta));old=f(a+b)+f(c+d);new=f(new1)+f(new2)
  row={'cost':name,'orientation':label,'theta':theta,'arms':[a,b,c,d],'old_lengths':[a+b,c+d],'new_lengths':[new1,new2],'old_cost':old,'new_cost':new,'new_minus_old':new-old};out.append(row);print(row)
pathlib.Path('cost_probe.json').write_text(json.dumps(out,indent=2),encoding='utf8')
