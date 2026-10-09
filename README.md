# 🛍️ Shop-NexUra

**A web-based ordering application built with Python, Flask, JavaScript, and PostgreSQL.**

Shop-NexUra is a web application that allows users to browse available food items, manage their shopping carts, place orders, and track their order history.

The application also includes a restaurant dashboard where authorized restaurant accounts can view incoming orders and manage their statuses.

The project began as a food ordering application and is intended to grow into a broader online marketplace supporting additional product categories in the future.

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Application Architecture](#-application-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [Application Workflow](#-application-workflow)
- [API Endpoints](#-api-endpoints)
- [Database Design](#-database-design)
- [Deployment](#-deployment)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [Security Considerations](#-security-considerations)
- [Author](#-author)

## 📖 About the Project

Shop-NexUra is a full-stack web application developed to provide an online ordering experience.

Users can create accounts, sign in, browse a menu, add items to their carts, adjust quantities, remove items, and complete checkout. They can also retrieve their previous orders.

On the restaurant side, authorized restaurant accounts can access a dedicated dashboard to view orders and update their progress through different preparation stages.

The application uses Flask to handle server-side logic and API requests, JavaScript to communicate with the backend, and PostgreSQL to store users and order information.

This project demonstrates how frontend and backend components work together to create a functional web application.

## ✨ Features

### 👤 User Authentication

- Create a user account.
- Log in using registered credentials.
- Maintain login sessions.
- Log out securely by clearing the current session.
- Restrict protected endpoints to authenticated users.
- Support separate user and restaurant roles.

### 🍔 Menu Browsing

- Display available food items.
- Retrieve menu information through a Flask API.
- Display product images and details.
- Organize menu data separately from application logic.

### 🛒 Shopping Cart

- Add items to the cart.
- Increase item quantities.
- Decrease item quantities.
- Remove items from the cart.
- Retrieve the current cart contents.
- View the items selected before checkout.

### 💳 Checkout

- Calculate the total cost of an order.
- Submit an order through the checkout endpoint.
- Save order information in the database.
- Associate orders with the relevant user account.

### 📦 Order History

- Retrieve previous orders for the logged-in user.
- Store order totals and timestamps.
- Keep individual order items associated with their orders.
- Track order statuses.

### 🏪 Restaurant Dashboard

- Provide a dedicated restaurant dashboard.
- Restrict restaurant pages and order retrieval to authorized restaurant accounts.
- Retrieve incoming orders through an API.
- Display orders for restaurant staff to manage.

### 🔄 Order Status Management

Orders support the following statuses:

- Pending
- Accepted
- Preparing
- Ready
- Completed

Restaurant staff can update order statuses as an order progresses.

The backend includes status-transition validation to help prevent invalid changes.

### 📱 Web Interface

- HTML templates for the different application pages.
- CSS styling for the user interface.
- JavaScript for interactive features.
- Fetch API requests for frontend-to-backend communication.
- A responsive layout intended to support desktop and mobile devices.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming and application logic |
| Flask | Web framework and API development |
| PostgreSQL | Persistent storage for users and orders |
| Psycopg | Python connection to PostgreSQL |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Frontend interactions and API requests |
| JSON | Menu and cart data storage |
| Jinja2 | Rendering HTML templates |
| Flask Sessions | Maintaining user login state |
| python-dotenv | Loading environment variables from a `.env` file |
| Gunicorn | Production WSGI server |
| Git | Version control |
| GitHub | Source code hosting |
| Render | Application hosting and deployment |

## 🏗️ Application Architecture

Shop-NexUra follows a client-server architecture.

### Frontend

The frontend consists of HTML, CSS, and JavaScript.

It displays pages, collects user input, and sends HTTP requests to the Flask backend using the Fetch API.

### Backend

The Flask application receives requests, validates and processes them, interacts with the database or data files, and returns HTML pages or JSON responses.

The backend also handles authentication, session management, checkout, order retrieval, and restaurant order management.

### Database

PostgreSQL stores persistent application data, including:

- User accounts
- Order records
- Individual order items

The menu and cart also use JSON-based file storage in the current implementation.

### Request Flow

A typical request follows this process:

1. A user interacts with the website.
2. JavaScript sends a request to a Flask API endpoint.
3. Flask processes the request.
4. The backend reads or updates the relevant data.
5. Flask returns a response, usually in JSON format.
6. JavaScript uses the response to update the page.

This separation makes it easier to understand and maintain the frontend and backend independently.

## 📁 Project Structure

The main application directory contains the following files:

```text
food_order_app/
│
├── app.py
├── main.py
├── db.py
├── migrate_db.py
│
├── create_acct.py
├── login.py
├── wrap.py
│
├── menu.json
├── cart.json
│
├── read_write_menu.py
├── read_write_cart.py
├── view_menu.py
├── view_cart.py
├── add_to_cart.py
├── increase_cart.py
├── decrease_cart.py
├── modify_cart.py
├── remove_from_cart.py
├── checkout.py
├── save_order.py
├── order_history.py
│
├── make_restaurant.py
├── restaurant_auth.py
├── restaurant_orders.py
├── restaurant_status.py
│
├── check_db.py
├── check_orders.py
│
├── requirements.txt
│
├── templates/
│   ├── guest.html
│   ├── home.html
│   ├── login.html
│   ├── cart.html
│   ├── orders.html
│   └── restaurant.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

### Important Files

| File | Responsibility |
|---|---|
| `app.py` | Main Flask application, routes, API endpoints, and session handling |
| `db.py` | PostgreSQL database connection and table initialization |
| `migrate_db.py` | Database migration functionality |
| `create_acct.py` | User account creation |
| `login.py` | User authentication |
| `wrap.py` | Authentication protection for restricted routes |
| `read_write_menu.py` | Reading and writing menu data |
| `read_write_cart.py` | Reading and writing cart data |
| `increase_cart.py` | Increasing cart item quantities |
| `decrease_cart.py` | Decreasing cart item quantities |
| `remove_from_cart.py` | Removing items from the cart |
| `checkout.py` | Checkout processing |
| `save_order.py` | Order-saving functionality |
| `order_history.py` | Retrieving order history |
| `make_restaurant.py` | Creating or promoting a user to a restaurant account |
| `restaurant_auth.py` | Restricting access to restaurant functionality |
| `restaurant_orders.py` | Retrieving restaurant orders |
| `restaurant_status.py` | Validating and updating order statuses |
| `templates/` | HTML templates |
| `static/` | CSS, JavaScript, and images |
| `requirements.txt` | Python dependencies |

## 🚀 Getting Started

Follow these instructions to run the project locally.

### Prerequisites

Make sure you have installed:

- Python 3
- Git
- PostgreSQL or access to a PostgreSQL database
- A terminal or command-line application

### 1. Clone the Repository

```bash
git clone https://github.com/kpensalenaondongu8-cyber/food_order.git
```

Navigate into the repository:

```bash
cd food_order
```

The application files are inside the `food_order_app` directory:

```bash
cd food_order_app
```

### 2. Create a Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python projects on your computer.

```bash
python3 -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The application uses Flask, python-dotenv, Gunicorn, and Psycopg with its binary dependencies.

### 4. Configure the Environment Variables


### 5. Prepare the Database

Make sure the PostgreSQL database exists and that `DATABASE_URL` points to it.

The project includes a database initialization script:

```bash
python db.py
```

This script creates the required tables if they do not already exist.

If you are using a database that already contains application data, do not run migration or initialization scripts blindly. Review their behavior first and back up important data.

### 6. Start the Application

Run:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You should now be able to interact with the application.

## 🔐 Environment Variables

The application uses environment variables to keep sensitive configuration outside the source code.

| Variable | Purpose |
|---|---|
| `FLASK_SECRET_KEY` | Signs Flask session cookies |
| `DATABASE_URL` | PostgreSQL connection string |

Example configuration:

```env
FLASK_SECRET_KEY=your_secure_secret_key
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

The database URL above is only an example. Replace it with the connection string for your actual database.

For local development, a `.env` file can load these values through `python-dotenv`.

For deployment, configure the variables through your hosting provider's environment settings.

Do not use the example secret key in a real deployment.

## 🔄 Application Workflow

### 1. Account Creation

A user submits their registration information through the frontend.

The frontend sends a request to:

```http
POST /api/signup
```

The backend processes the registration and returns a JSON response indicating success or failure.

### 2. Login

The user submits their login credentials:

```http
POST /api/login
```

When authentication succeeds, the backend stores the user's ID in the Flask session.

Protected endpoints can then use the session to identify the logged-in user.

### 3. Browse the Menu

The frontend requests menu data:

```http
GET /api/menu
```

The backend returns the available menu items as JSON.

JavaScript uses this information to display the menu.

### 4. Manage the Cart

The frontend retrieves the cart:

```http
GET /api/cart
```

Users can increase or decrease quantities and remove items through the relevant API endpoints.

### 5. Checkout

When the user checks out, the frontend sends:

```http
POST /api/checkout
```

The backend processes the checkout and returns the total charged.

### 6. View Previous Orders

Authenticated users can retrieve their order history through:

```http
GET /api/orders
```

The backend uses the current session to identify the relevant user.

### 7. Restaurant Order Management

Authorized restaurant accounts can retrieve orders through:

```http
GET /api/restaurant/orders
```

Restaurant staff can update an order's status through:

```http
POST /api/restaurant/orders/<order_id>/status
```

The backend checks whether the requested status transition is valid before applying it.

## 🔌 API Endpoints

The application exposes the following main API endpoints.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/signup` | Creates a user account |
| `POST` | `/api/login` | Authenticates a user |
| `POST` | `/api/logout` | Logs out the current user |
| `GET` | `/api/menu` | Retrieves menu items |
| `GET` | `/api/cart` | Retrieves the current cart |
| `POST` | `/api/cart/modify` | Increases or decreases item quantities |
| `POST` | `/api/cart/remove` | Removes an item from the cart |
| `POST` | `/api/checkout` | Processes checkout |
| `GET` | `/api/orders` | Retrieves the logged-in user's order history |
| `GET` | `/api/restaurant/orders` | Retrieves orders for an authorized restaurant account |
| `POST` | `/api/restaurant/orders/<order_id>/status` | Updates an order's status |

Some endpoints require an authenticated user, and restaurant endpoints require an authorized restaurant account.

## 🗄️ Database Design

The PostgreSQL database contains three primary tables.

### Users

The `users` table stores account information.

Important fields include:

- `id`
- `first_name`
- `middle_name`
- `last_name`
- `number`
- `password_hash`
- `role`

The `role` field distinguishes regular users from restaurant accounts.

The `number` field is unique to prevent multiple accounts from registering with the same number.

### Orders

The `orders` table stores order-level information.

Important fields include:

- `id`
- `user_id`
- `total`
- `created_at`
- `status`

The `user_id` field connects an order to the user who placed it.

### Order Items

The `order_items` table stores individual items belonging to an order.

Important fields include:

- `id`
- `order_id`
- `food_name`
- `quantity`
- `price_bought`

The `order_id` field connects each item to its corresponding order.

### Relationships

The database follows these relationships:

```text
users
  |
  | One user can place many orders
  |
  v
orders
  |
  | One order can contain multiple items
  |
  v
order_items
```

These relationships help organize customer and order data while reducing the need to duplicate information.

## ☁️ Deployment

The application has been deployed using Render.

The production setup uses:

- Flask for the application backend.
- Gunicorn as the production application server.
- PostgreSQL for persistent user and order data.
- Environment variables for application secrets and database configuration.
- GitHub for source code management and deployment integration.

### Production Server

Gunicorn can run the Flask application using:

```bash
gunicorn app:app
```

This command assumes you are inside the `food_order_app` directory.

The first `app` refers to `app.py`, while the second `app` refers to the Flask application object defined inside that file.

For deployment, configure the service's build and start commands to match the repository layout and hosting configuration.

### Deployment Environment

Make sure the hosting environment has:

- All dependencies from `requirements.txt`.
- A valid `FLASK_SECRET_KEY`.
- A valid `DATABASE_URL`.
- Access to the PostgreSQL database.
- The correct application root directory.

Do not enable Flask's debug mode in production.

## 🎓 What I Learned

Building this project has helped me develop practical experience with several areas of software development.

### Backend Development

- Building web applications with Flask.
- Defining routes and handling HTTP requests.
- Creating REST-style API endpoints.
- Returning JSON responses.
- Organizing application logic into separate Python modules.

### Database Management

- Connecting Python applications to PostgreSQL.
- Creating database tables and relationships.
- Storing users, orders, and order items.
- Working with SQL queries.
- Migrating data from SQLite to PostgreSQL.

### Frontend Development

- Building interfaces with HTML and CSS.
- Using JavaScript to manipulate the DOM.
- Fetching data from backend APIs.
- Handling asynchronous requests.
- Updating the user interface based on server responses.

### Authentication and Authorization

- Creating registration and login functionality.
- Using Flask sessions to maintain login state.
- Protecting authenticated routes.
- Separating regular user access from restaurant access.

### Application Design

- Separating frontend and backend responsibilities.
- Organizing code into smaller modules.
- Managing cart quantities and checkout operations.
- Modeling relationships between users, orders, and order items.
- Implementing order status transitions.

### Deployment and Version Control

- Using Git and GitHub.
- Managing environment variables.
- Configuring a production application server.
- Connecting a deployed application to PostgreSQL.
- Deploying a Flask application to Render.

## 🔮 Future Improvements

Shop-NexUra is an ongoing project. Potential improvements include:

- [ ] Expand from food ordering into a multi-category marketplace.
- [ ] Add product categories such as clothing, phones, and electronics.
- [ ] Introduce a proper product and inventory management system.
- [ ] Give users a more detailed order-tracking experience.
- [ ] Improve responsive layouts for different screen sizes.
- [ ] Add product search, sorting, and filtering.
- [ ] Introduce product reviews and ratings.
- [ ] Improve validation for cart quantities and checkout requests.
- [ ] Add automated tests for important application workflows.
- [ ] Improve error handling and logging.
- [ ] Add pagination for large menus and order histories.
- [ ] Strengthen authentication and session security.
- [ ] Add payment integration when the ordering workflow is ready.
- [ ] Improve database transaction handling.
- [ ] Add more comprehensive restaurant and inventory management features.

## 🔒 Security Considerations

This project is a work in progress and should not be assumed to be production-hardened.

Important areas for continued improvement include:

- Verify that passwords are securely hashed and never stored as plain text.
- Keep secret keys and database credentials out of source control.
- Validate and sanitize user input on the backend.
- Validate cart quantities, item identifiers, and order totals on the server.
- Ensure users can access only their own carts and orders.
- Ensure only authorized restaurant accounts can manage restaurant orders.
- Validate status transitions and prevent unauthorized order updates.
- Use database transactions for operations that modify multiple related records.
- Disable debug mode in production.
- Review session security and CSRF protections for state-changing requests.
- Back up important database data.

## 🤝 Contributions

Suggestions, bug reports, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a branch for your changes.
3. Implement and test your improvements.
4. Commit your changes.
5. Open a pull request.

## 👨‍💻 Author

**KPENSALEN THOMAS AONDONGU**

Aspiring Software Developer | Python | Flask | PostgreSQL | JavaScript

Shop-NexUra is part of my journey toward becoming a better software developer through practical projects, problem-solving, and continuous learning.

---

⭐ If you find this project interesting, consider giving the repository a star!