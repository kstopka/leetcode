// https://leetcode.com/problems/chunk-array/description/
// Easy
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  let start = 0;
  let end = size;
  const result = [];

  while (start < arr.length) {
    result.push(arr.slice(start, end));
    [start, end] = [end, end + size];
  }
  return result;
  // return arr.reduce((chunkedArray, element) => {
  //   const lastChunk = chunkedArray[chunkedArray.length - 1];
  //   if (!lastChunk || lastChunk.length === size) {
  //     chunkedArray.push([element]);
  //   } else {
  //     lastChunk.push(element);
  //   }
  //   return chunkedArray;
  // }, []);
};

console.log(chunk([1, 2, 3, 4, 5], 1));
console.log(chunk([1, 9, 6, 3, 2], 3));
console.log(chunk([8, 5, 3, 2, 6], 6));
console.log(chunk([], 1));
