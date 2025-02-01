from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get('/read_user/{id}', response_model=User)
async def read_user(id: int,
                    db: AsyncSession = Depends(deps.get_db),
                    current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Get a user.
    """

    user = await crud.user.get_by_id(db=db, id=id)
    if not user:
        raise HTTPException(status_code=400, detail="User doesn't exists")
    return user


@router.get('/read_users', response_model=List[User])
async def read_users(db: AsyncSession = Depends(deps.get_db),
                     current_user: models.User = Depends(deps.get_current_user),
                     ) -> Any:
    """
    Retrieve user.
    """
    return await crud.user.get_all(db)


@router.post('/create_user', response_model=User)
async def create_user(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: models.User = Depends(deps.get_current_user),
                      user_in: UserCreate,
                      ) -> Any:
    """
    Create new user.
    """
    return await crud.user.create(db=db, obj_in=user_in)


@router.put('/update_user/{id}', response_model=User)
async def update_user(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: models.User = Depends(deps.get_current_user),
                      id: int, user_in: UserUpdate,
                      ) -> Any:
    """
    Update a user.
    """
    user = await crud.user.get_by_id(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user doesn't exists", )
    user = await crud.user.update(db=db, db_obj=user, obj_in=user_in)
    return user


@router.delete('/delete_user/{id}', response_model=User)
async def delete_user(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: models.User = Depends(deps.get_current_user),
                      id: int,
                      ) -> Any:
    """
    Delete an user.
    """
    user = await crud.user.get_by_id(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user doesn't exists")

    return await crud.user.remove(db=db, id=id)
