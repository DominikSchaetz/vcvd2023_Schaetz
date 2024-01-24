#required imports
import matplotlib.pyplot as plt
import numpy as np
import argparse

#formula source: http://www.dbux.ch/physics/bremsweg.html
#code information source: https://www.w3schools.com/python



    #function
def deceleration(args):
    breakeVelocity = args.velocity - 9.81 * args.friction * np.linspace(0, args.velocity / (9.81 * args.friction), 100)
    distance = 0.5*np.linspace(0, args.velocity / (9.81 * args.friction), 100)*(2*args.velocity-(9.81 * args.friction)*np.linspace(0, args.velocity / (9.81 * args.friction), 100))

    #define figure and plots

    figure, axs = plt.subplots(1, 2)
    axs[0].plot(np.linspace(0, args.velocity / (9.81 * args.friction), 100), breakeVelocity)
    axs[0].set_title('Break velocity')
    axs[0].set_xlabel('time [s]')
    axs[0].set_ylabel('velocity [m/s]')
    axs[0].grid(True)

    axs[1].plot(np.linspace(0, args.velocity / (9.81 * args.friction), 100), distance)
    axs[1].set_title('Break distance')
    axs[1].set_xlabel('time [s]')
    axs[1].set_ylabel('distance [m]')
    axs[1].grid(True)
    figure.set_size_inches(11.7, 8.3)
    plt.show()

    #export plot as pdf

    figure.savefig("plot.pdf", dpi=300)


