from melee.enums import Character

from Chains.Abstract import ElementalDive
from Utils import Trajectory


class FalconDive(ElementalDive):
    TRAJECTORY = Trajectory.from_csv_file(Character.CPTFALCON, 0, 44, -999, 999, "Data/Trajectories/falcon_dive.csv")
    REVERSE_TRAJECTORY = Trajectory.from_csv_file(Character.CPTFALCON, 0, 44, 15, 999, "Data/Trajectories/reverse_falcon_dive.csv")

    @classmethod
    def _get_normal_trajectory(cls):
        return cls.TRAJECTORY

    @classmethod
    def _get_reverse_trajectory(cls):
        return cls.REVERSE_TRAJECTORY