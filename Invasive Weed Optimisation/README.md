# Algorithm - what I understood from different papers
1. Start
2. Define solution space
3. Repeat N Times<br>
3.1 *Initialize* Population <br>
3.2 *Evaluate* Fitness and Rank population<br>
3.3 *Reproduce* seeds based on rank of population<br>
3.4 *Disperse* new seeds over the solution space<br>
3.5 *Evaluate* Fitness and Rank population for new Weeds<br>
3.6 If the number of Weeds > some threshold <br>
    - Then *Eliminate* the Weeds with lower fitness
4. Weed with the best fitness is the final solution 



![image](https://user-images.githubusercontent.com/51333577/159119544-c374e839-1ba3-4eee-92fc-2439cbd2a037.png)

*Invasive weed optimization methodology*

![image](https://user-images.githubusercontent.com/51333577/159120087-4a72fe02-b024-49a0-8ec4-cb37361c3e5d.png)

*Invasive-weed optimization operators*

*(from Cuevas, E., Barocio Espejo, E., & Conde Enríquez, A. (2019). Non-conventional Overcurrent Relays Coordination)* 
[can be found here](https://doi:10.1007/978-3-030-11593-7_3/)


The initial steps are similar to a GA implementation, a possible system solution is known as weed and the weed population is randomly created and then evaluated.
The members of the population are allowed to leave a n seeds (S) depending on their own and on the highest and lowest population fitness as described by

![fitness](https://user-images.githubusercontent.com/51333577/159119627-dfefa877-a9a0-447c-9c23-930867c754c1.jpg)

Spreading operator explores the search space, dispersion one exploits the weed location, and the rolling-down combines these methods to improve the actual solution. Altogether the invasive-weed operators permit a rapid exploration and exploitation of the search space. 

In addition, mutation-based operators create new settings instead of performing crossover operations, requiring less computational effort.

