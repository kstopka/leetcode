/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
  if (Array.isArray(obj)) {
    return !obj.length;
  }
  return !Object.keys(obj).length;

  // if (Array.isArray(obj)) {
  //   return obj.length === 0;
  // } else {
  //   return Object.keys(obj).length === 0;
  // }
};

console.log(isEmpty([1]));
console.log(isEmpty([]));
console.log(isEmpty({}));
console.log(isEmpty({ val: "asd" }));
