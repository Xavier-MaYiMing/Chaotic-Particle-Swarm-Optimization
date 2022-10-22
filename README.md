### Chaotic Particle Swarm Optimization

##### Reference: Liu, B., Wang, L., Jin, Y.-H., Tang, F., & Huang, D.-X. (2005). Improved particle swarm optimization combined with chaos. Chaos, Solitons & Fractals, 25(5), 1261–1271.

| Variables       | Meaning                                                      |
| --------------- | ------------------------------------------------------------ |
| pop             | The number of particles                                      |
| iter            | The number of iterations                                     |
| iter_chaos      | The iteration number of chaotic local search                 |
| lbound          | List, the lower bound                                        |
| ubound          | List, the upper bound                                        |
| vmin            | List, the minimum velocity                                   |
| vmax            | List, the maximum velocity                                   |
| c1              | The acceleration coefficient of exploitation                 |
| c2              | The acceleration coefficient of exploration                  |
| omega_min       | The minimum value of inertia weight                          |
| omega_max       | The maximum value of inertia weight                          |
| dim             | The number of dimensions                                     |
| score           | List, the score of the i-th particle is score[i]             |
| position        | List, the position of the i-th particle is position[i]       |
| velocity        | List, the velocity of the i-th particle is velocity[i]       |
| g_best          | The global best score                                        |
| g_best_location | The position of the global best particle                     |
| p_best          | List, the personal best score of the i-th particle is p_best[i] |
| p_best_location | List, the personal best position of the i-th particle is p_best_location[i] |
| iter_best       | List, the best-so-far score of each iteration                |
| omega           | The inertia weight with Adaptive Inertia Weight Factor (AIWF) |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Chaotic-Particle-Swarm-Optimization/blob/main/Pressure%20vessel%20design.png)
$$
\begin{align*}
\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
\text{s.t.} -x_1+0.0193x_3\leq0,\\
-x_3+0.0095x_3\leq0,\\
-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
x_4-240\leq0,\\
0\leq x_1\leq99,\\
0\leq x_2 \leq99,\\
10\leq x_3 \leq 200,\\
10\leq x_4 \leq 200.
\end{align*}
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 100
    iter_chaos = 300
    c1 = 2
    c2 = 2
    omega_min = 0.2
    omega_max = 1.2
    lbound = [0, 0, 10, 10]
    ubound = [100, 100, 100, 100]
    vmin = [-2, -2, -2, -2]
    vmax = [2, 2, 2, 2]
    print(main(pop, iter, iter_chaos, lbound, ubound, vmin, vmax, c1, c2, omega_min, omega_max))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Chaotic-Particle-Swarm-Optimization/blob/main/PSO_CPSO%20comparison.png)

This comparative figure indicates that the CPSO finds a better solution compared to the PSO.

![](https://github.com/Xavier-MaYiMing/Chaotic-Particle-Swarm-Optimization/blob/main/Convergence%20Curve.png)



```python
{
    'best solution': [1.3553460966593345, 0.6489113019601358, 67.41527440529954, 15.750952463723596], 
    'best score': 8688.271882233967
}
```

