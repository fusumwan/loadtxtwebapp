from abc import abstractmethod
from ....io.Serializable import Serializable


class GrantedAuthority(Serializable):
    @abstractmethod
    def get_authority(self) -> str:
        pass