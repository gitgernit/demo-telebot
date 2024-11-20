__all__ = ['SQLModel']

from sqlmodel import SQLModel

# Initialize all models for SQLModel's __init_subclass__ to trigger
from .user import *
