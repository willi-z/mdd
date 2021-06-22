from abc import ABC, ABCMeta, abstractmethod
from .metadata import Metadata


class ConnectableInterface(ABC):# metaclass=ABCMeta
    @abstractmethod
    def get_value(self) -> []:
        pass

    @abstractmethod
    def set_value(self, value) -> bool:
        pass

    @abstractmethod
    def get_ingoing(self):
        pass

    @abstractmethod
    def get_outgoing(self) -> []:
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def connect_ingoing(self, output) -> bool:
        pass

    @abstractmethod
    def connect_outgoing(self, input) -> bool:
        pass

    @abstractmethod
    def disconnect_ingoing(self) -> bool:
        pass

    @abstractmethod
    def disconnect_outgoing(self) -> bool:
        pass

    @abstractmethod
    def is_changed(self) -> bool:
        pass

    @abstractmethod
    def update(self) -> bool:
        pass


class TypeInterface(ABC):
    """
    """

    @abstractmethod
    def is_same(self, value) -> bool:
        pass

    @abstractmethod
    def get_value(self):
        """
        Must return representative value for connectivity-checks
        """
        pass

    @abstractmethod
    def set_value(self, value) -> bool:
        pass

    @abstractmethod
    def is_changed(self) -> bool:
        """
        Returns True if value has changed.
        Important for optimisation, for deciding whether to ignore or process a recipe.
        """
        pass

    @abstractmethod
    def is_connectable(self, other) -> bool:
        pass

class UnitInterface(ABC):
    @abstractmethod
    def own_id(self):
        pass

    @abstractmethod
    def complete_id(self) -> []:
        pass

    @abstractmethod
    def get_metadata(self) -> Metadata:
        pass

    @abstractmethod
    def set_inverted(self, inverted:bool):
        pass

    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def find(self, id: [], complete=True):
        """
        Returns the first element if it can find the element based on the identifier.
        If the identifier is complete (i.e. generated by the identifier()) the algorithm will be use a
        """
        pass

    @abstractmethod
    def find_all(self, id: [], complete=True) -> []:
        """
        Returns the elements if it can find the element based on the identifier.

        """
        pass

    @abstractmethod
    def get_childs(self) -> []:
        pass

    @abstractmethod
    def get_parent(self):
        pass

    @abstractmethod
    def get_parents(self) -> []:
        pass

    @abstractmethod
    def update(self) -> bool:
        pass