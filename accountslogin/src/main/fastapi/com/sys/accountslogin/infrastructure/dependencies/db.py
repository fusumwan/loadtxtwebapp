from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy import delete, update, func
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List
from typing import AsyncGenerator
from fastapi import FastAPI, HTTPException, Depends, Request
from typing import List, Callable
from ...config.ApplicationProperties import ApplicationProperties

applicationProperties=ApplicationProperties()
DATABASE_URL = applicationProperties.AppDatasourceUrl
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)
# Adjusted dependency to correctly type-hint as an AsyncGenerator
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session