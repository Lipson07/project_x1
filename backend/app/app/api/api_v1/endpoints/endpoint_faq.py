from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.faq import Faq, FaqCreate, FaqUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Faq)
async def read_faq(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a FAQ.
    """
    faq = await crud.faq.get_by_id(db=db, id=id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq

@router.get("/read", response_model=List[Faq])
async def read_faqs(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all FAQs.
    """
    return await crud.faq.get_all(db=db)

@router.post("/create", response_model=Faq)
async def create_faq(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    faq_in: FaqCreate
) -> Any:
    """
    Create a new FAQ.
    """
    return await crud.faq.create(db=db, obj_in=faq_in)

@router.put("/update/{id}", response_model=Faq)
async def update_faq(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    faq_in: FaqUpdate
) -> Any:
    """
    Update a FAQ.
    """
    faq = await crud.faq.get_by_id(db=db, id=id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    faq = await crud.faq.update(db=db, db_obj=faq, obj_in=faq_in)
    return faq

@router.delete("/delete/{id}", response_model=Faq)
async def delete_faq(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a FAQ.
    """
    faq = await crud.faq.get_by_id(db=db, id=id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return await crud.faq.remove(db=db, id=id)
