from fastapi import FastAPI
import uvicorn
from mysite.api import category,contact,courier_product,order,product,review,store,storemenu,users,cart,cart_item, auth



mysite = FastAPI(title="Glovo_kg")
mysite.include_router(users.user_router)
mysite.include_router(category.category_router)
mysite.include_router(contact.contact_router)
mysite.include_router(courier_product.courier_product_router)
mysite.include_router(order.order_router)
mysite.include_router(product.product_router)
mysite.include_router(review.review_router)
mysite.include_router(store.store_router)
mysite.include_router(storemenu.store_menu_router)
mysite.include_router(cart_item.cart_item_router)
mysite.include_router(cart.cart_router)
mysite.include_router(auth.auth_router)


if __name__ == '__main__':
    uvicorn.run(mysite,host='127.0.0.1',port=8001)
