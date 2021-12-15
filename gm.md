# Generative Metagames

Consider a family of Generalized Dynamical Systems whose statespace is comprised of processes (interpretable as ongoing dynamic games). We will consider moves in the generative metagame to be "game mining" actions as in Bono and Wolpert [Bono, J.W. and Wolpert, D.H. (2014), "[Game Mining: How to Make Money from those about to Play a Game](https://doi.org/10.1108/S1529-213420140000018009)", Entangled Political Economy (Advances in Austrian Economics, Vol. 18), Emerald Group Publishing Limited, Bingley, pp. 179-211]. That is to say that we move to a new point in the statespace, a new process (interpretable as another ongoing dynamic game).

## Generalized Dynamical Systems

A quick recap on generalized dynamic systems (GDS) for the purpose of defining generative metagames (GM).

### Statespace

A generalized dynamical system has a statespace $\mathcal{X}$ which can be thought of as an abstract class with points $x\in\mathcal{X}$ representing instances of that abstract class. There are no _a priori_ limitations on the nature of the space $\mathcal{X}$ and for the purpose of our work on generative metagames, the statespace $\mathcal{X}$ is that of structured processes which are themselves representative of games.

### State Update Map

A generalized dynamical system has one or more methods $f$ through which the prior state $x$ may be transformed into a posterior state $x^+$, which must also satisfy $x^+\in \mathcal{X}$.

$$x^+ = f(x,u) $$

However, the state update is not deterministic, it is contingent on stochastic and/or strategic inputs $u \in \mathcal{U}$. Note that the method $f(x,u)$ has an explicit domain:  
$$\mathcal{U}= \bigcup_{x\in \mathcal{X}} U(x)$$

but that for any particular point in the $x\in \mathcal{X}$ the input  $u\in U(x) \subseteq \mathcal{U}$. The set $U(x)$ is called the admissible input space (and when considering agents playing games we refer to it as the admissible action space). It exists precisely to enforce
$$ f(x,u) \in \mathcal{X}$$

thus prior to defining boundary conditions and/or decision making polices which provide $u\in U(x) := \{u\in\mathcal{U} | f(x,u)\in \mathcal{X} \}$, a GDS is essentially a discrete time differential inclusion in the statespace $\mathcal{X}$.

In the case of generative metagames, a player *evolves* the game by introducing new mechanism(s) which compose(s) with the existing mechanisms.

### Characterizing The Inputs

One role of the inputs is to keep track of stochastic processes which represent information incident on the system from *outside*. These processes are generically denoted:

$$u=g(x)\in U(x)$$

For example, flipping a coin to determine the outcome of a chance process: 
$$u \sim \hbox{Bernoulli}(p)$$

They may also be used to encode the dynamics of a physical process, such as the solar energy incident upon an array of panels. In the later case, we often use the term *environmental process*. Although it would be possible to model environmental processes in detail, it is often best to simply factor them out and treat them as exogenous to the dynamics. 

The really interesting inputs are *endogenous*, for example the case of strategic activity on the part of agents playing games. Agent admissible action spaces may be denoted

$$U_a(x) \subset U(x) \subset \mathcal{U}$$

where $u_a \in U_a(x)$ is a **decision variable** determined by agent $a \in \mathcal{A}$ while the system is in state $x$ (for some set of agents $\mathcal{A}$). This results in the state transition

$$x^+ = f(x, u_a)\in \mathcal{X}$$

In any particular system there may be a lot of structure encoded in $f$, and in $\mathcal{X}$, players may have local state variables $x_a \subset x$, and the mechanisms available to the agents $a\in\mathcal{A}$ may be differentiated.

### Strategic Behavior

Suppose we have a strategic agent $a \in \mathcal{A}$ with some admissible action space $U_a(x)$ for all $x\in\mathcal{X}$. Let the action of $a$ be given by

$$u_a = g_a(x)$$

but suppose there is some additional nondeterminism caused by other players and stochastic processes denoted 

$$u_b = g_b(x)$$

such that

$$x^+ = f_b\big(f_a(x, u_a ), u_b\big).$$

This implies that agent $a$ does not have certainty over the consequeces of their choice $u_a \in U_a(x)$ on the state transition to $x^+$. 

However, let us assume that agent $a$ is _optimizing_ for their own payoff, denoted 

$$J_a\left(\{(x,u_a)_t| t\in \mathbb{N}\}\right)$$

where $\{(x,u_a)_t| t\in \mathbb{N}\}$ denotes the trajectory of the state $x$ through the statespace $\mathcal{X}$ and $u_a$ are the actions taken by $a$. For example, in keeping with the Dynamic Programming literature, we would generally expect the dynamic optimization objective to be comprised of the negative of a rewards function dependent on $x$ and a cost function denoting the resources expended in taking actions $u_a$.

Therefore the optimal behavior of agent $a$ is denoted by

$$
\DeclareMathOperator*{\argmin}{argmin}
(u_t, u_{t+1}, \ldots) = \argmin_{\{u_\tau\in U_a(x_\tau) | \tau \ge t \}} J_a\left(\{(x,u_a)_\tau| \tau\ge t\}\right) 
$$
and $u_t = g_a(x_t)$ is precisely the first action $u_t\in U(x_t)$ in the sequence of actions $\{u_\tau| \tau\ge t\}$ minimizing $J_a$. Keep in mind that this discussion is simplifed as we've not gone into any details regarding how the (unknown) non-determinsm of $u_b=g_b(x)$ is handled in solving for $g_a(x)$. Two points of further literature reviews are differential games (e.g. the [homocidal chauffeur](https://www.rand.org/pubs/papers/P257.html.) problem), and stochastic optimal control. The former addresses strategic activity of $b$ with a known (and opposed) optimization object, the latter addresses uncertainty about the environment.

## Defining the Metagame

### MAIDs as the Statespace

I dove into details exploring the properties of MAIDs as a family of process DAGs in this note: https://hackmd.io/X9sK2r2DTLexvIDyclfw5Q

There is some collision in notation between GDS and MAIDs that needs to be resolved in order to discuss them within the same work but they share a lot of conceptual foundations.

For the purpose of this document let us define the space of MAIDs as follows:

There is a network $G = (V,E)$ where $V$ is the vertex set and $E\subset V \times V$ is the set of directed edges $(i,j)$ pointing from $i$ to $j$. Furthermore, each vertex represents a _process_. There are 3 types of input-output processes:
* **Decision** Processes
* **Chance** Processes
* **Utility** Processes

Each edge represents a (potential) dependency between processes. That is to say that an edge from process $i$ to process $j$ indicates that the output of process $i$ is an input to process $j$. There are two types of edges:
* **Causal** Relationships
* **Observational** Relationships

In the case of a causal link we are representing a structural relationship within the game. In the case of an observational link we are representing the fact that an processes output is observable, such that a decision process may be conditioned on it. The absense of an observational link indicates that the output is not observable with respect to a particular decision process, and therefore that decision process may not be conditioned on it (though possibly on a belief or estimate thereof).

Some addition details about edges; this table is read as follows

[row] Process --> [col] Process

| Process Type | Decision |Chance |  Utility |
| -------- | -------- | -------- | -------- |
| Decision | may be observed by     | may cause; may be observed by    | may cause |
| Chance    | may be observed by    | may cause     |  may cause|
| Utility  | --     | --     | may cause |

Note that utilities are fixed within any instance of the game, but they may be manipulated (for example, during game mining actions in a metagame). This in turn backpropagates and affects the strategies of the players.

In addition to the network $G$, we require a process $P$ which respects the structure of $G$---this represents the manner in which an agent may change the game structure---and a set of agents $A$, such that 
1. each decision process is owned by exactly one agent $a\in A$, and
2. each agent $a\in A$ has precisely one utility process whose output is an optimization objective for that agent.

Thus the state of our Metagame is

$$x=(G,P,A) \in \bar{\mathcal{X}} \subset \mathcal{G} \times \mathcal{P} \times \mathcal{A} =\mathcal{X}$$

where $\bar{\mathcal{X}}$ is the configuration space denoting the subset of $\mathcal{G} \times \mathcal{P} \times \mathcal{A}$ which satisfied the rules discussed above. 

### Game Mining as State-Update Map

The above allows us to define the action spaces for game mining, because we can restrict game mining moves to the case where a new agent $z$ arrives

$$
A^+ = A \oplus \{z\}\\
$$

and introduces at least one new decision process

$$g_z(x) \in P^+$$

and its own utility process

$$r_z(x) \in P^+$$

and a new chance process

$$f_z(x, u_z; u_a \forall a\in A\setminus \{z\} )\in P^+$$

furthermore, these new processes expand the vertex set

$$ V^+ = V \oplus \{g_z,r_z,f_z\}$$

and the edges representing the functional dependence of these processes need to be appended to the edge set

$$ E^+ = E\cup\Delta E = E\cup (\Delta_1 \cup \Delta_2)$$
where $\Delta E$ has two components:
* edges between the new vertices $\Delta_1 \subset \{g_z,r_z,f_z\} \times \{g_z,r_z,f_z\}$
* edges from the old vertices to the new ones $\Delta_2 \subset E \times \{g_z,r_z,f_z\}$

Further discussion is required regarding links from the new vertices to the old ones, given that we are describing a compositional framework. New players may interact with the prior games dynamics but cannot directly mutate them, only change them indirectly through composition. Further exploration of the formalisms may be required.

Nonetheless the resulting game lies on the network $G^+=(V^+,E^+)$, which is the DAG structure of the process $P^+$, which is played by agents in the set $A^+$. The fact that these object collectively satisfy our game grammar based on MAIDs is equivalent to:

$$x^+=(G^+,P^+,A^+) \in \bar{\mathcal{X}} \subset \mathcal{G} \times \mathcal{P} \times \mathcal{A} =\mathcal{X}$$

and the action space $U_z(x)$ which induced this change was introducing the agent $z$ and the new processes $\{g_z,r_z,f_z\}$ to the game, the other aspects of the state mutation were merely accounting of the consequences of those changes on the MAID representation of the game. However this is far from inconsequential, assuming agents play the game according to dynamic optimization based strategies, their behavior may change considerably as a result of the (game mining) transition from $x$ to $x^+$.

## Killer Tree Example Metagame

Consider the following MAID to be $G$
![](https://i.imgur.com/UMAVkKg.png)

We can construct an example of a game mining move representing the introduction of a new agent, the Homeowners' Association (HOA), for the neighborhood that Alice and Bob live in. The HOA wants to feel safe so it might choose to introduce a neighborhood watch program, and if it observes a crime, report that crime to the police. The police investigation is treated as a chance process which may or may not result in a conviction related to the reported crime.

This may be seen as a game mining move on the part of the HOA, resulting in a new 3-player game for Alice, Bob and the HOA, with new vertices and edges in the MAID, now $G^+$.

![](https://i.imgur.com/DkrVoih.png)


In order to fully represent the new game we would need to flesh out the details of the new process vertices added to the network, as well as changes to the behavior of the agents in the original game. In this case, we might expect Alice is much less likely to Poison Tree if she knows the HOA has taken the action neighborhood watch.

Alternative, Alice (as unscrupulous as she is) might observe that there is a neighborhood watch in effect and proceed with the poisoning anyway, assuming that she will be in a position to _bribe_ the HOA agent in the event that she gets caught. Such a bribe would induce a conserved flow of money from Alice to the HOA agent, and indirectly affect the HOA agent's other utility process 'Feels Safe'. Taking bribes not to report a crime makes the neighborhood less safe, but depending on how the payoffs are scaled this may be worth it to the HOA agent.

![](https://i.imgur.com/pWp7mNI.png)

The takeaway from this example is that the admissible action set in the Metagame is extremely high dimensional. In its most generic form it represents an arbitrary extension of the MAID to another MAID via composition. For practical purposes it makes sense to bound the complexity of an individual game mining move to a single actor and a finite upper bound on new decision, chance and utility processes. Furthermore, we can anchor the agent's choice of mechanisms to append by asserting a utility process they are optimizing for. 

## Next Steps

The above should suffice to demonstrate that repeated applications of game mining will generate ever more complex games (although it is also possible to collapse some regions of the agents strategy spaces).

I am proposing we term these iterative metagame dynamics "generative metagames" when we introduce the concept of the metagame players and apply game mining moves repeatedly.

One might argue that human society as we experience it today is itself the product on an ongoing generative metagame... could make a nice pointer back to the big history work.

### Playing the Metagame

#### Utilities for Metagamers

#### Strategic behavior for metagamers

### Repeated Metagames Generate Sequences of New Games

#### Reachability?
#### Stability?