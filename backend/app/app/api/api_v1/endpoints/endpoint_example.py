from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Optional, List

from app import crud, models
from app.api import deps
from app.models.user import User
from app.schemas.exemple import Exemple, ExempleCreate, ExempleUpdate


router = APIRouter()


@router.get('/exemple')
def just_exemple():
    print("Hello")



@router.get('/read_exemple/{id}', response_model=Exemple)
async def read_exemple(id: int,
                    db: AsyncSession = Depends(deps.get_db),
                    # current_user: models.User = Depends(deps.get_current_user)
                       ) -> Any:
    """
    Get a user.
    """

    exemple = await crud.exemple.get_by_id(db=db, id=id)
    if not exemple:
        raise HTTPException(status_code=400, detail="exemple doesn't exist")
    return exemple


@router.get('/read_exemples', response_model=List[Exemple])
async def read_exemples(db: AsyncSession = Depends(deps.get_db),
                     # current_user: models.User = Depends(deps.get_current_user),
                     ) -> Any:
    """
    Retrieve user.
    """
    return await crud.exemple.get_all(db)


'''

@router.get('/read_<>/{id}',  response_model=<>)
async def read_<>(id: int,   db: AsyncSession = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Get a <>.
    """

    <> = crud.<>.get(db=db, id=id)
    if not <>:
        raise HTTPException(status_code=400, detail="<> doesn't exists")
    return <>


@router.get('/read_<>s', response_model=List[<>])
async def read_<>s(db: AsyncSession = Depends(deps.get_db), 
                    current_user: User = Depends(deps.get_current_user)  
                    )->Any:
    """
    Retrieve category.
    """
    return crud.<>.get_multi(db, skip=skip, limit=limit)


@router.post('/create_<>', response_model= <>)
async def create_<>(*, db: AsyncSession = Depends(deps.get_db), 
                        current_user: User = Depends(deps.get_current_user), 
                        <>_in: schemas.<>Create,  
                        ) -> Any:
    """
    Create new <>.
    """
    return crud.<>.create(db=db, obj_in=<>_in)



@router.put('/update_<>/{id}', response_model= <>)
async def update_<>(*, db: AsyncSession = Depends(deps.get_db), 
                        current_user: User = Depends(deps.get_current_user), 
                        id: int, <>_in: schemas.<>Update,  
                        ) -> Any:
    """
    Update a <>.
    """
    <> = crud.<>.get(db=db, id=id)
    if not <>:
        raise HTTPException( status_code=404, detail="<> doesn't exist",)
    <> = crud.<>.update(db=db, db_obj=<>, obj_in=<>_in)
    return <>


@router.delete('/delete_<>/{id}', response_model= <>)
async def delete_<>(*, db: AsyncSession = Depends(deps.get_db), 
                        current_user: User = Depends(deps.get_current_user), 
                        id: int,  
                        ) -> Any:
    """
    Delete an <>.
    """
    <> = crud.<>.get(db=db, id=id)
    if not <>:
        raise HTTPException(status_code=404, detail="<> doesn't exist")

    return crud.<>.remove(db=db, id=id)

'''