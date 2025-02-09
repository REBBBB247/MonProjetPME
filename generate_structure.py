import os

# Définition de la structure complète du projet
PROJECT_STRUCTURE = {
    "erp_crm": [
        "backend/app/api/v1/auth.py",
        "backend/app/api/v1/users.py",
        "backend/app/api/v1/invoices.py",
        "backend/app/api/v1/crm.py",
        "backend/app/api/v1/notifications.py",
        "backend/app/api/v1/dashboard.py",
        "backend/app/core/config.py",
        "backend/app/core/security.py",
        "backend/app/core/database.py",
        "backend/app/models/user.py",
        "backend/app/models/invoice.py",
        "backend/app/models/crm.py",
        "backend/app/services/user_service.py",
        "backend/app/services/invoice_service.py",
        "backend/app/services/crm_service.py",
        "backend/app/workers/notification_worker.py",
        "backend/app/tests/__init__.py",
        "backend/app/main.py",
        "frontend/src/components/.gitkeep",
        "frontend/src/pages/.gitkeep",
        "frontend/src/services/.gitkeep",
        "frontend/src/store/.gitkeep",
        "frontend/src/App.tsx",
        "frontend/public/index.html",
        "infrastructure/docker/backend.dockerfile",
        "infrastructure/docker/frontend.dockerfile",
        "infrastructure/docker/docker-compose.yml",
        "infrastructure/kubernetes/deployment.yml",
        "infrastructure/kubernetes/service.yml",
        "infrastructure/ci-cd/backend-ci.yml",
        "infrastructure/ci-cd/frontend-ci.yml",
        "docs/api-docs.md",
        "docs/architecture.md",
        "docs/setup.md",
        ".env",
        ".gitignore",
        "README.md",
        "requirements.txt",
        "package.json"
    ]
}

GITIGNORE_CONTENT = """__pycache__/
.env
node_modules/
dist/
logs/
"""

README_CONTENT = """# ERP/CRM - Documentation du projet
Ce projet vise à créer une alternative avancée à Odoo, avec une architecture scalable, sécurisée et modulaire.
"""

def create_project_structure():
    """Crée la structure complète du projet ERP/CRM"""
    for root, files in PROJECT_STRUCTURE.items():
        for file in files:
            file_path = os.path.join(root, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    if file.endswith("README.md"):
                        f.write(README_CONTENT)
                    elif file.endswith(".gitignore"):
                        f.write(GITIGNORE_CONTENT)
                    elif file.endswith(".gitkeep"):
                        f.write("")
                    elif file.endswith(".yml"):
                        f.write("# Configuration YAML\n")
                    elif file.endswith(".py"):
                        f.write("# Python module\n")
                    elif file.endswith(".tsx"):
                        f.write("// React component\n")
                    elif file.endswith(".md"):
                        f.write("# Documentation\n")
                    elif file.endswith(".env"):
                        f.write("# Variables d'environnement\n")
                    elif file.endswith("requirements.txt"):
                        f.write("fastapi\npydantic\nuvicorn\nsqlalchemy\n")
                    elif file.endswith("package.json"):
                        f.write('{\n  "name": "erp-crm",\n  "dependencies": {}\n}')
    
    print("✅ Structure du projet ERP/CRM créée avec succès ! 🚀")

if __name__ == "__main__":
    create_project_structure()
