class CredentialsContainer:
    """
    Interface indicating the implementing object contains sensitive data.
    """
    def erase_credentials(self):
        raise NotImplementedError("Must be implemented by subclasses.")
