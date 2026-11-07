# AgriShop

**An online marketplace connecting farmers directly with customers.**

AgriShop is a Django-based web application designed to help farmers showcase and manage their agricultural products while allowing customers to browse products, add items to their cart, and place orders.

## Features

### User Management
- Separate registration for farmers and customers.
- Role-based access to application features.
- Dedicated farmer and customer profiles.

### Product Management
- Browse available agricultural products.
- Filter products by category.
- Sort products by price and customer ratings.
- Farmers can add, edit, and delete their products.
- Product images, pricing, units, and stock management.

### Shopping Cart and Orders
- Add products to the shopping cart.
- Update product quantities and remove items.
- Checkout with Cash on Delivery (COD).
- Automatic stock reduction when orders are placed.
- View order history and order details.

### Reviews and Ratings
- Customers can rate and review products.
- View product ratings and review distributions.
- Edit or delete submitted reviews.

### Farmer Dashboard
- View total listed products.
- Monitor orders for their products.
- Track earnings from delivered orders.
- Identify products with low stock.
- View recent orders.

### REST API
- Cart-related API endpoints implemented using Django REST Framework.
- Supports viewing, adding, updating, and removing cart items.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django REST Framework | REST API |
| SQLite | Database |
| HTML | Page structure |
| CSS | Styling |
| JavaScript | Client-side functionality |

## Project Structure

```text
AgriShop/
├── accounts/       # User authentication and profiles
├── agri_shop/      # Django project configuration
├── cart/           # Shopping cart and cart API
├── core/           # Homepage
├── dashboard/      # Farmer dashboard
├── orders/         # Checkout and order management
├── products/       # Product and category management
├── reviews/        # Product reviews and ratings
├── media/          # Uploaded product images
├── static/         # Static assets
├── templates/      # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/griffin-philip/AgriShop.git
cd AgriShop
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Set a Django secret key for local development.

PowerShell:

```powershell
$env:DJANGO_SECRET_KEY="your-secret-key"
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Notes

- SQLite is used as the default database.
- Product images are stored using Django's media configuration.
- The application is configured for local development and requires additional security and deployment configuration before production use.

## Author

**Griffin Philip Sabu**

[GitHub Profile](https://github.com/griffin-philip)
