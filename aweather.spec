Name:		aweather
Summary:	Real-time weather data viewer
Version:	0.7
Release:	2
License:	GPLv3+
Group:		Sciences/Geosciences
URL:		http://lug.rose-hulman.edu/proj/aweather/
Source0:	http://lug.rose-hulman.edu/proj/aweather/files/%{name}-%{version}.tar.gz
Patch0:		aweather-0.6.3-mdv-includepath.patch
Patch1:		aweather-0.6.3-mdv-gthread.patch
Patch2:		aweather-0.6.1-mdv-desktop.patch
BuildRequires:	grits-devel >= %{version}
BuildRequires:	rsl-devel >= 1.42
BuildRequires:  glib2-devel
BuildRequires:  bzip2-devel

%description
AWeather is a free/open source application which has been designed to integrate
and visualize high-quality meteorological data using an interactive Virtual
Globe interface suitable for a wide range of users including weather
enthusiasts, academics, and professionals. It is designed to provide more
information than is typically available from weather widgets and simple desktop
applications. At the same time, it strives to be simpler and easier to use
than existing meteorological software packages such as GEMPAK and IDV.
Currently AWeather only displays data provided by the United States National
Weather Service.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

autoreconf

%build
%setup_compile_flags
%configure
%make

%install
%makeinstall_std

# Remove *.la files
rm -f %{buildroot}%{_libdir}/aweather/*.la

%files
%doc ChangeLog COPYING README TODO
%{_bindir}/aweather
%{_bindir}/wsr88ddec
%{_libdir}/aweather/*.so
%{_datadir}/applications/aweather.desktop
%{_datadir}/aweather
%{_iconsdir}/hicolor/*/apps/aweather.*
%{_mandir}/man1/*.1*


%changelog
* Fri Feb 17 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.7-1
+ Revision: 776179
- update to 0.7

* Wed Jan 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.6.3-1
+ Revision: 760193
- new version 0.6.3
- Remove *.la files, required for backporting

* Thu Dec 22 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.6.1-1
+ Revision: 744369
- BR bzip2-devel
- imported package aweather

