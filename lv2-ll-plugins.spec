%define		_name	ll-plugins
#
Summary:	LL - a set of LV2 audio plugins
Summary(pl.UTF-8):	LL - zestaw wtyczek dźwiękowych LV2
Name:		lv2-%{_name}
Version:	0.2.8
Release:	1
License:	GPL v3+
Group:		Applications/Sound
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{_name}-%{version}.tar.bz2
# Source0-md5:	56e7f4a62fce6b22b4acdb02ba06669c
Patch0:		%{name}-include.patch
Patch1:		%{name}-elven-lib.patch
URL:		http://ll-plugins.nongnu.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	bash >= 3.0
BuildRequires:	boost-devel
BuildRequires:	cairomm-devel >= 1.2.4
BuildRequires:	gtkmm-devel >= 2.8.8
BuildRequires:	jack-audio-connection-kit-devel >= 0.109.0
BuildRequires:	lash-devel >= 0.5.1
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.18
BuildRequires:	lv2-c++-tools-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	cairomm >= 1.2.4
Requires:	gtkmm >= 2.8.8
Requires:	libsamplerate >= 0.1.2
Requires:	libsndfile >= 1.0.18
Requires:	lv2core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LL is a set of LV2 audio plugins (see <http://ll-plugins.nongnu.org/>
for more details).

%description -l pl.UTF-8
LL to zestaw wtyczek dźwiękowych LV2 (więcej informacji pod adresem
<http://ll-plugins.nongnu.org/>).

%package -n elven
Summary:	Experimental LV2 Execution ENvironment
Summary(pl.UTF-8):	Eksperymentalne środowisko uruchomieniowe LV2
Group:		Applications/Sound
Requires:	cairomm >= 1.2.4
Requires:	gtkmm >= 2.8.8
Requires:	lash-libs >= 0.5.1
Requires:	lv2core

%description -n elven
Elven is Experimental LV2 Execution ENvironment.

%description -n elven -l pl.UTF-8
Elven jest eksperymentalnym środowiskiem uruchomieniowym LV2
(Experimental LV2 Execution ENvironment).

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p0
%ifarch %{x8664}
%patch1 -p0
%endif

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
%dir %{_libdir}/lv2/*.lv2
%{_libdir}/lv2/*.lv2/*.flac
%{_libdir}/lv2/*.lv2/*.png
%{_libdir}/lv2/*.lv2/*.svg
%{_libdir}/lv2/*.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/*.lv2/*.so

%files -n elven
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elven
