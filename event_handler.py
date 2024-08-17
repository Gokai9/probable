import tcod.event
from typing import Optional
from actions import Action, EscapeAction, MovementAction

class Event(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Action | None:
        raise SystemExit
    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        action: Action | None = None
        key = event.sym

        if key == tcod.event.KeySym.RIGHT:
            action = MovementAction(1, 0)
        if key == tcod.event.KeySym.LEFT:
            action = MovementAction(-1, 0)
        if key == tcod.event.KeySym.UP:
            action = MovementAction(0, -1)
        if key == tcod.event.KeySym.DOWN:
            action = MovementAction(0, 1)

        if key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction(self.ev_quit)

        return action
    