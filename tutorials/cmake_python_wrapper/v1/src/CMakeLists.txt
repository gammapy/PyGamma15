project (foo)
cmake_minimum_required(VERSION 3.4)
add_library(foo SHARED  foo.c)
install(TARGETS foo DESTINATION lib) 
