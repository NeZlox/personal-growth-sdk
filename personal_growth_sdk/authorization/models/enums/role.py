from enum import StrEnum

__all__ = ['RoleType']


class RoleType(StrEnum):
    """
    System roles for users.
    """

    DEVELOPER = 'developer'
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'
    GUEST = 'guest'

    @property
    def description(self) -> str:
        """
        Returns a human-readable description of the role.
        """

        descriptions = {
            'developer': (
                'Full access to system settings and APIs. '
                '!!! Used ONLY in testing environments, '
                'not available in production.'
            ),
            'admin': 'Full access to all business functions of the system.',
            'manager': 'Manage users and content.',
            'user': 'Access to basic system functions.',
            'guest': 'Limited read-only access.'
        }
        return descriptions.get(self, 'Unknown role')

    @classmethod
    def privileged_roles(cls) -> tuple['RoleType', ...]:
        """
        Returns roles with elevated privileges.
        """

        return cls.DEVELOPER, cls.ADMIN

    def has_access(self, required_role: 'RoleType') -> bool:
        """
        Checks whether the current role has sufficient privileges.
        """

        role_hierarchy = {
            RoleType.DEVELOPER: 400,
            RoleType.ADMIN: 300,
            RoleType.MANAGER: 200,
            RoleType.USER: 100,
            RoleType.GUEST: 0
        }
        return role_hierarchy.get(self, 0) >= role_hierarchy.get(required_role, 0)
