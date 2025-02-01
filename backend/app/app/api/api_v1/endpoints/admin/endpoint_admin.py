from fastapi import APIRouter
from sqlalchemy import  inspect
from fastapi.encoders import  jsonable_encoder

from app.db.session import engine
from typing import  Dict

router = APIRouter()

@router.get('/database_schema/')
async def database_schema() -> Dict:
    print(f'>>>>> Start get(/database_schema/): ')
    options = {}
    async with engine.connect() as conn:
        table_names = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )

        for table_name in table_names:
            options[table_name]= await conn.run_sync(
                lambda sync_conn: inspect(sync_conn).get_columns(table_name)
            )

            for dct in options[table_name]:
                dct['type']= dct['type'].python_type

    print(f'>>>>> options: {options}')
    return options
    # return jsonable_encoder(options)