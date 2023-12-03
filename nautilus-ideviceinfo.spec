# TODO
# - add mate (caja) package: https://bitbucket.org/ubuntu-mate/caja-ideviceinfo (separate .spec)
Summary:	Nautilus Property Page for iPhone/iPod Touch/iPad devices
Summary(pl.UTF-8):	Strona właściwości Nautilusa dla urządzeń iPhone/iPod Touch/iPad
Name:		nautilus-ideviceinfo
Version:	0.1.0
Release:	12
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://gitlab.gnome.org/GNOME/nautilus-ideviceinfo/-/tags
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	cf31bc0ffec70b33c87483f379bbdcf5
Patch0:		%{name}-gtk3.patch
Patch1:		%{name}-mobile-broadband-db-path.patch
Patch2:		%{name}-plist.patch
URL:		https://git.gnome.org/browse/nautilus-ideviceinfo
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool
BuildRequires:	libgpod-devel >= 0.7.90
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libplist-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.30
BuildRequires:	mobile-broadband-provider-info-devel >= 20100510-2
BuildRequires:	nautilus3-devel >= 3.0.0
BuildRequires:	pkgconfig
Requires:	libgpod >= 0.7.90
Requires:	mobile-broadband-provider-info
Requires:	nautilus3 >= 3.0.0
Requires:	usbmuxd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-iDeviceInfo is a Nautilus extension showing extended device
information in the Nautilus properties dialog. It shows details like
serial number, software version, baseband/modem firmware version, and
storage usage (with nice eye candy).

%description -l pl.UTF-8
Nautilus-iDeviceInfo to rozszerzenie Nautilusa pokazujące rozszerzone
informacje o urządzeniu w oknie właściwości Nautilusa. Pokazuje
szczegóły, takie jak numer seryjny, wersję oprogramowania, wersję
firmware'u urządzenia/modemu oraz wykorzystanie miejsca na karcie (z
ładnym widokiem).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-ideviceinfo.so
%{_libdir}/nautilus/extensions-3.0/nautilus-ideviceinfo.ui
