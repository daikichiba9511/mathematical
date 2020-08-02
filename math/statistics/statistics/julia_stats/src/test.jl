y = 100;

y >= 100 ? true : false

n = -1

# 短絡評価
# n >= 0 の時はエラーとしてプログラムを終了させたいとする
# a && b は a と b がどちらも真の場合のみ真を返す。
# a を評価した結果が偽だったときに最終的な結果は必ず偽になるため b は評価されない
# a => b のときは a && b
n >= 0 && error("n must be negative")

# n が0より小さいときにエラーにしたい場合
# a || b はaとbのどちらも偽の場合のみ偽を返す
# n >= 0 || error("n must be positive")

#=
i = 1;
while i <= 5
    println(i)
    global i += 1
end

for i = 1:5
    println(i)
end

for i in 1:5
    println(i)
end

=#

#=
# 例外処理
try
    i = parse(Int,str)
catch
    # 例外処理
end
=#

function f(x...)
    sum = 0
    for i = 1:length(x)
        println(x[i])
        sum += x[i]
    end
    sum
end

f(3, 4, 5)

square = x -> x * x

square(3)

square1 = x -> begin
    x * x + 1
end

square1(3)

array = [1, 2, 3, 4, 5]

map(x -> x * x, array)

filter(x -> x % 2 == 1, array)

struct Point
    x :: Int
    y :: Int
end

function distance(p::Point)
    sqrt(p.x^2 + p.y^2)
end

p = Point(2, 3)
distance(p)


mutable struct Point2{T}
    x::T
    y::T
end

p = Point2(3, 4)

# q = Point2(2.3, 4.5)

function distance2(p::Point2{T}) where T
    println(T)
    sqrt(p.x^2 + p.y^2)
end

distance2(p)