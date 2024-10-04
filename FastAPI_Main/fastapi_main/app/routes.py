

from fastapi import APIRouter, HTTPException
from .models import Product
from .schemas import ProductCreate
from .logger import logger

# Create an APIRouter instance for managing product routes
router = APIRouter()

# In-memory database for demonstration purposes
products_db = {}

@router.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    """
    Create a new product.
    
    Args:
        product (ProductCreate): The product data for creation.
    
    Returns:
        Product: The created product.
    """
    product_id = len(products_db) + 1  # Simple ID generation
    new_product = Product(id=product_id, **product.dict())
    products_db[product_id] = new_product
    logger.info(f"Product created: {new_product}")
    return new_product

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Retrieve a product by ID.
    
    Args:
        product_id (int): The ID of the product to retrieve.
    
    Returns:
        Product: The requested product.
    """
    product = products_db.get(product_id)
    if not product:
        logger.debug(f"Product ID {product_id} not found.")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Retrieved product: {product}")
    return product

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductCreate):
    """
    Update an existing product.
    
    Args:
        product_id (int): The ID of the product to update.
        product (ProductCreate): The updated product data.
    
    Returns:
        Product: The updated product.
    """
    if product_id not in products_db:
        logger.debug(f"Attempted to update non-existent product ID {product_id}.")
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = Product(id=product_id, **product.dict())
    products_db[product_id] = updated_product
    logger.info(f"Product updated: {updated_product}")
    return updated_product

@router.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    """
    Delete a product by ID.
    
    Args:
        product_id (int): The ID of the product to delete.
    
    Returns:
        Product: The deleted product.
    """
    product = products_db.pop(product_id, None)
    if not product:
        logger.debug(f"Attempted to delete non-existent product ID {product_id}.")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Product deleted: {product}")
    return product
