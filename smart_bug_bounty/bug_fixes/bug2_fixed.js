function calculate_cart_total(cart) {
    let total = 0;

    for (let i = 0; i < cart.length; i++) {
        const item = cart[i];

        if (item.quantity > 0) {
            total += item.price * item.quantity;
        }
    }

    return total;
}

const cart = [
    { name: "Book", price: 15, quantity: 2 },
    { name: "Pen", price: 3, quantity: 5 },
    { name: "Bag", price: 30, quantity: 1 }
];

console.log("Total:", calculate_cart_total(cart));
