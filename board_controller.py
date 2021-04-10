from signal import Signal

class BoardController:
    
    def __init__(self):
        self.config = {}
        self.pedal_on = [False, False, False]

    def set(self, config):
        self.config = config

    def go(self):
        # TODO: route based on internal config
        newcfg = self.config

    def isPedalOn(self, pedal):
        return self.pedal_on[pedal]