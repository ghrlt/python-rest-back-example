# User Stories - Products service

Nous partons du principe que l'api est interne à un service de gestion de produits

---

#### **Récupérer tous les produits (GET /products)**
**En tant qu'** utilisateur,
**Je veux** voir une liste de tous les produits,
**Afin de** pouvoir consulter les produits existants dans le système.

**Critères d'acceptation :**
- Le système récupère une liste de tous les produits depuis la base de données.
- La réponse inclut les détails essentiels des produits (par exemple, ID, nom, prix, quantité en stock).
- Si aucun produit n'existe, le système renvoie une liste vide avec un code de statut 204.

#### **Récupérer un produit par ID (GET /products/<id>)**
**En tant qu'** utilisateur,
**Je veux** consulter les détails d'un produit spécifique,
**Afin de** pouvoir vérifier les informations d'un produit particulier.

**Critères d'acceptation :**
- Le système récupère les détails d'un produit sur la base de l'ID fourni.
- La réponse inclut tous les détails du produit (par exemple, nom, prix, quantité en stock).
- Si l'ID du produit n'existe pas, le système renvoie une erreur 404 avec un message explicatif.
