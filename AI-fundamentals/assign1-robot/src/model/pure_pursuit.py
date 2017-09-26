from math import atan2, cos, sin

from .vector import Vector
from .quaternion import Quaternion


def convert_to_rcs(tar_pos, cur_pos, cur_rot):
    #angle = 2 * atan2(cur_rot.z, cur_rot.w)
    q = Quaternion(cur_rot.w, Vector(0, 0, cur_rot.z)).heading()
    angle = atan2(q.y, q.x)
    rcs_pos = Vector(0, 0, tar_pos.z)

    rcs_pos.x = (tar_pos.x - cur_pos.x) * cos(angle) + (tar_pos.y - cur_pos.y) * sin(angle)
    rcs_pos.y = -(tar_pos.x - cur_pos.x) * sin(angle) + (tar_pos.y - cur_pos.y) * cos(angle)

    return rcs_pos

def get_ang_spd(cur_pos, cur_rot, tar_pos, lin_spd):
    """
        Computes the angular speed using pure pursuit formulas
    """
    rcs_tar_pos = convert_to_rcs(tar_pos, cur_pos, cur_rot)

    ang_spd = lin_spd / ((pow(rcs_tar_pos.x, 2) + pow(rcs_tar_pos.y, 2)) / (2 * rcs_tar_pos.y))

    return ang_spd
