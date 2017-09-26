from logging import getLogger

from .controller import Controller
from model import pure_pursuit

logger = getLogger('controller')


class FixedController(Controller):
    def __init__(self, mrds_url, lin_spd=1, lookahead=5, delta_pos=0.75):
        super(FixedController, self).__init__(mrds_url, lin_spd=lin_spd, delta_pos=delta_pos)
        self.__lookahead = lookahead
        logger.info(
            'Using {} with linear speed={}, lookahead={}, delta position={}'.format(self.__class__.__name__, lin_spd,
                                                                                    lookahead, delta_pos))

    def pure_pursuit(self, pos_path):
        """
            Implements the pure pursuit algorithm with a fixed lookahead (step parameter).
            The robot aims for "step" position ahead on the path.

            :param pos_path: list of Vector
            :type pos_path: list
        """
        # Travel through the path skipping "lookahead" positions every time
        for i in range(0, len(pos_path), self.__lookahead):
            cur_pos, cur_rot = self.get_pos_and_orientation()
            self.travel(cur_pos, pos_path[i], self._lin_spd, pure_pursuit.get_ang_spd(cur_pos, cur_rot, pos_path[i], self._lin_spd))

        self.stop()