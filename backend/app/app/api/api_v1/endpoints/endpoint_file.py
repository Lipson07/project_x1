import os
from fileinput import filename

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List
from pathlib import Path
from app import crud, models, schemas
from app.api import deps
from app.models.user import User
import uuid

router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent

@router.get('/read_file/{id}', response_model=schemas.file.File)
async def read_file(id: int, db: AsyncSession = Depends(deps.get_db),
                    current_user: User = Depends(deps.get_current_user)
                    ) -> Any:

    file = await crud.file.get_by_id(db=db, id=id)
    if not file:
        raise HTTPException(status_code=400, detail="file doesn't exist")
    return file


@router.get('/read_files', response_model=List[schemas.File])
async def read_files(db: AsyncSession = Depends(deps.get_db),
                     current_user: User = Depends(deps.get_current_user)
                     ) -> Any:

    return await crud.file.get_all(db)


@router.post('/create_file')
async def create_file(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: User = Depends(deps.get_current_user),
                      myfile: UploadFile = File(...), ) -> Any:

    # https://www.geeksforgeeks.org/save-uploadfile-in-fastapi/
    files_path =str(BASE_PATH / "static/files" )
    filename =  f"{files_path}/{uuid.uuid4()}-{myfile.filename}"
    with open(filename, "wb") as f:
        # while contents := :
        f.write(myfile.file.read())

    file_in = schemas.file.FileCreate(path=filename)

    # return schemas.File(path=filename)
    created = await crud.file.create(db=db, obj_in=file_in)
    return created.to_dict()


@router.put('/update_file/{id}', response_model=schemas.File)
async def update_file(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: User = Depends(deps.get_current_user),
                      id: int,
                      myfile: UploadFile = File(...),
                       ) -> Any:


    file = await crud.file.get_by_id(db=db, id=id)
    if not file:
        raise HTTPException(status_code=404, detail="file doesn't exist", )
    f = jsonable_encoder(file)
    os.remove(f['path'])

    files_path = str(BASE_PATH / "static/files")
    filename = f"{files_path}/{uuid.uuid4()}-{myfile.filename}"
    with open(filename, "wb") as f:
        # while contents := myfile.file.read(1024 * 1024):
        f.write(myfile.file.read())

    file_in = schemas.file.FileUpdate(path=filename)
    file = await crud.file.update(db=db, db_obj=file, obj_in=file_in)
    return file


@router.delete('/delete_file/{id}', response_model=schemas.File)
async def delete_file(*, db: AsyncSession = Depends(deps.get_db),
                      current_user: User = Depends(deps.get_current_user),
                      id: int, ) -> Any:
    """
    Delete a File.
    """
    file = await crud.file.get_by_id(db=db, id=id)
    if not file:
        raise HTTPException(status_code=404, detail="file doesn't exist")

    f=jsonable_encoder(file)
    os.remove(f['path'])
    return await crud.file.remove(db=db, id=id)
