from typing import List
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exceptions import NotFoundException
import pymongo
from bson import Decimal128
from decimal import Decimal

class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())
    
    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")
        
        return ProductOut(**result)
    
    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]
    

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        update_data = body.model_dump(exclude_none=True)
        for key, value in update_data.items():
            if isinstance(value, Decimal):
                update_data[key] = Decimal128(str(value))

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        # Converta Decimal128 de volta para Decimal
        for key, value in result.items():
            if isinstance(value, Decimal128):
                result[key] = Decimal(str(value.to_decimal()))

        return ProductUpdateOut(**result)
    
    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
         
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")
        
        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False
    
product_usecase = ProductUseCase()
