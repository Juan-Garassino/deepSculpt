from deepSculpt.manager.manager import Manager
from deepSculpt.manager.tools.params import COLORS

import random
import numpy as np
from colorama import Fore, Style
import os


def attach_pipe(
    void,
    color_void,
    element_volume_min_ratio,
    element_volume_max_ratio,
    step,
):  # THIS IS GOOD!!

    element = None
    delta = None
    axis_selection = np.random.randint(low=0, high=2)
    shape_selection = np.random.randint(low=0, high=2)

    working_plane = None
    top_left_corner = None
    bottom_right_corner = None

    element_volume_min_index = int(element_volume_min_ratio * void.shape[0])
    element_volume_max = int(element_volume_max_ratio * void.shape[0])

    depth = random.randrange(element_volume_min_index, element_volume_max, step)

    """if int(os.environ.get("VERBOSE")) == 1:
        print(working_plane)"""

    element = np.ones(
        (
            random.randrange(element_volume_min_index, element_volume_max, step),
            random.randrange(element_volume_min_index, element_volume_max, step),
        )
    )
    element = np.repeat(element, repeats=depth, axis=0).reshape(
        (element.shape[0], element.shape[1], depth)
    )

    element_void = np.zeros((element.shape[0] - 2, element.shape[1] - 2))
    element_void = np.repeat(element_void, repeats=depth).reshape(
        (element_void.shape[0], element_void.shape[1], depth)
    )

    # element[1:-1,1:-1,:] = element_void # elegir pasar el vacio o no como parte del volumen

    delta = np.array(void.shape) - np.array(
        element.shape
    )  # ENCONTRAR LOS NUEVOS DELTAS

    corner_1 = np.array(
        (
            np.random.randint(low=0, high=delta[0]),
            np.random.randint(low=0, high=delta[1]),
            np.random.randint(low=0, high=delta[2]),
        )
    )
    corner_2 = np.array((corner_1[0] + element.shape[0], corner_1[1], corner_1[2]))
    corner_3 = np.array((corner_1[0], corner_1[1], corner_1[2] + element.shape[2]))
    corner_4 = np.array(
        (
            corner_1[0] + element.shape[0],
            corner_1[1],
            corner_1[2] + element.shape[2],
        )
    )

    corner_5 = np.array((corner_1[0], corner_1[1] + element.shape[1], corner_1[2]))
    corner_6 = np.array((corner_2[0], corner_2[1] + element.shape[1], corner_2[2]))
    corner_7 = np.array((corner_3[0], corner_3[1] + element.shape[1], corner_3[2]))
    corner_8 = np.array((corner_4[0], corner_4[1] + element.shape[1], corner_4[2]))

    color_volume = np.random.randint(0, len(COLORS["volumes"]))

    if int(os.environ.get("VERBOSE")) == 1:
        print(
            "\n ⏹ "
            + Fore.RED
            + f"The color of the volume is {COLORS['volumes'][color_volume]}"
            + Style.RESET_ALL
        )

    # creates the floor and ceiling
    void[
        corner_3[0] : corner_8[0], corner_3[1] : corner_8[1], corner_3[2] - 1
    ] = element[:, :, 0]
    color_void[
        corner_3[0] : corner_8[0], corner_3[1] : corner_8[1], corner_3[2] - 1
    ] = COLORS["volumes"][color_volume]

    void[corner_1[0] : corner_6[0], corner_1[1] : corner_6[1], corner_1[2]] = element[
        :, :, 1
    ]
    color_void[
        corner_1[0] : corner_6[0], corner_1[1] : corner_6[1], corner_1[2]
    ] = COLORS["volumes"][color_volume]

    # creates de walls
    if shape_selection == 0:
        if axis_selection == 0:
            void[
                corner_1[0], corner_1[1] : corner_7[1], corner_1[2] : corner_7[2]
            ] = element[0, :, :]
            color_void[
                corner_1[0], corner_1[1] : corner_7[1], corner_1[2] : corner_7[2]
            ] = COLORS["volumes"][color_volume]

            void[
                corner_2[0] - 1,
                corner_2[1] : corner_8[1],
                corner_2[2] : corner_8[2],
            ] = element[1, :, :]
            color_void[
                corner_2[0] - 1,
                corner_2[1] : corner_8[1],
                corner_2[2] : corner_8[2],
            ] = COLORS["volumes"][color_volume]
        else:
            void[
                corner_5[0] : corner_8[0], corner_5[1], corner_5[2] : corner_8[2]
            ] = element[:, 0, :]
            color_void[
                corner_5[0] : corner_8[0], corner_5[1], corner_5[2] : corner_8[2]
            ] = COLORS["volumes"][color_volume]

            void[
                corner_1[0] : corner_4[0], corner_1[1], corner_1[2] : corner_4[2]
            ] = element[:, 0, :]
            color_void[
                corner_1[0] : corner_4[0], corner_1[1], corner_1[2] : corner_4[2]
            ] = COLORS["volumes"][color_volume]

    else:
        if axis_selection == 0:
            void[
                corner_1[0], corner_1[1] : corner_7[1], corner_1[2] : corner_7[2]
            ] = element[0, :, :]
            color_void[
                corner_1[0], corner_1[1] : corner_7[1], corner_1[2] : corner_7[2]
            ] = COLORS["volumes"][color_volume]

            void[
                corner_5[0] : corner_8[0], corner_5[1], corner_5[2] : corner_8[2]
            ] = element[:, 0, :]
            color_void[
                corner_5[0] : corner_8[0], corner_5[1], corner_5[2] : corner_8[2]
            ] = COLORS["volumes"][color_volume]
        else:
            void[
                corner_2[0] - 1,
                corner_2[1] : corner_8[1],
                corner_2[2] : corner_8[2],
            ] = element[1, :, :]

            color_void[
                corner_2[0] - 1,
                corner_2[1] : corner_8[1],
                corner_2[2] : corner_8[2],
            ] = COLORS["volumes"][color_volume]

            void[
                corner_1[0] : corner_4[0], corner_1[1], corner_1[2] : corner_4[2]
            ] = element[:, 0, :]

            color_void[
                corner_1[0] : corner_4[0], corner_1[1], corner_1[2] : corner_4[2]
            ] = COLORS["volumes"][color_volume]

    if int(os.environ.get("VERBOSE")) == 1:
        Manager.verbose(
            void=void,
            element=element,
            delta=delta,
            top_left_corner=top_left_corner,
            bottom_right_corner=bottom_right_corner,
        )

    return void.astype("int8"), color_void
