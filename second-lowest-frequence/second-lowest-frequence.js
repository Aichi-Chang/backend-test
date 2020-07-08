
function secondLowest(arr) {

  if(arr === null || arr.length === 0) {
    return arr
  }

  const sorted = arr.sort((a, b) => a - b)


  let map = new Map()

  for (i=0; i<arr.length; i++) {
    map.has(arr[i]) ? map.set(arr[i], map.get(arr[i]) + 1) : map.set(arr[i], 1)
  }


  let value = [...map.entries()]
  let maxValue = value[0][1]

  for(j=0; j<value.length; j++) {
    
    if (value[j][1] > maxValue) {
      maxValue = value[j][1]
    }
  }

  let filter = [...map.entries()].filter(({1: val}) => val === maxValue)


  if (filter.length > 1) {
    return filter[1][0]
  } else {
    return filter[0][0]
  }
  
}




console.log(secondLowest([4, 3, 1, 1, 2]))
console.log(secondLowest([4, 3, 1, 1, 2, 2]))
console.log(secondLowest([4, 3, 1, 2]))