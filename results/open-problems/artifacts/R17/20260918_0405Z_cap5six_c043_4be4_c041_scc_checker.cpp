#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;
struct Frame{uint32_t u; uint8_t j;};
int main(int argc,char**argv){string f=argc>1?argv[1]:"/mnt/data/c041_product.bin";int fd=open(f.c_str(),O_RDONLY);if(fd<0){perror("open");return 2;}struct stat st;fstat(fd,&st);const int D=30;size_t N=st.st_size/(D*4);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);cerr<<"N="<<N<<"\n";
vector<uint32_t> disc(N,0),low(N),parent(N,UINT32_MAX),comp(N,UINT32_MAX),S;S.reserve(N);vector<uint8_t> on(N,0),self(N,0);vector<Frame> F;F.reserve(1000000);uint32_t tim=0,cid=0;vector<uint32_t> csz;vector<uint8_t> cyc;csz.reserve(100000);cyc.reserve(100000);
for(uint32_t root=0;root<N;root++) if(!disc[root]){disc[root]=low[root]=++tim;parent[root]=UINT32_MAX;S.push_back(root);on[root]=1;F.push_back({root,0});while(!F.empty()){Frame &fr=F.back();uint32_t u=fr.u;if(fr.j<D){uint32_t q=tr[(size_t)u*D+fr.j++];if(!q)continue;uint32_t v=q-1;if(v==u)self[u]=1;if(!disc[v]){parent[v]=u;disc[v]=low[v]=++tim;S.push_back(v);on[v]=1;F.push_back({v,0});}else if(on[v]) low[u]=min(low[u],disc[v]);continue;}F.pop_back();uint32_t p=parent[u];if(p!=UINT32_MAX) low[p]=min(low[p],low[u]);if(low[u]==disc[u]){uint32_t sz=0;bool iscy=false;while(1){uint32_t v=S.back();S.pop_back();on[v]=0;comp[v]=cid;sz++;if(self[v])iscy=true;if(v==u)break;}if(sz>1)iscy=true;csz.push_back(sz);cyc.push_back(iscy);cid++;}}
if((root+1)%1000000==0)cerr<<"root="<<root+1<<" time="<<tim<<" comps="<<cid<<"\n";}
uint64_t cycstates=0;uint32_t maxsz=0,maxc=0,ncyc=0;for(uint32_t c=0;c<cid;c++){if(cyc[c]){ncyc++;cycstates+=csz[c];}if(csz[c]>maxsz){maxsz=csz[c];maxc=c;}}
vector<pair<uint32_t,uint32_t>> top;for(uint32_t c=0;c<cid;c++)top.push_back({csz[c],c});sort(top.rbegin(),top.rend());cout<<"components="<<cid<<" cyclic_components="<<ncyc<<" cyclic_states="<<cycstates<<" largest_component="<<maxsz<<" largest_component_id="<<maxc<<"\n";for(int i=0;i<min<int>(20,top.size());i++)cout<<"top"<<i+1<<" size="<<top[i].first<<" id="<<top[i].second<<" cyclic="<<(int)cyc[top[i].second]<<"\n";
uint64_t in=0,out=0,internal=0;unordered_set<uint32_t> outc,inc;outc.reserve(1000);inc.reserve(1000);for(uint32_t u=0;u<N;u++){uint32_t cu=comp[u];for(int j=0;j<D;j++){uint32_t q=tr[(size_t)u*D+j];if(!q)continue;uint32_t v=q-1,cv=comp[v];if(cu==maxc&&cv==maxc)internal++;else if(cu==maxc){out++;outc.insert(cv);}else if(cv==maxc){in++;inc.insert(cu);}}}cout<<"largest_internal_edges="<<internal<<" incoming_edges="<<in<<" incoming_components="<<inc.size()<<" outgoing_edges="<<out<<" outgoing_components="<<outc.size()<<"\n";
}
