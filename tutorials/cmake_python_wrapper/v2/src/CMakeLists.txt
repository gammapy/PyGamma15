project (foo)
cmake_minimum_required(VERSION 2.8)
add_library(foo SHARED  foo.c)
install(TARGETS foo DESTINATION lib) 
