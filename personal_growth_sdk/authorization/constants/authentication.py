"""
Authentication-related constants and security parameters.

This module stores all security-sensitive constants including:
- Cookie names for authentication tokens
- Token validation parameters
"""

# Cookie storage parameters
AUTH_ACCESS_TOKEN_KEY: str = 'pg_access_token'  # noqa: S105
AUTH_REFRESH_TOKEN_KEY: str = 'pg_refresh_token'  # noqa: S105
