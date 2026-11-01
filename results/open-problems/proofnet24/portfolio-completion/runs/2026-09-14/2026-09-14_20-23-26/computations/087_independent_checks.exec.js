const code=String.raw`
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t}return a}
function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return [a/g,b/g]}
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]),sq=a=>mul(a,a),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],fmt=a=>a[1]===1n?String(a[0]):a.map(String).join("/");
const sum=arr=>arr.reduce(add,Q(0));
const zlaw=[[-1,Q(2,3)],[2,Q(1,3)]],wlaw=[[-1,Q(3,4)],[3,Q(1,4)]];
function tuples(m){if(!m)return [{t:[],p:Q(1)}];return tuples(m-1).flatMap(({t,p})=>zlaw.map(([z,q])=>({t:[...t,z],p:mul(p,q)})))}
function del(t,i){return t.filter((_,k)=>k!==i)}
function f(t,w,z){const s=t.reduce((a,b)=>a+b,0),a=t.reduce((v,b,k)=>v+(k+1)*b,0);return Q(w*a*z+s*s+t.length*w)}
function pf(t,w){return sum(zlaw.map(([z,p])=>mul(p,f(t,w,z))))}
function energy(t,u,w){return sum(zlaw.map(([z,p])=>mul(p,sq(sub(f(t,w,z),f(u,w,z))))))}
function beta(m){return sum(tuples(m).flatMap(({t,p})=>wlaw.map(([w,pw])=>mul(mul(p,pw),div(sum(t.map((_,i)=>energy(t,del(t,i),w))),Q(m))))))}
function check(n){
 const bn=beta(n),bn1=beta(n-1),B=sum(tuples(n-1).flatMap(({t,p})=>wlaw.flatMap(([w,pw])=>zlaw.map(([z,pz])=>mul(mul(mul(p,pw),pz),sq(f(t,w,z)))))));
 const Qh=div(add(B,mul(Q(n-1),bn1)),Q(n));
 let EF2=Q(0),ED2=Q(0),EH2=Q(0),EpairE=Q(0);
 const pairs={};for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)pairs[i+","+j]={c:[Q(0),Q(0),Q(0)],identity:Q(0)};
 for(const {t,p} of tuples(n))for(const [w,pw]of wlaw){
  const wt=mul(p,pw),fits=t.map((_,i)=>del(t,i)),h=fits.map((u,i)=>sub(pf(u,w),f(u,w,t[i]))),D=sub(pf(t,w),div(sum(fits.map(u=>pf(u,w))),Q(n))),H=div(sum(h),Q(n)),F=sub(pf(t,w),div(sum(fits.map((u,i)=>f(u,w,t[i]))),Q(n)));
  if(!eq(F,add(D,H)))throw Error("decomposition");
  EF2=add(EF2,mul(wt,sq(F)));ED2=add(ED2,mul(wt,sq(D)));EH2=add(EH2,mul(wt,sq(H)));
  for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j){
   const tt=t.filter((_,k)=>k!==i&&k!==j),a=sub(pf(tt,w),f(tt,w,t[i])),b=sub(pf(tt,w),f(tt,w,t[j])),di=sub(h[i],a),dj=sub(h[j],b),v=pairs[i+","+j];
   [mul(a,b),mul(a,dj),mul(di,b)].forEach((x,k)=>{v.c[k]=add(v.c[k],mul(wt,x))});
   v.identity=add(v.identity,mul(wt,sub(mul(h[i],h[j]),mul(di,dj))));
   EpairE=add(EpairE,mul(wt,energy(fits[i],tt,w)));
  }
 }
 const assertions=Object.values(pairs).every(v=>v.c.every(x=>eq(x,Q(0)))&&eq(v.identity,Q(0)))&&eq(EpairE,mul(Q(n*(n-1)),bn1))&&le(ED2,bn)&&le(EH2,Qh);
 const remainder=sub(sub(EF2,bn),Qh),main=le(remainder,Q(0))||le(sq(remainder),mul(Q(4),mul(bn,Qh)));
 if(!assertions||!main)throw Error("failed");
 return {n,configurations:2**n*2,separateCancellations:Object.keys(pairs).length*3,pairIdentities:Object.keys(pairs).length,B2:fmt(B),betaN2:fmt(bn),betaNminus1Squared:fmt(bn1),EF2:fmt(EF2),ED2:fmt(ED2),EH2:fmt(EH2),Qh:fmt(Qh),pairEnergySum:fmt(EpairE),allExactAssertionsPassed:true};
}
return [check(3),check(4)];
`;
store("independentCheckCode",code);const out=Function(code)();store("independentCheckOutput",out);text(out);