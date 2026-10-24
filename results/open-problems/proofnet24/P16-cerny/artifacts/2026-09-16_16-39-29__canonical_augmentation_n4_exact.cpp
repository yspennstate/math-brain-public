/*
Exact finite self-check for P16 Cerny run 52.
Scope: n=4 state-labeled transformation supports after duplicate-letter collapse.
It exhaustively checks distinct 3-supports and irreducibly synchronizing distinct
4-supports, exact reset thresholds by subset BFS, state-conjugacy canonicalization,
semigroup irredundancy, pair-trap escape, and canonical one-letter augmentation
from nonsynchronizing ternary parent orbits modulo parent automorphisms.
This is a validation of the full-scope reduction architecture on n=4; it does NOT
advance the tracked n=8 three/four-letter metric and is not an n=8 enumeration.
All arithmetic/combinatorics are exact; there is no floating point.
*/
#include <bits/stdc++.h>
using namespace std;
static inline uint32_t key3s(int a,int b,int c){int v[3]={a,b,c};sort(v,v+3);return (uint32_t(v[0])<<16)|(uint32_t(v[1])<<8)|uint32_t(v[2]);}
static inline uint32_t key4s(int a,int b,int c,int d){int v[4]={a,b,c,d};sort(v,v+4);return uint32_t(v[0])|(uint32_t(v[1])<<8)|(uint32_t(v[2])<<16)|(uint32_t(v[3])<<24);}
static inline array<int,3> dec3(uint32_t k){return {int(k>>16),int((k>>8)&255),int(k&255)};}
static inline array<int,4> dec4(uint32_t k){return {int(k&255),int((k>>8)&255),int((k>>16)&255),int(k>>24)};}
int main(){
 const int n=4,M=256;
 vector<array<unsigned char,16>> act(M); vector<array<unsigned char,4>> tr(M);
 for(int code=0;code<M;code++){int x=code;for(int i=0;i<4;i++){tr[code][i]=x&3;x>>=2;}for(int s=0;s<16;s++){int y=0;for(int i=0;i<4;i++)if(s>>i&1)y|=1<<tr[code][i];act[code][s]=y;}}
 auto sync=[&](const int*v,int k,int *distout=nullptr){signed char d[16];memset(d,-1,sizeof d);unsigned char q[16];int h=0,t=0;q[t++]=15;d[15]=0;while(h<t){int s=q[h++];if((s&(s-1))==0){if(distout)*distout=d[s];return true;}for(int j=0;j<k;j++){int z=act[v[j]][s];if(d[z]<0){d[z]=d[s]+1;q[t++]=z;}}}return false;};
 vector<array<int,4>> perms; array<int,4> p={0,1,2,3}; do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 int conj[24][256]; for(int pi=0;pi<24;pi++)for(int f=0;f<256;f++){
   int out[4]; for(int i=0;i<4;i++) out[perms[pi][i]]=perms[pi][tr[f][i]];
   int code=0,mul=1;for(int j=0;j<4;j++){code+=out[j]*mul;mul*=4;}conj[pi][f]=code;
 }
 auto can3=[&](int a,int b,int c){uint32_t best=UINT_MAX;for(int pi=0;pi<24;pi++)best=min(best,key3s(conj[pi][a],conj[pi][b],conj[pi][c]));return best;};
 auto can4=[&](int a,int b,int c,int d){uint32_t best=UINT_MAX;for(int pi=0;pi<24;pi++)best=min(best,key4s(conj[pi][a],conj[pi][b],conj[pi][c],conj[pi][d]));return best;};
 auto compose=[&](int f,int g){
   int code=0,mul=1; for(int i=0;i<4;i++){code+=tr[g][tr[f][i]]*mul;mul*=4;}return code;
 };
 auto in_monoid3=[&](int target,int a,int b,int c){bool seen[256]={};int q[256],h=0,t=0;int gens[3]={a,b,c};int id=0,mul=1;for(int i=0;i<4;i++){id+=i*mul;mul*=4;}seen[id]=1;q[t++]=id;while(h<t){int f=q[h++];if(f==target)return true;for(int g:gens){int z=compose(f,g);if(!seen[z]){seen[z]=1;q[t++]=z;}}}return false;};
 auto pair_escape=[&](int missing,int a,int b,int c){
   int gens[3]={a,b,c}; bool merge[4][4]{};
   for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){
     bool seen[16]={}; int q[16],h=0,t=0; int s=(1<<i)|(1<<j);seen[s]=1;q[t++]=s;bool ok=false;
     while(h<t){int x=q[h++];if((x&(x-1))==0){ok=true;break;}for(int g:gens){int z=act[g][x];if(!seen[z]){seen[z]=1;q[t++]=z;}}}
     merge[i][j]=ok;
   }
   int un=0; bool esc=false;
   for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(!merge[i][j]){un++;int x=tr[missing][i],y=tr[missing][j];if(x==y)esc=true;else{int lo=min(x,y),hi=max(x,y);if(merge[lo][hi])esc=true;}}
   return pair<int,bool>{un,esc};
 };
 vector<unsigned char> nons(1u<<24,0); unordered_set<uint32_t> base_orbits; base_orbits.reserve(10000); long long nonscnt=0;
 for(int a=0;a<256;a++)for(int b=a+1;b<256;b++)for(int c=b+1;c<256;c++){int v[3]={a,b,c};if(!sync(v,3)){nons[key3s(a,b,c)]=1;nonscnt++;base_orbits.insert(can3(a,b,c));}}
 vector<uint32_t> irre_labeled; map<int,long long> hist_lab;
 for(int a=0;a<253;a++)for(int b=a+1;b<254;b++)for(int c=b+1;c<255;c++){if(!nons[key3s(a,b,c)])continue;for(int d=c+1;d<256;d++){
   if(!nons[key3s(a,b,d)]||!nons[key3s(a,c,d)]||!nons[key3s(b,c,d)])continue;int v[4]={a,b,c,d},rt;if(sync(v,4,&rt)){irre_labeled.push_back(key4s(a,b,c,d));hist_lab[rt]++;}
 }}
 unordered_map<uint32_t,int> orbit_rt; long long semigroup_checks=0,pair_checks=0; int failures=0;
 for(uint32_t k:irre_labeled){auto v=dec4(k);int rt;int vv[4]={v[0],v[1],v[2],v[3]};sync(vv,4,&rt);uint32_t ck=can4(v[0],v[1],v[2],v[3]);auto it=orbit_rt.find(ck);if(it==orbit_rt.end())orbit_rt[ck]=rt;else if(it->second!=rt)failures++;
   for(int omit=0;omit<4;omit++){int w[3],j=0;for(int i=0;i<4;i++)if(i!=omit)w[j++]=v[i];semigroup_checks++;if(in_monoid3(v[omit],w[0],w[1],w[2]))failures++;auto pe=pair_escape(v[omit],w[0],w[1],w[2]);pair_checks++;if(pe.first==0||!pe.second)failures++;}
 }
 map<int,long long> hist_orb;for(auto &kv:orbit_rt)hist_orb[kv.second]++;
 unordered_set<uint32_t> gen_children; gen_children.reserve(orbit_rt.size()*2); long long aug_candidate_orbits=0,aug_alltrip_nons=0,aug_sync_irred=0;
 for(uint32_t tk:base_orbits){auto T=dec3(tk); vector<int> aut;for(int pi=0;pi<24;pi++){if(key3s(conj[pi][T[0]],conj[pi][T[1]],conj[pi][T[2]])==tk)aut.push_back(pi);}bool inT[256]={};for(int x:T)inT[x]=1;
   for(int d=0;d<256;d++)if(!inT[d]){int mn=d;for(int pi:aut)mn=min(mn,conj[pi][d]);if(d!=mn)continue;aug_candidate_orbits++;
     int s[4]={T[0],T[1],T[2],d};sort(s,s+4);bool all=true;for(int omit=0;omit<4;omit++){int w[3],j=0;for(int i=0;i<4;i++)if(i!=omit)w[j++]=s[i];if(!nons[key3s(w[0],w[1],w[2])]){all=false;break;}}if(!all)continue;aug_alltrip_nons++;
     int rt;if(sync(s,4,&rt)){aug_sync_irred++;gen_children.insert(can4(s[0],s[1],s[2],s[3]));}
   }
 }
 cout<<"N 4 TRANSFORMATIONS 256\n";
 cout<<"NONSYNC_DISTINCT_TRIPLES_LABELED "<<nonscnt<<"\n";
 cout<<"NONSYNC_TRIPLE_STATE_ORBITS "<<base_orbits.size()<<"\n";
 cout<<"IRREDUCIBLY_SYNC_DISTINCT_4SUPPORTS_LABELED "<<irre_labeled.size()<<"\n";
 cout<<"IRREDUCIBLY_SYNC_4SUPPORT_STATE_ORBITS "<<orbit_rt.size()<<"\n";
 cout<<"LABELED_RESET_HIST";for(auto [r,c]:hist_lab)cout<<" "<<r<<":"<<c;cout<<"\n";
 cout<<"ORBIT_RESET_HIST";for(auto [r,c]:hist_orb)cout<<" "<<r<<":"<<c;cout<<"\n";
 cout<<"MAX_RESET ";int maxrt=0;for(auto [k,r]:orbit_rt)maxrt=max(maxrt,r);cout<<maxrt<<"\n";
 cout<<"SEMIGROUP_IRREDUCIBILITY_CHECKS "<<semigroup_checks<<"\n";
 cout<<"PAIRTRAP_ESCAPE_CHECKS "<<pair_checks<<"\n";
 cout<<"CANONICAL_BASE_ORBITS "<<base_orbits.size()<<"\n";
 cout<<"AUT_QUOTIENT_AUGMENTATION_CANDIDATE_ORBITS "<<aug_candidate_orbits<<"\n";
 cout<<"AUG_ALL_TRIPLES_NONSYNC "<<aug_alltrip_nons<<"\n";
 cout<<"AUG_SYNC_IRRED_RAW "<<aug_sync_irred<<"\n";
 cout<<"AUG_UNIQUE_CHILD_STATE_ORBITS "<<gen_children.size()<<"\n";
 cout<<"BRUTE_UNIQUE_CHILD_STATE_ORBITS "<<orbit_rt.size()<<"\n";
 bool same=(gen_children.size()==orbit_rt.size()); if(same)for(auto &kv:orbit_rt)if(!gen_children.count(kv.first)){same=false;break;}
 cout<<"CANONICAL_AUGMENTATION_COVERAGE "<<(same?"PASS":"FAIL")<<"\n";
 cout<<"THEOREM_INVARIANT_CHECKS "<<(failures==0?"PASS":"FAIL")<<" failures="<<failures<<"\n";
 cout<<(same&&failures==0&&maxrt<=9?"ALL_EXACT_CHECKS_PASSED":"CHECK_FAILED")<<"\n";
}
