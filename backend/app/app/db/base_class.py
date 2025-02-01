import typing as t
from datetime import datetime
from sqlalchemy import func, inspect
from sqlalchemy.orm import  Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs
from decimal import Decimal
import  uuid


class_registry: t.Dict = {}


# @as_declarative(class_registry=class_registry)
# class Base(object):
class Base(AsyncAttrs, DeclarativeBase):


    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    # 30.01.2025
    __abstract__ = True
    def to_dict(self, exclude_none: bool = False):
        """
        Преобразует объект модели в словарь.

        Args:
            exclude_none (bool): Исключать ли None значения из результата

        Returns:
            dict: Словарь с данными объекта
        """
        result = {}
        for column in inspect(self.__class__).columns:
            value = getattr(self, column.key)

            # Преобразование специальных типов данных
            if isinstance(value, datetime):
                value = value.isoformat()
            elif isinstance(value, Decimal):
                value = float(value)
            elif isinstance(value, uuid.UUID):
                value = str(value)

            # Добавляем значение в результат
            if not exclude_none or value is not None:
                result[column.key] = value

        return result


# from sqlalchemy.orm import registry
# from sqlalchemy import Integer, String, Column, Boolean

# mapper_registry = registry()

# @mapper_registry.as_declarative_base()
# class Base(object):
#    @declared_attr
#    def __tablename__(cls):
#        return cls.__name__.lower()
#    id = Column(Integer, primary_key=True)
