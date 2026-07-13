from abc import ABC, abstractmethod
from typing import Collection
from collections.abc import Iterable
from ..access.AccessDecisionManager import *

class UserDetails(ABC):
    @abstractmethod
    def get_authorities(self) -> Collection[GrantedAuthority]:
        """
        Returns the authorities granted to the user. Cannot return None.
        """
        pass

    @abstractmethod
    def get_password(self) -> str:
        """
        Returns the password used to authenticate the user.
        """
        pass

    @abstractmethod
    def get_username(self) -> str:
        """
        Returns the username used to authenticate the user. Cannot return None.
        """
        pass

    @abstractmethod
    def is_account_non_expired(self) -> bool:
        """
        Indicates whether the user's account has expired. An expired account cannot be authenticated.
        """
        pass

    @abstractmethod
    def is_account_non_locked(self) -> bool:
        """
        Indicates whether the user is locked or unlocked. A locked user cannot be authenticated.
        """
        pass

    @abstractmethod
    def is_credentials_non_expired(self) -> bool:
        """
        Indicates whether the user's credentials (password) has expired. Expired credentials prevent authentication.
        """
        pass

    @abstractmethod
    def is_enabled(self) -> bool:
        """
        Indicates whether the user is enabled or disabled. A disabled user cannot be authenticated.
        """
        pass
