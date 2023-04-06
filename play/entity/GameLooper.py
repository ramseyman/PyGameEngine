import pygame

class GameLooper:
    def __init__(self, content):
        self.content = content
        return

    def loop(self):
        pygame.init()
        while True:
            event = pygame.event.get()
            for c in self.content:
                for actions in c.actions:
                    if actions.types == ["event"]:
                        for e in event:
                            actions.act(e)
                    elif actions.types == ["display"]:
                        actions.act(self.content[0].screen)
                    elif actions.types == ["loop"]:
                        actions.act()
                    elif actions.types == ["physics"]:
                        actions.act(c)
        return 