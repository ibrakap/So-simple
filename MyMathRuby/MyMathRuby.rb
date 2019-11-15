def isnegative(number)
  if number > 0
    return false
  else
    return true
  end
end

def ispositive(number)
  if number > 0
    return true
  else
    return false
  end
end

def square_of_number(number)
  return number * number
end

def to_abs(number)
  if number > 0
    return number
  else
    return number * -1
  end
end

def perimeter_of_square(number)
  return number * 4
end

def area_of_square(number)
  return number * number
end

def factorial(number)
  result = 1
  for i in 1..number
    result *= i
  end
  return result
end

def permutation(n,r)
  return factorial(n) / factorial(n - r)
end

def combination(n,r)
  return factorial(n) / (factorial(n - r) * factorial(r))
end

