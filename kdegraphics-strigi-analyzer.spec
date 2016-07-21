Name:		kdegraphics-strigi-analyzer
Summary:	Strigi plugins
Version:	16.04.3
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libstreams)
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
Strigi plugin for dvi & tiff.

%files
%doc COPYING COPYING.LIB
%{_kde_libdir}/strigi/strigiea_dvi.so
%{_kde_libdir}/strigi/strigiea_tiff.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
