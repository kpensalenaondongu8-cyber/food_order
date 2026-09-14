// Shared across index.html (menu) and cart.html (cart page)
// Update these paths to match whatever you saved in static/images/
const fallbackImages = {
    "Garlic Bread": "/static/images/garlic-bread.jpg",
    "Stuffed Mushrooms": "/static/images/mushrooms.jpg",
    "Classic Cheeseburger": "/static/images/cheeseburger.jpg",
    "Grilled Salmon": "/static/images/salmon.jpg",
    "Margherita Pizza": "/static/images/pizza.jpg",
    "Iced Coffee": "/static/images/iced-coffee.jpg",
    "Fresh Lemonade": "/static/images/lemonade.jpg",
    "Hennessey": "/static/images/whiskey.jpg",
    "Mashed Potatoes": "/static/images/potatoes.jpg",
    "Grilled Turkey": "/static/images/turkey.jpg",
    "Sharwama": "/static/images/sharwama.jpg",
};

function getDishImage(name) {
    return fallbackImages[name] || "/static/images/placeholder.jpg";
}