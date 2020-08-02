function solve_ode(f, t₀::Float64, y₀::Float6, n, h)
    t, y = float(t₀) , float(y₀)
    for _ in 1:n
        k₁ = f(t, y)
        k₂ = f(t + h / 2, y + k₁ / 2 * h)
        k₃ = f(t + h / 2, y + k₂ / 2 * h)
        k₄ = f(t + h , y + k₃ * h)
        t += h
        y += h * (k₁ + 2k₂ + 2k₃ + k₄) / 6
    end
    return t, y
end