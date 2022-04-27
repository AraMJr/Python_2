from dataclasses import dataclass, astuple, asdict


@dataclass(frozen=True)
class State:
    front_right: str = "stationary"
    back_right: str = "stationary"
    front_left: str = "stationary"
    back_left: str = "stationary"


@dataclass(frozen=True)
class Forward(State):
    def __init__(self):
        front_right = "forward"
        back_right = "forward"
        front_left = "forward"
        back_left = "forward"
        super(Forward, self).__init__(front_right, back_right, front_left, back_left)
    

@dataclass(frozen=True)
class Backward(State):
    def __init__(self):
        front_right = "backward"
        back_right = "backward"
        front_left = "backward"
        back_left = "backward"
        super(Backward, self).__init__(front_right, back_right, front_left, back_left)


@dataclass(frozen=True)
class Stationary(State):
    def __init__(self):
        front_right = "stationary"
        back_right = "stationary"
        front_left = "stationary"
        back_left = "stationary"
        super(Stationary, self).__init__(front_right, back_right, front_left, back_left)


@dataclass(frozen=True)
class Left(State):
    def __init__(self):
        front_right = "forward"
        back_right = "forward"
        front_left = "backward"
        back_left = "backward"
        super(Left, self).__init__(front_right, back_right, front_left, back_left)


@dataclass(frozen=True)
class Right(State):
    def __init__(self):
        front_right = "backward"
        back_right = "backward"
        front_left = "forward"
        back_left = "forward"
        super(Right, self).__init__(front_right, back_right, front_left, back_left)



