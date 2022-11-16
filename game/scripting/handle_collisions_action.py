import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the other player, or the cycle collides with its segments, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        # Set loser to true if player 2 loses. 
        self._loser = False

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_tail(cast)
            self._handle_game_over(cast)

    def _handle_tail(self, cast):
        """Handles how the cycles interact with the walls.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle_one = cast.get_first_actor("cycles")
        cycle_two = cast.get_second_actor("cycles")
        cycle_one.grow_tail()
        cycle_two.grow_tail()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        player_1 = cast.get_first_actor("cycles")
        player_2 = cast.get_second_actor("cycles")
        head1 = player_1.get_segments()[0]
        segments1 = player_1.get_segments()[1:]
        head2 = player_2.get_segments()[0]
        segments2 = player_2.get_segments()[1:]

        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._loser = True
                
        
        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._loser = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            if self._loser:
                cycle = cast.get_second_actor("cycles")
                segments = cycle.get_segments()
                winner = cast.get_first_actor("scores")
            elif self._loser == False:
                cycle = cast.get_first_actor("cycles")
                segments = cycle.get_segments()
                winner = cast.get_second_actor("scores")
            

            winner.add_points(1)
        

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)