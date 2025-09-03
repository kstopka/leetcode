// https://leetcode.com/problems/create-hello-world-function/
// Easy
/**
 * @return {Function}
 */
var createHelloWorld = function () {
  return function (...args) {
    console.log("args", args);
    return "Hello World";
  };
};

const f = createHelloWorld();
console.log(f());
console.log(f([]));
console.log(f([{}, null, 42]));
