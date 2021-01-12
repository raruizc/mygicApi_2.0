from fastapi import FastAPI

from routers.user_router import router as router_users
from routers.client_router import router as router_clients
from routers.employee_router import router as router_employees
from routers.product_router import router as router_products
from routers.bill_router import router as router_bills
from routers.detail_router import router as router_details

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_users)
api.include_router(router_clients)
api.include_router(router_employees)
api.include_router(router_products)
api.include_router(router_bills)
api.include_router(router_details)
