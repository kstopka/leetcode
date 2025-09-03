// https://leetcode.com/problems/to-be-or-not-to-be/description/

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
  return {
    toBe: (toBeVal) => {
      if (toBeVal === val) return true;
      throw Error("Not Equal");
    },
    notToBe: (notToBeVal) => {
      if (notToBeVal !== val) return true;
      throw Error("Equal");
    },
  };
};

// expect(5); // true
expect(5).toBe(5); // true
expect(5).notToBe(5); // throws "Equal"
