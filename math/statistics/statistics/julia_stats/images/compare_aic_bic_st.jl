using PyPlot

function plot_aic_bic_st()
    n = range(0, 10, length=100)
    f(x) = 1 / x
    g(x) = (log(x) - 1) * (1 / x)
    h(x) = 5.66 / x

    plot(n, f.(n), ".-", label="aic")
    plot(n, g.(n), ".-", label="bic")
    plot(n, h.(n), ".-", label="statistical testing")

    title("compare")
    xlabel("sample size")
    legend()
    grid()
    matplotlib.pyplot.savefig("images/compare_aic_bic_st.png")
    display(gcf())
    matplotlib.pyplot.close()
end

plot_aic_bic_st()