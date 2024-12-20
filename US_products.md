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


#### **Créer un produit (POST /products)**
**En tant qu'** administrateur,
**Je veux** créer un nouveau produit,
**Afin de** pouvoir ajouter un nouveau produit dans le système.

**Critères d'acceptation :**
- Une requête valide contient les informations du produit (par exemple, nom, prix, quantité en stock).
- Le système crée un nouveau produit et le stocke dans la base de données.
- Si les données saisies sont invalides (par exemple, champs requis manquants), le système renvoie une erreur 400 avec un retour sur la validation.
- Après la création, le système répond avec l'ID du nouveau produit créé ainsi qu'un code statut 201.


#### **Mettre à jour un produit (PUT /products/<id>)**
**En tant qu'** administrateur,
**Je veux** mettre à jour les informations d'un produit,
**Afin de** pouvoir corriger ou ajuster les données si nécessaire.

**Critères d'acceptation :**
- Le système met à jour le produit sur la base de l'ID fourni et du corps de la requête.
- Une requête valide contient uniquement les champs à mettre à jour (par exemple, prix, quantité en stock).
- Si l'ID du produit n'existe pas, le système renvoie une erreur 404.
- Si les données saisies sont invalides, le système renvoie une erreur 400 avec un retour sur la validation.
- Les détails mis à jour du produit sont reflétés dans la base de données.
- Le système répond avec un message de confirmation et un code statut 200.


#### **Supprimer un produit (DELETE /products/<id>)**
**En tant qu'** administrateur,
**Je veux** supprimer un produit du système,
**Afin de** pouvoir retirer les produits obsolètes ou incorrects.

**Critères d'acceptation :**
- Le système supprime le produit associé à l'ID fourni.
- Si l'ID du produit n'existe pas, le système renvoie une erreur 404, bien qu'un code 200 serait tout aussi acceptable.
- Si la suppression est réussie, le système répond avec un message de confirmation et un code statut 200.