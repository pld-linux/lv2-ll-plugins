%define		_name	ll-plugins
#
Summary:	A set of LV2 audio plugins
Summary(pl.UTF-8):	Zestaw wtyczek dźwiękowych LV2
Name:		lv2-%{_name}
Version:	0.2.1
Release:	1
License:	GPL v3
Group:		Applications/Sound
Source0:	http://download.savannah.nongnu.org/releases/%{_name}/%{_name}-%{version}.tar.bz2
# Source0-md5:	d41d8cd98f00b204e9800998ecf8427e
Patch0:		%{name}-include.patch
Patch1:		%{name}-elven-lib.patch
URL:		http://ll-plugins.nongnu.org
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-devel
BuildRequires:	cairomm-devel >= 1.2.4
BuildRequires:	gtkmm-devel >= 2.8.8
BuildRequires:	jack-audio-connection-kit-devel >= 0.109.0
BuildRequires:	lash-devel >= 0.5.1
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.16
BuildRequires:	lv2-c++-tools-static >= 1.0.0
BuildRequires:	pkgconfig
Requires:	lv2core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LV2 audio plugins (see http://ll-plugins.nongnu.org for more
details).

%description -l pl.UTF-8
Zestaw wtyczek dźwiękowych LV2 (więcej informacji pod adresem
http://ll-plugins.nongnu.org).

%package -n elven
Summary:	Experimental LV2 Execution ENvironment
Summary(pl.UTF-8):	Eksperymentale środowisko urochomieniowe LV2
Group:		Applications/Sound

%description -n elven
Elven is Experimental LV2 Execution ENvironment.

%description -n elven -l pl.UTF-8
Elven jest eksperymentalnym środowiskiem urochomieniowym LV2 (Experimental LV2 Execution ENvironment).

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p0
%ifarch %{x8664}
%patch1 -p0
%endif

%{__sed} -e 's:ar rcs $$@ $$^ $(LDFLAGS) $$($(2)_LDFLAGS):ar rcs	$$@ $$^:' \
	-i Makefile.template

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--CXX="%{__cxx}" \
	--CFLAGS="%{rpmcppflags} %{rpmcxxflags}" \
	--LDFLAGS="%{rpmcxxflags} %{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lv2/*

%files -n elven
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elven
