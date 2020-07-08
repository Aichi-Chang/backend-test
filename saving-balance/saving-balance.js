


function balance(openS, interestR, taxFree, taxR, numMonths) {

    const iRate = interestR / 100
    const tRate = taxR / 100

    openS = openS + (openS * iRate) 

    openS <= taxFree ? openS+=0 : openS -= (openS - taxFree) * tRate

    if (numMonths === 1) {
      return openS
    } else {
      return balance(openS, interestR, taxFree, taxR, numMonths - 1)
    }


}



console.log(balance(10000, 1, 20000, 1, 2))
console.log(balance(25000, 2, 20000, 1, 2))
console.log(balance(19800, 2, 20000, 1, 2))



