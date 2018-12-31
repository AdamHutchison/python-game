from statemachine import StateMachine
from map import Map
from inputhandler import InputHandler


class Bootstrap(object):
    @staticmethod
    def initialise():
        return {
            'state-machine': StateMachine(),
            'map': Map(),
        }