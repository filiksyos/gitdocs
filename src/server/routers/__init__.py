"""This module contains the routers for the FastAPI application."""

# Remove the download router import
# from server.routers.download import router as download
from server.routers.dynamic import router as dynamic
from server.routers.index import router as index

__all__ = ["dynamic", "index"]
