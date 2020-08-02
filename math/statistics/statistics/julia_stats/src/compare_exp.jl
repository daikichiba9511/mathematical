# watanabe bayes p61~62 o_p(exp(-n^{1/2})) 
# compare convergence of func. of exponential
# regarding -x and - sqrt(x)

using PyPlot



function plot_exp()
    end_N = 20.1
    ϵ = 0.2
    y = range(0.1, end_N, length=200)
    # println(y)
    f(x) = exp(-x)
    g(x) = exp(-sqrt(x))
    fig = figure()
    plot(y, f.(y), ".", label="exp(-n)")
    plot(y, g.(y), ".", label="exp(-sqrt(n))")
    # plot([0,end_N], [ϵ, ϵ])
    title("compare exp(-x) with exp(-sqrt(x))")
    xlabel("sample size")
    ylabel("the value of exponential")
    xlim(-1, 20)
    legend()
    grid()
    matplotlib.pyplot.savefig("images/compare_exponential.png")
    display(gcf())
    matplotlib.pyplot.close()
end

plot_exp()
