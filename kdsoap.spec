%define		qtver		5.9.0
%define		kfname	kdsoap

Summary:	Qt-based client-side and server-side SOAP component
Name:		kdsoap
Version:	2.0.0
Release:	2
License:	LGPL v2.1, LGPL v3.0, GPL v2.0, GPL v3.0, commercial
Group:		X11/Libraries
Source0:	https://github.com/KDAB/KDSoap/releases/download/%{name}-%{version}/kdsoap-%{version}.tar.gz
# Source0-md5:	511bf80dac042430edaabc46a658f101
URL:		https://www.kdab.com/development-resources/qt-tools/kd-soap/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.5
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KD Soap is a Qt-based client-side and server-side SOAP component.

%description -l pl.UTF-8
KD Soap jest opartym na Qt komponentem SOAP do programów po stronie
klienta jak i serwera.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.5
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-kcoreaddons-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSES README-commercial.txt README.txt kdsoap.pri kdwsdl2cpp.pri
%attr(755,root,root) %{_bindir}/kdwsdl2cpp
%ghost %{_libdir}/libkdsoap-server.so.2
%attr(755,root,root) %{_libdir}/libkdsoap-server.so.2.*.*
%ghost %{_libdir}/libkdsoap.so.2
%attr(755,root,root) %{_libdir}/libkdsoap.so.2.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDSoapClient
%{_includedir}/KDSoapServer
%{_libdir}/cmake/KDSoap
%{_libdir}/libkdsoap-server.so
%{_libdir}/libkdsoap.so
%dir %{_libdir}/qt5/mkspecs
%dir %{_libdir}/qt5/mkspecs/modules
%{_libdir}/qt5/mkspecs/modules/qt_KDSoapClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSoapServer.pri
%{_datadir}/mkspecs/features/kdsoap.prf
