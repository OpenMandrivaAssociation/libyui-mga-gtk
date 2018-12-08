%define major 8
%define libname %mklibname yui %{major}-mga-gtk
%define develname %mklibname yui-mga-gtk -d

Summary:	UI abstraction library - Mageia extension Gtk plugin
Name:		libyui-mga-gtk
Version:	1.0.3
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/manatools/libyui-mga-gtk
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libyui)
BuildRequires:	%{_lib}yui-gtk-devel
BuildRequires:	%{_lib}yui-mga-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	texlive
BuildRequires:	ghostscript
BuildRequires:	graphviz
Requires:	libyui
Requires:	libyui-mga
Requires:	libyui-gtk

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-mga-gtk = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-mga-gtk.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/Other
Requires:	libyui-devel
Requires:	%{libname} = %{EVRD}
Provides:	yui-mga-gtk-devel = %{EVRD}

%description -n %{develname}
This package provides headers files for libyui-mga-gtk development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/pkgconfig/libyui-mga-gtk.pc
%{_libdir}/cmake/libyui-mga-gtk
%doc %{_docdir}/libyui-mga-gtk%{major}

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir}  \
    -DLIB_DIR=%{_lib}     \
    -DINSTALL_DOCS=yes    \
    -DENABLE_WERROR=0     \
    -DINSTALL_DOCS=yes    \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -G Ninja

%ninja_build
%ninja_build docs

%install
%ninja_install -C build

find "%{buildroot}" -name "*.la" -delete
