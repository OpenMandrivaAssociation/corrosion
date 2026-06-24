# No code, but we still can't be noarch because
# of lib vs. lib64
%undefine _debugsource_packages

Name:		corrosion
Version:	0.6.1
Release:	1
Source0:	https://github.com/corrosion-rs/corrosion/archive/refs/tags/v%{version}.tar.gz
Summary:	Marrying Rust and CMake - Easy Rust and C/C++ Integration
URL:		https://github.com/corrosion-rs/corrosion
License:	MIT
Group:		Development/Tools
BuildRequires:	cmake
BuildSystem:	cmake
Requires:	cmake
Requires:	rust
Requires:	cargo

%description
Marrying Rust and CMake - Easy Rust and C/C++ Integration

%files
%{_libdir}/cmake/Corrosion
%{_datadir}/cmake/*
