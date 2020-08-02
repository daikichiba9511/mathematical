using PyPlot

y = range(0, 2pi, length=100)

plot(y, sin.(y), ".-")
plot(y, cos.(y), ".-")

title("sine wave")
xlabel("x")
ylabel("y")
grid()
tight_layout()
display(gcf())
close()