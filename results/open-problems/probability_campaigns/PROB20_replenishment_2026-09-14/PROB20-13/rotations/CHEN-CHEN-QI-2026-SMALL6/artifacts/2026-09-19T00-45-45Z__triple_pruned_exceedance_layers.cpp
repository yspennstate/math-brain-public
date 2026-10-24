#define main archived_n24_main
#include "2026-09-19T00-45-45Z__triple_pruned_matching_count.cpp"
#undef main
void init_data(){
 memset(comp,0,sizeof comp); memset(inc,0,sizeof inc); memset(ban,0,sizeof ban); C.clear(); G.clear();
 for(int r=0;r<6;r++)for(int c=0;c<6;c++)if(!inE(r,c))C.push_back({r,c});
 for(int i=0;i<20;i++)for(int j=i+1;j<20;j++)if(!hinge(C[i],C[j]))G.push_back({i,j});
 assert(G.size()==134);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j&&G[i][0]!=G[j][0]&&G[i][0]!=G[j][1]&&G[i][1]!=G[j][0]&&G[i][1]!=G[j][1])comp[i][j>>6]|=1ULL<<(j&63);
 for(auto &x:pb){comp[x[0]][x[1]>>6]&=~(1ULL<<(x[1]&63));comp[x[1]][x[0]>>6]&=~(1ULL<<(x[0]&63));}
 for(int v=0;v<N;v++)for(int q=0;q<2;q++)inc[G[v][q]][v>>6]|=1ULL<<(v&63);
 for(auto &x:tb)for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){int k=3-i-j;ban[x[i]][x[j]][x[k]>>6]|=1ULL<<(x[k]&63);ban[x[j]][x[i]][x[k]>>6]|=1ULL<<(x[k]&63);}
}
pair<I,I> count_layer(int e,int h){U av[3]={~0ULL,~0ULL,(1ULL<<6)-1};vector<int>s;I a=go((1u<<20)-1,av,s,e,h,0),b=go((1u<<20)-1,av,s,e,h,1);return {a,b};}
int main(){
 init_data(); auto n25=count_layer(9,2); auto n26=count_layer(10,0);
 assert(n25.first==I(172923632) && n25.second==I(156635384));
 assert(n26.first==I(10893528) && n26.second==I(9468448));
 cout<<"N25_PAIRWISE_ONLY="<<out(n25.first)<<"\nN25_AFTER_TRIPLE="<<out(n25.second)<<"\nN25_REMOVED="<<out(n25.first-n25.second)<<"\n";
 cout<<"N26_PAIRWISE_ONLY="<<out(n26.first)<<"\nN26_AFTER_TRIPLE="<<out(n26.second)<<"\nN26_REMOVED="<<out(n26.first-n26.second)<<"\nALL_EXACT_EXCEEDANCE_COUNTS_PASS\n";
}
