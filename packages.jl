using Pkg
Pkg.add("CSV")

using CSV
pkg = CSV.read("pkg_list.csv")

for x in pkg[1]
    Pkg.add(x)
end
