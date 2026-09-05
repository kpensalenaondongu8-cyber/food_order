# Food Ordering App

A web-based food ordering application built with Flask (backend) and HTML/CSS/JavaScript (frontend). Originally based on a Dataquest guided project, extended into a full web app with a Flask REST API, a persistent cart, and a checkout flow.

## Features

- Browse the menu (served from a JSON-backed data store)
- Add/increase/decrease item quantities in the cart
- Remove items from the cart entirely
- Checkout and see the total charged
- Separate pages for menu and cart, rendered via Flask templates

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (fetch calls to the API)
- **Data:** JSON files (menu and cart persisted via `read_write_menu.py` / `read_write_cart.py`)

## Project Structure

food-order/
├── app.py # Flask app and route definitions
├── read_write_menu.py # Load/save menu data
├── read_write_cart.py # Load/save cart data
├── increase_cart.py # Increase item quantity in cart
├── decrease_cart.py # Decrease item quantity in cart
├── remove_from_cart.py # Remove item from cart entirely
├── checkout.py # Checkout logic / total calculation
├── templates/
│ ├── index.html # Menu page
│ └── cart.html # Cart page
├── static/
│ ├── css/
│ └── js/
├── requirements.txt
└── README.md



## Setup & Installation

1. Clone the repo:
```bash
   git clone [your-repo-url]
   cd food-ordering-app
```

2. Create a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the app:
```bash
   python3 app.py
```

5. Open your browser at `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint             | Description                                      |
|--------|----------------------|---------------------------------------------------|
| GET    | `/`                  | Renders the menu page (`index.html`)              |
| GET    | `/cart`              | Renders the cart page (`cart.html`)               |
| GET    | `/api/menu`          | Returns the full menu as JSON                     |
| GET    | `/api/cart`          | Returns the current cart state as JSON            |
| POST   | `/api/cart/modify`   | Increases or decreases an item's quantity. Body: `{"item": str, "action": "increase"|"decrease", "amount": int}` |
| POST   | `/api/cart/remove`   | Removes an item from the cart entirely. Body: `{"item": str}` |
| POST   | `/api/checkout`      | Runs checkout and returns the total charged       |

## What I Learned

- Structuring a Flask app with modular route logic split across separate files
- Building a JSON-based REST API (GET/POST) consumed by a JS frontend
- Managing state (cart contents) persisted between requests via file storage
- Connecting frontend fetch calls to backend routes for a full add-to-cart → checkout flow

## Future Improvements

- [ ] Replace JSON file storage with a proper database
- [ ] Add input validation (e.g. reject unknown items, negative quantities)
- [ ] Add order history / persistence across checkouts
- [ ] Add basic user authentication

## License

MIT