%define major 16
%define oldlibname %mklibname yui 15-mga-gtk
%define libname %mklibname yui-mga-gtk
%define develname %mklibname yui-mga-gtk -d

Summary:	UI abstraction library - Mageia extension Gtk plugin
Name:		libyui-mga-gtk
Version:	1.2.0
Release:	9
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/manatools/libyui-mga-gtk
Source0:	https://github.com/manatools/libyui-mga-gtk/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:     00-libyui-gtk-dep.patch

BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(libyui-gtk)
BuildRequires:	pkgconfig(libyui-mga)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	ghostscript
BuildRequires:	graphviz
Requires:	%{_lib}yui
Requires:	%{_lib}yui-mga
Requires:	%{_lib}yui-gtk

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Requires:	%{_lib}yui
Requires:	%{_lib}yui-mga
Requires:	%{_lib}yui-gtk
Provides:	%{name} = %{EVRD}
Provides:	libyui-mga-gtk = %{EVRD}
%rename %{oldlibname}

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
#{_libdir}/pkgconfig/libyui-mga-gtk.pc
#{_libdir}/cmake/libyui-mga-gtk
#doc %{_docdir}/libyui-mga-gtk%{major}

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
    -G Ninja

%ninja_build

%install
%ninja_install -C build

find "%{buildroot}" -name "*.la" -delete
