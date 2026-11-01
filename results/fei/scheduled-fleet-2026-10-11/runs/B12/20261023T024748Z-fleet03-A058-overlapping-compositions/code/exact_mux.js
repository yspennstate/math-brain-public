// A058 mux v7 exact1. Frozen n=3; no dimension escalation.
const started=Date.now(), primes=[2,3,5,7], Q=4096n;
const lower=primes.map(p=>p===2?Q:BigInt((BigInt(p)**Q).toString(2).length-1));
let counts={pairs:0,posterior_nonnegative:0,upper_bound:0,disagreement_source:0,data_identities:0,mass_influence:0,exact_fallback:0};
const cache=new Map();
function factors(k){const r=[0,0,0,0]; k=Math.abs(k);if(!k)return r;for(let i=0;i<4;i++)while(k%primes[i]===0){r[i]++;k/=primes[i]}if(k!==1)throw Error("unfactored "+k);return r}
function add(a,b,c=1){return a.map((x,i)=>x+c*b[i])}
function ev(k,den=8){if(!k)return [0,0,0,0];const f=factors(k),d=factors(den),mass=512*k*k/(den*den);return f.map((x,i)=>2*mass*(d[i]-x))}
function ent(w){let v=[0,0,0,0];for(const x of w)v=add(v,ev(x));return v}
function wh(a){a=a.slice();for(let d=1;d<8;d*=2)for(let i=0;i<8;i+=2*d)for(let j=0;j<d;j++){const x=a[i+j],y=a[i+j+d];a[i+j]=x+y;a[i+j+d]=x-y}return a}
function hprob(m){let r=[0,0,0,0];for(const k of [m,8-m])if(k){const f=factors(k);r=add(r,f.map((x,i)=>64*k*((i===0?3:0)-x)))}return r}
function ge(v,label){if(v.some(x=>!Number.isInteger(x)))throw Error("noninteger");const key=v.join(",");if(cache.has(key)){if(!cache.get(key))throw Error(label);return}let lo=0n,hi=0n;for(let i=0;i<4;i++){const c=BigInt(v[i]),u=lower[i]+(i?1n:0n);lo+=c*(c>=0n?lower[i]:u);hi+=c*(c>=0n?u:lower[i])}let pass;if(lo>=0n)pass=true;else if(hi<0n)pass=false;else{counts.exact_fallback++;let lhs=1n,rhs=1n;for(let i=0;i<4;i++){const c=v[i];if(c>0)lhs*=BigInt(primes[i])**BigInt(c);else if(c<0)rhs*=BigInt(primes[i])**BigInt(-c)}pass=lhs>=rhs}cache.set(key,pass);if(!pass)throw Error(label+" "+key)}
const fs=Array.from({length:256},(_,k)=>Array.from({length:8},(_,x)=>(k>>x&1)?-1:1));
const ws=fs.map(wh), hs=ws.map(ent);
const children=fs.map(g=>[0,1,2].map(i=>[0,1].map(b=>g.map((_,x)=>g[(x&~(1<<i))|(b<<i)]))));
function gain(wg,whh,hg,hh){let hf=[0,0,0,0];for(let t=0;t<8;t++){hf=add(hf,ev(wg[t]+whh[t],16));hf=add(hf,ev(wg[t]-whh[t],16))}return {hf,L:add(add(hf,hg,-.5),hh,-.5)}}
const childW=children.map(cs=>cs.map(bs=>bs.map(wh)));
const childH=childW.map(cs=>cs.map(bs=>bs.map(ent)));
for(let g=0;g<256;g++)for(let h=0;h<256;h++){
 const {L,hf}=gain(ws[g],ws[h],hs[g],hs[h]);
 let m=0,edges=0;const ee=fs[g].map((x,i)=>x*fs[h][i]);for(let x=0;x<8;x++){if(ee[x]<0)m++;for(let i=0;i<3;i++)if(!(x>>i&1)&&ee[x]!==ee[x^(1<<i)])edges++}
 ge(L,"negative L");counts.posterior_nonnegative++;
 const upper=add(hprob(m),[256*m,0,0,0]);ge(add(upper,L,-1),"upper");counts.upper_bound++;
 ge(add([128*edges,0,0,0],hprob(m),-1),"source");counts.disagreement_source++;
 let mass=0,selector=0;for(let t=0;t<8;t++){mass+=(ws[g][t]+ws[h][t])**2+(ws[g][t]-ws[h][t])**2;selector+=(ws[g][t]-ws[h][t])**2}if(mass!==256||selector!==32*m)throw Error("mass/selector");counts.mass_influence++;
 for(let i=0;i<3;i++){let avgH=[0,0,0,0],avgK=[0,0,0,0],avgL=[0,0,0,0];for(let b=0;b<2;b++){const c=gain(childW[g][i][b],childW[h][i][b],childH[g][i][b],childH[h][i][b]);avgH=add(avgH,c.hf,.5);avgL=add(avgL,c.L,.5);avgK=add(avgK,add(childH[g][i][b],childH[h][i][b]),.25)}
 const delta=add(add(add(add(hf,avgH,-1),add(hs[g],hs[h]),-.5),avgK),add(L,avgL,-1),-1);if(delta.some(x=>x!==0))throw Error("data ledger");counts.data_identities++}
 counts.pairs++;
 if(Date.now()-started>60000)throw Error("frozen runtime exceeded");
}
const bent=[];for(let m=1;m<=6;m++){const M=2n**BigInt(m),N=M*M;const plus=(N+M)/2n,minus=(N-M)/2n;if(plus+minus!==N||plus-minus!==M)throw Error("bent counts");if(2n*(N-2n*M+2n)<N)throw Error("bent lower");bent.push({m,n:2*m,N:String(N),positive:String(plus),negative:String(minus),J:"1/"+N,source_influence:(4*m)+"/"+N,gain_over_J_lower:2*m-1,R_over_J_lower:2*m-5})}
const result={status:"PASS",helper:"A058-mux-v7-exact-1",domain:"all 65536 ordered pairs on 3 physical data coordinates; 196608 one-query restrictions; no symmetry",arithmetic:"exact integer Walsh, prime-log forms /512, BigInt-certified 4096 log intervals with exact-power fallback",counts,distinct_sign_forms:cache.size,bent,elapsed_ms:Date.now()-started,memory:"estimated under100MB; unmeasured",scope:"finite validation; all-dimensional proof in PROOF.md; independent review pending; FEI OPEN"};
globalThis.__result=result;

if(typeof console!=='undefined')console.log(JSON.stringify(globalThis.__result,null,2));
