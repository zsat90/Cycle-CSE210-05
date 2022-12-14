from game.scripting.action import Action
from game.shared.point import Point


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        player1 = cast.get_first_actor("cycles")
        player2 = cast.get_second_actor("cycles")
        segmentsP1 = player1.get_segments()
        segmentsP2 = player2.get_segments()
        messages = cast.get_actors("messages")
        position2 = Point(800, 0)

        score2.set_position(position2)

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segmentsP1)
        self._video_service.draw_actors(segmentsP2)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()