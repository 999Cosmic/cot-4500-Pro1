def approximation_algorithm():
  x0 = 1.5
  tol = 0.000001
  iter_count = 0
  diff = x0
  x = x0
  iterations = [(iter_count, x)]

  while diff >= tol:
      iter_count += 1
      y = x
      x = (x / 2) + (1 / x)
      iterations.append((iter_count, x))
      diff = abs(x - y)

  return iterations, iter_count

def f(x):
  return x**3 + 4*x**2 - 10

def f_prime(x):
  return 3*x**2 + 8*x

def bisection_method():
  tol = 0.0001
  left = -4
  right = 7
  max_iter = 100
  i = 0
  iterations = []

  while abs(right - left) > tol and i < max_iter:
      i += 1
      p = (left + right) / 2
      iterations.append((i, p))

      if f(p) == 0:
          break
      if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
          right = p
      else:
          left = p

  return iterations, p, i

def fixed_point_iteration():
  p0 = 1.5
  tol = 0.000001
  N0 = 50
  i = 1
  iterations = []

  while i <= N0:
      p = (10 - p0**3)**0.5 / 2

      if p != p:  
          return iterations, "Failure", i

      iterations.append((i, p))

      if abs(p - p0) < tol:
          return iterations, "Success", i

      i += 1
      p0 = p

  return iterations, "Failure", i

def newton_raphson_method():
  pprev = 1
  tol = 0.0001
  N0 = 50
  i = 1
  iterations = []

  while i <= N0:
      if f_prime(pprev) != 0:
          pnext = pprev - f(pprev) / f_prime(pprev)
          iterations.append((i, pnext))

          if abs(pnext - pprev) < tol:
              return iterations, pnext, i

          i += 1
          pprev = pnext
      else:
          return iterations, None, i  

  return iterations, None, i  