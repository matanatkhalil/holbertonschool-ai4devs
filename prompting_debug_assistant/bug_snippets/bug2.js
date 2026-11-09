// Bug 2: Logical error
function getShippingCost(orderTotal, isMember) {
  const standardShipping = 8;
  const freeShippingThreshold = 50;

  if (orderTotal >= freeShippingThreshold || isMember) {
    return 0;
  }

  return standardShipping;
}

function calculateOrderTotal(items, isMember) {
  const subtotal = items.reduce((sum, item) => {
    return sum + item.price * item.quantity;
  }, 0);

  const shipping = getShippingCost(subtotal, isMember);
  return subtotal + shipping;
}

const cart = [
  { name: "Notebook", price: 12, quantity: 2 },
  { name: "Pen set", price: 9, quantity: 1 }
];

console.log(calculateOrderTotal(cart, false));
