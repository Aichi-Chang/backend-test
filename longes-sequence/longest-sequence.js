

function longestS(str) {

  if (str === null || str === '') {
    return str
  }

  const lowerS = str.toLowerCase()
  let currentL = ''
  let sum = 1
  let highestSum = 0
  let highestL = ''


  for(i=0; i<lowerS.length; i++) {
    
    if(currentL === lowerS[i]) {
      sum += 1
    } else {
      currentL = lowerS[i]
      sum = 1
    }

    if (sum > highestSum) {
      highestSum = sum
      highestL = lowerS[i]
    }

  }

  return [highestL, highestSum]

}



console.log(longestS('dghhhmhmx'))
console.log(longestS('dhkkhhKKKt'))
console.log(longestS('aBbBadddadd'))