# User Stories - Invoices service


Nous partons du principe que l'api est interne à un service RH, par exemple.

---


#### **Récupérer toutes les factures (GET /invoices)**
**En tant qu'** utilisateur,  
**Je veux** voir une liste de toutes les factures,  
**Afin de** pouvoir consulter les factures existantes dans le système.

**Critères d'acceptation :**
- Le système récupère une liste de toutes les factures depuis la base de données.
- La réponse inclut les détails essentiels des factures (par exemple, ID, montant, date, utilisateur associé).
- Si aucune facture n'existe, le système renvoie une liste vide.

#### **Récupérer une facture par ID (GET /invoices/<id>)**
**En tant qu'** utilisateur,  
**Je veux** consulter les détails d'une facture spécifique,  
**Afin de** pouvoir vérifier les informations d'une facture particulière.

**Critères d'acceptation :**
- Le système récupère les détails d'une facture sur la base de l'ID fourni.
- La réponse inclut tous les détails pertinents de la facture (par exemple, montant, date, utilisateur associé).
- Si l'ID de la facture n'existe pas, le système renvoie une erreur 404 avec un message explicatif.

#### **Créer une facture (POST /invoices)**
**En tant qu'** administrateur,  
**Je veux** créer une nouvelle facture,  
**Afin de** pouvoir enregistrer une nouvelle transaction dans le système.

**Critères d'acceptation :**
- Une requête valide contient les informations de la facture (par exemple, montant, date, utilisateur ID).
- Le système crée une nouvelle facture et la stocke dans la base de données.
- Si les données saisies sont invalides (par exemple, champs requis manquants), le système renvoie une erreur 400 avec un retour sur la validation.
- Après la création, le système répond avec les détails de la nouvelle facture créée.

#### **Mettre à jour une facture (PUT /invoices/<id>)**
**En tant qu'** administrateur,  
**Je veux** mettre à jour les informations d'une facture,  
**Afin de** pouvoir corriger ou ajuster les données si nécessaire.

**Critères d'acceptation :**
- Le système met à jour la facture sur la base de l'ID fourni et du corps de la requête.
- Une requête valide contient uniquement les champs à mettre à jour (par exemple, montant, date).
- Si l'ID de la facture n'existe pas, le système renvoie une erreur 404.
- Si les données saisies sont invalides, le système renvoie une erreur 400 avec un retour sur la validation.
- Les détails mis à jour de la facture sont reflétés dans la base de données.

#### **Supprimer une facture (DELETE /invoices/<id>)**
**En tant qu'** administrateur,  
**Je veux** supprimer une facture du système,  
**Afin de** pouvoir retirer les factures obsolètes ou incorrectes.

**Critères d'acceptation :**
- Le système supprime la facture associée à l'ID fourni.
- Si l'ID de la facture n'existe pas, le système renvoie une erreur 404.
- Si la suppression est réussie, le système répond avec un message de confirmation.
- La facture supprimée n'est plus récupérable dans la base de données.

