import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cycle import Cycle


class Player2(Cycle):

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def _prepare_body(self):
        x = int(600)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(.25 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.BLUE

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def grow_tail(self):
        tail = self._segments[-1]
        velocity = tail.get_velocity()
        offset = velocity.reverse()
        position = tail.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        segment.set_color(constants.BLUE)
        self._segments.append(segment)
