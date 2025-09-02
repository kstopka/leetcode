// https://leetcode.com/problems/sort-by/

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  // return arr
  //   .map((el) => ({ val: fn(el), el }))
  //   .sort((a, b) => a.val - b.val)
  //   .map((el) => el.el);

  return arr.sort((a, b) => fn(a) - fn(b));
};
// const arr = [5, 4, 1, 2, 3];
// const fn = (x) => x;
// const arr = [{ x: 1 }, { x: 0 }, { x: -1 }];
// const fn = (x) => x.x;
const arr = [
  [3, 4],
  [5, 2],
  [10, 1],
];
const fn = (x) => x[1];
console.log(sortBy(arr, fn));
