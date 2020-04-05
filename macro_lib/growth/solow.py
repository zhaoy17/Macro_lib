'''
Simulating Solow-Swan model, which attempts to model the long-run economic growth
by looking at capital accumulation (K), population growth (L) and technological 
progress, which results in increase in productivity. It models the total production
of the economy using the constant-returns-to-scale Cobb-Douglas production function

    Y(t) = K(t)^{alpha} * (A(t)L(t))^{1-alpha}, where
    
    Y(t): a single good output at time t
    K(t): the amount of capital at time t
    L(t): population at time t
    A(t): total factor productivity at time t
    alpha: output elasticity of capital

with a law of motion:
    I(t) = sY(t)
    C(t) = (1-s)Y(t)
    K(t+1) = (1-delta)K(t) + I(t)
    N(t+1) = (1+n)N(t)

where, I(t): total investment at time t
       C(t): total consumption at time t
       K(t): total capital at time t
       N(t): total population at time t
          s: the saving rate
      delta: rate of capital depreciation
          n: rate of population growth

This simulation allows user to take controls of those parameters and plot the simulated
total output growth. The program also enables user to query data from the Federal Reserve
Economic Data
'''

class solow:
    '''
    A: total factor productivity
    k0: the initial amount of capital
    delta: rate of depreciation of cpiatal
    s: the saving rate
    n: the population growth rate
    alpha: output elasticity of capital
    starting_year: 
    '''
    def solow(self, A=2.87, k0=3.5, delta = 0.08, s = 0.1, n = 0.015, alpha = 0.36, t0 = 1956, tmax = 2060):
        self.A = A
        self.k0 = k0
        self.delta = delta
        self.s = s
        self.n = n
        self.alpha = alpha
        self.t0 = t0
        self.tmax = tmax
        self.Y = []
        self.t = range(t0, tmax + 1)
