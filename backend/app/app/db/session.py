# The Session is the time between the client logs in to the server and logs out of the server.
import sys

from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.pool import NullPool, QueuePool
import asyncio



# Heroku workaround: https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
connection_uri = settings.SQLALCHEMY_DATABASE_URI
'''
if connection_uri.startswith("postgres://"):
    connection_uri = connection_uri.replace("postgres://", "postgresql+asyncpg://", 1)

engine = create_async_engine(connection_uri, pool_reset_on_return=None,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)
'''


# For sqlite

engine = create_async_engine(url=connection_uri, pool_reset_on_return=None, connect_args={"check_same_thread": False})
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


