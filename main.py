import tcod
from actions import MovementAction, EscapeAction
from event_handler import Event

WIDTH = 90
HEIGHT = 45

def main():
    X_player = int(WIDTH / 2)
    Y_player = int(HEIGHT / 2)
    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    with tcod.context.new_terminal(WIDTH, HEIGHT, tileset=tileset, title="RogueLike", vsync= True) as context:
        root_console = tcod.console.Console(width=WIDTH, height=HEIGHT, order='F')
        event_handler = Event()
        while True:
            root_console.print(x=X_player, y=Y_player, string='@')
            context.present(root_console)
            root_console.clear()
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    X_player += action.x
                    Y_player += action.y
                
                if isinstance(action, EscapeAction):
                    action.quit(event)
                    


if __name__ == "__main__":
    main()