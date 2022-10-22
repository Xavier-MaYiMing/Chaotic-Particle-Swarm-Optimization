# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/12 11:41
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : CPSO.py
# @Statement : Chaotic Particle Swarm Optimization
# @Reference : Liu, B., Wang, L., Jin, Y.-H., Tang, F., & Huang, D.-X. (2005). Improved particle swarm optimization combined with chaos. Chaos, Solitons & Fractals, 25(5), 1261–1271.
import random
import copy
import math
import matplotlib.pyplot as plt
import numpy as np


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(value, l_bound, u_bound):
    """
    The boundary check
    :param value:
    :param l_bound: lower bound
    :param u_bound: upper bound
    :return:
    """
    for i in range(len(value)):
        value[i] = max(value[i], l_bound[i])
        value[i] = min(value[i], u_bound[i])
    return value


def main(pop, iter, iter_chaos, lbound, ubound, vmin, vmax, c1, c2, omega_min, omega_max):
    """
    The main function of the CPSO
    :param pop: the population size
    :param iter: the iteration number
    :param iter_chaos: the iteration number of chaotic local search
    :param lbound: the lower bound (list)
    :param ubound: the upper bound (list)
    :param vmin: the minimum velocity (list)
    :param vmax: the maximum velocity (list)
    :param c1: the acceleration coefficient of exploitation
    :param c2: the acceleration coefficient of exploration
    :param omega_min: the minimum of inertia weight
    :param omega_max: the maximum of inertia weight
    :return:
    """
    # Step 1. Initialization
    dim = len(lbound)  # dimension
    score = []  # the objective value of particles
    position = []  # the position of particles
    velocity = []  # the velocity of particles
    for i in range(pop):
        temp_position = [random.uniform(lbound[j], ubound[j]) for j in range(dim)]
        position.append(temp_position)
        velocity.append([random.uniform(vmin[j], vmax[j]) for j in range(dim)])
        score.append(obj(temp_position))
    g_best = min(score)  # global best
    p_best = copy.deepcopy(score)  # personal best
    g_best_position = position[score.index(g_best)]  # the position of global best
    p_best_position = copy.deepcopy(position)  # the position of personal best
    iter_best = [g_best]  # the global best value of each iteration

    # Step 2. The main loop
    for _ in range(iter):
        f_avg = sum(score) / len(score)
        f_min = min(score)
        for i in range(pop):

            # Step 2.1. Update global best and personal best
            for j in range(pop):
                if score[j] < p_best[j]:
                    p_best[j] = score[j]
                    p_best_position[j] = position[j]
                    if score[j] < g_best:
                        g_best = score[j]
                        g_best_position = position[j]

            # Step 2.2. Calculate the inertia weight of this particle
            if score[i] <= f_avg:
                omega = omega_min + (omega_max - omega_min) * (score[i] - f_min) / (f_avg - f_min)
            else:
                omega = omega_max

            # Step 2.3. Update the velocity and position
            velocity[i] = [omega * velocity[i][j] + c1 * random.random() * (
                p_best_position[i][j] - position[i][j]) + c2 * random.random() * (g_best_position[j] - position[i][j])
                           for j in range(dim)]
            velocity[i] = boundary_check(velocity[i], vmin, vmax)
            position[i] = [position[i][j] + velocity[i][j] for j in range(dim)]
            position[i] = boundary_check(position[i], lbound, ubound)
            new_score = obj(position[i])
            score[i] = new_score

        # Step 2.4. Implement the chaotic local search for the best particle
        index = np.argsort(score)
        best_index = index[0]
        best_score = score[best_index]
        best_position = position[best_index]
        temp_cx = [(best_position[i] - lbound[i]) / (ubound[i] - lbound[i]) for i in range(dim)]
        for _ in range(iter_chaos):
            new_cx = [4 * temp_cx[i] * (1 - temp_cx[i]) for i in range(dim)]
            new_x = [lbound[i] + new_cx[i] * (ubound[i] - lbound[i]) for i in range(dim)]
            new_score = obj(new_x)
            if new_score < best_score:
                position[best_index] = new_x
                score[best_index] = new_score
                if new_score < g_best:
                    g_best = new_score
                    g_best_position = new_x
                    break
            temp_cx = new_cx

        # Step 2.5. Record the global best value of each iteration
        iter_best.append(g_best)

    # Step 3. Sort the results
    x = [i for i in range(iter + 1)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.ticklabel_format(style='sci', scilimits=(0, 0))
    plt.show()
    return {'best solution': g_best_position, 'best score': g_best}


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
