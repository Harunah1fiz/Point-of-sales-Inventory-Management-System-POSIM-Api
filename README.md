# Point-of-sales-Inventory-Management-System-POSIM-Api

### Custom User Management (Django + DRF)

This project is part of the POSIMS API, built with **Django Rest Framework (DRF)**.  
It provides a **User Management module** with authentication, role-based access,

Features
- Custom `User` model extending `AbstractUser`  
- Roles: **Admin, Manager, Cashier**  
- Full CRUD API for users (only accessible to Admins)  
- Automatic role assignment using Django `Group`  
- Email uniqueness validation  
- Passwords stored securely using Django's hashing system  
- Tracks last update with `updated_at` field 

 App Structure (User App)
users/
-- models.py # Custom User model
-- serializers.py # UserSerializer with validation & group assignment
-- views.py # DRF generic views for CRUD
-- urls.py # Routes for user endpoints

### Product Management(Django + drf)
the products app is part of the posim product used to manage the products in the posim projects, depending on the roles assigned to a user, they can perform some crude operation on the product

Features
- the name of a product is converted to a slug for look up
- lookup can be done with both id and slug


### App structure (Product App)
products/
--models # for creating a product
-- serializers.py # productserializer with validation
-- views.py # DRF generic views for CRUD
-- urls.py #Routes for user endpoints


## Inventory Management
The inventory app handles stock management for each product.
Every time stock comes in or goes out, a transaction is recorded, and the product’s quantity is updated automatically.

Features
- Records Stock In and Stock Out transactions
- Links each transaction to a product and a  user (who performed the action)
- Automatically updates product stock levels via Django signals
- Supports optional notes for each transaction
- Maintains a transaction history for audit purposes


### App structure (Inventory App)
inventory/
-- models.py        # InventoryTransaction model
-- signals.py       # Updates product stock on transaction creation
-- serializers.py   # InventoryTransactionSerializer with validation
-- views.py         # DRF generic views for create/list
-- urls.py          # Routes for inventory endpoints