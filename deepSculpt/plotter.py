import matplotlib.pyplot as plt
import numpy as np
from deepSculpt.sculptor import Sculptor

class Plotter(Sculptor):

    def __init__(self, void, style):
        self.void = void
        self.style = style

    def plot_sections(self):
        sculpture = self.void
        fig, axes = plt.subplots(ncols=6,
                                 nrows=int(np.ceil(self.void.shape[0] / 6)),
                                 figsize=(25, 25),
                                 facecolor=(self.style))
        axes = axes.ravel()  # flats
        for index in range(self.void.shape[0]):
            axes[index].imshow(sculpture[index, :, :], cmap="gray")

    def plot_sculpture(self):  # add call to generative sculpt and then plot like 12
        fig, axes = plt.subplots(ncols=2,
                                 nrows=2,
                                 figsize=(25, 25),
                                 facecolor=(self.style),
                                 subplot_kw=dict(projection="3d"))
        axes = axes.ravel()  # flats
        for index in range(1):
            axes[0].voxels(self.void[0],
                               facecolors=self.void[1],
                               edgecolors="k",
                               linewidth=0.05)

            axes[1].voxels(np.rot90(self.void[0], 1),
                           facecolors=np.rot90(self.void[1], 1),
                           edgecolors="k",
                           linewidth=0.05)

            axes[2].voxels(np.rot90(self.void[0], 2),
                           facecolors=np.rot90(self.void[1], 2),
                           edgecolors="k",
                           linewidth=0.05)

            axes[3].voxels(np.rot90(self.void[0], 3),
                           facecolors=np.rot90(self.void[1], 3),
                           edgecolors="k",
                           linewidth=0.05)

        plt.savefig('image.png')  # agregar tiempo de impresion y exportar 3D
