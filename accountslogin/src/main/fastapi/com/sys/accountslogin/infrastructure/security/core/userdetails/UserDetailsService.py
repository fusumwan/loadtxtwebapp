from . import *
from ..UserDetails import UserDetails
class UserDetailsService:
    def load_user_by_username(self, username) -> UserDetails:
        """Load user by username.

        Args:
            username (str): The username of the user.

        Returns:
            UserDetails: The UserDetails object for the user.

        Raises:
            UsernameNotFoundException: If no user is found.
        """
        # Implement the logic to load user details by username
        # This is a placeholder implementation
        raise UsernameNotFoundException("User not found for username: {}".format(username))
