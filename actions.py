class Action:
    def __init__(self) -> None:
        pass
    
class EscapeAction(Action):
    def __init__(self, quit) -> None:
        self.quit = quit

class MovementAction(Action):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y