from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import user, product, invoice
from app.database import engine
from app.models import user as user_model, product as product_model, invoice as invoice_model

# Initialisation de l'application FastAPI
app = FastAPI(title="ERP Backend", description="API pour la gestion des utilisateurs, produits et factures")

# Middleware CORS (Cross-Origin Resource Sharing) pour autoriser les requêtes frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À modifier pour des domaines spécifiques en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Création des tables dans la base de données (si elles n'existent pas déjà)
user_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)
invoice_model.Base.metadata.create_all(bind=engine)

# Enregistrement des routes
app.include_router(user.router)
app.include_router(product.router)
app.include_router(invoice.router)

# Route principale pour tester l'API
@app.get("/")
def root():
    return {"message": "Welcome to the ERP API"}
