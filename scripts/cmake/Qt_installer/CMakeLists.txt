# Project settings
cmake_minimum_required( VERSION 3.15 )

project( key-manager-dependencies-qt6
    VERSION 1.0
    DESCRIPTION "Build system for key-manager Qt6 dependency."
    LANGUAGES CXX
)

# Error if building out of a build directory
file( TO_CMAKE_PATH "${PROJECT_BINARY_DIR}/CMakeLists.txt" LOC_PATH )
if( EXISTS "${LOC_PATH}" )
    message( FATAL_ERROR "You cannot build in a source directory (or any directory with "
                         "CMakeLists.txt file). Please make a build subdirectory. Feel free to "
                         "remove CMakeCache.txt and CMakeFiles." )
endif()

# Fetch the package
find_package( Qt6 6.4.2 QUIET )
if( NOT Qt6_FOUND )

    # Create directories
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E make_directory build/_deps/qt6
        COMMAND ${CMAKE_COMMAND} -E make_directory build/_deps/qt6/qt6-build
    )

    # MacOS
    if( CMAKE_SYSTEM_NAME STREQUAL "Darwin" )

        # Install
        message( STATUS "Building on MacOS" )
        execute_process(
                COMMAND brew install qt6
                RESULT_VARIABLE result
        )

        # Print possible errors
        if( result )
            message( FATAL_ERROR "Failed to install Qt6" )
        endif()

    # Linux
    elseif( CMAKE_SYSTEM_NAME STREQUAL "Linux" )

        # Check the distro
        message( STATUS "Building on Linux" )
        execute_process(
                COMMAND lsb_release -si
                OUTPUT_VARIABLE distro
                OUTPUT_STRIP_TRAILING_WHITESPACE
        )

        # Ubuntu prerequisites
        if( distro STREQUAL "Ubuntu" )

            # Updating the system
            message( STATUS "Updating package list..." )
            execute_process( COMMAND sudo apt update )
            execute_process( COMMAND sudo apt upgrade )

            # Installing prerequisites
            message( STATUS "Installing necessary packages..." )
            execute_process( COMMAND sudo apt install libclang-13-dev llvm perl unzip git build-essential libfontconfig1-dev libfreetype6-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libx11-xcb-dev libxcb-glx0-dev libxcb-keysyms1-dev libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-sync0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev libxcb-render-util0-dev libxcb-xinerama0-dev libxcb-util0-dev libxcb-xinput-dev libxcb-xkb-dev libxkbcommon-x11-dev libwayland-dev libwayland-egl1 libgl-dev libglu-dev libegl1-mesa-dev libgles2-mesa-dev libudev-dev libinput-dev libicu-dev libsqlite3-dev libssl-dev libpng-dev libjpeg-dev libgif-dev libwebp-dev liblzma-dev libzstd-dev libdouble-conversion-dev libpcre2-dev libharfbuzz-dev libxslt1-dev libxml2-dev libbz2-dev libz3-dev ninja-build )
        endif()

        # Cloning the repository
        message( STATUS "Downloading Qt..." )
        execute_process(
            COMMAND git clone git://code.qt.io/qt/qt5.git
            WORKING_DIRECTORY build/_deps/qt6
        )

        # Initialize the repository
        message( STATUS "Initializing the repo..." )
        execute_process(
            COMMAND git checkout v6.4.2
            COMMAND perl init-repository
            WORKING_DIRECTORY build/_deps/qt6/qt5
        )

        # Configure Qt 
        message( STATUS "Configuring..." )
        execute_process(
            COMMAND ../qt5/configure -prefix . -opensource -confirm-license -nomake examples -nomake tests
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )

        # Compile Qt
        message( STATUS "Compiling..." )
        execute_process(
            COMMAND cmake --build . --target qtbase qtscxml --parallel
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )

        # Install Qt
        message( STATUS "Installing..." )
        execute_process(
            COMMAND cmake --install .
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )

    # Windows
    elseif( CMAKE_SYSTEM_NAME STREQUAL "Windows" )

        # Cloning the repository
        message( STATUS "Downloading Qt..." )
        execute_process(
            COMMAND cmd /c git.exe clone git://code.qt.io/qt/qt5.git
            WORKING_DIRECTORY build/_deps/qt6
        )

        # Initialize the repository
        message( STATUS "Initializing the repo..." )
        execute_process(
            COMMAND cmd /c git.exe checkout v6.4.2
            COMMAND cmd /c perl init-repository
            WORKING_DIRECTORY build/_deps/qt6/qt5
        )

        # Configure Qt 
        message( STATUS "Configuring..." )
        execute_process(
            COMMAND build/_deps/qt6/qt5/configure -prefix . -opensource -confirm-license -nomake examples -nomake tests
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )
        
        # Compile Qt
        message( STATUS "Compiling..." )
        execute_process(
            COMMAND cmake --build . --target qtbase qtscxml --parallel
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )

        # Install Qt
        message( STATUS "Installing..." )
        execute_process(
            COMMAND cmake --install .
            WORKING_DIRECTORY build/_deps/qt6/qt6-build
        )
    endif()

else()
    message( STATUS "Qt 6.4.2 found in the system." )
endif()