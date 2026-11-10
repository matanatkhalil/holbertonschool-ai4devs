const assert = require("assert");
const { getShippingCost } = require("./bug2_fixed.js");
const { sortScores } = require("./bug5_fixed.js");

assert.strictEqual(getShippingCost(33), 8);
assert.strictEqual(getShippingCost(0), 8);
assert.strictEqual(getShippingCost(50), 0);
assert.strictEqual(getShippingCost(60), 0);
assert.deepStrictEqual(sortScores([9, 80, 100, 25]), [9, 25, 80, 100]);
console.log("All JS assertions passed");
