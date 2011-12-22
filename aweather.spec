%define _disable_ld_no_undefined 1

Name:		aweather
Summary:	Real-time weather data viewer
Version:	0.6.1
Release:	1
License:	GPLv3+
Group:		Sciences/Geosciences
URL:		http://lug.rose-hulman.edu/proj/aweather/
Source0:	http://lug.rose-hulman.edu/proj/aweather/files/%{name}-%{version}.tar.gz
Patch0:		aweather-0.6.1-mdv-includepath.patch
Patch1:		aweather-0.6.1-mdv-gthread.patch
Patch2:		aweather-0.6.1-mdv-desktop.patch
BuildRequires:	grits-devel >= 0.6
BuildRequires:	rsl-devel >= 1.41
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

%files
%{_bindir}/aweather
%{_bindir}/wsr88ddec
%{_libdir}/aweather/*.so
%{_datadir}/applications/aweather.desktop
%dir %{_datadir}/aweather
%dir %{_datadir}/aweather/colors
%{_datadir}/aweather/colors/*.clr
%{_datadir}/aweather/defaults.ini
%{_datadir}/aweather/fips.txt
%{_datadir}/aweather/logo.svg
%{_datadir}/aweather/main.ui
%{_defaultdocdir}/aweather/aweather.html
%{_iconsdir}/hicolor/*/apps/aweather.*
%{_mandir}/man1/*.1*
