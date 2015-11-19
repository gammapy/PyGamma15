cmake_minimum_required(VERSION 2.8)

find_program(PYTHON "python")

if (PYTHON)
    set(SETUP_PY_IN "${CMAKE_CURRENT_SOURCE_DIR}/setup.py.in")
    set(SETUP_PY    "${CMAKE_CURRENT_BINARY_DIR}/setup.py")
    set(DEPS        "${CMAKE_CURRENT_SOURCE_DIR}/foo/__init__.py")
    set(STAMP       "${CMAKE_CURRENT_BINARY_DIR}/build")

    configure_file(${SETUP_PY_IN} ${SETUP_PY})

    add_custom_command(OUTPUT ${STAMP}
                       COMMAND ${PYTHON} ${SETUP_PY} build )

    add_custom_target(target ALL DEPENDS ${STAMP})

    install(CODE "execute_process(COMMAND ${PYTHON} ${SETUP_PY} install)")
endif()