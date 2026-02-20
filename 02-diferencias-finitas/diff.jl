import Statistics: mean, var

function main()
  f(x)  = exp(x)
  df(x) = exp(x)

  x = 0:0.001:10
  fx = f.(x)
  h = step(x)

  df_approx = diff(fx) ./ h
  df_truth_full = df.(x)
  df_truth = df.(x)[2:length(df_truth_full)]
  err = abs.(df_approx - df_truth)
  # println("df(x)")
  # println(df_truth)
  # println("f(x)")
  # println(df_approx)
  # println("err")
  # println(err)
  println("Error promedio")
  println(mean(err))
  println("Varianza del error")
  println(var(err))
end

main()
