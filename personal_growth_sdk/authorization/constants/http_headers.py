"""
HTTP header constants used throughout the authorization subsystem.

This module contains standardized names for HTTP headers to ensure consistent
access across the application. Using these constants helps prevent typos
and simplifies header management.
"""

# Standard headers
HEADER_X_FORWARDED_FOR: str = 'x-forwarded-for'
HEADER_USER_AGENT: str = 'user-agent'

# Custom application headers
HEADER_DEVICE_FINGERPRINT: str = 'x-device-fingerprint'
