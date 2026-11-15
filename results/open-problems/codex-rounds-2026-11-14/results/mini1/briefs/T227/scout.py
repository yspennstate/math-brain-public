"""Small, single-threaded exploratory calculation; no proof claims."""
import json
import math
import resource

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

def state(p):
    a, b, c = p
    u = math.tanh(c)
    v = math.tanh(b*u)
    j = (v, a*(1-v*v)*u, a*(1-v*v)*b*(1-u*u))
    return a*v, j

def run(p, h, n=30):
    rows = []
    for t in range(n+1):
        f, j = state(p)
        rows.append(dict(t=t, p=p, loss=f*f/2, kernel=sum(x*x for x in j)))
        p = tuple(x-h*f*d for x,d in zip(p,j))
    return rows

if __name__ == '__main__':
    candidates = []
    for a in (2.,3.,4.,5.,8.):
        for b in (.05,.1,.2,.3,.5):
            for c in (.5,1.,2.):
                for h in (.5, .75, 1., 1.25, 1.5):
                    rows = run((a,b,c),h)
                    if h*rows[0]['kernel']>2 and rows[1]['loss']>1.1*rows[0]['loss'] and rows[-1]['loss']<1e-12:
                        candidates.append(dict(init=(a,b,c),h=h,initial=rows[0],spike=rows[1],tail=rows[3],final=rows[-1]))
    candidates.sort(key=lambda d: abs(d['tail']['p'][0]))
    with open('scout_data.json','w') as out:
        json.dump(candidates,out,indent=2)
    print('candidates:', len(candidates))
    for d in candidates[:5]:
        print(json.dumps(d))
    print('max_rss_bytes:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
