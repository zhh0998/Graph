## 基本概念
**图**是互连节点的集合，节点`node`通过边`edge`连接，由`G=(V, E)`表示  
> Edges can be `directed`、`weighted`  
> Nodes and edges can have `types` and `metadata`  
> 图可用于表示**Social networks**、**Collaboration networks**、**Transportation networks**、**Computer networks**、**Connectomics**等  
> Properties of real-world graphs: `big`、`sparse`、`degrees can be highly skewed/a power law degree distribution`

**相关术语**  
> 完备`complete`图：一个图的所有节点都有`n-1`个相邻节点，也就是说所有节点都具备所有可能的连接方式  
> 从`i`到`j`的路径`path`是指从`i`到达`j`的边的序列，该路径的长度`length`等于所经过的边的数量  
> 图的直径`diameter`是指连接任意两个节点的所有最短路径中最长路径的长度
> 测地路径`geodesic path`是指两个节点之间的最短路径  
> 如果所有节点都可通过某个路径连接到彼此，则它们构成一个连通分支`connected component`。如果一个图仅有一个连通分支，则该图是连通的`connected`  
> 如果一个图的边是有顺序的配对，则该图是有向的`directed`。`i`的入度`in-degree`是指向`i`的边的数量，出度`out-degree`是远离`i`的边的数量  
> 如果可以回到一个给定节点，则该图是有环的`cyclic`。相对地，如果至少有一个节点无法回到，则该图就是无环的`acyclic`  
> 图可以被加权`weighted`，即在节点或关系上施加权重  
> 如果一个图的边数量相比于节点数量较小，则该图是稀疏的`sparse`。相对地，如果节点之间的边非常多，则该图是密集的`dense`

**Social Network**  
> A social network is a graph made up of: a set of `individuals`, called “nodes”, and tied by one or more `interdependency`, such as friendship, called “edges”  
`Social Network Analysis`
- Community Detection
- Influence Maximization
- Link Prediction
- Network Evolution
- Network Embedding
- Deep Learning for Networks

**Dynamic Network**  
> networks are dynamic in nature  
> changes are smooth  
> edges and nodes arrive over time



## 图算法
### Pathfinding（寻路）
确定最优路径  
> `Breadth-First Search(BFS)` requires O(n+m) work on n vertices and m edges  
> `Depth-First Search(DFS)` requires O(n+m) work on n vertices and m edges

### Centrality（中心性）
确定网络中节点的重要性

### Community detection（社区检测）
评估群体聚类的方式

## 图表征
- `edge list`存储有边连接的每一对节点的ID
- `adjacency matrix`通常是在内存中加载的方式
- `adjacency list`
- `compressed sparse row (CSR)`需要两个数组Offsets和Edges  
![tradeoff-gr](https://github.com/Qingfeng-Yao/Graph/blob/master/images/tradeoff-gr.png)

## 图嵌入
**Problem** `Representation Learning for Networks` `Graph Representation Learning` `Network Embedding` `Graph Embedding`
**Tasks**  
- Node classification
- Link prediction
- Community detection  

**Includings** `Node Embedding` `Edge Embedding` `(sub)Graph Embedding`

### Node Embedding
**static graph setting**  
`Goal`: encode structural and content information  
- shallow embedding
> matrix factorization  
> random walk
- deep embedding
> neighborhood autoencoder  
> neighborhood aggregation 

**dynamic graph setting**  
`Goal`: encode evolving graph information  
- 直接添加时序信息  
- 先对动态过程建模，再利用模型encode

`evolving graph information`  
- global perspective  
> structures of dynamic graphs continue evolving since new nodes and edges are constantly introduced, which is dynamics of the graph(DOFG)  
> discrete-time/snapshot 
- local perspective  
> a node can keep establishing new edges, which is dynamics on the graph(DONG)  
> continuous-time

### 参考文献
#### Overview
2018 WWW Tutorial [Representation Learning on Networks](http://snap.stanford.edu/proj/embeddings-www/) William L. Hamilton, Rex Ying and Jure Leskovec

2019 WWW Tutorial [Representation Learning on Networks: Theories, Algorithms, and Applications](https://www.aminer.cn/nrl_www2019) Jie Tang and Yuxiao Dong

2019 KDD Workshop [Perspectives and Outlook on Network Embedding and GCN](http://pengcui.thumedialab.com/papers/Perspectives%20on%20NE%20and%20GCN_Peng.pdf) Peng Cui 

2019 KDD Tutorial [Learning From Networks ——Algorithms, Theory, & Applications](http://pengcui.thumedialab.com/papers/KDD19%20Tutorial%20on%20NE_Peng.pdf) Peng Cui

2017 IEEE [Representation Learning on Graphs: Methods and Applications](https://arxiv.org/pdf/1709.05584.pdf) William L. Hamilton, Rex Ying and Jure Leskovec

2017 [Graph Embedding Techniques, Applications, and Performance: A Survey](https://arxiv.org/pdf/1705.02801.pdf) Palash Goyal and Emilio Ferrara

#### Edge Embedding
2017 KDD [metapath2vec: Scalable representation learning for heterogeneous networks](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf) Yuxiao Dong, Nitesh V. Chawla and Ananthram Swami

#### (sub)Graph Embedding
2018 AAAI [Link prediction via subgraph embedding-based convex matrix completion](http://iiis.tsinghua.edu.cn/~weblt/papers/link-prediction-subgraphembeddings.pdf) Zhu Cao, Linlin Wang, and Gerard de Melo







