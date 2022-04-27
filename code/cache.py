import state as state
from dataclasses import dataclass, astuple, asdict


@dataclass
class Cache:
    stack = [state.State]
    
    def add_state(self, new_state: state.State):
        self.stack.insert(0, new_state)
        
    def remove_state(self, state: state.State):
        self.stack.remove(state)
        
    def update_state(self, state: state.State):
        if state in self.stack:
            self.remove_state(state)
        else:
            self.add_state(state)
        
    def get_state(self):
        try:
            return self.stack[0]
        except IndexError:
            return state.State


