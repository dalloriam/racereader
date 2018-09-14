from typing import Any

class State(object):

    def __init__(self) -> None:
        self._internal_state: dict = {}
    
    def reset(self) -> None:
        self._internal_state = {}
    
    def __getattr__(self, name: str) -> Any:
        allowed_members = ['reset', '_internal_state', '__str__', '__repr__', '__contains__']
        if name in allowed_members:
            return object.__getattribute__(self, name)

        return self._internal_state.get(name)
    
    def __getitem__(self, name: str) -> Any:
        return self.__getattr__(name)
    
    def __setitem__(self, name: str, val: Any) -> None:
        return self.__setattr__(name, val)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == '_internal_state':
            super().__setattr__(name, value)
            return

        self._internal_state[name] = value
    
    def __str__(self) -> str:
        return str(self._internal_state)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __contains__(self, value) -> bool:
        return value in self._internal_state
