project (foo)
cmake_minimum_required(VERSION 3.0)
add_library(foo SHARED  foo.c)
install(TARGETS foo DESTINATION lib) 
