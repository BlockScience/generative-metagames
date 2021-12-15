# Exploring MAIDs as a Family of Process DAGs

In our research on [generative metagames](https://hackmd.io/@mzargham/Hyrah379K), the "statespace" is an instance of a multi-agent influence diagram, or MAID. In order to proceed with that work, it is necessary to understand the nature of a point in that space, an instance of a MAID. In this note I work through the Killer Tree example from Koller and Milch (Koller, D. and B. Milch, 2003, "[Multi-agent influence diagrams for representing and solving games](https://doi.org/10.1016/S0899-8256(02)00544-4)", Games and Economic Behavior 45(1), pp. 181-221), in order to refine my understanding of the space of MAIDs.

## MAIDs notation

In instance of a multi-agent influence diageam and defined by Koller and Milch is a directed acyclic graph (DAG) made up of:


| Term | Notation | Visual Symbol |
| -------- | -------- | -------- |
| Agents     |   $a\in \mathcal{A}$   | color |
| Chance Variables | $x\in\mathcal{X}$ | ovals |
| Decision Variables | $d\in \mathcal{D}$ | rectangles|
| Agent's Decision Variables | $d_a \in \mathcal{D}_a\subset \mathcal{D}$ | rectangles|
| Utility Variables | $u\in \mathcal{U}$ | diamonds|
| Agent's Utility Variables | $u_a \in \mathcal{U}_a\subset \mathcal{U}$ | diamonds|

![](https://i.imgur.com/W9IMsxU.png)

### Observations

Exploring some different perspectives on this mathematical object I've made some preliminary observations.

#### Agents Utilities are Decomposed

This decomposition leaves agents with a multi-criterion optimization if we do not provide a "total" utility function which is some aggregation over their respective outcomes. In the simple examples provided it's prudent to simply normalize units of "cost" (such as time, money and effort) with units of value in the payoff matrix so that we can use simple addition to aggregate payoffs. However, there are definitely richer dynamic games where more complex aggregation operations would be required, including but not limited to products, $\max$ or $\min$. It is understood that these aggregations will affect the tractability of their respective optimization probems. 

![](https://i.imgur.com/yryEAUR.png)


#### Partially Ordered Stage Game

By focusing on the relationships between the chance processes, one can identify a variation of _stage game_. Stage games generally have strictly ordered stages whereas a MAID is capable of representing games which do not have strictly ordered stages. This is an area of particular interest because there are two very different approaches to implementing MAIDs. In variant 1, a particular strict ordering on the stages is imposed (which is one of a set of strict ordering satisfying the partial ordering implied by the DAG). In this case the choice of ordering may (or may not) have an impact on the outcome of the game. In variant 2, the agent's action space includes when to exercise their decision process in addition to which decision to take. In this case the precise ordering of events may be determined (and differ) for different instantiations of the same MAID. 

It is however, my conjecture that the explicit inclusion of the observational edges (to determine what can and cannot be observed by the agents to inform their decisions) already forces us into variant 1, but I am interested in what would happen if the model were relaxed enough to explore variant 2.

![](https://i.imgur.com/Fp7TQIp.png)



## Killer Tree Example

Inititally I directly transcribed the Killer Tree MAID from Koller and Milch, but shifted the node placement around in order to gain some intuition about the more general family of MAID network topologies.
![](https://i.imgur.com/S0LBTIM.png)


### Killer Tree in Subgraph Form
I reorganized the Killer Tree example into subgraphs with distinct properties:

![](https://i.imgur.com/IioTVXe.png)

The subgraphs in this model are as follows
- Decisions of Alice
    - decisions of Alice can be strictly ordered (using the observation edges)
    - decisions of Alice are Observable to Alice (but not to Bob)
    - decisions of Alice have causal effects on the Chance Processes
    - decisions of Alice have causal effects on the Utility Processes of Alice (but not *directly* Bob's)
- Decisions of Bob
    - decisions of Bob are Observable Bob (but not to Alice)
    - decisions of Bob have causal effects on the Chance Processes
    - decisions of Bob have causal effects on the Utility Processes of Bob (but not *directly* on Alice's)
- Chances Processes
    - chance processes may depend on one or more of the agents decision processes
    - outcomes of chance processes may or may not be observable any one or more agents
    - the subgraph of chance processes provides insight into the flow of the game even without knowing the agents decisions
- Utilities of Alice
    - utilities of Alice (may) depend directly on Alice's decisions (causal links are allowed but not required)
    - utilities of Alice (may) depend directly on chance processes (causal links are allowed but not required)
    - utilties of Alice do not depend directly on Bob's decisions (causal links are disallowed)
- Utilities of Bob
    - utilities of Bob (may) depend directly on Bob's decisions (causal links are allowed but not required)
    - utilities of Bob (may) depend directly on chance processes (causal links are allowed but not required)
    - utilties of Bob do not depend directly on Alices's decisions (causal links are disallowed)
### Killer Tree in Stages

Taking the union of the Alice's Decisions and Bob's Decisions with the chance processes subgraph, there is a strict ordering of events. The subgraph made up of the utilities has no outbound edges to the complementary subgraph of the MAID; therefore, we can compute them as soon as the relevant information becomes available, or after the completion of the games, or at any point in between and it will not affect their values, or the outcome of the game.

![](https://i.imgur.com/3tmD1LB.png)


#### Killer Tree Critical Path
1.  Poison the Tree
    - Decision Process
    - Agent Alice
    - output: $d_1\in\{0,1\}$
2. Tree Sick
    - Chance Process
    - output: $x_2\in\{0,1\}$
3. Tree Doctor
    - Decision Process
    - Agent: Bob
    - output: $d_3\in\{0,1\}$
4. Build Patio
    - Decision Process
    - Agent: Alice
    - output: $d_4\in\{0,1\}$
5. Tree Dies
    - Chance Process
    - output: $x_5\in\{0,1\}$

Note that the strict ordering includes the fact that Alice cannot observe whether the tree has died before deciding whether to build the patio. In this case, it's the absence of the observation edge between the Tree Dies chance process and the Build Patio Decision process which determines the ordering of 4 and 5.

#### Evaluating the Payoffs


Alice's Utilities
| Utility Process | Input variable(s) | Input |  Output | parameter(s)|
| -------- | -------- | -------- | ------| ----- |
| Effort | Poison Tree ($d_1$) |  $d_1\in\{0,1\}$    | $-e\cdot d_1$  | $e \in\mathbb{R}_+$|
| View | Tree Dead ($x_5$) and Build Patio ($d_4$) | $\left [\begin{array}{c}x_5\\ d_4\end{array}\right] \in \{0,1\}^2$ | $\left [\begin{array}{c}x_5 & 1- x_5\end{array}\right]V\left [\begin{array}{c}d_4\\ 1-d_4\end{array}\right]$ | $V\in \mathbb{R}^{2\times 2}$

Total utility for Alice
$$ u_a(d_1, d_4,x_5) =  \left [\begin{array}{c}x_5 & 1- x_5\end{array}\right]V\left [\begin{array}{c}d_4\\ 1-d_4\end{array}\right]-e\cdot d_1$$

Bob's Utilities
| Utility Process | Input variable(s) | Input |  Output | parameter(s)|
| -------- | -------- | -------- | ------| ----- |
| Cost | Tree Doctor ($d_3$) |  $d_3\in\{0,1\}$    | $-c\cdot d_3$  | $c \in\mathbb{R}_+$|
| Tree | Tree Dead ($x_5$) | $x_5 \in \{0,1\}$ | $t\cdot (1-x_5)$  | $t \in\mathbb{R}_+$|$

Total utility for Bob
$$ u_b(d_3,x_5) =  t\cdot (1-x_5)-c\cdot d_3$$

#### Considerations on Agent Strategies

Players within this game cannot develop strategies which manifest as decision rules for their decision processes conditioned on the information they have observed at the stage of the game that the decision must be made. In order to develop a strategy, a player should have its payoff parameter and at minimum a statistical model of the chance processes (even if those models are wrong).

## MAIDs are special cases of DAGs

Maids are specifically directed acyclic graphs (DAGs). The networks which represent MAIDs have additional structure:

There are 3 types of nodes:
* **Decision Processes**
    * which produce decision variables as outputs
    * Rectangles in figures
* **Chance Processes**, 
    * which produce chance variables as outputs
    * ovals in figures
* **Utility Processes**, 
    * which produce utility variables as outputs
    * diamonds in figures

There are 2 types of edges:
* **Causal Relationships**: 
    * inbound links pointing to Chance Processes or Utility processes representing functional dependence of the child process on the output of the parent process
    * solid lines in figures
* **Observational Relationships**: 
    * inbound links pointing to decision processes representing information the decision making agent is privy to; an agent may nonetheless choose not to condition their behavior on the observed signal
    * dotted lines in figures

It is prudent to further characterize the *Agent* dimension, as Decision process and Utility processes can be said to belong to agents. An agent will develop a strategy over its collection of decision processes in order to maximize some aggregate of its utility processes. The agent dimension, when appropriate, is indicated via color.


### 2-Agent View

A simple subgraph representation of a 2-player MAID is presented. Note that edges in the abstract diagram represent that links are allowed between the subgraphs, not that every such edge is present.

![](https://i.imgur.com/OyyoHe4.png)

### $n$-Agent View

A generalization of the subgraph representation for an  n-player MAID is presented. Note that edges in the abstract diagram represent that links are allowed between the subgraphs, not that every such edge is present.

![](https://i.imgur.com/KtJhcGv.png)

## Some Next steps

- Implement Killer Tree repeated game in cadCAD
- MAIDs as repeated games
    - learning models of the chance processes through play
    - learning models of the other agents through play
    - what are optimal strategies for players in MAIDs?
- Explore "metagame" moves which mutate the MAID network rather than play within it
    - What does the move space for a game miner look like in the case of a repeated MAID
    - what does do strategies for game miners (metagame players) look like
    - are there stable MAIDs which are (meta)stable under metagaming?


