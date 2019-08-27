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
- structure  
- attribute  
- evolution pattern

`time`  
- discrete-time/snapshot   
> loss of information between snapshots, lack of ability to capture fine-grained temporal dynamics, the selection of appropriate aggregation granularity which is often misspecified   
- continuous-time/finer time granularity

### 参考文献
#### Overview
2018 WWW Tutorial [Representation Learning on Networks](http://snap.stanford.edu/proj/embeddings-www/) William L. Hamilton, Rex Ying and Jure Leskovec

2017 [Representation Learning on Graphs: Methods and Applications](https://arxiv.org/pdf/1709.05584.pdf) William L. Hamilton, Rex Ying and Jure Leskovec

2019 WWW Tutorial [Representation Learning on Networks: Theories, Algorithms, and Applications](https://www.aminer.cn/nrl_www2019) Jie Tang and Yuxiao Dong 

2019 KDD Workshop [Perspectives and Outlook on Network Embedding and GCN](http://pengcui.thumedialab.com/papers/Perspectives%20on%20NE%20and%20GCN_Peng.pdf) Peng Cui 

2019 KDD Tutorial [Learning From Networks ——Algorithms, Theory, & Applications](http://pengcui.thumedialab.com/papers/KDD19%20Tutorial%20on%20NE_Peng.pdf) Peng Cui

2017 [A Survey on Network Embedding](https://arxiv.org/pdf/1711.08752.pdf) Peng Cui, Xiao Wang, Jian Pei and Wenwu Zhu  
> structure-preserving methods and property-preserving methods

2017 [Graph Embedding Techniques, Applications, and Performance: A Survey](https://arxiv.org/pdf/1705.02801.pdf) Palash Goyal and Emilio Ferrara

#### Matrix Factorization
2001 [Laplacian eigenmaps and spectral techniques for embedding and clustering](http://web.cse.ohio-state.edu/~belkin.8/papers/LEM_NIPS_01.pdf) Mikhail Belkin and Partha Niyogi

2015 CIKM [Grarep: Learning graph representations with global structural information](https://www.researchgate.net/profile/Qiongkai_Xu/publication/301417811_GraRep/links/5847ecdb08ae8e63e633b5f2/GraRep.pdf) Shaosheng Cao, Wei Lu, and Qiongkai Xu

#### Random Walk
2014 KDD [Deepwalk: online learning of social representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf) Bryan Perozzi, Rami Alrfou, and Steven Skiena  
> 新节点表示

2015 WWW [Line: Large-scale information network embedding](http://www.www2015.it/documents/proceedings/proceedings/p1067.pdf) Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, and Qiaozhu Mei  
> 新节点表示

2016 KDD [node2vec: Scalable feature learning for networks](https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf) Aditya Grover and Jure Leskovec

#### Autoencoder
2016 KDD [Structural deep network embedding](https://www.kdd.org/kdd2016/papers/files/rfp0191-wangAemb.pdf) Daixin Wang, Peng Cui and Wenwu Zhu

2016 AAAI [Deep neural networks for learning graph representations](https://pdfs.semanticscholar.org/1a37/f07606d60df365d74752857e8ce909f700b3.pdf) Shaosheng Cao, Wei Lu and Qiongkai Xu

#### GNN
2014 ICLR [Spectral networks and locally connected networks on graphs](https://arxiv.org/pdf/1312.6203.pdf) Joan Bruna, Wojciech Zaremba, Arthur Szlam and Yann LeCun

2015 NIPS [Convolutional networks on graphs for learning molecular fingerprints](https://arxiv.org/pdf/1509.09292.pdf) David Duvenaud, Dougal Maclaurin, Jorge Aguilera-Iparraguirre, Rafael Gomez-Bombarelli, Timothy Hirzel, Alan Aspuru-Guzik and Ryan P. Adams

2016 NIPS [Convolutional neural networks on graphs with fast localized spectral filtering](https://arxiv.org/pdf/1606.09375.pdf) Michael Defferrard, Xavier Bresson and Pierre Vandergheynst

2016 ICLR [Gated graph sequence neural networks](https://arxiv.org/pdf/1511.05493.pdf) Yujia Li, Daniel Tarlow, Marc Brockschmidt and Richard Zemel
 
2017 NIPS [Inductive representation learning on large graphs](https://papers.nips.cc/paper/6703-inductive-representation-learning-on-large-graphs.pdf) William L. Hamilton, Rex Ying and Jure Leskovec

2017 ICML [Neural message passing for quantum chemistry](https://arxiv.org/pdf/1704.01212.pdf) Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals and George E. Dahl

2017 ICLR [Semi-supervised classification with graph convolutional networks](https://arxiv.org/pdf/1609.02907.pdf) Thomas N. Kipf and Max Welling  
> GCN

2017 NIPS [Predicting organic reaction outcomes with Weisfeiler-Lehman network](https://arxiv.org/pdf/1709.04555.pdf) Wengong Jin, Connor W. Coley, Regina Barzilay and Tommi Jaakkola

2018 ICLR [FastGCN: Fast learning with graph convolutional networks via importance sampling](https://arxiv.org/pdf/1801.10247.pdf) Jie Chen, Tengfei Ma and Cao Xiao

2018 ICLR [Graph attention networks]() Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio and Yoshua Bengio

#### Edge Embedding
2017 KDD [metapath2vec: Scalable representation learning for heterogeneous networks](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf) Yuxiao Dong, Nitesh V. Chawla and Ananthram Swami

#### (sub)Graph Embedding
2018 AAAI [Link prediction via subgraph embedding-based convex matrix completion](http://iiis.tsinghua.edu.cn/~weblt/papers/link-prediction-subgraphembeddings.pdf) Zhu Cao, Linlin Wang, and Gerard de Melo

#### Dynamic embedding
2016 TKDE [Scalable Temporal Latent Space Inference for Link Prediction in Dynamic Social Networks](https://arxiv.org/pdf/1411.3675.pdf) Linhong Zhu, Dong Guo, Junming Yin, Greg Ver Steeg and Aram Galstyan [code](https://github.com/linhongseba/Temporal-Network-Embedding)  
> BCGD

2017 CIKM [Attributed Network Embedding for Learning in a Dynamic Environment](https://arxiv.org/pdf/1706.01860.pdf) Jundong Li, Harsh Dani, Xia Hu, Jiliang Tang, Yi Chang and Huan Liu  
> DANE

2017 ICML [Know-Evolve: Deep Temporal Reasoning for Dynamic Knowledge Graphs](https://arxiv.org/pdf/1705.05742.pdf) Rakshit Trivedi, Hanjun Dai, Yichen Wang and Le Song [code](https://github.com/rstriv/Know-Evolve)  
> Know-Evolve

2018 WWW [Continuous-Time Dynamic Network Embeddings](http://ryanrossi.com/pubs/nguyen-et-al-WWW18-BigNet.pdf) Giang Hoang Nguyen, John Boaz Lee, Ryan A. Rossi, Nesreen K. Ahmed, Eunyee Koh and Sungchul Kim  
> CTDNE

2018 [Streaming Graph Neural Networks](https://arxiv.org/pdf/1810.10627.pdf) Yao Ma, Ziyi Guo, Zhaochun Ren, Eric Zhao, Jiliang Tang and Dawei Yin  
> DGNN

2018 TKDE [High-order Proximity Preserved Embedding For Dynamic Networks](http://pengcui.thumedialab.com/papers/High-orderDynamic.pdf) Dingyuan Zhu, Peng Cui, Ziwei Zhang, Jian Pei and Wenwu Zhu  
> DHPE

2018 IJCAI [Dynamic Network Embedding :An Extended Approach for Skip-gram based Network Embedding](https://www.ijcai.org/proceedings/2018/0288.pdf) Lun Du, Yun Wang, Guojie Song, Zhicong Lu and Junshan Wang  
> DNE

2018 AAAI [Dynamic Network Embedding by Modeling Triadic Closure Process](http://yangy.org/works/dynamictriad/dynamic_triad.pdf) Lekui Zhou, Yang Yang, Xiang Ren, Fei Wu and Yueting Zhuang [code](https://github.com/luckiezhou/DynamicTriad)  
> DynamicTriad

2018 [DynGEM: Deep Embedding Method for Dynamic Graphs](https://arxiv.org/pdf/1805.11273.pdf) Palash Goyal, Nitin Kamra, Xinran He and Yan Liu [code](https://github.com/palash1992/DynamicGEM)  
> DynGEM

2018 [dyngraph2vec: Capturing Network Dynamics using Dynamic Graph Representation Learning](https://arxiv.org/pdf/1809.02657.pdf) Palash Goyal, Sujit Rokka Chhetri and Arquimedes Canedo [code](https://github.com/palash1992/DynamicGEM)  
> dyngraph2vec

2018 KDD [Embedding Temporal Network via Neighborhood Formation](http://shichuan.org/hin/topic/Embedding/2018.KDD%202018%20Embedding%20Temporal%20Network%20via%20Neighborhood%20Formation.pdf) Yuan Zuo, Guannan Liu, Hao Lin, Jia Guo, Xiaoqian Hu and Junjie Wu  
> HTNE

2018 KDD [NetWalk: A Flexible Deep Embedding Approach for Anomaly Detection in Dynamic Networks](http://shichuan.org/hin/time/2018.KDD%202018%20NetWalk_A%20Flexible%20Deep%20Embedding%20Approach%20for%20Anomaly%20Detection%20in%20Dynamic%20Networks.pdf) Wenchao Yu, Wei Cheng, Charu C. Aggarwal, Kai Zhang, Haifeng Chen and Wei Wang  
> NetWalk

2018 AAAI [TIMERS: Error-Bounded SVD Restart on Dynamic Networks](https://arxiv.org/pdf/1711.09541.pdf) Ziwei Zhang, Peng Cui, Jian Pei, Xiao Wang and Wenwu Zhu [code](https://github.com/palash1992/DynamicGEM)  
> TIMERS

2019 IJCAI [Large Scale Evolving Graphs with Burst Detection](http://keg.cs.tsinghua.edu.cn/jietang/publications/IJCAI19-Zhao-et-al-Evolving_Graphs_with_Burst_Detection.pdf) Yifeng Zhao, Xiangwei Wang, Hongxia Yang, Le Song and Jie Tang  
> BurstGraph

2019 ICLR [DyRep: Learning Representations over Dynamic Graphs](https://openreview.net/pdf?id=HyePrhR5KX) Rakshit Trivedi, Mehrdad Farajtabar, Prasenjeet Biswal and Hongyuan Zha  
> DyRep
 
#### Dynamic + GNN
2016 [Structured sequence modeling with graph convolutional recurrent networks](https://arxiv.org/pdf/1612.07659.pdf) Youngjoo Seo, Michael Defferrard, Pierre Vandergheynst and Xavier Bresson

2017 [Dynamic graph convolutional networks](https://arxiv.org/pdf/1704.06199.pdf) Franco Manessia, Alessandro Rozza and Mario Manzo

2018 [Learning graph dynamics using deep neural networks](https://www.sciencedirect.com/science/article/pii/S2405896318300788) Apurva Narayan and Peter H. O’N Roe

2019 [EvolveGCN: Evolving Graph Convolutional Networks for Dynamic Graphs](https://arxiv.org/pdf/1902.10191.pdf) Aldo Pareja, Giacomo Domeniconi, Jie Chen, Tengfei Ma, Toyotaro Suzumura, Hiroki Kanezashi, Tim Kaler and Charles E. Leisersen












