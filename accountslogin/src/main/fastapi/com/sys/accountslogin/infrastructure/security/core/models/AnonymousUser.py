from pydantic import BaseModel

class AnonymousUser(BaseModel):
    id: None = None
    is_authenticated: bool = False
    is_active: bool = False
    is_superuser: bool = False
    is_staff: bool = False
    
    def get_username(self) -> str:
        return 'AnonymousUser'

    def has_perm(self, perm, obj=None) -> bool:
        return False

    def has_module_perms(self, package_name) -> bool:
        return False

    def __str__(self):
        return 'AnonymousUser'
